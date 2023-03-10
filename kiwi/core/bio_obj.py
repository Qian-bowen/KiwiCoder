import json
import uuid
from abc import ABCMeta

from enum import Enum

from kiwi.util.event import EventBus

from kiwi.common.constant import SysStatus, MsgEndpoint, EventName

bus = EventBus()


class BioType(Enum):
    Periphery = 1


class BioObject(metaclass=ABCMeta):
    """
    class member end with _um means the function can not be mocked
    """
    def __init__(self, name=None, mock=False, mock_obj=None):
        self.bio_type = None
        self.id = None
        self.key = uuid.uuid4()
        self.name = name
        self.mock = mock
        self.mock_obj = mock_obj
        self._status = SysStatus.INIT
        self.content = None

    def set_id(self, obj_id: int) -> None:
        self.id = obj_id

    def get_id_um(self) -> None:
        return self.id

    def get_bio_type_um(self) -> BioType:
        return self.bio_type

    def is_mock_um(self) -> bool:
        return self.mock

    def set_mock_um(self, is_mock: bool) -> None:
        self.mock = is_mock

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status
        bus.emit(event=EventName.WATCH_EVENT, src=MsgEndpoint.BIO_OBJ, raw_mag=self.__str__())

    def __str__(self):
        return json.dumps(self.__dict__)


