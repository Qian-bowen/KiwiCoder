from kiwi.util import TreeNode, TreeAryN, EventBus, DAG
from kiwi.common import sort_default, EventName, SysStatus, Msg, MsgEndpoint, MsgLevel, ScheduleMode
from typing import List
from .step import Step
import random

bus = EventBus()


class Strategy:
    @staticmethod
    def next_object_random(schedule_list: []) -> Step:
        return schedule_list[random.randint(0, len(schedule_list) - 1)]

    @staticmethod
    def next_first(schedule_list: []) -> Step:
        return schedule_list[0]


class StepController:
    def __init__(self):
        self.step_tree = TreeAryN(sort_func=sort_default)
        self.step_graph = DAG()
        self.schedule_mode = ScheduleMode.SEQ
        root_step = Step(step_num="0", wait_list=[], children_parallel_list=[])
        self.step_tree.add_node(root_step)

    def add_step(self, step: Step):
        parent_step_key = Step.parent_step(step.step_num)
        self.step_tree.add_node(step, parent_step_key)

    def add_step_list(self, steps: List[Step]):
        for step in steps:
            parent_step_key = Step.parent_step(step.step_num)
            self.step_tree.add_node(step, parent_step_key)

    def build_schedule_steps(self, schedule_mode: ScheduleMode) -> None:
        self.schedule_mode = schedule_mode

    def next_step(self):
        schedule_list = []
        if self.schedule_mode == ScheduleMode.SEQ:
            schedule_list = self.step_tree.preorder(exclude_done=True)
            print("len:{}".format(len(schedule_list)))
        if len(schedule_list) == 0:
            return None
        return Strategy.next_first(schedule_list)

    def print_step_tree(self):
        print("\n===================step tree===================")
        print(self.step_tree)
        print("=================step tree end=================\n")

    @bus.on(event=EventName.STEP_EVENT)
    def _listen_step(self, step_name: str, step_status: SysStatus):
        pass
