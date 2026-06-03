<!-- 来源: Initial_Setup\installation.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Initial Setup](index.md)
* Installation

1.2.4

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Initial_Setup/installation.rst.txt)

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
* [Initial Setup](index.md)
  + Installation
  + [Prerequisites](prerequisites.md)
  + [Verifying Installation](verifying.md)
  + [SSH](ssh.md)
* [Examples](../Examples/index.md)
* [How-To](../How-To/index.md)
  + [Create a Circuit](../How-To/circuit.md)
  + [Run a Circuit Simulation](../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../How-To/sipro.md)
* [Release Notes](../release_notes/index.md)

# Installation[](#installation "Link to this heading")

These instructions describe how to use `pip` to install the EDA Toolbox.

Warning

These instructions assume you are using a standard Python distribution from [python.org](https://www.python.org). Python 3.10.x is the recommended installation to use.

On Linux:

```
pip install /path/to/wheelfile/keysight.edatoolbox-1.2.1-py3-none-any.whl
```

On Windows, Python is often installed through `py` allowing to select a particular version and acts as jump station to the various Python installation available on the system.

```
py -m pip install c:\path\to\wheelfile\keysight.edatoolbox-1.2.s1-py3-none-any.whl
```

The wheel files can be downloaded here: [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

## Installing in xxPro distribution[](#installing-in-xxpro-distribution "Link to this heading")

The EDA Toolbox can be installed in any generic Python distribution, but also be inside the Python distribution of EMPro or SIPro for that matter. That may be necessary if you
want to combine the capabilities of both. Some example scripts show how to do that and in those cases it is recommended to install the Toolbox into the distribution of xxPro.

Installing into the xxPro distribution starts with making sure you are using the Python of the xxPro distribution.

If you have ADS 2023 or more recent, open a terminal/command prompt and:

```
C:\Program Files\Keysight\ADS2025\fem\2025.00\win32_64\bin\emproenv.bat
```

On Linux start a bash shell under the xxPro environment:

```
/path/to/emproenv.sh bash
```

After you have done that, you can again use the pip installation procedure. Note that on Windows andyou will need to use python instead of py, on Linux use python:

```
python -m pip install c:\path\to\wheelfile\keysight.edatoolbox-1.2.1-py3-none-any.whl
```

```
python -m pip install /path/to/wheelfile/keysight.edatoolbox-1.2.1-py3-none-any.whl
```

### Examples[](#examples "Link to this heading")

The examples can be found on the [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

On this page

[Previous

Initial Setup](index.md)
[Next

Prerequisites](prerequisites.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top