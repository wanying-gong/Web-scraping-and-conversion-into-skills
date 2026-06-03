<!-- 来源: Examples\ex_dump_workspace_netlists.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example dump workspace netlists

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_dump_workspace_netlists.rst.txt)

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
  + Example dump workspace netlists
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

# Example dump workspace netlists[](#example-dump-workspace-netlists "Link to this heading")

This example demonstrates how to create a netlist for each circuit in a workspace.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
import os
import re

from keysight.edatoolbox import ads, circuit, util

try:
    import empro
    import ariane
except ImportError:
    print("ariane module is not found, run this example using the Python from xxPro")
    raise

def query(lib_defs):
    def map_libraries(lib_defs):
        if not os.path.isfile(lib_defs):
            raise ValueError("{lib_defs} does not exist".format(lib_defs=lib_defs))
        return {name: path for (path, name) in ariane.getFlattenedLibraryList(lib_defs)}

    libraries = map_libraries(lib_defs)
    for library in libraries:
        try:
            lib_path = libraries[library]
        except KeyError:
            raise ValueError(
                "{library} is not a library in {lib_defs}".format(
                    lib_defs=lib_defs, library=library
                )
            )

        lib = ariane.Library.open(lib_path)
        schematics = [
            ads.LibraryCellView(library, cell, view)
            for cell, view, type_ in lib.getCellViewNamesAndTypes()
            if type_ == "schematic"
        ]
        return schematics

if __name__ == "__main__":
    circuit_sim_built_in_vars = set(["NonLinearDemoKit_thermal"])

    parser = ArgumentParser()
    parser.add_argument(
        "--output-dir",
        action="store",
        default=None,
        help="Location of the workspace to query",
    )
    args = parser.parse_args()

    target_workspace_dir = args.output_dir
    util.safe_makedirs(target_workspace_dir)
    input_workspace_file = os.path.abspath("data/simple_matching_wrk.7zads")
    target_workspace = os.path.join(target_workspace_dir, "simple_matching_wrk")

    ads_application = ads.ADS()
    print("ADS application created")

    print("Unarchiving workspace")
    ads_application.unarchive_workspace(input_workspace_file, target_workspace_dir)

    lib_defs = os.path.join(target_workspace, "lib.defs")
    schematics = query(lib_defs)

    ads_application = ads.ADS()
    netlists = ads_application.generate_netlist(target_workspace, schematics)

    for index, netlist in enumerate(netlists):
        with open(f"{target_workspace}/netlist_{index}.ckt", "w") as nlf:
            nlf.write(netlist)
        ckt = circuit.Circuit(netlist)
        print(schematics[index])
        if ckt.instances:
            print(" Instances:")
            for inst_name, inst in ckt.instances.items():
                if isinstance(inst, circuit.Var):
                    # Var's are instances themselves but we do not enlist them here
                    # as they have a dedicated section
                    continue
                if hasattr(inst, "instance_parameters"):
                    # This part is a workaround to handle instance parameters
                    # with index "[x-x]"; will be replaced as an API
                    instanceParameters = ""
                    for p in inst.instance_parameters.keys():
                        numIndex = re.search(r"\[(.*?)\]", p)
                        if numIndex:
                            baseParameterName = p.split("[")[0]
                            startIndex = int(numIndex.group(1).split("-")[0])
                            endIndex = int(numIndex.group(1).split("-")[1])
                            for x in range(startIndex, endIndex + 1):
                                currentParameter = f'{baseParameterName}[{x}]'
                                if getattr(inst, baseParameterName):
                                    instanceParameters = ",".join(
                                        [instanceParameters, currentParameter]
                                    )
                        else:
                            if getattr(inst, p):
                                instanceParameters = ",".join([instanceParameters, p])
                    print("  ", inst_name, "->", instanceParameters)
                else:
                    print("  ", inst_name, "-> no instance parameters available")
        if ckt.variables:
            print(" Variables:")
            var_names = [
                var
                for var in ckt.variables.keys()
                if var not in circuit_sim_built_in_vars
            ]
            print("  ", ",".join(var_names))
            for var_name in var_names:
                var = ckt.instances[var_name]
                print(
                    f'   {var_name}={var.value} {var.optimization or "No optimization info"}, {var.tuning or "No tuning info"}'
                )
        else:
            print(" No variables found")
```

On this page

[Previous

Example create 3d empro serpentines](ex_create_3d_empro_serpentines.md)
[Next

Example empro extract resonance](ex_empro_extract_resonance.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top