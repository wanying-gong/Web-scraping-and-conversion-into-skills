<!-- 来源: examples\loadpull\swept_gamma_power_example.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-pwdatatools](../../index.md)
* [Examples](../index.md)
* [Load Pull Examples](index.md)
* Swept Gamma and Power

0.11.0

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/examples/loadpull/swept_gamma_power_example.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* [Initial Setup](../../initial_setup/index.md)
  + [Installation](../../initial_setup/installation.md)
  + [Dependencies](../../initial_setup/dependencies.md)
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
  + [Work with ADS Data](../../howto/work_with_ADS_data.md)
  + [Work with CSV Data](../../howto/work_with_csv_data.md)
  + [Work with Load Pull Data](../../howto/work_with_loadpull_data.md)
  + [Work with SystemVue Data](../../howto/work_with_SystemVue_data.md)
  + [Show or Hide Log Messages](../../howto/show_or_hide_messages.md)
  + [Get the Data Tools Version](../../howto/get_the_version.md)
  + [Use the New Data Tools Version](../../howto/use_new_version.md)
* [Examples](../index.md)
  + [Load Pull Examples](index.md)
    - [Swept Gamma](swept_gamma_example.md)
    - Swept Gamma and Power
    - [Swept Frequency, Gamma, and Power](swept_freq_gamma_power_example.md)
    - [Focus lpcwave file](focus_lpcwave.md)
* [API Reference](../../api_reference/index.md)
  + [Main](../../api_reference/main/index.md)
    - [Var](../../api_reference/main/var/index.md)
      * [keysight.pwdatatools.Var.attrs](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.attrs.md)
      * [keysight.pwdatatools.Var.block](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.block.md)
      * [keysight.pwdatatools.Var.kind](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.kind.md)
      * [keysight.pwdatatools.Var.dims](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.dims.md)
      * [keysight.pwdatatools.Var.dtype](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.dtype.md)
      * [keysight.pwdatatools.Var.name](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.name.md)
      * [keysight.pwdatatools.Var.ndim](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.ndim.md)
      * [keysight.pwdatatools.Var.role](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.role.md)
      * [keysight.pwdatatools.Var.shape](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.shape.md)
      * [keysight.pwdatatools.Var.size](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.size.md)
      * [keysight.pwdatatools.Var.unit](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.unit.md)
      * [keysight.pwdatatools.Var.\_\_array\_\_](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__array__.md)
      * [keysight.pwdatatools.Var.\_\_array\_ufunc\_\_](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__array_ufunc__.md)
      * [keysight.pwdatatools.Var.\_\_call\_\_](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__call__.md)
      * [keysight.pwdatatools.Var.\_\_getitem\_\_](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__getitem__.md)
      * [keysight.pwdatatools.Var.\_\_init\_\_](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__init__.md)
      * [keysight.pwdatatools.Var.\_\_iter\_\_](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__iter__.md)
      * [keysight.pwdatatools.Var.\_\_len\_\_](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__len__.md)
      * [keysight.pwdatatools.Var.\_\_repr\_\_](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__repr__.md)
      * [keysight.pwdatatools.Var.\_\_repr\_short\_\_](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.__repr_short__.md)
      * [keysight.pwdatatools.Var.copy](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.copy.md)
      * [keysight.pwdatatools.Var.copy\_metadata\_in\_place](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.copy_metadata_in_place.md)
      * [keysight.pwdatatools.Var.count\_observations](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.count_observations.md)
      * [keysight.pwdatatools.Var.drop\_observations](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.drop_observations.md)
      * [keysight.pwdatatools.Var.fill\_nan](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.fill_nan.md)
      * [keysight.pwdatatools.Var.fill\_null](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.fill_null.md)
      * [keysight.pwdatatools.Var.has\_empty\_dims](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.has_empty_dims.md)
      * [keysight.pwdatatools.Var.has\_role](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.has_role.md)
      * [keysight.pwdatatools.Var.info](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.info.md)
      * [keysight.pwdatatools.Var.is\_nan](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.is_nan.md)
      * [keysight.pwdatatools.Var.is\_null](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.is_null.md)
      * [keysight.pwdatatools.Var.keep\_observations](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.keep_observations.md)
      * [keysight.pwdatatools.Var.repeat\_observations](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.repeat_observations.md)
      * [keysight.pwdatatools.Var.rename](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.rename.md)
      * [keysight.pwdatatools.Var.replace](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.replace.md)
      * [keysight.pwdatatools.Var.select](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.select.md)
      * [keysight.pwdatatools.Var.set\_data\_in\_place](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.set_data_in_place.md)
      * [keysight.pwdatatools.Var.sort\_observations](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.sort_observations.md)
      * [keysight.pwdatatools.Var.to\_numpy\_maskedarray](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_numpy_maskedarray.md)
      * [keysight.pwdatatools.Var.to\_numpy\_ndarray](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_numpy_ndarray.md)
      * [keysight.pwdatatools.Var.to\_pandas\_dataframe](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_pandas_dataframe.md)
      * [keysight.pwdatatools.Var.to\_pandas\_series](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.to_pandas_series.md)
      * [keysight.pwdatatools.Var.from\_1D\_vars](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.from_1D_vars.md)
      * [keysight.pwdatatools.Var.from\_pandas\_dataframe](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.from_pandas_dataframe.md)
      * [keysight.pwdatatools.Var.from\_pandas\_series](../../api_reference/main/var/_autosummary/keysight.pwdatatools.Var.from_pandas_series.md)
    - [Block](../../api_reference/main/block/index.md)
      * [keysight.pwdatatools.Block.attrs](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.attrs.md)
      * [keysight.pwdatatools.Block.dvarnames](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.dvarnames.md)
      * [keysight.pwdatatools.Block.exprs](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.exprs.md)
      * [keysight.pwdatatools.Block.idxnames](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.idxnames.md)
      * [keysight.pwdatatools.Block.ivarnames](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.ivarnames.md)
      * [keysight.pwdatatools.Block.name](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.name.md)
      * [keysight.pwdatatools.Block.varnames](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.varnames.md)
      * [keysight.pwdatatools.Block.\_\_contains\_\_](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__contains__.md)
      * [keysight.pwdatatools.Block.\_\_delitem\_\_](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__delitem__.md)
      * [keysight.pwdatatools.Block.\_\_eq\_\_](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__eq__.md)
      * [keysight.pwdatatools.Block.\_\_getitem\_\_](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__getitem__.md)
      * [keysight.pwdatatools.Block.\_\_init\_\_](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__init__.md)
      * [keysight.pwdatatools.Block.\_\_iter\_\_](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__iter__.md)
      * [keysight.pwdatatools.Block.\_\_len\_\_](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__len__.md)
      * [keysight.pwdatatools.Block.\_\_repr\_\_](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__repr__.md)
      * [keysight.pwdatatools.Block.\_\_repr\_short\_\_](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__repr_short__.md)
      * [keysight.pwdatatools.Block.\_\_setitem\_\_](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.__setitem__.md)
      * [keysight.pwdatatools.Block.clear](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.clear.md)
      * [keysight.pwdatatools.Block.copy](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.copy.md)
      * [keysight.pwdatatools.Block.count\_observations](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.count_observations.md)
      * [keysight.pwdatatools.Block.crucial\_varnames](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.crucial_varnames.md)
      * [keysight.pwdatatools.Block.drop\_observations](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.drop_observations.md)
      * [keysight.pwdatatools.Block.drop\_vars](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.drop_vars.md)
      * [keysight.pwdatatools.Block.drop\_vars\_in\_place](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.drop_vars_in_place.md)
      * [keysight.pwdatatools.Block.expr\_as\_numpy\_ndarray](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.expr_as_numpy_ndarray.md)
      * [keysight.pwdatatools.Block.fill\_nan](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.fill_nan.md)
      * [keysight.pwdatatools.Block.fill\_null](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.fill_null.md)
      * [keysight.pwdatatools.Block.get](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.get.md)
      * [keysight.pwdatatools.Block.get\_var](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.get_var.md)
      * [keysight.pwdatatools.Block.get\_var\_as\_expr](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.get_var_as_expr.md)
      * [keysight.pwdatatools.Block.info](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.info.md)
      * [keysight.pwdatatools.Block.is\_block](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.is_block.md)
      * [keysight.pwdatatools.Block.is\_group](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.is_group.md)
      * [keysight.pwdatatools.Block.items](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.items.md)
      * [keysight.pwdatatools.Block.iter\_sections](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.iter_sections.md)
      * [keysight.pwdatatools.Block.iter\_vars](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.iter_vars.md)
      * [keysight.pwdatatools.Block.keep\_observations](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.keep_observations.md)
      * [keysight.pwdatatools.Block.keep\_vars](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.keep_vars.md)
      * [keysight.pwdatatools.Block.keep\_vars\_in\_place](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.keep_vars_in_place.md)
      * [keysight.pwdatatools.Block.keys](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.keys.md)
      * [keysight.pwdatatools.Block.pop](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.pop.md)
      * [keysight.pwdatatools.Block.rename\_vars](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.rename_vars.md)
      * [keysight.pwdatatools.Block.rename\_vars\_in\_place](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.rename_vars_in_place.md)
      * [keysight.pwdatatools.Block.set\_data](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.set_data.md)
      * [keysight.pwdatatools.Block.set\_data\_in\_place](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.set_data_in_place.md)
      * [keysight.pwdatatools.Block.set\_vars\_in\_place](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.set_vars_in_place.md)
      * [keysight.pwdatatools.Block.sort\_observations](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.sort_observations.md)
      * [keysight.pwdatatools.Block.sort\_observations\_by](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.sort_observations_by.md)
      * [keysight.pwdatatools.Block.to\_pandas\_dataframe](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.to_pandas_dataframe.md)
      * [keysight.pwdatatools.Block.to\_file](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.to_file.md)
      * [keysight.pwdatatools.Block.update](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.update.md)
      * [keysight.pwdatatools.Block.values](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.values.md)
      * [keysight.pwdatatools.Block.with\_idxs](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.with_idxs.md)
      * [keysight.pwdatatools.Block.from\_file](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.from_file.md)
      * [keysight.pwdatatools.Block.from\_pandas\_dataframe](../../api_reference/main/block/_autosummary/keysight.pwdatatools.Block.from_pandas_dataframe.md)
    - [Group](../../api_reference/main/group/index.md)
      * [keysight.pwdatatools.Group.attrs](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.attrs.md)
      * [keysight.pwdatatools.Group.members](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.members.md)
      * [keysight.pwdatatools.Group.name](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.name.md)
      * [keysight.pwdatatools.Group.\_\_add\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__add__.md)
      * [keysight.pwdatatools.Group.\_\_contains\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__contains__.md)
      * [keysight.pwdatatools.Group.\_\_delitem\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__delitem__.md)
      * [keysight.pwdatatools.Group.\_\_eq\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__eq__.md)
      * [keysight.pwdatatools.Group.\_\_getitem\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__getitem__.md)
      * [keysight.pwdatatools.Group.\_\_iadd\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__iadd__.md)
      * [keysight.pwdatatools.Group.\_\_init\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__init__.md)
      * [keysight.pwdatatools.Group.\_\_iter\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__iter__.md)
      * [keysight.pwdatatools.Group.\_\_len\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__len__.md)
      * [keysight.pwdatatools.Group.\_\_repr\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__repr__.md)
      * [keysight.pwdatatools.Group.\_\_repr\_short\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__repr_short__.md)
      * [keysight.pwdatatools.Group.\_\_setitem\_\_](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.__setitem__.md)
      * [keysight.pwdatatools.Group.append](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.append.md)
      * [keysight.pwdatatools.Group.clear](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.clear.md)
      * [keysight.pwdatatools.Group.copy](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.copy.md)
      * [keysight.pwdatatools.Group.count](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.count.md)
      * [keysight.pwdatatools.Group.extend](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.extend.md)
      * [keysight.pwdatatools.Group.fill\_membernames](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.fill_membernames.md)
      * [keysight.pwdatatools.Group.filled\_membernames](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.filled_membernames.md)
      * [keysight.pwdatatools.Group.flatten](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.flatten.md)
      * [keysight.pwdatatools.Group.flattened](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.flattened.md)
      * [keysight.pwdatatools.Group.get\_member\_as\_block](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.get_member_as_block.md)
      * [keysight.pwdatatools.Group.get\_member\_as\_group](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.get_member_as_group.md)
      * [keysight.pwdatatools.Group.get\_member\_as\_loadpullblock](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.get_member_as_loadpullblock.md)
      * [keysight.pwdatatools.Group.index](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.index.md)
      * [keysight.pwdatatools.Group.insert](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.insert.md)
      * [keysight.pwdatatools.Group.is\_block](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.is_block.md)
      * [keysight.pwdatatools.Group.is\_group](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.is_group.md)
      * [keysight.pwdatatools.Group.iter\_blocks](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.iter_blocks.md)
      * [keysight.pwdatatools.Group.iter\_members](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.iter_members.md)
      * [keysight.pwdatatools.Group.pop](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.pop.md)
      * [keysight.pwdatatools.Group.remove](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.remove.md)
      * [keysight.pwdatatools.Group.reverse](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.reverse.md)
      * [keysight.pwdatatools.Group.to\_file](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.to_file.md)
      * [keysight.pwdatatools.Group.tree](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.tree.md)
      * [keysight.pwdatatools.Group.from\_file](../../api_reference/main/group/_autosummary/keysight.pwdatatools.Group.from_file.md)
  + [Metadata](../../api_reference/metadata/index.md)
    - [AttrsDict](../../api_reference/metadata/attrsdict/index.md)
      * [keysight.pwdatatools.AttrsDict.key\_type](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.key_type.md)
      * [keysight.pwdatatools.AttrsDict.reserved\_keys](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.reserved_keys.md)
      * [keysight.pwdatatools.AttrsDict.value\_types](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.value_types.md)
      * [keysight.pwdatatools.AttrsDict.\_\_contains\_\_](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__contains__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_delitem\_\_](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__delitem__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_eq\_\_](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__eq__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_getitem\_\_](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__getitem__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_init\_\_](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__init__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_iter\_\_](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__iter__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_len\_\_](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__len__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_ne\_\_](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__ne__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_repr\_\_](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__repr__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_repr\_short\_\_](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__repr_short__.md)
      * [keysight.pwdatatools.AttrsDict.\_\_setitem\_\_](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.__setitem__.md)
      * [keysight.pwdatatools.AttrsDict.clear](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.clear.md)
      * [keysight.pwdatatools.AttrsDict.copy](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.copy.md)
      * [keysight.pwdatatools.AttrsDict.get](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.get.md)
      * [keysight.pwdatatools.AttrsDict.items](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.items.md)
      * [keysight.pwdatatools.AttrsDict.keys](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.keys.md)
      * [keysight.pwdatatools.AttrsDict.pop](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.pop.md)
      * [keysight.pwdatatools.AttrsDict.popitem](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.popitem.md)
      * [keysight.pwdatatools.AttrsDict.setdefault](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.setdefault.md)
      * [keysight.pwdatatools.AttrsDict.to\_builtins](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.to_builtins.md)
      * [keysight.pwdatatools.AttrsDict.update](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.update.md)
      * [keysight.pwdatatools.AttrsDict.values](../../api_reference/metadata/attrsdict/_autosummary/keysight.pwdatatools.AttrsDict.values.md)
    - [Dims](../../api_reference/metadata/dims/index.md)
      * [keysight.pwdatatools.Dims.ndim](../../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.ndim.md)
      * [keysight.pwdatatools.Dims.\_\_bool\_\_](../../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.__bool__.md)
      * [keysight.pwdatatools.Dims.\_\_eq\_\_](../../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.__eq__.md)
      * [keysight.pwdatatools.Dims.\_\_init\_\_](../../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.__init__.md)
      * [keysight.pwdatatools.Dims.\_\_repr\_\_](../../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.__repr__.md)
      * [keysight.pwdatatools.Dims.\_\_repr\_short\_\_](../../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.__repr_short__.md)
      * [keysight.pwdatatools.Dims.copy](../../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.copy.md)
      * [keysight.pwdatatools.Dims.is\_empty](../../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.is_empty.md)
      * [keysight.pwdatatools.Dims.replace](../../api_reference/metadata/dims/_autosummary/keysight.pwdatatools.Dims.replace.md)
  + [File I/O](../../api_reference/fileio/index.md)
    - [DataFile](../../api_reference/fileio/datafile/index.md)
      * [keysight.pwdatatools.DataFile.folder](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.folder.md)
      * [keysight.pwdatatools.DataFile.format\_override](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.format_override.md)
      * [keysight.pwdatatools.DataFile.ext](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.ext.md)
      * [keysight.pwdatatools.DataFile.name](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.name.md)
      * [keysight.pwdatatools.DataFile.path](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.path.md)
      * [keysight.pwdatatools.DataFile.stem](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.stem.md)
      * [keysight.pwdatatools.DataFile.suffix](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.suffix.md)
      * [keysight.pwdatatools.DataFile.\_\_init\_\_](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.__init__.md)
      * [keysight.pwdatatools.DataFile.\_\_repr\_\_](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.__repr__.md)
      * [keysight.pwdatatools.DataFile.copy](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.copy.md)
      * [keysight.pwdatatools.DataFile.delete](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.delete.md)
      * [keysight.pwdatatools.DataFile.exists](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.exists.md)
      * [keysight.pwdatatools.DataFile.find\_diffs](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.find_diffs.md)
      * [keysight.pwdatatools.DataFile.get\_format](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.get_format.md)
      * [keysight.pwdatatools.DataFile.has\_format](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.has_format.md)
      * [keysight.pwdatatools.DataFile.has\_modtime\_match](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.has_modtime_match.md)
      * [keysight.pwdatatools.DataFile.is\_ads](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_ads.md)
      * [keysight.pwdatatools.DataFile.is\_citi](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_citi.md)
      * [keysight.pwdatatools.DataFile.is\_farfieldio](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_farfieldio.md)
      * [keysight.pwdatatools.DataFile.is\_hfss\_ffd](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_hfss_ffd.md)
      * [keysight.pwdatatools.DataFile.is\_loadpull](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_loadpull.md)
      * [keysight.pwdatatools.DataFile.is\_mdif](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_mdif.md)
      * [keysight.pwdatatools.DataFile.is\_mdm](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_mdm.md)
      * [keysight.pwdatatools.DataFile.is\_native](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_native.md)
      * [keysight.pwdatatools.DataFile.is\_s2pmdif](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_s2pmdif.md)
      * [keysight.pwdatatools.DataFile.is\_same](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_same.md)
      * [keysight.pwdatatools.DataFile.is\_smatrixio](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_smatrixio.md)
      * [keysight.pwdatatools.DataFile.is\_touchstone](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.is_touchstone.md)
      * [keysight.pwdatatools.DataFile.lines](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.lines.md)
      * [keysight.pwdatatools.DataFile.modtime](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.modtime.md)
      * [keysight.pwdatatools.DataFile.modtime\_datetime](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.modtime_datetime.md)
      * [keysight.pwdatatools.DataFile.read\_as\_block](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.read_as_block.md)
      * [keysight.pwdatatools.DataFile.read\_as\_group](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.read_as_group.md)
      * [keysight.pwdatatools.DataFile.read\_as\_loadpullblock](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.read_as_loadpullblock.md)
      * [keysight.pwdatatools.DataFile.remove](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.remove.md)
      * [keysight.pwdatatools.DataFile.set\_modtime](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.set_modtime.md)
      * [keysight.pwdatatools.DataFile.translate](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.translate.md)
      * [keysight.pwdatatools.DataFile.tree](../../api_reference/fileio/datafile/_autosummary/keysight.pwdatatools.DataFile.tree.md)
    - [read\_file\_as\_block](../../api_reference/fileio/read_file_as_block.md)
    - [read\_file\_as\_group](../../api_reference/fileio/read_file_as_group.md)
    - [read\_file\_as\_loadpullblock](../../api_reference/fileio/read_file_as_loadpullblock.md)
    - [read\_file](../../api_reference/fileio/read_file.md)
    - [translate\_file](../../api_reference/fileio/translate_file.md)
    - [write\_file](../../api_reference/fileio/write_file.md)
    - [File IO Options](../../api_reference/fileio/options.md)
    - [File IO Options Defaults](../../api_reference/fileio/defaults.md)
  + [Load Pull](../../api_reference/loadpull/index.md)
    - [LoadPullBlock](../../api_reference/loadpull/loadpullblock/index.md)
      * [keysight.pwdatatools.LoadPullBlock.attrs](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.attrs.md)
      * [keysight.pwdatatools.LoadPullBlock.dvarnames](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.dvarnames.md)
      * [keysight.pwdatatools.LoadPullBlock.exprs](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.exprs.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_idxname](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_idxname.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_ivarname](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivarname.md)
      * [keysight.pwdatatools.LoadPullBlock.idxnames](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.idxnames.md)
      * [keysight.pwdatatools.LoadPullBlock.ivarnames](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.ivarnames.md)
      * [keysight.pwdatatools.LoadPullBlock.name](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.name.md)
      * [keysight.pwdatatools.LoadPullBlock.outer\_idxnames](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.outer_idxnames.md)
      * [keysight.pwdatatools.LoadPullBlock.outer\_ivarnames](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.outer_ivarnames.md)
      * [keysight.pwdatatools.LoadPullBlock.power\_idxname](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.power_idxname.md)
      * [keysight.pwdatatools.LoadPullBlock.power\_ivarname](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.power_ivarname.md)
      * [keysight.pwdatatools.LoadPullBlock.varnames](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.varnames.md)
      * [keysight.pwdatatools.LoadPullBlock.z\_idxname](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.z_idxname.md)
      * [keysight.pwdatatools.LoadPullBlock.z\_ivarname](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.z_ivarname.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_contains\_\_](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__contains__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_delitem\_\_](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__delitem__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_getitem\_\_](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__getitem__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_init\_\_](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__init__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_iter\_\_](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__iter__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_len\_\_](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__len__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_repr\_\_](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__repr__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_repr\_short\_\_](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__repr_short__.md)
      * [keysight.pwdatatools.LoadPullBlock.\_\_setitem\_\_](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__setitem__.md)
      * [keysight.pwdatatools.LoadPullBlock.at\_gcomp](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md)
      * [keysight.pwdatatools.LoadPullBlock.at\_power](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md)
      * [keysight.pwdatatools.LoadPullBlock.contourplot](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md)
      * [keysight.pwdatatools.LoadPullBlock.coord\_system](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.coord_system.md)
      * [keysight.pwdatatools.LoadPullBlock.copy](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.copy.md)
      * [keysight.pwdatatools.LoadPullBlock.count\_observations](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.count_observations.md)
      * [keysight.pwdatatools.LoadPullBlock.crucial\_varnames](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.crucial_varnames.md)
      * [keysight.pwdatatools.LoadPullBlock.drop\_invalid\_regular](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_invalid_regular.md)
      * [keysight.pwdatatools.LoadPullBlock.drop\_observations](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_observations.md)
      * [keysight.pwdatatools.LoadPullBlock.drop\_grid\_edges](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_grid_edges.md)
      * [keysight.pwdatatools.LoadPullBlock.drop\_vars](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_vars.md)
      * [keysight.pwdatatools.LoadPullBlock.drop\_vars\_in\_place](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_vars_in_place.md)
      * [keysight.pwdatatools.LoadPullBlock.expr\_as\_numpy\_ndarray](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.expr_as_numpy_ndarray.md)
      * [keysight.pwdatatools.LoadPullBlock.fill\_nan](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.fill_nan.md)
      * [keysight.pwdatatools.LoadPullBlock.fill\_null](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.fill_null.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_idx](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_idx.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_ivar](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_ivar\_scatterplot](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot.md)
      * [keysight.pwdatatools.LoadPullBlock.gamma\_to\_z](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_to_z.md)
      * [keysight.pwdatatools.LoadPullBlock.get](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get.md)
      * [keysight.pwdatatools.LoadPullBlock.get\_grid](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_grid.md)
      * [keysight.pwdatatools.LoadPullBlock.get\_sweep](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_sweep.md)
      * [keysight.pwdatatools.LoadPullBlock.get\_var](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_var.md)
      * [keysight.pwdatatools.LoadPullBlock.get\_var\_as\_expr](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_var_as_expr.md)
      * [keysight.pwdatatools.LoadPullBlock.grid\_data](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md)
      * [keysight.pwdatatools.LoadPullBlock.has\_gamma\_sweep](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_gamma_sweep.md)
      * [keysight.pwdatatools.LoadPullBlock.has\_power\_sweep](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_power_sweep.md)
      * [keysight.pwdatatools.LoadPullBlock.has\_outer\_sweep](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_outer_sweep.md)
      * [keysight.pwdatatools.LoadPullBlock.has\_regular\_power\_ivar](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar.md)
      * [keysight.pwdatatools.LoadPullBlock.has\_z\_sweep](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_z_sweep.md)
      * [keysight.pwdatatools.LoadPullBlock.info](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.info.md)
      * [keysight.pwdatatools.LoadPullBlock.is\_block](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.is_block.md)
      * [keysight.pwdatatools.LoadPullBlock.is\_group](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.is_group.md)
      * [keysight.pwdatatools.LoadPullBlock.items](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.items.md)
      * [keysight.pwdatatools.LoadPullBlock.iter\_sections](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.iter_sections.md)
      * [keysight.pwdatatools.LoadPullBlock.iter\_vars](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.iter_vars.md)
      * [keysight.pwdatatools.LoadPullBlock.is\_gridded](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.is_gridded.md)
      * [keysight.pwdatatools.LoadPullBlock.keep\_observations](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md)
      * [keysight.pwdatatools.LoadPullBlock.keep\_vars](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_vars.md)
      * [keysight.pwdatatools.LoadPullBlock.keep\_vars\_in\_place](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_vars_in_place.md)
      * [keysight.pwdatatools.LoadPullBlock.keys](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keys.md)
      * [keysight.pwdatatools.LoadPullBlock.pop](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.pop.md)
      * [keysight.pwdatatools.LoadPullBlock.power\_idx](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.power_idx.md)
      * [keysight.pwdatatools.LoadPullBlock.power\_ivar](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.power_ivar.md)
      * [keysight.pwdatatools.LoadPullBlock.regularize\_power\_ivar](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md)
      * [keysight.pwdatatools.LoadPullBlock.rename\_vars](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.rename_vars.md)
      * [keysight.pwdatatools.LoadPullBlock.rename\_vars\_in\_place](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.rename_vars_in_place.md)
      * [keysight.pwdatatools.LoadPullBlock.set\_data](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.set_data.md)
      * [keysight.pwdatatools.LoadPullBlock.set\_data\_in\_place](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.set_data_in_place.md)
      * [keysight.pwdatatools.LoadPullBlock.set\_vars\_in\_place](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.set_vars_in_place.md)
      * [keysight.pwdatatools.LoadPullBlock.set\_zrefload\_role](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.set_zrefload_role.md)
      * [keysight.pwdatatools.LoadPullBlock.sort\_observations](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.sort_observations.md)
      * [keysight.pwdatatools.LoadPullBlock.sort\_observations\_by](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.sort_observations_by.md)
      * [keysight.pwdatatools.LoadPullBlock.to\_adscontourblock](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_adscontourblock.md)
      * [keysight.pwdatatools.LoadPullBlock.to\_pandas\_dataframe](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_pandas_dataframe.md)
      * [keysight.pwdatatools.LoadPullBlock.to\_file](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_file.md)
      * [keysight.pwdatatools.LoadPullBlock.tricontourplot](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.tricontourplot.md)
      * [keysight.pwdatatools.LoadPullBlock.update](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.update.md)
      * [keysight.pwdatatools.LoadPullBlock.values](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.values.md)
      * [keysight.pwdatatools.LoadPullBlock.with\_idxs](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.with_idxs.md)
      * [keysight.pwdatatools.LoadPullBlock.z\_ivar](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.z_ivar.md)
      * [keysight.pwdatatools.LoadPullBlock.zrefload](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.zrefload.md)
      * [keysight.pwdatatools.LoadPullBlock.z\_to\_gamma](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.z_to_gamma.md)
      * [keysight.pwdatatools.LoadPullBlock.from\_block](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.from_block.md)
      * [keysight.pwdatatools.LoadPullBlock.from\_file](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.from_file.md)
      * [keysight.pwdatatools.LoadPullBlock.from\_pandas\_dataframe](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.from_pandas_dataframe.md)
    - [LoadPullSweep](../../api_reference/loadpull/loadpullsweep/index.md)
      * [keysight.pwdatatools.LoadPullSweep.idxnames](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.idxnames.md)
      * [keysight.pwdatatools.LoadPullSweep.idxnames\_map](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.idxnames_map.md)
      * [keysight.pwdatatools.LoadPullSweep.ivarnames](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.ivarnames.md)
      * [keysight.pwdatatools.LoadPullSweep.gamma\_idxname](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_idxname.md)
      * [keysight.pwdatatools.LoadPullSweep.gamma\_ivarname](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_ivarname.md)
      * [keysight.pwdatatools.LoadPullSweep.gamma\_or\_z\_idxname](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_or_z_idxname.md)
      * [keysight.pwdatatools.LoadPullSweep.gamma\_or\_z\_ivarname](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.gamma_or_z_ivarname.md)
      * [keysight.pwdatatools.LoadPullSweep.outer\_idxnames](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.outer_idxnames.md)
      * [keysight.pwdatatools.LoadPullSweep.outer\_ivarnames](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.outer_ivarnames.md)
      * [keysight.pwdatatools.LoadPullSweep.power\_idxname](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.power_idxname.md)
      * [keysight.pwdatatools.LoadPullSweep.power\_ivarname](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.power_ivarname.md)
      * [keysight.pwdatatools.LoadPullSweep.z\_idxname](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.z_idxname.md)
      * [keysight.pwdatatools.LoadPullSweep.z\_ivarname](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.z_ivarname.md)
      * [keysight.pwdatatools.LoadPullSweep.replace](../../api_reference/loadpull/loadpullsweep/_autosummary/keysight.pwdatatools.LoadPullSweep.replace.md)
    - [Grid](../../api_reference/loadpull/grid/index.md)
      * [keysight.pwdatatools.Grid.coord\_system](../../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.coord_system.md)
      * [keysight.pwdatatools.Grid.extents](../../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.extents.md)
      * [keysight.pwdatatools.Grid.npointsx](../../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.npointsx.md)
      * [keysight.pwdatatools.Grid.npointsy](../../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.npointsy.md)
      * [keysight.pwdatatools.Grid.x\_unique](../../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.x_unique.md)
      * [keysight.pwdatatools.Grid.y\_unique](../../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.y_unique.md)
      * [keysight.pwdatatools.Grid.apply](../../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.apply.md)
      * [keysight.pwdatatools.Grid.drop\_edges](../../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.drop_edges.md)
      * [keysight.pwdatatools.Grid.includes\_pole](../../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.includes_pole.md)
      * [keysight.pwdatatools.Grid.from\_gridded\_series](../../api_reference/loadpull/grid/_autosummary/keysight.pwdatatools.Grid.from_gridded_series.md)
  + [Public Submodules](../../api_reference/public_submodules/index.md)
    - [calc](../../api_reference/public_submodules/calc/index.md)
      * [keysight.pwdatatools.calc.db\_to\_power](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.db_to_power.md)
      * [keysight.pwdatatools.calc.db\_to\_voltage](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.db_to_voltage.md)
      * [keysight.pwdatatools.calc.dbm\_to\_w](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.dbm_to_w.md)
      * [keysight.pwdatatools.calc.deg\_to\_rad](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.deg_to_rad.md)
      * [keysight.pwdatatools.calc.gamma\_to\_gamma](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.gamma_to_gamma.md)
      * [keysight.pwdatatools.calc.gamma\_to\_z](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.gamma_to_z.md)
      * [keysight.pwdatatools.calc.polar\_to\_rect](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.polar_to_rect.md)
      * [keysight.pwdatatools.calc.power\_to\_db](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.power_to_db.md)
      * [keysight.pwdatatools.calc.rad\_to\_deg](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.rad_to_deg.md)
      * [keysight.pwdatatools.calc.rect\_to\_polar](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.rect_to_polar.md)
      * [keysight.pwdatatools.calc.voltage\_to\_db](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.voltage_to_db.md)
      * [keysight.pwdatatools.calc.w\_to\_dbm](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.w_to_dbm.md)
      * [keysight.pwdatatools.calc.z\_to\_gamma](../../api_reference/public_submodules/calc/_autosummary/keysight.pwdatatools.calc.z_to_gamma.md)
    - [datatypes](../../api_reference/public_submodules/datatypes/index.md)
      * [keysight.pwdatatools.datatypes.Boolean](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Boolean.md)
      * [keysight.pwdatatools.datatypes.Complex64](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Complex64.md)
      * [keysight.pwdatatools.datatypes.Complex128](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Complex128.md)
      * [keysight.pwdatatools.datatypes.DataType](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.DataType.md)
      * [keysight.pwdatatools.datatypes.FillValues](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.FillValues.md)
      * [keysight.pwdatatools.datatypes.Float32](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Float32.md)
      * [keysight.pwdatatools.datatypes.Float64](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Float64.md)
      * [keysight.pwdatatools.datatypes.Int8](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int8.md)
      * [keysight.pwdatatools.datatypes.Int16](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int16.md)
      * [keysight.pwdatatools.datatypes.Int32](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int32.md)
      * [keysight.pwdatatools.datatypes.Int64](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int64.md)
      * [keysight.pwdatatools.datatypes.String](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.String.md)
      * [keysight.pwdatatools.datatypes.UInt8](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt8.md)
      * [keysight.pwdatatools.datatypes.UInt16](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt16.md)
      * [keysight.pwdatatools.datatypes.UInt32](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt32.md)
      * [keysight.pwdatatools.datatypes.UInt64](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt64.md)
      * [keysight.pwdatatools.datatypes.FillValues](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.FillValues.md)
    - [roles](../../api_reference/public_submodules/roles/index.md)
    - [viz](../../api_reference/public_submodules/viz/index.md)
      * [keysight.pwdatatools.viz.complex\_vector\_to\_str\_series](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.complex_vector_to_str_series.md)
      * [keysight.pwdatatools.viz.contourplot](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.contourplot.md)
      * [keysight.pwdatatools.viz.draw\_smith\_chart](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.draw_smith_chart.md)
      * [keysight.pwdatatools.viz.float\_vector\_to\_str\_series](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.float_vector_to_str_series.md)
      * [keysight.pwdatatools.viz.make\_contour\_levels](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.make_contour_levels.md)
      * [keysight.pwdatatools.viz.tricontourplot](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.tricontourplot.md)
      * [keysight.pwdatatools.viz.use\_keysight\_theme](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.use_keysight_theme.md)
  + [Data Types](../../api_reference/datatypes.md)
    - [Boolean](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Boolean.md)
    - [Complex64](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Complex64.md)
    - [Complex128](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Complex128.md)
    - [DataType](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.DataType.md)
    - [FillValues](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.FillValues.md)
    - [Float32](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Float32.md)
    - [Float64](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Float64.md)
    - [Int8](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int8.md)
    - [Int16](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int16.md)
    - [Int32](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int32.md)
    - [Int64](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.Int64.md)
    - [String](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.String.md)
    - [UInt8](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt8.md)
    - [UInt16](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt16.md)
    - [UInt32](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt32.md)
    - [UInt64](../../api_reference/public_submodules/datatypes/_autosummary/keysight.pwdatatools.datatypes.UInt64.md)
  + [Concatenation Functions](../../api_reference/concat/index.md)
    - [concatenate\_blocks](../../api_reference/concat/concatenate_blocks.md)
    - [concatenate\_loadpullblocks](../../api_reference/concat/concatenate_loadpullblocks.md)
    - [concatenate\_vars](../../api_reference/concat/concatenate_vars.md)
  + [Global Options](../../api_reference/global_options.md)
* [Changelog](../../changelog.md)

# Swept Gamma and Power[](#swept-gamma-and-power "Link to this heading")

This example demonstrates how to work with load pull data with swept gamma and power. It is a very common type of load pull sweep.

See also

All Python scripts and data files for the load pull examples are located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

## Perform all imports[](#perform-all-imports "Link to this heading")

First, let’s import all the necessary modules. There are many Python libraries for plotting, but this example uses matplotlib, seaborn, and `pwdatatools.viz`. The `viz` module builds off matplotlib and seaborn to provide additional functionality. Also, we need the `pwdatatools.examples.loadpull` module to create the loadpull data. This example requires pwdatatools version 0.6.0 or later.

```
>>> import itertools
>>> import os
>>> from pathlib import Path
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> from keysight import pwdatatools as pwdt
>>> from keysight.pwdatatools import viz
>>> from keysight.pwdatatools.examples import loadpull as lp_examples
```

## Create the data[](#create-the-data "Link to this heading")

Let’s generate the data that we will use. First, let’s define the unique gamma and power points. These are the independent variables (ivars). We use `itertools.product()` to compute the cartesian product, which gives us all combinations of real and imaginary gamma points.

```
>>> gamma_real_points = [0, 0.25, 0.5]
>>> gamma_imag_points = [0, 0.25, 0.5]
>>> gamma_points = []
>>> for real_point, imag_point in itertools.product(gamma_real_points, gamma_imag_points):
...     gamma_points.append(real_point + 1j * imag_point)
>>> print(gamma_points)
[0j, 0.25j, 0.5j, (0.25+0j), (0.25+0.25j), (0.25+0.5j), (0.5+0j), (0.5+0.25j), (0.5+0.5j)]
>>> power_points = [-20.0, -10, -5, 0.0]
```

Next, we define the names of the ivars and create a [`Var`](../../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") for each.

```
>>> gamma_ivarname = "GammaLoad"
>>> gamma = pwdt.Var(gamma_points, name=gamma_ivarname)
>>> power_ivarname = "PSource"
>>> power = pwdt.Var(power_points, name=power_ivarname)
```

Now that we have the ivars handled, let’s create the dependent variables (dvars). We create two dvars: gain and efficiency. We only need to define nominal curves vs. power. These nominal curves will be modified to produce different values at each gamma. Each gain or efficiency value corresponds to a power value, so the nominal curves need to be the same length as the power points (in this example, the length is 4).

```
>>> gain_name = "Gp"
>>> eff_name = "DrainEff"
>>> gain_nominal = pwdt.Var([10, 10, 9, 8], name=gain_name)
>>> eff_nominal = pwdt.Var([50, 51, 48, 46], name=eff_name)
```

## Create a LoadPullBlock[](#create-a-loadpullblock "Link to this heading")

Now that we have all the variables ready, let’s create a [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock"). LoadPullBlock is a specialized Block class that is a superset of the generic [`Block`](../../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") class and contains additional functionality for working with load pull data. We use the `make_swept_gamma_power_loadpullblock()` function, which is part of the `keysight.pwdatatools.examples.loadpull` module, to create a LoadPullBlock.

```
>>> lpblock = lp_examples.make_swept_gamma_power_loadpullblock(
...     gamma, power, gain_nominal, eff_nominal
... )
>>> print(lpblock)
LoadPullBlock(
    <'Gp', 'DrainEff', ... with 36 observations>,
    name='example',
    gamma_ivarname='GammaLoad',
    power_ivarname='PSource',
    attrs={},
)
```

## Explore the variables[](#explore-the-variables "Link to this heading")

Let’s print the names of the independent variables (ivars), the dependent variables (dvars), and the index variables (idxs).

```
>>> print(f"ivars: {lpblock.ivarnames}")
ivars: ('GammaLoad', 'PSource')
>>> print(f"dvars: {lpblock.dvarnames}")
dvars: ('Gp', 'DrainEff')
>>> print(f"idxs: {lpblock.idxnames}")
idxs: ('iGammaLoad', 'iPSource')
```

There are two idxs: one for gamma and one for power. The idxs always contain integer data, and are typically named “i” + “varname” (where “varname” is the name of the variable with which the idx is associated). The idxs help with iterating over the combinations of the ivars’ values, avoiding floating point precision issues.

We can get variables from the LoadPullBlock using the [`LoadPullBlock.__getitem__()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__getitem__.md#keysight.pwdatatools.LoadPullBlock.__getitem__ "keysight.pwdatatools.LoadPullBlock.__getitem__") method. This returns a [`Var`](../../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") object.

```
>>> print(lpblock["GammaLoad"])
Var(
    <Complex128 data with shape (36,)>,
    name='GammaLoad',
    dims=<empty Dims>,
    role='gamma',
    unit=None,
    attrs={},
)
>>> print(lpblock["PSource"])
Var(
    <Float64 data with shape (36,)>,
    name='PSource',
    dims=<empty Dims>,
    role='power',
    unit=None,
    attrs={},
)
```

Note that the gamma variable has the role of “gamma” and the power variable has the role of “power”. These roles were assigned to the variables when the LoadPullBlock was created.

Before we start plotting, let’s activate a color theme. This is an optional step that applies Keysight’s color theme to all charts created by matplotlib and seaborn.

```
>>> viz.use_keysight_theme()
```

Let’s plot gain and efficency. We use the [`LoadPullBlock.gamma_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar.md#keysight.pwdatatools.LoadPullBlock.gamma_ivar "keysight.pwdatatools.LoadPullBlock.gamma_ivar") method to get the gamma variable, converting it to polar string form. This form works well for legend labels. We use these labels to set the hue of the plot. The hue parameter will trigger seaborn to create separate lines with distinct colors for each gamma.

```
>>> fig, axs = plt.subplots(1, 2, figsize=(12, 4))
>>> gamma_label = lpblock.gamma_ivar("polar_str")
>>> axs[0].set_title("GainP vs. Power")
>>> sns.lineplot(data=lpblock, x="PSource", y="Gp", hue=gamma_label, ax=axs[0])
>>> axs[0].legend(bbox_to_anchor=(2, -0.2), title="GammaLoad", ncols=5)
>>> axs[1].set_title("Efficiency vs. Power")
>>> sns.lineplot(data=lpblock, x="PSource", y="DrainEff", ax=axs[1], hue=gamma_label, legend=False)
>>> plt.show()
```

[![../../_images/simple_gamma_power_gain_eff_plot.png](../../_images/simple_gamma_power_gain_eff_plot.png)](../../_images/simple_gamma_power_gain_eff_plot.png)

Let’s plot the gamma points on a Smith chart using the [`LoadPullBlock.gamma_ivar_scatterplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot.md#keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot "keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot") method.

```
>>> fig, ax = plt.subplots()
>>> ax.set_title("Gamma Points")
>>> viz.draw_smith_chart(ax)
>>> lpblock.gamma_ivar_scatterplot(ax=ax)
>>> plt.show()
```

[![../../_images/gamma_points_plot.png](../../_images/gamma_points_plot.png)](../../_images/gamma_points_plot.png)

## Calculate gain compression[](#calculate-gain-compression "Link to this heading")

Let’s calculate gain compression points using the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp"). This method returns a new LoadPullBlock with the power dependency removed (since the data now only has a single power for each gamma). The default behavior is to add the gain compression as an outer independent variable (outer ivar) and to add a new column and integer index to the DataFrame corresponding to values of gain compression. By default, extrapolation is not performed. This means that if the requested gain compression value is not within the limits of the data, then the `fill_value` is used to fill in the data point (which defaults to `numpy.nan`. Here, we set the `extrap` argument to `True` to allow extrapolation, which is needed for the 3dB gcomp value.

```
>>> gcomp_values = [1.0, 2.0, 3.0]
>>> lpblock_at_gcomp = lpblock.at_gcomp(gcomp_values, "Gp", extrap=True)
>>> print(lpblock_at_gcomp)
LoadPullBlock(
    <'PSource', 'Gp', 'DrainEff', ... with 27 observations>,
    name='example',
    gamma_ivarname='GammaLoad',
    outer_ivarnames=('Gp_comp',),
    outer_idxnames=('iGp_comp',),
    attrs={},
)
```

Now, let’s plot the gain compression points along the gain and efficiency curves.

```
>>> gcomp_values_str = ", ".join([str(x) for x in gcomp_values])
>>> fig, axs = plt.subplots(1, 2, figsize=(12, 4))
>>> fig.suptitle(
...     f"GainP and Efficiency with Points at gcomp Values of {gcomp_values_str}",
...     fontsize=16,
... )
>>> gamma_label = lpblock.gamma_ivar("polar_str")
>>> gamma_label_at_gcomp = lpblock_at_gcomp.gamma_ivar("polar_str")
>>> sns.lineplot(
...     data=lpblock,
...     x="PSource",
...     y="Gp",
...     ax=axs[0],
...     hue=gamma_label,
... )
>>> sns.scatterplot(
...     data=lpblock_at_gcomp,
...     x="PSource",
...     y="Gp",
...     ax=axs[0],
...     hue=gamma_label_at_gcomp,
...     legend=False,
... )
>>> sns.lineplot(
...     data=lpblock,
...     x="PSource",
...     y="DrainEff",
...     ax=axs[1],
...     hue=gamma_label,
...     legend=False,
... )
>>> sns.scatterplot(
...    data=lpblock_at_gcomp,
...     x="PSource",
...     y="DrainEff",
...     ax=axs[1],
...     hue=lpblock_at_gcomp.gamma_ivar("polar_str"),
...     legend=False,
... )
>>> axs[0].legend(bbox_to_anchor=(2, -0.2), title="GammaLoad", ncols=5)
>>> plt.show()
```

[![../../_images/simple_gamma_power_gcomp_plot.png](../../_images/simple_gamma_power_gcomp_plot.png)](../../_images/simple_gamma_power_gcomp_plot.png)

You can see from the plots that the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method extrapolated past the last gain data point to find the gain compression point. The [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method automatically interpolates as needed.

## Calculate responses at specified power levels[](#calculate-responses-at-specified-power-levels "Link to this heading")

The LoadPullBlock class has a method called [`LoadPullBlock.at_power()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md#keysight.pwdatatools.LoadPullBlock.at_power "keysight.pwdatatools.LoadPullBlock.at_power") that can be used to calculate the responses at specific power level(s). This method is similar to the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method, but instead of calculating the responses at gain compression level(s), it calculates the responses at specific power level(s). The power variable that you use to specify the power levels can be **any variable** in the LoadPullBlock; it doesn’t have to be the swept power independent variable. So, using this method, you could calculate all responses at specified PLoad values. The default behavior is to assign whichever power col is being used to the role of power\_ivar, and to add an integer index to the DataFrame corresponding to values of power.

Let’s calculate the responses at a few power levels. We use the [`LoadPullBlock.at_power()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md#keysight.pwdatatools.LoadPullBlock.at_power "keysight.pwdatatools.LoadPullBlock.at_power") method to calculate the responses at -18 dBm, -10 dBm, and -2 dBm. In order to obtain the data at -18 dBm, interpolation must be used. To get the response values at -2 dBm, extrapolation must be used. For the responses at -10 dBm, the data is available in the LoadPullBlock, so no interpolation or extrapolation is needed.

```
>>> power_values = [-18, -10.0, 2]
>>> power_col = "PSource"
>>> lpblock_at_power = lpblock.at_power(
...      power_values, power_col, extrap=True, interp_method="linear", extrap_method="linear"
... )
>>> print(lpblock_at_power)
LoadPullBlock(
    <'Gp', 'DrainEff', ... with 27 observations>,
    name='example',
    gamma_ivarname='GammaLoad',
    power_ivarname='PSource',
    attrs={},
)
```

Plotting the responses calculated at different power levels is similar to plotting at specified gain compression levels. We can do it with minor tweaks to the code we used previously. The code is not shown here, but the resulting plots are shown below.

See also

You can find all the code here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

[![../../_images/simple_gamma_power_at_power_plot.png](../../_images/simple_gamma_power_at_power_plot.png)](../../_images/simple_gamma_power_at_power_plot.png)

## Create contour plots[](#create-contour-plots "Link to this heading")

Let’s plot gain and efficiency contours. We can utilize the [`LoadPullBlock.contourplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md#keysight.pwdatatools.LoadPullBlock.contourplot "keysight.pwdatatools.LoadPullBlock.contourplot") method to create contour plots. It provides additional conveniences beyond matplotlib’s `Axes.contour()` method, but if you prefer, you could use that method instead. Generally, you can pick either rectangular or Smith charts for these types of plots. So, just for demonstration purposes, the gain contours are plotted on Smith charts and the efficiency contours are plotted on rectangular charts. We are plotting contours at each gain compression level from the `lpblock_at_gcomp` object, but we could have just as easily plotted contours at each power level from the `lpblock_at_power` object. Note how `lpblock_at_gcomp` is filtered during each iteration of the for-loop with the [`LoadPullBlock.keep_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md#keysight.pwdatatools.LoadPullBlock.keep_observations "keysight.pwdatatools.LoadPullBlock.keep_observations") method in order to create a new LoadPullBlock containing only the data for a single gain compression level. Getting rid of the swept outer ivar Gp\_comp allows the [`LoadPullBlock.contourplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md#keysight.pwdatatools.LoadPullBlock.contourplot "keysight.pwdatatools.LoadPullBlock.contourplot") method to work correctly.

```
>>> fig_gain, axs_gain = plt.subplots(1, len(gcomp_values), figsize=(12, 4))
>>> fig_gain.suptitle("GainP Contours at Different Compression Levels", fontsize=20)
>>> fig_eff, axs_eff = plt.subplots(1, len(gcomp_values), figsize=(12, 4))
>>> fig_eff.suptitle(
...     "Efficiency Contours at Different GainP Compression Levels", fontsize=20
... )
>>> for i, gcomp_value in enumerate(gcomp_values):
...     viz.draw_smith_chart(axs_gain[i])
...     lpblock_at_single_gcomp = lpblock_at_gcomp.keep_observations(
...         lpblock_at_gcomp["iGp_comp"] == i
...     )
...     cs_gain = lpblock_at_single_gcomp.contourplot(
...         "Gp", ax=axs_gain[i], levels=5, colors="red"
...     )
...     axs_gain[i].clabel(cs_gain, fmt="%1.1f")
...     axs_gain[i].set_title(f"Gp_comp = {gcomp_value}")
...     fig_gain.tight_layout()
...     cs_eff = lpblock_at_single_gcomp.contourplot(
...         "DrainEff", ax=axs_eff[i], colors="blue"
...     )
...     axs_eff[i].clabel(cs_eff, fontsize=11)
...     axs_eff[i].set_title(f"Gp_comp = {gcomp_value}")
...     fig_eff.tight_layout()
>>> plt.show()
```

[![../../_images/simple_gamma_power_gain_contours_vs_gcomp.png](../../_images/simple_gamma_power_gain_contours_vs_gcomp.png)](../../_images/simple_gamma_power_gain_contours_vs_gcomp.png)
[![../../_images/simple_gamma_power_eff_contours_vs_gcomp.png](../../_images/simple_gamma_power_eff_contours_vs_gcomp.png)](../../_images/simple_gamma_power_eff_contours_vs_gcomp.png)

## Regularize power[](#regularize-power "Link to this heading")

It is common for data to contain irregular power sweeps, which means that the swept power values are not exactly the same at each gamma. There are certain scenarios where we want to ensure that the swept power is regular across all gamma values. The [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method can be used to regularize irregular power sweeps. Additionally, the [`LoadPullBlock.has_regular_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar.md#keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar "keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar") method is useful to check if the power sweeps are regular. Let’s check if the power sweeps in our example LoadPullBlocks are regular.

```
>>> print(f"lpblock has regular power: {lpblock.has_regular_power_ivar()}")
lpblock has regular power: True
>>> print(f"lpblock_at_power has regular power: {lpblock_at_power.has_regular_power_ivar()}")
lpblock_at_power has regular power: True
>>> print(f"lpblock_at_gcomp has regular power: {lpblock_at_gcomp.has_regular_power_ivar()}")
<raises ValueError because lpblock_at_gcomp does not have swept power>
```

So, our original [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object has regular power sweeps, as does our `lpblock_at_power` object. But the `lpblock_at_gcomp` object cannot be checked because it no longer has a power sweep. Let’s create a new LoadPullBlock by creating a LoadPullBlock with irregular power sweeps. Let’s drop two observations of data using the [`LoadPullBlock.drop_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_observations.md#keysight.pwdatatools.LoadPullBlock.drop_observations "keysight.pwdatatools.LoadPullBlock.drop_observations") method.

```
>>> gamma_idx = lpblock["iGammaLoad"]
>>> power_idx = lpblock["iPSource"]
>>> lpblock_irreg = lpblock.drop_observations(
...     (gamma_idx == 0) & (power_idx == 2) | (gamma_idx == 8) & (power_idx == 3),
... )
>>> print(lpblock_irreg.has_regular_power_ivar())
False
```

Let’s plot gamma vs power to help visualize regular and irregular power sweeps. We see there are two missing points in the irregular power sweeps.

```
>>> fig, axs = plt.subplots(1, 3, sharey=True, figsize=(7, 3))
>>> fig.suptitle("Gamma vs Power", fontsize=14)
>>> axs[0].set_title("lpblock (regular)", fontsize=10)
>>> axs[1].set_title("lpblock_at_power (regular)", fontsize=10)
>>> axs[2].set_title("lpblock_irreg (irregular)", fontsize=10)
>>> gamma_label = lpblock.gamma_ivar("polar_str")
>>> gamma_label_at_power = lpblock_at_power.gamma_ivar("polar_str")
>>> gamma_label_irreg = lpblock_irreg.gamma_ivar("polar_str")
>>> sns.scatterplot(data=lpblock, x="PSource", y=gamma_label, ax=axs[0])
>>> sns.scatterplot(data=lpblock_at_power, x="PSource", y=gamma_label_at_power, ax=axs[1])
>>> sns.scatterplot(data=lpblock_irreg, x="PSource", y=gamma_label_irreg, ax=axs[2])
>>> fig.tight_layout()
>>> plt.show()
```

[![../../_images/simple_gamma_power_gamma_vs_power_reg_vs_irreg.png](../../_images/simple_gamma_power_gamma_vs_power_reg_vs_irreg.png)](../../_images/simple_gamma_power_gamma_vs_power_reg_vs_irreg.png)

Now, let’s regularize the power sweeps in `lpblock_irreg` by calling the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method. This method will create a new [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") instance with the regularized power sweeps, leaving the original [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object unchanged.

Note

This is how most of the LoadPullBlock methods work; they return a new instance of LoadPullBlock. You can choose to store the new instance in a new variable, or you can store it in the same variable. The latter is useful if don’t you need to keep the original LoadPullBlock object.

We explicitly define the power points that we want to use for the regular power sweeps. This is optional because the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method is able to automatically determine power points to use. In this simple example, we can easily specify the power points, which helps reduce the amount of interpolation we need to perform. However, usually real measured load pull data will contain enough power points at each gamma to make this unnecessary. We are also explicitly specifying the interpolation and extrapolation methods as “linear”. The defaults are “cubic” for both, which usually works well. However, our simple data doesn’t contain enough power points at each gamma to use “cubic”. We are also specifying that we want to extrapolate the power sweeps. The default value for `extrap` is `False`.

```
>>> lpblock_reg = lpblock_irreg.regularize_power_ivar(
...     points=[-20, -10, -5, 0],
...     interp_method="linear",
...     extrap_method="linear",
...     extrap=True,
...)
>>> print(f"lpblock_reg has regular power: {lpblock_reg.has_regular_power_ivar()}")
lpblock_reg has regular power: True
```

Now let’s compare the irregular and regularized gain and efficiency plots. The code to generate the below plots is not shown here, but it is available on the Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

[![../../_images/simple_gamma_power_gain_vs_power_irreg_vs_reg_plot.png](../../_images/simple_gamma_power_gain_vs_power_irreg_vs_reg_plot.png)](../../_images/simple_gamma_power_gain_vs_power_irreg_vs_reg_plot.png)
[![../../_images/simple_gamma_power_eff_vs_power_irreg_vs_reg_plot.png](../../_images/simple_gamma_power_eff_vs_power_irreg_vs_reg_plot.png)](../../_images/simple_gamma_power_eff_vs_power_irreg_vs_reg_plot.png)

Examining the irregular plots reveals two missing points in the gain and efficiency plots (where gamma is 0 < 0 and 0.707 < 45). In the regularized plots, one of the missing points is filled by interpolation, and the other by extrapolation.

## Grid data[](#grid-data "Link to this heading")

If you do not understand the concept of “gridded” load pull data, please read [this section](../../howto/work_with_loadpull_data.md#what-is-gridded-load-pull-data) before proceeding.

Let’s check our regularized [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object to see if it is gridded.

```
>>> print(f"lpblock_reg is gridded: {lpblock_reg.is_gridded()}")
lpblock_reg is gridded: True
```

We can also get all the grid info. The [`LoadPullBlock.get_grid()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_grid.md#keysight.pwdatatools.LoadPullBlock.get_grid "keysight.pwdatatools.LoadPullBlock.get_grid") method returns a [`Grid`](../../api_reference/loadpull/grid/index.md#keysight.pwdatatools.Grid "keysight.pwdatatools.Grid") object (or `None` if the LoadPullBlock is not gridded). The [`Grid`](../../api_reference/loadpull/grid/index.md#keysight.pwdatatools.Grid "keysight.pwdatatools.Grid") object contains the coordinate system (‘rect’ or ‘polar’), the extents of the grid, and the number of x and y points. The `x` and `y` coordinates are real/imaginary for a rectangular grid, and magnitude/phase for a polar grid.

```
>>> grid = lpblock_reg.get_grid()
>>> print(f"lpblock_reg's grid:\n{grid}")
lpblock_reg's grid:
Grid(
    coord_system='rect',
    extents=<xmin=0.0, xmax=0.5, ymin=0.0, ymax=0.5>,
    npointsx=3,
    npointsy=3
)
```

What about our irregular [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object?

```
>>> print(f"lpblock_irreg is gridded: {lpblock_irreg.is_gridded()}")
lpblock_irreg is gridded: False
>>> print(f"lpblock_irreg's grid: {lpblock_irreg.get_grid()}")
lpblock_irreg's grid: None
```

No, the `lpblock_irreg` object is not gridded because its power sweep is not regular. Notice that the [`LoadPullBlock.get_grid()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_grid.md#keysight.pwdatatools.LoadPullBlock.get_grid "keysight.pwdatatools.LoadPullBlock.get_grid") method returns `None` if a LoadPullBlock is not gridded.

Another requirement to be gridded is having the same number of gamma or impedance y points for each x point. To demonstrate, let’s create a new LoadPullBlock that violates this requirement. We can do this by using the [`LoadPullBlock.drop_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_observations.md#keysight.pwdatatools.LoadPullBlock.drop_observations "keysight.pwdatatools.LoadPullBlock.drop_observations") method to drop one of the gamma points from the original `lpblock` object. This method returns a new LoadPullBlock instance.

```
>>> lpblock_ungridded = lpblock.drop_observations(lpblock["iGammaLoad"] == 0)
>>> print(f"lpblock_ungridded's grid: {lpblock_ungridded.get_grid()}")
lpblock_ungridded's grid: None
```

Now, let’s regrid the data so that the gamma points are once again considered “gridded”. The [`LoadPullBlock.grid_data()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md#keysight.pwdatatools.LoadPullBlock.grid_data "keysight.pwdatatools.LoadPullBlock.grid_data") method is able to grid the data onto a rectangular or polar 2D grid. This method creates a new [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") instance with the gridded data.

```
>>> lpblock_gridded = lpblock_ungridded.grid_data("rect")
>>> print(f"lpblock_gridded's grid:\n{lpblock_gridded.get_grid()}")
lpblock_gridded's grid:
Grid(
    coord_system='rect',
    extents=<xmin=0.055556, xmax=0.444444, ymin=0.055556, ymax=0.444444>,
    npointsx=8,
    npointsy=8
)
```

Note how the gridded data has 64 gamma points (8x8). The original data had only 8 gamma points (we had 9 gamma points, and then removed one gamma point to make it ungridded). The [`LoadPullBlock.grid_data()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md#keysight.pwdatatools.LoadPullBlock.grid_data "keysight.pwdatatools.LoadPullBlock.grid_data") method defaults to calculating a 10x10 grid and then dropping the outermost grid points along the edges (resulting in an 8x8 grid). Dropping the points along the grid’s edges is the default behavior because interpolation doesn’t work well there. If you decide you want to keep the outermost grid points, you can set the `drop_edges` argument to `False`. You can also control the number of x and y grid points with the `npointsx` and `npointsy` parameters.

We can plot gridded and ungridded gamma in order to help us visualize the changes.

```
>>> fig, ax = plt.subplots()
>>> ax.set_title("Gamma Points")
>>> viz.draw_smith_chart(ax)
>>> lpblock_gridded.gamma_ivar_scatterplot(ax=ax, color="red", label="gridded")
>>> lpblock_ungridded.gamma_ivar_scatterplot(ax=ax, color="blue", label="ungridded")
>>> plt.show()
```

[![../../_images/gamma_points_gridded_and_ungridded_plot.png](../../_images/gamma_points_gridded_and_ungridded_plot.png)](../../_images/gamma_points_gridded_and_ungridded_plot.png)

Note how the final grid covers a smaller area of the Smith Chart than the original data. Again, this is because the [`LoadPullBlock.grid_data()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md#keysight.pwdatatools.LoadPullBlock.grid_data "keysight.pwdatatools.LoadPullBlock.grid_data") method is dropping the outermost grid points along the edges because interpolation doesn’t work well at the edges of the grid. If you want the final grid edges to be closer to the original data’s extents, it’s recommended to increase the `npointsx` and `npointsy` parameter values, rather than setting the `drop_edges` parameter to `False`. The gridded data at the edges is usually too unreliable.

Finally, let’s plot the gain curves for the gridded data. The code is not shown here, but it’s almost identical to the code we used previously to plot gain and efficency vs. power.

[![../../_images/simple_gamma_power_gain_eff_vs_power_gridded_plot.png](../../_images/simple_gamma_power_gain_eff_vs_power_gridded_plot.png)](../../_images/simple_gamma_power_gain_eff_vs_power_gridded_plot.png)

## Send data to ADS[](#send-data-to-ads "Link to this heading")

Let’s demonstrate how to get data into PathWave Advanced Design System (ADS). We use the [`LoadPullBlock.to_adscontourblock()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_adscontourblock.md#keysight.pwdatatools.LoadPullBlock.to_adscontourblock "keysight.pwdatatools.LoadPullBlock.to_adscontourblock") method to do this. This method returns an `ADSContourBlock` object, which is a specialized type of Block class dedicated to arranging data in a way that is friendly to ADS contour plotting. We are writing several datasets to a workspace’s data folder `WRK_DATA_FOLDER`, whose definition exists in the example script but is not shown here.

```
>>> adsblock0 = lpblock_gridded.to_adscontourblock()
>>> adsblock0.to_file(WRK_DATA_FOLDER / "gamma_power_sweep.ds", dst_mode="w")
>>> adsblock1 = lpblock_at_gcomp.to_adscontourblock()
>>> adsblock1.to_file(WRK_DATA_FOLDER / "gamma_power_sweep_at_gcomp.ds", dst_mode="w")
>>> adsblock2 = lpblock_at_power.to_adscontourblock()
>>> adsblock2.to_file(WRK_DATA_FOLDER / "gamma_power_sweep_at_power.ds", dst_mode="w")
```

You can also directly write out a LoadPullBlock to an ADS dataset.

```
>>> lpblock_gridded.to_file(WRK_DATA_FOLDER / "gamma_power_sweep_block.ds", dst_mode="w")
```

Important

If you get a PermissionError when writing an ADS dataset, it is likely because the ADS Data Display window is open and accessing the dataset file you are trying to write. If this happens, you must close the ADS Data Display window and try running your script again.

See also

There is an accompanying ADS workspace that shows how to plot contours in ADS Data Display using this dataset. The workspace is on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools).

On this page

[Previous

Swept Gamma](swept_gamma_example.md)
[Next

Swept Frequency, Gamma, and Power](swept_freq_gamma_power_example.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top