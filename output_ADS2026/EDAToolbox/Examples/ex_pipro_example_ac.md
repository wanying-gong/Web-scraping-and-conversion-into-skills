<!-- 来源: Examples\ex_pipro_example_ac.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example pipro ac

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_pipro_example_ac.rst.txt)

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
  + Example pipro ac
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

# Example pipro ac[](#example-pipro-ac "Link to this heading")

This example demonstrates how load an SIPro view and setup and run an PIPro AC simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
import os

from keysight.edatoolbox import ads, util, xxpro

try:
    import empro
    import empro.toolkit
    import empro.toolkit.analysis
except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using the Python from EMPro.  Use it by launching emproenv.bat/.sh"
    )
    raise

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
    input_workspace_file = os.path.abspath("data/SIPro_PIPro_DDR4_wrk.7zads")
    target_workspace = os.path.join(target_workspace_dir, "SIPro_PIPro_DDR4_wrk")

    assert target_workspace_dir != None
    assert input_workspace_file != None
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
        library="PC4-RDIMM_V090_RC_F0_20131106_lib",
        cell="PC4-RDIMM_V090_RC_F0_20131106",
        view="layout",
    )
    pro_lcv = ads.LibraryCellView(
        library="PC4-RDIMM_V090_RC_F0_20131106_lib",
        cell="PC4-RDIMM_V090_RC_F0_20131106",
        view="sipro",
    )
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate="PC4-RDIMM_V090_RC_F0_20131106",
        pro_lcv=pro_lcv,
        tool="sipi",
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
        empro.activeProject.saveActiveProject()

        with empro.activeProject:
            layout = empro.activeProject.layout

            # create an analysis
            analysis = empro.analysis.Analysis(
                empro.analysis.Analysis.ACAnalysisType, "Test"
            )

            ground_nets = ["GND"]
            power_nets = ["VDD"]
            vrm_definitions = [("J1", "1.2 V")]
            sink_definitions = [(f"U{index}", "0.1 A") for index in range(1, 20)]

            net_list = analysis.nets
            for net_name in ground_nets + power_nets:
                net_list.append(layout.nets[net_name])

            vrm_list = analysis.vrms
            for vrm_name, vrm_voltage in vrm_definitions:
                instance = layout.instances[vrm_name]
                plus_pins = [
                    pin for pin in instance.pins() if pin.netName in power_nets
                ]
                minus_pins = [
                    pin for pin in instance.pins() if pin.netName in ground_nets
                ]
                vrm = empro.analysis.Vrm(plus_pins, minus_pins, vrm_name)
                vrm.voltage = vrm_voltage
                vrm.sourceType = "PackagedVrm"
                vrm_list.append(vrm)

            sink_list = analysis.sinks
            for sink_name, sink_current in sink_definitions:
                instance = layout.instances[sink_name]
                plus_pins = [
                    pin for pin in instance.pins() if pin.netName in power_nets
                ]
                minus_pins = [
                    pin for pin in instance.pins() if pin.netName in ground_nets
                ]
                sink = empro.analysis.Sink(plus_pins, minus_pins, sink_name)
                sink.current = sink_current
                sink_list.append(sink)

            component_model_group_list = analysis.componentModelGroups
            component_model_group = empro.analysis.ComponentModelGroup(
                layout.components[
                    "PC4-RDIMM_V090_RC_F0_20131106_lib:c_capacitors_0603-511-500044_4.7a_4.7uf"
                ]
            )
            instances = ["C106", "C14", "C16", "C28", "C74", "C79"]
            for instance_name in instances:
                component_model_group.appendInstance(
                    empro.analysis.ComponentInstance(layout.instances[instance_name])
                )
            component_model_group.appendModel(
                empro.analysis.ComponentModel(
                    empro.components.RLCSpecification(
                        "lumped", 0, 0, "4.7 uF", "Series"
                    )
                )
            )
            component_model_group_list.append(component_model_group)

            component_model_group = empro.analysis.ComponentModelGroup(
                layout.components[
                    "PC4-RDIMM_V090_RC_F0_20131106_lib:c_capacitors_0402-511-500201_4.7a_4.7uf"
                ]
            )
            instances = ["C116", "C117", "C118", "C119", "C120", "C121", "C122", "C123"]
            for instance_name in instances:
                component_model_group.appendInstance(
                    empro.analysis.ComponentInstance(layout.instances[instance_name])
                )
            component_model_group.appendModel(
                empro.analysis.ComponentModel(
                    empro.components.RLCSpecification(
                        "lumped", 0, 0, "4.7 uF", "Series"
                    )
                )
            )
            component_model_group_list.append(component_model_group)

            component_model_group = empro.analysis.ComponentModelGroup(
                layout.components[
                    "PC4-RDIMM_V090_RC_F0_20131106_lib:c_capacitors_0402-511-500048_1.0a_1.0uf"
                ]
            )
            instances = [
                "C100",
                "C102",
                "C104",
                "C105",
                "C107",
                "C108",
                "C109",
                "C110",
                "C111",
                "C24",
                "C31",
                "C33",
                "C35",
                "C37",
                "C42",
                "C44",
                "C46",
                "C54",
                "C60",
                "C63",
                "C66",
                "C68",
                "C70",
                "C75",
                "C76",
                "C77",
                "C78",
                "C81",
                "C83",
                "C85",
                "C87",
                "C91",
                "C95",
                "C96",
                "C97",
            ]
            for instance_name in instances:
                component_model_group.appendInstance(
                    empro.analysis.ComponentInstance(layout.instances[instance_name])
                )
            component_model_group.appendModel(
                empro.analysis.ComponentModel(
                    empro.components.RLCSpecification(
                        "lumped", 0, 0, "1.0 uF", "Series"
                    )
                )
            )
            component_model_group_list.append(component_model_group)

            frequency_plan_list = analysis.simulationSettings.femFrequencyPlanList()
            frequency_plan_list.clear()
            plan = empro.simulation.FrequencyPlan()
            plan.type = "Logarithmic"
            plan.startFrequency = empro.core.Expression("1 MHz")
            plan.stopFrequency = empro.core.Expression("100 MHz")
            plan.pointsPerDecade = 5
            plan.enabled = True
            frequency_plan_list.append(plan)

            empro.activeProject.analyses.append(analysis)

        print("Running and waiting for simulation...")
        active_analysis = empro.activeProject.analyses[-1]
        empro.toolkit.analysis.runAnalysis(
            active_analysis, waitForConfirmation=False, saveProject=True
        )
        empro.activeProject.simulations.isQueueHeld = False
        active_simulation = empro.activeProject.simulations[-1]
        empro.toolkit.simulation.wait(active_simulation)
        empro.activeProject.saveActiveProject()

        res = empro.analysis.CircuitResults(active_analysis)
        freqs = list(res.frequencies())
        for i, sink in enumerate(active_analysis.sinks):
            impedance = res.Zrc(i + 1, i + 1, "ComplexMagnitude")
            min_impedance = min(list(impedance))
            freq = freqs[list(impedance).index(min_impedance)]
            print(
                f"{impedance.name} minimum impedance: {min_impedance} ohm, found at f: {freq} Hz"
            )
```

On this page

[Previous

Example optimize matching network](ex_optimize_matching_network.md)
[Next

Example pipro dc](ex_pipro_example_dc.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top