<!-- 来源: howto\use_block_class.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-pwdatatools](../index.md)
* [How To](index.md)
* Use the Block Class

0.12.1

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/howto/use_block_class.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* [Initial Setup](../initial_setup.md)
* [Core Concepts](../core_concepts/index.md)
  + [All About Filepaths](../core_concepts/all_about_filepaths.md)
  + [File Extensions and Formats](../core_concepts/file_exts_and_formats.md)
  + [Multi-Dimensional Data](../core_concepts/multi_dimensional_data.md)
  + [pandas DataFrame Indexing](../core_concepts/pandas_dataframe_indexing.md)
* [How To](index.md)
  + [Read a File](read_a_file.md)
  + [Write a File](write_a_file.md)
  + [Translate a File](translate_a_file.md)
  + [Use the Var Class](use_var_class.md)
  + Use the Block Class
  + [Use the Group Class](use_group_class.md)
  + [Use Roles](use_roles.md)
  + [Work with ADS Data](work_with_ADS_data.md)
  + [Work with CSV Data](work_with_csv_data.md)
  + [Work with Load Pull Data](work_with_loadpull_data.md)
  + [Work with S-Parameter Data](work_with_s_parameter_data.md)
  + [Work with SystemVue Data](work_with_SystemVue_data.md)
  + [Show or Hide Log Messages](show_or_hide_messages.md)
  + [Get the Data Tools Version](get_the_version.md)
* [Examples](../examples/index.md)
  + [Getting Started with PathWave Data Tools](../examples/getting_started/getting_started.md)
  + [Load Pull Basics](../examples/loadpull/loadpull.md)
* [API Reference](../api_reference/index.md)
  + [Main](../api_reference/main.md)
    - [Var](../api_reference/_autosummary/keysight.pwdatatools.Var.md)
      * [Var.attrs](../api_reference/_autosummary/keysight.pwdatatools.Var.attrs.md)
      * [Var.block](../api_reference/_autosummary/keysight.pwdatatools.Var.block.md)
      * [Var.dims](../api_reference/_autosummary/keysight.pwdatatools.Var.dims.md)
      * [Var.dtype](../api_reference/_autosummary/keysight.pwdatatools.Var.dtype.md)
      * [Var.idx](../api_reference/_autosummary/keysight.pwdatatools.Var.idx.md)
      * [Var.idxname](../api_reference/_autosummary/keysight.pwdatatools.Var.idxname.md)
      * [Var.kind](../api_reference/_autosummary/keysight.pwdatatools.Var.kind.md)
      * [Var.name](../api_reference/_autosummary/keysight.pwdatatools.Var.name.md)
      * [Var.ndim](../api_reference/_autosummary/keysight.pwdatatools.Var.ndim.md)
      * [Var.role](../api_reference/_autosummary/keysight.pwdatatools.Var.role.md)
      * [Var.shape](../api_reference/_autosummary/keysight.pwdatatools.Var.shape.md)
      * [Var.size](../api_reference/_autosummary/keysight.pwdatatools.Var.size.md)
      * [Var.unit](../api_reference/_autosummary/keysight.pwdatatools.Var.unit.md)
      * [Var.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Var.__init__.md)
      * [Var.add\_role](../api_reference/_autosummary/keysight.pwdatatools.Var.add_role.md)
      * [Var.copy](../api_reference/_autosummary/keysight.pwdatatools.Var.copy.md)
      * [Var.count\_observations](../api_reference/_autosummary/keysight.pwdatatools.Var.count_observations.md)
      * [Var.drop\_observations](../api_reference/_autosummary/keysight.pwdatatools.Var.drop_observations.md)
      * [Var.fill\_nan](../api_reference/_autosummary/keysight.pwdatatools.Var.fill_nan.md)
      * [Var.fill\_null](../api_reference/_autosummary/keysight.pwdatatools.Var.fill_null.md)
      * [Var.from\_1D\_vars](../api_reference/_autosummary/keysight.pwdatatools.Var.from_1D_vars.md)
      * [Var.from\_pandas\_dataframe](../api_reference/_autosummary/keysight.pwdatatools.Var.from_pandas_dataframe.md)
      * [Var.from\_pandas\_series](../api_reference/_autosummary/keysight.pwdatatools.Var.from_pandas_series.md)
      * [Var.has\_dims](../api_reference/_autosummary/keysight.pwdatatools.Var.has_dims.md)
      * [Var.has\_idx](../api_reference/_autosummary/keysight.pwdatatools.Var.has_idx.md)
      * [Var.has\_nan](../api_reference/_autosummary/keysight.pwdatatools.Var.has_nan.md)
      * [Var.has\_null](../api_reference/_autosummary/keysight.pwdatatools.Var.has_null.md)
      * [Var.has\_role](../api_reference/_autosummary/keysight.pwdatatools.Var.has_role.md)
      * [Var.info](../api_reference/_autosummary/keysight.pwdatatools.Var.info.md)
      * [Var.is\_nan](../api_reference/_autosummary/keysight.pwdatatools.Var.is_nan.md)
      * [Var.is\_null](../api_reference/_autosummary/keysight.pwdatatools.Var.is_null.md)
      * [Var.keep\_observations](../api_reference/_autosummary/keysight.pwdatatools.Var.keep_observations.md)
      * [Var.rename](../api_reference/_autosummary/keysight.pwdatatools.Var.rename.md)
      * [Var.repeat\_observations](../api_reference/_autosummary/keysight.pwdatatools.Var.repeat_observations.md)
      * [Var.replace](../api_reference/_autosummary/keysight.pwdatatools.Var.replace.md)
      * [Var.select](../api_reference/_autosummary/keysight.pwdatatools.Var.select.md)
      * [Var.set\_data](../api_reference/_autosummary/keysight.pwdatatools.Var.set_data.md)
      * [Var.set\_data\_in\_place](../api_reference/_autosummary/keysight.pwdatatools.Var.set_data_in_place.md)
      * [Var.sort\_observations](../api_reference/_autosummary/keysight.pwdatatools.Var.sort_observations.md)
      * [Var.to\_numpy\_maskedarray](../api_reference/_autosummary/keysight.pwdatatools.Var.to_numpy_maskedarray.md)
      * [Var.to\_numpy\_ndarray](../api_reference/_autosummary/keysight.pwdatatools.Var.to_numpy_ndarray.md)
      * [Var.to\_pandas\_dataframe](../api_reference/_autosummary/keysight.pwdatatools.Var.to_pandas_dataframe.md)
      * [Var.to\_pandas\_series](../api_reference/_autosummary/keysight.pwdatatools.Var.to_pandas_series.md)
    - [Block](../api_reference/_autosummary/keysight.pwdatatools.Block.md)
      * [Block.attrs](../api_reference/_autosummary/keysight.pwdatatools.Block.attrs.md)
      * [Block.dvarnames](../api_reference/_autosummary/keysight.pwdatatools.Block.dvarnames.md)
      * [Block.exprs](../api_reference/_autosummary/keysight.pwdatatools.Block.exprs.md)
      * [Block.idxnames](../api_reference/_autosummary/keysight.pwdatatools.Block.idxnames.md)
      * [Block.ivarnames](../api_reference/_autosummary/keysight.pwdatatools.Block.ivarnames.md)
      * [Block.name](../api_reference/_autosummary/keysight.pwdatatools.Block.name.md)
      * [Block.varnames](../api_reference/_autosummary/keysight.pwdatatools.Block.varnames.md)
      * [Block.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Block.__init__.md)
      * [Block.clear](../api_reference/_autosummary/keysight.pwdatatools.Block.clear.md)
      * [Block.copy](../api_reference/_autosummary/keysight.pwdatatools.Block.copy.md)
      * [Block.count\_observations](../api_reference/_autosummary/keysight.pwdatatools.Block.count_observations.md)
      * [Block.crucial\_varnames](../api_reference/_autosummary/keysight.pwdatatools.Block.crucial_varnames.md)
      * [Block.drop\_observations](../api_reference/_autosummary/keysight.pwdatatools.Block.drop_observations.md)
      * [Block.drop\_vars](../api_reference/_autosummary/keysight.pwdatatools.Block.drop_vars.md)
      * [Block.drop\_vars\_in\_place](../api_reference/_autosummary/keysight.pwdatatools.Block.drop_vars_in_place.md)
      * [Block.eval\_expr\_as\_var](../api_reference/_autosummary/keysight.pwdatatools.Block.eval_expr_as_var.md)
      * [Block.fill\_nan](../api_reference/_autosummary/keysight.pwdatatools.Block.fill_nan.md)
      * [Block.fill\_null](../api_reference/_autosummary/keysight.pwdatatools.Block.fill_null.md)
      * [Block.from\_file](../api_reference/_autosummary/keysight.pwdatatools.Block.from_file.md)
      * [Block.from\_pandas\_dataframe](../api_reference/_autosummary/keysight.pwdatatools.Block.from_pandas_dataframe.md)
      * [Block.get](../api_reference/_autosummary/keysight.pwdatatools.Block.get.md)
      * [Block.get\_var](../api_reference/_autosummary/keysight.pwdatatools.Block.get_var.md)
      * [Block.get\_var\_as\_expr](../api_reference/_autosummary/keysight.pwdatatools.Block.get_var_as_expr.md)
      * [Block.info](../api_reference/_autosummary/keysight.pwdatatools.Block.info.md)
      * [Block.items](../api_reference/_autosummary/keysight.pwdatatools.Block.items.md)
      * [Block.iter\_sweep\_nodes](../api_reference/_autosummary/keysight.pwdatatools.Block.iter_sweep_nodes.md)
      * [Block.iter\_vars](../api_reference/_autosummary/keysight.pwdatatools.Block.iter_vars.md)
      * [Block.keep\_observations](../api_reference/_autosummary/keysight.pwdatatools.Block.keep_observations.md)
      * [Block.keep\_vars](../api_reference/_autosummary/keysight.pwdatatools.Block.keep_vars.md)
      * [Block.keep\_vars\_in\_place](../api_reference/_autosummary/keysight.pwdatatools.Block.keep_vars_in_place.md)
      * [Block.keys](../api_reference/_autosummary/keysight.pwdatatools.Block.keys.md)
      * [Block.make\_idxs](../api_reference/_autosummary/keysight.pwdatatools.Block.make_idxs.md)
      * [Block.pop](../api_reference/_autosummary/keysight.pwdatatools.Block.pop.md)
      * [Block.popitem](../api_reference/_autosummary/keysight.pwdatatools.Block.popitem.md)
      * [Block.rename\_vars](../api_reference/_autosummary/keysight.pwdatatools.Block.rename_vars.md)
      * [Block.rename\_vars\_in\_place](../api_reference/_autosummary/keysight.pwdatatools.Block.rename_vars_in_place.md)
      * [Block.set\_data](../api_reference/_autosummary/keysight.pwdatatools.Block.set_data.md)
      * [Block.set\_data\_in\_place](../api_reference/_autosummary/keysight.pwdatatools.Block.set_data_in_place.md)
      * [Block.set\_vars](../api_reference/_autosummary/keysight.pwdatatools.Block.set_vars.md)
      * [Block.set\_vars\_in\_place](../api_reference/_autosummary/keysight.pwdatatools.Block.set_vars_in_place.md)
      * [Block.setdefault](../api_reference/_autosummary/keysight.pwdatatools.Block.setdefault.md)
      * [Block.sort\_observations](../api_reference/_autosummary/keysight.pwdatatools.Block.sort_observations.md)
      * [Block.sort\_observations\_by](../api_reference/_autosummary/keysight.pwdatatools.Block.sort_observations_by.md)
      * [Block.sort\_vars](../api_reference/_autosummary/keysight.pwdatatools.Block.sort_vars.md)
      * [Block.to\_file](../api_reference/_autosummary/keysight.pwdatatools.Block.to_file.md)
      * [Block.to\_pandas\_dataframe](../api_reference/_autosummary/keysight.pwdatatools.Block.to_pandas_dataframe.md)
      * [Block.update](../api_reference/_autosummary/keysight.pwdatatools.Block.update.md)
      * [Block.values](../api_reference/_autosummary/keysight.pwdatatools.Block.values.md)
    - [Group](../api_reference/_autosummary/keysight.pwdatatools.Group.md)
      * [Group.attrs](../api_reference/_autosummary/keysight.pwdatatools.Group.attrs.md)
      * [Group.members](../api_reference/_autosummary/keysight.pwdatatools.Group.members.md)
      * [Group.name](../api_reference/_autosummary/keysight.pwdatatools.Group.name.md)
      * [Group.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Group.__init__.md)
      * [Group.append](../api_reference/_autosummary/keysight.pwdatatools.Group.append.md)
      * [Group.clear](../api_reference/_autosummary/keysight.pwdatatools.Group.clear.md)
      * [Group.copy](../api_reference/_autosummary/keysight.pwdatatools.Group.copy.md)
      * [Group.count](../api_reference/_autosummary/keysight.pwdatatools.Group.count.md)
      * [Group.extend](../api_reference/_autosummary/keysight.pwdatatools.Group.extend.md)
      * [Group.fill\_membernames](../api_reference/_autosummary/keysight.pwdatatools.Group.fill_membernames.md)
      * [Group.filled\_membernames](../api_reference/_autosummary/keysight.pwdatatools.Group.filled_membernames.md)
      * [Group.flatten](../api_reference/_autosummary/keysight.pwdatatools.Group.flatten.md)
      * [Group.flattened](../api_reference/_autosummary/keysight.pwdatatools.Group.flattened.md)
      * [Group.from\_file](../api_reference/_autosummary/keysight.pwdatatools.Group.from_file.md)
      * [Group.get\_member](../api_reference/_autosummary/keysight.pwdatatools.Group.get_member.md)
      * [Group.get\_member\_as\_block](../api_reference/_autosummary/keysight.pwdatatools.Group.get_member_as_block.md)
      * [Group.get\_member\_as\_group](../api_reference/_autosummary/keysight.pwdatatools.Group.get_member_as_group.md)
      * [Group.get\_member\_as\_loadpullblock](../api_reference/_autosummary/keysight.pwdatatools.Group.get_member_as_loadpullblock.md)
      * [Group.index](../api_reference/_autosummary/keysight.pwdatatools.Group.index.md)
      * [Group.insert](../api_reference/_autosummary/keysight.pwdatatools.Group.insert.md)
      * [Group.iter\_blocks](../api_reference/_autosummary/keysight.pwdatatools.Group.iter_blocks.md)
      * [Group.iter\_members](../api_reference/_autosummary/keysight.pwdatatools.Group.iter_members.md)
      * [Group.pop](../api_reference/_autosummary/keysight.pwdatatools.Group.pop.md)
      * [Group.remove](../api_reference/_autosummary/keysight.pwdatatools.Group.remove.md)
      * [Group.reverse](../api_reference/_autosummary/keysight.pwdatatools.Group.reverse.md)
      * [Group.to\_file](../api_reference/_autosummary/keysight.pwdatatools.Group.to_file.md)
      * [Group.tree](../api_reference/_autosummary/keysight.pwdatatools.Group.tree.md)
  + [Metadata](../api_reference/metadata.md)
    - [AttrsDict](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.md)
      * [AttrsDict.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.__init__.md)
      * [AttrsDict.clear](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.clear.md)
      * [AttrsDict.copy](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.copy.md)
      * [AttrsDict.get](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.get.md)
      * [AttrsDict.items](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.items.md)
      * [AttrsDict.keys](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.keys.md)
      * [AttrsDict.pop](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.pop.md)
      * [AttrsDict.popitem](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.popitem.md)
      * [AttrsDict.setdefault](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.setdefault.md)
      * [AttrsDict.update](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.update.md)
      * [AttrsDict.values](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.values.md)
    - [Dims](../api_reference/_autosummary/keysight.pwdatatools.Dims.md)
      * [Dims.i\_names](../api_reference/_autosummary/keysight.pwdatatools.Dims.i_names.md)
      * [Dims.i\_nums](../api_reference/_autosummary/keysight.pwdatatools.Dims.i_nums.md)
      * [Dims.idx](../api_reference/_autosummary/keysight.pwdatatools.Dims.idx.md)
      * [Dims.j\_names](../api_reference/_autosummary/keysight.pwdatatools.Dims.j_names.md)
      * [Dims.j\_nums](../api_reference/_autosummary/keysight.pwdatatools.Dims.j_nums.md)
      * [Dims.ndim](../api_reference/_autosummary/keysight.pwdatatools.Dims.ndim.md)
      * [Dims.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Dims.__init__.md)
      * [Dims.copy](../api_reference/_autosummary/keysight.pwdatatools.Dims.copy.md)
      * [Dims.get\_dimscale](../api_reference/_autosummary/keysight.pwdatatools.Dims.get_dimscale.md)
      * [Dims.has\_i\_names](../api_reference/_autosummary/keysight.pwdatatools.Dims.has_i_names.md)
      * [Dims.has\_i\_nums](../api_reference/_autosummary/keysight.pwdatatools.Dims.has_i_nums.md)
      * [Dims.has\_idx](../api_reference/_autosummary/keysight.pwdatatools.Dims.has_idx.md)
      * [Dims.has\_j\_names](../api_reference/_autosummary/keysight.pwdatatools.Dims.has_j_names.md)
      * [Dims.has\_j\_nums](../api_reference/_autosummary/keysight.pwdatatools.Dims.has_j_nums.md)
      * [Dims.is\_compatible\_with\_shape](../api_reference/_autosummary/keysight.pwdatatools.Dims.is_compatible_with_shape.md)
      * [Dims.is\_empty](../api_reference/_autosummary/keysight.pwdatatools.Dims.is_empty.md)
      * [Dims.keep\_where](../api_reference/_autosummary/keysight.pwdatatools.Dims.keep_where.md)
      * [Dims.partial\_shape](../api_reference/_autosummary/keysight.pwdatatools.Dims.partial_shape.md)
      * [Dims.replace](../api_reference/_autosummary/keysight.pwdatatools.Dims.replace.md)
    - [DimScale](../api_reference/_autosummary/keysight.pwdatatools.DimScale.md)
      * [DimScale.name](../api_reference/_autosummary/keysight.pwdatatools.DimScale.name.md)
      * [DimScale.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.DimScale.__init__.md)
      * [DimScale.copy](../api_reference/_autosummary/keysight.pwdatatools.DimScale.copy.md)
      * [DimScale.from\_pandas\_index](../api_reference/_autosummary/keysight.pwdatatools.DimScale.from_pandas_index.md)
      * [DimScale.has\_names\_values](../api_reference/_autosummary/keysight.pwdatatools.DimScale.has_names_values.md)
      * [DimScale.has\_nums\_values](../api_reference/_autosummary/keysight.pwdatatools.DimScale.has_nums_values.md)
      * [DimScale.rename](../api_reference/_autosummary/keysight.pwdatatools.DimScale.rename.md)
      * [DimScale.to\_numpy\_ndarray](../api_reference/_autosummary/keysight.pwdatatools.DimScale.to_numpy_ndarray.md)
      * [DimScale.view\_values](../api_reference/_autosummary/keysight.pwdatatools.DimScale.view_values.md)
    - [Expr](../api_reference/_autosummary/keysight.pwdatatools.Expr.md)
      * [Expr.input](../api_reference/_autosummary/keysight.pwdatatools.Expr.input.md)
      * [Expr.ops](../api_reference/_autosummary/keysight.pwdatatools.Expr.ops.md)
      * [Expr.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Expr.__init__.md)
      * [Expr.abs](../api_reference/_autosummary/keysight.pwdatatools.Expr.abs.md)
      * [Expr.angle](../api_reference/_autosummary/keysight.pwdatatools.Expr.angle.md)
      * [Expr.copy](../api_reference/_autosummary/keysight.pwdatatools.Expr.copy.md)
      * [Expr.dB](../api_reference/_autosummary/keysight.pwdatatools.Expr.dB.md)
      * [Expr.decibel](../api_reference/_autosummary/keysight.pwdatatools.Expr.decibel.md)
      * [Expr.eval\_as\_numpy\_ndarray](../api_reference/_autosummary/keysight.pwdatatools.Expr.eval_as_numpy_ndarray.md)
      * [Expr.imag](../api_reference/_autosummary/keysight.pwdatatools.Expr.imag.md)
      * [Expr.mag](../api_reference/_autosummary/keysight.pwdatatools.Expr.mag.md)
      * [Expr.real](../api_reference/_autosummary/keysight.pwdatatools.Expr.real.md)
    - [ExprsDict](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.md)
      * [ExprsDict.block](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.block.md)
      * [ExprsDict.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.__init__.md)
      * [ExprsDict.clear](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.clear.md)
      * [ExprsDict.copy](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.copy.md)
      * [ExprsDict.get](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.get.md)
      * [ExprsDict.items](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.items.md)
      * [ExprsDict.keys](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.keys.md)
      * [ExprsDict.pop](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.pop.md)
      * [ExprsDict.popitem](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.popitem.md)
      * [ExprsDict.setdefault](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.setdefault.md)
      * [ExprsDict.update](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.update.md)
      * [ExprsDict.values](../api_reference/_autosummary/keysight.pwdatatools.ExprsDict.values.md)
  + [File I/O](../api_reference/fileio.md)
    - [read\_file\_as\_block](../api_reference/_autosummary/keysight.pwdatatools.read_file_as_block.md)
    - [read\_file\_as\_group](../api_reference/_autosummary/keysight.pwdatatools.read_file_as_group.md)
    - [read\_file\_as\_loadpullblock](../api_reference/_autosummary/keysight.pwdatatools.read_file_as_loadpullblock.md)
    - [read\_file](../api_reference/_autosummary/keysight.pwdatatools.read_file.md)
    - [translate\_file](../api_reference/_autosummary/keysight.pwdatatools.translate_file.md)
    - [write\_file](../api_reference/_autosummary/keysight.pwdatatools.write_file.md)
    - [ADSReadOptions](../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.md)
      * [ADSReadOptions.engine\_pref](../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.engine_pref.md)
      * [ADSReadOptions.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.read_or_write.md)
      * [ADSReadOptions.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.__init__.md)
      * [ADSReadOptions.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.get_formats.md)
      * [ADSReadOptions.mapping](../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.mapping.md)
      * [ADSReadOptions.replace](../api_reference/_autosummary/keysight.pwdatatools.ADSReadOptions.replace.md)
    - [ADSWriteInvalid](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.md)
      * [ADSWriteInvalid.boolean](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.boolean.md)
      * [ADSWriteInvalid.boolean\_options](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.boolean_options.md)
      * [ADSWriteInvalid.complexfloating](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.complexfloating.md)
      * [ADSWriteInvalid.complexfloating\_options](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.complexfloating_options.md)
      * [ADSWriteInvalid.floating](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.floating.md)
      * [ADSWriteInvalid.floating\_options](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.floating_options.md)
      * [ADSWriteInvalid.integer](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.integer.md)
      * [ADSWriteInvalid.integer\_null\_rep](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.integer_null_rep.md)
      * [ADSWriteInvalid.integer\_options](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.integer_options.md)
      * [ADSWriteInvalid.nan\_rep](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.nan_rep.md)
      * [ADSWriteInvalid.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.read_or_write.md)
      * [ADSWriteInvalid.string](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.string.md)
      * [ADSWriteInvalid.string\_null\_rep](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.string_null_rep.md)
      * [ADSWriteInvalid.string\_options](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.string_options.md)
      * [ADSWriteInvalid.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.__init__.md)
      * [ADSWriteInvalid.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.get_formats.md)
      * [ADSWriteInvalid.mapping](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.mapping.md)
      * [ADSWriteInvalid.replace](../api_reference/_autosummary/keysight.pwdatatools.ADSWriteInvalid.replace.md)
    - [CITIReadOptions](../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.md)
      * [CITIReadOptions.engine\_pref](../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.engine_pref.md)
      * [CITIReadOptions.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.read_or_write.md)
      * [CITIReadOptions.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.__init__.md)
      * [CITIReadOptions.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.get_formats.md)
      * [CITIReadOptions.mapping](../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.mapping.md)
      * [CITIReadOptions.replace](../api_reference/_autosummary/keysight.pwdatatools.CITIReadOptions.replace.md)
    - [CSVReadOptions](../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.md)
      * [CSVReadOptions.engine\_pref](../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.engine_pref.md)
      * [CSVReadOptions.pandas\_kwargs](../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.pandas_kwargs.md)
      * [CSVReadOptions.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.read_or_write.md)
      * [CSVReadOptions.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.__init__.md)
      * [CSVReadOptions.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.get_formats.md)
      * [CSVReadOptions.mapping](../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.mapping.md)
      * [CSVReadOptions.replace](../api_reference/_autosummary/keysight.pwdatatools.CSVReadOptions.replace.md)
    - [CSVWriteOptions](../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.md)
      * [CSVWriteOptions.cols\_default\_ints](../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.cols_default_ints.md)
      * [CSVWriteOptions.cols\_default\_ints\_forced](../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.cols_default_ints_forced.md)
      * [CSVWriteOptions.cols\_dimscales\_delim](../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.cols_dimscales_delim.md)
      * [CSVWriteOptions.engine\_pref](../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.engine_pref.md)
      * [CSVWriteOptions.pandas\_kwargs](../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.pandas_kwargs.md)
      * [CSVWriteOptions.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.read_or_write.md)
      * [CSVWriteOptions.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.__init__.md)
      * [CSVWriteOptions.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.get_formats.md)
      * [CSVWriteOptions.mapping](../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.mapping.md)
      * [CSVWriteOptions.replace](../api_reference/_autosummary/keysight.pwdatatools.CSVWriteOptions.replace.md)
    - [DataFile](../api_reference/_autosummary/keysight.pwdatatools.DataFile.md)
      * [DataFile.ext](../api_reference/_autosummary/keysight.pwdatatools.DataFile.ext.md)
      * [DataFile.folder](../api_reference/_autosummary/keysight.pwdatatools.DataFile.folder.md)
      * [DataFile.format\_override](../api_reference/_autosummary/keysight.pwdatatools.DataFile.format_override.md)
      * [DataFile.name](../api_reference/_autosummary/keysight.pwdatatools.DataFile.name.md)
      * [DataFile.path](../api_reference/_autosummary/keysight.pwdatatools.DataFile.path.md)
      * [DataFile.stem](../api_reference/_autosummary/keysight.pwdatatools.DataFile.stem.md)
      * [DataFile.suffix](../api_reference/_autosummary/keysight.pwdatatools.DataFile.suffix.md)
      * [DataFile.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.DataFile.__init__.md)
      * [DataFile.copy](../api_reference/_autosummary/keysight.pwdatatools.DataFile.copy.md)
      * [DataFile.delete](../api_reference/_autosummary/keysight.pwdatatools.DataFile.delete.md)
      * [DataFile.exists](../api_reference/_autosummary/keysight.pwdatatools.DataFile.exists.md)
      * [DataFile.find\_diffs](../api_reference/_autosummary/keysight.pwdatatools.DataFile.find_diffs.md)
      * [DataFile.get\_format](../api_reference/_autosummary/keysight.pwdatatools.DataFile.get_format.md)
      * [DataFile.has\_format](../api_reference/_autosummary/keysight.pwdatatools.DataFile.has_format.md)
      * [DataFile.has\_modtime\_match](../api_reference/_autosummary/keysight.pwdatatools.DataFile.has_modtime_match.md)
      * [DataFile.is\_ads](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_ads.md)
      * [DataFile.is\_citi](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_citi.md)
      * [DataFile.is\_csv](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_csv.md)
      * [DataFile.is\_farfieldio](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_farfieldio.md)
      * [DataFile.is\_hfss\_ffd](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_hfss_ffd.md)
      * [DataFile.is\_loadpull](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_loadpull.md)
      * [DataFile.is\_mdif](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_mdif.md)
      * [DataFile.is\_mdm](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_mdm.md)
      * [DataFile.is\_native](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_native.md)
      * [DataFile.is\_s2pmdif](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_s2pmdif.md)
      * [DataFile.is\_same](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_same.md)
      * [DataFile.is\_smatrixio](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_smatrixio.md)
      * [DataFile.is\_systemvue](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_systemvue.md)
      * [DataFile.is\_touchstone](../api_reference/_autosummary/keysight.pwdatatools.DataFile.is_touchstone.md)
      * [DataFile.lines](../api_reference/_autosummary/keysight.pwdatatools.DataFile.lines.md)
      * [DataFile.modtime](../api_reference/_autosummary/keysight.pwdatatools.DataFile.modtime.md)
      * [DataFile.modtime\_datetime](../api_reference/_autosummary/keysight.pwdatatools.DataFile.modtime_datetime.md)
      * [DataFile.read\_as\_block](../api_reference/_autosummary/keysight.pwdatatools.DataFile.read_as_block.md)
      * [DataFile.read\_as\_group](../api_reference/_autosummary/keysight.pwdatatools.DataFile.read_as_group.md)
      * [DataFile.read\_as\_loadpullblock](../api_reference/_autosummary/keysight.pwdatatools.DataFile.read_as_loadpullblock.md)
      * [DataFile.remove](../api_reference/_autosummary/keysight.pwdatatools.DataFile.remove.md)
      * [DataFile.set\_modtime](../api_reference/_autosummary/keysight.pwdatatools.DataFile.set_modtime.md)
      * [DataFile.translate](../api_reference/_autosummary/keysight.pwdatatools.DataFile.translate.md)
      * [DataFile.tree](../api_reference/_autosummary/keysight.pwdatatools.DataFile.tree.md)
    - [LoadPullReadOptions](../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.md)
      * [LoadPullReadOptions.always\_freq\_suffixed](../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.always_freq_suffixed.md)
      * [LoadPullReadOptions.derived\_vars](../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.derived_vars.md)
      * [LoadPullReadOptions.power\_ivar\_pref](../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.power_ivar_pref.md)
      * [LoadPullReadOptions.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.read_or_write.md)
      * [LoadPullReadOptions.uniform\_ivars](../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.uniform_ivars.md)
      * [LoadPullReadOptions.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.__init__.md)
      * [LoadPullReadOptions.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.get_formats.md)
      * [LoadPullReadOptions.replace](../api_reference/_autosummary/keysight.pwdatatools.LoadPullReadOptions.replace.md)
    - [LoadPullDerivedVars](../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.md)
      * [LoadPullDerivedVars.freq\_enums](../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.freq_enums.md)
      * [LoadPullDerivedVars.main](../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.main.md)
      * [LoadPullDerivedVars.power\_units](../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.power_units.md)
      * [LoadPullDerivedVars.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.read_or_write.md)
      * [LoadPullDerivedVars.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.__init__.md)
      * [LoadPullDerivedVars.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.get_formats.md)
      * [LoadPullDerivedVars.replace](../api_reference/_autosummary/keysight.pwdatatools.LoadPullDerivedVars.replace.md)
    - [MDIFReadOptions](../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.md)
      * [MDIFReadOptions.engine\_pref](../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.engine_pref.md)
      * [MDIFReadOptions.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.read_or_write.md)
      * [MDIFReadOptions.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.__init__.md)
      * [MDIFReadOptions.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.get_formats.md)
      * [MDIFReadOptions.mapping](../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.mapping.md)
      * [MDIFReadOptions.replace](../api_reference/_autosummary/keysight.pwdatatools.MDIFReadOptions.replace.md)
    - [MDIFWriteInvalid](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.md)
      * [MDIFWriteInvalid.boolean](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.boolean.md)
      * [MDIFWriteInvalid.boolean\_options](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.boolean_options.md)
      * [MDIFWriteInvalid.complexfloating](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.complexfloating.md)
      * [MDIFWriteInvalid.complexfloating\_options](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.complexfloating_options.md)
      * [MDIFWriteInvalid.floating](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.floating.md)
      * [MDIFWriteInvalid.floating\_options](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.floating_options.md)
      * [MDIFWriteInvalid.integer](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.integer.md)
      * [MDIFWriteInvalid.integer\_null\_rep](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.integer_null_rep.md)
      * [MDIFWriteInvalid.integer\_options](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.integer_options.md)
      * [MDIFWriteInvalid.nan\_rep](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.nan_rep.md)
      * [MDIFWriteInvalid.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.read_or_write.md)
      * [MDIFWriteInvalid.string](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.string.md)
      * [MDIFWriteInvalid.string\_null\_rep](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.string_null_rep.md)
      * [MDIFWriteInvalid.string\_options](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.string_options.md)
      * [MDIFWriteInvalid.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.__init__.md)
      * [MDIFWriteInvalid.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.get_formats.md)
      * [MDIFWriteInvalid.mapping](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.mapping.md)
      * [MDIFWriteInvalid.replace](../api_reference/_autosummary/keysight.pwdatatools.MDIFWriteInvalid.replace.md)
    - [MDMReadOptions](../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.md)
      * [MDMReadOptions.iccap\_values\_as\_vars](../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.iccap_values_as_vars.md)
      * [MDMReadOptions.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.read_or_write.md)
      * [MDMReadOptions.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.__init__.md)
      * [MDMReadOptions.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.get_formats.md)
      * [MDMReadOptions.mapping](../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.mapping.md)
      * [MDMReadOptions.replace](../api_reference/_autosummary/keysight.pwdatatools.MDMReadOptions.replace.md)
    - [SMatrixIOReadOptions](../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.md)
      * [SMatrixIOReadOptions.engine\_pref](../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.engine_pref.md)
      * [SMatrixIOReadOptions.network\_blockname](../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.network_blockname.md)
      * [SMatrixIOReadOptions.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.read_or_write.md)
      * [SMatrixIOReadOptions.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.__init__.md)
      * [SMatrixIOReadOptions.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.get_formats.md)
      * [SMatrixIOReadOptions.mapping](../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.mapping.md)
      * [SMatrixIOReadOptions.replace](../api_reference/_autosummary/keysight.pwdatatools.SMatrixIOReadOptions.replace.md)
    - [TouchstoneReadOptions](../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.md)
      * [TouchstoneReadOptions.engine\_pref](../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.engine_pref.md)
      * [TouchstoneReadOptions.network\_blockname](../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.network_blockname.md)
      * [TouchstoneReadOptions.noise\_blockname](../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.noise_blockname.md)
      * [TouchstoneReadOptions.read\_or\_write](../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.read_or_write.md)
      * [TouchstoneReadOptions.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.__init__.md)
      * [TouchstoneReadOptions.get\_formats](../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.get_formats.md)
      * [TouchstoneReadOptions.mapping](../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.mapping.md)
      * [TouchstoneReadOptions.replace](../api_reference/_autosummary/keysight.pwdatatools.TouchstoneReadOptions.replace.md)
  + [Load Pull](../api_reference/loadpull.md)
    - [LoadPullBlock](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.md)
      * [LoadPullBlock.attrs](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.attrs.md)
      * [LoadPullBlock.dvarnames](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.dvarnames.md)
      * [LoadPullBlock.exprs](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.exprs.md)
      * [LoadPullBlock.gamma\_idxname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_idxname.md)
      * [LoadPullBlock.gamma\_ivarname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivarname.md)
      * [LoadPullBlock.idxnames](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.idxnames.md)
      * [LoadPullBlock.ivarnames](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.ivarnames.md)
      * [LoadPullBlock.name](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.name.md)
      * [LoadPullBlock.outer\_idxnames](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.outer_idxnames.md)
      * [LoadPullBlock.outer\_ivarnames](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.outer_ivarnames.md)
      * [LoadPullBlock.power\_idxname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.power_idxname.md)
      * [LoadPullBlock.power\_ivarname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.power_ivarname.md)
      * [LoadPullBlock.varnames](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.varnames.md)
      * [LoadPullBlock.z\_idxname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.z_idxname.md)
      * [LoadPullBlock.z\_ivarname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.z_ivarname.md)
      * [LoadPullBlock.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.__init__.md)
      * [LoadPullBlock.at\_gcomp](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md)
      * [LoadPullBlock.at\_power](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md)
      * [LoadPullBlock.clear](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.clear.md)
      * [LoadPullBlock.contourplot](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md)
      * [LoadPullBlock.coord\_system](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.coord_system.md)
      * [LoadPullBlock.copy](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.copy.md)
      * [LoadPullBlock.count\_observations](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.count_observations.md)
      * [LoadPullBlock.crucial\_varnames](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.crucial_varnames.md)
      * [LoadPullBlock.drop\_grid\_edges](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_grid_edges.md)
      * [LoadPullBlock.drop\_invalid\_regular](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_invalid_regular.md)
      * [LoadPullBlock.drop\_observations](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_observations.md)
      * [LoadPullBlock.drop\_vars](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_vars.md)
      * [LoadPullBlock.drop\_vars\_in\_place](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_vars_in_place.md)
      * [LoadPullBlock.eval\_expr\_as\_var](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.eval_expr_as_var.md)
      * [LoadPullBlock.fill\_nan](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.fill_nan.md)
      * [LoadPullBlock.fill\_null](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.fill_null.md)
      * [LoadPullBlock.from\_block](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.from_block.md)
      * [LoadPullBlock.from\_file](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.from_file.md)
      * [LoadPullBlock.from\_pandas\_dataframe](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.from_pandas_dataframe.md)
      * [LoadPullBlock.gamma\_idx](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_idx.md)
      * [LoadPullBlock.gamma\_ivar](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar.md)
      * [LoadPullBlock.gamma\_ivar\_scatterplot](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot.md)
      * [LoadPullBlock.gamma\_to\_z](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_to_z.md)
      * [LoadPullBlock.get](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.get.md)
      * [LoadPullBlock.get\_grid](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.get_grid.md)
      * [LoadPullBlock.get\_sweep](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.get_sweep.md)
      * [LoadPullBlock.get\_var](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.get_var.md)
      * [LoadPullBlock.get\_var\_as\_expr](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.get_var_as_expr.md)
      * [LoadPullBlock.grid\_data](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md)
      * [LoadPullBlock.has\_gamma\_sweep](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.has_gamma_sweep.md)
      * [LoadPullBlock.has\_outer\_sweep](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.has_outer_sweep.md)
      * [LoadPullBlock.has\_power\_sweep](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.has_power_sweep.md)
      * [LoadPullBlock.has\_regular\_power\_ivar](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar.md)
      * [LoadPullBlock.has\_z\_sweep](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.has_z_sweep.md)
      * [LoadPullBlock.info](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.info.md)
      * [LoadPullBlock.is\_gridded](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.is_gridded.md)
      * [LoadPullBlock.items](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.items.md)
      * [LoadPullBlock.iter\_sweep\_nodes](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.iter_sweep_nodes.md)
      * [LoadPullBlock.iter\_vars](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.iter_vars.md)
      * [LoadPullBlock.keep\_observations](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md)
      * [LoadPullBlock.keep\_vars](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_vars.md)
      * [LoadPullBlock.keep\_vars\_in\_place](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_vars_in_place.md)
      * [LoadPullBlock.keys](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.keys.md)
      * [LoadPullBlock.make\_idxs](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.make_idxs.md)
      * [LoadPullBlock.pop](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.pop.md)
      * [LoadPullBlock.popitem](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.popitem.md)
      * [LoadPullBlock.power\_idx](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.power_idx.md)
      * [LoadPullBlock.power\_ivar](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.power_ivar.md)
      * [LoadPullBlock.regularize\_power\_ivar](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md)
      * [LoadPullBlock.rename\_vars](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.rename_vars.md)
      * [LoadPullBlock.rename\_vars\_in\_place](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.rename_vars_in_place.md)
      * [LoadPullBlock.set\_data](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.set_data.md)
      * [LoadPullBlock.set\_data\_in\_place](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.set_data_in_place.md)
      * [LoadPullBlock.set\_vars](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.set_vars.md)
      * [LoadPullBlock.set\_vars\_in\_place](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.set_vars_in_place.md)
      * [LoadPullBlock.set\_zrefload\_role](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.set_zrefload_role.md)
      * [LoadPullBlock.setdefault](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.setdefault.md)
      * [LoadPullBlock.sort\_observations](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.sort_observations.md)
      * [LoadPullBlock.sort\_observations\_by](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.sort_observations_by.md)
      * [LoadPullBlock.sort\_vars](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.sort_vars.md)
      * [LoadPullBlock.to\_adscontourblock](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.to_adscontourblock.md)
      * [LoadPullBlock.to\_file](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.to_file.md)
      * [LoadPullBlock.to\_pandas\_dataframe](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.to_pandas_dataframe.md)
      * [LoadPullBlock.tricontourplot](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.tricontourplot.md)
      * [LoadPullBlock.update](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.update.md)
      * [LoadPullBlock.values](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.values.md)
      * [LoadPullBlock.z\_idx](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.z_idx.md)
      * [LoadPullBlock.z\_ivar](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.z_ivar.md)
      * [LoadPullBlock.z\_to\_gamma](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.z_to_gamma.md)
      * [LoadPullBlock.zrefload](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.zrefload.md)
    - [LoadPullSweep](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.md)
      * [LoadPullSweep.gamma\_idxname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_idxname.md)
      * [LoadPullSweep.gamma\_ivarname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_ivarname.md)
      * [LoadPullSweep.gamma\_or\_z\_idxname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_or_z_idxname.md)
      * [LoadPullSweep.gamma\_or\_z\_ivarname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_or_z_ivarname.md)
      * [LoadPullSweep.idxnames](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.idxnames.md)
      * [LoadPullSweep.idxnames\_map](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.idxnames_map.md)
      * [LoadPullSweep.ivarnames](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.ivarnames.md)
      * [LoadPullSweep.outer\_idxnames](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.outer_idxnames.md)
      * [LoadPullSweep.outer\_ivarnames](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.outer_ivarnames.md)
      * [LoadPullSweep.power\_idxname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.power_idxname.md)
      * [LoadPullSweep.power\_ivarname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.power_ivarname.md)
      * [LoadPullSweep.z\_idxname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.z_idxname.md)
      * [LoadPullSweep.z\_ivarname](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.z_ivarname.md)
      * [LoadPullSweep.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.__init__.md)
      * [LoadPullSweep.replace](../api_reference/_autosummary/keysight.pwdatatools.LoadPullSweep.replace.md)
    - [Grid](../api_reference/_autosummary/keysight.pwdatatools.Grid.md)
      * [Grid.coord\_system](../api_reference/_autosummary/keysight.pwdatatools.Grid.coord_system.md)
      * [Grid.extents](../api_reference/_autosummary/keysight.pwdatatools.Grid.extents.md)
      * [Grid.npointsx](../api_reference/_autosummary/keysight.pwdatatools.Grid.npointsx.md)
      * [Grid.npointsy](../api_reference/_autosummary/keysight.pwdatatools.Grid.npointsy.md)
      * [Grid.x\_unique](../api_reference/_autosummary/keysight.pwdatatools.Grid.x_unique.md)
      * [Grid.y\_unique](../api_reference/_autosummary/keysight.pwdatatools.Grid.y_unique.md)
      * [Grid.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Grid.__init__.md)
      * [Grid.apply](../api_reference/_autosummary/keysight.pwdatatools.Grid.apply.md)
      * [Grid.drop\_edges](../api_reference/_autosummary/keysight.pwdatatools.Grid.drop_edges.md)
      * [Grid.from\_gridded\_series](../api_reference/_autosummary/keysight.pwdatatools.Grid.from_gridded_series.md)
      * [Grid.includes\_pole](../api_reference/_autosummary/keysight.pwdatatools.Grid.includes_pole.md)
  + [Public Submodules](../api_reference/public_submodules.md)
    - [keysight.pwdatatools.calc](../api_reference/_autosummary/keysight.pwdatatools.calc.md)
      * [db\_to\_power](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.db_to_power.md)
      * [db\_to\_voltage](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.db_to_voltage.md)
      * [dbm\_to\_w](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.dbm_to_w.md)
      * [deg\_to\_rad](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.deg_to_rad.md)
      * [gamma\_to\_gamma](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.gamma_to_gamma.md)
      * [gamma\_to\_z](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.gamma_to_z.md)
      * [polar\_to\_rect](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.polar_to_rect.md)
      * [power\_to\_db](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.power_to_db.md)
      * [rad\_to\_deg](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.rad_to_deg.md)
      * [rect\_to\_polar](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.rect_to_polar.md)
      * [voltage\_to\_db](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.voltage_to_db.md)
      * [w\_to\_dbm](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.w_to_dbm.md)
      * [z\_to\_gamma](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.calc.z_to_gamma.md)
    - [keysight.pwdatatools.roles](../api_reference/_autosummary/keysight.pwdatatools.roles.md)
      * [VARNAMES\_DEFAULT](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.VARNAMES_DEFAULT.md)
      * [FrozenRolesSet](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.FrozenRolesSet.md)
      * [RolesSet](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.RolesSet.md)
      * [finalize\_role](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.finalize_role.md)
      * [is\_subrole](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.is_subrole.md)
      * [is\_valid\_role](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.roles.is_valid_role.md)
    - [keysight.pwdatatools.viz](../api_reference/_autosummary/keysight.pwdatatools.viz.md)
      * [complex\_vector\_to\_str\_series](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.complex_vector_to_str_series.md)
      * [contourplot](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.contourplot.md)
      * [float\_vector\_to\_str\_series](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.float_vector_to_str_series.md)
      * [make\_contour\_levels](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.make_contour_levels.md)
      * [smith\_chart](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.smith_chart.md)
      * [tricontourplot](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.tricontourplot.md)
      * [use\_keysight\_theme](../api_reference/_autosummary/_autosummary/keysight.pwdatatools.viz.use_keysight_theme.md)
  + [Data Types](../api_reference/datatypes.md)
    - [DataType](../api_reference/_autosummary/keysight.pwdatatools.DataType.md)
      * [DataType.name](../api_reference/_autosummary/keysight.pwdatatools.DataType.name.md)
      * [DataType.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.DataType.__init__.md)
      * [DataType.from\_name](../api_reference/_autosummary/keysight.pwdatatools.DataType.from_name.md)
      * [DataType.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.DataType.from_numpy_dtype.md)
      * [DataType.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.DataType.is_boolean.md)
      * [DataType.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.DataType.is_complex.md)
      * [DataType.is\_float](../api_reference/_autosummary/keysight.pwdatatools.DataType.is_float.md)
      * [DataType.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.DataType.is_integer.md)
      * [DataType.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.DataType.is_numeric.md)
      * [DataType.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.DataType.is_signed_integer.md)
      * [DataType.is\_string](../api_reference/_autosummary/keysight.pwdatatools.DataType.is_string.md)
      * [DataType.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.DataType.is_unsigned_integer.md)
      * [DataType.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.DataType.to_numpy_dtype.md)
    - [Boolean](../api_reference/_autosummary/keysight.pwdatatools.Boolean.md)
      * [Boolean.name](../api_reference/_autosummary/keysight.pwdatatools.Boolean.name.md)
      * [Boolean.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Boolean.__init__.md)
      * [Boolean.from\_name](../api_reference/_autosummary/keysight.pwdatatools.Boolean.from_name.md)
      * [Boolean.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Boolean.from_numpy_dtype.md)
      * [Boolean.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_boolean.md)
      * [Boolean.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_complex.md)
      * [Boolean.is\_float](../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_float.md)
      * [Boolean.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_integer.md)
      * [Boolean.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_numeric.md)
      * [Boolean.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_signed_integer.md)
      * [Boolean.is\_string](../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_string.md)
      * [Boolean.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.Boolean.is_unsigned_integer.md)
      * [Boolean.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Boolean.to_numpy_dtype.md)
    - [Complex64](../api_reference/_autosummary/keysight.pwdatatools.Complex64.md)
      * [Complex64.name](../api_reference/_autosummary/keysight.pwdatatools.Complex64.name.md)
      * [Complex64.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Complex64.__init__.md)
      * [Complex64.from\_name](../api_reference/_autosummary/keysight.pwdatatools.Complex64.from_name.md)
      * [Complex64.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Complex64.from_numpy_dtype.md)
      * [Complex64.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_boolean.md)
      * [Complex64.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_complex.md)
      * [Complex64.is\_float](../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_float.md)
      * [Complex64.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_integer.md)
      * [Complex64.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_numeric.md)
      * [Complex64.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_signed_integer.md)
      * [Complex64.is\_string](../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_string.md)
      * [Complex64.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.Complex64.is_unsigned_integer.md)
      * [Complex64.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Complex64.to_numpy_dtype.md)
    - [Complex128](../api_reference/_autosummary/keysight.pwdatatools.Complex128.md)
      * [Complex128.name](../api_reference/_autosummary/keysight.pwdatatools.Complex128.name.md)
      * [Complex128.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Complex128.__init__.md)
      * [Complex128.from\_name](../api_reference/_autosummary/keysight.pwdatatools.Complex128.from_name.md)
      * [Complex128.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Complex128.from_numpy_dtype.md)
      * [Complex128.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_boolean.md)
      * [Complex128.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_complex.md)
      * [Complex128.is\_float](../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_float.md)
      * [Complex128.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_integer.md)
      * [Complex128.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_numeric.md)
      * [Complex128.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_signed_integer.md)
      * [Complex128.is\_string](../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_string.md)
      * [Complex128.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.Complex128.is_unsigned_integer.md)
      * [Complex128.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Complex128.to_numpy_dtype.md)
    - [Float32](../api_reference/_autosummary/keysight.pwdatatools.Float32.md)
      * [Float32.name](../api_reference/_autosummary/keysight.pwdatatools.Float32.name.md)
      * [Float32.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Float32.__init__.md)
      * [Float32.from\_name](../api_reference/_autosummary/keysight.pwdatatools.Float32.from_name.md)
      * [Float32.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Float32.from_numpy_dtype.md)
      * [Float32.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.Float32.is_boolean.md)
      * [Float32.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.Float32.is_complex.md)
      * [Float32.is\_float](../api_reference/_autosummary/keysight.pwdatatools.Float32.is_float.md)
      * [Float32.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.Float32.is_integer.md)
      * [Float32.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.Float32.is_numeric.md)
      * [Float32.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.Float32.is_signed_integer.md)
      * [Float32.is\_string](../api_reference/_autosummary/keysight.pwdatatools.Float32.is_string.md)
      * [Float32.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.Float32.is_unsigned_integer.md)
      * [Float32.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Float32.to_numpy_dtype.md)
    - [Float64](../api_reference/_autosummary/keysight.pwdatatools.Float64.md)
      * [Float64.name](../api_reference/_autosummary/keysight.pwdatatools.Float64.name.md)
      * [Float64.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Float64.__init__.md)
      * [Float64.from\_name](../api_reference/_autosummary/keysight.pwdatatools.Float64.from_name.md)
      * [Float64.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Float64.from_numpy_dtype.md)
      * [Float64.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.Float64.is_boolean.md)
      * [Float64.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.Float64.is_complex.md)
      * [Float64.is\_float](../api_reference/_autosummary/keysight.pwdatatools.Float64.is_float.md)
      * [Float64.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.Float64.is_integer.md)
      * [Float64.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.Float64.is_numeric.md)
      * [Float64.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.Float64.is_signed_integer.md)
      * [Float64.is\_string](../api_reference/_autosummary/keysight.pwdatatools.Float64.is_string.md)
      * [Float64.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.Float64.is_unsigned_integer.md)
      * [Float64.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Float64.to_numpy_dtype.md)
    - [Int8](../api_reference/_autosummary/keysight.pwdatatools.Int8.md)
      * [Int8.name](../api_reference/_autosummary/keysight.pwdatatools.Int8.name.md)
      * [Int8.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Int8.__init__.md)
      * [Int8.from\_name](../api_reference/_autosummary/keysight.pwdatatools.Int8.from_name.md)
      * [Int8.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Int8.from_numpy_dtype.md)
      * [Int8.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.Int8.is_boolean.md)
      * [Int8.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.Int8.is_complex.md)
      * [Int8.is\_float](../api_reference/_autosummary/keysight.pwdatatools.Int8.is_float.md)
      * [Int8.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int8.is_integer.md)
      * [Int8.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.Int8.is_numeric.md)
      * [Int8.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int8.is_signed_integer.md)
      * [Int8.is\_string](../api_reference/_autosummary/keysight.pwdatatools.Int8.is_string.md)
      * [Int8.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int8.is_unsigned_integer.md)
      * [Int8.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Int8.to_numpy_dtype.md)
    - [Int16](../api_reference/_autosummary/keysight.pwdatatools.Int16.md)
      * [Int16.name](../api_reference/_autosummary/keysight.pwdatatools.Int16.name.md)
      * [Int16.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Int16.__init__.md)
      * [Int16.from\_name](../api_reference/_autosummary/keysight.pwdatatools.Int16.from_name.md)
      * [Int16.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Int16.from_numpy_dtype.md)
      * [Int16.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.Int16.is_boolean.md)
      * [Int16.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.Int16.is_complex.md)
      * [Int16.is\_float](../api_reference/_autosummary/keysight.pwdatatools.Int16.is_float.md)
      * [Int16.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int16.is_integer.md)
      * [Int16.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.Int16.is_numeric.md)
      * [Int16.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int16.is_signed_integer.md)
      * [Int16.is\_string](../api_reference/_autosummary/keysight.pwdatatools.Int16.is_string.md)
      * [Int16.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int16.is_unsigned_integer.md)
      * [Int16.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Int16.to_numpy_dtype.md)
    - [Int32](../api_reference/_autosummary/keysight.pwdatatools.Int32.md)
      * [Int32.name](../api_reference/_autosummary/keysight.pwdatatools.Int32.name.md)
      * [Int32.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Int32.__init__.md)
      * [Int32.from\_name](../api_reference/_autosummary/keysight.pwdatatools.Int32.from_name.md)
      * [Int32.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Int32.from_numpy_dtype.md)
      * [Int32.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.Int32.is_boolean.md)
      * [Int32.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.Int32.is_complex.md)
      * [Int32.is\_float](../api_reference/_autosummary/keysight.pwdatatools.Int32.is_float.md)
      * [Int32.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int32.is_integer.md)
      * [Int32.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.Int32.is_numeric.md)
      * [Int32.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int32.is_signed_integer.md)
      * [Int32.is\_string](../api_reference/_autosummary/keysight.pwdatatools.Int32.is_string.md)
      * [Int32.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int32.is_unsigned_integer.md)
      * [Int32.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Int32.to_numpy_dtype.md)
    - [Int64](../api_reference/_autosummary/keysight.pwdatatools.Int64.md)
      * [Int64.name](../api_reference/_autosummary/keysight.pwdatatools.Int64.name.md)
      * [Int64.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.Int64.__init__.md)
      * [Int64.from\_name](../api_reference/_autosummary/keysight.pwdatatools.Int64.from_name.md)
      * [Int64.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Int64.from_numpy_dtype.md)
      * [Int64.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.Int64.is_boolean.md)
      * [Int64.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.Int64.is_complex.md)
      * [Int64.is\_float](../api_reference/_autosummary/keysight.pwdatatools.Int64.is_float.md)
      * [Int64.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int64.is_integer.md)
      * [Int64.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.Int64.is_numeric.md)
      * [Int64.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int64.is_signed_integer.md)
      * [Int64.is\_string](../api_reference/_autosummary/keysight.pwdatatools.Int64.is_string.md)
      * [Int64.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.Int64.is_unsigned_integer.md)
      * [Int64.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.Int64.to_numpy_dtype.md)
    - [String](../api_reference/_autosummary/keysight.pwdatatools.String.md)
      * [String.name](../api_reference/_autosummary/keysight.pwdatatools.String.name.md)
      * [String.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.String.__init__.md)
      * [String.from\_name](../api_reference/_autosummary/keysight.pwdatatools.String.from_name.md)
      * [String.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.String.from_numpy_dtype.md)
      * [String.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.String.is_boolean.md)
      * [String.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.String.is_complex.md)
      * [String.is\_float](../api_reference/_autosummary/keysight.pwdatatools.String.is_float.md)
      * [String.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.String.is_integer.md)
      * [String.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.String.is_numeric.md)
      * [String.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.String.is_signed_integer.md)
      * [String.is\_string](../api_reference/_autosummary/keysight.pwdatatools.String.is_string.md)
      * [String.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.String.is_unsigned_integer.md)
      * [String.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.String.to_numpy_dtype.md)
    - [UInt8](../api_reference/_autosummary/keysight.pwdatatools.UInt8.md)
      * [UInt8.name](../api_reference/_autosummary/keysight.pwdatatools.UInt8.name.md)
      * [UInt8.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.UInt8.__init__.md)
      * [UInt8.from\_name](../api_reference/_autosummary/keysight.pwdatatools.UInt8.from_name.md)
      * [UInt8.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.UInt8.from_numpy_dtype.md)
      * [UInt8.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_boolean.md)
      * [UInt8.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_complex.md)
      * [UInt8.is\_float](../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_float.md)
      * [UInt8.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_integer.md)
      * [UInt8.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_numeric.md)
      * [UInt8.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_signed_integer.md)
      * [UInt8.is\_string](../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_string.md)
      * [UInt8.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt8.is_unsigned_integer.md)
      * [UInt8.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.UInt8.to_numpy_dtype.md)
    - [UInt16](../api_reference/_autosummary/keysight.pwdatatools.UInt16.md)
      * [UInt16.name](../api_reference/_autosummary/keysight.pwdatatools.UInt16.name.md)
      * [UInt16.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.UInt16.__init__.md)
      * [UInt16.from\_name](../api_reference/_autosummary/keysight.pwdatatools.UInt16.from_name.md)
      * [UInt16.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.UInt16.from_numpy_dtype.md)
      * [UInt16.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_boolean.md)
      * [UInt16.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_complex.md)
      * [UInt16.is\_float](../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_float.md)
      * [UInt16.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_integer.md)
      * [UInt16.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_numeric.md)
      * [UInt16.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_signed_integer.md)
      * [UInt16.is\_string](../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_string.md)
      * [UInt16.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt16.is_unsigned_integer.md)
      * [UInt16.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.UInt16.to_numpy_dtype.md)
    - [UInt32](../api_reference/_autosummary/keysight.pwdatatools.UInt32.md)
      * [UInt32.name](../api_reference/_autosummary/keysight.pwdatatools.UInt32.name.md)
      * [UInt32.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.UInt32.__init__.md)
      * [UInt32.from\_name](../api_reference/_autosummary/keysight.pwdatatools.UInt32.from_name.md)
      * [UInt32.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.UInt32.from_numpy_dtype.md)
      * [UInt32.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_boolean.md)
      * [UInt32.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_complex.md)
      * [UInt32.is\_float](../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_float.md)
      * [UInt32.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_integer.md)
      * [UInt32.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_numeric.md)
      * [UInt32.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_signed_integer.md)
      * [UInt32.is\_string](../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_string.md)
      * [UInt32.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt32.is_unsigned_integer.md)
      * [UInt32.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.UInt32.to_numpy_dtype.md)
    - [UInt64](../api_reference/_autosummary/keysight.pwdatatools.UInt64.md)
      * [UInt64.name](../api_reference/_autosummary/keysight.pwdatatools.UInt64.name.md)
      * [UInt64.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.UInt64.__init__.md)
      * [UInt64.from\_name](../api_reference/_autosummary/keysight.pwdatatools.UInt64.from_name.md)
      * [UInt64.from\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.UInt64.from_numpy_dtype.md)
      * [UInt64.is\_boolean](../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_boolean.md)
      * [UInt64.is\_complex](../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_complex.md)
      * [UInt64.is\_float](../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_float.md)
      * [UInt64.is\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_integer.md)
      * [UInt64.is\_numeric](../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_numeric.md)
      * [UInt64.is\_signed\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_signed_integer.md)
      * [UInt64.is\_string](../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_string.md)
      * [UInt64.is\_unsigned\_integer](../api_reference/_autosummary/keysight.pwdatatools.UInt64.is_unsigned_integer.md)
      * [UInt64.to\_numpy\_dtype](../api_reference/_autosummary/keysight.pwdatatools.UInt64.to_numpy_dtype.md)
    - [FillValues](../api_reference/_autosummary/keysight.pwdatatools.FillValues.md)
      * [FillValues.boolean](../api_reference/_autosummary/keysight.pwdatatools.FillValues.boolean.md)
      * [FillValues.complexfloating](../api_reference/_autosummary/keysight.pwdatatools.FillValues.complexfloating.md)
      * [FillValues.floating](../api_reference/_autosummary/keysight.pwdatatools.FillValues.floating.md)
      * [FillValues.integer](../api_reference/_autosummary/keysight.pwdatatools.FillValues.integer.md)
      * [FillValues.string](../api_reference/_autosummary/keysight.pwdatatools.FillValues.string.md)
      * [FillValues.\_\_init\_\_](../api_reference/_autosummary/keysight.pwdatatools.FillValues.__init__.md)
      * [FillValues.get\_fill\_value](../api_reference/_autosummary/keysight.pwdatatools.FillValues.get_fill_value.md)
      * [FillValues.replace](../api_reference/_autosummary/keysight.pwdatatools.FillValues.replace.md)
  + [Concatenation](../api_reference/concatenation.md)
    - [concatenate\_blocks](../api_reference/_autosummary/keysight.pwdatatools.concatenate_blocks.md)
    - [concatenate\_loadpullblocks](../api_reference/_autosummary/keysight.pwdatatools.concatenate_loadpullblocks.md)
    - [concatenate\_vars](../api_reference/_autosummary/keysight.pwdatatools.concatenate_vars.md)
  + [Global Options](../api_reference/global_options.md)
* [Changelog](../changelog.md)

# Use the Block Class[](#use-the-block-class "Link to this heading")

The [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") is one of the most important and fundamental classes in the `keysight.pwdatatools` library. It primarily behaves as a dict-like object that maps variable names to [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") instances. Each Var in a Block holds the data and metadata for a single dataset variable. The next sections walk through some simple examples that illustrate how to use the [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") class.

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

For more information on the [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class, see [Use the Var Class](use_var_class.md#use-var-class).

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

If you want more control over how a pandas DataFrame is cast as data in a Block, use the [`Block.from_pandas_dataframe()`](../api_reference/_autosummary/keysight.pwdatatools.Block.from_pandas_dataframe.md#keysight.pwdatatools.Block.from_pandas_dataframe "keysight.pwdatatools.Block.from_pandas_dataframe") method instead.

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

You can also instantiate a Block from a file. The file can be any supported datafile format. Usually, the file extension determines the file format. For example, if the file extension is `.pwdt`, then the file is assumed to be a native pwdatatools file. If the file extension is `.ds`, then the file is assumed to be an ADS dataset. The Block class has a [`Block.from_file()`](../api_reference/_autosummary/keysight.pwdatatools.Block.from_file.md#keysight.pwdatatools.Block.from_file "keysight.pwdatatools.Block.from_file") method that reads the file and returns a Block. The following code reads an ADS dataset and returns a Block. The Block is assigned to the variable `block_from_file`.

```
>>> block_from_file = pwdt.Block.from_file('/data_folder/amplifier_sim.ds')
```

However, the above will not work if the ADS dataset cannot be represented by a single Block. ADS datasets (as well as other datafile formats) are hierarchical in nature and thus may require multiple Blocks to represent the data. In this case, it is better to use the free function `read_file_as_group()`. This function always returns a [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") containing one or more Blocks, and it works for hierarchical datasets.

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

If a Block has too many variable names to fit on the variables line, that line will be truncated. If we would like to see all variable names, we can use the [`Block.varnames`](../api_reference/_autosummary/keysight.pwdatatools.Block.varnames.md#keysight.pwdatatools.Block.varnames "keysight.pwdatatools.Block.varnames") property to get a tuple of all variable names. The following code returns the variable names of the `block` we created earlier. In this case, the line did not need to be truncated.

```
>>> block.varnames
('bias', 'freq', 'Zin', 'passed')
```

Blocks store each variable as an instance of [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var"), which stores the data and metadata for that variable. Variables can be accessed using the `[]` operator on the Block. The following code gets the variable `bias` from the Block.

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

There are other methods for retrieving variables from a Block. See [`Block.get()`](../api_reference/_autosummary/keysight.pwdatatools.Block.get.md#keysight.pwdatatools.Block.get "keysight.pwdatatools.Block.get"), [`Block.get_var()`](../api_reference/_autosummary/keysight.pwdatatools.Block.get_var.md#keysight.pwdatatools.Block.get_var "keysight.pwdatatools.Block.get_var"), [`Block.iter_vars()`](../api_reference/_autosummary/keysight.pwdatatools.Block.iter_vars.md#keysight.pwdatatools.Block.iter_vars "keysight.pwdatatools.Block.iter_vars"), [`Block.pop()`](../api_reference/_autosummary/keysight.pwdatatools.Block.pop.md#keysight.pwdatatools.Block.pop "keysight.pwdatatools.Block.pop"), and [`Block.values()`](../api_reference/_autosummary/keysight.pwdatatools.Block.values.md#keysight.pwdatatools.Block.values "keysight.pwdatatools.Block.values") for more information.

## Mutating variables in a Block[](#mutating-variables-in-a-block "Link to this heading")

Block objects are mutable, meaning they can change state after they are created. This means we can add or remove variables, or change the Block’s metadata. We can also change the data or metadata of any variable in the Block, because the [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class is also mutable. The following sections show how to do this.

We can change the data for one or more variables by using the [`Block.set_data_in_place()`](../api_reference/_autosummary/keysight.pwdatatools.Block.set_data_in_place.md#keysight.pwdatatools.Block.set_data_in_place "keysight.pwdatatools.Block.set_data_in_place") method. The following code sets the data for the `bias` variable.

```
>>> block.set_data_in_place({'bias': [4, 4, 4, 5, 5, 5]})
```

We can also rename a variable in a Block. The following code renames the `bias` variable to `bias2`. There are two different approaches shown below. The first approach is to directly change the name of the variable by setting the [`Var.name`](../api_reference/_autosummary/keysight.pwdatatools.Var.name.md#keysight.pwdatatools.Var.name "keysight.pwdatatools.Var.name") property.

```
>>> block['bias'].name = 'bias2'
```

The next line of code achieves the same result by using the [`Block.rename_vars_in_place()`](../api_reference/_autosummary/keysight.pwdatatools.Block.rename_vars_in_place.md#keysight.pwdatatools.Block.rename_vars_in_place "keysight.pwdatatools.Block.rename_vars_in_place") method.

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

There are other methods for adding Vars or data to a Block. See [`Block.set_data_in_place()`](../api_reference/_autosummary/keysight.pwdatatools.Block.set_data_in_place.md#keysight.pwdatatools.Block.set_data_in_place "keysight.pwdatatools.Block.set_data_in_place") and [`Block.set_vars_in_place()`](../api_reference/_autosummary/keysight.pwdatatools.Block.set_vars_in_place.md#keysight.pwdatatools.Block.set_vars_in_place "keysight.pwdatatools.Block.set_vars_in_place") for more information.

## Observations in a Block[](#observations-in-a-block "Link to this heading")

### What are they?[](#what-are-they "Link to this heading")

Each variable we’ve added to the Block has a length of 6. All variables in a Block must have equal length along axis 0 (the first dimension). So far, all of our variables are 1D, so their overall sizes are also 6. But in the case of multi-dimensional variables, we must make sure the length along axis 0 is also 6 if we want to add it to this Block. The length of the variables along axis 0 in any particular Block can be accessed via the [`Block.count_observations()`](../api_reference/_autosummary/keysight.pwdatatools.Block.count_observations.md#keysight.pwdatatools.Block.count_observations "keysight.pwdatatools.Block.count_observations") method.

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

A very common operation is filtering observations in a Block. This can be done using the [`Block.drop_observations()`](../api_reference/_autosummary/keysight.pwdatatools.Block.drop_observations.md#keysight.pwdatatools.Block.drop_observations "keysight.pwdatatools.Block.drop_observations") and [`Block.keep_observations()`](../api_reference/_autosummary/keysight.pwdatatools.Block.keep_observations.md#keysight.pwdatatools.Block.keep_observations "keysight.pwdatatools.Block.keep_observations") methods. Both methods take boolean array-like input which is used to select observations to keep or drop. The boolean array-like must be 1D and have the same length as the Block’s observations count. The following code drops all observations in the Block except for the first 3 observations.

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

For more information on filtering observations, see [`Block.drop_observations()`](../api_reference/_autosummary/keysight.pwdatatools.Block.drop_observations.md#keysight.pwdatatools.Block.drop_observations "keysight.pwdatatools.Block.drop_observations") and [`Block.keep_observations()`](../api_reference/_autosummary/keysight.pwdatatools.Block.keep_observations.md#keysight.pwdatatools.Block.keep_observations "keysight.pwdatatools.Block.keep_observations").

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

Set the [`Block.ivarnames`](../api_reference/_autosummary/keysight.pwdatatools.Block.ivarnames.md#keysight.pwdatatools.Block.ivarnames "keysight.pwdatatools.Block.ivarnames") attribute as an iterable of string variable names (tuple, list, etc.). The ordering of the ivarnames is important. The outermost ivar should be first and the innermost ivar should be last. If there are other ivars, they should be listed in order of their “nesting” a.k.a. “level”. By assigning `bias2` and `freq` as `ivarnames`, all the rest of the variables are automatically assigned as dvars, and will thus appear in the [`Block.dvarnames`](../api_reference/_autosummary/keysight.pwdatatools.Block.dvarnames.md#keysight.pwdatatools.Block.dvarnames "keysight.pwdatatools.Block.dvarnames") attribute. Unlike [`Block.ivarnames`](../api_reference/_autosummary/keysight.pwdatatools.Block.ivarnames.md#keysight.pwdatatools.Block.ivarnames "keysight.pwdatatools.Block.ivarnames"), the ordering of [`Block.dvarnames`](../api_reference/_autosummary/keysight.pwdatatools.Block.dvarnames.md#keysight.pwdatatools.Block.dvarnames "keysight.pwdatatools.Block.dvarnames") is not typically important. However, the [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") class makes every effort to maintain the original dvar ordering during all operations.

```
>>> block.ivarnames = ('bias2', 'freq')
>>> print(f'ivarnames = {block.ivarnames}\ndvarnames = {block.dvarnames}')
ivarnames = ('bias2', 'freq')
dvarnames = ('Zin', 'passed', 'new_var', 'PortZ')
```

Important

The [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") class has another property [`Block.idxnames`](../api_reference/_autosummary/keysight.pwdatatools.Block.idxnames.md#keysight.pwdatatools.Block.idxnames "keysight.pwdatatools.Block.idxnames") that defines variables that are meant to be used for indexing along the Block’s observations (along axis 0 of each Var). We will not set the [`Block.idxnames`](../api_reference/_autosummary/keysight.pwdatatools.Block.idxnames.md#keysight.pwdatatools.Block.idxnames "keysight.pwdatatools.Block.idxnames") property in this example, but the load pull examples in [Examples](../examples/index.md#examples) illustrate its use. The [`LoadPullBlock`](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") class uses the [`Block.idxnames`](../api_reference/_autosummary/keysight.pwdatatools.Block.idxnames.md#keysight.pwdatatools.Block.idxnames "keysight.pwdatatools.Block.idxnames") property and index variables extensively. In [`LoadPullBlock`](../api_reference/_autosummary/keysight.pwdatatools.LoadPullBlock.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock"), the idxs are integer indexes that correspond to the ivars.

### Add arbitrary attributes[](#add-arbitrary-attributes "Link to this heading")

Arbitrary metadata may be stored in the [`Block.attrs`](../api_reference/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs") property. The [`Block.attrs`](../api_reference/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs") property stores an instance of [`AttrsDict`](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.md#keysight.pwdatatools.AttrsDict "keysight.pwdatatools.AttrsDict"), which behaves like a type-restricted dict. It’s up to you what kind of arbitrary attributes you want to store. The only requirement is that they must be HDF5-serializable. This means that the attributes must be one of the following types: float, complex, int, str, bool, None, list, dict, numpy.ndarray, or a combination of these types. The attributes may be nested to any depth (nested lists, dicts, etc. are supported). Here are just a few examples of useful information that may be stored in [`Block.attrs`](../api_reference/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs"):

* constant values; for example, temperature or reference impedance
* simulation settings or measurement info; for example, calibration info, name of the engineeer that made the measurement, the date the data was collected, etc.
* comments

Saving constant values as metadata instead of as variables helps save memory because we avoid repeating constant values over every observation. Constants may be one of the following types: float, complex, int, str, bool, and None. Below, we add some constants to the [`Block.attrs`](../api_reference/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs") property using the `[]` operator, just like a regular dict.

```
>>> block.attrs['sample'] = 'batch1'
>>> block.attrs['temperature'] = 150
>>> block.attrs['Zref'] = 3+4j
```

Comments can be also stored in [`Block.attrs`](../api_reference/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs"). They can be stored as a list of strings, or a numpy.ndarray of strings, or as a single string with optional newline characters. There is no special reserved key for comments, so the using the key `'comments'` here is completely arbitrary.

```
>>> block.attrs['comments'] = [
...    'This was collected by Mike for customer A.',
...    'This was an outlier.',
...    'The product was delivered on June 15th.'
... ]
```

Arbitrary attributes to be associated with any particular variable may be stored in each [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") object. In contrast, the attributes stored in [`Block.attrs`](../api_reference/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs") are associated with the entire [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"). Here we add a few attributes to the `bias` variable.

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

It’s not covered here, but there are other types of metadata that can be stored in the [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") object. Examples are dims, role, and unit. See [Use the Var Class](use_var_class.md#use-var-class) for more information.

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

Another option is to use the [`Block.info()`](../api_reference/_autosummary/keysight.pwdatatools.Block.info.md#keysight.pwdatatools.Block.info "keysight.pwdatatools.Block.info") method, which returns a DataFrame containing information about the variables.

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

The `pandas` library is a very popular library for data analysis. The main data structure in pandas is the DataFrame. The Block class has a [`Block.to_pandas_dataframe()`](../api_reference/_autosummary/keysight.pwdatatools.Block.to_pandas_dataframe.md#keysight.pwdatatools.Block.to_pandas_dataframe "keysight.pwdatatools.Block.to_pandas_dataframe") method that returns a pandas DataFrame containing all the data in the Block. This allows you to take full advantage of all the pandas.DataFrame methods for data analysis and manipulation.

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

Because the [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") and [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") classes implement the necessary interfaces, they can be directly used in many plotting libraries. For example, the `matplotlib` and `seaborn` libraries can plot data from Blocks and Vars. The following code plots the `new_var` variable from our Block.

```
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> ax = sns.lineplot(data=block, x='freq', y='new_var', hue='bias2', palette='tab10')
>>> ax.set_title('Simple Demo of Plotting Data from a Block')
>>> plt.show()
```

[![Simple Demo of Plotting Data from a Block](../_images/block_plot.png)](../_images/block_plot.png)

## Write a Block to a file[](#write-a-block-to-a-file "Link to this heading")

The Block class has a [`Block.to_file()`](../api_reference/_autosummary/keysight.pwdatatools.Block.to_file.md#keysight.pwdatatools.Block.to_file "keysight.pwdatatools.Block.to_file") method that writes the Block to any supported datafile format. Usually, the file extension determines the file format.

```
>>> block.to_file('/data_folder/myblock.ds')  # write to an ADS dataset
>>> block.to_file('/data_folder/myblock.pwdt') # write to a native pwdatatools file
```

Some datafile formats do a better job at storing metadata than others. For example, the native pwdt format stores all of the Var and Block metadata. However, the ADS dataset format does not store much other than the variable names, the ivarnames, and the data.

We can also combine our Block with other Blocks before writing to a file. This only works for datafile formats that support hierarchy such as ADS datasets, pwdt HDF5 files, and generic MDIFs (and others). The following code creates another simple Block and then groups our `block` together with this new Block called `block2`. The resulting [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") is then written to file.

```
>>> block2 = pwdt.Block({'x': np.array([1, 2, 3, 4, 5, 6])}, name='foo') # instantiate with a Block name
>>> group = pwdt.Group([block, block2])
>>> group.to_file('/data_folder/combined_results.ds')  # write both Blocks to a single ADS dataset
```

See also

For more information on writing datafiles, see [Write a File](write_a_file.md#write-a-file).

On this page

[Previous

Use the Var Class](use_var_class.md)
[Next

Use the Group Class](use_group_class.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top