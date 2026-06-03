<!-- 来源: reference\index.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../index.md)
* Reference

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/reference/index.rst.txt)

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
* Reference
  + [keysight.ads.experimental\_simulation](hpc/index.md)
    - [SimulationMode](hpc/SimulationMode.md)
    - [JobStatus](hpc/JobStatus.md)
    - [ResourceSettings](hpc/ResourceSettings.md)
    - [LocalResourceSettings](hpc/LocalResourceSettings.md)
    - [SiteclusterResourceSettings](hpc/SiteclusterResourceSettings.md)
    - [Job](hpc/Job.md)
    - [JobStartupInfo](hpc/JobStartupInfo.md)
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
* [Examples](../examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](../examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](../examples/ex_simulate_dc_server.md)
  + [Simulate multiple designs of a workspace on Design Cloud](../examples/ex_simulate_multiple_designs.md)
  + [Run RFPro Simulation on Design Cloud Server](../examples/ex_run_rfpro_simulation_on_dc_server.md)

# Reference[](#reference "Link to this heading")

* [keysight.ads.experimental\_simulation](hpc/index.md)
  + [Classes](hpc/index.md#classes)
    - [SimulationMode](hpc/SimulationMode.md)
    - [JobStatus](hpc/JobStatus.md)
    - [ResourceSettings](hpc/ResourceSettings.md)
    - [LocalResourceSettings](hpc/LocalResourceSettings.md)
    - [SiteclusterResourceSettings](hpc/SiteclusterResourceSettings.md)
    - [Job](hpc/Job.md)
    - [JobStartupInfo](hpc/JobStartupInfo.md)
  + [Functions](hpc/index.md#functions)
    - [`submit_design_with_settings()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_design_with_settings)
    - [`submit_design()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_design)
    - [`submit_netlist()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_netlist)
    - [`get_jobs()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.get_jobs)
    - [`get_resource_settings()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.get_resource_settings)
    - [`set_resource_settings()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.set_resource_settings)
    - [`set_simulation_mode()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.set_simulation_mode)
    - [`await_all_jobs()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.await_all_jobs)

**Indices**

* [Index](../genindex.md)
* [Module Index](../py-modindex.md)

On this page

[Previous

Using Visual Studio Code](../intro/vscode.md)
[Next

keysight.ads.experimental\_simulation](hpc/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top