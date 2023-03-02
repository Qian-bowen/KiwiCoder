from kiwi.util.graph import DAG


class Watcher:
    def __init__(self):
        self.dependency_graph = None

    def add_dependency_graph(self, dependency_graph: DAG):
        self.dependency_graph = dependency_graph

    def print_graph_topology(self) -> str:
        """ export dot file, visualize the graph """
        pass

    def encode_graph_topology(self) -> str:
        pass


