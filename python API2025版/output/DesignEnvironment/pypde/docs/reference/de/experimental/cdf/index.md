<!-- 来源: pypde\docs\reference\de\experimental\cdf\index.html -->

[![Logo](../../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../../index.md)
* [Design](../../../../index.md)
* [Reference](../../../index.md)
* [keysight.ads.de.experimental](../index.md)
* CDF

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../../../../../../pydocs/intro/index.md)
  + [Licensing](../../../../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../../../../pydocs/intro/extension.md)
* [Concepts](../../../../../../pydocs/concepts/index.md)
  + [Terminology](../../../../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../../../../pydocs/concepts/execution.md)
* [How-To](../../../../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../../../../pydocs/howto/pytest.md)

* [Design](../../../../index.md)
  + [Reference](../../../index.md)
    - [keysight.ads.de](../../index.md)
      * [Workspace](../../workspace.md)
      * [Library](../../library.md)
      * [Cell](../../cell.md)
      * [View](../../view.md)
      * [CellviewRef](../../cellviewref.md)
      * [DesignHierarchy](../../design_hierarchy.md)
      * [DMData](../../dmdata.md)
      * [ItemInfo](../../item_info.md)
      * [Points](../../points.md)
      * [Collections](../../collections.md)
    - [keysight.ads.de.ael](../../ael.md)
    - [keysight.ads.de.app](../../app/index.md)
      * [Actions and Menus](../../app/action.md)
      * [Addons](../../app/addon.md)
      * [Callbacks](../../app/callbacks.md)
      * [Windows and Widgets](../../app/window.md)
    - [keysight.ads.de.db](../../db/index.md)
      * [Callbacks](../../db/callbacks.md)
      * [Enumerated Types](../../db/enums.md)
      * [Parameter Forms](../../db/forms.md)
      * [GenPolyline](../../db/genpolyline.md)
      * [Model Definition](../../db/model_def.md)
      * [Parameters](../../db/parameters.md)
      * [Properties](../../db/properties.md)
      * [Transaction](../../db/transaction.md)
    - [keysight.ads.de.db\_dbu](../../db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../../db_uu/index.md)
      * [Design Elements](../../db_uu/db_uu.md)
      * [LayerId](../../db_uu/layer_id.md)
      * [LineTypeInfo](../../db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../index.md)
      * CDF
      * [Commands](../commands.md)
      * [Handles](../handles.md)
      * [Netlist Utilities](../netlist_helper.md)
      * [Polygon Utilities](../polygon_utils.md)
      * [Preferences](../preferences.md)
      * [xxPro View](../pro_view.md)
      * [Symbol Generator](../symbol.md)
      * [Text Maker](../text_maker.md)
    - [keysight.ads.de.tech](../../tech/index.md)
      * [Tech](../../tech/tech.md)
      * [Padstacks](../../tech/pads/pads.md)
      * [Via Rules](../../tech/rule/rule.md)
      * [Nested Technology](../../tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../../app/dds.md)
  + [Examples](../../../../examples/index.md)
    - [Calling Between AEL and Python](../../../../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../../../examples/ex_create_layout.md)
    - [Create Schematic](../../../../examples/ex_create_schematic.md)
    - [Create Workspace](../../../../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../../../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../../../examples/ex_cdf.md)
    - [Component Parameters](../../../../examples/ex_parameters.md)
    - [Creating an Item Definition](../../../../examples/ex_itemdef.md)
    - [Model Definition Properties](../../../../examples/ex_model.md)
    - [Adding Instances to a Design](../../../../examples/ex_lpf.md)
    - [Properties](../../../../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../../../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../../../examples/ex_padstack.md)
    - [Nested Technology](../../../../examples/ex_nested.md)
    - [Rules](../../../../examples/ex_rules.md)
    - [Placing Text](../../../../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../../../examples/ex_polygon.md)
    - [PySide2](../../../../examples/ex_pyside.md)
    - [Traversing Hierarchy](../../../../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../../../examples/ex_working_with_var.md)
    - [XML RPC](../../../../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../../../examples/ex_translate_gds.md)
* [Technology](../../../../../../pysubst/docs/index.md)
  + [Reference](../../../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# CDF[](#module-keysight.ads.de.experimental.cdf "Link to this heading")

CDF module contains the API for interoperable components.

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.cdf.CDFBase[](#keysight.ads.de.experimental.cdf.CDFBase "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.cdf.CDFBase.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    add\_param(*param: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*) → None[](#keysight.ads.de.experimental.cdf.CDFBase.add_param "Link to this definition")

    delete\_param(*index: int*) → None[](#keysight.ads.de.experimental.cdf.CDFBase.delete_param "Link to this definition")

    *property* done\_proc*: str*[](#keysight.ads.de.experimental.cdf.CDFBase.done_proc "Link to this definition")

    find\_param(*name: str*) → [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef") | None[](#keysight.ads.de.experimental.cdf.CDFBase.find_param "Link to this definition")

    find\_sim\_info(*sim\_name: str*) → [SimInfo](#keysight.ads.de.experimental.cdf.SimInfo "keysight.ads.de.experimental.cdf.sim_info.SimInfo") | None[](#keysight.ads.de.experimental.cdf.CDFBase.find_sim_info "Link to this definition")

    find\_view\_info(*view\_name: str*) → [ViewInfo](#keysight.ads.de.experimental.cdf.ViewInfo "keysight.ads.de.experimental.cdf.view_info.ViewInfo") | None[](#keysight.ads.de.experimental.cdf.CDFBase.find_view_info "Link to this definition")

    *property* form\_init\_proc*: str*[](#keysight.ads.de.experimental.cdf.CDFBase.form_init_proc "Link to this definition")

    insert\_param(*param: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*, *index: int*) → None[](#keysight.ads.de.experimental.cdf.CDFBase.insert_param "Link to this definition")

    *property* num\_params*: int*[](#keysight.ads.de.experimental.cdf.CDFBase.num_params "Link to this definition")

    param(*id\_: int*) → [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")[](#keysight.ads.de.experimental.cdf.CDFBase.param "Link to this definition")

    param(*id\_: str*) → [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")

    *property* params*: NamedItemCollectionAbc[[ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")]*[](#keysight.ads.de.experimental.cdf.CDFBase.params "Link to this definition")

    sim\_info(*sim\_name: str*) → [SimInfo](#keysight.ads.de.experimental.cdf.SimInfo "keysight.ads.de.experimental.cdf.sim_info.SimInfo")[](#keysight.ads.de.experimental.cdf.CDFBase.sim_info "Link to this definition")

    view\_info(*view\_name: str*) → [ViewInfo](#keysight.ads.de.experimental.cdf.ViewInfo "keysight.ads.de.experimental.cdf.view_info.ViewInfo")[](#keysight.ads.de.experimental.cdf.CDFBase.view_info "Link to this definition")

*class* keysight.ads.de.experimental.cdf.CellCDF[](#keysight.ads.de.experimental.cdf.CellCDF "Link to this definition")
:   Bases: [`ManagedCDF`](#keysight.ads.de.experimental.cdf.ManagedCDF "keysight.ads.de.experimental.cdf.comp_def.ManagedCDF")

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.cdf.CellCDF.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* cell*: [Cell](../../cell.md#keysight.ads.de.Cell "keysight.ads.de._core.cell.Cell")*[](#keysight.ads.de.experimental.cdf.CellCDF.cell "Link to this definition")

    *property* library*: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.de.experimental.cdf.CellCDF.library "Link to this definition")

*class* keysight.ads.de.experimental.cdf.InstanceParams[](#keysight.ads.de.experimental.cdf.InstanceParams "Link to this definition")
:   Supports editing parameter values for interoperable instances.

    \_\_init\_\_(*inst\_or\_design: Instance | [Instance](../../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*, *cdf: 'CellCDF' | None = None*) → None[](#keysight.ads.de.experimental.cdf.InstanceParams.__init__ "Link to this definition")

    \_\_init\_\_(*inst\_or\_design: Design | [Design](../../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *cdf: [CellCDF](#keysight.ads.de.experimental.cdf.CellCDF "keysight.ads.de.experimental.cdf.CellCDF")*) → None

    *property* cell\_cdf*: [CellCDF](#keysight.ads.de.experimental.cdf.CellCDF "keysight.ads.de.experimental.cdf.CellCDF")*[](#keysight.ads.de.experimental.cdf.InstanceParams.cell_cdf "Link to this definition")

    execute\_callback(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*) → None[](#keysight.ads.de.experimental.cdf.InstanceParams.execute_callback "Link to this definition")

    execute\_callback(*id\_: str*) → None

    find\_param(*param\_name: str*) → Parameter | None[](#keysight.ads.de.experimental.cdf.InstanceParams.find_param "Link to this definition")

    find\_param\_def(*param\_name: str*) → [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef") | None[](#keysight.ads.de.experimental.cdf.InstanceParams.find_param_def "Link to this definition")

    *property* instance\_dbu*: Instance | None*[](#keysight.ads.de.experimental.cdf.InstanceParams.instance_dbu "Link to this definition")

    *property* instance\_uu*: [Instance](../../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance") | None*[](#keysight.ads.de.experimental.cdf.InstanceParams.instance_uu "Link to this definition")

    *property* is\_modified*: bool*[](#keysight.ads.de.experimental.cdf.InstanceParams.is_modified "Link to this definition")

    param(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*) → Parameter[](#keysight.ads.de.experimental.cdf.InstanceParams.param "Link to this definition")

    param(*id\_: str*) → Parameter

    param\_def(*param\_name: str*) → [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")[](#keysight.ads.de.experimental.cdf.InstanceParams.param_def "Link to this definition")

    param\_value(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*) → bool | int | float | str[](#keysight.ads.de.experimental.cdf.InstanceParams.param_value "Link to this definition")

    param\_value(*id\_: str*) → bool | int | float | str

    param\_value\_no\_default(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*) → bool | int | float | str | None[](#keysight.ads.de.experimental.cdf.InstanceParams.param_value_no_default "Link to this definition")

    param\_value\_no\_default(*id\_: str*) → bool | int | float | str | None

    *property* params*: NamedItemCollectionAbc[Parameter]*[](#keysight.ads.de.experimental.cdf.InstanceParams.params "Link to this definition")

    *property* parent\_design\_dbu*: Design*[](#keysight.ads.de.experimental.cdf.InstanceParams.parent_design_dbu "Link to this definition")

    *property* parent\_design\_uu*: [Design](../../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*[](#keysight.ads.de.experimental.cdf.InstanceParams.parent_design_uu "Link to this definition")

    reset\_to\_defaults() → None[](#keysight.ads.de.experimental.cdf.InstanceParams.reset_to_defaults "Link to this definition")

    set\_param\_value(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*, *value: bool | int | float | str*) → None[](#keysight.ads.de.experimental.cdf.InstanceParams.set_param_value "Link to this definition")

    set\_param\_value(*id\_: str*, *value: bool | int | float | str*) → None
    :   Set the parameter value and call the callback if one exists.

    set\_param\_value\_no\_callback(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*, *value: bool | int | float | str*) → None[](#keysight.ads.de.experimental.cdf.InstanceParams.set_param_value_no_callback "Link to this definition")

    set\_param\_value\_no\_callback(*id\_: str*, *value: bool | int | float | str*) → None
    :   Set the parameter value without calling any callback.

    update\_instance(*inst: Instance | [Instance](../../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance") | None*) → None[](#keysight.ads.de.experimental.cdf.InstanceParams.update_instance "Link to this definition")
    :   Assign all the modified parameter values to the instance.

*class* keysight.ads.de.experimental.cdf.LibraryCDF[](#keysight.ads.de.experimental.cdf.LibraryCDF "Link to this definition")
:   Bases: [`ManagedCDF`](#keysight.ads.de.experimental.cdf.ManagedCDF "keysight.ads.de.experimental.cdf.comp_def.ManagedCDF")

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.cdf.LibraryCDF.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* library*: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.de.experimental.cdf.LibraryCDF.library "Link to this definition")

*class* keysight.ads.de.experimental.cdf.ManagedCDF[](#keysight.ads.de.experimental.cdf.ManagedCDF "Link to this definition")
:   Bases: [`CDFBase`](#keysight.ads.de.experimental.cdf.CDFBase "keysight.ads.de.experimental.cdf.comp_def.CDFBase")

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.cdf.ManagedCDF.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* library\_name*: str*[](#keysight.ads.de.experimental.cdf.ManagedCDF.library_name "Link to this definition")

*class* keysight.ads.de.experimental.cdf.ParamDef[](#keysight.ads.de.experimental.cdf.ParamDef "Link to this definition")
:   \_\_init\_\_(*name: str*, *param\_type: [ParamType](#keysight.ads.de.experimental.cdf.ParamType "keysight.ads.de.experimental.cdf.params.ParamType")*) → None[](#keysight.ads.de.experimental.cdf.ParamDef.__init__ "Link to this definition")

    *property* callback*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.callback "Link to this definition")

    change\_type(*param\_type: [ParamType](#keysight.ads.de.experimental.cdf.ParamType "keysight.ads.de.experimental.cdf.params.ParamType")*) → None[](#keysight.ads.de.experimental.cdf.ParamDef.change_type "Link to this definition")
    :   Change the type of a parameter. This may require changing the default value.

    *property* choices*: list[str]*[](#keysight.ads.de.experimental.cdf.ParamDef.choices "Link to this definition")

    *property* default\_oa\_param*: [OAParam](../../db/parameters.md#keysight.ads.de.db.OAParam "keysight.ads.de.db._pcell_parameters.OAParam")*[](#keysight.ads.de.experimental.cdf.ParamDef.default_oa_param "Link to this definition")
    :   Mainly for testing. Use default\_value.

    *property* default\_value*: bool | int | float | str*[](#keysight.ads.de.experimental.cdf.ParamDef.default_value "Link to this definition")

    *property* display\_condition*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.display_condition "Link to this definition")

    *property* dont\_save\_condition*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.dont_save_condition "Link to this definition")

    *property* editable\_condition*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.editable_condition "Link to this definition")

    *property* has\_callback*: bool*[](#keysight.ads.de.experimental.cdf.ParamDef.has_callback "Link to this definition")

    *property* has\_choices*: bool*[](#keysight.ads.de.experimental.cdf.ParamDef.has_choices "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.name "Link to this definition")

    *property* param\_type*: [ParamType](#keysight.ads.de.experimental.cdf.ParamType "keysight.ads.de.experimental.cdf.params.ParamType")*[](#keysight.ads.de.experimental.cdf.ParamDef.param_type "Link to this definition")

    *property* parse\_as\_cel*: bool | None*[](#keysight.ads.de.experimental.cdf.ParamDef.parse_as_cel "Link to this definition")

    *property* parse\_as\_cel\_expr*: str | None*[](#keysight.ads.de.experimental.cdf.ParamDef.parse_as_cel_expr "Link to this definition")

    *property* parse\_as\_number*: bool | None*[](#keysight.ads.de.experimental.cdf.ParamDef.parse_as_number "Link to this definition")

    *property* parse\_as\_number\_expr*: str | None*[](#keysight.ads.de.experimental.cdf.ParamDef.parse_as_number_expr "Link to this definition")

    *property* prompt*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.prompt "Link to this definition")

    set\_choices(*choices: str*) → None[](#keysight.ads.de.experimental.cdf.ParamDef.set_choices "Link to this definition")

    *property* store\_default*: bool | None*[](#keysight.ads.de.experimental.cdf.ParamDef.store_default "Link to this definition")

    *property* store\_default\_expr*: str | None*[](#keysight.ads.de.experimental.cdf.ParamDef.store_default_expr "Link to this definition")

    *property* units*: [ParamUnits](#keysight.ads.de.experimental.cdf.ParamUnits "keysight.ads.de.experimental.cdf.params.ParamUnits")*[](#keysight.ads.de.experimental.cdf.ParamDef.units "Link to this definition")

    *property* use\_condition*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.use_condition "Link to this definition")

*class* keysight.ads.de.experimental.cdf.ScratchCDF[](#keysight.ads.de.experimental.cdf.ScratchCDF "Link to this definition")
:   Bases: [`CDFBase`](#keysight.ads.de.experimental.cdf.CDFBase "keysight.ads.de.experimental.cdf.comp_def.CDFBase")

    \_\_init\_\_() → None[](#keysight.ads.de.experimental.cdf.ScratchCDF.__init__ "Link to this definition")

*class* keysight.ads.de.experimental.cdf.SimInfo[](#keysight.ads.de.experimental.cdf.SimInfo "Link to this definition")
:   \_\_init\_\_(*name: str*) → None[](#keysight.ads.de.experimental.cdf.SimInfo.__init__ "Link to this definition")

    cdf\_name\_from\_sim\_param\_name(*sim\_param\_name: str*) → str[](#keysight.ads.de.experimental.cdf.SimInfo.cdf_name_from_sim_param_name "Link to this definition")

    *property* comp\_name*: str*[](#keysight.ads.de.experimental.cdf.SimInfo.comp_name "Link to this definition")

    *property* inst\_parameters*: list[str]*[](#keysight.ads.de.experimental.cdf.SimInfo.inst_parameters "Link to this definition")

    is\_cdf\_param\_in\_inst\_parameters(*cdf\_param\_name: str*) → bool[](#keysight.ads.de.experimental.cdf.SimInfo.is_cdf_param_in_inst_parameters "Link to this definition")

    is\_cdf\_param\_in\_other\_parameters(*cdf\_param\_name: str*) → bool[](#keysight.ads.de.experimental.cdf.SimInfo.is_cdf_param_in_other_parameters "Link to this definition")

    *property* is\_empty*: bool*[](#keysight.ads.de.experimental.cdf.SimInfo.is_empty "Link to this definition")

    *property* netlist\_procedure*: str*[](#keysight.ads.de.experimental.cdf.SimInfo.netlist_procedure "Link to this definition")

    *property* other\_parameters*: list[str]*[](#keysight.ads.de.experimental.cdf.SimInfo.other_parameters "Link to this definition")

    *property* prop\_mapping*: dict[str, str]*[](#keysight.ads.de.experimental.cdf.SimInfo.prop_mapping "Link to this definition")

    set\_prop\_mapping(*prop\_mapping: str*) → None[](#keysight.ads.de.experimental.cdf.SimInfo.set_prop_mapping "Link to this definition")

    set\_term\_mapping(*term\_mapping: str*) → None[](#keysight.ads.de.experimental.cdf.SimInfo.set_term_mapping "Link to this definition")

    set\_term\_order(*term\_order: str*) → None[](#keysight.ads.de.experimental.cdf.SimInfo.set_term_order "Link to this definition")

    *property* sim\_name*: str*[](#keysight.ads.de.experimental.cdf.SimInfo.sim_name "Link to this definition")

    sim\_term\_name\_from\_term\_name(*term\_name: str*) → str[](#keysight.ads.de.experimental.cdf.SimInfo.sim_term_name_from_term_name "Link to this definition")

    *property* term\_mapping*: dict[str, str]*[](#keysight.ads.de.experimental.cdf.SimInfo.term_mapping "Link to this definition")

    *property* term\_order*: list[str]*[](#keysight.ads.de.experimental.cdf.SimInfo.term_order "Link to this definition")

*class* keysight.ads.de.experimental.cdf.ViewInfo[](#keysight.ads.de.experimental.cdf.ViewInfo "Link to this definition")
:   \_\_init\_\_(*name: str*) → None[](#keysight.ads.de.experimental.cdf.ViewInfo.__init__ "Link to this definition")

    cdf\_name\_from\_sim\_param\_name(*sim\_param\_name: str*) → str[](#keysight.ads.de.experimental.cdf.ViewInfo.cdf_name_from_sim_param_name "Link to this definition")

    *property* inst\_parameters*: list[str]*[](#keysight.ads.de.experimental.cdf.ViewInfo.inst_parameters "Link to this definition")

    is\_cdf\_param\_in\_parameters(*cdf\_param\_name: str*) → bool[](#keysight.ads.de.experimental.cdf.ViewInfo.is_cdf_param_in_parameters "Link to this definition")

    *property* is\_empty*: bool*[](#keysight.ads.de.experimental.cdf.ViewInfo.is_empty "Link to this definition")

    *property* module\_name*: str*[](#keysight.ads.de.experimental.cdf.ViewInfo.module_name "Link to this definition")

    *property* netlist\_procedure*: str*[](#keysight.ads.de.experimental.cdf.ViewInfo.netlist_procedure "Link to this definition")

    *property* parameters*: list[str]*[](#keysight.ads.de.experimental.cdf.ViewInfo.parameters "Link to this definition")

    *property* prop\_mapping*: dict[str, str]*[](#keysight.ads.de.experimental.cdf.ViewInfo.prop_mapping "Link to this definition")

    set\_prop\_mapping(*prop\_mapping: str*) → None[](#keysight.ads.de.experimental.cdf.ViewInfo.set_prop_mapping "Link to this definition")

    set\_term\_mapping(*term\_mapping: str*) → None[](#keysight.ads.de.experimental.cdf.ViewInfo.set_term_mapping "Link to this definition")

    set\_term\_order(*term\_order: str*) → None[](#keysight.ads.de.experimental.cdf.ViewInfo.set_term_order "Link to this definition")

    sim\_term\_name\_from\_term\_name(*term\_name: str*) → str[](#keysight.ads.de.experimental.cdf.ViewInfo.sim_term_name_from_term_name "Link to this definition")

    *property* term\_mapping*: dict[str, str]*[](#keysight.ads.de.experimental.cdf.ViewInfo.term_mapping "Link to this definition")

    *property* term\_order*: list[str]*[](#keysight.ads.de.experimental.cdf.ViewInfo.term_order "Link to this definition")

    *property* view\_name*: str*[](#keysight.ads.de.experimental.cdf.ViewInfo.view_name "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.experimental.cdf.ParamType[](#keysight.ads.de.experimental.cdf.ParamType "Link to this definition")
:   Bases: `Enum`

    The type of a CDF Parameter - determines how values are stored.

    UNKNOWN *= <ParamType.UNKNOWN: -1>*[](#keysight.ads.de.experimental.cdf.ParamType.UNKNOWN "Link to this definition")

    STRING *= <ParamType.STRING: 0>*[](#keysight.ads.de.experimental.cdf.ParamType.STRING "Link to this definition")

    INT *= <ParamType.INT: 1>*[](#keysight.ads.de.experimental.cdf.ParamType.INT "Link to this definition")

    FLOAT *= <ParamType.FLOAT: 2>*[](#keysight.ads.de.experimental.cdf.ParamType.FLOAT "Link to this definition")

    RADIO *= <ParamType.RADIO: 3>*[](#keysight.ads.de.experimental.cdf.ParamType.RADIO "Link to this definition")
    :   Has choices - stored as a string.

    CYCLIC *= <ParamType.CYCLIC: 4>*[](#keysight.ads.de.experimental.cdf.ParamType.CYCLIC "Link to this definition")
    :   Has choices - stored as a string.

    BOOLEAN *= <ParamType.BOOLEAN: 5>*[](#keysight.ads.de.experimental.cdf.ParamType.BOOLEAN "Link to this definition")
    :   Should be True/False, but stored as an int.

    BUTTON *= <ParamType.BUTTON: 6>*[](#keysight.ads.de.experimental.cdf.ParamType.BUTTON "Link to this definition")
    :   Not stored as a value.

    NETSET *= <ParamType.NETSET: 7>*[](#keysight.ads.de.experimental.cdf.ParamType.NETSET "Link to this definition")
    :   Not stored as a value. Used for net connections.

*class* keysight.ads.de.experimental.cdf.ParamUnits[](#keysight.ads.de.experimental.cdf.ParamUnits "Link to this definition")
:   Bases: `Enum`

    The units used for a CDF Parameter.

    UNKNOWN *= <ParamUnits.UNKNOWN: -1>*[](#keysight.ads.de.experimental.cdf.ParamUnits.UNKNOWN "Link to this definition")

    RESISTANCE *= <ParamUnits.RESISTANCE: 0>*[](#keysight.ads.de.experimental.cdf.ParamUnits.RESISTANCE "Link to this definition")

    CAPACITANCE *= <ParamUnits.CAPACITANCE: 1>*[](#keysight.ads.de.experimental.cdf.ParamUnits.CAPACITANCE "Link to this definition")

    INDUCTANCE *= <ParamUnits.INDUCTANCE: 2>*[](#keysight.ads.de.experimental.cdf.ParamUnits.INDUCTANCE "Link to this definition")

    CONDUCTANCE *= <ParamUnits.CONDUCTANCE: 3>*[](#keysight.ads.de.experimental.cdf.ParamUnits.CONDUCTANCE "Link to this definition")

    TIME *= <ParamUnits.TIME: 4>*[](#keysight.ads.de.experimental.cdf.ParamUnits.TIME "Link to this definition")

    FREQUENCY *= <ParamUnits.FREQUENCY: 5>*[](#keysight.ads.de.experimental.cdf.ParamUnits.FREQUENCY "Link to this definition")

    POWER *= <ParamUnits.POWER: 6>*[](#keysight.ads.de.experimental.cdf.ParamUnits.POWER "Link to this definition")

    POWER\_DB *= <ParamUnits.POWER\_DB: 7>*[](#keysight.ads.de.experimental.cdf.ParamUnits.POWER_DB "Link to this definition")

    LENGTH *= <ParamUnits.LENGTH: 8>*[](#keysight.ads.de.experimental.cdf.ParamUnits.LENGTH "Link to this definition")

    LENGTH\_ENGLISH *= <ParamUnits.LENGTH\_ENGLISH: 9>*[](#keysight.ads.de.experimental.cdf.ParamUnits.LENGTH_ENGLISH "Link to this definition")

    ANGLE *= <ParamUnits.ANGLE: 10>*[](#keysight.ads.de.experimental.cdf.ParamUnits.ANGLE "Link to this definition")

    VOLTAGE *= <ParamUnits.VOLTAGE: 11>*[](#keysight.ads.de.experimental.cdf.ParamUnits.VOLTAGE "Link to this definition")

    CURRENT *= <ParamUnits.CURRENT: 12>*[](#keysight.ads.de.experimental.cdf.ParamUnits.CURRENT "Link to this definition")

    TEMPERATURE *= <ParamUnits.TEMPERATURE: 13>*[](#keysight.ads.de.experimental.cdf.ParamUnits.TEMPERATURE "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.de.experimental.cdf.cell\_cdf(*lib\_or\_cell: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library") | [Cell](../../cell.md#keysight.ads.de.Cell "keysight.ads.de._core.cell.Cell")*, *cell\_name: str | None = None*) → [CellCDF](#keysight.ads.de.experimental.cdf.CellCDF "keysight.ads.de.experimental.cdf.comp_def.CellCDF")[](#keysight.ads.de.experimental.cdf.cell_cdf "Link to this definition")

keysight.ads.de.experimental.cdf.find\_cell\_cdf(*lib\_or\_cell: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *cell\_name: str*) → [CellCDF](#keysight.ads.de.experimental.cdf.CellCDF "keysight.ads.de.experimental.cdf.comp_def.CellCDF") | None[](#keysight.ads.de.experimental.cdf.find_cell_cdf "Link to this definition")

keysight.ads.de.experimental.cdf.find\_cell\_cdf(*lib\_or\_cell: [Cell](../../cell.md#keysight.ads.de.Cell "keysight.ads.de._core.cell.Cell")*) → [CellCDF](#keysight.ads.de.experimental.cdf.CellCDF "keysight.ads.de.experimental.cdf.comp_def.CellCDF") | None

keysight.ads.de.experimental.cdf.find\_library\_cdf(*lib: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*) → [LibraryCDF](#keysight.ads.de.experimental.cdf.LibraryCDF "keysight.ads.de.experimental.cdf.comp_def.LibraryCDF") | None[](#keysight.ads.de.experimental.cdf.find_library_cdf "Link to this definition")

keysight.ads.de.experimental.cdf.library\_cdf(*lib: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*) → [LibraryCDF](#keysight.ads.de.experimental.cdf.LibraryCDF "keysight.ads.de.experimental.cdf.comp_def.LibraryCDF")[](#keysight.ads.de.experimental.cdf.library_cdf "Link to this definition")

On this page

[Previous

keysight.ads.de.experimental](../index.md)
[Next

Commands](../commands.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top