<!-- 来源: pypde\docs\reference\de\experimental\_autosummary\keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.html -->

[![Logo](../../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../../index.md)
* [Reference](../../../../../../reference.md)
* [Design Environment](../../../index.md)
* [keysight.ads.de.experimental](../index.md)
* [Netlist Utilities](../netlist_helper.md)
* NetlistStringBuilder

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../../../../../../pydocs/intro/index.md)
* [How-To](../../../../../../pydocs/howto/index.md)
  + [Use Python in the ADS Application](../../../../../../pydocs/howto/embedded.md)
  + [Set Up a Python Virtual Environment](../../../../../../pydocs/howto/venv.md)
  + [Set Up Visual Studio Code for Development](../../../../../../pydocs/howto/vscode.md)
  + [Use Pytest](../../../../../../pydocs/howto/pytest.md)
  + [Enable Python Support For Your Library](../../../../../../pydocs/howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../../../../../../pydocs/howto/execution.md)
  + [Export Workspace and Design Objects to Python](../../../../../../pydocs/howto/exporter.md)
  + [Record Actions in ADS as Python Code](../../../../../../pydocs/howto/recorder.md)
  + [Develop a Python Pcell in ADS](../../../../../../pydocs/howto/pcell.md)
* [ADS Concepts](../../../../../../pydocs/concepts/index.md)
  + [Workspace Elements](../../../../../../pydocs/concepts/workspace_elements.md)
  + [Connectivity Objects](../../../../../../pydocs/concepts/connectivity.md)
* [Reference](../../../../../../reference.md)
  + [Deprecated APIs](../../../../../../pydocs/py/_generated/deprecations.md)
  + [Design Environment](../../../index.md)
    - [keysight.ads.de](../../index.md)
      * [ADS Application Environment](../../ads_environment.md)
      * [ADS Workspace Components](../../workspace_components.md)
      * [Design Hierarchy](../../design_hierarchy.md)
      * [Smart Package](../../package.md)
      * [Geometry](../../geometry.md)
      * [Collections](../../collections.md)
      * [Printer](../../printer.md)
    - [keysight.ads.de.ael](../../ael.md)
    - [keysight.ads.de.app](../../app/index.md)
      * [Application](../../app/application.md)
      * [Actions and Menus](../../app/action.md)
      * [Addons](../../app/addon.md)
      * [Window and Design Callbacks](../../app/callbacks.md)
      * [Windows and Widgets](../../app/window.md)
      * [Experimental](../../app/experimental.md)
    - [keysight.ads.de.app.dds](../../app/dds.md)
      * [exec\_python](../../app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../db/index.md)
      * [Models, Parameters, and Forms](../../db/parameters.md)
      * [Properties](../../db/properties.md)
      * [Preferences](../../db/preferences.md)
      * [Transaction](../../db/transaction.md)
      * [Smart Mount](../../db/smart_mount.md)
      * [Geometry](../../db/geometry.md)
      * [Teardrops](../../db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../db_dbu/index.md)
      * [DbBox](../../db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../db_uu/index.md)
      * [Database Objects](../../db_uu/database_objects.md)
      * [Iterators](../../db_uu/iterators.md)
      * [Designs](../../db_uu/design.md)
      * [Teardrops](../../db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../index.md)
      * [CDF](../cdf.md)
      * [Design Commands](../commands.md)
      * [Component Handles](../handles.md)
      * [Netlist Utilities](../netlist_helper.md)
      * [Polygon Utilities](../polygon_utils.md)
      * [xxPro View](../pro_view.md)
      * [Symbol Generator](../symbol.md)
      * [Text Maker](../text_maker.md)
      * [Notebook](../notebook.md)
      * [Layer/Purpose Pairs](../lpp.md)
    - [keysight.ads.de.tech](../../tech/index.md)
      * [Technology](../../tech/tech.md)
      * [Layers](../../tech/layers.md)
      * [Line Items](../../tech/line_items.md)
      * [Padstacks](../../tech/pads.md)
      * [Rules](../../tech/rule.md)
  + [Substrate](../../../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../../../../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../../../../../examples.md)
  + [Design Environment](../../../../examples/index.md)
    - [Workspace Creation](../../../../examples/workspace/ex_workspace.md)
    - [Design Creation](../../../../examples/design_creation/index.md)
      * [Create Layout](../../../../examples/design_creation/ex_create_layout.md)
      * [Create Schematic](../../../../examples/design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../../../../examples/design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../../../../examples/design_elements/index.md)
      * [Placing Text](../../../../examples/design_elements/ex_place_text.md)
      * [Moving Objects](../../../../examples/design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../../../../examples/design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../../../../examples/design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../../../../examples/design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../../../../examples/design_elements/ex_plane_editing.md)
    - [Parameters](../../../../examples/parameters/index.md)
      * [Interoperable Component Parameters](../../../../examples/parameters/ex_cdf.md)
      * [Working with VAR](../../../../examples/parameters/ex_working_with_var.md)
      * [Component Parameters](../../../../examples/parameters/ex_parameters.md)
      * [Creating an Item Definition](../../../../examples/parameters/ex_itemdef.md)
      * [Model Definition Properties](../../../../examples/parameters/ex_model.md)
      * [Creating a Text Form](../../../../examples/parameters/ex_text_form.md)
      * [Properties](../../../../examples/parameters/ex_properties.md)
    - [Technology](../../../../examples/technology/index.md)
      * [Padstacks and Vias](../../../../examples/technology/ex_padstack.md)
      * [Nested Technology](../../../../examples/technology/ex_nested.md)
      * [Rules](../../../../examples/technology/ex_rules.md)
    - [Translators](../../../../examples/translators/index.md)
      * [DXF Import and Export](../../../../examples/translators/ex_translate_dxf.md)
      * [Gerber Export](../../../../examples/translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../../../../examples/translators/ex_translate_gds.md)
    - [UI](../../../../examples/ui/index.md)
      * [Creating Custom Menus Using an Addon](../../../../examples/ui/ex_menu_addon.md)
      * [PySide](../../../../examples/ui/ex_pyside.md)
    - [Utility](../../../../examples/utility/index.md)
      * [Calling Between AEL and Python](../../../../examples/utility/ex_calling_ael_and_python.md)
      * [Smart Package](../../../../examples/utility/ex_smart_pkg.md)
      * [XML RPC](../../../../examples/utility/ex_xml_rpc.md)
  + [Substrate](../../../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../../../../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../../../../../genindex.md)

# NetlistStringBuilder[](#netliststringbuilder "Link to this heading")

*class* NetlistStringBuilder[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder "Link to this definition")
:   Bases: `object`

    Methods

    |  |  |
    | --- | --- |
    | [`__init__`](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.__init__ "keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.__init__")(instance) | Class to help with creating a custom netlist string for use in a netlist callback. |
    | [`append_connectivity`](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_connectivity "keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_connectivity")() |  |
    | [`append_instance_name`](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_instance_name "keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_instance_name")() |  |
    | [`append_model_and_instance_name`](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_model_and_instance_name "keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_model_and_instance_name")() | Append the model and instance name with a : separator (<model\_name:instance\_name>). |
    | [`append_model_name`](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_model_name "keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_model_name")() |  |
    | [`append_parameter`](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_parameter "keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_parameter")(param\_name) |  |
    | [`append_parameters`](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_parameters "keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_parameters")() |  |
    | [`append_str`](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_str "keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_str")(to\_append) | Append a custom string. |
    | [`clear`](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.clear "keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.clear")() | Clear any previously created string. |
    | [`clear_and_get_default_netlist_str`](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.clear_and_get_default_netlist_str "keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.clear_and_get_default_netlist_str")() | Clear out any existing string and return the default netlist string. |

    Attributes

    |  |  |
    | --- | --- |
    | [`netlist_str`](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.netlist_str "keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.netlist_str") | The built-up netlist string; default is an empty string. |

    \_\_init\_\_(*instance: [StandardInstance](../../db/_autosummary/keysight.ads.de.db.StandardInstance.md#keysight.ads.de.db.StandardInstance "keysight.ads.de.db._callbacks.StandardInstance")*) → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.__init__ "Link to this definition")
    :   Class to help with creating a custom netlist string for use in a netlist callback.

        Provides methods for adding the model name, instance name, connectivity, parameters, and
        custom strings.

        instance: The StandardInstance passed to the netlist callback

    clear() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.clear "Link to this definition")
    :   Clear any previously created string.

    append\_str(*to\_append: str*) → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_str "Link to this definition")
    :   Append a custom string.

    append\_model\_name() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_model_name "Link to this definition")

    append\_instance\_name() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_instance_name "Link to this definition")

    append\_model\_and\_instance\_name() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_model_and_instance_name "Link to this definition")
    :   Append the model and instance name with a : separator (<model\_name:instance\_name>).

        Equivalent to calling:

        ```
        append_model_name()
        append_str(":")
        append_instance_name()
        ```

    append\_connectivity() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_connectivity "Link to this definition")

    append\_parameters() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_parameters "Link to this definition")

    append\_parameter(*param\_name: str*) → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_parameter "Link to this definition")

    clear\_and\_get\_default\_netlist\_str() → str[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.clear_and_get_default_netlist_str "Link to this definition")
    :   Clear out any existing string and return the default netlist string.

        This function will use the format string associated with the component.
        If no format string has been defined, will use an internally defined default
        format string, functionally equivalent to the below:

        ```
        builder.clear()
        builder.append_model_name()
        builder.append_str(":")
        builder.append_instance_name()
        builder.append_connectivity()
        builder.append_parameters()
        netlist_str = builder.netlist_str

        # OR:
        builder.clear()
        builder.append_model_and_instance_name()
        builder.append_connectivity()
        builder.append_parameters()
        netlist_str = builder.netlist_str
        ```

    *property* netlist\_str*: str*[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.netlist_str "Link to this definition")
    :   The built-up netlist string; default is an empty string.

On this page

[Previous

Netlist Utilities](../netlist_helper.md)
[Next

Polygon Utilities](../polygon_utils.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top