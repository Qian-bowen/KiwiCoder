# ==================================== #
#           Encoder/Decoder            #
# ==================================== #
import uuid
from json import JSONEncoder
from types import MappingProxyType
from typing import Any

from kiwi.common.constant import SysStatus

not_serializable = "$$"


class CustomJSONEncoder(JSONEncoder):

    def default(self, o: Any) -> Any:
        print(type(o))
        if isinstance(o, uuid.UUID):
            return str(o)
        elif isinstance(o, SysStatus):
            return int(o)
        elif isinstance(o, MappingProxyType):
            return o.copy()
        else:
            return JSONEncoder.default(self, o)