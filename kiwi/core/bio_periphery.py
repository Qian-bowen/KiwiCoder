from abc import abstractmethod
from typing import Optional
from time import sleep

from .bio_obj import BioObject


class Periphery(BioObject):
    def __init__(self, mock=False, mock_obj=None):
        super().__init__(mock=mock, mock_obj=mock_obj)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass


class ControlPeriphery(Periphery):
    """ center hardware that controls other periphery, e.g. Raspberry Pi"""

    def __init__(self, mock=False, mock_obj=None):
        super().__init__(mock=mock, mock_obj=mock_obj)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass


class InstrumPeriphery(Periphery):
    """ bio instruments, e.g. PCR """

    def __init__(self, mock=False, mock_obj=None):
        super().__init__(mock=mock, mock_obj=mock_obj)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass


class DriverPeriphery(Periphery):
    def __init__(self, mock=False, mock_obj=None):
        super().__init__(mock=mock, mock_obj=mock_obj)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass


# ==================================== #
#        Specific instrum              #
# ==================================== #

class MeasureInstrumPeriphery(InstrumPeriphery):
    def __init__(self, mock=False, mock_obj=None):
        super().__init__(mock=mock, mock_obj=mock_obj)

    def start(self):
        pass

    def shutdown(self):
        pass

    def read(self) -> Optional[float]:
        pass

    def accumulate_read(self, target: float, times_in_second: int, interval: float = 0.1) -> Optional[float]:
        accumulate = 0.0
        last_measured = self.read()
        while accumulate < target:
            measured = self.read()
            if measured is None:
                continue
            measure_delta = (((last_measured + measured) / 2) * interval) / times_in_second
            accumulate += measure_delta
            last_measured = measured
            sleep(interval)
        return accumulate
