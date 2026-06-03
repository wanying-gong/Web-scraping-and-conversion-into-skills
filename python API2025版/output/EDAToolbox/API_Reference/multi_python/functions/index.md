<!-- 来源: API_Reference\multi_python\functions\index.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../../../index.md)
* [API Reference](../../index.md)
* [Multi Python API](../index.md)
* Functions

1.2.4

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../../_sources/API_Reference/multi_python/functions/index.rst.txt)

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

* [API Reference](../../index.md)
  + [ADS](../../ads/index.md)
    - [Functions](../../ads/functions/index.md)
    - [Classes](../../ads/classes/index.md)
      * [ADS](../../ads/classes/ads.md)
      * [CircuitSimulator](../../ads/classes/circuit_simulator.md)
  + [Circuit API](../../circuit/index.md)
    - [Functions](../../circuit/functions/index.md)
    - [Classes](../../circuit/classes/index.md)
      * [Circuit](../../circuit/classes/circuit.md)
      * [Definition](../../circuit/classes/definition.md)
      * [Instance](../../circuit/classes/instance.md)
      * [Node](../../circuit/classes/node.md)
      * [OptimizationRange](../../circuit/classes/optimization_range.md)
      * [TuningRange](../../circuit/classes/tuning_range.md)
      * [Value](../../circuit/classes/value.md)
  + [Dataset](../../dataset/index.md)
  + [External API](../../extra/index.md)
    - [empro.analysis](../../extra/empro/index.md)
  + [Multi Python API](../index.md)
    - Functions
  + [xxPro](../../xxpro/index.md)
* [Initial Setup](../../../Initial_Setup/index.md)
  + [Installation](../../../Initial_Setup/installation.md)
  + [Prerequisites](../../../Initial_Setup/prerequisites.md)
  + [Verifying Installation](../../../Initial_Setup/verifying.md)
  + [SSH](../../../Initial_Setup/ssh.md)
* [Examples](../../../Examples/index.md)
* [How-To](../../../How-To/index.md)
  + [Create a Circuit](../../../How-To/circuit.md)
  + [Run a Circuit Simulation](../../../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../../../How-To/sipro.md)
* [Release Notes](../../../release_notes/index.md)

# Functions[](#functions "Link to this heading")

keysight.edatoolbox.multi\_python.xxpro\_context(*python\_xxpro\_location=None*)[](#keysight.edatoolbox.multi_python.xxpro_context "Link to this definition")
:   Create a context manager that will yield an object to which functions can be sent to be executed in a separate process with the Python version of EMPro/RFPro/SIPro.

    Args:
    :   python\_xxpro\_location (str): The location of the Python executable to use for xxPro (=directory, not the location to the executable).
        :   If not provided, the default Python executable for xxPro will be used

    Usage:

    ```
    >>> with xxpro_context() as caller:
    ...     result = caller.call(my_function, args=[1,2], kwargs={'a':3})
    ```

keysight.edatoolbox.multi\_python.ads\_context(*python\_ads\_location=None*)[](#keysight.edatoolbox.multi_python.ads_context "Link to this definition")
:   Create a context manager that will yield an object to which functions can be sent to be executed in a separate process with the Python version of ADS.

    Args:
    :   python\_ads\_location (str): The location of the Python executable to use for ADS (=directory, not the location to the executable).
        :   If not provided, the default Python executable for ADS will be used.

    Usage:

    ```
    >>> with ads_context() as caller:
    ...     result = caller.call(my_function, args=[1,2], kwargs={'a':3})
    ```

On this page

[Previous

Multi Python API](../index.md)
[Next

xxPro](../../xxpro/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top