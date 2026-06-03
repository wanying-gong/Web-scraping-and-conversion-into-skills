<!-- 来源: Examples\ex_quantumpro_one_qubit_epr.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example quantumpro one qubit epr

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_quantumpro_one_qubit_epr.rst.txt)

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
  + Example quantumpro one qubit epr
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

# Example quantumpro one qubit epr[](#example-quantumpro-one-qubit-epr "Link to this heading")

This example demonstrates how to load a QuantumPro view and setup and run an extraction of the Qubit parameters, like anharmonicity and quality factor.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2023 Keysight Technologies, Inc, Keysight Confidential
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
    input_workspace_file = os.path.abspath("data/QuantumPro_Single_Qubit_wrk.7zads")
    target_workspace = os.path.join(target_workspace_dir, "Single_Qubit_Chip_wrk")

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
        library="Single_Qubit_Chip_lib",
        cell="Single_Qubit",
        view="layout",
    )
    pro_lcv = ads.LibraryCellView(
        library="Single_Qubit_Chip_lib",
        cell="Single_Qubit",
        view="quantumpro-setup",
    )
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate="tech",
        pro_lcv=pro_lcv,
        tool="quantumpro",
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

        analysisName = 'Energy Participation Analysis by Script'
        with empro.activeProject: # Create an Analysis
            for component in empro.activeProject.geometry[0]._componentList():
                if "Q_InductorAbstract" in component.cellName or "R_Space" in component.cellName:
                    component.cellRole = empro.geometry.Component.CIRCUIT
                else:
                    component.cellRole = empro.geometry.Component.SUBDESIGN
            empro.activeProject.layout.reExtractNets()
            empro.activeProject.saveActiveProject()

            # Create an Analysis
            analysis = empro.analysis.Analysis()
            analysis.name = analysisName
            analysis.analysisType = empro.analysis.Analysis.QEPAnalysisType

            # Set Netlist
            netList = analysis.nets

            net = empro.analysis.Net('P5', empro.activeProject.geometry[0])
            netList.append(net)

            net = empro.analysis.Net('P6', empro.activeProject.geometry[0])
            netList.append(net)

            # Set Component Model Group List
            componentModelGroupList = analysis.componentModelGroups

            # Create Component Model Group
            componentModelGroup = empro.analysis.ComponentModelGroup('ads_quantum:Q_InductorAbstract', empro.activeProject.geometry[0])
            componentModelGroup.name = 'Q_InductorAbstract'
            componentModelGroup.arrayedComponent = False
            componentModelGroup.updateableAfterSimulation = True
            pinNamePortNumberPairs = (('P1', 1), ('P2', -1))
            pinPortMap = componentModelGroup.pinPortMap()
            pinPortMap.update(pinNamePortNumberPairs)
            instances = ['L1']
            for instance in instances:
                componentModelGroup.appendInstance(empro.toolkit.analysis.createComponentInstanceFromInstance(instance))

            # Create Component Model
            componentModel = empro.analysis.ComponentModel(1, "") # LumpedType = 1, ModelDBType = 2, SnPType = 3, LibCell = 4
            componentModel.name = 'model'
            componentModel.getPassiveLoad().impedance.resistance=empro.core.Expression('0 Ohm')
            componentModel.getPassiveLoad().impedance.capacitance=empro.core.Expression('0 F')
            componentModel.getPassiveLoad().impedance.inductance=empro.core.Expression('11 nH')
            componentModel.getPassiveLoad().impedance.elementArrangement='Parallel'
            componentModelGroup.appendModel(componentModel)
            componentModelGroupList.append(componentModelGroup)

            # Set Analysis Options
            options = analysis.simulationSettings

            # Set Ambient Conditions
            options.ambientConditions.backgroundTemperature = empro.core.Expression(298.15)

            # Set Frequency Plans

            # Set Frequency Plan List
            frequencyPlanList = options.femFrequencyPlanList()
            frequencyPlanList.clear()

            # Set Field Storage
            options.saveFieldsFor = 'AllFrequencies'
            options.farFieldEnabled = False
            options.farFieldAngularResolution = empro.core.Expression('5 deg')

            # Set Simulator

            # Set Preset Simulator Setup By Name
            options.preset = None

            # Set User-Defined Advanced Simulator Setup

            # Set FEM Options

            # Set FEM Matrix Solver
            options.femMatrixSolver.solverType = 'MatrixSolverAuto'

            # Set FEM Eigen Solver Settings
            femEigenSolverSettings = options.femEigenSolverSettings
            femEigenSolverSettings.lowFreqLimit = empro.core.Expression('1 GHz')
            femEigenSolverSettings.highFreqLimit = empro.core.Expression('10 GHz')

            # Set FEM Mesh Settings
            femMeshSettings = options.femMeshSettings
            femMeshSettings.generation = 'Generation2'
            femMeshSettings.includeResistiveLossesInGround = True
            femMeshSettings.orderOfBasisFunctions = 2
            femMeshSettings.useTargetMeshSize = True
            femMeshSettings.autoTargetMeshSize = True
            femMeshSettings.targetMeshSize = empro.core.Expression('wavelength(maxFreq)/3.0')
            femMeshSettings.useMeshDomainOptimization = False
            femMeshSettings.generation = 'Generation2'
            femMeshSettings.minimumNumberOfPasses = 1
            femMeshSettings.maximumNumberOfPasses = 15
            femMeshSettings.refineAtSpecificFrequency = False
            femMeshSettings.refinementFrequency = empro.core.Expression('10 GHz')

            # Set FEM Per Layer Overrides
            femPerPartOverrides = options.femPerLayerOverrides

            override = femPerPartOverrides.add('cond (1)', 1)
            override.targetMeshSize = empro.core.Expression('5 um')

            # Set Resources Settings
            resourceSettings = empro.simulation.LocalResourceSettings()
            resourceSettings.numberOfWorkers = 1
            resourceSettings.numberOfThreads = 0
            options.resourceSettings = resourceSettings

            # Set ParameterSweep
            options.parameterSweepEnabled = False
            options.parameterSequences.clear()

            # Add the Analysis to the list of Analyses
            empro.activeProject.analyses.append(analysis)

        empro.activeProject.saveActiveProject()
        print("Running and waiting for simulation...")
        active_analysis = empro.activeProject.analyses[-1]
        empro.toolkit.analysis.runAnalysis(
            active_analysis, waitForConfirmation=False, saveProject=True
        )
        empro.activeProject.simulations.isQueueHeld = False
        active_simulation = empro.activeProject.simulations[-1]
        empro.toolkit.simulation.wait(active_simulation)
        empro.activeProject.saveActiveProject()

        #Extract parameters
        analysis = empro.activeProject.analyses[analysisName]
        params = empro.analysis.QubitParameters(analysis)

        print("Results:")
        results = params.getResults()
        chi = results.chiMatrix
        rabi = results.rabiMatrix

        for qubit in results.qubits:
            print(qubit.name)
            print(f"Frequency: {qubit.frequency}")
            print(f"Inductance: {qubit.inductance}")
            print(f"Anharmonicity: {qubit.anharmonicity}")
            print(f"Quality Factor: {qubit.qualityFactor}")
            print(f"T1: {qubit.t1}")
            print()

        for resonator in results.resonators:
            print(resonator.name)
            print(f"Frequency: {resonator.frequency}")
            print(f"Anharmonicity: {resonator.anharmonicity}")
            print(f"Quality Factor: {resonator.qualityFactor}")
            print(f"T1: {resonator.t1}")
            print()

        print("Chi Matrix:")
        print(chi.values)
        print()
```

On this page

[Previous

Example pipro dc](ex_pipro_example_dc.md)
[Next

Example quantumpro one qubit freq](ex_quantumpro_one_qubit_freq.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top