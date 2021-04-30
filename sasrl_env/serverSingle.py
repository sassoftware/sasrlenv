# Copyright © 2020, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import gym
import grpc
import numpy as np
from concurrent import futures
import argparse
from sasrl_env.common.env_pb2 import Info, Observation, Transition, Action, Empty, RenderOut, MetaData
from sasrl_env.common.env_pb2_grpc import EnvServicer as Service, \
    add_EnvServicer_to_server as register
from sasrl_env.utils import get_ip, get_space_message, serialize_data, deserialize_data
from sasrl_env.common.utils import get_logger

logger = get_logger(log_level='debug')


def get_observation_m(observation):
    """
    Creates the observation message
    @param observation: observation which can be a scalar, numpy array, list, or dict
    @return: observation message
    """

    # serialize observations in a 1d numpy array
    observation = serialize_data(observation)

    # create the observation message
    if np.issubdtype(observation.dtype, np.floating):
        observation_m = Observation(data_f=observation)
    elif np.issubdtype(observation.dtype, np.integer):
        observation_m = Observation(data_i=observation)
    else:
        raise Exception('Observation should have a type int or float.')

    return observation_m


def decode_action(action_m, action_space):
    if action_m.data_i:
        action = deserialize_data(action_m.data_i, action_space)
    elif action_m.data_f:
        action = deserialize_data(action_m.data_f, action_space)

    return action


class Env(Service):

    def __init__(self, port):
        self.port = port
        super(Env, self).__init__()

    def Handshake(self, empty, _):
        """
        Sets the metadata for environment server. This meta data includes the version of sasrl_env package and
        it will be used to check for consistency of tkrl and sasrl_env.
        @param empty:
        @return: the metadata message which includes the version number
        """
        # set the version manually
        version = "1.0.0"
        return MetaData(EnvVersion=version)

    def Make(self, name_m, _):
        """
        This function creates an environment instance on remote environment server.
        @param name_m: name of the environment
        @return: information message which includes observation_space, action_space and episode
                length of the environment
        """
        name = name_m.data
        if not hasattr(self, 'env') or self.env.spec.id != name:
            self.env = gym.make(name)
        logger.info('Env {} created at port {}'.format(name, str(self.port)))

        # check validity of observation_space
        try:
            self.env.observation_space
        except AttributeError:
            raise AttributeError(
                'Environment should have an observation_space object. Use either Box, Discrete, Tuple or Dict space '
                'types to define the observation space.')
        observation_space_m = get_space_message(self.env.observation_space)

        # check validity of action_space
        try:
            self.env.action_space
        except AttributeError:
            raise AttributeError('Environment should have an action_space object. Use either Box, '
                                 'Discrete, Tuple or Dict space types to define the action space.')
        action_space_m = get_space_message(self.env.action_space)

        try:
            _max_episode_steps = self.env._max_episode_steps
        except AttributeError:
            _max_episode_steps = None

        return Info(observation_space=observation_space_m,
                    action_space=action_space_m,
                    max_episode_steps=_max_episode_steps)

    def Reset(self, empty_m, _):
        """
        This function resets the environment and returns the encoded observation message.
        @param empty_m: empty message
        @return: 1 dimensional encoded observation
        """
        return get_observation_m(self.env.reset())

    def Step(self, action_m, _):
        """
        This functions runs a step in the environment according to the received action message.
        @param action_m: the action message
        @return: the transition message which includes next observations, reward and terminal signal
        """
        action = decode_action(action_m, self.env.action_space)
        try:
            next_observation, reward, done, _ = self.env.step(action)
        except TypeError:
            next_observation, reward, done, _ = self.env.step(action.tolist())

        next_observation = get_observation_m(next_observation)
        return Transition(next_observation=next_observation,
                          reward=reward,
                          done=done)

    def Render(self, rendermode_m, _):
        """
        Renders the environment if the .render() function of environment is implemented.
        @param rendermode_m: the type of render. It can be 'rgb_array', ansi', or 'human'
        @return: render message
        """
        res = self.env.render(rendermode_m.data)

        mode = rendermode_m.data
        if mode == 'rgb_array':
            reno = RenderOut(rgb_array=res.flatten())
        elif mode == 'ansi':
            reno = RenderOut(ansi=res)
        elif mode == 'human':
            reno = RenderOut()
        else:
            raise Exception("render mode {} not supported.".format(mode))

        return reno

    def Sample(self, empty_m, _):
        """
        Samples an action from environment.
        @param empty_m:
        @return: the action message sampled from environment
        """
        action = self.env.action_space.sample()
        if np.issubdtype(action, np.floating):
            action_m = Action(data_f=action.ravel())
        elif np.issubdtype(action, np.integer):
            action_m = Action(data_i=action.ravel())
        else:
            raise Exception("Sampling was unsuccessful due to unsupported data type.")

        return action_m

    def Close(self, empty_m, _):
        """
        Closes the environment
        @param empty_m: empty message
        @return: empty message
        """
        self.env.close()
        return Empty()

    def Seed(self, env_seed_m, _):
        """
        Sets seed of the environment.
        @param env_seed_m: the seed message
        @return: empty message
        """
        if hasattr(self.env, 'seed'):
            self.env.seed(env_seed_m.data)
        else:
            logger.warning("There is no function to set seed in the environment.")
        return Empty()


class register_server(object):
    """
    This class is responsible for assigning the environment server to specified port.
    """

    def start(self, port):
        host = get_ip()
        address = '{}:{}'.format(host, port)
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        register(Env(port), server)
        server.add_insecure_port(address)
        server.start()
        logger.info("Started server at: {}".format(address))
        server.wait_for_termination()
        return 0


def start(port):
    """
    Starts an environment server on the assigned port
    @param port:
    @return: status
    """
    rs = register_server()
    rs.start(port)
    return 0


if __name__ == '__main__':
    # this python file can be executed directly or via the environment controller
    parser = argparse.ArgumentParser('environment server')
    parser.add_argument('--port', type=int, default=10007,
                        help='the port number which hosts a single environment server.')
    args = parser.parse_args()

    # start a single environment server
    start(args.port)
