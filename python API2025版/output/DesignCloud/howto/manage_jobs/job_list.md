<!-- 来源: howto\manage_jobs\job_list.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [How-To](../index.md)
* [How to Manage Simulation Jobs](../job.md)
* Get the List of Submitted Jobs

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/howto/manage_jobs/job_list.rst.txt)

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
    - [Submitting simulations on a Local Queue](../submit_sims/local_queue.md)
    - [Submitting simulations on a Site Cluster Queue](../submit_sims/sitecluster_queue.md)
    - [Submitting Simulations on a Design Cloud Server](../submit_sims/dc_server.md)
    - [Submit a Netlist to Design Cloud Server](../submit_sims/submit_netlist.md)
    - [Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings](../submit_sims/submit_pre.md)
  + [How to Manage Simulation Jobs](../job.md)
    - [Cancel a Job](cancel_job.md)
    - [Get the name of a job](job_name.md)
    - [Wait for a Job to Complete](job_wait.md)
    - Get the List of Submitted Jobs
    - [Wait for All Jobs to Complete](all_job_wait.md)
* [Examples](../../examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)

# Get the List of Submitted Jobs[](#get-the-list-of-submitted-jobs "Link to this heading")

To get the list of submitted jobs, you can use the `get_jobs()` function. This function returns a list of all the jobs submitted by the user.

```
from keysight.ads.experimental_simulation import hpc
jobs = hpc.get_jobs()
print(jobs)
```

On this page

[Previous

Wait for a Job to Complete](job_wait.md)
[Next

Wait for All Jobs to Complete](all_job_wait.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top