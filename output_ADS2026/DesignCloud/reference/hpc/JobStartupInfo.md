<!-- 来源: reference\hpc\JobStartupInfo.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.experimental\_simulation](index.md)
* JobStartupInfo

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/reference/hpc/JobStartupInfo.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

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
    - [SimulationMode](SimulationMode.md)
    - [JobStatus](JobStatus.md)
    - [ResourceSettings](ResourceSettings.md)
    - [LocalResourceSettings](LocalResourceSettings.md)
    - [SiteclusterResourceSettings](SiteclusterResourceSettings.md)
    - [Job](Job.md)
    - JobStartupInfo
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
    - [Polling the Status of a Job](../../howto/manage_jobs/polling_status.md)
    - [Getting the dataset after a simulation](../../howto/manage_jobs/get_dataset.md)
    - [Checking for Running Jobs](../../howto/manage_jobs/check_running_jobs.md)
* [Examples](../../examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)
  + [Simulate multiple designs of a workspace on Design Cloud](../../examples/ex_simulate_multiple_designs.md)
  + [Run RFPro Simulation on Design Cloud Server](../../examples/ex_run_rfpro_simulation_on_dc_server.md)

# JobStartupInfo[](#jobstartupinfo "Link to this heading")

*class* JobStartupInfo[](#keysight.ads.experimental_simulation.hpc.JobStartupInfo "Link to this definition")
:   Bases: `object`

    Class containing job startup information. Returned by [`Job.get_startup_info()`](Job.md#keysight.ads.experimental_simulation.hpc.Job.get_startup_info "keysight.ads.experimental_simulation.hpc.Job.get_startup_info").

    *property* start\_time*: datetime*[](#keysight.ads.experimental_simulation.hpc.JobStartupInfo.start_time "Link to this definition")
    :   The start time of the job.

        Returns:
        :   The start time of the job.

        Return type:
        :   datetime.datetime

    *property* url*: str*[](#keysight.ads.experimental_simulation.hpc.JobStartupInfo.url "Link to this definition")
    :   The URL that the job was submitted to.

        Returns:
        :   The URL that the job was submitted to.

        Return type:
        :   str

    *property* queue*: str*[](#keysight.ads.experimental_simulation.hpc.JobStartupInfo.queue "Link to this definition")
    :   The queue that the job was submitted to.

        Returns:
        :   The queue that the job was submitted to.

        Return type:
        :   str

    *property* workspace\_dir*: str*[](#keysight.ads.experimental_simulation.hpc.JobStartupInfo.workspace_dir "Link to this definition")
    :   The directory of the workspace.

        Returns:
        :   The directory of the workspace.

        Return type:
        :   str

    *property* job\_dir*: str*[](#keysight.ads.experimental_simulation.hpc.JobStartupInfo.job_dir "Link to this definition")
    :   The job directory. This the working directory where files are copied to when the job is submitted.

        Returns:
        :   The job directory.

        Return type:
        :   str

    *property* dataset\_name*: str*[](#keysight.ads.experimental_simulation.hpc.JobStartupInfo.dataset_name "Link to this definition")
    :   The name of the dataset.

        The dataset file is typically stored in the workspace’s data directory and has a `.ds` extension.

        Returns:
        :   The name of the dataset.

        Return type:
        :   str

    *property* datadisplay\_name*: str*[](#keysight.ads.experimental_simulation.hpc.JobStartupInfo.datadisplay_name "Link to this definition")
    :   The name of the data display.

        Returns:
        :   The name of the data display.

        Return type:
        :   str

    *property* top\_level\_design*: str*[](#keysight.ads.experimental_simulation.hpc.JobStartupInfo.top_level_design "Link to this definition")
    :   The top-level design name.

        Returns:
        :   The top-level design name.

        Return type:
        :   str

On this page

[Previous

Job](Job.md)
[Next

How-To](../../howto/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top