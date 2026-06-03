<!-- 来源: reference\hpc\SimulationMode.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Design Cloud Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.experimental\_simulation](index.md)
* SimulationMode

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/reference/hpc/SimulationMode.rst.txt)

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
    - SimulationMode
    - [JobStatus](JobStatus.md)
    - [ResourceSettings](ResourceSettings.md)
    - [LocalResourceSettings](LocalResourceSettings.md)
    - [SiteclusterResourceSettings](SiteclusterResourceSettings.md)
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

On this page

[Previous

keysight.ads.experimental\_simulation](index.md)
[Next

JobStatus](JobStatus.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top