<!-- 来源: examples\loadpull\focus_lpcwave.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-pwdatatools](../../index.md)
* [Examples](../index.md)
* [Load Pull Examples](index.md)
* Focus lpcwave file

0.11.0

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../_sources/examples/loadpull/focus_lpcwave.rst.txt)

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
    - [Swept Gamma and Power](swept_gamma_power_example.md)
    - [Swept Frequency, Gamma, and Power](swept_freq_gamma_power_example.md)
    - Focus lpcwave file
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

# Focus lpcwave file[](#focus-lpcwave-file "Link to this heading")

In this example, we read a Focus lpcwave file that contains swept gamma and power. This file is an A/B Wave file. Several variables are automatically derived from the A and B waves when the file is read into a LoadPullBlock. Then, we manipulate the data using various methods available in the [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") class. If you haven’t reviewed [Simple Examples](index.md#simple-load-pull-examples) yet, you should do so before continuing.

See also

All Python scripts and data files for the load pull examples are located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

## Perform all imports[](#perform-all-imports "Link to this heading")

First, let’s import all the necessary modules. There are many Python libraries for plotting, but this example uses matplotlib, seaborn, and `pwdatatools.viz`. The `viz` module builds off matplotlib and seaborn to provide additional functionality. Also, we need the `pwdatatools.examples.loadpull` module to create the loadpull data. This example requires pwdatatools version 0.6.0 or later.

```
>>> import os
>>> from pathlib import Path
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> import pandas as pd
>>> import seaborn as sns
>>> from keysight import pwdatatools as pwdt
>>> from keysight.pwdatatools import viz
```

## Read the file[](#read-the-file "Link to this heading")

```
>>> lpblock = pwdt.read_file_as_loadpullblock(input_filepath)
```

Let’s print the [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object to see what it contains:

```
>>> print(lpblock)
LoadPullBlock(
    <'Vin', 'Vout', 'Iout', 'PinDel', 'PLoad', 'GainT', 'GainP', 'PAE', ... with 482 observations>,
    name='loadpull_powersweep_2',
    gamma_ivarname='GammaLoad_F1',
    power_ivarname='PinAvail',
    attrs={'Measurement_Type': ..., 'Sweep_Type': ..., 'Date': ..., 'Re ...},
)
```

We can see some (but not all) of the variable names, including the swept gamma and power independent variable names that are explicitly shown. Also note that the name of the LoadPullBlock is the name of the file (minus the file extension).

## Explore the data[](#explore-the-data "Link to this heading")

We can view all the variable names with the [`LoadPullBlock.varnames`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.varnames.md#keysight.pwdatatools.LoadPullBlock.varnames "keysight.pwdatatools.LoadPullBlock.varnames") attribute.

```
>>> print(lpblock.varnames)
('iGammaLoad_F1', 'iPinAvail', 'PinAvail', 'GammaLoad_F1', 'Vin', 'Vout', 'Iout', 'PinDel', 'PLoad', 'GainT', 'GainP', 'PAE', 'PSource', 'a1_F1', 'b1_F1', 'a2_F1', 'b2_F1', 'a1_F2', 'b1_F2', 'a2_F2', 'b2_F2', 'a1_F3', 'b1_F3', 'a2_F3', 'b2_F3', 'ZrefSource', 'ZrefLoad', 'GammaSource_F1', 'GammaSource_F2', 'GammaSource_F3', 'F1', 'F2', 'F3', 'GammaIn_F1', 'GammaIn_F2', 'GammaLoad_F2', 'GammaIn_F3', 'GammaLoad_F3', 'AMPM', 'DrainEff')
```

There are a bunch of variables in the LoadPullBlock. The variables that start with “i” are the index variables (iGammaLoad\_F1 and iPinAvail). The variables that start with “a” and “b” are A and B power waves (A waves are incident, B waves are reflected). The variables that start with “F” are the frequencies. In this file, F1 is the fundamental frequency, F2 is the second harmonic, and F3 is the third harmonic. However, in general, the frequencies do not necessarily have to be harmonically related. Note that some variables have suffixes like “\_F1”, “\_F2”, and “\_F3”. This means that the variable was measured at a particular frequency. However, some other variables like PLoad, PAE, GainT, GainP, and others are also measured at a particular frequency (F1). But since these variables only have an F1 component, the suffix is omitted. The voltages and currents (Vin, Vout, Iin, and Iout) are measured at DC.

## Reduce number of variables[](#reduce-number-of-variables "Link to this heading")

It is usually a good idea to exclude or remove variables that you will not need. This will speed up data processing tasks and make the DataFrame easier to view. We can easily drop variables using the `LoadpullBlock.drop_vars()` method, or conversely, we can keep only the variables that we want using the `LoadpullBlock.keep_vars()` method. In this example, we keep only a small handful of variables.

```
>>> lpblock = lpblock.keep_vars(["PLoad", "GainP", "DrainEff", "AMPM"])
>>> print(lpblock.varnames)
('iGammaLoad_F1', 'iPinAvail', 'PinAvail', 'GammaLoad_F1', 'PLoad', 'GainP', 'ZrefLoad', 'AMPM', 'DrainEff')
```

Note that the index variables, ZrefLoad, and the swept independent variables (ivars) are still present. By default, these crucial variables are kept by the [`LoadPullBlock.keep_vars()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_vars.md#keysight.pwdatatools.LoadPullBlock.keep_vars "keysight.pwdatatools.LoadPullBlock.keep_vars") method, even when not explicitly listed as variables to keep.

It’s also possible to modify which variables are derived when reading Wave data load pull files. This is done by setting the global option `options.reading.format_specific.loadpull.derived_vars` as shown below. This is useful if you want to keep the LoadPullBlock’s data as small as possible.

```
>>> derived_vars = pwdt.options.reading.format_specific.loadpull.derived_vars
>>> print(derived_vars)
FrozenRolesSet({'power.delivered.load', 'power.delivered.input', 'efficiency.drain', 'efficiency.power-added', 'power.available.source', 'gamma.load', 'gain.power', 'gamma.input', 'power.available.input', 'distortion.ampm'})
```

We can’t directly modify the set of roles, because it’s frozen. Instead, we create a new set of roles and assign it to the global option.

```
>>> new_derived_vars = set(derived_vars)
>>> new_derived_vars.remove("efficiency.power-added")
>>> pwdt.options.reading.format_specific.loadpull.derived_vars = new_derived_vars
```

Now, when we read the load pull datafile, the “efficiency.power-added” variable will not be derived.

```
>>> lpblock_alt = pwdt.LoadPullBlock.from_file(input_filepath)
```

## Renaming variables[](#renaming-variables "Link to this heading")

We can rename variables using the [`LoadPullBlock.rename_vars()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.rename_vars.md#keysight.pwdatatools.LoadPullBlock.rename_vars "keysight.pwdatatools.LoadPullBlock.rename_vars") method. Below, we rename the “GainP” variable to “Gp”.

```
>>> lpblock = lpblock.rename_vars({"GainP": "Gp"})
>>> print(lpblock.varnames)
('iGammaLoad_F1', 'iPinAvail', 'PinAvail', 'GammaLoad_F1', 'PLoad', 'Gp', 'ZrefLoad', 'AMPM', 'DrainEff')
```

## Reduce number of data points[](#reduce-number-of-data-points "Link to this heading")

Many times, loadpull data can include data that you don’t want to include in your analysis. For example, there may be bad data points that distort contours. For convenience, the [`LoadPullBlock.keep_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md#keysight.pwdatatools.LoadPullBlock.keep_observations "keysight.pwdatatools.LoadPullBlock.keep_observations") and [`LoadPullBlock.drop_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_observations.md#keysight.pwdatatools.LoadPullBlock.drop_observations "keysight.pwdatatools.LoadPullBlock.drop_observations") methods are provided. To use either method, we provide a boolean array that is the same length as the number of observations in the LoadPullBlock’s data. For the [`LoadPullBlock.keep_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md#keysight.pwdatatools.LoadPullBlock.keep_observations "keysight.pwdatatools.LoadPullBlock.keep_observations") method, the boolean array should be True for the observations to keep and False for the observations to drop. One way to do this is to use a boolean array from a comparison of a variable to a single value, as shown below.

```
>>> lpblock_filtered = lpblock.keep_observations(lpblock["PLoad"] > 34)
```

Notice the difference in observations count for the two LoadPullBlock instances below. If we didn’t need to keep the unfiltered data, we could’ve assigned the output of the [`LoadPullBlock.keep_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md#keysight.pwdatatools.LoadPullBlock.keep_observations "keysight.pwdatatools.LoadPullBlock.keep_observations") method to the original lpblock variable.

```
>>> print(lpblock.count_observations())
482
>>> print(lpblock_filtered.count_observations())
447
```

Note

The number of observations in the LoadPullBlock’s data is derived from the length of the ndarrays in their first dimension, which is axis 0. This also corresponds to the number of rows if the data is converted to a DataFrame.

## Examine the gamma ivar[](#examine-the-gamma-ivar "Link to this heading")

Let’s take a look at the first few data values of the gamma ivar, which in this dataset is named “GammaLoad\_F1”.

```
>>> print(lpblock['GammaLoad_F1'].to_numpy_ndarray()[0:10])
[-0.59950543-0.0571924j  -0.59945139-0.05724519j -0.59944071-0.05696654j
 -0.59948777-0.05712827j -0.59944238-0.05717805j -0.5993984 -0.05707937j
 -0.59945897-0.05701205j -0.59934044-0.05703576j -0.59934251-0.05693113j
 -0.59926347-0.05688538j]
```

We can see that the real and imaginary parts of gamma can vary slightly, even for the same “gamma point” that corresponds to a single iGammaLoad\_F1 value. This is one of the reasons why we use an integer index for the gamma ivar instead of indexing using the gamma values themselves. The same is true of the other ivars, such as the PinAvail ivar. We use an integer index to avoid any issues related to precision.

Let’s plot the gamma points on a Smith Chart. If we plot all of the gamma values, it would work just fine, but we may end up plotting multiple gammas that are really close to each other. So, before we plot the gamma ivar, let’s select a subset of the data at the first power value at each gamma index value.

```
>>> lpblock_subset = lpblock.keep_observations(lpblock["iPinAvail"] == 0)
```

The LoadPullBlock has a method [`LoadPullBlock.gamma_ivar_scatterplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot.md#keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot "keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot") that can be used to plot the gamma ivar on a rectangular or Smith chart. We must first import matplotlib so that we can create a matplotlib Axes object and also invoke `matplotlib.pyplot.show()` to display the plot. We will use the [`viz.draw_smith_chart()`](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.draw_smith_chart.md#keysight.pwdatatools.viz.draw_smith_chart "keysight.pwdatatools.viz.draw_smith_chart") function from the `pwdatatools.viz` module to create a Smith chart. All keyword arguments to the `gamma_ivar_scatterplot()` method are passed to the `seaborn.scatterplot()` function. See the [seaborn.scatterplot documentation](https://seaborn.pydata.org/generated/seaborn.scatterplot.html) for more information on the available keyword parameters.

```
>>> import matplotlib.pyplot as plt
>>> from keysight.pwdatatools import viz
>>> fig, ax = plt.subplots()
>>> viz.draw_smith_chart(ax)
>>> ax.set_title("Gamma Points")
>>> lpblock_subset.gamma_ivar_scatterplot(ax=ax)
>>> plt.show()
```

[![../../_images/realistic_gamma_points_ungridded_smithchart.png](../../_images/realistic_gamma_points_ungridded_smithchart.png)](../../_images/realistic_gamma_points_ungridded_smithchart.png)

## Select data at a specific power value[](#select-data-at-a-specific-power-value "Link to this heading")

When we plotted the ungridded gamma points above, we selected only the data at the first power value. In practice, the power values may be irregular at each gamma, and so the first power value may not be the same at each gamma. Furthermore, we may want to select data at a specific power value that was not explicitly measured. This requires interpolation and/or extrapolation. We can use the [`LoadPullBlock.at_power()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md#keysight.pwdatatools.LoadPullBlock.at_power "keysight.pwdatatools.LoadPullBlock.at_power") method to select data at specific power value(s). Here, we select one power value (40), but we could also select more than one and input them as a list. We can choose any variable to use for the `power_varname` argument. In this case, we use “PLoad”. Below, we convert the resulting LoadPullBlock’s data to a pandas DataFrame and print the first and last 5 observations of the data.

```
>>> lpblock_at_power = lpblock.at_power(40, "PLoad", power_idxname=None)
>>> dataframe_at_power = lpblock_at_power.to_pandas_dataframe(index="idxs")
>>> print(dataframe_at_power.head())
                     GammaLoad_F1  PLoad   PinAvail         Gp       AMPM   DrainEff   ZrefLoad
iGammaLoad_F1
0             -0.599505-0.057192j   40.0  21.811387  18.337554 -38.916208  29.971846  50.0+0.0j
1             -0.583814-0.159089j   40.0  22.114087  18.079940 -30.199213  28.553411  50.0+0.0j
2             -0.551828-0.256465j   40.0  22.791501  17.464683 -24.248914  26.393401  50.0+0.0j
3             -0.502717-0.343823j   40.0  23.658831  16.670029 -20.936101  29.347165  50.0+0.0j
4             -0.557693-0.380377j   40.0  23.837073  16.502647 -16.757597  23.511156  50.0+0.0j
>>> print(dataframe_at_power.tail())
                     GammaLoad_F1  PLoad   PinAvail         Gp       AMPM   DrainEff   ZrefLoad
iGammaLoad_F1
28            -0.865695-0.394581j   40.0  27.803563  12.651950  -1.825245  13.181057  50.0+0.0j
29            -0.896517-0.318402j   40.0  26.773933  13.605971  -3.776363  14.022184  50.0+0.0j
30            -0.920679-0.240904j   40.0  25.473713  14.826748  -8.160523  15.819262  50.0+0.0j
31            -0.936829-0.162784j   40.0  23.757357  16.441197 -19.359945  19.037109  50.0+0.0j
32            -0.947198-0.081638j   40.0  25.117598  14.927344 -66.137104  23.932672  50.0+0.0j
```

Note that the returned LoadPullBlock has the same number of gamma points as the original LoadPullBlock (33). However, the PLoad values are all the same and there is no longer a power ivar or index (iGammaLoad\_F1 is the only index). We can easily check a LoadPullBlock’s sweep information using the [`LoadPullBlock.get_sweep()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_sweep.md#keysight.pwdatatools.LoadPullBlock.get_sweep "keysight.pwdatatools.LoadPullBlock.get_sweep") method. The returned [`LoadPullSweep`](../../api_reference/loadpull/loadpullsweep/index.md#keysight.pwdatatools.LoadPullSweep "keysight.pwdatatools.LoadPullSweep") object contains all the ivarnames and idxnames of the LoadPullBlock. Note that the power sweep has been removed and therefore `power_ivarname` and `power_idxname` are now None. This is because we set the `power_idxname` argument to `None` in the call to the [`LoadPullBlock.at_power()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md#keysight.pwdatatools.LoadPullBlock.at_power "keysight.pwdatatools.LoadPullBlock.at_power") method.

```
>>> print(lpblock_at_power.get_sweep())
LoadPullSweep(
    outer_ivarnames=(),
    outer_idxnames=(),
    gamma_ivarname='GammaLoad_F1',
    gamma_idxname='iGammaLoad_F1',
    power_ivarname=None,
    power_idxname=None,
)
```

## Calculate gain compression points[](#calculate-gain-compression-points "Link to this heading")

The LoadPullBlock class has an [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method that can calculate all responses at specified gain compression point(s) and return a new LoadPullBlock. The method interpolates and/or extrapolates as needed. You need to specify the gain compression value(s) and the name of the gain variable to use. In this case, we will use “Gp” and calculate at a single gain compression value. However, it is possible to provide a list of more than one compression value to the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method. Note below that `extrap=True`. The default is `extrap=False`, but we need to extrapolate to calculate the gain compression at some gamma points.

```
>>> gcomp_value = 1
>>> lpblock_at_gcomp = lpblock.at_gcomp(gcomp_value, "Gp", gcomp_idxname=None, extrap=True)
```

Viewing the `sweep` attribute of `lpblock_at_gcomp`, we see there is no longer a power sweep defined since we calculated the data at one power level per gamma. Therefore, `power_ivarname` and `power_idxname` are now None. The gamma sweep is still defined since we calculated the gain compression at each gamma point. And because we set `gcomp_idxname` to `None` in the call to the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method, the gain compression does not become a new outer ivar.

```
>>> print(lpblock_at_gcomp.get_sweep())
LoadPullSweep(
    outer_ivarnames=(),
    outer_idxnames=(),
    gamma_ivarname='GammaLoad_F1',
    gamma_idxname='iGammaLoad_F1',
    power_ivarname=None,
    power_idxname=None,
)
```

Let’s plot the 1dB gain compression points for Gp. We create a function to plot Gp from the original LoadPullBlock and then plot the compression points on top.

```
>>> def plot_gain_and_compression_points(
...     loadpullblock, loadpullblock_at_gcomp, gcomp_value, gain_varname
... ):
...     _, ax = plt.subplots()
...     sns.lineplot(
...         y=gain_varname,
...         x="PinAvail",
...         data=loadpullblock,
...         ax=ax,
...         hue=loadpullblock.gamma_ivar("polar_str"),
...         palette="viridis",
...         legend=False,
...         linestyle="--",
...         linewidth=0.5,
...     )
...     sns.scatterplot(
...         y=gain_varname,
...         x="PinAvail",
...         data=loadpullblock_at_gcomp,
...         ax=ax,
...         hue=loadpullblock_at_gcomp.gamma_ivar("polar_str"),
...         palette="viridis",
...     )
...     ax.set_title(f"{gain_varname} at Gcomp = {gcomp_value}")
...     ax.legend(
...         title="GammaLoad values",
...         bbox_to_anchor=(1.1, 1.1),
...         loc="upper left",
...         borderaxespad=0,
...         ncol=2,
...     )
...     plt.show()
```

Now, let’s call the function.

```
>>> plot_gain_and_compression_points(lpblock, lpblock_at_gcomp, gcomp_value, "Gp")
```

[![../../_images/realistic_gcomp_points_all.png](../../_images/realistic_gcomp_points_all.png)](../../_images/realistic_gcomp_points_all.png)

The [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method interpolates and extrapolates to find the gain compression point at each gamma point. The gain compression points are the dots in the plot above. For some gammas, especially those with larger magnitudes, we are extrapolating quite a bit. To limit the amount of extrapolation, we could eliminate some gamma points. Let’s try that now.

```
>>> gamma_mag = np.abs(lpblock.gamma_ivar())
>>> lpblock_filtered = lpblock.keep_observations(gamma_mag < 0.95)
>>> lpblock_filtered_at_gcomp = lpblock_filtered.at_gcomp(gcomp_value, "Gp")
```

Plotting the filtered LoadPullBlock’s gain compression points shows that less extrapolation is needed to calculate the 1dB compression points.

```
>>> plot_gain_and_compression_points(
...     lpblock_filtered, lpblock_filtered_at_gcomp, gcomp_value, "Gp"
... )
```

[![../../_images/realistic_gcomp_points_filtered.png](../../_images/realistic_gcomp_points_filtered.png)](../../_images/realistic_gcomp_points_filtered.png)

## Plot contours[](#plot-contours "Link to this heading")

To create contour plots, we can use the [`LoadPullBlock.contourplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md#keysight.pwdatatools.LoadPullBlock.contourplot "keysight.pwdatatools.LoadPullBlock.contourplot") method. It’s common to plot contours at a particular power level or compression level. So, let’s plot gain and efficiency contours for the `lpblock_at_power` and `lpblock_at_gcomp` objects that we created in the previous steps.

```
>>> fig, axs = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(9, 3))
>>> cs_at_power = lpblock_at_power.contourplot("Gp", ax=axs[0], colors="blue")
>>> plt.clabel(cs_at_power, inline=True, fontsize=10)
>>> cs_at_gcomp = lpblock_at_gcomp.contourplot("Gp", ax=axs[1], colors="blue")
>>> plt.clabel(cs_at_gcomp, inline=True, fontsize=10)
>>> axs[0].set_title("Gp contours at PLoad = 40")
>>> axs[1].set_title(f"Gp contours at Gcomp = {gcomp_value}")
>>> axs[1].set_ylabel("")
>>> plt.show()
```

[![../../_images/realistic_contour_plots.png](../../_images/realistic_contour_plots.png)](../../_images/realistic_contour_plots.png)

## Regularize and grid the data[](#regularize-and-grid-the-data "Link to this heading")

If you do not understand the concept of “gridded” load pull data, please read [What is “gridded” load pull data?](../../howto/work_with_loadpull_data.md#what-is-gridded-load-pull-data) and [this simple gridding tutorial](swept_gamma_power_example.md#grid-data) before proceeding.

The pattern of sampled gamma points looks somewhat polar-shaped. Is the original data gridded? Let’s find out.

```
>>> print(lpblock.is_gridded())
False
```

No, it’s not gridded. Let’s grid it. But before we can apply a grid, the LoadPullBlock must have a regular power sweep. Let’s check if the power sweep is regular.

```
>>> print(lpblock.has_regular_power_ivar())
False
```

No, the power sweep is not regular. But what does this really mean? Let’s plot the power sweeps at each gamma point to see what’s going on. We will create a function to do this.

```
>>> def plot_power_levels_at_each_gamma(loadpullblock, title):
...     _, axes = plt.subplots(figsize=(5, 8))
...     sweep = loadpullblock.get_sweep()
...     gamma_polar_str = viz.complex_vector_to_str_series(
...         loadpullblock.gamma_ivar().to_numpy_ndarray(), "polar"
...     )
...     axes = sns.scatterplot(
...         x=loadpullblock[sweep.power_ivarname],
...         y=gamma_polar_str,
...     )
...     axes.set_title(title)
...     axes.set_xlabel(sweep.power_ivarname, fontsize=14, labelpad=10)
...     axes.set_ylabel(sweep.gamma_ivarname, fontsize=14, labelpad=10)
...     axes.tick_params(axis="y", which="major", labelsize=9)
...     plt.show()
```

Now, let’s use our function to plot the power sweeps at each gamma point.

```
>>> plot_power_levels_at_each_gamma(lpblock, "Irregular Power Sweeps at Each Gamma")
```

[![../../_images/realistic_gamma_vs_power_irreg.png](../../_images/realistic_gamma_vs_power_irreg.png)](../../_images/realistic_gamma_vs_power_irreg.png)

After examining the above plot, it should be clear that the power sweep is not the same for every gamma.

Note

Having a “regular power sweep” does **not** necessarily mean the power values are evenly-spaced.

Let’s regularize the power sweep. We’ll use the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method with extrapolation enabled. Then, we’ll use the [`LoadPullBlock.has_regular_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar.md#keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar "keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar") method to check if the new LoadPullBlock instance has a regular power sweep.

```
>>> lpblock_reg = lpblock.regularize_power_ivar(extrap=True)
>>> print(f"lpblock_reg has regular power sweep: {lpblock_reg.has_regular_power_ivar()}")
lpblock_reg has regular power sweep: True
```

For our regularized LoadPullBlock, let’s use our same function we used before to plot the power sweep values at each gamma point.

```
>>> plot_power_levels_at_each_gamma(lpblock_reg, "Regularized Power Sweeps at Each Gamma")
```

[![../../_images/realistic_gamma_vs_power_reg.png](../../_images/realistic_gamma_vs_power_reg.png)](../../_images/realistic_gamma_vs_power_reg.png)

Let’s also print out all the unique power values for our original LoadPullBlock and compare them to the regularized LoadPullBlock.

```
>>> original_power_vals = np.unique(lpblock.power_ivar())
>>> regularized_power_vals = np.unique(lpblock_reg.power_ivar())
>>> print(f"Original power values:\n{original_power_vals}")
Original power values:
[17.94 17.95 17.96 17.97 17.98 17.99 18.   18.01 18.02 18.04 18.58 18.61
 18.62 18.95 18.97 18.99 19.   19.01 19.02 19.04 19.05 19.56 19.61 19.92
 19.95 19.96 19.97 19.98 19.99 20.   20.01 20.02 20.03 20.55 20.57 20.58
 20.6  20.61 20.94 20.96 20.97 20.98 20.99 21.   21.01 21.02 21.57 21.6
 21.95 21.96 21.97 21.98 21.99 22.   22.02 22.03 22.57 22.6  22.61 22.95
 22.96 22.97 22.98 22.99 23.   23.01 23.02 23.04 23.56 23.58 23.6  23.63
 23.97 23.98 23.99 24.   24.01 24.02 24.03 24.04 24.6  24.62 24.98 24.99
 25.   25.01 25.02 25.03 25.04 25.05 25.06 25.6  25.61 25.65 26.01 26.02
 26.03 26.04 26.05 26.06 26.07 26.08 26.09 26.53 26.63 26.64 26.67 27.05
 27.06 27.07 27.08 27.09 27.1  27.11 27.12 27.64 27.66 27.67 27.69 27.71
 28.08 28.09 28.1  28.11 28.12 28.13 28.15 28.61 28.62 28.65 28.7  28.72
 29.1  29.11 29.12 29.13 29.14 29.15 29.16 29.17 29.18 29.7  29.72 29.73
 29.75 30.1  30.11 30.12 30.13 30.14 30.15 30.16 30.17 30.54 30.7  30.71
 30.73 31.07 31.09 31.1  31.11 31.12 31.13 31.14 31.15 31.16 31.55 31.56
 31.57 31.68 31.7  32.04 32.05 32.07 32.08 32.09 32.11 32.12 32.54 32.65
 33.03 33.04 33.05 33.06 33.63]
>>> print(f"Regularized power values:\n{regularized_power_vals}")
Regularized power values:
[-25.  -23.9 -22.9 -21.8 -20.7 -19.6 -18.6 -17.5 -16.4 -15.4 -14.3 -13.2
-12.1 -11.1 -10. ]
```

By default, the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method produces evenly-spaced sweeps between the max and min power values, rounded to the nearest tenth. However, as previously mentioned, having evenly-spaced power values is not a requirement for a LoadPullBlock’s power sweep to be considered “regular”. By default, the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method uses cubic interpolation to calculate all responses at the new power values. Extrapolation is off by default, but there are cubic, linear, and constant `extrap_method` options. See the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method for more information.

Now that we’ve regularized the LoadPullBlock’s power sweep, let’s grid it. First, let’s create a function that we can use to plot gridded and ungridded gamma points on a Smith chart. That way, we can repeatedly call the function throughout the demo.

```
>>> def plot_gamma_gridded_vs_ungridded_at_power(
...     lpblock_gridded, lpblock_ungridded, power_val, power_col
... ):
...     lpblock_ungridded_at_power = lpblock_ungridded.at_power(power_val, power_col)
...     lpblock_gridded_at_power = lpblock_gridded.at_power(power_val, power_col)
...     fig, ax = plt.subplots()
...     viz.draw_smith_chart(ax)
...     ax.set_title(f"GammaLoad at {power_col} = {power_val}")
...     lpblock_ungridded_at_power.gamma_ivar_scatterplot(
...         color="red", marker="D", label="Ungridded", ax=ax
...     )
...     lpblock_gridded_at_power.gamma_ivar_scatterplot(
..          color="blue", alpha=0.8, marker="X", label="Gridded", ax=ax
...     )
...     plt.show()
```

Either a ‘rect’ or ‘polar’ coordinate system will indeed work, but the ‘polar’ coordinate system is more appropriate for this data since the gamma points are sampled in a polar-shaped pattern.

```
>>> lpblock_gridded = lpblock.grid_data('polar')
>>> plot_gamma_gridded_vs_ungridded_at_power(lpblock_gridded, lpblock_reg, 20, "PSource")
```

[![../../_images/realistic_gamma_points_polar_gridded_smithchart.png](../../_images/realistic_gamma_points_polar_gridded_smithchart.png)](../../_images/realistic_gamma_points_polar_gridded_smithchart.png)

## Send data to ADS[](#send-data-to-ads "Link to this heading")

Let’s demonstrate how to get data into PathWave Advanced Design System (ADS). You can write out the gridded data into an ADS dataset and plot contours in ADS data display. The specialized Block object called ADSContourBlock arranges the data in such a way as to facilitate plotting contours in ADS. You may need to set the HPEESOF\_DIR environment variable as shown to point to an ADS installation.

```
>>> os.environ["HPEESOF_DIR"] = r"C:\Program Files\Keysight\ADS2024"
>>> cblock = lpblock_gridded.to_adscontourblock()
>>> cblock.to_file(output_filepath, dst_mode="w")
```

You can also directly write out a LoadPullBlock to an ADS dataset.

```
>>> lpblock_gridded.to_file(WRK_DATA_FOLDER / output_filepath, dst_mode="w")
```

See also

All Python scripts and data files for the load pull examples are located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

On this page

[Previous

Swept Frequency, Gamma, and Power](swept_freq_gamma_power_example.md)
[Next

API Reference](../../api_reference/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top