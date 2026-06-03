<!-- 来源: pypde\docs\reference\de\experimental\symbol.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.experimental](index.md)
* Symbol Generator

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
      * [Netlist Utilities](netlist_helper.md)
      * [Polygon Utilities](polygon_utils.md)
      * [Preferences](preferences.md)
      * [xxPro View](pro_view.md)
      * Symbol Generator
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

# Symbol Generator[](#module-keysight.ads.de.experimental.generate_symbol "Link to this heading")

Functions for Generate Symbol.

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.generate\_symbol.SymbolGenerator[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator "Link to this definition")
:   \_\_init\_\_(*symbol\_design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *source\_design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *lead\_len: float*, *lead\_spacing: float*)[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.__init__ "Link to this definition")

    generate\_symbol() → None[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.generate_symbol "Link to this definition")

    *property* is\_add\_ref\_pin*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_add_ref_pin "Link to this definition")

    *property* is\_dual\_symbol\_type*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_dual_symbol_type "Link to this definition")

    *property* is\_pin\_one\_warn\_off*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_pin_one_warn_off "Link to this definition")

    *property* is\_use\_one\_pin\_per\_em\_port*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_use_one_pin_per_em_port "Link to this definition")

    *property* is\_use\_pin\_net\_text\_label*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_use_pin_net_text_label "Link to this definition")

    *property* is\_use\_single\_line\_body*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_use_single_line_body "Link to this definition")

    *property* order*: [OrderType](#keysight.ads.de.experimental.generate_symbol.OrderType "keysight.ads.de.experimental.generate_symbol.OrderType")*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.order "Link to this definition")

    *property* pin\_shape*: str*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.pin_shape "Link to this definition")

    *property* should\_replace*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.should_replace "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.experimental.generate\_symbol.OrderType[](#keysight.ads.de.experimental.generate_symbol.OrderType "Link to this definition")
:   Bases: `Enum`

    ORDER\_LOCATION *= 0*[](#keysight.ads.de.experimental.generate_symbol.OrderType.ORDER_LOCATION "Link to this definition")

    ORDER\_NUMBER1 *= 1*[](#keysight.ads.de.experimental.generate_symbol.OrderType.ORDER_NUMBER1 "Link to this definition")

    ORDER\_NUMBER2 *= 2*[](#keysight.ads.de.experimental.generate_symbol.OrderType.ORDER_NUMBER2 "Link to this definition")

    ORDER\_NUMBER3 *= 3*[](#keysight.ads.de.experimental.generate_symbol.OrderType.ORDER_NUMBER3 "Link to this definition")

    ORDER\_NUMBER4 *= 4*[](#keysight.ads.de.experimental.generate_symbol.OrderType.ORDER_NUMBER4 "Link to this definition")

On this page

[Previous

xxPro View](pro_view.md)
[Next

Text Maker](text_maker.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top