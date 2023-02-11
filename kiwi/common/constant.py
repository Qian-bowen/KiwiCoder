class ConstWrapper:
    BASE_WRAPPER = 0
    STEP_WRAPPER = 1


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


class MsgEndpoint:
    OP = "op"
    STEP = "step"
    WATCH = "watch"


class EventName:
    OP_EVENT = "event:op"
    STEP_EVENT = "event:step"
    FATAL_ALARM_EVENT = "event:fatal_alarm"
