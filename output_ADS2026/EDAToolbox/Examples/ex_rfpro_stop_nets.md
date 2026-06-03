<!-- 来源: Examples\ex_rfpro_stop_nets.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example rfpro stop nets

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_rfpro_stop_nets.rst.txt)

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
  + Example rfpro stop nets
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

# Example rfpro stop nets[](#example-rfpro-stop-nets "Link to this heading")

This example demonstrates how to setup an RFPro simulation using the concept of stop nets.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

# This example can be run from within a running RFPro session opened on the
# ADS Example "RFPro Two Stage RF Board Amplifier"

# It will generate an analysis with all nets and components found between
# Q1.P1 and Q2.P2, stop at GND-typed nets

from argparse import ArgumentParser
from collections import defaultdict
import os

import empro

from keysight.edatoolbox import ads, util, xxpro

stop_pins = ["R4.P1"]
stop_nets = ["Gnd", "C5.P1"]
io_pins = ["Q1.P1", "Q2.P2"]

def populate_analysis_from_io_pins_stop_nets(analysis, io_pins, stop_pins, stop_nets):
    # take an existing analysis and based on io_pins, stop_pins and stop_nets
    # fill the analysis
    layout = empro.activeProject.layout
    pins = layout.topLevelPins

    pin_to_nets = {}
    pin_to_shorted_pins = (
        {}
    )  # tracks which pins are shorted across a component instance
    instance_to_connected_nets = {}
    pin_name_to_pin = {}
    net_to_pins = defaultdict(list)
    for pin in pins:
        pin_to_nets[pin.name] = pin.netName
    for instance in layout.instances:
        pins_on_instance = []
        nets_on_instance = []
        for pin in instance.pins():
            pin_name = f"{instance.name}.{pin.name}"
            pin_name_to_pin[pin_name] = pin
            pin_to_nets[pin_name] = pin.netName
            net_to_pins[pin.netName] = net_to_pins.get(pin.netName, []) + [
                pin_name,
            ]
            pins_on_instance.append(pin_name)
            nets_on_instance.append(pin.netName)
        for pin in pins_on_instance:
            pin_to_shorted_pins[pin] = pins_on_instance
        instance_to_connected_nets[instance.name] = nets_on_instance

    nets_to_analyse = []
    for startPin in io_pins:
        nets_to_consider = [pin_to_nets[startPin]]
        nets_visited = set()  # to avoid loops

        iteration = 0
        while nets_to_consider:
            active_net = nets_to_consider.pop(0)
            if active_net in nets_visited:
                continue

            nets_visited.add(active_net)
            nets_to_analyse.append(active_net)

            pins_range = stop_pins + io_pins
            # what is connected to this net?
            all_pins_connected_to_net = [
                pin for pin in net_to_pins[active_net] if pin not in pins_range
            ]
            # for each of the pins part of the net, collect what nets they are connected to
            # this should be only the active_net
            nets_connected = set(
                [pin_to_nets[pin] for pin in all_pins_connected_to_net]
            )
            assert len(nets_connected) == 1
            # for all pins request which components they optionally belong to and assume
            # there is a short on that component and travel over that component
            shorted_pins = []
            for pin in all_pins_connected_to_net:
                shorted_pins += pin_to_shorted_pins.get(pin, [])

            shorted_pins = [pin for pin in shorted_pins if pin not in pins_range]

            # collected the nets of these pins
            nets_connected = [pin_to_nets[pin] for pin in shorted_pins]
            nets_connected = [
                net for net in set(nets_connected) if net not in stop_nets
            ]

            nets_to_consider += nets_connected
            iteration += 1
            # avoid getting stuck in large loops due to mistakes in algorithm
            if iteration == 1000:
                raise RuntimeError("Iteration limit encountered")

    # add also the stop nets
    nets_to_analyse += stop_nets
    # add all the required nets to the analysis
    for net in nets_to_analyse:
        analysis.nets.append(layout.nets[net])

    # find all instances that have at least two nets part of the nets_to_analyse
    instances_to_analyse = []
    for instance in layout.instances:
        nets_at_instance = set(instance_to_connected_nets[instance.name])
        nets_at_instance = nets_at_instance.intersection(set(nets_to_analyse))
        if len(nets_at_instance) >= 2:
            # check if none of the io_pins are at the instance, as we can't add those instances
            # as it will generate an error
            pin_names_from_instance = set(
                [f"{instance.name}.{pin.name}" for pin in instance.pins()]
            )
            if len(pin_names_from_instance.intersection(io_pins)) == 0:
                instances_to_analyse.append(instance)

    for instance in instances_to_analyse:
        component_model_group = empro.analysis.ComponentModelGroup(
            layout.components[f"{instance.libraryName}:{instance.cellName}"]
        )
        component_model_group.name = instance.name
        component_model_group.appendInstance(
            empro.analysis.ComponentInstance(layout.instances[instance.name])
        )

        print(instance.name, instance.libraryName)
        if instance.cellName == "HBFP-0420":
            model = empro.analysis.ComponentModel(
                4, f"{instance.libraryName}:{instance.cellName}"
            )
            model.viewName = "symbol"
        else:
            model = empro.analysis.ComponentModel(
                empro.components.RLCSpecification("lumped", "15 Ohm", 0, 0, "Series")
            )
        component_model_group.appendModel(model)
        component_model_group.pinPortMap().update([("P1", 1), ("P2", -1)])
        analysis.componentModelGroups.append(component_model_group)

    gnd_layer = layout.layers["ground_bottom (6)"]
    if "Reference Pin on ground_bottom (6)" not in [
        x.name for x in layout.topLevelPins
    ]:
        ref_gnd_pin = layout.addReferencePin(
            "Reference Pin on ground_bottom (6)", gnd_layer
        )
    else:
        ref_gnd_pin = layout.topLevelPins["Reference Pin on ground_bottom (6)"]
    for pin in io_pins:
        port = empro.analysis.Port([pin_name_to_pin[pin]], [ref_gnd_pin], f"{pin}")
        analysis.ports.append(port)

    for net in analysis.requiredNets():
        analysis.nets.append(net)

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

    target_workspace_dir = args.output_dir
    util.safe_makedirs(target_workspace_dir)
    input_workspace_file = os.path.abspath("data/RFPro_2Stage_RF_Board_Amp_wrk.7zads")
    target_workspace = os.path.join(
        target_workspace_dir, "RFPro_2Stage_RF_Board_Amp_wrk"
    )

    assert target_workspace_dir is not None
    assert input_workspace_file is not None
    assert os.path.exists(target_workspace_dir)
    assert os.path.exists(input_workspace_file)
    assert not os.path.exists(
        target_workspace
    ), f"Target workspace {target_workspace} already exists!"

    print(f"Input workspace file: {input_workspace_file}")
    print(f"Target output dir: {target_workspace_dir}")

    ads_application = ads.ADS()
    print("ADS application created")

    print("Unarchiving workspace")
    ads_application.unarchive_workspace(input_workspace_file, target_workspace_dir)

    print("Creating xxPro simulation view")
    input_lcv = ads.LibraryCellView(
        library="RF_Board_lib", cell="Two_Stage_Amp", view="layout"
    )
    pro_lcv = ads.LibraryCellView(
        library="RF_Board_lib", cell="Two_Stage_Amp", view="rfpro"
    )
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate="tech",
        pro_lcv=pro_lcv,
        tool="rfpro",
    )

    print("xxPro simulation view created")

    with util.remember_cwd():
        os.environ[
            "HPEESOF_DIR"
        ] = (
            ads.get_ads_location()
        )  # ensure the referenced env vars in lib.defs can be found
        xxpro.use_workspace(target_workspace)

        # at this stage the view is still completely empty
        # we still need to load the requested layouts in it
        xxpro.load_pro_view(pro_lcv)
        with empro.activeProject as project:
            # Change the roles of the components once the view is loaded
            for component in empro.activeProject.layout.components:
                if component.cellRole != empro.geometry.Component.CIRCUIT:
                    component.cellRole = empro.geometry.Component.CIRCUIT
            empro.activeProject.layout.reExtractNets()

            empro.activeProject.saveActiveProject()

        with empro.activeProject:
            analysis = empro.analysis.Analysis(
                empro.analysis.Analysis.EMUDAnalysisType, "ScriptedAnalysis"
            )
            populate_analysis_from_io_pins_stop_nets(
                analysis, io_pins, stop_pins, stop_nets
            )
            empro.activeProject.analyses.append(analysis)

        empro.activeProject.saveActiveProject()
```

On this page

[Previous

Example quantumpro one qubit freq](ex_quantumpro_one_qubit_freq.md)
[Next

Example run hb simulation](ex_run_hb_simulation.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top