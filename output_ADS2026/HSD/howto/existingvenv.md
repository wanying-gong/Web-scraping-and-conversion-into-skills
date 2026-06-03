<!-- 来源: howto\existingvenv.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../index.md)
* [How-To](index.md)
* [How to Set Up a Python Virtual Environment](venv.md)
* Installing Keysight ADS wheels into an existing Python virtual environment

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
    - Installing Keysight ADS wheels into an existing Python virtual environment
  + [How to Use Pytest](pytest.md)
* [Examples](../examples/index.md)
  + [Setup a Printed Circuit Board (PCB)](../examples/pcb_setup.md)
  + [Setup a design for Memory Designer](../examples/sample_design.md)

# Installing Keysight ADS wheels into an existing Python virtual environment[](#installing-keysight-ads-wheels-into-an-existing-python-virtual-environment "Link to this heading")

1. Open a console window and load an existing virtual environment

   > The existing venv must have been created from a Python installation with the same major and minor Python version as ADS.
2. Navigate to the ADS wheelhouse directory

   > Example for Linux:
   >
   > ```
   > cd $HPEESOF_DIR/tools/python/wheelhouse
   > ```
   >
   > Example for Windows:
   >
   > ```
   > cd %HPEESOF_DIR%\tools\python\wheelhouse
   > ```
3. Install packages with pip requirements file

   > Example for Linux:
   >
   > ```
   > python3 -m pip install -r venv_requirements.txt --no-index --no-cache-dir --only-binary=:all: --find-links=.
   > ```
   >
   > Example for Windows:
   >
   > ```
   > python -m pip install -r venv_requirements.txt --no-index --no-cache-dir --only-binary=:all: --find-links=.
   > ```
4. To verify packages have been installed
   :   Example for Linux:

       ```
       python3 -m pip list
       ```

       Example for Windows:

       ```
       python -m pip list
       ```

       You should see various keysight-ads-\* wheels listed

On this page

[Previous

Creating a new Python virtual environment based on ADS Python](newvenv.md)
[Next

How to Use Pytest](pytest.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top