<!-- 来源: examples\ex_simulate_local_queue.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../index.md)
* [Examples](index.md)
* Create and Simulate a Circuit on Design Cloud Local Queue

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/examples/ex_simulate_local_queue.rst.txt)

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
  + Create and Simulate a Circuit on Design Cloud Local Queue
  + [Simulate a Circuit on Design Cloud Server](ex_simulate_dc_server.md)

# Create and Simulate a Circuit on Design Cloud Local Queue[](#create-and-simulate-a-circuit-on-design-cloud-local-queue "Link to this heading")

This example will create a new workspace in your `HOME` directory called create\_simulate\_on\_hpc\_wrk. In the workspace a new library and schematic are created and populated with an RC filter. Next, the circuit will be subitted to the design cloud local queue for simulation.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example demonstrates how to run a simulation on Design Cloud using
Python APIs provided by Keysight Advanced Design System (ADS).
"""

import os
from pathlib import Path
from keysight.ads import de
from keysight.ads.de import db_uu as db
from keysight.ads.experimental_simulation import hpc

def create_workspace_and_design_then_simulate_on_hpc() -> None:
    """
    Create a new workspace, design and simulate it on HPC
    """
    home_dir = os.environ["HOME"]
    workspace_path = os.path.join(home_dir, "create_simulate_on_hpc_wrk")

    workspace_directory = Path(workspace_path)
    if workspace_directory.exists():
        raise RuntimeError(f"Workspace directory already exists: {workspace_path}")

    # Create the workspace
    workspace = de.create_workspace(workspace_path)
    workspace.open()

    create_design_then_simulate_over_hpc(workspace)

def create_design_then_simulate_over_hpc(workspace: de.Workspace) -> None:
    """
    Create a new design and simulate it on HPC
    """
    # Create a new library
    lib_dir = os.path.join(workspace.path, "low_pass_filter_lib")
    de.create_new_library("low_pass_filter_lib", lib_dir)
    workspace.add_library("low_pass_filter_lib", lib_dir, de.LibraryMode.NON_SHARED)

    # Create a new schematic
    design = db.create_schematic("low_pass_filter_lib:cell:schematic")

    # add components to the schematic
    design.add_instance(("ads_sources", "V_AC", "symbol"), (-2, 0), name="SRC1", angle=-90)
    r = design.add_instance(("ads_rflib", "R", "symbol"), (0, 0), name="R1", angle=0)
    r.parameters["R"].value = "3.0 kOhm"
    c = design.add_instance(("ads_rflib", "C", "symbol"), (2, 0), name="C1", angle=-90)
    c.parameters["C"].value = "1.0 uF"

    design.add_instance(("ads_rflib", "GROUND", "symbol"), (-2, -1), angle=-90)
    design.add_instance(("ads_rflib", "GROUND", "symbol"), (2, -1), angle=-90)

    design.add_wire([(-2.0, 0.0), (0.0, 0.0)])
    wire = design.add_wire([(1.0, 0.0), (2.0, 0.0)])

    wire.add_wire_label("R1_v")

    ac = design.add_instance(("ads_simulation", "AC", "symbol"), (-4, 1), name="AC1", angle=0)
    ac.parameters["Start"].value = "1.0 Hz"

    ac.parameters["Stop"].value = "1.0 MHz"
    ac.parameters["Dec"].value = "5"
    ac.parameters["Step"].value = ""

    v = design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 2), name="VAR1", angle=-90)
    assert v.is_var_instance

    v.vars["X"] = "1.0"
    v.vars["Y"] = "X/2.0"
    design.save_design()

    # Submit the design to HPC for simulation
    submit_design_to_hpc(design)

def submit_design_to_hpc(design: db.Design) -> None:
    """
    Submit the design to Local Queue for simulation
    """

    # Setting resources for the simulation
    settings = hpc.LocalResourceSettings()
    settings.parallel_jobs = 2
    settings.max_threads_per_job = 4
    settings.memory_value = 8
    settings.memory_unit = "GB"

    # Submit the test bench with the settings to the HPC
    job = hpc.submit_design_with_settings(design, settings)

    check_job_status(job)

def check_job_status(job: hpc.Job) -> None:
    """
    Check the job status
    """

    # Wait for the job to complete
    job.await_job(600)

    # Check the job status
    job_status = job.get_status()
    print(f"Job status: {job_status}")

create_workspace_and_design_then_simulate_on_hpc()
```

On this page

[Previous

Examples](index.md)
[Next

Simulate a Circuit on Design Cloud Server](ex_simulate_dc_server.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top