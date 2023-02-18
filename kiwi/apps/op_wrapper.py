from .wrapper import *
from kiwi.core.bio_periphery import InstrumPeriphery
from kiwi.core.bio_quantity import Volume
from kiwi.common.constant import AutoLevel

def start_protocol(_comment: str):
    pass


def end_protocol():
    pass


def comment(_comment: str):
    pass


def measure_fluid(measure_instrum: InstrumPeriphery, from_container: Container, to_container: Container, vol: Volume, auto_level=AutoLevel.FULL):
    """ measures out a fluid into another fluid """
    Wrapper(vol=vol, measure_instrum=measure_instrum, drivers=[], auto_level=auto_level, wrapper_type=ConstWrapper.OP_MEASURE_FLUID_WRAPPER)


def inoculation():
    pass


def centrifuge_pellet():
    pass
