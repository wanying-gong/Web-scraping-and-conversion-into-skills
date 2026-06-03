<!-- 来源: examples\sample_design.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../index.md)
* [Examples](index.md)
* Setup a design for Memory Designer

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../intro/index.md)
  + [Using Visual Studio Code](../intro/vscode.md)
* [Reference](../reference/index.md)
  + [keysight.ads.hsd](../reference/hsd/index.md)
    - [Core](../reference/hsd/core.md)
    - [Metadata](../reference/hsd/metadata.md)
    - [Smart Wire](../reference/hsd/smartwire.md)
  + [keysight.ads.hsd.memory](../reference/hsd/memory/index.md)
    - [Memory Setup](../reference/hsd/memory/setup.md)
    - [Memory Pre-layout](../reference/hsd/memory/prelayout.md)
    - [Memory Printed Circuit Board (PCB)](../reference/hsd/memory/pcb.md)
    - [Memory Bus T-Line](../reference/hsd/memory/bus_tline.md)
    - [Memory Bus Designer](../reference/hsd/memory/bus_designer.md)
    - [Memory Controller](../reference/hsd/memory/ddr_controller.md)
    - [Memory DRAM](../reference/hsd/memory/ddr_memory.md)
    - [Memory Interface Simulator](../reference/hsd/memory/simulator.md)
    - [Memory Probe](../reference/hsd/memory/probe.md)
    - [Memory Termination](../reference/hsd/memory/ddr_termination.md)
    - [Memory IO Component](../reference/hsd/memory/io_component.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
  + [How to Use Pytest](../howto/pytest.md)
* [Examples](index.md)
  + [Setup a Printed Circuit Board (PCB)](pcb_setup.md)
  + Setup a design for Memory Designer

# Setup a design for Memory Designer[](#setup-a-design-for-memory-designer "Link to this heading")

This example demonstrates how to setup a design for a simulation using HSD’s Memory Designer.

If you are unfamiliar with how to [create a workspace and a library](../../../de/html/pypde/docs/examples/design_creation/ex_workspace.md)
or [create a schematic](../../../de/html/pypde/docs/examples/design_creation/ex_create_schematic.md), please review those examples first.

Then, import the required modules.

```
import keysight.ads.de as de

from keysight.ads.hsd import smart_wire
from keysight.ads.hsd.memory import pcb
from keysight.ads.hsd.memory.controller import NonIbisController as MemoryController
from keysight.ads.hsd.memory.memory import NonIbisMemory as MemoryDram
from keysight.ads.hsd.memory.probe import Probe
from keysight.ads.hsd.memory.probe import ProbeFlowType

```

Then, add Memory\_Interface\_Simulator, MD\_Setup, DDR\_PCB, DDR\_Controller, DDR\_Memory, and Memory\_Probe to the design.

```
        sim_inst = design.add_instance(
            ["ads_simulation", "Memory_Interface_Simulator", "symbol"],
            (-0.625, 6.125),
            name="Memory_Interface_Simulator1",
        )
        setup_inst = design.add_instance(["ads_simulation", "MD_Setup", "symbol"], (-7.750, 6.125), name="MD_Setup")

        pcb_inst = design.add_instance(["ads_simulation", "DDR_PCB", "symbol"], (0.000, 0.000), name="DDR_PCB1")
        controller_inst = design.add_instance(
            ["ads_sources", "DDR_Controller", "symbol"], (-7.750, 0.000), name="DDR_Controller1"
        )
        memory_inst = design.add_instance(
            ["ads_simulation", "DDR_Memory", "symbol"], (7.750, 0.000), name="DDR_Memory1"
        )

        probe_inst = design.add_instance(
            ["ads_simulation", "Memory_Probe", "symbol"], (6.375, 5.125), name="Memory_Probe"
        )
```

Then, setup the PCB.

```
        pcb_editor = pcb.PCBEditor(pcb_inst)
        pcb_editor.setup_with_datafile("dummy.s20p")  # Replace with actual data file path
        pcb_editor.read_metadata_from_csv_file("dummy.csv")  # Replace with actual CSV file path
        pcb_editor.save_change()
```

Then, setup the Controller.

```
        controller = MemoryController(controller_inst)
        controller.initialize_ref_des_from = "DDR_PCB1"
        controller.ref_des["U1"].include = True
        for pin_data in controller.pin:
            pin_data.simulate = True
```

Then, setup the DRAM.

```
        dram = MemoryDram(memory_inst)
        dram.initialize_ref_des_from = "DDR_PCB1"
        dram.ref_des["U60"].include = True
        for pin_data in dram.pin:
            pin_data.simulate = True
```

Then, connect the Controller and DRAM to the PCB.

```
        smart_wire.auto_connect(controller_inst, pcb_inst)
        smart_wire.auto_connect(memory_inst, pcb_inst)
```

Finally, setup the Probe.

```
        probe = Probe(probe_inst)
        probe.flow_type = ProbeFlowType.MEASUREMENT
        select_signal_list = [signal_key for signal_key in probe.available_signals if "U60" in signal_key]
        probe.add_signals(select_signal_list)
        measurement_list = ["Eye", "Eye Height and Width"]
        probe.add_measurements(select_signal_list, measurement_list)
```

On this page

[Previous

Setup a Printed Circuit Board (PCB)](pcb_setup.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top