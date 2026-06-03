<!-- 来源: Examples\ex_odbpp_simulate_pipro_dc.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example odbpp simulate pipro dc

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_odbpp_simulate_pipro_dc.rst.txt)

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
  + Example odbpp simulate pipro dc
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

# Example odbpp simulate pipro dc[](#example-odbpp-simulate-pipro-dc "Link to this heading")

This example demonstrates how to import an ODB++ file and setup a PIPro DC simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2025 Keysight Technologies, Keysight Confidential
from argparse import ArgumentParser
import os
from pathlib import Path

from keysight.edatoolbox import ads, momentum, util, xxpro

try:
    import empro
    import empro.toolkit
    import empro.toolkit.analysis
    from empro.toolkit.analysis.dc import output
    from empro.toolkit.analysis.dc.results import DCResult
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
    output_dir = Path(args.output_dir).absolute()
    util.safe_makedirs(args.output_dir)

    # Path to the ODB++ file
    odb_file = Path(__file__).parent / "data" / "Minipc" / "minipc_pm_v0_pm.zip"
    cell_name = "minipc_pm"
    lib_name = f"{cell_name}_lib"
    tech_lib_name = f"{cell_name}_tech_lib"
    component_lib_name = f"{cell_name}_component_lib"
    target_workspace_name = f"{cell_name}_wrk"
    target_workspace_path = output_dir / target_workspace_name
    target_workspace = str(target_workspace_path)

    assert odb_file.exists(), f"ODB++ file {odb_file} does not exist!"
    assert output_dir.exists(), f"Output directory {output_dir} does not exist!"
    assert not target_workspace_path.exists(), (
        f"Target workspace {target_workspace} already exists!"
    )

    print(f"Input ODB++: {odb_file}")
    print(f"Target workspace: {target_workspace}")

    # Step 1: Creating the ADS application object
    ads_application = ads.ADS()
    print("ADS application created")
    print("Creating workspace")
    if not target_workspace_path.exists():
        ads_application.create_workspace(output_dir, target_workspace_name)

    # Step 2: Import odb++ file

    print("Importing ODB++")
    ads_application.import_odbpp(
        target_workspace,
        odb_file,
        library=lib_name,
        cell=cell_name,
        use_legacy_importer=False,
    )
    print("ODB++ imported")

    # update the material database
    matdb_path = str(target_workspace_path / tech_lib_name / "materials.matdb")
    matdb = ads.MaterialDatabase(matdb_path)
    for diel in matdb.dielectrics:
        eps_r = float(diel.er_real)
        if eps_r <= 0.0:
            diel.er_real = 4.0
    matdb.write(matdb_path)

    # update the thickness of metal layers
    subst_path = str(target_workspace_path / tech_lib_name / f"{cell_name}.subst")
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

    input_lcv = ads.LibraryCellView(library=lib_name, cell=cell_name, view="layout")
    pro_lcv = ads.LibraryCellView(library=lib_name, cell=cell_name, view="sipi1")

    # Step 3: Creating the SIPro view
    print("Creating PIPro simulation view")
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate=cell_name,
        pro_lcv=pro_lcv,
        tool="sipi",
        substrate_library=tech_lib_name,
    )
    print("PIPro simulation view created")

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
        analysis.name = "DC by Script"
        analysis.analysisType = empro.analysis.Analysis.DCAnalysisType

        # Set VRM List
        vrmList = analysis.vrms

        plusPins = ["Q4.1", "Q4.2", "Q4.3"]
        minusPins = ["C3.1", "Q6.2"]
        vrm = empro.toolkit.analysis.createVrmFromPins(plusPins, minusPins)
        vrm.name = "PLL_1V8_Q4"
        vrm.resistance = empro.core.Expression("0 Ohm")
        vrm.tolerance = empro.core.Expression("0.01")
        vrm.outputVoltagePositiveVariation = empro.core.Expression("0.00")
        vrm.outputVoltageNegativeVariation = empro.core.Expression("0.00")
        vrm.inductance = empro.core.Expression("0 mH")
        vrm.voltage = empro.core.Expression("1.5 V")
        vrm.sourceType = "PackagedVrm"
        vrm.hasSenseLine = False
        vrmList.append(vrm)

        # Set Sink List
        sinkList = analysis.sinks

        plusPins = [
            "U1.AB14",
            "U1.AC14",
            "U1.AC16",
            "U1.AC17",
            "U1.AC19",
            "U1.AC21",
            "U1.AD27",
            "U1.AE18",
            "U1.AH27",
            "U1.AM27",
            "U1.D27",
            "U1.H27",
            "U1.M27",
            "U1.T27",
            "U1.U15",
            "U1.U16",
            "U1.U17",
            "U1.U20",
            "U1.U21",
            "U1.U22",
            "U1.W19",
            "U1.Y27",
        ]
        minusPins = [
            "U1.A6",
            "U1.A11",
            "U1.A16",
            "U1.A21",
            "U1.A27",
            "U1.A29",
            "U1.A30",
            "U1.A31",
            "U1.A34",
            "U1.A35",
            "U1.A38",
            "U1.AA1",
            "U1.AA11",
            "U1.AA17",
            "U1.AA21",
            "U1.AA26",
            "U1.AA27",
            "U1.AA28",
            "U1.AA29",
            "U1.AA30",
            "U1.AA31",
            "U1.AA34",
            "U1.AA35",
            "U1.AA38",
            "U1.AA39",
            "U1.AB3",
            "U1.AB8",
            "U1.AB13",
            "U1.AB18",
            "U1.AB23",
            "U1.AB26",
            "U1.AB27",
            "U1.AB32",
            "U1.AB33",
            "U1.AB36",
            "U1.AB37",
            "U1.AC10",
            "U1.AC15",
            "U1.AC20",
            "U1.AC22",
            "U1.AC25",
            "U1.AC27",
            "U1.AC28",
            "U1.AC29",
            "U1.AC30",
            "U1.AC31",
            "U1.AC34",
            "U1.AC35",
            "U1.AC38",
            "U1.AC39",
            "U1.AD2",
            "U1.AD12",
            "U1.AD26",
            "U1.AD32",
            "U1.AD33",
            "U1.AD36",
            "U1.AD37",
            "U1.AE4",
            "U1.AE9",
            "U1.AE19",
            "U1.AE24",
            "U1.AE26",
            "U1.AE27",
            "U1.AE30",
            "U1.AE31",
            "U1.AE34",
            "U1.AE35",
            "U1.AE38",
            "U1.AE39",
            "U1.AF1",
            "U1.AF6",
            "U1.AF11",
            "U1.AF16",
            "U1.AF26",
            "U1.AF27",
            "U1.AF30",
            "U1.AF31",
            "U1.AF32",
            "U1.AF33",
            "U1.AF34",
            "U1.AF35",
            "U1.AF36",
            "U1.AF37",
            "U1.AG3",
            "U1.AG13",
            "U1.AG18",
            "U1.AG23",
            "U1.AG26",
            "U1.AG27",
            "U1.AG30",
            "U1.AG31",
            "U1.AG34",
            "U1.AG35",
            "U1.AG38",
            "U1.AG39",
            "U1.AH10",
            "U1.AH15",
            "U1.AH20",
            "U1.AH26",
            "U1.AH32",
            "U1.AH33",
            "U1.AH36",
            "U1.AH37",
            "U1.AJ2",
            "U1.AJ7",
            "U1.AJ12",
            "U1.AJ17",
            "U1.AJ22",
            "U1.AJ27",
            "U1.AJ28",
            "U1.AJ29",
            "U1.AJ30",
            "U1.AJ31",
            "U1.AJ34",
            "U1.AJ35",
            "U1.AJ38",
            "U1.AJ39",
            "U1.AK4",
            "U1.AK27",
            "U1.AK32",
            "U1.AK33",
            "U1.AK36",
            "U1.AK37",
            "U1.AL1",
            "U1.AL16",
            "U1.AL27",
            "U1.AL30",
            "U1.AL31",
            "U1.AL34",
            "U1.AL35",
            "U1.AL38",
            "U1.AL39",
            "U1.AM3",
            "U1.AM15",
            "U1.AM23",
            "U1.AM26",
            "U1.AM32",
            "U1.AM33",
            "U1.AM36",
            "U1.AM37",
            "U1.AN5",
            "U1.AN10",
            "U1.AN15",
            "U1.AN20",
            "U1.AN27",
            "U1.AN30",
            "U1.AN31",
            "U1.AN34",
            "U1.AN35",
            "U1.AN38",
            "U1.AN39",
            "U1.AP2",
            "U1.AP7",
            "U1.AP12",
            "U1.AP14",
            "U1.AP27",
            "U1.AP32",
            "U1.AP33",
            "U1.AP36",
            "U1.AP37",
            "U1.AR4",
            "U1.AR9",
            "U1.AR14",
            "U1.AR15",
            "U1.AR19",
            "U1.AR27",
            "U1.AR30",
            "U1.AR31",
            "U1.AR34",
            "U1.AR35",
            "U1.AR38",
            "U1.AR39",
            "U1.AT1",
            "U1.AT6",
            "U1.AT11",
            "U1.AT16",
            "U1.AT27",
            "U1.AT28",
            "U1.AT29",
            "U1.AT32",
            "U1.AT33",
            "U1.AT36",
            "U1.AT37",
            "U1.AU3",
            "U1.AU8",
            "U1.AU13",
            "U1.AU18",
            "U1.AU23",
            "U1.AU29",
            "U1.AU30",
            "U1.AU31",
            "U1.AU34",
            "U1.AU35",
            "U1.AU38",
            "U1.AU39",
            "U1.AV5",
            "U1.AV10",
            "U1.AV15",
            "U1.AV20",
            "U1.AV25",
            "U1.AV31",
            "U1.AV32",
            "U1.AV33",
            "U1.AV36",
            "U1.AV37",
            "U1.AW7",
            "U1.AW12",
            "U1.AW17",
            "U1.AW22",
            "U1.AW27",
            "U1.AW29",
            "U1.AW31",
            "U1.AW34",
            "U1.AW35",
            "U1.AW38",
            "U1.B2",
            "U1.B3",
            "U1.B8",
            "U1.B13",
            "U1.B17",
            "U1.B18",
            "U1.B23",
            "U1.B25",
            "U1.B27",
            "U1.B28",
            "U1.B29",
            "U1.B32",
            "U1.B33",
            "U1.B36",
            "U1.B37",
            "U1.C5",
            "U1.C10",
            "U1.C15",
            "U1.C20",
            "U1.C27",
            "U1.C28",
            "U1.C29",
            "U1.C30",
            "U1.C31",
            "U1.C34",
            "U1.C35",
            "U1.C38",
            "U1.C39",
            "U1.D2",
            "U1.D7",
            "U1.D12",
            "U1.D15",
            "U1.D17",
            "U1.D22",
            "U1.D26",
            "U1.D30",
            "U1.D31",
            "U1.D32",
            "U1.D33",
            "U1.D36",
            "U1.D37",
            "U1.E4",
            "U1.E9",
            "U1.E14",
            "U1.E19",
            "U1.E27",
            "U1.E30",
            "U1.E31",
            "U1.E32",
            "U1.E33",
            "U1.E34",
            "U1.E35",
            "U1.E38",
            "U1.E39",
            "U1.F1",
            "U1.F6",
            "U1.F11",
            "U1.F16",
            "U1.F21",
            "U1.F27",
            "U1.F30",
            "U1.F31",
            "U1.F32",
            "U1.F33",
            "U1.F36",
            "U1.F37",
            "U1.G3",
            "U1.G18",
            "U1.G23",
            "U1.G27",
            "U1.G30",
            "U1.G31",
            "U1.G32",
            "U1.G33",
            "U1.G34",
            "U1.G35",
            "U1.G38",
            "U1.G39",
            "U1.H5",
            "U1.H10",
            "U1.H15",
            "U1.H26",
            "U1.H30",
            "U1.H31",
            "U1.H32",
            "U1.H33",
            "U1.H36",
            "U1.H37",
            "U1.J2",
            "U1.J7",
            "U1.J17",
            "U1.J27",
            "U1.J30",
            "U1.J31",
            "U1.J32",
            "U1.J33",
            "U1.J34",
            "U1.J35",
            "U1.J38",
            "U1.J39",
            "U1.K27",
            "U1.K32",
            "U1.K33",
            "U1.K36",
            "U1.K37",
            "U1.L1",
            "U1.L16",
            "U1.L21",
            "U1.L27",
            "U1.L30",
            "U1.L31",
            "U1.L34",
            "U1.L35",
            "U1.L38",
            "U1.L39",
            "U1.M3",
            "U1.M13",
            "U1.M18",
            "U1.M23",
            "U1.M26",
            "U1.M32",
            "U1.M33",
            "U1.M36",
            "U1.M37",
            "U1.N5",
            "U1.N10",
            "U1.N15",
            "U1.N21",
            "U1.N26",
            "U1.N27",
            "U1.N30",
            "U1.N31",
            "U1.N34",
            "U1.N35",
            "U1.N38",
            "U1.N39",
            "U1.P2",
            "U1.P7",
            "U1.P12",
            "U1.P17",
            "U1.P26",
            "U1.P27",
            "U1.P32",
            "U1.P33",
            "U1.P36",
            "U1.P37",
            "U1.R9",
            "U1.R19",
            "U1.R24",
            "U1.R26",
            "U1.R27",
            "U1.R30",
            "U1.R31",
            "U1.R34",
            "U1.R35",
            "U1.R38",
            "U1.R39",
            "U1.T1",
            "U1.T11",
            "U1.T16",
            "U1.T21",
            "U1.T26",
            "U1.T32",
            "U1.T33",
            "U1.T36",
            "U1.T37",
            "U1.U3",
            "U1.U8",
            "U1.U13",
            "U1.U18",
            "U1.U23",
            "U1.U27",
            "U1.U30",
            "U1.U31",
            "U1.U34",
            "U1.U35",
            "U1.U38",
            "U1.U39",
            "U1.V10",
            "U1.V15",
            "U1.V20",
            "U1.V25",
            "U1.V26",
            "U1.V27",
            "U1.V32",
            "U1.V33",
            "U1.V36",
            "U1.V37",
            "U1.W2",
            "U1.W7",
            "U1.W12",
            "U1.W17",
            "U1.W22",
            "U1.W26",
            "U1.W27",
            "U1.W30",
            "U1.W31",
            "U1.W34",
            "U1.W35",
            "U1.W38",
            "U1.W39",
            "U1.Y9",
            "U1.Y15",
            "U1.Y19",
            "U1.Y24",
            "U1.Y26",
            "U1.Y32",
            "U1.Y33",
            "U1.Y36",
            "U1.Y37",
        ]
        sink = empro.toolkit.analysis.createSinkFromPins(plusPins, minusPins)
        sink.name = "PLL_1V8_U1"
        sink.resistance = empro.core.Expression("1 MOhm")
        sink.positiveTolerance = empro.core.Expression("0.05")
        sink.negativeTolerance = empro.core.Expression("0.05")
        sink.current = empro.core.Expression("3 A")
        sink.pinCurrentModel = "EqualVoltage"

        sink.packageModel = None
        sinkList.append(sink)

        # Set Netlist
        netList = analysis.nets

        net = empro.analysis.Net("GND", empro.activeProject.geometry[0])
        netList.append(net)

        net = empro.analysis.Net("PLL_1V8", empro.activeProject.geometry[0])
        netList.append(net)

        # Set Component Model Group List
        componentModelGroupList = analysis.componentModelGroups

        # Create Component Model Group
        componentModelGroup = empro.analysis.ComponentModelGroup(
            f"{component_lib_name}:grm033r60j104ke19d_capc0603x33x15ll03t05",
            empro.activeProject.geometry[0],
        )
        componentModelGroup.name = "grm033r60j104ke19d_capc0603x33x15ll03t05"
        componentModelGroup.arrayedComponent = False
        componentModelGroup.updateableAfterSimulation = True
        pinNamePortNumberPairs = (("1", -1), ("2", 1))
        pinPortMap = componentModelGroup.pinPortMap()
        pinPortMap.update(pinNamePortNumberPairs)
        instances = [
            "C424",
            "C425",
            "C426",
            "C427",
            "C428",
            "C429",
            "C430",
            "C431",
            "C432",
            "C433",
            "C434",
            "C435",
            "C436",
            "C437",
            "C438",
            "C439",
            "C440",
            "C441",
            "C442",
            "C443",
            "C444",
        ]
        for instance in instances:
            componentModelGroup.appendInstance(
                empro.toolkit.analysis.createComponentInstanceFromInstance(instance)
            )

        # Create Component Model
        componentModel = empro.analysis.ComponentModel(
            1, ""
        )  # LumpedType = 1, ModelDBType = 2, SnPType = 3, LibCell = 4
        componentModel.name = "model"
        componentModel.getPassiveLoad().impedance.resistance = empro.core.Expression(
            "0 Ohm"
        )
        componentModel.getPassiveLoad().impedance.capacitance = empro.core.Expression(
            "0.1 uF"
        )
        componentModel.getPassiveLoad().impedance.inductance = empro.core.Expression(
            "0 H"
        )
        componentModel.getPassiveLoad().impedance.elementArrangement = "Series"
        componentModelGroup.appendModel(componentModel)
        componentModelGroupList.append(componentModelGroup)

        # Create Component Model Group
        componentModelGroup = empro.analysis.ComponentModelGroup(
            f"{component_lib_name}:grm31cr60j107me39l_capc3216x190x55ml30t25",
            empro.activeProject.geometry[0],
        )
        componentModelGroup.name = "grm31cr60j107me39l_capc3216x190x55ml30t25"
        componentModelGroup.arrayedComponent = False
        componentModelGroup.updateableAfterSimulation = True
        pinNamePortNumberPairs = (("1", -1), ("2", 1))
        pinPortMap = componentModelGroup.pinPortMap()
        pinPortMap.update(pinNamePortNumberPairs)
        instances = ["C423"]
        for instance in instances:
            componentModelGroup.appendInstance(
                empro.toolkit.analysis.createComponentInstanceFromInstance(instance)
            )

        # Create Component Model
        componentModel = empro.analysis.ComponentModel(
            1, ""
        )  # LumpedType = 1, ModelDBType = 2, SnPType = 3, LibCell = 4
        componentModel.name = "model"
        componentModel.getPassiveLoad().impedance.resistance = empro.core.Expression(
            "0 Ohm"
        )
        componentModel.getPassiveLoad().impedance.capacitance = empro.core.Expression(
            "100 uF"
        )
        componentModel.getPassiveLoad().impedance.inductance = empro.core.Expression(
            "0 H"
        )
        componentModel.getPassiveLoad().impedance.elementArrangement = "Series"
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

        plan = empro.simulation.FrequencyPlan()
        plan.type = "Adaptive"
        plan.startFrequency = empro.core.Expression("10 kHz")
        plan.stopFrequency = empro.core.Expression("300 MHz")
        plan.numberOfFrequencyPoints = 300
        plan.samplePointsLimit = 300
        plan.pointsPerDecade = 5
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
        femMeshSettings.useMeshDomainOptimization = False
        femMeshSettings.minimumNumberOfPasses = 1
        femMeshSettings.maximumNumberOfPasses = 1
        femMeshSettings.refineAtSpecificFrequency = False
        femMeshSettings.refinementFrequency = empro.core.Expression("10 GHz")

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

        print("Simulation complete, IR drop per sink:")
        dc_result = DCResult(active_analysis)

        for sink in dc_result.sinks:
            irDrop = sink.vrmOutputVoltage - sink.inputVoltage
            print(f"{sink.name}: {irDrop * 1000:2.2f} mV")

        if ads_application.version >= 591:  # >= ADS 2024
            print("DC report generation in progress...")
            # HTML Report
            output.exportDCResultstoHtml(
                dc_result,
                directory=target_workspace,
                report_name="DCReport",
                open_report=True,
            )
            # Docx Report
            output.exportDCResultstoDocx(
                dc_result,
                directory=target_workspace,
                report_name="DCReport",
                open_report=True,
            )
            print("DC report generated")
    print("====Analysis Successfully Completed====")
```

On this page

[Previous

Example odbpp simulate pipro ac reuse sio](ex_odbpp_simulate_pipro_ac_reuse_sio.md)
[Next

Example odbpp simulate rfpro](ex_odbpp_simulate_rfpro.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top