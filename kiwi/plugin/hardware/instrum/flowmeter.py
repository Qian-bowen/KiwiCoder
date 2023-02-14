from kiwi.core import MeasureInstrumPeriphery
from kiwi.common import class_mock_enable
from typing import Optional


@class_mock_enable
class FlowMeter(MeasureInstrumPeriphery):
    def __init__(self, mock=False, mock_obj=None):
        super().__init__(mock=mock, mock_obj=mock_obj)

    def read(self) -> Optional[float]:
        print("\nfm read")
        return

    def __mock_read__(self) -> Optional[float]:
        print("\nfm mock read")
        return

    def start(self):
        pass

    def shutdown(self):
        pass
