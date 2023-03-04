import grpc
import kiwi_pb2
import kiwi_pb2_grpc


class KiwiServer(kiwi_pb2_grpc.KiwiServiceServicer):
    def __init__(self):
        self.msg_pool = None
        pass

    async def GetMsg(self, request, context):
        while True:
            msg = self.msg_pool.get_msg()
            yield kiwi_pb2.GetMsgResponse()

    @staticmethod
    async def serve() -> None:
        server = grpc.aio.server()
        kiwi_pb2_grpc.add_KiwiServiceServicer_to_server(
            KiwiServer(), server)
        server.add_insecure_port('[::]:50051')
        await server.start()
        await server.wait_for_termination()

