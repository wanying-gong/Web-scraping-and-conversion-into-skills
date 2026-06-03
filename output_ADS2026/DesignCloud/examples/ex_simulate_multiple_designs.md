<!-- 来源: examples\ex_simulate_multiple_designs.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../index.md)
* [Examples](index.md)
* Simulate multiple designs of a workspace on Design Cloud

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/examples/ex_simulate_multiple_designs.rst.txt)

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
  + Simulate multiple designs of a workspace on Design Cloud
  + [Run RFPro Simulation on Design Cloud Server](ex_run_rfpro_simulation_on_dc_server.md)

# Simulate multiple designs of a workspace on Design Cloud[](#simulate-multiple-designs-of-a-workspace-on-design-cloud "Link to this heading")

This example will unarchive an ADS example BatchSim\_Example1\_wrk in your current working directory and run multiple designs on the Design Cloud server.

Note

A dummy Design Cloud server is shown in the example. Please replace it with your own Design Cloud server.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example uses existing ADS example "BatchSim_Example1_wrk" to demonstrate how to run multiple designs
of same workspace on Design Cloud using Python APIs provided by Keysight Advanced Design System (ADS).
"""

import argparse
import os
import shutil
from pathlib import Path
import sys
from keysight.ads import de
from keysight.ads.de import db_uu as db
from keysight.ads.experimental_simulation import hpc

def run_multiple_designs_on_design_cloud(example_dir: str, workspace_name: str, design_config: dict, timeout=0) -> int:
    """
    Unarchives a workspace, opens each design specified in the design config and
    submits the design on the Design Cloud
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

    def submit_designs_on_design_cloud(design_config: dict) -> None:
        """
        Opens each design and submit to Design Cloud
        """

        if not design_config:
            raise ValueError("Design Configuration cannot be empty")

        for design_name, resource_settings in design_config.items():
            print(f"Opening design: {design_name}")
            design = db.open_design(design_name, db.DesignMode.APPEND)
            job = hpc.submit_design_with_settings(design, resource_settings)
            # You can also check the job startup information
            job_startup_info = job.get_startup_info()
            info_dict = {
                "job name": job.get_name(),
                "workspace dir": job_startup_info.workspace_dir,
                "job dir": job_startup_info.job_dir,
                "start time": job_startup_info.start_time,
                "host url": job_startup_info.url,
                "queue": job_startup_info.queue,
                "dataset name": job_startup_info.dataset_name,
                "data display name": job_startup_info.datadisplay_name,
                "top level design": job_startup_info.top_level_design,
            }
            for key, value in info_dict.items():
                print(f"{key}: {value}")
            print("-----------------------------------------------------------")

    def monitor_all_submitted_jobs(timeout=0):
        """
        Monitor all submitted jobs on Design Cloud
        """

        # Check running status of all jobs

        running_jobs = [job for job in hpc.get_jobs() if job.is_running()]

        # Optional: You can give a timeout to wait for the jobs to complete
        if running_jobs:
            job_names = [job.get_name() for job in running_jobs]
            print(f"The following jobs are running: {job_names}")
            if timeout:
                print(f"Waiting for jobs to complete within {timeout} seconds...")
            hpc.await_all_jobs(timeout=timeout)
        # Check job status
        failed = False
        for job in hpc.get_jobs():
            job_status = job.get_status()
            print(f"Job {job.get_name()} status: {job_status}")
            if job_status != hpc.JobStatus.COMPLETED:
                failed = True

            # Check if job is still not completed, cancel it
            if job.is_running():
                print(f"Job {job.get_name()} is still in {job.get_status()} mode...")
                print(f"Canceling job {job.get_name()}...")
                job.cancel()

            # Print job output
            print(f"Job {job.get_name()} output:")
            print(job.get_output())
            print("\n".join([f"Subjob {i} output:\n {output}" for i, output in enumerate(job.get_subjob_output())]))
            print("-----------------------------------------------------------")

        if failed:
            raise RuntimeError("One or more jobs failed. Please check the job status and output.")

    # Execution
    workspace_dir = unarchive_example_workspace(example_dir, workspace_name)
    workspace = de.open_workspace(workspace_dir)
    try:
        submit_designs_on_design_cloud(design_config)
        monitor_all_submitted_jobs(timeout)
    except RuntimeError as error:
        print(f"An Error occurred during design cloud simulation: {error}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 2
    finally:
        # Close the workspace
        print(f"Closing workspace: {workspace_dir}")
        workspace.close()
    return 0

if __name__ == "__main__":
    # Parse command line arguments
    # Example usage: python ex_simulate_multiple_designs.py http://your-design-cloud-url
    parser = argparse.ArgumentParser(description="Run simulation on Design Cloud")
    parser.add_argument("url", help="Design Cloud server URL")
    parser.add_argument("sitecluster", help="path to sitecluster executable")
    args = parser.parse_args()

    EXAMPLE_DIR = "examples/RF_Microwave"
    WORKSPACE_NAME = "BatchSim_Example1_wrk"
    DESIGN_CONFIG = {
        "BatchSim_Example1_lib:Batch_SweepPlan:schematic": hpc.ResourceSettings(
            url=args.url,
            parallel_jobs=4,
            max_threads_per_job=4,
            memory_value=30,
            memory_unit="GB",
            queue="default",  # Replace with your queue name
            # Additional options for Design Cloud
            # project_name='your_project_name', # Replace with your own project name if you have configured
            # uploading_filename='/path/to/your/upload_file.upl', # Replace with your own upload file path
            # email='your_email@address.com', # Replace with your own email address
            # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
        ),
        "BatchSim_Example1_lib:Batch_CSVList:schematic": hpc.LocalResourceSettings(
            parallel_jobs=3,
            max_threads_per_job=1,  # In UI, this is equivalent to setting threads = 1
            queue_job_locally=True,  # Setting true means you can queue the multiple jobs on Local queue
        ),
        "BatchSim_Example1_lib:Batch_DataFileSweep:schematic": hpc.LocalResourceSettings(
            parallel_jobs=4,
            max_threads_per_job=3,
            queue_job_locally=True,  # This design will be queued and will run after the Batch_CSVList
        ),
        "BatchSim_Example1_lib:Batch_CSVSweep:schematic": hpc.SiteclusterResourceSettings(
            sitecluster=args.sitecluster,
            parallel_jobs=4,
            max_threads_per_job=4,
            memory_value=30,
            memory_unit="GB",
            queue="default",  # Replace with your queue name
            # Additional options for Design Cloud
            # project_name='your_project_name', # Replace with your own project name if you have configured
            # email='your_email@address.com', # Replace with your own email address
            # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
        ),
    }
    TIMEOUT = 10 * 60  # 10 min

    EXIT_CODE = run_multiple_designs_on_design_cloud(EXAMPLE_DIR, WORKSPACE_NAME, DESIGN_CONFIG, TIMEOUT)
    sys.exit(EXIT_CODE)
```

On this page

[Previous

Simulate a Circuit on Design Cloud Server](ex_simulate_dc_server.md)
[Next

Run RFPro Simulation on Design Cloud Server](ex_run_rfpro_simulation_on_dc_server.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top