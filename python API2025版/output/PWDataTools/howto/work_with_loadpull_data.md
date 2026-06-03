<!-- 来源: howto\work_with_loadpull_data.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-pwdatatools](../index.md)
* [How To](index.md)
* Work with Load Pull Data

0.11.0

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/howto/work_with_loadpull_data.rst.txt)

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
  + Work with Load Pull Data
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

On this page

[Previous

Work with CSV Data](work_with_csv_data.md)
[Next

Work with SystemVue Data](work_with_SystemVue_data.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top