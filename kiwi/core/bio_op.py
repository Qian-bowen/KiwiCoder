from abc import ABC, abstractmethod
from time import sleep
from typing import Dict, List, Callable

from kiwi.util.graph import DAG

from kiwi.core.bio_obj import BioObject
from .bio_entity import Container

from .bio_periphery import Periphery, MeasureInstrumPeriphery
from .bio_quantity import Volume, Temperature
from kiwi.common import SysStatus, EventName, Msg, MsgEndpoint, MsgLevel, AutoLevel, SysSignal, with_defer, defer, \
    UserMsg
from kiwi.util import EventBus

bus = EventBus()


class BioOp(ABC):
    def __init__(
            self,
            step_name: str,
            op_index: int,
            dependency_graph: DAG,
            auto_level=AutoLevel.FULL,
    ):
        """
        Args:
            step_name:
            op_index:
            auto_level: the operation needs human or not
            operation has at most three stages, pre run & post run can be block by human, run is the main part
        """
        self.id = None
        self.name = None
        self.step_name = step_name
        self.op_index = op_index
        self.key = BioOp.get_op_identifier(self.step_name, self.op_index)
        self.auto_level = auto_level
        self.dependency_graph = dependency_graph
        self.periphery_dict = Dict[int, Periphery]
        self.bio_obj_dict = Dict[int, BioObject]
        self.status = SysStatus.INIT
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

    def delay_init(self, step_name: str, op_index: int, auto_level=AutoLevel.FULL):
        self.step_name = step_name
        self.op_index = op_index
        self.auto_level = auto_level

    def attach_periphery(self, periphery: Periphery) -> None:
        self.periphery_dict[periphery.get_id_um()] = periphery
        return

    def all_stage_run(self) -> SysStatus:
        """ run the whole operation, check status first """
        while self.status == SysStatus.PENDING:
            ''' sleep to yield cpu to cmd thread '''
            sleep(0.1)

        for func in self.run_funcs:
            BioOp._print_to_screen(msg=UserMsg.OP_STAGE_START_TEMPLATE
                                   .format(self.step_name, self.op_index, func.__name__), level=MsgLevel.INFO)
            status = func()
        return SysStatus.SUCCESS

    @abstractmethod
    @with_defer
    def _run(self) -> SysStatus:
        """ the main stage of run, execute automatically """
        # defer(lambda: BioOp._print_to_screen(msg=UserMsg.OP_STAGE_END_TEMPLATE
        #                                      .format(self.step_name, self.op_index, "_run"),
        #                                      level=MsgLevel.INFO))
        return SysStatus.SUCCESS

    def _human_run(self) -> SysStatus:
        """ notify human to operate """
        BioOp._print_to_screen(msg=UserMsg.OP_OPERATE_HUMAN_TEMPLATE.format(self.step_name, self.op_index),
                               level=MsgLevel.IMPORTANT)
        self.status = SysStatus.PENDING
        while self.status == SysStatus.PENDING:
            ''' sleep to yield cpu to cmd thread '''
            sleep(0.1)
        return SysStatus.SUCCESS

    def _signal_handler(self, signal: SysSignal) -> None:
        if signal == SysSignal.RUN:
            self.status = SysStatus.RUNNING
            self.all_stage_run()
        elif signal == SysSignal.CONTINUE:
            self.status = SysStatus.RUNNING
        elif signal == SysSignal.SUSPEND:
            self.status = SysStatus.PENDING
        BioOp._print_to_screen(msg=UserMsg.OP_SIGNAL_TEMPLATE
                               .format(self.step_name, self.op_index, signal.name), level=MsgLevel.INFO)

    def _pack_op_info(self) -> str:
        pass

    @staticmethod
    def _print_to_screen(msg: str, level: MsgLevel):
        bus.emit(event=EventName.SCREEN_PRINT_EVENT,
                 msg=Msg(msg=msg, source=MsgEndpoint.OP, destinations=[MsgEndpoint.USER_TERMINAL],
                         code=SysStatus.SUCCESS, level=level))

    @staticmethod
    def get_op_identifier(step_name: str, op_index: int) -> str:
        return step_name + " " + str(op_index)

    @abstractmethod
    def get_html_text(self) -> str:
        """ output the text describe the operation """
        pass


class MeasureFluidOp(BioOp):
    def __init__(self, step_name: str, op_index: int, vol: Volume, measure_instrum: MeasureInstrumPeriphery,
                 drivers: List[Periphery], auto_level=AutoLevel.FULL):
        super().__init__(step_name=step_name, op_index=op_index, auto_level=auto_level)
        self.drivers = []
        self.measure_instrum = measure_instrum
        self.threshold = vol.std_value()
        self.drivers = drivers

    @with_defer
    def _run(self) -> SysStatus:
        defer(lambda: BioOp._print_to_screen(msg=UserMsg.OP_STAGE_END_TEMPLATE
                                             .format(self.step_name, self.op_index, "_run"),
                                             level=MsgLevel.INFO))
        for driver in self.drivers:
            driver.start()
        self.measure_instrum.accumulate_read(target=self.threshold, times_in_second=3600, interval=0.1)
        for driver in self.drivers:
            driver.shutdown()
        return SysStatus.SUCCESS

    def get_html_text(self) -> str:
        """ output the text describe the operation """
        return ""


# ==================================== #
#              6. Storage              #
# ==================================== #
class StoreOp(BioOp):
    """ Stores the specified container at a given temperature. """

    def __init__(self, container: Container, temp: Temperature, step_name: str, op_index: int, dependency_graph: DAG,
                 auto_level=AutoLevel.FULL):
        super().__init__(step_name, op_index, dependency_graph, auto_level)
        self.dependency_graph.add_node(target_node=container)
        self.dependency_graph.add_node(target_node=self)
        self.dependency_graph.add_edge(container, self)

    def _run(self) -> SysStatus:
        print("run store op, hello world")
        return SysStatus.SUCCESS

    def get_html_text(self) -> str:
        """ output the text describe the operation """
        return ""
