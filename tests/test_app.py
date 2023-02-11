import pytest
from kiwi.apps import KiwiCoder, Step, Vol, Container, measure_fluid, MeasureHardware
from kiwi.hardware import FlowMeter


def test_app_config():
    kiwi = KiwiCoder()

    Step("step 1", "sn:1")

    container1 = Container()
    container2 = Container()
    flow_meter = MeasureHardware()
    measure_fluid(flow_meter, container1, container2, Vol())

    Step("step 1.1", "sn:1.1")
    Step("step 1.2", "sn:1.2")
    Step("step 2", "sn:2")
    Step("step 2.1", "sn:2.1")
    Step("step 2.1.1", "sn:2.1.1")

    kiwi.run()


def config():
    """connector attach, e.g pcr:chan1->container:2"""
    pass


class MockFlowMeter:
    def read(self):
        print("\nmock in class")


def test_mocked_func():
    mock_fm = MockFlowMeter()
    fm = FlowMeter(mock_obj=mock_fm)
    print("\n ----init finish-------")
    fm.set_mock_um(True)
    fm.read()
    fm.set_mock_um(False)
    fm.read()
    pass
