# Reference
> **说明：** Reference 相关页面。

> **何时使用：** 当你需要查阅 Reference 相关内容时

---

## 本文件目录

- **keysight.ads.experimental\_simulation** (`reference/hpc/index.md`)
- **Job** (`reference/hpc/Job.md`)
- **JobStartupInfo** (`reference/hpc/JobStartupInfo.md`)
- **JobStatus** (`reference/hpc/JobStatus.md`)
- **LocalResourceSettings** (`reference/hpc/LocalResourceSettings.md`)
- **ResourceSettings** (`reference/hpc/ResourceSettings.md`)
- **SimulationMode** (`reference/hpc/SimulationMode.md`)
- **SiteclusterResourceSettings** (`reference/hpc/SiteclusterResourceSettings.md`)
- **Reference** (`reference/index.md`)

---

<!-- === 来源: reference/hpc/index.md === -->

# keysight.ads.experimental\_simulation[](#module-keysight.ads.experimental_simulation.hpc "Link to this heading")

## Classes[](#classes "Link to this heading")

> * [SimulationMode](SimulationMode.md)
>   + [`SimulationMode`](SimulationMode.md#keysight.ads.experimental_simulation.hpc.SimulationMode)
> * [JobStatus](JobStatus.md)
>   + [`JobStatus`](JobStatus.md#keysight.ads.experimental_simulation.hpc.JobStatus)
> * [ResourceSettings](ResourceSettings.md)
>   + [`ResourceSettings`](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings)
> * [LocalResourceSettings](LocalResourceSettings.md)
>   + [`LocalResourceSettings`](LocalResourceSettings.md#keysight.ads.experimental_simulation.hpc.LocalResourceSettings)
> * [SiteclusterResourceSettings](SiteclusterResourceSettings.md)
>   + [`SiteclusterResourceSettings`](SiteclusterResourceSettings.md#keysight.ads.experimental_simulation.hpc.SiteclusterResourceSettings)
> * [Job](Job.md)
>   + [`Job`](Job.md#keysight.ads.experimental_simulation.hpc.Job)
> * [JobStartupInfo](JobStartupInfo.md)
>   + [`JobStartupInfo`](JobStartupInfo.md#keysight.ads.experimental_simulation.hpc.JobStartupInfo)

## Functions[](#functions "Link to this heading")

submit\_design\_with\_settings(*design: Design*, *resource\_settings: [ResourceSettings](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.core.simulation.ResourceSettings")*) → [Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.core.simulation.Job")[](#keysight.ads.experimental_simulation.hpc.submit_design_with_settings "Link to this definition")
:   Submit a design with resource settings.

    ### Args:[](#args "Link to this heading")

    > design (Design): The design to submit.
    > resource\_settings (ResourceSettings): The resource settings to use.

    ### Returns:[](#returns "Link to this heading")

    > Job: The submitted design cloud job. If the job could not be submitted, an exception is thrown.

submit\_design(*design: Design*) → [Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.core.simulation.Job")[](#keysight.ads.experimental_simulation.hpc.submit_design "Link to this definition")
:   Submit a design with pre-saved resource settings.

    Parameters:
    :   **design** (*Design*) – The design to submit.

    Returns:
    :   The submitted design cloud job. If the job could not be submitted, an exception is thrown.

    Return type:
    :   [Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.Job")

submit\_netlist(*jobname: str*, *netlist\_path: str*, *resource\_settings: [ResourceSettings](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.core.simulation.ResourceSettings")*) → [Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.core.simulation.Job")[](#keysight.ads.experimental_simulation.hpc.submit_netlist "Link to this definition")
:   Submit a netlist with resource settings.

    Parameters:
    :   * **jobname** (*str*) – The name of the job.
        * **netlist\_path** (*str*) – The path to the netlist.
        * **resource\_settings** ([*ResourceSettings*](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.ResourceSettings")) – The resource settings to use.

    Returns:
    :   The submitted design cloud job. If the job could not be submitted, an exception is thrown.

    Return type:
    :   [Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.Job")

get\_jobs() → list[[Job](Job.md#keysight.ads.experimental_simulation.hpc.Job "keysight.ads.experimental_simulation.hpc.core.simulation.Job")][](#keysight.ads.experimental_simulation.hpc.get_jobs "Link to this definition")
:   Get the list of design cloud jobs.

    Return type:
    :   The list of submitted jobs

get\_resource\_settings(*design: Design*) → [ResourceSettings](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.ResourceSettings")[](#keysight.ads.experimental_simulation.hpc.get_resource_settings "Link to this definition")
:   Get the resource settings for a design.

    Parameters:
    :   **design** (*Design*) – The design to get the resource settings for.

    Returns:
    :   The resource settings of the design.

    Return type:
    :   [ResourceSettings](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.ResourceSettings")

set\_resource\_settings(*design: Design*, *settings: [ResourceSettings](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.ResourceSettings")*) → None[](#keysight.ads.experimental_simulation.hpc.set_resource_settings "Link to this definition")
:   Set the resource settings for a design.

    Parameters:
    :   * **design** (*Design*) – The design to set the resource settings for.
        * **settings** ([*ResourceSettings*](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.ResourceSettings")) – The resource settings to set.

set\_simulation\_mode(*design: Design*, *mode: [SimulationMode](SimulationMode.md#keysight.ads.experimental_simulation.hpc.SimulationMode "keysight.ads.experimental_simulation.hpc.core.simulation.SimulationMode")*) → None[](#keysight.ads.experimental_simulation.hpc.set_simulation_mode "Link to this definition")
:   Set the simulation mode for a design.

    If you are using [`submit_design_with_settings()`](#keysight.ads.experimental_simulation.hpc.submit_design_with_settings "keysight.ads.experimental_simulation.hpc.submit_design_with_settings")
    or [`submit_design()`](#keysight.ads.experimental_simulation.hpc.submit_design "keysight.ads.experimental_simulation.hpc.submit_design"), you do not need to call this method, these methods
    set the mode to DESIGN\_CLOUD by default.

    If you have run Design Cloud simulations and wish to revert to Local simulations then you can call this method.

    Parameters:
    :   * **design** (*Design*) – The design to set the simulation mode for. Valid choices SimulationMode.LOCAL or SimulationMode.DESIGN\_CLOUD.
        * **mode** ([*SimulationMode*](SimulationMode.md#keysight.ads.experimental_simulation.hpc.SimulationMode "keysight.ads.experimental_simulation.hpc.SimulationMode")) – The simulation mode to set.

await\_all\_jobs(*timeout: int = 0*) → None[](#keysight.ads.experimental_simulation.hpc.await_all_jobs "Link to this definition")
:   Wait for all jobs to complete.

    Parameters:
    :   **timeout** – An optional timeout in seconds. Defaults to 0, i.e. no timeout.


---

<!-- === 来源: reference/hpc/Job.md === -->

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


---

<!-- === 来源: reference/hpc/JobStartupInfo.md === -->

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


---

<!-- === 来源: reference/hpc/JobStatus.md === -->

# JobStatus[](#jobstatus "Link to this heading")

*class* JobStatus(*value*, *names=<not given>*, *\*values*, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[](#keysight.ads.experimental_simulation.hpc.JobStatus "Link to this definition")
:   Bases: `StrEnum`

    String Enum representing possible job statuses.

    UNKNOWN *= 'Unknown'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.UNKNOWN "Link to this definition")

    READY *= 'Ready'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.READY "Link to this definition")

    SENDING *= 'Sending'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.SENDING "Link to this definition")

    SUBMITTED *= 'Submitted'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.SUBMITTED "Link to this definition")

    PENDING *= 'Pending'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.PENDING "Link to this definition")

    RUNNING *= 'Running'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.RUNNING "Link to this definition")

    SUSPENDED *= 'Suspended'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.SUSPENDED "Link to this definition")

    READY\_TO\_DOWNLOAD *= 'Ready to download'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.READY_TO_DOWNLOAD "Link to this definition")

    DOWNLOADING *= 'Downloading'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.DOWNLOADING "Link to this definition")

    COMPLETED *= 'Completed'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.COMPLETED "Link to this definition")

    UNKNOWN\_ID *= 'UnknownId'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.UNKNOWN_ID "Link to this definition")

    ERROR *= 'Error'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.ERROR "Link to this definition")

    CANCELLED *= 'Cancelled'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.CANCELLED "Link to this definition")

    DELETED *= 'Deleted'*[](#keysight.ads.experimental_simulation.hpc.JobStatus.DELETED "Link to this definition")

    encode(*encoding='utf-8'*, *errors='strict'*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.encode "Link to this definition")
    :   Encode the string using the codec registered for encoding.

        encoding
        :   The encoding in which to encode the string.

        errors
        :   The error handling scheme to use for encoding errors.
            The default is ‘strict’ meaning that encoding errors raise a
            UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and
            ‘xmlcharrefreplace’ as well as any other name registered with
            codecs.register\_error that can handle UnicodeEncodeErrors.

    replace(*old*, *new*, */*, *count=-1*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.replace "Link to this definition")
    :   Return a copy with all occurrences of substring old replaced by new.

        > count
        > :   Maximum number of occurrences to replace.
        >     -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.

    split(*sep=None*, *maxsplit=-1*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.split "Link to this definition")
    :   Return a list of the substrings in the string, using sep as the separator string.

        > sep
        > :   The separator used to split the string.
        >
        >     When set to None (the default value), will split on any whitespace
        >     character (including n r t f and spaces) and will discard
        >     empty strings from the result.
        >
        > maxsplit
        > :   Maximum number of splits.
        >     -1 (the default value) means no limit.

        Splitting starts at the front of the string and works to the end.

        Note, str.split() is mainly useful for data that has been intentionally
        delimited. With natural text that includes punctuation, consider using
        the regular expression module.

    rsplit(*sep=None*, *maxsplit=-1*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.rsplit "Link to this definition")
    :   Return a list of the substrings in the string, using sep as the separator string.

        > sep
        > :   The separator used to split the string.
        >
        >     When set to None (the default value), will split on any whitespace
        >     character (including n r t f and spaces) and will discard
        >     empty strings from the result.
        >
        > maxsplit
        > :   Maximum number of splits.
        >     -1 (the default value) means no limit.

        Splitting starts at the end of the string and works to the front.

    join(*iterable*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.join "Link to this definition")
    :   Concatenate any number of strings.

        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.

        Example: ‘.’.join([‘ab’, ‘pq’, ‘rs’]) -> ‘ab.pq.rs’

    capitalize()[](#keysight.ads.experimental_simulation.hpc.JobStatus.capitalize "Link to this definition")
    :   Return a capitalized version of the string.

        More specifically, make the first character have upper case and the rest lower
        case.

    casefold()[](#keysight.ads.experimental_simulation.hpc.JobStatus.casefold "Link to this definition")
    :   Return a version of the string suitable for caseless comparisons.

    title()[](#keysight.ads.experimental_simulation.hpc.JobStatus.title "Link to this definition")
    :   Return a version of the string where each word is titlecased.

        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.

    center(*width*, *fillchar=' '*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.center "Link to this definition")
    :   Return a centered string of length width.

        Padding is done using the specified fill character (default is a space).

    count()[](#keysight.ads.experimental_simulation.hpc.JobStatus.count "Link to this definition")
    :   Return the number of non-overlapping occurrences of substring sub in string S[start:end].

        Optional arguments start and end are interpreted as in slice notation.

    expandtabs(*tabsize=8*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.expandtabs "Link to this definition")
    :   Return a copy where all tab characters are expanded using spaces.

        If tabsize is not given, a tab size of 8 characters is assumed.

    find()[](#keysight.ads.experimental_simulation.hpc.JobStatus.find "Link to this definition")
    :   Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

        Optional arguments start and end are interpreted as in slice notation.
        Return -1 on failure.

    partition(*sep*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.partition "Link to this definition")
    :   Partition the string into three parts using the given separator.

        This will search for the separator in the string. If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.

    index()[](#keysight.ads.experimental_simulation.hpc.JobStatus.index "Link to this definition")
    :   Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

        Optional arguments start and end are interpreted as in slice notation.
        Raises ValueError when the substring is not found.

    ljust(*width*, *fillchar=' '*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.ljust "Link to this definition")
    :   Return a left-justified string of length width.

        Padding is done using the specified fill character (default is a space).

    lower()[](#keysight.ads.experimental_simulation.hpc.JobStatus.lower "Link to this definition")
    :   Return a copy of the string converted to lowercase.

    lstrip(*chars=None*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.lstrip "Link to this definition")
    :   Return a copy of the string with leading whitespace removed.

        If chars is given and not None, remove characters in chars instead.

    rfind()[](#keysight.ads.experimental_simulation.hpc.JobStatus.rfind "Link to this definition")
    :   Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

        Optional arguments start and end are interpreted as in slice notation.
        Return -1 on failure.

    rindex()[](#keysight.ads.experimental_simulation.hpc.JobStatus.rindex "Link to this definition")
    :   Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

        Optional arguments start and end are interpreted as in slice notation.
        Raises ValueError when the substring is not found.

    rjust(*width*, *fillchar=' '*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.rjust "Link to this definition")
    :   Return a right-justified string of length width.

        Padding is done using the specified fill character (default is a space).

    rstrip(*chars=None*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.rstrip "Link to this definition")
    :   Return a copy of the string with trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.

    rpartition(*sep*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.rpartition "Link to this definition")
    :   Partition the string into three parts using the given separator.

        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.

    splitlines(*keepends=False*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.splitlines "Link to this definition")
    :   Return a list of the lines in the string, breaking at line boundaries.

        Line breaks are not included in the resulting list unless keepends is given and
        true.

    strip(*chars=None*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.strip "Link to this definition")
    :   Return a copy of the string with leading and trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.

    swapcase()[](#keysight.ads.experimental_simulation.hpc.JobStatus.swapcase "Link to this definition")
    :   Convert uppercase characters to lowercase and lowercase characters to uppercase.

    translate(*table*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.translate "Link to this definition")
    :   Replace each character in the string using the given translation table.

        > table
        > :   Translation table, which must be a mapping of Unicode ordinals to
        >     Unicode ordinals, strings, or None.

        The table must implement lookup/indexing via \_\_getitem\_\_, for instance a
        dictionary or list. If this operation raises LookupError, the character is
        left untouched. Characters mapped to None are deleted.

    upper()[](#keysight.ads.experimental_simulation.hpc.JobStatus.upper "Link to this definition")
    :   Return a copy of the string converted to uppercase.

    startswith()[](#keysight.ads.experimental_simulation.hpc.JobStatus.startswith "Link to this definition")
    :   Return True if the string starts with the specified prefix, False otherwise.

        prefix
        :   A string or a tuple of strings to try.

        start
        :   Optional start position. Default: start of the string.

        end
        :   Optional stop position. Default: end of the string.

    endswith()[](#keysight.ads.experimental_simulation.hpc.JobStatus.endswith "Link to this definition")
    :   Return True if the string ends with the specified suffix, False otherwise.

        suffix
        :   A string or a tuple of strings to try.

        start
        :   Optional start position. Default: start of the string.

        end
        :   Optional stop position. Default: end of the string.

    removeprefix(*prefix*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.removeprefix "Link to this definition")
    :   Return a str with the given prefix string removed if present.

        If the string starts with the prefix string, return string[len(prefix):].
        Otherwise, return a copy of the original string.

    removesuffix(*suffix*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.removesuffix "Link to this definition")
    :   Return a str with the given suffix string removed if present.

        If the string ends with the suffix string and that suffix is not empty,
        return string[:-len(suffix)]. Otherwise, return a copy of the original
        string.

    isascii()[](#keysight.ads.experimental_simulation.hpc.JobStatus.isascii "Link to this definition")
    :   Return True if all characters in the string are ASCII, False otherwise.

        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.

    islower()[](#keysight.ads.experimental_simulation.hpc.JobStatus.islower "Link to this definition")
    :   Return True if the string is a lowercase string, False otherwise.

        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.

    isupper()[](#keysight.ads.experimental_simulation.hpc.JobStatus.isupper "Link to this definition")
    :   Return True if the string is an uppercase string, False otherwise.

        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.

    istitle()[](#keysight.ads.experimental_simulation.hpc.JobStatus.istitle "Link to this definition")
    :   Return True if the string is a title-cased string, False otherwise.

        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.

    isspace()[](#keysight.ads.experimental_simulation.hpc.JobStatus.isspace "Link to this definition")
    :   Return True if the string is a whitespace string, False otherwise.

        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.

    isdecimal()[](#keysight.ads.experimental_simulation.hpc.JobStatus.isdecimal "Link to this definition")
    :   Return True if the string is a decimal string, False otherwise.

        A string is a decimal string if all characters in the string are decimal and
        there is at least one character in the string.

    isdigit()[](#keysight.ads.experimental_simulation.hpc.JobStatus.isdigit "Link to this definition")
    :   Return True if the string is a digit string, False otherwise.

        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.

    isnumeric()[](#keysight.ads.experimental_simulation.hpc.JobStatus.isnumeric "Link to this definition")
    :   Return True if the string is a numeric string, False otherwise.

        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.

    isalpha()[](#keysight.ads.experimental_simulation.hpc.JobStatus.isalpha "Link to this definition")
    :   Return True if the string is an alphabetic string, False otherwise.

        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.

    isalnum()[](#keysight.ads.experimental_simulation.hpc.JobStatus.isalnum "Link to this definition")
    :   Return True if the string is an alpha-numeric string, False otherwise.

        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.

    isidentifier()[](#keysight.ads.experimental_simulation.hpc.JobStatus.isidentifier "Link to this definition")
    :   Return True if the string is a valid Python identifier, False otherwise.

        Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
        such as “def” or “class”.

    isprintable()[](#keysight.ads.experimental_simulation.hpc.JobStatus.isprintable "Link to this definition")
    :   Return True if all characters in the string are printable, False otherwise.

        A character is printable if repr() may use it in its output.

    zfill(*width*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.zfill "Link to this definition")
    :   Pad a numeric string with zeros on the left, to fill a field of the given width.

        The string is never truncated.

    format(*\*args*, *\*\*kwargs*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.format "Link to this definition")
    :   Return a formatted version of the string, using substitutions from args and kwargs.
        The substitutions are identified by braces (‘{’ and ‘}’).

    format\_map(*mapping*, */*)[](#keysight.ads.experimental_simulation.hpc.JobStatus.format_map "Link to this definition")
    :   Return a formatted version of the string, using substitutions from mapping.
        The substitutions are identified by braces (‘{’ and ‘}’).

    *static* maketrans()[](#keysight.ads.experimental_simulation.hpc.JobStatus.maketrans "Link to this definition")
    :   Return a translation table usable for str.translate().

        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.


---

<!-- === 来源: reference/hpc/LocalResourceSettings.md === -->

# LocalResourceSettings[](#localresourcesettings "Link to this heading")

*class* LocalResourceSettings(*parallel\_jobs: int = 1*, *max\_threads\_per\_job: int = 0*, *queue\_job\_locally: bool = False*, *uploading\_filename: str = ''*)[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings "Link to this definition")
:   Bases: [`ResourceSettings`](ResourceSettings.md#keysight.ads.experimental_simulation.hpc.ResourceSettings "keysight.ads.experimental_simulation.hpc.core.simulation.ResourceSettings")

    Class to manage local resource settings for design cloud simulations.

    Initialize local resource settings for design cloud simulations.

    Local resource settings are used for running simulations on the local machine.
    The URL is automatically set to ‘sitecluster://local’ and cannot be changed.

    Parameters:
    :   * **parallel\_jobs** (*int**,* *optional*) – The number of parallel subjobs to run. Defaults to 1.
        * **max\_threads\_per\_job** (*int**,* *optional*) – The maximum number of threads per job. Defaults to 0, which means the number of threads is unrestricted.
        * **queue\_job\_locally** (*bool**,* *optional*) – If True, the queue is set to “run\_local\_queue”, otherwise it’s set to “run\_local\_process”.
          Defaults to False.
        * **uploading\_filename** (*str**,* *optional*) – The path to a .upl file that controls how simulation job files are managed. Defaults to empty string.

    *property* queue*: str*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.queue "Link to this definition")
    :   The queue to submit the job to. Must be either “run\_local\_process” or “run\_local\_queue”.

    *property* queue\_job\_locally*: bool*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.queue_job_locally "Link to this definition")
    :   Whether jobs are queued locally or run directly.

        Returns:
        :   True if the queue is set to “run\_local\_queue”, False if set to “run\_local\_process”.

        Return type:
        :   bool

    *property* max\_threads\_per\_job*: int*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.max_threads_per_job "Link to this definition")
    :   The maximum number of threads per job.

        Defaults to 0, which means the number of threads is unrestricted.

    *property* parallel\_jobs*: int*[](#keysight.ads.experimental_simulation.hpc.LocalResourceSettings.parallel_jobs "Link to this definition")
    :   The number of parallel subjobs to run. Defaults to 1.


---

<!-- === 来源: reference/hpc/ResourceSettings.md === -->

# ResourceSettings[](#resourcesettings "Link to this heading")

*class* ResourceSettings(*url: str*, *parallel\_jobs: int = 1*, *max\_threads\_per\_job: int = 0*, *memory\_value: int = 0*, *memory\_unit: str = 'MiB'*, *queue: str = ''*, *email\_address: str = ''*, *project\_name: str = ''*, *uploading\_filename: str = ''*, *site\_cluster\_extra\_options: str = ''*)[](#keysight.ads.experimental_simulation.hpc.ResourceSettings "Link to this definition")
:   Bases: `object`

    Class to manage resource settings for design cloud simulations.

    Initialize resource settings for design cloud simulations.

    Parameters:
    :   * **url** (*str*) – The full URL of the design cloud host, e.g. ‘<https://mydesigncloudserver.com>’ or ‘<http://mydesigncloudserver.com>:<port>’.
        * **parallel\_jobs** (*int**,* *optional*) – The number of parallel subjobs to run. Defaults to 1.
        * **max\_threads\_per\_job** (*int**,* *optional*) – The maximum number of threads per job. Defaults to 0, which means the number of threads is unrestricted.
        * **memory\_value** (*int**,* *optional*) – The numerical value of the memory to use. Defaults to 0, which typically means that no memory values
          will be passed to the cluster.
        * **memory\_unit** (*str**,* *optional*) – The memory unit to use. Supported values are `MB`, `MiB`, `GB`, `GiB`, `TB`, `TiB`. Defaults to `MiB`.
        * **queue** (*str**,* *optional*) – The queue to submit the job to. Defaults to empty string.
        * **email\_address** (*str**,* *optional*) – The email address to send the job status notification to. Defaults to empty string.
        * **project\_name** (*str**,* *optional*) – The name of the project to use. Defaults to empty string.
        * **uploading\_filename** (*str**,* *optional*) – The path to a .upl file that controls how simulation job files are managed. Defaults to empty string.
        * **site\_cluster\_extra\_options** (*str**,* *optional*) – Additional sitecluster options that will be passed while submitting a simulation.
          Defaults to empty string.

    *property* url*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.url "Link to this definition")
    :   The full URL of the design cloud host.

        e.g. ‘<https://mydesigncloudserver.com>’ or ‘<http://mydesigncloudserver.com>:<port>’.
        This is a required property.

    *property* parallel\_jobs*: int*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.parallel_jobs "Link to this definition")
    :   The number of parallel subjobs to run. Defaults to 1.

    *property* queue*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.queue "Link to this definition")
    :   The queue to submit the job to.

    *property* site\_cluster\_extra\_options*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.site_cluster_extra_options "Link to this definition")
    :   Additional sitecluster options that will be passed while submitting a simulation.

    *property* max\_threads\_per\_job*: int*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.max_threads_per_job "Link to this definition")
    :   The maximum number of threads per job.

        Defaults to 0, which means the number of threads is unrestricted.

    *property* memory\_value*: int*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.memory_value "Link to this definition")
    :   The numerical value of the memory to use. See [`memory_unit()`](#keysight.ads.experimental_simulation.hpc.ResourceSettings.memory_unit "keysight.ads.experimental_simulation.hpc.ResourceSettings.memory_unit") for the unit.

        This defaults to zero which typically means that no memory values will be passed to the cluster.

    *property* memory\_unit*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.memory_unit "Link to this definition")
    :   The memory unit to use.

        Supported values are `MB`, `MiB`, `GB`, `GiB`, `TB`, `TiB`. Defaults to `MiB`.

    *property* email\_address*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.email_address "Link to this definition")
    :   The email address that will be passed to sitecluster.

    *property* project\_name*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.project_name "Link to this definition")
    :   The project name that will be passed to sitecluster.

    *property* uploading\_filename*: str*[](#keysight.ads.experimental_simulation.hpc.ResourceSettings.uploading_filename "Link to this definition")
    :   The path to a .upl file that controls how simulation job files are managed.


---

<!-- === 来源: reference/hpc/SimulationMode.md === -->

# SimulationMode[](#simulationmode "Link to this heading")

*class* SimulationMode(*value*, *names=<not given>*, *\*values*, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode "Link to this definition")
:   Bases: `StrEnum`

    Enum to represent available simulation modes.

    LOCAL *= 'Local'*[](#keysight.ads.experimental_simulation.hpc.SimulationMode.LOCAL "Link to this definition")

    DESIGN\_CLOUD *= 'Design Cloud'*[](#keysight.ads.experimental_simulation.hpc.SimulationMode.DESIGN_CLOUD "Link to this definition")

    encode(*encoding='utf-8'*, *errors='strict'*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.encode "Link to this definition")
    :   Encode the string using the codec registered for encoding.

        encoding
        :   The encoding in which to encode the string.

        errors
        :   The error handling scheme to use for encoding errors.
            The default is ‘strict’ meaning that encoding errors raise a
            UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and
            ‘xmlcharrefreplace’ as well as any other name registered with
            codecs.register\_error that can handle UnicodeEncodeErrors.

    replace(*old*, *new*, */*, *count=-1*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.replace "Link to this definition")
    :   Return a copy with all occurrences of substring old replaced by new.

        > count
        > :   Maximum number of occurrences to replace.
        >     -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.

    split(*sep=None*, *maxsplit=-1*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.split "Link to this definition")
    :   Return a list of the substrings in the string, using sep as the separator string.

        > sep
        > :   The separator used to split the string.
        >
        >     When set to None (the default value), will split on any whitespace
        >     character (including n r t f and spaces) and will discard
        >     empty strings from the result.
        >
        > maxsplit
        > :   Maximum number of splits.
        >     -1 (the default value) means no limit.

        Splitting starts at the front of the string and works to the end.

        Note, str.split() is mainly useful for data that has been intentionally
        delimited. With natural text that includes punctuation, consider using
        the regular expression module.

    rsplit(*sep=None*, *maxsplit=-1*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.rsplit "Link to this definition")
    :   Return a list of the substrings in the string, using sep as the separator string.

        > sep
        > :   The separator used to split the string.
        >
        >     When set to None (the default value), will split on any whitespace
        >     character (including n r t f and spaces) and will discard
        >     empty strings from the result.
        >
        > maxsplit
        > :   Maximum number of splits.
        >     -1 (the default value) means no limit.

        Splitting starts at the end of the string and works to the front.

    join(*iterable*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.join "Link to this definition")
    :   Concatenate any number of strings.

        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.

        Example: ‘.’.join([‘ab’, ‘pq’, ‘rs’]) -> ‘ab.pq.rs’

    capitalize()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.capitalize "Link to this definition")
    :   Return a capitalized version of the string.

        More specifically, make the first character have upper case and the rest lower
        case.

    casefold()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.casefold "Link to this definition")
    :   Return a version of the string suitable for caseless comparisons.

    title()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.title "Link to this definition")
    :   Return a version of the string where each word is titlecased.

        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.

    center(*width*, *fillchar=' '*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.center "Link to this definition")
    :   Return a centered string of length width.

        Padding is done using the specified fill character (default is a space).

    count()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.count "Link to this definition")
    :   Return the number of non-overlapping occurrences of substring sub in string S[start:end].

        Optional arguments start and end are interpreted as in slice notation.

    expandtabs(*tabsize=8*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.expandtabs "Link to this definition")
    :   Return a copy where all tab characters are expanded using spaces.

        If tabsize is not given, a tab size of 8 characters is assumed.

    find()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.find "Link to this definition")
    :   Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

        Optional arguments start and end are interpreted as in slice notation.
        Return -1 on failure.

    partition(*sep*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.partition "Link to this definition")
    :   Partition the string into three parts using the given separator.

        This will search for the separator in the string. If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.

    index()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.index "Link to this definition")
    :   Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

        Optional arguments start and end are interpreted as in slice notation.
        Raises ValueError when the substring is not found.

    ljust(*width*, *fillchar=' '*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.ljust "Link to this definition")
    :   Return a left-justified string of length width.

        Padding is done using the specified fill character (default is a space).

    lower()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.lower "Link to this definition")
    :   Return a copy of the string converted to lowercase.

    lstrip(*chars=None*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.lstrip "Link to this definition")
    :   Return a copy of the string with leading whitespace removed.

        If chars is given and not None, remove characters in chars instead.

    rfind()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.rfind "Link to this definition")
    :   Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

        Optional arguments start and end are interpreted as in slice notation.
        Return -1 on failure.

    rindex()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.rindex "Link to this definition")
    :   Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

        Optional arguments start and end are interpreted as in slice notation.
        Raises ValueError when the substring is not found.

    rjust(*width*, *fillchar=' '*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.rjust "Link to this definition")
    :   Return a right-justified string of length width.

        Padding is done using the specified fill character (default is a space).

    rstrip(*chars=None*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.rstrip "Link to this definition")
    :   Return a copy of the string with trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.

    rpartition(*sep*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.rpartition "Link to this definition")
    :   Partition the string into three parts using the given separator.

        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.

    splitlines(*keepends=False*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.splitlines "Link to this definition")
    :   Return a list of the lines in the string, breaking at line boundaries.

        Line breaks are not included in the resulting list unless keepends is given and
        true.

    strip(*chars=None*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.strip "Link to this definition")
    :   Return a copy of the string with leading and trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.

    swapcase()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.swapcase "Link to this definition")
    :   Convert uppercase characters to lowercase and lowercase characters to uppercase.

    translate(*table*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.translate "Link to this definition")
    :   Replace each character in the string using the given translation table.

        > table
        > :   Translation table, which must be a mapping of Unicode ordinals to
        >     Unicode ordinals, strings, or None.

        The table must implement lookup/indexing via \_\_getitem\_\_, for instance a
        dictionary or list. If this operation raises LookupError, the character is
        left untouched. Characters mapped to None are deleted.

    upper()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.upper "Link to this definition")
    :   Return a copy of the string converted to uppercase.

    startswith()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.startswith "Link to this definition")
    :   Return True if the string starts with the specified prefix, False otherwise.

        prefix
        :   A string or a tuple of strings to try.

        start
        :   Optional start position. Default: start of the string.

        end
        :   Optional stop position. Default: end of the string.

    endswith()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.endswith "Link to this definition")
    :   Return True if the string ends with the specified suffix, False otherwise.

        suffix
        :   A string or a tuple of strings to try.

        start
        :   Optional start position. Default: start of the string.

        end
        :   Optional stop position. Default: end of the string.

    removeprefix(*prefix*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.removeprefix "Link to this definition")
    :   Return a str with the given prefix string removed if present.

        If the string starts with the prefix string, return string[len(prefix):].
        Otherwise, return a copy of the original string.

    removesuffix(*suffix*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.removesuffix "Link to this definition")
    :   Return a str with the given suffix string removed if present.

        If the string ends with the suffix string and that suffix is not empty,
        return string[:-len(suffix)]. Otherwise, return a copy of the original
        string.

    isascii()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.isascii "Link to this definition")
    :   Return True if all characters in the string are ASCII, False otherwise.

        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.

    islower()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.islower "Link to this definition")
    :   Return True if the string is a lowercase string, False otherwise.

        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.

    isupper()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.isupper "Link to this definition")
    :   Return True if the string is an uppercase string, False otherwise.

        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.

    istitle()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.istitle "Link to this definition")
    :   Return True if the string is a title-cased string, False otherwise.

        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.

    isspace()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.isspace "Link to this definition")
    :   Return True if the string is a whitespace string, False otherwise.

        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.

    isdecimal()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.isdecimal "Link to this definition")
    :   Return True if the string is a decimal string, False otherwise.

        A string is a decimal string if all characters in the string are decimal and
        there is at least one character in the string.

    isdigit()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.isdigit "Link to this definition")
    :   Return True if the string is a digit string, False otherwise.

        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.

    isnumeric()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.isnumeric "Link to this definition")
    :   Return True if the string is a numeric string, False otherwise.

        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.

    isalpha()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.isalpha "Link to this definition")
    :   Return True if the string is an alphabetic string, False otherwise.

        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.

    isalnum()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.isalnum "Link to this definition")
    :   Return True if the string is an alpha-numeric string, False otherwise.

        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.

    isidentifier()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.isidentifier "Link to this definition")
    :   Return True if the string is a valid Python identifier, False otherwise.

        Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
        such as “def” or “class”.

    isprintable()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.isprintable "Link to this definition")
    :   Return True if all characters in the string are printable, False otherwise.

        A character is printable if repr() may use it in its output.

    zfill(*width*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.zfill "Link to this definition")
    :   Pad a numeric string with zeros on the left, to fill a field of the given width.

        The string is never truncated.

    format(*\*args*, *\*\*kwargs*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.format "Link to this definition")
    :   Return a formatted version of the string, using substitutions from args and kwargs.
        The substitutions are identified by braces (‘{’ and ‘}’).

    format\_map(*mapping*, */*)[](#keysight.ads.experimental_simulation.hpc.SimulationMode.format_map "Link to this definition")
    :   Return a formatted version of the string, using substitutions from mapping.
        The substitutions are identified by braces (‘{’ and ‘}’).

    *static* maketrans()[](#keysight.ads.experimental_simulation.hpc.SimulationMode.maketrans "Link to this definition")
    :   Return a translation table usable for str.translate().

        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.


---

<!-- === 来源: reference/hpc/SiteclusterResourceSettings.md === -->

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


---

<!-- === 来源: reference/index.md === -->

# Reference[](#reference "Link to this heading")

* [keysight.ads.experimental\_simulation](hpc/index.md)
  + [Classes](hpc/index.md#classes)
    - [SimulationMode](hpc/SimulationMode.md)
    - [JobStatus](hpc/JobStatus.md)
    - [ResourceSettings](hpc/ResourceSettings.md)
    - [LocalResourceSettings](hpc/LocalResourceSettings.md)
    - [SiteclusterResourceSettings](hpc/SiteclusterResourceSettings.md)
    - [Job](hpc/Job.md)
    - [JobStartupInfo](hpc/JobStartupInfo.md)
  + [Functions](hpc/index.md#functions)
    - [`submit_design_with_settings()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_design_with_settings)
    - [`submit_design()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_design)
    - [`submit_netlist()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_netlist)
    - [`get_jobs()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.get_jobs)
    - [`get_resource_settings()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.get_resource_settings)
    - [`set_resource_settings()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.set_resource_settings)
    - [`set_simulation_mode()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.set_simulation_mode)
    - [`await_all_jobs()`](hpc/index.md#keysight.ads.experimental_simulation.hpc.await_all_jobs)

**Indices**

* [Index](../genindex.md)
* [Module Index](../py-modindex.md)


---

