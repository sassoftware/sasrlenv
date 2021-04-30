# Copyright © 2020, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import grpc
import numpy as np

from sasrl_env.common.env_pb2 import Action, Empty, Name
from sasrl_env.common.env_pb2_grpc import EnvStub
from sasrl_env.utils import decode_space_message, serialize_data, deserialize_data


def decode_observation(observation_m, observation_space):
    if observation_m.data_i:
        observation = deserialize_data(observation_m.data_i, observation_space)
    elif observation_m.data_f:
        observation = deserialize_data(observation_m.data_f, observation_space)
    else:
        raise Exception("Client received no observation data.")


    return observation


def get_action_m(action):
    """
    Creates the action message
    @param action: action which can be a scalar, numpy array, list, or dict
    @return: action message
    """

    # convert action to 1d numpy array
    action = serialize_data(action)

    # create the action message
    if np.issubdtype(action.dtype, np.floating):
        action_m = Action(data_f=action)
    elif np.issubdtype(action.dtype, np.integer):
        action_m = Action(data_i=action)
    else:
        raise Exception('Action should be a numpy array of type int or float.')

    return action_m

class Env(object):

    def __init__(self, name, address):
        self.channel = grpc.insecure_channel(address)
        self.env = EnvStub(self.channel)
        self.make(name)

    def make(self, name):
        info = self.env.Make(Name(data=name))

        self.observation_space = decode_space_message(info.observation_space)
        self.action_space = decode_space_message(info.action_space)
        self._max_episode_steps = info.max_episode_steps

    def reset(self):
        return decode_observation(self.env.Reset(Empty()), self.observation_space)

    def step(self, action):
        action_m = get_action_m(action)
        transition = self.env.Step(action_m)
        next_observation = decode_observation(transition.next_observation, self.observation_space)
        return next_observation, transition.reward, transition.done

    def Sample(self):
        action = self.env.Sample(Empty())
        return action

    def Close(self):
        self.env.Close()

    def close(self):
        self.channel.close()


if __name__ == '__main__':
    import time

    host = '10.122.32.31'
    port = '10007'
    address = '{}:{}'.format(host, port)

    env_names = [
        'CartPole-v0', 'MountainCar-v0', 'MountainCarContinuous-v0', 'Pendulum-v0',
        'Acrobot-v1', 'LunarLander-v2', 'LunarLanderContinuous-v2', 'BipedalWalker-v3',
        'BipedalWalkerHardcore-v3', 'Blackjack-v0', 'KellyCoinflip-v0', 'KellyCoinflipGeneralized-v0',
        'FrozenLake-v0', 'FrozenLake8x8-v0', 'CliffWalking-v0', 'NChain-v0', 'Roulette-v0',
        'Taxi-v3', 'GuessingGame-v0', 'HotterColder-v0'
    ]

    for game in ['adventure',
                 # 'air_raid', 'alien', 'amidar', 'assault', 'asterix', 'asteroids', 'atlantis',
        #          'bank_heist', 'battle_zone', 'beam_rider', 'berzerk', 'bowling', 'boxing', 'breakout', 'carnival',
        #          'centipede', 'chopper_command', 'crazy_climber', 'demon_attack', 'double_dunk',
        #          'elevator_action', 'enduro', 'fishing_derby', 'freeway', 'frostbite', 'gopher', 'gravitar',
        #          'hero', 'ice_hockey', 'jamesbond', 'journey_escape', 'kangaroo', 'krull', 'kung_fu_master',
        #          'montezuma_revenge', 'ms_pacman', 'name_this_game', 'phoenix', 'pitfall', 'pong', 'pooyan',
        #          'private_eye', 'qbert', 'riverraid', 'road_runner', 'robotank', 'seaquest', 'skiing',
        #          'solaris', 'space_invaders', 'star_gunner', 'tennis', 'time_pilot', 'tutankham', 'up_n_down',
        #          'venture', 'video_pinball', 'wizard_of_wor', 'yars_revenge', 'zaxxon'
                 ]:
        for obs_type in ['image', 'ram']:
            name = ''.join([g.capitalize() for g in game.split('_')])
            if obs_type == 'ram':
                name = '{}-ram'.format(name)
            env_names.append('{}-v0'.format(name))

    # env_names_with_error = ['CarRacing-v0' #rendering error]
    # env_names = env_names[-1:]
    # env_names = env_names[12:13]
    for env_name in env_names:
        print(env_name)
        env = Env(env_name, address)

        st = time.time()
        cnt = 0
        for i in range(1):
            s = env.reset()
            cnt += 1
            j = 0
            done = False
            while not done:
                if env_name == 'LunarLanderContinuous-v2':
                    action = [1, 1]
                elif env_name == 'BipedalWalker-v3' or env_name == 'BipedalWalkerHardcore-v3':
                    action = [1, 1, 1, 1]
                else:
                    action = 1
                ns, r, done = env.step(action)
                cnt += 1
                j += 1
                s = ns
                # report
                if cnt % 100 == 0:
                    print("cnt: {} -- rate: {}".format(cnt, cnt / (time.time() - st)))
                if j>200:
                    break
            if cnt>1000:
                break
        env.close()
