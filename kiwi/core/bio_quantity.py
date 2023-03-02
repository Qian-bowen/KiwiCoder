from abc import abstractmethod

from .bio_obj import BioObject


class Quantity(BioObject):
    def __init__(self, value: float, unit_denote: str):
        super().__init__()
        self.value = value
        self.unit_denote = unit_denote

    @abstractmethod
    def std_value(self) -> float:
        """ return value in common unit in bio experiments """
        pass


class Volume(Quantity):
    def __init__(self, value: float, unit_denote: str):
        super().__init__(value, unit_denote)

    def std_value(self) -> float:
        if self.unit_denote == "ml":
            return self.value
        elif self.unit_denote == "ul":
            return self.value * 0.001


class Speed(Quantity):
    pass


class Temperature(Quantity):
    ON_ICE = 0.0
    ON_BOIL = 100.0

    def __init__(self, temp: float):
        super().__init__(value=temp, unit_denote="dc")
        self.temp = temp

    def std_value(self) -> float:
        return self.temp


class Time(Quantity):
    pass
