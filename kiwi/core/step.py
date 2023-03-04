from kiwi.core.bio_op import BioOp
from kiwi.util import TreeNode, EventBus
from kiwi.common import EventName, SysStatus, Msg, MsgEndpoint, MsgLevel, UserMsg
from typing import Optional

bus = EventBus()


class Step(TreeNode):
    """
    Step is composed of one or multiple operations.Operations in step runs in sequence.
    Step is the minimum unit for scheduling.
    """

    def __init__(self, name: str, step_num: str, wait_list: [str], children_parallel_list: [str], repeat_times: int):
        """
            step_num: step hierarchy, e.g. 1.2.1
        """
        super().__init__(key=step_num)
        self.name = name
        self.step_num = step_num
        self.wait_list = wait_list
        self.children_parallel_list = children_parallel_list
        self.repeat_times = repeat_times
        self.operations = []
        self.status = SysStatus.INIT

    def reset(self):
        self.__init__(step_num=self.step_num,
                      wait_list=self.wait_list,
                      children_parallel_list=self.children_parallel_list,
                      repeat_times=self.repeat_times)

    def done(self) -> bool:
        return self.status == SysStatus.DONE

    def append_operation(self, operation) -> None:
        self.operations.append(operation)

    def execute(self) -> SysStatus:
        """ execute the step operations, if fail, rollback and retry """
        all_status = SysStatus.DONE
        for step_repeat_time in range(0, self.repeat_times):
            Step._print_to_screen(
                msg=UserMsg.STEP_START_TEMPLATE.format(self.step_num, self.repeat_times, step_repeat_time))
            for op in self.operations:
                op_status = op.all_stage_run()
                if op_status != SysStatus.SUCCESS:
                    rollback_status = op.rollback()
                    if rollback_status == SysStatus.SUCCESS:
                        op_status = op.all_stage_run()
                        if op_status != SysStatus.SUCCESS:
                            all_status = op_status
                            break
                    else:
                        all_status = op_status
                        break
            Step._print_to_screen(msg=UserMsg.STEP_END_TEMPLATE.format(self.step_num), code=all_status)
        self.status = all_status
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

    @staticmethod
    def _print_to_screen(msg: str, code=SysStatus.SUCCESS, level=MsgLevel.INFO):
        bus.emit(event=EventName.SCREEN_PRINT_EVENT,
                 msg=Msg(msg=msg, source=MsgEndpoint.STEP, destinations=[MsgEndpoint.USER_TERMINAL],
                         code=code, level=level))

    def __str__(self):
        return self.step_num

    def __repr__(self):
        return self.step_num
