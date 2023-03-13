from kiwi.common import class_mock_enable
from kiwi.core import SignalPeriphery, ControlPeriphery


@class_mock_enable
class Pump(SignalPeriphery):
    def __init__(self, control_periphery: ControlPeriphery, mock=False, mock_obj=None):
        super().__init__(control_periphery=control_periphery, mock=mock, mock_obj=mock_obj)

    def start(self):
        self.attach_to.set_signal(self.id)

    def shutdown(self):
        self.attach_to.unset_signal(self.id)

