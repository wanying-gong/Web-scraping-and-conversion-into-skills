<!-- 来源: howto\manage_jobs\check_running_jobs.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [How-To](../index.md)
* [How to Manage Simulation Jobs](../job.md)
* Checking for Running Jobs

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/howto/manage_jobs/check_running_jobs.rst.txt)

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
    - [Getting the dataset after a simulation](get_dataset.md)
    - Checking for Running Jobs
* [Examples](../../examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)
  + [Simulate multiple designs of a workspace on Design Cloud](../../examples/ex_simulate_multiple_designs.md)
  + [Run RFPro Simulation on Design Cloud Server](../../examples/ex_run_rfpro_simulation_on_dc_server.md)

# Checking for Running Jobs[](#checking-for-running-jobs "Link to this heading")

While writing automation scripts you may often be able to assume that it’s okay to submit a new job, but if someone has started a job manually, or if a script started a job and left it running, it’s possible that you won’t be able submit a job because an old instance with the same name is already running.

To account for this you can check for running jobs using [`get_jobs()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.get_jobs "keysight.ads.experimental_simulation.hpc.get_jobs") and wait for them to finish if necessary.

For example:

```
running_jobs = [job for job in hpc.get_jobs() if job.is_running()]
if running_jobs:
    job_names = [job.get_name() for job in running_jobs]
    print(f"These jobs are running : {job_names}, waiting for them to complete")
    hpc.await_all_jobs()

# Now you can submit a new job
```

On this page

[Previous

Getting the dataset after a simulation](get_dataset.md)
[Next

Examples](../../examples/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top