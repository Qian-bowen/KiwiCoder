import json
import uuid
from abc import ABCMeta

from enum import Enum

from kiwi.common import watch_change, CustomJSONEncoder
from kiwi.util.event import EventBus

from kiwi.common.constant import SysStatus, MsgEndpoint, EventName

bus = EventBus()


class BioType(Enum):
    DEFAULT = 0
    Periphery = 1


@watch_change(watch_list=["status"])
class BioObject(metaclass=ABCMeta):
    """
    class member end with _um means the function can not be mocked
    """

    def __init__(self, name="", mock=False, mock_obj=None):
        self.id = None
        self.key = str(uuid.uuid4())
        self.name = name
        self.mock = mock
        self.mock_obj = mock_obj
        self.status = SysStatus.INIT
        self.content = None

    def set_id(self, obj_id: int) -> None:
        self.id = obj_id

    def get_id_um(self) -> int:
        return self.id

    def get_bio_type_um(self) -> BioType:
        return self.bio_type

    def is_mock_um(self) -> bool:
        return self.mock

    def set_mock_um(self, is_mock: bool) -> None:
        self.mock = is_mock

    def _watch(self, name, old_value, value) -> None:
        """ _watch will be called when attributes in @watch_change changes"""
        raw_msg = json.dumps(self.__dict__, cls=CustomJSONEncoder)
        bus.emit(event=EventName.WATCH_EVENT, src=MsgEndpoint.BIO_OBJ, raw_msg=raw_msg)

    def __str__(self):
        return json.dumps(self.__dict__, cls=CustomJSONEncoder)
