<!-- 来源: pypde\docs\reference\de\db_dbu\index.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* keysight.ads.de.db\_dbu

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
    - keysight.ads.de.db\_dbu
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

# keysight.ads.de.db\_dbu[](#keysight-ads-de-db-dbu "Link to this heading")

The classes and functions defined in the [keysight.ads.de.db\_uu](../db_uu/index.md) and keysight.ads.de.db\_dbu packages are largely identical but are differentiated by units; user units (uu) and database units (dbu).

See the [keysight.ads.de.db\_uu](../db_uu/index.md) package for the API definition that is available in both the keysight.ads.de.db\_uu and keysight.ads.de.db\_dbu packages.

Database module using integer database units without conversion.

## Classes[](#classes "Link to this heading")

> *class* keysight.ads.de.db\_dbu.DbBox[](#keysight.ads.de.db_dbu.DbBox "Link to this definition")
> :   Bases: `object`
>
>     \_\_init\_\_(*x1: int | None = None*, *y1: int | None = None*, *x2: int | None = None*, *y2: int | None = None*, *lower\_left: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU") | None = None*, *upper\_right: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU") | None = None*) → None[](#keysight.ads.de.db_dbu.DbBox.__init__ "Link to this definition")
>
>     contains\_box(*box: [DbBox](#keysight.ads.de.db_dbu.DbBox "keysight.ads.de.db_dbu._db_box.DbBox")*) → bool[](#keysight.ads.de.db_dbu.DbBox.contains_box "Link to this definition")
>
>     contains\_coordinates(*x: int*, *y: int*) → bool[](#keysight.ads.de.db_dbu.DbBox.contains_coordinates "Link to this definition")
>
>     contains\_point(*point: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*) → bool[](#keysight.ads.de.db_dbu.DbBox.contains_point "Link to this definition")
>
>     *property* has\_zero\_area*: bool*[](#keysight.ads.de.db_dbu.DbBox.has_zero_area "Link to this definition")
>
>     *property* is\_degenerate*: bool*[](#keysight.ads.de.db_dbu.DbBox.is_degenerate "Link to this definition")
>
>     *property* lower\_left*: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*[](#keysight.ads.de.db_dbu.DbBox.lower_left "Link to this definition")
>
>     *property* lower\_right*: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*[](#keysight.ads.de.db_dbu.DbBox.lower_right "Link to this definition")
>
>     overlaps(*box: [DbBox](#keysight.ads.de.db_dbu.DbBox "keysight.ads.de.db_dbu._db_box.DbBox")*) → bool[](#keysight.ads.de.db_dbu.DbBox.overlaps "Link to this definition")
>
>     *property* upper\_left*: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*[](#keysight.ads.de.db_dbu.DbBox.upper_left "Link to this definition")
>
>     *property* upper\_right*: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*[](#keysight.ads.de.db_dbu.DbBox.upper_right "Link to this definition")
>
>     *property* x1*: int*[](#keysight.ads.de.db_dbu.DbBox.x1 "Link to this definition")
>
>     *property* x2*: int*[](#keysight.ads.de.db_dbu.DbBox.x2 "Link to this definition")
>
>     *property* y1*: int*[](#keysight.ads.de.db_dbu.DbBox.y1 "Link to this definition")
>
>     *property* y2*: int*[](#keysight.ads.de.db_dbu.DbBox.y2 "Link to this definition")

On this page

[Previous

Transaction](../db/transaction.md)
[Next

keysight.ads.de.db\_uu](../db_uu/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top