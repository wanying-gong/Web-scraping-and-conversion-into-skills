# Root
> **说明：** Root 相关页面。

> **何时使用：** 当你需要查阅 Root 相关内容时

---

## 本文件目录

- **Changelog** (`changelog.md`)
- **Welcome to the PathWave Data Tools Docs** (`index.md`)
- **Initial Setup** (`initial_setup.md`)

---

<!-- === 来源: changelog.md === -->

# Changelog[](#changelog "Link to this heading")

## [0.12.1] - 2025-06-09[](#id2 "Link to this heading")

### Added[](#added "Link to this heading")

* Support for RedHat Enterprise Linux 7 was restored.

## [0.12.0] - 2025-06-03[](#id3 "Link to this heading")

### Added[](#id4 "Link to this heading")

* Support for Python 3.13.
* A new Group.get\_member method was added, and it can retrieve a member by string location or integer.
* New attributes for the Dims class: Dims.i\_names, Dims.i\_nums, Dims.j\_names, Dims.j\_nums for accessing the names and numbers of the i and j scales as DimScales. If you would like to access the scales as numpy ndarrays, you can use the DimScale.to\_numpy\_ndarray method.
* A new Touchstone file reader, written in Rust. This new reader is much faster than the Python-based reader, and is now enabled as the default. The new reader is not only faster, but supports more features of the Touchstone 2.0 specification. For more info, see the docs on how to work with S-parameter data. The old Python-based reader is still available by setting the global option pwdatatools.options.reading.format\_specific.touchstone.engine\_pref=”python”, but it will be removed in a future release.
* A new method Var.set\_data, which will eventually replace the method Var.set\_data\_in\_place.
* There are several new attributes and methods related to Var’s dimensional metadata. There is a new Var.idx attribute that returns either an unsigned integer index (as a DimScale) along axis 0, or None if it doesn’t exist. There are new methods Var.has\_idx and Var.has\_dims that check if the Var has non-empty dimensional metadata.
* A new method Block.iter\_sweep\_nodes, which is meant to replace the old Block.iter\_sections method. Not only does it have a new name, it has a new signature and behavior. It now returns a generator that yields sub-Blocks where each outer ivar has constant value.

### Removed[](#removed "Link to this heading")

* Support for Python 3.9. The minimum supported version of Python is now 3.10.
* Support for RedHat 7. The minimum supported version is now 8.
* The Var.data property was removed. Previously, this property returned a numpy ndarray or MaskedArray and a warning was generated. Now, the property is removed completely. Use the Var.to\_numpy\_ndarray or Var.to\_numpy\_maskedarray methods instead.
* The Var.has\_empty\_dims method was removed in favor of the new Var.has\_dims method.
* The Var.copy\_metadata\_in\_place method was removed. In order to achieve similar behavior, you must manually assign each attribute (Var.name, Var.role, Var.unit, Var.attrs, etc.) to the Var.
* The viz.draw\_smith\_chart function, which was previously deprecated, is now removed in favor of the newer viz.smith\_chart function.
* The Block.iter\_sections method was removed in favor of the new Block.iter\_sweep\_nodes method. The new method has a different signature and behavior, so you will need to update your code accordingly.

### Changed[](#changed "Link to this heading")

* The Group.get\_member\_as\_block, Group.get\_member\_as\_group, and Group.get\_member\_as\_loadpullblock methods were modified. The ability to cast members to another type of object was removed. Also, retrieval by string now works through multiple levels of hierarchy.
* There were numerous changes to roles. Refer to the roles module’s documentation to see the updates to the roles that Vars can have (s\_parameters, frequency, etc.). This includes some new terminology. Previously, roles were comprised of a single “main role” and zero or more “aux roles”. Now, the main role is called the “role base” and aux roles are known as “role qualifiers” instead.
* The way that Block’s idxs work in pwdatatools has changed. Previously, these were separate variables in a Block. Now, idxs are dimensional metadata associated with Vars (typically ivars in a Block). This has implications in several places in the API.
* The new current native file version was updated from 2.0 to 3.0 to support the new idxs framework. Note that the native file format is not considered stable from version to version of pwdatatools.
* Changed some of the parameters in Var.to\_pandas\_dataframe, Var.to\_pandas\_series, Var.from\_pandas\_dataframe, Var.from\_pandas\_series methods.
* A new in\_place parameter was added to the following Block methods: Block.drop\_vars, Block.fill\_nan, Block.fill\_null, Block.keep\_vars, Block.rename\_vars, Block.set\_vars, Block.sort\_observations, Block.sort\_observations\_by. If in\_place is True, each method modifies the Block in place and returns a reference to the modified Block. If in\_place is False, each method returns a new Block with the changes applied (and leaves the original Block unchanged). The default value for in\_place is False.
* A new in\_place parameter was added to the following Var methods: Var.fill\_nan, Var.fill\_null, Var.sort\_observations. If in\_place is True, each method modifies the Var in place and returns a reference to the modified Var. If in\_place is False, each method returns a new Var with the changes applied (and leaves the original Var unchanged). The default value for in\_place is False.

### Fixed[](#fixed "Link to this heading")

* Issues with reading some Maury load pull datafiles (.spl and .cst) related to UTF-8 encoding.
* Issues related to reading ADS datasets with multiple variables with the same role.
* Improved behavior for parsing portnames in the comments of Touchstone files.

### Deprecated[](#deprecated "Link to this heading")

* The method Var.set\_data\_in\_place is deprecated in favor of the new Var.set\_data method. The Var.set\_data\_in\_place method will be removed in a future release.
* The use of the parameter index=”idxs” into the method Block.to\_pandas\_dataframe has been deprecated. To get similar behavior, make sure to add idxs to the Block’s ivars first and then use the method with parameter set to index=”ivars”. The parameter index=”idxs” will be removed in a future release.
* The Block.drop\_vars\_in\_place, Block.keep\_vars\_in\_place, Block.rename\_vars\_in\_place, and Block.set\_vars\_in\_place methods are deprecated in favor of the new in\_place parameter. The old methods will be removed in a future release.

## [0.11.0] - 2024-09-30[](#id5 "Link to this heading")

### Added[](#id6 "Link to this heading")

* Better support for reading of MDM files (a file format used by Keysight’s device modeling and measurement software such as IC-CAP, WPE, MBP, MQA, and PD1000A). Now, more types of these files can be read, and there are added options for how ICCAP\_VALUES are handled.
* New native DataType classes to define the types of data in a Var: Boolean, Complex128, Complex64, Float64, Float32, Int64, Int32, Int16, Int8, UInt64, UInt32, UInt16, UInt8, and String. These datatypes are used by the Var class as optional input arguments during initialization. They are also returned from the Var.dtype property (in previous versions, this property returned a numpy dtype).
* Two new attributes to the Var class. The Var.block attribute returns the Block that contains the Var, or else None if the Var is not associated with a Block. The Var.kind attribute returns “idx’, ‘ivar’, or ‘dvar’, if it is stored in a Block. It returns None if the Var is not part of a Block. Any instance of Var can be associated with only one Block. But, using Var.pop removes the Var from the Block, and the Var’s block attribute is set back to None. The Var’s kind attribute is also set to None. The Var can then be added to another Block, and the block and kind attributes will be updated accordingly.
* A new Var.info method that returns a pandas Series containing a summary of the Var’s properties. This is used under the hood to generate a new, revamped output for the Block.info method, which places all the variables’ info Series outputs into a DataFrame.
* A new Var.replace method that can be used to replace the data and/or metadata, returning a new Var.
* New Var.fill\_nan and Var.fill\_null methods that fill NaN or null values, respectively. Both methods return a new Var.
* New Var.is\_nan and Var.is\_null methods that return a boolean array indicating whether each element in the Var is NaN or null, respectively.
* A new file reading parameter idxs that controls whether index variables are created during file reading. If idxs is set to True, idxs are created from the ivars for all file formats. If False, idxs are not created for any file formats. If ‘auto’, the default behavior is used, which is to create idxs from the ivars for certain file formats like loadpull, while not creating idxs for other file formats like ADS datasets. The idxs option is available as a global option at pwdatatools.options.reading.idxs, as well as a keyword argument to all file-reading methods and functions. The keyword argument takes precedence over the global option. There is also a related idxs\_tol global option and keyword argument that controls the tolerance for creating idxs from float and complex ivars. The default value is NaN, which means that idxs are created by using exact equality with no tolerance.
* A new viz.smith\_chart function with a new and improved Smith Chart. This will eventually totally replace the old viz.draw\_smith\_chart function (which is now deprecated). The new function produces a better, easier to read Smith Chart and can optionally create R and J text labels.
* A new Block.sort\_observations\_by method that sorts the observations in a Block by the values of one or more variables. The method returns a new Block with the observations sorted.
* New Block.fill\_nan Block.fill\_null methods fill NaNs and nulls, respectively. Both methods return a new Block.
* New experimental expressions framework for Block. This framework allows for the creation expressions that are dynamically calculated using Vars or other expressions as inputs. The expressions are stored in a new Block.exprs attribute.
* A new Dims class to store metadata related to a Var’s higher dimensions. Previously, Var’s dimensional metadata was stored in a more flexible DimsTuple. However, the DimsTuple was hard to use and its flexbility made certain things overly complicated. The new Dims class is easier to use but also less flexible. The Dims class enforces consistent names for higher dimensions (“i” and “j”). It also enforces having a maximum of two scales for each dimension: a numeric one (always called “nums”) and a string one (always called “names”). Previously, the number of scales in each dimension were completely arbitrary, and the scale names were also completely arbitrary. Note that the Dims class only supports up to a maximum of 3-dimensional Vars. This could be expanded in the future, if there are use cases for it.

### Changed[](#id7 "Link to this heading")

* Directly changing the Var.name property value is now supported. Before, trying to directly set a new value resulted in an error. If the Var is stored in a Block, the necessary changes automatically propagate to the Block.
* Directly accessing the Var.data property now returns a copy of the data in the Var, instead of the underlying ndarray. Accessing this property now generates a UserWarning. Any code that uses the Var.data property should be modified as soon as possible because this property will eventually be removed completely. This change was made to prevent mutation of the data array. If you want the data as a numpy object, it is recommended to use either Var.to\_numpy\_ndarray or Var.to\_numpy\_maskedarray. If you want the data as a pandas object, use Var.to\_pandas\_series or Var.to\_pandas\_dataframe. If you want to change the Var’s data, use either Var.replace or Var.set\_data\_in\_place.
* The Var.dtype attribute now returns a new native DataType, instead of a numpy dtype.
* The Var.dims attribute now returns a new Dims object, instead of a DimsTuple.
* Changed the Var.to\_pandas\_series, Var.to\_pandas\_dataframe, and Block.to\_pandas\_dataframe methods in order to account for the changes to Var.dims. This includes changes to the input parameters of the methods.
* The Block.info method now returns additional information about the variables in the Block, including their kinds, shapes, dims, attrs, and counts of nan and null values. What’s also changed is that all the rows in the returned pandas DataFrame contain string data. Previously, it was a mix between numeric and string data.
* pwdatatools now uses standard Python warnings, in addition to logging warnings. This means that you can now use the warnings module to filter out warnings from pwdatatools. Also, the default logging level for pwdatatools is now ‘error’, which means that only error messages are displayed by default. You can change the logging level to ‘debug’, ‘info’, or ‘warning’ to see more messages.
* The Block.sort\_observations method’s functionality was split into two separate methods: Block.sort\_observations and Block.sort\_observations\_by. The Block.sort\_observations method now sorts the observations using integer indices, while the Block.sort\_observations\_by method sorts the observations by the values of one or more variables. The Block.sort\_observations method used to perform both functions, but now it only sorts by integer indices.
* The Group.tree method now returns a string instead of printing. So now, if you want a printout, you have to use print(group.tree()).
* The DataFile.tree method now returns a string instead of printing. So now, if you want a printout, you have to use print(datafile.tree()).
* The viz module is updated with new Keysight color theme settings.
* Subtle changes to various Block and Group methods to make them more strictly adhere to the MutableMapping and MutableSequence interfaces.
* Slight changes to the function signatures for concatenate\_blocks and concatenate\_loadpullblocks.
* All references in the API to “N/A” or “masked” were changed to use the term “null”. Note that nulls in pwdatatools are treated differently than NaNs.
* The native file format (typically with .pwdt file extension) was updated to support the new Block expressions stored in Block.exprs, and the current native file format version is now 2.0.
* Changed name of “iccap” file format to “mdm” to reflect the fact that the format is used by other software packages besides IC-CAP.
* LoadPullBlock now supports multiple ZrefLoad variables for cases where ZrefLoad varies vs. frequency. Because of this added support, some of the methods related to ZrefLoad have been changed or removed.
* Changed the default variable names for roles related to reference impedance and port name to “ZrefLoad” and “PortName”, respectively.
* Changed the roles and default variable names of the DC voltages and currents when reading load pull datafiles to be ‘voltage.dc.input’, ‘voltage.dc.output’, ‘current.direct.input’, and ‘current.direct.output’. In previous versions, these contained ‘enumerated’ aux roles and their variable names contained integers. This is no longer the case. Their names are now ‘Vin’, ‘Vout’, ‘Iin’, and ‘Iout’, respectively.

### Removed[](#id8 "Link to this heading")

* Support for Python 3.8. The minimum supported version of Python is now 3.9.
* Reading and writing of IVI files is now removed because the keysight-cdm library is no longer being maintained. Instead, it is recommended to use the native binary file format introduced in pwdatatools version 0.9.0 (with .pwdt file extension).
* The Var.\_\_setitem\_\_ method is removed. This method allowed for the mutation of the underlying data array. This method was removed in order to prevent mutation of the underlying array. Use the Var.replace or Var.set\_data methods instead, which completely replace the data in a Var instead of mutating it.
* The Var.fill\_value attribute is removed. This attribute was used to store the fill value for numpy masked arrays.
* The Block.get\_data method is removed in order to be consistent with the changes to Var (especially the deprecation and eventual removal of Var.data). It’s recommended instead to use one of several Var retrieval methods, such as Block.get, Block.get\_var, Block.\_\_getitem\_\_, Block.pop, or others.
* The Group.tree\_str method is removed now that the Group.tree method returns a string instead of printing.
* The DataFile.tree\_str method is removed now that the DataFile.tree method returns a string instead of printing.
* The DimScale class is removed from the top-level API. See the new Dims class for similar functionality.
* The DimsTuple class is removed from the top-level API. See the new Dims class for similar functionality.
* The Dim class is removed from the top-level API. See the new Dims class for similar functionality.

### Deprecated[](#id9 "Link to this heading")

* The Var.data property is deprecated in favor of the Var.to\_numpy\_ndarray and Var.to\_numpy\_maskedarray methods. The Var.data property will be removed in a future release.
* The viz.draw\_smith\_chart function is deprecated in favor of the new viz.smith\_chart function.

## [0.10.0] - 2024-06-25[](#id10 "Link to this heading")

### Added[](#id11 "Link to this heading")

* Support for reading Maury’s .mat and .lp load pull datafile formats.
* Direct support for reading and writing CSV files. Before, CSV files were indirectly supported, but required users to write code that utilized 3rd party libraries like pandas. Now, you can read and write CSV files using all the available functions and methods in pwdatatools.
* Support for reading port names in Touchstone files. The port names are stored in the S-parameters Var’s dims property (which stores dimensional metadata) as a DimScale. See the docs on the Var class for more information on to perform various indexing operations using the port names.
* When performing partial file reading, support for positional values for loc is now supported for all file formats. For example, read\_file\_as\_block(‘./foo.mdf’, loc=’1’) will read the second block in the MDIF file (positional loc uses 0-based indexing).
* New Block.iter\_sections method to iterate over sections of a Block. Sections are created by grouping together observations that have the same values for a variable or more than one variable. There are two auto options, ‘ivars’ and ‘idxs’, which create sections based on the independent variables (ivars) or the index variables (idxs), respectively. However, you can also pass in arbitrary variable names to create the sections. This method is similar to iterating over sub-DataFrames using the pandas.DataFrame.groupby method.
* New Block.make\_idxs method to create integer index Vars from data Vars. Especially useful for creating idxs from ivars, but any data vars can be used.
* Better support for Keysight Wideband Active Load Pull (WALP) files. Now, more types of these files can be read as a LoadPullBlock, including those with and without A and B wave data.
* LoadPullBlock class now supports multiple gamma ivars. There is still only one gamma ivarname designated by the gamma\_ivarname attribute, but other gamma variables can be defined in the LoadPullBlock’s outer ivarnames.

### Changed[](#id12 "Link to this heading")

* The hard dependencies for pwdatatools now only includes numpy and pandas. The matplotlib and seaborn libraries are no longer required to use the library. However, if you want to use the plotting functions in pwdatatools, you will need to install matplotlib and seaborn.
* The matplotlib and seaborn libraries are not imported until they are needed (i.e. when calling a function or method that uses them).
* All file extensions are now case insensitive when reading and writing files. For example, now both .MDIF and .mdif are supported MDIF file extensions.
* When reading non-hierarchical data files (for example iccap, loadpull, hfss\_ffd, ffio) as a Group, the resulting Group’s name is now equal to the filename without the extension. Previously, the Group’s name was empty.
* When reading load pull data files, PinAvail is now the default power ivar, instead of PSource.
* Some changes were made to the naming rules for load pull variable names related to the logic of when a frequency suffix is added or not. Also, a new option related to this was added at pwdatatools.options.reading.format\_specific.loadpull.always\_freq\_suffixed.
* Some default variable names were changed (e.g. Gp -> GainP, Gt -> GainT, etc.) to be more descriptive.
* Some new variable roles were added (e.g. ‘gain.vector’).
* When writing MDIF files, empty Block names are now disallowed. Previously, empty Block names were auto-renamed to ‘Block’.
* The format for S2PMDIF files is now ‘s2pmdif’ instead of ‘mdif\_s2p’. Also, the S2PMDIF network and noise blocknames now have associated global options under options.reading.format\_specific.s2pmdif.network\_blockname and options.reading.format\_specific.s2pmdif.noise\_blockname, respectively. The default blocknames have also been changed to be the same as the default blocknames for Touchstone and SMatrixIO.
* The names of the keyword arguments for the Var.to\_pandas\_dataframe, Var.to\_pandas\_series, and Block.to\_pandas\_dataframe methods in order to make them easier to understand.

### Fixed[](#id13 "Link to this heading")

* Issue with reading Focus load pull files with mismatching source and load frequencies.
* Issue with reading Focus load pull files with bad (commented out with !) data observations. Those observations are now ignored.
* Issue with reading MDIF files where mixed case “Var” keywords were not recognized.
* Issue with reading S2PMDIF files where a missing column name line (line starting with %) caused problems. Now, files with missing column name lines are supported.
* Issue with reading Touchstone version 2.0 files.
* Issue with reading SystemVue datasets with empty independent variable data.

## [0.9.0] - 2024-02-28[](#id14 "Link to this heading")

### Added[](#id15 "Link to this heading")

* A new binary file format has been created for pwdatatools. It has great performance and robust metadata storage capabilities. The new binary format is called “native”, and its default file extension is .pwdt (which used to be the default extension for IVI files). This new format has the advantage over the existing IVI HDF5-based format in that it doesn’t depend on any libraries other than those in the Python standard library and numpy. In contrast, the IVI format depends on the h5py and keysight-cdm libraries. The two formats have similar read/write performance in terms of speed and memory usage. Also, both formats have complete coverage of all supported metadata of the pwdatatools library.

### Changed[](#id16 "Link to this heading")

* The IVI HDF5-based format has been renamed from “pwdt” to “ivi”, and the default file extension has been changed from “.pwdt” to “.ivif”.
* The h5py library is no longer a hard dependency of pwdatatools. If you want to use the IVI HDF5-based format, you will need to install h5py (if using pwdatatools inside of ADS Python, h5py is already installed).
* The keysight-cdm and h5py libraries do not get imported until they are needed, which fixes a problem that was causing crashes in ADS on Linux due to HDF5 library version incompatiblity between ADS and the h5py library. This allows users to use all non-HDF5-related features of pwdatatools in ADS on Linux until the HDF5 library version problem is resolved.
* scipy is no longer a hard dependency of pwdatatools. scipy is used for a small handful of load pull related functions and methods. If you need to use these functions, you will need to install scipy (if using pwdatatools inside of ADS Python, scipy is already installed).

## [0.8.0] - 2024-02-01[](#id17 "Link to this heading")

### Added[](#id18 "Link to this heading")

* A new Var class to store variable data and metadata in Blocks.
* Support for reading Touchstone version 2.0 files (this is in addition to the already-supported version 1.0 files). Not all features of version 2.0 are supported. For example, Matrix Format keyword values other than “Full” are not supported.
* Support for reading .ffio files, which are Keysight’s far field data file format.
* A new data parameter in all file-reading functions and class methods for a new metadata-only read mode, which is enabled when `data=False`. This allows for file reading that is usually much faster and allows for quick examination of metadata such as variable names, variable dtypes, variable shapes, and the file hierarchy.
* New methods are available for the DataFile class, including read\_as\_group, read\_as\_block, read\_as\_loadpullblock, and tree.
* New tricontourplot function to the viz module and a corresponding method LoadPullBlock.tricontourplot. Both use triangulation to perform contour plotting and support irregular data. These complement the existing viz.contourplot and LoadPullBlock.contourplot, which automatically interpolate the data into a regular grid before plotting.
* The Block class now implements the MutableMapping interface.
* The Group class now implements the MutableSequence interface.
* There are several new Block methods, including clear, drop\_observations, drop\_vars\_in\_place, fill\_masked, get, get\_data, items, keep\_observations, keep\_vars\_in\_place, keys, count\_observations, pop, rename\_vars\_in\_place, repeat\_observations, set\_data\_in\_place, set\_vars\_in\_place, sort\_observations, update, and values.
* There are several new Group methods, including append, count, clear, extend, flatten, flattened, index, insert, iter\_blocks, iter\_members, pop, remove, reverse.

### Changed[](#id19 "Link to this heading")

* Reorganized how data and metadata are stored in a Block. Blocks no longer store a pandas DataFrame and instead behave as a mapping of varname to Var. However, initializing a Block with a DataFrame (for example, `Block(df)`) is still supported. Variable-level metadata is now stored with each Var, and Block-level metadata is now stored in a property called `attrs`. The `attrs` property is a dictionary-like object that stores arbitrary metadata. The `attrs` property is available on all Block objects, including the generic Block and the specialized LoadPullBlock.
* Blocks and Groups now always have str names. Previously, they could have name equal to None. Now, a Block or Group without a name will have a name equal to the empty string.
* Formalized the concept of Block “idxs”, also known as “index variables”. Now, they are just a special type of variable, stored along with the rest of the variables, and denoted by the `idxnames` attribute.
* The Block’s \_\_getitem\_\_ method now returns a Var. Previously, it returned a new Block instance.
* Group metadata is now stored in an attribute called attrs. Previously, it was stored in a metadata attribute. This is consistent with the Block class.
* Unified the naming of variables across all datafile formats by mapping variables’ roles to their names. There is a new option in `pwdatatools.options.reading.varnames` that allows the user to specify the variable names to use for each role. There are pre-populated default names for common roles.
* New organization of data and metadata when reading S-parameters datafiles. Now, S-parameter (and noise) data and metadata is organized the same no matter if reading ADS datasets, Touchstone files, or SMatrixIO files.
* Renamed the LoadPullBlock’s apply\_grid method to grid\_data.
* Changed some aspects of how data and metadata are stored in pwdt files. Because of this change (and to help manage future changes), a VERSION attribute was added to each Group and Block stored in a .pwdt file. This attribute is used to determine how to read the object.
* pwdatatools now defaults to using the keysight-ads-dataset library when reading ADS datasets due to speed ups in the latest version of that library. If you do not have that library installed, reading ADS datasets still works, but it’s not as fast as when using the new library, and you will see a performance warning message.

### Removed[](#id20 "Link to this heading")

* The Block.data attribute, which used to store a DataFrame. You can still initialize a Block with a DataFrame directly like `Block(df)`, or via the new from\_pandas\_dataframe method. And a pandas DataFrame can be created from a Block using the Block.to\_pandas\_dataframe method.
* The global option for reading.indexing. This is no longer needed, since the Block object no longer stores DataFrame objects.
* The global option for reading.dtypes and also dtypes-related parameters from all file reading functions and methods.
* The Group method find\_blocks\_with\_varname was removed in favor of the new iter\_blocks method. You can search for the desired varnames in each Block during iteration, like this:

  > ```
  > for block in group.iter_blocks():
  >     if 'foo' in block:
  >         # do something with block
  > ```

### Fixed[](#id21 "Link to this heading")

* Various issues with reading Maury and Focus load pull datafiles.
* Load Pull polar gridding issues.
* Issues with writing Blocks to data files where the ivars were not written if the Block has idxnames.

## [0.7.0] - 2023-06-22[](#id22 "Link to this heading")

### Added[](#id23 "Link to this heading")

* New circular parameter was added to the LoadPullBlock.drop\_grid\_edges method to provide better control over how polar grid edges are dropped.
* Reading of load pull datafiles now requires an ADS Data Display license.

### Changed[](#id24 "Link to this heading")

* Cleaned up top-level API so that modules meant to be private start with underscores.
* Several type annotations to allow for numpy ints and float, in addition to already-supported Python ints and floats.
* Some of LoadPullBlock’s method signatures (changed some parameter names and removed others).

### Fixed[](#id25 "Link to this heading")

* Issue with importing calc and viz modules that prevented users from seeing the functions and classes that are available (and their docstrings).
* Issues with LoadPullBlock.regularize\_power\_ivar and LoadPullBlock.at\_gcomp methods when load pull data has repeated power values in the same gamma point.
* Issues with automatic polar grid extents calculation in the LoadPullBlock.apply\_grid method.
* Issues with type annotations in the calc module.
* Issue with reading empty portions of SystemVue datasets.

## [0.6.0] - 2023-05-15[](#id26 "Link to this heading")

### Added[](#id27 "Link to this heading")

* Support for Python 3.11.
* A new top-level `version` function to get the pwdatatools version.
* A new loadpull module for processing Load Pull data. This module includes a new class called LoadPullBlock that provides most of the new functionality.
* New viz module for data plotting and visualization. This module requires matplotlib and seaborn in order to be fully functional, but matplotlib and seaborn were not added as pwdatatools dependencies.
* Dependency on scipy (to support loadpull and viz modules).
* New top-level functions read\_file\_as\_group, read\_file\_as\_block, and read\_file\_as\_loadpullblock. The old read\_file function is still available, but may become deprecated in the future.
* Full support for reading SystemVue datasets. Requires installation of the keysight-systemvue Python library and SystemVue 2023 or later. It is only supported on Windows OS and Python 3.10.
* Support for reading HFSS far field data files (.ffd and portmap files)
* New format-specific global options for file reading and writing.
* New indexing and iteration methods for Blocks, including ones that mirror those built-in to pandas DataFrame. Examples are `Block.iloc`, `Block.loc`, `Block.xs`, `Block.drop`, and `Block.groupby`. The benefit of using these over the built-in pandas attributes and methods is that the Block’s versions handle metadata. Note that these attrs and methods are available on all pandas-DataFrame-based Block objects, including the generic Block and the specialized LoadPullBlock.
* Formalized the concepts of variable roles, idxnames, and colnames, which are all stored as metadata.
* New mapping objects to store metadata: BlockMetadata, GroupMetadata, VarsMetadata, AttrsDict, ColnamesMap, IdxnamesMap, RolesMap, UnitsDict.
* Support for pandas 2.0 and later.

### Changed[](#id28 "Link to this heading")

* Changed all references of a file’s “type” to “format”, in order to provide more clarity. For example, the src\_type argument to the read\_file function was changed to src\_format, and the attribute pwdatatools.options.files.readable\_types was renamed to pwdatatools.options.reading.formats. These are just two examples. There are many more.
* The global options have been reorganized.
* The way that metadata is stored in Groups and Blocks.
* Better organized docs.
* Indexing behavior of Blocks when getting items with square brackets. In previous versions, block[‘foo’] returned either a pandas Series or a pandas DataFrame, depending on whether ‘foo’ refers to a single column or a multi-dim variable from a Block with a MultiIndex column index. Now, block[‘foo’] always returns a new Block instance. The key(s) select the dvars in the Block to keep. So, you can also do block[[‘foo’, ‘bar’]] to create a new Block with only the dvars named ‘foo’ and ‘bar’. However, all ivars and idxs are always automatically included.
* Unified the variable names for all supported load pull data file formats. Now, if you import Maury, Focus, or Keysight load pull files, the variable names are consistent and settable in the global options.

### Removed[](#id29 "Link to this heading")

* The filter\_dataframe amd filter\_series functions were removed from the calc module. Use keepwhere\_dataframe or drop\_where\_dataframe instead.
* The DataFilter class was removed. The keepwhere\_dataframe and drop\_where\_dataframe functions have all the arguments that used to be contained within DataFilter.

### Fixed[](#id30 "Link to this heading")

* Fixed some issues with reading impedances from the header in Focus files. Also, added fail safes so that if parsing fails, it no longer crashes and instead returns NaN impedance(s).

## [0.5.0] - 2022-09-14[](#id31 "Link to this heading")

### Removed[](#id32 "Link to this heading")

* Undocumented plotting module. The plotting module will remain as a part of Data Tools Add-Ons, for now.
* Dependencies on matplotlib, seaborn, and scipy.

## [0.4.0] - 2022-09-14[](#id33 "Link to this heading")

### Added[](#id34 "Link to this heading")

* A new plotting module that builds off of matplotlib and seaborn to provide a consistent and flexible plotting interface. It provides new RectChart and SmithChart classes, as well as RectChartGrid and SmithChartGrid for producing gridded multi-plots (a technique known as faceting or small-multiples). Each chart class has methods for creating line plots, scatter plots, and contour plots. This module is still experimental and may change in future releases.
* A new calc module that provides a number of useful functions for engineering-related calculations and transformations (dB, dBm, etc.). This module currently has a limited number of functions, but will grow in future releases.
* Support for reading S2PMDIF files.
* For ADS dataset writing, increased the speed and reduced the need for intermediate file generation. To get these improvements, you must also have the keysight-ads-dataset library installed.
* Dependencies on matplotlib and seaborn, to support the new plotting module.

### Changed[](#id35 "Link to this heading")

* Got rid of Group.shared\_namespace attribute in favor of a new Group.find\_blocks\_with\_varname() method.

### Removed[](#id36 "Link to this heading")

* Support for Python 3.7
* Dependency on typing-extensions (which was only used for Python 3.7 support)

## [0.3.1] - 2022-04-26[](#id37 "Link to this heading")

### Fixed[](#id38 "Link to this heading")

* Some docs and docstring issues

## [0.3.0] - 2022-04-25[](#id39 "Link to this heading")

### Added[](#id40 "Link to this heading")

* New dependencies: h5py and typing-extensions Python libraries.
* Support writing of additional types of datafiles, including Touchstone (currently limited to Touchstone 1.0 spec), CITI, and SMatrixIO.
* Support for bool variables in MDIFs in the Python parser.
* Better support for ICCAP mdm data files. Previously, only mdm files from the 1/f ALFNA noise measurements system were supported for reading. Now, any mdm file should be able to be read (that’s the goal at least). Also, the imported header data is better organized.
* Better support for Focus and Maury loadpull reading. The data and metadata are better organized. Also, new types of loadpull datafiles are supported.
* NaN values are now supported when writing to MDIFs and ADS datasets.
* More options were added to allow users to dynamically control behavior wrt indexing, invalid data handling, and more. All options are collected into one place under pwdatatools.options.
* Block objects now have an metadata property which allows for storage of arbitrary metadata.

### Changed[](#id41 "Link to this heading")

* Changed Python version requirement to be at least 3.7, instead of 3.6.
* Package name is now keysight-pwdatatools, which makes it a namespace package and changes how users import the library in their scripts.
* Bumped pandas version in dependencies.
* Changed main top-level class names from `DataBlock` and `DataStore` to `Block` and `Group`.
* Better support for multi-dimensional variables.
* Groups can store other Groups. Previously, a DataStore (which is replaced by Group) could only store DataBlocks (replaced by Blocks). Now, Groups can store Blocks and other Groups.
* Changed default logging level to ‘warning’, which will suppress info messages.
* Removed mdf\_units argument from file read functions and methods. The functions and methods will automatically invoke units parsing if needed.
* Changed the organization of loadpull data when loadpull datafiles are read.
* The native HDF5 file format changed to one that is compliant with the IVI specifications.
* Reading a datafile no longer auto-generates an HDF5 file.

### Fixed[](#id42 "Link to this heading")

* The Python MDIF parser was previously unable to handle some MDIF files which use “wrapped” lines. The Python MDIF parser now supports this (the ADS MDIF parser already supported it).

### Removed[](#id43 "Link to this heading")

* Removed an undocumented module called dds that could create ADS Data Display windows from scratch.
* Removed an undocumented plotting module with some functions for generating matplotlib plots.
* Removed Block’s comments and units properties (use metadata instead).

## [0.2.1] - 2021-02-04[](#id44 "Link to this heading")

### Fixed[](#id45 "Link to this heading")

* Fixed issues with writing loadpull data to ADS datasets.

## [0.2.0] - 2021-02-01[](#id46 "Link to this heading")

### Added[](#id47 "Link to this heading")

* New to\_file and from\_file methods for DataStore and DataBlock.
* New base classes for DataBlock and DataStore. Doesn’t affect users, just developers.
* Started using `black` for all Python code formatting.
* New methods for the Directories class, including refresh, reset, and update.
* New tests for dirs object.

### Changed[](#id48 "Link to this heading")

* All file-format-specific DataBlock and DataStore methods (from\_ds, from\_mdf, to\_ds, to\_hdf, etc.) are now private methods. This reduces the number of top-level methods and simplifies the UI quite a bit. It also makes it so that as more and more file formats are supported, the API doesn’t get too cluttered.
* Changed to a new settings.json file format to store install directories.

### Fixed[](#id49 "Link to this heading")

* Updated the docs to reflect the new file read and write methods.
* Improved the isolation of tests by using temporary directories when reading and writing files.

## [0.1.0] - 2021-01-12[](#id50 "Link to this heading")

### Added[](#id51 "Link to this heading")

* First release


---

<!-- === 来源: index.md === -->

# Welcome to the PathWave Data Tools Docs[](#welcome-to-the-pathwave-data-tools-docs "Link to this heading")

PathWave Data Tools (also known as `pwdatatools`) is a Python library that makes it easy to work with all types of data. It enables you to combine PathWave and Python for a highly flexible data workflow. The library provides three main benefits: [Universal Data Structures](#data-structs-section), [Easy and Consistent File I/O](#file-io-section), and [Application-Specific Functionality](#app-specific-section).

## Universal Data Structures[](#universal-data-structures "Link to this heading")

PathWave Data Tools defines powerful Python-based data structures that can represent (in memory) any type of dataset. No matter the source(s) of your data, when you read it into these Python objects, the data and metadata are always structured in a consistent manner. This consistency enables easy combination and manipulation of data from virtually any source. If you learn how to use these objects, you can work with any kind of dataset in Python!

Before we discuss these objects, we need to explain the concept of a hierarchical dataset, which motivates some of the design decisions in PathWave Data Tools.

### Hierarchical datasets[](#hierarchical-datasets "Link to this heading")

PathWave Data Tools provides Python objects that can represent any dataset, including those with hierarchy. Examples of hierarchical file formats are [HDF5](https://www.hdfgroup.org/solutions/hdf5), ADS datasets (.ds files), and MDIF files. Even though a hierarchical dataset may exist as a single file on your computer, it can be helpful to think of it as a directory tree. There is a top-level “folder” which contains everything. But this is not an actual folder on your computer… it is a virtual folder or location within the datafile. This top-level location is analogous to the root folder “/” on a Linux system. There could also be more sub-folders within the root folder which create more groups. Within these groups, there may be different “datablocks”. In our file system analogy, these datablocks (or blocks) are the files (but remember… all these blocks are inside a single file on your computer). Although the blocks are grouped together into virtual folders, they are still independent from one another. Each block has its own data and metadata.

[![_images/directory_tree.png](_images/directory_tree.png)](_images/directory_tree.png)

Figure 1 - Hierarchical dataset as a directory tree[](#id1 "Link to this image")

### Hierarchical Python objects[](#hierarchical-python-objects "Link to this heading")

Below is a simplified illustration of how PathWave Data Tools organizes hierarchical datasets into two Python object types: the [`Group`](api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") and the [`Block`](api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"). Each Block stores its own variables as [`Var`](api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") objects. Multiple levels of hierarchical Groups are possible, because each member of a Group may be a Block, or another Group.

[![_images/Group_and_Block_illustration1.png](_images/Group_and_Block_illustration1.png)](_images/Group_and_Block_illustration1.png)

Figure 2 - PathWave Data Tools supports datasets from simulations and measurements, including hierarchical datafile formats[](#id2 "Link to this image")

There are many Python libraries that define their own data objects. For example, numpy has the ndarray, pandas has the Series and DataFrame, and xarray has the DataArray and the Dataset. So, why do you need pwdatatools if you are already using libraries like numpy, pandas, or xarray? Here are some reasons:

* Hierarchical datasets cannot be easily or cleanly stored in a single pandas.DataFrame, numpy.ndarray, or xarray.Dataset. Hierarchical datafile formats include HDF5 files, ADS datasets, generic MDIFs, CITIfiles, and others. pwdatatools helps you express the relationships between the subsets of the data with the [`Group`](api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") object. You can establish parent-child or sibling-sibling types of relationships. You can also maintain an ordering of the Group’s members in a list (the ordering of nested datasets in some hierarchical dataset formats is significant). Also, the Group can store additional arbitrary metadata in the [`Group.attrs`](api_reference/_autosummary/keysight.pwdatatools.Group.attrs.md#keysight.pwdatatools.Group.attrs "keysight.pwdatatools.Group.attrs") property, which brings us to the next reason…
* pandas, numpy, and xarray have fairly limited capabilities with respect to storing and persisting metadata (although xarray probably does the best when compared to the other two). The [`Block`](api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") and [`Group`](api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") classes can store a lot of different types of metadata. This metadata may be stored in the native pwdatatools file format.

See also

For more information about how to use [`Var`](api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var"), [`Block`](api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"), and [`Group`](api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group"), see [Use the Var Class](howto/use_var_class.md#use-var-class), [Use the Block Class](howto/use_block_class.md#use-block-class), and [Use the Group Class](howto/use_group_class.md#use-group-class).

## Easy and Consistent File I/O[](#easy-and-consistent-file-i-o "Link to this heading")

Data Tools has easy and consistent file input/output for your data, supporting many proprietary and industry-standard file formats. No matter what format(s) you read, datafiles are represented in Python in a consistent way (as detailed in the section [Universal Data Structures](#data-structs-section)). This makes it easy to manipulate or combine datasets. Ultimately, you may want to write these data structures to new datafiles. Or, you can directly translate from one file format to another. The supported file formats are listed in the table below.

| File Format | Description | Typical File Extensions | Read | Write |
| --- | --- | --- | --- | --- |
| PathWave Data Tools native files | A binary datafile format with great performance and robust metadata storage. Supports any arbitrary number of levels of hierarchy | .pwdt | Yes | Yes |
| PathWave Advanced Design System (ADS) datasets | Keysight’s proprietary binary dataset format for ADS. Supports one level of hierarchy | .ds | Yes | Yes |
| MDM (Measured Data Management) datafiles | Text format used by various Keysight modeling and measurement software such as IC-CAP, WPE, MBP, MQA, and PD1000A. Not hierarchical | .mdm | Yes | No |
| PathWave System Design (SystemVue) datasets | Keysight’s proprietary format, stored within SystemVue workspaces. Each dataset supports one level of hierarchy | .wsv | Yes | No |
| Generic MDIFs (Measurement Data Interchange Format) files | A popular, general-purpose text format. Supports one level of hierarchy | .mdf .mdif | Yes | Yes |
| Comma-separated values (CSV) files | Comma-delimited text format (tab-delimited files also supported). Not hierarchical | .csv | Yes | Yes |
| CITI (Common Instrumentation Transfer and Interchange) files | A general-purpose text format. Supports one level of hierarchy | .cti .citi | Yes | Yes |
| S2PMDIF files | A specialized MDIF format for S-parameters. Supports one level of hierarchy for noise parameters | .s2p | Yes | No |
| Touchstone files | The most popular text format for S-parameters. Supports one level of hierarchy for noise parameters | .snp .ts | Yes | Yes |
| SMatrixIO files | A highly-efficient Keysight proprietary binary format for S-parameters. Not hierarchical | .sio | Yes | Yes |
| Load Pull datafiles | Supports many formats from Keysight, Focus, and Maury measurement systems. Not hierarchical | .cst .lp .lpacwave .lpc .lpcwave .lpd .lpwave .mat .sat .satwave .spl | Yes | No |
| Electromagnetic far field datafiles | Supports Keysight’s ffio format and the HFSS ffd format. Not hierarchical | .ffio .ffd | Yes | No |

In addition to the formats listed in the table, many other formats are *indirectly* supported by using 3rd party libraries together with pwdatatools. Examples are JSON, Excel’s .xlsx, and more…

See also

To learn more about how file I/O works in pwdatatools, see [Read a File](howto/read_a_file.md#read-a-file), [Write a File](howto/write_a_file.md#write-a-file), and [Translate a File](howto/translate_a_file.md#translate-a-file).

## Application-Specific Functionality[](#application-specific-functionality "Link to this heading")

The `keysight.pwdatatools` library adds domain knowledge to your data and metadata. For example, it provides specialized Block objects for different applications. One example is the [`LoadPullBlock`](api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock"), which has many special methods for manipulating load pull data. For more information, see [Work with Load Pull Data](howto/work_with_loadpull_data.md#work-with-load-pull-data).

Also, the [`keysight.pwdatatools.calc`](api_reference/_autosummary/keysight.pwdatatools.calc.md#module-keysight.pwdatatools.calc "keysight.pwdatatools.calc") module provides a variety of functions for performing common engineering calculations. For example, it has functions for converting to and from decibels, converting between impedances and gammas, and more.

## Summary[](#summary "Link to this heading")

In summary, PathWave Data Tools extends the capabilities of other libraries like pandas, numpy, and xarray to include hierarchical datasets, robust treatment of metadata, and application-specific methods and functions. It also supports a wide variety of file formats. The most flexible format is the native `pwdatatools` format because it is the most capable with respect to metadata and hierarchy. The native file format is also among the best in read/write times and compactness.


---

<!-- === 来源: initial_setup.md === -->

# Initial Setup[](#initial-setup "Link to this heading")

## Installation[](#installation "Link to this heading")

These instructions describe how to use `pip` to install Data Tools. Note that `pip` will also install or update the Python libraries listed in [Dependencies](#dependencies).

Warning

These instructions assume you are using a standard Python distribution from [python.org](https://www.python.org), and are not appropriate for Anaconda. If you are using Anaconda, refer to [their website](https://www.anaconda.com/) for instructions on how to properly install a Python wheel into your Anaconda environment.

Note

You can ignore these installation instructions if you are using the Python environment that is included in ADS because `pwdatatools` and all its dependencies are already installed.

You won’t find `pwdatatools` on PyPI.org, so unless you’re a Keysight employee, you won’t be able to pip install `pwdatatools` from the web like most Python libraries you are using. You will have to obtain a wheel file from our Knowledge Center or from a product that includes it (for example ADS). You can obtain the wheel file from the Knowledge Center here: <https://edadocs.software.keysight.com/pages/viewpage.action?pageId=748497656>.

See also

If you are new to installing Python packages, refer to the [Python Packaging User Guide](https://packaging.python.org/tutorials/installing-packages/).

Below shows how to pip install a `pwdatatools` wheel file. It assumes you have already downloaded the wheel file to some local folder on your computer.

```
> pip install keysight_pwdatatools-0.11.0-cp312-cp312-win_amd64.whl
```

Note

There are several wheel files created for each release of `pwdatatools`. Each wheel is targeted to one version of Python and one operating system (Windows or Linux). Verify that the wheel file that you have matches your version of Python and the operating system that you are using. Also, when you install it, be sure you are invoking the correct version of pip that is associated with your desired Python environment. The aforementioned tutorial on installing packages covers this, as well as how to create and activate a Python virtual environment (a good practice).

Some capabilities in `pwdatatools` rely on having ADS or SystemVue installed. See [Keysight software](#keysight-software) for more details.

Important

An ADS Data Display license is required to read measured load pull datafile formats. Additionally, if you are on Windows OS, you must download and install EEsof Licensing Tools from here: [https://edadocs.software.keysight.com/display/downloads/Licensing+Software+Downloads](https://edadocs.software.keysight.com/display/downloads/Licensing%2BSoftware%2BDownloads).

## Dependencies[](#dependencies "Link to this heading")

### Python libraries[](#python-libraries "Link to this heading")

Below are the Python and library dependencies for `pwdatatools`.

* Python: 3.10 and higher
* pandas: 1.3 and higher
* numpy: 1.18 and higher

Note

The term ‘and higher’ above includes new minor and maintenance versions, but *not* any new major versions.

If you use pip to install `pwdatatools`, the dependencies are installed automatically (if missing from your Python environment). If you have an older version of a dependency already installed, pip has various options for controlling what happens. If you are using Anaconda, see the Anaconda documentation for instructions on how to install a Python wheel file.

In addition to the above depedencies, pwdatatools has the following “soft” dependencies:

* scipy
* matplotlib (required by the `pwdatatools.viz` module)
* seaborn (required by the `pwdatatools.viz` module)
* keysight-ads-dataset
* keysight-systemvue

A “soft” dependency is a library that is not required for the basic functionality of `pwdatatools`, but is required for certain features. If you are using pip to install `pwdatatools`, these libraries will not be installed automatically. If you want to use the features that depend on these libraries, you will need to install them yourself (unless you are using ADS or ICCAP, which already include some of these libraries). Note that the `keysight-ads-dataset` library is not strictly required for reading and writing ADS datasets, but is recommended since it speeds up file processing and is located in the ADS installation directory in the “tools/python/wheelhouse” subdirectory. The `keysight-systemvue` library is required for reading and writing SystemVue datasets and is located in the SystemVue installation directory in the “Python” subdirectory.

### Keysight software[](#keysight-software "Link to this heading")

In order to work with certain types of datafiles, ADS or SystemVue installations may be required. Below are the minimum recommended versions.

* PathWave Advanced Design System (ADS) 2021 or later
* PathWave System Design (SystemVue) 2023 or later

### Licensing[](#licensing "Link to this heading")

Most of the functionality of `pwdatatools` does not require a license. However, an ADS Data Display license is required to read measured load pull datafile formats (Maury, Focus, and Keysight formats). Addtionally, if you are on Windows OS, you must download and install EEsof Licensing Tools from here: [https://edadocs.software.keysight.com/display/downloads/Licensing+Software+Downloads](https://edadocs.software.keysight.com/display/downloads/Licensing%2BSoftware%2BDownloads). This extra licensing tool is not required on Linux because the required licensing bits are already included in the ADS installation.


---

