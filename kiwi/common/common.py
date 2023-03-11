import inspect
import sys
from functools import wraps
from typing import Callable, Any

from kiwi.common import MathOp
from kiwi.common.exception import MethodNotExistException


# ==================================== #
#          Python decorator            #
# ==================================== #

def defer(x):
    for f in inspect.stack():
        if '__defers__' in f[0].f_locals:
            f[0].f_locals['__defers__'].append(x)
            break


class DefersContainer(object):
    def __init__(self):
        # List for sustain refer in shallow clone
        self.defers = []

    def append(self, defer):
        self.defers.append(defer)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        __suppress__ = []
        for d in reversed(self.defers):
            try:
                d()
            except:
                __suppress__ = []
                exc_type, exc_value, traceback = sys.exc_info()
        return __suppress__


def with_defer(func) -> Callable:
    @wraps(func)
    def __wrap__(*args, **kwargs):
        __defers__ = DefersContainer()
        with __defers__:
            return func(*args, **kwargs)

    return __wrap__


def singleton(cls):
    _instance = {}

    def __wrapper__(*args, **kw):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kw)
        return _instance[cls]

    return __wrapper__


def class_mock_enable(cls_t):
    """
    enable all functions in class can be mocked
    function end with _um, means that it can not be mocked
    """

    def __mock_decorator__(cls, func) -> Callable:

        @wraps(func)
        def __inner__(*args, **kwargs):
            is_mock = cls.mock
            mock_obj = cls.mock_obj

            if is_mock is False:
                return func(*args, **kwargs)
            else:
                func_name = func.__name__
                if mock_obj is not None:
                    call_func = getattr(mock_obj, func_name)
                    call_func(*args, **kwargs)
                else:
                    call_func = getattr(cls, "__mock_" + func_name + "__")
                    call_func(*args, **kwargs)

        return __inner__

    def __decorator__(*args, **kwarg):
        cls = cls_t(*args, **kwarg)
        for obj in dir(cls):
            member = getattr(cls, obj)
            if callable(member) and not obj.startswith("__") and not obj.endswith("_um"):
                setattr(cls, obj, __mock_decorator__(cls=cls, func=member))
        return cls

    return __decorator__


def sort_default(origin_list: []):
    origin_list.sort()


registry = {}


class MultiMethod(object):
    def __init__(self, name):
        self.name = name
        self.type_map = {}

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args)
        # print("types when call:{}".format(types))
        function = self.type_map.get(types, None)
        if function is None:
            raise TypeError("no match")
        return function(*args)

    def register(self, method):
        sig = inspect.signature(method)
        types = []
        for name, parm in sig.parameters.items():
            if parm.default is not inspect.Parameter.empty:
                self.type_map[tuple(types)] = method
                # print("types when register:{}".format(types))
            types.append(parm.annotation)
        self.type_map[tuple(types)] = method
        # print("types when register:{}".format(types))


def multimethod(*types):
    """ support overload for python function """

    def register(function):
        function = getattr(function, "__lastreg__", function)
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethod(name)
        mm.register(function)
        mm.__lastreg__ = function
        return mm

    return register


def watch_change(watch_list: [str] = None, alarm_list: [(str, MathOp, Any)] = None):
    """
    monitor the class attributes, and call _watch method in class when change.
    call _alarm when attribute change exceeds the threshold.
    alarm_list is composed of list of tuple, with name, math operation and threshold value
    """

    def __decorator__(cls):
        # print("type:{} watch list:{} alarm list:{}".format(type(cls), watch_list, alarm_list))
        watch_attr_set = set()
        alarm_attr_dict = dict()
        if watch_list is not None:
            watch_attr_set = set(attr for attr in watch_list)
        if alarm_list is not None:
            for alarm_raw in alarm_list:
                alarm_attr_dict[alarm_raw[0]] = (alarm_raw[1], alarm_raw[2])

        _sentinel = object()
        cls_setattr = getattr(cls, '__setattr__', None)
        cls_watch = getattr(cls, '_watch', None)
        cls_alarm = getattr(cls, '_alarm', None)
        cls_watch_set = getattr(cls, 'watch_set', None)
        cls_alarm_dict = getattr(cls, 'alarm_dict', None)
        if cls_watch_set is None:
            setattr(cls, 'watch_set', set())
            cls_watch_set = getattr(cls, 'watch_set', None)
        if cls_alarm_dict is None:
            setattr(cls, 'alarm_dict', dict())
            cls_alarm_dict = getattr(cls, 'alarm_dict', None)

        for elem in watch_attr_set:
            cls_watch_set.add(elem)
        for k, v in alarm_attr_dict.items():
            cls_alarm_dict[k] = v

        setattr(cls, 'watch_set', cls_watch_set)
        setattr(cls, 'alarm_dict', cls_alarm_dict)
        # print("after set:{} dict:{}".format(cls_watch_set, cls_alarm_dict))

        def __setattr__(self, name, value):
            # print("runtime set:{} dict:{}".format(cls.watch_set, cls.alarm_dict))
            if name in cls.watch_set:
                old_value = getattr(self, name, _sentinel)
                if old_value is not _sentinel and old_value != value:
                    if cls_watch is None:
                        raise MethodNotExistException("_watch")
                    cls_watch(self, name, old_value, value)
            if name in cls.alarm_dict:
                math_op = cls.alarm_dict[name][0]
                threshold_value = cls.alarm_dict[name][1]
                if MathOp.compare(value, threshold_value, math_op):
                    if cls_alarm is None:
                        raise MethodNotExistException("_alarm")
                    cls_alarm(self, name, value, threshold_value, math_op)
            cls_setattr(self, name, value)

        cls.__setattr__ = __setattr__
        return cls

    return __decorator__

