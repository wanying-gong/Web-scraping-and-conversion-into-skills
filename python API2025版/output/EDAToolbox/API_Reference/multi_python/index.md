<!-- 来源: API_Reference\multi_python\index.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../../index.md)
* [API Reference](../index.md)
* Multi Python API

1.2.4

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/API_Reference/multi_python/index.rst.txt)

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
  + Multi Python API
    - [Functions](functions/index.md)
  + [xxPro](../xxpro/index.md)
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

# Multi Python API[](#multi-python-api "Link to this heading")

The multi\_python module provides the ability to run multiple Python versions in the same process. This is useful when you need to run both ADS and xxPro in the same Python session.
When you use the multi\_python module, a context for each Python version you want to run a given function in needs to be provided. Once a context is created it is alive until
the context is deleted.

To use the multi\_python module in combination with ADS and xxPro, the EDA Toolbox needs to be installed in the target environment and needs to be sufficiently recent. The EDA Toolbox multi\_python
does detect if that is the case and when it is not, it will raise an exception.

An example of how to use the multi\_python module is shown below:

```
import keysight.edatoolbox.multi_python as mp

def hello_from_xxpro():
    print("Hello from xxPro")
    return 1

def hello_from_ads():
    print("Hello from ADS")
    return 2

with mp.xxpro_context() as xxpro:
    r = xxpro.call(hello_from_xxpro)
    print(r)

with mp.ads_context() as ads:
    r = ads.call(hello_from_ads)
    print(r)
```

* [Functions](functions/index.md)
  + [`xxpro_context()`](functions/index.md#keysight.edatoolbox.multi_python.xxpro_context)
  + [`ads_context()`](functions/index.md#keysight.edatoolbox.multi_python.ads_context)

On this page

[Previous

empro.analysis](../extra/empro/index.md)
[Next

Functions](functions/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top