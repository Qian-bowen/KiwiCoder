from .bio_obj import BioObject
from kiwi.common import ContainerType
from .bio_quantity import Temperature, Volume


class Container(BioObject):
    def __init__(self, container_type: ContainerType, name=None, fluid=None):
        super().__init__(name=name)


class Column(Container):
    pass


class Slide(Container):
    pass


class Fluid(BioObject):
    def __init__(self, name: str, state=None, temp=None, volume=None):
        super().__init__()
        self.temp = temp
        self.volume = volume


class Solid(Fluid):
    pass


class Plate(Solid):
    pass


class Tissue(Solid):
    pass


