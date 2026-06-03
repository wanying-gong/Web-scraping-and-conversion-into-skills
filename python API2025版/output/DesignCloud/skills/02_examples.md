# Examples
> **说明：** Examples 相关页面。

> **何时使用：** 当你需要查阅 Examples 相关内容时

---

## 本文件目录

- **Simulate a Circuit on Design Cloud Server** (`examples/ex_simulate_dc_server.md`)
- **Create and Simulate a Circuit on Design Cloud Local Queue** (`examples/ex_simulate_local_queue.md`)
- **Examples** (`examples/index.md`)

---

<!-- === 来源: examples/ex_simulate_dc_server.md === -->

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


---

<!-- === 来源: examples/ex_simulate_local_queue.md === -->

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


---

<!-- === 来源: examples/index.md === -->

# Examples[](#examples "Link to this heading")

Contents:

* [Create and Simulate a Circuit on Design Cloud Local Queue](ex_simulate_local_queue.md)
* [Simulate a Circuit on Design Cloud Server](ex_simulate_dc_server.md)


---

