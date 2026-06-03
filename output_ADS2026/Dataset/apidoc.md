<!-- 来源: apidoc.html -->

[![Logo](_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-ads-dataset](index.md)
* API Documentation

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* [Concepts](concepts.md)
* API Documentation
* [Examples](examples/index.md)
  + [Merge DataFrames](examples/ex_merge_dataframes.md)
  + [Merge Irregular DataFrames](examples/ex_merge_irregular_dataframes.md)
  + [Merge Datasets](examples/ex_merge_datasets.md)
  + [Create Dataset from DataFrame](examples/ex_create_dataset_from_dataframe.md)
* [History](history.md)
* [Dependencies](dependencies.md)

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

On this page

[Previous

Concepts](concepts.md)
[Next

Examples](examples/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top