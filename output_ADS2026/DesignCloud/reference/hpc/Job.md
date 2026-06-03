<!-- 来源: reference\hpc\Job.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.experimental\_simulation](index.md)
* Job

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/reference/hpc/Job.rst.txt)

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
    - Job
    - [JobStartupInfo](JobStartupInfo.md)
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

# Job[](#job "Link to this heading")

*class* Job(*name: str*)[](#keysight.ads.experimental_simulation.hpc.Job "Link to this definition")
:   Bases: `object`

    Class to manage simulation jobs.

    get\_name() → str[](#keysight.ads.experimental_simulation.hpc.Job.get_name "Link to this definition")
    :   Get the name of the design cloud job.

        Returns:
        :   The name of the design cloud job.

        Return type:
        :   str

    get\_status() → [JobStatus](JobStatus.md#keysight.ads.experimental_simulation.hpc.JobStatus "keysight.ads.experimental_simulation.hpc.core.simulation.JobStatus")[](#keysight.ads.experimental_simulation.hpc.Job.get_status "Link to this definition")
    :   Get the status of the job.

        Returns:
        :   * *JobStatus* – The status of the job.
            * *Possible values are defined in the JobStatus enum*
            * **- UNKNOWN** (*Status is unknown*)
            * **- READY** (*Job is ready to be submitted*)
            * **- SENDING** (*Job is being sent to the server*)
            * **- SUBMITTED** (*Job has been submitted to the server*)
            * **- PENDING** (*Job is pending execution*)
            * **- RUNNING** (*Job is currently running*)
            * **- SUSPENDED** (*Job has been suspended*)
            * **- READY\_TO\_DOWNLOAD** (*Job is ready to download results*)
            * **- DOWNLOADING** (*Results are being downloaded*)
            * **- COMPLETED** (*Job has completed successfully*)
            * **- UNKNOWN\_ID** (*Job ID is unknown*)
            * **- ERROR** (*Job encountered an error*)
            * **- CANCELLED** (*Job was cancelled*)
            * **- DELETED** (*Job was deleted*)
            * Note that if you want to check if a job is running or not use [`is_running()`](#keysight.ads.experimental_simulation.hpc.Job.is_running "keysight.ads.experimental_simulation.hpc.Job.is_running")
            * *rather than checking if the status is JobStatus.RUNNING.*

    get\_output() → str[](#keysight.ads.experimental_simulation.hpc.Job.get_output "Link to this definition")
    :   Get the job log output.

        Returns:
        :   The output log the design cloud job.

        Return type:
        :   str

    get\_subjob\_output() → list[str][](#keysight.ads.experimental_simulation.hpc.Job.get_subjob_output "Link to this definition")
    :   Gets the output for any subjobs.

        Subjob output is only available when a job is complete (get\_status() returns “COMPLETED”) and has been downloaded,
        if called before it will return a list of empty strings.

        Returns:
        :   A list of strings, one for each subjob.

        Return type:
        :   str

    get\_subjob\_status() → list[[JobStatus](JobStatus.md#keysight.ads.experimental_simulation.hpc.JobStatus "keysight.ads.experimental_simulation.hpc.core.simulation.JobStatus")][](#keysight.ads.experimental_simulation.hpc.Job.get_subjob_status "Link to this definition")
    :   Gets the status for any subjobs.

        Returns:
        :   * *list[JobStatus]* – A list of sub job statuses.
            * The possible values are the same as for [`get_status()`](#keysight.ads.experimental_simulation.hpc.Job.get_status "keysight.ads.experimental_simulation.hpc.Job.get_status").

    get\_startup\_info() → [JobStartupInfo](JobStartupInfo.md#keysight.ads.experimental_simulation.hpc.JobStartupInfo "keysight.ads.experimental_simulation.hpc.core.simulation.JobStartupInfo")[](#keysight.ads.experimental_simulation.hpc.Job.get_startup_info "Link to this definition")
    :   Get the startup information of the job. This will not change as the job runs.

        Returns:
        :   The startup information of the job.

        Return type:
        :   [JobStartupInfo](JobStartupInfo.md#keysight.ads.experimental_simulation.hpc.JobStartupInfo "keysight.ads.experimental_simulation.hpc.JobStartupInfo")

    is\_running() → bool[](#keysight.ads.experimental_simulation.hpc.Job.is_running "Link to this definition")
    :   Check if the design cloud job is running.

        Returns:
        :   True if the design cloud job is running, False otherwise.

        Return type:
        :   bool

    cancel() → None[](#keysight.ads.experimental_simulation.hpc.Job.cancel "Link to this definition")
    :   Cancel the job.

    remove() → None[](#keysight.ads.experimental_simulation.hpc.Job.remove "Link to this definition")
    :   Remove the job from the design cloud server.

    await\_job(*timeout: int = 0*) → None[](#keysight.ads.experimental_simulation.hpc.Job.await_job "Link to this definition")
    :   Wait for the job to complete.

        Parameters:
        :   **timeout** – An optional timeout in seconds. Defaults to 0, i.e no timeout.

On this page

[Previous

SiteclusterResourceSettings](SiteclusterResourceSettings.md)
[Next

JobStartupInfo](JobStartupInfo.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top