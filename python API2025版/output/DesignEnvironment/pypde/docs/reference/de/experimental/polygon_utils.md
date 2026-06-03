<!-- 来源: pypde\docs\reference\de\experimental\polygon_utils.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.experimental](index.md)
* Polygon Utilities

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
      * Polygon Utilities
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

# Polygon Utilities[](#module-keysight.ads.de.experimental.polygon_utils "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.polygon\_utils.Oversizer[](#keysight.ads.de.experimental.polygon_utils.Oversizer "Link to this definition")
:   *property* minimum\_vertex\_distance*: float*[](#keysight.ads.de.experimental.polygon_utils.Oversizer.minimum_vertex_distance "Link to this definition")

    *property* miter\_angle\_degrees*: float*[](#keysight.ads.de.experimental.polygon_utils.Oversizer.miter_angle_degrees "Link to this definition")

    *property* oversize\_amount*: float*[](#keysight.ads.de.experimental.polygon_utils.Oversizer.oversize_amount "Link to this definition")

*class* keysight.ads.de.experimental.polygon\_utils.PolygonOversizer[](#keysight.ads.de.experimental.polygon_utils.PolygonOversizer "Link to this definition")
:   Bases: [`Oversizer`](#keysight.ads.de.experimental.polygon_utils.Oversizer "keysight.ads.de.experimental.polygon_utils.Oversizer")

    \_\_init\_\_(*polygon: [GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")*, *design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design") | None = None*, *oversize\_amount: float = 0.0*, *miter\_angle\_degrees: float = 0.0*, *minimum\_vertex\_distance: float = 0.0*)[](#keysight.ads.de.experimental.polygon_utils.PolygonOversizer.__init__ "Link to this definition")

    oversize() → list[[GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")][](#keysight.ads.de.experimental.polygon_utils.PolygonOversizer.oversize "Link to this definition")

*class* keysight.ads.de.experimental.polygon\_utils.PolygonVertexToArcConverter[](#keysight.ads.de.experimental.polygon_utils.PolygonVertexToArcConverter "Link to this definition")
:   Bases: [`VertexToArcConverter`](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter "keysight.ads.de.experimental.polygon_utils.VertexToArcConverter")

    \_\_init\_\_(*polygon: [GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")*, *design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design") | None = None*, *radius: float = 0.0*, *arc\_resolution\_degrees: float = 5.0*, *minimum\_vertex\_distance: float = 0.0*)[](#keysight.ads.de.experimental.polygon_utils.PolygonVertexToArcConverter.__init__ "Link to this definition")

    convert() → list[[GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")][](#keysight.ads.de.experimental.polygon_utils.PolygonVertexToArcConverter.convert "Link to this definition")

*class* keysight.ads.de.experimental.polygon\_utils.ShapeOversizer[](#keysight.ads.de.experimental.polygon_utils.ShapeOversizer "Link to this definition")
:   Bases: [`Oversizer`](#keysight.ads.de.experimental.polygon_utils.Oversizer "keysight.ads.de.experimental.polygon_utils.Oversizer")

    \_\_init\_\_(*shape: [Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")*, *oversizeAmount: float | None = None*, *miter\_angle\_degrees: float = 0.0*, *minimum\_vertex\_distance: float = 0.0*, *make\_copy: bool = False*)[](#keysight.ads.de.experimental.polygon_utils.ShapeOversizer.__init__ "Link to this definition")

    *property* make\_copy*: bool*[](#keysight.ads.de.experimental.polygon_utils.ShapeOversizer.make_copy "Link to this definition")

    oversize() → list[[Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")][](#keysight.ads.de.experimental.polygon_utils.ShapeOversizer.oversize "Link to this definition")

*class* keysight.ads.de.experimental.polygon\_utils.ShapeVertexToArcConverter[](#keysight.ads.de.experimental.polygon_utils.ShapeVertexToArcConverter "Link to this definition")
:   Bases: [`VertexToArcConverter`](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter "keysight.ads.de.experimental.polygon_utils.VertexToArcConverter")

    \_\_init\_\_(*shape: [Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")*, *radius: float | None = None*, *arc\_resolution\_degrees: float = 5.0*, *minimum\_vertex\_distance: float = 0.0*)[](#keysight.ads.de.experimental.polygon_utils.ShapeVertexToArcConverter.__init__ "Link to this definition")

    convert() → list[[Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")][](#keysight.ads.de.experimental.polygon_utils.ShapeVertexToArcConverter.convert "Link to this definition")

*class* keysight.ads.de.experimental.polygon\_utils.VertexToArcConverter[](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* arc\_resolution*: float*[](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter.arc_resolution "Link to this definition")

    *property* minimum\_vertex\_distance*: float*[](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter.minimum_vertex_distance "Link to this definition")

    *property* radius*: float*[](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter.radius "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.de.experimental.polygon\_utils.convert\_vertices\_to\_arcs(*shape: [Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")*, *radius: float = 0*) → list[[Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")][](#keysight.ads.de.experimental.polygon_utils.convert_vertices_to_arcs "Link to this definition")

keysight.ads.de.experimental.polygon\_utils.oversize(*shape: [Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")*, *oversize\_amount: float = 0*, *make\_copy: bool = False*) → list[[Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")][](#keysight.ads.de.experimental.polygon_utils.oversize "Link to this definition")

On this page

[Previous

Netlist Utilities](netlist_helper.md)
[Next

Preferences](preferences.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top