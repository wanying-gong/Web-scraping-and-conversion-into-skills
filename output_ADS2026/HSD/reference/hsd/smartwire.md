<!-- 来源: reference\hsd\smartwire.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.hsd](index.md)
* Smart Wire

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

* [Introduction](../../intro/index.md)
  + [Using Visual Studio Code](../../intro/vscode.md)
* [Reference](../index.md)
  + [keysight.ads.hsd](index.md)
    - [Core](core.md)
    - [Metadata](metadata.md)
    - Smart Wire
  + [keysight.ads.hsd.memory](memory/index.md)
    - [Memory Setup](memory/setup.md)
    - [Memory Pre-layout](memory/prelayout.md)
    - [Memory Printed Circuit Board (PCB)](memory/pcb.md)
    - [Memory Bus T-Line](memory/bus_tline.md)
    - [Memory Bus Designer](memory/bus_designer.md)
    - [Memory Controller](memory/ddr_controller.md)
    - [Memory DRAM](memory/ddr_memory.md)
    - [Memory Interface Simulator](memory/simulator.md)
    - [Memory Probe](memory/probe.md)
    - [Memory Termination](memory/ddr_termination.md)
    - [Memory IO Component](memory/io_component.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
  + [How to Use Pytest](../../howto/pytest.md)
* [Examples](../../examples/index.md)
  + [Setup a Printed Circuit Board (PCB)](../../examples/pcb_setup.md)
  + [Setup a design for Memory Designer](../../examples/sample_design.md)

# Smart Wire[](#smart-wire "Link to this heading")

## Functions[](#functions "Link to this heading")

keysight.ads.hsd.smart\_wire.auto\_connect(*from\_instance: Instance | Term*, *to\_instance: Instance | Term*) → bool[](#keysight.ads.hsd.smart_wire.auto_connect "Link to this definition")
:   Auto connect a smart component or term to a smart component or term.

    Two terms will raise an exception.

keysight.ads.hsd.smart\_wire.custom\_connect(*from\_instance: Instance | Term*, *to\_instance: Instance | Term*, *from\_port\_names: list[str]*, *to\_port\_names: list[str]*) → bool[](#keysight.ads.hsd.smart_wire.custom_connect "Link to this definition")
:   Custom connect a smart component or term to a smart component or term with the port name lists that should be connected.

    Port name list can be empty if it is associated with a term. Otherwise, the port name lists must be the same length.
    If the port name lists are not the same length, InvalidCustomConnectPortNamesError with be raised.
    Two terms will raise an exception.

On this page

[Previous

Metadata](metadata.md)
[Next

keysight.ads.hsd.memory](memory/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top