<!-- 来源: API_Reference\dataset\index.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../../index.md)
* [API Reference](../index.md)
* Dataset

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/API_Reference/dataset/index.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* [Initial Setup](../../Initial_Setup/index.md)
  + [Installation](../../Initial_Setup/installation.md)
  + [Prerequisites](../../Initial_Setup/prerequisites.md)
  + [Verifying Installation](../../Initial_Setup/verifying.md)
  + [SSH](../../Initial_Setup/ssh.md)
* [How-To](../../How-To/index.md)
  + [Create a Circuit](../../How-To/circuit.md)
  + [Run a Circuit Simulation](../../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../../How-To/sipro.md)
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
  + Dataset
  + [External API](../extra/index.md)
    - [empro.analysis](../extra/empro/index.md)
  + [Multi Python API](../multi_python/index.md)
    - [Functions](../multi_python/functions/index.md)
  + [xxPro](../xxpro/index.md)
* [Examples](../../Examples/index.md)
  + [Running EDA Toolbox Examples](../../Examples/Running%20Examples.md)
  + [Example baluns](../../Examples/ex_baluns.md)
  + [Example co optimize matching network](../../Examples/ex_co_optimize_matching_network.md)
  + [Example create 3d empro serpentines](../../Examples/ex_create_3d_empro_serpentines.md)
  + [Example dump workspace netlists](../../Examples/ex_dump_workspace_netlists.md)
  + [Example empro extract resonance](../../Examples/ex_empro_extract_resonance.md)
  + [Example high pass filter sub circuit](../../Examples/ex_high_pass_filter_sub_circuit.md)
  + [Example import brd](../../Examples/ex_import_brd.md)
  + [Example import ipc2581](../../Examples/ex_import_ipc2581.md)
  + [Example import odb](../../Examples/ex_import_odb.md)
  + [Example low pass filter](../../Examples/ex_low_pass_filter.md)
  + [Example multi python](../../Examples/ex_multi_python.md)
  + [Example odbpp simulate pipro ac reuse sio](../../Examples/ex_odbpp_simulate_pipro_ac_reuse_sio.md)
  + [Example odbpp simulate pipro dc](../../Examples/ex_odbpp_simulate_pipro_dc.md)
  + [Example odbpp simulate rfpro](../../Examples/ex_odbpp_simulate_rfpro.md)
  + [Example optimize matching network](../../Examples/ex_optimize_matching_network.md)
  + [Example pipro ac](../../Examples/ex_pipro_example_ac.md)
  + [Example pipro dc](../../Examples/ex_pipro_example_dc.md)
  + [Example quantumpro one qubit epr](../../Examples/ex_quantumpro_one_qubit_epr.md)
  + [Example quantumpro one qubit freq](../../Examples/ex_quantumpro_one_qubit_freq.md)
  + [Example rfpro stop nets](../../Examples/ex_rfpro_stop_nets.md)
  + [Example run hb simulation](../../Examples/ex_run_hb_simulation.md)
  + [Example run netlist](../../Examples/ex_run_netlist.md)
  + [Example run netlist from disk](../../Examples/ex_run_netlist_from_disk.md)
  + [Example run schematic](../../Examples/ex_run_schematic.md)
  + [Example sipro automation](../../Examples/ex_sipro_automation.md)
  + [Example sipro channelsim flow](../../Examples/ex_sipro_channelsim_flow.md)
  + [Example sipro SI](../../Examples/ex_sipro_example_si.md)
  + [Example sipro extract tdr](../../Examples/ex_sipro_extract_tdr.md)
  + [Example sipro eye diagram](../../Examples/ex_sipro_eye_diagram.md)
  + [Example sipro ploteye plotly](../../Examples/ex_sipro_ploteye_plotly.md)
  + [Example sweep inductor values](../../Examples/ex_sweep_inductor_values.md)
  + [Example systemvue basic](../../Examples/ex_systemvue_basic.md)
  + [Example voltage divider](../../Examples/ex_voltage_divider.md)
  + [Example vsa meas demo](../../Examples/ex_vsa_meas_demo.md)
* [Release Notes](../../release_notes/index.md)

# Dataset[](#dataset "Link to this heading")

*class* keysight.edatoolbox.dataset.Dataset[](#keysight.edatoolbox.dataset.Dataset "Link to this definition")
:   Dataset is an alias for either keysight.edatoolbox.dataset.Dataset\_DsDump or keysight.edatoolbox.dataset.Dataset\_AdsDataset. Depending on whether
    the keysight.dataset functionality can be loaded from ADS, it will choose either implementation. The keysight.dataset based one is the most performant and complete.

*class* keysight.edatoolbox.dataset.Dataset\_DsDump(*filename=''*)[](#keysight.edatoolbox.dataset.Dataset_DsDump "Link to this definition")
:   Class to query ADS dataset files. Internally it will use a dsdump approach and parse the contents. This implementation only supports 1 independent variable.

    *class* VariableBlock(*name: str*, *ivar\_names: List[str]*, *dvar\_names: List[str]*, *values: list*)[](#keysight.edatoolbox.dataset.Dataset_DsDump.VariableBlock "Link to this definition")

    dvar\_names(*varblock: str*) → List[str][](#keysight.edatoolbox.dataset.Dataset_DsDump.dvar_names "Link to this definition")
    :   Returns the list of names of dependent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    dvar\_values(*varblock: str*, *var: str*)[](#keysight.edatoolbox.dataset.Dataset_DsDump.dvar_values "Link to this definition")
    :   Returns the values of the specified dependent variable.

        Parameters:
        :   * **varblock** (*str*) – The variable block
            * **var** (*str*) – The variable name

    ivar\_names(*varblock: str*)[](#keysight.edatoolbox.dataset.Dataset_DsDump.ivar_names "Link to this definition")
    :   Returns the list of names of independent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    ivar\_values(*varblock: str*, *var: str*) → List[str][](#keysight.edatoolbox.dataset.Dataset_DsDump.ivar_values "Link to this definition")
    :   Returns the values of the independent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    to\_dataframe(*varblock: str*)[](#keysight.edatoolbox.dataset.Dataset_DsDump.to_dataframe "Link to this definition")
    :   Converts the chosen varblock into a Pandas dataframe

        Parameters:
        :   **varblock** (*str*) – Name of the varblock to convert.

    values(*varblock: str*, *var: str*)[](#keysight.edatoolbox.dataset.Dataset_DsDump.values "Link to this definition")
    :   Returns the values of either the independent or dependent variables in the specified variable block. Gives precedence
        to dependent variable names over independents in the lookup.

        Parameters:
        :   **varblock** (*str*) – The variable block

*class* keysight.edatoolbox.dataset.Dataset\_AdsDataset(*filename: str = ''*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset "Link to this definition")
:   Class to query ADS dataset files. Internally it will use the keysight.dataset module. This implementation is automatically selected when it is available. It is the most
    performant and complete implementation.

    dvar\_names(*varblock: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.dvar_names "Link to this definition")
    :   Returns the list of names of dependent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    dvar\_values(*varblock: str*, *var: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.dvar_values "Link to this definition")
    :   Returns the values of the specified dependent variable.

        Parameters:
        :   * **varblock** (*str*) – The variable block
            * **var** (*str*) – The variable name

    ivar\_names(*varblock: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.ivar_names "Link to this definition")
    :   Returns the list of names of independent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    ivar\_values(*varblock: str*, *var: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.ivar_values "Link to this definition")
    :   Returns the values of the independent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    to\_dataframe(*varblock: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.to_dataframe "Link to this definition")
    :   Converts the chosen varblock into a Pandas dataframe

        Parameters:
        :   **varblock** (*str*) – Name of the varblock to convert.

    values(*varblock: str*, *var: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.values "Link to this definition")
    :   Returns the values of either the independent or dependent variables in the specified variable block. Gives precedence
        to dependent variable names over independents in the lookup.

        Parameters:
        :   **varblock** (*str*) – The variable block

On this page

[Previous

Value](../circuit/classes/value.md)
[Next

External API](../extra/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top