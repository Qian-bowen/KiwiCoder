from functools import wraps

from kiwi.common import singleton
from queue import Queue
from threading import Thread
from typing import Callable, List
from collections import defaultdict


@singleton
class EventBus:
    def __init__(self, worker_num=5):
        self.events = defaultdict(set)
        self.que = Queue()
        self.worker_num = worker_num
        for i in range(self.worker_num):
            self._init_worker()

    def _init_worker(self) -> None:
        def _worker_run(que: Queue) -> None:
            while True:
                que.get()
                que.task_done()

        worker = Thread(target=_worker_run, args=(self.que,))
        worker.setDaemon(True)
        worker.start()

    def on(self, event: str) -> Callable:
        """a decorator to add an event"""

        def __outer__(func):
            self.add_event(func, event)

            @wraps(func)
            def __wrapper__(*args, **kwargs):
                return func(*args, **kwargs)

            return __wrapper__

        return __outer__

    def add_event(self, func: Callable, event: str) -> None:
        self.events[event].add(func)

    def emit(self, event: str, *args, **kwargs) -> None:
        """
        emit event and run function
        mode: block, unblock, queue
        """
        block = kwargs.pop('block', None)
        if block:
            for func in self.events[event]:
                self.que.put(Thread(target=func, args=args, kwargs=kwargs).start())
        else:
            for func in self.events[event]:
                func(*args, **kwargs)

    def emit_only(self, event: str, func_names: List[str], *args, **kwargs) -> None:
        """emit only to specific events by function name"""
        block = kwargs.pop('block', None)
        if block:
            for func in self.events[event]:
                self.que.put(Thread(target=func, args=args, kwargs=kwargs).start())
        else:
            for func in self.events[event]:
                if func.__name__ in func_names:
                    func(*args, **kwargs)

    def emit_after(self, event: str) -> Callable:
        """a decorator to emit after function finish"""

        def __outer__(func):
            @wraps(func)
            def __wrapper__(*args, **kwargs):
                return_func = func(*args, **kwargs)
                self.emit(event)
                return return_func

            return __wrapper__

        return __outer__
