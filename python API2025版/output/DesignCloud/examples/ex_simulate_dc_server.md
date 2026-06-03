<!-- 来源: examples\ex_simulate_dc_server.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../index.md)
* [Examples](index.md)
* Simulate a Circuit on Design Cloud Server

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/examples/ex_simulate_dc_server.rst.txt)

*help\_center* Help

Contact Keysight

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
    - [ResourceSettings](../reference/hpc/ResourceSettings.md)
    - [LocalResourceSettings](../reference/hpc/LocalResourceSettings.md)
    - [SiteclusterResourceSettings](../reference/hpc/SiteclusterResourceSettings.md)
    - [Job](../reference/hpc/Job.md)
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
* [Examples](index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](ex_simulate_local_queue.md)
  + Simulate a Circuit on Design Cloud Server

# Simulate a Circuit on Design Cloud Server[](#simulate-a-circuit-on-design-cloud-server "Link to this heading")

This example will unarchive an ADS example BatchSim\_Example1\_wrk in your in your `HOME` directory and run Batch\_CSVSweep test bench on the design cloud server. Note that a dummy design cloud server is shown in the example. Please replace it with your own server.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example uses existing ADS example "BatchSim_Example1_wrk:Batch_CSVSweep" to demonstrate how to run a
simulation on Design Cloud Server using Python APIs provided by Keysight Advanced Design System (ADS).
"""

import os
from pathlib import Path
from keysight.ads import de
from keysight.ads.de import db_uu as db
from keysight.ads.experimental_simulation import hpc

def unarchive_workspace_and_open_design_then_simulate_on_hpc_server() -> None:
    """
    Unarchive a workspace, open a design and simulate it on HPC Server
    """
    home_dir = os.environ["HOME"]
    example_wrk_path = os.path.join(
        os.environ["HPEESOF_DIR"], "examples", "RF_Microwave", "BatchSim_Example1_wrk.7zads"
    )

    workspace_path = os.path.join(home_dir, "BatchSim_Example1_wrk")
    workspace_path = Path(workspace_path)
    if workspace_path.exists():
        raise RuntimeError(f"Workspace directory already exists: {workspace_path}")

    # Unarchive the workspace
    de.unarchive_file(example_wrk_path, home_dir, exclude_em_files=True)

    # Open the workspace
    de.open_workspace(workspace_path)
    design = db.open_design("BatchSim_Example1_lib:Batch_CSVSweep:schematic", db.DesignMode.APPEND)

    # Simulate the design on HPC Server
    simulate_on_hpc_server(design)

def simulate_on_hpc_server(design: db.Design) -> None:
    """
    Simulate the design on HPC Server
    """

    # Set the resource settings for the simulation
    resource_settings = hpc.ResourceSettings()
    resource_settings.url = "https://mydesigncloudserver.com"  # Replace with your Design Cloud Server URL
    resource_settings.parallel_jobs = 4
    resource_settings.max_threads_per_job = 4
    resource_settings.memory_value = 8
    resource_settings.memory_unit = "GB"
    resource_settings.queue = "normal"  # Replace with your queue name

    # If you have a upload file, you can set it here
    # resource_settings.uploading_filename = "/my/example/upload_file.upl"

    # To notify the job status over email, you can set the email here
    # Note that your underlying cluster should be configured to send emails
    # resource_settings.email = "myemail@address.com" # Replace with your email address

    # To add extra options for the site cluster, you can set it here
    # resource_settings.site_cluster_extra_options = "--customargs \"-q normal\"" # Replace with your custom args

    # Simulate the design on HPC Server
    job = hpc.submit_design_with_settings(design, resource_settings)

    check_job_status(job)

def check_job_status(job: hpc.Job) -> None:
    """
    Check the job status
    """

    # Let's assume the job will finish within 10 minutes
    # You can change the timeout value based on your job
    # The job will wait until the job is finished or the timeout is reached
    job.await_job(600)

    # Check the job status
    job_status = job.get_status()
    print(f"Job status: {job_status}")

unarchive_workspace_and_open_design_then_simulate_on_hpc_server()
```

On this page

[Previous

Create and Simulate a Circuit on Design Cloud Local Queue](ex_simulate_local_queue.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top