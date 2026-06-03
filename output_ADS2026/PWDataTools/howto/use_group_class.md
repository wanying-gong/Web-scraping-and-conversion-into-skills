<!-- 来源: howto\use_group_class.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-pwdatatools](../index.md)
* [How To](index.md)
* Use the Group Class

0.12.1

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/howto/use_group_class.rst.txt)

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
  + [Use the Block Class](use_block_class.md)
  + Use the Group Class
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

# Use the Group Class[](#use-the-group-class "Link to this heading")

A [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") is essentially a collection of child objects. These children are also referred to as members. A Group’s members can include instances of [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"), as well as other instances of [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group"). Thus, the [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") class is the key enabler to representing hierarchical datasets in the `keysight.pwdatatools` library. This section walks through how to use the [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") class. It builds off the previous section, [Use the Block Class](use_block_class.md#use-block-class).

See also

If you aren’t sure what hierarchical datasets are, or how they relate to Groups and Blocks, see [Universal Data Structures](../index.md#data-structs-section).

## Create a Group[](#create-a-group "Link to this heading")

There are two main ways to create a [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") instance. The first is to instantiate a Group directly, using the [`Group.__init__()`](../api_reference/_autosummary/keysight.pwdatatools.Group.__init__.md#keysight.pwdatatools.Group.__init__ "keysight.pwdatatools.Group.__init__") method. The second is to read a file into a Group using the [`Group.from_file()`](../api_reference/_autosummary/keysight.pwdatatools.Group.from_file.md#keysight.pwdatatools.Group.from_file "keysight.pwdatatools.Group.from_file") method. We’ll cover both of these instantiation methods.

### Direct instantiation[](#direct-instantiation "Link to this heading")

Let’s instantiate a [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") with a list of members, a name, and an arbitrary attribute (the date). Below, we first create two simple [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") instances, then we instantiate the Group.

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

Our dict with the date was converted to an [`AttrsDict`](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.md#keysight.pwdatatools.AttrsDict "keysight.pwdatatools.AttrsDict") object and stored in the [`Group.attrs`](../api_reference/_autosummary/keysight.pwdatatools.Group.attrs.md#keysight.pwdatatools.Group.attrs "keysight.pwdatatools.Group.attrs") attribute. This is the same type of object that is used for the [`Block.attrs`](../api_reference/_autosummary/keysight.pwdatatools.Block.attrs.md#keysight.pwdatatools.Block.attrs "keysight.pwdatatools.Block.attrs") attribute. The [`AttrsDict`](../api_reference/_autosummary/keysight.pwdatatools.AttrsDict.md#keysight.pwdatatools.AttrsDict "keysight.pwdatatools.AttrsDict") class behaves like a type-restricted dict.

### From a file[](#from-a-file "Link to this heading")

Below, we create a Group by reading a Touchstone file. First, we write the Touchstone file using one of the functions available in the `keysight.pwdatatools.examples.touchstone` module. Then, we read the file into a Group using the [`Group.from_file()`](../api_reference/_autosummary/keysight.pwdatatools.Group.from_file.md#keysight.pwdatatools.Group.from_file "keysight.pwdatatools.Group.from_file") method.

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

The [`Group.from_file()`](../api_reference/_autosummary/keysight.pwdatatools.Group.from_file.md#keysight.pwdatatools.Group.from_file "keysight.pwdatatools.Group.from_file") method is a class method, so it can be called directly from the [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") class. Alternatively, you can use the free function `read_file_as_group()` to read a file into a Group.

See also

The [Read a File](read_a_file.md#read-a-file) section has more information on reading datafiles.

## Retrieve a member[](#retrieve-a-member "Link to this heading")

In order to access members in a Group, it’s possible to use the `[]` operator to perform list-like indexing and slicing, as well as dict-like lookups by member name. However, it is recommended instead to use the [`Group.get_member_as_block()`](../api_reference/_autosummary/keysight.pwdatatools.Group.get_member_as_block.md#keysight.pwdatatools.Group.get_member_as_block "keysight.pwdatatools.Group.get_member_as_block") and [`Group.get_member_as_group()`](../api_reference/_autosummary/keysight.pwdatatools.Group.get_member_as_group.md#keysight.pwdatatools.Group.get_member_as_group "keysight.pwdatatools.Group.get_member_as_group") methods. Both of these methods are able to retrieve members by integer index or by name, plus they have the following additional benefits over using list-like indexing (which invokes the `Group.__getitem__()` method):

* their return types are more specific. This means that IDEs and type checkers can be more helpful.
* they can cast members to the desired type. For example, if you request a member as a [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group"), but it is actually a [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block"), the [`Group.get_member_as_group()`](../api_reference/_autosummary/keysight.pwdatatools.Group.get_member_as_group.md#keysight.pwdatatools.Group.get_member_as_group "keysight.pwdatatools.Group.get_member_as_group") method can optionally cast it to a [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") for you.

Below, we demonstrate how to use the [`Group.get_member_as_block()`](../api_reference/_autosummary/keysight.pwdatatools.Group.get_member_as_block.md#keysight.pwdatatools.Group.get_member_as_block "keysight.pwdatatools.Group.get_member_as_block") with integer index and name lookup.

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

A for-loop does *not* recursively iterate over the members of any child Groups. To recursively iterate, use the [`Group.iter_members()`](../api_reference/_autosummary/keysight.pwdatatools.Group.iter_members.md#keysight.pwdatatools.Group.iter_members "keysight.pwdatatools.Group.iter_members") method with `recursive=True`. Let’s create a child Group, add it to our Group, and recursively iterate.

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

It is also possible to iterate over only the Blocks in a Group using the [`Group.iter_blocks()`](../api_reference/_autosummary/keysight.pwdatatools.Group.iter_blocks.md#keysight.pwdatatools.Group.iter_blocks "keysight.pwdatatools.Group.iter_blocks") method. This method also accepts the `recursive` argument. Note how `child_group` is not yielded during iteration, but `grandchild_block`, which is contained in `child_group`, is yielded.

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
* the [`Group.append()`](../api_reference/_autosummary/keysight.pwdatatools.Group.append.md#keysight.pwdatatools.Group.append "keysight.pwdatatools.Group.append") method
* the [`Group.extend()`](../api_reference/_autosummary/keysight.pwdatatools.Group.extend.md#keysight.pwdatatools.Group.extend "keysight.pwdatatools.Group.extend") method
* the [`Group.insert()`](../api_reference/_autosummary/keysight.pwdatatools.Group.insert.md#keysight.pwdatatools.Group.insert "keysight.pwdatatools.Group.insert") method

The `+=` operator is the most concise way to add a single member to a Group. It is equivalent to calling the [`Group.append()`](../api_reference/_autosummary/keysight.pwdatatools.Group.append.md#keysight.pwdatatools.Group.append "keysight.pwdatatools.Group.append") method. If we view the [`Group.members`](../api_reference/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") attribute, we can see that the new Block is added to the end of the list of members.

```
>>> group += pwdt.Block(name='block3')
>>> group.members
MembersList(
    [
        <Block 'power_meas' with 2 Vars and 2 observations>,
        <Block 'power_sim' with 2 Vars and 2 observations>,
        <Group 'child_group' with 1 Block>,
        <Block 'block3' with 0 Vars and -1 observations>,
    ]
)
```

The [`Group.extend()`](../api_reference/_autosummary/keysight.pwdatatools.Group.extend.md#keysight.pwdatatools.Group.extend "keysight.pwdatatools.Group.extend") method is the most straightforward way to add multiple members. It is equivalent to calling the [`Group.append()`](../api_reference/_autosummary/keysight.pwdatatools.Group.append.md#keysight.pwdatatools.Group.append "keysight.pwdatatools.Group.append") method for each member in the list.

```
>>> list_of_blocks = [pwdt.Block(name='block4'), pwdt.Block(name='block5')]
>>> group.extend(list_of_blocks)
>>> group.members
MembersList(
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

The [`Group.insert()`](../api_reference/_autosummary/keysight.pwdatatools.Group.insert.md#keysight.pwdatatools.Group.insert "keysight.pwdatatools.Group.insert") method is the best way to insert a single member into a Group at a specific index.

```
>>> group.insert(0, pwdt.Block(name='block0'))
>>> group.members
MembersList(
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

* the [`Group.remove()`](../api_reference/_autosummary/keysight.pwdatatools.Group.remove.md#keysight.pwdatatools.Group.remove "keysight.pwdatatools.Group.remove") method
* the [`Group.pop()`](../api_reference/_autosummary/keysight.pwdatatools.Group.pop.md#keysight.pwdatatools.Group.pop "keysight.pwdatatools.Group.pop") method
* the [`Group.clear()`](../api_reference/_autosummary/keysight.pwdatatools.Group.clear.md#keysight.pwdatatools.Group.clear "keysight.pwdatatools.Group.clear") method

The [`Group.remove()`](../api_reference/_autosummary/keysight.pwdatatools.Group.remove.md#keysight.pwdatatools.Group.remove "keysight.pwdatatools.Group.remove") method can be called with either an integer index or a member name.

```
>>> group.remove(0)  # remove the first member
```

The [`Group.pop()`](../api_reference/_autosummary/keysight.pwdatatools.Group.pop.md#keysight.pwdatatools.Group.pop "keysight.pwdatatools.Group.pop") method is very similar to [`Group.remove()`](../api_reference/_autosummary/keysight.pwdatatools.Group.remove.md#keysight.pwdatatools.Group.remove "keysight.pwdatatools.Group.remove"), except that [`Group.pop()`](../api_reference/_autosummary/keysight.pwdatatools.Group.pop.md#keysight.pwdatatools.Group.pop "keysight.pwdatatools.Group.pop") also returns the removed member. Also, a more subtle difference is that [`Group.pop()`](../api_reference/_autosummary/keysight.pwdatatools.Group.pop.md#keysight.pwdatatools.Group.pop "keysight.pwdatatools.Group.pop") defaults to removing the last member, whereas [`Group.remove()`](../api_reference/_autosummary/keysight.pwdatatools.Group.remove.md#keysight.pwdatatools.Group.remove "keysight.pwdatatools.Group.remove") does not have a default index. This is because [`Group.pop()`](../api_reference/_autosummary/keysight.pwdatatools.Group.pop.md#keysight.pwdatatools.Group.pop "keysight.pwdatatools.Group.pop") is modeled after the built-in `list.pop()` method, which also defaults to removing the last item.

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
MembersList(
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

* the [`Group.members`](../api_reference/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") attribute
* the [`Group.tree()`](../api_reference/_autosummary/keysight.pwdatatools.Group.tree.md#keysight.pwdatatools.Group.tree "keysight.pwdatatools.Group.tree") method

Note

The [`Group.members`](../api_reference/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") attribute was previously introduced, but this section gives more details.

The [`Group.members`](../api_reference/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") stores a `MembersList` object, which is a type-restricted list of [`Block`](../api_reference/_autosummary/keysight.pwdatatools.Block.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") and [`Group`](../api_reference/_autosummary/keysight.pwdatatools.Group.md#keysight.pwdatatools.Group "keysight.pwdatatools.Group") instances. This object works just like a regular Python list. If you view the [`Group.members`](../api_reference/_autosummary/keysight.pwdatatools.Group.members.md#keysight.pwdatatools.Group.members "keysight.pwdatatools.Group.members") attribute, you will see one-line summaries of each Group and Block, which can be useful because it shows some details about the members while still being concise.

```
>>> group.members
MembersList(
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

Another method that can be used to help understand the hierarchy of a Group is [`Group.tree()`](../api_reference/_autosummary/keysight.pwdatatools.Group.tree.md#keysight.pwdatatools.Group.tree "keysight.pwdatatools.Group.tree"). This method prints a tree-like representation of the Group and its members. This has the added benefit of expanding child Groups recursively, showing summaries of their members.

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

The [`Group.to_file()`](../api_reference/_autosummary/keysight.pwdatatools.Group.to_file.md#keysight.pwdatatools.Group.to_file "keysight.pwdatatools.Group.to_file") method can be used to write a Group to a file. This method is equivalent to passing a Group into the top-level function `write_file()`. Typically, the datafile format is inferred from the file extension. Below, we write out the Group to a .pwdt file, an MDIF file, and an ADS dataset file.

```
>>> group.to_file('/datafolder/meas_and_sim_data.pwdt') # .pwdt file format can directly handle this 2-level hierarchy
>>> group.to_file('/datafolder/meas_and_sim_data.mdif') # 2nd level of hierarchy gets flattened using default naming scheme
>>> group.to_file('/datafolder/meas_and_sim_data.ds') # 2nd level of hierarchy gets flattened using default naming scheme
```

Not all file formats are able to handle hierarchical datasets. Furthermore, most supported hierarchical file formats can only handle one level of hierarchy (with the notable exception of the native pwdt format). However, when writing a file from a Group that contains child Groups, those additional levels of hierarchy are automatically flattened if the datafile format can handle only one level (for example, ADS datasets and generic MDIF files). This is done by flattening the child Groups and representing those parent-child relationships via hierarchical names. For more control over how this flattening is done, you can use the [`Group.flatten()`](../api_reference/_autosummary/keysight.pwdatatools.Group.flatten.md#keysight.pwdatatools.Group.flatten "keysight.pwdatatools.Group.flatten") method to flatten the hierarchy yourself before writing to a file. However, the effects of the [`Group.flatten()`](../api_reference/_autosummary/keysight.pwdatatools.Group.flatten.md#keysight.pwdatatools.Group.flatten "keysight.pwdatatools.Group.flatten") method are not reversible. There is a context manager version of [`Group.flatten()`](../api_reference/_autosummary/keysight.pwdatatools.Group.flatten.md#keysight.pwdatatools.Group.flatten "keysight.pwdatatools.Group.flatten") called [`Group.flattened()`](../api_reference/_autosummary/keysight.pwdatatools.Group.flattened.md#keysight.pwdatatools.Group.flattened "keysight.pwdatatools.Group.flattened"), which can be used to temporarily flatten a Group for specific operation(s). Below, we use the [`Group.flattened()`](../api_reference/_autosummary/keysight.pwdatatools.Group.flattened.md#keysight.pwdatatools.Group.flattened "keysight.pwdatatools.Group.flattened") method to temporarily flatten the Group before writing to an MDIF file and printing the tree.

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

Note how the `grandchild_block` is now named `child_group:grandchild_block`, which uses a non-default parameter setting `sep=':'`. The `child_group` was flattened into the parent Group, and the parent-child relationship is now represented via the hierarchical name. This extra step to explicitly flatten the Group is not necessary unless you want to use some non-default settings for hierarchical membernames, as we are doing here with the non-default `sep`. If want to use all the default hierarchical membername settings (which include not only `sep` but also a parameter that controls behavior related to empty membernames), you can just call [`Group.to_file()`](../api_reference/_autosummary/keysight.pwdatatools.Group.to_file.md#keysight.pwdatatools.Group.to_file "keysight.pwdatatools.Group.to_file") directly and it will automatically flatten the Group for you when writing to MDIF, ADS dataset, etc. However, the hierarchy will remain intact when writing to the native .pwdt format.

Now if we call the [`Group.tree()`](../api_reference/_autosummary/keysight.pwdatatools.Group.tree.md#keysight.pwdatatools.Group.tree "keysight.pwdatatools.Group.tree") method again outside of the context manager code block, we can see that the Group’s hierarchy has been restored.

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

On this page

[Previous

Use the Block Class](use_block_class.md)
[Next

Use Roles](use_roles.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top