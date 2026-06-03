# Examples
> **说明：** Examples 相关页面。

> **何时使用：** 当你需要查阅 Examples 相关内容时

---

## 本文件目录

- **Examples** (`examples/index.md`)
- **Setup a Printed Circuit Board (PCB)** (`examples/pcb_setup.md`)
- **Setup a design for Memory Designer** (`examples/sample_design.md`)

---

<!-- === 来源: examples/index.md === -->

# Examples[](#examples "Link to this heading")

Contents:

* [Setup a Printed Circuit Board (PCB)](pcb_setup.md)
* [Setup a design for Memory Designer](sample_design.md)


---

<!-- === 来源: examples/pcb_setup.md === -->

# Setup a Printed Circuit Board (PCB)[](#setup-a-printed-circuit-board-pcb "Link to this heading")

This example demonstrates how to setup a PCB for a simulation using HSD’s Memory Designer.

If you are unfamiliar with how to [create a workspace and a library](../../../de/html/pypde/docs/examples/design_creation/ex_workspace.md)
or [create a schematic](../../../de/html/pypde/docs/examples/design_creation/ex_create_schematic.md), please review those examples first.

Then, add a PCB to the design.

```
pcb_component = design.add_instance(de.LCVName("ads_simulation", "DDR_PCB", "symbol"), (0, 0))
```

Then, create a PCB editing session.

```
pcb_edit_session = pcb.PCBEditor(pcb_component)
### Setting up the PCB with a data file
data_file_absolute_path: Path = de.active_workspace().path / "data" / "your_data_file.sio"
if pcb_edit_session.setup_with_datafile(data_file_absolute_path):
    pcb_edit_session.save_change()
```

You can setup the PCB with a data file.

```
data_file_absolute_path: Path = de.active_workspace().path / "data" / "your_data_file.sio"
if pcb_edit_session.setup_with_datafile(data_file_absolute_path):
    pcb_edit_session.save_change()
### End creating a PCBEditor object
# Showing the signal table
print(pcb_edit_session.pcb_model.metadata)
```

Alternatively, you can setup the PCB with a SIPro cell.

```
if pcb_edit_session.setup_with_sipro_cell(("example_library", "your_sipro_cell", "schematic")):
    pcb_edit_session.save_change()
# Showing the signal table
print(pcb_edit_session.pcb_model.metadata)
```


---

<!-- === 来源: examples/sample_design.md === -->

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


---

