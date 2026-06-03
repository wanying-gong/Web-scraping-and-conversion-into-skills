<!-- 来源: howto\manage_jobs\job_wait.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [How-To](../index.md)
* [How to Manage Simulation Jobs](../job.md)
* Wait for a Job to Complete

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/howto/manage_jobs/job_wait.rst.txt)

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
    - Wait for a Job to Complete
    - [Get the List of Submitted Jobs](job_list.md)
    - [Wait for All Jobs to Complete](all_job_wait.md)
    - [Polling the Status of a Job](polling_status.md)
    - [Getting the dataset after a simulation](get_dataset.md)
    - [Checking for Running Jobs](check_running_jobs.md)
* [Examples](../../examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)
  + [Simulate multiple designs of a workspace on Design Cloud](../../examples/ex_simulate_multiple_designs.md)
  + [Run RFPro Simulation on Design Cloud Server](../../examples/ex_run_rfpro_simulation_on_dc_server.md)

# Wait for a Job to Complete[](#wait-for-a-job-to-complete "Link to this heading")

To wait for a job to complete, you can use the [`await_job()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.await_job "keysight.ads.experimental_simulation.hpc.Job.await_job") function. This function takes an argument timeout which is the maximum time to wait for the job to complete.

```
from keysight.ads.experimental_simulation import hpc
job = hpc.submit_design_with_settings(design, resource_settings)

job.await_job(timeout=60)  # Wait for 60 seconds

# If the job is completed, the function will return True
# If the job is not completed within the timeout, the function will return False

# You can also check the status of the job
job_status = job.get_status()
print(job_status.value)
```

Note that [`await_job()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.await_job "keysight.ads.experimental_simulation.hpc.Job.await_job") will block until the job is completed or the timeout is reached. If you want to cancel the await early, you must cancel the job.

For example, you can cancel a job on a Ctrl-C by adding a signal handler for SIGINT.

```
# cancel a job on a Ctrl-C
signal.signal(signal.SIGINT, lambda signal, frame: job.cancel())
```

Note : you could also leave a job running after a Control-C by calling QCoreApplication.quit() in the signal handler.
If you do this you may have to check if the job is running in any scripts you run later, see [Checking for Running Jobs](check_running_jobs.md) for more information.

On this page

[Previous

Get the name of a job](job_name.md)
[Next

Get the List of Submitted Jobs](job_list.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top