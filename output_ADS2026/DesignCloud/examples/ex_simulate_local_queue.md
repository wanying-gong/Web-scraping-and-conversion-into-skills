<!-- 来源: examples\ex_simulate_local_queue.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../index.md)
* [Examples](index.md)
* Create and Simulate a Circuit on Design Cloud Local Queue

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/examples/ex_simulate_local_queue.rst.txt)

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
  + Create and Simulate a Circuit on Design Cloud Local Queue
  + [Simulate a Circuit on Design Cloud Server](ex_simulate_dc_server.md)
  + [Simulate multiple designs of a workspace on Design Cloud](ex_simulate_multiple_designs.md)
  + [Run RFPro Simulation on Design Cloud Server](ex_run_rfpro_simulation_on_dc_server.md)

# Create and Simulate a Circuit on Design Cloud Local Queue[](#create-and-simulate-a-circuit-on-design-cloud-local-queue "Link to this heading")

This example will create a new workspace in your current working directory called design\_cloud\_demo\_wrk. In the workspace, a new library and schematic is created and populated with an RC filter. Next, the circuit is be subitted to the Design Cloud Local Queue for simulation.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example demonstrates how to run a simulation on Design Cloud Local Queue
using Python APIs provided by Keysight Advanced Design System (ADS).
"""

import os
import shutil
from pathlib import Path
import sys
from keysight.ads import de
from keysight.ads.de import db_uu as db
from keysight.ads.experimental_simulation import hpc

def create_workspace_and_design_then_simulate_on_design_cloud(
    workspace_name: str, library_name: str, cell_name: str
) -> int:
    """
    Create a new workspace, design and simulate it on Design Cloud
    """

    def create_and_open_workspace(workspace_name) -> de.Workspace:
        """
        Creates a workspace and opens it
        """
        workspace_path = Path(workspace_name)
        if workspace_path.exists():
            print(f"Removing existing workspace: {workspace_path}")
            shutil.rmtree(workspace_path)

        # Create the workspace
        print(f"Creating workspace: {workspace_path}")
        workspace = de.create_workspace(workspace_path)
        workspace.open()
        return workspace

    def create_library_and_design(workspace: de.Workspace, library_name: str, cell_name: str) -> db.Design:
        """
        Creates a new library and design inside the workspace
        """
        library_path = os.path.join(workspace.path, library_name)
        print(f"Creating library: {library_path}")
        de.create_new_library(library_name, library_path)
        workspace.add_library(library_name, library_path, de.LibraryMode.NON_SHARED)

        print(f"Creating design: {library_name}:{cell_name}:schematic")
        # Create a new schematic
        design = db.create_schematic(f"{library_name}:{cell_name}:schematic")
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
        return design

    def submit_design_on_design_cloud_local_queue(design: db.Design) -> hpc.Job:
        """
        Submit the design on Design Cloud Local Queue
        """
        # Setting resources for the simulation
        resource_settings = hpc.LocalResourceSettings(parallel_jobs=1, max_threads_per_job=1, queue_job_locally=False)

        # If you want to queue multiple designs on "Local queue",
        # then, set the queue_job_locally = True

        # Submit the test bench with the settings to the Design Cloud Local queue
        print("Submitting design to Design Cloud Local Queue")
        job = hpc.submit_design_with_settings(design, resource_settings)
        return job

    def check_job_status(job: hpc.Job):
        """
        Check job status
        """
        # Wait for the job to complete
        job.await_job(600)

        # Check the job status
        job_status = job.get_status()
        print(f"Job status: {job_status.value}")

        # Print job output
        print(f"Job {job.get_name()} output:")
        print(job.get_output())
        print("\n".join([f"Subjob {i} output:\n {output}" for i, output in enumerate(job.get_subjob_output())]))

        if job_status == hpc.JobStatus.COMPLETED:
            print("Job completed successfully")
        elif job_status == hpc.JobStatus.ERROR:
            print("Job failed")
        elif job_status == hpc.JobStatus.RUNNING:
            print("Job is still running")
        else:
            print(f"Job status is: {job_status.value}")

    # Execution
    workspace = create_and_open_workspace(workspace_name)
    design = create_library_and_design(workspace, library_name, cell_name)
    try:
        job = submit_design_on_design_cloud_local_queue(design)
        check_job_status(job)
    except RuntimeError as error:
        print(f"An error occurred while submitting design to local queue: {error}")
        return 1
    except Exception as error:
        print(f"Unexpected  error: {error}")
        return 2
    finally:
        # Close the workspace
        print(f"Closing workspace: {workspace_name}")
        workspace.close()
    return 0

if __name__ == "__main__":
    WORKSPACE_NAME = "design_cloud_demo_wrk"
    LIBRARY_NAME = "design_cloud_demo_lib"
    CELL_NAME = "design_cloud_local_queue"
    EXIT_CODE = create_workspace_and_design_then_simulate_on_design_cloud(WORKSPACE_NAME, LIBRARY_NAME, CELL_NAME)
    sys.exit(EXIT_CODE)
```

On this page

[Previous

Examples](index.md)
[Next

Simulate a Circuit on Design Cloud Server](ex_simulate_dc_server.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top