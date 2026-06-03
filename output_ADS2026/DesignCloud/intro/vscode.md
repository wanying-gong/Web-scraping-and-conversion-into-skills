<!-- 来源: intro\vscode.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../index.md)
* [Introduction](index.md)
* Using Visual Studio Code

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/intro/vscode.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](index.md)
  + [Using Design Cloud Functionality in Python](usage.md)
  + Using Visual Studio Code
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
* [Examples](../examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](../examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](../examples/ex_simulate_dc_server.md)
  + [Simulate multiple designs of a workspace on Design Cloud](../examples/ex_simulate_multiple_designs.md)
  + [Run RFPro Simulation on Design Cloud Server](../examples/ex_run_rfpro_simulation_on_dc_server.md)

# Using Visual Studio Code[](#using-visual-studio-code "Link to this heading")

To invoke ADS Python from VS-Code:

> 1. In VS-Code, execute the menu "View->Command Palette…"
> 2. Type the command "Python:Select Interpreter"
> 3. Set the python interpreter by browsing to $HPEESOF\_DIR\tools\python\python.exe (python3 for linux)

To use a python virtual environment instead of the ADS python installation:

> 1. Set up a python virtual environment. see [How to Set Up a Python Virtual Environment](../howto/venv.md)
> 2. Repeat steps 1-3 above
> 3. Set the python interpreter by browsing to the python executable in the virtual environment.

On this page

[Previous

Using Design Cloud Functionality in Python](usage.md)
[Next

Reference](../reference/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top