from pathlib import Path

from kiwi.core.step import Step

from kiwi.core.bio_periphery import Periphery

from kiwi.core.bio_quantity import Temperature

from kiwi.core.bio_entity import Fluid, Container

from kiwi.util.graph import DAG


class ReportGen:
    def __init__(self):
        self.dependency_graph = DAG()

    def add_dependency_graph(self, dependency_graph: DAG):
        self.dependency_graph = dependency_graph

    def gen_graph_topology_file(self, filename: str) -> None:
        """ export dot file, visualize the graph """
        f = Path(filename).open("w+")
        f.write("digraph G{\n")
        f.write("  graph [ dpi = 300 ];\n")
        f.write("  size=\"8.5,10.25\";\n")
        for u in self.dependency_graph.graph:
            f.write("{} [label=\"{}\" color=blue];\n".format(u.key, u.name))
            for v in self.dependency_graph.graph[u]:
                f.write("{} -> {};\n".format(u.key, v.key))
        f.write("}\n")
        f.close()

    def gen_html_report_file(self, filename: str, seq_steps: [Step], fluids: [Fluid], periphery_list: [Periphery],
                             container_list: [Container]) -> None:
        """ generate reagents, equipments and steps """
        f = Path(filename).open("w+")
        ReportGen._gen_reagents(f, fluids)
        ReportGen._gen_periphery(f, periphery_list, container_list)
        ReportGen._gen_steps(f, seq_steps)
        f.close()

    @staticmethod
    def _gen_steps(file, steps: [Step]) -> None:
        file.write("</ul><h2>Steps:</h2><ol>")
        file.write("<p><li>")
        for step in steps:
            file.write("</li></p><p><li><b><font size=3>{}</font></b><br>".format(step.name))
            for op in step.operations:
                op_text = op.get_html_text()
                file.write(op_text)

    @staticmethod
    def _gen_reagents(file, fluids: [Fluid]) -> None:
        file.write("<h2 style=\"margin-top:50px;\">Solutions/reagents:</h2><ul type=\"circle\">")
        for fluid in fluids:
            if fluid.temp is None:
                file.write("<li>{} stored at {}{}</li>".format(fluid.name, fluid.temp, 0x00B0))
            elif fluid.temp == Temperature.ON_ICE:
                file.write("<li>{}</li>".format(fluid.name))

    @staticmethod
    def _gen_periphery(file, periphery_list: [Periphery], container_list: [Container]) -> None:
        file.write("<div style=\"top: 25px; margin-top: 50px; margin-left: 700px; position: absolute; z-index: 1; "
                   "visibility: show;\">")
        file.write("<h2>Equipment:</h2><ul type=\"circle\">")
        for periphery in periphery_list:
            file.write("<li>{}</li>".format(periphery.name))
        for container in container_list:
            file.write("<li>{}</li>".format(container.name))
        file.write("</ul></div>")




