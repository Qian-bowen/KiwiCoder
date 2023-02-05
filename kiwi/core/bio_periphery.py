from abc import abstractmethod

from .bio_obj import BioObject


class Periphery(BioObject):
    def __init__(self, mock=False):
        super().__init__(mock=mock)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass


class ControlPeriphery(Periphery):
    def __init__(self, mock=False):
        super().__init__(mock=mock)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass


class InstrumPeriphery(Periphery):
    def __init__(self, mock=False):
        super().__init__(mock=mock)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass

    @abstractmethod
    def produce(self):
        pass

    @abstractmethod
    def measure(self):
        pass
