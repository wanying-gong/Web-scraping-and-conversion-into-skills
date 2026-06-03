<!-- 来源: How-To\sipro.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [How-To](index.md)
* Create SIPro View and Run Simulation

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/How-To/sipro.rst.txt)

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
* [How-To](index.md)
  + [Create a Circuit](circuit.md)
  + [Run a Circuit Simulation](circuit_sim.md)
  + Create SIPro View and Run Simulation
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

# Create SIPro View and Run Simulation[](#create-sipro-view-and-run-simulation "Link to this heading")

This section will go through an example of how to run a SIPro simulation, starting from a zipped workspace.

## Step 0: Get the example workspaces[](#step-0-get-the-example-workspaces "Link to this heading")

Download the example workspaces, or if you are familiar with the git revision control system, directly clone the whole directory to a working location.

The examples can be found on the [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

Assume you have put these files in your “f:/temp/edatoolbox” directory.

## Step 1: Creating the ADS application object[](#step-1-creating-the-ads-application-object "Link to this heading")

First, let’s make an ADS application object that gives access to a workspace and its contents. But even before that, import the `edatoolbox`

```
>>> from keysight.edatoolbox import ads, momentum, xxpro
>>> ads_application = ads.ADS()
```

## Step 2: Unarchiving[](#step-2-unarchiving "Link to this heading")

Next, we use the ads module to unarchive the workspace. Alternatively you can use this manually with tools like 7-zip.

```
>>> target_workspace_dir = r"f:\temp\edatoolbox\examples\scratch"
>>> ads_application.unarchive_workspace(r"f:\temp\edatoolbox\examples\data\SIPro_PIPro_DDR4_wrk.7zads", target_workspace_dir)
```

## Step 3: Creating the SIPro view[](#step-3-creating-the-sipro-view "Link to this heading")

Now that we have unarchived the workspace, we want to create the SIPro view. To achieve this we define our input LibraryCellView and SIPro LibraryCellView.

```
>>> input_lcv = ads.LibraryCellView( library = "PC4-RDIMM_V090_RC_F0_20131106_lib",
...                                  cell = "PC4-RDIMM_V090_RC_F0_20131106",
...                                  view = "layout")
>>> sipro_lcv = ads.LibraryCellView( library = "PC4-RDIMM_V090_RC_F0_20131106_lib",
...                                  cell = "PC4-RDIMM_V090_RC_F0_20131106",
...                                  view = "sipro")
```

And we use our ads\_application to create the SIPro view.

```
>>> import os
>>> target_workspace = os.path.join(target_workspace_dir, "SIPro_PIPro_DDR4_wrk")
>>> ads_application.create_pro_view( target_workspace,
...                                  input_lcv = input_lcv,
...                                  substrate = "PC4-RDIMM_V090_RC_F0_20131106",
...                                  pro_lcv = sipro_lcv,
...                                  tool = "sipi")
```

## Step 4: Loading the SIPro view into the SIPro tool[](#step-4-loading-the-sipro-view-into-the-sipro-tool "Link to this heading")

In this step, we will start using SIPro’s built-in python API, so we will need to import `empro`

```
>>> import empro
>>> import empro.toolkit
>>> import empro.toolkit.analysis
```

At this point, we have created the SIPro view, but in order to start using SIPro we still need to properly configure it.

First, we will first tell SIPro what momentum to use, using the `edatoolbox`

```
>>> momentum_dir = momentum.get_momentum_location()
>>> empro.toolkit.analysis.setMomentumDir(momentum_dir)
```

Next, we tell SIPro what workspace we are currently using.

```
>>> os.environ['HPEESOF_DIR'] = ads.get_ads_location()  # ensure the referenced env vars in lib.defs can be found
>>> xxpro.use_workspace(target_workspace)
```

Finally, we can load the SIPro view into the SIPro tool and save the SIPro project.

```
>>> xxpro.load_pro_view(sipro_lcv)
>>> empro.activeProject.saveActiveProject()
```

## Step 5: Creating an Analysis[](#step-5-creating-an-analysis "Link to this heading")

Now we are ready to create an Analysis, we will name it “Test”. Use the `empro.analysis.Analysis.PASIAnalysisType` as a first argument, to make sure it will be a Power-Aware-SI Analysis.

```
>>> analysis = empro.analysis.Analysis(empro.analysis.Analysis.PASIAnalysisType, "Test")
```

Let’s define all the ports using the convention: `(port_name, list_of_plus_pin_names, list_of_min_pin_names)`.

```
>>> port_definitions = [ ('DQ00_J1', ['J1.P_5'], ['J1.P_6']),
...                      ('DQ00R_U19', ['U19.P_D3'], ['U19.P_D1']),
...                      ('DQ01_J1',['J1.P_150'],['J1.P_149']),
...                      ('DQ01R_U19',['U19.P_C2'],['U19.P_D1']),
...                      ('DQ02_J1',['J1.P_12'],['J1.P_11']),
...                      ('DQ02R_U19',['U19.P_D7'],['U19.P_C8']),
...                      ('DQ03_J1',['J1.P_157'],['J1.P_156']),
...                      ('DQ03R_U19',['U19.P_B7'],['U19.P_C8'])]
```

To aid us, we will define a helper function to get the `empro.geometry.Pin` object from the `layout`.

```
>>> def pin_from_name(layout, name):
...     try:
...         inst_name, pin_name = name.split(".")
...         return layout.instances[inst_name].instPin(pin_name)
...     except ValueError:
...         return layout.topLevelPins[name]
```

Now we can add the ports to the Analysis.

```
>>> layout = empro.activeProject.layout
>>> for port_def in port_definitions:
...     name, plus_pins, minus_pins = port_def
...     plus_pins = [pin_from_name(layout, name) for name in plus_pins]
...     minus_pins = [pin_from_name(layout, name) for name in minus_pins]
...     port = empro.analysis.Port(plus_pins,minus_pins, name)
...     analysis.ports.append(port)
```

Next, we add the components and set a model for the components to use.

```
>>> component_model_group = empro.analysis.ComponentModelGroup(layout.components['PC4-RDIMM_V090_RC_F0_20131106_lib:rn_2pos_respack_2x0201-510-501140a_15'])
>>> component_model_group.arrayedComponent = True
>>> component_model_group.pinPortMap().update( [('P_1', 1), ('P_2', 2), ('P_3', -2), ('P_4', -1)] )
>>> for instance_name in ['RN95', 'RN97']:
...     component_model_group.appendInstance(empro.analysis.ComponentInstance(layout.instances[instance_name]))

>>> component_model = empro.analysis.ComponentModel(empro.components.RLCSpecification('lumped','15 Ohm',0,0,'Series') )
>>> component_model_group.appendModel(component_model)
>>> analysis.componentModelGroups.append(component_model_group)
```

Finally, we add all the required nets to the Analysis.

```
>>> for net in analysis.requiredNets():
...     analysis.nets.append(net)
```

Now that the Analysis is complete, don’t forget to add it to the activeProject.

```
>>> empro.activeProject.analyses.append(analysis)
```

## Step 6: Running an Analysis[](#step-6-running-an-analysis "Link to this heading")

The previous step actually adds a clone of `analysis` to the activeProject’s analyses list. If we want to be able to view the results afterwards using the SIPro GUI, we need to make sure we run the Analysis that was actually added to the analyses list.

```
>>> active_analysis = empro.activeProject.analyses[-1]
```

Next, we run, wait for completion, and save `active_analysis`.

```
>>> empro.toolkit.analysis.runAnalysis(active_analysis, waitForConfirmation=False, saveProject=True)
>>> empro.activeProject.simulations.isQueueHeld = False
>>> active_simulation = empro.activeProject.simulations[-1]
>>> empro.toolkit.simulation.wait(active_simulation)
>>> empro.activeProject.saveActiveProject()
```

These commands might take some time, depending on the machine you are using.

## Step 7: Extracting some results[](#step-7-extracting-some-results "Link to this heading")

In this final step, we will extract the S21 data and write it to a csv-file. First we grab the datasets.

```
>>> res = empro.analysis.CircuitResults(active_analysis)
>>> freqs = list(res.frequencies())
>>> S21_mag = res.Src(1,0,"ComplexMagnitude")
>>> S21_phase = res.Src(1,0,"Phase")
```

The dataset in `Src` (S-row-column) are 0 indexed, so S21 is accessed as row 1, column 0.

Now we can open a csv file and write the S parameter data to it.

```
>>> output_file = os.path.join(target_workspace_dir, "sparams.csv")
>>> with open(output_file,"w") as file:
...     line = ",".join(["Frequency", "S21 (mag)", "S21 (phase)"])
...     file.write(line + "\n")
...     for i in range(len(freqs)):
...         line = f"{freqs[i]},{S21_mag[i]},{S21_phase[i]}"
...         file.write(line + "\n")
```

On this page

[Previous

Run a Circuit Simulation](circuit_sim.md)
[Next

API Reference](../API_Reference/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top