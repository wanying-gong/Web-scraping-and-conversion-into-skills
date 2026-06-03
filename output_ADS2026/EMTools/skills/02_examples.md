# Examples
> **说明：** Examples 相关页面。

> **何时使用：** 当你需要查阅 Examples 相关内容时

---

## 本文件目录

- **Examples** (`examples/index.md`)
- **Creates a new selected nets type analysis in pepro View and run the simulation.** (`examples/pepro/ex_create_and_run_selected_nets_analysis.md`)
- **Creates a new pe thermal analysis in pepro View and run the simulation.** (`examples/pepro/ex_create_and_run_thermal_analysis.md`)
- **Creates a new pepro View** (`examples/pepro/ex_create_pepro_view.md`)
- **Run existing PEPro analysis persent in workspace.** (`examples/pepro/ex_run_pepro_sim.md`)
- **PEPro Examples** (`examples/pepro/index.md`)
- **Convert EM Setup to RFPro View** (`examples/rfpro/ex_convert_emsetup_to_rfpro_view.md`)
- **Create RFPro View** (`examples/rfpro/ex_create_rfpro_view.md`)
- **Get the Substrate from an EM Setup View** (`examples/rfpro/ex_get_emsetup_substrate_info.md`)
- **RFPro Examples** (`examples/rfpro/index.md`)

---

<!-- === 来源: examples/index.md === -->

# Examples[](#examples "Link to this heading")

The source code for the examples referenced by these help pages can be found in **$HPEESOF\_DIR/doc/python/emtools/automation/examples**

Contents:

* [RFPro Examples](rfpro/index.md)
  + [Create RFPro View](rfpro/ex_create_rfpro_view.md)
  + [Get the Substrate from an EM Setup View](rfpro/ex_get_emsetup_substrate_info.md)
  + [Convert EM Setup to RFPro View](rfpro/ex_convert_emsetup_to_rfpro_view.md)
* [PEPro Examples](pepro/index.md)
  + [Creates a new pepro View](pepro/ex_create_pepro_view.md)
  + [Run existing PEPro analysis persent in workspace.](pepro/ex_run_pepro_sim.md)
  + [Creates a new selected nets type analysis in pepro View and run the simulation.](pepro/ex_create_and_run_selected_nets_analysis.md)
  + [Creates a new pe thermal analysis in pepro View and run the simulation.](pepro/ex_create_and_run_thermal_analysis.md)


---

<!-- === 来源: examples/pepro/ex_create_and_run_selected_nets_analysis.md === -->

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


---

<!-- === 来源: examples/pepro/ex_create_and_run_thermal_analysis.md === -->

# Creates a new pe thermal analysis in pepro View and run the simulation.[](#creates-a-new-pe-thermal-analysis-in-pepro-view-and-run-the-simulation "Link to this heading")

Creates a new thermal analysis in pepro View and run the simulation.

1. Find the PEPro view in the workspace.
2. Create a new thermal analysis in the pepro view.
3. Runs the new analysis.

```
# Copyright Keysight Technologies 2025
"""
This example demonstrates how to create a new thermal analysis in pepro and run that simualtion
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
    analysis = empro.analysis.Analysis()
    analysis.name = 'Thermal analysis 2 by Script'
    analysis.analysisType = empro.analysis.Analysis.THAnalysisType

    # Set Thermal Component Group List
    thermalComponentGroupList = analysis.thermalComponentGroups

    # Create Thermal Component Group
    thermalComponentGroup = empro.analysis.ThermalComponentGroup('Power_module_lib:imw65r057m1h_l1_3T_pemb', empro.activeProject.geometry[0])

    thermalComponentGroup.thermalResistance =  empro.components.Package3RSpecification('1.13 K/W', '100 K/W', '20 K/W', 1, 1)

    thermalComponent = empro.toolkit.analysis.createThermalComponentFromInstance('X1')
    thermalComponent.heatSource = '0.429'
    thermalComponent.temperatureSource = '25 degC'
    thermalComponent.sourceType = 'HeatSource'
    thermalComponent.dissipationFactors = {}
    thermalComponentGroup.append(thermalComponent)

    thermalComponent = empro.toolkit.analysis.createThermalComponentFromInstance('X2')
    thermalComponent.heatSource = '0.429'
    thermalComponent.temperatureSource = '25 degC'
    thermalComponent.sourceType = 'HeatSource'
    thermalComponent.dissipationFactors = {}
    thermalComponentGroup.append(thermalComponent)

    thermalComponent = empro.toolkit.analysis.createThermalComponentFromInstance('X6')
    thermalComponent.heatSource = '0.298'
    thermalComponent.temperatureSource = '25 degC'
    thermalComponent.sourceType = 'HeatSource'
    thermalComponent.dissipationFactors = {}
    thermalComponentGroup.append(thermalComponent)
    thermalComponentGroupList.append(thermalComponentGroup)
    # Set Analysis Options
    options = analysis.simulationSettings
    # Set Ambient Conditions
    options.ambientConditions.backgroundTemperature = empro.core.Expression(298.15)
    # Set Frequency Plans
    # Set Frequency Plan List
    frequencyPlanList = options.femFrequencyPlanList()
    frequencyPlanList.clear()

    plan = empro.simulation.FrequencyPlan()
    plan.type = 'Automatic'
    plan.startFrequency = empro.core.Expression('10 kHz')
    plan.stopFrequency = empro.core.Expression('500 MHz')
    plan.numberOfFrequencyPoints = 300
    plan.samplePointsLimit = 300
    plan.pointsPerDecade = 20
    plan.enabled = True
    frequencyPlanList.append(plan)
    # Set Field Storage
    options.saveFieldsFor = 'NoFrequencies'
    options.farFieldEnabled = False
    options.farFieldAngularResolution = empro.core.Expression('5 deg')
    # Set Simulator
    # Set Preset Simulator Setup By Name
    options.preset = None
    # Set User-Defined Advanced Simulator Setup
    # Set FEM Options
    # Set FEM Mesh Settings
    femMeshSettings = options.femMeshSettings
    femMeshSettings.generation = empro.simulation.FemMeshSettings.Generation.GenerationAutomatic
    femMeshSettings.includeResistiveLossesInGround = True
    femMeshSettings.useTargetMeshSize = False
    femMeshSettings.autoTargetMeshSize = False
    femMeshSettings.targetMeshSize = empro.core.Expression('2 mm')
    femMeshSettings.useMeshDomainOptimization = False
    # Set Resources Settings
    resourceSettings = empro.simulation.LocalResourceSettings()
    resourceSettings.numberOfWorkers = 2
    resourceSettings.numberOfThreads = 0
    options.resourceSettings = resourceSettings
    # Set ParameterSweep
    options.parameterSweepEnabled = False
    options.parameterSequences.clear()
    # set thermal source import map
    analysis.thermalSourceImportMap = {'imw65r057m1h_l1_3T_pemb_X1': 'imw65r057m1h_l1_3T_pemb_X1',
    'imw65r057m1h_l1_3T_pemb_X2': 'imw65r057m1h_l1_3T_pemb_X2',
    'imw65r057m1h_l1_3T_pemb_X3': 'imw65r057m1h_l1_3T_pemb_X3',
    'imw65r057m1h_l1_3T_pemb_X4': 'imw65r057m1h_l1_3T_pemb_X4',
    'imw65r057m1h_l1_3T_pemb_X5': 'imw65r057m1h_l1_3T_pemb_X5',
    'imw65r057m1h_l1_3T_pemb_X6': 'imw65r057m1h_l1_3T_pemb_X6'}
    # Add the Analysis to the list of Analyses
    empro.activeProject.analyses.append(analysis)
    print("Created Analysis: Thermal analysis 2 by Script")
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
    PEPRO_ANALYSIS_NAME = "Thermal analysis 2 by Script"
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


---

<!-- === 来源: examples/pepro/ex_create_pepro_view.md === -->

# Creates a new pepro View[](#creates-a-new-pepro-view "Link to this heading")

This example shows how to creates a new pepro(pepro1) view.

1. Creates pepro view in workspace.

```
# Copyright Keysight Technologies 2025
"""
This example demonstrates how to create a new pepro view.
"""
from tempfile import gettempdir
import os
import shutil
from pathlib import Path
import keysight.ads.de as de
import keysight.ads.emtools as em

def create_pepro_view(example_dir : str, workspace_name : str, libray_name : str, cell_name : str):

    tempdir = gettempdir()
    print(f"Using temporary directory: {tempdir}")
    workspace_dir = Path(os.path.join(tempdir, workspace_name))
    if workspace_dir.exists():
        shutil.rmtree(workspace_dir)

    archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
    de.unarchive_file(archive_file, tempdir)
    workspace = de.open_workspace(workspace_dir)

    library = de.Library.get(libray_name)
    cell = library.cell(cell_name)
    if not cell.view_exists("pepro1"):
        print("creating pepro view")
        em.create_empro_view(
            (library.name, cell.name, "pepro1"), # pepro LCV
            "pepro", # tool
            (library.name, cell.name, "layout"), # layout LCV
            (library.name, "tech.subst") # substrate
            )
    else:
        print("pepro view already exists")

    workspace.close()

if __name__ == "__main__":

    create_pepro_view("examples/PE", "Power_module_wrk", "Power_module_lib", "SiC_intelligent_power_module")
    print("Done!")

```


---

<!-- === 来源: examples/pepro/ex_run_pepro_sim.md === -->

# Run existing PEPro analysis persent in workspace.[](#run-existing-pepro-analysis-persent-in-workspace "Link to this heading")

This example runs the analysis persent in existing pepro view.

1. Find the PEPro view in the workspace.
2. Run the analysis present in the existing PEPro view.

```
# Copyright Keysight Technologies
"""
This example uses existing ADS example "Power_module_wrk" to demonstrate how to run PEPro simulation.
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

def pepro_run_analysis(
    workspace_name: str,
    library_name: str,
    cell_name: str,
    substrate_name: str,
    pepro_view: str,
    pepro_analysis_name: str,
    timeout=0,
) -> int:
    """
    Run the existing PEPro analysis.
    """
    import os #due to multi_python context manager issue moved import here
    import empro    #due to multi_python context manager issue moved import here
    from empro.toolkit import simulation #due to multi_python context manager issue moved import here
    import empro.toolkit.analysis as pepro #due to multi_python context manager issue moved import here

    print(f"Loading the pepro view: {pepro_view}")
    pepro.loadDesign(
        path=os.path.join(os.getcwd(), workspace_name),
        lib=library_name,
        subst=substrate_name,
        cell=cell_name,
        layout_view="layout",
        sipi_view=pepro_view,
    )

    setup = None
    analyses = empro.activeProject.analyses
    for analysis in analyses:
        if analysis.name == pepro_analysis_name:
            print(analysis.name)
            setup = analysis
            break
    if not setup:
        raise RuntimeError(f"The pepro analysis {pepro_analysis_name} does not exist.")
    print(f"Running the pepro analysis: {pepro_analysis_name}")
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
    # PEPRO_ANALYSIS_NAME = "Thermal Analysis"
    PEPRO_ANALYSIS_NAME = "Parasitic Extraction-All Nets"
    TIMEOUT = 20 * 60  # 20 minutes

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
            pepro_run_analysis,
            args=[
                WORKSPACE_NAME,
                LIBRARY_NAME,
                CELL_NAME,
                SUBSTRATE_NAME,
                PEPRO_VIEW_NAME,
                PEPRO_ANALYSIS_NAME,
                TIMEOUT,
            ],
        )
```


---

<!-- === 来源: examples/pepro/index.md === -->

# PEPro Examples[](#pepro-examples "Link to this heading")

The source code for the examples referenced by these help pages can be found in **$HPEESOF\_DIR/doc/python/emtools/automation/examples**

Contents:

* [Creates a new pepro View](ex_create_pepro_view.md)
* [Run existing PEPro analysis persent in workspace.](ex_run_pepro_sim.md)
* [Creates a new selected nets type analysis in pepro View and run the simulation.](ex_create_and_run_selected_nets_analysis.md)
* [Creates a new pe thermal analysis in pepro View and run the simulation.](ex_create_and_run_thermal_analysis.md)


---

<!-- === 来源: examples/rfpro/ex_convert_emsetup_to_rfpro_view.md === -->

# Convert EM Setup to RFPro View[](#convert-em-setup-to-rfpro-view "Link to this heading")

This example shows how to create an RFPro view with an analysis created from an existing EM Setup view.

1. An RFPro view is created, if needed, in the python context of ADS.
2. An RFPro analysis is created from the EM Setup view in the python context of RFPro.

```
# Copyright Keysight Technologies 2025

def ads_find_emsetup_view_and_create_rfpro_view(example_dir : str, workspace_name : str, libray_name : str, cell_name : str) -> tuple [str:str]:
    from tempfile import gettempdir
    import os
    import shutil
    from pathlib import Path
    import keysight.ads.de as de
    import keysight.ads.emtools as em

    tempdir = gettempdir()
    workspace_dir = Path(os.path.join(tempdir, workspace_name))
    if workspace_dir.exists():
        shutil.rmtree(workspace_dir)

    archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
    de.unarchive_file(archive_file, tempdir)
    workspace = de.open_workspace(workspace_dir)

    library = de.Library.get(libray_name)
    cell = library.cell(cell_name)

    layout_view_name = "layout"
    emsetup_view_name = em.find_emsetup_view_name((libray_name, cell_name, layout_view_name))
    if not cell.view_exists(emsetup_view_name):
        raise RuntimeError(f"\"{library.name}:{cell.name}\" has no EM Setup view")
    (substrateLibraryName, substrateName) = em.get_substrate_info((libray_name, cell_name, emsetup_view_name))

    rfpro_view_name = "rfpro"
    if not cell.view_exists(rfpro_view_name):
        print("Creating the rfpro view")
        em.create_empro_view(
            (library.name, cell.name, rfpro_view_name), # rfpro LCV
            "rfpro", # tool
            (library.name, cell.name, layout_view_name), # layout LCV
            (substrateLibraryName, substrateName) # substrate LS
            )
    else:
        print("The rfpro view exists")
    workspace.close()

    return (emsetup_view_name, rfpro_view_name)

def rfpro_create_analysis_from_emsetup_view(workspace_name : str, libray_name : str, cell_name : str, rfpro_view_name : str, emsetup_view_name : str):
    import empro
    import empro.toolkit
    import keysight.edatoolbox.xxpro as xxpro
    import keysight.edatoolbox.ads as ads

    print("Opening the rfpro view...")
    xxpro.use_workspace(workspace_name)
    pro_lcv = ads.LibraryCellView(library=libray_name, cell=cell_name, view=rfpro_view_name)
    xxpro.load_pro_view(pro_lcv)
    with empro.activeProject as project:
        print("Creating an analysis from an EM Setup view...")
        analysis = empro.analysis.Analysis.fromEmSetup(emsetup_view_name)
        empro.activeProject.analyses.clear()
        empro.activeProject.analyses.append(analysis)
        project.saveActiveProject()

if __name__ == "__main__":

    EXAMPLE_DIR = "examples/EM/Antenna"
    WORKSPACE_NAME = "Single_patch_wrk"
    LIBRARY_NAME = "Single_patch_lib"
    CELL_NAME = "Single_patch"

    import keysight.edatoolbox.multi_python as multi_python

    with multi_python.ads_context() as ads_ctx:
        (emsetup_view_name, rfpro_view_name) = ads_ctx.call(ads_find_emsetup_view_and_create_rfpro_view, args=[EXAMPLE_DIR, WORKSPACE_NAME, LIBRARY_NAME, CELL_NAME])

    with multi_python.xxpro_context() as empro_ctx:
        empro_ctx.call(rfpro_create_analysis_from_emsetup_view, args=[WORKSPACE_NAME, LIBRARY_NAME, CELL_NAME, rfpro_view_name, emsetup_view_name])

    print("Done!")
```


---

<!-- === 来源: examples/rfpro/ex_create_rfpro_view.md === -->

# Create RFPro View[](#create-rfpro-view "Link to this heading")

This example shows how to create an RFPro view.

```
# Copyright Keysight Technologies 2025

def create_rfpro_view(example_dir : str, workspace_name : str, libray_name : str, cell_name : str):
    from tempfile import gettempdir
    import os
    import shutil
    from pathlib import Path
    import keysight.ads.de as de
    import keysight.ads.emtools as em

    tempdir = gettempdir()
    workspace_dir = Path(os.path.join(tempdir, workspace_name))
    if workspace_dir.exists():
        shutil.rmtree(workspace_dir)

    archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
    de.unarchive_file(archive_file, tempdir)
    workspace = de.open_workspace(workspace_dir)

    library = de.Library.get(libray_name)
    cell = library.cell(cell_name)
    if not cell.view_exists("rfpro"):
        print("creating rfpro view")
        em.create_empro_view(
            (library.name, cell.name, "rfpro"), # rfpro LCV
            "rfpro", # tool
            (library.name, cell.name, "layout"), # layout LCV
            (library.name, "tech.subst") # substrate
            )
    else:
        print("rfpro view already exists")

    workspace.close()

if __name__ == "__main__":

    create_rfpro_view("examples/EM/Antenna", "Single_patch_wrk", "Single_patch_lib", "Single_patch")
    print("Done!")
```


---

<!-- === 来源: examples/rfpro/ex_get_emsetup_substrate_info.md === -->

# Get the Substrate from an EM Setup View[](#get-the-substrate-from-an-em-setup-view "Link to this heading")

This example shows how to retrieve the substrate information from an existing EM Setup view.

1. First, the name if the active EM Setup view is retrieved from the Layout view.
2. Then, the substrate information, library name, substrate name and extension is retrieved from the EM Setup view.

```
# Copyright Keysight Technologies 2025

def get_emsetup_substrate_info(example_dir : str, workspace_name : str, libray_name : str, cell_name : str):
    from tempfile import gettempdir
    import os
    import shutil
    from pathlib import Path
    import keysight.ads.de as de
    import keysight.ads.emtools as em

    tempdir = gettempdir()
    workspace_dir = Path(os.path.join(tempdir, workspace_name))
    if workspace_dir.exists():
        shutil.rmtree(workspace_dir)

    archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
    de.unarchive_file(archive_file, tempdir)
    workspace = de.open_workspace(workspace_dir)

    emsetup_view_name = em.find_emsetup_view_name((libray_name, cell_name, "layout"))
    print(f"EM Setup view name={emsetup_view_name}")

    library = de.Library.get(libray_name)
    cell = library.cell(cell_name)
    if cell.view_exists(emsetup_view_name):
        (substrateLibraryName, substrateFileName) = em.get_substrate_info((libray_name, cell_name, emsetup_view_name))
        print(f"Substrate library={substrateLibraryName}, name={substrateFileName}");
    else:
        print(f"EM Setup view does not exist.")

    workspace.close()

if __name__ == "__main__":

    get_emsetup_substrate_info("examples/EM/Antenna", "Single_patch_wrk", "Single_patch_lib", "Single_patch")
    print("Done!")
```


---

<!-- === 来源: examples/rfpro/index.md === -->

# RFPro Examples[](#rfpro-examples "Link to this heading")

The source code for the examples referenced by these help pages can be found in **$HPEESOF\_DIR/doc/python/emtools/automation/examples**

Contents:

* [Create RFPro View](ex_create_rfpro_view.md)
* [Get the Substrate from an EM Setup View](ex_get_emsetup_substrate_info.md)
* [Convert EM Setup to RFPro View](ex_convert_emsetup_to_rfpro_view.md)


---

