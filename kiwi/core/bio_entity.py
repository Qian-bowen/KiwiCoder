from .bio_obj import BioObject
from kiwi.common import ContainerType
from .bio_quantity import Temperature, Volume


class Container(BioObject):
    def __init__(self, container_type: ContainerType, fluid=None):
        super().__init__()


class Column(BioObject):
    pass


class Plate(BioObject):
    pass


class Fluid(BioObject):
    def __init__(self, name: str, temp=None, volume=None):
        super().__init__()
        self.temp = temp
        self.volume = volume
