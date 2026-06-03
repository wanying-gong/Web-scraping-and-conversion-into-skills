<!-- 来源: examples\ex_run_rfpro_simulation_on_dc_server.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../index.md)
* [Examples](index.md)
* Run RFPro Simulation on Design Cloud Server

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/examples/ex_run_rfpro_simulation_on_dc_server.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../intro/index.md)
  + [Using Design Cloud Functionality in Python](../intro/usage.md)
  + [Using Visual Studio Code](../intro/vscode.md)
* [Reference](../reference/index.md)
  + [keysight.ads.experimental\_simulation](../reference/hpc/index.md)
    - [SimulationMode](../reference/hpc/SimulationMode.md)
    - [JobStatus](../reference/hpc/JobStatus.md)
    - [ResourceSettings](../reference/hpc/ResourceSettings.md)
    - [LocalResourceSettings](../reference/hpc/LocalResourceSettings.md)
    - [SiteclusterResourceSettings](../reference/hpc/SiteclusterResourceSettings.md)
    - [Job](../reference/hpc/Job.md)
    - [JobStartupInfo](../reference/hpc/JobStartupInfo.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../howto/newvenv.md)
  + [How to Submit Simulations on Design Cloud Hosts](../howto/submit_simulations.md)
    - [Submitting simulations on a Local Queue](../howto/submit_sims/local_queue.md)
    - [Submitting simulations on a Site Cluster Queue](../howto/submit_sims/sitecluster_queue.md)
    - [Submitting Simulations on a Design Cloud Server](../howto/submit_sims/dc_server.md)
    - [Submit a Netlist to Design Cloud Server](../howto/submit_sims/submit_netlist.md)
    - [Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings](../howto/submit_sims/submit_pre.md)
  + [How to Manage Simulation Jobs](../howto/job.md)
    - [Cancel a Job](../howto/manage_jobs/cancel_job.md)
    - [Get the name of a job](../howto/manage_jobs/job_name.md)
    - [Wait for a Job to Complete](../howto/manage_jobs/job_wait.md)
    - [Get the List of Submitted Jobs](../howto/manage_jobs/job_list.md)
    - [Wait for All Jobs to Complete](../howto/manage_jobs/all_job_wait.md)
    - [Polling the Status of a Job](../howto/manage_jobs/polling_status.md)
    - [Getting the dataset after a simulation](../howto/manage_jobs/get_dataset.md)
    - [Checking for Running Jobs](../howto/manage_jobs/check_running_jobs.md)
* [Examples](index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](ex_simulate_dc_server.md)
  + [Simulate multiple designs of a workspace on Design Cloud](ex_simulate_multiple_designs.md)
  + Run RFPro Simulation on Design Cloud Server

# Run RFPro Simulation on Design Cloud Server[](#run-rfpro-simulation-on-design-cloud-server "Link to this heading")

This example will unarchive an ADS example RFPro\_2Stage\_RF\_Board\_Amp\_wrk in your current working directory and run Full EM Analysis test on the Design Cloud server.

Note

This example will only work in command line mode as `keysight.edatoolbox.multi_python` is not supported on `IPython`. A dummy Design Cloud server is shown in the example. Please replace it with your own Design Cloud server.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example uses existing ADS example "RFPro_2Stage_RF_Board_Amp_wrk" to demonstrate how to
run RFPro simulation on Design Cloud using Python APIs provided by Keysight Advanced Design System (ADS).
"""

import argparse
import sys

def ads_find_rfpro_view_in_workspace(
    example_dir: str,
    workspace_name: str,
    library_name: str,
    cell_name: str,
    rfpro_view_name: str,
) -> None:
    """
    Find the RFPro view for the given workspace, library and cell.
    """

    import os
    import shutil
    from pathlib import Path
    import keysight.ads.de as de

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

    if not cell.view_exists(rfpro_view_name):
        raise RuntimeError(f"The rfpro view {rfpro_view_name} does not exist.")
    workspace.close()

def rfpro_run_analysis_on_design_cloud(
    workspace_name: str,
    library_name: str,
    cell_name: str,
    substrate_name: str,
    rfpro_view: str,
    rfpro_analysis_name: str,
    resource_settings: dict,
    timeout=0,
) -> int:
    """
    Run the RFPro analysis on the design cloud server.
    """
    import os
    import empro
    from empro.toolkit import simulation
    import empro.toolkit.analysis as rfpro

    print(f"Loading the rfpro view: {rfpro_view}")
    rfpro.loadDesign(
        path=os.path.join(os.getcwd(), workspace_name),
        lib=library_name,
        subst=substrate_name,
        cell=cell_name,
        layout_view="layout",
        sipi_view=rfpro_view,
    )

    setup = None
    analyses = empro.activeProject.analyses
    for analysis in analyses:
        if analysis.name == rfpro_analysis_name:
            setup = analysis
            break
    if not setup:
        raise RuntimeError(f"The rfpro analysis {rfpro_analysis_name} does not exist.")

    options = setup.simulationSettings
    resourceSettings = empro.simulation.RemoteResourceSettings()
    resourceSettings.numberOfWorkers = resource_settings.get("parallel_jobs", 1)
    resourceSettings.numberOfThreads = resource_settings.get("threads_per_job", 0)
    resourceSettings.options = resource_settings.get("options", "")
    resourceSettings.alphaOptions = resource_settings.get("alpha_options", "")
    resourceSettings.betaOptions = resource_settings.get("beta_options", "")
    resourceSettings.omegaOptions = resource_settings.get("omega_options", "")
    resourceSettings.host = resource_settings.get("host", None)
    resourceSettings.queue = resource_settings.get("queue", "")
    resourceSettings.memory = resource_settings.get("memory", "")
    options.resourceSettings = resourceSettings
    print(f"Running the rfpro analysis: {rfpro_analysis_name}..")
    try:
        rfpro.runAnalysis(setup, waitForConfirmation=False, saveProject=True)
        if timeout:
            print(f"waiting for {timeout} secs...")
        simulation.wait(rfpro.getSimulation(setup), timeout)
        print("Simulation completed.")
        sim = rfpro.getSimulation(setup)
        print(f"Simulation Status: {sim.status}")
        if sim.status == "Completed":
            return 0
        else:
            return 3
    except simulation.TimeOutError as error:
        print(f"Simulation timed out: {error}")
        return 1
    except RuntimeError as error:
        print(f"Runtime error occurred: {error}")
        return 2
    finally:
        print(f"simulation path = {setup.simulationPath}")
        print("Done\n")

if __name__ == "__main__":
    EXAMPLE_DIR = "examples/EM/RFPro"
    WORKSPACE_NAME = "RFPro_2Stage_RF_Board_Amp_wrk"
    LIBRARY_NAME = "RF_Board_lib"
    CELL_NAME = "Two_Stage_Amp"
    SUBSTRATE_NAME = "tech.subst"
    RFPRO_VIEW_NAME = "rfpro"
    RFPRO_ANALYSIS_NAME = "Full EM Analysis"
    TIMEOUT = 20 * 60  # 20 minutes

    # Parse command line arguments
    # Example usage: python ex_simulate_on_design_cloud_server.py http://your-design-cloud-url
    parser = argparse.ArgumentParser(description="Run simulation on Design Cloud")
    parser.add_argument("url", help="Design Cloud server URL")
    args = parser.parse_args()

    RESOURCE_SETTINGS = {
        "parallel_jobs": 1,
        "threads_per_job": 4,
        "options": "",
        "alpha_options": "",
        "beta_options": "",
        "omega_options": "",
        "host": args.url,
        "queue": "normal",  # Replace with your queue name
        "memory": "20 GiB",
    }

    import keysight.edatoolbox.multi_python as multi_python

    with multi_python.ads_context() as ads_ctx:
        ads_ctx.call(
            ads_find_rfpro_view_in_workspace,
            args=[
                EXAMPLE_DIR,
                WORKSPACE_NAME,
                LIBRARY_NAME,
                CELL_NAME,
                RFPRO_VIEW_NAME,
            ],
        )

    return_code = 3
    with multi_python.xxpro_context() as empro_ctx:
        return_code = empro_ctx.call(
            rfpro_run_analysis_on_design_cloud,
            args=[
                WORKSPACE_NAME,
                LIBRARY_NAME,
                CELL_NAME,
                SUBSTRATE_NAME,
                RFPRO_VIEW_NAME,
                RFPRO_ANALYSIS_NAME,
                RESOURCE_SETTINGS,
                TIMEOUT,
            ],
        )
    sys.exit(return_code)
```

On this page

[Previous

Simulate multiple designs of a workspace on Design Cloud](ex_simulate_multiple_designs.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top