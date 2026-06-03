<!-- 来源: reference\hpc\SiteclusterResourceSettings.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.experimental\_simulation](index.md)
* SiteclusterResourceSettings

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/reference/hpc/SiteclusterResourceSettings.rst.txt)

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
    - SiteclusterResourceSettings
    - [Job](Job.md)
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

# SiteclusterResourceSettings[](#siteclusterresourcesettings "Link to this heading")

*class* SiteclusterResourceSettings(*sitecluster: str*, *parallel\_jobs: int = 1*, *max\_threads\_per\_job: int = 0*, *memory\_value: int = 0*, *memory\_unit: str = 'MiB'*, *queue: str = ''*, *email\_address: str = ''*, *project\_name: str = ''*, *site\_cluster\_extra\_options: str = ''*)[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings "Link to this definition")
:   Bases: [`ResourceSettings`](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.core.simulation.ResourceSettings")

    Class to manage site cluster resource settings for design cloud simulations.

    Initialize site cluster resource settings for design cloud simulations.

    Site cluster resource settings are used for running simulations on a remote site cluster.
    The URL is automatically constructed from the sitecluster path and cannot be set directly.

    Parameters:
    :   * **sitecluster** (*str*) – The path to the sitecluster wrapper, e.g. `/path/to/sitecluster|.sh|.bat`.
        * **parallel\_jobs** (*int**,* *optional*) – The number of parallel subjobs to run. Defaults to 1.
        * **max\_threads\_per\_job** (*int**,* *optional*) – The maximum number of threads per job. Defaults to 0, which means the number of threads is unrestricted.
        * **memory\_value** (*int**,* *optional*) – The numerical value of the memory to use. Defaults to 0, which typically means that no memory values
          will be passed to the cluster.
        * **memory\_unit** (*str**,* *optional*) – The memory unit to use. Supported values are `MB`, `MiB`, `GB`, `GiB`, `TB`, `TiB`. Defaults to `MiB`.
        * **queue** (*str**,* *optional*) – The queue to submit the job to. Defaults to empty string.
        * **email\_address** (*str**,* *optional*) – The email address to send the job status notification to. Defaults to empty string.
        * **project\_name** (*str**,* *optional*) – The project name to use. Defaults to empty string.
        * **site\_cluster\_extra\_options** (*str**,* *optional*) – Additional sitecluster options that will be passed while submitting a simulation.

    *property* sitecluster*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.sitecluster "Link to this definition")
    :   The path to the sitecluster wrapper, e.g. `/path/to/sitecluster|.sh|.bat`.

    *property* email\_address*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.email_address "Link to this definition")
    :   The email address that will be passed to sitecluster.

    *property* max\_threads\_per\_job*: int*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.max_threads_per_job "Link to this definition")
    :   The maximum number of threads per job.

        Defaults to 0, which means the number of threads is unrestricted.

    *property* memory\_unit*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.memory_unit "Link to this definition")
    :   The memory unit to use.

        Supported values are `MB`, `MiB`, `GB`, `GiB`, `TB`, `TiB`. Defaults to `MiB`.

    *property* memory\_value*: int*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.memory_value "Link to this definition")
    :   The numerical value of the memory to use. See [`memory_unit()`](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings.memory_unit "keysight.ads.experimental_simulation.hpc.ResourceSettings.memory_unit") for the unit.

        This defaults to zero which typically means that no memory values will be passed to the cluster.

    *property* parallel\_jobs*: int*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.parallel_jobs "Link to this definition")
    :   The number of parallel subjobs to run. Defaults to 1.

    *property* project\_name*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.project_name "Link to this definition")
    :   The project name that will be passed to sitecluster.

    *property* queue*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.queue "Link to this definition")
    :   The queue to submit the job to.

    *property* site\_cluster\_extra\_options*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.site_cluster_extra_options "Link to this definition")
    :   Additional sitecluster options that will be passed while submitting a simulation.

On this page

[Previous

LocalResourceSettings](LocalResourceSettings.md)
[Next

Job](Job.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top