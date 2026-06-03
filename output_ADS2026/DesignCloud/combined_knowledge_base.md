# Design Cloud Python Documentation Knowledge Base
> 本文件由 MarkItDown 自动转换，BFS 遍历自 Keysight ADS2026 Update 2.1 Design Cloud Python Documentation HTML 文档。
> 共 36 个页面。

---

## 目录 (Table of Contents)

1. [index.md](#index)
2. [intro\index.md](#intro--index)
3. [intro\usage.md](#intro--usage)
4. [intro\vscode.md](#intro--vscode)
5. [reference\index.md](#reference--index)
6. [reference\hpc\index.md](#reference--hpc--index)
7. [reference\hpc\SimulationMode.md](#reference--hpc--simulationmode)
8. [reference\hpc\JobStatus.md](#reference--hpc--jobstatus)
9. [reference\hpc\ResourceSettings.md](#reference--hpc--resourcesettings)
10. [reference\hpc\LocalResourceSettings.md](#reference--hpc--localresourcesettings)
11. [reference\hpc\SiteclusterResourceSettings.md](#reference--hpc--siteclusterresourcesettings)
12. [reference\hpc\Job.md](#reference--hpc--job)
13. [reference\hpc\JobStartupInfo.md](#reference--hpc--jobstartupinfo)
14. [howto\index.md](#howto--index)
15. [howto\venv.md](#howto--venv)
16. [howto\newvenv.md](#howto--newvenv)
17. [howto\submit_simulations.md](#howto--submit_simulations)
18. [howto\submit_sims\local_queue.md](#howto--submit_sims--local_queue)
19. [howto\submit_sims\sitecluster_queue.md](#howto--submit_sims--sitecluster_queue)
20. [howto\submit_sims\dc_server.md](#howto--submit_sims--dc_server)
21. [howto\submit_sims\submit_netlist.md](#howto--submit_sims--submit_netlist)
22. [howto\submit_sims\submit_pre.md](#howto--submit_sims--submit_pre)
23. [howto\job.md](#howto--job)
24. [howto\manage_jobs\cancel_job.md](#howto--manage_jobs--cancel_job)
25. [howto\manage_jobs\job_name.md](#howto--manage_jobs--job_name)
26. [howto\manage_jobs\job_wait.md](#howto--manage_jobs--job_wait)
27. [howto\manage_jobs\job_list.md](#howto--manage_jobs--job_list)
28. [howto\manage_jobs\all_job_wait.md](#howto--manage_jobs--all_job_wait)
29. [howto\manage_jobs\polling_status.md](#howto--manage_jobs--polling_status)
30. [howto\manage_jobs\get_dataset.md](#howto--manage_jobs--get_dataset)
31. [howto\manage_jobs\check_running_jobs.md](#howto--manage_jobs--check_running_jobs)
32. [examples\index.md](#examples--index)
33. [examples\ex_simulate_local_queue.md](#examples--ex_simulate_local_queue)
34. [examples\ex_simulate_dc_server.md](#examples--ex_simulate_dc_server)
35. [examples\ex_simulate_multiple_designs.md](#examples--ex_simulate_multiple_designs)
36. [examples\ex_run_rfpro_simulation_on_dc_server.md](#examples--ex_run_rfpro_simulation_on_dc_server)

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
  + [Simulate multiple designs of a workspace on Design Cloud](examples/ex_simulate_multiple_designs.md)
  + [Run RFPro Simulation on Design Cloud Server](examples/ex_run_rfpro_simulation_on_dc_server.md)


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

A Python script running outside ADS can access the functionality of Design Cloud.

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

## 6. reference\hpc\index.md {#reference--hpc--index}

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

## 7. reference\hpc\SimulationMode.md {#reference--hpc--simulationmode}

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

## 8. reference\hpc\JobStatus.md {#reference--hpc--jobstatus}

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

## 9. reference\hpc\ResourceSettings.md {#reference--hpc--resourcesettings}

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

## 10. reference\hpc\LocalResourceSettings.md {#reference--hpc--localresourcesettings}

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

## 11. reference\hpc\SiteclusterResourceSettings.md {#reference--hpc--siteclusterresourcesettings}

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

## 12. reference\hpc\Job.md {#reference--hpc--job}

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

## 13. reference\hpc\JobStartupInfo.md {#reference--hpc--jobstartupinfo}

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

## 14. howto\index.md {#howto--index}

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
  + [Polling the Status of a Job](manage_jobs/polling_status.md)
  + [Getting the dataset after a simulation](manage_jobs/get_dataset.md)
  + [Checking for Running Jobs](manage_jobs/check_running_jobs.md)


---

## 15. howto\venv.md {#howto--venv}

# How to Set Up a Python Virtual Environment[](#how-to-set-up-a-python-virtual-environment "Link to this heading")

It is possible to use ADS modules from a Python virtual environment rather than within the embedded ADS Python.
To do this you can create a new virtual environment based on the ADS Python executable.

* [Creating a new Python virtual environment based on ADS Python](newvenv.md)


---

## 16. howto\newvenv.md {#howto--newvenv}

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

## 17. howto\submit_simulations.md {#howto--submit_simulations}

# How to Submit Simulations on Design Cloud Hosts[](#how-to-submit-simulations-on-design-cloud-hosts "Link to this heading")

* [Submitting simulations on a Local Queue](submit_sims/local_queue.md)
* [Submitting simulations on a Site Cluster Queue](submit_sims/sitecluster_queue.md)
* [Submitting Simulations on a Design Cloud Server](submit_sims/dc_server.md)
* [Submit a Netlist to Design Cloud Server](submit_sims/submit_netlist.md)
* [Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings](submit_sims/submit_pre.md)


---

## 18. howto\submit_sims\local_queue.md {#howto--submit_sims--local_queue}

# Submitting simulations on a Local Queue[](#submitting-simulations-on-a-local-queue "Link to this heading")

If you want to run your design on your local host, you can use the [`LocalResourceSettings`](../../reference/hpc/LocalResourceSettings.md#keysight.ads.experimental_simulation.hpc.LocalResourceSettings "keysight.ads.experimental_simulation.hpc.LocalResourceSettings") class to specify the resource settings. Under this mode, you can also simulate your design parallelly on your local machine.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.LocalResourceSettings(
    parallel_jobs = 8,
    max_threads_per_job = 4,
    queue_job_locally = False,
    # Note: To submit multiple designs on Local queue and want to queue them
    # set queue_job_locally = True".
)

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```

We have provided an example for your reference on how to submit simulations on a local queue. see [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)


---

## 19. howto\submit_sims\sitecluster_queue.md {#howto--submit_sims--sitecluster_queue}

# Submitting simulations on a Site Cluster Queue[](#submitting-simulations-on-a-site-cluster-queue "Link to this heading")

If you use ADS on a machine which is also a submit host of your HPC cluster then you can directly submit your simulations to the cluster without installing the Design Cloud server.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.SiteclusterResourceSettings(
    sitecluster = "/path/to/your/sitecluster/wrapper/script", # Replace with your own sitecluster wrapper script path (.bat|.sh)
    parallel_jobs = 4,
    max_threads_per_job = 4,
    memory_value = 16,
    memory_unit = 'GB',
    queue = 'default', # Replace with your queue name
    # Additional options for Design Cloud
    # project_name='your_project_name', # Replace with your own project name if you have configured
    # uploading_filename='/path/to/your/upload_file.upl', # Replace with your own upload file path
    # email='your_email@address.com', # Replace with your own email address
    # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
)

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```


---

## 20. howto\submit_sims\dc_server.md {#howto--submit_sims--dc_server}

# Submitting Simulations on a Design Cloud Server[](#submitting-simulations-on-a-design-cloud-server "Link to this heading")

If you already have deployed a Design Cloud Server, you can specify the url of that server in the resource settings.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.ResourceSettings(
    url = "https://mydesigncloudserver.com", # Replace with your Design Cloud Server URL
    parallel_jobs = 4,
    max_threads_per_job = 4,
    memory_value = 16,
    memory_unit = 'GB',
    queue = 'default', # Replace with your queue name
    # Additional options for Design Cloud
    # project_name='your_project_name', # Replace with your own project name if you have configured
    # uploading_filename='/path/to/your/upload_file.upl', # Replace with your own upload file path
    # email='your_email@address.com', # Replace with your own email address
    # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
)

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```

We have provided an example for your reference on how to submit simulations on a Design Cloud server. see [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)


---

## 21. howto\submit_sims\submit_netlist.md {#howto--submit_sims--submit_netlist}

# Submit a Netlist to Design Cloud Server[](#submit-a-netlist-to-design-cloud-server "Link to this heading")

If you have a netlist and want to submit it to the Design Cloud Server, you can use the [`submit_netlist()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_netlist "keysight.ads.experimental_simulation.hpc.submit_netlist") function.

```
from keysight.ads.experimental_simulation import hpc

resource_settings.url = 'https://mydesigncloudserver.com' # Replace with your Design Cloud server URL
resource_settings = hpc.ResourceSettings(
    url = "https://mydesigncloudserver.com", # Replace with your Design Cloud server URL
    parallel_jobs = 4,
    max_threads_per_job = 4,
    memory_value = 16,
    memory_unit = 'GB',
    queue = 'default', # Replace with your queue name
    # Additional options for Design Cloud
    # project_name='your_project_name', # Replace with your own project name if you have configured
    # uploading_filename='/path/to/your/upload_file.upl', # Replace with your own upload file path
    # email='your_email@address.com', # Replace with your own email address
    # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
)

jobname = "mynetlist_job"
netlist_path = "path/to/your/netlist.net"

job = hpc.submit_netlist(jobname, netlist_path, resource_settings)  # Where netlist is the path to your netlist file

# You can also check the status of the job
job_status = job.get_status()
print(job_status.value)
```


---

## 22. howto\submit_sims\submit_pre.md {#howto--submit_sims--submit_pre}

# Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings[](#submitting-simulations-on-a-design-cloud-server-with-pre-defined-resource-settings "Link to this heading")

If the design context is already set up with the resource settings, you can directly submit the design to the Design Cloud Server using you can use the [`submit_design()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_design "keysight.ads.experimental_simulation.hpc.submit_design") function.

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

## 23. howto\job.md {#howto--job}

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
* [Polling the Status of a Job](manage_jobs/polling_status.md)
* [Getting the dataset after a simulation](manage_jobs/get_dataset.md)
* [Checking for Running Jobs](manage_jobs/check_running_jobs.md)


---

## 24. howto\manage_jobs\cancel_job.md {#howto--manage_jobs--cancel_job}

# Cancel a Job[](#cancel-a-job "Link to this heading")

To cancel a job, you can use the [`cancel()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.cancel "keysight.ads.experimental_simulation.hpc.Job.cancel") function. We assume that you already have a design to submit with the resource settings.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.ResourceSettings(
    url = "https://mydesigncloudserver.com", # Replace with your Design Cloud Server URL
    parallel_jobs = 4,
    max_threads_per_job = 4,
)
job = hpc.submit_design_with_settings(design, resource_settings)

# Cancel a running job
if job.is_running():
    job.cancel()

# Cancel a pending job
job_status = job.get_status()
if job_status == hpc.JobStatus.PENDING:
    job.cancel()
```


---

## 25. howto\manage_jobs\job_name.md {#howto--manage_jobs--job_name}

# Get the name of a job[](#get-the-name-of-a-job "Link to this heading")

To get the name of a job, you can use the [`get_name()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.get_name "keysight.ads.experimental_simulation.hpc.Job.get_name") function.

```
from keysight.ads.experimental_simulation import hpc
job = hpc.submit_design_with_settings(design, resource_settings)

job_name = job.get_name()
print(job_name)
```


---

## 26. howto\manage_jobs\job_wait.md {#howto--manage_jobs--job_wait}

# Wait for a Job to Complete[](#wait-for-a-job-to-complete "Link to this heading")

To wait for a job to complete, you can use the [`await_job()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.await_job "keysight.ads.experimental_simulation.hpc.Job.await_job") function. This function takes an argument timeout which is the maximum time to wait for the job to complete.

```
from keysight.ads.experimental_simulation import hpc
job = hpc.submit_design_with_settings(design, resource_settings)

job.await_job(timeout=60)  # Wait for 60 seconds

# If the job is completed, the function will return True
# If the job is not completed within the timeout, the function will return False

# You can also check the status of the job
job_status = job.get_status()
print(job_status.value)
```

Note that [`await_job()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.await_job "keysight.ads.experimental_simulation.hpc.Job.await_job") will block until the job is completed or the timeout is reached. If you want to cancel the await early, you must cancel the job.

For example, you can cancel a job on a Ctrl-C by adding a signal handler for SIGINT.

```
# cancel a job on a Ctrl-C
signal.signal(signal.SIGINT, lambda signal, frame: job.cancel())
```

Note : you could also leave a job running after a Control-C by calling QCoreApplication.quit() in the signal handler.
If you do this you may have to check if the job is running in any scripts you run later, see [Checking for Running Jobs](check_running_jobs.md) for more information.


---

## 27. howto\manage_jobs\job_list.md {#howto--manage_jobs--job_list}

# Get the List of Submitted Jobs[](#get-the-list-of-submitted-jobs "Link to this heading")

To get the list of submitted jobs, you can use the [`get_jobs()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.get_jobs "keysight.ads.experimental_simulation.hpc.get_jobs") function. This function returns a list of all the jobs submitted by the user.

```
from keysight.ads.experimental_simulation import hpc
jobs = hpc.get_jobs()
print(jobs)
```


---

## 28. howto\manage_jobs\all_job_wait.md {#howto--manage_jobs--all_job_wait}

# Wait for All Jobs to Complete[](#wait-for-all-jobs-to-complete "Link to this heading")

To wait for all jobs to complete, you can use the [`await_all_jobs()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.await_all_jobs "keysight.ads.experimental_simulation.hpc.await_all_jobs") function. This function takes an argument timeout which is the maximum time to wait for all jobs to complete.

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
    print(job_status.value)
```

Note that [`await_all_jobs()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.await_all_jobs "keysight.ads.experimental_simulation.hpc.await_all_jobs") will block until all jobs are completed or the timeout is reached. If you want to cancel the await early, you must cancel all the running jobs.

For example, you can cancel all jobs on a Ctrl-C by adding a signal handler for SIGINT.

```
# cancel all jobs on a Ctrl-C
signal.signal(signal.SIGINT, lambda signal, frame: [job.cancel() for job in hpc.get_jobs()])
```

Note : you could also leave jobs running after a Control-C by calling QCoreApplication.quit() in the signal handler.
If you do this you may have to check if the job is running in any scripts you run later, see [Checking for Running Jobs](check_running_jobs.md) for more information.


---

## 29. howto\manage_jobs\polling_status.md {#howto--manage_jobs--polling_status}

# Polling the Status of a Job[](#polling-the-status-of-a-job "Link to this heading")

To poll the status of a running job you can use a QT Timer and query [`get_status()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.get_status "keysight.ads.experimental_simulation.hpc.Job.get_status") and/or [`get_subjob_status()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.get_subjob_status "keysight.ads.experimental_simulation.hpc.Job.get_subjob_status").

```
from keysight.ads.experimental_simulation import hpc
job = hpc.submit_design_with_settings(design, resource_settings)

# create a QTimer that will poll the job status, and subjob statuses every second
timer = QTimer()
timer.timeout.connect(
    lambda: print(f"Job status: {job.get_status()} : {job.get_subjob_status()}")
)
timer.start(1000)

job.await_job()  # wait for the job to finish
```


---

## 30. howto\manage_jobs\get_dataset.md {#howto--manage_jobs--get_dataset}

# Getting the dataset after a simulation[](#getting-the-dataset-after-a-simulation "Link to this heading")

When a simulation is finished you can find and read the dataset using the information held in [`JobStartupInfo`](../../reference/hpc/JobStartupInfo.md#keysight.ads.experimental_simulation.hpc.JobStartupInfo "keysight.ads.experimental_simulation.hpc.JobStartupInfo").

```
from keysight.ads.experimental_simulation import hpc
import keysight.ads.dataset as dataset
from pathlib import Path

job = hpc.submit_design_with_settings(design, settings)
job_startup_info = job.get_startup_info()

# wait for the job to complete
hpc.await_all_jobs(600)

# use the workspace dir and dataset name to get the file name of the dataset
dataset_file_name = Path(job_startup_info.workspace_dir) / "data" / (job_startup_info.dataset_name + ".ds")

# open it and print the contents
data = dataset.open(dataset_file_name)
for (name, vb) in data.items():
    print(f"VariableBlock DataFrame: {name}\n{vb.to_dataframe()}")
```


---

## 31. howto\manage_jobs\check_running_jobs.md {#howto--manage_jobs--check_running_jobs}

# Checking for Running Jobs[](#checking-for-running-jobs "Link to this heading")

While writing automation scripts you may often be able to assume that it’s okay to submit a new job, but if someone has started a job manually, or if a script started a job and left it running, it’s possible that you won’t be able submit a job because an old instance with the same name is already running.

To account for this you can check for running jobs using [`get_jobs()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.get_jobs "keysight.ads.experimental_simulation.hpc.get_jobs") and wait for them to finish if necessary.

For example:

```
running_jobs = [job for job in hpc.get_jobs() if job.is_running()]
if running_jobs:
    job_names = [job.get_name() for job in running_jobs]
    print(f"These jobs are running : {job_names}, waiting for them to complete")
    hpc.await_all_jobs()

# Now you can submit a new job
```


---

## 32. examples\index.md {#examples--index}

# Examples[](#examples "Link to this heading")

Contents:

* [Create and Simulate a Circuit on Design Cloud Local Queue](ex_simulate_local_queue.md)
* [Simulate a Circuit on Design Cloud Server](ex_simulate_dc_server.md)
* [Simulate multiple designs of a workspace on Design Cloud](ex_simulate_multiple_designs.md)
* [Run RFPro Simulation on Design Cloud Server](ex_run_rfpro_simulation_on_dc_server.md)


---

## 33. examples\ex_simulate_local_queue.md {#examples--ex_simulate_local_queue}

# Create and Simulate a Circuit on Design Cloud Local Queue[](#create-and-simulate-a-circuit-on-design-cloud-local-queue "Link to this heading")

This example will create a new workspace in your current working directory called design\_cloud\_demo\_wrk. In the workspace, a new library and schematic is created and populated with an RC filter. Next, the circuit is be subitted to the Design Cloud Local Queue for simulation.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example demonstrates how to run a simulation on Design Cloud Local Queue
using Python APIs provided by Keysight Advanced Design System (ADS).
"""

import os
import shutil
from pathlib import Path
import sys
from keysight.ads import de
from keysight.ads.de import db_uu as db
from keysight.ads.experimental_simulation import hpc

def create_workspace_and_design_then_simulate_on_design_cloud(
    workspace_name: str, library_name: str, cell_name: str
) -> int:
    """
    Create a new workspace, design and simulate it on Design Cloud
    """

    def create_and_open_workspace(workspace_name) -> de.Workspace:
        """
        Creates a workspace and opens it
        """
        workspace_path = Path(workspace_name)
        if workspace_path.exists():
            print(f"Removing existing workspace: {workspace_path}")
            shutil.rmtree(workspace_path)

        # Create the workspace
        print(f"Creating workspace: {workspace_path}")
        workspace = de.create_workspace(workspace_path)
        workspace.open()
        return workspace

    def create_library_and_design(workspace: de.Workspace, library_name: str, cell_name: str) -> db.Design:
        """
        Creates a new library and design inside the workspace
        """
        library_path = os.path.join(workspace.path, library_name)
        print(f"Creating library: {library_path}")
        de.create_new_library(library_name, library_path)
        workspace.add_library(library_name, library_path, de.LibraryMode.NON_SHARED)

        print(f"Creating design: {library_name}:{cell_name}:schematic")
        # Create a new schematic
        design = db.create_schematic(f"{library_name}:{cell_name}:schematic")
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
        return design

    def submit_design_on_design_cloud_local_queue(design: db.Design) -> hpc.Job:
        """
        Submit the design on Design Cloud Local Queue
        """
        # Setting resources for the simulation
        resource_settings = hpc.LocalResourceSettings(parallel_jobs=1, max_threads_per_job=1, queue_job_locally=False)

        # If you want to queue multiple designs on "Local queue",
        # then, set the queue_job_locally = True

        # Submit the test bench with the settings to the Design Cloud Local queue
        print("Submitting design to Design Cloud Local Queue")
        job = hpc.submit_design_with_settings(design, resource_settings)
        return job

    def check_job_status(job: hpc.Job):
        """
        Check job status
        """
        # Wait for the job to complete
        job.await_job(600)

        # Check the job status
        job_status = job.get_status()
        print(f"Job status: {job_status.value}")

        # Print job output
        print(f"Job {job.get_name()} output:")
        print(job.get_output())
        print("\n".join([f"Subjob {i} output:\n {output}" for i, output in enumerate(job.get_subjob_output())]))

        if job_status == hpc.JobStatus.COMPLETED:
            print("Job completed successfully")
        elif job_status == hpc.JobStatus.ERROR:
            print("Job failed")
        elif job_status == hpc.JobStatus.RUNNING:
            print("Job is still running")
        else:
            print(f"Job status is: {job_status.value}")

    # Execution
    workspace = create_and_open_workspace(workspace_name)
    design = create_library_and_design(workspace, library_name, cell_name)
    try:
        job = submit_design_on_design_cloud_local_queue(design)
        check_job_status(job)
    except RuntimeError as error:
        print(f"An error occurred while submitting design to local queue: {error}")
        return 1
    except Exception as error:
        print(f"Unexpected  error: {error}")
        return 2
    finally:
        # Close the workspace
        print(f"Closing workspace: {workspace_name}")
        workspace.close()
    return 0

if __name__ == "__main__":
    WORKSPACE_NAME = "design_cloud_demo_wrk"
    LIBRARY_NAME = "design_cloud_demo_lib"
    CELL_NAME = "design_cloud_local_queue"
    EXIT_CODE = create_workspace_and_design_then_simulate_on_design_cloud(WORKSPACE_NAME, LIBRARY_NAME, CELL_NAME)
    sys.exit(EXIT_CODE)
```


---

## 34. examples\ex_simulate_dc_server.md {#examples--ex_simulate_dc_server}

# Simulate a Circuit on Design Cloud Server[](#simulate-a-circuit-on-design-cloud-server "Link to this heading")

This example will unarchive an ADS example BatchSim\_Example1\_wrk in your current working directory and run Batch\_CSVSweep test bench on the Design Cloud server.

Note

A dummy Design Cloud server is shown in the example. Please replace it with your own Design Cloud server.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example uses existing ADS example "BatchSim_Example1_wrk:Batch_CSVSweep" to demonstrate how to
run a simulation on Design Cloud using Python APIs provided by Keysight Advanced Design System (ADS).
"""

import argparse
import os
import shutil
from pathlib import Path
import sys
from keysight.ads import de
from keysight.ads.de import db_uu as db
from keysight.ads.experimental_simulation import hpc

def run_design_on_design_cloud(
    example_dir: str, workspace_name: str, library_name: str, cell_name: str, settings: hpc.ResourceSettings, timeout=0
) -> int:
    """
    Unarchives a workspace, opens the design specified
    and submits the design on the Design Cloud
    """

    def unarchive_example_workspace(example_dir: str, workspace_name: str) -> Path:
        """
        Unarchive example workspace
        """
        workspace_dir = Path(workspace_name)
        if workspace_dir.exists():
            print(f"Removing existing workspace: {workspace_dir}")
            shutil.rmtree(workspace_dir)

        archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
        print(f"Unarchiving Workspace: {archive_file} in current working directory: {os.getcwd()}")
        de.unarchive_file(archive_file, ".")
        return workspace_dir

    def check_job_status(job: hpc.Job, timeout=0) -> None:
        """
        Check the job status
        """
        job.await_job(timeout=timeout)

        # Check the job status
        job_status = job.get_status()
        print(f"Job status: {job_status.value}")

        # Print job output
        print(f"Job {job.get_name()} output:")
        print(job.get_output())

        # Subjob Status
        subjob_statuses = job.get_subjob_status()
        completed = 0
        failed = 0
        pending = 0
        running = 0

        for subjob_status in subjob_statuses:
            if subjob_status == hpc.JobStatus.COMPLETED:
                completed += 1
            elif subjob_status == hpc.JobStatus.ERROR:
                failed += 1
            elif subjob_status == hpc.JobStatus.PENDING:
                pending += 1
            elif subjob_status == hpc.JobStatus.RUNNING:
                running += 1

        print(f"Subjob status: {completed} completed, {failed} failed, {pending} pending, {running} running")
        print("\n".join([f"Subjob {i} output:\n {output}" for i, output in enumerate(job.get_subjob_output())]))

        if job_status == hpc.JobStatus.COMPLETED:
            print("Job completed successfully")
        elif job_status == hpc.JobStatus.ERROR:
            print("Job failed")
            raise RuntimeError("Job failed")
        elif job_status == hpc.JobStatus.RUNNING:
            print("Job is still running")
        else:
            print(f"Job status is: {job_status.value}")

    # Execution
    workspace_dir = unarchive_example_workspace(example_dir, workspace_name)
    workspace = de.open_workspace(workspace_dir)
    design = db.open_design(f"{library_name}:{cell_name}:schematic", db.DesignMode.APPEND)
    try:
        job = hpc.submit_design_with_settings(design, settings)
        if job:
            check_job_status(job, timeout)
        else:
            print("Failed to submit the design to Design Cloud")
            return 1
    except RuntimeError as error:
        print(f"An error occurred while submitting design to Design Cloud: {error}")
        return 1
    except Exception as error:
        print(f"Unexpected  error: {error}")
        return 2
    finally:
        # Close the workspace
        print(f"Closing workspace: {workspace_dir}")
        workspace.close()
    return 0

if __name__ == "__main__":
    EXAMPLE_DIR = "examples/RF_Microwave"
    WORKSPACE_NAME = "BatchSim_Example1_wrk"
    LIBRARY_NAME = "BatchSim_Example1_lib"
    CELL_NAME = "Batch_CSVSweep"

    # Parse command line arguments
    # Example usage: python ex_simulate_on_design_cloud_server.py http://your-design-cloud-url
    parser = argparse.ArgumentParser(description="Run simulation on Design Cloud")
    parser.add_argument("url", help="Design Cloud server URL")
    args = parser.parse_args()
    RESOURCE_SETTINGS = hpc.ResourceSettings(
        url=args.url,
        parallel_jobs=4,
        max_threads_per_job=4,
        memory_value=12,
        memory_unit="GB",
        queue="default",  #  Replace with your own queue name
        # Additional options for Design Cloud
        # project_name='your_project_name', # Replace with your own project name if you have configured
        # uploading_filename='/path/to/your/upload_file.upl', # Replace with your own upload file path
        # email='your_email@address.com', # Replace with your own email address
        # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
    )
    TIMEOUT = 10 * 60  # 10 minutes

    EXIT_CODE = run_design_on_design_cloud(
        EXAMPLE_DIR, WORKSPACE_NAME, LIBRARY_NAME, CELL_NAME, RESOURCE_SETTINGS, TIMEOUT
    )
    sys.exit(EXIT_CODE)
```


---

## 35. examples\ex_simulate_multiple_designs.md {#examples--ex_simulate_multiple_designs}

# Simulate multiple designs of a workspace on Design Cloud[](#simulate-multiple-designs-of-a-workspace-on-design-cloud "Link to this heading")

This example will unarchive an ADS example BatchSim\_Example1\_wrk in your current working directory and run multiple designs on the Design Cloud server.

Note

A dummy Design Cloud server is shown in the example. Please replace it with your own Design Cloud server.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example uses existing ADS example "BatchSim_Example1_wrk" to demonstrate how to run multiple designs
of same workspace on Design Cloud using Python APIs provided by Keysight Advanced Design System (ADS).
"""

import argparse
import os
import shutil
from pathlib import Path
import sys
from keysight.ads import de
from keysight.ads.de import db_uu as db
from keysight.ads.experimental_simulation import hpc

def run_multiple_designs_on_design_cloud(example_dir: str, workspace_name: str, design_config: dict, timeout=0) -> int:
    """
    Unarchives a workspace, opens each design specified in the design config and
    submits the design on the Design Cloud
    """

    def unarchive_example_workspace(example_dir: str, workspace_name: str) -> Path:
        """
        Unarchive example workspace
        """
        workspace_dir = Path(workspace_name)
        if workspace_dir.exists():
            print(f"Removing existing workspace: {workspace_dir}")
            shutil.rmtree(workspace_dir)

        archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
        print(f"Unarchiving Workspace: {archive_file} in current working directory: {os.getcwd()}")
        de.unarchive_file(archive_file, ".")
        return workspace_dir

    def submit_designs_on_design_cloud(design_config: dict) -> None:
        """
        Opens each design and submit to Design Cloud
        """

        if not design_config:
            raise ValueError("Design Configuration cannot be empty")

        for design_name, resource_settings in design_config.items():
            print(f"Opening design: {design_name}")
            design = db.open_design(design_name, db.DesignMode.APPEND)
            job = hpc.submit_design_with_settings(design, resource_settings)
            # You can also check the job startup information
            job_startup_info = job.get_startup_info()
            info_dict = {
                "job name": job.get_name(),
                "workspace dir": job_startup_info.workspace_dir,
                "job dir": job_startup_info.job_dir,
                "start time": job_startup_info.start_time,
                "host url": job_startup_info.url,
                "queue": job_startup_info.queue,
                "dataset name": job_startup_info.dataset_name,
                "data display name": job_startup_info.datadisplay_name,
                "top level design": job_startup_info.top_level_design,
            }
            for key, value in info_dict.items():
                print(f"{key}: {value}")
            print("-----------------------------------------------------------")

    def monitor_all_submitted_jobs(timeout=0):
        """
        Monitor all submitted jobs on Design Cloud
        """

        # Check running status of all jobs

        running_jobs = [job for job in hpc.get_jobs() if job.is_running()]

        # Optional: You can give a timeout to wait for the jobs to complete
        if running_jobs:
            job_names = [job.get_name() for job in running_jobs]
            print(f"The following jobs are running: {job_names}")
            if timeout:
                print(f"Waiting for jobs to complete within {timeout} seconds...")
            hpc.await_all_jobs(timeout=timeout)
        # Check job status
        failed = False
        for job in hpc.get_jobs():
            job_status = job.get_status()
            print(f"Job {job.get_name()} status: {job_status}")
            if job_status != hpc.JobStatus.COMPLETED:
                failed = True

            # Check if job is still not completed, cancel it
            if job.is_running():
                print(f"Job {job.get_name()} is still in {job.get_status()} mode...")
                print(f"Canceling job {job.get_name()}...")
                job.cancel()

            # Print job output
            print(f"Job {job.get_name()} output:")
            print(job.get_output())
            print("\n".join([f"Subjob {i} output:\n {output}" for i, output in enumerate(job.get_subjob_output())]))
            print("-----------------------------------------------------------")

        if failed:
            raise RuntimeError("One or more jobs failed. Please check the job status and output.")

    # Execution
    workspace_dir = unarchive_example_workspace(example_dir, workspace_name)
    workspace = de.open_workspace(workspace_dir)
    try:
        submit_designs_on_design_cloud(design_config)
        monitor_all_submitted_jobs(timeout)
    except RuntimeError as error:
        print(f"An Error occurred during design cloud simulation: {error}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 2
    finally:
        # Close the workspace
        print(f"Closing workspace: {workspace_dir}")
        workspace.close()
    return 0

if __name__ == "__main__":
    # Parse command line arguments
    # Example usage: python ex_simulate_multiple_designs.py http://your-design-cloud-url
    parser = argparse.ArgumentParser(description="Run simulation on Design Cloud")
    parser.add_argument("url", help="Design Cloud server URL")
    parser.add_argument("sitecluster", help="path to sitecluster executable")
    args = parser.parse_args()

    EXAMPLE_DIR = "examples/RF_Microwave"
    WORKSPACE_NAME = "BatchSim_Example1_wrk"
    DESIGN_CONFIG = {
        "BatchSim_Example1_lib:Batch_SweepPlan:schematic": hpc.ResourceSettings(
            url=args.url,
            parallel_jobs=4,
            max_threads_per_job=4,
            memory_value=30,
            memory_unit="GB",
            queue="default",  # Replace with your queue name
            # Additional options for Design Cloud
            # project_name='your_project_name', # Replace with your own project name if you have configured
            # uploading_filename='/path/to/your/upload_file.upl', # Replace with your own upload file path
            # email='your_email@address.com', # Replace with your own email address
            # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
        ),
        "BatchSim_Example1_lib:Batch_CSVList:schematic": hpc.LocalResourceSettings(
            parallel_jobs=3,
            max_threads_per_job=1,  # In UI, this is equivalent to setting threads = 1
            queue_job_locally=True,  # Setting true means you can queue the multiple jobs on Local queue
        ),
        "BatchSim_Example1_lib:Batch_DataFileSweep:schematic": hpc.LocalResourceSettings(
            parallel_jobs=4,
            max_threads_per_job=3,
            queue_job_locally=True,  # This design will be queued and will run after the Batch_CSVList
        ),
        "BatchSim_Example1_lib:Batch_CSVSweep:schematic": hpc.SiteclusterResourceSettings(
            sitecluster=args.sitecluster,
            parallel_jobs=4,
            max_threads_per_job=4,
            memory_value=30,
            memory_unit="GB",
            queue="default",  # Replace with your queue name
            # Additional options for Design Cloud
            # project_name='your_project_name', # Replace with your own project name if you have configured
            # email='your_email@address.com', # Replace with your own email address
            # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
        ),
    }
    TIMEOUT = 10 * 60  # 10 min

    EXIT_CODE = run_multiple_designs_on_design_cloud(EXAMPLE_DIR, WORKSPACE_NAME, DESIGN_CONFIG, TIMEOUT)
    sys.exit(EXIT_CODE)
```


---

## 36. examples\ex_run_rfpro_simulation_on_dc_server.md {#examples--ex_run_rfpro_simulation_on_dc_server}

# Run RFPro Simulation on Design Cloud Server[](#run-rfpro-simulation-on-design-cloud-server "Link to this heading")

This example will unarchive an ADS example RFPro\_2Stage\_RF\_Board\_Amp\_wrk in your current working directory and run Full EM Analysis test on the Design Cloud server.

Note

This example will only work in command line mode as `keysight.edatoolbox.multi_python` is not supported on `IPython`. A dummy Design Cloud server is shown in the example. Please replace it with your own Design Cloud server.

```
# Copyright 2025 Keysight Technologies, Inc , Keysight Confidential

"""
This example uses existing ADS example "RFPro_2Stage_RF_Board_Amp_wrk" to demonstrate how to
run RFPro simulation on Design Cloud using Python APIs provided by Keysight Advanced Design System (ADS).
"""

import argparse
import sys

def ads_find_rfpro_view_in_workspace(
    example_dir: str,
    workspace_name: str,
    library_name: str,
    cell_name: str,
    rfpro_view_name: str,
) -> None:
    """
    Find the RFPro view for the given workspace, library and cell.
    """

    import os
    import shutil
    from pathlib import Path
    import keysight.ads.de as de

    workspace_dir = Path(workspace_name)
    if workspace_dir.exists():
        print(f"Removing existing workspace: {workspace_dir}")
        shutil.rmtree(workspace_dir)

    archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
    print(f"Unarchiving Workspace: {archive_file} in current working directory: {os.getcwd()}")
    de.unarchive_file(archive_file, ".")
    print(f"Opening workspace: {workspace_dir}")
    workspace = de.open_workspace(workspace_name)
    library = de.Library.get(library_name)
    cell = library.cell(cell_name)

    if not cell.view_exists(rfpro_view_name):
        raise RuntimeError(f"The rfpro view {rfpro_view_name} does not exist.")
    workspace.close()

def rfpro_run_analysis_on_design_cloud(
    workspace_name: str,
    library_name: str,
    cell_name: str,
    substrate_name: str,
    rfpro_view: str,
    rfpro_analysis_name: str,
    resource_settings: dict,
    timeout=0,
) -> int:
    """
    Run the RFPro analysis on the design cloud server.
    """
    import os
    import empro
    from empro.toolkit import simulation
    import empro.toolkit.analysis as rfpro

    print(f"Loading the rfpro view: {rfpro_view}")
    rfpro.loadDesign(
        path=os.path.join(os.getcwd(), workspace_name),
        lib=library_name,
        subst=substrate_name,
        cell=cell_name,
        layout_view="layout",
        sipi_view=rfpro_view,
    )

    setup = None
    analyses = empro.activeProject.analyses
    for analysis in analyses:
        if analysis.name == rfpro_analysis_name:
            setup = analysis
            break
    if not setup:
        raise RuntimeError(f"The rfpro analysis {rfpro_analysis_name} does not exist.")

    options = setup.simulationSettings
    resourceSettings = empro.simulation.RemoteResourceSettings()
    resourceSettings.numberOfWorkers = resource_settings.get("parallel_jobs", 1)
    resourceSettings.numberOfThreads = resource_settings.get("threads_per_job", 0)
    resourceSettings.options = resource_settings.get("options", "")
    resourceSettings.alphaOptions = resource_settings.get("alpha_options", "")
    resourceSettings.betaOptions = resource_settings.get("beta_options", "")
    resourceSettings.omegaOptions = resource_settings.get("omega_options", "")
    resourceSettings.host = resource_settings.get("host", None)
    resourceSettings.queue = resource_settings.get("queue", "")
    resourceSettings.memory = resource_settings.get("memory", "")
    options.resourceSettings = resourceSettings
    print(f"Running the rfpro analysis: {rfpro_analysis_name}..")
    try:
        rfpro.runAnalysis(setup, waitForConfirmation=False, saveProject=True)
        if timeout:
            print(f"waiting for {timeout} secs...")
        simulation.wait(rfpro.getSimulation(setup), timeout)
        print("Simulation completed.")
        sim = rfpro.getSimulation(setup)
        print(f"Simulation Status: {sim.status}")
        if sim.status == "Completed":
            return 0
        else:
            return 3
    except simulation.TimeOutError as error:
        print(f"Simulation timed out: {error}")
        return 1
    except RuntimeError as error:
        print(f"Runtime error occurred: {error}")
        return 2
    finally:
        print(f"simulation path = {setup.simulationPath}")
        print("Done\n")

if __name__ == "__main__":
    EXAMPLE_DIR = "examples/EM/RFPro"
    WORKSPACE_NAME = "RFPro_2Stage_RF_Board_Amp_wrk"
    LIBRARY_NAME = "RF_Board_lib"
    CELL_NAME = "Two_Stage_Amp"
    SUBSTRATE_NAME = "tech.subst"
    RFPRO_VIEW_NAME = "rfpro"
    RFPRO_ANALYSIS_NAME = "Full EM Analysis"
    TIMEOUT = 20 * 60  # 20 minutes

    # Parse command line arguments
    # Example usage: python ex_simulate_on_design_cloud_server.py http://your-design-cloud-url
    parser = argparse.ArgumentParser(description="Run simulation on Design Cloud")
    parser.add_argument("url", help="Design Cloud server URL")
    args = parser.parse_args()

    RESOURCE_SETTINGS = {
        "parallel_jobs": 1,
        "threads_per_job": 4,
        "options": "",
        "alpha_options": "",
        "beta_options": "",
        "omega_options": "",
        "host": args.url,
        "queue": "normal",  # Replace with your queue name
        "memory": "20 GiB",
    }

    import keysight.edatoolbox.multi_python as multi_python

    with multi_python.ads_context() as ads_ctx:
        ads_ctx.call(
            ads_find_rfpro_view_in_workspace,
            args=[
                EXAMPLE_DIR,
                WORKSPACE_NAME,
                LIBRARY_NAME,
                CELL_NAME,
                RFPRO_VIEW_NAME,
            ],
        )

    return_code = 3
    with multi_python.xxpro_context() as empro_ctx:
        return_code = empro_ctx.call(
            rfpro_run_analysis_on_design_cloud,
            args=[
                WORKSPACE_NAME,
                LIBRARY_NAME,
                CELL_NAME,
                SUBSTRATE_NAME,
                RFPRO_VIEW_NAME,
                RFPRO_ANALYSIS_NAME,
                RESOURCE_SETTINGS,
                TIMEOUT,
            ],
        )
    sys.exit(return_code)
```
