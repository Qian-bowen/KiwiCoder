class NodeNotFoundException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ParseParamException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

