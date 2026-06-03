# Design Cloud Python Documentation Knowledge Base
> 本文件由 MarkItDown 自动转换，BFS 遍历自 Keysight ADS2025 Update 2 Design Cloud Python Documentation HTML 文档。
> 共 28 个页面。

---

## 目录 (Table of Contents)

1. [index.md](#index)
2. [intro\index.md](#intro--index)
3. [intro\usage.md](#intro--usage)
4. [intro\vscode.md](#intro--vscode)
5. [reference\index.md](#reference--index)
6. [reference\hpc\index.md](#reference--hpc--index)
7. [reference\hpc\ResourceSettings.md](#reference--hpc--resourcesettings)
8. [reference\hpc\LocalResourceSettings.md](#reference--hpc--localresourcesettings)
9. [reference\hpc\SiteclusterResourceSettings.md](#reference--hpc--siteclusterresourcesettings)
10. [reference\hpc\Job.md](#reference--hpc--job)
11. [howto\index.md](#howto--index)
12. [howto\venv.md](#howto--venv)
13. [howto\newvenv.md](#howto--newvenv)
14. [howto\submit_simulations.md](#howto--submit_simulations)
15. [howto\submit_sims\local_queue.md](#howto--submit_sims--local_queue)
16. [howto\submit_sims\sitecluster_queue.md](#howto--submit_sims--sitecluster_queue)
17. [howto\submit_sims\dc_server.md](#howto--submit_sims--dc_server)
18. [howto\submit_sims\submit_netlist.md](#howto--submit_sims--submit_netlist)
19. [howto\submit_sims\submit_pre.md](#howto--submit_sims--submit_pre)
20. [howto\job.md](#howto--job)
21. [howto\manage_jobs\cancel_job.md](#howto--manage_jobs--cancel_job)
22. [howto\manage_jobs\job_name.md](#howto--manage_jobs--job_name)
23. [howto\manage_jobs\job_wait.md](#howto--manage_jobs--job_wait)
24. [howto\manage_jobs\job_list.md](#howto--manage_jobs--job_list)
25. [howto\manage_jobs\all_job_wait.md](#howto--manage_jobs--all_job_wait)
26. [examples\index.md](#examples--index)
27. [examples\ex_simulate_local_queue.md](#examples--ex_simulate_local_queue)
28. [examples\ex_simulate_dc_server.md](#examples--ex_simulate_dc_server)

---



---

## 1. index.md {#index}

# Design Cloud Python documentation[](#design-cloud-python-documentation "Link to this heading")

Contents:

* [Introduction](intro/index.md)
  + [Using Design Cloud Functionality in Python](intro/usage.md)
  + [Using Visual Studio Code](intro/vscode.md)
* [Reference](reference/index.md)
  + [keysight.ads.experimental\_simulation](reference/hpc/index.md)
* [How-To](howto/index.md)
  + [How to Set Up a Python Virtual Environment](howto/venv.md)
  + [How to Submit Simulations on Design Cloud Hosts](howto/submit_simulations.md)
  + [How to Manage Simulation Jobs](howto/job.md)
* [Examples](examples/index.md)
  + [Create and Simulate a Circuit on Design Cloud Local Queue](examples/ex_simulate_local_queue.md)
  + [Simulate a Circuit on Design Cloud Server](examples/ex_simulate_dc_server.md)


---

## 2. intro\index.md {#intro--index}

# Introduction[](#introduction "Link to this heading")

* [Using Design Cloud Functionality in Python](usage.md)
* [Using Visual Studio Code](vscode.md)


---

## 3. intro\usage.md {#intro--usage}

# Using Design Cloud Functionality in Python[](#using-design-cloud-functionality-in-python "Link to this heading")

Design Cloud provides Python APIs that allow a user to run circuit simulations
on the design cloud server, Local Queue or Site Cluster Queue

A Python script running outside ADS can access the functionality of Desing Cloud.

```
from keysight.ads.experimental_simulation import hpc
```

The `keysight.ads.experimental_simulation` package is not currently available as a pip-installable package.
To get access to this package, use any one of these approaches:

> 1. Use the Python interpreter in `$HPEESOF_DIR/tools/python`.
> 2. Create a virtual environment based on that interpreter. See [How to Set Up a Python Virtual Environment](../howto/venv.md).

Set the environment variable `HPEESOF_DIR` to point to your ADS installation prior to
using the `keysight.ads.experimental_simulation` package.


---

## 4. intro\vscode.md {#intro--vscode}

# Using Visual Studio Code[](#using-visual-studio-code "Link to this heading")

To invoke ADS Python from VS-Code:

> 1. In VS-Code, execute the menu "View->Command Palette…"
> 2. Type the command "Python:Select Interpreter"
> 3. Set the python interpreter by browsing to $HPEESOF\_DIR\tools\python\python.exe (python3 for linux)

To use a python virtual environment instead of the ADS python installation:

> 1. Set up a python virtual environment. see [How to Set Up a Python Virtual Environment](../howto/venv.md)
> 2. Repeat steps 1-3 above
> 3. Set the python interpreter by browsing to the python executable in the virtual environment.


---

## 5. reference\index.md {#reference--index}

# Reference[](#reference "Link to this heading")

* [keysight.ads.experimental\_simulation](hpc/index.md)
  + [Classes](hpc/index.md#classes)
    - [ResourceSettings](hpc/ResourceSettings.md)
    - [LocalResourceSettings](hpc/LocalResourceSettings.md)
    - [SiteclusterResourceSettings](hpc/SiteclusterResourceSettings.md)
    - [Job](hpc/Job.md)
  + [Functions](hpc/index.md#functions)
    - [`submit_design_with_settings()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_design_with_settings)
    - [`submit_design()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_design)
    - [`submit_netlist()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_netlist)
    - [`get_jobs()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.get_jobs)
    - [`get_resource_settings()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.get_resource_settings)
    - [`set_resource_settings()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.set_resource_settings)

**Indices**

* [Index](../genindex.md)
* [Module Index](../py-modindex.md)


---

## 6. reference\hpc\index.md {#reference--hpc--index}

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


---

## 7. reference\hpc\ResourceSettings.md {#reference--hpc--resourcesettings}

# ResourceSettings[](#resourcesettings "Link to this heading")

*class* keysight.ads.experimental\_simulation.hpc.ResourceSettings[](#keysight.ads.experimental_simulation.hpc.ResourceSettings "Link to this definition")
:   Bases: `object`

    Class to manage resource settings for design cloud simulations.

    *property* email\_address*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.email_address "Link to this definition")

    *property* max\_threads\_per\_job*: int*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.max_threads_per_job "Link to this definition")

    *property* memory\_unit*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.memory_unit "Link to this definition")

    *property* memory\_value*: int*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.memory_value "Link to this definition")

    *property* parallel\_jobs*: int*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.parallel_jobs "Link to this definition")

    *property* project\_name*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.project_name "Link to this definition")

    *property* queue*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.queue "Link to this definition")

    *property* site\_cluster\_extra\_options*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.site_cluster_extra_options "Link to this definition")

    *property* uploading\_filename*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.uploading_filename "Link to this definition")

    *property* url*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.url "Link to this definition")


---

## 8. reference\hpc\LocalResourceSettings.md {#reference--hpc--localresourcesettings}

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


---

## 9. reference\hpc\SiteclusterResourceSettings.md {#reference--hpc--siteclusterresourcesettings}

# SiteclusterResourceSettings[](#siteclusterresourcesettings "Link to this heading")

*class* keysight.ads.experimental\_simulation.hpc.SiteclusterResourceSettings[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings "Link to this definition")
:   Bases: [`ResourceSettings`](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.core.simulation.ResourceSettings")

    Class to manage site cluster resource settings for design cloud simulations.

    *property* email\_address*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.email_address "Link to this definition")

    *property* max\_threads\_per\_job*: int*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.max_threads_per_job "Link to this definition")

    *property* memory\_unit*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.memory_unit "Link to this definition")

    *property* memory\_value*: int*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.memory_value "Link to this definition")

    *property* parallel\_jobs*: int*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.parallel_jobs "Link to this definition")

    *property* project\_name*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.project_name "Link to this definition")

    *property* queue*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.queue "Link to this definition")

    set\_sitecluster\_path(*sitecluster: str*) → None[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.set_sitecluster_path "Link to this definition")
    :   Set the site cluster path.

        Parameters:
        :   **sitecluster** (*str*) – The site cluster path.

    *property* site\_cluster\_extra\_options*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.site_cluster_extra_options "Link to this definition")

    *property* uploading\_filename*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.uploading_filename "Link to this definition")

    *property* url*: str*[](#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings.url "Link to this definition")


---

## 10. reference\hpc\Job.md {#reference--hpc--job}

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


---

## 11. howto\index.md {#howto--index}

# How-To[](#how-to "Link to this heading")

* [How to Set Up a Python Virtual Environment](venv.md)
  + [Creating a new Python virtual environment based on ADS Python](newvenv.md)
* [How to Submit Simulations on Design Cloud Hosts](submit_simulations.md)
  + [Submitting simulations on a Local Queue](submit_sims/local_queue.md)
  + [Submitting simulations on a Site Cluster Queue](submit_sims/sitecluster_queue.md)
  + [Submitting Simulations on a Design Cloud Server](submit_sims/dc_server.md)
  + [Submit a Netlist to Design Cloud Server](submit_sims/submit_netlist.md)
  + [Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings](submit_sims/submit_pre.md)
* [How to Manage Simulation Jobs](job.md)
  + [Cancel a Job](manage_jobs/cancel_job.md)
  + [Get the name of a job](manage_jobs/job_name.md)
  + [Wait for a Job to Complete](manage_jobs/job_wait.md)
  + [Get the List of Submitted Jobs](manage_jobs/job_list.md)
  + [Wait for All Jobs to Complete](manage_jobs/all_job_wait.md)


---

## 12. howto\venv.md {#howto--venv}

# How to Set Up a Python Virtual Environment[](#how-to-set-up-a-python-virtual-environment "Link to this heading")

It is possible to use ADS modules from a Python virtual environment rather than within the embedded ADS Python.
To do this you can create a new virtual environment based on the ADS Python executable.

* [Creating a new Python virtual environment based on ADS Python](newvenv.md)


---

## 13. howto\newvenv.md {#howto--newvenv}

# Creating a new Python virtual environment based on ADS Python[](#creating-a-new-python-virtual-environment-based-on-ads-python "Link to this heading")

1. Create a Python virtual environment (venv).

   The venv must be created using the Python shipped with ADS, or with another Python installation with the same major and minor version.

   Example for Linux:

   ```
   $HPEESOF_DIR/tools/python/bin/python3 -m venv --system-site-packages $HOME/ads_venv
   ```

   Example for Windows:

   ```
   %HPEESOF_DIR%\tools\python\python -m venv --system-site-packages %USERPROFILE%\ads_venv
   ```
2. Select the venv by setting **ADS\_PYTHONHOME**.

   This can be accomplished either as an environment variable or in de\_sim.cfg (user level or above, i.e. not supported in workspace-level cfg)

   Example for Linux:

   ```
   export ADS_PYTHONHOME=$HOME/ads_venv
   ```

   Example for Windows:

   ```
   set ADS_PYTHONHOME=%USERPROFILE%\ads_venv
   ```

   To set the venv path in de\_sim.cfg rather than an environment variable, add a line like this:

   ```
   ADS_PYTHONHOME={$HOME}/ads_venv
   ```
3. Run ADS. Python support is automatically enabled.

   ```
   ads
   ```

   To verify the venv is being used, execute menu **Python->Python Console…**, and type the following in the console:

   ```
   import sys
   print(sys.executable)
   ```

   The path to the Python executable will be displayed, and it should be prefixed by the venv path.


---

## 14. howto\submit_simulations.md {#howto--submit_simulations}

# How to Submit Simulations on Design Cloud Hosts[](#how-to-submit-simulations-on-design-cloud-hosts "Link to this heading")

* [Submitting simulations on a Local Queue](submit_sims/local_queue.md)
* [Submitting simulations on a Site Cluster Queue](submit_sims/sitecluster_queue.md)
* [Submitting Simulations on a Design Cloud Server](submit_sims/dc_server.md)
* [Submit a Netlist to Design Cloud Server](submit_sims/submit_netlist.md)
* [Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings](submit_sims/submit_pre.md)


---

## 15. howto\submit_sims\local_queue.md {#howto--submit_sims--local_queue}

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


---

## 16. howto\submit_sims\sitecluster_queue.md {#howto--submit_sims--sitecluster_queue}

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


---

## 17. howto\submit_sims\dc_server.md {#howto--submit_sims--dc_server}

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


---

## 18. howto\submit_sims\submit_netlist.md {#howto--submit_sims--submit_netlist}

# Submit a Netlist to Design Cloud Server[](#submit-a-netlist-to-design-cloud-server "Link to this heading")

If you have a netlist and want to submit it to the Design Cloud Server, you can use the `submit_netlist()` function.

```
from keysight.ads.experimental_simulation import hpc

resource_settings.url = 'https://mydesigncloudserver.com' # Replace with your Design Cloud server URL
resource_settings = hpc.ResourceSettings()
resource_settings.parallel_jobs = 8
resource_settings.threads = 4
resource_settings.memory_value = 16
resource_settings.memory_unit = 'GB'

# In case you want to upload a supporting file
resource_settings.uploading_filename = "/my/example/upload_file.upl" # Replace with your upl file path
resource_settings.queue = 'normal' # Replace with your queue name

job = hpc.submit_netlist(netlist)  # Where netlist is the netlist object: db.Netlist

# You can also check the status of the job
job_status = job.get_status()
print(job_status)
```


---

## 19. howto\submit_sims\submit_pre.md {#howto--submit_sims--submit_pre}

# Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings[](#submitting-simulations-on-a-design-cloud-server-with-pre-defined-resource-settings "Link to this heading")

If the design context is already set up with the resource settings, you can directly submit the design to the Design Cloud Server using you can use the `submit_design()` function.

```
from keysight.ads.experimental_simulation import hpc

# To view the resource settings saved in the context
resource_settings = hpc.get_resource_settings()
print(resource_settings)

job = hpc.submit_design(design)  # Where design is the design object: db.Design

# You can also check the status of the job
job_status = job.get_status()
print(job_status)

# You can also set the same resource settings to a different design

design2 = db.Design()
hpc.set_resource_settings(design2, resource_settings)
job2 = hpc.submit_design(design2)

# You can also check the status of the job
job_status2 = job2.get_status()
print(job_status2)
```


---

## 20. howto\job.md {#howto--job}

# How to Manage Simulation Jobs[](#how-to-manage-simulation-jobs "Link to this heading")

Once you submit your job with the resource settings to a Design Cloud host, you can perform various operations on the job such as:
- cancel a running/pending job
- get the status of a job
- wait for a job to complete

* [Cancel a Job](manage_jobs/cancel_job.md)
* [Get the name of a job](manage_jobs/job_name.md)
* [Wait for a Job to Complete](manage_jobs/job_wait.md)
* [Get the List of Submitted Jobs](manage_jobs/job_list.md)
* [Wait for All Jobs to Complete](manage_jobs/all_job_wait.md)


---

## 21. howto\manage_jobs\cancel_job.md {#howto--manage_jobs--cancel_job}

# Cancel a Job[](#cancel-a-job "Link to this heading")

To cancel a job, you can use the `cancel()` function. We assume that you already have a design to submit with the resource settings.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.ResourceSettings()
resource_settings.url = "https://mydesigncloudserver.com"  # Replace with your Design Cloud Server URL
resource_settings.parallel_jobs = 4
resource_settings.max_threads_per_job = 4
job = hpc.submit_design_with_settings(design, resource_settings)

# Cancel a running job
if job.is_running():
    job.cancel()

# Cancel a pending job
job_status = job.get_status()
if job_status == "Pending":
    job.cancel()

# Valid job status values:
# - "Running"
# - "Pending"
# - "Completed"
# - "Error"
# - "Canceled"
# - "UnknownId"
# - "Downloading"
```


---

## 22. howto\manage_jobs\job_name.md {#howto--manage_jobs--job_name}

# Get the name of a job[](#get-the-name-of-a-job "Link to this heading")

To get the name of a job, you can use the `get_name()` function.

```
from keysight.ads.experimental_simulation import hpc
job = hpc.submit_design_with_settings(design, resource_settings)

job_name = job.get_name()
print(job_name)
```


---

## 23. howto\manage_jobs\job_wait.md {#howto--manage_jobs--job_wait}

# Wait for a Job to Complete[](#wait-for-a-job-to-complete "Link to this heading")

To wait for a job to complete, you can use the `await_job()` function. This function takes an argument timeout which is the maximum time to wait for the job to complete.

```
from keysight.ads.experimental_simulation import hpc
job = hpc.submit_design_with_settings(design, resource_settings)

job.await_job(timeout=60)  # Wait for 60 seconds

# If the job is completed, the function will return True
# If the job is not completed within the timeout, the function will return False

# You can also check the status of the job
job_status = job.get_status()
print(job_status)
```


---

## 24. howto\manage_jobs\job_list.md {#howto--manage_jobs--job_list}

# Get the List of Submitted Jobs[](#get-the-list-of-submitted-jobs "Link to this heading")

To get the list of submitted jobs, you can use the `get_jobs()` function. This function returns a list of all the jobs submitted by the user.

```
from keysight.ads.experimental_simulation import hpc
jobs = hpc.get_jobs()
print(jobs)
```


---

## 25. howto\manage_jobs\all_job_wait.md {#howto--manage_jobs--all_job_wait}

# Wait for All Jobs to Complete[](#wait-for-all-jobs-to-complete "Link to this heading")

To wait for all jobs to complete, you can use the `await_all_jobs()` function. This function takes an argument timeout which is the maximum time to wait for all jobs to complete.

```
from keysight.ads.experimental_simulation import hpc
jobs = hpc.get_jobs()

# If you wish to wait for all jobs to complete
status = hpc.await_all_jobs(jobs)
print(status)

# If you wish to wait for all jobs to complete within a timeout
status = hpc.await_all_jobs(jobs, timeout=60) # Wait for 60 seconds
print(status)

# If all jobs are completed, the function will return True
# If all jobs are not completed within the timeout, the function will return False

# You can also check the status of each job
for job in jobs:
    job_status = job.get_status()
    print(job_status)
```


---

## 26. examples\index.md {#examples--index}

# Examples[](#examples "Link to this heading")

Contents:

* [Create and Simulate a Circuit on Design Cloud Local Queue](ex_simulate_local_queue.md)
* [Simulate a Circuit on Design Cloud Server](ex_simulate_dc_server.md)


---

## 27. examples\ex_simulate_local_queue.md {#examples--ex_simulate_local_queue}

# Create and Simulate a Circuit on Design Cloud Local Queue[](#create-and-simulate-a-circuit-on-design-cloud-local-queue "Link to this heading")

This example will create a new workspace in your `HOME` directory called create\_simulate\_on\_hpc\_wrk. In the workspace a new library and schematic are created and populated with an RC filter. Next, the circuit will be subitted to the design cloud local queue for simulation.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example demonstrates how to run a simulation on Design Cloud using
Python APIs provided by Keysight Advanced Design System (ADS).
"""

import os
from pathlib import Path
from keysight.ads import de
from keysight.ads.de import db_uu as db
from keysight.ads.experimental_simulation import hpc

def create_workspace_and_design_then_simulate_on_hpc() -> None:
    """
    Create a new workspace, design and simulate it on HPC
    """
    home_dir = os.environ["HOME"]
    workspace_path = os.path.join(home_dir, "create_simulate_on_hpc_wrk")

    workspace_directory = Path(workspace_path)
    if workspace_directory.exists():
        raise RuntimeError(f"Workspace directory already exists: {workspace_path}")

    # Create the workspace
    workspace = de.create_workspace(workspace_path)
    workspace.open()

    create_design_then_simulate_over_hpc(workspace)

def create_design_then_simulate_over_hpc(workspace: de.Workspace) -> None:
    """
    Create a new design and simulate it on HPC
    """
    # Create a new library
    lib_dir = os.path.join(workspace.path, "low_pass_filter_lib")
    de.create_new_library("low_pass_filter_lib", lib_dir)
    workspace.add_library("low_pass_filter_lib", lib_dir, de.LibraryMode.NON_SHARED)

    # Create a new schematic
    design = db.create_schematic("low_pass_filter_lib:cell:schematic")

    # add components to the schematic
    design.add_instance(("ads_sources", "V_AC", "symbol"), (-2, 0), name="SRC1", angle=-90)
    r = design.add_instance(("ads_rflib", "R", "symbol"), (0, 0), name="R1", angle=0)
    r.parameters["R"].value = "3.0 kOhm"
    c = design.add_instance(("ads_rflib", "C", "symbol"), (2, 0), name="C1", angle=-90)
    c.parameters["C"].value = "1.0 uF"

    design.add_instance(("ads_rflib", "GROUND", "symbol"), (-2, -1), angle=-90)
    design.add_instance(("ads_rflib", "GROUND", "symbol"), (2, -1), angle=-90)

    design.add_wire([(-2.0, 0.0), (0.0, 0.0)])
    wire = design.add_wire([(1.0, 0.0), (2.0, 0.0)])

    wire.add_wire_label("R1_v")

    ac = design.add_instance(("ads_simulation", "AC", "symbol"), (-4, 1), name="AC1", angle=0)
    ac.parameters["Start"].value = "1.0 Hz"

    ac.parameters["Stop"].value = "1.0 MHz"
    ac.parameters["Dec"].value = "5"
    ac.parameters["Step"].value = ""

    v = design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 2), name="VAR1", angle=-90)
    assert v.is_var_instance

    v.vars["X"] = "1.0"
    v.vars["Y"] = "X/2.0"
    design.save_design()

    # Submit the design to HPC for simulation
    submit_design_to_hpc(design)

def submit_design_to_hpc(design: db.Design) -> None:
    """
    Submit the design to Local Queue for simulation
    """

    # Setting resources for the simulation
    settings = hpc.LocalResourceSettings()
    settings.parallel_jobs = 2
    settings.max_threads_per_job = 4
    settings.memory_value = 8
    settings.memory_unit = "GB"

    # Submit the test bench with the settings to the HPC
    job = hpc.submit_design_with_settings(design, settings)

    check_job_status(job)

def check_job_status(job: hpc.Job) -> None:
    """
    Check the job status
    """

    # Wait for the job to complete
    job.await_job(600)

    # Check the job status
    job_status = job.get_status()
    print(f"Job status: {job_status}")

create_workspace_and_design_then_simulate_on_hpc()
```


---

## 28. examples\ex_simulate_dc_server.md {#examples--ex_simulate_dc_server}

# Simulate a Circuit on Design Cloud Server[](#simulate-a-circuit-on-design-cloud-server "Link to this heading")

This example will unarchive an ADS example BatchSim\_Example1\_wrk in your in your `HOME` directory and run Batch\_CSVSweep test bench on the design cloud server. Note that a dummy design cloud server is shown in the example. Please replace it with your own server.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example uses existing ADS example "BatchSim_Example1_wrk:Batch_CSVSweep" to demonstrate how to run a
simulation on Design Cloud Server using Python APIs provided by Keysight Advanced Design System (ADS).
"""

import os
from pathlib import Path
from keysight.ads import de
from keysight.ads.de import db_uu as db
from keysight.ads.experimental_simulation import hpc

def unarchive_workspace_and_open_design_then_simulate_on_hpc_server() -> None:
    """
    Unarchive a workspace, open a design and simulate it on HPC Server
    """
    home_dir = os.environ["HOME"]
    example_wrk_path = os.path.join(
        os.environ["HPEESOF_DIR"], "examples", "RF_Microwave", "BatchSim_Example1_wrk.7zads"
    )

    workspace_path = os.path.join(home_dir, "BatchSim_Example1_wrk")
    workspace_path = Path(workspace_path)
    if workspace_path.exists():
        raise RuntimeError(f"Workspace directory already exists: {workspace_path}")

    # Unarchive the workspace
    de.unarchive_file(example_wrk_path, home_dir, exclude_em_files=True)

    # Open the workspace
    de.open_workspace(workspace_path)
    design = db.open_design("BatchSim_Example1_lib:Batch_CSVSweep:schematic", db.DesignMode.APPEND)

    # Simulate the design on HPC Server
    simulate_on_hpc_server(design)

def simulate_on_hpc_server(design: db.Design) -> None:
    """
    Simulate the design on HPC Server
    """

    # Set the resource settings for the simulation
    resource_settings = hpc.ResourceSettings()
    resource_settings.url = "https://mydesigncloudserver.com"  # Replace with your Design Cloud Server URL
    resource_settings.parallel_jobs = 4
    resource_settings.max_threads_per_job = 4
    resource_settings.memory_value = 8
    resource_settings.memory_unit = "GB"
    resource_settings.queue = "normal"  # Replace with your queue name

    # If you have a upload file, you can set it here
    # resource_settings.uploading_filename = "/my/example/upload_file.upl"

    # To notify the job status over email, you can set the email here
    # Note that your underlying cluster should be configured to send emails
    # resource_settings.email = "myemail@address.com" # Replace with your email address

    # To add extra options for the site cluster, you can set it here
    # resource_settings.site_cluster_extra_options = "--customargs \"-q normal\"" # Replace with your custom args

    # Simulate the design on HPC Server
    job = hpc.submit_design_with_settings(design, resource_settings)

    check_job_status(job)

def check_job_status(job: hpc.Job) -> None:
    """
    Check the job status
    """

    # Let's assume the job will finish within 10 minutes
    # You can change the timeout value based on your job
    # The job will wait until the job is finished or the timeout is reached
    job.await_job(600)

    # Check the job status
    job_status = job.get_status()
    print(f"Job status: {job_status}")

unarchive_workspace_and_open_design_then_simulate_on_hpc_server()
```
