from abc import ABC, abstractmethod
from typing import Dict

from .bio_periphery import Periphery


class BioOp(ABC):
    def __init__(
            self,
            op_detail: str
    ):
        self.op_detail = op_detail
        self.periphery_dict = Dict[int, Periphery]

    def get_detail(self) -> str:
        return self.op_detail

    def attach_periphery(self, periphery: Periphery) -> None:
        self.periphery_dict[periphery.get_id()] = periphery
        return

    @abstractmethod
    def run(self) -> None:
        pass


class FirstStepOp(BioOp):
    def __init__(self, op_detail: str):
        super().__init__(op_detail=op_detail)

    def run(self) -> None:
        pass


class StartProtocolOp(BioOp):
    def __init__(
            self,
            op_detail: str
    ):
        super().__init__(op_detail=op_detail)

    def run(self) -> None:
        pass
