# Copyright © 2020, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import atexit
import grpc
from sasrl_env.common.env_pb2 import Empty, ServerInfo
from sasrl_env.common.env_pb2_grpc import EnvControlStub
from sasrl_env.client import Env


class EnvControl(object):

    def __init__(self, address):
        self.channel = grpc.insecure_channel(address)
        self.server = EnvControlStub(self.channel)
        self.ports = {}
        atexit.register(self.cleanup)

    def start(self):
        server_info_m = self.server.Start(Empty())
        port = server_info_m.port
        self.ports[port] = 1
        return port

    def close(self, port):
        server_info_m = ServerInfo(port=port)
        self.server.Close(server_info_m)
        del self.ports[port]

    def cleanup(self):
        # pass
        for port, _ in self.ports.items():
            self.server.Close(ServerInfo(port=port))


if __name__ == '__main__':

    import time

    host = '10.122.32.31'
    port = '10006'
    address = '{}:{}'.format(host, port)

    # env = Env('Pong-v0', address)
    ctl = EnvControl(address)
    env_port = ctl.start()
    # sleep for some time to make sure env server is up and running
    time.sleep(2)

    envAddress = '{}:{}'.format(host, env_port)
    env = Env('CartPole-v0', envAddress)

    st = time.time()
    cnt = 0
    for i in range(1000):
        s = env.reset()
        cnt += 1
        done = False
        while not done:
            ns, r, done = env.step(1)
            cnt += 1
            s = ns
            # report
            if cnt % 100 == 0:
                print("cnt: {} -- rate: {}".format(cnt, cnt / (time.time() - st)))
    env.close()
    ctl.close(env_port)
