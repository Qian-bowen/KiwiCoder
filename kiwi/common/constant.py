from enum import Enum


class ConstWrapper:
    BASE_WRAPPER = 0
    STEP_WRAPPER = 1

    OP_WRAPPER = 10
    OP_MEASURE_FLUID_WRAPPER = 11

    ENTITY_WRAPPER = 1000
    ENTITY_CONTAINER_WRAPPER = 1001
    ENTITY_FLUID_WRAPPER = 1002

    QUANTITY_WRAPPER = 1800
    QUANTITY_VOL_WRAPPER = 1801

    PERIPHERY_WRAPPER = 2000
    PERIPHERY_CONTROL_WRAPPER = 2001
    PERIPHERY_INSTRUM_WRAPPER = 2002
    PERIPHERY_SIGNAL_WRAPPER = 2003

    @staticmethod
    def is_op_wrapper(wrapper_type: int) -> bool:
        return ConstWrapper.OP_WRAPPER <= wrapper_type < ConstWrapper.ENTITY_WRAPPER

    @staticmethod
    def is_quantity_wrapper(wrapper_type: int) -> bool:
        return ConstWrapper.QUANTITY_WRAPPER <= wrapper_type < ConstWrapper.PERIPHERY_WRAPPER


class SysStatus(Enum):
    FAIL = 0
    SUCCESS = 1

    INIT = 100
    AVAILABLE = 101
    RUNNING = 102
    PENDING = 103
    DONE = 104


class MsgLevel(Enum):
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
    SYS = "sys"


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


class ScheduleMode(Enum):
    SEQ = 0
    GRAPH = 1


class UserMsg:
    OP_OPERATE_HUMAN_TEMPLATE = "This operation(step:{} op:{}) requires human. Send 'Continue' signal when finish."
    OP_STAGE_START_TEMPLATE = "Step:{} Operation:{} Stage:{} begin."
    OP_STAGE_END_TEMPLATE = "Step:{} Operation:{} Stage:{} finish."
    STEP_START_TEMPLATE = "Step:{} begin."
    STEP_END_TEMPLATE = "Step:{} finish."


class Config:
    OUTPUT_MSG_BUFFER_SIZE = 100
