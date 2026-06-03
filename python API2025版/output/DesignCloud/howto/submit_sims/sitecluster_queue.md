<!-- 来源: howto\submit_sims\sitecluster_queue.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [How-To](../index.md)
* [How to Submit Simulations on Design Cloud Hosts](../submit_simulations.md)
* Submitting simulations on a Site Cluster Queue

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/howto/submit_sims/sitecluster_queue.rst.txt)

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
    - Submitting simulations on a Site Cluster Queue
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

# Submitting simulations on a Site Cluster Queue[](#submitting-simulations-on-a-site-cluster-queue "Link to this heading")

If you use ADS on a machine which is also a submit host of your HPC cluster then you can directly submit your simulations to the cluster without installing the Design Cloud server.
To do that you can either set `SITECLUSTER` environment variable or use the `set_sitecluster_path()` function.

`SITECLUSTER` refers to the path of the sitecluster wrapper script. This script is used to submit the simulation to the cluster.
You can also define your sitecluster queue name by setting the `SITECLUSTER_NAME` environment variable.

If you have `SITECLUSTER` set in your environment

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.SiteclusterResourceSettings()
```

If you want to set the sitecluster wrapper path in your script

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.SiteclusterResourceSettings()
resource_settings.set_sitecluster_path('/path/to/your/sitecluster/wrapper/script') # path to the sitecluster wrapper script
resource_settings.parallel_jobs = 8
resource_settings.threads = 4
resource_settings.memory_value = 16
resource_settings.memory_unit = 'GB'

# You can specify additional site cluster options. We have given an example below for LSF cluster
# The below option allows user to select the sles15 machines in his LSF cluster
# You can specify any other options as per your cluster configuration.
resource_settings.site_cluster_extra_options = "--customargs=\"-R select[sles15]\""

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```

On this page

[Previous

Submitting simulations on a Local Queue](local_queue.md)
[Next

Submitting Simulations on a Design Cloud Server](dc_server.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top