<!-- 来源: intro\vscode.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../index.md)
* [Introduction](index.md)
* Using Visual Studio Code

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

* [Introduction](index.md)
  + Using Visual Studio Code
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
* [Examples](../examples/index.md)
  + [Setup a Printed Circuit Board (PCB)](../examples/pcb_setup.md)
  + [Setup a design for Memory Designer](../examples/sample_design.md)

# Using Visual Studio Code[](#using-visual-studio-code "Link to this heading")

To invoke VS-Code from DDS:

> 1. In DDS, execute the menu "Tools->VS-Code.."
> 2. In VS-Code, execute the menu "View->Command Palette…"
> 3. Type the command "Python:Select Interpreter"
> 4. Set the python interpreter by browsing to $HPEESOF\_DIR\tools\python\python.exe (python3 for linux)

To use a python virtual environment instead of the ADS python installation:

> 1. Set up a python virtual environment. see [How to Set Up a Python Virtual Environment](../howto/venv.md)
> 2. Repeat steps 1-3 above
> 3. Set the python interpreter by browsing to the python executable in the virtual environment.

On this page

[Previous

Introduction](index.md)
[Next

Reference](../reference/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top