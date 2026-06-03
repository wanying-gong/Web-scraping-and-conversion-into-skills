<!-- 来源: pypde\docs\reference\de\experimental\netlist_helper.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.experimental](index.md)
* Netlist Utilities

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
    - [keysight.ads.de.db](../db/index.md)
      * [Callbacks](../db/callbacks.md)
      * [Enumerated Types](../db/enums.md)
      * [Parameter Forms](../db/forms.md)
      * [GenPolyline](../db/genpolyline.md)
      * [Model Definition](../db/model_def.md)
      * [Parameters](../db/parameters.md)
      * [Properties](../db/properties.md)
      * [Transaction](../db/transaction.md)
    - [keysight.ads.de.db\_dbu](../db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../db_uu/index.md)
      * [Design Elements](../db_uu/db_uu.md)
      * [LayerId](../db_uu/layer_id.md)
      * [LineTypeInfo](../db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](index.md)
      * [CDF](cdf/index.md)
      * [Commands](commands.md)
      * [Handles](handles.md)
      * Netlist Utilities
      * [Polygon Utilities](polygon_utils.md)
      * [Preferences](preferences.md)
      * [xxPro View](pro_view.md)
      * [Symbol Generator](symbol.md)
      * [Text Maker](text_maker.md)
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

# Netlist Utilities[](#module-keysight.ads.de.experimental.netlist_helper "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.netlist\_helper.NetlistStringBuilder[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder "Link to this definition")
:   \_\_init\_\_(*instance: [StandardInstance](../db/callbacks.md#keysight.ads.de.db.StandardInstance "keysight.ads.de.db._callbacks.StandardInstance")*) → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.__init__ "Link to this definition")
    :   Class to help with creating a custom netlist string for use in a netlist callback.

        Provides methods for adding the model name, instance name, connectivity, parameters, and
        custom strings.

        instance: The StandardInstance passed to the netlist callback

    append\_connectivity() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_connectivity "Link to this definition")

    append\_instance\_name() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_instance_name "Link to this definition")

    append\_model\_and\_instance\_name() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_model_and_instance_name "Link to this definition")
    :   Append the model and instance name with a : separator (<model\_name:instance\_name>).

        Equivalent to calling:
        append\_model\_name()
        append\_str(“:”)
        append\_instance\_name()

    append\_model\_name() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_model_name "Link to this definition")

    append\_parameter(*param\_name: str*) → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_parameter "Link to this definition")

    append\_parameters() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_parameters "Link to this definition")

    append\_str(*to\_append: str*) → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_str "Link to this definition")
    :   Append a custom string.

    clear() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.clear "Link to this definition")
    :   Clear any previously created string.

    clear\_and\_get\_default\_netlist\_str() → str[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.clear_and_get_default_netlist_str "Link to this definition")
    :   Clear out any existing string and return the default netlist string.

        This function will use the format string associated with the component.
        If no format string has been defined, will use an internally defined default
        format string, functionally equivalent to the below:

        builder.clear()
        builder.append\_model\_name()
        builder.append\_str(“:”)
        builder.append\_instance\_name()
        builder.append\_connectivity()
        builder.append\_parameters()
        netlist\_str = builder.netlist\_str

        OR:
        builder.clear()
        builder.append\_model\_and\_instance\_name()
        builder.append\_connectivity()
        builder.append\_parameters()
        netlist\_str = builder.netlist\_str

    *property* netlist\_str*: str*[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.netlist_str "Link to this definition")
    :   The built-up netlist string; default is an empty string.

On this page

[Previous

Handles](handles.md)
[Next

Polygon Utilities](polygon_utils.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top