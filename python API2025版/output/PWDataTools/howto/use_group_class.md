<!-- 来源: howto\use_group_class.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-pwdatatools](../index.md)
* [How To](index.md)
* Use the Group Class

0.11.0

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/howto/use_group_class.rst.txt)

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
  + [Use the Block Class](use_block_class.md)
  + Use the Group Class
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

On this page

[Previous

Use the Block Class](use_block_class.md)
[Next

Work with ADS Data](work_with_ADS_data.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top