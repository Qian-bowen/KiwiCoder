import pytest
from kiwi.apps import KiwiCoder, Step


def test_app_config():
    kiwi = KiwiCoder()

    Step("step 1", "sn:1")
    Step("step 1.1", "sn:1.1")
    Step("step 1.2", "sn:1.2")
    Step("step 2", "sn:2")
    Step("step 2.1", "sn:2.1")
    Step("step 2.1.1", "sn:2.1.1")

    kiwi.run()
