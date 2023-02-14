from kiwi.util import TreeNode, TreeAryN, EventBus
from kiwi.common import sort_default, EventName, SysStatus, Msg, MsgEndpoint, MsgLevel
from typing import List
from .bio_op import BioOp

bus = EventBus()


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
        self.operations = List[BioOp]

    def append_operation(self, operation) -> None:
        self.operations.append(operation)

    def execute(self) -> None:
        """ execute the step operations, if fail, rollback and retry """
        for op in self.operations:
            op_status = op.all_stage_run()
            if op_status != SysStatus.SUCCESS:
                rollback_status = op.rollback()
                if rollback_status == SysStatus.SUCCESS:
                    re_op_status = op.all_stage_run()
                    if re_op_status != SysStatus.SUCCESS:
                        self._fatal_alarm()
                else:
                    self._fatal_alarm()

    def rollback(self) -> SysStatus:
        pass

    @bus.on(event=EventName.OP_EVENT)
    def _listen_operation(self, op_index: int, op_status: SysStatus):
        """ log and print """
        """ check all """
        pass

    @staticmethod
    def parent_step(step_num: str) -> str:
        seq_nums_list = step_num.split('.')
        if len(seq_nums_list) == 1:
            return "0"
        parent_key = ""
        for i in range(0, len(seq_nums_list) - 1):
            parent_key += seq_nums_list[i] + "."
        return parent_key[:-1]

    def _fatal_alarm(self) -> None:
        raw = str(self)
        msg = Msg(msg=raw, source=MsgEndpoint.STEP, destinations=[MsgEndpoint.WATCH], level=MsgLevel.FATAL)
        bus.emit(event=EventName.FATAL_ALARM_EVENT, msg=msg)


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

    @bus.on(event=EventName.STEP_EVENT)
    def _listen_step(self, step_name: str, step_status: SysStatus):
        pass
