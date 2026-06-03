<!-- 来源: pypde\docs\reference\de\db\model_def.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.db](index.md)
* Model Definition

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
      * Model Definition
      * [Parameters](parameters.md)
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

# Model Definition[](#model-definition "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.ModelDef[](#keysight.ads.de.db.ModelDef "Link to this definition")
:   A model definition implemented in Python.

    \_\_init\_\_(*name: str*, *label: str*) → None[](#keysight.ads.de.db.ModelDef.__init__ "Link to this definition")
    :   Construct a ModelDef.

        Parameters:
        :   * **name** (*str*) – The name of the item, for a cell definition, this is the cell name
            * **label** (*str*) – Display label, e.g. “Resistor”

*class* keysight.ads.de.db.ModelDefAEL[](#keysight.ads.de.db.ModelDefAEL "Link to this definition")
:   A model definition implemented in AEL.

*class* keysight.ads.de.db.ModelDefBase[](#keysight.ads.de.db.ModelDefBase "Link to this definition")
:   A model definition, sometimes referred to as an item definition or component definition, contains the parameter definitions for a particular component or design.

    append\_parameter(*parameter: [ModelParam](#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")*) → None[](#keysight.ads.de.db.ModelDefBase.append_parameter "Link to this definition")
    :   append\_parameter is deprecated, and will be removed in the 2025 Update 2 release. Use: parameters.append(name)

    *property* callbacks*: ListRefAbc[[ModelCbBase](callbacks.md#keysight.ads.de.db.ModelCbBase "keysight.ads.de.db._callbacks.ModelCbBase")]*[](#keysight.ads.de.db.ModelDefBase.callbacks "Link to this definition")
    :   Return the collection of callbacks in this model definition.

    *property* component\_name*: str*[](#keysight.ads.de.db.ModelDefBase.component_name "Link to this definition")

    delete\_parameter(*index: int*) → None[](#keysight.ads.de.db.ModelDefBase.delete_parameter "Link to this definition")
    :   delete\_parameter is deprecated, and will be removed in the 2025 Update 2 release. Use: del(parameters[index])

    *static* find\_model\_def(*libOrCell: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *cellName: str*) → [ModelDefBase](#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db._model_def.ModelDefBase") | None[](#keysight.ads.de.db.ModelDefBase.find_model_def "Link to this definition")

    *static* find\_model\_def(*libOrCell: [Cell](../cell.md#keysight.ads.de.Cell "keysight.ads.de._core.cell.Cell")*) → [ModelDefBase](#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db._model_def.ModelDefBase") | None

    *property* has\_model\_param*: bool*[](#keysight.ads.de.db.ModelDefBase.has_model_param "Link to this definition")
    :   A model definition with has\_model\_param set to True will netlist the first parameter as the model name.

        See the [Model Definition Properties](../../../examples/ex_model.md#model-definition-properties) section in the ADS Python Design Environment documentation.

    insert\_parameter(*parameter: [ModelParam](#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")*, *index: int*) → None[](#keysight.ads.de.db.ModelDefBase.insert_parameter "Link to this definition")
    :   insert\_parameter is deprecated, and will be removed in the 2025 Update 2 release. Use: parameters.insert(index, parameter)

    *property* inst\_name\_prefix*: str*[](#keysight.ads.de.db.ModelDefBase.inst_name_prefix "Link to this definition")

    *property* is\_bom\_item*: bool*[](#keysight.ads.de.db.ModelDefBase.is_bom_item "Link to this definition")

    *property* is\_custom\_variable*: bool*[](#keysight.ads.de.db.ModelDefBase.is_custom_variable "Link to this definition")

    *property* is\_ground*: bool*[](#keysight.ads.de.db.ModelDefBase.is_ground "Link to this definition")

    *property* is\_smart\_component*: bool*[](#keysight.ads.de.db.ModelDefBase.is_smart_component "Link to this definition")

    *property* is\_sub\_design*: bool*[](#keysight.ads.de.db.ModelDefBase.is_sub_design "Link to this definition")

    *property* is\_transmission\_line*: bool*[](#keysight.ads.de.db.ModelDefBase.is_transmission_line "Link to this definition")

    *property* is\_unique*: bool*[](#keysight.ads.de.db.ModelDefBase.is_unique "Link to this definition")
    :   Only one instance of this model is allowed in a design.

    *property* is\_variable*: bool*[](#keysight.ads.de.db.ModelDefBase.is_variable "Link to this definition")

    *property* label*: str*[](#keysight.ads.de.db.ModelDefBase.label "Link to this definition")

    *property* legacy\_dialog\_data*: str*[](#keysight.ads.de.db.ModelDefBase.legacy_dialog_data "Link to this definition")

    *property* legacy\_dialog\_name*: str*[](#keysight.ads.de.db.ModelDefBase.legacy_dialog_name "Link to this definition")

    *property* library\_name*: str*[](#keysight.ads.de.db.ModelDefBase.library_name "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.ModelDefBase.name "Link to this definition")

    *property* parameters*: NamedListRefAbc[[ModelParam](#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")]*[](#keysight.ads.de.db.ModelDefBase.parameters "Link to this definition")
    :   Return the collection of parameter definitions in this model definition.

        A parameter definition may be accessed by using the [] operator.
        Use parameters.find to find a parameter by name.

*class* keysight.ads.de.db.ModelParam[](#keysight.ads.de.db.ModelParam "Link to this definition")
:   ModelParam is a parameter definition that is a part of a model definition (see `de.db.ModelDef`).

    Parameter values have associated forms (see `de.db.Form`).
    The allowed forms for a given parameter are listed in its formset (see `de.db.Formset`)

    \_\_init\_\_(*name: str*, *label: str*, *formset: [Formset](forms.md#keysight.ads.de.db.Formset "keysight.ads.de.db.Formset") | None = None*, *unit\_type: [ModelUnitType](parameters.md#keysight.ads.de.db.ModelUnitType "keysight.ads.de.db.ModelUnitType") | str | None = None*, *param\_type: [ModelParamType](parameters.md#keysight.ads.de.db.ModelParamType "keysight.ads.de.db.ModelParamType") | str | None = None*) → None[](#keysight.ads.de.db.ModelParam.__init__ "Link to this definition")
    :   Initialize a ModelParam.

        Parameters:
        :   * **name** (*str*) – Name of the parameter
            * **label** (*str*) – Descriptive label for the parameter
            * **formset** ([*Formset*](forms.md#keysight.ads.de.db.Formset "keysight.ads.de.db.Formset")) – A Formset is a list of one or more [`Form`](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db.Form") that describe how the parameter
              is stored, how it is netlisted and how it is displayed on a schematic
              If not specified, the global StdFormSet will be used.
            * **unit\_type** (*Optional**[*[*ModelUnitType*](parameters.md#keysight.ads.de.db.ModelUnitType "keysight.ads.de.db.ModelUnitType")*]*) – The units of the parameter, defaults to NO\_UNIT (plain numbers)
            * **param\_type** (*Optional**[*[*ModelParamType*](parameters.md#keysight.ads.de.db.ModelParamType "keysight.ads.de.db.ModelParamType")*]*) – The datatype of the parameter value, defaults to REAL

    *property* callbacks*: ListRefAbc[[ModelCbBase](callbacks.md#keysight.ads.de.db.ModelCbBase "keysight.ads.de.db._callbacks.ModelCbBase")]*[](#keysight.ads.de.db.ModelParam.callbacks "Link to this definition")
    :   Return the collection of callbacks in this parameter definition.

    *property* default\_value*: [ParamItem](parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem") | None*[](#keysight.ads.de.db.ModelParam.default_value "Link to this definition")

    find\_parameter\_form(*param: [ParamItem](parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem")*) → [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db.Form") | None[](#keysight.ads.de.db.ModelParam.find_parameter_form "Link to this definition")
    :   find\_parameter\_form is deprecated, and will be removed in the 2025 Update 2 release. Use: formset.forms.find(param.form\_name)

    find\_parameter\_form\_by\_name(*name: str*) → [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db.Form") | None[](#keysight.ads.de.db.ModelParam.find_parameter_form_by_name "Link to this definition")
    :   find\_parameter\_form\_by\_name is deprecated, and will be removed in the 2025 Update 2 release. Use: formset.forms.find(name)

    *property* forms*: Sequence[[Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db.Form")]*[](#keysight.ads.de.db.ModelParam.forms "Link to this definition")
    :   formset.forms

        Type:
        :   forms is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* formset*: [Formset](forms.md#keysight.ads.de.db.Formset "keysight.ads.de.db.Formset")*[](#keysight.ads.de.db.ModelParam.formset "Link to this definition")

    get\_default\_value\_copy(*design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*, *model\_definition: [ModelDefBase](#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db.ModelDefBase")*) → [ParamItem](parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem")[](#keysight.ads.de.db.ModelParam.get_default_value_copy "Link to this definition")
    :   Get a copy of the default value, invoking the callback if one exists.

    *property* is\_constant*: bool*[](#keysight.ads.de.db.ModelParam.is_constant "Link to this definition")

    *property* is\_design\_name*: bool*[](#keysight.ads.de.db.ModelParam.is_design_name "Link to this definition")

    *property* is\_discrete\_value*: bool*[](#keysight.ads.de.db.ModelParam.is_discrete_value "Link to this definition")

    *property* is\_displayed\_by\_default*: bool*[](#keysight.ads.de.db.ModelParam.is_displayed_by_default "Link to this definition")

    *property* is\_doe*: bool*[](#keysight.ads.de.db.ModelParam.is_doe "Link to this definition")

    *property* is\_editable*: bool*[](#keysight.ads.de.db.ModelParam.is_editable "Link to this definition")

    *property* is\_evaluated*: bool*[](#keysight.ads.de.db.ModelParam.is_evaluated "Link to this definition")

    *property* is\_ignored\_by\_pcell*: bool*[](#keysight.ads.de.db.ModelParam.is_ignored_by_pcell "Link to this definition")

    *property* is\_netlist\_rhs\_only*: bool*[](#keysight.ads.de.db.ModelParam.is_netlist_rhs_only "Link to this definition")

    *property* is\_netlistable*: bool*[](#keysight.ads.de.db.ModelParam.is_netlistable "Link to this definition")

    *property* is\_not\_netlisted\_at\_definition*: bool*[](#keysight.ads.de.db.ModelParam.is_not_netlisted_at_definition "Link to this definition")

    *property* is\_on\_screen\_editable*: bool*[](#keysight.ads.de.db.ModelParam.is_on_screen_editable "Link to this definition")

    *property* is\_optimizable*: bool*[](#keysight.ads.de.db.ModelParam.is_optimizable "Link to this definition")

    *property* is\_repeated*: bool*[](#keysight.ads.de.db.ModelParam.is_repeated "Link to this definition")

    *property* is\_statistical*: bool*[](#keysight.ads.de.db.ModelParam.is_statistical "Link to this definition")

    *property* label*: str*[](#keysight.ads.de.db.ModelParam.label "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.ModelParam.name "Link to this definition")

    *property* param\_type*: [ModelParamType](parameters.md#keysight.ads.de.db.ModelParamType "keysight.ads.de.db.ModelParamType")*[](#keysight.ads.de.db.ModelParam.param_type "Link to this definition")

    *property* unit\_type*: [ModelUnitType](parameters.md#keysight.ads.de.db.ModelUnitType "keysight.ads.de.db.ModelUnitType")*[](#keysight.ads.de.db.ModelParam.unit_type "Link to this definition")

On this page

[Previous

GenPolyline](genpolyline.md)
[Next

Parameters](parameters.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top