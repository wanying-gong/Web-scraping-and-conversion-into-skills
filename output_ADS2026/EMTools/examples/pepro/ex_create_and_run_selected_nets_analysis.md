<!-- 来源: examples\pepro\ex_create_and_run_selected_nets_analysis.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [EM Tools Python Documentation](../../index.md)
* [Examples](../index.md)
* [PEPro Examples](index.md)
* Creates a new selected nets type analysis in pepro View and run the simulation.

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../../intro/index.md)
* [Reference](../../reference/index.md)
  + [keysight.ads.emtools](../../reference/emtools.md)
* [Examples](../index.md)
  + [RFPro Examples](../rfpro/index.md)
    - [Create RFPro View](../rfpro/ex_create_rfpro_view.md)
    - [Get the Substrate from an EM Setup View](../rfpro/ex_get_emsetup_substrate_info.md)
    - [Convert EM Setup to RFPro View](../rfpro/ex_convert_emsetup_to_rfpro_view.md)
  + [PEPro Examples](index.md)
    - [Creates a new pepro View](ex_create_pepro_view.md)
    - [Run existing PEPro analysis persent in workspace.](ex_run_pepro_sim.md)
    - Creates a new selected nets type analysis in pepro View and run the simulation.
    - [Creates a new pe thermal analysis in pepro View and run the simulation.](ex_create_and_run_thermal_analysis.md)

# Creates a new selected nets type analysis in pepro View and run the simulation.[](#creates-a-new-selected-nets-type-analysis-in-pepro-view-and-run-the-simulation "Link to this heading")

This example creates a new pepro(pepro1) view in workspace.

1. Find the PEPro view in the workspace.
2. Create a new selected nets type analysis in the pepro view.
3. Runs the new analysis.

```
# Copyright Keysight Technologies 2025

"""
This example demonstrates how to create a new slected nets analysis in pepro and run that simualtion
using Python APIs provided by Keysight Advanced Design System (ADS).
"""
import keysight.edatoolbox.multi_python as multi_python
import os
import shutil
from pathlib import Path

def ads_find_pepro_view_in_workspace(
    example_dir: str,
    workspace_name: str,
    library_name: str,
    cell_name: str,
    pepro_view_name: str,
) -> None:
    """
    Find the PEPro view for the given workspace, library and cell.
    """
    import keysight.ads.de as de #due to multi_python context manager issue moved import here

    workspace_dir = Path(workspace_name)
    if workspace_dir.exists():
        print(f"Removing existing workspace: {workspace_dir}")
        shutil.rmtree(workspace_dir)

    archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
    print(f"Unarchiving Workspace: {archive_file} in current working directory: {os.getcwd()}")
    de.unarchive_file(archive_file, ".")
    print(f"Opening workspace: {workspace_dir}")
    workspace = de.open_workspace(workspace_name)
    library = de.Library.get(library_name)
    cell = library.cell(cell_name)
    print("found pepro view in workspace")
    if not cell.view_exists(pepro_view_name):
        raise RuntimeError(f"The pepro view {pepro_view_name} does not exist.")
    workspace.close()

def create_and_run_selected_nets_analysis(workspace_path: str,library_name: str,cell_name: str,substrate_name: str,pepro_view: str,pepro_analyis_name: str,timeout: int):
    import empro #due to multi_python context manager issue moved import here
    from empro.toolkit import simulation #due to multi_python context manager issue moved import here
    import empro.toolkit.analysis as pepro #due to multi_python context manager issue moved import here
    print(f"Loading the pepro view: {pepro_view}")
    pepro.loadDesign(
        path=os.path.join(os.getcwd(), workspace_path),
        lib=library_name,
        subst=substrate_name,
        cell=cell_name,
        layout_view="layout",
        sipi_view=pepro_view,)
    # Create an Analysis
    import empro
    # Create an Analysis
    analysis = empro.analysis.Analysis()
    analysis.name = 'Selected-NetsAnalysis'
    analysis.analysisType = empro.analysis.Analysis.EMUDPEAnalysisType

    # Set PortList
    portList = analysis.ports

    plusPins = ['U']
    minusPins = ['Reference Pin On Cover']
    port = empro.toolkit.analysis.createPortFromPins(plusPins,minusPins)
    port.name = 'U'
    port.referenceImpedance = empro.core.Expression('50 Ohm')
    port.feedType = 'Auto'
    portList.append(port)

    # Set Netlist
    netList = analysis.nets

    net = empro.analysis.Net('P7', empro.activeProject.geometry[0])
    netList.append(net)

    net = empro.analysis.Net('U', empro.activeProject.geometry[0])
    netList.append(net)

    # Set Component Model Group List
    componentModelGroupList = analysis.componentModelGroups

    # Create Component Model Group
    componentModelGroup = empro.analysis.ComponentModelGroup('Power_module_lib:imw65r057m1h_l1_3T_pemb', empro.activeProject.geometry[0])
    componentModelGroup.name = 'imw65r057m1h_l1_3T_pemb'
    componentModelGroup.arrayedComponent = False
    componentModelGroup.updateableAfterSimulation = True
    pinNamePortNumberPairs = (('P1', 1), ('P2', 2), ('P3', 3), ('Reference Pin On Cover', 0))
    pinPortMap = componentModelGroup.pinPortMap()
    pinPortMap.update(pinNamePortNumberPairs)
    instances = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6']
    for instance in instances:
        componentModelGroup.appendInstance(empro.toolkit.analysis.createComponentInstanceFromInstance(instance))

    # Create Component Model
    componentModel = empro.analysis.ComponentModel(4, 'Power_module_lib:imw65r057m1h_l1_3T_pemb') # LibCell = 4
    componentModel.name = 'model'
    componentModel.viewName = 'symbol'
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
    try:
        frequencyPlanList._frequencyPlanType = 'NoInterpolating_AllFields'
    except:
        print("New frequencyplan features are not available prior to 2023.20")
        pass

    plan = empro.simulation.FrequencyPlan()
    try:
        plan.computeType = 'Simulated'
        plan.sweepType = 'Linear'
        plan.nearFieldType = 'NoNearFields'
        plan.farFieldType = 'NoFarFields'
    except:
        plan.type = 'Linear'
        plan.enabled = True
    plan.startFrequency = empro.core.Expression('10 kHz')
    plan.stopFrequency = empro.core.Expression('500 MHz')
    plan.numberOfFrequencyPoints = 5
    plan.samplePointsLimit = 300
    plan.pointsPerDecade = 20
    frequencyPlanList.append(plan)

    # Set frequency plan global settings
    options.nearFieldsSaveFor = 'AsDefinedByFrequencyPlans'
    options.farFieldsSaveFor = 'AsDefinedByFrequencyPlans'
    options.farFieldAngularResolution = empro.core.Expression('5 deg')
    options.adaptiveFpMaxSamples = 300
    options.adaptiveFpSaveFieldsFor = 'AllFrequencies'
    # Set Simulator
    # Set Preset Simulator Setup By Name
    options.setPresetByName('FEM')
    # Set User-Defined Advanced Simulator Setup
    # Set FEM Options
    # Set FEM Mesh Settings
    femMeshSettings = options.femMeshSettings
    femMeshSettings.includeResistiveLossesInGround = True
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

    print("Created Analysis: Selected-NetsAnalysis by Script")
    # Run the Analysis
    analyses = empro.activeProject.analyses
    for analysis in analyses:
        if analysis.name == pepro_analyis_name:
            print(analysis.name)
            setup = analysis
            break
    if not setup:
        raise RuntimeError(f"The pepro analysis {pepro_analyis_name} does not exist.")
    print(f"Running the pepro analysis: {pepro_analyis_name}..")
    try:
        pepro.runAnalysis(setup, waitForConfirmation=False, saveProject=True)
        if timeout:
            print(f"waiting for {timeout} secs...")
        simulation.wait(pepro.getSimulation(setup), timeout)
        print("Simulation completed.")
        sim = pepro.getSimulation(setup)
        print(f"Simulation Status: {sim.status}")
    except simulation.TimeOutError as error:
        print(f"Simulation timed out: {error}")
    except RuntimeError as error:
        print(f"Runtime error occured: {error}")
    finally:
        print(f"simulation path = {setup.simulationPath}")
        print("Done\n")

if __name__ == "__main__":
    EXAMPLE_DIR = "examples/PE"
    WORKSPACE_NAME= "Power_module_wrk"
    WORKSPACE_PATH = "Power_module_wrk"
    LIBRARY_NAME = "Power_module_lib"
    CELL_NAME = "SiC_intelligent_power_module"
    SUBSTRATE_NAME = "tech.subst"
    PEPRO_VIEW_NAME = "pepro"
    PEPRO_ANALYSIS_NAME = "Selected-NetsAnalysis"
    TIMEOUT = 10 * 60  # 10 minutes
    with multi_python.ads_context() as ads_ctx:
        ads_ctx.call(
                ads_find_pepro_view_in_workspace,
                args=[
                    EXAMPLE_DIR,
                    WORKSPACE_NAME,
                    LIBRARY_NAME,
                    CELL_NAME,
                    PEPRO_VIEW_NAME,
                ],
            )
    with multi_python.xxpro_context() as empro_ctx:
        empro_ctx.call(
            create_and_run_selected_nets_analysis,
            args=[
                WORKSPACE_PATH,
                LIBRARY_NAME,
                CELL_NAME,
                SUBSTRATE_NAME,
                PEPRO_VIEW_NAME,
                PEPRO_ANALYSIS_NAME,
                TIMEOUT,
            ],
        )
```

On this page

[Previous

Run existing PEPro analysis persent in workspace.](ex_run_pepro_sim.md)
[Next

Creates a new pe thermal analysis in pepro View and run the simulation.](ex_create_and_run_thermal_analysis.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top