from kiwi.util import TreeNode, TreeAryN
from kiwi.common import sort_default


class Step(TreeNode):
    """
    Step is composed of one or multiple operations.Operations in step runs in sequence.
    Step is the minimum unit for scheduling.
    """

    def __init__(self, step_num: str, wait_list: [str], children_parallel_list: [str]):
        """
            step_num: step hierarchy, e.g. 1.2.1
        """
        super().__init__(step_num)
        self.step_num = step_num
        self.wait_list = wait_list
        self.children_parallel_list = children_parallel_list
        self.operations = []

    def append_operation(self, operation) -> None:
        self.operations.append(operation)

    @staticmethod
    def parent_step(step_num: str) -> str:
        return ""


class StepController:
    def __init__(self):
        self.step_tree = TreeAryN(sort_func=sort_default)
        self.step_graph = None
        root_step = Step(step_num="0", wait_list=[], children_parallel_list=[])
        self.step_tree.add_node(root_step)

    def add_step(self, step: Step):
        parent_step_key = Step.parent_step(step.step_num)
        self.step_tree.add_node(step, parent_step_key)

    def _build_step_graph(self) -> None:
        if self.step_graph is not None:
            return
