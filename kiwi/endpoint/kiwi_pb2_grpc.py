# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import kiwi_pb2 as kiwi__pb2


class KiwiServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMsg = channel.unary_stream(
                '/endpoint.KiwiService/GetMsg',
                request_serializer=kiwi__pb2.GetMsgRequest.SerializeToString,
                response_deserializer=kiwi__pb2.GetMsgResponse.FromString,
                )


class KiwiServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMsg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KiwiServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMsg': grpc.unary_stream_rpc_method_handler(
                    servicer.GetMsg,
                    request_deserializer=kiwi__pb2.GetMsgRequest.FromString,
                    response_serializer=kiwi__pb2.GetMsgResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'endpoint.KiwiService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KiwiService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMsg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/endpoint.KiwiService/GetMsg',
            kiwi__pb2.GetMsgRequest.SerializeToString,
            kiwi__pb2.GetMsgResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
