import asyncio

from kiwi.core.bio_obj import BioObject
from typing import Dict, List
from kiwi.core.sched import StepController
from kiwi.common import singleton, ConstWrapper, SysStatus
from kiwi.core.step import Step
from kiwi.core.bio_op import MeasureFluidOp
from threading import Thread


@singleton
class GenericEnv:
    """GenericEnv class handles user defined wrapper, and makes a basic environment"""

    def __init__(self):
        self.wrappers = []
        self.steps_generic = []

    def append_wrapper(self, wrapper, *args, **kwargs):
        self.wrappers.append(wrapper)
        self._wrapper2core(*args, **kwargs, wrapper=wrapper)

    def _wrapper2core(self, wrapper, *args, **kwargs):
        if wrapper.get_wrapper_type() == ConstWrapper.STEP_WRAPPER:
            step = Step(*args, **kwargs)
            self.steps_generic.append(step)
        elif ConstWrapper.is_op_wrapper(wrapper.get_wrapper_type()):
            op = None
            current_step = self.steps_generic[len(self.steps_generic) - 1]
            if wrapper.get_wrapper_type() == ConstWrapper.OP_MEASURE_FLUID_WRAPPER:
                op = MeasureFluidOp(step_name=current_step.step_num, op_index=len(current_step.operations), *args,
                                    **kwargs)
            current_step.append_operation(op)


@singleton
class KiwiSys:
    def __init__(self):
        self.obj_map = Dict[int, BioObject]
        self.obj_relation = Dict[BioObject, BioObject]
        self.step_controller = StepController()
        # self.server = KiwiServer()

    def build_sys(self):
        """prepare the system"""
        pass

    def shutdown_sys(self):
        pass

    def task_scanner_callback(self):
        self._scan_env()

    def run_task_callback(self):
        task_thread = Thread(target=self._thread_run_task)
        task_thread.start()
        # task_thread.join()

    def _thread_run_task(self):
        while True:
            next_step = self.step_controller.next_step()
            if next_step is None:
                break
            print(next_step.step_num)
            status = next_step.execute()
            print("status:{}".format(status))
            if status != SysStatus.DONE:
                break

    def _init_endpoint(self):
        asyncio.get_event_loop().run_until_complete(self.serve())

    def _scan_process(self):
        """scan steps and build process graph"""
        pass

    def _scan_periphery(self):
        """connect all periphery"""
        pass

    def _scan_entity(self):
        """check reagents"""
        pass

    def _scan_env(self):
        for wrapper in GenericEnv().wrappers:
            if wrapper.get_wrapper_type() == ConstWrapper.STEP_WRAPPER:
                pass
        self.step_controller.add_step_list(GenericEnv().steps_generic)
        self.step_controller.print_step_tree()

    def topology_view(self):
        pass

    def print_sys_init_log(self):
        self.step_controller.print_step_tree()
