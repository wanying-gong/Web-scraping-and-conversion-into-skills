<!-- 来源: howto\submit_sims\local_queue.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [How-To](../index.md)
* [How to Submit Simulations on Design Cloud Hosts](../submit_simulations.md)
* Submitting simulations on a Local Queue

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/howto/submit_sims/local_queue.rst.txt)

*help\_center* Help

Contact Keysight

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
    - [ResourceSettings](../../reference/hpc/ResourceSettings.md)
    - [LocalResourceSettings](../../reference/hpc/LocalResourceSettings.md)
    - [SiteclusterResourceSettings](../../reference/hpc/SiteclusterResourceSettings.md)
    - [Job](../../reference/hpc/Job.md)
* [How-To](../index.md)
  + [How to Set Up a Python Virtual Environment](../venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../newvenv.md)
  + [How to Submit Simulations on Design Cloud Hosts](../submit_simulations.md)
    - Submitting simulations on a Local Queue
    - [Submitting simulations on a Site Cluster Queue](sitecluster_queue.md)
    - [Submitting Simulations on a Design Cloud Server](dc_server.md)
    - [Submit a Netlist to Design Cloud Server](submit_netlist.md)
    - [Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings](submit_pre.md)
  + [How to Manage Simulation Jobs](../job.md)
    - [Cancel a Job](../manage_jobs/cancel_job.md)
    - [Get the name of a job](../manage_jobs/job_name.md)
    - [Wait for a Job to Complete](../manage_jobs/job_wait.md)
    - [Get the List of Submitted Jobs](../manage_jobs/job_list.md)
    - [Wait for All Jobs to Complete](../manage_jobs/all_job_wait.md)
* [Examples](../../examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)

# Submitting simulations on a Local Queue[](#submitting-simulations-on-a-local-queue "Link to this heading")

If you want to run your design on your local host, you can use the `LocalResourceSettings` class to specify the resource settings. Under this mode, you can also simulate your design parallely on your local machine.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.LocalResourceSettings()
resource_settings.parallel_jobs = 8
resource_settings.threads = 4
resource_settings.memory_value = 16
resource_settings.memory_unit = 'GB'

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```

We have provided an example for your reference on how to submit simulations on a local queue. see [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)

On this page

[Previous

How to Submit Simulations on Design Cloud Hosts](../submit_simulations.md)
[Next

Submitting simulations on a Site Cluster Queue](sitecluster_queue.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top