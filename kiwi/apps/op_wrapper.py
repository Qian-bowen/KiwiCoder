from .wrapper import *


def attach(attach_spec: str):
    def __outer_wrapper__(func):
        def __inner_wrapper__(*args, **kwargs):
            return func(*args, **kwargs)

        return __inner_wrapper__

    return __outer_wrapper__


def mock():
    def __outer_wrapper__(func):
        def __inner_wrapper__(*args, **kwargs):
            return func(*args, **kwargs)

        return __inner_wrapper__

    return __outer_wrapper__


def measure_fluid(from_container: Container, to_container: Container, vol: Vol):
    """ measures out a fluid into another fluid"""
