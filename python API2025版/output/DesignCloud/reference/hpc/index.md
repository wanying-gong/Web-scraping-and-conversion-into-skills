<!-- 来源: reference\hpc\index.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [Reference](../index.md)
* keysight.ads.experimental\_simulation

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/reference/hpc/index.rst.txt)

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
  + keysight.ads.experimental\_simulation
    - [ResourceSettings](ResourceSettings.md)
    - [LocalResourceSettings](LocalResourceSettings.md)
    - [SiteclusterResourceSettings](SiteclusterResourceSettings.md)
    - [Job](Job.md)
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

# keysight.ads.experimental\_simulation[](#module-keysight.ads.experimental_simulation.hpc "Link to this heading")

## Classes[](#classes "Link to this heading")

> * [ResourceSettings](ResourceSettings.md)
>   + [`ResourceSettings`](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings)
> * [LocalResourceSettings](LocalResourceSettings.md)
>   + [`LocalResourceSettings`](LocalResourceSettings.md#keysight.ads.experimental_simulation.hpc.LocalResourceSettings)
> * [SiteclusterResourceSettings](SiteclusterResourceSettings.md)
>   + [`SiteclusterResourceSettings`](SiteclusterResourceSettings.md#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings)
> * [Job](Job.md)
>   + [`Job`](Job.md#keysight.ads.experimental_simulation.hpc.Job)

## Functions[](#functions "Link to this heading")

keysight.ads.experimental\_simulation.hpc.submit\_design\_with\_settings(*design: Design*, *resourceSettings: [ResourceSettings](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.core.simulation.ResourceSettings")*) → [Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.core.simulation.Job")[](#keysight.ads.experimental_simulation.hpc.submit_design_with_settings "Link to this definition")
:   Submit a design with resource settings.

    Parameters:
    :   * **design** (*Design*) – The design to submit.
        * **resourceSettings** ([*ResourceSettings*](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.ResourceSettings")) – The resource settings to use.

    Returns:
    :   The submitted design cloud job.

    Return type:
    :   [Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.Job")

keysight.ads.experimental\_simulation.hpc.submit\_design(*design: Design*) → [Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.core.simulation.Job")[](#keysight.ads.experimental_simulation.hpc.submit_design "Link to this definition")
:   Submit a design with pre-saved resource settings.

    Parameters:
    :   **design** (*Design*) – The design to submit.

    Returns:
    :   The submitted design cloud job.

    Return type:
    :   [Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.Job")

keysight.ads.experimental\_simulation.hpc.submit\_netlist(*jobName: str*, *netlistPath: str*, *resourceSettings: [ResourceSettings](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.core.simulation.ResourceSettings")*) → [Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.core.simulation.Job")[](#keysight.ads.experimental_simulation.hpc.submit_netlist "Link to this definition")
:   Submit a netlist with resource settings.

    Parameters:
    :   * **jobName** (*str*) – The name of the job.
        * **netlistPath** (*str*) – The path to the netlist.
        * **resourceSettings** ([*ResourceSettings*](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.ResourceSettings")) – The resource settings to use.

    Returns:
    :   The submitted design cloud job.

    Return type:
    :   [Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.Job")

keysight.ads.experimental\_simulation.hpc.get\_jobs() → list[[Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.core.simulation.Job")][](#keysight.ads.experimental_simulation.hpc.get_jobs "Link to this definition")
:   Get the list of design cloud jobs.

    Return type:
    :   The list of submitted jobs

keysight.ads.experimental\_simulation.hpc.get\_resource\_settings(*design: Design*) → [ResourceSettings](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.ResourceSettings")[](#keysight.ads.experimental_simulation.hpc.get_resource_settings "Link to this definition")
:   Get the resource settings for a design.

    Parameters:
    :   **design** (*Design*) – The design to get the resource settings for.

    Returns:
    :   The resource settings of the design.

    Return type:
    :   [ResourceSettings](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.ResourceSettings")

keysight.ads.experimental\_simulation.hpc.set\_resource\_settings(*design: Design*, *settings: [ResourceSettings](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.ResourceSettings")*) → None[](#keysight.ads.experimental_simulation.hpc.set_resource_settings "Link to this definition")
:   Set the resource settings for a design.

    Parameters:
    :   * **design** (*Design*) – The design to set the resource settings for.
        * **settings** ([*ResourceSettings*](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.ResourceSettings")) – The resource settings to set.

On this page

[Previous

Reference](../index.md)
[Next

ResourceSettings](ResourceSettings.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top