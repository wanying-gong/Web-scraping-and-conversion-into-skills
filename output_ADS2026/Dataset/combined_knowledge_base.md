# ADS Dataset Documentation Knowledge Base
> 本文件由 MarkItDown 自动转换，BFS 遍历自 Keysight ADS2026 Update 2.1 ADS Dataset Documentation HTML 文档。
> 共 10 个页面。

---

## 目录 (Table of Contents)

1. [index.md](#index)
2. [concepts.md](#concepts)
3. [apidoc.md](#apidoc)
4. [examples\index.md](#examples--index)
5. [examples\ex_merge_dataframes.md](#examples--ex_merge_dataframes)
6. [examples\ex_merge_irregular_dataframes.md](#examples--ex_merge_irregular_dataframes)
7. [examples\ex_merge_datasets.md](#examples--ex_merge_datasets)
8. [examples\ex_create_dataset_from_dataframe.md](#examples--ex_create_dataset_from_dataframe)
9. [history.md](#history)
10. [dependencies.md](#dependencies)

---



---

## 1. index.md {#index}

# ADS Dataset[](#ads-dataset "Link to this heading")

This package provides a Python API to work with [ADS datasets](concepts.md#concepts-dataset).

## Features[](#features "Link to this heading")

* Read the variable blocks in a dataset.
* Read the structure of a variable block.
* Extract the data of a variable block as a pandas DataFrame.
* Create a new variable block from a DataFrame.

## Contents[](#contents "Link to this heading")

* [Concepts](concepts.md)
* [API Documentation](apidoc.md)
* [Examples](examples/index.md)
* [History](history.md)
* [Dependencies](dependencies.md)

## Indices and tables[](#indices-and-tables "Link to this heading")

* [Index](genindex.md)
* [Module Index](py-modindex.md)
* [Search Page](search.md)


---

## 2. concepts.md {#concepts}

# Concepts[](#concepts "Link to this heading")

## Dataset[](#dataset "Link to this heading")

A **Dataset** contains a list of **VariableBlock**s, which are accessed by their
name. See [Dataset.varblocks](apidoc.md#keysight.ads.dataset.Dataset.varblocks "keysight.ads.dataset.Dataset.varblocks").

## VariableBlock[](#variableblock "Link to this heading")

A **VariableBlock** contains an ordered list of independent variables (`ivars`),
and an ordered list of dependent variables (`dvars`), which are each of type
**Variable**. These lists use a 0-based index.

A VariableBlock has a name. This name is typically formatted as a dotted string,
like `"Optim1.SP1.SP"`, describing the hierarchy of the origin of the data.
There is no hierarchy in the dataset corresponding to the dotted parts of the name.

A VariableBlock has a list of attributes. It’s more common to see attributes on
a **Variable** within a block, than on the block itself.

See [Variable Data](#concepts-variable-data) for more information on getting the data for a
VariableBlock.

## Variable[](#variable "Link to this heading")

A **Variable** contains a series of numeric data. In some cases it can contain a
series of string data, though these cases are rare. Typically a Variable contains
numeric data.

A Variable has a name, which is formatted as a dotted string. The dots typically
represent hierarchy in the simulator’s inputs, or in the simulator’s implementation.
There is no hierarchy in the dataset corresponding to the dotted parts of the name.

Multidimensional data (like S-parameters) is separated into multiple Variables,
with 1-based indices in square brackets.

Example

For example, 2-port S-parameter data produced by the ADS circuit simulator has
these variables:

| Independents | Dependents |
| --- | --- |
| * `freq` | * `S[1,1]` * `S[1,2]` * `S[2,2]` * `S[2,2]` * `PortZ[1]` * `PortZ[2]` |

The S-parameter results, which are a 2x2x*N* array of complex numbers for *N*
frequency points, are represented as 4 Variables, each of size *N*. Similarly,
the reference impedance, which is a 2x*N* array, is represented as 2 Variables.

A Variable has an element type. All data for that Variable is of the same element
type. The types are:

* `float`
* `complex`
* `int`
* `bool`
* `str`
* `None`

A Variable has a list of attributes. Each attribute has a name and a value, and
both are strings. A commonly used attribute is named `"flags"`, which is
accessible through the [Variable.flags](apidoc.md#keysight.ads.dataset.Variable.flags "keysight.ads.dataset.Variable.flags") and
[Variable.variable\_type](apidoc.md#keysight.ads.dataset.Variable.variable_type "keysight.ads.dataset.Variable.variable_type") properties.

## Variable Data[](#variable-data "Link to this heading")

Each **Variable** has a series of data. However, each variable’s series is not
stored separately; instead the **VariableBlock** contains data for all of its
variables.

In concept, a VariableBlock is analogous to a
[pandas DataFrame](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe).
Each Variable is analogous to a series in the dataframe, analogous to one column
in a table.

Use [VariableBlock.to\_dataframe](apidoc.md#keysight.ads.dataset.VariableBlock.to_dataframe "keysight.ads.dataset.VariableBlock.to_dataframe") to extract the data
as a dataframe.

## Attributes[](#attributes "Link to this heading")

Attributes are a list of key/value pairs. The key and value are both strings.

Several different object types can hold attributes. Currently the only one
accessible from Python is [Variable.attrs](apidoc.md#keysight.ads.dataset.Variable.attrs "keysight.ads.dataset.Variable.attrs").


---

## 3. apidoc.md {#apidoc}

# API Documentation[](#api-documentation "Link to this heading")

## open[](#open "Link to this heading")

keysight.ads.dataset.open(*path: [PathLike](https://docs.python.org/3/library/os.md#os.PathLike "(in Python v3.14)")*, *mode: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'r'*) → [Dataset](#keysight.ads.dataset.Dataset "keysight.ads.dataset.Dataset")[](#keysight.ads.dataset.open "Link to this definition")
:   Open or create a dataset.

    Interpretation of the `mode` flag:

    | `mode` | if `path` exists | if `path` does not exist |
    | --- | --- | --- |
    | `"r"` | [`open_dataset_for_reading()`](#keysight.ads.dataset.open_dataset_for_reading "keysight.ads.dataset.open_dataset_for_reading") | fail |
    | `"w"` | remove, then [`create_dataset()`](#keysight.ads.dataset.create_dataset "keysight.ads.dataset.create_dataset") | [`create_dataset()`](#keysight.ads.dataset.create_dataset "keysight.ads.dataset.create_dataset") |
    | `"a"` | [`open_dataset_for_read_write()`](#keysight.ads.dataset.open_dataset_for_read_write "keysight.ads.dataset.open_dataset_for_read_write") | [`create_dataset()`](#keysight.ads.dataset.create_dataset "keysight.ads.dataset.create_dataset") |
    | `"x"` | fail | [`create_dataset()`](#keysight.ads.dataset.create_dataset "keysight.ads.dataset.create_dataset") |

    To create an in-memory temporary dataset, use `":memory:"` for the `path`.
    The `mode` must be one of `"w"`, `"a"`, or `"x"`, and for any of those
    modes the implementation is [`create_dataset_in_memory()`](#keysight.ads.dataset.create_dataset_in_memory "keysight.ads.dataset.create_dataset_in_memory").

## open\_dataset\_for\_reading[](#open-dataset-for-reading "Link to this heading")

keysight.ads.dataset.open\_dataset\_for\_reading(*path: [PathLike](https://docs.python.org/3/library/os.md#os.PathLike "(in Python v3.14)")*) → [Dataset](#keysight.ads.dataset.Dataset "keysight.ads.dataset.Dataset")[](#keysight.ads.dataset.open_dataset_for_reading "Link to this definition")
:   Open a dataset file in a read-only mode.

    The resulting [`Dataset`](#keysight.ads.dataset.Dataset "keysight.ads.dataset.Dataset") object can be used as a context manager,
    for example:

    ```
    with dataset.open_dataset_for_reading("data.ds") as ds:
        print(ds.varblock_names)
    ```

## open\_dataset\_for\_read\_write[](#open-dataset-for-read-write "Link to this heading")

keysight.ads.dataset.open\_dataset\_for\_read\_write(*path: [PathLike](https://docs.python.org/3/library/os.md#os.PathLike "(in Python v3.14)")*) → [Dataset](#keysight.ads.dataset.Dataset "keysight.ads.dataset.Dataset")[](#keysight.ads.dataset.open_dataset_for_read_write "Link to this definition")
:   Open a dataset file for reading and writing.

    The resulting [`Dataset`](#keysight.ads.dataset.Dataset "keysight.ads.dataset.Dataset") object can be used as a context manager,
    for example:

    ```
    with dataset.open_dataset_for_read_write("data.ds") as ds:
        print(ds.varblock_names)
    ```

## create\_dataset[](#create-dataset "Link to this heading")

keysight.ads.dataset.create\_dataset(*path: [PathLike](https://docs.python.org/3/library/os.md#os.PathLike "(in Python v3.14)")*) → [Dataset](#keysight.ads.dataset.Dataset "keysight.ads.dataset.Dataset")[](#keysight.ads.dataset.create_dataset "Link to this definition")
:   Create a dataset file for writing.

    The resulting [`Dataset`](#keysight.ads.dataset.Dataset "keysight.ads.dataset.Dataset") object can be used as a context manager,
    for example:

    ```
    with dataset.create_dataset("data.ds") as ds:
        ds.create_varblock_from_dataframe(...)
    ```

## create\_dataset\_in\_memory[](#create-dataset-in-memory "Link to this heading")

keysight.ads.dataset.create\_dataset\_in\_memory() → [Dataset](#keysight.ads.dataset.Dataset "keysight.ads.dataset.Dataset")[](#keysight.ads.dataset.create_dataset_in_memory "Link to this definition")
:   Create a temporary dataset in memory, with no file storage.

    This is useful for temporary data, like intermediate results of a
    calculation, or testing dataset capabilities in scenarios where
    you don’t need a file to persist afterwards.

    The resulting [`Dataset`](#keysight.ads.dataset.Dataset "keysight.ads.dataset.Dataset") object can be used as a context manager,
    for example:

    ```
    with dataset.create_dataset_in_memory() as ds:
        ds.create_varblock_from_dataframe(...)
    ```

*class* keysight.ads.dataset.Dataset[](#keysight.ads.dataset.Dataset "Link to this definition")
:   Represents an ADS dataset, a file which typically has a `.ds` extension.

    The Dataset is a context manager. It can be used inside a `with` statement,
    like this:

    ```
    with dataset.open(path) as ds:
        print(ds.varblock_names)
    ```

    Don’t initialize a Dataset object directly. Use one of the functions:

    * [`open()`](#keysight.ads.dataset.open "keysight.ads.dataset.open")
    * [`open_dataset_for_reading()`](#keysight.ads.dataset.open_dataset_for_reading "keysight.ads.dataset.open_dataset_for_reading")
    * [`open_dataset_for_read_write()`](#keysight.ads.dataset.open_dataset_for_read_write "keysight.ads.dataset.open_dataset_for_read_write")
    * [`create_dataset()`](#keysight.ads.dataset.create_dataset "keysight.ads.dataset.create_dataset")
    * [`create_dataset_in_memory()`](#keysight.ads.dataset.create_dataset_in_memory "keysight.ads.dataset.create_dataset_in_memory")

    The Dataset works like a mapping of [`VariableBlock`](#keysight.ads.dataset.VariableBlock "keysight.ads.dataset.VariableBlock") objects, keyed by
    their names. Each of these rows shows equivalent syntax:

    | Using the `varblocks` property | Using `Dataset` directly |
    | --- | --- |
    | `ds.varblocks[name]` | `ds[name]` |
    | `for vb_name in ds.varblocks:` | `for vb_name in ds:` |
    | `for (name, vb) in ds.varblocks.items():` | `for (name, vb) in ds.items():` |

    create\_varblock\_from\_dataframe(*block\_name: [str](https://docs.python.org/3/library/stdtypes.md#str "(in Python v3.14)")*, *df: DataFrame*) → [VariableBlock](#keysight.ads.dataset.VariableBlock "keysight.ads.dataset.VariableBlock")[](#keysight.ads.dataset.Dataset.create_varblock_from_dataframe "Link to this definition")
    :   Create a VariableBlock from a pandas DataFrame.

        Parameters:
        :   * **block\_name** – The name for the created VariableBlock.
            * **df** – The dataframe containing the ivars (`df.index`),
              dvars (`df.columns`), and data values.

        The VariableBlock is added to the Dataset, and also returned.
        This returned value is the same as what you’d get from querying
        the `varblocks` afterward:

        ```
        vb1 = ds.create_varblock_from_dataframe(name, df)
        vb2 = ds.varblocks[name]
        assert vb1 == vb2
        ```

        Any pandas DataFrame that contains string data must set the
        type of the data to `string` before creating the VariableBlock
        to be added to the Dataset:

        ```
        strdata = ['A', 'B', 'C']
        df = pd.DataFrame({'data': strdata})
        assert df['data'].dtype == 'object'
        df['data'] = df['data'].astype('string')
        assert df['data'].dtype == 'string'
        vb = ds.create_varblock_from_dataframe(name, df)
        ```

    find\_varblocks\_with\_var\_name(*var\_name: [str](https://docs.python.org/3/library/stdtypes.md#str "(in Python v3.14)")*) → [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[VariableBlock](#keysight.ads.dataset.VariableBlock "keysight.ads.dataset.VariableBlock")][](#keysight.ads.dataset.Dataset.find_varblocks_with_var_name "Link to this definition")
    :   Find all variable blocks that contain a variable with the name var\_name.

        For example:

        ```
        for vb in ds.find_varblocks_with_var_name("freq"):
            print(vb.name)
        ```

    *property* is\_in\_memory\_type*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*[](#keysight.ads.dataset.Dataset.is_in_memory_type "Link to this definition")
    :   `True` if the dataset is an in-memory dataset, or
        `False` if it is on disk.

    *property* is\_read\_only*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*[](#keysight.ads.dataset.Dataset.is_read_only "Link to this definition")
    :   `True` if the dataset is open for reading only, or
        `False` if modifications are allowed.

    *property* path*: [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*[](#keysight.ads.dataset.Dataset.path "Link to this definition")
    :   The path to the file on the filesystem, or `None` for
        an in-memory dataset.

    *property* varblock\_names*: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[](#keysight.ads.dataset.Dataset.varblock_names "Link to this definition")
    :   The names of variable blocks in the dataset.

        `ds.varblock_names` is equivalent to, and faster than,
        `ds.varblocks.keys()`.

    *property* varblocks*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [VariableBlock](#keysight.ads.dataset.VariableBlock "keysight.ads.dataset.VariableBlock")]*[](#keysight.ads.dataset.Dataset.varblocks "Link to this definition")
    :   The variable blocks in the dataset.

        For less typing, you can subscript the Dataset object directly. These two
        lines are equivalent:

        ```
        ds.varblocks[name]
        ds[name]
        ```

*class* keysight.ads.dataset.VariableBlock[](#keysight.ads.dataset.VariableBlock "Link to this definition")
:   Contains a set of dependent and independent variables.

    Use [`Dataset.varblocks`](#keysight.ads.dataset.Dataset.varblocks "keysight.ads.dataset.Dataset.varblocks") to get an existing VariableBlock
    object, or [`Dataset.create_varblock_from_dataframe()`](#keysight.ads.dataset.Dataset.create_varblock_from_dataframe "keysight.ads.dataset.Dataset.create_varblock_from_dataframe") to
    create a new VariableBlock.

    *property* dvars*: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[Variable](#keysight.ads.dataset.Variable "keysight.ads.dataset.Variable")]*[](#keysight.ads.dataset.VariableBlock.dvars "Link to this definition")
    :   The dependent variables.

    *property* dvars\_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[](#keysight.ads.dataset.VariableBlock.dvars_count "Link to this definition")
    :   The number of dependent variables.

        `vb.dvars_count` is equivalent to, and faster than, `len(vb.dvars)`.

    *property* ivars*: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[Variable](#keysight.ads.dataset.Variable "keysight.ads.dataset.Variable")]*[](#keysight.ads.dataset.VariableBlock.ivars "Link to this definition")
    :   The independent variables.

    *property* ivars\_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*[](#keysight.ads.dataset.VariableBlock.ivars_count "Link to this definition")
    :   The number of independent variables.

        `vb.ivars_count` is equivalent to, and faster than, `len(vb.ivars)`.

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[](#keysight.ads.dataset.VariableBlock.name "Link to this definition")
    :   The name of the VariableBlock.

    to\_dataframe(*dvar\_names: [Sequence](https://docs.python.org/3/library/typing.md#typing.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → DataFrame[](#keysight.ads.dataset.VariableBlock.to_dataframe "Link to this definition")
    :   Extracts the VariableBlock’s data as a pandas DataFrame.

        Currently this is the only way to access the data inside a VariableBlock.

        Example:

        ```
        with dataset.open(path) as ds:
            df = ds["My Results"].to_dataframe()
        max_voltage = df["Vout"].max()
        avg_voltage = df["Vout"].mean()
        df["Delta Vout"] = df["Vout"] - df["Vout"].min()

        # only convert a single Vout to a dataframe
        with dataset.open(path) as ds:
            df = ds["My Results"].to_dataframe(dependent_vars=["Vout"])
        max_voltage = df["Vout"].max()
        ```

*class* keysight.ads.dataset.Variable[](#keysight.ads.dataset.Variable "Link to this definition")
:   A dependent variable or an independent variable inside a VariableBlock.

    Use [`VariableBlock.ivars`](#keysight.ads.dataset.VariableBlock.ivars "keysight.ads.dataset.VariableBlock.ivars") or [`VariableBlock.dvars`](#keysight.ads.dataset.VariableBlock.dvars "keysight.ads.dataset.VariableBlock.dvars") to get
    a Variable object.

    *property* attrs*: VariableAttributes*[](#keysight.ads.dataset.Variable.attrs "Link to this definition")
    :   The attributes stored on the variable, represented as a mapping with
        keys as strings and values as strings.

    *property* data\_type*: [Type](https://docs.python.org/3/library/typing.html#typing.Type "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [complex](https://docs.python.org/3/library/functions.html#complex "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*[](#keysight.ads.dataset.Variable.data_type "Link to this definition")
    :   The data type of the variable’s elements, as a Python type.

        This attribute’s value is a Python type like `int` or `complex`.

    *property* dtype*: [dtype](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)") | ExtensionDtype*[](#keysight.ads.dataset.Variable.dtype "Link to this definition")
    :   The data type of the variable’s elements, as a numpy dtype.

        This attribute’s value is a numpy dtype like `np.dtype(float)`
        or `np.dtype(complex)`, or a pandas extension type like
        `pd.StringDtype()`.

    *property* flags*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[](#keysight.ads.dataset.Variable.flags "Link to this definition")
    :   The `"flags"` attribute stored on the variable, parsed into name-value pairs.

        Sometimes a variable have a “variable type” as an initial entry in its flags.
        This entry has no name. It’s currently represented in this mapping with the key
        `""`, however this is subject to change. Use [`variable_type`](#keysight.ads.dataset.Variable.variable_type "keysight.ads.dataset.Variable.variable_type") to get this
        value.

    *property* is\_indep*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*[](#keysight.ads.dataset.Variable.is_indep "Link to this definition")
    :   Indicates whether the variable is an independent (`True`) or
        dependent (`False`).

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[](#keysight.ads.dataset.Variable.name "Link to this definition")
    :   The name of the variable.

    *property* variable\_type*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*[](#keysight.ads.dataset.Variable.variable_type "Link to this definition")
    :   The type of variable, such as `"voltage"` or `"s-parameters"`. If there’s
        no variable type provided, this property holds an empty string, `""`.


---

## 4. examples\index.md {#examples--index}

# Examples[](#examples "Link to this heading")

Contents:

* [Merge DataFrames](ex_merge_dataframes.md)
* [Merge Irregular DataFrames](ex_merge_irregular_dataframes.md)
* [Merge Datasets](ex_merge_datasets.md)
* [Create Dataset from DataFrame](ex_create_dataset_from_dataframe.md)


---

## 5. examples\ex_merge_dataframes.md {#examples--ex_merge_dataframes}

# Merge DataFrames[](#merge-dataframes "Link to this heading")

This example shows how to merge two DataFrames into a single
DataFrame adding an outer variable corresponding to the original
DataFrames. This same method can be utilized to merge data from
multiple ADS Datasets.

```
# Copyright Keysight Technologies 2025 - 2025

import numpy as np
import pandas as pd

# Create data for the DataFrames
ind_data = [1e-3, 2e-3, 3e-3, 4e-3]
dep_data1 = [1, 2, 5, 10]
dep_data2 = [10, 20, 50, 100]

# Create an Index object named 'time' using the independent data
idx = pd.Index(data=ind_data, name="time")

# Create the DataFrames with the data and index.
df1 = pd.DataFrame({"V": dep_data1}, index=idx)
df2 = pd.DataFrame({"V": dep_data2}, index=idx)

# NOTE: At this point, these DataFrame objects could have come from
#       two ADS Datasets generated from ADS simulations.

# Add a new outer independent variable. In this case we will add 'R'
# to indicate that the data came from two different simulations where
# a resistor value was equal to 100 for one simulation and 2000 for
# the other.

# Get the Index of the data from each DataFrame object (we already
# know the Index value but we would do this if we were using
# DataFrames from ADS Datasets).
idx1 = df1.index.to_frame()
idx2 = df2.index.to_frame()

# Add R to the Index objects
idx1.insert(0, "R", 100)
idx2.insert(0, "R", 2000)

# Update the DataFrames with the updated Index with 'R' values.
df1.index = pd.MultiIndex.from_frame(idx1)
df2.index = pd.MultiIndex.from_frame(idx2)

# Finally create the merged DataFrame
merged_df = pd.concat([df1, df2])

# Validate the data we just created....
expected_dep_data = np.array([[1], [2], [5], [10], [10], [20], [50], [100]])
np.testing.assert_array_equal(merged_df.values, expected_dep_data)

expected_r_data = np.array([100, 100, 100, 100, 2000, 2000, 2000, 2000])
np.testing.assert_array_equal(merged_df.index.get_level_values(0), expected_r_data)

expected_time_data = np.array([1e-3, 2e-3, 3e-3, 4e-3, 1e-3, 2e-3, 3e-3, 4e-3])
np.testing.assert_array_equal(merged_df.index.get_level_values(1), expected_time_data)

# At this point you can display the results directly in Data Display
# using the py_var() function.  Or you can create a new ADS Dataset
# containing the merged DataFrame.
```


---

## 6. examples\ex_merge_irregular_dataframes.md {#examples--ex_merge_irregular_dataframes}

# Merge Irregular DataFrames[](#merge-irregular-dataframes "Link to this heading")

This example shows how to merge two DataFrames which contain
different sized data into a single DataFrame. First new outer
independent variables are added the DataFrames corresponding to the
original DataFrames. Then the DataFrames are merged into a single
DataFrame that can be displayed in Data Display or saved to an ADS
Dataset.

```
# Copyright Keysight Technologies 2025 - 2025

import numpy as np
import pandas as pd

# Create data for the DataFrames
ind_data1 = [1e-3, 2e-3, 3e-3, 4e-3]
dep_data1 = [1, 2, 5, 10]

# The second set to data has different independent values and
# different number of data points.
ind_data2 = [1.5e-3, 2e-3, 2.5e-3, 3e-3, 3.5e-3]
dep_data2 = [10, 155, 50, 55, 100]

# Create Index objects named 'time' using the independent data.
idx1 = pd.Index(data=ind_data1, name="time")
idx2 = pd.Index(data=ind_data2, name="time")

# Create the DataFrames with the data and index.
df1 = pd.DataFrame({"V": dep_data1}, index=idx1)
df2 = pd.DataFrame({"V": dep_data2}, index=idx2)

# NOTE: At this point, these DataFrame objects could have come from
#       two ADS Datasets generated from ADS simulations.

# Add a new outer independent variable. In this case we will add 'L'
# and 'R' as the outer independent variables.

# Get the Index of the data from each DataFrame object (we already know
# the Index values but we would do this if we were using DataFrames from
# ADS Datasets).
idx1 = df1.index.to_frame()
idx2 = df2.index.to_frame()

# Add L and R to the Index objects
idx1.insert(0, "R", 100)
idx1.insert(0, "L", 1e-9)
idx2.insert(0, "R", 2000)
idx2.insert(0, "L", 10e-9)

# Update the DataFrames with the updated Index values.
df1.index = pd.MultiIndex.from_frame(idx1)
df2.index = pd.MultiIndex.from_frame(idx2)

# Finally create the merged DataFrame
merged_df = pd.concat([df1, df2])

# Validate the data we just created....
expected_dep_data = np.array([[1], [2], [5], [10], [10], [155], [50], [55], [100]])
np.testing.assert_array_equal(merged_df.values, expected_dep_data)

expected_l_data = np.array([1e-9, 1e-9, 1e-9, 1e-9, 10e-9, 10e-9, 10e-9, 10e-9, 10e-9])
np.testing.assert_array_equal(merged_df.index.get_level_values(0), expected_l_data)

expected_r_data = np.array([100, 100, 100, 100, 2000, 2000, 2000, 2000, 2000])
np.testing.assert_array_equal(merged_df.index.get_level_values(1), expected_r_data)

expected_time_data = np.array(
    [1e-3, 2e-3, 3e-3, 4e-3, 1.5e-3, 2e-3, 2.5e-3, 3e-3, 3.5e-3]
)
np.testing.assert_array_equal(merged_df.index.get_level_values(2), expected_time_data)
```


---

## 7. examples\ex_merge_datasets.md {#examples--ex_merge_datasets}

# Merge Datasets[](#merge-datasets "Link to this heading")

This example shows how to merge three ADS Datasets into a single ADS
Dataset containing the merged data.

```
# Copyright Keysight Technologies 2025 - 2025

from os import PathLike
from pathlib import Path
from collections.abc import Sequence

import keysight.ads.dataset as ds
import pandas as pd

example_path = Path(__file__).parent.parent.resolve() / "examples"

def _validate_input_values(
    datasets_to_merge_paths: list[Path],
    sweep_names: list[str],
    sweep_values: list[list[int | float | str]],
) -> None:
    if not datasets_to_merge_paths:
        raise RuntimeError("No datasets to merge were specified.")
    if len(datasets_to_merge_paths) < 2:
        raise RuntimeError("Must include at least 2 datasets to merge.")
    if len(sweep_values) != len(datasets_to_merge_paths):
        raise RuntimeError("The number of datasets and sweep values must be equation.")
    for sweep_value in sweep_values:
        if len(sweep_names) != len(sweep_value):
            raise RuntimeError(
                "The number of sweep names and sweep values must be equation."
            )

def _init_unique_list_of_varblock_names(
    datasets_to_merge_paths: list[Path],
) -> list[str]:
    varblock_names = []
    for ds_path in datasets_to_merge_paths:
        dataset = ds.open_dataset_for_reading(ds_path)
        varblock_names += dataset.varblock_names
    return list(set(varblock_names))

def _add_sweeps_to_single_dataframe(
    df: pd.DataFrame,
    sweep_names: list[str],
    sweep_values: list[int | float | str],
) -> None:
    idx = df.index.to_frame()
    for sn, sv in zip(sweep_names, sweep_values, strict=True):
        idx.insert(0, sn, sv)
    df.index = pd.MultiIndex.from_frame(idx)

def _add_sweeps_to_multiple_dataframes(
    dfs: list[pd.DataFrame],
    sweep_names: list[str],
    sweep_values: list[list[int | float | str]],
) -> None:
    for df, sv in zip(dfs, sweep_values, strict=True):
        _add_sweeps_to_single_dataframe(df, sweep_names, sv)

def _get_dataframe_for_varblock_name_in_single_dataset(
    ds_path: Path, varblock_name: str
) -> pd.DataFrame:
    dataset = ds.open_dataset_for_reading(ds_path)
    if varblock_name not in dataset.varblock_names:
        return pd.DataFrame()
    return dataset[varblock_name].to_dataframe()

def _get_dataframes_for_varblock_name_in_multiple_datasets(
    datasets_to_merge_paths: list[Path],
    varblock_name: str,
) -> list[pd.DataFrame]:
    dfs = []
    for ds_path in datasets_to_merge_paths:
        df = _get_dataframe_for_varblock_name_in_single_dataset(ds_path, varblock_name)
        dfs.append(df)
    return dfs

def _get_merged_dataframe_for_varblock_name_in_multiple_datasets(
    datasets_to_merge_paths: list[Path],
    sweep_names: list[str],
    sweep_values: list[list[int | float | str]],
    varblock_name: str,
) -> pd.DataFrame:
    dfs = _get_dataframes_for_varblock_name_in_multiple_datasets(
        datasets_to_merge_paths, varblock_name
    )
    if not dfs:
        raise RuntimeError(
            'Internal Error: Failed to get at least one DataFrame for the VarBlock "'
            + varblock_name
            + '".'
        )
    _add_sweeps_to_multiple_dataframes(dfs, sweep_names, sweep_values)
    return pd.concat(dfs)

def merge_datasets(
    merged_dataset_name: str | PathLike,
    datasets_to_merge: Sequence[str | PathLike],
    swp_names: Sequence[str],
    swp_values: Sequence[Sequence[int | float | str]],
) -> None:
    """Create a merged dataset from a group of datasets.

    This class creates a single merge dataset from a group of
    datasets. The expectation is that each dataset to be merged was
    created from ADS with the same simulation setup but with different
    discreate values for one or more compentents. The class takes in
    lists of names for each component value that was changed in each
    simulation and the values that were varied.

    Parameters
    ----------
    datasets_to_merge
        A list of datasets names or Paths.
    sweep_names
        A list of sweep names to utilize for each dataset begin merged.
    sweep_values
        A list of list of sweep values. The outer list has an entry
        for each dataset being merged. The inner lists has values that
        match the number of sweep names.

    Example
    -------
        This example creates a merged dataset called 'merged.ds'. It
        takes two ADS Datasets that were created with value R and C
        being changed in the simulations. The simulation that created
        the "a.ds" dataset utilized the values "R=500" and "C=1e-9". A
        different simulation created the "b.ds" dataset with the
        values for set to "R=1000" and "C=10e-9".

    >>> merge_datasets('merged.ds',['a.ds', 'b.ds'], ['R', 'C'], [[500, 1e-9], [1000, 10e-9]])
    """

    datasets_to_merge_paths = [Path(t) for t in datasets_to_merge]
    sweep_names = list(reversed(swp_names))
    sweep_values = [list(reversed(t)) for t in swp_values]
    _validate_input_values(datasets_to_merge_paths, sweep_names, sweep_values)
    varblock_names = _init_unique_list_of_varblock_names(datasets_to_merge_paths)

    merged_dataset_path = Path(merged_dataset_name)
    merged_dataset = ds.open(merged_dataset_path, mode="w")

    for varblock_name in varblock_names:
        df = _get_merged_dataframe_for_varblock_name_in_multiple_datasets(
            datasets_to_merge_paths, sweep_names, sweep_values, varblock_name
        )
        if df.empty:
            raise RuntimeError(
                'Internal Error: Failed to get at least one merged DataFrame for the VarBlock "'
                + varblock_name
                + '".'
            )
        merged_dataset.create_varblock_from_dataframe(varblock_name, df)

if __name__ == "__main__":
    data_path = example_path / "data"
    dataset_paths = (
        data_path / "RLC_10_15_20.ds",
        data_path / "RLC_10_15_25.ds",
        data_path / "RLC_10_20_15.ds",
    )

    sweep_names = ("R", "L", "C")
    sweep_values = ((10, 15, 20), (10, 15, 25), (10, 20, 15))

    # Cleanup the old merged dataset (if it exists).
    merged_dataset_path = Path("RLC_merged.ds").resolve()
    if merged_dataset_path.exists():
        merged_dataset_path.unlink()

    # Do the merge of datsets.
    merge_datasets(merged_dataset_path, dataset_paths, sweep_names, sweep_values)

    # Validate that the merged dataset was created.
    if not merged_dataset_path.exists():
        raise RuntimeError(
            'Failed to generate dataset output in "merge_datasets.py" for "'
            + str(merged_dataset_path.name)
            + '"'
        )
```


---

## 8. examples\ex_create_dataset_from_dataframe.md {#examples--ex_create_dataset_from_dataframe}

# Create Dataset from DataFrame[](#create-dataset-from-dataframe "Link to this heading")

This example shows how to create a ADS Dataset from a DataFrame.

```
# Copyright Keysight Technologies 2025 - 2025

from pathlib import Path

import pandas as pd
import keysight.ads.dataset as ds

# Create data
str_data = ["str1", "str2", "str3", "str4", "str5", "str6"]
int_data = [1, 20, 50, 2, 22, 55]

# Create independent data
time_data = [1e-3, 1.2e-3, 1.5e-3, 1e-3, 1.2e-3, 1.5e-3]
name_data = ["A", "A", "A", "B", "B", "B"]

# Create an empty DataFrame
df = pd.DataFrame(
    {
        "name": name_data,
        "time": time_data,
        "str_data": str_data,
        "int_data": int_data,
    }
)

assert df["name"].dtype == "object"
assert df["time"].dtype == "float64"
assert df["str_data"].dtype == "object"
assert df["int_data"].dtype == "int64"

# At this point the string data is of dtype == object. However,
# dataset code doesn't know what to do with the dtype of object.
# So, change the dtype to "string" before calling the dataset
# code to create the datasets.
df[["name", "str_data"]] = df[["name", "str_data"]].astype("string")

assert df["name"].dtype == "string"
assert df["time"].dtype == "float64"
assert df["str_data"].dtype == "string"
assert df["int_data"].dtype == "int64"

# Reorganize the DataFrame making "name" and "time" independents
df.set_index(["name", "time"], inplace=True)

# Build the dataset from the dataframe.
dataset_path = Path("string_test.ds")
dataset = ds.open(dataset_path, mode="w")
dataset.create_varblock_from_dataframe("StringTest", df)

assert dataset_path.exists()
```


---

## 9. history.md {#history}

# History[](#history "Link to this heading")

## 0.9.9 (2025-05-22)[](#id1 "Link to this heading")

* Drop dependency on GLIBCXX

## 0.9.8 (2025-02-27)[](#id2 "Link to this heading")

* Updated numpy version to >=1.21,<3
* Removed support for Python 3.8 and Python 3.9
* Added support for Python 3.13

## 0.9.6 (2024-07-03)[](#id3 "Link to this heading")

* Added support for Python 3.12.

## 0.9.4 (2024-06-28)[](#id4 "Link to this heading")

* Added optional argument to specify which variable blocks to convert in to\_dataframe() function
* Improved support for missing independent data when converting to a dataframe
* Improved dataframe support for variable blocks with one independent variable

## 0.9.3 (2024-02-26)[](#id5 "Link to this heading")

* Read and write performance improvement
* Corresponds to keysight-ads-dataset “600” wheel available in ADS installation wheelhouse (python 3.10 only)

## 0.9.2 (2023-04-19)[](#id6 "Link to this heading")

* Updated requirements to be less strict.
* Added support for Python 3.11.

## 0.9.1 (2022-09-01)[](#id7 "Link to this heading")

* Added [dataset.open](apidoc.md#keysight.ads.dataset.open "keysight.ads.dataset.open") function.
* Added support for Python 3.8, 3.9, and 3.10.

## 0.9.0 (2022-06-09)[](#id8 "Link to this heading")

* First public release.


---

## 10. dependencies.md {#dependencies}

# Dependencies[](#dependencies "Link to this heading")

Below are the Python package dependencies.

* pandas >= 1.4
* numpy >= 1.21 <3
