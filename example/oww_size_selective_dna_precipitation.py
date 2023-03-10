from build.lib.kiwi.apps.op_wrapper import dissolve
from kiwi.core.bio_quantity import Speed, Temperature, Time

from kiwi import Volume
from kiwi.apps.op_wrapper import measure_fluid, tap, vortex, centrifuge_pellet, comment, start_protocol, end_protocol

from kiwi.apps.wrapper import Step

from kiwi.common.constant import ContainerType

from kiwi.core.bio_entity import Fluid, Container


def kiwi_protocol():
    start_protocol("Chromosomal DNA isolation from E.coli")
    dna = Fluid("DNA sample", "DNA to be separated (e.g. PCR reaction mixture)")
    peg = Fluid("PEG/MgCl2", "30% (w/v) PEG 8000/30 mM MgCl2 (concentration of PEG 8000 can be varied to shift the "
                             "size of the percipitated DNA. The concentration used here will remove DNA fragments "
                             "with less than 300bp)")
    te = Fluid("TE buffer", "10 mM TRIS-HCl, 1 mM EDTA, pH 8.0")
    buffer = Fluid("buffer of choice")
    eppendorf = Container(ContainerType.EPPENDORF)

    Step("step 1", "sn:1")
    measure_fluid(dna, eppendorf, Volume(50, "ul"))
    measure_fluid(te, eppendorf, Volume(150, "ul"))
    tap(eppendorf)

    Step("step 2", "sn:2")
    measure_fluid(peg, eppendorf, Volume(10, "ul"))

    Step("step 3", "sn:3")
    vortex(eppendorf)

    Step("step 4", "sn:4")
    centrifuge_pellet(eppendorf, Speed(10000, "G"), Temperature(Temperature.ROOM), Time(15, "mins"))
    end_protocol()

    Step("step 5", "sn:5")
    comment("Carefully remove supernatant not to disturb the pellet, which will be invisible.")

    Step("step 6", "sn:6")
    measure_fluid(buffer, eppendorf)
    comment("Add appropriate volume of buffer.")
    dissolve(eppendorf)


