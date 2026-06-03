<!-- 来源: pypde\docs\reference\de\db\index.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* keysight.ads.de.db

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
    - keysight.ads.de.db
      * [Callbacks](callbacks.md)
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

# keysight.ads.de.db[](#module-keysight.ads.de.db "Link to this heading")

Database module.

Contains classes that are independent of database units.
See also ..db\_uu and ..db\_dbu.

## Classes[](#classes "Link to this heading")

* [Callbacks](callbacks.md)
  + [Classes](callbacks.md#classes)
  + [Enumerated Types](callbacks.md#enumerated-types)
  + [Functions](callbacks.md#functions)
* [Enumerated Types](enums.md)
  + [`AttrType`](enums.md#keysight.ads.de.db.AttrType)
  + [`DesignAttrType`](enums.md#keysight.ads.de.db.DesignAttrType)
  + [`DesignMode`](enums.md#keysight.ads.de.db.DesignMode)
  + [`InstAttrType`](enums.md#keysight.ads.de.db.InstAttrType)
  + [`InstTermAttrType`](enums.md#keysight.ads.de.db.InstTermAttrType)
  + [`NetAttrType`](enums.md#keysight.ads.de.db.NetAttrType)
  + [`Orientation`](enums.md#keysight.ads.de.db.Orientation)
  + [`SignalType`](enums.md#keysight.ads.de.db.SignalType)
  + [`TermAttrType`](enums.md#keysight.ads.de.db.TermAttrType)
  + [`TermType`](enums.md#keysight.ads.de.db.TermType)
  + [`TextAlignment`](enums.md#keysight.ads.de.db.TextAlignment)
  + [`TextDisplayFormat`](enums.md#keysight.ads.de.db.TextDisplayFormat)
* [Parameter Forms](forms.md)
  + [Classes](forms.md#classes)
  + [Functions](forms.md#functions)
* [GenPolyline](genpolyline.md)
  + [Classes](genpolyline.md#classes)
  + [Enumerated Types](genpolyline.md#enumerated-types)
* [Model Definition](model_def.md)
  + [Classes](model_def.md#classes)
* [Parameters](parameters.md)
  + [Classes](parameters.md#classes)
  + [Enumerated Types](parameters.md#enumerated-types)
  + [Functions](parameters.md#functions)
* [Properties](properties.md)
  + [Classes](properties.md#classes)
  + [Enumerated Types](properties.md#enumerated-types)
* [Transaction](transaction.md)
  + [Classes](transaction.md#classes)
  + [Enumerated Types](transaction.md#enumerated-types)

On this page

[Previous

Windows and Widgets](../app/window.md)
[Next

Callbacks](callbacks.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top