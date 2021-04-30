# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sasrl_env.common.env_pb2 as env__pb2


class EnvControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Start = channel.unary_unary(
                '/EnvControl/Start',
                request_serializer=env__pb2.Empty.SerializeToString,
                response_deserializer=env__pb2.ServerInfo.FromString,
                )
        self.Close = channel.unary_unary(
                '/EnvControl/Close',
                request_serializer=env__pb2.ServerInfo.SerializeToString,
                response_deserializer=env__pb2.Empty.FromString,
                )


class EnvControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Start(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Close(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EnvControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=env__pb2.Empty.FromString,
                    response_serializer=env__pb2.ServerInfo.SerializeToString,
            ),
            'Close': grpc.unary_unary_rpc_method_handler(
                    servicer.Close,
                    request_deserializer=env__pb2.ServerInfo.FromString,
                    response_serializer=env__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EnvControl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EnvControl(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EnvControl/Start',
            env__pb2.Empty.SerializeToString,
            env__pb2.ServerInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Close(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EnvControl/Close',
            env__pb2.ServerInfo.SerializeToString,
            env__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class EnvStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Handshake = channel.unary_unary(
                '/Env/Handshake',
                request_serializer=env__pb2.Empty.SerializeToString,
                response_deserializer=env__pb2.MetaData.FromString,
                )
        self.Make = channel.unary_unary(
                '/Env/Make',
                request_serializer=env__pb2.Name.SerializeToString,
                response_deserializer=env__pb2.Info.FromString,
                )
        self.Reset = channel.unary_unary(
                '/Env/Reset',
                request_serializer=env__pb2.Empty.SerializeToString,
                response_deserializer=env__pb2.Observation.FromString,
                )
        self.Step = channel.unary_unary(
                '/Env/Step',
                request_serializer=env__pb2.Action.SerializeToString,
                response_deserializer=env__pb2.Transition.FromString,
                )
        self.Render = channel.unary_unary(
                '/Env/Render',
                request_serializer=env__pb2.RenderMode.SerializeToString,
                response_deserializer=env__pb2.RenderOut.FromString,
                )
        self.Seed = channel.unary_unary(
                '/Env/Seed',
                request_serializer=env__pb2.EnvSeed.SerializeToString,
                response_deserializer=env__pb2.Empty.FromString,
                )
        self.Sample = channel.unary_unary(
                '/Env/Sample',
                request_serializer=env__pb2.Empty.SerializeToString,
                response_deserializer=env__pb2.Action.FromString,
                )
        self.Close = channel.unary_unary(
                '/Env/Close',
                request_serializer=env__pb2.Empty.SerializeToString,
                response_deserializer=env__pb2.Empty.FromString,
                )


class EnvServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Handshake(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Make(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Step(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Render(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Seed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sample(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Close(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EnvServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Handshake': grpc.unary_unary_rpc_method_handler(
                    servicer.Handshake,
                    request_deserializer=env__pb2.Empty.FromString,
                    response_serializer=env__pb2.MetaData.SerializeToString,
            ),
            'Make': grpc.unary_unary_rpc_method_handler(
                    servicer.Make,
                    request_deserializer=env__pb2.Name.FromString,
                    response_serializer=env__pb2.Info.SerializeToString,
            ),
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=env__pb2.Empty.FromString,
                    response_serializer=env__pb2.Observation.SerializeToString,
            ),
            'Step': grpc.unary_unary_rpc_method_handler(
                    servicer.Step,
                    request_deserializer=env__pb2.Action.FromString,
                    response_serializer=env__pb2.Transition.SerializeToString,
            ),
            'Render': grpc.unary_unary_rpc_method_handler(
                    servicer.Render,
                    request_deserializer=env__pb2.RenderMode.FromString,
                    response_serializer=env__pb2.RenderOut.SerializeToString,
            ),
            'Seed': grpc.unary_unary_rpc_method_handler(
                    servicer.Seed,
                    request_deserializer=env__pb2.EnvSeed.FromString,
                    response_serializer=env__pb2.Empty.SerializeToString,
            ),
            'Sample': grpc.unary_unary_rpc_method_handler(
                    servicer.Sample,
                    request_deserializer=env__pb2.Empty.FromString,
                    response_serializer=env__pb2.Action.SerializeToString,
            ),
            'Close': grpc.unary_unary_rpc_method_handler(
                    servicer.Close,
                    request_deserializer=env__pb2.Empty.FromString,
                    response_serializer=env__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Env', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Env(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Handshake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Env/Handshake',
            env__pb2.Empty.SerializeToString,
            env__pb2.MetaData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Make(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Env/Make',
            env__pb2.Name.SerializeToString,
            env__pb2.Info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Env/Reset',
            env__pb2.Empty.SerializeToString,
            env__pb2.Observation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Step(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Env/Step',
            env__pb2.Action.SerializeToString,
            env__pb2.Transition.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Render(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Env/Render',
            env__pb2.RenderMode.SerializeToString,
            env__pb2.RenderOut.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Seed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Env/Seed',
            env__pb2.EnvSeed.SerializeToString,
            env__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sample(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Env/Sample',
            env__pb2.Empty.SerializeToString,
            env__pb2.Action.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Close(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Env/Close',
            env__pb2.Empty.SerializeToString,
            env__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
