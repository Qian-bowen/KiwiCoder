from kiwi.core import InstrumPeriphery
import copy


class Anneal(InstrumPeriphery):
    def __init__(self, primers, template, limit):
        super().__init__()
        self.primers = primers
        self.template = copy.deepcopy(template)
        self.limit = limit
        self.products = None

    def start(self):
        pass

    def shutdown(self):
        pass

    def produce(self):
        return self.products

    def measure(self):
        pass
