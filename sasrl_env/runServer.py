# Copyright © 2020, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import subprocess
from concurrent import futures
import grpc
import atexit

import pkg_resources

from sasrl_env.utils.utils import check_free_port, get_ip, find_free_port
from sasrl_env.common.env_pb2 import ServerInfo, Empty
from sasrl_env.common.env_pb2_grpc import EnvControlServicer as Service, \
    add_EnvControlServicer_to_server as register

# gym packages to import
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
                                  for i in installed_packages
                                  if (i.key.startswith('gym') or i.key.endswith('gym'))])

modules = sorted(["%s" % i.key.replace('-', '_')
                  for i in installed_packages
                  if ((i.key.startswith('gym') or i.key.endswith('gym')) and (i.key != 'gym'))])
for library in modules:
    try:
        exec("import {module}".format(module=library))
    except Exception as e:
        print(e)

from sasrl_env.common.utils import get_logger

logger = get_logger(log_level='debug')
logger.info("Available gym packages: " + str(installed_packages_list))


class EnvControl(Service):
    def __init__(self, port=None):
        """
        This class handles starting new python subprocesses which runs RL environment server on different ports.
        @param port: the port number which hosts the env controller service. If not specified, the port will be
            assigned automatically.
        """

        super(EnvControl, self).__init__()
        self.host = get_ip()
        self.main_port = port
        self.cur_port = port + 1
        self.subps = {}
        atexit.register(self.cleanup)

    def Start(self, empty_m, _):
        """
        Start a new subprocess serving the env
        @param empty_m: an empty message
        @return: the server information which contains the port number
            in which the environment server process is listening
        """
        # todo: raise if no free port found
        self.cur_port = self.main_port + 1
        while True:
            if self.cur_port not in self.subps.keys():
                if check_free_port(self.host, self.cur_port):
                    # subp = subprocess.Popen(['python', 'serverSingle.py', '--port', '{}'.format(str(self.cur_port))])
                    try:
                        subp = subprocess.Popen(
                            ['python', '-m', 'sasrl_env.serverSingle', '--port', '{}'.format(str(self.cur_port))])
                    except:
                        try:
                            subp = subprocess.Popen(
                                ['python3', '-m', 'sasrl_env.serverSingle', '--port', '{}'.format(str(self.cur_port))])
                        except:
                            raise Exception("Could not find Python executable to run the environment server.")


                    port_number = self.cur_port
                    self.subps[port_number] = subp
                    self.cur_port += 1
                    break

            self.cur_port += 1

        # return server info message
        server_info_m = ServerInfo(port=port_number)
        return server_info_m

    def Close(self, server_info_m, context):

        """
        Removes the job running on the specified port.
        @param port_m: the port message in which the env server is listening
        @return: An empty message
        """
        #
        port = server_info_m.port
        self.subps[port].terminate()
        logger.info("Env server listening on port {} terminated".format(str(port)))
        del self.subps[port]

        return Empty()

    def cleanup(self):
        """
        This function terminates all open subprocesses when terminated. This function is called automatically
        when the the env controller runs in an error or keyboard interrupt at the destruction time.
        """
        logger.info("Running cleanup...")
        for port, sp in self.subps.items():
            sp.terminate()
            logger.debug("Cleaned up env server listening on port {}".format(str(port)))


class registerController(object):
    def __init__(self):
        """
        Initialize the env controller
        """
        self.port = None
        self.host = get_ip()  # get host ip

    def start(self, port, max_workers=1):
        """
        This function start a environment server listening on a port and waits for termination
        @param port: the port that the environment is listening for calls
        @param max_workers: maximum number of workers
        """
        # find the controller port
        if port == 0:
            # find the port number if not specified by user
            self.port = find_free_port()
            if self.port is None:
                logger.error("No free port available on {}".format(self.host))
        else:
            # check if the port is available, otherwise increase port number
            while True:
                if check_free_port(self.host, port):
                    self.port = port
                    break
                port += 1

        # register a grpc server
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        register(EnvControl(self.port), server)

        # start the server
        address = '{}:{}'.format(self.host, self.port)
        server.add_insecure_port(address)
        server.start()
        logger.info('Env controller started at: {}:{}'.format(self.host, self.port))
        server.wait_for_termination()


def start(port):
    rs = registerController()
    rs.start(port)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Environment Controller')
    parser.add_argument('--port', '-p', type=int, default=0,
                        help='The port number which hosts the env controller service. '
                             'If not specified, the port will be assigned automatically.')
    args = parser.parse_args()
    start(args.port)
