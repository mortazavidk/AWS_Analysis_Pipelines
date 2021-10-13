# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import smile_lowercase_pb2 as smile__lowercase__pb2


class LowrSmilesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.lowersmile = channel.unary_unary(
                '/LowrSmiles/lowersmile',
                request_serializer=smile__lowercase__pb2.LowerSmileRequest.SerializeToString,
                response_deserializer=smile__lowercase__pb2.LowerSmileResponse.FromString,
                )


class LowrSmilesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def lowersmile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LowrSmilesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'lowersmile': grpc.unary_unary_rpc_method_handler(
                    servicer.lowersmile,
                    request_deserializer=smile__lowercase__pb2.LowerSmileRequest.FromString,
                    response_serializer=smile__lowercase__pb2.LowerSmileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LowrSmiles', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LowrSmiles(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def lowersmile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LowrSmiles/lowersmile',
            smile__lowercase__pb2.LowerSmileRequest.SerializeToString,
            smile__lowercase__pb2.LowerSmileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
