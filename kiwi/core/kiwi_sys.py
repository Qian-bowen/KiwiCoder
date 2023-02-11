from .bio_obj import BioObject
from typing import Dict
from .sched import Scheduler
from kiwi.common import singleton, ConstWrapper
from .step import Step, StepController


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
            return step


@singleton
class SysLoader:
    def __init__(self):
        self.obj_map = Dict[int, BioObject]
        self.obj_relation = Dict[BioObject, BioObject]
        self.step_scheduler = Scheduler()
        self.step_controller = StepController()

    def build_sys(self):
        """prepare the system"""
        self._scan_env()
        pass

    def shutdown_sys(self):
        pass

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

    def topology_view(self):
        pass

    def print_sys_init_log(self):
        self.step_controller.print_step_tree()
