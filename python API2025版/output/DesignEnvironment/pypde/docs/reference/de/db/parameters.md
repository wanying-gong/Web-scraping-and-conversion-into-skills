<!-- 来源: pypde\docs\reference\de\db\parameters.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.db](index.md)
* Parameters

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

* [Introduction](../../../../../pydocs/intro/index.md)
  + [Licensing](../../../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../../../pydocs/intro/extension.md)
* [Concepts](../../../../../pydocs/concepts/index.md)
  + [Terminology](../../../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../../../pydocs/concepts/execution.md)
* [How-To](../../../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../../../pydocs/howto/pytest.md)

* [Design](../../../index.md)
  + [Reference](../../index.md)
    - [keysight.ads.de](../index.md)
      * [Workspace](../workspace.md)
      * [Library](../library.md)
      * [Cell](../cell.md)
      * [View](../view.md)
      * [CellviewRef](../cellviewref.md)
      * [DesignHierarchy](../design_hierarchy.md)
      * [DMData](../dmdata.md)
      * [ItemInfo](../item_info.md)
      * [Points](../points.md)
      * [Collections](../collections.md)
    - [keysight.ads.de.ael](../ael.md)
    - [keysight.ads.de.app](../app/index.md)
      * [Actions and Menus](../app/action.md)
      * [Addons](../app/addon.md)
      * [Callbacks](../app/callbacks.md)
      * [Windows and Widgets](../app/window.md)
    - [keysight.ads.de.db](index.md)
      * [Callbacks](callbacks.md)
      * [Enumerated Types](enums.md)
      * [Parameter Forms](forms.md)
      * [GenPolyline](genpolyline.md)
      * [Model Definition](model_def.md)
      * Parameters
      * [Properties](properties.md)
      * [Transaction](transaction.md)
    - [keysight.ads.de.db\_dbu](../db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../db_uu/index.md)
      * [Design Elements](../db_uu/db_uu.md)
      * [LayerId](../db_uu/layer_id.md)
      * [LineTypeInfo](../db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../experimental/index.md)
      * [CDF](../experimental/cdf/index.md)
      * [Commands](../experimental/commands.md)
      * [Handles](../experimental/handles.md)
      * [Netlist Utilities](../experimental/netlist_helper.md)
      * [Polygon Utilities](../experimental/polygon_utils.md)
      * [Preferences](../experimental/preferences.md)
      * [xxPro View](../experimental/pro_view.md)
      * [Symbol Generator](../experimental/symbol.md)
      * [Text Maker](../experimental/text_maker.md)
    - [keysight.ads.de.tech](../tech/index.md)
      * [Tech](../tech/tech.md)
      * [Padstacks](../tech/pads/pads.md)
      * [Via Rules](../tech/rule/rule.md)
      * [Nested Technology](../tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../app/dds.md)
  + [Examples](../../../examples/index.md)
    - [Calling Between AEL and Python](../../../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../../examples/ex_create_layout.md)
    - [Create Schematic](../../../examples/ex_create_schematic.md)
    - [Create Workspace](../../../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../../examples/ex_cdf.md)
    - [Component Parameters](../../../examples/ex_parameters.md)
    - [Creating an Item Definition](../../../examples/ex_itemdef.md)
    - [Model Definition Properties](../../../examples/ex_model.md)
    - [Adding Instances to a Design](../../../examples/ex_lpf.md)
    - [Properties](../../../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../../examples/ex_padstack.md)
    - [Nested Technology](../../../examples/ex_nested.md)
    - [Rules](../../../examples/ex_rules.md)
    - [Placing Text](../../../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../../examples/ex_polygon.md)
    - [PySide2](../../../examples/ex_pyside.md)
    - [Traversing Hierarchy](../../../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../../examples/ex_working_with_var.md)
    - [XML RPC](../../../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../../examples/ex_translate_gds.md)
* [Technology](../../../../../pysubst/docs/index.md)
  + [Reference](../../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Parameters[](#parameters "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.AppParam[](#keysight.ads.de.db.AppParam "Link to this definition")
:   Bases: `object`

    Holds the value for an application defined OAParam.

    \_\_init\_\_(*app\_type: str*, *value: str | ndarray*) → None[](#keysight.ads.de.db.AppParam.__init__ "Link to this definition")

    *property* app\_type*: str*[](#keysight.ads.de.db.AppParam.app_type "Link to this definition")

    set\_value\_from\_string(*value: str*) → None[](#keysight.ads.de.db.AppParam.set_value_from_string "Link to this definition")

    *property* value*: ndarray*[](#keysight.ads.de.db.AppParam.value "Link to this definition")

    value\_as\_string() → str[](#keysight.ads.de.db.AppParam.value_as_string "Link to this definition")

*class* keysight.ads.de.db.ExpressionContext[](#keysight.ads.de.db.ExpressionContext "Link to this definition")
:   Used for expression evaluation.

    \_\_init\_\_()[](#keysight.ads.de.db.ExpressionContext.__init__ "Link to this definition")

    clear\_design\_caches() → None[](#keysight.ads.de.db.ExpressionContext.clear_design_caches "Link to this definition")
    :   Clear all the caches for this design.

    evaluate\_expression(*expr: str*, *\**, *clear\_caches: bool = False*) → str[](#keysight.ads.de.db.ExpressionContext.evaluate_expression "Link to this definition")
    :   Evaluate the expression in this expression context and return the result.

        If clear\_caches is True, clear all the caches for this design before evaluating.

    *property* hierarchy\_context*: [DesignHierarchy](../design_hierarchy.md#keysight.ads.de.DesignHierarchy "keysight.ads.de._core.design_hierarchy.DesignHierarchy")*[](#keysight.ads.de.db.ExpressionContext.hierarchy_context "Link to this definition")

    *property* is\_valid*: bool*[](#keysight.ads.de.db.ExpressionContext.is_valid "Link to this definition")
    :   Returns True if the HierarchyContext is valid.

    pop() → None[](#keysight.ads.de.db.ExpressionContext.pop "Link to this definition")

    push\_instance\_for\_reading(*inst: InstanceDbu | InstanceUu*) → None[](#keysight.ads.de.db.ExpressionContext.push_instance_for_reading "Link to this definition")

    setup\_hierarchy\_for\_design(*design: DesignDbu | DesignUu*) → None[](#keysight.ads.de.db.ExpressionContext.setup_hierarchy_for_design "Link to this definition")

    setup\_hierarchy\_for\_layout\_only(*design: DesignDbu | DesignUu*) → None[](#keysight.ads.de.db.ExpressionContext.setup_hierarchy_for_layout_only "Link to this definition")

*class* keysight.ads.de.db.OAParam[](#keysight.ads.de.db.OAParam "Link to this definition")
:   OAParams are accessed by your artwork function when generating artwork for your Pcell.

    They are also used to store properties and CDF parameters.
    See `Design.pcell_parameters()`

    \_\_init\_\_(*name: str*, *param\_type: [OAParamType](#keysight.ads.de.db.OAParamType "keysight.ads.de.db._pcell_parameters.OAParamType")*, *val: int | float | str | [TimeParam](#keysight.ads.de.db.TimeParam "keysight.ads.de.db._pcell_parameters.TimeParam") | [AppParam](#keysight.ads.de.db.AppParam "keysight.ads.de.db._pcell_parameters.AppParam")*) → None[](#keysight.ads.de.db.OAParam.__init__ "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.OAParam.name "Link to this definition")

    string\_value\_from\_app\_type(*app\_type: str*) → str[](#keysight.ads.de.db.OAParam.string_value_from_app_type "Link to this definition")

    *property* type*: [OAParamType](#keysight.ads.de.db.OAParamType "keysight.ads.de.db._pcell_parameters.OAParamType")*[](#keysight.ads.de.db.OAParam.type "Link to this definition")

    *property* value*: int | float | str | [TimeParam](#keysight.ads.de.db.TimeParam "keysight.ads.de.db._pcell_parameters.TimeParam") | [AppParam](#keysight.ads.de.db.AppParam "keysight.ads.de.db._pcell_parameters.AppParam")*[](#keysight.ads.de.db.OAParam.value "Link to this definition")

    value\_from\_list\_app\_type() → list[](#keysight.ads.de.db.OAParam.value_from_list_app_type "Link to this definition")

*class* keysight.ads.de.db.Param[](#keysight.ads.de.db.Param "Link to this definition")
:   Bases: [`ParamNonRepeated`](#keysight.ads.de.db.ParamNonRepeated "keysight.ads.de.db._parameters.ParamNonRepeated")

    A single-valued parameter with a value, netlist value, and display value.

    *property* display\_value*: str*[](#keysight.ads.de.db.Param.display_value "Link to this definition")

    evaluate(*expr\_context: [ExpressionContext](#keysight.ads.de.db.ExpressionContext "keysight.ads.de.db._parameters.ExpressionContext")*) → bool | int | float | str[](#keysight.ads.de.db.Param.evaluate "Link to this definition")
    :   Evaluate this parameter value.

    evaluate\_no\_expr() → str[](#keysight.ads.de.db.Param.evaluate_no_expr "Link to this definition")
    :   Prepare this parameter value for use by removing quotes and evaluating units.

        Does not support expressions.
        Will raise an exception if the value has an arithmetic expression
        or references other parameters or variables.

    *property* netlist\_value*: str*[](#keysight.ads.de.db.Param.netlist_value "Link to this definition")

    *property* value*: str*[](#keysight.ads.de.db.Param.value "Link to this definition")

*class* keysight.ads.de.db.ParamBase[](#keysight.ads.de.db.ParamBase "Link to this definition")
:   Base class that holds both a parameter item and its definition.

    See [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem") and `de.db.ModelParam`.

    *property* definition*: [ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam") | None*[](#keysight.ads.de.db.ParamBase.definition "Link to this definition")

    *property* display\_value*: str | list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamBase.display_value "Link to this definition")

    evaluate(*expr\_context: [ExpressionContext](#keysight.ads.de.db.ExpressionContext "keysight.ads.de.db._parameters.ExpressionContext")*) → bool | int | float | str | list[bool | int | float | str] | list[list[bool | int | float | str]][](#keysight.ads.de.db.ParamBase.evaluate "Link to this definition")
    :   Evaluate this parameter value.

    evaluate\_no\_expr() → str | list[str] | list[list[str]][](#keysight.ads.de.db.ParamBase.evaluate_no_expr "Link to this definition")
    :   Prepare this parameter value for use by removing quotes and evaluating units.

        Does not support expressions.
        Will raise an exception if the value has an arithmetic expression
        or references other parameters or variables.

    *property* form\_name*: str*[](#keysight.ads.de.db.ParamBase.form_name "Link to this definition")

    *static* is\_compound(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[ParamCompound](#keysight.ads.de.db.ParamCompound "keysight.ads.de.db._parameters.ParamCompound")][](#keysight.ads.de.db.ParamBase.is_compound "Link to this definition")

    *static* is\_const(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")][](#keysight.ads.de.db.ParamBase.is_const "Link to this definition")

    *static* is\_null(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")][](#keysight.ads.de.db.ParamBase.is_null "Link to this definition")

    *static* is\_repeated(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[ParamRepeated](#keysight.ads.de.db.ParamRepeated "keysight.ads.de.db._parameters.ParamRepeated")][](#keysight.ads.de.db.ParamBase.is_repeated "Link to this definition")

    *static* is\_single\_valued(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")][](#keysight.ads.de.db.ParamBase.is_single_valued "Link to this definition")

    *static* is\_string(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")][](#keysight.ads.de.db.ParamBase.is_string "Link to this definition")

    *property* item*: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*[](#keysight.ads.de.db.ParamBase.item "Link to this definition")

    *static* make\_param(*item: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*, *model\_param: [ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam") | None*) → [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")[](#keysight.ads.de.db.ParamBase.make_param "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.ParamBase.name "Link to this definition")

    *property* netlist\_value*: str | list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamBase.netlist_value "Link to this definition")

    *property* no\_plot*: bool*[](#keysight.ads.de.db.ParamBase.no_plot "Link to this definition")
    :   When True, this parameter will not be displayed in schematic view.

    *property* value*: str | list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamBase.value "Link to this definition")

*class* keysight.ads.de.db.ParamCompound[](#keysight.ads.de.db.ParamCompound "Link to this definition")
:   Bases: [`ParamNonRepeated`](#keysight.ads.de.db.ParamNonRepeated "keysight.ads.de.db._parameters.ParamNonRepeated")

    A parameter that consists of one or more sub-parameters.

    The sub-parameters may be accessed via sub\_params.

    *property* display\_value*: list[str]*[](#keysight.ads.de.db.ParamCompound.display_value "Link to this definition")

    evaluate(*expr\_context: [ExpressionContext](#keysight.ads.de.db.ExpressionContext "keysight.ads.de.db._parameters.ExpressionContext")*) → list[bool | int | float | str][](#keysight.ads.de.db.ParamCompound.evaluate "Link to this definition")
    :   Evaluate this compound parameter value.

    evaluate\_no\_expr() → list[str][](#keysight.ads.de.db.ParamCompound.evaluate_no_expr "Link to this definition")
    :   Prepare this compound parameter value for use by removing quotes and evaluating units.

        Does not support expressions.
        Will raise an exception if the value has an arithmetic expression
        or references other parameters or variables.

    *property* fields*: list[[Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")]*[](#keysight.ads.de.db.ParamCompound.fields "Link to this definition")
    :   list(sub\_params)

        Type:
        :   fields is deprecated, and will be removed in the 2025 Update 2 release. Use

    get\_field(*index: int*) → [Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")[](#keysight.ads.de.db.ParamCompound.get_field "Link to this definition")
    :   Return the sub-parameter at the specified index.

        get\_field is deprecated, and will be removed in the 2025 Update 2 release. Use: sub\_params[index]

    *property* netlist\_value*: list[str]*[](#keysight.ads.de.db.ParamCompound.netlist_value "Link to this definition")

    *property* num\_fields*: int*[](#keysight.ads.de.db.ParamCompound.num_fields "Link to this definition")
    :   len(sub\_params)

        Type:
        :   num\_fields is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* sub\_params*: \_SubParamCollection*[](#keysight.ads.de.db.ParamCompound.sub_params "Link to this definition")

    *property* value*: list[str]*[](#keysight.ads.de.db.ParamCompound.value "Link to this definition")

*class* keysight.ads.de.db.ParamItem[](#keysight.ads.de.db.ParamItem "Link to this definition")
:   Base class for parameter items.

    See also `de.db.ModelParam` which is the parameter definition.
    The classes derived from ParamItem are used for default values in ModelParam
    and to hold instance and terminal parameter values.

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.ParamItem.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    clone() → [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")[](#keysight.ads.de.db.ParamItem.clone "Link to this definition")

    *property* form\_name*: str*[](#keysight.ads.de.db.ParamItem.form_name "Link to this definition")

    *static* is\_compound(*p: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → TypeGuard[[ParamItemCompound](#keysight.ads.de.db.ParamItemCompound "keysight.ads.de.db._parameters.ParamItemCompound")][](#keysight.ads.de.db.ParamItem.is_compound "Link to this definition")

    *static* is\_const(*p: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → TypeGuard[[ParamItemConst](#keysight.ads.de.db.ParamItemConst "keysight.ads.de.db._parameters.ParamItemConst")][](#keysight.ads.de.db.ParamItem.is_const "Link to this definition")

    *static* is\_null(*p: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → TypeGuard[[ParamItemNull](#keysight.ads.de.db.ParamItemNull "keysight.ads.de.db._parameters.ParamItemNull")][](#keysight.ads.de.db.ParamItem.is_null "Link to this definition")

    *static* is\_repeated(*p: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → TypeGuard[[ParamItemRepeated](#keysight.ads.de.db.ParamItemRepeated "keysight.ads.de.db._parameters.ParamItemRepeated")][](#keysight.ads.de.db.ParamItem.is_repeated "Link to this definition")

    *static* is\_string(*p: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → TypeGuard[[ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString")][](#keysight.ads.de.db.ParamItem.is_string "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.ParamItem.name "Link to this definition")

    *property* no\_plot*: bool*[](#keysight.ads.de.db.ParamItem.no_plot "Link to this definition")
    :   When True, this parameter will not be displayed in schematic view.

*class* keysight.ads.de.db.ParamItemCompound[](#keysight.ads.de.db.ParamItemCompound "Link to this definition")
:   Bases: [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")

    A parameter item that consists one or more sub-parameters.

    The number of sub-parameters must match the number of sub-parameters on the
    compound form that is used to create the parameter definition.

    \_\_init\_\_(*param\_name: str*, *form\_name: str*, *subparams: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → None[](#keysight.ads.de.db.ParamItemCompound.__init__ "Link to this definition")

    get\_sub\_parameter(*index: int*) → [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")[](#keysight.ads.de.db.ParamItemCompound.get_sub_parameter "Link to this definition")
    :   get\_sub\_parameter is deprecated, and will be removed in the 2025 Update 2 release. Use sub\_params[index]

    get\_sub\_parameters() → Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")][](#keysight.ads.de.db.ParamItemCompound.get_sub_parameters "Link to this definition")
    :   get\_sub\_parameters is deprecated, and will be removed in the 2025 Update 2 release. Use: list(sub\_params)

    *property* has\_sub\_parameters*: bool*[](#keysight.ads.de.db.ParamItemCompound.has_sub_parameters "Link to this definition")
    :   len(sub\_params) > 0

        Type:
        :   has\_sub\_parameters is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* number\_of\_sub\_parameters*: int*[](#keysight.ads.de.db.ParamItemCompound.number_of_sub_parameters "Link to this definition")
    :   len(sub\_params)

        Type:
        :   number\_of\_sub\_parameters is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* sub\_params*: IndexedSettableCollectionAbc[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*[](#keysight.ads.de.db.ParamItemCompound.sub_params "Link to this definition")

    *property* value*: list[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*[](#keysight.ads.de.db.ParamItemCompound.value "Link to this definition")
    :   sub\_params

        Type:
        :   value is deprecated, and will be removed in the 2025 Update 2 release. Use

*class* keysight.ads.de.db.ParamItemConst[](#keysight.ads.de.db.ParamItemConst "Link to this definition")
:   Bases: [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")

    A parameter item whose value is determined by its form - (see `de.db.ConstForm`).

    \_\_init\_\_(*param\_name: str*) → None[](#keysight.ads.de.db.ParamItemConst.__init__ "Link to this definition")

    \_\_init\_\_(*param\_name: str*, *form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → None

*class* keysight.ads.de.db.ParamItemNull[](#keysight.ads.de.db.ParamItemNull "Link to this definition")
:   Bases: [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")

    A parameter item with no value.

    \_\_init\_\_(*param\_name: str*) → None[](#keysight.ads.de.db.ParamItemNull.__init__ "Link to this definition")

    *property* value*: None*[](#keysight.ads.de.db.ParamItemNull.value "Link to this definition")

*class* keysight.ads.de.db.ParamItemRepeated[](#keysight.ads.de.db.ParamItemRepeated "Link to this definition")
:   Bases: [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")

    A parameter item that holds a list of one or more repeats.

    The parameter definition’s formset dictates the forms that can be used for each repeat.
    A repeat cannot also be repeated but may use compound forms, having their own sub-parameters.

    \_\_init\_\_(*param\_name: str*, *repeats: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → None[](#keysight.ads.de.db.ParamItemRepeated.__init__ "Link to this definition")

    append\_repeat(*param: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → None[](#keysight.ads.de.db.ParamItemRepeated.append_repeat "Link to this definition")
    :   append\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.append(param)

    append\_repeats(*params: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → None[](#keysight.ads.de.db.ParamItemRepeated.append_repeats "Link to this definition")
    :   append\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.append(params)

    clear\_and\_set\_repeats(*parameters: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → None[](#keysight.ads.de.db.ParamItemRepeated.clear_and_set_repeats "Link to this definition")
    :   clear\_and\_set\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats = parameters

    clear\_and\_set\_single\_repeat(*parameter: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → None[](#keysight.ads.de.db.ParamItemRepeated.clear_and_set_single_repeat "Link to this definition")
    :   clear\_and\_set\_single\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats = parameter

    extract\_repeat(*index: int*) → [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")[](#keysight.ads.de.db.ParamItemRepeated.extract_repeat "Link to this definition")
    :   extract\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.pop(index)

    get\_repeat(*index: int*) → [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")[](#keysight.ads.de.db.ParamItemRepeated.get_repeat "Link to this definition")
    :   get\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats[index]

    get\_repeats() → Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")][](#keysight.ads.de.db.ParamItemRepeated.get_repeats "Link to this definition")
    :   get\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use: list(repeats)

    *property* has\_repeats*: bool*[](#keysight.ads.de.db.ParamItemRepeated.has_repeats "Link to this definition")
    :   len(repeats) > 0

        Type:
        :   has\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use

    insert\_repeat(*index: int*, *param: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → None[](#keysight.ads.de.db.ParamItemRepeated.insert_repeat "Link to this definition")
    :   insert\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.insert(index, param)

    *property* number\_of\_repeats*: int*[](#keysight.ads.de.db.ParamItemRepeated.number_of_repeats "Link to this definition")
    :   len(repeats)

        Type:
        :   number\_of\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* repeats*: \_RepeatParamItemCollection*[](#keysight.ads.de.db.ParamItemRepeated.repeats "Link to this definition")

    *property* value*: list[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*[](#keysight.ads.de.db.ParamItemRepeated.value "Link to this definition")
    :   list(repeats)

        Type:
        :   value is deprecated, and will be removed in the 2025 Update 2 release. Use

*class* keysight.ads.de.db.ParamItemString[](#keysight.ads.de.db.ParamItemString "Link to this definition")
:   Bases: [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")

    A string-valued parameter item.

    \_\_init\_\_(*param\_name: str*) → None[](#keysight.ads.de.db.ParamItemString.__init__ "Link to this definition")

    \_\_init\_\_(*param\_name: str*, *form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*, *param\_value: str*) → None

    *property* value*: str*[](#keysight.ads.de.db.ParamItemString.value "Link to this definition")

*class* keysight.ads.de.db.ParamIter[](#keysight.ads.de.db.ParamIter "Link to this definition")
:   An iterator that can be used to visit parameters of an instance or terminal.

    \_\_init\_\_(*owner: InstanceDbu | InstanceUu*) → None[](#keysight.ads.de.db.ParamIter.__init__ "Link to this definition")

    \_\_init\_\_(*owner: TermBaseDbu | TermBaseUu*) → None

    *property* definition*: [ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")*[](#keysight.ads.de.db.ParamIter.definition "Link to this definition")

    *property* is\_valid*: bool*[](#keysight.ads.de.db.ParamIter.is_valid "Link to this definition")

    *property* item*: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*[](#keysight.ads.de.db.ParamIter.item "Link to this definition")

    *property* value*: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*[](#keysight.ads.de.db.ParamIter.value "Link to this definition")

*class* keysight.ads.de.db.ParamNonRepeated[](#keysight.ads.de.db.ParamNonRepeated "Link to this definition")
:   Bases: [`ParamBase`](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")

    Non-repeated parameters are either Param or ParamCompound.

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.ParamNonRepeated.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* display\_value*: str | list[str]*[](#keysight.ads.de.db.ParamNonRepeated.display_value "Link to this definition")

    evaluate(*expr\_context: [ExpressionContext](#keysight.ads.de.db.ExpressionContext "keysight.ads.de.db._parameters.ExpressionContext")*) → bool | int | float | str | list[bool | int | float | str][](#keysight.ads.de.db.ParamNonRepeated.evaluate "Link to this definition")
    :   Evaluate this parameter value.

    evaluate\_no\_expr() → str | list[str][](#keysight.ads.de.db.ParamNonRepeated.evaluate_no_expr "Link to this definition")
    :   Prepare this parameter value for use by removing quotes and evaluating units.

        Does not support expressions.
        Will raise an exception if the value has an arithmetic expression
        or references other parameters or variables.

    *property* netlist\_value*: str | list[str]*[](#keysight.ads.de.db.ParamNonRepeated.netlist_value "Link to this definition")

    *property* value*: str | list[str]*[](#keysight.ads.de.db.ParamNonRepeated.value "Link to this definition")

*class* keysight.ads.de.db.ParamRepeated[](#keysight.ads.de.db.ParamRepeated "Link to this definition")
:   Bases: [`ParamBase`](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")

    A parameter that is essentially a vector of parameters of the same definition.

    The repeats of a repeated parameter must be non-repeating.
    There must always be at least one repeat.

    append\_repeat(*value: str | Sequence[str]*) → None[](#keysight.ads.de.db.ParamRepeated.append_repeat "Link to this definition")
    :   append\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.append(value)

    delete\_repeat(*index: int*) → None[](#keysight.ads.de.db.ParamRepeated.delete_repeat "Link to this definition")
    :   delete\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.remove(index)

    *property* display\_value*: list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamRepeated.display_value "Link to this definition")

    evaluate(*expr\_context: [ExpressionContext](#keysight.ads.de.db.ExpressionContext "keysight.ads.de.db._parameters.ExpressionContext")*) → list[bool | int | float | str] | list[list[bool | int | float | str]][](#keysight.ads.de.db.ParamRepeated.evaluate "Link to this definition")
    :   Evaluate this repeated parameter value.

    evaluate\_no\_expr() → str | list[str] | list[list[str]][](#keysight.ads.de.db.ParamRepeated.evaluate_no_expr "Link to this definition")
    :   Prepare this repeated parameter value for use by removing quotes and evaluating units.

        Does not support expressions.
        Will raise an exception if the value has an arithmetic expression
        or references other parameters or variables.

    get\_repeat(*index: int*) → [ParamNonRepeated](#keysight.ads.de.db.ParamNonRepeated "keysight.ads.de.db._parameters.ParamNonRepeated")[](#keysight.ads.de.db.ParamRepeated.get_repeat "Link to this definition")
    :   get\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats[index]

    insert\_repeat(*index: int*, *value: str | Sequence[str]*) → None[](#keysight.ads.de.db.ParamRepeated.insert_repeat "Link to this definition")
    :   insert\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.insert(index, value)

    *property* netlist\_value*: list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamRepeated.netlist_value "Link to this definition")

    *property* num\_repeats*: int*[](#keysight.ads.de.db.ParamRepeated.num_repeats "Link to this definition")
    :   len(repeats)

        Type:
        :   num\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* repeats*: \_RepeatParamCollection*[](#keysight.ads.de.db.ParamRepeated.repeats "Link to this definition")

    *property* value*: list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamRepeated.value "Link to this definition")

*class* keysight.ads.de.db.TimeParam[](#keysight.ads.de.db.TimeParam "Link to this definition")
:   \_\_init\_\_(*time: int*) → None[](#keysight.ads.de.db.TimeParam.__init__ "Link to this definition")

    *property* time*: int*[](#keysight.ads.de.db.TimeParam.time "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.db.ModelParamType[](#keysight.ads.de.db.ModelParamType "Link to this definition")
:   REAL *= 'real'*[](#keysight.ads.de.db.ModelParamType.REAL "Link to this definition")

    STRING *= 'string'*[](#keysight.ads.de.db.ModelParamType.STRING "Link to this definition")

    INT *= 'int'*[](#keysight.ads.de.db.ModelParamType.INT "Link to this definition")

    COMPLEX *= 'complex'*[](#keysight.ads.de.db.ModelParamType.COMPLEX "Link to this definition")

    REAL\_ARRAY *= 'realArray'*[](#keysight.ads.de.db.ModelParamType.REAL_ARRAY "Link to this definition")

    INT\_ARRAY *= 'intArray'*[](#keysight.ads.de.db.ModelParamType.INT_ARRAY "Link to this definition")

    STRING\_ARRAY *= 'stringArray'*[](#keysight.ads.de.db.ModelParamType.STRING_ARRAY "Link to this definition")

    COMPLEX\_ARRAY *= 'complexArray'*[](#keysight.ads.de.db.ModelParamType.COMPLEX_ARRAY "Link to this definition")

    FIXED\_POINT *= 'fixed'*[](#keysight.ads.de.db.ModelParamType.FIXED_POINT "Link to this definition")

    FIXED\_POINT\_ARRAY *= 'fixedArray'*[](#keysight.ads.de.db.ModelParamType.FIXED_POINT_ARRAY "Link to this definition")

    PRECISION\_STRING *= 'precision'*[](#keysight.ads.de.db.ModelParamType.PRECISION_STRING "Link to this definition")

    UNSPECIFIED *= 'unspecified'*[](#keysight.ads.de.db.ModelParamType.UNSPECIFIED "Link to this definition")

*class* keysight.ads.de.db.ModelUnitType[](#keysight.ads.de.db.ModelUnitType "Link to this definition")
:   STRING *= 'string'*[](#keysight.ads.de.db.ModelUnitType.STRING "Link to this definition")

    NO\_UNIT *= 'num'*[](#keysight.ads.de.db.ModelUnitType.NO_UNIT "Link to this definition")

    FREQUENCY *= 'freq'*[](#keysight.ads.de.db.ModelUnitType.FREQUENCY "Link to this definition")

    RESISTANCE *= 'res'*[](#keysight.ads.de.db.ModelUnitType.RESISTANCE "Link to this definition")

    CONDUCTANCE *= 'cond'*[](#keysight.ads.de.db.ModelUnitType.CONDUCTANCE "Link to this definition")

    INDUCTANCE *= 'ind'*[](#keysight.ads.de.db.ModelUnitType.INDUCTANCE "Link to this definition")

    CAPACITANCE *= 'cap'*[](#keysight.ads.de.db.ModelUnitType.CAPACITANCE "Link to this definition")

    LENGTH *= 'lng'*[](#keysight.ads.de.db.ModelUnitType.LENGTH "Link to this definition")

    TIME *= 'time'*[](#keysight.ads.de.db.ModelUnitType.TIME "Link to this definition")

    ANGLE *= 'ang'*[](#keysight.ads.de.db.ModelUnitType.ANGLE "Link to this definition")

    POWER *= 'power'*[](#keysight.ads.de.db.ModelUnitType.POWER "Link to this definition")

    VOLTAGE *= 'volt'*[](#keysight.ads.de.db.ModelUnitType.VOLTAGE "Link to this definition")

    CURRENT *= 'cur'*[](#keysight.ads.de.db.ModelUnitType.CURRENT "Link to this definition")

    DISTANCE *= 'dist'*[](#keysight.ads.de.db.ModelUnitType.DISTANCE "Link to this definition")

    TEMPERATURE *= 'temp'*[](#keysight.ads.de.db.ModelUnitType.TEMPERATURE "Link to this definition")

    DB\_GAIN *= 'dbg'*[](#keysight.ads.de.db.ModelUnitType.DB_GAIN "Link to this definition")

    DATARATE *= 'datarate'*[](#keysight.ads.de.db.ModelUnitType.DATARATE "Link to this definition")

    PERCENT *= 'pct'*[](#keysight.ads.de.db.ModelUnitType.PERCENT "Link to this definition")

*class* keysight.ads.de.db.OAParamType[](#keysight.ads.de.db.OAParamType "Link to this definition")
:   The type of an OAParam.

    INT *= <OAParamType.INT: 0>*[](#keysight.ads.de.db.OAParamType.INT "Link to this definition")

    FLOAT *= <OAParamType.FLOAT: 1>*[](#keysight.ads.de.db.OAParamType.FLOAT "Link to this definition")

    STRING *= <OAParamType.STRING: 2>*[](#keysight.ads.de.db.OAParamType.STRING "Link to this definition")

    APP\_PARAM *= <OAParamType.APP\_PARAM: 3>*[](#keysight.ads.de.db.OAParamType.APP_PARAM "Link to this definition")
    :   Application defined parameter holding typed data.

    DOUBLE *= <OAParamType.DOUBLE: 4>*[](#keysight.ads.de.db.OAParamType.DOUBLE "Link to this definition")

    BOOLEAN *= <OAParamType.BOOLEAN: 5>*[](#keysight.ads.de.db.OAParamType.BOOLEAN "Link to this definition")

    TIME *= <OAParamType.TIME: 6>*[](#keysight.ads.de.db.OAParamType.TIME "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.de.db.add\_variable\_to\_var\_instance(*instance: InstanceDbu | InstanceUu*, *name: str*, *value: str*) → None[](#keysight.ads.de.db.add_variable_to_var_instance "Link to this definition")

keysight.ads.de.db.compound\_param(*form\_name: str*, *sub\_params: Sequence[[ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString") | [ParamItemConst](#keysight.ads.de.db.ParamItemConst "keysight.ads.de.db._parameters.ParamItemConst")]*) → [ParamItemCompound](#keysight.ads.de.db.ParamItemCompound "keysight.ads.de.db._parameters.ParamItemCompound")[](#keysight.ads.de.db.compound_param "Link to this definition")

keysight.ads.de.db.const\_param(*form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → [ParamItemConst](#keysight.ads.de.db.ParamItemConst "keysight.ads.de.db._parameters.ParamItemConst")[](#keysight.ads.de.db.const_param "Link to this definition")

keysight.ads.de.db.get\_ui\_indexed\_parameter\_ui\_string(*instance: InstanceDbu | InstanceUu*, *index: int*) → str[](#keysight.ads.de.db.get_ui_indexed_parameter_ui_string "Link to this definition")

keysight.ads.de.db.make\_compound\_param(*form\_name: str*, *sub\_params: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → [ParamItemCompound](#keysight.ads.de.db.ParamItemCompound "keysight.ads.de.db._parameters.ParamItemCompound")[](#keysight.ads.de.db.make_compound_param "Link to this definition")
:   make\_compound\_param is deprecated, and will be removed in the 2025 Update 2 release. Use: compound\_param

keysight.ads.de.db.make\_const\_param(*form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → [ParamItemConst](#keysight.ads.de.db.ParamItemConst "keysight.ads.de.db._parameters.ParamItemConst")[](#keysight.ads.de.db.make_const_param "Link to this definition")
:   make\_const\_param is deprecated, and will be removed in the 2025 Update 2 release. Use: const\_param

keysight.ads.de.db.make\_repeated\_param(*repeats: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → [ParamItemRepeated](#keysight.ads.de.db.ParamItemRepeated "keysight.ads.de.db._parameters.ParamItemRepeated")[](#keysight.ads.de.db.make_repeated_param "Link to this definition")
:   make\_repeated\_param is deprecated, and will be removed in the 2025 Update 2 release. Use: repeated\_param

keysight.ads.de.db.make\_string\_param(*form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*, *value: str*) → [ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString")[](#keysight.ads.de.db.make_string_param "Link to this definition")
:   make\_string\_param is deprecated, and will be removed in the 2025 Update 2 release. Use: string\_param or std\_string\_param

keysight.ads.de.db.repeated\_param(*repeats: Sequence[[ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString") | [ParamItemConst](#keysight.ads.de.db.ParamItemConst "keysight.ads.de.db._parameters.ParamItemConst") | [ParamItemCompound](#keysight.ads.de.db.ParamItemCompound "keysight.ads.de.db._parameters.ParamItemCompound")]*) → [ParamItemRepeated](#keysight.ads.de.db.ParamItemRepeated "keysight.ads.de.db._parameters.ParamItemRepeated")[](#keysight.ads.de.db.repeated_param "Link to this definition")

keysight.ads.de.db.std\_string\_param(*value: str*) → [ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString")[](#keysight.ads.de.db.std_string_param "Link to this definition")
:   Make a ParamItemString using the StdForm.

keysight.ads.de.db.string\_param(*form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*, *value: str*) → [ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString")[](#keysight.ads.de.db.string_param "Link to this definition")

keysight.ads.de.db.update\_pcell\_params\_and\_maybe\_relocate\_in\_layout(*instance: InstanceDbu | InstanceUu*, *hierarchy\_context: [DesignHierarchy](../design_hierarchy.md#keysight.ads.de.DesignHierarchy "keysight.ads.de._core.design_hierarchy.DesignHierarchy")*) → None[](#keysight.ads.de.db.update_pcell_params_and_maybe_relocate_in_layout "Link to this definition")

On this page

[Previous

Model Definition](model_def.md)
[Next

Properties](properties.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top