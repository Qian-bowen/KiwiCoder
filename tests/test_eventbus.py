from kiwi.util import EventBus

bus = EventBus()

@bus.on('hello')
def subscribe_event_bus():
    print('world')

def test_event_bus():
    print('Hello')
    bus.emit('hello', block=True)