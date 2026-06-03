<!-- 来源: pypde\docs\reference\de\db\callbacks.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.db](index.md)
* Callbacks

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
      * Callbacks
      * [Enumerated Types](enums.md)
      * [Parameter Forms](forms.md)
      * [GenPolyline](genpolyline.md)
      * [Model Definition](model_def.md)
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

# Callbacks[](#callbacks "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.ModelCb[](#keysight.ads.de.db.ModelCb "Link to this definition")
:   Bases: [`ModelCbBase`](#keysight.ads.de.db.ModelCbBase "keysight.ads.de.db._callbacks.ModelCbBase")

    A model callback that is implemented in Python.

    \_\_init\_\_(*callback\_type: Literal[ModelCbType.PARAMETER\_DEFAULT\_VALUE]*, *callback: Callable[['ModelParam', 'ModelDefBase', 'Design'], 'ParamItem']*) → None[](#keysight.ads.de.db.ModelCb.__init__ "Link to this definition")

    \_\_init\_\_(*callback\_type: Literal[ModelCbType.PARAMETER\_MODIFIED]*, *callback: Callable[['ItemInfo'], bool]*) → None

    \_\_init\_\_(*callback\_type: Literal[ModelCbType.ITEM\_NETLIST]*, *callback: Callable[[[StandardInstance](#keysight.ads.de.db.StandardInstance "keysight.ads.de.db._callbacks.StandardInstance")], str]*) → None

    \_\_init\_\_(*callback\_type: Literal[ModelCbType.ITEM\_MODIFIED]*, *callback: Callable[['Instance'], None]*) → None
    :   Initialize a callback.

        callback\_typeModelCbType
        :   **ModelCbType.PARAMETER\_DEFAULT\_VALUE** :
            Override the default value set in [`ModelParam.default_value`](model_def.md#keysight.ads.de.db.ModelParam.default_value "keysight.ads.de.db.ModelParam.default_value").
            Return a [`ParamItem`](parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem")

            **ModelCbType.PARAMETER\_MODIFIED** :
            Called when a parameter has been modified.
            Return True if dependent parameter data had been modified.

            **ModelCbType.ITEM\_NETLIST** :
            Called when generating a netlist.
            Return the netlist string

            **ModelCbType.ITEM\_MODIFIED** :
            Called when this item has been modified.
            Return None

        callback : The user-supplied function to call

*class* keysight.ads.de.db.ModelCbAEL[](#keysight.ads.de.db.ModelCbAEL "Link to this definition")
:   Bases: [`ModelCbBase`](#keysight.ads.de.db.ModelCbBase "keysight.ads.de.db._callbacks.ModelCbBase")

    A model callback that is implemented in AEL.

    \_\_init\_\_(*callback\_type: [ModelCbType](#keysight.ads.de.db.ModelCbType "keysight.ads.de.db._callbacks.ModelCbType")*, *vocabulary: str*, *function: str*, *client\_data: object*, *enabled: bool = True*) → None[](#keysight.ads.de.db.ModelCbAEL.__init__ "Link to this definition")

    *property* function\_name*: str*[](#keysight.ads.de.db.ModelCbAEL.function_name "Link to this definition")

    get\_client\_data\_string(*format\_strings: bool*) → str[](#keysight.ads.de.db.ModelCbAEL.get_client_data_string "Link to this definition")

    *property* vocabulary*: str*[](#keysight.ads.de.db.ModelCbAEL.vocabulary "Link to this definition")

*class* keysight.ads.de.db.ModelCbBase[](#keysight.ads.de.db.ModelCbBase "Link to this definition")
:   Base class for callbacks used by model definitions and model parameters.

    See `de.db.ModelParam` and `de.db.ModelDef`.
    Each callback function can be implemented in Python or AEL.

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.ModelCbBase.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* enabled*: bool*[](#keysight.ads.de.db.ModelCbBase.enabled "Link to this definition")

    *property* type*: [ModelCbType](#keysight.ads.de.db.ModelCbType "keysight.ads.de.db._callbacks.ModelCbType")*[](#keysight.ads.de.db.ModelCbBase.type "Link to this definition")

*class* keysight.ads.de.db.NetlistInstance[](#keysight.ads.de.db.NetlistInstance "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.NetlistInstance.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* instance\_name*: str*[](#keysight.ads.de.db.NetlistInstance.instance_name "Link to this definition")

    *property* instance\_name\_for\_netlist*: str*[](#keysight.ads.de.db.NetlistInstance.instance_name_for_netlist "Link to this definition")

    *property* netlisted\_master\_name*: str*[](#keysight.ads.de.db.NetlistInstance.netlisted_master_name "Link to this definition")

    *property* nodes*: list[[NetlistNode](#keysight.ads.de.db.NetlistNode "keysight.ads.de.db._callbacks.NetlistNode")]*[](#keysight.ads.de.db.NetlistInstance.nodes "Link to this definition")

    *property* parent\_design*: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design") | None*[](#keysight.ads.de.db.NetlistInstance.parent_design "Link to this definition")

    *property* parent\_design\_name*: str*[](#keysight.ads.de.db.NetlistInstance.parent_design_name "Link to this definition")

*class* keysight.ads.de.db.NetlistNode[](#keysight.ads.de.db.NetlistNode "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.NetlistNode.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* is\_grounded*: bool*[](#keysight.ads.de.db.NetlistNode.is_grounded "Link to this definition")

    *property* node\_name*: str*[](#keysight.ads.de.db.NetlistNode.node_name "Link to this definition")

    *property* pin\_name*: str*[](#keysight.ads.de.db.NetlistNode.pin_name "Link to this definition")

    *property* pin\_number*: int*[](#keysight.ads.de.db.NetlistNode.pin_number "Link to this definition")

*class* keysight.ads.de.db.StandardInstance[](#keysight.ads.de.db.StandardInstance "Link to this definition")
:   Bases: [`NetlistInstance`](#keysight.ads.de.db.NetlistInstance "keysight.ads.de.db._callbacks.NetlistInstance")

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.StandardInstance.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* instance*: [Instance](../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*[](#keysight.ads.de.db.StandardInstance.instance "Link to this definition")

    *property* model\_def*: [ModelDefBase](model_def.md#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db.ModelDefBase") | None*[](#keysight.ads.de.db.StandardInstance.model_def "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.db.ModelCbType[](#keysight.ads.de.db.ModelCbType "Link to this definition")
:   An enumeration specifying the purpose of a parameter callback.

    PARAMETER\_DEFAULT\_VALUE *= <ModelCbType.PARM\_DEFAULT\_VALUE\_CB: 0>*[](#keysight.ads.de.db.ModelCbType.PARAMETER_DEFAULT_VALUE "Link to this definition")
    :   This type of callback returns a design specific default parameter value.

    PARAMETER\_MODIFIED *= <ModelCbType.PARM\_MODIFIED\_CB: 1>*[](#keysight.ads.de.db.ModelCbType.PARAMETER_MODIFIED "Link to this definition")
    :   This type of callback is called whenever a specific parameter is modified.

    ITEM\_NETLIST *= <ModelCbType.ITEM\_NETLIST\_CB: 3>*[](#keysight.ads.de.db.ModelCbType.ITEM_NETLIST "Link to this definition")
    :   This type of callback returns a custom netlist string.

    ITEM\_MODIFIED *= <ModelCbType.ITEM\_MODIFIED\_CB: 8>*[](#keysight.ads.de.db.ModelCbType.ITEM_MODIFIED "Link to this definition")
    :   This type of callback is called whenever a specific item is modified.

## Functions[](#functions "Link to this heading")

keysight.ads.de.db.invoke\_parameter\_changed\_callback(*instance: [Instance](../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*, *parameter\_names: Sequence[str]*) → None[](#keysight.ads.de.db.invoke_parameter_changed_callback "Link to this definition")

On this page

[Previous

keysight.ads.de.db](index.md)
[Next

Enumerated Types](enums.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top