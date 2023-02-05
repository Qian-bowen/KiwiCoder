from .bio_obj import BioObject
from typing import Dict
from .sched import Scheduler


class SysLoader:
    def __init__(self):
        self.obj_map = Dict[int, BioObject]
        self.obj_relation = Dict[BioObject, BioObject]
        self.step_scheduler = Scheduler()
        pass

    def build_sys(self):
        """prepare the system"""
        pass

    def shutdown_sys(self):
        """prepare the system"""
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

    def _build_view(self):
        """build the relationship view of all bio objects"""
        pass

    def _build_connectors(self):
        """build the message system"""
        pass


class Runtime:
    def __init__(self, sys: SysLoader):
        self.sys = sys

    def run(self):
        """event loop, receive msg and send signal"""
        pass

    def get_status(self):
        pass

    def _send_signal(self, from_id: int, to_id: int, seq_num: int, msg: str):
        """signal can only be send to bio object with receive connector"""
        pass
