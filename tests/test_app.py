import pytest
from kiwi.core import KiwiCoder,BioObject,bio_obj_mock
from abc import ABC

@bio_obj_mock
def mock_obj():


def test_app_config():
    app = KiwiCoder()
    b = BioObject

    b.is_mock()


    # BioObject b
