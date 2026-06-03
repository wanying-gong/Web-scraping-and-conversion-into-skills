<!-- 来源: howto\use_var_class.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-pwdatatools](../index.md)
* [How To](index.md)
* Use the Var Class

0.12.1

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/howto/use_var_class.rst.txt)

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
  + Use the Var Class
  + [Use the Block Class](use_block_class.md)
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

# Use the Var Class[](#use-the-var-class "Link to this heading")

The [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class is fundamental to storing and manipulating data in the `keysight.pwdatatools` library. It holds data and metadata for a single variable in a [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"). This section walks through how to use the [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class.

## Basics[](#basics "Link to this heading")

At a minimum, creating a [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") requires data, which can be any array-like object (numpy ndarray, Python list, pandas Series, etc.). Usually, a [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") will also be initialized with a string name. But, if no name is provided, the Var’s name is set to an empty string. Here, we initialize a Var with data as a Python list and the name `'freq'`. The data argument may be positional, but all other arguments must be keyword arguments.

```
>>> from keysight.pwdatatools import Var
>>> freq = Var([1e9, 2e9, 3e9], name='freq')
```

If we view the output of `Var.__repr__()`, we can see several other attributes that have been initialized as empty or None: [`Var.dims`](../api_reference/_autosummary/keysight.pwdatatools.Var.dims.md#keysight.pwdatatools.Var.dims "keysight.pwdatatools.Var.dims"), [`Var.role`](../api_reference/_autosummary/keysight.pwdatatools.Var.role.md#keysight.pwdatatools.Var.role "keysight.pwdatatools.Var.role"), [`Var.unit`](../api_reference/_autosummary/keysight.pwdatatools.Var.unit.md#keysight.pwdatatools.Var.unit "keysight.pwdatatools.Var.unit"), and [`Var.attrs`](../api_reference/_autosummary/keysight.pwdatatools.Var.attrs.md#keysight.pwdatatools.Var.attrs "keysight.pwdatatools.Var.attrs").

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

As an alternative to invoking the `Var.__repr__()` method, we can use the [`Var.info()`](../api_reference/_autosummary/keysight.pwdatatools.Var.info.md#keysight.pwdatatools.Var.info "keysight.pwdatatools.Var.info") method to get a more detailed summary of the Var. This method returns a `pandas.Series`.

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

All of the Var’s metadata that we see in the repr have dedicated attributes: [`Var.name`](../api_reference/_autosummary/keysight.pwdatatools.Var.name.md#keysight.pwdatatools.Var.name "keysight.pwdatatools.Var.name"), [`Var.dims`](../api_reference/_autosummary/keysight.pwdatatools.Var.dims.md#keysight.pwdatatools.Var.dims "keysight.pwdatatools.Var.dims"), [`Var.role`](../api_reference/_autosummary/keysight.pwdatatools.Var.role.md#keysight.pwdatatools.Var.role "keysight.pwdatatools.Var.role"), and [`Var.unit`](../api_reference/_autosummary/keysight.pwdatatools.Var.unit.md#keysight.pwdatatools.Var.unit "keysight.pwdatatools.Var.unit"), [`Var.attrs`](../api_reference/_autosummary/keysight.pwdatatools.Var.attrs.md#keysight.pwdatatools.Var.attrs "keysight.pwdatatools.Var.attrs"). Let’s demonstrate how to get these attributes. For now, let’s ignore the [`Var.dims`](../api_reference/_autosummary/keysight.pwdatatools.Var.dims.md#keysight.pwdatatools.Var.dims "keysight.pwdatatools.Var.dims") attribute because it only applies to multi-dimensional Vars. We will explore that attribute later.

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

For more information on variable roles, see [Use Roles](use_roles.md#how-to-use-roles).

We can optionally include any of these additional attributes during instantiation of a new [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var"), instead of setting their values after instantiation. To illustrate, let’s create a new Var with a role, unit, and a couple arbitrary attributes. This time, we use a `numpy.ndarray` as the data input (instead of a Python list).

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

The [`Var.dtype`](../api_reference/_autosummary/keysight.pwdatatools.Var.dtype.md#keysight.pwdatatools.Var.dtype "keysight.pwdatatools.Var.dtype"), [`Var.ndim`](../api_reference/_autosummary/keysight.pwdatatools.Var.ndim.md#keysight.pwdatatools.Var.ndim "keysight.pwdatatools.Var.ndim"), [`Var.shape`](../api_reference/_autosummary/keysight.pwdatatools.Var.shape.md#keysight.pwdatatools.Var.shape "keysight.pwdatatools.Var.shape"), and [`Var.size`](../api_reference/_autosummary/keysight.pwdatatools.Var.size.md#keysight.pwdatatools.Var.size "keysight.pwdatatools.Var.size") attributes are read-only attributes that provide information about the Var’s data.

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

To illustrate how to work with multi-dimensional Vars, let’s create a new [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") to represent S-parameters. 2 port S-parameter data is a 2x2 matrix with one extra dimension for frequency. Let’s assume we have 3 frequency points.

```
>>> import numpy as np
>>> s_data = (np.random.random(12) + 1j * np.random.random(12)).reshape(3, 2, 2)
>>> s = Var(s_data, name='S', role='s_parameters')
>>> s
Var(
    <Complex128 data with shape (3, 2, 2)>,
    name='S',
    dims=<empty Dims>,
    role='s_parameters',
    unit=None,
    attrs={},
)
```

This Var has 3 dimensions called axis 0, axis 1, and axis 2. Here is more info about each axis:

> * Axis 0 is called the “shared” dimension in pwdatatools and represents the 3 observations of the S-parameters over frequency.
> * Axis 1 is called the “i” dimension in pwdatatools and represents the “output” port of the S-parameters. It has a size of 2.
> * Axis 2 is called the “j” dimension in pwdatatools and represents the “input” port of the S-parameters. It also has a size of 2.

Important

A Var’s first dimension, which corresponds to axis 0 of the data, is known as the “shared dimension” because it is the common dimension shared by all Vars in a [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"). In the case of our S-parameters variable, there are 3 observations (because there are 3 frequency points), so the length of axis 0 must be 3. Therefore, the final shape of a 2 port S-parameter array with 3 frequency points must be (3, 2, 2).

The [`Var.dims`](../api_reference/_autosummary/keysight.pwdatatools.Var.dims.md#keysight.pwdatatools.Var.dims "keysight.pwdatatools.Var.dims") attribute can be used to store metadata (as an instance of [`Dims`](../api_reference/_autosummary/keysight.pwdatatools.Dims.md#keysight.pwdatatools.Dims "keysight.pwdatatools.Dims")) associated with the higher dimensions of a multi-dimensional Var. Let’s create a new instance of [`Dims`](../api_reference/_autosummary/keysight.pwdatatools.Dims.md#keysight.pwdatatools.Dims "keysight.pwdatatools.Dims") and assign it to the [`Var.dims`](../api_reference/_autosummary/keysight.pwdatatools.Var.dims.md#keysight.pwdatatools.Var.dims "keysight.pwdatatools.Var.dims") attribute of our S-parameters Var. For this example, we will include strings that act as port names.

```
>>> from keysight.pwdatatools import Dims
>>> dims = Dims(ndim=3, i_names=['P1', 'P2'], j_names=['P1', 'P2'])
>>> s.dims = dims
>>> s
Var(
    <Complex128 data with shape (3, 2, 2)>,
    name='S',
    dims=<Dims with names>,
    role='s_parameters',
    unit=None,
    attrs={},
)
```

Later, in the [indexing section](#var-indexing-select-method), we will see how to use the [`Var.select()`](../api_reference/_autosummary/keysight.pwdatatools.Var.select.md#keysight.pwdatatools.Var.select "keysight.pwdatatools.Var.select") method to index multi-dimensional Vars based on dimension names and labels.

## NumPy functions[](#numpy-functions "Link to this heading")

The [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class implements a standard array interface that supports many numpy ufuncs (universal functions). This means we can use numpy ufuncs directly on a Var. The ufuncs always return a `numpy.ndarray`, not a [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var").

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

The [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class supports the same operators as numpy ndarrays. Just like with numpy ufuncs, using operators with one or more Vars always returns a numpy ndarray instead of a Var.

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

The [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class implements a standard array interface that supports many matplotlib and seaborn plotting functions.

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

We saved the topic of indexing for last since it is the most involved. The [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class supports several different options: [numpy-style indexing](#var-indexing-numpy-style), [one-based integer indexing and parentheses syntax](#var-indexing-one-based), and the [Var select method](#var-indexing-select-method). Also, if you prefer, you can can convert a Var to a `pandas.Series` or `pandas.DataFrame` and use pandas indexing directly. When you are done, you can convert the pandas object back to a Var. This pandas-based approach is covered last, in the [pandas indexing section](#pandas-indexing).

Let’s explore each of these in detail.

### NumPy style[](#numpy-style "Link to this heading")

The [`Var`](../api_reference/_autosummary/keysight.pwdatatools.Var.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") class supports all the same indexing operations as numpy. All indexing operations return a new Var with new data (and possibly new dims). All other metadata, including the new Var’s name, is copied from the old Var. Let’s create a new 2D Var to illustrate.

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
>>> s = Var(s_data, name='S', role='s_parameters')
>>> s
Var(
    <Complex128 data with shape (3, 2, 2)>,
    name='S',
    dims=<empty Dims>,
    role='s_parameters',
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
    role='s_parameters',
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
    role='s_parameters',
    unit=None,
    attrs={},
)
```

### The select method[](#the-select-method "Link to this heading")

The [`Var.select()`](../api_reference/_autosummary/keysight.pwdatatools.Var.select.md#keysight.pwdatatools.Var.select "keysight.pwdatatools.Var.select") method is a powerful way to index into multi-dimensional Vars. It allows indexing based upon arbitrary strings and numbers, rather than 0-based or 1-based integer positions. Let’s create a new Var to illustrate. We also need to create an instance of [`Dims`](../api_reference/_autosummary/keysight.pwdatatools.Dims.md#keysight.pwdatatools.Dims "keysight.pwdatatools.Dims") to store metadata about the higher dimensions.

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

Let’s use the [`Var.select()`](../api_reference/_autosummary/keysight.pwdatatools.Var.select.md#keysight.pwdatatools.Var.select "keysight.pwdatatools.Var.select") method to get S(2,1) from the S-parameters variable. Note the new shape of the data and the new dims.

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

Now, let’s use the [`Var.select()`](../api_reference/_autosummary/keysight.pwdatatools.Var.select.md#keysight.pwdatatools.Var.select "keysight.pwdatatools.Var.select") method to get all the S-parameters associated with ports 3 and 4. Just for illustration purposes, this time we use a dict instead of keyword arguments.

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

On this page

[Previous

Translate a File](translate_a_file.md)
[Next

Use the Block Class](use_block_class.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top