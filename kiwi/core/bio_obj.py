from abc import ABCMeta
from functools import wraps

from enum import Enum


class BioType(Enum):
    Periphery = 1


class BioObject(metaclass=ABCMeta):
    def __init__(self, mock=False):
        self.bio_type = None
        self.id = None
        self.mock = mock
        self.status = False

    def get_id(self) -> None:
        return self.id

    def get_bio_type(self) -> BioType:
        return self.bio_type

    def is_mock(self) -> bool:
        return self.mock

    def input(self, in_msg: str, stream=False, connector=None):
        """
        receive msg from other object
        if connector does not exist, just set the msg;
        or receive from connector until end
        """
        pass

    def output(self, stream=False, connector=None) -> str:
        """
        send msg to other object
        if connector does not exist, just return the msg;
        or send the message through connector
        """
        pass
