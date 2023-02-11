from .bio_obj import BioObject


class Quantity(BioObject):
    def __init__(self, value: float, unit_denote: str):
        super().__init__()
        self.value = value
        self.unit_denote = unit_denote

    def std_value(self) -> float:
        pass


class Volume(Quantity):
    def __init__(self, value: float, unit_denote: str):
        super().__init__(value, unit_denote)

    def std_value(self) -> float:
        pass
