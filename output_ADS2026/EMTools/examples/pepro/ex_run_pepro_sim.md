<!-- 来源: examples\pepro\ex_run_pepro_sim.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [EM Tools Python Documentation](../../index.md)
* [Examples](../index.md)
* [PEPro Examples](index.md)
* Run existing PEPro analysis persent in workspace.

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
    - Run existing PEPro analysis persent in workspace.
    - [Creates a new selected nets type analysis in pepro View and run the simulation.](ex_create_and_run_selected_nets_analysis.md)
    - [Creates a new pe thermal analysis in pepro View and run the simulation.](ex_create_and_run_thermal_analysis.md)

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

On this page

[Previous

Creates a new pepro View](ex_create_pepro_view.md)
[Next

Creates a new selected nets type analysis in pepro View and run the simulation.](ex_create_and_run_selected_nets_analysis.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top