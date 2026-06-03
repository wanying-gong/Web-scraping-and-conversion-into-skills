<!-- 来源: How-To\index.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* How-To

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/How-To/index.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* [Initial Setup](../Initial_Setup/index.md)
  + [Installation](../Initial_Setup/installation.md)
  + [Prerequisites](../Initial_Setup/prerequisites.md)
  + [Verifying Installation](../Initial_Setup/verifying.md)
  + [SSH](../Initial_Setup/ssh.md)
* How-To
  + [Create a Circuit](circuit.md)
  + [Run a Circuit Simulation](circuit_sim.md)
  + [Create SIPro View and Run Simulation](sipro.md)
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
* [Examples](../Examples/index.md)
  + [Running EDA Toolbox Examples](../Examples/Running%20Examples.md)
  + [Example baluns](../Examples/ex_baluns.md)
  + [Example co optimize matching network](../Examples/ex_co_optimize_matching_network.md)
  + [Example create 3d empro serpentines](../Examples/ex_create_3d_empro_serpentines.md)
  + [Example dump workspace netlists](../Examples/ex_dump_workspace_netlists.md)
  + [Example empro extract resonance](../Examples/ex_empro_extract_resonance.md)
  + [Example high pass filter sub circuit](../Examples/ex_high_pass_filter_sub_circuit.md)
  + [Example import brd](../Examples/ex_import_brd.md)
  + [Example import ipc2581](../Examples/ex_import_ipc2581.md)
  + [Example import odb](../Examples/ex_import_odb.md)
  + [Example low pass filter](../Examples/ex_low_pass_filter.md)
  + [Example multi python](../Examples/ex_multi_python.md)
  + [Example odbpp simulate pipro ac reuse sio](../Examples/ex_odbpp_simulate_pipro_ac_reuse_sio.md)
  + [Example odbpp simulate pipro dc](../Examples/ex_odbpp_simulate_pipro_dc.md)
  + [Example odbpp simulate rfpro](../Examples/ex_odbpp_simulate_rfpro.md)
  + [Example optimize matching network](../Examples/ex_optimize_matching_network.md)
  + [Example pipro ac](../Examples/ex_pipro_example_ac.md)
  + [Example pipro dc](../Examples/ex_pipro_example_dc.md)
  + [Example quantumpro one qubit epr](../Examples/ex_quantumpro_one_qubit_epr.md)
  + [Example quantumpro one qubit freq](../Examples/ex_quantumpro_one_qubit_freq.md)
  + [Example rfpro stop nets](../Examples/ex_rfpro_stop_nets.md)
  + [Example run hb simulation](../Examples/ex_run_hb_simulation.md)
  + [Example run netlist](../Examples/ex_run_netlist.md)
  + [Example run netlist from disk](../Examples/ex_run_netlist_from_disk.md)
  + [Example run schematic](../Examples/ex_run_schematic.md)
  + [Example sipro automation](../Examples/ex_sipro_automation.md)
  + [Example sipro channelsim flow](../Examples/ex_sipro_channelsim_flow.md)
  + [Example sipro SI](../Examples/ex_sipro_example_si.md)
  + [Example sipro extract tdr](../Examples/ex_sipro_extract_tdr.md)
  + [Example sipro eye diagram](../Examples/ex_sipro_eye_diagram.md)
  + [Example sipro ploteye plotly](../Examples/ex_sipro_ploteye_plotly.md)
  + [Example sweep inductor values](../Examples/ex_sweep_inductor_values.md)
  + [Example systemvue basic](../Examples/ex_systemvue_basic.md)
  + [Example voltage divider](../Examples/ex_voltage_divider.md)
  + [Example vsa meas demo](../Examples/ex_vsa_meas_demo.md)
* [Release Notes](../release_notes/index.md)

# How-To[](#how-to "Link to this heading")

* [Create a Circuit](circuit.md)
  + [Step 0: Getting ready](circuit.md#step-0-getting-ready)
  + [Step 1: Adding the components](circuit.md#step-1-adding-the-components)
  + [Step 2: Connecting the instances](circuit.md#step-2-connecting-the-instances)
  + [Step 3: Analysis](circuit.md#step-3-analysis)
  + [Step 4: Run the simulation](circuit.md#step-4-run-the-simulation)
  + [Step 5: Extracting and plotting results](circuit.md#step-5-extracting-and-plotting-results)
* [Run a Circuit Simulation](circuit_sim.md)
  + [Step 0: Get the example workspaces](circuit_sim.md#step-0-get-the-example-workspaces)
  + [Step 1: Creating the ADS application object](circuit_sim.md#step-1-creating-the-ads-application-object)
  + [Step 2: Unarchiving](circuit_sim.md#step-2-unarchiving)
  + [Step 3: Generating the netlist](circuit_sim.md#step-3-generating-the-netlist)
  + [Step 4: Working the circuit](circuit_sim.md#step-4-working-the-circuit)
  + [Step 5: Run the simulation](circuit_sim.md#step-5-run-the-simulation)
  + [Step 6: Extract the results](circuit_sim.md#step-6-extract-the-results)
* [Create SIPro View and Run Simulation](sipro.md)
  + [Step 0: Get the example workspaces](sipro.md#step-0-get-the-example-workspaces)
  + [Step 1: Creating the ADS application object](sipro.md#step-1-creating-the-ads-application-object)
  + [Step 2: Unarchiving](sipro.md#step-2-unarchiving)
  + [Step 3: Creating the SIPro view](sipro.md#step-3-creating-the-sipro-view)
  + [Step 4: Loading the SIPro view into the SIPro tool](sipro.md#step-4-loading-the-sipro-view-into-the-sipro-tool)
  + [Step 5: Creating an Analysis](sipro.md#step-5-creating-an-analysis)
  + [Step 6: Running an Analysis](sipro.md#step-6-running-an-analysis)
  + [Step 7: Extracting some results](sipro.md#step-7-extracting-some-results)

On this page

[Previous

SSH](../Initial_Setup/ssh.md)
[Next

Create a Circuit](circuit.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top