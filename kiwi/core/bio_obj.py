from abc import ABCMeta
from functools import wraps

from enum import Enum


class BioType(Enum):
    Periphery = 1


class BioObject(metaclass=ABCMeta):
    """
    class member end with _um means the function can not be mocked
    """
    def __init__(self, mock=False, mock_obj=None):
        self.bio_type = None
        self.id = None
        self.mock = mock
        self.mock_obj = mock_obj
        self.status = False

    def get_id_um(self) -> None:
        return self.id

    def get_bio_type_um(self) -> BioType:
        return self.bio_type

    def is_mock_um(self) -> bool:
        return self.mock

    def set_mock_um(self, is_mock: bool) -> None:
        self.mock = is_mock
