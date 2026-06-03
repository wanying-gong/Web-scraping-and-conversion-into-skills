# Examples
> **说明：** Examples 相关页面。

> **何时使用：** 当你需要查阅 Examples 相关内容时

---

## 本文件目录

- **Run RFPro Simulation on Design Cloud Server** (`examples/ex_run_rfpro_simulation_on_dc_server.md`)
- **Simulate a Circuit on Design Cloud Server** (`examples/ex_simulate_dc_server.md`)
- **Create and Simulate a Circuit on Design Cloud Local Queue** (`examples/ex_simulate_local_queue.md`)
- **Simulate multiple designs of a workspace on Design Cloud** (`examples/ex_simulate_multiple_designs.md`)
- **Examples** (`examples/index.md`)

---

<!-- === 来源: examples/ex_run_rfpro_simulation_on_dc_server.md === -->

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


---

<!-- === 来源: examples/ex_simulate_dc_server.md === -->

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


---

<!-- === 来源: examples/ex_simulate_local_queue.md === -->

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


---

<!-- === 来源: examples/ex_simulate_multiple_designs.md === -->

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


---

<!-- === 来源: examples/index.md === -->

# Examples[](#examples "Link to this heading")

Contents:

* [Create and Simulate a Circuit on Design Cloud Local Queue](ex_simulate_local_queue.md)
* [Simulate a Circuit on Design Cloud Server](ex_simulate_dc_server.md)
* [Simulate multiple designs of a workspace on Design Cloud](ex_simulate_multiple_designs.md)
* [Run RFPro Simulation on Design Cloud Server](ex_run_rfpro_simulation_on_dc_server.md)


---

