<!-- 来源: Examples\ex_run_schematic.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example run schematic

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_run_schematic.rst.txt)

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
* [How-To](../How-To/index.md)
  + [Create a Circuit](../How-To/circuit.md)
  + [Run a Circuit Simulation](../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../How-To/sipro.md)
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
* [Examples](index.md)
  + [Running EDA Toolbox Examples](Running%20Examples.md)
  + [Example baluns](ex_baluns.md)
  + [Example co optimize matching network](ex_co_optimize_matching_network.md)
  + [Example create 3d empro serpentines](ex_create_3d_empro_serpentines.md)
  + [Example dump workspace netlists](ex_dump_workspace_netlists.md)
  + [Example empro extract resonance](ex_empro_extract_resonance.md)
  + [Example high pass filter sub circuit](ex_high_pass_filter_sub_circuit.md)
  + [Example import brd](ex_import_brd.md)
  + [Example import ipc2581](ex_import_ipc2581.md)
  + [Example import odb](ex_import_odb.md)
  + [Example low pass filter](ex_low_pass_filter.md)
  + [Example multi python](ex_multi_python.md)
  + [Example odbpp simulate pipro ac reuse sio](ex_odbpp_simulate_pipro_ac_reuse_sio.md)
  + [Example odbpp simulate pipro dc](ex_odbpp_simulate_pipro_dc.md)
  + [Example odbpp simulate rfpro](ex_odbpp_simulate_rfpro.md)
  + [Example optimize matching network](ex_optimize_matching_network.md)
  + [Example pipro ac](ex_pipro_example_ac.md)
  + [Example pipro dc](ex_pipro_example_dc.md)
  + [Example quantumpro one qubit epr](ex_quantumpro_one_qubit_epr.md)
  + [Example quantumpro one qubit freq](ex_quantumpro_one_qubit_freq.md)
  + [Example rfpro stop nets](ex_rfpro_stop_nets.md)
  + [Example run hb simulation](ex_run_hb_simulation.md)
  + [Example run netlist](ex_run_netlist.md)
  + [Example run netlist from disk](ex_run_netlist_from_disk.md)
  + Example run schematic
  + [Example sipro automation](ex_sipro_automation.md)
  + [Example sipro channelsim flow](ex_sipro_channelsim_flow.md)
  + [Example sipro SI](ex_sipro_example_si.md)
  + [Example sipro extract tdr](ex_sipro_extract_tdr.md)
  + [Example sipro eye diagram](ex_sipro_eye_diagram.md)
  + [Example sipro ploteye plotly](ex_sipro_ploteye_plotly.md)
  + [Example sweep inductor values](ex_sweep_inductor_values.md)
  + [Example systemvue basic](ex_systemvue_basic.md)
  + [Example voltage divider](ex_voltage_divider.md)
  + [Example vsa meas demo](ex_vsa_meas_demo.md)
* [Release Notes](../release_notes/index.md)

# Example run schematic[](#example-run-schematic "Link to this heading")

This example demonstrates how to run a simulation by specifying the schematic from a workspace.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc , Keysight Confidential
#

import os
from argparse import ArgumentParser

# import the automation tools for Python for ADS and CircuitSimulation
# load the edatoolbox
from keysight.edatoolbox import ads, circuit, dataset
from keysight.edatoolbox.util import safe_makedirs

class Bunch(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

if __name__=="__main__":
    parser = ArgumentParser()
    parser.add_argument('--output-dir',action="store", required=True, default=None, help='Location where the output will be created')
    args = parser.parse_args()

    ads_application = ads.ADS()

    target_output_dir = args.output_dir
    safe_makedirs(target_output_dir)
    target_workspace = os.path.join(target_output_dir, 'run_schematic_wrk')
    input_workspace_file = os.path.abspath('data/run_schematic_wrk.7zads')

    assert(target_output_dir!=None)
    assert(input_workspace_file!=None)
    assert(os.path.exists(target_output_dir))
    assert(os.path.exists(input_workspace_file))
    assert not os.path.exists(target_workspace), f"Target workspace {target_workspace} already exists!"

    print("Unarchiving workspace")
    ads_application.unarchive_workspace(input_workspace_file, target_output_dir)

    print(f"Input workspace file: {input_workspace_file}")
    print(f"Target output dir: {target_output_dir}")

    print("Generating netlist")
    netlist = ads_application.generate_netlist( target_workspace,
                                                ads.LibraryCellView( library="run_schematic_lib",
                                                                    cell="voltage_divider",
                                                                    view="schematic") )

    voltage_divider = circuit.Circuit(netlist, import_options=Bunch(extract_analyses=False))
    print(f'Existing value of R2.R={voltage_divider.R2.R}')
    voltage_divider.R2.R = '10 ohm'

    print("Running netlist")
    ads_circuitsim = ads.CircuitSimulator()
    ads_circuitsim.run_netlist(voltage_divider.generate_netlist(), output_dir=target_output_dir, rel_data_dir=target_output_dir)

    output_data = dataset.Dataset(os.path.join(target_output_dir,'voltage_divider.ds'))
    print(f"Voltage at node 'in' {output_data.values('DC1.DC', 'in')[0]}V")
    print(f"Voltage at node 'out' {output_data.values('DC1.DC', 'out')[0]}V")

    print("Simulation completed")
```

On this page

[Previous

Example run netlist from disk](ex_run_netlist_from_disk.md)
[Next

Example sipro automation](ex_sipro_automation.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top