<!-- 来源: Examples\ex_empro_extract_resonance.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example empro extract resonance

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_empro_extract_resonance.rst.txt)

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
  + Example empro extract resonance
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
  + [Example run schematic](ex_run_schematic.md)
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

# Example empro extract resonance[](#example-empro-extract-resonance "Link to this heading")

This example demonstrates how to extract the resonant frequency of a patch antenna.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2025 Keysight Technologies, Keysight Confidential
# ruff: noqa: D100

from argparse import ArgumentParser
import json
import math
import os

import ariane
import empro
import empro.toolkit.portparam
import empro.toolkit.simulation
import empro.toolkit.zap

from keysight.edatoolbox import util

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--output-dir",
        action="store",
        required=True,
        default=None,
        help="Location where the output will be created",
    )
    args = parser.parse_args()

    assert not os.path.exists(args.output_dir), (
        f"Target workspace {args.output_dir} already exists!"
    )

    util.safe_makedirs(args.output_dir)

    parameters = None
    parameter_filepath = os.path.abspath("data/parameters.json")
    with open(parameter_filepath, "r") as parameter_file:
        data = parameter_file.read()
        parameters = json.loads(data)
        print("Loaded parameters: {parameters}", parameters)

    # assume it is an OA version, create the hosting library
    libraryDir = args.output_dir
    ariane.Library.create(libraryDir, os.path.basename(libraryDir))
    # unzep in the library
    proj_path = os.path.abspath("data/test_antenna_inverted_f.zep")
    empro.toolkit.zap.unzep(proj_path, "all", libraryDir)
    proj = empro.activeProject.loadActiveProjectFrom(
        os.path.join(libraryDir, "test_antenna_inverted_f")
    )

    with empro.activeProject as project:
        project.parameters.setFormula(
            "conductor_thickness", parameters["conductor_thickness"]
        )
        project.parameters.setFormula(
            "substrate_thickness", parameters["substrate_thickness"]
        )

    simulation = empro.activeProject.createSimulation(True)
    print("Running and waiting for simulation...")
    empro.activeProject.simulations.isQueueHeld = False
    empro.toolkit.simulation.wait(simulation)

    s = empro.toolkit.portparam.getSMatrix(sim=simulation.id())
    s11 = s[1, 1]
    resonant_value, resonant_frequency = min(
        zip(abs(s11), s11.dimension(0), strict=False)
    )
    resonant_value = 20.0 * math.log(resonant_value) / math.log(10.0)

    print("Resonance frequency: {}".format(resonant_frequency))
    print("Resonance value: {}".format(resonant_value))
    output_file = os.path.join(libraryDir, "output.txt")
    with open(output_file, "w") as output_file:
        output_file.write("Resonance frequency: {}\n".format(resonant_frequency))
        output_file.write("Resonance value: {}".format(resonant_value))
```

On this page

[Previous

Example dump workspace netlists](ex_dump_workspace_netlists.md)
[Next

Example high pass filter sub circuit](ex_high_pass_filter_sub_circuit.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top