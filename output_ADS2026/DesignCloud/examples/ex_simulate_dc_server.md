<!-- 来源: examples\ex_simulate_dc_server.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../index.md)
* [Examples](index.md)
* Simulate a Circuit on Design Cloud Server

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/examples/ex_simulate_dc_server.rst.txt)

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
  + Simulate a Circuit on Design Cloud Server
  + [Simulate multiple designs of a workspace on Design Cloud](ex_simulate_multiple_designs.md)
  + [Run RFPro Simulation on Design Cloud Server](ex_run_rfpro_simulation_on_dc_server.md)

# Simulate a Circuit on Design Cloud Server[](#simulate-a-circuit-on-design-cloud-server "Link to this heading")

This example will unarchive an ADS example BatchSim\_Example1\_wrk in your current working directory and run Batch\_CSVSweep test bench on the Design Cloud server.

Note

A dummy Design Cloud server is shown in the example. Please replace it with your own Design Cloud server.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example uses existing ADS example "BatchSim_Example1_wrk:Batch_CSVSweep" to demonstrate how to
run a simulation on Design Cloud using Python APIs provided by Keysight Advanced Design System (ADS).
"""

import argparse
import os
import shutil
from pathlib import Path
import sys
from keysight.ads import de
from keysight.ads.de import db_uu as db
from keysight.ads.experimental_simulation import hpc

def run_design_on_design_cloud(
    example_dir: str, workspace_name: str, library_name: str, cell_name: str, settings: hpc.ResourceSettings, timeout=0
) -> int:
    """
    Unarchives a workspace, opens the design specified
    and submits the design on the Design Cloud
    """

    def unarchive_example_workspace(example_dir: str, workspace_name: str) -> Path:
        """
        Unarchive example workspace
        """
        workspace_dir = Path(workspace_name)
        if workspace_dir.exists():
            print(f"Removing existing workspace: {workspace_dir}")
            shutil.rmtree(workspace_dir)

        archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
        print(f"Unarchiving Workspace: {archive_file} in current working directory: {os.getcwd()}")
        de.unarchive_file(archive_file, ".")
        return workspace_dir

    def check_job_status(job: hpc.Job, timeout=0) -> None:
        """
        Check the job status
        """
        job.await_job(timeout=timeout)

        # Check the job status
        job_status = job.get_status()
        print(f"Job status: {job_status.value}")

        # Print job output
        print(f"Job {job.get_name()} output:")
        print(job.get_output())

        # Subjob Status
        subjob_statuses = job.get_subjob_status()
        completed = 0
        failed = 0
        pending = 0
        running = 0

        for subjob_status in subjob_statuses:
            if subjob_status == hpc.JobStatus.COMPLETED:
                completed += 1
            elif subjob_status == hpc.JobStatus.ERROR:
                failed += 1
            elif subjob_status == hpc.JobStatus.PENDING:
                pending += 1
            elif subjob_status == hpc.JobStatus.RUNNING:
                running += 1

        print(f"Subjob status: {completed} completed, {failed} failed, {pending} pending, {running} running")
        print("\n".join([f"Subjob {i} output:\n {output}" for i, output in enumerate(job.get_subjob_output())]))

        if job_status == hpc.JobStatus.COMPLETED:
            print("Job completed successfully")
        elif job_status == hpc.JobStatus.ERROR:
            print("Job failed")
            raise RuntimeError("Job failed")
        elif job_status == hpc.JobStatus.RUNNING:
            print("Job is still running")
        else:
            print(f"Job status is: {job_status.value}")

    # Execution
    workspace_dir = unarchive_example_workspace(example_dir, workspace_name)
    workspace = de.open_workspace(workspace_dir)
    design = db.open_design(f"{library_name}:{cell_name}:schematic", db.DesignMode.APPEND)
    try:
        job = hpc.submit_design_with_settings(design, settings)
        if job:
            check_job_status(job, timeout)
        else:
            print("Failed to submit the design to Design Cloud")
            return 1
    except RuntimeError as error:
        print(f"An error occurred while submitting design to Design Cloud: {error}")
        return 1
    except Exception as error:
        print(f"Unexpected  error: {error}")
        return 2
    finally:
        # Close the workspace
        print(f"Closing workspace: {workspace_dir}")
        workspace.close()
    return 0

if __name__ == "__main__":
    EXAMPLE_DIR = "examples/RF_Microwave"
    WORKSPACE_NAME = "BatchSim_Example1_wrk"
    LIBRARY_NAME = "BatchSim_Example1_lib"
    CELL_NAME = "Batch_CSVSweep"

    # Parse command line arguments
    # Example usage: python ex_simulate_on_design_cloud_server.py http://your-design-cloud-url
    parser = argparse.ArgumentParser(description="Run simulation on Design Cloud")
    parser.add_argument("url", help="Design Cloud server URL")
    args = parser.parse_args()
    RESOURCE_SETTINGS = hpc.ResourceSettings(
        url=args.url,
        parallel_jobs=4,
        max_threads_per_job=4,
        memory_value=12,
        memory_unit="GB",
        queue="default",  #  Replace with your own queue name
        # Additional options for Design Cloud
        # project_name='your_project_name', # Replace with your own project name if you have configured
        # uploading_filename='/path/to/your/upload_file.upl', # Replace with your own upload file path
        # email='your_email@address.com', # Replace with your own email address
        # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
    )
    TIMEOUT = 10 * 60  # 10 minutes

    EXIT_CODE = run_design_on_design_cloud(
        EXAMPLE_DIR, WORKSPACE_NAME, LIBRARY_NAME, CELL_NAME, RESOURCE_SETTINGS, TIMEOUT
    )
    sys.exit(EXIT_CODE)
```

On this page

[Previous

Create and Simulate a Circuit on Design Cloud Local Queue](ex_simulate_local_queue.md)
[Next

Simulate multiple designs of a workspace on Design Cloud](ex_simulate_multiple_designs.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top