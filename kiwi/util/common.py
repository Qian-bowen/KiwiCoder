import inspect
import sys
from functools import wraps


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


def with_defer(func):
    @wraps(func)
    def __wrap__(*args, **kwargs):
        __defers__ = DefersContainer()
        with __defers__:
            return func(*args, **kwargs)

    return __wrap__
