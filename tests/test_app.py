import pytest
from kiwi.apps import KiwiCoder, Step, Vol, Container, measure_fluid, attach, mock


def test_app_config():
    kiwi = KiwiCoder()

    Step("step 1", "sn:1")

    container1 = Container()
    container2 = Container()
    measure_fluid(container1, container2, Vol())

    Step("step 1.1", "sn:1.1")
    Step("step 1.2", "sn:1.2")
    Step("step 2", "sn:2")
    Step("step 2.1", "sn:2.1")
    Step("step 2.1.1", "sn:2.1.1")

    kiwi.run()

def config():
    """connector attach, e.g pcr:chan1->container:2"""
    pass

@mock
def mocked_func():
    pass
