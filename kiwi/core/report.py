from pathlib import Path

from kiwi.util.graph import DAG


class ReportGen:
    def __init__(self):
        self.dependency_graph = DAG()

    def add_dependency_graph(self, dependency_graph: DAG):
        self.dependency_graph = dependency_graph

    def gen_graph_topology_file(self, filename: str) -> None:
        """ export dot file, visualize the graph """
        f = Path(filename+".dot").open("w+")
        f.write("digraph G{\n")
        f.write("  graph [ dpi = 300 ];\n")
        f.write("  size=\"8.5,10.25\";\n")
        for u in self.dependency_graph.graph:
            f.write("{} [label=\"{}\" color=blue];\n".format(u.key, u.name))
            for v in self.dependency_graph.graph[u]:
                f.write("{} -> {};\n".format(u.key, v.key))
        f.write("}\n")
        f.close()

    def gen_html_report_file(self) -> None:
        pass
