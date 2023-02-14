from Phidget22.Devices.DigitalOutput import DigitalOutput
from kiwi.core import ControlPeriphery

from threading import Timer, Lock


class PhidgetRelay(ControlPeriphery):
    def __init__(self, vintport, channel, hold_duty=1.0, hit_delay=0.2, mock=False, mock_obj=None):
        super().__init__(mock=mock, mock_obj=mock_obj)
        self.rly = DigitalOutput()
        self.rly.setHubPort(vintport)
        self.rly.setChannel(channel)
        self.rly.openWaitForAttachment(5000)
        self.lock = Lock()
        self.state = False  # false -> closed, true->open, or duty>0%
        self.hit_delay = hit_delay
        self.hold_duty = hold_duty
        self.t = Timer(0, None)

    def start(self):
        pass

    def shutdown(self):
        pass

    def set_signal(self, bio_id: int):
        def _hold():
            with self.lock:
                if self.state:
                    self.rly.setDutyCycle(self.hold_duty)

        with self.lock:
            self.rly.setDutyCycle(1.0)
            self.state = True

        # set hold_duty after hit_delay seconds
        self.t = Timer(self.hit_delay, _hold)
        self.t.start()

    def unset_signal(self, bio_id: int):
        with self.lock:
            self.t.cancel()
            self.rly.setDutyCycle(0.0)
            self.rly.state = False

    def set_signal_with_value(self, bio_id: int, val: float):
        pass
