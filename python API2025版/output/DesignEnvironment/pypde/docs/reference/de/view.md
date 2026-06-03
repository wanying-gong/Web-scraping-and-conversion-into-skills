<!-- 来源: pypde\docs\reference\de\view.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Design](../../index.md)
* [Reference](../index.md)
* [keysight.ads.de](index.md)
* View

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

* [Introduction](../../../../pydocs/intro/index.md)
  + [Licensing](../../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../../pydocs/intro/extension.md)
* [Concepts](../../../../pydocs/concepts/index.md)
  + [Terminology](../../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../../pydocs/concepts/execution.md)
* [How-To](../../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../../pydocs/howto/pytest.md)

* [Design](../../index.md)
  + [Reference](../index.md)
    - [keysight.ads.de](index.md)
      * [Workspace](workspace.md)
      * [Library](library.md)
      * [Cell](cell.md)
      * View
      * [CellviewRef](cellviewref.md)
      * [DesignHierarchy](design_hierarchy.md)
      * [DMData](dmdata.md)
      * [ItemInfo](item_info.md)
      * [Points](points.md)
      * [Collections](collections.md)
    - [keysight.ads.de.ael](ael.md)
    - [keysight.ads.de.app](app/index.md)
      * [Actions and Menus](app/action.md)
      * [Addons](app/addon.md)
      * [Callbacks](app/callbacks.md)
      * [Windows and Widgets](app/window.md)
    - [keysight.ads.de.db](db/index.md)
      * [Callbacks](db/callbacks.md)
      * [Enumerated Types](db/enums.md)
      * [Parameter Forms](db/forms.md)
      * [GenPolyline](db/genpolyline.md)
      * [Model Definition](db/model_def.md)
      * [Parameters](db/parameters.md)
      * [Properties](db/properties.md)
      * [Transaction](db/transaction.md)
    - [keysight.ads.de.db\_dbu](db_dbu/index.md)
    - [keysight.ads.de.db\_uu](db_uu/index.md)
      * [Design Elements](db_uu/db_uu.md)
      * [LayerId](db_uu/layer_id.md)
      * [LineTypeInfo](db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](experimental/index.md)
      * [CDF](experimental/cdf/index.md)
      * [Commands](experimental/commands.md)
      * [Handles](experimental/handles.md)
      * [Netlist Utilities](experimental/netlist_helper.md)
      * [Polygon Utilities](experimental/polygon_utils.md)
      * [Preferences](experimental/preferences.md)
      * [xxPro View](experimental/pro_view.md)
      * [Symbol Generator](experimental/symbol.md)
      * [Text Maker](experimental/text_maker.md)
    - [keysight.ads.de.tech](tech/index.md)
      * [Tech](tech/tech.md)
      * [Padstacks](tech/pads/pads.md)
      * [Via Rules](tech/rule/rule.md)
      * [Nested Technology](tech/nested/nested.md)
    - [keysight.ads.de.app.dds](app/dds.md)
  + [Examples](../../examples/index.md)
    - [Calling Between AEL and Python](../../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../examples/ex_create_layout.md)
    - [Create Schematic](../../examples/ex_create_schematic.md)
    - [Create Workspace](../../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../examples/ex_cdf.md)
    - [Component Parameters](../../examples/ex_parameters.md)
    - [Creating an Item Definition](../../examples/ex_itemdef.md)
    - [Model Definition Properties](../../examples/ex_model.md)
    - [Adding Instances to a Design](../../examples/ex_lpf.md)
    - [Properties](../../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../examples/ex_padstack.md)
    - [Nested Technology](../../examples/ex_nested.md)
    - [Rules](../../examples/ex_rules.md)
    - [Placing Text](../../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../examples/ex_polygon.md)
    - [PySide2](../../examples/ex_pyside.md)
    - [Traversing Hierarchy](../../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../examples/ex_working_with_var.md)
    - [XML RPC](../../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../examples/ex_translate_gds.md)
* [Technology](../../../../pysubst/docs/index.md)
  + [Reference](../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# View[](#view "Link to this heading")

*class* keysight.ads.de.View[](#keysight.ads.de.View "Link to this definition")
:   \_\_init\_\_(*lib: str*, *cell: str*, *view: str*) → None[](#keysight.ads.de.View.__init__ "Link to this definition")

    \_\_init\_\_(*lib: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library")*, *cell: str*, *view: str*) → None

    \_\_init\_\_(*\**, *cell: [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")*, *view: str*) → None
    :   \_\_init\_\_ is deprecated, and will be removed in the 2025 Update 2 release. Use View.get(cell, view\_name) or cell.view(view\_name).

    *property* cell*: [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")*[](#keysight.ads.de.View.cell "Link to this definition")

    *property* cell\_name*: str*[](#keysight.ads.de.View.cell_name "Link to this definition")

    delete\_dm\_data() → None[](#keysight.ads.de.View.delete_dm_data "Link to this definition")

    dm\_data(*mode: str*) → [DMData](dmdata.md#keysight.ads.de.DMData "keysight.ads.de.DMData")[](#keysight.ads.de.View.dm_data "Link to this definition")

    *static* get(*cell: [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")*, *view\_name: str*) → [View](#keysight.ads.de.View "keysight.ads.de.View")[](#keysight.ads.de.View.get "Link to this definition")

    get\_design(*mode: [DesignMode](db/enums.md#keysight.ads.de.db.DesignMode "keysight.ads.de.db._design_mode.DesignMode") = DesignMode.READ\_ONLY*) → [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")[](#keysight.ads.de.View.get_design "Link to this definition")

    *property* has\_dm\_data*: bool*[](#keysight.ads.de.View.has_dm_data "Link to this definition")

    *property* is\_any\_verilog\_view*: bool*[](#keysight.ads.de.View.is_any_verilog_view "Link to this definition")

    *property* is\_config\_view*: bool*[](#keysight.ads.de.View.is_config_view "Link to this definition")

    *property* is\_design\_view*: bool*[](#keysight.ads.de.View.is_design_view "Link to this definition")

    *property* is\_layout\_view*: bool*[](#keysight.ads.de.View.is_layout_view "Link to this definition")

    *property* is\_schematic\_view*: bool*[](#keysight.ads.de.View.is_schematic_view "Link to this definition")

    *property* is\_symbol\_view*: bool*[](#keysight.ads.de.View.is_symbol_view "Link to this definition")

    *property* is\_verilog\_view*: bool*[](#keysight.ads.de.View.is_verilog_view "Link to this definition")

    *property* is\_veriloga\_view*: bool*[](#keysight.ads.de.View.is_veriloga_view "Link to this definition")

    *property* is\_verilogams\_view*: bool*[](#keysight.ads.de.View.is_verilogams_view "Link to this definition")

    *property* lcv\_name*: str*[](#keysight.ads.de.View.lcv_name "Link to this definition")

    *property* lib\_name*: str*[](#keysight.ads.de.View.lib_name "Link to this definition")

    *property* library*: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library")*[](#keysight.ads.de.View.library "Link to this definition")

    module\_name() → str[](#keysight.ads.de.View.module_name "Link to this definition")
    :   Return the full name of the Python module for this View.

        Will raise an exception if this View does not have a Python module.

    *property* name*: str*[](#keysight.ads.de.View.name "Link to this definition")

    *property* path*: Path*[](#keysight.ads.de.View.path "Link to this definition")

    *property* view\_name*: str*[](#keysight.ads.de.View.view_name "Link to this definition")

    *property* view\_type\_name*: str*[](#keysight.ads.de.View.view_type_name "Link to this definition")

On this page

[Previous

Cell](cell.md)
[Next

CellviewRef](cellviewref.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top