from kiwi.util import TreeNode, EventBus
from kiwi.common import EventName, SysStatus, Msg, MsgEndpoint, MsgLevel
from typing import Optional

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
        self.operations = []
        self.status = SysStatus.INIT

    def done(self) -> bool:
        return self.status == SysStatus.DONE

    def append_operation(self, operation) -> None:
        self.operations.append(operation)

    def execute(self) -> None:
        """ execute the step operations, if fail, rollback and retry """
        all_status = SysStatus.INIT
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
        all_status = SysStatus.DONE
        self.status = SysStatus.DONE
        return all_status

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

    @staticmethod
    def brother_step(step_num: str, younger_one: bool) -> Optional[str]:
        seq_nums_list = step_num.split('.')
        if len(seq_nums_list) == 1 and seq_nums_list[0] == "0":
            return None
        last_num = seq_nums_list[len(seq_nums_list) - 1]
        if younger_one and last_num == "1":
            return None
        if younger_one:
            brother_last = str(int(last_num) - 1)
        else:
            brother_last = str(int(last_num) + 1)
        brother_key = ""
        for i in range(0, len(seq_nums_list) - 1):
            brother_key += seq_nums_list[i] + "."
        return brother_key + brother_last

    def _fatal_alarm(self) -> None:
        raw = str(self)
        msg = Msg(msg=raw, source=MsgEndpoint.STEP, destinations=[MsgEndpoint.WATCH], level=MsgLevel.FATAL)
        bus.emit(event=EventName.FATAL_ALARM_EVENT, msg=msg)
