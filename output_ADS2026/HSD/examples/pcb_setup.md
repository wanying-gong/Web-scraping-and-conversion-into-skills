<!-- 来源: examples\pcb_setup.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../index.md)
* [Examples](index.md)
* Setup a Printed Circuit Board (PCB)

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
  + Setup a Printed Circuit Board (PCB)
  + [Setup a design for Memory Designer](sample_design.md)

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

On this page

[Previous

Examples](index.md)
[Next

Setup a design for Memory Designer](sample_design.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top