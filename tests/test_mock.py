from threading import Thread

from kiwi.apps import KiwiCoder, Step, Container, measure_fluid
from kiwi.core.bio_quantity import Volume
from kiwi.plugin.hardware.instrum import FlowMeter


class MockFlowMeter:
    def read(self):
        return 0.2


def test_run_kiwi():
    kiwi = KiwiCoder()

    Step("step 1", "sn:1")

    container1 = Container()
    container2 = Container()
    mock_fm = MockFlowMeter()
    fm = FlowMeter(mock_obj=mock_fm)
    measure_fluid(fm, container1, container2, Volume(1, "ml"), 1)

    Step("step 1.1", "sn:1.1")
    Step("step 1.2", "sn:1.2")
    Step("step 2", "sn:2")
    Step("step 2.1", "sn:2.1")
    Step("step 2.1.1", "sn:2.1.1")

    kiwi.run()






    cmd_thread.join()