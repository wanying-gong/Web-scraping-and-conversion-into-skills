<!-- 来源: howto\use_block_class.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-pwdatatools](../index.md)
* [How To](index.md)
* Use the Block Class

0.11.0

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/howto/use_block_class.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* [Initial Setup](../initial_setup/index.md)
  + [Installation](../initial_setup/installation.md)
  + [Dependencies](../initial_setup/dependencies.md)
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
  + [Work with ADS Data](work_with_ADS_data.md)
  + [Work with CSV Data](work_with_csv_data.md)
  + [Work with Load Pull Data](work_with_loadpull_data.md)
  + [Work with SystemVue Data](work_with_SystemVue_data.md)
  + [Show or Hide Log Messages](show_or_hide_messages.md)
  + [Get the Data Tools Version](get_the_version.md)
  + [Use the New Data Tools Version](use_new_version.md)
* [Examples](../examples/index.md)
  + [Load Pull Examples](../examples/loadpull/index.md)
    - [Swept Gamma](../examples/loadpull/swept_gamma_example.md)
    - [Swept Gamma and Power](../examples/loadpull/swept_gamma_power_example.md)
    - [Swept Frequency, Gamma, and Power](../examples/loadpull/swept_freq_gamma_power_example.md)
    - [Focus lpcwave file](../examples/loadpull/focus_lpcwave.md)
* [API Reference](../api_reference/index.md)
  + [Main](../api_reference/main/index.md)
    - [Var](../api_reference/main/var/index.md)
      * [keysight.pwdatatools.Var.attrs](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.attrs.md)
      * [keysight.pwdatatools.Var.block](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.block.md)
      * [keysight.pwdatatools.Var.kind](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.kind.md)
      * [keysight.pwdatatools.Var.dims](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.dims.md)
      * [keysight.pwdatatools.Var.dtype](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.dtype.md)
      * [keysight.pwdatatools.Var.name](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.name.md)
      * [keysight.pwdatatools.Var.ndim](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.ndim.md)
      * [keysight.pwdatatools.Var.role](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.role.md)
      * [keysight.pwdatatools.Var.shape](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.shape.md)
      * [keysight.pwdatatools.Var.size](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.size.md)
      * [keysight.pwdatatools.Var.unit](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.unit.md)
      * [keysight.pwdatatools.Var.\_\_array\_\_](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__array__.md)
      * [keysight.pwdatatools.Var.\_\_array\_ufunc\_\_](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__array_ufunc__.md)
      * [keysight.pwdatatools.Var.\_\_call\_\_](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__call__.md)
      * [keysight.pwdatatools.Var.\_\_getitem\_\_](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__getitem__.md)
      * [keysight.pwdatatools.Var.\_\_init\_\_](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__init__.md)
      * [keysight.pwdatatools.Var.\_\_iter\_\_](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__iter__.md)
      * [keysight.pwdatatools.Var.\_\_len\_\_](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__len__.md)
      * [keysight.pwdatatools.Var.\_\_repr\_\_](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__repr__.md)
      * [keysight.pwdatatools.Var.\_\_repr\_short\_\_](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__repr_short__.md)
      * [keysight.pwdatatools.Var.copy](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.copy.md)
      * [keysight.pwdatatools.Var.copy\_metadata\_in\_place](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.copy_metadata_in_place.md)
      * [keysight.pwdatatools.Var.count\_observations](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.count_observations.md)
      * [keysight.pwdatatools.Var.drop\_observations](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.drop_observations.md)
      * [keysight.pwdatatools.Var.fill\_nan](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.fill_nan.md)
      * [keysight.pwdatatools.Var.fill\_null](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.fill_null.md)
      * [keysight.pwdatatools.Var.has\_empty\_dims](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.has_empty_dims.md)
      * [keysight.pwdatatools.Var.has\_role](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.has_role.md)
      * [keysight.pwdatatools.Var.info](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.info.md)
      * [keysight.pwdatatools.Var.is\_nan](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.is_nan.md)
      * [keysight.pwdatatools.Var.is\_null](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.is_null.md)
      * [keysight.pwdatatools.Var.keep\_observations](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.keep_observations.md)
      * [keysight.pwdatatools.Var.repeat\_observations](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.repeat_observations.md)
      * [keysight.pwdatatools.Var.rename](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.rename.md)
      * [keysight.pwdatatools.Var.replace](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.replace.md)
      * [keysight.pwdatatools.Var.select](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.select.md)
      * [keysight.pwdatatools.Var.set\_data\_in\_place](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.set_data_in_place.md)
      * [keysight.pwdatatools.Var.sort\_observations](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.sort_observations.md)
      * [keysight.pwdatatools.Var.to\_numpy\_maskedarray](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_numpy_maskedarray.md)
      * [keysight.pwdatatools.Var.to\_numpy\_ndarray](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_numpy_ndarray.md)
      * [keysight.pwdatatools.Var.to\_pandas\_dataframe](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_pandas_dataframe.md)
      * [keysight.pwdatatools.Var.to\_pandas\_series](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_pandas_series.md)
      * [keysight.pwdatatools.Var.from\_1D\_vars](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.from_1D_vars.md)
      * [keysight.pwdatatools.Var.from\_pandas\_dataframe](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.from_pandas_dataframe.md)
      * [keysight.pwdatatools.Var.from\_pandas\_series](../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.from_pandas_series.md)
    - [Block](../api_reference/main/block/index.md)
      * [keysight.pwdatatools.Block.attrs](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.attrs.md)
      * [keysight.pwdatatools.Block.dvarnames](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.dvarnames.md)
      * [keysight.pwdatatools.Block.exprs](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.exprs.md)
      * [keysight.pwdatatools.Block.idxnames](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.idxnames.md)
      * [keysight.pwdatatools.Block.ivarnames](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.ivarnames.md)
      * [keysight.pwdatatools.Block.name](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.name.md)
      * [keysight.pwdatatools.Block.varnames](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.varnames.md)
      * [keysight.pwdatatools.Block.\_\_contains\_\_](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__contains__.md)
      * [keysight.pwdatatools.Block.\_\_delitem\_\_](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__delitem__.md)
      * [keysight.pwdatatools.Block.\_\_eq\_\_](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__eq__.md)
      * [keysight.pwdatatools.Block.\_\_getitem\_\_](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__getitem__.md)
      * [keysight.pwdatatools.Block.\_\_init\_\_](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__init__.md)
      * [keysight.pwdatatools.Block.\_\_iter\_\_](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__iter__.md)
      * [keysight.pwdatatools.Block.\_\_len\_\_](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__len__.md)
      * [keysight.pwdatatools.Block.\_\_repr\_\_](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__repr__.md)
      * [keysight.pwdatatools.Block.\_\_repr\_short\_\_](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__repr_short__.md)
      * [keysight.pwdatatools.Block.\_\_setitem\_\_](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__setitem__.md)
      * [keysight.pwdatatools.Block.clear](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.clear.md)
      * [keysight.pwdatatools.Block.copy](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.copy.md)
      * [keysight.pwdatatools.Block.count\_observations](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.count_observations.md)
      * [keysight.pwdatatools.Block.crucial\_varnames](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.crucial_varnames.md)
      * [keysight.pwdatatools.Block.drop\_observations](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.drop_observations.md)
      * [keysight.pwdatatools.Block.drop\_vars](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.drop_vars.md)
      * [keysight.pwdatatools.Block.drop\_vars\_in\_place](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.drop_vars_in_place.md)
      * [keysight.pwdatatools.Block.expr\_as\_numpy\_ndarray](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.expr_as_numpy_ndarray.md)
      * [keysight.pwdatatools.Block.fill\_nan](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.fill_nan.md)
      * [keysight.pwdatatools.Block.fill\_null](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.fill_null.md)
      * [keysight.pwdatatools.Block.get](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.get.md)
      * [keysight.pwdatatools.Block.get\_var](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.get_var.md)
      * [keysight.pwdatatools.Block.get\_var\_as\_expr](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.get_var_as_expr.md)
      * [keysight.pwdatatools.Block.info](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.info.md)
      * [keysight.pwdatatools.Block.is\_block](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.is_block.md)
      * [keysight.pwdatatools.Block.is\_group](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.is_group.md)
      * [keysight.pwdatatools.Block.items](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.items.md)
      * [keysight.pwdatatools.Block.iter\_sections](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.iter_sections.md)
      * [keysight.pwdatatools.Block.iter\_vars](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.iter_vars.md)
      * [keysight.pwdatatools.Block.keep\_observations](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.keep_observations.md)
      * [keysight.pwdatatools.Block.keep\_vars](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.keep_vars.md)
      * [keysight.pwdatatools.Block.keep\_vars\_in\_place](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.keep_vars_in_place.md)
      * [keysight.pwdatatools.Block.keys](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.keys.md)
      * [keysight.pwdatatools.Block.pop](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.pop.md)
      * [keysight.pwdatatools.Block.rename\_vars](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.rename_vars.md)
      * [keysight.pwdatatools.Block.rename\_vars\_in\_place](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.rename_vars_in_place.md)
      * [keysight.pwdatatools.Block.set\_data](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.set_data.md)
      * [keysight.pwdatatools.Block.set\_data\_in\_place](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.set_data_in_place.md)
      * [keysight.pwdatatools.Block.set\_vars\_in\_place](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.set_vars_in_place.md)
      * [keysight.pwdatatools.Block.sort\_observations](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.sort_observations.md)
      * [keysight.pwdatatools.Block.sort\_observations\_by](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.sort_observations_by.md)
      * [keysight.pwdatatools.Block.to\_pandas\_dataframe](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.to_pandas_dataframe.md)
      * [keysight.pwdatatools.Block.to\_file](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.to_file.md)
      * [keysight.pwdatatools.Block.update](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.update.md)
      * [keysight.pwdatatools.Block.values](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.values.md)
      * [keysight.pwdatatools.Block.with\_idxs](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.with_idxs.md)
      * [keysight.pwdatatools.Block.from\_file](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.from_file.md)
      * [keysight.pwdatatools.Block.from\_pandas\_dataframe](../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.from_pandas_dataframe.md)
    - [Group](../api_reference/main/group/index.md)
      * [keysight.pwdatatools.Group.attrs](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.attrs.md)
      * [keysight.pwdatatools.Group.members](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.members.md)
      * [keysight.pwdatatools.Group.name](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.name.md)
      * [keysight.pwdatatools.Group.\_\_add\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__add__.md)
      * [keysight.pwdatatools.Group.\_\_contains\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__contains__.md)
      * [keysight.pwdatatools.Group.\_\_delitem\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__delitem__.md)
      * [keysight.pwdatatools.Group.\_\_eq\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__eq__.md)
      * [keysight.pwdatatools.Group.\_\_getitem\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__getitem__.md)
      * [keysight.pwdatatools.Group.\_\_iadd\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__iadd__.md)
      * [keysight.pwdatatools.Group.\_\_init\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__init__.md)
      * [keysight.pwdatatools.Group.\_\_iter\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__iter__.md)
      * [keysight.pwdatatools.Group.\_\_len\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__len__.md)
      * [keysight.pwdatatools.Group.\_\_repr\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__repr__.md)
      * [keysight.pwdatatools.Group.\_\_repr\_short\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__repr_short__.md)
      * [keysight.pwdatatools.Group.\_\_setitem\_\_](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__setitem__.md)
      * [keysight.pwdatatools.Group.append](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.append.md)
      * [keysight.pwdatatools.Group.clear](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.clear.md)
      * [keysight.pwdatatools.Group.copy](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.copy.md)
      * [keysight.pwdatatools.Group.count](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.count.md)
      * [keysight.pwdatatools.Group.extend](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.extend.md)
      * [keysight.pwdatatools.Group.fill\_membernames](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.fill_membernames.md)
      * [keysight.pwdatatools.Group.filled\_membernames](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.filled_membernames.md)
      * [keysight.pwdatatools.Group.flatten](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.flatten.md)
      * [keysight.pwdatatools.Group.flattened](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.flattened.md)
      * [keysight.pwdatatools.Group.get\_member\_as\_block](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.get_member_as_block.md)
      * [keysight.pwdatatools.Group.get\_member\_as\_group](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.get_member_as_group.md)
      * [keysight.pwdatatools.Group.get\_member\_as\_loadpullblock](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.get_member_as_loadpullblock.md)
      * [keysight.pwdatatools.Group.index](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.index.md)
      * [keysight.pwdatatools.Group.insert](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.insert.md)
      * [keysight.pwdatatools.Group.is\_block](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.is_block.md)
      * [keysight.pwdatatools.Group.is\_group](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.is_group.md)
      * [keysight.pwdatatools.Group.iter\_blocks](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.iter_blocks.md)
      * [keysight.pwdatatools.Group.iter\_members](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.iter_members.md)
      * [keysight.pwdatatools.Group.pop](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.pop.md)
      * [keysight.pwdatatools.Group.remove](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.remove.md)
      * [keysight.pwdatatools.Group.reverse](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.reverse.md)
      * [keysight.pwdatatools.Group.to\_file](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.to_file.md)
      * [keysight.pwdatatools.Group.tree](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.tree.md)
      * [keysight.pwdatatools.Group.from\_file](../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.from_file.md)
  + [Metadata](../api_reference/metadata/index.md)
    - [AttrsDict](../api_reference/metadata/attrsdict/index.md)
      * [keysight.pwdatatools.AttrsDict.key\_type](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.key_type.md)
      * [keysight.pwdatatools.AttrsDict.reserved\_keys](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.reserved_keys.md)
      * [keysight.pwdatatools.AttrsDict.value\_types](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.value_types.md)
      * [keysight.pwdatatools.AttrsDict.\_\_contains\_\_](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__contains__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_delitem\_\_](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__delitem__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_eq\_\_](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__eq__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_getitem\_\_](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__getitem__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_init\_\_](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__init__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_iter\_\_](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__iter__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_len\_\_](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__len__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_ne\_\_](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__ne__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_repr\_\_](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__repr__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_repr\_short\_\_](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__repr_short__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_setitem\_\_](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__setitem__.md)
      * [keysight.pwdatatools.AttrsDict.clear](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.clear.md)
      * [keysight.pwdatatools.AttrsDict.copy](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.copy.md)
      * [keysight.pwdatatools.AttrsDict.get](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.get.md)
      * [keysight.pwdatatools.AttrsDict.items](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.items.md)
      * [keysight.pwdatatools.AttrsDict.keys](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.keys.md)
      * [keysight.pwdatatools.AttrsDict.pop](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.pop.md)
      * [keysight.pwdatatools.AttrsDict.popitem](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.popitem.md)
      * [keysight.pwdatatools.AttrsDict.setdefault](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.setdefault.md)
      * [keysight.pwdatatools.AttrsDict.to\_builtins](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.to_builtins.md)
      * [keysight.pwdatatools.AttrsDict.update](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.update.md)
      * [keysight.pwdatatools.AttrsDict.values](../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.values.md)
    - [Dims](../api_reference/metadata/dims/index.md)
      * [keysight.pwdatatools.Dims.ndim](../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.ndim.md)
      * [keysight.pwdatatools.Dims.\_\_bool\_\_](../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.__bool__.md)
      * [keysight.pwdatatools.Dims.\_\_eq\_\_](../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.__eq__.md)
      * [keysight.pwdatatools.Dims.\_\_init\_\_](../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.__init__.md)
      * [keysight.pwdatatools.Dims.\_\_repr\_\_](../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.__repr__.md)
      * [keysight.pwdatatools.Dims.\_\_repr\_short\_\_](../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.__repr_short__.md)
      * [keysight.pwdatatools.Dims.copy](../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.copy.md)
      * [keysight.pwdatatools.Dims.is\_empty](../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.is_empty.md)
      * [keysight.pwdatatools.Dims.replace](../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.replace.md)
  + [File I/O](../api_reference/fileio/index.md)
    - [DataFile](../api_reference/fileio/datafile/index.md)
      * [keysight.pwdatatools.DataFile.folder](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.folder.md)
      * [keysight.pwdatatools.DataFile.format\_override](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.format_override.md)
      * [keysight.pwdatatools.DataFile.ext](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.ext.md)
      * [keysight.pwdatatools.DataFile.name](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.name.md)
      * [keysight.pwdatatools.DataFile.path](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.path.md)
      * [keysight.pwdatatools.DataFile.stem](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.stem.md)
      * [keysight.pwdatatools.DataFile.suffix](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.suffix.md)
      * [keysight.pwdatatools.DataFile.\_\_init\_\_](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.__init__.md)
      * [keysight.pwdatatools.DataFile.\_\_repr\_\_](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.__repr__.md)
      * [keysight.pwdatatools.DataFile.copy](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.copy.md)
      * [keysight.pwdatatools.DataFile.delete](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.delete.md)
      * [keysight.pwdatatools.DataFile.exists](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.exists.md)
      * [keysight.pwdatatools.DataFile.find\_diffs](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.find_diffs.md)
      * [keysight.pwdatatools.DataFile.get\_format](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.get_format.md)
      * [keysight.pwdatatools.DataFile.has\_format](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.has_format.md)
      * [keysight.pwdatatools.DataFile.has\_modtime\_match](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.has_modtime_match.md)
      * [keysight.pwdatatools.DataFile.is\_ads](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_ads.md)
      * [keysight.pwdatatools.DataFile.is\_citi](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_citi.md)
      * [keysight.pwdatatools.DataFile.is\_farfieldio](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_farfieldio.md)
      * [keysight.pwdatatools.DataFile.is\_hfss\_ffd](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_hfss_ffd.md)
      * [keysight.pwdatatools.DataFile.is\_loadpull](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_loadpull.md)
      * [keysight.pwdatatools.DataFile.is\_mdif](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_mdif.md)
      * [keysight.pwdatatools.DataFile.is\_mdm](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_mdm.md)
      * [keysight.pwdatatools.DataFile.is\_native](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_native.md)
      * [keysight.pwdatatools.DataFile.is\_s2pmdif](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_s2pmdif.md)
      * [keysight.pwdatatools.DataFile.is\_same](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_same.md)
      * [keysight.pwdatatools.DataFile.is\_smatrixio](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_smatrixio.md)
      * [keysight.pwdatatools.DataFile.is\_touchstone](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_touchstone.md)
      * [keysight.pwdatatools.DataFile.lines](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.lines.md)
      * [keysight.pwdatatools.DataFile.modtime](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.modtime.md)
      * [keysight.pwdatatools.DataFile.modtime\_datetime](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.modtime_datetime.md)
      * [keysight.pwdatatools.DataFile.read\_as\_block](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.read_as_block.md)
      * [keysight.pwdatatools.DataFile.read\_as\_group](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.read_as_group.md)
      * [keysight.pwdatatools.DataFile.read\_as\_loadpullblock](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.read_as_loadpullblock.md)
      * [keysight.pwdatatools.DataFile.remove](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.remove.md)
      * [keysight.pwdatatools.DataFile.set\_modtime](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.set_modtime.md)
      * [keysight.pwdatatools.DataFile.translate](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.translate.md)
      * [keysight.pwdatatools.DataFile.tree](../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.tree.md)
    - [read\_file\_as\_block](../api_reference/fileio/read_file_as_block.md)
    - [read\_file\_as\_group](../api_reference/fileio/read_file_as_group.md)
    - [read\_file\_as\_loadpullblock](../api_reference/fileio/read_file_as_loadpullblock.md)
    - [read\_file](../api_reference/fileio/read_file.md)
    - [translate\_file](../api_reference/fileio/translate_file.md)
    - [write\_file](../api_reference/fileio/write_file.md)
    - [File IO Options](../api_reference/fileio/options.md)
    - [File IO Options Defaults](../api_reference/fileio/defaults.md)
  + [Load Pull](../api_reference/loadpull/index.md)
    - [LoadPullBlock](../api_reference/loadpull/loadpullblock/index.md)
      * [keysight.pwdatatools.LoadPullBlock.attrs](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.attrs.md)
      * [keysight.pwdatatools.LoadPullBlock.dvarnames](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.dvarnames.md)
      * [keysight.pwdatatools.LoadPullBlock.exprs](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.exprs.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_idxname](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_idxname.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_ivarname](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivarname.md)
      * [keysight.pwdatatools.LoadPullBlock.idxnames](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.idxnames.md)
      * [keysight.pwdatatools.LoadPullBlock.ivarnames](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.ivarnames.md)
      * [keysight.pwdatatools.LoadPullBlock.name](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.name.md)
      * [keysight.pwdatatools.LoadPullBlock.outer\_idxnames](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.outer_idxnames.md)
      * [keysight.pwdatatools.LoadPullBlock.outer\_ivarnames](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.outer_ivarnames.md)
      * [keysight.pwdatatools.LoadPullBlock.power\_idxname](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.power_idxname.md)
      * [keysight.pwdatatools.LoadPullBlock.power\_ivarname](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.power_ivarname.md)
      * [keysight.pwdatatools.LoadPullBlock.varnames](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.varnames.md)
      * [keysight.pwdatatools.LoadPullBlock.z\_idxname](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.z_idxname.md)
      * [keysight.pwdatatools.LoadPullBlock.z\_ivarname](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.z_ivarname.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_contains\_\_](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__contains__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_delitem\_\_](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__delitem__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_getitem\_\_](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__getitem__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_init\_\_](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__init__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_iter\_\_](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__iter__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_len\_\_](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__len__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_repr\_\_](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__repr__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_repr\_short\_\_](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__repr_short__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_setitem\_\_](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__setitem__.md)
      * [keysight.pwdatatools.LoadPullBlock.at\_gcomp](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md)
      * [keysight.pwdatatools.LoadPullBlock.at\_power](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md)
      * [keysight.pwdatatools.LoadPullBlock.contourplot](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md)
      * [keysight.pwdatatools.LoadPullBlock.coord\_system](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.coord_system.md)
      * [keysight.pwdatatools.LoadPullBlock.copy](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.copy.md)
      * [keysight.pwdatatools.LoadPullBlock.count\_observations](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.count_observations.md)
      * [keysight.pwdatatools.LoadPullBlock.crucial\_varnames](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.crucial_varnames.md)
      * [keysight.pwdatatools.LoadPullBlock.drop\_invalid\_regular](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_invalid_regular.md)
      * [keysight.pwdatatools.LoadPullBlock.drop\_observations](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_observations.md)
      * [keysight.pwdatatools.LoadPullBlock.drop\_grid\_edges](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_grid_edges.md)
      * [keysight.pwdatatools.LoadPullBlock.drop\_vars](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_vars.md)
      * [keysight.pwdatatools.LoadPullBlock.drop\_vars\_in\_place](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_vars_in_place.md)
      * [keysight.pwdatatools.LoadPullBlock.expr\_as\_numpy\_ndarray](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.expr_as_numpy_ndarray.md)
      * [keysight.pwdatatools.LoadPullBlock.fill\_nan](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.fill_nan.md)
      * [keysight.pwdatatools.LoadPullBlock.fill\_null](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.fill_null.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_idx](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_idx.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_ivar](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_ivar\_scatterplot](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_to\_z](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_to_z.md)
      * [keysight.pwdatatools.LoadPullBlock.get](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get.md)
      * [keysight.pwdatatools.LoadPullBlock.get\_grid](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_grid.md)
      * [keysight.pwdatatools.LoadPullBlock.get\_sweep](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_sweep.md)
      * [keysight.pwdatatools.LoadPullBlock.get\_var](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_var.md)
      * [keysight.pwdatatools.LoadPullBlock.get\_var\_as\_expr](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_var_as_expr.md)
      * [keysight.pwdatatools.LoadPullBlock.grid\_data](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md)
      * [keysight.pwdatatools.LoadPullBlock.has\_gamma\_sweep](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_gamma_sweep.md)
      * [keysight.pwdatatools.LoadPullBlock.has\_power\_sweep](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_power_sweep.md)
      * [keysight.pwdatatools.LoadPullBlock.has\_outer\_sweep](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_outer_sweep.md)
      * [keysight.pwdatatools.LoadPullBlock.has\_regular\_power\_ivar](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar.md)
      * [keysight.pwdatatools.LoadPullBlock.has\_z\_sweep](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_z_sweep.md)
      * [keysight.pwdatatools.LoadPullBlock.info](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.info.md)
      * [keysight.pwdatatools.LoadPullBlock.is\_block](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.is_block.md)
      * [keysight.pwdatatools.LoadPullBlock.is\_group](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.is_group.md)
      * [keysight.pwdatatools.LoadPullBlock.items](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.items.md)
      * [keysight.pwdatatools.LoadPullBlock.iter\_sections](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.iter_sections.md)
      * [keysight.pwdatatools.LoadPullBlock.iter\_vars](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.iter_vars.md)
      * [keysight.pwdatatools.LoadPullBlock.is\_gridded](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.is_gridded.md)
      * [keysight.pwdatatools.LoadPullBlock.keep\_observations](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md)
      * [keysight.pwdatatools.LoadPullBlock.keep\_vars](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_vars.md)
      * [keysight.pwdatatools.LoadPullBlock.keep\_vars\_in\_place](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_vars_in_place.md)
      * [keysight.pwdatatools.LoadPullBlock.keys](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keys.md)
      * [keysight.pwdatatools.LoadPullBlock.pop](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.pop.md)
      * [keysight.pwdatatools.LoadPullBlock.power\_idx](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.power_idx.md)
      * [keysight.pwdatatools.LoadPullBlock.power\_ivar](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.power_ivar.md)
      * [keysight.pwdatatools.LoadPullBlock.regularize\_power\_ivar](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md)
      * [keysight.pwdatatools.LoadPullBlock.rename\_vars](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.rename_vars.md)
      * [keysight.pwdatatools.LoadPullBlock.rename\_vars\_in\_place](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.rename_vars_in_place.md)
      * [keysight.pwdatatools.LoadPullBlock.set\_data](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.set_data.md)
      * [keysight.pwdatatools.LoadPullBlock.set\_data\_in\_place](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.set_data_in_place.md)
      * [keysight.pwdatatools.LoadPullBlock.set\_vars\_in\_place](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.set_vars_in_place.md)
      * [keysight.pwdatatools.LoadPullBlock.set\_zrefload\_role](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.set_zrefload_role.md)
      * [keysight.pwdatatools.LoadPullBlock.sort\_observations](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.sort_observations.md)
      * [keysight.pwdatatools.LoadPullBlock.sort\_observations\_by](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.sort_observations_by.md)
      * [keysight.pwdatatools.LoadPullBlock.to\_adscontourblock](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_adscontourblock.md)
      * [keysight.pwdatatools.LoadPullBlock.to\_pandas\_dataframe](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_pandas_dataframe.md)
      * [keysight.pwdatatools.LoadPullBlock.to\_file](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_file.md)
      * [keysight.pwdatatools.LoadPullBlock.tricontourplot](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.tricontourplot.md)
      * [keysight.pwdatatools.LoadPullBlock.update](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.update.md)
      * [keysight.pwdatatools.LoadPullBlock.values](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.values.md)
      * [keysight.pwdatatools.LoadPullBlock.with\_idxs](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.with_idxs.md)
      * [keysight.pwdatatools.LoadPullBlock.z\_ivar](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.z_ivar.md)
      * [keysight.pwdatatools.LoadPullBlock.zrefload](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.zrefload.md)
      * [keysight.pwdatatools.LoadPullBlock.z\_to\_gamma](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.z_to_gamma.md)
      * [keysight.pwdatatools.LoadPullBlock.from\_block](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.from_block.md)
      * [keysight.pwdatatools.LoadPullBlock.from\_file](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.from_file.md)
      * [keysight.pwdatatools.LoadPullBlock.from\_pandas\_dataframe](../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.from_pandas_dataframe.md)
    - [LoadPullSweep](../api_reference/loadpull/loadpullsweep/index.md)
      * [keysight.pwdatatools.LoadPullSweep.idxnames](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.idxnames.md)
      * [keysight.pwdatatools.LoadPullSweep.idxnames\_map](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.idxnames_map.md)
      * [keysight.pwdatatools.LoadPullSweep.ivarnames](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.ivarnames.md)
      * [keysight.pwdatatools.LoadPullSweep.gamma\_idxname](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_idxname.md)
      * [keysight.pwdatatools.LoadPullSweep.gamma\_ivarname](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_ivarname.md)
      * [keysight.pwdatatools.LoadPullSweep.gamma\_or\_z\_idxname](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_or_z_idxname.md)
      * [keysight.pwdatatools.LoadPullSweep.gamma\_or\_z\_ivarname](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_or_z_ivarname.md)
      * [keysight.pwdatatools.LoadPullSweep.outer\_idxnames](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.outer_idxnames.md)
      * [keysight.pwdatatools.LoadPullSweep.outer\_ivarnames](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.outer_ivarnames.md)
      * [keysight.pwdatatools.LoadPullSweep.power\_idxname](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.power_idxname.md)
      * [keysight.pwdatatools.LoadPullSweep.power\_ivarname](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.power_ivarname.md)
      * [keysight.pwdatatools.LoadPullSweep.z\_idxname](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.z_idxname.md)
      * [keysight.pwdatatools.LoadPullSweep.z\_ivarname](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.z_ivarname.md)
      * [keysight.pwdatatools.LoadPullSweep.replace](../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.replace.md)
    - [Grid](../api_reference/loadpull/grid/index.md)
      * [keysight.pwdatatools.Grid.coord\_system](../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.coord_system.md)
      * [keysight.pwdatatools.Grid.extents](../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.extents.md)
      * [keysight.pwdatatools.Grid.npointsx](../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.npointsx.md)
      * [keysight.pwdatatools.Grid.npointsy](../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.npointsy.md)
      * [keysight.pwdatatools.Grid.x\_unique](../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.x_unique.md)
      * [keysight.pwdatatools.Grid.y\_unique](../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.y_unique.md)
      * [keysight.pwdatatools.Grid.apply](../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.apply.md)
      * [keysight.pwdatatools.Grid.drop\_edges](../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.drop_edges.md)
      * [keysight.pwdatatools.Grid.includes\_pole](../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.includes_pole.md)
      * [keysight.pwdatatools.Grid.from\_gridded\_series](../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.from_gridded_series.md)
  + [Public Submodules](../api_reference/public_submodules/index.md)
    - [calc](../api_reference/public_submodules/calc/index.md)
      * [keysight.pwdatatools.calc.db\_to\_power](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.db_to_power.md)
      * [keysight.pwdatatools.calc.db\_to\_voltage](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.db_to_voltage.md)
      * [keysight.pwdatatools.calc.dbm\_to\_w](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.dbm_to_w.md)
      * [keysight.pwdatatools.calc.deg\_to\_rad](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.deg_to_rad.md)
      * [keysight.pwdatatools.calc.gamma\_to\_gamma](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.gamma_to_gamma.md)
      * [keysight.pwdatatools.calc.gamma\_to\_z](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.gamma_to_z.md)
      * [keysight.pwdatatools.calc.polar\_to\_rect](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.polar_to_rect.md)
      * [keysight.pwdatatools.calc.power\_to\_db](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.power_to_db.md)
      * [keysight.pwdatatools.calc.rad\_to\_deg](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.rad_to_deg.md)
      * [keysight.pwdatatools.calc.rect\_to\_polar](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.rect_to_polar.md)
      * [keysight.pwdatatools.calc.voltage\_to\_db](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.voltage_to_db.md)
      * [keysight.pwdatatools.calc.w\_to\_dbm](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.w_to_dbm.md)
      * [keysight.pwdatatools.calc.z\_to\_gamma](../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.z_to_gamma.md)
    - [datatypes](../api_reference/public_submodules/datatypes/index.md)
      * [keysight.pwdatatools.datatypes.Boolean](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Boolean.md)
      * [keysight.pwdatatools.datatypes.Complex64](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Complex64.md)
      * [keysight.pwdatatools.datatypes.Complex128](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Complex128.md)
      * [keysight.pwdatatools.datatypes.DataType](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.DataType.md)
      * [keysight.pwdatatools.datatypes.FillValues](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.FillValues.md)
      * [keysight.pwdatatools.datatypes.Float32](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Float32.md)
      * [keysight.pwdatatools.datatypes.Float64](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Float64.md)
      * [keysight.pwdatatools.datatypes.Int8](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int8.md)
      * [keysight.pwdatatools.datatypes.Int16](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int16.md)
      * [keysight.pwdatatools.datatypes.Int32](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int32.md)
      * [keysight.pwdatatools.datatypes.Int64](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int64.md)
      * [keysight.pwdatatools.datatypes.String](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.String.md)
      * [keysight.pwdatatools.datatypes.UInt8](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt8.md)
      * [keysight.pwdatatools.datatypes.UInt16](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt16.md)
      * [keysight.pwdatatools.datatypes.UInt32](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt32.md)
      * [keysight.pwdatatools.datatypes.UInt64](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt64.md)
      * [keysight.pwdatatools.datatypes.FillValues](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.FillValues.md)
    - [roles](../api_reference/public_submodules/roles/index.md)
    - [viz](../api_reference/public_submodules/viz/index.md)
      * [keysight.pwdatatools.viz.complex\_vector\_to\_str\_series](../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.complex_vector_to_str_series.md)
      * [keysight.pwdatatools.viz.contourplot](../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.contourplot.md)
      * [keysight.pwdatatools.viz.draw\_smith\_chart](../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.draw_smith_chart.md)
      * [keysight.pwdatatools.viz.float\_vector\_to\_str\_series](../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.float_vector_to_str_series.md)
      * [keysight.pwdatatools.viz.make\_contour\_levels](../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.make_contour_levels.md)
      * [keysight.pwdatatools.viz.tricontourplot](../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.tricontourplot.md)
      * [keysight.pwdatatools.viz.use\_keysight\_theme](../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.use_keysight_theme.md)
  + [Data Types](../api_reference/datatypes.md)
    - [Boolean](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Boolean.md)
    - [Complex64](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Complex64.md)
    - [Complex128](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Complex128.md)
    - [DataType](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.DataType.md)
    - [FillValues](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.FillValues.md)
    - [Float32](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Float32.md)
    - [Float64](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Float64.md)
    - [Int8](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int8.md)
    - [Int16](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int16.md)
    - [Int32](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int32.md)
    - [Int64](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int64.md)
    - [String](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.String.md)
    - [UInt8](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt8.md)
    - [UInt16](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt16.md)
    - [UInt32](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt32.md)
    - [UInt64](../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt64.md)
  + [Concatenation Functions](../api_reference/concat/index.md)
    - [concatenate\_blocks](../api_reference/concat/concatenate_blocks.md)
    - [concatenate\_loadpullblocks](../api_reference/concat/concatenate_loadpullblocks.md)
    - [concatenate\_vars](../api_reference/concat/concatenate_vars.md)
  + [Global Options](../api_reference/global_options.md)
* [Changelog](../changelog.md)

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

On this page

[Previous

Use the Var Class](use_var_class.md)
[Next

Use the Group Class](use_group_class.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top