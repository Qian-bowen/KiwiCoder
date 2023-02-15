from .wrapper import *


def start_protocol(_comment: str):
    pass


def end_protocol():
    pass


def comment(_comment: str):
    pass


def measure_fluid(measure_instrum: MeasureHardware, from_container: Container, to_container: Container, vol: Vol):
    """ measures out a fluid into another fluid"""
    Wrapper(vol=vol, measure_instrum=measure_instrum, drivers=[], wrapper_type=ConstWrapper.OP_MEASURE_FLUID_WRAPPER)


def inoculation():
    pass


def centrifuge_pellet():
    pass
