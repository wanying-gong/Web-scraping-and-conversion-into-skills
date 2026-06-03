<!-- 来源: howto\manage_jobs\get_dataset.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [How-To](../index.md)
* [How to Manage Simulation Jobs](../job.md)
* Getting the dataset after a simulation

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/howto/manage_jobs/get_dataset.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../../intro/index.md)
  + [Using Design Cloud Functionality in Python](../../intro/usage.md)
  + [Using Visual Studio Code](../../intro/vscode.md)
* [Reference](../../reference/index.md)
  + [keysight.ads.experimental\_simulation](../../reference/hpc/index.md)
    - [SimulationMode](../../reference/hpc/SimulationMode.md)
    - [JobStatus](../../reference/hpc/JobStatus.md)
    - [ResourceSettings](../../reference/hpc/ResourceSettings.md)
    - [LocalResourceSettings](../../reference/hpc/LocalResourceSettings.md)
    - [SiteclusterResourceSettings](../../reference/hpc/SiteclusterResourceSettings.md)
    - [Job](../../reference/hpc/Job.md)
    - [JobStartupInfo](../../reference/hpc/JobStartupInfo.md)
* [How-To](../index.md)
  + [How to Set Up a Python Virtual Environment](../venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../newvenv.md)
  + [How to Submit Simulations on Design Cloud Hosts](../submit_simulations.md)
    - [Submitting simulations on a Local Queue](../submit_sims/local_queue.md)
    - [Submitting simulations on a Site Cluster Queue](../submit_sims/sitecluster_queue.md)
    - [Submitting Simulations on a Design Cloud Server](../submit_sims/dc_server.md)
    - [Submit a Netlist to Design Cloud Server](../submit_sims/submit_netlist.md)
    - [Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings](../submit_sims/submit_pre.md)
  + [How to Manage Simulation Jobs](../job.md)
    - [Cancel a Job](cancel_job.md)
    - [Get the name of a job](job_name.md)
    - [Wait for a Job to Complete](job_wait.md)
    - [Get the List of Submitted Jobs](job_list.md)
    - [Wait for All Jobs to Complete](all_job_wait.md)
    - [Polling the Status of a Job](polling_status.md)
    - Getting the dataset after a simulation
    - [Checking for Running Jobs](check_running_jobs.md)
* [Examples](../../examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)
  + [Simulate multiple designs of a workspace on Design Cloud](../../examples/ex_simulate_multiple_designs.md)
  + [Run RFPro Simulation on Design Cloud Server](../../examples/ex_run_rfpro_simulation_on_dc_server.md)

# Getting the dataset after a simulation[](#getting-the-dataset-after-a-simulation "Link to this heading")

When a simulation is finished you can find and read the dataset using the information held in [`JobStartupInfo`](../../reference/hpc/JobStartupInfo.md#keysight.ads.experimental_simulation.hpc.JobStartupInfo "keysight.ads.experimental_simulation.hpc.JobStartupInfo").

```
from keysight.ads.experimental_simulation import hpc
import keysight.ads.dataset as dataset
from pathlib import Path

job = hpc.submit_design_with_settings(design, settings)
job_startup_info = job.get_startup_info()

# wait for the job to complete
hpc.await_all_jobs(600)

# use the workspace dir and dataset name to get the file name of the dataset
dataset_file_name = Path(job_startup_info.workspace_dir) / "data" / (job_startup_info.dataset_name + ".ds")

# open it and print the contents
data = dataset.open(dataset_file_name)
for (name, vb) in data.items():
    print(f"VariableBlock DataFrame: {name}\n{vb.to_dataframe()}")
```

On this page

[Previous

Polling the Status of a Job](polling_status.md)
[Next

Checking for Running Jobs](check_running_jobs.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top