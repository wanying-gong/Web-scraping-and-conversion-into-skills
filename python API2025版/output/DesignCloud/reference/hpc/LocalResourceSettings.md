<!-- 来源: reference\hpc\LocalResourceSettings.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.experimental\_simulation](index.md)
* LocalResourceSettings

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/reference/hpc/LocalResourceSettings.rst.txt)

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
    - LocalResourceSettings
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

# LocalResourceSettings[](#localresourcesettings "Link to this heading")

*class* keysight.ads.experimental\_simulation.hpc.LocalResourceSettings[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings "Link to this definition")
:   Bases: [`ResourceSettings`](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.core.simulation.ResourceSettings")

    Class to manage local resource settings for design cloud simulations.

    *property* email\_address*: str*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.email_address "Link to this definition")

    *property* max\_threads\_per\_job*: int*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.max_threads_per_job "Link to this definition")

    *property* memory\_unit*: str*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.memory_unit "Link to this definition")

    *property* memory\_value*: int*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.memory_value "Link to this definition")

    *property* parallel\_jobs*: int*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.parallel_jobs "Link to this definition")

    *property* project\_name*: str*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.project_name "Link to this definition")

    *property* queue*: str*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.queue "Link to this definition")

    *property* site\_cluster\_extra\_options*: str*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.site_cluster_extra_options "Link to this definition")

    *property* uploading\_filename*: str*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.uploading_filename "Link to this definition")

    *property* url*: str*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.url "Link to this definition")

On this page

[Previous

ResourceSettings](ResourceSettings.md)
[Next

SiteclusterResourceSettings](SiteclusterResourceSettings.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top