from .wrapper import *
from kiwi.core.bio_quantity import Volume, Temperature, Time, Speed
from kiwi.core.bio_entity import Container, Column
from kiwi.common.constant import AutoLevel, PCRType, UntilType


# ==================================== #
#      1. Writing a new protocol       #
# ==================================== #
from ..core.bio_entity import Plate


def start_protocol(protocol_name: str):
    pass


def end_protocol():
    pass


def comment(content: str):
    pass


# ==================================== #
#      3. Measuring out materials      #
# ==================================== #


def measure_fluid(from_container: Container, to_container: Container, vol: Volume, auto_level=AutoLevel.FULL):
    """ measures out a fluid into another fluid """
    pass


# ==================================== #
#        4. Combination/mixing         #
# ==================================== #
def combine():
    """ Combines the contents of the given containers. """
    pass


# ==================================== #
#        5.Temperature change          #
# ==================================== #


def thermocycler(plate: Plate, pcr_type: PCRType):
    """ Programs the thermocycler with the appropriate values to carry out a specific type of PCR. """
    pass


def thermocycler_anneal(container: Container, cool_to_temp: Temperature, gradient: Temperature, time: Time):
    """ Programs the thermocycler with the appropriate values for annealing the primers with the template according
    to the specified gradient and sends the contents of the specified container for thermocycling. """
    pass


def store_for(container: Container, temp: Temperature, time: Time):
    """ Stores the specified container at a given temperature and given duration of time. """
    pass


def store_until(container: Container, temp: Temperature, until_event: UntilType, time: Time):
    """ Stores the specified container at a given temperature until the occurence of a specified event. The
    approximate time taken for the occurence of the event is also specified. """
    pass


# ==================================== #
#              6. Storage              #
# ==================================== #
def wait(container: Container, time: Time):
    """ Holds the given container for the specified unit of time. """
    # TODO: LOCK container when wait
    pass


def store(container: Container, temp: Temperature):
    """ Stores the specified container at a given temperature. """
    Wrapper(container=container, temp=temp, wrapper_type=ConstWrapper.OP_STORE_WRAPPER)


# ==================================== #
#           7. Centrifugation          #
# ==================================== #


def centrifuge(container: Container, speed: Speed, temp: Temperature, time: Time):
    """ Performs centrifugation of given container at the specified temperature, speed and time. """
    pass


def centrifuge_flow_through(column: Column, speed: Speed, temp: Temperature, time: Time, container: Container):
    """  Performs centrifugation of given column at the specified temperature and for the specified duration of time.
    The column is discarded and the flow-through is left in the collection tube, container. """
    pass


# ==================================== #
#             8. Disposal              #
# ==================================== #

def discard(container: Container):
    """ Discards the contents of the specified container. """
    pass


def drain(container: Container):
    """ Drains the specified container. """
    pass


# ==================================== #
#   9. Transfer of fluid and columns   #
# ==================================== #

def transfer(from_container: Container, to_container: Container):
    """ Transfers the contents of a container to another specified container. """
    pass


def transfer_column(column: Column, container: Container):
    """ Transfers the contents of a container to another specified container. """
    pass


# ==================================== #
# 11. Detection/separation/techniques  #
# ==================================== #
def sequencing(container: Container):
    """ Prompts the user to send the sample for sequencing after diluting to appropriate concentration. """
    pass


# ==================================== #
#   12. Column-specific instructions   #
# ==================================== #

def add_to_column(column: Column, container: Container):
    """ Adds the contents of container to the specified column. """
    pass
