<!-- 来源: howto\pytest.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../index.md)
* [How-To](index.md)
* How to Use Pytest

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
* [How-To](index.md)
  + [How to Set Up a Python Virtual Environment](venv.md)
    - [Creating a new Python virtual environment based on ADS Python](newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)
  + How to Use Pytest
* [Examples](../examples/index.md)
  + [Setup a Printed Circuit Board (PCB)](../examples/pcb_setup.md)
  + [Setup a design for Memory Designer](../examples/sample_design.md)

# How to Use Pytest[](#how-to-use-pytest "Link to this heading")

Pytest is a mature full-featured testing tool for Python. It is useful when developing Python scripts.
Pytest is not installed in the ADS Python installation.

The recommended steps to use Pytest are:

> 1. Create a Python virtual environment. See [How to Set Up a Python Virtual Environment](venv.md).
> 2. Activate the Python virtual environment.
> 3. Install pytest into the virtual environment.
>
>    > ```
>    > pip install pytest
>    > ```
> 4. Run pytest on your test scripts.
>
>    > ```
>    > cd path/to/tests
>    > pytest
>    > ```

On this page

[Previous

Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)
[Next

Examples](../examples/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top