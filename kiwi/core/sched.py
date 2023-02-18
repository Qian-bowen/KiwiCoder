from kiwi.util import TreeNode, TreeAryN, EventBus, DAG
from kiwi.common import sort_default, EventName, SysStatus, Msg, MsgEndpoint, MsgLevel, ScheduleMode
from typing import List
from .step import Step
import random

bus = EventBus()


class Strategy:
    @staticmethod
    def next_object_random(schedule_list: []) -> [Step]:
        return [schedule_list[random.randint(0, len(schedule_list) - 1)]]

    @staticmethod
    def next_first(schedule_list: []) -> [Step]:
        return [schedule_list[0]]

    @staticmethod
    def next_all(schedule_list: []) -> [Step]:
        return schedule_list


class StepController:
    def __init__(self):
        self.step_tree = TreeAryN(sort_func=sort_default)
        self.step_graph = DAG()
        self.schedule_mode = ScheduleMode.SEQ
        root_step = Step(step_num="0", wait_list=[], children_parallel_list=[])
        self.step_tree.add_node(root_step)

    def add_step_list(self, steps: List[Step]):
        for step in steps:
            parent_step_key = Step.parent_step(step.step_num)
            self.step_tree.add_node(step, parent_step_key)

    def add_step_list_to_graph(self, steps: List[Step]):
        for step in steps:
            self.step_graph.add_node(step)
        for step in steps:
            younger_brother_step = Step.brother_step(step.step_num, True)
            if younger_brother_step is not None:
                self.step_graph.add_edge(younger_brother_step, step.step_num)
            wait_list = step.wait_list
            for wait_step_num in wait_list:
                self.step_graph.add_edge(wait_step_num, step.step_num)
        for step in steps:
            parallel_list = step.children_parallel_list
            for pa_i in parallel_list:
                for pa_j in parallel_list:
                    if self.step_graph.is_edge_exist(pa_i, pa_j):
                        self.step_graph.delete_edge_by_key(pa_i, pa_j)

    def build_schedule_steps(self, schedule_mode: ScheduleMode) -> None:
        self.schedule_mode = schedule_mode

    def next_steps(self) -> [Step]:
        schedule_list = []
        ''' get steps that are available '''
        if self.schedule_mode == ScheduleMode.SEQ:
            schedule_list = self.step_tree.preorder(exclude_done=True)
        elif self.schedule_mode == ScheduleMode.GRAPH:
            schedule_list = self.step_graph.available_nodes()
        if len(schedule_list) == 0:
            return None
        ''' choose steps according to strategy '''
        if self.schedule_mode == ScheduleMode.SEQ:
            return Strategy.next_first(schedule_list)
        elif self.schedule_mode == ScheduleMode.GRAPH:
            return Strategy.next_all(schedule_list)
        return []

    def print_step_tree(self):
        print("\n===================step tree===================")
        print(self.step_tree)
        print("=================step tree end=================\n")

    @bus.on(event=EventName.STEP_EVENT)
    def _listen_step(self, step_name: str, step_status: SysStatus):
        pass
