# Core Concepts
> **说明：** Core Concepts 相关页面。

> **何时使用：** 当你需要查阅 Core Concepts 相关内容时

---

## 本文件目录

- **All About Filepaths** (`core_concepts/all_about_filepaths.md`)
- **File Extensions and Formats** (`core_concepts/file_exts_and_formats.md`)
- **Core Concepts** (`core_concepts/index.md`)
- **Multi-Dimensional Data** (`core_concepts/multi_dimensional_data.md`)
- **pandas DataFrame Indexing** (`core_concepts/pandas_dataframe_indexing.md`)

---

<!-- === 来源: core_concepts/all_about_filepaths.md === -->

# All About Filepaths[](#all-about-filepaths "Link to this heading")

This section contains some tips for working with filepaths. Many of these tips are relevant not only to pwdatatools, but to Python in general. There are two notable Python stadard libraries that facilitate working with filepaths: `os` (more specifically, the `os.path` module) and `pathlib`. This section covers both of these libraries, as well as a class available in `keysight.pwdatatools` called [`DataFile`](../api_reference/_autosummary/keysight.pwdatatools.DataFile.md#keysight.pwdatatools.DataFile "keysight.pwdatatools.DataFile").

## String paths[](#string-paths "Link to this heading")

Filepaths can either be represented as strings or higher-level objects. If you are writing a quick Python script, it is easy to just copy a filepath and paste it into your code, as shown below.

```
>>> # On a Linux system
>>> from keysight import pwdatatools as pwdt
>>> group = pwdt.read_file('/home/username/Data/meaured_data.mdf')
```

The filepath above is defined as a Unicode string (the default string encoding in Python 3). In Python, strings are surrounded by either single or double quotes. The above code snippet works, assuming it is a valid path to a datafile. However, take a look at the below path on a Windows file system.

```
>>> # On a Windows system
>>> from keysight import pwdatatools as pwdt
>>> group = pwdt.read_file(r'C:\Users\username\Data\meaured_data.mdf')
```

In order to make the Windows path valid, the letter “r” has been prepended to the string. This syntax defines a *raw string* in Python. In regular strings, the backslashes are treated as escape characters, which is problematic when defining Windows filepaths since the path separators are backslashes (unlike Linux which uses forward slashes). By prepending the letter “r”, the string is treated as a raw string, and the backslashes are treated as literal characters.

The two below alternatives would also work on a Windows system. One solution is to use double backslashes, and the other is to convert backslashes to forward slashes. However, neither solution is convenient, because copy and paste from the Windows File Explorer will not work.

```
>>> # On a Windows system
>>> group = pwdt.read_file('C:\\Users\\username\\Data\\meaured_data.mdf')
>>> group = pwdt.read_file('C:/Users/username/Data/meaured_data.mdf')
```

## The os.path module[](#the-os-path-module "Link to this heading")

Copying and pasting a full filepath works great for some situations, but not for cases where the path needs to be programatically set or changed. Python has a standard library called `os` which contains a `path` module for defining and manipulating filepaths. Below, the `os.path` module is used to create a couple paths.

```
>>> import os
>>> homefolder = os.path.expanduser('~')
>>> print(homefolder)
C:\Users\username
>>> datafolder = os.path.join(homefolder, 'data')
>>> print(datafolder)
C:\Users\username\data
```

The above code assigns the full path to the user’s home directory to the variable `homefolder`. Then, the variable `datafolder` is created, which is a subfolder inside the user’s home folder. The benefits of creating a path this way vs. copying and pasting full string paths are 1) this code can potentially work for different users on different computers, and 2) this code can work for both Windows and Linux.

There is a subtle difference between printing a path using the `print()` function vs. directly viewing a path’s `__repr__()` (which is what you see when you type in a variable’s name at a Python prompt and then press enter). Note below how printing a path results in a nice-looking path without double backslashes or quotes around it. Contrast that with typing the path variable’s name into the prompt and pressing enter.

```
>>> # view printed output
>>> print(datafolder)
C:\Users\username\data
>>> # view __repr__ output
>>> datafolder
'C:\\Users\\username\\data'
```

Above, we created a path consisting of only directories (no file). As a next step, let’s include a file in a path. Also, let’s introduce some functions that help us distinguish between directories and files.

```
>>> mdfpath = os.path.join(datafolder, 'measured_data.mdf')
>>> print(mdfpath)
C:\Users\username\data\measured_data.mdf
>>> os.path.isdir(datafolder)
True
>>> os.path.isfile(mdfpath)
True
```

Any function or class in the pwdatatools library that accepts a filepath argument can accept a path created directly from `os.path` module, as shown below.

```
>>> from keysight import pwdatatools as pwdt
>>> group = pwdt.read_file(os.path.join(datafolder, 'measured_data.mdf'))
```

The `os.path` module contains other useful functions, such as `os.path.exists()`, `os.path.basename()`, `os.path.splitext()`, `os.path.dirname()`, and more. The below code block illustrates the use of some of these.

```
>>> os.path.exists(homefolder)
True
>>> os.path.basename(datafolder)
'data'
>>> os.path.splitext(mdfpath)
('C:\\Users\\username\\data\\measured_data', '.mdf')
>>> os.path.dirname(mdfpath)
'C:\\Users\\username\\data'
```

Below illustrates a methodology for iterating through files. Let’s assume `datafolder` contains two other .mdf files called “blah.mdf” and “foo.mdf”, and the goal is to translate all .mdf files to ADS datasets (.ds).

```
>>> files = os.listdir(datafolder)
>>> print(files)
['blah.mdf', 'foo.mdf', 'measured_data.mdf']
>>> for file in files:
...     mdfpath = os.path.join(myfolder, file)
...     dspath = os.path.splitext(mdfpath)[0] + '.ds'
...     pwdt.translate_file(mdfpath, dspath)
```

Any non-mdf files in the directory are skipped during iteration by checking the file extensions as shown below. If any of the output .ds files already exist, they need to be either manually deleted, or else the `dst_mode` argument to the `translate_file` function should be set to `'w'`.

```
>>> mdfs = [file for file in files if os.path.splitext(file)[0] == '.mdf']
>>> for file in mdfs:
...     mdfpath = os.path.join(myfolder, file)
...     dspath = os.path.splitext(mdfpath)[0] + '.ds'
...     pwdt.translate_file(mdfpath, dspath, 'w')
```

The `os` library has other path-related functions that are not in the `os.path` module but instead in the top-level `os` library namespace, such as `os.makedirs()`, `os.rmdir()`, `os.listdir()`, `os.chdir()`, `os.getcwd()`, and `os.rename()`. Check out these other functions if you are interested.

## The pathlib library[](#the-pathlib-library "Link to this heading")

Python has another standard library to facilitate creating and manipulating paths called `pathlib`. The `pathlib` library takes a fundamentally different approach than the `os` library. When using `pathlib`, paths are defined as objects: they are instances of the `pathlib.Path` class. These `pathlib.Path` objects can be of subtype `WindowsPath` or `PosixPath`. In contrast, all paths in the `os.path` module are ultimately represented as strings.

```
>>> # On a Linux system
>>> from pathlib import Path
>>> mypath = Path('/home/username/Documents')
>>> print(mypath)
/home/username/Documents
>>> mypath
PosixPath('/home/username/Documents')
```

```
>>> # On a Windows system
>>> from pathlib import Path
>>> mypath = Path(r'C:\Users\username\Documents')
>>> print(mypath)
C:\Users\username\Documents
>>> mypath
WindowsPath('C:/Users/username/Documents')
```

As shown above, instances of `pathlib.Path` can look slightly different depending on the OS, and whether or not the `print()` function is used.

The `pathlib` library has some nice conveniences for creating paths that you may find slightly easier than `os.path.join()`. Note that `pathlib` automatically uses the correct path separator based upon the OS. However, when creating the `filepath` variable below, always use a forward slash, even when using Windows OS.

```
>>> # On a Windows system
>>> mypath = Path(r'C:\Users\username\Documents')
>>> filepath = mypath / 'foo'/ 'blah.mdf'
>>> print(filepath)
C:\Users\username\Documents\foo\blah.mdf
>>> # On a Linux system
>>> mypath = Path(home/username/data')
>>> filepath = mypath / 'foo'/ 'blah.mdf'
>>> print(filepath)
home/username/data/foo/blah.mdf
```

## The DataFile class[](#the-datafile-class "Link to this heading")

pwdatatools provides a class called [`DataFile`](../api_reference/_autosummary/keysight.pwdatatools.DataFile.md#keysight.pwdatatools.DataFile "keysight.pwdatatools.DataFile"), which represents a file on disk (which may or may not exist yet). An instance of [`DataFile`](../api_reference/_autosummary/keysight.pwdatatools.DataFile.md#keysight.pwdatatools.DataFile "keysight.pwdatatools.DataFile") may be used as input to any pwdatatools function or method that acceots a filepath. For example, see below where a DataFile is the input argument to the `read_file()` function. Previously, it was shown that the `read_file()` function can also accept Python strings, `os.PathLike`, or `pathlib.Path` filepaths.

```
>>> # On a Windows system
>>> from keysight import pwdatatools as pwdt
>>> datafile = pwdt.DataFile(r'C:\Users\username\Data\meaured_data.mdf')
>>> group = pwdt.read_file(datafile)
```

This example just replicates something that can be done without needing the [`DataFile`](../api_reference/_autosummary/keysight.pwdatatools.DataFile.md#keysight.pwdatatools.DataFile "keysight.pwdatatools.DataFile") class, and therefore does not show the motivation behind using a DataFile. In order to see some good use cases for DataFiles, see [`DataFile`](../api_reference/_autosummary/keysight.pwdatatools.DataFile.md#keysight.pwdatatools.DataFile "keysight.pwdatatools.DataFile").


---

<!-- === 来源: core_concepts/file_exts_and_formats.md === -->

# File Extensions and Formats[](#file-extensions-and-formats "Link to this heading")

The `keysight.pwdatatools` library makes use of file extensions in order to determine file formats. All known file extensions and file formats are stored in `pwdatatools.options.files`. These global known file extensions and formats are not editable. If you need to read or write a file with an unrecogized or missing file extension, all file reading/writing functions and methods have `src_format` and `dst_format` parameters which can help. Alternatively, you can make a [`DataFile`](../api_reference/_autosummary/keysight.pwdatatools.DataFile.md#keysight.pwdatatools.DataFile "keysight.pwdatatools.DataFile") and use the `format_override` parameter.

```
>>> from keysight import pwdatatools as pwdt
>>> # missing file extension
>>> pwdt.read_file('/home/data/s_params')                       # Won't work because of missing file extension
>>> pwdt.read_file('/home/data/s_params', src_format='mdif')      # This works
>>> # unknown file extension
>>> pwdt.read_file('/home/data/s_params.foo')                   # Won't work because of unknown file extension
>>> pwdt.read_file('/home/data/s_params.foo', src_format='mdif')  # This works
>>> # using DataFile with missing file extension
>>> datafile = pwdt.DataFile('/home/data/noise_parameters', format_override='mdif')
>>> group = pwdt.read_file(datafile)   # This works because format_override is set for DataFile
```

Note

Touchstone file extensions are special in that they change vs. port numbers, and thus there are many valid Touchstone file extensions. For example, ‘.s2p’, ‘.s4p’, and ‘.s32p’ are all valid extensions. Since there are so many valid Touchstone file extensions, they cannot all be stored in the options. However, any valid Touchstone extension will be automatically detected when reading/writing files.

Below are the readable extensions and formats.

```
>>> from keysight import pwdatatools as pwdt
>>> pwdt.options.reading.format_to_extension_map
FormatToExtMap(
  {
    'ads': ('.ds',),
    'ads_text': (),
    'citi': ('.citi', '.cti'),
    'csv': ('.csv',),
    'farfieldio': ('.ffio',),
    'hfss_ffd': ('.ffd',),
    'loadpull': ('.cst', '.lp', '.lpacwave', '.lpc', '.lpcwave', '.lpd', '.lpwave', '.mat', '.sat', '.satwave', '.spl'),
    'mdif': ('.mdif', '.mdf'),
    'mdm': ('.mdm',),
    'native': ('.pwdt',),
    's2pmdif': (),
    'smatrixio': ('.sio',),
    'systemvue': ('.wsv',),
    'touchstone': ('.snp', '.ts'),
  }
)
```

Below are the writeable extensions and formats.

```
>>> pwdt.options.writing.format_to_extension_map
FormatToExtMap(
  {
    'ads': ('.ds',),
    'ads_text': (),
    'citi': ('.citi', '.cti'),
    'csv': ('.csv',),
    'mdif': ('.mdif', '.mdf'),
    'mdm': ('.mdm',),
    'native': ('.pwdt',),
    'smatrixio': ('.sio',),
    'touchstone': ('.snp', '.ts'),
  }
)
```


---

<!-- === 来源: core_concepts/index.md === -->

# Core Concepts[](#core-concepts "Link to this heading")

* [All About Filepaths](all_about_filepaths.md)
  + [String paths](all_about_filepaths.md#string-paths)
  + [The os.path module](all_about_filepaths.md#the-os-path-module)
  + [The pathlib library](all_about_filepaths.md#the-pathlib-library)
  + [The DataFile class](all_about_filepaths.md#the-datafile-class)
* [File Extensions and Formats](file_exts_and_formats.md)
* [Multi-Dimensional Data](multi_dimensional_data.md)
  + [Variable dependencies](multi_dimensional_data.md#variable-dependencies)
  + [Variable dimensionality](multi_dimensional_data.md#variable-dimensionality)
    - [Scalar](multi_dimensional_data.md#scalar)
    - [Vector](multi_dimensional_data.md#vector)
    - [Matrix](multi_dimensional_data.md#matrix)
* [pandas DataFrame Indexing](pandas_dataframe_indexing.md)
  + [Row indexing](pandas_dataframe_indexing.md#row-indexing)
  + [Column indexing](pandas_dataframe_indexing.md#column-indexing)


---

<!-- === 来源: core_concepts/multi_dimensional_data.md === -->

# Multi-Dimensional Data[](#multi-dimensional-data "Link to this heading")

The term “multi-dimensional data” here refers to two distinct aspects: [Variable dependencies](#variable-dependencies) and [Variable dimensionality](#variable-dimensionality).

## Variable dependencies[](#variable-dependencies "Link to this heading")

When using pwdatatools, it is helpful to have a general understanding of independent variables (called ivars) and dependent variables (called dvars).

Independent variables:
:   * These are the “input” variables that are being directly controlled, swept, set, changed, optimized, or statistically varied.
    * Some simulation and measurement examples are frequency, time, DC voltage for swept bias, RF power for swept input power, part parameter values e.g. inductance or capacitance,
      Monte Carlo Trial number (mcTrial), Batch Simulation number (batchNumber), etc.

Dependent variables:
:   * These are the “output” variables that are measured or calculated.
    * Examples are calculated node voltages or branch currents, S-parameters, power measured through a resistor, etc.

If a dataset contains more than one independent variable (ivar), it is *multi-dimensional*. Example: a swept S-parameters simulation vs freq and a capacitor value. The inner ivar is freq, and the outer ivar is capacitance. If a dataset contains one independent variable (ivar) it is not considered multi-dimensional. Example: S-parameters vs freq.

A multi-dimensional dataset
:   * has exactly one inner independent variable
    * has one or more outer independent variables
    * has one or more dependent variables

The ordering of independent variables (ivars) matters. Ivars depend on any other ivars further outside the nested sweep. The term “level” is used for describing the order. For outer ivar, its level is 0. For the inner ivar, its level is nlevels-1.

Let’s look at an ADS dataset as an example. In Figure 1, the ivars are *L1*, *C1*, and *freq*. The inner ivar *freq* depends on all outer ivars, so *freq* depends on both *L1* and *C1*. *C1* depends on *L1*. The outermost ivar *L1* only depends on itself (no other dependencies), and all dependent variables (e.g. *S11*) depend on all independent variables.

[![../_images/ads_variable_dependencies.png](../_images/ads_variable_dependencies.png)](../_images/ads_variable_dependencies.png)

Figure 1 - Examining variable dependencies in an ADS dataset with 3 ivars[](#id3 "Link to this image")

In ADS, the inner ivar is commonly *freq* or *time*, but it’s not always the case, such as for DC simulations. In Figure 2, the *IDS* current depends on both *VGS* (outer ivar) and *VDS* (inner ivar). This dataset resulted from a swept I-V curve simulation of a transistor model.

[![../_images/ads_dc_variable_dependencies.png](../_images/ads_dc_variable_dependencies.png)](../_images/ads_dc_variable_dependencies.png)

Figure 2 - Examining variable dependencies in an ADS dataset with 2 ivars[](#id4 "Link to this image")

Important

In `keysight.pwdatatools`, variable dependencies are set by the [`Block.ivarnames`](../api_reference/_autosummary/keysight.pwdatatools.Block.ivarnames.md#keysight.pwdatatools.Block.ivarnames "keysight.pwdatatools.Block.ivarnames") attribute.

## Variable dimensionality[](#variable-dimensionality "Link to this heading")

In a [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"), variables are stored as instances of [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var"). These Vars may have 1, 2, or 3 dimensions. Understanding variable dimensionality can be a bit confusing because there is usually an implicit dimension shared by all variables. For example, a “scalar” variable can be thought of as a 1D array instead of a true zero-dimensional (0D) scalar value. A “vector” variable is a 2D array, instead of a 1D array. A matrix variable is a 3D array. The number of observations in a [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") adds an “implicit” dimension to each variable. This implicit dimension is, by convention, represented by rows in a DataFrame or the first dimension of an array. In both cases, this shared dimension is known as axis 0. Below, we will use pandas DataFrames to help illustrate some of these concepts.

See also

The `keysight.pwdatatools` library supports various [pandas DataFrame Indexing](pandas_dataframe_indexing.md#pandas-dataframe-indexing) options when creating a pandas DataFrame from a [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block").

### Scalar[](#scalar "Link to this heading")

In the code snippet below, *floatvar*, *intvar*, *complexvar*, *strvar*, and *boolvar* are scalar variables presented in a pandas DataFrame.

```
>>> import pandas as pd
>>> df = pd.DataFrame(
...     {
...         "floatvar": [0.1, 0.5, 3.0],
...         "intvar": [4, 2, 7],
...         "complexvar": [1 + 2j, 2 + 5j, 3 - 2j],
...         "strvar": ["foo", "bar", "baz"],
...         "boolvar": [True, False, True],
...     }
... )
>>> print(df)
    floatvar  intvar  complexvar strvar  boolvar
0        0.1       4    1.0+2.0j    foo     True
1        0.5       2    2.0+5.0j    bar    False
2        3.0       7    3.0-2.0j    baz     True
```

In the above DataFrame, each scalar contains a single value at each observation (row). In the `keysight.pwdatatools` library, scalars may be of the following data types: integer, float, complex, boolean, or string. The term “scalar” might be a bit of a misnomer, since you can’t “scale” anything with a string or a boolean. However, the term “scalar” is used to distinguish it from a vector or matrix.

### Vector[](#vector "Link to this heading")

In the code snippet below, *intvar*, *floatvar*, *complexvar*, *boolvar*, and *strvar* are vector variables presented in a pandas DataFrame.

```
>>> pd.set_option('display.width', 200)
>>> df = pd.DataFrame(
...     {
...         "intvar[0]": [1, 5, 0],
...         "intvar[1]": [8, 7, 3],
...         "intvar[2]": [3, 3, 4],
...         "floatvar[1]": [0.12, 0.5, 1.51],
...         "floatvar[2]": [0.44, 0.32, 7.8],
...         "complexvar['a']": [1 + 2j, 2 + 5j, 3 - 2j],
...         "boolvar[10]": [True, False, True],
...         "boolvar[42]": [False, False, True],
...         "strvar[0]": ['pass', 'fail', 'pass'],
...         "strvar[1]": ['pass', 'fail', 'pass'],
...     }
... )
>>> print(df)
   intvar[0]  intvar[1]  intvar[2]  floatvar[1]  floatvar[2]  complexvar['a']  boolvar[10]  boolvar[42] strvar[0] strvar[1]
0          1          8          3         0.12         0.44         1.0+2.0j         True        False      pass      pass
1          5          7          3         0.50         0.32         2.0+5.0j        False        False      fail      fail
2          0          3          4         1.51         7.80         3.0-2.0j         True         True      pass      pass
```

If using a flat string Index for a DataFrame’s columns (as we are here), `keysight.pwdatatools` interprets square brackets as delimiters. The portion inside the square brackets is called an “embedded address”, or a “dimension scale”. Multi-dimensional variables (such as the vectors shown here) may have different types of scales used to index across their higher dimensions. The *intvar* variable is a vector that uses 0-based ints as the addresses (the ints inside the square brackets). The *floatvar* variable uses 1-based int addresses. The *complexvar* variable is a vector with a length of only 1 and uses a str address. The *boolvar* variable uses non-sequential int addresses. The *strvar* vectors uses 0-based ints. In the `keysight.pwdatatools` library, vectors can hold integer, float, complex, bool, or string data (these are the same supported data types as scalars). All columns of a vector must be of the same data type. For example, all of the *intvar* columns contain integer data, and both of the *boolvar* columns contain boolean data.

Note

Other tools (for example, ADS) only support 1-based integer vector dimension scales. Furthermore, any missing integer indexes can cause issues in other tools. In order to maintain compatibility with other tools, you must follow these rules. However, the `keysight.pwdatatools` library’s structures and the native .pwdt file format are flexible and fully support int, float, and str vector dimension scales, as well as missing or non-sequential dimension scales.

The above DataFrame can be used to instantiate a [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"). The DataFrame is converted to instances of [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") and stored in the Block. Note that the columns for each vector variable are combined into a single ndarray.

```
>>> from keysight import pwdatatools as pwdt
>>> block = pwdt.Block(df)
>>> print(block)
Block(
    <'intvar', 'floatvar', 'complexvar', 'boolvar', 'strvar', ... with 3 observations>,
    name='',
    ivarnames=(),
    attrs={},
)
```

The Block converts the embedded addresses and stores them in the [`Var.dims`](../api_reference/_autosummary/keysight.pwdatatools.Var.dims.md#keysight.pwdatatools.Var.dims "keysight.pwdatatools.Var.dims") attribute for each variable.

```
>>> block['intvar'].dims
Dims(
    ndim=2,
    i_nums=[0, 1, 2],
    i_names=None,
)
>>> block['floatvar'].dims
Dims(
    ndim=2,
    i_nums=[1, 2],
    i_names=None,
)
>>> block['complexvar'].dims
Dims(
    ndim=2,
    i_nums=None,
    i_names=['a'],
)
>>> block['boolvar'].dims
Dims(
    ndim=2,
    i_nums=[10, 42],
    i_names=None,
)
>>> block['strvar'].dims
Dims(
    ndim=2,
    i_nums=[0, 1],
    i_names=None,
)
```

A pandas DataFrame can be created from a Block by calling the [`Block.to_pandas_dataframe()`](../api_reference/_autosummary/keysight.pwdatatools.Block.to_pandas_dataframe.md#keysight.pwdatatools.Block.to_pandas_dataframe "keysight.pwdatatools.Block.to_pandas_dataframe") method. By default, this creates a DataFrame with a flat string column index containing embedded dimension scales.

```
>>> df_from_block = block.to_pandas_dataframe()
>>> print(df_from_block)
   intvar[0]  intvar[1]  intvar[2]  floatvar[1]  floatvar[2]  complexvar['a']  boolvar[10]  boolvar[42] strvar[0] strvar[1]
0          1          8          3         0.12         0.44         1.0+2.0j         True        False      pass      pass
1          5          7          3         0.50         0.32         2.0+5.0j        False        False      fail      fail
2          0          3          4         1.51         7.80         3.0-2.0j         True         True      pass      pass
```

The Block can optionally create a DataFrame with a column index that has default integer addresses instead of the variables’ dimension scales. This is done by setting `cols_default_ints_forced=True` when calling [`Block.to_pandas_dataframe()`](../api_reference/_autosummary/keysight.pwdatatools.Block.to_pandas_dataframe.md#keysight.pwdatatools.Block.to_pandas_dataframe "keysight.pwdatatools.Block.to_pandas_dataframe"). By default, these are 1-based integers, but there is an option to use 0-based integers as well. The reason the default is 1-based is because it is more compatible with other tools (such as ADS).

```
>>> df_from_block_with_default_ints = block.to_pandas_dataframe(cols_default_ints_forced=True)
>>> print(df_from_block_with_default_ints)
   intvar[1]  intvar[2]  intvar[3]  floatvar[1]  floatvar[2]  complexvar[1]  boolvar[1]  boolvar[2] strvar[1] strvar[2]
0          1          8          3         0.12         0.44       1.0+2.0j        True       False      pass      pass
1          5          7          3         0.50         0.32       2.0+5.0j       False       False      fail      fail
2          0          3          4         1.51         7.80       3.0-2.0j        True        True      pass      pass
```

We can also optionally create MultiIndex columns when creating the DataFrame. This is done by setting the `cols_nlevels=-1` (or any value greater than 1). The first level of the columns index is the variable name and the following level(s) are the dimension scale(s). In this case, we only need two total levels because the maximum number of dimensions for any variable in this Block is 2.

```
>>> df_multi = block.to_pandas_dataframe(cols_nlevels=-1)
>>> print(df_multi)
varname intvar       floatvar       complexvar boolvar        strvar
i            0  1  2        1     2          a      10     42      0     1
0            1  8  3     0.12  0.44   1.0+2.0j    True  False   pass  pass
1            5  7  3     0.50  0.32   2.0+5.0j   False  False   fail  fail
2            0  3  4     1.51  7.80   3.0-2.0j    True   True   pass  pass
```

If using a MultiIndex for the columns, the dimension scales are no longer strings that look like ints, but actual ints. This allows for nice ease-of-use when indexing into vectors, as shown below.

```
>>> df_multi['floatvar'][1]
0    0.12
1    0.50
2    1.51
Name: 1, dtype: float64
>>> df_multi['boolvar'][10]
0     True
1    False
2     True
Name: 1.2, dtype: bool
```

See also

For more info on pandas DataFrame indexing, see [pandas DataFrame Indexing](pandas_dataframe_indexing.md#pandas-dataframe-indexing).

### Matrix[](#matrix "Link to this heading")

In the code snippet below, *var1*, *var2*, and *var3* are matrix variables presented in a pandas DataFrame.

```
>>> df = pd.DataFrame(
...     {
...         "var1[1,1]": [1.1, 2.5, 9.0],
...         "var1[2,1]": [0.12, 0.5, 1.51],
...         "var1[1,2]": [0.74, 0.32, 7.8],
...         "var1[2,2]": [0.44, 0.2, 8.2],
...         "var2['foo','bar']": [1 + 2j, 2 + 5j, 3 - 2j],
...         "var2['foo','baz']": [7 + 4j, 4 + 5j, 1 + 9j],
...         "var3[0,'foo']": [True, False, True],
...         "var3[1,'foo']": [False, False, True],
...     }
... )
>>> print(df)
   var1[1,1]  var1[2,1]  var1[1,2]  var1[2,2]  var2['foo','bar']  var2['foo','baz']  var3[0,'foo']  var3[1,'foo']
0        1.1       0.12       0.74       0.44           1.0+2.0j           7.0+4.0j           True          False
1        2.5       0.50       0.32       0.20           2.0+5.0j           4.0+5.0j          False          False
2        9.0       1.51       7.80       8.20           3.0-2.0j           1.0+9.0j           True           True
```

By default, the `keysight.pwdatatools` library uses square brackets and commas as delimiters between the variable names and their embedded dimension scales. Matrix variables in DataFrames may be any one of the numpy or pandas dtypes that can hold integer, float, complex, bool, or string data. Note that numpy’s object dtype and pandas datetime dtype should be avoided. All columns of a matrix must be of the same dtype. For example, in Figure 5, note that each column associated *var1* is float. `keysight.pwdatatools` fully supports square (for example, *var1*) and non-square (for example, *var2* and *var3*) matrices.

A common example of a matrix variable is S-parameters, which have two dimensions (*output\_port*, *input\_port*), plus an implicit shared dimension (usually frequency, but it could include other dependencies as well).

Important

There is nothing stopping you from creating a DataFrame that contains a matrix variable with missing entries. For example, having columns ‘S[1,1]’, ‘S[1,2]’, and ‘S[2,2]’ with a missing ‘S[2,1]’ column. While this is allowed in a DataFrame, it can cause problems when performing certain tasks and should be avoided.

Note

Other tools (for example, ADS) only support 1-based integer matrix dimension scales. So, *var2* and *var3* could be problematic in some tools or file formats. In order to maintain compatibility with other tools, you must follow these rules. However, the `keysight.pwdatatools` library’s in-memory data structures and the native .pwdt file format are very flexible and fully support arbitrary integer and string dimension scales.

As shown previously for the vectors, we can convert a flat string column index containing embedded dimension scales to a MultiIndex. Again we create a [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") from the DataFrame, and use the method [`Block.to_pandas_dataframe()`](../api_reference/_autosummary/keysight.pwdatatools.Block.to_pandas_dataframe.md#keysight.pwdatatools.Block.to_pandas_dataframe "keysight.pwdatatools.Block.to_pandas_dataframe") to create a new DataFrame with MultiIndex columns.

```
>>> block = pwdt.Block(df)
>>> df_multi = block.to_pandas_dataframe(cols_nlevels=-1)
>>> print(df_multi)
varname var1                        var2             var3
i          1           2             foo                0      1
j          1     2     1     2       bar       baz    foo    foo
0        1.1  0.74  0.12  0.44  1.0+2.0j  7.0+4.0j   True  False
1        2.5  0.32  0.50  0.20  2.0+5.0j  4.0+5.0j  False  False
2        9.0  7.80  1.51  8.20  3.0-2.0j  1.0+9.0j   True   True
```

Note that again the Vars that were created when we converted the DataFrame to a Block store the dimensional scales that were extracted from the DataFrame’s columns. Also note how the scales for var3 are a mix of numeric and string values.

```
>>> block['var1'].dims
Dims(
    ndim=3,
    i_nums=[1, 2],
    i_names=None,
    j_nums=[1, 2],
    j_names=None,
)
>>> block['var2'].dims
Dims(
    ndim=3,
    i_nums=None,
    i_names=['foo'],
    j_nums=None,
    j_names=['bar', 'baz'],
)
>>> block['var3'].dims
Dims(
    ndim=3,
    i_nums=[0, 1],
    i_names=None,
    j_nums=None,
    j_names=['foo'],
)
```


---

<!-- === 来源: core_concepts/pandas_dataframe_indexing.md === -->

# pandas DataFrame Indexing[](#pandas-dataframe-indexing "Link to this heading")

There are very powerful indexing capabilities built into pandas DataFrames. Arranging the proper indexes in a DataFrame can greatly improve your ability to select subsets of data. There are two indexes in a DataFrame: a row index and a column index. If we follow the “tidy data” format, each column should hold a variable (or one portion of a multi-dimensional variable) and each row holds an observation. By default, a DataFrame’s row index is 0-based integer `pandas.RangeIndex`. The column index usually consists of the string variable names. In the case of multi-dimensional variables, there may also be dimensional info embedded in the strings. For example, ‘S[1,1]’ is one particular “entry” of a matrix variable “S” with i=1 and j=1.

See also

[Multi-Dimensional Data](multi_dimensional_data.md#multidim-data)

## Row indexing[](#row-indexing "Link to this heading")

Let’s start with some pandas DataFrame indexing examples using a default 0-based integer row index.

```
>>> import pandas as pd
>>> df = pd.DataFrame(
...     {
...         "var1": [0.1, 0.1, 0.5, 0.5],
...         "var2": [0, 2, 0, 2],
...         "var3": [1 + 2j, 2 + 5j, 3 - 2j, 7+1j],
...         "var4": ["foo", "bar", "baz", 'fizz'],
...         "var5": [True, False, True, True],
...     }
... )
>>> print(df)
   var1  var2      var3  var4   var5
0   0.1     0  1.0+2.0j   foo   True
1   0.1     2  2.0+5.0j   bar  False
2   0.5     0  3.0-2.0j   baz   True
3   0.5     2  7.0+1.0j  fizz   True
>>> df['var1'][0]  # select the first point of var1
0.1
>>> df['var1'][0:2]  # select the first two points of var1
0    0.1
1    0.1
Name: var1, dtype: float64
```

Now, let’s suppose that ‘var1’ and ‘var2’ are independent variables (ivars) for our dataset. Instead of using the default 0-based integer index for the rows, let’s use the values of our ivars as the row index.

```
>>> df = df.set_index(['var1', 'var2'])
>>> print(df)
               var3  var4   var5
var1 var2
0.1  0     1.0+2.0j   foo   True
     2     2.0+5.0j   bar  False
0.5  0     3.0-2.0j   baz   True
     2     7.0+1.0j  fizz   True
```

Note that the 0-based index on the left is gone and now ‘var1’ and ‘var2’ look a little different. That’s because they are no longer columns but instead are a `pandas.MultiIndex` for the DataFrame’s rows. Now, we can use ‘var1’ and ‘var2’ as our row indexers. This leads to some nice ease of use.

```
>>> df['var3'][0.1]  # select var3 values, but only where var1=0.1
var2
0    1.0+2.0j
2    2.0+5.0j
Name: var3, dtype: complex128
>>> df['var4'][:, 2]  # select var4 values, but only where var2=2
var1
0.1     bar
0.5    fizz
Name: var4, dtype: object
>>> df['var5'][0.5, 0]  # select var5 values, but only where var1=0.5 and var2=0
True
```

There is a third option for row indexing: create integer indexes for each ivar. There are several advantages to this approach. When there is more than one ivar, we can easily perform groupby operations using the integer row indexes. This allows us to iterate over the combinations of the ivars very reliably. The fact that we are using integers is an advantage over using floats or complex numbers because we avoid the risk of encountering problems related to small floating point differences. For example, in a measured load pull data file, one measured GammaLoad value might be 0.1113 + 0.2223j and the measurement system might record the next point as 0.1114 + 0.2225j. Despite the small differences, these points might need to be considered as the same Gamma point. Creating integer indexes can help with this problem. Another advantage to this indexing option over placing the ivar values into the row index is that the the ivar values remain in the columns and thus will be easier to use in calculations and plotting. Many built-in pandas DataFrame methods and third-party functions that operate on DataFrames work better if all the variables are in the columns.

Here is an example of creating integer indexes for the ivars in a DataFrame. We will use the same DataFrame as before, but this time we will create integer indexes for the ivars.

```
>>> df = df.reset_index()  # reset to the default 0-based integer index
>>> mi = pd.MultiIndex.from_product([[0, 1], [0, 1]], names=['var1_idx', 'var2_idx'])
>>> df.index = mi
>>> print(df)
                    var1  var2      var3  var4   var5
var1_idx var2_idx
0        0           0.1     0  1.0+2.0j   foo   True
         1           0.1     2  2.0+5.0j   bar  False
1        0           0.5     0  3.0-2.0j   baz   True
         1           0.5     2  7.0+1.0j  fizz   True
```

## Column indexing[](#column-indexing "Link to this heading")

A pandas DataFrame’s column index usually consists of string variable names. However, in the case of multi-dimensional variables, there may also be dimensional info embedded the column index. For example, ‘S[1,1]’ is one particular “entry” of a matrix variable “S” with i=1 and j=1. This is an example where the dimensional info is embedded in the string name of the column. We can also use multi-index columns to represent multi-dimensional variables, which allows for even more flexible indexing of the columns. For example, the columns for S[1,1] would be (‘S’, 1, 1), where ‘S’ is the string variable name, and the i and j labels are integers. `keysight.pwdatatools` has options for indexing that allow you to turn on and off multi-indexing for multi-dimensional variables, according to your preferences.

```
>>> # create DataFrame with one scalar, one vector, and one matrix variable with flat string index
>>> df = pd.DataFrame(
...     {
...         "freq": [1e9, 2e9, 3e9, 4e9, 5e9],
...         "S[1,1]": [6 + 2j, 2 + 5j, 3 - 2j, 7 + 1j, 1 - 1j],
...         "S[1,2]": [2 + 2j, 5 + 2j, 4 - 1j, 8 + 2j, 3 - 1j],
...         "S[2,1]": [1 + 8j, 2 + 5j, 3 - 1j, 7 + 1j, 2 + 5j],
...         "S[2,2]": [3 + 9j, 2 + 3j, 9 - 2j, 3 + 3j, 6 - 6j],
...         "PortZ[1]": [3 + 3j, 4 + 2j, 7 - 1j, 4 - 1j, 2 + 1j],
...         "PortZ[2]": [1 + 2j, 4 + 1j, 6 - 2j, 4 + 1j, 4 - 5j],
...     }
... )
>>> print(df)
           freq    S[1,1]    S[1,2]    S[2,1]    S[2,2]  PortZ[1]  PortZ[2]
0  1.000000e+09  6.0+2.0j  2.0+2.0j  1.0+8.0j  3.0+9.0j  3.0+3.0j  1.0+2.0j
1  2.000000e+09  2.0+5.0j  5.0+2.0j  2.0+5.0j  2.0+3.0j  4.0+2.0j  4.0+1.0j
2  3.000000e+09  3.0-2.0j  4.0-1.0j  3.0-1.0j  9.0-2.0j  7.0-1.0j  6.0-2.0j
3  4.000000e+09  7.0+1.0j  8.0+2.0j  7.0+1.0j  3.0+3.0j  4.0-1.0j  4.0+1.0j
4  5.000000e+09  1.0-1.0j  3.0-1.0j  2.0+5.0j  6.0-6.0j  2.0+1.0j  4.0-5.0j
```

Column indexing into flat string index for scalars, vectors, and matrices all works the same.

```
>>> df['freq']  # returns freq column as a Series
0    1.000000e+09
1    2.000000e+09
2    3.000000e+09
3    4.000000e+09
4    5.000000e+09
Name: freq, dtype: float64
>>> df['S[1,2]'] # returns one entry in the S matrix as a Series
0    2.0+2.0j
1    5.0+2.0j
2    4.0-1.0j
3    8.0+2.0j
4    3.0-1.0j
Name: S[1,2], dtype: complex128
>>> df['PortZ[1]'] # returns one entry in the PortZ vector as a Series
0    3.0+3.0j
1    4.0+2.0j
2    7.0-1.0j
3    4.0-1.0j
4    2.0+1.0j
Name: PortZ[1], dtype: complex128
```

Let’s make a new DataFrame for our data that uses a multi-level column index instead.

```
>>> mi = pd.MultiIndex.from_tuples(
...     [
...         ("freq", "", ""),
...         ("S", 1, 1),
...         ("S", 1, 2),
...         ("S", 2, 1),
...         ("S", 2, 2),
...         ("PortZ", 1, ""),
...         ("PortZ", 2, ""),
...     ],
...     names=["varname", "i", "j"],
... )
>>> df.columns = mi
>>> print(df)
           freq         S                                   PortZ
                        1                   2                   1         2
                        1         2         1         2
0  1.000000e+09  6.0+2.0j  2.0+2.0j  1.0+8.0j  3.0+9.0j  3.0+3.0j  1.0+2.0j
1  2.000000e+09  2.0+5.0j  5.0+2.0j  2.0+5.0j  2.0+3.0j  4.0+2.0j  4.0+1.0j
2  3.000000e+09  3.0-2.0j  4.0-1.0j  3.0-1.0j  9.0-2.0j  7.0-1.0j  6.0-2.0j
3  4.000000e+09  7.0+1.0j  8.0+2.0j  7.0+1.0j  3.0+3.0j  4.0-1.0j  4.0+1.0j
4  5.000000e+09  1.0-1.0j  3.0-1.0j  2.0+5.0j  6.0-6.0j  2.0+1.0j  4.0-5.0j
```

Now, let’s index into the multi-level columns.

```
>>> df['freq']  # indexing into the freq column stays the same because it's a scalar
0    1.000000e+09
1    2.000000e+09
2    3.000000e+09
3    4.000000e+09
4    5.000000e+09
Name: freq, dtype: float64
>>> df['S'][1,2]  # indexing into S[1,1] now uses actual integers
0    2.0+2.0j
1    5.0+2.0j
2    4.0-1.0j
3    8.0+2.0j
4    3.0-1.0j
Name: (1, 2), dtype: complex128
>>> df.S[1,2]  # another benefit is that we can index like this, using a dot
0    2.0+2.0j
1    5.0+2.0j
2    4.0-1.0j
3    8.0+2.0j
4    3.0-1.0j
Name: (1, 2), dtype: complex128
>>> sub_matrix = df.S[:][2]  # we can grab S[1,2] and S[2,2] like this, which returns a DataFrame
>>> print(sub_matrix)
          1         2
0  1.0+8.0j  3.0+9.0j
1  2.0+5.0j  2.0+3.0j
2  3.0-1.0j  9.0-2.0j
3  7.0+1.0j  3.0+3.0j
4  2.0+5.0j  6.0-6.0j
```


---

