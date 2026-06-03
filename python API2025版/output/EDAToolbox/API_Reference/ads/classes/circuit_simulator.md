<!-- 来源: API_Reference\ads\classes\circuit_simulator.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../../../index.md)
* [API Reference](../../index.md)
* [ADS](../index.md)
* [Classes](index.md)
* CircuitSimulator

1.2.4

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../../_sources/API_Reference/ads/classes/circuit_simulator.rst.txt)

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

* [API Reference](../../index.md)
  + [ADS](../index.md)
    - [Functions](../functions/index.md)
    - [Classes](index.md)
      * [ADS](ads.md)
      * CircuitSimulator
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
  + [Multi Python API](../../multi_python/index.md)
    - [Functions](../../multi_python/functions/index.md)
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

# CircuitSimulator[](#circuitsimulator "Link to this heading")

*class* keysight.edatoolbox.ads.CircuitSimulator(*hpeesof\_dir=None*)[](#keysight.edatoolbox.ads.CircuitSimulator "Link to this definition")
:   run(*commandline: str | List[str]*, *working\_dir: str = None*)[](#keysight.edatoolbox.ads.CircuitSimulator.run "Link to this definition")
    :   Run the circuit simulator with given commandline, for instance ‘-h’

        Parameters:
        :   **commandline** (*Union**[**str**,* *List**[**str**]**]*) – Either a well-formed string or a list of strings (=recommended). The list of strings is then passed on to the circuit simulator.

        Returns:
        :   * *Returns a tuple with as first value the return code of the process. The second part of the tuple is the output collected on stdout/err from*
            * *the circuit simulator.*

        Example

        ```
        >>> CircuitSimulator().run(['-h','R'])
        ```

    run\_netlist(*netlist: str*, *output\_dir: str*, *working\_dir: str = None*, *output\_file: str = None*, *netlist\_file: str = None*, *rel\_data\_dir: str = None*, *dataset\_name: str = None*, *verilog\_dir: str = None*, *pdk\_dirs: List[str] = None*, *extra\_args: List[str] = None*)[](#keysight.edatoolbox.ads.CircuitSimulator.run_netlist "Link to this definition")
    :   Run the provided netlist through the circuit simulator.

        Parameters:
        :   * **netlist** (*str*) – The netlist to run
            * **output\_dir** (*str*) – Where the data should be produced
            * **working\_dir** (*str*) – The optional working dir where the circuit simulator should be started, otherwise the current.
            * **output\_file** (*str*) – Optionally specify the output file where all output from the circuit simulator should be collected. Can be used to extract additional
              information from the run. Otherwise a temporary file is created.
            * **netlist\_file** (*str*) – Optionally specify in which file the netlist will be temporary stored before handing it over to the circuit simulator. If not specified a
              temporary file is created.
            * **rel\_data\_dir** (*str*) – The specification of the data directory where the circuit simulator can pick up additional files specified in the netlist.
            * **dataset\_name** (*str*) – The name of the dataset to save to. Name overrides the default name specified in the netlist.
            * **verilog\_dir** (*str*) – The specification of the verilog directory where the circuit simulator can pick up additional VerilogA files specified in the netlist.
            * **pdk\_dirs** (*List**[**str**]*) – The specification of the PDK directories where the circuit simulator can pick up additional PDK files specified in the netlist. A list of absolute paths is recommended.
            * **extra\_args** (*List**[**str**]*) – Optional list of arguments to pass to the circuit simulator, typically left empty

On this page

[Previous

ADS](ads.md)
[Next

Circuit API](../../circuit/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top