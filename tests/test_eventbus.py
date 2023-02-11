from kiwi.util import EventBus

bus = EventBus()


def safe_print(*args, sep=" ", end="", **kwargs):
    joined_string = sep.join([str(arg) for arg in args])
    print(joined_string + "\n", sep=sep, end=end, **kwargs)


@bus.on('hello')
def subscribe_event_bus(a, b):
    safe_print('world', a, b)


def test_event_bus():
    safe_print('Hello')
    for i in range(10):
        bus.emit('hello', a=i, b=2, block=False)
