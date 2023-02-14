from .constant import MsgLevel, SysStatus


class Msg:
    def __init__(self, msg: str, source: str, destinations: [str], code=SysStatus.FAIL, level=MsgLevel.GOSSIP):
        self.msg = msg
        self.code = code
        self.level = level
        self.source = source
        self.destinations = destinations

    def _pack(self) -> str:
        # TODO
        return self.msg

    @staticmethod
    def unpack(raw_msg: str):
        pass

    def __str__(self):
        return self._pack()
