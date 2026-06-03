<!-- 来源: examples\loadpull\loadpull.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-pwdatatools](../../index.md)
* [Examples](../index.md)
* Load Pull Basics

0.12.1

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/examples/loadpull/loadpull.ipynb.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* [Initial Setup](../../initial_setup.md)
* [Core Concepts](../../core_concepts/index.md)
  + [All About Filepaths](../../core_concepts/all_about_filepaths.md)
  + [File Extensions and Formats](../../core_concepts/file_exts_and_formats.md)
  + [Multi-Dimensional Data](../../core_concepts/multi_dimensional_data.md)
  + [pandas DataFrame Indexing](../../core_concepts/pandas_dataframe_indexing.md)
* [How To](../../howto/index.md)
  + [Read a File](../../howto/read_a_file.md)
  + [Write a File](../../howto/write_a_file.md)
  + [Translate a File](../../howto/translate_a_file.md)
  + [Use the Var Class](../../howto/use_var_class.md)
  + [Use the Block Class](../../howto/use_block_class.md)
  + [Use the Group Class](../../howto/use_group_class.md)
  + [Use Roles](../../howto/use_roles.md)
  + [Work with ADS Data](../../howto/work_with_ADS_data.md)
  + [Work with CSV Data](../../howto/work_with_csv_data.md)
  + [Work with Load Pull Data](../../howto/work_with_loadpull_data.md)
  + [Work with S-Parameter Data](../../howto/work_with_s_parameter_data.md)
  + [Work with SystemVue Data](../../howto/work_with_SystemVue_data.md)
  + [Show or Hide Log Messages](../../howto/show_or_hide_messages.md)
  + [Get the Data Tools Version](../../howto/get_the_version.md)
* [Examples](../index.md)
  + [Getting Started with PathWave Data Tools](../getting_started/getting_started.md)
  + Load Pull Basics
* [API Reference](../../api_reference/index.md)
  + [Main](../../api_reference/main.md)
    - [Var](../../api_reference/_autosummary/keysight.pwdatatools.Var.md)
      * [Var.attrs](../../api_reference/_autosummary/keysight.pwdatatools.Var.attrs.md)
      * [Var.block](../../api_reference/_autosummary/keysight.pwdatatools.Var.block.md)
      * [Var.dims](../../api_reference/_autosummary/keysight.pwdatatools.Var.dims.md)
      * [Var.dtype](../../api_reference/_autosummary/keysight.pwdatatools.Var.dtype.md)
      * [Var.idx](../../api_reference/_autosummary/keysight.pwdatatools.Var.idx.md)
      * [Var.idxname](../../api_reference/_autosummary/keysight.pwdatatools.Var.idxname.md)
      * [Var.kind](../../api_reference/_autosummary/keysight.pwdatatools.Var.kind.md)
      * [Var.name](../../api_reference/_autosummary/keysight.pwdatatools.Var.name.md)
      * [Var.ndim](../../api_reference/_autosummary/keysight.pwdatatools.Var.ndim.md)
      * [Var.role](../../api_reference/_autosummary/keysight.pwdatatools.Var.role.md)
      * [Var.shape](../../api_reference/_autosummary/keysight.pwdatatools.Var.shape.md)
      * [Var.size](../../api_reference/_autosummary/keysight.pwdatatools.Var.size.md)
      * [Var.unit](../../api_reference/_autosummary/keysight.pwdatatools.Var.unit.md)
      * [Var.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Var.__init__.md)
      * [Var.add\_role](../../api_reference/_autosummary/keysight.pwdatatools.Var.add_role.md)
      * [Var.copy](../../api_reference/_autosummary/keysight.pwdatatools.Var.copy.md)
      * [Var.count\_observations](../../api_reference/_autosummary/keysight.pwdatatools.Var.count_observations.md)
      * [Var.drop\_observations](../../api_reference/_autosummary/keysight.pwdatatools.Var.drop_observations.md)
      * [Var.fill\_nan](../../api_reference/_autosummary/keysight.pwdatatools.Var.fill_nan.md)
      * [Var.fill\_null](../../api_reference/_autosummary/keysight.pwdatatools.Var.fill_null.md)
      * [Var.from\_1D\_vars](../../api_reference/_autosummary/keysight.pwdatatools.Var.from_1D_vars.md)
      * [Var.from\_pandas\_dataframe](../../api_reference/_autosummary/keysight.pwdatatools.Var.from_pandas_dataframe.md)
      * [Var.from\_pandas\_series](../../api_reference/_autosummary/keysight.pwdatatools.Var.from_pandas_series.md)
      * [Var.has\_dims](../../api_reference/_autosummary/keysight.pwdatatools.Var.has_dims.md)
      * [Var.has\_idx](../../api_reference/_autosummary/keysight.pwdatatools.Var.has_idx.md)
      * [Var.has\_nan](../../api_reference/_autosummary/keysight.pwdatatools.Var.has_nan.md)
      * [Var.has\_null](../../api_reference/_autosummary/keysight.pwdatatools.Var.has_null.md)
      * [Var.has\_role](../../api_reference/_autosummary/keysight.pwdatatools.Var.has_role.md)
      * [Var.info](../../api_reference/_autosummary/keysight.pwdatatools.Var.info.md)
      * [Var.is\_nan](../../api_reference/_autosummary/keysight.pwdatatools.Var.is_nan.md)
      * [Var.is\_null](../../api_reference/_autosummary/keysight.pwdatatools.Var.is_null.md)
      * [Var.keep\_observations](../../api_reference/_autosummary/keysight.pwdatatools.Var.keep_observations.md)
      * [Var.rename](../../api_reference/_autosummary/keysight.pwdatatools.Var.rename.md)
      * [Var.repeat\_observations](../../api_reference/_autosummary/keysight.pwdatatools.Var.repeat_observations.md)
      * [Var.replace](../../api_reference/_autosummary/keysight.pwdatatools.Var.replace.md)
      * [Var.select](../../api_reference/_autosummary/keysight.pwdatatools.Var.select.md)
      * [Var.set\_data](../../api_reference/_autosummary/keysight.pwdatatools.Var.set_data.md)
      * [Var.set\_data\_in\_place](../../api_reference/_autosummary/keysight.pwdatatools.Var.set_data_in_place.md)
      * [Var.sort\_observations](../../api_reference/_autosummary/keysight.pwdatatools.Var.sort_observations.md)
      * [Var.to\_numpy\_maskedarray](../../api_reference/_autosummary/keysight.pwdatatools.Var.to_numpy_maskedarray.md)
      * [Var.to\_numpy\_ndarray](../../api_reference/_autosummary/keysight.pwdatatools.Var.to_numpy_ndarray.md)
      * [Var.to\_pandas\_dataframe](../../api_reference/_autosummary/keysight.pwdatatools.Var.to_pandas_dataframe.md)
      * [Var.to\_pandas\_series](../../api_reference/_autosummary/keysight.pwdatatools.Var.to_pandas_series.md)
    - [Block](../../api_reference/_autosummary/keysight.pwdatatools.Block.md)
      * [Block.attrs](../../api_reference/_autosummary/keysight.pwdatatools.Block.attrs.md)
      * [Block.dvarnames](../../api_reference/_autosummary/keysight.pwdatatools.Block.dvarnames.md)
      * [Block.exprs](../../api_reference/_autosummary/keysight.pwdatatools.Block.exprs.md)
      * [Block.idxnames](../../api_reference/_autosummary/keysight.pwdatatools.Block.idxnames.md)
      * [Block.ivarnames](../../api_reference/_autosummary/keysight.pwdatatools.Block.ivarnames.md)
      * [Block.name](../../api_reference/_autosummary/keysight.pwdatatools.Block.name.md)
      * [Block.varnames](../../api_reference/_autosummary/keysight.pwdatatools.Block.varnames.md)
      * [Block.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Block.__init__.md)
      * [Block.clear](../../api_reference/_autosummary/keysight.pwdatatools.Block.clear.md)
      * [Block.copy](../../api_reference/_autosummary/keysight.pwdatatools.Block.copy.md)
      * [Block.count\_observations](../../api_reference/_autosummary/keysight.pwdatatools.Block.count_observations.md)
      * [Block.crucial\_varnames](../../api_reference/_autosummary/keysight.pwdatatools.Block.crucial_varnames.md)
      * [Block.drop\_observations](../../api_reference/_autosummary/keysight.pwdatatools.Block.drop_observations.md)
      * [Block.drop\_vars](../../api_reference/_autosummary/keysight.pwdatatools.Block.drop_vars.md)
      * [Block.drop\_vars\_in\_place](../../api_reference/_autosummary/keysight.pwdatatools.Block.drop_vars_in_place.md)
      * [Block.eval\_expr\_as\_var](../../api_reference/_autosummary/keysight.pwdatatools.Block.eval_expr_as_var.md)
      * [Block.fill\_nan](../../api_reference/_autosummary/keysight.pwdatatools.Block.fill_nan.md)
      * [Block.fill\_null](../../api_reference/_autosummary/keysight.pwdatatools.Block.fill_null.md)
      * [Block.from\_file](../../api_reference/_autosummary/keysight.pwdatatools.Block.from_file.md)
      * [Block.from\_pandas\_dataframe](../../api_reference/_autosummary/keysight.pwdatatools.Block.from_pandas_dataframe.md)
      * [Block.get](../../api_reference/_autosummary/keysight.pwdatatools.Block.get.md)
      * [Block.get\_var](../../api_reference/_autosummary/keysight.pwdatatools.Block.get_var.md)
      * [Block.get\_var\_as\_expr](../../api_reference/_autosummary/keysight.pwdatatools.Block.get_var_as_expr.md)
      * [Block.info](../../api_reference/_autosummary/keysight.pwdatatools.Block.info.md)
      * [Block.items](../../api_reference/_autosummary/keysight.pwdatatools.Block.items.md)
      * [Block.iter\_sweep\_nodes](../../api_reference/_autosummary/keysight.pwdatatools.Block.iter_sweep_nodes.md)
      * [Block.iter\_vars](../../api_reference/_autosummary/keysight.pwdatatools.Block.iter_vars.md)
      * [Block.keep\_observations](../../api_reference/_autosummary/keysight.pwdatatools.Block.keep_observations.md)
      * [Block.keep\_vars](../../api_reference/_autosummary/keysight.pwdatatools.Block.keep_vars.md)
      * [Block.keep\_vars\_in\_place](../../api_reference/_autosummary/keysight.pwdatatools.Block.keep_vars_in_place.md)
      * [Block.keys](../../api_reference/_autosummary/keysight.pwdatatools.Block.keys.md)
      * [Block.make\_idxs](../../api_reference/_autosummary/keysight.pwdatatools.Block.make_idxs.md)
      * [Block.pop](../../api_reference/_autosummary/keysight.pwdatatools.Block.pop.md)
      * [Block.popitem](../../api_reference/_autosummary/keysight.pwdatatools.Block.popitem.md)
      * [Block.rename\_vars](../../api_reference/_autosummary/keysight.pwdatatools.Block.rename_vars.md)
      * [Block.rename\_vars\_in\_place](../../api_reference/_autosummary/keysight.pwdatatools.Block.rename_vars_in_place.md)
      * [Block.set\_data](../../api_reference/_autosummary/keysight.pwdatatools.Block.set_data.md)
      * [Block.set\_data\_in\_place](../../api_reference/_autosummary/keysight.pwdatatools.Block.set_data_in_place.md)
      * [Block.set\_vars](../../api_reference/_autosummary/keysight.pwdatatools.Block.set_vars.md)
      * [Block.set\_vars\_in\_place](../../api_reference/_autosummary/keysight.pwdatatools.Block.set_vars_in_place.md)
      * [Block.setdefault](../../api_reference/_autosummary/keysight.pwdatatools.Block.setdefault.md)
      * [Block.sort\_observations](../../api_reference/_autosummary/keysight.pwdatatools.Block.sort_observations.md)
      * [Block.sort\_observations\_by](../../api_reference/_autosummary/keysight.pwdatatools.Block.sort_observations_by.md)
      * [Block.sort\_vars](../../api_reference/_autosummary/keysight.pwdatatools.Block.sort_vars.md)
      * [Block.to\_file](../../api_reference/_autosummary/keysight.pwdatatools.Block.to_file.md)
      * [Block.to\_pandas\_dataframe](../../api_reference/_autosummary/keysight.pwdatatools.Block.to_pandas_dataframe.md)
      * [Block.update](../../api_reference/_autosummary/keysight.pwdatatools.Block.update.md)
      * [Block.values](../../api_reference/_autosummary/keysight.pwdatatools.Block.values.md)
    - [Group](../../api_reference/_autosummary/keysight.pwdatatools.Group.md)
      * [Group.attrs](../../api_reference/_autosummary/keysight.pwdatatools.Group.attrs.md)
      * [Group.members](../../api_reference/_autosummary/keysight.pwdatatools.Group.members.md)
      * [Group.name](../../api_reference/_autosummary/keysight.pwdatatools.Group.name.md)
      * [Group.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Group.__init__.md)
      * [Group.append](../../api_reference/_autosummary/keysight.pwdatatools.Group.append.md)
      * [Group.clear](../../api_reference/_autosummary/keysight.pwdatatools.Group.clear.md)
      * [Group.copy](../../api_reference/_autosummary/keysight.pwdatatools.Group.copy.md)
      * [Group.count](../../api_reference/_autosummary/keysight.pwdatatools.Group.count.md)
      * [Group.extend](../../api_reference/_autosummary/keysight.pwdatatools.Group.extend.md)
      * [Group.fill\_membernames](../../api_reference/_autosummary/keysight.pwdatatools.Group.fill_membernames.md)
      * [Group.filled\_membernames](../../api_reference/_autosummary/keysight.pwdatatools.Group.filled_membernames.md)
      * [Group.flatten](../../api_reference/_autosummary/keysight.pwdatatools.Group.flatten.md)
      * [Group.flattened](../../api_reference/_autosummary/keysight.pwdatatools.Group.flattened.md)
      * [Group.from\_file](../../api_reference/_autosummary/keysight.pwdatatools.Group.from_file.md)
      * [Group.get\_member](../../api_reference/_autosummary/keysight.pwdatatools.Group.get_member.md)
      * [Group.get\_member\_as\_block](../../api_reference/_autosummary/keysight.pwdatatools.Group.get_member_as_block.md)
      * [Group.get\_member\_as\_group](../../api_reference/_autosummary/keysight.pwdatatools.Group.get_member_as_group.md)
      * [Group.get\_member\_as\_loadpullblock](../../api_reference/_autosummary/keysight.pwdatatools.Group.get_member_as_loadpullblock.md)
      * [Group.index](../../api_reference/_autosummary/keysight.pwdatatools.Group.index.md)
      * [Group.insert](../../api_reference/_autosummary/keysight.pwdatatools.Group.insert.md)
      * [Group.iter\_blocks](../../api_reference/_autosummary/keysight.pwdatatools.Group.iter_blocks.md)
      * [Group.iter\_members](../../api_reference/_autosummary/keysight.pwdatatools.Group.iter_members.md)
      * [Group.pop](../../api_reference/_autosummary/keysight.pwdatatools.Group.pop.md)
      * [Group.remove](../../api_reference/_autosummary/keysight.pwdatatools.Group.remove.md)
      * [Group.reverse](../../api_reference/_autosummary/keysight.pwdatatools.Group.reverse.md)
      * [Group.to\_file](../../api_reference/_autosummary/keysight.pwdatatools.Group.to_file.md)
      * [Group.tree](../../api_reference/_autosummary/keysight.pwdatatools.Group.tree.md)
  + [Metadata](../../api_reference/metadata.md)
    - [AttrsDict](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.md)
      * [AttrsDict.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.__init__.md)
      * [AttrsDict.clear](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.clear.md)
      * [AttrsDict.copy](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.copy.md)
      * [AttrsDict.get](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.get.md)
      * [AttrsDict.items](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.items.md)
      * [AttrsDict.keys](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.keys.md)
      * [AttrsDict.pop](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.pop.md)
      * [AttrsDict.popitem](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.popitem.md)
      * [AttrsDict.setdefault](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.setdefault.md)
      * [AttrsDict.update](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.update.md)
      * [AttrsDict.values](../../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.values.md)
    - [Dims](../../api_reference/_autosummary/keysight.pwdatatools.Dims.md)
      * [Dims.i\_names](../../api_reference/_autosummary/keysight.pwdatatools.Dims.i_names.md)
      * [Dims.i\_nums](../../api_reference/_autosummary/keysight.pwdatatools.Dims.i_nums.md)
      * [Dims.idx](../../api_reference/_autosummary/keysight.pwdatatools.Dims.idx.md)
      * [Dims.j\_names](../../api_reference/_autosummary/keysight.pwdatatools.Dims.j_names.md)
      * [Dims.j\_nums](../../api_reference/_autosummary/keysight.pwdatatools.Dims.j_nums.md)
      * [Dims.ndim](../../api_reference/_autosummary/keysight.pwdatatools.Dims.ndim.md)
      * [Dims.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Dims.__init__.md)
      * [Dims.copy](../../api_reference/_autosummary/keysight.pwdatatools.Dims.copy.md)
      * [Dims.get\_dimscale](../../api_reference/_autosummary/keysight.pwdatatools.Dims.get_dimscale.md)
      * [Dims.has\_i\_names](../../api_reference/_autosummary/keysight.pwdatatools.Dims.has_i_names.md)
      * [Dims.has\_i\_nums](../../api_reference/_autosummary/keysight.pwdatatools.Dims.has_i_nums.md)
      * [Dims.has\_idx](../../api_reference/_autosummary/keysight.pwdatatools.Dims.has_idx.md)
      * [Dims.has\_j\_names](../../api_reference/_autosummary/keysight.pwdatatools.Dims.has_j_names.md)
      * [Dims.has\_j\_nums](../../api_reference/_autosummary/keysight.pwdatatools.Dims.has_j_nums.md)
      * [Dims.is\_compatible\_with\_shape](../../api_reference/_autosummary/keysight.pwdatatools.Dims.is_compatible_with_shape.md)
      * [Dims.is\_empty](../../api_reference/_autosummary/keysight.pwdatatools.Dims.is_empty.md)
      * [Dims.keep\_where](../../api_reference/_autosummary/keysight.pwdatatools.Dims.keep_where.md)
      * [Dims.partial\_shape](../../api_reference/_autosummary/keysight.pwdatatools.Dims.partial_shape.md)
      * [Dims.replace](../../api_reference/_autosummary/keysight.pwdatatools.Dims.replace.md)
    - [DimScale](../../api_reference/_autosummary/keysight.pwdatatools.DimScale.md)
      * [DimScale.name](../../api_reference/_autosummary/keysight.pwdatatools.DimScale.name.md)
      * [DimScale.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.DimScale.__init__.md)
      * [DimScale.copy](../../api_reference/_autosummary/keysight.pwdatatools.DimScale.copy.md)
      * [DimScale.from\_pandas\_index](../../api_reference/_autosummary/keysight.pwdatatools.DimScale.from_pandas_index.md)
      * [DimScale.has\_names\_values](../../api_reference/_autosummary/keysight.pwdatatools.DimScale.has_names_values.md)
      * [DimScale.has\_nums\_values](../../api_reference/_autosummary/keysight.pwdatatools.DimScale.has_nums_values.md)
      * [DimScale.rename](../../api_reference/_autosummary/keysight.pwdatatools.DimScale.rename.md)
      * [DimScale.to\_numpy\_ndarray](../../api_reference/_autosummary/keysight.pwdatatools.DimScale.to_numpy_ndarray.md)
      * [DimScale.view\_values](../../api_reference/_autosummary/keysight.pwdatatools.DimScale.view_values.md)
    - [Expr](../../api_reference/_autosummary/keysight.pwdatatools.Expr.md)
      * [Expr.input](../../api_reference/_autosummary/keysight.pwdatatools.Expr.input.md)
      * [Expr.ops](../../api_reference/_autosummary/keysight.pwdatatools.Expr.ops.md)
      * [Expr.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Expr.__init__.md)
      * [Expr.abs](../../api_reference/_autosummary/keysight.pwdatatools.Expr.abs.md)
      * [Expr.angle](../../api_reference/_autosummary/keysight.pwdatatools.Expr.angle.md)
      * [Expr.copy](../../api_reference/_autosummary/keysight.pwdatatools.Expr.copy.md)
      * [Expr.dB](../../api_reference/_autosummary/keysight.pwdatatools.Expr.dB.md)
      * [Expr.decibel](../../api_reference/_autosummary/keysight.pwdatatools.Expr.decibel.md)
      * [Expr.eval\_as\_numpy\_ndarray](../../api_reference/_autosummary/keysight.pwdatatools.Expr.eval_as_numpy_ndarray.md)
      * [Expr.imag](../../api_reference/_autosummary/keysight.pwdatatools.Expr.imag.md)
      * [Expr.mag](../../api_reference/_autosummary/keysight.pwdatatools.Expr.mag.md)
      * [Expr.real](../../api_reference/_autosummary/keysight.pwdatatools.Expr.real.md)
    - [ExprsDict](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.md)
      * [ExprsDict.block](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.block.md)
      * [ExprsDict.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.__init__.md)
      * [ExprsDict.clear](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.clear.md)
      * [ExprsDict.copy](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.copy.md)
      * [ExprsDict.get](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.get.md)
      * [ExprsDict.items](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.items.md)
      * [ExprsDict.keys](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.keys.md)
      * [ExprsDict.pop](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.pop.md)
      * [ExprsDict.popitem](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.popitem.md)
      * [ExprsDict.setdefault](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.setdefault.md)
      * [ExprsDict.update](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.update.md)
      * [ExprsDict.values](../../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.values.md)
  + [File I/O](../../api_reference/fileio.md)
    - [read\_file\_as\_block](../../api_reference/_autosummary/keysight.pwdatatools.read_file_as_block.md)
    - [read\_file\_as\_group](../../api_reference/_autosummary/keysight.pwdatatools.read_file_as_group.md)
    - [read\_file\_as\_loadpullblock](../../api_reference/_autosummary/keysight.pwdatatools.read_file_as_loadpullblock.md)
    - [read\_file](../../api_reference/_autosummary/keysight.pwdatatools.read_file.md)
    - [translate\_file](../../api_reference/_autosummary/keysight.pwdatatools.translate_file.md)
    - [write\_file](../../api_reference/_autosummary/keysight.pwdatatools.write_file.md)
    - [ADSReadOptions](../../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.md)
      * [ADSReadOptions.engine\_pref](../../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.engine_pref.md)
      * [ADSReadOptions.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.read_or_write.md)
      * [ADSReadOptions.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.__init__.md)
      * [ADSReadOptions.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.get_formats.md)
      * [ADSReadOptions.mapping](../../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.mapping.md)
      * [ADSReadOptions.replace](../../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.replace.md)
    - [ADSWriteInvalid](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.md)
      * [ADSWriteInvalid.boolean](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.boolean.md)
      * [ADSWriteInvalid.boolean\_options](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.boolean_options.md)
      * [ADSWriteInvalid.complexfloating](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.complexfloating.md)
      * [ADSWriteInvalid.complexfloating\_options](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.complexfloating_options.md)
      * [ADSWriteInvalid.floating](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.floating.md)
      * [ADSWriteInvalid.floating\_options](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.floating_options.md)
      * [ADSWriteInvalid.integer](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.integer.md)
      * [ADSWriteInvalid.integer\_null\_rep](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.integer_null_rep.md)
      * [ADSWriteInvalid.integer\_options](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.integer_options.md)
      * [ADSWriteInvalid.nan\_rep](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.nan_rep.md)
      * [ADSWriteInvalid.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.read_or_write.md)
      * [ADSWriteInvalid.string](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.string.md)
      * [ADSWriteInvalid.string\_null\_rep](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.string_null_rep.md)
      * [ADSWriteInvalid.string\_options](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.string_options.md)
      * [ADSWriteInvalid.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.__init__.md)
      * [ADSWriteInvalid.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.get_formats.md)
      * [ADSWriteInvalid.mapping](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.mapping.md)
      * [ADSWriteInvalid.replace](../../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.replace.md)
    - [CITIReadOptions](../../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.md)
      * [CITIReadOptions.engine\_pref](../../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.engine_pref.md)
      * [CITIReadOptions.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.read_or_write.md)
      * [CITIReadOptions.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.__init__.md)
      * [CITIReadOptions.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.get_formats.md)
      * [CITIReadOptions.mapping](../../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.mapping.md)
      * [CITIReadOptions.replace](../../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.replace.md)
    - [CSVReadOptions](../../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.md)
      * [CSVReadOptions.engine\_pref](../../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.engine_pref.md)
      * [CSVReadOptions.pandas\_kwargs](../../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.pandas_kwargs.md)
      * [CSVReadOptions.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.read_or_write.md)
      * [CSVReadOptions.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.__init__.md)
      * [CSVReadOptions.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.get_formats.md)
      * [CSVReadOptions.mapping](../../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.mapping.md)
      * [CSVReadOptions.replace](../../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.replace.md)
    - [CSVWriteOptions](../../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.md)
      * [CSVWriteOptions.cols\_default\_ints](../../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.cols_default_ints.md)
      * [CSVWriteOptions.cols\_default\_ints\_forced](../../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.cols_default_ints_forced.md)
      * [CSVWriteOptions.cols\_dimscales\_delim](../../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.cols_dimscales_delim.md)
      * [CSVWriteOptions.engine\_pref](../../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.engine_pref.md)
      * [CSVWriteOptions.pandas\_kwargs](../../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.pandas_kwargs.md)
      * [CSVWriteOptions.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.read_or_write.md)
      * [CSVWriteOptions.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.__init__.md)
      * [CSVWriteOptions.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.get_formats.md)
      * [CSVWriteOptions.mapping](../../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.mapping.md)
      * [CSVWriteOptions.replace](../../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.replace.md)
    - [DataFile](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.md)
      * [DataFile.ext](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.ext.md)
      * [DataFile.folder](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.folder.md)
      * [DataFile.format\_override](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.format_override.md)
      * [DataFile.name](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.name.md)
      * [DataFile.path](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.path.md)
      * [DataFile.stem](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.stem.md)
      * [DataFile.suffix](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.suffix.md)
      * [DataFile.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.__init__.md)
      * [DataFile.copy](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.copy.md)
      * [DataFile.delete](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.delete.md)
      * [DataFile.exists](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.exists.md)
      * [DataFile.find\_diffs](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.find_diffs.md)
      * [DataFile.get\_format](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.get_format.md)
      * [DataFile.has\_format](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.has_format.md)
      * [DataFile.has\_modtime\_match](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.has_modtime_match.md)
      * [DataFile.is\_ads](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_ads.md)
      * [DataFile.is\_citi](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_citi.md)
      * [DataFile.is\_csv](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_csv.md)
      * [DataFile.is\_farfieldio](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_farfieldio.md)
      * [DataFile.is\_hfss\_ffd](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_hfss_ffd.md)
      * [DataFile.is\_loadpull](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_loadpull.md)
      * [DataFile.is\_mdif](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_mdif.md)
      * [DataFile.is\_mdm](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_mdm.md)
      * [DataFile.is\_native](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_native.md)
      * [DataFile.is\_s2pmdif](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_s2pmdif.md)
      * [DataFile.is\_same](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_same.md)
      * [DataFile.is\_smatrixio](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_smatrixio.md)
      * [DataFile.is\_systemvue](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_systemvue.md)
      * [DataFile.is\_touchstone](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_touchstone.md)
      * [DataFile.lines](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.lines.md)
      * [DataFile.modtime](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.modtime.md)
      * [DataFile.modtime\_datetime](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.modtime_datetime.md)
      * [DataFile.read\_as\_block](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.read_as_block.md)
      * [DataFile.read\_as\_group](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.read_as_group.md)
      * [DataFile.read\_as\_loadpullblock](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.read_as_loadpullblock.md)
      * [DataFile.remove](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.remove.md)
      * [DataFile.set\_modtime](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.set_modtime.md)
      * [DataFile.translate](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.translate.md)
      * [DataFile.tree](../../api_reference/_autosummary/keysight.pwdatatools.DataFile.tree.md)
    - [LoadPullReadOptions](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.md)
      * [LoadPullReadOptions.always\_freq\_suffixed](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.always_freq_suffixed.md)
      * [LoadPullReadOptions.derived\_vars](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.derived_vars.md)
      * [LoadPullReadOptions.power\_ivar\_pref](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.power_ivar_pref.md)
      * [LoadPullReadOptions.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.read_or_write.md)
      * [LoadPullReadOptions.uniform\_ivars](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.uniform_ivars.md)
      * [LoadPullReadOptions.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.__init__.md)
      * [LoadPullReadOptions.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.get_formats.md)
      * [LoadPullReadOptions.replace](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.replace.md)
    - [LoadPullDerivedVars](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.md)
      * [LoadPullDerivedVars.freq\_enums](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.freq_enums.md)
      * [LoadPullDerivedVars.main](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.main.md)
      * [LoadPullDerivedVars.power\_units](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.power_units.md)
      * [LoadPullDerivedVars.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.read_or_write.md)
      * [LoadPullDerivedVars.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.__init__.md)
      * [LoadPullDerivedVars.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.get_formats.md)
      * [LoadPullDerivedVars.replace](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.replace.md)
    - [MDIFReadOptions](../../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.md)
      * [MDIFReadOptions.engine\_pref](../../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.engine_pref.md)
      * [MDIFReadOptions.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.read_or_write.md)
      * [MDIFReadOptions.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.__init__.md)
      * [MDIFReadOptions.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.get_formats.md)
      * [MDIFReadOptions.mapping](../../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.mapping.md)
      * [MDIFReadOptions.replace](../../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.replace.md)
    - [MDIFWriteInvalid](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.md)
      * [MDIFWriteInvalid.boolean](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.boolean.md)
      * [MDIFWriteInvalid.boolean\_options](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.boolean_options.md)
      * [MDIFWriteInvalid.complexfloating](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.complexfloating.md)
      * [MDIFWriteInvalid.complexfloating\_options](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.complexfloating_options.md)
      * [MDIFWriteInvalid.floating](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.floating.md)
      * [MDIFWriteInvalid.floating\_options](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.floating_options.md)
      * [MDIFWriteInvalid.integer](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.integer.md)
      * [MDIFWriteInvalid.integer\_null\_rep](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.integer_null_rep.md)
      * [MDIFWriteInvalid.integer\_options](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.integer_options.md)
      * [MDIFWriteInvalid.nan\_rep](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.nan_rep.md)
      * [MDIFWriteInvalid.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.read_or_write.md)
      * [MDIFWriteInvalid.string](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.string.md)
      * [MDIFWriteInvalid.string\_null\_rep](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.string_null_rep.md)
      * [MDIFWriteInvalid.string\_options](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.string_options.md)
      * [MDIFWriteInvalid.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.__init__.md)
      * [MDIFWriteInvalid.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.get_formats.md)
      * [MDIFWriteInvalid.mapping](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.mapping.md)
      * [MDIFWriteInvalid.replace](../../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.replace.md)
    - [MDMReadOptions](../../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.md)
      * [MDMReadOptions.iccap\_values\_as\_vars](../../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.iccap_values_as_vars.md)
      * [MDMReadOptions.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.read_or_write.md)
      * [MDMReadOptions.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.__init__.md)
      * [MDMReadOptions.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.get_formats.md)
      * [MDMReadOptions.mapping](../../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.mapping.md)
      * [MDMReadOptions.replace](../../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.replace.md)
    - [SMatrixIOReadOptions](../../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.md)
      * [SMatrixIOReadOptions.engine\_pref](../../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.engine_pref.md)
      * [SMatrixIOReadOptions.network\_blockname](../../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.network_blockname.md)
      * [SMatrixIOReadOptions.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.read_or_write.md)
      * [SMatrixIOReadOptions.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.__init__.md)
      * [SMatrixIOReadOptions.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.get_formats.md)
      * [SMatrixIOReadOptions.mapping](../../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.mapping.md)
      * [SMatrixIOReadOptions.replace](../../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.replace.md)
    - [TouchstoneReadOptions](../../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.md)
      * [TouchstoneReadOptions.engine\_pref](../../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.engine_pref.md)
      * [TouchstoneReadOptions.network\_blockname](../../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.network_blockname.md)
      * [TouchstoneReadOptions.noise\_blockname](../../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.noise_blockname.md)
      * [TouchstoneReadOptions.read\_or\_write](../../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.read_or_write.md)
      * [TouchstoneReadOptions.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.__init__.md)
      * [TouchstoneReadOptions.get\_formats](../../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.get_formats.md)
      * [TouchstoneReadOptions.mapping](../../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.mapping.md)
      * [TouchstoneReadOptions.replace](../../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.replace.md)
  + [Load Pull](../../api_reference/loadpull.md)
    - [LoadPullBlock](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.md)
      * [LoadPullBlock.attrs](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.attrs.md)
      * [LoadPullBlock.dvarnames](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.dvarnames.md)
      * [LoadPullBlock.exprs](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.exprs.md)
      * [LoadPullBlock.gamma\_idxname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_idxname.md)
      * [LoadPullBlock.gamma\_ivarname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivarname.md)
      * [LoadPullBlock.idxnames](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.idxnames.md)
      * [LoadPullBlock.ivarnames](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.ivarnames.md)
      * [LoadPullBlock.name](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.name.md)
      * [LoadPullBlock.outer\_idxnames](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.outer_idxnames.md)
      * [LoadPullBlock.outer\_ivarnames](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.outer_ivarnames.md)
      * [LoadPullBlock.power\_idxname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.power_idxname.md)
      * [LoadPullBlock.power\_ivarname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.power_ivarname.md)
      * [LoadPullBlock.varnames](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.varnames.md)
      * [LoadPullBlock.z\_idxname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.z_idxname.md)
      * [LoadPullBlock.z\_ivarname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.z_ivarname.md)
      * [LoadPullBlock.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.__init__.md)
      * [LoadPullBlock.at\_gcomp](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md)
      * [LoadPullBlock.at\_power](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md)
      * [LoadPullBlock.clear](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.clear.md)
      * [LoadPullBlock.contourplot](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md)
      * [LoadPullBlock.coord\_system](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.coord_system.md)
      * [LoadPullBlock.copy](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.copy.md)
      * [LoadPullBlock.count\_observations](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.count_observations.md)
      * [LoadPullBlock.crucial\_varnames](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.crucial_varnames.md)
      * [LoadPullBlock.drop\_grid\_edges](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_grid_edges.md)
      * [LoadPullBlock.drop\_invalid\_regular](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_invalid_regular.md)
      * [LoadPullBlock.drop\_observations](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_observations.md)
      * [LoadPullBlock.drop\_vars](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_vars.md)
      * [LoadPullBlock.drop\_vars\_in\_place](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_vars_in_place.md)
      * [LoadPullBlock.eval\_expr\_as\_var](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.eval_expr_as_var.md)
      * [LoadPullBlock.fill\_nan](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.fill_nan.md)
      * [LoadPullBlock.fill\_null](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.fill_null.md)
      * [LoadPullBlock.from\_block](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.from_block.md)
      * [LoadPullBlock.from\_file](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.from_file.md)
      * [LoadPullBlock.from\_pandas\_dataframe](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.from_pandas_dataframe.md)
      * [LoadPullBlock.gamma\_idx](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_idx.md)
      * [LoadPullBlock.gamma\_ivar](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar.md)
      * [LoadPullBlock.gamma\_ivar\_scatterplot](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot.md)
      * [LoadPullBlock.gamma\_to\_z](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_to_z.md)
      * [LoadPullBlock.get](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.get.md)
      * [LoadPullBlock.get\_grid](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.get_grid.md)
      * [LoadPullBlock.get\_sweep](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.get_sweep.md)
      * [LoadPullBlock.get\_var](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.get_var.md)
      * [LoadPullBlock.get\_var\_as\_expr](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.get_var_as_expr.md)
      * [LoadPullBlock.grid\_data](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md)
      * [LoadPullBlock.has\_gamma\_sweep](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.has_gamma_sweep.md)
      * [LoadPullBlock.has\_outer\_sweep](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.has_outer_sweep.md)
      * [LoadPullBlock.has\_power\_sweep](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.has_power_sweep.md)
      * [LoadPullBlock.has\_regular\_power\_ivar](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar.md)
      * [LoadPullBlock.has\_z\_sweep](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.has_z_sweep.md)
      * [LoadPullBlock.info](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.info.md)
      * [LoadPullBlock.is\_gridded](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.is_gridded.md)
      * [LoadPullBlock.items](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.items.md)
      * [LoadPullBlock.iter\_sweep\_nodes](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.iter_sweep_nodes.md)
      * [LoadPullBlock.iter\_vars](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.iter_vars.md)
      * [LoadPullBlock.keep\_observations](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md)
      * [LoadPullBlock.keep\_vars](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_vars.md)
      * [LoadPullBlock.keep\_vars\_in\_place](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_vars_in_place.md)
      * [LoadPullBlock.keys](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.keys.md)
      * [LoadPullBlock.make\_idxs](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.make_idxs.md)
      * [LoadPullBlock.pop](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.pop.md)
      * [LoadPullBlock.popitem](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.popitem.md)
      * [LoadPullBlock.power\_idx](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.power_idx.md)
      * [LoadPullBlock.power\_ivar](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.power_ivar.md)
      * [LoadPullBlock.regularize\_power\_ivar](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md)
      * [LoadPullBlock.rename\_vars](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.rename_vars.md)
      * [LoadPullBlock.rename\_vars\_in\_place](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.rename_vars_in_place.md)
      * [LoadPullBlock.set\_data](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.set_data.md)
      * [LoadPullBlock.set\_data\_in\_place](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.set_data_in_place.md)
      * [LoadPullBlock.set\_vars](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.set_vars.md)
      * [LoadPullBlock.set\_vars\_in\_place](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.set_vars_in_place.md)
      * [LoadPullBlock.set\_zrefload\_role](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.set_zrefload_role.md)
      * [LoadPullBlock.setdefault](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.setdefault.md)
      * [LoadPullBlock.sort\_observations](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.sort_observations.md)
      * [LoadPullBlock.sort\_observations\_by](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.sort_observations_by.md)
      * [LoadPullBlock.sort\_vars](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.sort_vars.md)
      * [LoadPullBlock.to\_adscontourblock](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.to_adscontourblock.md)
      * [LoadPullBlock.to\_file](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.to_file.md)
      * [LoadPullBlock.to\_pandas\_dataframe](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.to_pandas_dataframe.md)
      * [LoadPullBlock.tricontourplot](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.tricontourplot.md)
      * [LoadPullBlock.update](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.update.md)
      * [LoadPullBlock.values](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.values.md)
      * [LoadPullBlock.z\_idx](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.z_idx.md)
      * [LoadPullBlock.z\_ivar](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.z_ivar.md)
      * [LoadPullBlock.z\_to\_gamma](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.z_to_gamma.md)
      * [LoadPullBlock.zrefload](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.zrefload.md)
    - [LoadPullSweep](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.md)
      * [LoadPullSweep.gamma\_idxname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_idxname.md)
      * [LoadPullSweep.gamma\_ivarname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_ivarname.md)
      * [LoadPullSweep.gamma\_or\_z\_idxname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_or_z_idxname.md)
      * [LoadPullSweep.gamma\_or\_z\_ivarname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_or_z_ivarname.md)
      * [LoadPullSweep.idxnames](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.idxnames.md)
      * [LoadPullSweep.idxnames\_map](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.idxnames_map.md)
      * [LoadPullSweep.ivarnames](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.ivarnames.md)
      * [LoadPullSweep.outer\_idxnames](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.outer_idxnames.md)
      * [LoadPullSweep.outer\_ivarnames](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.outer_ivarnames.md)
      * [LoadPullSweep.power\_idxname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.power_idxname.md)
      * [LoadPullSweep.power\_ivarname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.power_ivarname.md)
      * [LoadPullSweep.z\_idxname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.z_idxname.md)
      * [LoadPullSweep.z\_ivarname](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.z_ivarname.md)
      * [LoadPullSweep.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.__init__.md)
      * [LoadPullSweep.replace](../../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.replace.md)
    - [Grid](../../api_reference/_autosummary/keysight.pwdatatools.Grid.md)
      * [Grid.coord\_system](../../api_reference/_autosummary/keysight.pwdatatools.Grid.coord_system.md)
      * [Grid.extents](../../api_reference/_autosummary/keysight.pwdatatools.Grid.extents.md)
      * [Grid.npointsx](../../api_reference/_autosummary/keysight.pwdatatools.Grid.npointsx.md)
      * [Grid.npointsy](../../api_reference/_autosummary/keysight.pwdatatools.Grid.npointsy.md)
      * [Grid.x\_unique](../../api_reference/_autosummary/keysight.pwdatatools.Grid.x_unique.md)
      * [Grid.y\_unique](../../api_reference/_autosummary/keysight.pwdatatools.Grid.y_unique.md)
      * [Grid.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Grid.__init__.md)
      * [Grid.apply](../../api_reference/_autosummary/keysight.pwdatatools.Grid.apply.md)
      * [Grid.drop\_edges](../../api_reference/_autosummary/keysight.pwdatatools.Grid.drop_edges.md)
      * [Grid.from\_gridded\_series](../../api_reference/_autosummary/keysight.pwdatatools.Grid.from_gridded_series.md)
      * [Grid.includes\_pole](../../api_reference/_autosummary/keysight.pwdatatools.Grid.includes_pole.md)
  + [Public Submodules](../../api_reference/public_submodules.md)
    - [keysight.pwdatatools.calc](../../api_reference/_autosummary/keysight.pwdatatools.calc.md)
      * [db\_to\_power](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.db_to_power.md)
      * [db\_to\_voltage](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.db_to_voltage.md)
      * [dbm\_to\_w](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.dbm_to_w.md)
      * [deg\_to\_rad](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.deg_to_rad.md)
      * [gamma\_to\_gamma](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.gamma_to_gamma.md)
      * [gamma\_to\_z](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.gamma_to_z.md)
      * [polar\_to\_rect](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.polar_to_rect.md)
      * [power\_to\_db](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.power_to_db.md)
      * [rad\_to\_deg](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.rad_to_deg.md)
      * [rect\_to\_polar](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.rect_to_polar.md)
      * [voltage\_to\_db](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.voltage_to_db.md)
      * [w\_to\_dbm](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.w_to_dbm.md)
      * [z\_to\_gamma](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.z_to_gamma.md)
    - [keysight.pwdatatools.roles](../../api_reference/_autosummary/keysight.pwdatatools.roles.md)
      * [VARNAMES\_DEFAULT](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.VARNAMES_DEFAULT.md)
      * [FrozenRolesSet](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.FrozenRolesSet.md)
      * [RolesSet](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.RolesSet.md)
      * [finalize\_role](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.finalize_role.md)
      * [is\_subrole](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.is_subrole.md)
      * [is\_valid\_role](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.is_valid_role.md)
    - [keysight.pwdatatools.viz](../../api_reference/_autosummary/keysight.pwdatatools.viz.md)
      * [complex\_vector\_to\_str\_series](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.complex_vector_to_str_series.md)
      * [contourplot](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.contourplot.md)
      * [float\_vector\_to\_str\_series](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.float_vector_to_str_series.md)
      * [make\_contour\_levels](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.make_contour_levels.md)
      * [smith\_chart](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.smith_chart.md)
      * [tricontourplot](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.tricontourplot.md)
      * [use\_keysight\_theme](../../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.use_keysight_theme.md)
  + [Data Types](../../api_reference/datatypes.md)
    - [DataType](../../api_reference/_autosummary/keysight.pwdatatools.DataType.md)
      * [DataType.name](../../api_reference/_autosummary/keysight.pwdatatools.DataType.name.md)
      * [DataType.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.DataType.__init__.md)
      * [DataType.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.DataType.from_name.md)
      * [DataType.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.DataType.from_numpy_dtype.md)
      * [DataType.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.DataType.is_boolean.md)
      * [DataType.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.DataType.is_complex.md)
      * [DataType.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.DataType.is_float.md)
      * [DataType.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.DataType.is_integer.md)
      * [DataType.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.DataType.is_numeric.md)
      * [DataType.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.DataType.is_signed_integer.md)
      * [DataType.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.DataType.is_string.md)
      * [DataType.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.DataType.is_unsigned_integer.md)
      * [DataType.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.DataType.to_numpy_dtype.md)
    - [Boolean](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.md)
      * [Boolean.name](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.name.md)
      * [Boolean.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.__init__.md)
      * [Boolean.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.from_name.md)
      * [Boolean.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.from_numpy_dtype.md)
      * [Boolean.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_boolean.md)
      * [Boolean.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_complex.md)
      * [Boolean.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_float.md)
      * [Boolean.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_integer.md)
      * [Boolean.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_numeric.md)
      * [Boolean.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_signed_integer.md)
      * [Boolean.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_string.md)
      * [Boolean.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_unsigned_integer.md)
      * [Boolean.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Boolean.to_numpy_dtype.md)
    - [Complex64](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.md)
      * [Complex64.name](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.name.md)
      * [Complex64.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.__init__.md)
      * [Complex64.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.from_name.md)
      * [Complex64.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.from_numpy_dtype.md)
      * [Complex64.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_boolean.md)
      * [Complex64.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_complex.md)
      * [Complex64.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_float.md)
      * [Complex64.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_integer.md)
      * [Complex64.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_numeric.md)
      * [Complex64.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_signed_integer.md)
      * [Complex64.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_string.md)
      * [Complex64.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_unsigned_integer.md)
      * [Complex64.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Complex64.to_numpy_dtype.md)
    - [Complex128](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.md)
      * [Complex128.name](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.name.md)
      * [Complex128.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.__init__.md)
      * [Complex128.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.from_name.md)
      * [Complex128.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.from_numpy_dtype.md)
      * [Complex128.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_boolean.md)
      * [Complex128.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_complex.md)
      * [Complex128.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_float.md)
      * [Complex128.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_integer.md)
      * [Complex128.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_numeric.md)
      * [Complex128.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_signed_integer.md)
      * [Complex128.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_string.md)
      * [Complex128.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_unsigned_integer.md)
      * [Complex128.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Complex128.to_numpy_dtype.md)
    - [Float32](../../api_reference/_autosummary/keysight.pwdatatools.Float32.md)
      * [Float32.name](../../api_reference/_autosummary/keysight.pwdatatools.Float32.name.md)
      * [Float32.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Float32.__init__.md)
      * [Float32.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.Float32.from_name.md)
      * [Float32.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Float32.from_numpy_dtype.md)
      * [Float32.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.Float32.is_boolean.md)
      * [Float32.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.Float32.is_complex.md)
      * [Float32.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.Float32.is_float.md)
      * [Float32.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Float32.is_integer.md)
      * [Float32.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.Float32.is_numeric.md)
      * [Float32.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Float32.is_signed_integer.md)
      * [Float32.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.Float32.is_string.md)
      * [Float32.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Float32.is_unsigned_integer.md)
      * [Float32.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Float32.to_numpy_dtype.md)
    - [Float64](../../api_reference/_autosummary/keysight.pwdatatools.Float64.md)
      * [Float64.name](../../api_reference/_autosummary/keysight.pwdatatools.Float64.name.md)
      * [Float64.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Float64.__init__.md)
      * [Float64.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.Float64.from_name.md)
      * [Float64.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Float64.from_numpy_dtype.md)
      * [Float64.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.Float64.is_boolean.md)
      * [Float64.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.Float64.is_complex.md)
      * [Float64.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.Float64.is_float.md)
      * [Float64.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Float64.is_integer.md)
      * [Float64.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.Float64.is_numeric.md)
      * [Float64.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Float64.is_signed_integer.md)
      * [Float64.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.Float64.is_string.md)
      * [Float64.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Float64.is_unsigned_integer.md)
      * [Float64.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Float64.to_numpy_dtype.md)
    - [Int8](../../api_reference/_autosummary/keysight.pwdatatools.Int8.md)
      * [Int8.name](../../api_reference/_autosummary/keysight.pwdatatools.Int8.name.md)
      * [Int8.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Int8.__init__.md)
      * [Int8.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.Int8.from_name.md)
      * [Int8.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Int8.from_numpy_dtype.md)
      * [Int8.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.Int8.is_boolean.md)
      * [Int8.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.Int8.is_complex.md)
      * [Int8.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.Int8.is_float.md)
      * [Int8.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int8.is_integer.md)
      * [Int8.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.Int8.is_numeric.md)
      * [Int8.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int8.is_signed_integer.md)
      * [Int8.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.Int8.is_string.md)
      * [Int8.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int8.is_unsigned_integer.md)
      * [Int8.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Int8.to_numpy_dtype.md)
    - [Int16](../../api_reference/_autosummary/keysight.pwdatatools.Int16.md)
      * [Int16.name](../../api_reference/_autosummary/keysight.pwdatatools.Int16.name.md)
      * [Int16.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Int16.__init__.md)
      * [Int16.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.Int16.from_name.md)
      * [Int16.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Int16.from_numpy_dtype.md)
      * [Int16.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.Int16.is_boolean.md)
      * [Int16.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.Int16.is_complex.md)
      * [Int16.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.Int16.is_float.md)
      * [Int16.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int16.is_integer.md)
      * [Int16.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.Int16.is_numeric.md)
      * [Int16.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int16.is_signed_integer.md)
      * [Int16.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.Int16.is_string.md)
      * [Int16.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int16.is_unsigned_integer.md)
      * [Int16.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Int16.to_numpy_dtype.md)
    - [Int32](../../api_reference/_autosummary/keysight.pwdatatools.Int32.md)
      * [Int32.name](../../api_reference/_autosummary/keysight.pwdatatools.Int32.name.md)
      * [Int32.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Int32.__init__.md)
      * [Int32.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.Int32.from_name.md)
      * [Int32.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Int32.from_numpy_dtype.md)
      * [Int32.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.Int32.is_boolean.md)
      * [Int32.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.Int32.is_complex.md)
      * [Int32.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.Int32.is_float.md)
      * [Int32.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int32.is_integer.md)
      * [Int32.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.Int32.is_numeric.md)
      * [Int32.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int32.is_signed_integer.md)
      * [Int32.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.Int32.is_string.md)
      * [Int32.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int32.is_unsigned_integer.md)
      * [Int32.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Int32.to_numpy_dtype.md)
    - [Int64](../../api_reference/_autosummary/keysight.pwdatatools.Int64.md)
      * [Int64.name](../../api_reference/_autosummary/keysight.pwdatatools.Int64.name.md)
      * [Int64.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.Int64.__init__.md)
      * [Int64.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.Int64.from_name.md)
      * [Int64.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Int64.from_numpy_dtype.md)
      * [Int64.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.Int64.is_boolean.md)
      * [Int64.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.Int64.is_complex.md)
      * [Int64.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.Int64.is_float.md)
      * [Int64.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int64.is_integer.md)
      * [Int64.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.Int64.is_numeric.md)
      * [Int64.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int64.is_signed_integer.md)
      * [Int64.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.Int64.is_string.md)
      * [Int64.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.Int64.is_unsigned_integer.md)
      * [Int64.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.Int64.to_numpy_dtype.md)
    - [String](../../api_reference/_autosummary/keysight.pwdatatools.String.md)
      * [String.name](../../api_reference/_autosummary/keysight.pwdatatools.String.name.md)
      * [String.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.String.__init__.md)
      * [String.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.String.from_name.md)
      * [String.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.String.from_numpy_dtype.md)
      * [String.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.String.is_boolean.md)
      * [String.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.String.is_complex.md)
      * [String.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.String.is_float.md)
      * [String.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.String.is_integer.md)
      * [String.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.String.is_numeric.md)
      * [String.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.String.is_signed_integer.md)
      * [String.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.String.is_string.md)
      * [String.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.String.is_unsigned_integer.md)
      * [String.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.String.to_numpy_dtype.md)
    - [UInt8](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.md)
      * [UInt8.name](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.name.md)
      * [UInt8.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.__init__.md)
      * [UInt8.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.from_name.md)
      * [UInt8.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.from_numpy_dtype.md)
      * [UInt8.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_boolean.md)
      * [UInt8.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_complex.md)
      * [UInt8.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_float.md)
      * [UInt8.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_integer.md)
      * [UInt8.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_numeric.md)
      * [UInt8.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_signed_integer.md)
      * [UInt8.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_string.md)
      * [UInt8.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_unsigned_integer.md)
      * [UInt8.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.UInt8.to_numpy_dtype.md)
    - [UInt16](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.md)
      * [UInt16.name](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.name.md)
      * [UInt16.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.__init__.md)
      * [UInt16.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.from_name.md)
      * [UInt16.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.from_numpy_dtype.md)
      * [UInt16.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_boolean.md)
      * [UInt16.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_complex.md)
      * [UInt16.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_float.md)
      * [UInt16.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_integer.md)
      * [UInt16.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_numeric.md)
      * [UInt16.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_signed_integer.md)
      * [UInt16.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_string.md)
      * [UInt16.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_unsigned_integer.md)
      * [UInt16.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.UInt16.to_numpy_dtype.md)
    - [UInt32](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.md)
      * [UInt32.name](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.name.md)
      * [UInt32.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.__init__.md)
      * [UInt32.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.from_name.md)
      * [UInt32.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.from_numpy_dtype.md)
      * [UInt32.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_boolean.md)
      * [UInt32.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_complex.md)
      * [UInt32.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_float.md)
      * [UInt32.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_integer.md)
      * [UInt32.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_numeric.md)
      * [UInt32.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_signed_integer.md)
      * [UInt32.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_string.md)
      * [UInt32.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_unsigned_integer.md)
      * [UInt32.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.UInt32.to_numpy_dtype.md)
    - [UInt64](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.md)
      * [UInt64.name](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.name.md)
      * [UInt64.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.__init__.md)
      * [UInt64.from\_name](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.from_name.md)
      * [UInt64.from\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.from_numpy_dtype.md)
      * [UInt64.is\_boolean](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_boolean.md)
      * [UInt64.is\_complex](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_complex.md)
      * [UInt64.is\_float](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_float.md)
      * [UInt64.is\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_integer.md)
      * [UInt64.is\_numeric](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_numeric.md)
      * [UInt64.is\_signed\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_signed_integer.md)
      * [UInt64.is\_string](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_string.md)
      * [UInt64.is\_unsigned\_integer](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_unsigned_integer.md)
      * [UInt64.to\_numpy\_dtype](../../api_reference/_autosummary/keysight.pwdatatools.UInt64.to_numpy_dtype.md)
    - [FillValues](../../api_reference/_autosummary/keysight.pwdatatools.FillValues.md)
      * [FillValues.boolean](../../api_reference/_autosummary/keysight.pwdatatools.FillValues.boolean.md)
      * [FillValues.complexfloating](../../api_reference/_autosummary/keysight.pwdatatools.FillValues.complexfloating.md)
      * [FillValues.floating](../../api_reference/_autosummary/keysight.pwdatatools.FillValues.floating.md)
      * [FillValues.integer](../../api_reference/_autosummary/keysight.pwdatatools.FillValues.integer.md)
      * [FillValues.string](../../api_reference/_autosummary/keysight.pwdatatools.FillValues.string.md)
      * [FillValues.\_\_init\_\_](../../api_reference/_autosummary/keysight.pwdatatools.FillValues.__init__.md)
      * [FillValues.get\_fill\_value](../../api_reference/_autosummary/keysight.pwdatatools.FillValues.get_fill_value.md)
      * [FillValues.replace](../../api_reference/_autosummary/keysight.pwdatatools.FillValues.replace.md)
  + [Concatenation](../../api_reference/concatenation.md)
    - [concatenate\_blocks](../../api_reference/_autosummary/keysight.pwdatatools.concatenate_blocks.md)
    - [concatenate\_loadpullblocks](../../api_reference/_autosummary/keysight.pwdatatools.concatenate_loadpullblocks.md)
    - [concatenate\_vars](../../api_reference/_autosummary/keysight.pwdatatools.concatenate_vars.md)
  + [Global Options](../../api_reference/global_options.md)
* [Changelog](../../changelog.md)

# Load Pull Basics[](#Load-Pull-Basics "Link to this heading")

This example demonstrates how to work with load pull data in pwdatatools. First, we create some example data using the pwdatatools loadpull example module. Then, we explore that data using various features of the pwdatatools library. This notebook is available for download from the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools).

## Create some data[](#Create-some-data "Link to this heading")

Let’s generate the data that we will use throughout this example. There are many ways to do this, but we will use a function available in the `pwdatatools.examples` submodule that can manufacture load pull data as a pandas DataFrame. To use the function , we must provide it the unique values of all the independents, and the nominal values of the dependents (vs. power). Then, the function fabricates new data, based on the nominal values, at each gamma and frequency. First, let’s define the
unique frequency, gamma, and power points. These will be our independent variables (ivars).

```
[1]:
```

```
freq_points = [1e9, 2e9, 3e9]
gamma_points = [
    0 + 0j,
    0 + 0.25j,
    0 + 0.5j,
    0.25 + 0j,
    0.25 + 0.25j,
    0.25 + 0.5j,
    0.5 + 0j,
    0.5 + 0.25j,
    0.5 + 0.5j,
]
power_points = [-20.0, -10, -5, 0.0]
```

Now that we have the ivars handled, let’s create the data points for the dependent variables (dvars). We will create two dvars: gain and efficiency. We only need to define nominal curves vs. power. These nominal curves will be modified to produce different values at each gamma and frequency. Each gain or efficiency value corresponds to a power value, so the nominal curves need to be the same length as the power points (in this example, the length is 4).

```
[2]:
```

```
gain_nominal_points = [10, 10, 9, 8]
eff_nominal_points = [50, 51, 48, 46]
```

Now lets make a pandas Series for each variable.

```
[3]:
```

```
import pandas as pd

freq = pd.Series(freq_points, name="freq")
gamma = pd.Series(gamma_points, name="GammaLoad")
power = pd.Series(power_points, name="PSource")
gain_nominal = pd.Series(gain_nominal_points, name="Gp")
eff_nominal = pd.Series(eff_nominal_points, name="DrainEff")
```

Now, let’s use a function from the `pwdatatools` examples module to create a pandas DataFrame. First, we import pwdatatools with a shorter alias. Then, we access the loadpull examples submodule and the function that is located there.

```
[4]:
```

```
from keysight import pwdatatools as pwdt

df = pwdt.examples.loadpull.make_swept_freq_gamma_power_loadpull_dataframe(
    freq, gamma, power, gain_nominal, eff_nominal
)
df
```

```
[4]:
```

|  |  |  | freq | GammaLoad | PSource | Gp | DrainEff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ifreq | iGammaLoad | iPSource |  |  |  |  |  |
| 0 | 0 | 0 | 1.000000e+09 | 0.00+0.00j | -20.0 | 10.000000 | 50.000000 |
| 1 | 1.000000e+09 | 0.00+0.00j | -10.0 | 10.000000 | 51.000000 |
| 2 | 1.000000e+09 | 0.00+0.00j | -5.0 | 9.000000 | 48.000000 |
| 3 | 1.000000e+09 | 0.00+0.00j | 0.0 | 8.000000 | 46.000000 |
| 1 | 0 | 1.000000e+09 | 0.00+0.25j | -20.0 | 10.250000 | 45.000000 |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 2 | 7 | 3 | 3.000000e+09 | 0.70+0.35j | 0.0 | 8.782624 | 30.347524 |
| 8 | 0 | 3.000000e+09 | 0.70+0.70j | -20.0 | 10.989949 | 30.201010 |
| 1 | 3.000000e+09 | 0.70+0.70j | -10.0 | 10.989949 | 31.201010 |
| 2 | 3.000000e+09 | 0.70+0.70j | -5.0 | 9.989949 | 28.201010 |
| 3 | 3.000000e+09 | 0.70+0.70j | 0.0 | 8.989949 | 26.201010 |

108 rows × 5 columns

Note that the function not only placed the nominal values into the DataFrame, but also manufactured data at each unique frequency point and gamma value. This resulted in a DataFrame with 108 rows. Also, it created integer indexes for each independent variable. These are called idxs in pwdatatools, and the idxnames are always constructed by prefixing an “i” to each ivarname.

## Create a LoadPullBlock[](#Create-a-LoadPullBlock "Link to this heading")

Now let’s create a `LoadPullBlock` from our pandas DataFrame. LoadPullBlock is a subclass of the `Block` class that contains additional functionality for working with load pull data. We use the a function in the `keysight.pwdatatools.examples.loadpull` module to create an example LoadPullBlock. It uses the nominal gain and efficiency values to make points that vary with the magnitude of gamma such that gain increases with increasing gamma magnitude, and efficiency decreases vs. increasing
gamma magnitude. Also, the function varies all the responses vs frequency.

```
[5]:
```

```
lpblock = pwdt.LoadPullBlock.from_pandas_dataframe(
    df, gamma_ivarname="GammaLoad", power_ivarname="PSource", outer_ivarnames=["freq"]
)
lpblock
```

```
[5]:
```

```

LoadPullBlock(
    <'Gp', 'DrainEff' with 108 observations>,
    name='',
    gamma_ivarname='GammaLoad',
    power_ivarname='PSource',
    outer_ivarnames=('freq',),
    attrs={},
)
```

We can see that this LoadPullBlock has 108 observations, which corresponds with the 108 rows in the DataFrame. Remember, the example function automatically created dependent values at each combination of the values of the independents. Let’s print the names of the independent variables (ivars), the dependent variables (dvars), and the indexes (idxs).

```
[6]:
```

```
print("ivars:", lpblock.ivarnames)
print("dvars:", lpblock.dvarnames)
print("idxs:", lpblock.idxnames)
```

```

ivars: ('freq', 'GammaLoad', 'PSource')
dvars: ('Gp', 'DrainEff')
idxs: ('ifreq', 'iGammaLoad', 'iPSource')
```

There are 3 independents (ivars). `LoadPullBlock` can support more than one outer ivar, but we are using just one (`freq`). Each of the LoadPullBlock’s 3 ivars have an associated integer index. Integer indexes are used to avoid floating point precision issues, as well as problems associated with having independent variables that have complex values (i.e. values with real and imaginary parts), like gammas.

## Explore the LoadPullBlock and Vars[](#Explore-the-LoadPullBlock-and-Vars "Link to this heading")

The `LoadPullBlock.info` method provides a useful summary of all the variables. It gives information about each Var’s role, data type, shape, dimensional metadata (dims), unit, min/max, nan/null counts, and whether there is arbitrary metadata (attrs).

```
[7]:
```

```
lpblock.info()
```

```
[7]:
```

|  | freq | GammaLoad | PSource | Gp | DrainEff |
| --- | --- | --- | --- | --- | --- |
| kind | ivar | ivar | ivar | dvar | dvar |
| role | - | gamma | power | - | - |
| dtype | Float64 | Complex128 | Float64 | Float64 | Float64 |
| shape | (108,) | (108,) | (108,) | (108,) | (108,) |
| dims | idx | idx | idx | - | - |
| unit | - | - | - | - | - |
| min | 1.000e+09 | 0.000 | -2.000e+01 | 8.000 | 26.201 |
| max | 3.000e+09 | 0.990 | 0.000e+00 | 10.990 | 51.000 |
| null | - | - | - | - | - |
| nan | - | - | - | - | - |
| attrs | - | - | - | - | - |

To access any variable, you can use the `LoadPullBlock.__getitem__` method by using square brackets and a string key equal to the Var’s name. Let’s access the gamma variable. An instance of `Var` is returned, which stores the data and metadata for a single variable.

```
[8]:
```

```
gamma = lpblock["GammaLoad"]
print(gamma)
```

```

Var(
    <Complex128 data with shape (108,)>,
    name='GammaLoad',
    dims=<Dims with idx>,
    role='gamma',
    unit=None,
    attrs={},
)
```

Note that the above Var has a role equal to “gamma”. This is because when we initialized the LoadPullBlock, we provided the `gamma_ivarname` argument, which causes automatic assignment of the role of “gamma”. Likewise, “PSource” has been assigned the role of “power”.

```
[9]:
```

```
lpblock["PSource"].role
```

```
[9]:
```

```

'power'
```

However, “freq” is a outer ivar, and outer ivars aren’t automatically assigned a role because they are arbitrary.

```
[10]:
```

```
lpblock["freq"].role
```

```
[10]:
```

```

''
```

As previously mentioned, all ivars in this LoadPullBlock have an idx which is stored in the `Var.dims` attribute, and also accessible from the `Var.idx` attribute.

```
[11]:
```

```
gamma.dims
```

```
[11]:
```

```

Dims(
    ndim=1,
    idx=[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3 ...],
)
```

```
[12]:
```

```
gamma.idx
```

```
[12]:
```

```

DimScale([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3 ...])
```

While the `Var` and `LoadPullBlock` classes don’t have any built-in ways to view the raw data points, you can convert them to numpy or pandas objects to view the raw data.

```
[13]:
```

```
gamma.to_numpy_ndarray()
```

```
[13]:
```

```

array([0.  +0.j  , 0.  +0.j  , 0.  +0.j  , 0.  +0.j  , 0.  +0.25j,
       0.  +0.25j, 0.  +0.25j, 0.  +0.25j, 0.  +0.5j , 0.  +0.5j ,
       0.  +0.5j , 0.  +0.5j , 0.25+0.j  , 0.25+0.j  , 0.25+0.j  ,
       0.25+0.j  , 0.25+0.25j, 0.25+0.25j, 0.25+0.25j, 0.25+0.25j,
       0.25+0.5j , 0.25+0.5j , 0.25+0.5j , 0.25+0.5j , 0.5 +0.j  ,
       0.5 +0.j  , 0.5 +0.j  , 0.5 +0.j  , 0.5 +0.25j, 0.5 +0.25j,
       0.5 +0.25j, 0.5 +0.25j, 0.5 +0.5j , 0.5 +0.5j , 0.5 +0.5j ,
       0.5 +0.5j , 0.  +0.j  , 0.  +0.j  , 0.  +0.j  , 0.  +0.j  ,
       0.  +0.3j , 0.  +0.3j , 0.  +0.3j , 0.  +0.3j , 0.  +0.6j ,
       0.  +0.6j , 0.  +0.6j , 0.  +0.6j , 0.3 +0.j  , 0.3 +0.j  ,
       0.3 +0.j  , 0.3 +0.j  , 0.3 +0.3j , 0.3 +0.3j , 0.3 +0.3j ,
       0.3 +0.3j , 0.3 +0.6j , 0.3 +0.6j , 0.3 +0.6j , 0.3 +0.6j ,
       0.6 +0.j  , 0.6 +0.j  , 0.6 +0.j  , 0.6 +0.j  , 0.6 +0.3j ,
       0.6 +0.3j , 0.6 +0.3j , 0.6 +0.3j , 0.6 +0.6j , 0.6 +0.6j ,
       0.6 +0.6j , 0.6 +0.6j , 0.  +0.j  , 0.  +0.j  , 0.  +0.j  ,
       0.  +0.j  , 0.  +0.35j, 0.  +0.35j, 0.  +0.35j, 0.  +0.35j,
       0.  +0.7j , 0.  +0.7j , 0.  +0.7j , 0.  +0.7j , 0.35+0.j  ,
       0.35+0.j  , 0.35+0.j  , 0.35+0.j  , 0.35+0.35j, 0.35+0.35j,
       0.35+0.35j, 0.35+0.35j, 0.35+0.7j , 0.35+0.7j , 0.35+0.7j ,
       0.35+0.7j , 0.7 +0.j  , 0.7 +0.j  , 0.7 +0.j  , 0.7 +0.j  ,
       0.7 +0.35j, 0.7 +0.35j, 0.7 +0.35j, 0.7 +0.35j, 0.7 +0.7j ,
       0.7 +0.7j , 0.7 +0.7j , 0.7 +0.7j ])
```

```
[14]:
```

```
lpblock.to_pandas_dataframe()
```

```
[14]:
```

|  | ifreq | iGammaLoad | iPSource | freq | GammaLoad | PSource | Gp | DrainEff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 1.000000e+09 | 0.00+0.00j | -20.0 | 10.000000 | 50.000000 |
| 1 | 0 | 0 | 1 | 1.000000e+09 | 0.00+0.00j | -10.0 | 10.000000 | 51.000000 |
| 2 | 0 | 0 | 2 | 1.000000e+09 | 0.00+0.00j | -5.0 | 9.000000 | 48.000000 |
| 3 | 0 | 0 | 3 | 1.000000e+09 | 0.00+0.00j | 0.0 | 8.000000 | 46.000000 |
| 4 | 0 | 1 | 0 | 1.000000e+09 | 0.00+0.25j | -20.0 | 10.250000 | 45.000000 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 103 | 2 | 7 | 3 | 3.000000e+09 | 0.70+0.35j | 0.0 | 8.782624 | 30.347524 |
| 104 | 2 | 8 | 0 | 3.000000e+09 | 0.70+0.70j | -20.0 | 10.989949 | 30.201010 |
| 105 | 2 | 8 | 1 | 3.000000e+09 | 0.70+0.70j | -10.0 | 10.989949 | 31.201010 |
| 106 | 2 | 8 | 2 | 3.000000e+09 | 0.70+0.70j | -5.0 | 9.989949 | 28.201010 |
| 107 | 2 | 8 | 3 | 3.000000e+09 | 0.70+0.70j | 0.0 | 8.989949 | 26.201010 |

108 rows × 8 columns

## Manipulating Vars[](#Manipulating-Vars "Link to this heading")

The `Var` class stores data and metadata for a single variable. We already showed how a Var can be converted to a pandas or numpy object. It is also possible to directly use numpy functions with Var objects. It is very common to make calculations for new quantities and figures of merit. If a Var is input into a numpy function, the output is always a numpy ndarray.

```
[15]:
```

```
import numpy as np

np.abs(gamma)  # calculate magnitude of gamma (input is a Var, output is a numpy array)
```

```
[15]:
```

```

array([0.        , 0.        , 0.        , 0.        , 0.25      ,
       0.25      , 0.25      , 0.25      , 0.5       , 0.5       ,
       0.5       , 0.5       , 0.25      , 0.25      , 0.25      ,
       0.25      , 0.35355339, 0.35355339, 0.35355339, 0.35355339,
       0.55901699, 0.55901699, 0.55901699, 0.55901699, 0.5       ,
       0.5       , 0.5       , 0.5       , 0.55901699, 0.55901699,
       0.55901699, 0.55901699, 0.70710678, 0.70710678, 0.70710678,
       0.70710678, 0.        , 0.        , 0.        , 0.        ,
       0.3       , 0.3       , 0.3       , 0.3       , 0.6       ,
       0.6       , 0.6       , 0.6       , 0.3       , 0.3       ,
       0.3       , 0.3       , 0.42426407, 0.42426407, 0.42426407,
       0.42426407, 0.67082039, 0.67082039, 0.67082039, 0.67082039,
       0.6       , 0.6       , 0.6       , 0.6       , 0.67082039,
       0.67082039, 0.67082039, 0.67082039, 0.84852814, 0.84852814,
       0.84852814, 0.84852814, 0.        , 0.        , 0.        ,
       0.        , 0.35      , 0.35      , 0.35      , 0.35      ,
       0.7       , 0.7       , 0.7       , 0.7       , 0.35      ,
       0.35      , 0.35      , 0.35      , 0.49497475, 0.49497475,
       0.49497475, 0.49497475, 0.78262379, 0.78262379, 0.78262379,
       0.78262379, 0.7       , 0.7       , 0.7       , 0.7       ,
       0.78262379, 0.78262379, 0.78262379, 0.78262379, 0.98994949,
       0.98994949, 0.98994949, 0.98994949])
```

If you have already created a Var, you can directly set its role. Here, we set the role for the “freq” outer ivar and the two dependent variables (dvars). Note that setting the roles for outer ivars and for dvars is not as critical as setting roles for gamma and power ivars, but can still be useful.

```
[16]:
```

```
lpblock["freq"].role = "frequency"
lpblock["Gp"].role = "gain"
lpblock["DrainEff"].role = "efficiency"
```

## Filter the LoadPullBlock’s observations[](#Filter-the-LoadPullBlock's-observations "Link to this heading")

It is a common need to filter data according to condition(s). The LoadPullBlock has several methods that can be used for this, including `LoadPullBlock.keep_observations` and `LoadPullBlock.drop_observations`. For example, the following line selects one gamma value of interest.

```
[17]:
```

```
lpblock_single_gamma = lpblock.keep_observations(lpblock["GammaLoad"] == 0 + 0.25j)
```

We can view the filtered LoadPullBlock as a pandas DataFrame to confirm the desired outcome.

```
[18]:
```

```
lpblock_single_gamma.to_pandas_dataframe()
```

```
[18]:
```

|  | ifreq | iGammaLoad | iPSource | freq | GammaLoad | PSource | Gp | DrainEff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 0 | 1.000000e+09 | 0.00+0.25j | -20.0 | 10.25 | 45.0 |
| 1 | 0 | 1 | 1 | 1.000000e+09 | 0.00+0.25j | -10.0 | 10.25 | 46.0 |
| 2 | 0 | 1 | 2 | 1.000000e+09 | 0.00+0.25j | -5.0 | 9.25 | 43.0 |
| 3 | 0 | 1 | 3 | 1.000000e+09 | 0.00+0.25j | 0.0 | 8.25 | 41.0 |

This filtering worked well because the gamma values are all exact. However, this will not always be the case, especially if the data is from a load pull measurement system. In cases where there could be slight variations from gamma point to gamma point even though they are supposed to be considered “the same”, you can use the idxs for filtering instead. This is extremely robust. Below, we filter the LoadPullBlock to select all the second gamma points (which is where gamma index is equal to 1,
since indexing starts at 0).

```
[19]:
```

```
lpblock_2nd_gammas = lpblock.keep_observations(lpblock.gamma_idx() == 1)
lpblock_2nd_gammas.to_pandas_dataframe()
```

```
[19]:
```

|  | ifreq | iGammaLoad | iPSource | freq | GammaLoad | PSource | Gp | DrainEff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 0 | 1.000000e+09 | 0.00+0.25j | -20.0 | 10.25 | 45.0 |
| 1 | 0 | 1 | 1 | 1.000000e+09 | 0.00+0.25j | -10.0 | 10.25 | 46.0 |
| 2 | 0 | 1 | 2 | 1.000000e+09 | 0.00+0.25j | -5.0 | 9.25 | 43.0 |
| 3 | 0 | 1 | 3 | 1.000000e+09 | 0.00+0.25j | 0.0 | 8.25 | 41.0 |
| 4 | 1 | 1 | 0 | 2.000000e+09 | 0.00+0.30j | -20.0 | 10.30 | 44.0 |
| 5 | 1 | 1 | 1 | 2.000000e+09 | 0.00+0.30j | -10.0 | 10.30 | 45.0 |
| 6 | 1 | 1 | 2 | 2.000000e+09 | 0.00+0.30j | -5.0 | 9.30 | 42.0 |
| 7 | 1 | 1 | 3 | 2.000000e+09 | 0.00+0.30j | 0.0 | 8.30 | 40.0 |
| 8 | 2 | 1 | 0 | 3.000000e+09 | 0.00+0.35j | -20.0 | 10.35 | 43.0 |
| 9 | 2 | 1 | 1 | 3.000000e+09 | 0.00+0.35j | -10.0 | 10.35 | 44.0 |
| 10 | 2 | 1 | 2 | 3.000000e+09 | 0.00+0.35j | -5.0 | 9.35 | 41.0 |
| 11 | 2 | 1 | 3 | 3.000000e+09 | 0.00+0.35j | 0.0 | 8.35 | 39.0 |

A condition used to filter a LoadPullBlock can be any boolean 1D array-like object. Common comparison operators such as `<`, `>`, `==`, `!=`, `<=`, and `>=` are supported for use directly on the Vars in the LoadPullBlock. Also, you can combine multiple conditions using boolean operators like `&` and `|`. And instead of specifying which observations we would like to keep, we can specifiy the observations we’d like to drop. Some of these additional filtering capabilities are
illustrated below.

```
[20]:
```

```
lpblock_filtered = lpblock.drop_observations(
    (lpblock["DrainEff"] < 40) | (lpblock["freq"] <= 2e9)
)
lpblock_filtered.to_pandas_dataframe()
```

```
[20]:
```

|  | ifreq | iGammaLoad | iPSource | freq | GammaLoad | PSource | Gp | DrainEff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2 | 0 | 0 | 3.000000e+09 | 0.00+0.00j | -20.0 | 10.000000 | 50.000000 |
| 1 | 2 | 0 | 1 | 3.000000e+09 | 0.00+0.00j | -10.0 | 10.000000 | 51.000000 |
| 2 | 2 | 0 | 2 | 3.000000e+09 | 0.00+0.00j | -5.0 | 9.000000 | 48.000000 |
| 3 | 2 | 0 | 3 | 3.000000e+09 | 0.00+0.00j | 0.0 | 8.000000 | 46.000000 |
| 4 | 2 | 1 | 0 | 3.000000e+09 | 0.00+0.35j | -20.0 | 10.350000 | 43.000000 |
| 5 | 2 | 1 | 1 | 3.000000e+09 | 0.00+0.35j | -10.0 | 10.350000 | 44.000000 |
| 6 | 2 | 1 | 2 | 3.000000e+09 | 0.00+0.35j | -5.0 | 9.350000 | 41.000000 |
| 7 | 2 | 3 | 0 | 3.000000e+09 | 0.35+0.00j | -20.0 | 10.350000 | 43.000000 |
| 8 | 2 | 3 | 1 | 3.000000e+09 | 0.35+0.00j | -10.0 | 10.350000 | 44.000000 |
| 9 | 2 | 3 | 2 | 3.000000e+09 | 0.35+0.00j | -5.0 | 9.350000 | 41.000000 |
| 10 | 2 | 4 | 0 | 3.000000e+09 | 0.35+0.35j | -20.0 | 10.494975 | 40.100505 |
| 11 | 2 | 4 | 1 | 3.000000e+09 | 0.35+0.35j | -10.0 | 10.494975 | 41.100505 |

## Plot the Vars in a LoadPullBlock[](#Plot-the-Vars-in-a-LoadPullBlock "Link to this heading")

Viewing the raw data can only provide basic sanity checks. To gain real insights, we must plot it. There are many Python libraries for plotting, but this demo uses `matplotlib`, `seaborn`, and the `viz` submodule in pwdatatools. The `keysight.pwdatatools.viz` module builds on matplotlib and seaborn and provides additional functionality and conveniences. For example, the `viz.smith_chart` function draws a Smith chart on a matplotlib Axes. The `viz.use_keysight_theme` function sets the
matplotlib rcParams to use the Keysight color theme. The `viz.contourplot` function and the `LoadPullBlock.contourplot` method provide some conveniences for contour plotting beyond those available in matplotlib alone. But, using the plotting features in `keysight.pwdatatools.viz` is optional.

First, let’s import matplotlib, seaborn, and the `pwdatatools.viz` module and activate the Keysight plotting theme.

```
[21]:
```

```
import matplotlib.pyplot as plt
import seaborn as sns
from keysight.pwdatatools import viz

viz.use_keysight_theme()
```

### Gamma scatter plot[](#Gamma-scatter-plot "Link to this heading")

Let’s plot the gamma ivar as a scatterplot using the `LoadPullBlock.gamma_ivar_scatterplot` method. We can see from the gamma plot below that gamma magnitude increases vs. freq. Note that we format the freq values to scientific notation with one decimal place to make the legend more readable.

```
[22]:
```

```
fig, ax = plt.subplots(figsize=(5, 3))
lpblock.gamma_ivar_scatterplot(ax=ax, hue="freq", palette="viridis")
# the next lines are optional, but they make the plot look better
ax.set_title("Gamma points", fontsize=14)
ax.set_xlabel("real(GammaLoad)", fontsize=12)
ax.set_ylabel("imag(GammaLoad)", fontsize=12)
ax.tick_params(labelsize=9)
handles, labels = ax.get_legend_handles_labels()
formatted_labels = [f"{float(label):.1e}" for label in labels]
ax.legend(
    handles,
    formatted_labels,
    bbox_to_anchor=(1, 1),
    loc="upper left",
    title="freq",
    fontsize=10,
    title_fontsize=12,
)
plt.show()
```

![../../_images/examples_loadpull_loadpull_44_0.png](../../_images/examples_loadpull_loadpull_44_0.png)

### Gamma scatter plot on a Smith Chart[](#Gamma-scatter-plot-on-a-Smith-Chart "Link to this heading")

We can also plot gamma on a Smith Chart. The `pwdatatools.viz` module has a function that adds a Smith Chart to a matplotlib Axes.

```
[23]:
```

```
fig, ax = plt.subplots(figsize=(6, 6))
viz.smith_chart(ax)
lpblock.gamma_ivar_scatterplot(ax=ax, hue="freq", palette="viridis")
ax.set_title("Gamma points", fontsize=14)
formatted_labels = [f"{float(label):.1e}" for label in labels]
ax.legend(
    handles,
    formatted_labels,
    title="freq",
    bbox_to_anchor=(0.3, 0.65),
    loc="center",
    fontsize=10,
    title_fontsize=12,
)
plt.show()
```

![../../_images/examples_loadpull_loadpull_46_0.png](../../_images/examples_loadpull_loadpull_46_0.png)

### Gain and efficiency line plots[](#Gain-and-efficiency-line-plots "Link to this heading")

Let’s plot gain vs. power at each frequency. We use `seaborn.lineplot` rather than matplotlib since this function makes it a little easier to automatically sweep the color of each gamma value. Note that we are also accessing the gamma ivar as a string in polar form. This makes the legend work very nicely. If we didn’t do this, we would have warnings from seaborn about complex numbers.

```
[24]:
```

```
fig, axs = plt.subplots(1, 3, figsize=(13, 4), sharey=True)
for ax, freq in zip(axs, freq_points):
    lpblock_at_freq = lpblock.keep_observations(lpblock["freq"] == freq)
    ax.set_title(f"Power Gain at {freq / 1e9} GHz", fontsize=12)
    sns.lineplot(
        data=lpblock_at_freq,
        x="PSource",
        y="Gp",
        hue=lpblock_at_freq.gamma_ivar("polar_str"),
        palette="viridis",
        ax=ax,
    )
    ax.legend(title="GammaLoad", fontsize=8, ncols=3, loc="lower left")
    ax.set_xlabel("PSource (dBm)", fontsize=10)
    ax.set_ylabel("Gp (dB)", fontsize=10)
    ax.set_ylim(6, 12)
    ax.tick_params(labelsize=9)
plt.tight_layout()
```

![../../_images/examples_loadpull_loadpull_48_0.png](../../_images/examples_loadpull_loadpull_48_0.png)

We can see from the plots that gain compresses with increasing power, and increases with the magnitude of gamma. This is simply because the `make_swept_freq_gamma_power_loadpull_dataframe` function that we used earlier constructed the data in this way.

Now, let’s generate similar plots for efficiency.

```
[25]:
```

```
fig, axs = plt.subplots(1, 3, figsize=(13, 4), sharey=True)
for ax, freq in zip(axs, freq_points):
    lpblock_at_freq = lpblock.keep_observations(lpblock["freq"] == freq)
    ax.set_title(f"Drain Efficiency at {freq / 1e9} GHz", fontsize=12)
    sns.lineplot(
        data=lpblock_at_freq,
        x="PSource",
        y="DrainEff",
        hue=lpblock_at_freq.gamma_ivar("polar_str"),
        palette="viridis",
        ax=ax,
    )
    ax.legend(title="GammaLoad", fontsize=8, ncols=3, loc="lower left")
    ax.set_xlabel("PSource (dBm)", fontsize=10)
    ax.set_ylabel("DrainEff (%)", fontsize=10)
    ax.set_ylim(10, 60)
    ax.tick_params(labelsize=9)
plt.tight_layout()
```

![../../_images/examples_loadpull_loadpull_50_0.png](../../_images/examples_loadpull_loadpull_50_0.png)

### Gain and efficiency contour plots[](#Gain-and-efficiency-contour-plots "Link to this heading")

Next, let’s plot gain and efficiency contours. Rather than sweep through frequencies and power levels like before, let’s just plot contours at a particular frequency and source power value. The `LoadPullBlock.contourplot` method is a convenient way to plot contours. It returns a `matplotlib.QuadContourSet` object, which can be further customized. For example, we customize it using the `matplotlib.pyplot.clabel` function to add labels to the contours. From the plots, we can see that the
nominal gain and efficiency values are at the center of the Smith chart, and that gain increases as we move away from the center, while efficiency decreases as we move away from the center.

```
[26]:
```

```
lpblock_at_single_freq_and_power = lpblock.keep_observations(
    (lpblock["freq"] == 1e9) & (lpblock["PSource"] == -10)
)
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
titles = ["Power Gain", "Drain Efficiency"]
varnames = ["Gp", "DrainEff"]
for i, ax in enumerate(axs):
    viz.smith_chart(ax)
    ax.set_title(titles[i], fontsize=12)
    cs = lpblock_at_single_freq_and_power.contourplot(
        varnames[i], ax=ax, levels=10, colors="red", alpha=0.8, linewidths=1.2
    )
    plt.clabel(cs, inline=True, fontsize=10, fmt="%.1f")
plt.tight_layout()
```

![../../_images/examples_loadpull_loadpull_52_0.png](../../_images/examples_loadpull_loadpull_52_0.png)

## Interpolate and extrapolate power values[](#Interpolate-and-extrapolate-power-values "Link to this heading")

Previously, we selected an existing power value using the `LoadPullBlock.keep_observations` method. The `LoadPullBlock.at_power` method allows for interpolation and extrapolation of the responses at different, non-existent power values (in addition to existing power values). We use linear interpolation and extrapolation here, rather than the cubic defaults because our manufactured data has a very limited number of data points. We are interpolating at power level -12dBm. We are using the
existing -5dBm power point (no interpolation or extrapolation). We are extrapolating up to +5dBm.

```
[27]:
```

```
lpblock_at_powers = lpblock.at_power(
    [-12, -5, 5], "PSource", extrap=True, extrap_method="linear", interp_method="linear"
)
```

Now, let’s plot the interpolated gain and efficiency on top of the existing plots, at a particular frequency.

```
[28]:
```

```
freq = 2e9
lpblock_at_single_freq = lpblock.keep_observations(lpblock["freq"] == freq)
lpblock_at_powers_single_freq = lpblock_at_powers.keep_observations(
    lpblock_at_powers["freq"] == freq
)
fig, axs = plt.subplots(1, 2, figsize=(13, 4))
titles = ["Power Gain", "Drain Efficiency"]
varnames = ["Gp", "DrainEff"]
for i, ax in enumerate(axs):
    ax.set_title(f"{titles[i]} at {freq / 1e9} GHz", fontsize=12)
    sns.lineplot(
        data=lpblock_at_single_freq,
        x="PSource",
        y=varnames[i],
        hue=lpblock_at_single_freq.gamma_ivar("polar_str"),
        palette="viridis",
        ax=ax,
    )
    sns.scatterplot(
        data=lpblock_at_powers_single_freq,
        x="PSource",
        y=varnames[i],
        hue=lpblock_at_powers_single_freq.gamma_ivar("polar_str"),
        palette="viridis",
        ax=ax,
        marker="o",
        legend=False,
    )
    ax.legend(title="GammaLoad", fontsize=8, ncols=3, loc="lower left")
    ax.set_xlabel("PSource (dBm)", fontsize=10)
    ax.set_ylabel(titles[i], fontsize=10)
    ax.tick_params(labelsize=9)
plt.tight_layout()
```

![../../_images/examples_loadpull_loadpull_56_0.png](../../_images/examples_loadpull_loadpull_56_0.png)

## Calculate responses at gain compression points[](#Calculate-responses-at-gain-compression-points "Link to this heading")

The `LoadPullBlock.at_gcomp` method can be used to calculate all responses at the desired level(s) of gain compression.

```
[29]:
```

```
lpblock_at_gcomp = lpblock.at_gcomp([1, 3], "Gp", extrap=True)
```

Now, let’s plot the gain and efficiency points at those particular compression levels on top of the existing plots, at a particular frequency.

```
[30]:
```

```
freq = 3e9
lpblock_at_single_freq = lpblock.keep_observations(lpblock["freq"] == freq)
lpblock_at_gcomp_single_freq = lpblock_at_gcomp.keep_observations(
    lpblock_at_gcomp["freq"] == freq
)
fig, axs = plt.subplots(1, 2, figsize=(13, 4))
titles = ["Power Gain", "Drain Efficiency"]
varnames = ["Gp", "DrainEff"]
for i, ax in enumerate(axs):
    ax.set_title(f"{titles[i]} at {freq / 1e9} GHz", fontsize=12)
    sns.lineplot(
        data=lpblock_at_single_freq,
        x="PSource",
        y=varnames[i],
        hue=lpblock_at_single_freq.gamma_ivar("polar_str"),
        palette="viridis",
        ax=ax,
    )
    sns.scatterplot(
        data=lpblock_at_gcomp_single_freq,
        x="PSource",
        y=varnames[i],
        hue=lpblock_at_gcomp_single_freq.gamma_ivar("polar_str"),
        palette="viridis",
        ax=ax,
        marker="o",
        legend=False,
    )
    ax.legend(title="GammaLoad", fontsize=8, ncols=3, loc="lower left")
    ax.set_xlabel("PSource (dBm)", fontsize=10)
    ax.set_ylabel(titles[i], fontsize=10)
    ax.tick_params(labelsize=9)
plt.tight_layout()
```

![../../_images/examples_loadpull_loadpull_60_0.png](../../_images/examples_loadpull_loadpull_60_0.png)

The plots above indicate that we were able to interpolate to find the 1dB compression point, but we had to extrapolate to find the 3dB compression point.

## Plot contours at a desired level of gain compression[](#Plot-contours-at-a-desired-level-of-gain-compression "Link to this heading")

We could also choose to plots contours at a particular frequency and level of gain compression. Below, we plot gain and efficiency contours at 1 GHz and gain compression of 1.5 dB.

```
[31]:
```

```
lpblock_at_one_gcomp_and_freq = lpblock.keep_observations(
    lpblock["freq"] == 1e9
).at_gcomp(1.5, "Gp")
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle("Contour plots at 1.5 Gain Compression and 1 GHz", fontsize=14)
fig.subplots_adjust(top=0.75)
titles = ["Power Gain", "Drain Efficiency"]
varnames = ["Gp", "DrainEff"]
for i, ax in enumerate(axs):
    viz.smith_chart(ax)
    ax.set_title(titles[i], fontsize=12)
    cs = lpblock_at_one_gcomp_and_freq.contourplot(
        varnames[i], ax=ax, levels=10, colors="red", alpha=0.8, linewidths=1.2
    )
    plt.clabel(cs, inline=True, fontsize=10, fmt="%.1f")
plt.tight_layout()
```

![../../_images/examples_loadpull_loadpull_62_0.png](../../_images/examples_loadpull_loadpull_62_0.png)

On this page

[Previous

Getting Started with PathWave Data Tools](../getting_started/getting_started.md)
[Next

API Reference](../../api_reference/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top