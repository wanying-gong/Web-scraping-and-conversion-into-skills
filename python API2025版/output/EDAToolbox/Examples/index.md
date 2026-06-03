<!-- 来源: Examples\index.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* Examples

1.2.4

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/index.rst.txt)

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

* [API Reference](../API_Reference/index.md)
  + [ADS](../API_Reference/ads/index.md)
    - [Functions](../API_Reference/ads/functions/index.md)
    - [Classes](../API_Reference/ads/classes/index.md)
      * [ADS](../API_Reference/ads/classes/ads.md)
      * [CircuitSimulator](../API_Reference/ads/classes/circuit_simulator.md)
  + [Circuit API](../API_Reference/circuit/index.md)
    - [Functions](../API_Reference/circuit/functions/index.md)
    - [Classes](../API_Reference/circuit/classes/index.md)
      * [Circuit](../API_Reference/circuit/classes/circuit.md)
      * [Definition](../API_Reference/circuit/classes/definition.md)
      * [Instance](../API_Reference/circuit/classes/instance.md)
      * [Node](../API_Reference/circuit/classes/node.md)
      * [OptimizationRange](../API_Reference/circuit/classes/optimization_range.md)
      * [TuningRange](../API_Reference/circuit/classes/tuning_range.md)
      * [Value](../API_Reference/circuit/classes/value.md)
  + [Dataset](../API_Reference/dataset/index.md)
  + [External API](../API_Reference/extra/index.md)
    - [empro.analysis](../API_Reference/extra/empro/index.md)
  + [Multi Python API](../API_Reference/multi_python/index.md)
    - [Functions](../API_Reference/multi_python/functions/index.md)
  + [xxPro](../API_Reference/xxpro/index.md)
* [Initial Setup](../Initial_Setup/index.md)
  + [Installation](../Initial_Setup/installation.md)
  + [Prerequisites](../Initial_Setup/prerequisites.md)
  + [Verifying Installation](../Initial_Setup/verifying.md)
  + [SSH](../Initial_Setup/ssh.md)
* Examples
* [How-To](../How-To/index.md)
  + [Create a Circuit](../How-To/circuit.md)
  + [Run a Circuit Simulation](../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../How-To/sipro.md)
* [Release Notes](../release_notes/index.md)

# Examples[](#examples "Link to this heading")

This guide will go through how to run the examples that are included in the toolbox.
We will assume that you have installed the toolbox, instructions on how to successfully do so are found in the [Initial Setup](../Initial_Setup/installation.md).

Note

Certain examples require additional python packages to be installed. Instructions on which packages, and how they can be installed, are found in the [Verifying Installation](../Initial_Setup/verifying.md) section.

Note

Certain examples require additional products to be installed, such as SystemVue or VSA.

## Get the example workspaces[](#get-the-example-workspaces "Link to this heading")

Download the example workspaces from the [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

Assume you have put these files in your “f:/temp/edatoolbox” directory.
Use a command prompt to navigate to this directory.

## Running the examples[](#running-the-examples "Link to this heading")

Next we need to choose which example to run, and where to write the output to.
Assume the output directory is “f:/temp/edatoolbox/output”.
Run the choses example using python.

```
>>> py <example>.py --output-dir=f:/temp/edatoolbox/output
```

Note

Certain examples require xxPro’s python to be used. If this is the case, make sure the toolbox and any other required packages are installed in xxPro’s distribution. And call python using `python` instead of `py`.

On this page

[Previous

SSH](../Initial_Setup/ssh.md)
[Next

How-To](../How-To/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top