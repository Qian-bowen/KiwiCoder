from .constant import MsgLevel, SysStatus


class Msg:
    def __init__(self, msg: str, source: str, destination: str, code=SysStatus.FAIL, level=MsgLevel.GOSSIP):
        self.msg = msg
        self.code = code
        self.level = level
        self.source = source
        self.destination = destination

    def _pack(self) -> str:
        pass

    @staticmethod
    def unpack(raw_msg: str):
        pass

    def __str__(self):
        return self._pack()
