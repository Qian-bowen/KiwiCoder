from concurrent import futures

import grpc
from kiwi.common.constant import SysStatus


from kiwi.core.watch import Watcher
from kiwi.endpoint.protos import kiwi_pb2, kiwi_pb2_grpc


class KiwiServer(kiwi_pb2_grpc.KiwiServiceServicer):
    def __init__(self):
        self.msg_watch = Watcher()

    async def WatchBioObj(self, request, context):
        while True:
            msg = self.msg_watch.bio_obj_msg.get()
            bio_meta = kiwi_pb2.BioMeta(spec=msg)
            yield kiwi_pb2.BioStatus(status=SysStatus.SUCCESS, bio_meta_list=[bio_meta])

    @staticmethod
    def serve() -> None:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        kiwi_pb2_grpc.add_KiwiServiceServicer_to_server(
            KiwiServer(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()

