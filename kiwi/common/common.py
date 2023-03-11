import inspect
import sys
import uuid
from functools import wraps
from json import JSONEncoder
from types import MappingProxyType
from typing import Callable, Any

from kiwi.util.graph import DAG

from kiwi.common import SysStatus
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
        print("types when call:{}".format(types))
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
                print("types when register:{}".format(types))
            types.append(parm.annotation)
        self.type_map[tuple(types)] = method
        print("types when register:{}".format(types))


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


def watch_change(watch_list: [str]):
    """ monitor the class attributes, and call _watch method in class when change """
    watch_attr_set = set(attr for attr in watch_list)

    def __decorator__(cls):

        _sentinel = object()
        cls_setattr = getattr(cls, '__setattr__', None)
        cls_watch = getattr(cls, '_watch', None)
        if cls_watch is None:
            raise MethodNotExistException("_watch")

        def __setattr__(self, name, value):
            if name in watch_attr_set:
                old_value = getattr(self, name, _sentinel)
                if old_value is not _sentinel and old_value != value:
                    cls_watch(self, name, old_value, value)
            cls_setattr(self, name, value)

        cls.__setattr__ = __setattr__
        return cls

    return __decorator__


# ==================================== #
#           Encoder/Decoder            #
# ==================================== #
not_serializable = "$$"


class CustomJSONEncoder(JSONEncoder):

    def default(self, o: Any) -> Any:
        print(type(o))
        if isinstance(o, uuid.UUID):
            return str(o)
        if isinstance(o, SysStatus):
            return int(o)
        if isinstance(o, MappingProxyType):
            return o.copy()
        else:
            return JSONEncoder.default(self, o)
