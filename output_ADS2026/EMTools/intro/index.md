<!-- 来源: intro\index.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [EM Tools Python Documentation](../index.md)
* Introduction

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

* Introduction
* [Reference](../reference/index.md)
  + [keysight.ads.emtools](../reference/emtools.md)
* [Examples](../examples/index.md)
  + [RFPro Examples](../examples/rfpro/index.md)
    - [Create RFPro View](../examples/rfpro/ex_create_rfpro_view.md)
    - [Get the Substrate from an EM Setup View](../examples/rfpro/ex_get_emsetup_substrate_info.md)
    - [Convert EM Setup to RFPro View](../examples/rfpro/ex_convert_emsetup_to_rfpro_view.md)
  + [PEPro Examples](../examples/pepro/index.md)
    - [Creates a new pepro View](../examples/pepro/ex_create_pepro_view.md)
    - [Run existing PEPro analysis persent in workspace.](../examples/pepro/ex_run_pepro_sim.md)
    - [Creates a new selected nets type analysis in pepro View and run the simulation.](../examples/pepro/ex_create_and_run_selected_nets_analysis.md)
    - [Creates a new pe thermal analysis in pepro View and run the simulation.](../examples/pepro/ex_create_and_run_thermal_analysis.md)

# Introduction[](#introduction "Link to this heading")

A Python script can access functionality needed to work with the EM tools in ADS.

```
from keysight.ads import emtools
```

The `keysight.ads.emtools` package is not currently available as a pip-installable package.
To get access to this package, use any one of these approaches:

> 1. Use the Python interpreter in `$HPEESOF_DIR/tools/python`.
> 2. Create a virtual environment based on that interpreter.
> 3. Add `$HPEESOF_DIR/tools/python/packages` onto your Python’s `sys.path`.

Set the environment variable `HPEESOF_DIR` to point to your ADS installation prior to
using the `keysight.ads.emtools` package.

On this page

[Previous

EM Tools Python Documentation](../index.md)
[Next

Reference](../reference/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top