<!-- 来源: Examples\ex_odbpp_simulate_rfpro.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example odbpp simulate rfpro

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_odbpp_simulate_rfpro.rst.txt)

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
  + Example odbpp simulate rfpro
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

# Example odbpp simulate rfpro[](#example-odbpp-simulate-rfpro "Link to this heading")

This example demonstrates how to how to import an ODB++ file and setup and run an RFPro simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2025 Keysight Technologies, Keysight Confidential
# ruff: noqa: D100
from argparse import ArgumentParser
import os
from pathlib import Path

from keysight.edatoolbox import ads, util, xxpro

try:
    import empro
    from empro.geometry import Vector3d
    import empro.toolkit
    import empro.toolkit.analysis
except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using the Python"
        " from EMPro. Use it by launching emproenv.bat/.sh"
    )
    raise

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--output-dir",
        action="store",
        default=None,
        help="Location where the workspace will be created",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir).absolute()
    util.safe_makedirs(args.output_dir)
    tgz_file = Path(__file__).parent / "data" / "line_via_stub.tgz"
    target_workspace_name = "line_via_stub_wrk"
    target_workspace_path = output_dir / target_workspace_name
    target_workspace = str(target_workspace_path)

    cell_name = "line_via_stub"
    library_name = f"{cell_name}_lib"

    assert output_dir.exists(), f"Output directory {output_dir} does not exist!"
    assert tgz_file.exists(), f"Input ODB++ file {tgz_file} does not exist!"
    assert not target_workspace_path.exists(), (
        f"Target workspace {target_workspace} already exists!"
    )

    print(f"Input ODB++: {tgz_file}")
    print(f"Target workspace: {target_workspace}")

    ads_application = ads.ADS()
    print("ADS application created")

    print("Creating workspace")
    if not os.path.exists(target_workspace):
        ads_application.create_workspace(output_dir, target_workspace_name)

    print("Importing ODB++")

    odbpp_import_options = ads.OdbImportOptions()
    odbpp_import_options.separate_component_lib = False
    odbpp_import_options.separate_tech_lib = False

    ads_application.import_odbpp(
        target_workspace,
        tgz_file,
        library=library_name,
        cell=cell_name,
        use_legacy_importer=False,
        import_options=odbpp_import_options,
    )

    print("ODB++ imported")

    # update the material database
    matdb_path = str(target_workspace_path / library_name / "materials.matdb")
    matdb = ads.MaterialDatabase(matdb_path)
    for diel in matdb.dielectrics:
        if diel.er_real <= 0.0:
            diel.er_real = 4.0
    matdb.write(matdb_path)

    # update the thickness of metal layers
    subst_path = str(target_workspace_path / library_name / "tech.subst")
    substrate_info = ads.SubstrateModel(subst_path)
    for layer in substrate_info.layers:
        if layer.layer == 1023:
            layer.thick = -1.39188  # negative thickness : below interface
        if layer.index == 6:
            layer.thick = 1.371

    # update the thickness of dielectric layers
    for material in substrate_info.materials:
        if material.index == 1:
            material.thick = 12.051

    substrate_info.write(subst_path)
    input_lcv = ads.LibraryCellView(library=library_name, cell=cell_name, view="layout")
    pro_lcv = ads.LibraryCellView(
        library=library_name, cell=cell_name, view="rfproSetup"
    )

    print("Creating xxPro simulation view")
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate="tech",
        pro_lcv=pro_lcv,
        tool="rfpro",
    )
    print("xxPro simulation view created")

    with util.remember_cwd():
        os.environ["HPEESOF_DIR"] = (
            ads.get_ads_location()
        )  # ensure the referenced env vars in lib.defs can be found
        xxpro.use_workspace(target_workspace)

        # To load existing project instead of creating a new one
        # res = empro.activeProject.loadActiveProjectFrom(library_name, cell_name,
        #   "rfproSetup")

        # at this stage the view is still completely empty
        # we still need to load the requested layouts in it
        xxpro.load_pro_view(pro_lcv)

        # create an analysis
        with empro.activeProject as project:
            # Change the roles of the components once the view is loaded
            for component in empro.activeProject.layout.components:
                component.cellRole = empro.geometry.Component.CIRCUIT
            empro.activeProject.layout.reExtractNets()
            empro.activeProject.saveActiveProject()

            layout = empro.activeProject.layout
            component_side = layout.layers["component_side (1004)"]
            gnd_layer = layout.layers["ground_plane (1005)"]

            # add a reference pin on the ground layer
            ref_gnd_pin = layout.addReferencePin("ref_gnd_pin", gnd_layer)

            # locate the positive pins and add pins
            vpin1 = layout.addVirtualPin(
                "vpin1",
                Vector3d("2377.51 mil", "3038.88 mil", 0),
                component_side,
                layout.ZPositionOnLayer.TOP,
            )
            vpin2 = layout.addVirtualPin(
                "vpin2",
                Vector3d("3120.36 mil", "3040.82 mil", 0),
                component_side,
                layout.ZPositionOnLayer.TOP,
            )

            # setup the analysis given the pins, use the user-defined analysis
            # although it will give the entire design to simulate
            analysis = empro.analysis.Analysis(
                empro.analysis.Analysis.EMUDAnalysisType, "Analysis"
            )

            # Set PortList
            portDefinitions = [
                (vpin1, ref_gnd_pin),
                (vpin2, ref_gnd_pin),
            ]

            for portIdx, portDef in enumerate(portDefinitions):
                plusPin, minusPin = portDef
                analysis.ports.append(
                    empro.analysis.Port([plusPin], [minusPin], f"port{portIdx + 1}")
                )

            analysis.nets.append(layout.nets["DRV_N"])
            analysis.nets.append(layout.nets["GND"])

            options = analysis.simulationSettings
            frequencyPlanList = options.femFrequencyPlanList()
            frequencyPlanList.clear()

            plan = empro.simulation.FrequencyPlan()
            plan.type = "Linear"
            plan.startFrequency = "0 Hz"
            plan.stopFrequency = "1 GHz"
            plan.numberOfFrequencyPoints = 11
            frequencyPlanList.append(plan)

            # Set Field Storage
            options.saveFieldsFor = "NoFrequencies"
            options.farFieldEnabled = False
            options.setPresetByName("FEM")

            femMeshSettings = options.femMeshSettings
            femMeshSettings.generation = "Generation2"
            femMeshSettings.autoConductorMeshing = True
            femMeshSettings.maximumNumberOfPasses = 1
            empro.activeProject.analyses.append(analysis)

        empro.activeProject.saveActiveProject()
        active_analysis = empro.activeProject.analyses[-1]

        empro.toolkit.analysis.runAnalysis(
            active_analysis, waitForConfirmation=False, saveProject=True
        )
        print("Running and waiting for simulation...")
        empro.activeProject.simulations.isQueueHeld = False
        sim_from_list = empro.activeProject.simulations[-1]
        empro.toolkit.simulation.wait(sim_from_list)

        print("Extracting results")
        result = empro.analysis.CircuitResults(active_analysis)
        delay12 = result.delay(0, 1)

        nr_results = len(delay12)
        freq_dimension = delay12.dimension(0)
        frequencies = [freq_dimension.at(idx) for idx in range(nr_results)]
        delay_values = [delay12.at(idx) for idx in range(nr_results)]
        delays = list(zip(frequencies, delay_values, strict=False))
        frequency, delay_at_1GHz = delays[-1]
        print(f"Delay at 1 GHz={delay_at_1GHz}")
```

On this page

[Previous

Example odbpp simulate pipro dc](ex_odbpp_simulate_pipro_dc.md)
[Next

Example optimize matching network](ex_optimize_matching_network.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top