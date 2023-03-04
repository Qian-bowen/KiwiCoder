from abc import ABCMeta

from enum import Enum


class BioType(Enum):
    Periphery = 1


class BioObject(metaclass=ABCMeta):
    """
    class member end with _um means the function can not be mocked
    """
    def __init__(self, name=None, mock=False, mock_obj=None):
        self.bio_type = None
        self.id = None
        self.key = None
        self.name = name
        self.mock = mock
        self.mock_obj = mock_obj
        self.status = False
        self.content = None

    def set_id(self, obj_id: int) -> None:
        self.id = obj_id
        self.key = str(obj_id)

    def get_id_um(self) -> None:
        return self.id

    def get_bio_type_um(self) -> BioType:
        return self.bio_type

    def is_mock_um(self) -> bool:
        return self.mock

    def set_mock_um(self, is_mock: bool) -> None:
        self.mock = is_mock

