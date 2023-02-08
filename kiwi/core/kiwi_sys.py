from .bio_obj import BioObject
from typing import Dict
from .sched import Scheduler
from kiwi.common import singleton, ConstWrapper


@singleton
class Environment:
    def __init__(self):
        self.wrappers = []

    def append_wrapper(self, wrapper):
        self.wrappers.append(wrapper)


@singleton
class SysLoader:
    def __init__(self):
        self.obj_map = Dict[int, BioObject]
        self.obj_relation = Dict[BioObject, BioObject]
        self.step_scheduler = Scheduler()

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
        for wrapper in Environment().wrappers:
            if wrapper.get_wrapper_type() == ConstWrapper.STEP_WRAPPER:
                pass

    def _build_connectors(self):
        """build the message system"""
        pass


class Runtime:
    def __init__(self, sys: SysLoader):
        self.sys = sys

    def run(self):
        """event loop, receive msg and send signal"""

    def prepare(self):
        pass

    def shutdown(self):
        pass

    def get_status(self):
        pass

    def _send_signal(self, from_id: int, to_id: int, seq_num: int, msg: str):
        """signal can only be send to bio object with receive connector"""
        pass
