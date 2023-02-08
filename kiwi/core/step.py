from kiwi.util import TreeNode, TreeAryN
from kiwi.common import sort_default, singleton
from typing import List


class Step(TreeNode):
    """
    Step is composed of one or multiple operations.Operations in step runs in sequence.
    Step is the minimum unit for scheduling.
    """

    def __init__(self, step_num: str, wait_list: [str], children_parallel_list: [str]):
        """
            step_num: step hierarchy, e.g. 1.2.1
        """
        super().__init__(key=step_num)
        self.step_num = step_num
        self.wait_list = wait_list
        self.children_parallel_list = children_parallel_list
        self.operations = []

    def append_operation(self, operation) -> None:
        self.operations.append(operation)

    @staticmethod
    def parent_step(step_num: str) -> str:
        seq_nums_list = step_num.split('.')
        if len(seq_nums_list) == 1:
            return "0"
        parent_key = ""
        for i in range(0, len(seq_nums_list) - 1):
            parent_key += seq_nums_list[i] + "."
        return parent_key[:-1]


class StepController:
    def __init__(self):
        self.step_tree = TreeAryN(sort_func=sort_default)
        self.step_graph = None
        root_step = Step(step_num="0", wait_list=[], children_parallel_list=[])
        self.step_tree.add_node(root_step)

    def add_step(self, step: Step):
        parent_step_key = Step.parent_step(step.step_num)
        self.step_tree.add_node(step, parent_step_key)

    def add_step_list(self, steps: List[Step]):
        for step in steps:
            parent_step_key = Step.parent_step(step.step_num)
            self.step_tree.add_node(step, parent_step_key)

    def _build_step_graph(self) -> None:
        if self.step_graph is not None:
            return

    def print_step_tree(self):
        print("\n===================step tree===================")
        print(self.step_tree)
        print("=================step tree end=================\n")
