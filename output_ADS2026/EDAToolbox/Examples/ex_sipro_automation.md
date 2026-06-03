<!-- 来源: Examples\ex_sipro_automation.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example sipro automation

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_sipro_automation.rst.txt)

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
  + Example sipro automation
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

# Example sipro automation[](#example-sipro-automation "Link to this heading")

This example demonstartes how to run an SIPro SI simulation starting from an ODB++.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2025 Keysight Technologies, Keysight Confidential
#
"""Create and execute SIPro analyses based on an input .csv file."""

from argparse import ArgumentParser
from collections import defaultdict
import json
import os
from pathlib import Path
import re

from keysight.edatoolbox import ads, momentum, util, xxpro

SIGNAL_INDEX = 0
SIGNAL_POLARITY = 1

try:
    # import empro stuff for this specific sipro simulation
    import empro
    import empro.toolkit
    import empro.toolkit.analysis

except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using the Python"
        " from EMPro.  Use it by launching emproenv.bat/.sh"
    )
    raise

def get_inst_pins_on_net(project, netName):
    """Get all pins of instances connected to a net."""
    instPinsOnNet = []
    for inst in project.layout.instances:
        for pin in inst.pins():
            if pin.netName == netName:
                instPinsOnNet.append((inst, pin))
    return instPinsOnNet

def pin_to_pin_distance(pinPos1, pinPos2, precision=8):
    """Calculate the distance between two pins."""
    import math

    return round(
        math.sqrt(
            (pinPos1.x - pinPos2.x) ** 2
            + (pinPos1.y - pinPos2.y) ** 2
            + (pinPos1.z - pinPos2.z) ** 2
        ),
        precision,
    )

def get_closest_ref_pin_on_ground(instAndInstPinPair, sameInstanceOnly, project):
    """Get the closest reference pin on ground."""
    groundNetNames = {
        net.name for net in project.layout.nets if net.type == empro.geometry.Net.GROUND
    }
    inst = instAndInstPinPair[0]
    instPin = instAndInstPinPair[1]
    distDictionary = defaultdict(list)
    if sameInstanceOnly:
        for pin in inst.pins():
            if pin.netName in groundNetNames:
                dist = pin_to_pin_distance(instPin.dotPosition, pin.dotPosition)
                distDictionary[dist].append((inst, pin))
    else:
        for inst in project.layout.instances:
            for pin in inst.pins():
                if pin.netName in groundNetNames:
                    dist = pin_to_pin_distance(instPin.dotPosition, pin.dotPosition)
                    distDictionary[dist].append((inst, pin))

    if len(distDictionary) > 0:
        distDictionary = sorted(distDictionary.items(), key=lambda x: x[0])
        return distDictionary[0]
    return []

def start_find_reference(project, targetNetName):
    """Find the reference pins on the target net."""
    allPins = []
    instPins = get_inst_pins_on_net(project, targetNetName)

    findInSameInstanceOnly = False
    for instAndInstPinPair in instPins:
        plusPins = []
        minusPins = []
        dist, instAndInstPinPairGnds = get_closest_ref_pin_on_ground(
            instAndInstPinPair, findInSameInstanceOnly, project
        )
        plusPins.append(instAndInstPinPair[0].name + "." + instAndInstPinPair[1].name)

        if len(instAndInstPinPairGnds) > 0:
            for instAndInstPinPairGnd in instAndInstPinPairGnds:
                minusPins.append(
                    instAndInstPinPairGnd[0].name + "." + instAndInstPinPairGnd[1].name
                )
            allPins.append(plusPins)
            allPins.append(minusPins)

    return allPins

def load_layout_in_project(project, lcv):
    """Create the SIPro layout."""
    projectLocation = empro.libCellViewProjectLocation(lcv.library, lcv.cell, lcv.view)
    defaultSimDir = empro.simulation.directoryForSimulations(projectLocation, False)
    oaDesignRefMap = empro.geometry._processViewSetupAndGetDesignRefMap(
        lcv.library, lcv.cell, lcv.view
    )

    # loads a lib/cell/view into a project
    # usually view=layout and there is only 1 layout,
    # but this can be extended to load multiple layouts at the same time

    project.location = projectLocation
    for key, oaDesignRef in oaDesignRefMap.items():
        # we need to use this special routine to allow the LTD file
        # to be picked up so the simulators can perform
        # simulations using it, important for encrypted workflows but also for Momentum
        layout = empro.geometry.OaLayout.readLayoutEx(
            oaDesignRef, key, os.path.join(defaultSimDir, "extra")
        )
        empro.activeProject.geometry.append(layout)

def create_workspace(
    workspace_path: str | Path,
    odbpp_file: str | Path,
    cell_name: str,
    library_name: str,
):
    """Create a workspace and import an ODB++ file into it."""
    workspace_path = Path(workspace_path).absolute()
    workspace_str = str(workspace_path)
    odbpp_file = Path(odbpp_file).absolute()

    # start running ADS and create workspace and import ODB++ file
    ads_application = ads.ADS()
    print("ADS application created ")

    # is not existing, create new workspace
    if not workspace_path.exists():
        ads_application.create_workspace(workspace_path.parent, workspace_path.stem)
        print(f"Created workspace {workspace_path}")

        print(f"Importing ODB++ {odbpp_file}")

        odbpp_import_options = ads.OdbImportOptions()
        odbpp_import_options.separate_component_lib = False
        odbpp_import_options.separate_tech_lib = False

        ads_application.import_odbpp(
            workspace_str,
            odbpp_file,
            library=library_name,
            cell=cell_name,
            use_legacy_importer=False,
            import_options=odbpp_import_options,
        )
        print("ODB++ imported ")

        # update the material database
        matdb_path = str(workspace_path / library_name / "materials.matdb")
        matdb = ads.MaterialDatabase(matdb_path)
        for diel in matdb.dielectrics:
            if diel.er_real <= 0.0:
                diel.er_real = 4.0
        matdb.write(matdb_path)

        # update the thickness of metal layers
        subst_path = str(workspace_path / library_name / "tech.subst")
        substrate_info = ads.SubstrateModel(subst_path)
        for layer in substrate_info.layers:
            if layer.layer == 1036:
                layer.thick = -1.761411  # negative thickness : below interface
            if layer.index == 8:
                layer.thick = 0.6654142

        # update the thickness of dielectric layers
        for material in substrate_info.materials:
            if material.index == 1:
                material.thick = 3.9371

        substrate_info.write(subst_path)

        print("Creating xxPro simulation view... ")
        input_lcv = ads.LibraryCellView(library_name, cell_name, "layout")

        pro_lcv = ads.LibraryCellView(library_name, cell_name, "sipro")

        ads_application.create_pro_view(
            workspace_str,
            input_lcv=input_lcv,
            substrate=cell_name,
            pro_lcv=pro_lcv,
            tool="sipi",
        )
        print("xxPro simulation view created!")

        # load library
        xxpro.use_workspace(workspace_str)

        with util.remember_cwd():
            # at this stage the view is still completely empty
            # we still need to load the requested layouts in it
            with empro.activeProject as project:
                load_layout_in_project(project, pro_lcv)

        momentum_dir = momentum.get_momentum_location()
        empro.toolkit.analysis.setMomentumDir(momentum_dir)
        print("Workspace created!")
    # if already existing workspace, open it
    else:
        xxpro.use_workspace(workspace_str)

        print(f"Workspace {workspace_path} already exists.")
        # Load the project
        empro.activeProject.loadActiveProjectFrom(library_name, cell_name, "sipro")
        momentum_dir = momentum.get_momentum_location()
        empro.toolkit.analysis.setMomentumDir(momentum_dir)
        print("Workspace loaded! ")
    empro.activeProject.saveActiveProject()

def create_analysis(
    net_definitions, start_freq, stop_freq, freq_pts, num_of_Sim, freq_type
):
    """Create an SIPro analysis."""
    with util.remember_cwd():
        layout = empro.activeProject.layout
        assert layout is not None
        analysis = empro.analysis.Analysis()
        analysis.name = f"Analysis {str(num_of_Sim)} by Script"
        analysis.analysisType = empro.analysis.Analysis.PASIAnalysisType
        print(f"{analysis.name} is now running")
        portList = analysis.ports
        netNames = ["GND"]

        for net_i in net_definitions:
            net_list = net_i.split(",")

            # given a range of nets
            if len(net_list) >= 3:
                net = net_list[0]
                print("Analyzing a range of nets")
                start_range = net_list[1]
                end_range = net_list[2]
                for i in range(int(start_range), int(end_range) + 1):
                    # find plus and minus pins
                    print(f"Creating ports for {net}{i}")
                    allPins = start_find_reference(empro.activeProject, net + str(i))
                    plusPins = [
                        allPins[index]
                        for index in filter(lambda x: x % 2 == 0, range(len(allPins)))
                    ]
                    minusPins = [
                        allPins[index]
                        for index in filter(lambda x: x % 2 == 1, range(len(allPins)))
                    ]

                    # create ports
                    for j in range(len(plusPins)):
                        port = empro.toolkit.analysis.createPortFromPins(
                            plusPins[j], minusPins[j]
                        )
                        for k in plusPins[j]:
                            ref, _ = k.split(".")
                            port.name = f"{net}{i}_{ref}"
                            portList.append(port)

                    # add net name into netNames array
                    netNames.append(f"{net}{i}")

            # given single nets in a line
            else:
                net = net_list[0]
                print(f"Creating ports for {net}")
                netNames.append(net)
                allPins = start_find_reference(empro.activeProject, net)
                plusPins = [
                    allPins[index]
                    for index in filter(lambda x: x % 2 == 0, range(len(allPins)))
                ]
                minusPins = [
                    allPins[index]
                    for index in filter(lambda x: x % 2 == 1, range(len(allPins)))
                ]

                for j in range(len(plusPins)):
                    port = empro.toolkit.analysis.createPortFromPins(
                        plusPins[j], minusPins[j]
                    )

                    for k in plusPins[j]:
                        ref, _ = k.split(".")
                        port.name = f"{net}_{ref}"
                        portList.append(port)

        # Build nets, add them to the analysis
        layout = empro.activeProject.geometry[0]
        net_list = analysis.nets
        for netName in netNames:
            net = empro.analysis.Net(netName, layout)
            net_list.append(net)

        # Create new frequency plan
        options = analysis.simulationSettings
        frequencyPlanList = options.femFrequencyPlanList()
        frequencyPlanList.clear()
        plan = empro.simulation.FrequencyPlan()
        plan.type = freq_type
        plan.startFrequency = start_freq
        plan.stopFrequency = stop_freq
        plan.numberOfFrequencyPoints = freq_pts
        plan.samplePointsLimit = freq_pts
        plan.enabled = True
        frequencyPlanList.append(plan)

        return analysis

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--output-dir",
        action="store",
        default=None,
        help="Location where the workspace will be created",
    )
    args = parser.parse_args()
    data_path = Path(__file__).parent / "data"
    input_file_location = data_path / "sample.txt"
    output_dir = Path(args.output_dir).absolute()
    util.safe_makedirs(args.output_dir)
    tgz_file = data_path / "sipro_sample_odb.tgz"
    cell_name = "sipro_sample_odb"
    library_name = f"{cell_name}_lib"
    target_workspace_name = f"{cell_name}_wrk"
    target_workspace_path = output_dir / target_workspace_name

    assert input_file_location.exists(), f"{input_file_location} does not exist"
    assert tgz_file.exists(), f"{tgz_file} does not exist"
    assert output_dir.exists(), f"{output_dir} does not exist"
    assert not target_workspace_path.exists(), f"{target_workspace_path} already exists"

    os.environ["HPEESOF_DIR"] = (
        ads.get_ads_location()
    )  # ensure the referenced env vars in lib.defs can be found

    # create workspace information
    create_workspace(
        target_workspace_path,
        odbpp_file=tgz_file,
        cell_name=cell_name,
        library_name=library_name,
    )

    # collect all information
    simSessionsList = []
    with open(input_file_location) as myfile:
        for jsonObj in myfile:
            tempData = json.loads(jsonObj)
            simSessionsList.append(tempData)

        for simData in simSessionsList:
            testId = simData["id"]
            net_definitions = []
            for signal_net in simData["signal_net"]:
                signal_name = signal_net["name"]
                signal_index = re.findall(r"\[(\w+:\w)\]", signal_name)
                filtered_name = re.sub(r"\[(\w+:\w)\]", "", signal_name)
                polarity_list = ["N", "P"]
                if 2 == len(signal_index):
                    start_index = int(signal_index[SIGNAL_INDEX].split(":")[0])
                    end_index = int(signal_index[SIGNAL_INDEX].split(":")[1]) + 1
                    net_definitions = [
                        "{}{}_{}".format(filtered_name, i, j)
                        for i in range(start_index, end_index)
                        for j in polarity_list
                    ]
                elif 1 == len(signal_index):
                    temp = signal_index[SIGNAL_INDEX].split(":")[0]
                    if temp.isdigit():
                        start_index = int(signal_index[SIGNAL_INDEX].split(":")[0])
                        end_index = int(signal_index[SIGNAL_INDEX].split(":")[1]) + 1
                        net_definitions = [
                            f"{filtered_name}{i}" for i in range(start_index, end_index)
                        ]
                    else:
                        net_definitions = [
                            f"{filtered_name}_{i}" for i in polarity_list
                        ]
                else:
                    net_definitions = filtered_name
            start_freq = float(simData["start_frequency"])
            stop_freq = float(simData["stop_frequency"])
            freq_pts = int(simData["frequency_points"])
            freq_type = simData["type"]
            num_of_Sim = len(empro.activeProject.analyses) + 1
            # create analysis
            analysis = create_analysis(
                net_definitions, start_freq, stop_freq, freq_pts, num_of_Sim, freq_type
            )

            # add analysis to project
            analyses = empro.activeProject.analyses
            analyses.append(analysis)
            analysis = analyses[-1]

            # run the analysis
            print(analysis.name, " running")
            empro.toolkit.analysis.runAnalysis(analysis, waitForConfirmation=False)
            print("Waiting on Simulation...")
            my_simulation = empro.toolkit.analysis.getSimulation(analysis)
            empro.toolkit.simulation.wait(my_simulation)
            empro.activeProject.saveActiveProject()

            # Possible simulation status: "Initialized", "Error", "Queued",
            # "Completed", "Killed", "Solving", "Unarchiving", "Unarchived",
            # "Killing", "Solved"
            # Will be added into an enum inside EDA Toolbox
            print("Simulation Done, Status: ", my_simulation.status)
            if my_simulation.status == "Completed":
                results = empro.analysis.CircuitResults(analysis)
                results.samplingConfig = empro.enparams.SamplingConfig(
                    freq_type, freq_pts
                )

                numPorts = results.numberOfPorts()
                freqs = results.frequencies()
                for p in range(numPorts):
                    for q in range(numPorts):
                        print(
                            [
                                results.Src(p, q, "ComplexMagnitude").at(freq_idx)
                                for freq_idx in range(len(freqs))
                            ]
                        )
            elif my_simulation.status == "Error":
                print("Simulation invalid because: ", my_simulation.reasonWhyInvalid())
            else:
                print("Done with Error!")

    print("Total number of simulations ", num_of_Sim)
```

On this page

[Previous

Example run schematic](ex_run_schematic.md)
[Next

Example sipro channelsim flow](ex_sipro_channelsim_flow.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top