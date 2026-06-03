<!-- 来源: howto\submit_sims\submit_pre.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [How-To](../index.md)
* [How to Submit Simulations on Design Cloud Hosts](../submit_simulations.md)
* Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/howto/submit_sims/submit_pre.rst.txt)

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
    - [Submitting simulations on a Local Queue](local_queue.md)
    - [Submitting simulations on a Site Cluster Queue](sitecluster_queue.md)
    - [Submitting Simulations on a Design Cloud Server](dc_server.md)
    - [Submit a Netlist to Design Cloud Server](submit_netlist.md)
    - Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings
  + [How to Manage Simulation Jobs](../job.md)
    - [Cancel a Job](../manage_jobs/cancel_job.md)
    - [Get the name of a job](../manage_jobs/job_name.md)
    - [Wait for a Job to Complete](../manage_jobs/job_wait.md)
    - [Get the List of Submitted Jobs](../manage_jobs/job_list.md)
    - [Wait for All Jobs to Complete](../manage_jobs/all_job_wait.md)
    - [Polling the Status of a Job](../manage_jobs/polling_status.md)
    - [Getting the dataset after a simulation](../manage_jobs/get_dataset.md)
    - [Checking for Running Jobs](../manage_jobs/check_running_jobs.md)
* [Examples](../../examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)
  + [Simulate multiple designs of a workspace on Design Cloud](../../examples/ex_simulate_multiple_designs.md)
  + [Run RFPro Simulation on Design Cloud Server](../../examples/ex_run_rfpro_simulation_on_dc_server.md)

# Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings[](#submitting-simulations-on-a-design-cloud-server-with-pre-defined-resource-settings "Link to this heading")

If the design context is already set up with the resource settings, you can directly submit the design to the Design Cloud Server using you can use the [`submit_design()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_design "keysight.ads.experimental_simulation.hpc.submit_design") function.

```
from keysight.ads.experimental_simulation import hpc

# To view the resource settings saved in the context
resource_settings = hpc.get_resource_settings()
print(resource_settings)

job = hpc.submit_design(design)  # Where design is the design object: db.Design

# You can also check the status of the job
job_status = job.get_status()
print(job_status)

# You can also set the same resource settings to a different design

design2 = db.Design()
hpc.set_resource_settings(design2, resource_settings)
job2 = hpc.submit_design(design2)

# You can also check the status of the job
job_status2 = job2.get_status()
print(job_status2)
```

On this page

[Previous

Submit a Netlist to Design Cloud Server](submit_netlist.md)
[Next

How to Manage Simulation Jobs](../job.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top