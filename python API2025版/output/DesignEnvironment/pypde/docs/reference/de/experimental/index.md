<!-- 来源: pypde\docs\reference\de\experimental\index.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* keysight.ads.de.experimental

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
    - keysight.ads.de.experimental
      * [CDF](cdf/index.md)
      * [Commands](commands.md)
      * [Handles](handles.md)
      * [Netlist Utilities](netlist_helper.md)
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

# keysight.ads.de.experimental[](#module-keysight.ads.de.experimental "Link to this heading")

Experimental additions to the API.

* [CDF](cdf/index.md)
  + [Classes](cdf/index.md#classes)
    - [`CDFBase`](cdf/index.md#keysight.ads.de.experimental.cdf.CDFBase)
    - [`CellCDF`](cdf/index.md#keysight.ads.de.experimental.cdf.CellCDF)
    - [`InstanceParams`](cdf/index.md#keysight.ads.de.experimental.cdf.InstanceParams)
    - [`LibraryCDF`](cdf/index.md#keysight.ads.de.experimental.cdf.LibraryCDF)
    - [`ManagedCDF`](cdf/index.md#keysight.ads.de.experimental.cdf.ManagedCDF)
    - [`ParamDef`](cdf/index.md#keysight.ads.de.experimental.cdf.ParamDef)
    - [`ScratchCDF`](cdf/index.md#keysight.ads.de.experimental.cdf.ScratchCDF)
    - [`SimInfo`](cdf/index.md#keysight.ads.de.experimental.cdf.SimInfo)
    - [`ViewInfo`](cdf/index.md#keysight.ads.de.experimental.cdf.ViewInfo)
  + [Enumerated Types](cdf/index.md#enumerated-types)
    - [`ParamType`](cdf/index.md#keysight.ads.de.experimental.cdf.ParamType)
    - [`ParamUnits`](cdf/index.md#keysight.ads.de.experimental.cdf.ParamUnits)
  + [Functions](cdf/index.md#functions)
    - [`cell_cdf()`](cdf/index.md#keysight.ads.de.experimental.cdf.cell_cdf)
    - [`find_cell_cdf()`](cdf/index.md#keysight.ads.de.experimental.cdf.find_cell_cdf)
    - [`find_library_cdf()`](cdf/index.md#keysight.ads.de.experimental.cdf.find_library_cdf)
    - [`library_cdf()`](cdf/index.md#keysight.ads.de.experimental.cdf.library_cdf)
* [Commands](commands.md)
  + [Classes](commands.md#classes)
    - [`DesignTrackingPainter`](commands.md#keysight.ads.de.experimental.commands.DesignTrackingPainter)
    - [`CommandInfo`](commands.md#keysight.ads.de.experimental.commands.CommandInfo)
  + [Functions](commands.md#functions)
    - [`start_design_command()`](commands.md#keysight.ads.de.experimental.commands.start_design_command)
* [Handles](handles.md)
  + [Classes](handles.md#classes)
    - [`Handle`](handles.md#keysight.ads.de.experimental.handles.Handle)
    - [`DesignWidget`](handles.md#keysight.ads.de.experimental.handles.DesignWidget)
  + [Enumerated Types](handles.md#enumerated-types)
    - [`HandleType`](handles.md#keysight.ads.de.experimental.handles.HandleType)
  + [Functions](handles.md#functions)
    - [`create_custom_handle_for_instance()`](handles.md#keysight.ads.de.experimental.handles.create_custom_handle_for_instance)
    - [`register_handle_generator()`](handles.md#keysight.ads.de.experimental.handles.register_handle_generator)
    - [`unregister_handle_generators_for_library()`](handles.md#keysight.ads.de.experimental.handles.unregister_handle_generators_for_library)
* [Netlist Utilities](netlist_helper.md)
  + [Classes](netlist_helper.md#classes)
    - [`NetlistStringBuilder`](netlist_helper.md#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder)
* [Polygon Utilities](polygon_utils.md)
  + [Classes](polygon_utils.md#classes)
    - [`Oversizer`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.Oversizer)
    - [`PolygonOversizer`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.PolygonOversizer)
    - [`PolygonVertexToArcConverter`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.PolygonVertexToArcConverter)
    - [`ShapeOversizer`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.ShapeOversizer)
    - [`ShapeVertexToArcConverter`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.ShapeVertexToArcConverter)
    - [`VertexToArcConverter`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter)
  + [Functions](polygon_utils.md#functions)
    - [`convert_vertices_to_arcs()`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.convert_vertices_to_arcs)
    - [`oversize()`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.oversize)
* [Preferences](preferences.md)
  + [Enumerated Types](preferences.md#enumerated-types)
    - [`WorkspacePreference`](preferences.md#keysight.ads.de.experimental.preferences.WorkspacePreference)
    - [`LibSpecificPreference`](preferences.md#keysight.ads.de.experimental.preferences.LibSpecificPreference)
* [xxPro View](pro_view.md)
  + [Functions](pro_view.md#functions)
    - [`create_pro_view()`](pro_view.md#keysight.ads.de.experimental.pro_view.create_pro_view)
* [Symbol Generator](symbol.md)
  + [Classes](symbol.md#classes)
    - [`SymbolGenerator`](symbol.md#keysight.ads.de.experimental.generate_symbol.SymbolGenerator)
  + [Enumerated Types](symbol.md#enumerated-types)
    - [`OrderType`](symbol.md#keysight.ads.de.experimental.generate_symbol.OrderType)
* [Text Maker](text_maker.md)
  + [Classes](text_maker.md#classes)
    - [`TextMaker`](text_maker.md#keysight.ads.de.experimental.text_maker.TextMaker)

On this page

[Previous

LineTypeInfo](../db_uu/line_type_info.md)
[Next

CDF](cdf/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top