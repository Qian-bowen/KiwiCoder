class ConstWrapper:
    BASE_WRAPPER = 0
    STEP_WRAPPER = 1

    OP_WRAPPER = 10
    OP_MEASURE_FLUID_WRAPPER = 11

    ENTITY_WRAPPER = 1000

    @staticmethod
    def is_op_wrapper(wrapper_type: int):
        return ConstWrapper.OP_WRAPPER <= wrapper_type < ConstWrapper.ENTITY_WRAPPER


class SysStatus:
    FAIL = 0
    SUCCESS = 1

    INIT = 100
    AVAILABLE = 101
    RUNNING = 102
    PENDING = 103
    DONE = 104


class MsgLevel:
    GOSSIP = 0
    INFO = 1
    IMPORTANT = 2
    WARN = 3
    ERROR = 4
    FATAL = 5

    @staticmethod
    def to_string(level: int) -> str:
        ret = ""
        if level == 0:
            ret = "GOSSIP"
        elif level == 1:
            ret = "INFO"
        elif level == 2:
            ret = "IMPORTANT"
        elif level == 3:
            ret = "WARN"
        elif level == 4:
            ret = "ERROR"
        elif level == 5:
            ret = "FATAL"
        return ret


class MsgEndpoint:
    OP = "op"
    STEP = "step"
    WATCH = "watch"
    USER_TERMINAL = "user_terminal"


class EventName:
    OP_EVENT = "event:op"
    OP_SIGNAL_RECEIVE_EVENT = "event:op:{}:sig:receive"
    STEP_EVENT = "event:step"
    FATAL_ALARM_EVENT = "event:fatal_alarm"
    SCREEN_PRINT_EVENT = "event:screen:print"


class AutoLevel:
    HUMAN = 0
    SEMI = 1
    FULL = 2


class SysSignal:
    STOP = 0
    RUN = 1
    SUSPEND = 2
    KILL = 3
    CONTINUE = 4


class ScheduleMode:
    SEQ = 0
    GRAPH = 1


class UserMsg:
    OP_OPERATE_HUMAN = "This operation requires human. Send 'Continue' signal when finish."
    OP_STAGE_START_TEMPLATE = "Step:{} Operation:{} Stage:{} begin."
    OP_STAGE_END_TEMPLATE = "Step:{} Operation:{} Stage:{} finish."


class Config:
    OUTPUT_MSG_BUFFER_SIZE = 100
