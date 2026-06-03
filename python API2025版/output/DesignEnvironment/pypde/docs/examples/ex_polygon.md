<!-- 来源: pypde\docs\examples\ex_polygon.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* [Examples](index.md)
* Paths, Traces, and Polygons

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

* [Introduction](../../../pydocs/intro/index.md)
  + [Licensing](../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../pydocs/intro/extension.md)
* [Concepts](../../../pydocs/concepts/index.md)
  + [Terminology](../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../pydocs/concepts/execution.md)
* [How-To](../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../pydocs/howto/pytest.md)

* [Design](../index.md)
  + [Reference](../reference/index.md)
    - [keysight.ads.de](../reference/de/index.md)
      * [Workspace](../reference/de/workspace.md)
      * [Library](../reference/de/library.md)
      * [Cell](../reference/de/cell.md)
      * [View](../reference/de/view.md)
      * [CellviewRef](../reference/de/cellviewref.md)
      * [DesignHierarchy](../reference/de/design_hierarchy.md)
      * [DMData](../reference/de/dmdata.md)
      * [ItemInfo](../reference/de/item_info.md)
      * [Points](../reference/de/points.md)
      * [Collections](../reference/de/collections.md)
    - [keysight.ads.de.ael](../reference/de/ael.md)
    - [keysight.ads.de.app](../reference/de/app/index.md)
      * [Actions and Menus](../reference/de/app/action.md)
      * [Addons](../reference/de/app/addon.md)
      * [Callbacks](../reference/de/app/callbacks.md)
      * [Windows and Widgets](../reference/de/app/window.md)
    - [keysight.ads.de.db](../reference/de/db/index.md)
      * [Callbacks](../reference/de/db/callbacks.md)
      * [Enumerated Types](../reference/de/db/enums.md)
      * [Parameter Forms](../reference/de/db/forms.md)
      * [GenPolyline](../reference/de/db/genpolyline.md)
      * [Model Definition](../reference/de/db/model_def.md)
      * [Parameters](../reference/de/db/parameters.md)
      * [Properties](../reference/de/db/properties.md)
      * [Transaction](../reference/de/db/transaction.md)
    - [keysight.ads.de.db\_dbu](../reference/de/db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../reference/de/db_uu/index.md)
      * [Design Elements](../reference/de/db_uu/db_uu.md)
      * [LayerId](../reference/de/db_uu/layer_id.md)
      * [LineTypeInfo](../reference/de/db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../reference/de/experimental/index.md)
      * [CDF](../reference/de/experimental/cdf/index.md)
      * [Commands](../reference/de/experimental/commands.md)
      * [Handles](../reference/de/experimental/handles.md)
      * [Netlist Utilities](../reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../reference/de/experimental/polygon_utils.md)
      * [Preferences](../reference/de/experimental/preferences.md)
      * [xxPro View](../reference/de/experimental/pro_view.md)
      * [Symbol Generator](../reference/de/experimental/symbol.md)
      * [Text Maker](../reference/de/experimental/text_maker.md)
    - [keysight.ads.de.tech](../reference/de/tech/index.md)
      * [Tech](../reference/de/tech/tech.md)
      * [Padstacks](../reference/de/tech/pads/pads.md)
      * [Via Rules](../reference/de/tech/rule/rule.md)
      * [Nested Technology](../reference/de/tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../reference/de/app/dds.md)
  + [Examples](index.md)
    - [Calling Between AEL and Python](ex_calling_ael_and_python.md)
    - [Create Layout](ex_create_layout.md)
    - [Create Schematic](ex_create_schematic.md)
    - [Create Workspace](ex_workspace.md)
    - [Create, Simulate, and Plot](ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](ex_cdf.md)
    - [Component Parameters](ex_parameters.md)
    - [Creating an Item Definition](ex_itemdef.md)
    - [Model Definition Properties](ex_model.md)
    - [Adding Instances to a Design](ex_lpf.md)
    - [Properties](ex_properties.md)
    - [Creating Custom Menus Using an Addon](ex_menu_addon.md)
    - [Padstacks and Vias](ex_padstack.md)
    - [Nested Technology](ex_nested.md)
    - [Rules](ex_rules.md)
    - [Placing Text](ex_place_text.md)
    - Paths, Traces, and Polygons
    - [PySide2](ex_pyside.md)
    - [Traversing Hierarchy](ex_traversing_hierarchy.md)
    - [Working with VAR](ex_working_with_var.md)
    - [XML RPC](ex_xml_rpc.md)
    - [GDSII Import and Export](ex_translate_gds.md)
* [Technology](../../../pysubst/docs/index.md)
  + [Reference](../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../pysubst/docs/examples/ex_substrate_with_layout.md)

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

Placing Text](ex_place_text.md)
[Next

PySide2](ex_pyside.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top