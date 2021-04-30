# Copyright © 2020, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0


import numbers
import socket
from contextlib import closing
import gym
import numpy as np

from sasrl_env.common.env_pb2 import Space


def get_ip():
    """
    Get ip address of the machine which runs the python code
    @return: ip address
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


def check_free_port(ip, port):
    """
    Check if a requested port is idle
    @param ip: ip address of the host
    @param port: the port number to check its availability
    @return: a boolean determining if the port is idle of not
    """
    #

    # Create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        return False
    except socket.error:
        return True
    finally:
        s.close()


def find_free_port():
    """
    Automatically assigns an idle port
    @return: the port number
    """
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def get_space_type(space):
    try:
        if space.__class__ == gym.spaces.Box:
            space_type = 'box'
        elif space.__class__ == gym.spaces.Discrete:
            space_type = 'discrete'
        elif space.__class__ == gym.spaces.Dict:
            space_type = 'dict'
        elif space.__class__ == gym.spaces.Tuple:
            space_type = 'tuple'
    except:
        raise Exception('The space type {} is not supported. Choose from Box, Discrete, Dict, or Tuple '
                        'space types.'.format(str(space.__class__)))

    return space_type


def get_space_message(space):
    type = get_space_type(space)
    dtype = space.dtype

    if type == 'box':
        if np.issubdtype(dtype, np.floating):
            space_m = [Space(type=type,
                             shape=space.shape,
                             dtype='float',
                             low_f=list(space.low.flatten()),
                             high_f=list(space.high.flatten()))]
        elif np.issubdtype(dtype, np.integer):
            space_m = [Space(type=type,
                             shape=space.shape,
                             dtype='int',
                             low_i=list(space.low.flatten()),
                             high_i=list(space.high.flatten()))]
        else:
            raise Exception("Only float and int data types are supported for the Box space.")

    elif type == 'discrete':
        if np.issubdtype(dtype, np.integer):
            space_m = [Space(type=type,
                             dtype='int',
                             n=[space.n])]
        else:
            raise Exception("Only int data type is supported for space of type Discrete.")

    elif type == 'dict':
        space_m = []
        for k, s in space.spaces.items():
            sub_type = get_space_type(s)
            sub_dtype = s.dtype

            if sub_type == 'box':
                if np.issubdtype(sub_dtype, np.floating):
                    space_m.append(Space(type=sub_type,
                                         shape=s.shape,
                                         dtype='float',
                                         key=k,
                                         low_f=list(s.low.flatten()),
                                         high_f=list(s.high.flatten())))
                elif np.issubdtype(sub_dtype, np.integer):
                    space_m.append(Space(type=sub_type,
                                         shape=s.shape,
                                         key=k,
                                         dtype='int',
                                         low_i=list(s.low.flatten()),
                                         high_i=list(s.high.flatten())))
                else:
                    raise Exception("Only float and int data types are supported for the Box space.")

            elif sub_type == 'discrete':
                if np.issubdtype(sub_dtype, np.integer):
                    space_m.append(Space(type=sub_type,
                                         key=k,
                                         dtype='int',
                                         n=[s.n]))
                else:
                    raise Exception("Only int data type is supported for space of type Discrete.")

            else:
                raise Exception("The Dict space can have subspaces of type Box or Discrete.")

    elif type == 'tuple':
        space_m = []
        for s in space.spaces:
            sub_type = get_space_type(s)
            sub_dtype = s.dtype

            if sub_type == 'box':
                if np.issubdtype(sub_dtype, np.floating):
                    space_m.append(Space(type=sub_type,
                                         shape=s.shape,
                                         dtype='float',
                                         low_f=list(s.low.flatten()),
                                         high_f=list(s.high.flatten())))
                elif np.issubdtype(sub_dtype, np.integer):
                    space_m.append(Space(type=sub_type,
                                         shape=s.shape,
                                         dtype='int',
                                         low_i=list(s.low.flatten()),
                                         high_i=list(s.high.flatten())))
                else:
                    raise Exception("Only float and int data types are supported for the Box space.")

            elif sub_type == 'discrete':
                if np.issubdtype(sub_dtype, np.integer):
                    space_m.append(Space(type=sub_type,
                                         dtype='int',
                                         n=[s.n]))
                else:
                    raise Exception("Only int data type is supported for space of type Discrete.")

            else:
                raise Exception("The Tuple space can have subspaces of type Box or Discrete.")

    return space_m


def decode_space_message(sms):
    if sms[0].key is not '':
        # dict space
        space = {}
        for sm in sms:
            if sm.type == 'box':
                if sm.dtype == 'float':
                    space[sm.key] = gym.spaces.Box(np.array(sm.low_f).reshape(sm.shape),
                                                   np.array(sm.high_f).reshape(sm.shape),
                                                   np.array(sm.shape),
                                                   dtype=float)
                elif sm.dtype == 'int':
                    space[sm.key] = gym.spaces.Box(np.array(sm.low_i).reshape(sm.shape),
                                                   np.array(sm.high_i).reshape(sm.shape),
                                                   np.array(sm.shape),
                                                   dtype=int)

            elif sm.type == 'discrete':
                space[sm.key] = gym.spaces.Discrete(np.array(sm.n))

    else:
        # tuple space
        space = []
        for sm in sms:
            if sm.type == 'box':
                if sm.dtype == 'float':
                    space.append(gym.spaces.Box(np.array(sm.low_f).reshape(sm.shape),
                                                np.array(sm.high_f).reshape(sm.shape),
                                                np.array(sm.shape),
                                                dtype=float))
                elif sm.dtype == 'int':
                    space.append(gym.spaces.Box(np.array(sm.low_i).reshape(sm.shape),
                                                np.array(sm.high_i).reshape(sm.shape),
                                                np.array(sm.shape),
                                                dtype=int))

            elif sm.type == 'discrete':
                space.append(gym.spaces.Discrete(np.array(sm.n)))

        if len(space) == 1:
            space = space[0]
        else:
            space = tuple(space)

    return space


def serialize_data(data):
    # serialize action in a 1d numpy array
    if isinstance(data, tuple) or isinstance(data, list):
        data = np.concatenate([np.array(x).ravel() for x in data])
    elif isinstance(data, dict):
        data = np.concatenate([np.array(x).ravel() for _, x in data.items()])

    elif type(data) is np.ndarray:
        if len(data.shape) > 1:
            data = data.ravel()
    else:  # int of float
        assert isinstance(data, numbers.Integral) or isinstance(data,
                                                                numbers.Real), "Unknown data type for serialization."
        data = np.array([data])
    return data


def deserialize_data(data, space):

    if not isinstance(data, np.ndarray):
        data = np.array(data)

    # space type of tuple
    if isinstance(space, tuple):
        data_ = []
        cnt = 0
        for osp in space:
            osp_size = int(np.prod(osp.shape))

            data_.append(data[cnt:cnt + osp_size].reshape(osp.shape))
            cnt += osp_size

        assert cnt == len(data), 'There is a bug in decoding tuple space.'
        data_ = tuple(data_)

    # space type of dict
    elif isinstance(space, dict):
        data_ = []
        cnt = 0
        for k, osp in space.items():
            osp_size = np.prod(osp.shape)

            data_[k] =data[cnt:cnt + osp_size].reshape(osp.shape)
            cnt += osp_size
        assert cnt == len(data), 'There is a bug in decoding dict space.'

    else:
        data_ = np.array(data, dtype=np.int).squeeze().reshape(space.shape)

    return data_


if __name__ == '__main__':
    # test space_m

    from gym.spaces import Box, Discrete, Dict, Tuple

    # float box 1
    space_box = Box(low=-1.0, high=2.0, shape=(3, 4), dtype=float)
    space_box_m = get_space_message(space_box)

    # float box 2
    space_box = Box(low=np.array([-1.0, -2.0]), high=np.array([2.0, 4.0]), dtype=np.float32)
    space_box_m = get_space_message(space_box)

    # int box
    space_box = Box(low=-1, high=2, shape=(3, 4), dtype=int)
    space_box_m = get_space_message(space_box)

    # discrete
    space_dis = Discrete(2)
    space_dis_m = get_space_message(space_dis)

    # dict
    space_dict = Dict({
        'position': Box(low=-100, high=100, shape=(3,)),
        'velocity': Box(low=-1, high=1, shape=(3,)),
        'task': Discrete(5),
        'progress': Box(low=0, high=100, shape=(), dtype=int),
    })
    space_dict_m = get_space_message(space_dict)

    # tuple
    space_tup = Tuple((Box(low=-1, high=1, shape=(3,)), Discrete(2), Discrete(3)))
    space_tup_m = get_space_message(space_tup)
