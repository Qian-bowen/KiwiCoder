from .wrapper import *
from kiwi.core.bio_quantity import Volume
from kiwi.common.constant import AutoLevel


# ==================================== #
#        Protocol Framework            #
# ==================================== #

def start_protocol(protocol_name: str):
    pass


def end_protocol():
    pass


def comment(content: str):
    pass


def repeat(times: int):
    pass


def measure_fluid(from_container: Container, to_container: Container, vol: Volume, auto_level=AutoLevel.FULL):
    """ measures out a fluid into another fluid """
    Wrapper(vol=vol, measure_instrum=measure_instrum, drivers=[], auto_level=auto_level,
            wrapper_type=ConstWrapper.OP_MEASURE_FLUID_WRAPPER)


def transfer(from_container: Container, to_container: Container, vol: Volume, auto_level=AutoLevel.FULL):
    pass


def inoculation():
    pass


def centrifuge_pellet():
    pass
