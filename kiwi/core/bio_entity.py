from .bio_obj import BioObject
from kiwi.common import ContainerType, watch_change, MathOp
from .bio_quantity import Temperature, Volume


@watch_change(alarm_list=[("volume", MathOp.LE, Volume(0, "ml"))])
class Container(BioObject):
    def __init__(self, container_type: ContainerType, name="", fluid=None, volume=Volume(100, "ml")):
        super().__init__(name=name)
        self.volume = volume


class Column(Container):
    pass


class Slide(Container):
    pass


class Fluid(BioObject):
    def __init__(self, name: str, state=None, temp=None, volume=None):
        super().__init__(name=name)
        self.temp = temp
        self.volume = volume


class Solid(Fluid):
    pass


class Plate(Solid):
    pass


class Tissue(Solid):
    pass
