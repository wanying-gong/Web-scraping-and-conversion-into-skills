<!-- 来源: intro\usage.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../index.md)
* [Introduction](index.md)
* Using Design Cloud Functionality in Python

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/intro/usage.rst.txt)

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](index.md)
  + Using Design Cloud Functionality in Python
  + [Using Visual Studio Code](vscode.md)
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
* [Examples](../examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](../examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](../examples/ex_simulate_dc_server.md)

# Using Design Cloud Functionality in Python[](#using-design-cloud-functionality-in-python "Link to this heading")

Design Cloud provides Python APIs that allow a user to run circuit simulations
on the design cloud server, Local Queue or Site Cluster Queue

A Python script running outside ADS can access the functionality of Desing Cloud.

```
from keysight.ads.experimental_simulation import hpc
```

The `keysight.ads.experimental_simulation` package is not currently available as a pip-installable package.
To get access to this package, use any one of these approaches:

> 1. Use the Python interpreter in `$HPEESOF_DIR/tools/python`.
> 2. Create a virtual environment based on that interpreter. See [How to Set Up a Python Virtual Environment](../howto/venv.md).

Set the environment variable `HPEESOF_DIR` to point to your ADS installation prior to
using the `keysight.ads.experimental_simulation` package.

On this page

[Previous

Introduction](index.md)
[Next

Using Visual Studio Code](vscode.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top