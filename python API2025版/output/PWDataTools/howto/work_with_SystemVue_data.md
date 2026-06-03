<!-- 来源: howto\work_with_SystemVue_data.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-pwdatatools](../index.md)
* [How To](index.md)
* Work with SystemVue Data

0.11.0

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/howto/work_with_SystemVue_data.rst.txt)

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
  + [Use the Group Class](use_group_class.md)
  + [Work with ADS Data](work_with_ADS_data.md)
  + [Work with CSV Data](work_with_csv_data.md)
  + [Work with Load Pull Data](work_with_loadpull_data.md)
  + Work with SystemVue Data
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

On this page

[Previous

Work with Load Pull Data](work_with_loadpull_data.md)
[Next

Show or Hide Log Messages](show_or_hide_messages.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top