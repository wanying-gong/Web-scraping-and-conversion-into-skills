<!-- 来源: reference\hsd\core.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.hsd](index.md)
* Core

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
    - Core
    - [Metadata](metadata.md)
    - [Smart Wire](smartwire.md)
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

# Core[](#core "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.DesignParameters[](#keysight.ads.hsd.DesignParameters "Link to this definition")
:   Bases: `MutableMapping`[`str`, `str`]

    A dictionary-like wrapper for design parameters that supports item assignment.

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.DesignParameters.get "Link to this definition")

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.DesignParameters.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.DesignParameters.keys "Link to this definition")

    update([*E*, ]*\*\*F*) → None.  Update D from mapping/iterable E and F.[](#keysight.ads.hsd.DesignParameters.update "Link to this definition")
    :   If E present and has a .keys() method, does: for k in E.keys(): D[k] = E[k]
        If E present and lacks .keys() method, does: for (k, v) in E: D[k] = v
        In either case, this is followed by: for k, v in F.items(): D[k] = v

    values() → an object providing a view on D's values[](#keysight.ads.hsd.DesignParameters.values "Link to this definition")

On this page

[Previous

keysight.ads.hsd](index.md)
[Next

Metadata](metadata.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top