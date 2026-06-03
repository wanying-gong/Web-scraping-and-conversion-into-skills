<!-- 来源: Examples\ex_sipro_channelsim_flow.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example sipro channelsim flow

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_sipro_channelsim_flow.rst.txt)

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
  + Example sipro channelsim flow
  + [Example sipro SI](ex_sipro_example_si.md)
  + [Example sipro extract tdr](ex_sipro_extract_tdr.md)
  + [Example sipro eye diagram](ex_sipro_eye_diagram.md)
  + [Example sipro ploteye plotly](ex_sipro_ploteye_plotly.md)
  + [Example sweep inductor values](ex_sweep_inductor_values.md)
  + [Example systemvue basic](ex_systemvue_basic.md)
  + [Example voltage divider](ex_voltage_divider.md)
  + [Example vsa meas demo](ex_vsa_meas_demo.md)
* [Release Notes](../release_notes/index.md)

# Example sipro channelsim flow[](#example-sipro-channelsim-flow "Link to this heading")

This example demonstrates how to run a channel simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2025 Keysight Technologies, Keysight Confidential
# ruff: noqa: D100
from argparse import ArgumentParser
import os
from pathlib import Path
import re

import plotly.express as px
from plotly.subplots import make_subplots

from keysight.edatoolbox import ads, circuit, momentum, util, xxpro
import keysight.pwdatatools as pwdt

def update_sio_path_in_subckt(new_sio_file_location: str, subckt_file: str):
    """Update the file location of an SIO file in a subcircuit netlist.

    Parameters
    ----------
    new_sio_file_location : str
        New location of the SIO file.
    subckt_file : str
        Path to the subcircuit file.
    """
    new_sio_file_location = str(new_sio_file_location).replace("\\", "\\\\")
    with open(subckt_file, "r") as file:
        data = file.read()
    data = re.sub(r'File="[^"]*"', 'File="' + new_sio_file_location + '"', data)
    with open(subckt_file, "w") as file:
        file.write(data)
    print("New Sio file location updated")

def update_subckt_path_in_netlist(new_subckt_file_location: str, netlist_file: str):
    """Update the file location of a subcircuit netlist in a netlist file.

    Parameters
    ----------
    new_subckt_file_location : str
        New location of subcircuit netlist.
    netlist_file : str
        Path for netlist file.
    """
    new_subckt_file_location = str(new_subckt_file_location).replace("\\", "\\\\")
    with open(netlist_file, "r") as file:
        data = file.read()
    data = re.sub(
        r'#include "[^"]*"', '#include "' + new_subckt_file_location + '"', data
    )
    with open(netlist_file, "w") as file:
        file.write(data)
    print("New subckt file location updated")

def read_netlist(netlist_file_location: str):
    """Return the content of the netlist file.

    Parameters
    ----------
    netlist_file_location : str
        Path for netlist.log file.

    Returns
    -------
    str
        Content of the netlist file.
    """
    netlist = ""
    with open(netlist_file_location, "r") as file:
        netlist = file.read()
    return netlist

try:
    import empro
    import empro.toolkit
    import empro.toolkit.analysis
except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using the Python"
        " from EMPro.  Use it by launching emproenv.bat/.sh"
    )
    raise

class Bunch(object):
    """Convert kwargs to object attributes."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

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
    output_dir = Path(args.output_dir).absolute()
    util.safe_makedirs(args.output_dir)

    data_path = Path(__file__).parent / "data"
    odb_file = data_path / "Minipc" / "minipc_pm_v0_pm.zip"
    cell_name = "minipc_pm"
    library_name = f"{cell_name}_lib"
    target_workspace_name = f"{cell_name}_wrk"
    target_workspace_path = output_dir / target_workspace_name
    target_workspace = str(target_workspace_path)
    netlist_file = data_path / "Minipc" / "Netlist" / "netlist.log"
    subckt_file = (
        data_path
        / "Minipc"
        / "Netlist"
        / "minipc_pm_lib_minipc_pm_DDR_Ckt_DQ0_DDR_PCB1_subCktNetlist.log"
    )

    assert odb_file.exists(), f"ODB++ file {odb_file} does not exist"
    assert netlist_file.exists(), f"Netlist file {netlist_file} does not exist"
    assert subckt_file.exists(), f"Subcircuit file {subckt_file} does not exist"
    assert output_dir.exists(), f"Output directory {output_dir} does not exist"
    assert not target_workspace_path.exists(), (
        f"Target workspace {target_workspace} already exists!"
    )

    print(f"Input ODB++: {odb_file}")

    print(f"Target workspace: {target_workspace}")

    # Step 1: Creating the ADS application object
    ads_application = ads.ADS()
    print("ADS application created")
    print("Creating workspace")
    if not os.path.exists(target_workspace):
        ads_application.create_workspace(output_dir, target_workspace_name)

    # Step 2: Import odb++ file

    print("Importing ODB++")

    odbpp_import_options = ads.OdbImportOptions()
    odbpp_import_options.separate_component_lib = False
    odbpp_import_options.separate_tech_lib = False

    ads_application.import_odbpp(
        target_workspace,
        odb_file,
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
    subst_path = str(target_workspace_path / library_name / f"{cell_name}.subst")
    substrate_info = ads.SubstrateModel(subst_path)
    for layer in substrate_info.layers:
        if layer.layer == 1033:
            layer.thick = -1.761411  # negative thickness : below interface
        if layer.index == 8:
            layer.thick = 0.6654142

    # update the thickness of dielectric layers
    for material in substrate_info.materials:
        if material.index == 1:
            material.thick = 3.01

    substrate_info.write(subst_path)

    input_lcv = ads.LibraryCellView(library=library_name, cell=cell_name, view="layout")
    pro_lcv = ads.LibraryCellView(library=library_name, cell=cell_name, view="sipi1")

    # Step 3: Creating the SIPro view
    print("Creating SIPro simulation view")
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate=cell_name,
        pro_lcv=pro_lcv,
        tool="sipi",
    )
    print("xxPro simulation view created")

    momentum_dir = momentum.get_momentum_location()
    empro.toolkit.analysis.setMomentumDir(momentum_dir)
    with util.remember_cwd():
        os.environ["HPEESOF_DIR"] = (
            ads.get_ads_location()
        )  # ensure the referenced env vars in lib.defs can be found

        # Step 4: Loading the SIPro view into the SIPro tool
        xxpro.use_workspace(target_workspace)
        xxpro.load_pro_view(pro_lcv)
        empro.activeProject.saveActiveProject()

        # Step 5 : ==== Script generated by ADS Window starts here =====
        # Create an Analysis
        analysis = empro.analysis.Analysis()
        analysis.name = "DQ0 by Script"
        analysis.analysisType = empro.analysis.Analysis.PASIAnalysisType

        # Set PortList
        portList = analysis.ports

        plusPins = ["U1.AV26"]
        minusPins = ["U1.AV25"]
        port = empro.toolkit.analysis.createPortFromPins(plusPins, minusPins)
        port.name = "DDR4_DQ0_U1"
        port.referenceImpedance = empro.core.Expression("50")
        port.feedType = "Auto"
        portList.append(port)

        plusPins = ["U15.G2"]
        minusPins = ["U15.H1"]
        port = empro.toolkit.analysis.createPortFromPins(plusPins, minusPins)
        port.name = "DDR4_DQ0_U15"
        port.referenceImpedance = empro.core.Expression("50")
        port.feedType = "Auto"
        portList.append(port)

        # Set Netlist
        netList = analysis.nets

        net = empro.analysis.Net("GND", empro.activeProject.geometry[0])
        netList.append(net)

        net = empro.analysis.Net("DDR4_DQ0", empro.activeProject.geometry[0])
        netList.append(net)

        # Set Analysis Options
        options = analysis.simulationSettings

        # Set Ambient Conditions
        options.ambientConditions.backgroundTemperature = empro.core.Expression(298.15)

        # Set Frequency Plans

        # Set Frequency Plan List
        frequencyPlanList = options.femFrequencyPlanList()
        frequencyPlanList.clear()

        plan = empro.simulation.FrequencyPlan()
        plan.type = "Linear"
        plan.startFrequency = empro.core.Expression("20 kHz")
        plan.stopFrequency = empro.core.Expression("20.416667 GHz")
        plan.numberOfFrequencyPoints = 66
        plan.samplePointsLimit = 300
        plan.pointsPerDecade = 20
        plan.enabled = True
        frequencyPlanList.append(plan)

        # Set Field Storage
        options.saveFieldsFor = "NoFrequencies"
        options.farFieldEnabled = False
        options.farFieldAngularResolution = empro.core.Expression("5 deg")

        # Set Simulator

        # Set Preset Simulator Setup By Name
        options.preset = None

        # Set User-Defined Advanced Simulator Setup

        # Set FEM Options

        # Set FEM Matrix Solver
        options.femMatrixSolver.solverType = "MatrixSolverAuto"

        # Set FEM Mesh Settings
        femMeshSettings = options.femMeshSettings
        femMeshSettings.includeResistiveLossesInGround = False
        femMeshSettings.orderOfBasisFunctions = 1
        femMeshSettings.useTargetMeshSize = False
        femMeshSettings.autoTargetMeshSize = False
        femMeshSettings.targetMeshSize = empro.core.Expression("2 mm")
        femMeshSettings.useMeshDomainOptimization = True
        femMeshSettings.minimumNumberOfPasses = 1
        femMeshSettings.maximumNumberOfPasses = 1
        femMeshSettings.refineAtSpecificFrequency = False
        femMeshSettings.refinementFrequency = empro.core.Expression("1 GHz")

        # Set Resources Settings
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
        # ===== Script generated by ADS Window Ends here ======
        # take the latest analysis
        active_analysis = empro.activeProject.analyses[-1]

        # Step 6: Run Analysis for the nets added in SIPro
        print("Running and waiting for simulation...")
        empro.toolkit.analysis.runAnalysis(
            active_analysis, waitForConfirmation=False, saveProject=True
        )
        empro.activeProject.simulations.isQueueHeld = False
        active_simulation = empro.activeProject.simulations[-1]
        empro.toolkit.simulation.wait(active_simulation)
        new_sio_location = os.path.join(
            active_simulation.simulationPath(), "emds_dsn", "design", "design.sio"
        )
        empro.activeProject.saveActiveProject()

    # replace new sio in the subckt netlist
    # Step 7 : update netlist for Memory designer Schematic with new sio file
    update_sio_path_in_subckt(new_sio_location, subckt_file)

    # replace new subckt in the netlist file
    update_subckt_path_in_netlist(subckt_file, netlist_file)

    netlist = read_netlist(netlist_file)
    # Step 8:
    # Run Channel simulation using circuit simulator module using updated netlist

    ads_circuitsim = ads.CircuitSimulator()
    ckt = circuit.Circuit(netlist, import_options=Bunch(extract_analyses=False))
    ads_circuitsim.run_netlist(ckt.generate_netlist(), output_dir=target_workspace)

    # Step 9 : Plot measurement results
    print("====Measurement Results====")
    ds_file = os.path.join(target_workspace, "md.ds")
    results = pwdt.read_file(ds_file)

    eye_meas_summary = results.get_member_as_block(
        "Tran1.TDM.Memory_Probe.Ch0_U15_DQ0.EyeHeight"
    ).to_pandas_dataframe()

    print(eye_meas_summary.to_string(index=False))

    eyevout_data1 = results.get_member_as_block(
        "Tran1.TDM.Memory_Probe.Ch0_U15_DQ0.Eye"
    ).to_pandas_dataframe()
    eyevout_data2 = results.get_member_as_block(
        "Tran1.TDM.Memory_Probe.Ch0_U1_DQ0.Eye"
    ).to_pandas_dataframe()
    config = dict({"scrollZoom": True})

    if "index" not in eyevout_data1.columns:
        # creating dummy index column for plotly to color the points.
        # TODO : Remove if once pwdatatools stops discarding the index
        # column containing the eye diagram density values.
        eyevout_data1["index"] = (
            eyevout_data1["Density"] / max(eyevout_data1["Density"]) * 100
        )

    if "index" not in eyevout_data2.columns:
        # creating dummy index column for plotly to color the points.
        # TODO : Remove if once pwdatatools stops discarding the index
        # column containing the eye diagram density values.
        eyevout_data2["index"] = (
            eyevout_data2["Density"] / max(eyevout_data2["Density"]) * 100
        )

    fig1 = px.scatter(eyevout_data1, y="Density", x="time", color="index")
    fig2 = px.scatter(eyevout_data2, y="Density", x="time", color="index")
    fig = make_subplots(
        rows=2,
        cols=1,
        subplot_titles=(
            "Ch0_U15_DQ0.Eye.Density Vs Time",
            "Ch0_U1_DQ0.Eye.Density Vs Time",
        ),
        shared_xaxes=True,
        shared_yaxes=True,
        x_title="Time (psec)",
        y_title="Density",
    )
    fig.add_traces(fig1.data, rows=1, cols=1)
    fig.add_traces(fig2.data, rows=2, cols=1)
    fig.update_layout(title_text=f"Eye Diagram plots for : {odb_file}")
    fig.show(config=config)
    # imagefile = os.path.join(target_workspace, "eyeplot.jpeg")
    # fig.write_image(imagefile)
    print("====Analysis Successfully Completed====")
```

On this page

[Previous

Example sipro automation](ex_sipro_automation.md)
[Next

Example sipro SI](ex_sipro_example_si.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top