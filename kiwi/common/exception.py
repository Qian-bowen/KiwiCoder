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


class ModuleNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return repr("module {} not found".format(self.name))


class ClassNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return repr("class {} not found".format(self.name))


class ToBeImplementException(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return repr("{} has not been implemented yet".format(self.name))


class MethodNotExistException(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return repr("Method {} does not exist".format(self.name))


class AttributeNotExistException(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return repr("Attribute {} does not exist".format(self.name))


class PeripheryOpException(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return repr("Exception occurs in periphery of operation {}".format(self.name))


class BioObjNotExistException(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return repr("Bio object with name {} does not exist. Or its name is not specified.".format(self.name))






