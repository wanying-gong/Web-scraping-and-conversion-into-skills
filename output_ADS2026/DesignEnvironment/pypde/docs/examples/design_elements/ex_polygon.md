<!-- 来源: pypde\docs\examples\design_elements\ex_polygon.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Examples](../../../../examples.md)
* [Design Environment](../index.md)
* [Design Elements](index.md)
* Paths, Traces, and Polygons

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

* [Introduction](../../../../pydocs/intro/index.md)
* [How-To](../../../../pydocs/howto/index.md)
  + [Use Python in the ADS Application](../../../../pydocs/howto/embedded.md)
  + [Set Up a Python Virtual Environment](../../../../pydocs/howto/venv.md)
  + [Set Up Visual Studio Code for Development](../../../../pydocs/howto/vscode.md)
  + [Use Pytest](../../../../pydocs/howto/pytest.md)
  + [Enable Python Support For Your Library](../../../../pydocs/howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../../../../pydocs/howto/execution.md)
  + [Export Workspace and Design Objects to Python](../../../../pydocs/howto/exporter.md)
  + [Record Actions in ADS as Python Code](../../../../pydocs/howto/recorder.md)
  + [Develop a Python Pcell in ADS](../../../../pydocs/howto/pcell.md)
* [ADS Concepts](../../../../pydocs/concepts/index.md)
  + [Workspace Elements](../../../../pydocs/concepts/workspace_elements.md)
  + [Connectivity Objects](../../../../pydocs/concepts/connectivity.md)
* [Reference](../../../../reference.md)
  + [Deprecated APIs](../../../../pydocs/py/_generated/deprecations.md)
  + [Design Environment](../../reference/index.md)
    - [keysight.ads.de](../../reference/de/index.md)
      * [ADS Application Environment](../../reference/de/ads_environment.md)
      * [ADS Workspace Components](../../reference/de/workspace_components.md)
      * [Design Hierarchy](../../reference/de/design_hierarchy.md)
      * [Smart Package](../../reference/de/package.md)
      * [Geometry](../../reference/de/geometry.md)
      * [Collections](../../reference/de/collections.md)
      * [Printer](../../reference/de/printer.md)
    - [keysight.ads.de.ael](../../reference/de/ael.md)
    - [keysight.ads.de.app](../../reference/de/app/index.md)
      * [Application](../../reference/de/app/application.md)
      * [Actions and Menus](../../reference/de/app/action.md)
      * [Addons](../../reference/de/app/addon.md)
      * [Window and Design Callbacks](../../reference/de/app/callbacks.md)
      * [Windows and Widgets](../../reference/de/app/window.md)
      * [Experimental](../../reference/de/app/experimental.md)
    - [keysight.ads.de.app.dds](../../reference/de/app/dds.md)
      * [exec\_python](../../reference/de/app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../reference/de/db/index.md)
      * [Models, Parameters, and Forms](../../reference/de/db/parameters.md)
      * [Properties](../../reference/de/db/properties.md)
      * [Preferences](../../reference/de/db/preferences.md)
      * [Transaction](../../reference/de/db/transaction.md)
      * [Smart Mount](../../reference/de/db/smart_mount.md)
      * [Geometry](../../reference/de/db/geometry.md)
      * [Teardrops](../../reference/de/db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../reference/de/db_dbu/index.md)
      * [DbBox](../../reference/de/db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../reference/de/db_uu/index.md)
      * [Database Objects](../../reference/de/db_uu/database_objects.md)
      * [Iterators](../../reference/de/db_uu/iterators.md)
      * [Designs](../../reference/de/db_uu/design.md)
      * [Teardrops](../../reference/de/db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../../reference/de/experimental/index.md)
      * [CDF](../../reference/de/experimental/cdf.md)
      * [Design Commands](../../reference/de/experimental/commands.md)
      * [Component Handles](../../reference/de/experimental/handles.md)
      * [Netlist Utilities](../../reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../reference/de/experimental/polygon_utils.md)
      * [xxPro View](../../reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../reference/de/experimental/symbol.md)
      * [Text Maker](../../reference/de/experimental/text_maker.md)
      * [Notebook](../../reference/de/experimental/notebook.md)
      * [Layer/Purpose Pairs](../../reference/de/experimental/lpp.md)
    - [keysight.ads.de.tech](../../reference/de/tech/index.md)
      * [Technology](../../reference/de/tech/tech.md)
      * [Layers](../../reference/de/tech/layers.md)
      * [Line Items](../../reference/de/tech/line_items.md)
      * [Padstacks](../../reference/de/tech/pads.md)
      * [Rules](../../reference/de/tech/rule.md)
  + [Substrate](../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../../../examples.md)
  + [Design Environment](../index.md)
    - [Workspace Creation](../workspace/ex_workspace.md)
    - [Design Creation](../design_creation/index.md)
      * [Create Layout](../design_creation/ex_create_layout.md)
      * [Create Schematic](../design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](index.md)
      * [Placing Text](ex_place_text.md)
      * [Moving Objects](ex_move.md)
      * Paths, Traces, and Polygons
      * [Adding Instances to a Design](ex_lpf.md)
      * [Traversing Hierarchy](ex_traversing_hierarchy.md)
      * [Plane Editing](ex_plane_editing.md)
    - [Parameters](../parameters/index.md)
      * [Interoperable Component Parameters](../parameters/ex_cdf.md)
      * [Working with VAR](../parameters/ex_working_with_var.md)
      * [Component Parameters](../parameters/ex_parameters.md)
      * [Creating an Item Definition](../parameters/ex_itemdef.md)
      * [Model Definition Properties](../parameters/ex_model.md)
      * [Creating a Text Form](../parameters/ex_text_form.md)
      * [Properties](../parameters/ex_properties.md)
    - [Technology](../technology/index.md)
      * [Padstacks and Vias](../technology/ex_padstack.md)
      * [Nested Technology](../technology/ex_nested.md)
      * [Rules](../technology/ex_rules.md)
    - [Translators](../translators/index.md)
      * [DXF Import and Export](../translators/ex_translate_dxf.md)
      * [Gerber Export](../translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../translators/ex_translate_gds.md)
    - [UI](../ui/index.md)
      * [Creating Custom Menus Using an Addon](../ui/ex_menu_addon.md)
      * [PySide](../ui/ex_pyside.md)
    - [Utility](../utility/index.md)
      * [Calling Between AEL and Python](../utility/ex_calling_ael_and_python.md)
      * [Smart Package](../utility/ex_smart_pkg.md)
      * [XML RPC](../utility/ex_xml_rpc.md)
  + [Substrate](../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../../../genindex.md)

# Paths, Traces, and Polygons[](#paths-traces-and-polygons "Link to this heading")

This examples shows different ways to add paths, traces, and polygons to your design

Adding a Path:

```
def adding_a_path(design: db_uu.Design) -> None:
    from keysight.ads import de

    # This example will add a path using the specified points directly
    points = [(100.0, 0.0), (150.0, 0.0), (150.0, 50.0), (200.0, 50.0)]
    # points_uu = [de.PointUU(point[0], point[1]) for point in points]
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    # TODO: Bend_style, cap_style, miter_radius, when supported
    # When creating a path, a width must be specified
    path = design.add_path(layer_id, points, 10.0)
    assert path is not None

    path_offset = 25.0  # Using an offset to easily adjust the placement of each path (for illustration purposes)
    points_offset = [(point[0] - path_offset, point[1] + path_offset) for point in points]
    # Paths may be added using a GenPolyline
    polyline = de.GenPolyline(points_offset, 10.0, "Square", "Square", 0.0)
    assert polyline.bend_style == de.db.BendStyle.SQUARE
    assert polyline.cap_style == de.db.CapStyle.SQUARE
    path = design.add_path(layer_id, polyline)
    assert path is not None

    path_offset = 50.0
    points_offset = [(point[0] - path_offset, point[1] + path_offset) for point in points]
    # Paths have different cap (end-points) and bend styles (corners)
    # Mitered bend styles apply a miter cutoff percentage
    polyline = de.GenPolyline(points_offset, 10.0, "Mitered", "Round", 30.0)
    assert polyline.bend_style == de.db.BendStyle.MITERED
    assert polyline.cap_style == de.db.CapStyle.ROUND
    path = design.add_path(layer_id, polyline)
    assert path is not None

    path_offset = 75.0
    points_offset = [(point[0] - path_offset, point[1] + path_offset) for point in points]
    # Curved bend styles apply a miter radius
    polyline = de.GenPolyline(points_offset, 10.0, "Curved", "Square", 45.0)
    assert polyline.bend_style == de.db.BendStyle.CURVED
    assert polyline.cap_style == de.db.CapStyle.SQUARE
    path = design.add_path(layer_id, polyline)
    assert path is not None
```

Adding a Trace:

```
def adding_a_trace(design: db_uu.Design) -> None:
    from keysight.ads import de

    transaction = de.db.Transaction(design, "Adding traces")
    # This example will add a trace using the specified points directly
    points = [(-100.0, 0.0), (-50.0, 0.0), (-50.0, 50.0), (0.0, 50.0)]
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    # TODO: Bend_style, cap_style, miter_radius, when supported
    # When creating a trace, a width must be specified
    path = design.add_trace(layer_id, points, 10.0)
    assert path is not None

    trace_offset = 25.0  # Using an offset to easily adjust the placement of each trace (for illustration purposes)
    points_offset = [(point[0] - trace_offset, point[1] + trace_offset) for point in points]
    # Traces may also be added using a GenPolyline
    polyline = de.GenPolyline(points_offset, 10.0, de.BendStyle.SQUARE, de.CapStyle.SQUARE, 0.0)
    path = design.add_trace(layer_id, polyline)
    assert path is not None

    trace_offset = 50.0
    points_offset = [(point[0] - trace_offset, point[1] + trace_offset) for point in points]
    # Traces have different cap (end-points) and bend styles (corners)
    # Mitered bend styles apply a miter cutoff percentage
    polyline = de.GenPolyline(points_offset, 10.0, de.BendStyle.MITERED, de.CapStyle.ROUND, 30.0)
    path = design.add_trace(layer_id, polyline)
    assert path is not None

    trace_offset = 75.0
    points_offset = [(point[0] - trace_offset, point[1] + trace_offset) for point in points]
    # Curved bend styles apply a miter radius
    polyline = de.GenPolyline(points_offset, 10.0, de.BendStyle.CURVED, de.CapStyle.SQUARE, 45.0)
    path = design.add_trace(layer_id, polyline)
    assert path is not None
    transaction.commit()
```

Adding a Polygon:

```
def adding_a_polygon(design: db_uu.Design) -> None:
    from keysight.ads import de

    # This example will add a polygon using the specified points directly
    points = [(15.0, -80.0), (35.0, -115.0), (75.0, -115.0), (95.0, -80.0), (75.0, -45.0), (35.0, -45.0)]
    # Using a poly_offset to easily adjust the placement of each polygon (for illustration purposes)
    poly_offset = 100.0
    points_offset = [(point[0] + poly_offset, point[1]) for point in points]
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    polygon = design.add_polygon(layer_id, points_offset)
    assert polygon is not None

    points_offset = [(point[0] - poly_offset, point[1]) for point in points]
    # Polygons may be added using a GenPolygon
    gen_polygon = de.GenPolygon(points_offset)
    polygon = design.add_polygon(layer_id, gen_polygon)
    assert polygon is not None

    # A polygon with holes may be added using a GenPolygonWithHoles
    hole_points = [(40.0, -60.0), (70.0, -60.0), (80.0, -80.0), (70.0, -100.0), (40.0, -100.0), (30.0, -80.0)]
    points_offset = [(point[0], point[1]) for point in points]

    outer_boundary = de.GenPolygon(points_offset)
    inner_boundary = de.GenPolygon(hole_points)
    gen_polygon_with_holes = de.GenPolygonWithHoles(None, outer_boundary, [inner_boundary])
    polygon = design.add_polygon(layer_id, gen_polygon_with_holes)
    assert polygon is not None
```

Iterating over Shapes in a Design:

```
def iterating_over_shapes_in_design(design: db_uu.Design) -> None:
    from keysight.ads.de.db import Transform

    # For this example, clear the design to ensure its empty
    design.clear_design()
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    # Let's add shapes
    adding_a_path(design)
    adding_a_trace(design)
    adding_a_polygon(design)

    # Create a ShapeIter to iterate over all shapes
    shape_iter = db_uu.ShapeIter(design, layer_id)
    # New shapes will be placed on a different layer
    target_layer_id = db_uu.LayerId(229 if design.is_schematic is True else 2)
    for shape in shape_iter:
        shape_type = shape.type
        # Paths, traces, and polygons added to a design are all Polygons
        assert shape_type.is_oa_polygon
        assert isinstance(shape, db_uu.Polygon)
        # ApolloType may be used to distinguish the kind of component the Polygon represents
        # Paths and traces have a centerline; other polygons do not.
        if shape_type.is_ads_path:
            # Use a transform to move the points of the existing path
            path_line = shape.get_centerline()
            transform = Transform()
            transform.translate(dx=200.0, dy=0.0)
            path_line.transform(transform)
            # And then place the path onto a different layer
            design.add_path(target_layer_id, path_line)

        elif shape_type.is_trace:
            # Use a transform to move the points and rotate an existing trace
            trace_line = shape.get_centerline()
            transform = Transform()
            transform.rotate_degrees(45.0)
            transform.translate(dx=-100.0, dy=200.0)
            trace_line.transform(transform)
            # And then place the trace onto a different layer
            design.add_trace(target_layer_id, trace_line)

        elif shape_type.is_ads_polygon:
            # Use a transform to move the points of an existing polygon
            transform = Transform()
            transform.translate(dx=0.0, dy=-100.0)
            polygon = shape.get_gen_polygon()
            polygon.transform(transform, 0.0)
            # Convert vertices to arcs and place the new shape in another layer
            converted_polys = polygon.convert_vertices_to_arcs(15.0)
            # Only one polygon will be returned when converting vertices to arcs on a simple shape
            assert len(converted_polys) == 1
            design.add_polygon(target_layer_id, converted_polys[0])
        else:
            raise RuntimeError("Unexpected shape present in design.")
```

On this page

[Previous

Moving Objects](ex_move.md)
[Next

Adding Instances to a Design](ex_lpf.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top