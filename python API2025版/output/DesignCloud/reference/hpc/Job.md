<!-- 来源: reference\hpc\Job.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.experimental\_simulation](index.md)
* Job

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/reference/hpc/Job.rst.txt)

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
* [Reference](../index.md)
  + [keysight.ads.experimental\_simulation](index.md)
    - [ResourceSettings](ResourceSettings.md)
    - [LocalResourceSettings](LocalResourceSettings.md)
    - [SiteclusterResourceSettings](SiteclusterResourceSettings.md)
    - Job
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
  + [How to Submit Simulations on Design Cloud Hosts](../../howto/submit_simulations.md)
    - [Submitting simulations on a Local Queue](../../howto/submit_sims/local_queue.md)
    - [Submitting simulations on a Site Cluster Queue](../../howto/submit_sims/sitecluster_queue.md)
    - [Submitting Simulations on a Design Cloud Server](../../howto/submit_sims/dc_server.md)
    - [Submit a Netlist to Design Cloud Server](../../howto/submit_sims/submit_netlist.md)
    - [Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings](../../howto/submit_sims/submit_pre.md)
  + [How to Manage Simulation Jobs](../../howto/job.md)
    - [Cancel a Job](../../howto/manage_jobs/cancel_job.md)
    - [Get the name of a job](../../howto/manage_jobs/job_name.md)
    - [Wait for a Job to Complete](../../howto/manage_jobs/job_wait.md)
    - [Get the List of Submitted Jobs](../../howto/manage_jobs/job_list.md)
    - [Wait for All Jobs to Complete](../../howto/manage_jobs/all_job_wait.md)
* [Examples](../../examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)

# Job[](#job "Link to this heading")

*class* keysight.ads.experimental\_simulation.hpc.Job(*name: str*)[](#keysight.ads.experimental_simulation.hpc.Job "Link to this definition")
:   Bases: `object`

    Class to manage simulation jobs.

    await\_job(*timeout: int = 0*) → None[](#keysight.ads.experimental_simulation.hpc.Job.await_job "Link to this definition")

    cancel() → None[](#keysight.ads.experimental_simulation.hpc.Job.cancel "Link to this definition")
    :   Cancel the job.

    get\_name() → str[](#keysight.ads.experimental_simulation.hpc.Job.get_name "Link to this definition")
    :   Get the name of the design cloud job.

        Returns:
        :   The name of the design cloud job.

        Return type:
        :   str

    get\_status() → str[](#keysight.ads.experimental_simulation.hpc.Job.get_status "Link to this definition")
    :   Get the status of thejob.

        Returns:
        :   The status of the design cloud job.

        Return type:
        :   str

    is\_running() → bool[](#keysight.ads.experimental_simulation.hpc.Job.is_running "Link to this definition")
    :   Check if the design cloud job is running.

        Returns:
        :   True if the design cloud job is running, False otherwise.

        Return type:
        :   bool

On this page

[Previous

SiteclusterResourceSettings](SiteclusterResourceSettings.md)
[Next

How-To](../../howto/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top