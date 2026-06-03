<!-- 来源: API_Reference\xxpro\index.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../../index.md)
* [API Reference](../index.md)
* xxPro

1.2.4

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/API_Reference/xxpro/index.rst.txt)

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

* [API Reference](../index.md)
  + [ADS](../ads/index.md)
    - [Functions](../ads/functions/index.md)
    - [Classes](../ads/classes/index.md)
      * [ADS](../ads/classes/ads.md)
      * [CircuitSimulator](../ads/classes/circuit_simulator.md)
  + [Circuit API](../circuit/index.md)
    - [Functions](../circuit/functions/index.md)
    - [Classes](../circuit/classes/index.md)
      * [Circuit](../circuit/classes/circuit.md)
      * [Definition](../circuit/classes/definition.md)
      * [Instance](../circuit/classes/instance.md)
      * [Node](../circuit/classes/node.md)
      * [OptimizationRange](../circuit/classes/optimization_range.md)
      * [TuningRange](../circuit/classes/tuning_range.md)
      * [Value](../circuit/classes/value.md)
  + [Dataset](../dataset/index.md)
  + [External API](../extra/index.md)
    - [empro.analysis](../extra/empro/index.md)
  + [Multi Python API](../multi_python/index.md)
    - [Functions](../multi_python/functions/index.md)
  + xxPro
* [Initial Setup](../../Initial_Setup/index.md)
  + [Installation](../../Initial_Setup/installation.md)
  + [Prerequisites](../../Initial_Setup/prerequisites.md)
  + [Verifying Installation](../../Initial_Setup/verifying.md)
  + [SSH](../../Initial_Setup/ssh.md)
* [Examples](../../Examples/index.md)
* [How-To](../../How-To/index.md)
  + [Create a Circuit](../../How-To/circuit.md)
  + [Run a Circuit Simulation](../../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../../How-To/sipro.md)
* [Release Notes](../../release_notes/index.md)

# xxPro[](#module-keysight.edatoolbox.xxpro "Link to this heading")

*exception* keysight.edatoolbox.xxpro.XXProNotFound[](#keysight.edatoolbox.xxpro.XXProNotFound "Link to this definition")
:   Raise if cannot find SI/PI/RFPro.

keysight.edatoolbox.xxpro.get\_python\_xxpro\_location(*from\_ads=True*) → str[](#keysight.edatoolbox.xxpro.get_python_xxpro_location "Link to this definition")
:   Returns the location of the python installed with xxPro.

    Parameters:
    :   **from\_ads** (*bool**,* *default=True*) – If True get xxPro from ADS install folder, otherwise look for EMPROHOME environment variable.

keysight.edatoolbox.xxpro.get\_xxpro\_location(*from\_ads=True*) → str[](#keysight.edatoolbox.xxpro.get_xxpro_location "Link to this definition")
:   Returns the location of the latest installed xxPro.

    Parameters:
    :   **from\_ads** (*bool**,* *default=True*) – If True get xxPro from ADS install folder, otherwise look for EMPROHOME environment variable.

keysight.edatoolbox.xxpro.load\_pro\_view(*xxpro\_lcv: LibraryCellView*)[](#keysight.edatoolbox.xxpro.load_pro_view "Link to this definition")
:   Load an xxpro LibraryCellView into the empro.activeProject.

    Parameters:
    :   **xxpro\_lcv** (*LibraryCellView*) – An xxpro LibraryCellView object.

    Raises:
    :   **ImportError** – Failed to import empro module.

keysight.edatoolbox.xxpro.use\_workspace(*workspace: str*)[](#keysight.edatoolbox.xxpro.use_workspace "Link to this definition")
:   Tell xxpro what workspace to use.

    Parameters:
    :   **workspace** (*str*) – The full path of the workspace.

On this page

[Previous

Functions](../multi_python/functions/index.md)
[Next

Initial Setup](../../Initial_Setup/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top