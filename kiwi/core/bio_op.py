from abc import ABC, abstractmethod
from typing import Dict, List

from .bio_periphery import Periphery, MeasureInstrumPeriphery, DriverPeriphery
from .bio_quantity import Volume
from kiwi.common import SysStatus, EventName, Msg, MsgEndpoint, MsgLevel
from kiwi.util import EventBus

bus = EventBus()


class BioOp(ABC):
    def __init__(
            self,
            step_name: str,
            op_index: int,
    ):
        self.step_name = step_name
        self.op_index = op_index
        self.periphery_dict = Dict[int, Periphery]
        self.status = SysStatus.INIT

    def __str__(self) -> str:
        return self._pack_op_info()

    def attach_periphery(self, periphery: Periphery) -> None:
        self.periphery_dict[periphery.get_id_um()] = periphery
        return

    def run(self) -> SysStatus:
        pass

    def rollback(self) -> None:
        pass

    def snapshot(self) -> str:
        pass

    def _pack_op_info(self) -> str:
        pass

    def _fatal_alarm(self) -> None:
        raw = str(self)
        msg = Msg(msg=raw, source=MsgEndpoint.OP, destinations=[MsgEndpoint.WATCH], level=MsgLevel.FATAL)
        bus.emit(event=EventName.FATAL_ALARM_EVENT, msg=msg)


class MeasureFluid(BioOp):
    def __init__(self, step_name: str, op_index: int, vol: Volume, measure_instrum: MeasureInstrumPeriphery,
                 drivers: List[DriverPeriphery]):
        super().__init__(step_name, op_index)
        self.drivers = []
        self.measure_instrum = measure_instrum
        self.threshold = vol.std_value()
        self.drivers = drivers

    def run(self) -> SysStatus:
        for driver in self.drivers:
            driver.start()
        self.measure_instrum.accumulate_read(target=self.threshold, times_in_second=3600, interval=0.1)
        for driver in self.drivers:
            driver.shutdown()
        return SysStatus.SUCCESS


class Heat(BioOp):
    def __init__(self, step_name: str, op_index: int):
        super().__init__(step_name, op_index)


class FirstStepOp(BioOp):
    def __init__(self, step_name: str):
        super().__init__(step_name=step_name)

    def run(self) -> None:
        pass


class StartProtocolOp(BioOp):
    def __init__(
            self,
            step_name: str
    ):
        super().__init__(step_name=step_name)

    def run(self) -> None:
        pass
