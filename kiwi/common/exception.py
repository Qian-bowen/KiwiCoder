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


class TypeErrorException(Exception):
    def __init__(self, expect_type, actual_type):
        self.expect_type = str(expect_type)
        self.actual_type = str(actual_type)

    def __str__(self):
        return "expect type:{}, actual type:{}".format(self.expect_type, self.actual_type)
