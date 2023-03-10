from queue import Queue

from kiwi.common.constant import MsgEndpoint, EventName

from kiwi.util.event import EventBus

from kiwi.util.graph import DAG

bus = EventBus()


class Watcher:
    def __init__(self):
        self.bio_obj_msg = Queue()

    @bus.on(event=EventName.WATCH_EVENT)
    def dispatch_watch_msg(self, src: MsgEndpoint, raw_msg: str):
        if src == MsgEndpoint.BIO_OBJ:
            self.bio_obj_msg.put(raw_msg)
