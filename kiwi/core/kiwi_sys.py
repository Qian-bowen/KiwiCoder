import asyncio

from kiwi.core.bio_obj import BioObject
from typing import Dict, List, Any, Callable
from kiwi.core.sched import StepController
from kiwi.common import singleton, ConstWrapper, ScheduleMode
from kiwi.core.step import Step
from kiwi.core.bio_op import MeasureFluidOp
from threading import Thread
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


@singleton
class GenericEnv:
    """GenericEnv class handles user defined wrapper, and makes a basic environment"""

    def __init__(self):
        self.wrappers = []
        self.steps_generic = []

    def reset(self):
        self.__init__()

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
    def __init__(self, thread_pool_size: int, schedule_mode=ScheduleMode.SEQ):
        self.obj_map = Dict[int, BioObject]
        self.obj_relation = Dict[BioObject, BioObject]
        self.step_controller = StepController(schedule_mode)
        self.thread_pool = ThreadPoolExecutor(max_workers=thread_pool_size)
        self.sys_var_map = Dict[str, Callable]

    def build_sys(self):
        """prepare the system"""
        self._init_sys_var_map()

    def shutdown_sys(self):
        pass

    def task_scanner(self):
        self._scan_env()

    def run_task(self):
        task_thread = Thread(target=self._thread_run_task)
        task_thread.start()

    def set_sys_variable(self, var_name: str, var_value) -> str:
        self.sys_var_map[var_name+"_setter"](var_value)
        val = self.sys_var_map[var_name+"_getter"]()
        if hasattr(val, 'name'):
            val = val.name
        return str(val)

    def get_sys_variable(self, var_name: str) -> str:
        val = self.sys_var_map[var_name+"_getter"]()
        if hasattr(val, 'name'):
            val = val.name
        return str(val)

    def _thread_run_task(self):
        while True:
            next_steps = self.step_controller.next_steps()
            if next_steps is None or len(next_steps) == 0:
                break
            all_step_task = [self.thread_pool.submit(next_step.execute) for next_step in next_steps]
            wait(all_step_task, return_when=ALL_COMPLETED)
            for step_task in all_step_task:
                status = step_task.result()
                # print("status:{}".format(status))

    def _init_endpoint(self):
        asyncio.get_event_loop().run_until_complete(self.serve())

    def _init_sys_var_map(self):
        def schedule_mode_getter(): return self.step_controller.schedule_mode
        def schedule_mode_setter(val): self.step_controller.schedule_mode = val
        self.sys_var_map = {
            "schedule_mode_getter": schedule_mode_getter,
            "schedule_mode_setter": schedule_mode_setter
        }

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
        self.step_controller = StepController(schedule_mode=ScheduleMode.GRAPH)
        self.step_controller.add_step_list(GenericEnv().steps_generic)
        self.step_controller.print_step_tree()
        self.step_controller.add_step_list_to_graph(GenericEnv().steps_generic)

    def topology_view(self):
        pass

    def print_sys_init_log(self):
        self.step_controller.print_step_tree()
