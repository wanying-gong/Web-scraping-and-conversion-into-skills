# Reference
> **说明：** Reference 相关页面。

> **何时使用：** 当你需要查阅 Reference 相关内容时

---

## 本文件目录

- **keysight.ads.experimental\_simulation** (`reference/hpc/index.md`)
- **Job** (`reference/hpc/Job.md`)
- **LocalResourceSettings** (`reference/hpc/LocalResourceSettings.md`)
- **ResourceSettings** (`reference/hpc/ResourceSettings.md`)
- **SiteclusterResourceSettings** (`reference/hpc/SiteclusterResourceSettings.md`)
- **Reference** (`reference/index.md`)

---

<!-- === 来源: reference/hpc/index.md === -->

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

<!-- === 来源: reference/hpc/Job.md === -->

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

<!-- === 来源: reference/hpc/LocalResourceSettings.md === -->

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

<!-- === 来源: reference/hpc/ResourceSettings.md === -->

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

<!-- === 来源: reference/hpc/SiteclusterResourceSettings.md === -->

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

<!-- === 来源: reference/index.md === -->

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

