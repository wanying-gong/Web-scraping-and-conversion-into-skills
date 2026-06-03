<!-- 来源: API_Reference\multi_python\functions\index.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../../../index.md)
* [API Reference](../../index.md)
* [Multi Python API](../index.md)
* Functions

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../../_sources/API_Reference/multi_python/functions/index.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* [Initial Setup](../../../Initial_Setup/index.md)
  + [Installation](../../../Initial_Setup/installation.md)
  + [Prerequisites](../../../Initial_Setup/prerequisites.md)
  + [Verifying Installation](../../../Initial_Setup/verifying.md)
  + [SSH](../../../Initial_Setup/ssh.md)
* [How-To](../../../How-To/index.md)
  + [Create a Circuit](../../../How-To/circuit.md)
  + [Run a Circuit Simulation](../../../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../../../How-To/sipro.md)
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
* [Examples](../../../Examples/index.md)
  + [Running EDA Toolbox Examples](../../../Examples/Running%20Examples.md)
  + [Example baluns](../../../Examples/ex_baluns.md)
  + [Example co optimize matching network](../../../Examples/ex_co_optimize_matching_network.md)
  + [Example create 3d empro serpentines](../../../Examples/ex_create_3d_empro_serpentines.md)
  + [Example dump workspace netlists](../../../Examples/ex_dump_workspace_netlists.md)
  + [Example empro extract resonance](../../../Examples/ex_empro_extract_resonance.md)
  + [Example high pass filter sub circuit](../../../Examples/ex_high_pass_filter_sub_circuit.md)
  + [Example import brd](../../../Examples/ex_import_brd.md)
  + [Example import ipc2581](../../../Examples/ex_import_ipc2581.md)
  + [Example import odb](../../../Examples/ex_import_odb.md)
  + [Example low pass filter](../../../Examples/ex_low_pass_filter.md)
  + [Example multi python](../../../Examples/ex_multi_python.md)
  + [Example odbpp simulate pipro ac reuse sio](../../../Examples/ex_odbpp_simulate_pipro_ac_reuse_sio.md)
  + [Example odbpp simulate pipro dc](../../../Examples/ex_odbpp_simulate_pipro_dc.md)
  + [Example odbpp simulate rfpro](../../../Examples/ex_odbpp_simulate_rfpro.md)
  + [Example optimize matching network](../../../Examples/ex_optimize_matching_network.md)
  + [Example pipro ac](../../../Examples/ex_pipro_example_ac.md)
  + [Example pipro dc](../../../Examples/ex_pipro_example_dc.md)
  + [Example quantumpro one qubit epr](../../../Examples/ex_quantumpro_one_qubit_epr.md)
  + [Example quantumpro one qubit freq](../../../Examples/ex_quantumpro_one_qubit_freq.md)
  + [Example rfpro stop nets](../../../Examples/ex_rfpro_stop_nets.md)
  + [Example run hb simulation](../../../Examples/ex_run_hb_simulation.md)
  + [Example run netlist](../../../Examples/ex_run_netlist.md)
  + [Example run netlist from disk](../../../Examples/ex_run_netlist_from_disk.md)
  + [Example run schematic](../../../Examples/ex_run_schematic.md)
  + [Example sipro automation](../../../Examples/ex_sipro_automation.md)
  + [Example sipro channelsim flow](../../../Examples/ex_sipro_channelsim_flow.md)
  + [Example sipro SI](../../../Examples/ex_sipro_example_si.md)
  + [Example sipro extract tdr](../../../Examples/ex_sipro_extract_tdr.md)
  + [Example sipro eye diagram](../../../Examples/ex_sipro_eye_diagram.md)
  + [Example sipro ploteye plotly](../../../Examples/ex_sipro_ploteye_plotly.md)
  + [Example sweep inductor values](../../../Examples/ex_sweep_inductor_values.md)
  + [Example systemvue basic](../../../Examples/ex_systemvue_basic.md)
  + [Example voltage divider](../../../Examples/ex_voltage_divider.md)
  + [Example vsa meas demo](../../../Examples/ex_vsa_meas_demo.md)
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

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top