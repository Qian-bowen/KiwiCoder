import inspect

from .wrapper import *
from kiwi.core.bio_quantity import Volume, Temperature, Time, Speed
from kiwi.core.bio_entity import Container, Column, Fluid
from kiwi.common.constant import AutoLevel, PCRType, UntilType
from kiwi.common import multimethod, ToBeImplementException
from kiwi.core.bio_entity import Plate


# ==================================== #
#      1. Writing a new protocol       #
# ==================================== #


def start_protocol(protocol_name: str):
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def end_protocol():
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def comment(content: str):
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def do_nothing():
    """ Do nothing and wait until receive signal """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
#      3. Measuring out materials      #
# ==================================== #

@multimethod(Container, Container, Volume, AutoLevel)
def measure_fluid(from_container: Container, to_container: Container, vol: Volume, auto_level=AutoLevel.FULL):
    """ Measures out container's into another specified container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


@multimethod(Fluid, Container, Volume, AutoLevel)
def measure_fluid(fluid: Fluid, container: Container, vol: Volume, auto_level=AutoLevel.FULL):
    """ Measures out a specified volume of fluid into the given container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


@multimethod(Fluid, Container, AutoLevel)
def measure_fluid(fluid: Fluid, container: Container, auto_level=AutoLevel.FULL):
    """ Measures out fluid into the specified container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
#        4. Combination/mixing         #
# ==================================== #
def combine(auto_level=AutoLevel.FULL):
    """ Combines the contents of the given containers. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def vortex(container: Container, auto_level=AutoLevel.FULL):
    """ Mixes the contents of the given container by vortexing the container for a few seconds. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def tap(container: Container, auto_level=AutoLevel.FULL):
    """ Mixes the contents of the given container by tapping the container for a few seconds. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def dissolve(container: Container, auto_level=AutoLevel.FULL):
    """ Dissolves the contents of the solution in tube. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
#        5.Temperature change          #
# ==================================== #


def thermocycler(plate: Plate, pcr_type: PCRType, auto_level=AutoLevel.FULL):
    """ Programs the thermocycler with the appropriate values to carry out a specific type of PCR. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def thermocycler_anneal(container: Container, cool_to_temp: Temperature, gradient: Temperature, time: Time,
                        auto_level=AutoLevel.FULL):
    """ Programs the thermocycler with the appropriate values for annealing the primers with the template according
    to the specified gradient and sends the contents of the specified container for thermocycling. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def store_for(container: Container, temp: Temperature, time: Time, auto_level=AutoLevel.FULL):
    """ Stores the specified container at a given temperature and given duration of time. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def store_until(container: Container, temp: Temperature, until_event: UntilType, time: Time, auto_level=AutoLevel.FULL):
    """ Stores the specified container at a given temperature until the occurence of a specified event. The
    approximate time taken for the occurence of the event is also specified. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
#              6. Storage              #
# ==================================== #
def wait(container: Container, time: Time, auto_level=AutoLevel.FULL):
    """ Holds the given container for the specified unit of time. """
    # TODO: LOCK container when wait
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def store(container: Container, temp: Temperature, auto_level=AutoLevel.FULL):
    """ Stores the specified container at a given temperature. """
    Wrapper(container=container, temp=temp, auto_level=auto_level, wrapper_type=ConstWrapper.OP_STORE_WRAPPER)


# ==================================== #
#           7. Centrifugation          #
# ==================================== #


def centrifuge(container: Container, speed: Speed, temp: Temperature, time: Time, auto_level=AutoLevel.FULL):
    """ Performs centrifugation of given container at the specified temperature, speed and time. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def centrifuge_pellet(container: Container, speed: Speed, temp: Temperature, time: Time, auto_level=AutoLevel.FULL):
    """ Performs centrifugation of given container at the specified temperature, speed and time and yields a pellet.
    The supernatant is discarded. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def centrifuge_flow_through(column: Column, speed: Speed, temp: Temperature, time: Time, container: Container,
                            auto_level=AutoLevel.FULL):
    """  Performs centrifugation of given column at the specified temperature and for the specified duration of time.
    The column is discarded and the flow-through is left in the collection tube, container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
#             8. Disposal              #
# ==================================== #

def discard(container: Container, auto_level=AutoLevel.FULL):
    """ Discards the contents of the specified container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def drain(container: Container, auto_level=AutoLevel.FULL):
    """ Drains the specified container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
#   9. Transfer of fluid and columns   #
# ==================================== #

def transfer(from_container: Container, to_container: Container, auto_level=AutoLevel.FULL):
    """ Transfers the contents of a container to another specified container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def transfer_column(column: Column, container: Container, auto_level=AutoLevel.FULL):
    """ Transfers the contents of a container to another specified container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
# 11. Detection/separation/techniques  #
# ==================================== #
def sequencing(container: Container, auto_level=AutoLevel.FULL):
    """ Prompts the user to send the sample for sequencing after diluting to appropriate concentration. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
#   12. Column-specific instructions   #
# ==================================== #

def add_to_column(column: Column, container: Container, auto_level=AutoLevel.FULL):
    """ Adds the contents of container to the specified column. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass
