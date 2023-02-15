from abc import ABC, abstractmethod
from typing import Dict, List, Callable
from threading import Lock

from .bio_periphery import Periphery, MeasureInstrumPeriphery
from .bio_quantity import Volume
from kiwi.common import SysStatus, EventName, Msg, MsgEndpoint, MsgLevel, AutoLevel, SysSignal, with_defer, defer, \
    UserMsg
from kiwi.util import EventBus

bus = EventBus()


class BioOp(ABC):
    def __init__(
            self,
            step_name: str,
            op_index: int,
            auto_level=AutoLevel.FULL
    ):
        """
        Args:
            step_name:
            op_index:
            auto_level: the operation needs human or not
            operation has at most three stages, pre run & post run can be block by human, run is the main part
        """
        self.step_name = step_name
        self.op_index = op_index
        self.auto_level = auto_level
        self.periphery_dict = Dict[int, Periphery]
        self.status = SysStatus.INIT
        self.running_lock = Lock()
        self.run_funcs = List[Callable]

        bus.add_event(func=self._signal_handler,
                      event=EventName.OP_SIGNAL_RECEIVE_EVENT
                      .format(BioOp.get_op_identifier(self.step_name, self.op_index)))
        if auto_level == AutoLevel.FULL:
            self.run_funcs = [self._run]
        elif auto_level == AutoLevel.SEMI:
            self.run_funcs = [self._human_run, self._run, self._human_run]
        elif auto_level == AutoLevel.HUMAN:
            self.run_funcs = [self._human_run]

    def __str__(self) -> str:
        return self._pack_op_info()

    def attach_periphery(self, periphery: Periphery) -> None:
        self.periphery_dict[periphery.get_id_um()] = periphery
        return

    def all_stage_run(self) -> SysStatus:
        for func in self.run_funcs:
            BioOp._print_to_screen(msg=UserMsg.OP_STAGE_START_TEMPLATE
                                   .format(self.step_name, self.op_index, func.__name__), level=MsgLevel.INFO)
            self.running_lock.acquire()
            status = func()
            BioOp._print_to_screen(msg=UserMsg.OP_STAGE_END_TEMPLATE
                                   .format(self.step_name, self.op_index, func.__name__), level=MsgLevel.INFO)
        return SysStatus.SUCCESS

    @abstractmethod
    @with_defer
    def _run(self) -> SysStatus:
        """ the main stage of run, execute automatically """
        defer(lambda: self.running_lock.release())
        return SysStatus.SUCCESS

    def _human_run(self) -> SysStatus:
        """ notify human to operate """
        BioOp._print_to_screen(msg=UserMsg.OP_OPERATE_HUMAN, level=MsgLevel.IMPORTANT)
        return SysStatus.SUCCESS

    def _signal_handler(self, signal: SysSignal) -> None:
        if signal == SysSignal.RUN:
            self.all_stage_run()
        elif signal == SysSignal.CONTINUE:
            self.running_lock.release()

    def _pack_op_info(self) -> str:
        pass

    @staticmethod
    def _print_to_screen(msg: str, level: MsgLevel):
        bus.emit(EventName.SCREEN_PRINT_EVENT,
                 Msg(msg=msg, source=MsgEndpoint.OP, destinations=[MsgEndpoint.USER_TERMINAL],
                     code=SysStatus.AVAILABLE, level=level))

    @staticmethod
    def get_op_identifier(step_name: str, op_index: int) -> str:
        return step_name + " " + str(op_index)


class MeasureFluidOp(BioOp):
    def __init__(self, step_name: str, op_index: int, vol: Volume, measure_instrum: MeasureInstrumPeriphery,
                 drivers: List[Periphery]):
        super().__init__(step_name, op_index)
        self.drivers = []
        self.measure_instrum = measure_instrum
        self.threshold = vol.std_value()
        self.drivers = drivers

    @with_defer
    def _run(self) -> SysStatus:
        defer(lambda: self.running_lock.release())
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
