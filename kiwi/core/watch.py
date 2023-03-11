from queue import Queue

from kiwi.common.message import Msg

from kiwi.common.constant import MsgEndpoint, EventName, MsgLevel, SysStatus

from kiwi.util.event import EventBus

from kiwi.util.graph import DAG

bus = EventBus()


class Watcher:
    def __init__(self):
        self.bio_obj_msg = Queue()
        bus.add_event(func=self.dispatch_watch_msg, event=EventName.WATCH_EVENT)

    def dispatch_watch_msg(self, src: str, raw_msg: str, level=MsgLevel.GOSSIP):
        bus.emit(event=EventName.SCREEN_PRINT_EVENT, msg=Msg(msg=raw_msg, source=src,
                                                             destinations=[MsgEndpoint.USER_TERMINAL],
                                                             code=SysStatus.SUCCESS, level=level))
        if src == MsgEndpoint.BIO_OBJ:
            self.bio_obj_msg.put(raw_msg)
