from .wrapper import *
from kiwi.core.bio_quantity import Volume
from kiwi.common.constant import AutoLevel, PCRType


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


def centrifuge(container: Container, speed: Speed, temp: Temperature, time: Time):
    """ Performs centrifugation of given container at the specified temperature, speed and time. """
    pass


def centrifuge_flow_through(column: Column, speed: Speed, temp: Temperature, time: Time, container: Container):
    """  Performs centrifugation of given column at the specified temperature and for the specified duration of time.
    The column is discarded and the flow-through is left in the collection tube, container. """
    pass


def thermocycler(plate: Plate, pcr_type: PCRType):
    """ Programs the thermocycler with the appropriate values to carry out a specific type of PCR. """
    pass

def thermocycler_anneal(container: Container, ):
    pass

