from abc import abstractmethod

from .bio_obj import BioObject


class Periphery(BioObject):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass


class SimplAmplifier(Periphery):
    def start(self):
        pass

    def shutdown(self):
        pass
