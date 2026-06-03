<!-- 来源: Examples\ex_sipro_example_si.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example sipro SI

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_sipro_example_si.rst.txt)

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
  + [Example run schematic](ex_run_schematic.md)
  + [Example sipro automation](ex_sipro_automation.md)
  + [Example sipro channelsim flow](ex_sipro_channelsim_flow.md)
  + Example sipro SI
  + [Example sipro extract tdr](ex_sipro_extract_tdr.md)
  + [Example sipro eye diagram](ex_sipro_eye_diagram.md)
  + [Example sipro ploteye plotly](ex_sipro_ploteye_plotly.md)
  + [Example sweep inductor values](ex_sweep_inductor_values.md)
  + [Example systemvue basic](ex_systemvue_basic.md)
  + [Example voltage divider](ex_voltage_divider.md)
  + [Example vsa meas demo](ex_vsa_meas_demo.md)
* [Release Notes](../release_notes/index.md)

# Example sipro SI[](#example-sipro-si "Link to this heading")

This example demonstrates how to run an SI simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
import os

from keysight.edatoolbox import ads, momentum, util, xxpro

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

    # for SI analyses and Momentum analyses we need to pass on to xxPro the location of the Momentum binaries
    momentum_dir = momentum.get_momentum_location()
    empro.toolkit.analysis.setMomentumDir(momentum_dir)

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
                empro.analysis.Analysis.PASIAnalysisType, "Test"
            )

            portList = analysis.ports
            port_definitions = [
                ("DQ00_J1", ["J1.P_5"], ["J1.P_6"]),
                ("DQ00R_U19", ["U19.P_D3"], ["U19.P_D1"]),
                ("DQ01_J1", ["J1.P_150"], ["J1.P_149"]),
                ("DQ01R_U19", ["U19.P_C2"], ["U19.P_D1"]),
                ("DQ02_J1", ["J1.P_12"], ["J1.P_11"]),
                ("DQ02R_U19", ["U19.P_D7"], ["U19.P_C8"]),
                ("DQ03_J1", ["J1.P_157"], ["J1.P_156"]),
                ("DQ03R_U19", ["U19.P_B7"], ["U19.P_C8"]),
            ]

            def pin_from_name(layout, name: str):
                """Return a pin object from a hierachical pin name.

                Parameters
                ----------
                layout : empro.layout_wrapper.LayoutWrapper
                    Layout of an active xxPro project.
                name : str
                    Pin name.

                Returns
                -------
                empro.geometry.Pin
                    A pin object corresponding to the pin name.
                """
                try:
                    inst_name, pin_name = name.split(".")
                    return layout.instances[inst_name].instPin(pin_name)
                except ValueError:
                    return layout.topLevelPins[name]

            for port_def in port_definitions:
                name, plus_pins, minus_pins = port_def
                plus_pins = [pin_from_name(layout, name) for name in plus_pins]
                minus_pins = [pin_from_name(layout, name) for name in minus_pins]
                port = empro.analysis.Port(plus_pins, minus_pins, name)
                portList.append(port)

            component_model_group_list = analysis.componentModelGroups
            component_model_group = empro.analysis.ComponentModelGroup(
                layout.components[
                    "PC4-RDIMM_V090_RC_F0_20131106_lib:rn_2pos_respack_2x0201-510-501140a_15"
                ]
            )
            component_model_group.arrayedComponent = True
            component_model_group.pinPortMap().update(
                [("P_1", 1), ("P_2", 2), ("P_3", -2), ("P_4", -1)]
            )
            for instance_name in ["RN95", "RN97"]:
                component_model_group.appendInstance(
                    empro.analysis.ComponentInstance(layout.instances[instance_name])
                )

            component_model = empro.analysis.ComponentModel(
                empro.components.RLCSpecification("lumped", "15 Ohm", 0, 0, "Series")
            )
            component_model_group.appendModel(component_model)
            component_model_group_list.append(component_model_group)

            net_list = analysis.nets
            for net in analysis.requiredNets():
                net_list.append(net)

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
        S21_mag = res.Src(1, 0, "ComplexMagnitude")
        S21_phase = res.Src(1, 0, "Phase")
        S43_mag = res.Src(3, 2, "ComplexMagnitude")
        S43_phase = res.Src(3, 2, "Phase")
        S65_mag = res.Src(5, 4, "ComplexMagnitude")
        S65_phase = res.Src(5, 4, "Phase")
        S87_mag = res.Src(7, 6, "ComplexMagnitude")
        S87_phase = res.Src(7, 6, "Phase")

        output_file = os.path.join(target_workspace_dir, "sparams.csv")
        print(f"Writing S parameter data to {output_file}")
        with open(output_file, "w") as file:
            line = ",".join(
                [
                    "Frequency",
                    "S21 (mag)",
                    "S21 (phase)",
                    "S43 (mag)",
                    "S43 (phase)",
                    "S65 (mag)",
                    "S65 (phase)",
                    "S87 (mag)",
                    "S87 (phase)",
                ]
            )
            file.write(line + "\n")
            for i in range(len(freqs)):
                line = f"{freqs[i]},{S21_mag[i]},{S21_phase[i]},{S43_mag[i]},{S43_phase[i]},{S65_mag[i]},{S65_phase[i]},{S87_mag[i]},{S87_phase[i]}"
                file.write(line + "\n")
```

On this page

[Previous

Example sipro channelsim flow](ex_sipro_channelsim_flow.md)
[Next

Example sipro extract tdr](ex_sipro_extract_tdr.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top