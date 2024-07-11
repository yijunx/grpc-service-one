# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from app.helloworld import helloworld_pb2 as app_dot_helloworld_dot_helloworld__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in app/helloworld/helloworld_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class GreeterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/helloworld.Greeter/SayHello',
                request_serializer=app_dot_helloworld_dot_helloworld__pb2.HelloRequest.SerializeToString,
                response_deserializer=app_dot_helloworld_dot_helloworld__pb2.HelloReply.FromString,
                _registered_method=True)
        self.SayHelloStreamReply = channel.unary_stream(
                '/helloworld.Greeter/SayHelloStreamReply',
                request_serializer=app_dot_helloworld_dot_helloworld__pb2.HelloRequest.SerializeToString,
                response_deserializer=app_dot_helloworld_dot_helloworld__pb2.HelloReply.FromString,
                _registered_method=True)
        self.SayHelloBidiStream = channel.stream_stream(
                '/helloworld.Greeter/SayHelloBidiStream',
                request_serializer=app_dot_helloworld_dot_helloworld__pb2.HelloRequest.SerializeToString,
                response_deserializer=app_dot_helloworld_dot_helloworld__pb2.HelloReply.FromString,
                _registered_method=True)


class GreeterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloStreamReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloBidiStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=app_dot_helloworld_dot_helloworld__pb2.HelloRequest.FromString,
                    response_serializer=app_dot_helloworld_dot_helloworld__pb2.HelloReply.SerializeToString,
            ),
            'SayHelloStreamReply': grpc.unary_stream_rpc_method_handler(
                    servicer.SayHelloStreamReply,
                    request_deserializer=app_dot_helloworld_dot_helloworld__pb2.HelloRequest.FromString,
                    response_serializer=app_dot_helloworld_dot_helloworld__pb2.HelloReply.SerializeToString,
            ),
            'SayHelloBidiStream': grpc.stream_stream_rpc_method_handler(
                    servicer.SayHelloBidiStream,
                    request_deserializer=app_dot_helloworld_dot_helloworld__pb2.HelloRequest.FromString,
                    response_serializer=app_dot_helloworld_dot_helloworld__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('helloworld.Greeter', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/helloworld.Greeter/SayHello',
            app_dot_helloworld_dot_helloworld__pb2.HelloRequest.SerializeToString,
            app_dot_helloworld_dot_helloworld__pb2.HelloReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SayHelloStreamReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/helloworld.Greeter/SayHelloStreamReply',
            app_dot_helloworld_dot_helloworld__pb2.HelloRequest.SerializeToString,
            app_dot_helloworld_dot_helloworld__pb2.HelloReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SayHelloBidiStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/helloworld.Greeter/SayHelloBidiStream',
            app_dot_helloworld_dot_helloworld__pb2.HelloRequest.SerializeToString,
            app_dot_helloworld_dot_helloworld__pb2.HelloReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
