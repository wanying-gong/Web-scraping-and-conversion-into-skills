<!-- 来源: howto\submit_sims\dc_server.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [How-To](../index.md)
* [How to Submit Simulations on Design Cloud Hosts](../submit_simulations.md)
* Submitting Simulations on a Design Cloud Server

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/howto/submit_sims/dc_server.rst.txt)

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
    - [Submitting simulations on a Local Queue](local_queue.md)
    - [Submitting simulations on a Site Cluster Queue](sitecluster_queue.md)
    - Submitting Simulations on a Design Cloud Server
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

# Submitting Simulations on a Design Cloud Server[](#submitting-simulations-on-a-design-cloud-server "Link to this heading")

If you already have deployed a Design Cloud Server, you can specify the url of that server in the resource settings.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.ResourceSettings()
resource_settings.url = 'https://mydesigncloudserver.com' # Replace with your Design Cloud server URL
resource_settings.parallel_jobs = 8
resource_settings.threads = 4
resource_settings.memory_value = 16
resource_settings.memory_unit = 'GB'

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```

We have provided an example for your reference on how to submit simulations on a Design Cloud server. see [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)

On this page

[Previous

Submitting simulations on a Site Cluster Queue](sitecluster_queue.md)
[Next

Submit a Netlist to Design Cloud Server](submit_netlist.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top