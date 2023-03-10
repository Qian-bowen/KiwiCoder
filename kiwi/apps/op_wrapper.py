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
    Wrapper(protocol_name=protocol_name, wrapper_type=ConstWrapper.OP_START_PROTOCOL_WRAPPER)


def end_protocol():
    Wrapper(wrapper_type=ConstWrapper.OP_END_PROTOCOL_WRAPPER)


def comment(content: str):
    Wrapper(content=content, wrapper_type=ConstWrapper.OP_COMMENT_WRAPPER)


def do_nothing():
    """ Do nothing and wait until receive signal """
    Wrapper(wrapper_type=ConstWrapper.OP_DO_NOTHING_WRAPPER)


# ==================================== #
#      3. Measuring out materials      #
# ==================================== #

@multimethod(Fluid, Container, Volume, AutoLevel)
def measure_fluid(fluid: Fluid, container: Container, vol: Volume, auto_level: AutoLevel = AutoLevel.FULL):
    """ Measures out a specified volume of fluid into the given container. """
    Wrapper(fluid=fluid, container=container, vol=vol, auto_level=auto_level,
            wrapper_type=ConstWrapper.OP_MEASURE_FLUID_WRAPPER)


@multimethod(Fluid, Container, AutoLevel)
def measure_fluid(fluid: Fluid, container: Container, auto_level: AutoLevel = AutoLevel.FULL):
    """ Measures out fluid into the specified container. """
    Wrapper(fluid=fluid, container=container, vol=None, auto_level=auto_level,
            wrapper_type=ConstWrapper.OP_MEASURE_FLUID_WRAPPER)


# ==================================== #
#        4. Combination/mixing         #
# ==================================== #
def combine(auto_level: AutoLevel = AutoLevel.FULL):
    """ Combines the contents of the given containers. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def vortex(container: Container, auto_level: AutoLevel = AutoLevel.FULL):
    """ Mixes the contents of the given container by vortexing the container for a few seconds. """
    Wrapper(container=container, auto_level=auto_level, wrapper_type=ConstWrapper.OP_VORTEX_WRAPPER)


def tap(container: Container, auto_level: AutoLevel = AutoLevel.FULL):
    """ Mixes the contents of the given container by tapping the container for a few seconds. """
    Wrapper(container=container, auto_level=auto_level, wrapper_type=ConstWrapper.OP_TAP_WRAPPER)


def dissolve(container: Container, auto_level: AutoLevel = AutoLevel.FULL):
    """ Dissolves the contents of the solution in tube. """
    Wrapper(container=container, auto_level=auto_level, wrapper_type=ConstWrapper.OP_DISSOLVE_WRAPPER)


# ==================================== #
#        5.Temperature change          #
# ==================================== #


def thermocycler(plate: Plate, pcr_type: PCRType, auto_level: AutoLevel = AutoLevel.FULL):
    """ Programs the thermocycler with the appropriate values to carry out a specific type of PCR. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def thermocycler_anneal(container: Container, cool_to_temp: Temperature, gradient: Temperature, time: Time,
                        auto_level: AutoLevel = AutoLevel.FULL):
    """ Programs the thermocycler with the appropriate values for annealing the primers with the template according
    to the specified gradient and sends the contents of the specified container for thermocycling. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def store_for(container: Container, temp: Temperature, time: Time, auto_level: AutoLevel = AutoLevel.FULL):
    """ Stores the specified container at a given temperature and given duration of time. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def store_until(container: Container, temp: Temperature, until_event: UntilType, time: Time, auto_level: AutoLevel = AutoLevel.FULL):
    """ Stores the specified container at a given temperature until the occurence of a specified event. The
    approximate time taken for the occurence of the event is also specified. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
#              6. Storage              #
# ==================================== #
def wait(container: Container, time: Time, auto_level: AutoLevel = AutoLevel.FULL):
    """ Holds the given container for the specified unit of time. """
    # TODO: LOCK container when wait
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def store(container: Container, temp: Temperature, auto_level: AutoLevel = AutoLevel.FULL):
    """ Stores the specified container at a given temperature. """
    Wrapper(container=container, temp=temp, auto_level=auto_level, wrapper_type=ConstWrapper.OP_STORE_WRAPPER)


# ==================================== #
#           7. Centrifugation          #
# ==================================== #


def centrifuge(container: Container, speed: Speed, temp: Temperature, time: Time, auto_level: AutoLevel = AutoLevel.FULL):
    """ Performs centrifugation of given container at the specified temperature, speed and time. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def centrifuge_pellet(container: Container, speed: Speed, temp: Temperature, time: Time, auto_level: AutoLevel = AutoLevel.FULL):
    """ Performs centrifugation of given container at the specified temperature, speed and time and yields a pellet.
    The supernatant is discarded. """
    Wrapper(container=container, speed=speed, temp=temp, time=time, auto_level=auto_level,
            wrapper_type=ConstWrapper.OP_CENTRIFUGE_PELLET_WRAPPER)


def centrifuge_flow_through(column: Column, speed: Speed, temp: Temperature, time: Time, container: Container,
                            auto_level: AutoLevel = AutoLevel.FULL):
    """  Performs centrifugation of given column at the specified temperature and for the specified duration of time.
    The column is discarded and the flow-through is left in the collection tube, container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
#             8. Disposal              #
# ==================================== #

def discard(container: Container, auto_level: AutoLevel = AutoLevel.FULL):
    """ Discards the contents of the specified container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def drain(container: Container, auto_level: AutoLevel = AutoLevel.FULL):
    """ Drains the specified container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
#   9. Transfer of fluid and columns   #
# ==================================== #

def transfer(from_container: Container, to_container: Container, auto_level: AutoLevel = AutoLevel.FULL):
    """ Transfers the contents of a container to another specified container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


def transfer_column(column: Column, container: Container, auto_level: AutoLevel = AutoLevel.FULL):
    """ Transfers the contents of a container to another specified container. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
# 11. Detection/separation/techniques  #
# ==================================== #
def sequencing(container: Container, auto_level: AutoLevel = AutoLevel.FULL):
    """ Prompts the user to send the sample for sequencing after diluting to appropriate concentration. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass


# ==================================== #
#   12. Column-specific instructions   #
# ==================================== #

def add_to_column(column: Column, container: Container, auto_level: AutoLevel = AutoLevel.FULL):
    """ Adds the contents of container to the specified column. """
    raise ToBeImplementException(inspect.currentframe().f_code.co_name)
    pass
