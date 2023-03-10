# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from kiwi.endpoint.protos import kiwi_pb2 as kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2


class KiwiServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WatchBioObj = channel.unary_stream(
                '/endpoint.KiwiService/WatchBioObj',
                request_serializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.WatchBioRequest.SerializeToString,
                response_deserializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.BioStatus.FromString,
                )
        self.WatchProtocol = channel.unary_stream(
                '/endpoint.KiwiService/WatchProtocol',
                request_serializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.WatchProtocolRequest.SerializeToString,
                response_deserializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.ProtocolStatus.FromString,
                )
        self.WatchNotification = channel.unary_stream(
                '/endpoint.KiwiService/WatchNotification',
                request_serializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.WatchNotificationRequest.SerializeToString,
                response_deserializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.NotificationResponse.FromString,
                )


class KiwiServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WatchBioObj(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchProtocol(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WatchNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KiwiServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'WatchBioObj': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchBioObj,
                    request_deserializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.WatchBioRequest.FromString,
                    response_serializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.BioStatus.SerializeToString,
            ),
            'WatchProtocol': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchProtocol,
                    request_deserializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.WatchProtocolRequest.FromString,
                    response_serializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.ProtocolStatus.SerializeToString,
            ),
            'WatchNotification': grpc.unary_stream_rpc_method_handler(
                    servicer.WatchNotification,
                    request_deserializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.WatchNotificationRequest.FromString,
                    response_serializer=kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.NotificationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'endpoint.KiwiService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KiwiService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WatchBioObj(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/endpoint.KiwiService/WatchBioObj',
            kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.WatchBioRequest.SerializeToString,
            kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.BioStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WatchProtocol(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/endpoint.KiwiService/WatchProtocol',
            kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.WatchProtocolRequest.SerializeToString,
            kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.ProtocolStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WatchNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/endpoint.KiwiService/WatchNotification',
            kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.WatchNotificationRequest.SerializeToString,
            kiwi_dot_endpoint_dot_protos_dot_kiwi__pb2.NotificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
