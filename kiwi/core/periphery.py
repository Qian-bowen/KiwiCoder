from abc import ABC, abstractmethod

class Periphery(ABC):

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