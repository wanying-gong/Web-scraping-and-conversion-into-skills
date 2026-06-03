# Howto
> **说明：** Howto 相关页面。

> **何时使用：** 当你需要查阅 Howto 相关内容时

---

## 本文件目录

- **Get the Data Tools Version** (`howto/get_the_version.md`)
- **How To** (`howto/index.md`)
- **Read a File** (`howto/read_a_file.md`)
- **Show or Hide Log Messages** (`howto/show_or_hide_messages.md`)
- **Translate a File** (`howto/translate_a_file.md`)
- **Use the Block Class** (`howto/use_block_class.md`)
- **Use the Group Class** (`howto/use_group_class.md`)
- **Use the New Data Tools Version** (`howto/use_new_version.md`)
- **Use the Var Class** (`howto/use_var_class.md`)
- **Work with ADS Data** (`howto/work_with_ADS_data.md`)
- **Work with CSV Data** (`howto/work_with_csv_data.md`)
- **Work with Load Pull Data** (`howto/work_with_loadpull_data.md`)
- **Work with SystemVue Data** (`howto/work_with_SystemVue_data.md`)
- **Write a File** (`howto/write_a_file.md`)

---

<!-- === 来源: howto/get_the_version.md === -->

# Get the Data Tools Version[](#get-the-data-tools-version "Link to this heading")

The version of PathWave Data Tools can be obtained from Python or from a terminal.

## From Python[](#from-python "Link to this heading")

You can use either the `version()` function or the `__version__` attribute to get the version of PathWave Data Tools.

```
>>> from keysight import pwdatatools as pwdt
>>> pwdt.version()
0.8.0
>>> pwdt.__version__
0.8.0
```

## From a Terminal[](#from-a-terminal "Link to this heading")

You can use `pip list` from a command line:

On Windows:

```
> pip list | FINDSTR /I "keysight-pwdatatools"
keysight-pwdatatools   0.8.0
```

On Linux:

```
$ pip list | grep -i keysight-pwdatatools
keysight-pwdatatools   0.8.0
```


---

<!-- === 来源: howto/index.md === -->

# How To[](#how-to "Link to this heading")

* [Read a File](read_a_file.md)
* [Write a File](write_a_file.md)
* [Translate a File](translate_a_file.md)
* [Use the Var Class](use_var_class.md)
* [Use the Block Class](use_block_class.md)
* [Use the Group Class](use_group_class.md)
* [Work with ADS Data](work_with_ADS_data.md)
* [Work with CSV Data](work_with_csv_data.md)
* [Work with Load Pull Data](work_with_loadpull_data.md)
* [Work with SystemVue Data](work_with_SystemVue_data.md)
* [Show or Hide Log Messages](show_or_hide_messages.md)
* [Get the Data Tools Version](get_the_version.md)
* [Use the New Data Tools Version](use_new_version.md)


---

<!-- === 来源: howto/read_a_file.md === -->

# Read a File[](#read-a-file "Link to this heading")

Data Tools has several top-level functions to read datafiles. You can use [`read_file_as_group()`](../api_reference/fileio/read_file_as_group.md#keysight.pwdatatools._api.funcs.read_file_as_group "keysight.pwdatatools._api.funcs.read_file_as_group") to read any datafile, including those with hierarchy or multiple blocks. You can use [`read_file_as_block()`](../api_reference/fileio/read_file_as_block.md#keysight.pwdatatools._api.funcs.read_file_as_block "keysight.pwdatatools._api.funcs.read_file_as_block") for datafiles that are not hierarchical or only contain a single block. There is also a function [`read_file()`](../api_reference/fileio/read_file.md#keysight.pwdatatools._api.funcs.read_file "keysight.pwdatatools._api.funcs.read_file") that will read a file as a [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group"), unless you perform a partial read (in which case it could return either a [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") or [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block")). The [`read_file()`](../api_reference/fileio/read_file.md#keysight.pwdatatools._api.funcs.read_file "keysight.pwdatatools._api.funcs.read_file") function is the least-preferred way to read datafiles because it can return either a [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") or a [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"). If you know the file is hierarchical, use [`read_file_as_group()`](../api_reference/fileio/read_file_as_group.md#keysight.pwdatatools._api.funcs.read_file_as_group "keysight.pwdatatools._api.funcs.read_file_as_group"). If you know the file is not hierarchical, use [`read_file_as_block()`](../api_reference/fileio/read_file_as_block.md#keysight.pwdatatools._api.funcs.read_file_as_block "keysight.pwdatatools._api.funcs.read_file_as_block"). If you don’t know whether the file is hierarchical, use [`read_file_as_group()`](../api_reference/fileio/read_file_as_group.md#keysight.pwdatatools._api.funcs.read_file_as_group "keysight.pwdatatools._api.funcs.read_file_as_group") and then examine the returned [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group").

The functions [`read_file_as_group()`](../api_reference/fileio/read_file_as_group.md#keysight.pwdatatools._api.funcs.read_file_as_group "keysight.pwdatatools._api.funcs.read_file_as_group") and [`read_file_as_block()`](../api_reference/fileio/read_file_as_block.md#keysight.pwdatatools._api.funcs.read_file_as_block "keysight.pwdatatools._api.funcs.read_file_as_block") also have equivalent aliases [`Group.from_file()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.from_file.md#keysight.pwdatatools.Group.from_file "keysight.pwdatatools.Group.from_file") and [`Block.from_file()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.from_file.md#keysight.pwdatatools.Block.from_file "keysight.pwdatatools.Block.from_file"), respectively.

You can also read load pull data directly into a specialized type of Block called a [`LoadPullBlock`](../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock"). This is done with [`read_file_as_loadpullblock()`](../api_reference/fileio/read_file_as_loadpullblock.md#keysight.pwdatatools._api.funcs.read_file_as_loadpullblock "keysight.pwdatatools._api.funcs.read_file_as_loadpullblock"), or [`LoadPullBlock.from_file()`](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.from_file.md#keysight.pwdatatools.LoadPullBlock.from_file "keysight.pwdatatools.LoadPullBlock.from_file").

See also

[File Extensions and Formats](../core_concepts/file_exts_and_formats.md#file-exts-and-formats)

Click on any of the below functions or methods to jump to their documentation:

* [`read_file()`](../api_reference/fileio/read_file.md#keysight.pwdatatools._api.funcs.read_file "keysight.pwdatatools._api.funcs.read_file")
* [`read_file_as_group()`](../api_reference/fileio/read_file_as_group.md#keysight.pwdatatools._api.funcs.read_file_as_group "keysight.pwdatatools._api.funcs.read_file_as_group") (or its alias [`Group.from_file()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.from_file.md#keysight.pwdatatools.Group.from_file "keysight.pwdatatools.Group.from_file"))
* [`read_file_as_block()`](../api_reference/fileio/read_file_as_block.md#keysight.pwdatatools._api.funcs.read_file_as_block "keysight.pwdatatools._api.funcs.read_file_as_block") (or its alias [`Block.from_file()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.from_file.md#keysight.pwdatatools.Block.from_file "keysight.pwdatatools.Block.from_file"))
* [`read_file_as_loadpullblock()`](../api_reference/fileio/read_file_as_loadpullblock.md#keysight.pwdatatools._api.funcs.read_file_as_loadpullblock "keysight.pwdatatools._api.funcs.read_file_as_loadpullblock") (or its alias [`LoadPullBlock.from_file()`](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.from_file.md#keysight.pwdatatools.LoadPullBlock.from_file "keysight.pwdatatools.LoadPullBlock.from_file"))

## Partial reading[](#partial-reading "Link to this heading")

PathWave Data Tools supports partial reading for hierarchical datafile formats. Examples of hierarchical formats are ADS datasets, SystemVue workspace files, generic MDIF files, CITI files, and the native `pwdatatools` file format (with a .pwdt file extension). All file reading functions and methods support partial reading via the `loc` parameter. For some file formats, partial reading can be much faster than a full read. How much faster depends on how large the total file is and whether the file format is text or binary. Below are a few examples of partial reading.

```
>>> import keysight.pwdatatools as pwdt
>>> # partial read of a native pwdatatools file can return either a Group or Block
>>> group = pwdt.read_file_as_group('/data/my_file.pwdt', loc='/my_group')
>>> block = pwdt.read_file_as_block('/data/my_file.pwdt', loc='/my_group/my_block')
>>> # partial read of ADS dataset returns a Block
>>> block = pwdt.read_file_as_block('/data/hb_sim.ds', loc='/HB.HB1')
>>> # partial read a CITIfile returns a Block
>>> block = pwdt.read_file_as_block('/data/my_file.citi', loc='/my_block')
>>> # partial read of a dataset from SystemVue workspace returns a Group
>>> group = pwdt.read_file_as_group('/data/my_file.wsv', loc='/my_dataset')
```

Important

In all of the above examples, the [`read_file()`](../api_reference/fileio/read_file.md#keysight.pwdatatools._api.funcs.read_file "keysight.pwdatatools._api.funcs.read_file") function would have worked. However, [`read_file_as_group()`](../api_reference/fileio/read_file_as_group.md#keysight.pwdatatools._api.funcs.read_file_as_group "keysight.pwdatatools._api.funcs.read_file_as_group") and [`read_file_as_block()`](../api_reference/fileio/read_file_as_block.md#keysight.pwdatatools._api.funcs.read_file_as_block "keysight.pwdatatools._api.funcs.read_file_as_block") are more explicit in their return types and therefore should be preferred.

In order to use the `loc` parameter, you must know either the name or position of the Group or Block you’d like to read. You can use the [`DataFile.tree()`](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.tree.md#keysight.pwdatatools.DataFile.tree "keysight.pwdatatools.DataFile.tree") method to examine the file’s hierarchy and determine the desired `loc`. To demonstrate, below we would like to read a Block from an ADS dataset. So, we first use the [`DataFile.tree()`](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.tree.md#keysight.pwdatatools.DataFile.tree "keysight.pwdatatools.DataFile.tree") method to examine the dataset’s hierarchy and find the name and position of the Block to read.

```
>>> import keysight.pwdatatools as pwdt
>>> # create a DataFile object from an ADS dataset
>>> datafile = pwdt.DataFile('/data/s_param_and_hb.ds')
>>> # examine the dataset's hierarchy
>>> print(datafile.tree())
<[/] Group 's_param_w_2sweptvars_HB'>
├── <[0] Block 'Sweep2.Sweep1.SP1.SP' with 5 Vars>
├── <[1] Block 'HB1.HB' with 4 Vars>
└── <[2] Block 'aele_0.HB1.HB' with 2 Vars>
```

In the above tree printout, the positions of each Block are shown in square brackets and their names are in single quotes. Now, we can read the second Block from the dataset using the [`read_file_as_block()`](../api_reference/fileio/read_file_as_block.md#keysight.pwdatatools._api.funcs.read_file_as_block "keysight.pwdatatools._api.funcs.read_file_as_block") function, using either a name-based or position-based `loc` value.

```
>>> block = pwdt.read_file_as_block('/data/s_param_and_hb.ds', loc='/HB1.HB') # read the Block by name
>>> block = pwdt.read_file_as_block('/data/s_param_and_hb.ds', loc='/1') # read the Block by position
```

Alternatively, you can leave out the leading slash when specifying a value for `loc`. For example, the following two lines of code are equivalent to the previous two lines of code.

```
>>> block = pwdt.read_file_as_block('/data/s_param_and_hb.ds', loc='HB1.HB')
>>> block = pwdt.read_file_as_block('/data/s_param_and_hb.ds', loc='1')
```

Note

The [`DataFile.tree()`](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.tree.md#keysight.pwdatatools.DataFile.tree "keysight.pwdatatools.DataFile.tree") method does *not* read the data into memory, so it should be faster than a full read. How much faster depends on the file format. It tends to be much faster for binary files, and only slightly faster for text files. See the next section for more information on metadata-only reading.

## Metadata-only reading[](#metadata-only-reading "Link to this heading")

PathWave Data Tools supports metadata-only reading for all file formats. Excluding the data during a read can be helpful if you’d like to quickly see information about the variables (their names, dtypes, dimensions,etc.), or if you’d like to see a datafile’s hierarchy (examine Block names, Group names, etc.). Metadata-only reading can be significantly faster than a full read, but how much faster depends upon the overall size of the datafile and whether the datafile format is text or binary. All file reading functions and methods support metadata-only file reading via the `data` parameter (setting `data=False` enables metadata-only mode). Below are a few examples of metadata-only reading.

```
>>> import keysight.pwdatatools as pwdt
>>> # metadata-only read of a native pwdatatools file using the read_file function
>>> group = pwdt.read_file('/data/my_file.pwdt', data=False, loc='/my_group')
>>> # metadata-only read of an ADS dataset using the read_file_as_group function
>>> block = pwdt.read_file_as_group('/data/my_file.ds', data=False)
>>> # metadata-only read of an MDIF file using the Group.from_file method
>>> group = pwdt.Group.from_file('/data/my_file.mdif', data=False)
```

Reading a file as a Group or Block in metadata-only mode gives much more information than [`DataFile.tree()`](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.tree.md#keysight.pwdatatools.DataFile.tree "keysight.pwdatatools.DataFile.tree"). We can examine the names of the variables in the Block, and all other metadata (both variable-level and Block-level metadata).

```
>>> import keysight.pwdatatools as pwdt
>>> # Metadata-only read of an ADS dataset using the read_file_as_block function
>>> block = pwdt.read_file_as_block('/data/my_sdata.ds', data=False, loc='SP1.SP')
>>> # Examine the Block's summary, noting that it has 0 observations
>>> block
Block(
    <'S', 'PortZ', ... with 0 observations>,
    name='SP1.SP',
    ivarnames=('freq',),
    attrs={},
)
>>> # Examine the names of the variables in the Block
>>> block.varnames
('freq', 'S', 'PortZ')
>>> # Examine the ivarnames of the Block
>>> block.ivarnames
('freq',)
>>> # Examine the variables
>>> # Note that all metadata is present, but the data arrays are empty
>>> block['freq']
Var(
    <Float64 data with shape (0,)>,
    name='freq',
    dims=<empty Dims>,
    role='frequency.primary',
    unit=None,
    attrs={'mixop': ...},
)
>>> block['S']
Var(
    <Complex128 data with shape (0, 2, 2)>,
    name='S',
    dims=<Dims with nums>,
    role='network_parameters.s',
    unit=None,
    attrs={},
)
>>> block['PortZ']
Var(
    <Complex128 data with shape (0, 2)>,
    name='PortZ',
    dims=<Dims with nums>,
    role='impedance.port',
    unit=None,
    attrs={},
)
```


---

<!-- === 来源: howto/show_or_hide_messages.md === -->

# Show or Hide Log Messages[](#show-or-hide-log-messages "Link to this heading")

The `keysight.pwdatatools` library prints info, warning, and error logging messages to the console in certain situations. The default behavior is to print only warnings and errors, hiding info and debug messages. This behavior can be modified as shown below.

```
>>> from keysight.pwdatatools as pwdt
>>> # view the current level. Here it is 'warning', which only shows warnings and errors, not info messages
>>> pwdt.options.logging.level
'warning'
>>> # change the level to 'info', will show all info, warning and error messages
>>> pwdt.options.logging.level = 'info'
```

For more information, see [Global Options](../api_reference/global_options.md#global-options).


---

<!-- === 来源: howto/translate_a_file.md === -->

# Translate a File[](#translate-a-file "Link to this heading")

There are several options for performing file translation. The top-level function [`translate_file()`](../api_reference/fileio/translate_file.md#keysight.pwdatatools._api.funcs.translate_file "keysight.pwdatatools._api.funcs.translate_file") should be able to handle most use cases and all supported file formats. Another option is the [`DataFile.translate()`](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.translate.md#keysight.pwdatatools.DataFile.translate "keysight.pwdatatools.DataFile.translate") method, which is similar to [`translate_file()`](../api_reference/fileio/translate_file.md#keysight.pwdatatools._api.funcs.translate_file "keysight.pwdatatools._api.funcs.translate_file"). Alternatively, you can perform translation as a two-step process: 1) read a file as a [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group"), and 2) write the [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") to a new file. This approach may be helpful in diagnosing and correcting issues during input or output of datafiles, and also allows for modification before writing out the final datafile. For example, you can add or remove variables or metadata.

See also

[File Extensions and Formats](../core_concepts/file_exts_and_formats.md#file-exts-and-formats), [Read a File](read_a_file.md#read-a-file), and [Write a File](write_a_file.md#write-a-file).

Click on any of the below functions or methods to jump to their documentation:

* [`translate_file()`](../api_reference/fileio/translate_file.md#keysight.pwdatatools._api.funcs.translate_file "keysight.pwdatatools._api.funcs.translate_file")
* [`DataFile.translate()`](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.translate.md#keysight.pwdatatools.DataFile.translate "keysight.pwdatatools.DataFile.translate")


---

<!-- === 来源: howto/use_block_class.md === -->

# Use the Block Class[](#use-the-block-class "Link to this heading")

The [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") is one of the most important and fundamental classes in the `keysight.pwdatatools` library. It primarily behaves as a dict-like object that maps variable names to [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") instances. Each Var in a Block holds the data and metadata for a single dataset variable. The next sections walk through some simple examples that illustrate how to use the [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") class.

See also

For an introduction to hierarchical datasets, and how they relate to Groups and Blocks, see [Universal Data Structures](../index.md#data-structs-section).

## Create a Block[](#create-a-block "Link to this heading")

This section shows how to create a Block from a dict, a pandas DataFrame, or a file.

### From a dict[](#from-a-dict "Link to this heading")

Here we create a dict that maps variable names to data or Vars. If data, it can be any array-like object. The benefit of using Var(s) is that you can define various metadata to be associated with the variable. For demonstration purposes, we use a few different types of objects, including a numpy.ndarray, a pwdatatools.Var, a pandas.Series, and a Python list. Also, we include several different datatypes such as int, float, complex, and bool (str datatypes are also supported, but not shown here).

```
>>> from keysight import pwdatatools as pwdt
>>> import pandas as pd
>>> import numpy as np
>>> z_var = pwdt.Var(
...     data=np.array([4 + 5j, 1 - 2j, 3 + 0.1j, 4 + 0.2j, 0 - 1j, 2 + 7j]),
...     name='Zin',
...     role='impedance.input',
...     unit='Ohm',
... )
>>> variables = {
...     "bias": np.array([1, 1, 1, 2, 2, 2]),
...     "freq": pd.Series([1e9, 1.5e9, 2e9, 1e9, 1.5e9, 2e9]),
...     "Zin": z_var,
...     "passed": [True, False, False, True, False, False],
... }
```

See also

For more information on the [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class, see [Use the Var Class](use_var_class.md#use-var-class).

Next, we make a Block, inputting our dict. Then, we print the our newly-created Block.

```
>>> block = pwdt.Block(variables)
>>> print(block)
Block(
    <'bias', 'freq', 'Zin', 'passed' with 6 observations>,
    name='',
    ivarnames=(),
    attrs={},
)
```

### From a pandas DataFrame[](#from-a-pandas-dataframe "Link to this heading")

You can also instantiate a Block with a pandas DataFrame. The DataFrame’s columns become the variable names.

```
>>> df = pd.DataFrame(variables)
>>> print(df)
   bias          freq       Zin   passed
0     1  1.000000e+09  4.0+5.0j     True
1     1  1.500000e+09  1.0-2.0j    False
2     1  2.000000e+09  3.0+0.1j    False
3     2  1.000000e+09  4.0+0.2j     True
4     2  1.500000e+09  0.0-1.0j    False
5     2  2.000000e+09  2.0+7.0j    False
>>> block_from_df = pwdt.Block(df)
>>> print(block_from_df)
Block(
    <'bias', 'freq', 'Zin', 'passed' with 6 observations>,
    name='',
    ivarnames=(),
    attrs={},
)
```

See also

If you want more control over how a pandas DataFrame is cast as data in a Block, use the [`Block.from_pandas_dataframe()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.from_pandas_dataframe.md#keysight.pwdatatools.Block.from_pandas_dataframe "keysight.pwdatatools.Block.from_pandas_dataframe") method instead.

At first glance, `block_from_df` (which we created from a pandas DataFrame) might appear identical to `block` (created from a dict that included a Var for Zin). However, upon closer examination, we can see that the `Zin` variable in `block_from_df` is missing all the metadata we defined (role and unit), whereas the `Zin` variable in `block` includes it. Below, we use the `[]` operator to access the `Zin` variable in each Block. Later, we will cover more details on variables.

```
>>> block['Zin']
Var(
    <Complex128 data with shape (6,)>,
    name='Zin',
    dims=<empty Dims>,
    role='impedance.input',
    unit='Ohm',
    attrs={},
)
>>> block_from_df['Zin']
Var(
    <Complex128 data with shape (6,)>,
    name='Zin',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
```

### From a file[](#from-a-file "Link to this heading")

You can also instantiate a Block from a file. The file can be any supported datafile format. Usually, the file extension determines the file format. For example, if the file extension is `.pwdt`, then the file is assumed to be a native pwdatatools file. If the file extension is `.ds`, then the file is assumed to be an ADS dataset. The Block class has a [`Block.from_file()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.from_file.md#keysight.pwdatatools.Block.from_file "keysight.pwdatatools.Block.from_file") method that reads the file and returns a Block. The following code reads an ADS dataset and returns a Block. The Block is assigned to the variable `block_from_file`.

```
>>> block_from_file = pwdt.Block.from_file('/data_folder/amplifier_sim.ds')
```

However, the above will not work if the ADS dataset cannot be represented by a single Block. ADS datasets (as well as other datafile formats) are hierarchical in nature and thus may require multiple Blocks to represent the data. In this case, it is better to use the free function [`read_file_as_group()`](../api_reference/fileio/read_file_as_group.md#keysight.pwdatatools._api.funcs.read_file_as_group "keysight.pwdatatools._api.funcs.read_file_as_group"). This function always returns a [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") containing one or more Blocks, and it works for hierarchical datasets.

See also

For more information on reading datafiles, see [Read a File](read_a_file.md#read-a-file). For an introduction to hierarchical datasets, and how they relate to Groups and Blocks, see [Universal Data Structures](../index.md#data-structs-section).

## Understand variables in a Block[](#understand-variables-in-a-block "Link to this heading")

Whenever we view a Block’s repr or print it to the console, we see a summary of the Block. The summary shows the variable names, the number of observations, and some other Block properties which we will cover later. The following code prints the summary of the `block` we created earlier.

```
>>> print(block)
Block(
    <'bias', 'freq', 'Zin', 'passed' with 6 observations>,
    name='',
    ivarnames=(),
    attrs={},
)
```

If a Block has too many variable names to fit on the variables line, that line will be truncated. If we would like to see all variable names, we can use the [`Block.varnames`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.varnames.md#keysight.pwdatatools.Block.varnames "keysight.pwdatatools.Block.varnames") property to get a tuple of all variable names. The following code returns the variable names of the `block` we created earlier. In this case, the line did not need to be truncated.

```
>>> block.varnames
('bias', 'freq', 'Zin', 'passed')
```

Blocks store each variable as an instance of [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var"), which stores the data and metadata for that variable. Variables can be accessed using the `[]` operator on the Block. The following code gets the variable `bias` from the Block.

```
>>> block['bias']
Var(
    <Int64 data with shape (6,)>,
    name='bias',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
```

See also

There are other methods for retrieving variables from a Block. See [`Block.get()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.get.md#keysight.pwdatatools.Block.get "keysight.pwdatatools.Block.get"), [`Block.get_var()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.get_var.md#keysight.pwdatatools.Block.get_var "keysight.pwdatatools.Block.get_var"), [`Block.iter_vars()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.iter_vars.md#keysight.pwdatatools.Block.iter_vars "keysight.pwdatatools.Block.iter_vars"), [`Block.pop()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.pop.md#keysight.pwdatatools.Block.pop "keysight.pwdatatools.Block.pop"), and [`Block.values()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.values.md#keysight.pwdatatools.Block.values "keysight.pwdatatools.Block.values") for more information.

## Mutating variables in a Block[](#mutating-variables-in-a-block "Link to this heading")

Block objects are mutable, meaning they can change state after they are created. This means we can add or remove variables, or change the Block’s metadata. We can also change the data or metadata of any variable in the Block, because the [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class is also mutable. The following sections show how to do this.

We can change the data for one or more variables by using the [`Block.set_data_in_place()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.set_data_in_place.md#keysight.pwdatatools.Block.set_data_in_place "keysight.pwdatatools.Block.set_data_in_place") method. The following code sets the data for the `bias` variable.

```
>>> block.set_data_in_place({'bias': [4, 4, 4, 5, 5, 5]})
```

We can also rename a variable in a Block. The following code renames the `bias` variable to `bias2`. There are two different approaches shown below. The first approach is to directly change the name of the variable by setting the [`Var.name`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.name.md#keysight.pwdatatools.Var.name "keysight.pwdatatools.Var.name") property.

```
>>> block['bias'].name = 'bias2'
```

The next line of code achieves the samee result by using the [`Block.rename_vars_in_place()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.rename_vars_in_place.md#keysight.pwdatatools.Block.rename_vars_in_place "keysight.pwdatatools.Block.rename_vars_in_place") method.

```
>>> block.rename_vars_in_place({'bias': 'bias2'})
```

Both approaches are equivalent in this example, but the second approach has the additional capability of renaming multiple variables at once. After the name of the variable is changed, all Block metadata is updated to reflect the new variable name.

```
>>> block.varnames
('bias2', 'freq', 'Zin', 'passed')
```

We can add data or Vars to a Block using the `[]` operator. The following code adds a new variable to the Block.

```
>>> block['new_var'] = np.array([1, 2, 3, 4, 5, 6])
>>> print(block['new_var'])
Var(
    <Int64 data with shape (6,)>,
    name='new_var',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
```

See also

There are other methods for adding Vars or data to a Block. See [`Block.set_data_in_place()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.set_data_in_place.md#keysight.pwdatatools.Block.set_data_in_place "keysight.pwdatatools.Block.set_data_in_place") and [`Block.set_vars_in_place()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.set_vars_in_place.md#keysight.pwdatatools.Block.set_vars_in_place "keysight.pwdatatools.Block.set_vars_in_place") for more information.

## Observations in a Block[](#observations-in-a-block "Link to this heading")

### What are they?[](#what-are-they "Link to this heading")

Each variable we’ve added to the Block has a length of 6. All variables in a Block must have equal length along axis 0 (the first dimension). So far, all of our variables are 1D, so their overall sizes are also 6. But in the case of multi-dimensional variables, we must make sure the length along axis 0 is also 6 if we want to add it to this Block. The length of the variables along axis 0 in any particular Block can be accessed via the [`Block.count_observations()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.count_observations.md#keysight.pwdatatools.Block.count_observations "keysight.pwdatatools.Block.count_observations") method.

```
>>> block.count_observations()
6
```

Let’s add a multi-dimensional variable to the Block. Here we create a 2D numpy data with shape (6, 2). The length along axis 0 is 6, so it is compatible with the other variables in the Block. We can add it to the Block using the `[]` operator. The numpy ndarray is automatically converted to a Var.

```
>>> portz_2D_data = np.array(
    [[ 1 +  2j,  3 +  4j],
     [ 5 +  6j,  7 +  8j],
     [ 9 + 10j, 11 + 12j],
     [13 + 14j, 15 + 16j],
     [17 + 18j, 19 + 20j],
     [21 + 22j, 23 + 24j]])
>>> block['PortZ'] = portz_2D_data
>>> print(block['PortZ'])
Var(
    <Complex128 data with shape (6, 2)>,
    name='PortZ',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
```

### Filter observations[](#filter-observations "Link to this heading")

A very common operation is filtering observations in a Block. This can be done using the [`Block.drop_observations()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.drop_observations.md#keysight.pwdatatools.Block.drop_observations "keysight.pwdatatools.Block.drop_observations") and [`Block.keep_observations()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.keep_observations.md#keysight.pwdatatools.Block.keep_observations "keysight.pwdatatools.Block.keep_observations") methods. Both methods take boolean array-like input which is used to select observations to keep or drop. The boolean array-like must be 1D and have the same length as the Block’s observations count. The following code drops all observations in the Block except for the first 3 observations.

```
>>> filtered_block = block.drop_observations([False, False, False, True, True, True])
>>> filtered_block.count_observations()
3
```

If we compare the data of the `bias2` Var in the unfiltered and filtered Blocks, we can see that only the first 3 observations remain in the filtered Block.

```
>>> block['bias2'].to_numpy_ndarray()
array([4, 4, 4, 5, 5, 5])
>>> filtered_block['bias2'].to_numpy_ndarray()
array([4, 4, 4])
```

Many times, we want to create the boolean input array by making some comparison against a variable’s values in the Block. Below, we filter the observations to only keep those where `passed` is True.

```
>>> filtered_block = block.keep_observations(block['passed'] == True)
>>> filtered_block.count_observations()
2
>>> block['passed'].to_numpy_ndarray()
array([ True, False, False,  True, False, False])
>>> filtered_block['passed'].to_numpy_ndarray()
array([ True,  True])
```

See also

For more information on filtering observations, see [`Block.drop_observations()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.drop_observations.md#keysight.pwdatatools.Block.drop_observations "keysight.pwdatatools.Block.drop_observations") and [`Block.keep_observations()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.keep_observations.md#keysight.pwdatatools.Block.keep_observations "keysight.pwdatatools.Block.keep_observations").

## Add metadata to a Block[](#add-metadata-to-a-block "Link to this heading")

### Name a Block[](#name-a-block "Link to this heading")

Next, we assign a string `name` to the Block. In general, naming a Block is optional. However, sometimes a name is required (for example, when writing certain types of data files such as ADS datasets).

```
>>> block.name = 'DUT_test_data'
```

### Tag independent variables[](#tag-independent-variables "Link to this heading")

Next, let’s assign some variables as independents (ivars). This is especially important if the Block will later be written to a file. This takes some understanding of the data. For a basic tutorial of multi-dimensional data see [Multi-Dimensional Data](../core_concepts/multi_dimensional_data.md#multidim-data). Note how `bias2` is changing the slowest and it repeats. This is a clue that it is the outermost ivar.

```
>>> block['bias2'].to_numpy_ndarray()
array([4, 4, 4, 5, 5, 5])
```

Note how `freq` also repeats, but changes more quickly. This is likely the innermost ivar.

```
>>> block['freq'].to_numpy_ndarray()
array([1.0e+09, 1.5e+09, 2.0e+09, 1.0e+09, 1.5e+09, 2.0e+09])
```

The rest of the variables have data that seem fairly non-repeating and non-ordered. That means these other variables are likely dependent variables (dvars).

Set the [`Block.ivarnames`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.ivarnames.md#keysight.pwdatatools.Block.ivarnames "keysight.pwdatatools.Block.ivarnames") attribute as an iterable of string variable names (tuple, list, etc.). The ordering of the ivarnames is important. The outermost ivar should be first and the innermost ivar should be last. If there are other ivars, they should be listed in order of their “nesting” a.k.a. “level”. By assigning `bias2` and `freq` as `ivarnames`, all the rest of the variables are automatically assigned as dvars, and will thus appear in the [`Block.dvarnames`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.dvarnames.md#keysight.pwdatatools.Block.dvarnames "keysight.pwdatatools.Block.dvarnames") attribute. Unlike [`Block.ivarnames`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.ivarnames.md#keysight.pwdatatools.Block.ivarnames "keysight.pwdatatools.Block.ivarnames"), the ordering of [`Block.dvarnames`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.dvarnames.md#keysight.pwdatatools.Block.dvarnames "keysight.pwdatatools.Block.dvarnames") is not typically important. However, the [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") class makes every effort to maintain the original dvar ordering during all operations.

```
>>> block.ivarnames = ('bias2', 'freq')
>>> print(f'ivarnames = {block.ivarnames}\ndvarnames = {block.dvarnames}')
ivarnames = ('bias2', 'freq')
dvarnames = ('Zin', 'passed', 'new_var', 'PortZ')
```

Important

The [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") class has another property [`Block.idxnames`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.idxnames.md#keysight.pwdatatools.Block.idxnames "keysight.pwdatatools.Block.idxnames") that defines variables that are meant to be used for indexing along the Block’s observations (along axis 0 of each Var). We will not set the [`Block.idxnames`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.idxnames.md#keysight.pwdatatools.Block.idxnames "keysight.pwdatatools.Block.idxnames") property in this example, but [Load Pull Examples](../examples/loadpull/index.md#load-pull-examples) illustrate its use. The [`LoadPullBlock`](../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") class uses the [`Block.idxnames`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.idxnames.md#keysight.pwdatatools.Block.idxnames "keysight.pwdatatools.Block.idxnames") property and index variables extensively. In [`LoadPullBlock`](../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock"), the idxs are integer indexes that correspond to the ivars.

### Add arbitrary attributes[](#add-arbitrary-attributes "Link to this heading")

Arbitrary metadata may be stored in the [`Block.attrs`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs") property. The [`Block.attrs`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs") property stores an instance of [`AttrsDict`](../api_reference/metadata/attrsdict/index.md#keysight.pwdatatools.AttrsDict "keysight.pwdatatools.AttrsDict"), which behaves like a type-restricted dict. It’s up to you what kind of arbitrary attributes you want to store. The only requirement is that they must be HDF5-serializable. This means that the attributes must be one of the following types: float, complex, int, str, bool, None, list, dict, numpy.ndarray, or a combination of these types. The attributes may be nested to any depth (nested lists, dicts, etc. are supported). Here are just a few examples of useful information that may be stored in [`Block.attrs`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs"):

* constant values; for example, temperature or reference impedance
* simulation settings or measurement info; for example, calibration info, name of the engineeer that made the measurement, the date the data was collected, etc.
* comments

Saving constant values as metadata instead of as variables helps save memory because we avoid repeating constant values over every observation. Constants may be one of the following types: float, complex, int, str, bool, and None. Below, we add some constants to the [`Block.attrs`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs") property using the `[]` operator, just like a regular dict.

```
>>> block.attrs['sample'] = 'batch1'
>>> block.attrs['temperature'] = 150
>>> block.attrs['Zref'] = 3+4j
```

Comments can be also stored in [`Block.attrs`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs"). They can be stored as a list of strings, or a numpy.ndarray of strings, or as a single string with optional newline characters. There is no special reserved key for comments, so the using the key `'comments'` here is completely arbitrary.

```
>>> block.attrs['comments'] = [
...    'This was collected by Mike for customer A.',
...    'This was an outlier.',
...    'The product was delivered on June 15th.'
... ]
```

Arbitrary attributes to be associated with any particular variable may be stored in each [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") object. In contrast, the attributes stored in [`Block.attrs`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs") are associated with the entire [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"). Here we add a few attributes to the `bias` variable.

```
>>> block['bias2'].attrs = {'port': 2, 'type': 'dc'}
>>> print(block['bias2'])
Var(
    <Int64 data with shape (6,)>,
    name='bias2',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={'port': ..., 'type': ...},
)
```

It’s not covered here, but there are other types of metadata that can be stored in the [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") object. Examples are dims, role, and unit. See [Use the Var Class](use_var_class.md#use-var-class) for more information.

## View a Block’s summary and info[](#view-a-block-s-summary-and-info "Link to this heading")

The Block summary can be viewed in the console by printing it or viewing its repr.

```
>>> print(block)
Block(
    <'Zin', 'passed', 'new_var', 'PortZ' with 6 observations>,
    name='DUT_test_data',
    ivarnames=('bias2', 'freq'),
    attrs={'sample': ..., 'temperature': ..., 'Zref': ..., 'comments': ...},
)
```

Another option is to use the [`Block.info()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.info.md#keysight.pwdatatools.Block.info "keysight.pwdatatools.Block.info") method, which returns a DataFrame containing information about the variables.

```
>>> print(block.info())
           bias2       freq              Zin   passed new_var       PortZ
kind        dvar       dvar             dvar     dvar    dvar        dvar
role           -          -  impedance.input        -       -           -
dtype      Int32    Float64       Complex128  Boolean   Int32  Complex128
shape       (6,)       (6,)             (6,)     (6,)    (6,)      (6, 2)
dims           -          -                -        -       -           -
unit           -          -              Ohm        -       -           -
min            4  1.000e+09            1.000        -       1       2.236
max            5  2.000e+09            7.280        -       6      33.242
null           -          -                -        -       -           -
nan            -          -                -        -       -           -
attrs  <2 attrs>          -                -        -       -           -
```

## Create a pandas DataFrame from a Block[](#create-a-pandas-dataframe-from-a-block "Link to this heading")

The `pandas` library is a very popular library for data analysis. The main data structure in pandas is the DataFrame. The Block class has a [`Block.to_pandas_dataframe()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.to_pandas_dataframe.md#keysight.pwdatatools.Block.to_pandas_dataframe "keysight.pwdatatools.Block.to_pandas_dataframe") method that returns a pandas DataFrame containing all the data in the Block. This allows you to take full advantage of all the pandas.DataFrame methods for data analysis and manipulation.

Let’s create a pandas DataFrame from our Block.

```
>>> df = block.to_pandas_dataframe()
>>> print(df)
   bias2          freq       Zin   passed  new_var    PortZ[1]    PortZ[2]
0      4  1.000000e+09  4.0+5.0j     True        1  1.00+2.00j  3.00+4.00j
1      4  1.500000e+09  1.0-2.0j    False        2  5.00+6.00j  7.00+8.00j
2      4  2.000000e+09  3.0+0.1j    False        3   9.0+10.0j  11.0+12.0j
3      5  1.000000e+09  4.0+0.2j     True        4  13.0+14.0j  15.0+16.0j
4      5  1.500000e+09  0.0-1.0j    False        5  17.0+18.0j  19.0+20.0j
5      5  2.000000e+09  2.0+7.0j    False        6  21.0+22.0j  23.0+24.0j
```

The Block’s observations become the DataFrame’s rows. The Block’s variable names become the DataFrame’s columns. By default, the DataFrame’s row index is a default pandas.RangeIndex. However, we can use the Block’s ivars as the row index instead. Since there are two ivars in our Block (`bias2` and `freq`), the resulting DataFrame has a rows MultiIndex with two levels.

```
>>> df = block.to_pandas_dataframe(index='ivars')
>>> print(df)
                         Zin   passed  new_var    PortZ[1]    PortZ[2]
bias2 freq
4     1.000000e+09  4.0+5.0j     True        1  1.00+2.00j  3.00+4.00j
      1.500000e+09  1.0-2.0j    False        2  5.00+6.00j  7.00+8.00j
      2.000000e+09  3.0+0.1j    False        3   9.0+10.0j  11.0+12.0j
5     1.000000e+09  4.0+0.2j     True        4  13.0+14.0j  15.0+16.0j
      1.500000e+09  0.0-1.0j    False        5  17.0+18.0j  19.0+20.0j
      2.000000e+09  2.0+7.0j    False        6  21.0+22.0j  23.0+24.0j
```

See also

For more information on why creating a MultiIndex for the rows of a DataFrame might be useful, see [Multi-Dimensional Data](../core_concepts/multi_dimensional_data.md#multidim-data).

Note that our 2D variable `PortZ` was automatically converted into two 1D columns `PortZ[1]` and `PortZ[2]`. The default behavior is to embed one-based integers into the column names for multi-dimensional variables. This maximizes compatiblity with other tools like ADS, which require one-based integer indexing for vectors and matrices. However, there are other options for how to handle the dimension scales of multi-dimensional variables. See [Multi-Dimensional Data](../core_concepts/multi_dimensional_data.md#multidim-data) for more information.

We can also create a MultiIndex for the columns of the DataFrame. Below, we set `cols_nlevels=-1`, which means that the MultiIndex will contain the minimum number of levels needed to represent all the multi-dimensional variables in the Block. Below, we are creating a MultiIndex for not only the columns, but also the rows (using the ivars).

```
>>> df = block.to_pandas_dataframe(index='ivars', cols_nlevels=-1)
>>> print(df)
varname                  Zin   passed   new_var       PortZ
i                                                         1           2
bias2 freq
4     1.000000e+09  4.0+5.0j     True         1  1.00+2.00j  3.00+4.00j
      1.500000e+09  1.0-2.0j    False         2  5.00+6.00j  7.00+8.00j
      2.000000e+09  3.0+0.1j    False         3   9.0+10.0j  11.0+12.0j
5     1.000000e+09  4.0+0.2j     True         4  13.0+14.0j  15.0+16.0j
      1.500000e+09  0.0-1.0j    False         5  17.0+18.0j  19.0+20.0j
      2.000000e+09  2.0+7.0j    False         6  21.0+22.0j  23.0+24.0j
```

See also

For more information on why creating a MultiIndex for the columns of a DataFrame might be useful, see [Multi-Dimensional Data](../core_concepts/multi_dimensional_data.md#multidim-data).

## Plot data in a Block[](#plot-data-in-a-block "Link to this heading")

Because the [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") and [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") classes implement the necessary interfaces, they can be directly used in many plotting libraries. For example, the `matplotlib` and `seaborn` libraries can plot data from Blocks and Vars. The following code plots the `new_var` variable from our Block.

```
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> ax = sns.lineplot(data=block, x='freq', y='new_var', hue='bias2', palette='tab10')
>>> ax.set_title('Simple Demo of Plotting Data from a Block')
>>> plt.show()
```

[![Simple Demo of Plotting Data from a Block](../_images/block_plot.png)](../_images/block_plot.png)

## Write a Block to a file[](#write-a-block-to-a-file "Link to this heading")

The Block class has a [`Block.to_file()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.to_file.md#keysight.pwdatatools.Block.to_file "keysight.pwdatatools.Block.to_file") method that writes the Block to any supported datafile format. Usually, the file extension determines the file format.

```
>>> block.to_file('/data_folder/myblock.ds')  # write to an ADS dataset
>>> block.to_file('/data_folder/myblock.pwdt') # write to a native pwdatatools file
```

Some datafile formats do a better job at storing metadata than others. For example, the native pwdt HDF5-based format stores all of the Var and Block metadata. However, the ADS dataset format does not store much other than the variable names, the ivarnames, and the data.

We can also combine our Block with other Blocks before writing to a file. This only works for datafile formats that support hierarchy such as ADS datasets, pwdt HDF5 files, and generic MDIFs (and others). The following code creates another simple Block and then groups our `block` together with this new Block called `block2`. The resulting [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") is then written to file.

```
>>> block2 = pwdt.Block({'x': np.array([1, 2, 3, 4, 5, 6])}, name='foo') # instantiate with a Block name
>>> group = pwdt.Group([block, block2])
>>> group.to_file('/data_folder/combined_results.ds')  # write both Blocks to a single ADS dataset
```

See also

For more information on writing datafiles, see [Write a File](write_a_file.md#write-a-file).


---

<!-- === 来源: howto/use_group_class.md === -->

# Use the Group Class[](#use-the-group-class "Link to this heading")

A [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") is essentially a collection of child objects. These children are also referred to as members. A Group’s members can include instances of [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"), as well as other instances of [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group"). Thus, the [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") class is the key enabler to representing hierarchical datasets in the `keysight.pwdatatools` library. This section walks through how to use the [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") class. It builds off the previous section, [Use the Block Class](use_block_class.md#use-block-class).

See also

If you aren’t sure what hierarchical datasets are, or how they relate to Groups and Blocks, see [Universal Data Structures](../index.md#data-structs-section).

## Create a Group[](#create-a-group "Link to this heading")

There are two main ways to create a [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") instance. The first is to instantiate a Group directly, using the [`Group.__init__()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__init__.md#keysight.pwdatatools.Group.__init__ "keysight.pwdatatools.Group.__init__") method. The second is to read a file into a Group using the [`Group.from_file()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.from_file.md#keysight.pwdatatools.Group.from_file "keysight.pwdatatools.Group.from_file") method. We’ll cover both of these instantiation methods.

### Direct instantiation[](#direct-instantiation "Link to this heading")

Let’s instantiate a [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") with a list of members, a name, and an arbitrary attribute (the date). Below, we first create two simple [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") instances, then we instantiate the Group.

```
>>> import keysight.pwdatatools as pwdt
>>> block1 = pwdt.Block({'freq': [1e9, 2e9], 'Pout': [10.0, 12.5]}, name='power_meas')
>>> block2 = pwdt.Block({'freq': [1e9, 2e9], 'Pout': [10.2, 12.3]}, name='power_sim')
>>> group = pwdt.Group([block1, block2], name='power_meas_and_sim', attrs={'date': '2020-10-01'})
>>> group
Group(
    <2 Blocks>,
    name='power_meas_and_sim',
    attrs={'date': ...},
)
```

Our dict with the date was converted to an [`AttrsDict`](../api_reference/metadata/attrsdict/index.md#keysight.pwdatatools.AttrsDict "keysight.pwdatatools.AttrsDict") object and stored in the [`Group.attrs`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.attrs.md#keysight.pwdatatools.Group.attrs "keysight.pwdatatools.Group.attrs") attribute. This is the same type of object that is used for the [`Block.attrs`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs") attribute. The [`AttrsDict`](../api_reference/metadata/attrsdict/index.md#keysight.pwdatatools.AttrsDict "keysight.pwdatatools.AttrsDict") class behaves like a type-restricted dict.

### From a file[](#from-a-file "Link to this heading")

Below, we create a Group by reading a Touchstone file. First, we write the Touchstone file using one of the functions available in the `keysight.pwdatatools.examples.touchstone` module. Then, we read the file into a Group using the [`Group.from_file()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.from_file.md#keysight.pwdatatools.Group.from_file "keysight.pwdatatools.Group.from_file") method.

```
>>> from pathlib import Path
>>> from keysight.pwdatatools.examples import touchstone
>>> folder = Path(".")
>>> filepath = touchstone.write_ads_example_version1_with_noise_data_s2p(folder)
>>> group_from_s2p = pwdt.Group.from_file(filepath)
>>> group_from_s2p
Group(
    <2 Blocks>,
    name='ads_example_version1_with_noise_data',
    attrs={},
)
```

The [`Group.from_file()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.from_file.md#keysight.pwdatatools.Group.from_file "keysight.pwdatatools.Group.from_file") method is a class method, so it can be called directly from the [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") class. Alternatively, you can use the free function [`read_file_as_group()`](../api_reference/fileio/read_file_as_group.md#keysight.pwdatatools._api.funcs.read_file_as_group "keysight.pwdatatools._api.funcs.read_file_as_group") to read a file into a Group.

See also

The [Read a File](read_a_file.md#read-a-file) section has more information on reading datafiles.

## Retrieve a member[](#retrieve-a-member "Link to this heading")

In order to access members in a Group, it’s possible to use the `[]` operator to perform list-like indexing and slicing, as well as dict-like lookups by member name. However, it is recommended instead to use the [`Group.get_member_as_block()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.get_member_as_block.md#keysight.pwdatatools.Group.get_member_as_block "keysight.pwdatatools.Group.get_member_as_block") and [`Group.get_member_as_group()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.get_member_as_group.md#keysight.pwdatatools.Group.get_member_as_group "keysight.pwdatatools.Group.get_member_as_group") methods. Both of these methods are able to retrieve members by integer index or by name, plus they have the following additional benefits over using list-like indexing (which invokes the [`Group.__getitem__()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__getitem__.md#keysight.pwdatatools.Group.__getitem__ "keysight.pwdatatools.Group.__getitem__") method):

* their return types are more specific. This means that IDEs and type checkers can be more helpful.
* they can cast members to the desired type. For example, if you request a member as a [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group"), but it is actually a [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"), the [`Group.get_member_as_group()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.get_member_as_group.md#keysight.pwdatatools.Group.get_member_as_group "keysight.pwdatatools.Group.get_member_as_group") method can optionally cast it to a [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") for you.

Below, we demonstrate how to use the [`Group.get_member_as_block()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.get_member_as_block.md#keysight.pwdatatools.Group.get_member_as_block "keysight.pwdatatools.Group.get_member_as_block") with integer index and name lookup.

```
>>> block0 = group.get_member_as_block(0) # get the first member as a Block
>>> print(block0.name)
power_meas
>>> block1 = group.get_member_as_block(1) # get the second member as a Block
>>> print(block1.name)
power_sim
>>> block_meas = group.get_member_as_block('power_meas') # get Block by name
>>> print(block_meas.name)
power_meas
>>> block_sim = group.get_member_as_block('power_sim') # get Block by name
>>> print(block_sim.name)
power_sim
```

## Iterate over members[](#iterate-over-members "Link to this heading")

It is possible to iterate over the members of a Group using a for-loop.

```
>>> for member in group:
...     print(member.name)
power_meas
power_sim
```

A for-loop does *not* recursively iterate over the members of any child Groups. To recursively iterate, use the [`Group.iter_members()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.iter_members.md#keysight.pwdatatools.Group.iter_members "keysight.pwdatatools.Group.iter_members") method with `recursive=True`. Let’s create a child Group, add it to our Group, and recursively iterate.

```
>>> child_group = pwdt.Group([pwdt.Block(name='grandchild_block')], name='child_group')
>>> group += child_group  # have not covered adding members yet, but this is one way
>>> group
Group(
    <2 Blocks and 1 Group>,
    name='power_meas_and_sim',
    attrs={'date': ...},
)
>>> for member in group.iter_members(recursive=True):
...     print(member.name)
power_meas
power_sim
child_group
grandchild_block
```

It is also possible to iterate over only the Blocks in a Group using the [`Group.iter_blocks()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.iter_blocks.md#keysight.pwdatatools.Group.iter_blocks "keysight.pwdatatools.Group.iter_blocks") method. This method also accepts the `recursive` argument. Note how `child_group` is not yielded during iteration, but `grandchild_block`, which is contained in `child_group`, is yielded.

```
>>> for block in group.iter_blocks(recursive=True):
...     print(block.name)
power_meas
power_sim
grandchild_block
```

It can be very useful to iterate over only the Block(s) with certain variable name(s) of interest. For example, if you have a Group with many Blocks, and you want to iterate over only the Blocks that have a `'freq'` variable, you can use the below pattern.

```
>>> for block in group.iter_blocks(recursive=True):
...     if 'freq' in block:
...         print(block.name)
...
power_meas
power_sim
```

## Add members[](#add-members "Link to this heading")

There are several ways to add members to a Group.

* the `+=` operator
* the [`Group.append()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.append.md#keysight.pwdatatools.Group.append "keysight.pwdatatools.Group.append") method
* the [`Group.extend()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.extend.md#keysight.pwdatatools.Group.extend "keysight.pwdatatools.Group.extend") method
* the [`Group.insert()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.insert.md#keysight.pwdatatools.Group.insert "keysight.pwdatatools.Group.insert") method

The `+=` operator is the most concise way to add a single member to a Group. It is equivalent to calling the [`Group.append()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.append.md#keysight.pwdatatools.Group.append "keysight.pwdatatools.Group.append") method. If we view the [`Group.members`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") attribute, we can see that the new Block is added to the end of the list of members.

```
>>> group += pwdt.Block(name='block3')
>>> group.members
MemberList(
    [
        <Block 'power_meas' with 2 Vars and 2 observations>,
        <Block 'power_sim' with 2 Vars and 2 observations>,
        <Group 'child_group' with 1 Block>,
        <Block 'block3' with 0 Vars and -1 observations>,
    ]
)
```

The [`Group.extend()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.extend.md#keysight.pwdatatools.Group.extend "keysight.pwdatatools.Group.extend") method is the most straightforward way to add multiple members. It is equivalent to calling the [`Group.append()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.append.md#keysight.pwdatatools.Group.append "keysight.pwdatatools.Group.append") method for each member in the list.

```
>>> list_of_blocks = [pwdt.Block(name='block4'), pwdt.Block(name='block5')]
>>> group.extend(list_of_blocks)
>>> group.members
MemberList(
    [
        <Block 'power_meas' with 2 Vars and 2 observations>,
        <Block 'power_sim' with 2 Vars and 2 observations>,
        <Group 'child_group' with 1 Block>,
        <Block 'block3' with 0 Vars and -1 observations>,
        <Block 'block4' with 0 Vars and -1 observations>,
        <Block 'block5' with 0 Vars and -1 observations>,
    ]
)
```

The [`Group.insert()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.insert.md#keysight.pwdatatools.Group.insert "keysight.pwdatatools.Group.insert") method is the best way to insert a single member into a Group at a specific index.

```
>>> group.insert(0, pwdt.Block(name='block0'))
>>> group.members
MemberList(
    [
        <Block 'block0' with 0 Vars and -1 observations>,
        <Block 'power_meas' with 2 Vars and 2 observations>,
        <Block 'power_sim' with 2 Vars and 2 observations>,
        <Group 'child_group' with 1 Block>,
        <Block 'block3' with 0 Vars and -1 observations>,
        <Block 'block4' with 0 Vars and -1 observations>,
        <Block 'block5' with 0 Vars and -1 observations>,
    ]
)
```

## Remove members[](#remove-members "Link to this heading")

There are several ways to remove members from a Group.

* the [`Group.remove()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.remove.md#keysight.pwdatatools.Group.remove "keysight.pwdatatools.Group.remove") method
* the [`Group.pop()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.pop.md#keysight.pwdatatools.Group.pop "keysight.pwdatatools.Group.pop") method
* the [`Group.clear()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.clear.md#keysight.pwdatatools.Group.clear "keysight.pwdatatools.Group.clear") method

The [`Group.remove()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.remove.md#keysight.pwdatatools.Group.remove "keysight.pwdatatools.Group.remove") method can be called with either an integer index or a member name.

```
>>> group.remove(0)  # remove the first member
```

The [`Group.pop()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.pop.md#keysight.pwdatatools.Group.pop "keysight.pwdatatools.Group.pop") method is very similar to [`Group.remove()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.remove.md#keysight.pwdatatools.Group.remove "keysight.pwdatatools.Group.remove"), except that [`Group.pop()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.pop.md#keysight.pwdatatools.Group.pop "keysight.pwdatatools.Group.pop") also returns the removed member. Also, a more subtle difference is that [`Group.pop()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.pop.md#keysight.pwdatatools.Group.pop "keysight.pwdatatools.Group.pop") defaults to removing the last member, whereas [`Group.remove()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.remove.md#keysight.pwdatatools.Group.remove "keysight.pwdatatools.Group.remove") does not have a default index. This is because [`Group.pop()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.pop.md#keysight.pwdatatools.Group.pop "keysight.pwdatatools.Group.pop") is modeled after the built-in `list.pop()` method, which also defaults to removing the last item.

```
>>> block = group.pop()  # by default, the last member is removed and returned
>>> block
Block(
    <no dvars>,
    name='block5',
    ivarnames=(),
    attrs={},
)
>>> group.members
MemberList(
    [
        <Block 'power_meas' with 2 Vars and 2 observations>,
        <Block 'power_sim' with 2 Vars and 2 observations>,
        <Group 'child_group' with 1 Block>,
        <Block 'block3' with 0 Vars and -1 observations>,
        <Block 'block4' with 0 Vars and -1 observations>,
    ]
)
```

## View summaries of the members[](#view-summaries-of-the-members "Link to this heading")

THere are two main ways to view summaries of the members of a Group.

* the [`Group.members`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") attribute
* the [`Group.tree()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.tree.md#keysight.pwdatatools.Group.tree "keysight.pwdatatools.Group.tree") method

Note

The [`Group.members`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") attribute was previously introduced, but this section gives more details.

The [`Group.members`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") stores a `MembersList` object, which is a type-restricted list of [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") and [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") instances. This object works just like a regular Python list. If you view the [`Group.members`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") attribute, you will see one-line summaries of each Group and Block, which can be useful because it shows some details about the members while still being concise.

```
>>> group.members
MemberList(
    [
        <Block 'power_meas' with 2 Vars and 2 observations>,
        <Block 'power_sim' with 2 Vars and 2 observations>,
        <Group 'child_group' with 1 Block>,
        <Block 'block3' with 0 Vars and -1 observations>,
        <Block 'block4' with 0 Vars and -1 observations>,
    ]
)
```

Note

The `-1 observations` in some of the Blocks means that the number of observations is not set yet. This is because some Blocks were created without variables. The number of observations is set when the first variable is added to a Block.

Another method that can be used to help understand the hierarchy of a Group is [`Group.tree()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.tree.md#keysight.pwdatatools.Group.tree "keysight.pwdatatools.Group.tree"). This method prints a tree-like representation of the Group and its members. This has the added benefit of expanding child Groups recursively, showing summaries of their members.

```
>>> print(group.tree())
<Group 'power_meas_and_sim'>
├── <Block 'power_meas' with 2 Vars and 2 observations>
├── <Block 'power_sim' with 2 Vars and 2 observations>
├── <Group 'child_group'>
│   └── <Block 'grandchild_block' with 0 Vars and -1 observations>
├── <Block 'block3' with 0 Vars and -1 observations>
└── <Block 'block4' with 0 Vars and -1 observations>
```

## Write to a file[](#write-to-a-file "Link to this heading")

The [`Group.to_file()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.to_file.md#keysight.pwdatatools.Group.to_file "keysight.pwdatatools.Group.to_file") method can be used to write a Group to a file. This method is equivalent to passing a Group into the top-level function [`write_file()`](../api_reference/fileio/write_file.md#keysight.pwdatatools._api.funcs.write_file "keysight.pwdatatools._api.funcs.write_file"). Typically, the datafile format is inferred from the file extension. Below, we write out the Group to a .pwdt file, an MDIF file, and an ADS dataset file.

```
>>> group.to_file('/datafolder/meas_and_sim_data.pwdt') # .pwdt file format can directly handle this 2-level hierarchy
>>> group.to_file('/datafolder/meas_and_sim_data.mdif') # 2nd level of hierarchy gets flattened using default naming scheme
>>> group.to_file('/datafolder/meas_and_sim_data.ds') # 2nd level of hierarchy gets flattened using default naming scheme
```

Not all file formats are able to handle hierarchical datasets. Furthermore, most hierarchical file formats (except for HDF5) can only handle one level of hierarchy. However, when writing a file from a Group that contains child Groups, those additional levels of hierarchy are automatically flattened if the datafile format can handle only one level (for example, ADS datasets and generic MDIF files). This is done by flattening the child Groups and representing those parent-child relationships via hierarchical names. For more control over how this flattening is done, you can use the [`Group.flatten()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.flatten.md#keysight.pwdatatools.Group.flatten "keysight.pwdatatools.Group.flatten") method to flatten the hierarchy yourself before writing to a file. However, the effects of the [`Group.flatten()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.flatten.md#keysight.pwdatatools.Group.flatten "keysight.pwdatatools.Group.flatten") method are not reversible. There is a context manager version of [`Group.flatten()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.flatten.md#keysight.pwdatatools.Group.flatten "keysight.pwdatatools.Group.flatten") called [`Group.flattened()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.flattened.md#keysight.pwdatatools.Group.flattened "keysight.pwdatatools.Group.flattened"), which can be used to temporarily flatten a Group for specific operation(s). Below, we use the [`Group.flattened()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.flattened.md#keysight.pwdatatools.Group.flattened "keysight.pwdatatools.Group.flattened") method to temporarily flatten the Group before writing to an MDIF file and printing the tree.

```
>>> # using a non-default sep; the default is '.'
>>> with group.flattened(sep=':'):
...     group.to_file('/datafolder/meas_and_sim_data.mdif')
...     (print(group.tree())
<Group 'power_meas_and_sim'>
├── <Block 'power_meas' with 2 Vars and 2 observations>
├── <Block 'power_sim' with 2 Vars and 2 observations>
├── <Block 'child_group:grandchild_block' with 0 Vars and -1 observations>
├── <Block 'block3' with 0 Vars and -1 observations>
└── <Block 'block4' with 0 Vars and -1 observations>
```

Note how the `grandchild_block` is now named `child_group:grandchild_block`, which uses a non-default parameter setting `sep=':'`. The `child_group` was flattened into the parent Group, and the parent-child relationship is now represented via the hierarchical name. This extra step to explicitly flatten the Group is not necessary unless you want to use some non-default settings for hierarchical membernames, as we are doing here with the non-default `sep`. If want to use all the default hierarchical membername settings (which include not only `sep` but also a parameter that controls behavior related to empty membernames), you can just call [`Group.to_file()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.to_file.md#keysight.pwdatatools.Group.to_file "keysight.pwdatatools.Group.to_file") directly and it will automatically flatten the Group for you when writing to MDIF, ADS dataset, etc. However, the hierarchy will remain intact when writing to the native .pwdt format.

Now if we call the [`Group.tree()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.tree.md#keysight.pwdatatools.Group.tree "keysight.pwdatatools.Group.tree") method again outside of the context manager code block, we can see that the Group’s hierarchy has been restored.

```
>>> print(group.tree())
<Group 'power_meas_and_sim'>
├── <Block 'power_meas' with 2 Vars and 2 observations>
├── <Block 'power_sim' with 2 Vars and 2 observations>
├── <Group 'child_group'>
│   └── <Block 'grandchild_block' with 0 Vars and -1 observations>
├── <Block 'block3' with 0 Vars and -1 observations>
└── <Block 'block4' with 0 Vars and -1 observations>
```

Note

The default hierarchical name delimiter parameter `sep` defaults to `'.'` because that value works well for ADS datasets and generic MDIF files.

See also

The [Write a File](write_a_file.md#write-a-file) section has more information on writing datafiles.


---

<!-- === 来源: howto/use_new_version.md === -->

# Use the New Data Tools Version[](#use-the-new-data-tools-version "Link to this heading")

The Data Tools API has been in development for a while now, and it has gone through a few iterations. With the release of version 0.8.0, the API is now nearing the point where we can consider it stable. Once it is considered stable, we will signify that by changing the version number to 1.0.0. Until then, we will continue to use the 0.x.x versioning scheme. The API is now stable enough that we will try to avoid making breaking changes. However, we may still make breaking changes if we feel it is necessary to improve the API. If we do make breaking changes, we will try to make the transition as painless as possible by deprecating features before removing them and by providing migration guides like this one.

If it is important to you to head off any potential compatibility problems with future versions of any libraies you are using (not just pwdatatools), it is recommended to periodically run your scripts with the -Wd flag in order to show all deprecation warnings. You can also use Python’s standard warnings module to suppress the warnings or to raise an exception when a deprecation warning is issued.

```
python -Wd my_script.py
```

## Migrating to version 0.11.0 or later[](#migrating-to-version-0-11-0-or-later "Link to this heading")

One of the biggest changes in version 0.11.0 is that the `Var.data` attribute was deprecated. Previously, it gave access to the Var’s underlying data as a numpy ndarray. However, this design was problematic because it allowed the data arrays to be mutated, necessitating many defensive copies of the data. Starting with version 0.11.0, the `Var.data` attribute creates a copy of the data array and also raises a DeprecationWarning. The recommended way to access a Var’s data moving forward is by using [`Var.to_numpy_ndarray()`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_numpy_ndarray.md#keysight.pwdatatools.Var.to_numpy_ndarray "keysight.pwdatatools.Var.to_numpy_ndarray"), [`Var.to_numpy_maskedarray()`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_numpy_maskedarray.md#keysight.pwdatatools.Var.to_numpy_maskedarray "keysight.pwdatatools.Var.to_numpy_maskedarray"), [`Var.to_pandas_series()`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_pandas_series.md#keysight.pwdatatools.Var.to_pandas_series "keysight.pwdatatools.Var.to_pandas_series"), or [`Var.to_pandas_dataframe()`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_pandas_dataframe.md#keysight.pwdatatools.Var.to_pandas_dataframe "keysight.pwdatatools.Var.to_pandas_dataframe"). These methods return a copy of the data in the desired format. Eventually, the `Var.data` attribute will be removed, so it is recommended to update your scripts to use the new methods.

## Migrating to version 0.8.0 or later[](#migrating-to-version-0-8-0-or-later "Link to this heading")

If you have been using Data Tools version 0.7.0 or previous and would like to migrate to the new version, this section will help you do that. The new version has a lot of new features and improvements, but it also has some breaking changes. This section is meant to guide you through how to make the necessary changes to your scripts.

See also

[Get the Data Tools Version](get_the_version.md#get-the-version)

The biggest changes are in the [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") class. The Block class no longer stores a pandas DataFrame in a `Block.data` attribute (this attribute no longer exists). The Block stores its variables as instances of the [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class. But, you can still instantiate a Block with a DataFrame, just like before.

```
from keysight.pwdatatools import Block
import pandas as pd

>>> df = pd.DataFrame({'freq': [1, 2, 3], 's11': [1, 2, 3]})
>>> block = Block(df)
```

You can also create a Block from a pandas DataFrame using the new [`Block.from_pandas_dataframe()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.from_pandas_dataframe.md#keysight.pwdatatools.Block.from_pandas_dataframe "keysight.pwdatatools.Block.from_pandas_dataframe") method, which gives you more control over how the DataFrame is cast to Var instances within the Block.

```
>>> block = Block.from_pandas_dataframe(df)
```

If you want to represent a Block as a pandas DataFrame, you can use the [`Block.to_pandas_dataframe()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.to_pandas_dataframe.md#keysight.pwdatatools.Block.to_pandas_dataframe "keysight.pwdatatools.Block.to_pandas_dataframe") method.

```
>>> df = block.to_pandas_dataframe()
```

There are a bunch of new things to learn with respect to working with the new Var class. We won’t cover it here, but you can refer to [Use the Var Class](use_var_class.md#use-var-class) for more information.

### Making your scripts compatible with both versions[](#making-your-scripts-compatible-with-both-versions "Link to this heading")

If you would like to make a script that works for both pre-0.8.0 and post-0.8.0 versions of Data Tools, you can follow the recipes below.

One way to accomplish this is by checking for the presence of a `Block.data` attribute. If it exists, then you are using the old version of Data Tools. If it does not exist, then you are using the new version.

```
from keysight.pwdatatools import Block

>>> data_input = {'x': [1, 2, 3], 'y': [1, 2, 3]}
>>> block = Block(data_input)
>>> if hasattr(block, 'data'):
...     df = block.data
... else:
...     df = block.to_pandas_dataframe()
```

Another way to check for the presence of the `Block.data` attribute is to use a try-except pattern.

```
from keysight.pwdatatools import Block

>>> data_input = {'x': [1, 2, 3], 'y': [1, 2, 3]}
>>> block = Block(data_input)
>>> try:
...     df = block.data
... except AttributeError:
...     df = block.to_pandas_dataframe()
```

If you are using the new version of Data Tools, make sure you always convert it back to a new Block at the end if you make any modifications to the DataFrame.

```
>>> if hasattr(block, 'data'):
>>>     using_old_version = True
...     df = block.data
... else:
...     using_old_version = False
...     df = block.to_pandas_dataframe()
... # do some stuff with the DataFrame
... if not using_old_version:
>>>     block = pwdt.Block.from_pandas_dataframe(df)
```

Instead of checking for the data attribute, you can check the pwdatatools version.

```
>>> version = pwdt.version()
>>> version_split = version.split('.')
>>> major_version = int(version_split[0])
>>> minor_version = int(version_split[1])
>>> if major_version < 1 and minor_version >= 8:
...     df = block.to_pandas_dataframe()
...     # do some stuff with the DataFrame
...     block = Block.from_pandas_dataframe(df)
>>> else:
...     df = block.data
...     # do some stuff with the DataFrame
```

See also

See the [Changelog](../changelog.md#changelog) for more information.

## Migrating to version 0.3.0 or later[](#migrating-to-version-0-3-0-or-later "Link to this heading")

If you have been using Data Tools version 0.2.1 or previous, then you will notice some significant changes to the API. Some of these are breaking changes (sorry about that!), which will require you to make some changes to your scripts. This section of the docs is meant to guide you through how to do that as painlessly as possible.

See also

[Get the Data Tools Version](get_the_version.md#get-the-version)

### Import PathWave Data Tools[](#import-pathwave-data-tools "Link to this heading")

The Data Tools library was made into a “namespace package” under the “keysight” namespace. This affects the way you import Data Tools at the top of your scripts. Previously, you did this: `import pwdatatools as pwdt`. Now, you import like this: `from keysight import pwdatatools as pwdt`.

### Group and Block[](#group-and-block "Link to this heading")

The two main classes that store datasets have new names. These were previously called `DataStore` and `DataBlock`. Now, these same roles are fulfilled by the [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") and [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") classes. So, wherever you were using DataStore, change that to Group. Wherever you used DataBlock, change it to Block. Previously, the DataBlock held its DataFrame in the `Block.variables` property. Now, you can access the DataFrame in Block’s `Block.data` property. Finally, all Block metadata has been consolidated into one dict in `Block.metadata`. Previously, DataBlock had dedicated properties for comments, constants, and units.

### File operation functions[](#file-operation-functions "Link to this heading")

The top-level Functions for reading and writing files have new names. The function previously called `file_read()` has been renamed to [`read_file()`](../api_reference/fileio/read_file.md#keysight.pwdatatools._api.funcs.read_file "keysight.pwdatatools._api.funcs.read_file"). The previously named `file_write()` and `file_translate()` functions are now called [`write_file()`](../api_reference/fileio/write_file.md#keysight.pwdatatools._api.funcs.write_file "keysight.pwdatatools._api.funcs.write_file") and [`translate_file()`](../api_reference/fileio/translate_file.md#keysight.pwdatatools._api.funcs.translate_file "keysight.pwdatatools._api.funcs.translate_file"), respectively.

### Setting the ADS installation location[](#setting-the-ads-installation-location "Link to this heading")

The previous Data Tools versions used a global setting `pwdatatools.dirs` for the ADS installation location. This setting has been completely removed in favor of relying solely on the HPEESOF\_DIR environment variable.

### Options[](#options "Link to this heading")

All global options have been consolidated into one location at `pwdatatools.options`. For example, Data Tools has a top-level property `pwdatatools.options.reading` and `pwdatatools.options.writing` that contain all the options for reading and writing files. Previously, these options were located at `pwdatatools.files`.

### Logging[](#logging "Link to this heading")

In previous versions, the default behavior was to print info messages to the console. This has been changed so that only warnings and errors are printed. If you would like to see info messages, set `pwdatatools.options.logging.level = 'info'` or use `pwdatatools.options.logging.set_level()`. In previous versions, this option was located at `pwdatatools.set_logging_level()`.

### Summary[](#summary "Link to this heading")

* `import pwdatatools as pwdt` => `from keysight import pwdatatools as pwdt`
* `DataStore` => [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group")
* `DataBlock` => [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block")
* `DataBlock.variables` => `Block.data`
* `DataBlock.comments`, `DataBlock.constants`, `DataBlock.units` => `Block.metadata`
* `file_read()` => [`read_file()`](../api_reference/fileio/read_file.md#keysight.pwdatatools._api.funcs.read_file "keysight.pwdatatools._api.funcs.read_file")
* `file_write()` => [`write_file()`](../api_reference/fileio/write_file.md#keysight.pwdatatools._api.funcs.write_file "keysight.pwdatatools._api.funcs.write_file")
* `file_translate()` => [`translate_file()`](../api_reference/fileio/translate_file.md#keysight.pwdatatools._api.funcs.translate_file "keysight.pwdatatools._api.funcs.translate_file")
* `pwdatatools.dirs` => HPEESOF\_DIR environment variable
* `pwdatatools.files` => `pwdatatools.options.reading` and `pwdatatools.options.writing`
* ``` pwdatatools.set_logging_level ` => ``pwdatatools.options.logging.level = 'info'`() ``` or `pwdatatools.options.logging.set_level()`


---

<!-- === 来源: howto/use_var_class.md === -->

# Use the Var Class[](#use-the-var-class "Link to this heading")

The [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class is fundamental to storing and manipulating data in the `keysight.pwdatatools` library. It holds data and metadata for a single variable in a [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"). This section walks through how to use the [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class.

## Basics[](#basics "Link to this heading")

At a minimum, creating a [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") requires data, which can be any array-like object (numpy ndarray, Python list, pandas Series, etc.). Usually, a [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") will also be initialized with a string name. But, if no name is provided, the Var’s name is set to an empty string. Here, we initialize a Var with data as a Python list and the name `'freq'`. The data argument may be positional, but all other arguments must be keyword arguments.

```
>>> from keysight.pwdatatools import Var
>>> freq = Var([1e9, 2e9, 3e9], name='freq')
```

If we view the output of [`Var.__repr__()`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__repr__.md#keysight.pwdatatools.Var.__repr__ "keysight.pwdatatools.Var.__repr__"), we can see several other attributes that have been initialized as empty or None: [`Var.dims`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.dims.md#keysight.pwdatatools.Var.dims "keysight.pwdatatools.Var.dims"), [`Var.role`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.role.md#keysight.pwdatatools.Var.role "keysight.pwdatatools.Var.role"), [`Var.unit`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.unit.md#keysight.pwdatatools.Var.unit "keysight.pwdatatools.Var.unit"), and [`Var.attrs`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.attrs.md#keysight.pwdatatools.Var.attrs "keysight.pwdatatools.Var.attrs").

```
>>> freq
Var(
    <Float64 data with shape (3,)>,
    name='freq',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
```

As an alternative to invoking the [`Var.__repr__()`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__repr__.md#keysight.pwdatatools.Var.__repr__ "keysight.pwdatatools.Var.__repr__") method, we can use the [`Var.info()`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.info.md#keysight.pwdatatools.Var.info "keysight.pwdatatools.Var.info") method to get a more detailed summary of the Var. This method returns a `pandas.Series`.

```
>>> freq.info()
kind             -
role             -
dtype      Float64
shape         (3,)
dims             -
unit             -
min      1.000e+09
max      3.000e+09
null             -
nan              -
attrs            -
Name: freq, dtype: string
```

All of the Var’s metadata that we see in the repr have dedicated attributes: [`Var.name`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.name.md#keysight.pwdatatools.Var.name "keysight.pwdatatools.Var.name"), [`Var.dims`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.dims.md#keysight.pwdatatools.Var.dims "keysight.pwdatatools.Var.dims"), [`Var.role`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.role.md#keysight.pwdatatools.Var.role "keysight.pwdatatools.Var.role"), and [`Var.unit`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.unit.md#keysight.pwdatatools.Var.unit "keysight.pwdatatools.Var.unit"), [`Var.attrs`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.attrs.md#keysight.pwdatatools.Var.attrs "keysight.pwdatatools.Var.attrs"). Let’s demonstrate how to get these attributes. For now, let’s ignore the [`Var.dims`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.dims.md#keysight.pwdatatools.Var.dims "keysight.pwdatatools.Var.dims") attribute because it only applies to multi-dimensional Vars. We will explore that attribute later.

```
>>> freq.name
'freq'
>>> freq.role
''
>>> freq.unit
<returns None>
>>> freq.attrs
AttrsDict({})
```

All of Var’s metadata attributes are mutable. To demonstrate, let’s set new values for the name, role, and unit. Also, let’s add an item into the empty attrs dict.

```
>>> freq.name = 'bar'
>>> freq.role = 'frequency'
>>> freq.unit = 'Hz'
>>> freq.attrs['mixed'] = False
>>> freq  # view the updated Var
Var(
    <Float64 data with shape (3,)>,
    name='bar',
    dims=<empty Dims>,
    role='frequency',
    unit='Hz',
    attrs={'mixed': ...},
)
```

See also

For more information on variable roles, see [roles](../api_reference/public_submodules/roles/index.md#roles-module).

We can optionally include any of these additional attributes during instantiation of a new [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var"), instead of setting their values after instantiation. To illustrate, let’s create a new Var with a role, unit, and a couple arbitrary attributes. This time, we use a `numpy.ndarray` as the data input (instead of a Python list).

```
>>> import numpy as np
>>> data = np.arange(12)
>>> v = Var(data, name='v', role='voltage', unit='V', attrs={'type': 'DC', 'input': True})
>>> v
Var(
    <Int32 data with shape (12,)>,
    name='v',
    dims=<empty Dims>,
    role='voltage',
    unit='V',
    attrs={'type': ..., 'input': ...},
)
```

The [`Var.dtype`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.dtype.md#keysight.pwdatatools.Var.dtype "keysight.pwdatatools.Var.dtype"), [`Var.ndim`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.ndim.md#keysight.pwdatatools.Var.ndim "keysight.pwdatatools.Var.ndim"), [`Var.shape`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.shape.md#keysight.pwdatatools.Var.shape "keysight.pwdatatools.Var.shape"), and [`Var.size`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.size.md#keysight.pwdatatools.Var.size "keysight.pwdatatools.Var.size") attributes are read-only attributes that provide information about the Var’s data.

```
>>> v.dtype
Int32()
>>> v.ndim
1
>>> v.shape
(12,)
>>> v.size
12
```

## Multi-dimensional Vars[](#multi-dimensional-vars "Link to this heading")

To illustrate how to work with multi-dimensional Vars, let’s create a new [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") to represent S-parameters. 2 port S-parameter data is a 2x2 matrix with one extra dimension for frequency. Let’s assume we have 3 frequency points.

```
>>> import numpy as np
>>> s_data = (np.random.random(12) + 1j * np.random.random(12)).reshape(3, 2, 2)
>>> s = Var(s_data, name='S', role='network_parameters.s')
>>> s
Var(
    <Complex128 data with shape (3, 2, 2)>,
    name='S',
    dims=<empty Dims>,
    role='network_parameters.s',
    unit=None,
    attrs={},
)
```

This Var has 3 dimensions called axis 0, axis 1, and axis 2. Here is more info about each axis:

> * Axis 0 is called the “shared” dimension in pwdatatools and represents the 3 observations of the S-parameters over frequency.
> * Axis 1 is called the “i” dimension in pwdatatools and represents the “output” port of the S-parameters. It has a size of 2.
> * Axis 2 is called the “j” dimension in pwdatatools and represents the “input” port of the S-parameters. It also has a size of 2.

Important

A Var’s first dimension, which corresponds to axis 0 of the data, is known as the “shared dimension” because it is the common dimension shared by all Vars in a [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"). In the case of our S-parameters variable, there are 3 observations (because there are 3 frequency points), so the length of axis 0 must be 3. Therefore, the final shape of a 2 port S-parameter array with 3 frequency points must be (3, 2, 2).

The [`Var.dims`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.dims.md#keysight.pwdatatools.Var.dims "keysight.pwdatatools.Var.dims") attribute can be used to store metadata (as an instance of [`Dims`](../api_reference/metadata/dims/index.md#keysight.pwdatatools.Dims "keysight.pwdatatools.Dims")) associated with the higher dimensions of a multi-dimensional Var. Let’s create a new instance of [`Dims`](../api_reference/metadata/dims/index.md#keysight.pwdatatools.Dims "keysight.pwdatatools.Dims") and assign it to the [`Var.dims`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.dims.md#keysight.pwdatatools.Var.dims "keysight.pwdatatools.Var.dims") attribute of our S-parameters Var. For this example, we will include strings that act as port names.

```
>>> from keysight.pwdatatools import Dims
>>> dims = Dims(ndim=3, i_names=['P1', 'P2'], j_names=['P1', 'P2'])
>>> s.dims = dims
>>> s
Var(
    <Complex128 data with shape (3, 2, 2)>,
    name='S',
    dims=<Dims with names>,
    role='network_parameters.s',
    unit=None,
    attrs={},
)
```

Later, in the [indexing section](#var-indexing-select-method), we will see how to use the [`Var.select()`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.select.md#keysight.pwdatatools.Var.select "keysight.pwdatatools.Var.select") method to index multi-dimensional Vars based on dimension names and labels.

## NumPy functions[](#numpy-functions "Link to this heading")

The [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class implements a standard array interface that supports many numpy ufuncs (universal functions). This means we can use numpy ufuncs directly on a Var. The ufuncs always return a `numpy.ndarray`, not a [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var").

```
>>> v = Var(np.arange(12), name='v')
>>> np.sin(v)
array([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ,
       -0.95892427, -0.2794155 ,  0.6569866 ,  0.98935825,  0.41211849,
       -0.54402111, -0.99999021])
>>> np.max(v)
11
>>> np.isclose(v, 3)
array([False, False, False,  True, False, False, False, False, False,
       False, False, False])
```

Another option is to explicitly create a numpy ndarray before using numpy functions.

```
>>> arr = v.to_numpy_ndarray()
>>> np.sin(arr)
array([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ,
       -0.95892427, -0.2794155 ,  0.6569866 ,  0.98935825,  0.41211849,
       -0.54402111, -0.99999021])
```

Let’s create a new Var with some null data values. Null values can be included in the data input to a Var in several ways: as masked points in a numpy MaskedArray, as NA values in a pandas Series or DataFrame, or as None values in a Python list. Here, we use a Python list with None values to create nulls in a Var.

```
>>> v_null = Var([1, None, None, 4, 5], name='v_null')
>>> v_null.info()
kind         -
role         -
dtype    Int64
shape     (5,)
dims         -
unit         -
min          1
max          5
null         2
nan          -
attrs        -
Name: v_null, dtype: string
```

Now, let’s convert the Var with nulls to a numpy ndarray.

```
>>> arr = v_null.to_numpy_ndarray()
>>> arr
masked_array(data=[1, --, --, 4, 5],
         mask=[False,  True,  True, False, False],
   fill_value=0,
        dtype=int64)
```

Note that `arr` is a numpy MaskedArray and the null values are masked. We can use numpy functions on this MaskedArray, but we must use numpy.ma functions instead of numpy functions. For example, to sum the MaskedArray, we use `numpy.ma.sum()` instead of `numpy.sum()`.

```
>>> np.ma.sum(arr) # use np.ma.sum instead of np.sum
10
```

Note

PathWave Data Tools has different behavior for null and NaN values. NaN values present in float or complex Vars are *not* treated as null values.

## Operators[](#operators "Link to this heading")

The [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class supports the same operators as numpy ndarrays. Just like with numpy ufuncs, using operators with one or more Vars always returns a numpy ndarray instead of a Var.

```
>>> v1 = Var(np.arange(7), name='v1')
>>> v2 = Var(np.full(7, 10), name='v2')
>>> v1 + v2
array([10, 11, 12, 13, 14, 15, 16])
>>> v1 * v2
array([ 0, 10, 20, 30, 40, 50, 60])
>>> v1 > v2
array([False, False, False, False, False, False, False])
```

## Plotting[](#plotting "Link to this heading")

The [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class implements a standard array interface that supports many matplotlib and seaborn plotting functions.

```
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> import seaborn as sns
>>> from keysight.pwdatatools import Var
>>> data = np.arange(6)
>>> x_var = Var(data, name="v")
>>> y_var = Var(data**2, name="v^2")
>>> plt.plot(x_var, y_var)  # matplotlib lineplot
>>> sns.scatterplot(x=x_var, y=y_var, ax=plt.gca(), color="red")  # seaborn scatterplot
>>> plt.xlabel(x_var.name)
>>> plt.ylabel(y_var.name)
>>> plt.title("Simple Variable Plot Demo")
>>> plt.show()
```

[![Simple Variable Plot Demo](../_images/var_plot.png)](../_images/var_plot.png)

## Indexing[](#indexing "Link to this heading")

We saved the topic of indexing for last since it is the most involved. The [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class supports several different options: [numpy-style indexing](#var-indexing-numpy-style), [one-based integer indexing and parentheses syntax](#var-indexing-one-based), and the [Var select method](#var-indexing-select-method). Also, if you prefer, you can can convert a Var to a `pandas.Series` or `pandas.DataFrame` and use pandas indexing directly. When you are done, you can convert the pandas object back to a Var. This pandas-based approach is covered last, in the [pandas indexing section](#pandas-indexing).

Let’s explore each of these in detail.

### NumPy style[](#numpy-style "Link to this heading")

The [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class supports all the same indexing operations as numpy. All indexing operations return a new Var with new data (and possibly new dims). All other metadata, including the new Var’s name, is copied from the old Var. Let’s create a new 2D Var to illustrate.

```
>>> data = np.arange(12).reshape(3, 4)
>>> data
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> v = Var(data, name='v')
>>> v
Var(
    <Int32 data with shape (3, 4)>,
    name='v',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
```

Just like numpy, we can index a Var with integers or slices.

```
>>> v0 = v[0] # integer indexing
>>> v0
Var(
    <Int32 data with shape (4,)>,
    name='v',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
>>> v0.to_numpy_ndarray()
array([0, 1, 2, 3])
>>> v_slice = v[1:3, 0:3] # slice indexing
>>> v_slice
Var(
    <Int32 data with shape (2, 3)>,
    name='v',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
>>> v_slice.to_numpy_ndarray()
array([[ 4,  5,  6],
       [ 8,  9, 10]])
```

Below are some other numpy-style indexing examples, but there are many more options not shown here. See the numpy indexing documentation for more information.

```
>>> v12 = v[[1,2], :]
>>> v12.to_numpy_ndarray()
array([[ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> bool_mask = np.array([True, False, True])
>>> v_bool = v[bool_mask, :]
>>> v_bool.to_numpy_ndarray()
array([[ 0,  1,  2,  3],
       [ 8,  9, 10, 11]])
```

### One-based integer in parentheses[](#one-based-integer-in-parentheses "Link to this heading")

Another way to index a Var is by using parentheses instead of square brackets. When using parentheses, it is assumed that the indexes are one-based integers instead of zero-based integers. This is useful when working with multi-dimensional data that employs one-based integer indexes, such as S-parameter data. Let’s create a new Var to illustrate.

```
>>> s_data = (np.random.random(12) + 1j * np.random.random(12)).reshape(3, 2, 2)
>>> s = Var(s_data, name='S', role='network_parameters.s')
>>> s
Var(
    <Complex128 data with shape (3, 2, 2)>,
    name='S',
    dims=<empty Dims>,
    role='network_parameters.s',
    unit=None,
    attrs={},
)
```

We can index the Var with one-based integers using parentheses. In the output below, note that the name of the new Var is `'S(1,1)'` instead of `'S'`.

```
>>> s11 = s(1, 1)
>>> s11
Var(
    <Complex128 data with shape (3,)>,
    name='S(1,1)',
    dims=<empty Dims>,
    role='network_parameters.s',
    unit=None,
    attrs={},
)
```

If we wanted to use traditional zero-based indexing to retrieve S(1,1) from the S-matrix, we would have to use the following syntax: `s[:, 0, 0]`. Indexing with one-based integer indexing and parentheses is much more natural for S-parameters than the zero-based integer indexing we typically use in Python and numpy. When utilizing parentheses indexing, the new Var’s data and dims are always reduced to one dimension. The roles, attrs, and unit are copied from original Var.

Important

When performing this type of indexing, it is only applied to the higher dimensions, and never the first dimension (also known as the shared dimension or axis 0). In other words, you cannot index the Var’s data along axis 0 with parentheses-based indexing. The indexes are only applied to axis 1 and higher. This means you cannot index 1D Vars using parentheses.

Can we combine zero-based and one-based integer indexing? Yes, we can. Let’s illustrate using the S-parameters Var and get S(1,1) at the first two frequency points.

```
>>> s11_partial = s(1, 1)[0:2]
>>> s11_partial
Var(
    <Complex128 data with shape (2,)>,
    name='S(1,1)',
    dims=<empty Dims>,
    role='network_parameters.s',
    unit=None,
    attrs={},
)
```

### The select method[](#the-select-method "Link to this heading")

The [`Var.select()`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.select.md#keysight.pwdatatools.Var.select "keysight.pwdatatools.Var.select") method is a powerful way to index into multi-dimensional Vars. It allows indexing based upon arbitrary strings and numbers, rather than 0-based or 1-based integer positions. Let’s create a new Var to illustrate. We also need to create an instance of [`Dims`](../api_reference/metadata/dims/index.md#keysight.pwdatatools.Dims "keysight.pwdatatools.Dims") to store metadata about the higher dimensions.

```
>>> import numpy as np
>>> from keysight.pwdatatools import Dims, Var
>>> data = np.arange(160).reshape(10, 4, 4)
>>> dims = Dims(
...    ndim=3,
...    i_nums=[1, 2, 3, 4],
...    i_names=['P1', 'P2', 'P3', 'P4'],
...    j_nums=[1, 2, 3, 4],
...    j_names=['P1', 'P2', 'P3', 'P4']
... )
>>> s = Var(data, name='S', dims=dims)
>>> s
Var(
    <Int32 data with shape (10, 4, 4)>,
    name='S',
    dims=<Dims with nums and names>,
    role='',
    unit=None,
    attrs={},
)
```

Let’s use the [`Var.select()`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.select.md#keysight.pwdatatools.Var.select "keysight.pwdatatools.Var.select") method to get S(2,1) from the S-parameters variable. Note the new shape of the data and the new dims.

```
>>> s21 = s.select(i=2, j=1)
>>> s21
Var(
    <Int32 data with shape (10, 1, 1)>,
    name='S',
    dims=<Dims with nums and names>,
    role='',
    unit=None,
    attrs={},
)
>>> s21.dims
Dims(
    ndim=3,
    i_nums=[2],
    i_names=['P2'],
    j_nums=[1],
    j_names=['P1'],
)
```

Let’s do the same thing, except let’s use the portnames this time.

```
>>> s21 = s.select(i='P2', j='P1')
>>> s21
Var(
    <Int32 data with shape (10, 1, 1)>,
    name='S',
    dims=<Dims with nums and names>,
    role='',
    unit=None,
    attrs={},
)
>>> s21.dims
Dims(
    ndim=3,
    i_nums=[2],
    i_names=['P2'],
    j_nums=[1],
    j_names=['P1'],
)
```

Now, let’s use the [`Var.select()`](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.select.md#keysight.pwdatatools.Var.select "keysight.pwdatatools.Var.select") method to get all the S-parameters associated with ports 3 and 4. Just for illustration purposes, this time we use a dict instead of keyword arguments.

```
>>> s_p3_p4 = s.select({'i': [3, 4], 'j': [3, 4]})
>>> s_p3_p4
Var(
    <Int32 data with shape (10, 2, 2)>,
    name='S',
    dims=<Dims with nums and names>,
    role='',
    unit=None,
    attrs={},
)
>>> s_p3_p4.dims
Dims(
    ndim=3,
    i_nums=[3, 4],
    i_names=['P3', 'P4'],
    j_nums=[3, 4],
    j_names=['P3', 'P4'],
)
```

### Pandas indexing[](#pandas-indexing "Link to this heading")

If you are familiar with pandas, you may prefer to use pandas indexing instead of Var’s built-in indexing covered above. This is possible by converting a Var to a `pandas.Series` (for a 1D Var) or `pandas.DataFrame` (for a multi-dimensional Var) and then using pandas indexing. When you are done, you can convert the pandas object back to a Var. Let’s demonstrate with a 3D Var.

```
>>> import numpy as np
>>> from keysight.pwdatatools import Var
>>> data = np.linspace(1000, 20000, 20).reshape(5, 2, 2)
>>> v = Var(data, name='v')
```

Let’s convert the Var to a `pandas.DataFrame` and use pandas indexing. Below, we set `cols_nlevels=-1` so that a MultiIndex is created for the columns with as many levels needed to hold the Var’s dims.

```
>>> df = v.to_pandas_dataframe(cols_nlevels=-1)
>>> df
varname        v
i              1                 2
j              1        2        1        2
0         1000.0   2000.0   3000.0   4000.0
1         5000.0   6000.0   7000.0   8000.0
2         9000.0  10000.0  11000.0  12000.0
3        13000.0  14000.0  15000.0  16000.0
4        17000.0  18000.0  19000.0  20000.0
```

We can use pandas indexing to select a subset of the data.

```
>>> df.loc[:, ('v', 1, 2)]
0     2000.0
1     6000.0
2    10000.0
3    14000.0
4    18000.0
Name: (v, 1, 2), dtype: float64
```

We can also assign new values in place.

Note

When setting data in place in pandas, beware of the infamous “SettingWithCopyWarning” when using pandas indexing. This warning is raised when you try to assign values to a slice of a pandas object that is a view of the original object.

```
>>> df.loc[:, ('v', 1, 2)] = 42
>>> df
varname        v
i              1              2
j              1     2        1        2
0         1000.0  42.0   3000.0   4000.0
1         5000.0  42.0   7000.0   8000.0
2         9000.0  42.0  11000.0  12000.0
3        13000.0  42.0  15000.0  16000.0
4        17000.0  42.0  19000.0  20000.0
```

When we are done, we can convert the `pandas.DataFrame` back to a Var.

```
>>> v_new = Var.from_pandas_dataframe(df)
>>> v_new
Var(
    <Float64 data with shape (5, 2, 2)>,
    name='v',
    dims=<Dims with nums>,
    role='',
    unit=None,
    attrs={},
)
```

Note that the new Var has dims which were extracted from the MultiIndex of the DataFrame.

```
>>> v_new.dims
Dims(
    ndim=3,
    i_nums=[1, 2],
    i_names=None,
    j_nums=[1, 2],
    j_names=None,
)
```

See also

For more information on pandas indexing, see [pandas DataFrame Indexing](../core_concepts/pandas_dataframe_indexing.md#pandas-dataframe-indexing) and the [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html).


---

<!-- === 来源: howto/work_with_ADS_data.md === -->

# Work with ADS Data[](#work-with-ads-data "Link to this heading")

This section walks through an example of reading an ADS dataset file (.ds file) into a Group. However, the procedure is similar if you want to read any type of supported datafile. Before proceeding, if you aren’t familiar with Groups or Blocks, see [Universal Data Structures](../index.md#data-structs-section).

Important

Before importing an ADS dataset file, you must either install ADS and set the HPEESOF\_DIR environment variable to point to your ADS installation directory, or you must install the `keysight.ads.dataset` Python library. If you are using Data Tools from within the ADS Python environment (by pointing to the ADS Python executable or by using the built-in Python Console), everything is already set up for you.

## Read the file as a Group[](#read-the-file-as-a-group "Link to this heading")

First, import the `keysight.pwdatatools` library. Then, use the top-level function [`read_file_as_group()`](../api_reference/fileio/read_file_as_group.md#keysight.pwdatatools._api.funcs.read_file_as_group "keysight.pwdatatools._api.funcs.read_file_as_group"), which can read all supported types of datafiles, including ADS datasets. Input a full path to the dataset as a Python string. You can optionally prepend an “r” to the path to denote a raw string, in order to make sure backslashes in Windows paths are not interpreted by Python as escape characters. For more information on filepaths, see [All About Filepaths](../core_concepts/all_about_filepaths.md#all-about-filepaths).

```
>>> from keysight import pwdatatools as pwdt
>>> group = pwdt.read_file_as_group(r'C:\data\s_param.ds')
>>> group
Group(
    <3 Blocks>,
    name='s_param',
    attrs={},
)
```

## Examine the Blocks[](#examine-the-blocks "Link to this heading")

This particular ADS dataset is represented as a Group with 3 Blocks. The Blocks are stored in the [`Group.members`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") attribute. In order to see one-line summaries of the Blocks that were created, access the [`Group.members`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") attribute.

```
>>> group.members
MemberList(
    [
        <Block 'Sweep1.SP1.SP' with 4 Vars and 6 observations>,
        <Block 'aele_0.Sweep1.SP1' with 3 Vars and 6 observations>,
        <Block 'aele_1.Sweep1.SP1' with 2 Vars and 2 observations>,
    ]
)
```

The ADS schematic that generated this dataset has two MeasEqns in it; the two MeasEqns created two additional Blocks (the ones that start with *aele*).

Note

ADS datasets often contain hierarchy (nested datasets). As already mentioned, nested datasets are generated when a schematic uses MeasEqns. Hierarchical datasets are also created when a schematic contains Eye Probes or more than one simulation controller. This is the reason many imported ADS datasets result in a Group with more than one Block.

There are several ways to access one of the Blocks. All of the methods below yield the same result. However, the method [`Group.get_member_as_block()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.get_member_as_block.md#keysight.pwdatatools.Group.get_member_as_block "keysight.pwdatatools.Group.get_member_as_block") is the most preferred method, because it is the most explicit in its return type.

```
>>> # All lines below yield the same result, but the first two are preferred
>>> blk0 = group.get_member_as_block(0)  # (must know the Block's position)
>>> blk0 = group.get_member_as_block('Sweep1.SP1.SP')  # (must know the Block's name)
>>> blk0 = group.members[0]  # index into members (must know Block's position)
>>> blk0 = group[0]  # index into Group (must know Block's position)
>>> blk0 = group['Sweep1.SP1.SP']  # key into Group (must know the Block's name)
```

We can view a more detailed summary of the Block by printing it or by viewing its `__repr__`.

```
>>> print(blk0)  # print the Block
Block(
    <'S', 'PortZ' with 6 observations>,
    name='Sweep1.SP1.SP',
    ivarnames=('C1', 'freq'),
    attrs={},
)
>>> blk0  # or equivalently, view the Block's __repr__
Block(
    <'S', 'PortZ' with 6 observations>,
    name='Sweep1.SP1.SP',
    ivarnames=('C1', 'freq'),
    attrs={},
)
```

A Block’s name can be accessed via the [`Block.name`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.name.md#keysight.pwdatatools.Block.name "keysight.pwdatatools.Block.name") attribute.

```
>>> blk0.name
'Sweep1.SP1.SP'
```

Variables can be retrived by name from the Block as shown below.

```
>>> blk0['S']
Var(
    <Complex128 data with shape (6, 2, 2)>,
    name='S',
    dims=<Dims with nums>,
    role='network_parameters.s',
    unit=None,
    attrs={},
)
```

Variables are stored as instances of [`Var`](../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var"). Vars store data along with metadata such as name, attributes, dimensions, role, and unit. For more information on Vars, see [Use the Var Class](use_var_class.md#use-var-class).

The Block has properties that store the names of the independent variables (ivarnames) and dependent variables (dvarnames), as shown below. The ordering in the [`Block.ivarnames`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.ivarnames.md#keysight.pwdatatools.Block.ivarnames "keysight.pwdatatools.Block.ivarnames") property value is critical in order to maintain proper dependencies when writing to new files.

```
>>> blk0.ivarnames
('C1', 'freq')
>>> blk0.dvarnames
('S', 'PortZ')
```

So for `blk0`, the outer ivar is ‘C1’ and the inner ivar is “freq’. The ordering of the dvarnames is not important, **but the ordering in the ivarnames attribute is critical, especially if you write out a file from a Block**.

Note

If you aren’t sure how to determine which variables are independents (ivars) vs dependents (dvars), please see [Multi-Dimensional Data](../core_concepts/multi_dimensional_data.md#multidim-data) for more info. This info can be especially helpful if you want to create a Group and Block(s) using data sources other than the officially-supported file formats. When reading officially-supported file formats, the assignment of each variable to a role of ivar or dvar is automatically performed, and thus the resulting Block(s) will already have the correct [`Block.ivarnames`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.ivarnames.md#keysight.pwdatatools.Block.ivarnames "keysight.pwdatatools.Block.ivarnames") and [`Block.dvarnames`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.dvarnames.md#keysight.pwdatatools.Block.dvarnames "keysight.pwdatatools.Block.dvarnames") property values.

The [`Block.info()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.info.md#keysight.pwdatatools.Block.info "keysight.pwdatatools.Block.info") method can be useful for understanding the variables in a dataset. It returns a pandas DataFrame containing useful information about variable(s) in a Block. If [`Block.info()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.info.md#keysight.pwdatatools.Block.info "keysight.pwdatatools.Block.info") is invoked without any arguments, the info on all variables are returned in a DataFrame. Several uses of the [`Block.info()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.info.md#keysight.pwdatatools.Block.info "keysight.pwdatatools.Block.info") method are illustrated below using `blk0`.

```
>>> blk0.info('C1')  # calling with a single varname
            C1
kind      ivar
role         -
dtype  Float64
shape     (6,)
dims         -
unit         -
min     10.000
max     15.000
null         -
nan          -
attrs        -

>>> blk0.info()  # calling without any varnames returns info on all variables
            C1               freq                     S           PortZ
kind      ivar               ivar                  dvar            dvar
role         -  frequency.primary  network_parameters.s  impedance.port
dtype  Float64            Float64            Complex128      Complex128
shape     (6,)               (6,)             (6, 2, 2)          (6, 2)
dims         -                  -                  nums            nums
unit         -                  -                     -               -
min     10.000          1.000e+09                 0.117          50.000
max     15.000          2.000e+09                 0.985          50.000
null         -                  -                     -               -
nan          -                  -                     -               -
attrs        -          <1 attrs>                     -               -

>>> blk0.info(['C1', 'PortZ'])  # calling with an list of varnames
            C1           PortZ
kind      ivar            dvar
role         -  impedance.port
dtype  Float64      Complex128
shape     (6,)          (6, 2)
dims         -            nums
unit         -               -
min     10.000          50.000
max     15.000          50.000
null         -               -
nan          -               -
attrs        -               -
```

Remember that this particular ADS dataset is represented as 3 Blocks. We just examined the first Block, which contains the main S-parameter simulation data. The next two Blocks contain variables from MeasEqns. Notice how the Blocks have different dependencies (`ivarnames`) and different numbers of observations. This is indeed why ADS datasets are hierarchical… the Blocks need to be independent from one another because of these differences.

```
>>> blk1 = group.get_member_as_block(1)
>>> blk2 = group.get_member_as_block(2)
>>> blk1
Block(
    <'VSWR1' with 6 observations>,
    name='aele_0.Sweep1.SP1',
    ivarnames=('C1', 'freq'),
    attrs={},
)
>>> blk2
Block(
    <'Phase_dev_at_1p5GHz' with 2 observations>,
    name='aele_1.Sweep1.SP1',
    ivarnames=('C1',),
    attrs={},
)
```

As we did in the first Block, we can access variables for these other two Blocks.

```
>>> blk1['VSWR1']
Var(
    <Float64 data with shape (6,)>,
    name='VSWR1',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
>>> blk2['Phase_dev_at_1p5GHz']
Var(
    <Float64 data with shape (2,)>,
    name='Phase_dev_at_1p5GHz',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
```


---

<!-- === 来源: howto/work_with_csv_data.md === -->

# Work with CSV Data[](#work-with-csv-data "Link to this heading")

CSV (comma-separated values) datafiles are a commonly-used format. CSV files are often used to store data from spreadsheets, databases, and other applications. This section describes how to use CSV datafiles with PathWave Data Tools.

Note

In addition to CSV, tab-separated values (TSV) datafiles are also common. The following examples focus on CSV files, but TSV files and similar formats are also supported.

## Read a CSV file[](#read-a-csv-file "Link to this heading")

While basic comma-separated-value files (CSV files) are fairly standard, there are many considerations to making a robust CSV file reader. Here are a few:

* How to handle string data, expecially special characters like quotes and commas
* How to handle headers and footers
* What datatypes to use for each column of data
* What to do with missing or invalid data points
* How to make it fast for large files

PathWave Data Tools relies on 3rd-party CSV file readers rather than trying to accommodate all these scenarios with its own CSV file reader. This avoids reinventing the same CSV-reading functionality that already exists in other libraries like pandas, pyarrow, and the standard Python `csv` library. By default, PathWave Data Tools uses the [pandas](https://pandas.pydata.org/) library under the hood to read CSV files. However, all the standard file reading and writing functions and methods in PathWave Data Tools work directly with CSV files. CSV files are not hierarchical data formats, so they never contain more than one Block.

```
>>> from keysight import pwdatatools as pwdt
>>> block = pwdt.read_file_as_block('./mydata.csv')
```

The `pandas.read_csv()` function, which is used by default under the hood, has many options for reading CSV files. You can pass keyword arguments (kwargs) as a dict into the `pandas.read_csv()` function via the global option `pwdatatools.options.reading.format_specific.csv.pandas_kwargs`. For more information on available kwargs, see the [pandas read\_csv documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html).

Since the CSV file does not contain any information about variable dependencies, you may want to manually set the `ivarnames` attribute after reading the CSV file. The remaining variables in the CSV file become dependent variables in the Block.

```
>>> block.ivarnames = ('V1', 'freq')
```

## Write a CSV file[](#write-a-csv-file "Link to this heading")

We can easily write a CSV file from a Block object, as shown below.

```
>>> block.to_file('./mydata.csv')
```

Under the hood, pwdatatools converts the Block into a pandas DataFrame and uses the `pandas.DataFrame.to_csv()` method to write the file. This function has many options for writing CSV files. You can pass options as keyword arguments (kwargs) as a dict to the global option `pwdatatools.options.writing.format_specific.csv.pandas_kwargs`. For more information, see the [pandas DataFrame.to\_csv documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html).


---

<!-- === 来源: howto/work_with_loadpull_data.md === -->

# Work with Load Pull Data[](#work-with-load-pull-data "Link to this heading")

## Overview[](#overview "Link to this heading")

PathWave Data Tools has several features to help you work with load pull data:

* supports reading of many different file formats from Maury, Focus, and Keysight loadpull measurement systems.
* includes many types of useful data manipulation functions and methods, including rectangular and polar gridding and regridding, dropping bad data points, gain compression calculations, interpolation, extrapolation, regularizing irregular data, and more.
* provides a visualization submodule that builds off matplotlib and seaborn, making it easy to do contour plotting and Smith Charts.
* makes it easy to write out new data files, with support for many different file formats, including MDIF files and ADS dataset files (.ds files). This includes automatic reformatting of the data so that it is directly compatible with ADS contour plotting functions in ADS Display.

Important

An ADS Data Display license is required to read measured load pull datafile formats. Addtionally, if you are on Windows OS, you must download and install EEsof Licensing Tools from here: [https://edadocs.software.keysight.com/display/downloads/Licensing+Software+Downloads](https://edadocs.software.keysight.com/display/downloads/Licensing%2BSoftware%2BDownloads).

While the main PathWave Data Tools classes [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") and [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") may be used to work with load pull data, the dedicated [`LoadPullBlock`](../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") class is recommended because it provides additional functionality targeted specifically to load pull data. The [`LoadPullBlock`](../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") class is a subclass of the [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") class. Therefore, all the methods and attributes of [`Block`](../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") are also available in [`LoadPullBlock`](../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock"). An instance of [`LoadPullBlock`](../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") can be created as shown below.

```
>>> from keysight import pwdatatools as pwdt
>>> lpblock = pwdt.LoadPullBlock(
...     dataframe,
...     name='mylpdata'
...     gamma_ivarname='GammaLoad',
...     power_ivarname='PSource',
... )
```

The above assumes that `dataframe` is a pandas DataFrame and that there are columns in the DataFrame named ‘GammaLoad’ and ‘PSource’ that represent the swept Gamma and Power variables (ivars). The `name` parameter is optional and is used to set the name of the [`LoadPullBlock`](../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object.

If you are reading load pull data files, you will not need to create a [`LoadPullBlock`](../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") directly as shown above. Instead, the [`read_file_as_loadpullblock()`](../api_reference/fileio/read_file_as_loadpullblock.md#keysight.pwdatatools._api.funcs.read_file_as_loadpullblock "keysight.pwdatatools._api.funcs.read_file_as_loadpullblock") function can be used, which returns an instance of [`LoadPullBlock`](../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock"). Alternatively, the [`LoadPullBlock.from_file()`](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.from_file.md#keysight.pwdatatools.LoadPullBlock.from_file "keysight.pwdatatools.LoadPullBlock.from_file") method can be used.

```
from keysight import pwdatatools as pwdt
# Read a load pull data file
lpblock = pwdt.read_file_as_loadpullblock(r'C:\Users\data\myloadpullfile.lpd')
# Alternatively, use the from_file method
lpblock = pwdt.LoadPullBlock.from_file(r'C:\Users\data\myloadpullfile.lpd')
```

## Types of load pull files[](#types-of-load-pull-files "Link to this heading")

PathWave Data Tools supports reading data files from the following loadpull measurement systems:

* Keysight (in generic MDIF format)
* Focus (file extensions .lpd, .lpc, .lpcwave, and .lpacwave)
* Maury (file extensions .cst, .lp, .mat, and .spl)

Load Pull data files can be broadly categorized into two types:

* Wave data formats
* Derived data formats

The wave data formats contain measured A and B waves, as well as DC voltages and currents. Wave formats are the most flexible because they contain all the information needed to calculate (or derive) many common load pull variables. In contrast, the derived data formats contain only the calculated variables (such as PLoad, GammaIn, DrainEff, etc). If a variable was not measured or calculated during the load pull measurement, it likely cannot be calculated from a file in one of the derived data formats.

Note

Some Focus load pull data files contain both wave data and derived variables. These derived variables in the files contain the suffix “Waves” in their names. When reading these types of files, `pwdatatools` uses both the wave data and the derived variables from the file, and if necessary, derives additional variables from the wave data.

## Variable names[](#variable-names "Link to this heading")

The following table lists some of the variables created from load pull files. This is not an exhaustive list because many load pull measurement systems allow custom variables. These are the *default* variable names used by `keysight.pwdatatools`. However, there are various ways to override the default names and set your own desired variable names. You can modify the names of many common variables that are read from loadpull files with the global option `options.reading.varnames`. For example, if you want to change the name of “PSource” to “Pavs”, you can do the following: `options.reading.varnames['power.available.source'] = "Pavs"`. This setting is applied during the file reading process. Alternatively, you can use the [`LoadPullBlock.rename_vars()`](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.rename_vars.md#keysight.pwdatatools.LoadPullBlock.rename_vars "keysight.pwdatatools.LoadPullBlock.rename_vars") method or the [`Block.rename_vars()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.rename_vars.md#keysight.pwdatatools.Block.rename_vars "keysight.pwdatatools.Block.rename_vars") method to change the names of variables after the data has been read.

Load Pull variables[](#id6 "Link to this table")

| Variable | Description | Role | Derivable from wave data formats? |
| --- | --- | --- | --- |
| a1 | A wave (incident) at input | wave.enumerated.incident | Yes |
| a2 | A wave (incident) at output | wave.enumerated.incident | Yes |
| b1 | B wave (reflected) at input | wave.enumerated.reflected | Yes |
| b2 | B wave (reflected) at output | wave.enumerated.reflected | Yes |
| AMPM | Input amplitude variation converted to output phase variation | distortion.ampm | Yes |
| DrainEff | Drain efficiency | efficiency.drain | Yes |
| Fn (F1, F2, etc.) | Frequency | frequency.enumerated | Yes |
| GainP | Power gain | gain.power | Yes |
| GainT | Transducer gain | gain.transducer | Yes [[note]](#note) |
| GammaIn | Reflection coefficient looking into the device input | gamma.input | Yes |
| GammaLoad | Reflection coefficient looking into the load | gamma.load | Yes |
| GammaOut | Reflection coefficient looking into the device output | gamma.output | Yes |
| GammaSource | Reflection coefficient looking into the source | gamma.source | No |
| Iin | DC current at input | current.direct.input | Yes |
| Iout | DC current at output | current.direct.output | Yes |
| PAE | Power added efficiency | efficiency.power-added | Yes |
| PinAvail | Power available at device input | power.available.input | Yes [[note]](#note) |
| PinDel | Power delivered to the device input | power.delivered.input | Yes |
| PLoad | Power delivered to the load | power.delivered.load | Yes |
| PSource | Power available from the source | power.available.source | No |
| Vin | DC voltage at input | voltage.dc.input | Yes |
| Vout | DC voltage at output | voltage.dc.output | Yes |
| Zin | Impedance looking into the device input | impedance.input | Yes [[note]](#note) |
| ZrefLoad | Load reference impedance | impedance.load.reference | No |
| ZrefSource | Source reference impedance | impedance.reference.source | No |

[note]
([1](#id2),[2](#id3),[3](#id4))

Besides the wave data, additional variables are needed to derive these quantities (such as GammaSource and/or ZrefSource).

PathWave Data Tools uses the following conventions for frequency variables and suffixes:

* Frequency variables F1, F2, F3, etc. are called *enumerated frequencies*. Most of the time, these are harmonically-related, but that is not always the case (which is why they are referred to as enumerated frequencies rather than harmonics). If the frequencies are harmonically-related, F1 is the fundamental frequency, F2 is the second harmonic, F3 is the third harmonic, and so on. These frequencies may also be swept during a measurement. For example, one could sweep the fundamental frequency F1 and measure at the second harmonic F2. In this case, F1 is the swept frequency and F2 is the measured frequency (which is also varying).
* Many common load pull variables are measured at a particular frequency. Many times, a variable’s name will contain a suffix indicating the frequency. For example, the variable “GammaLoad\_F2” is GammaLoad at the second harmonic. Under certain circumstances, frequency suffixes are omitted. For example, variables like GainP, GainT, AMPM, etc. are only typically derived at the fundamental frequency F1. So by default, their suffixes are omitted. Otherwise, these variables would have been named “Gp\_F1”, “Gt\_F1”, “AMPM\_F1”, etc., which is a bit of overkill since usually these derived quantites only make sense at the fundamental. However, it is possible to derive these variables at other frequencies by modifying the global option. For example, to enable AMPM to be calculated at all available frequencies, you can do the following.

```
>>> from keysight import pwdatatools as pwdt
>>> freq_enums_global = pwdt.options.reading.format_specific.loadpull.derived_vars.freq_enums
>>> freq_enums_global
FrozenRolesSet({'gamma.load', 'gamma.input'})
```

The global frequency enums is a frozen set, so to modify it, we must create a mutable container (like a set) and then add the new frequency enums to it. In the example below, we are adding the AMPM variable (which has a role of “distortion.ampm”) to the set of frequency enums.

```
>>> freq_enums = set(freq_enums_global)
>>> freq_enums.add('distortion.ampm')
>>> pwdt.options.reading.format_specific.loadpull.derived_vars.freq_enums = freq_enums
```

Now, if we check the global frequency enums, we will see that AMPM has been added to the set.

```
>>> pwdt.options.reading.format_specific.loadpull.derived_vars.freq_enums
FrozenRolesSet({'gamma.load', 'gamma.input', 'distortion.ampm'})
```

## Sending data to Advanced Design System[](#sending-data-to-advanced-design-system "Link to this heading")

PathWave Data Tools provides several ways to get load pull data into ADS. You can directly translate a load pull file into an ADS dataset using the top-level [`translate_file()`](../api_reference/fileio/translate_file.md#keysight.pwdatatools._api.funcs.translate_file "keysight.pwdatatools._api.funcs.translate_file") function. Or, you can translate a file using a two-step process. First, you read the load pull file and then write out a new ADS dataset file. See the [Translate a File](translate_a_file.md#translate-a-file) section for more information.

Important

When sending data to ADS, it’s important to know that ADS does not support complex ivars. So, a complex gamma or impedance ivar could prevent the data from being translated into an ADS dataset. Therefore, you should either split the complex ivar into two real ivars or use integer indexes instead of the ivar values.

One approach is to write an ADS dataset directly from a LoadPullBlock. The LoadPullBlock’s `idxnames` are used as the independent variables in the ADS dataset. This is because there is always at least one complex ivar (gamma or impedance) and ADS does not support complex ivars and so the integer idxs will work better as ivars in ADS.

```
>>> lpblock.to_file(r"C:\Users\data\loadpull_data.ds")
```

Another approach is create a `ADSContourBlock` from the LoadPullBlock using the [`LoadPullBlock.to_adscontourblock()`](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_adscontourblock.md#keysight.pwdatatools.LoadPullBlock.to_adscontourblock "keysight.pwdatatools.LoadPullBlock.to_adscontourblock") method. You can optionally give the ADSContourBlock a name that is different than the name of the LoadPullBlock, or else it will inherit the same name.

```
>>> adscontourblock = lpblock.to_adscontourblock(name='contour_data')
>>> print(adscontourblock.ivarnames)
('imag_of_GammaLoad', 'real_of_GammaLoad', 'PSource')
```

If we examine the printout above, we can see that the gamma ivar was split into real and imaginary parts. The ivars are arranged in an ordering that is friendly to the way that the contour plotting functions work in ADS Data Display.

The ADSContourBlock class provides the `ADSContourBlock.to_file()` method to write the data to a file. Alternatively, you can place the ADSContourBlock into a [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") object and then write the data to a file. All specialized Block classes are groupable, meaning they can be placed into a Group object. Below, we are grouping the ADSContourBlock with the LoadPullBlock and writing them to the same file.

```
>>> adscontourblock.to_file(r"C:\Users\data\loadpull_data.ds")
>>> # Alternatively, you can place the ADSContourBlock into a Group and write the Group.
>>> # Just for demonstration purposes, we are grouping it with a LoadPullBlock to show
>>> # that all specialized and generic Block classes are groupable.
>>> group = pwdt.Group([adscontourblock, lpblock])
>>> group.to_file(r"C:\Users\data\loadpull_data.ds")
```

## What is “gridded” load pull data?[](#what-is-gridded-load-pull-data "Link to this heading")

When working with load pull data, sometimes it is useful to have gamma or impedance points that are on a regular rectangular or polar grid. For example, this is useful for plotting in ADS. For data to be considered “gridded”, the following conditions must be met:

* The data must have either a gamma or impedance dependency.
* The gamma or impedance values must be regularly-spaced.
* There must be the same number of y points for each x point. On a rectangular coordinate system, x and y are real and imaginary. On a polar coordinate system, x and y are magnitude and phase.
* If the data has a power-dependency, the power sweeps must be regular.
* If the data has outer swept variable(s) (for example, frequency, bias, temperature, etc.), the 2D grid is allowed to vary across those outer ivar values. For example, in the case of a frequency ivar, the data can have different grid spacings, number of grid points, and grid extents at each frequency point. However, the grid’s coordinate system (‘rect’ or ‘polar’) must be consistent across frequencies. If, at any frequency, the data does not meet any of the conditions above, the data is not considered “gridded”.

## Examples[](#examples "Link to this heading")

Check out the load pull examples here: [Load Pull Examples](../examples/loadpull/index.md#load-pull-examples).

See also

All Python scripts and data files for the load pull examples are located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

## The Load Pull Data GUI[](#the-load-pull-data-gui "Link to this heading")

The Load Pull Data GUI is a graphical user interface that makes it easy to work with load pull data. It is a separate application that complements PathWave Data Tools. It can be launched from PathWave Advanced Design System (ADS) after intalling it as an add-on. It can be used to read load pull data files, visualize and manipulate the data, combine multiple data files, create Artificial Neural Network (ANN) models for use in simulations, and write out new data files.

See also

To download the application, or for more information (including a nice demo video), visit the [Load Pull Data GUI page on the Knowledge Center](https://edadocs.software.keysight.com/pages/viewpage.action?pageId=816194640).


---

<!-- === 来源: howto/work_with_SystemVue_data.md === -->

# Work with SystemVue Data[](#work-with-systemvue-data "Link to this heading")

This section walks through an example of reading SystemVue datasets. SystemVue datasets are always contained within a SystemVue workspace files, which have a .wsv file extension.

Important

SystemVue dataset reading is only supported on Windows OS and Python 3.10.

Before reading SystemVue datasets, SystemVue 2023 or later must be installed and the `keysight-systemvue` library must be installed. The `keysight-systemvue` library is included as part of the SystemVue installation in the <SYSTEMVUE\_INSTALL\_DIR>/Bin/Python folder. You can install it using the following command (modify it to point to your exact installation location and SystemVue version).

```
> python -m pip install 'C:\Program Files\Keysight\SystemVue2024\Python\keysight_systemvue-2024.0-py3-none-any.whl'
```

The `keysight-systemvue` library has algorithms to search for your SystemVue installation folder. However, if you want or need to manually override it, you can do so by setting an environment variable `SYSTEMVUE_DIR` that points to the location of your SystemVue installation folder.

```
>>> import os
>>> os.environ['SYSTEMVUE_DIR'] = r'C:\Program Files\Keysight\SystemVue2024'
```

When writing scripts that read SystemVue datasets, it is necessary to use the `if __name__ == "__main__"` pattern. This pattern ensures that the multiprocessing code used inside `keysight-pwdatatools` works correctly. The following code snippet shows how to use this pattern.

```
if __name__ == "__main__":
    # Your code here
```

However, if you are using an interactive Python session, you don’t need to use this pattern. You can run the code directly in the interactive session. This includes running the code in a Jupyter notebook, VS Code’s Interactive Python window, or any other interactive Python environment.

Important

If you forget to use the `if __name__ == "__main__"` pattern in a script that reads SystemVue datasets, you will likely encounter a RuntimeError error.

## Explore a SystemVue workspace[](#explore-a-systemvue-workspace "Link to this heading")

It can be helpful to explore the datasets in a workspace before reading the data. One way to do it is by creating an instance of [`DataFile`](../api_reference/fileio/datafile/index.md#keysight.pwdatatools.DataFile "keysight.pwdatatools.DataFile") and using the [`DataFile.tree()`](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.tree.md#keysight.pwdatatools.DataFile.tree "keysight.pwdatatools.DataFile.tree") method to print the structure of the workspace. The following code snippet shows how to do this.

```
>>> from keysight import pwdatatools as pwdt
>>> if __name__ == "__main__":
>>>     datafile = pwdt.DataFile(r'C:\Program Files\Keysight\SystemVue2024\Examples\Comms\DQPSK Modem.wsv')
>>>     print(datafile.tree())
<[/] Group 'DQPSK Modem'>
├── <[0] Group 'DF1_Data'>
│   ├── <[0] Block '' with 2 Vars>
│   ├── <[1] Block '' with 2 Vars>
│   ├── <[2] Block '' with 2 Vars>
│   ├── <[3] Block '' with 2 Vars>
│   ├── <[4] Block '' with 2 Vars>
│   ├── <[5] Block '' with 2 Vars>
│   ├── <[6] Block '' with 2 Vars>
│   └── <[7] Block '' with 2 Vars>
└── <[1] Group 'DF3_Data'>
│   ├── <[0] Block '' with 2 Vars>
│   ├── <[1] Block '' with 2 Vars>
│   ├── <[2] Block '' with 2 Vars>
│   ├── <[3] Block '' with 2 Vars>
│   ├── <[4] Block '' with 2 Vars>
│   ├── <[5] Block '' with 2 Vars>
│   ├── <[6] Block '' with 2 Vars>
│   ├── <[7] Block '' with 2 Vars>
│   ├── <[8] Block '' with 2 Vars>
│   └── <[9] Block '' with 2 Vars>
```

So, examining the above tree printout tells us that the workspace contains two datasets, DF1\_Data and DF3\_Data. These datasets are represented as Groups. The DF1\_Data dataset contains 8 Blocks, and the DF3\_Data dataset contains 10 Blocks.

See also

If you aren’t familiar with Groups or Blocks, see [Universal Data Structures](../index.md#data-structs-section).

Each Block contains 2 variables. Note that the names of the Blocks are empty strings, which means that the Blocks don’t have names. This means we cannot reliably access the Blocks by name. Instead, when working with SystemVue workspaces and datasets, we must always access Blocks by index (position). Note that the index of each Block is shown in square brackets in the tree printout. The tree printout shows us the number of variables in each Block, but it doesn’t show us the names of the variables. There is another way to explore a SystemVue workspace without reading the data. This is accomplished by reading the SystemVue workspace and setting `data=False` in the file reading function or method (this is supported in all of the file reading functions and methods in pwdatatools). This reads the structure of the workspace without reading the data, which is typicaly faster and more memory efficient.

```
>>> from keysight import pwdatatools as pwdt
>>> if __name__ == "__main__":
>>>     wsv_group = pwdt.read_file_as_group(r'C:\Program Files\Keysight\SystemVue2024\Examples\Comms\DQPSK Modem.wsv', data=False)
>>>     print(wsv_group)
Group(
    <2 Groups>,
    name='DQPSK Modem',
    attrs={},
)
```

If we wanted to view all the variable names in a particular dataset, we could do so by using the [`Group.iter_blocks()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.iter_blocks.md#keysight.pwdatatools.Group.iter_blocks "keysight.pwdatatools.Group.iter_blocks") method, as shown below.

```
>>> # Iterate over the Blocks in the first dataset and print the varnames in each Block
>>> for block in wsv_group[0].iter_blocks():
...    print(block.varnames)
('Bits_In_Time', 'Bits_In')
('Bits_Out_Time', 'Bits_Out')
('F1__DemodQAMI_Time', 'F1__DemodQAMI')
('F1__DemodQAMQ_Time', 'F1__DemodQAMQ')
('F3__RRC_I_Mod_Time', 'F3__RRC_I_Mod')
('F3__RRC_Q_Mod_Time', 'F3__RRC_Q_Mod')
('ModulatorQAMI_Time', 'ModulatorQAMI')
('ModulatorQAMQ_Time', 'ModulatorQAMQ')
>>> # Iterate over the Blocks in the second dataset and print the varnames in each Block
>>> for block in wsv_group[1].iter_blocks():
...    print(block.varnames)
('Bits_In_Time', 'Bits_In')
('Bits_Out_Time', 'Bits_Out')
('Data1__RRC_I_Mod_Time', 'Data1__RRC_I_Mod')
('Data1__RRC_Q_Mod_Time', 'Data1__RRC_Q_Mod')
('Data2__S1_Time', 'Data2__S1')
('Data3__DemodQAMI_Time', 'Data3__DemodQAMI')
('Data3__DemodQAMQ_Time', 'Data3__DemodQAMQ')
('S1_Time', 'S1')
('S2_Phase_Freq', 'S2_Phase')
('S2_Power_Freq', 'S2_Power')
```

The above methodology is useful for exploring the structure of a SystemVue workspace without reading the data. Exploration without full reading of the data into memory saves both time and RAM, making your code more efficient. Once you understand the structure of the workspace, you can read the data contained within the needed Group(s) and/or Block(s). The following sections show how to read the data from a SystemVue workspace.

## Read data in a workspace[](#read-data-in-a-workspace "Link to this heading")

The following code snippet reads all datasets in one of SystemVue’s example workspaces. The returned object is a [`Group`](../api_reference/main/group/index.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group"). Each dataset in the workspace is also a Group. This approach does not take advantage of the information about the structure of the workspace that we obtained in the previous section. It is more efficient to read only the datasets that you need, which is shown later.

```
>>> from keysight import pwdatatools as pwdt
>>> if __name__ == "__main__":
>>>     wsv_group = pwdt.read_file_as_group(r'C:\Program Files\Keysight\SystemVue2024\Examples\Comms\DQPSK Modem.wsv')
>>>     print(wsv_group)
Group(
    <2 Groups>,
    name='DQPSK Modem',
    attrs={},
)
```

Another option is to read a single dataset from a workspace. The following code snippet reads the first dataset in the workspace. In order to use this approach, you need to know either the name or position of the dataset that you want. Note that the loc parameter can be used to specify either name or position. Note that the loc is always a string, even if you are using the position of the dataset.

```
>>> # using the name of the dataset
>>> ds1 = pwdt.read_file_as_group(r'C:\Program Files\Keysight\SystemVue2024\Examples\Comms\DQPSK Modem.wsv', loc='DF1_Data')
>>> # using the position of the dataset yields identical results
>>> ds1 = pwdt.read_file_as_group(r'C:\Program Files\Keysight\SystemVue2024\Examples\Comms\DQPSK Modem.wsv', loc='0')
>>> print(ds1)
Group(
    <8 Blocks>,
    name='DF1_Data',
    attrs={},
)
```

## Explore the variables[](#explore-the-variables "Link to this heading")

We can retrieve a variable from a dataset by indexing into the Group to get the Block containing the variable, and then indexing into the Block to get the variable. The following code snippet retrieves the variable Bits\_In from the first Block in the dataset.

```
>>> first_block_in_dataset = ds1.get_member_as_block(0)
>>> bits_in = first_block_in_dataset['Bits_In']
>>> print(bits_in)
Var(
    <bool data with shape (512,)>,
    name='Bits_In',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
```

If you know the name of the variable that you want to access, but you don’t know which Block in a dataset contains the variable, you can use the [`Group.iter_blocks()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.iter_blocks.md#keysight.pwdatatools.Group.iter_blocks "keysight.pwdatatools.Group.iter_blocks") method to iterate through all the Blocks and search for the variable by name. The below code snippet shows how to iterate over all the Blocks in the workspace’s datasets that contain the variable name S1. We use `recursive=True` to search all the datasets.

```
>>> for block in wsv_group.iter_blocks(recursive=True):
...    if 'S1' in block.varnames:
...        print(block)
Block(
    <'S1', ... with 16377 observations>,
    name='',
    ivarnames=('S1_Time',),
    attrs={},
)
```

If you want to search for a variable that has a particular role (instead of searching by variable name), you can do something like the below.

```
>>> for block in wsv_group.iter_blocks(recursive=True):
...    for var in block.iter_vars():
...        if var.has_role("power"):
...            print(var)
Var(
    <Float64 data with shape (16381,)>,
    name='S2_Power',
    dims=<empty Dims>,
    role='power',
    unit='W',
    attrs={'default_unit': ...},
)
```

See also

For more information on variable roles, see [roles](../api_reference/public_submodules/roles/index.md#roles-module).


---

<!-- === 来源: howto/write_a_file.md === -->

# Write a File[](#write-a-file "Link to this heading")

Data Tools has several functions and methods to write datafiles. You can use [`write_file()`](../api_reference/fileio/write_file.md#keysight.pwdatatools._api.funcs.write_file "keysight.pwdatatools._api.funcs.write_file"), [`Group.to_file()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.to_file.md#keysight.pwdatatools.Group.to_file "keysight.pwdatatools.Group.to_file"), or [`Block.to_file()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.to_file.md#keysight.pwdatatools.Block.to_file "keysight.pwdatatools.Block.to_file").

Before you attempt to write a file, make sure it is one of the supported file formats in `pwdatatools.options.writing.formats`.

See also

[File Extensions and Formats](../core_concepts/file_exts_and_formats.md#file-exts-and-formats)

Click on any of the below functions or methods to jump to their documentation:

* [`write_file()`](../api_reference/fileio/write_file.md#keysight.pwdatatools._api.funcs.write_file "keysight.pwdatatools._api.funcs.write_file")
* [`Group.to_file()`](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.to_file.md#keysight.pwdatatools.Group.to_file "keysight.pwdatatools.Group.to_file")
* [`Block.to_file()`](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.to_file.md#keysight.pwdatatools.Block.to_file "keysight.pwdatatools.Block.to_file")


---

