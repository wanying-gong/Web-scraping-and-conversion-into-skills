<!-- 来源: pypde\docs\examples\design_elements\ex_plane_editing.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Examples](../../../../examples.md)
* [Design Environment](../index.md)
* [Design Elements](index.md)
* Plane Editing

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
      * [Paths, Traces, and Polygons](ex_polygon.md)
      * [Adding Instances to a Design](ex_lpf.md)
      * [Traversing Hierarchy](ex_traversing_hierarchy.md)
      * Plane Editing
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

# Plane Editing[](#plane-editing "Link to this heading")

Example showing how to degas a Plane.

For more information on plane and plane degas attributes, see [Plane Parameters](..%5C..%5C..%5C..%5C..%5C..%5C..%5Cads%5CContent%5Cads2026update2%5Cusrguide%5CPlane_Parameters.md).

Plane Degassing:

```
def degassing_a_plane(design: db_uu.Design) -> None:
    lib = design.library
    assert lib.has_tech

    design.clear_design()
    layer_id = design.create_layer_id("cond")

    # Populating plane info
    plane_info = db_uu.PlaneInfo(design)
    plane_info.use_clearance_rules = False
    plane_info.net_name = "N1"
    plane_info.clearance = 4

    # Degassing options
    plane_info.degassing_enabled = True

    # The shape of the perforation (Rectangle, Square, Circle, or Octagon).
    plane_info.degas_options.vent_shape = "Rectangle"

    # The width of the vent shape. For the Square, Circle, and Octagon shape, only the width is used for determining its size.
    # This must be greater than 0.0.
    plane_info.degas_options.vent_shape_width = 5

    # The height of the vent shape. This field only applies to the Rectangle vent shape. When used, this must be greater than 0.0.
    plane_info.degas_options.vent_shape_height = 5

    # The horizontal separation between the center points of two venting holes. This must be greater than the width of the shape
    plane_info.degas_options.pitch_width = 10

    # The vertical separation between the center points of two venting holes. For the Rectangle shape, this must be greater than the height.
    # For Square, Circle, and Octagon, this must be greater than the width of the shape.
    plane_info.degas_options.pitch_height = 8

    # The minimum area of a plane shape that will be considered for perforation.
    plane_info.degas_options.min_venting_area = 675

    # The minimum_edge_distance is the amount of space from clearance or the edge of the plane.
    # For a perforation to be made, there must be enough space for the bounding box of the vent shape plus the Minimum Distance, in all four directions.
    plane_info.degas_options.min_edge_distance = 4

    # One of the four corners of the bounding box of the plane (Lower Left, Lower Right, Upper Left, Upper Right),
    # the starting position affects the location of the initial perforation.
    plane_info.degas_options.vent_starting_position = "LowerLeft"

    # Note: The starting point is the center of the first vent that will be computed.
    # The offsets are always inputted as positive values but may be interpreted as negative,
    # depending on the corner used as the starting position.

    # The amount of horizontal spacing from the Starting Position to the initial perforation
    # Offset X moves the columns of perforations horizontally.
    plane_info.degas_options.starting_offset_x = 15

    # The amount of vertical spacing from the Starting Position to the initial perforation.
    # Offset Y moves the rows of perforations vertically.
    plane_info.degas_options.starting_offset_y = 5

    # Create a polygon, on layer: 'cond'
    square_1 = design.add_polygon(
        layer_id, [(-95.000, -35.000), (20.000, -35.000), (20.000, 55.000), (-95.000, 55.000)]
    )
    # Adding the plane to the design
    plane1 = design.add_plane(plane_info, square_1, "plane1")

    # Note: The degassing algorithm won't perforate areas where shapes exist on the same layer and net as the plane.

    # Adding Shapes to dodge
    points_t1 = [(-75.000, 60.000), (-75.000, 20.000), (-35.000, 20.000), (-35.000, -10.000), (0.000, -10.000)]
    points_t2 = [(-85.000, 60.000), (-85.000, 10.000), (-50.000, 10.000), (-50.000, -20.000), (-15.000, -20.000)]
    polyline_1 = de.GenPolyline(points_t1, 2.0, de.BendStyle.ROUNDED, de.CapStyle.ROUND, 0.0)
    polyline_2 = de.GenPolyline(points_t2, 2.0, de.BendStyle.ROUNDED, de.CapStyle.ROUND, 0.0)
    design.add_trace(layer_id, polyline_1)
    design.add_trace(layer_id, polyline_2)

    design.add_rectangle(layer_id, (-43.506, 25.16), (-38.506, 55.16))

    # place a circle on the plane with the same net as the plane
    circle1 = design.add_circle(layer_id, (-5.0, 40.0), 10.0)
    net1 = design.find_net(plane_info.net_name)
    assert net1 is not None, "Net not found!"
    circle1.net = net1  # Don't perforate the area of the shape on the same layer and net as the plane

    db_uu.Plane.rebuild_plane(plane1)
    design.save_design()
```

![../../../../_images/ex_plane_degassing.png](../../../../_images/ex_plane_degassing.png)

Merging Planes:

The following example demonstrates plane merging by creating overlapping rectangles (planes) on the same net and layer,
and shows how the algorithm merges planes with equivalent PlaneInfo into a single unified plane.

Create And Merge Planes In A Design:

```
# Copyright Keysight Technologies 2023 - 2023
from typing import Optional

from keysight.ads import de
from keysight.ads.de import db_uu

def create_and_merge_planes_in_design(design: db_uu.Design) -> None:
    design.clear_design()
    layer_id = design.create_layer_id("cond")
    # Create two overlapping rectangles to use for planes
    rect1 = design.add_rectangle(layer_id, (0, 0), (100, 100))
    rect2 = design.add_rectangle(layer_id, (50, 50), (150, 150))
    # Create circles for planes to dodge
    design.add_circle(layer_id, (25, 25), 5)
    design.add_circle(layer_id, (75, 75), 5)
    design.add_circle(layer_id, (125, 125), 5)

    # Make two planes with the same PlaneInfo
    plane_info = db_uu.PlaneInfo(design)
    plane_info.use_clearance_rules = False
    plane_info.net_name = "gnd!"
    plane_info.clearance = 10
    plane_info.layer_id = layer_id

    # Adding the planes to the design
    # NOTE: Since neither rectangle is on a net, the first plane will avoid
    # the second rectangle.
    design.add_plane(plane_info, rect1, "plane1")
    # Since plane1 is on gnd!, this second plane will not avoid plane1.
    design.add_plane(plane_info, rect2, "plane2")
    # If we were to rebuild plane1 now, it would not avoid plane2.

    # Merge them
    merge_planes_in_design(design)

def get_equivalent_planes(design: db_uu.Design, plane_info: db_uu.PlaneInfo) -> list[db_uu.Plane]:
    # Return a list of planes in the design that have equivalent PlaneInfo.
    matching_planes = []
    for obj in db_uu.CompositeDesignIter(design):
        if isinstance(obj, db_uu.Plane):
            obj_info = obj.copy_plane_info()
            if plane_info.same_props(obj_info):
                matching_planes.append(obj)
    return matching_planes

def merge_equivalent_planes(design: db_uu.Design, plane_info: db_uu.PlaneInfo) -> None:
    # Merge any planes in the design that have equivalent PlaneInfo.
    planes = get_equivalent_planes(design, plane_info)
    if len(planes) < 2:
        return  # Nothing to merge if fewer than 2 planes match

    # Collect original polygons
    original_polys = []
    for plane in planes:
        original_polys.append(plane.copy_original_polygon())

    # This could be smarter and check if the merged polygons are any different from the original_polys.
    if False:
        # This uses the arc resolution 5 degrees when eliminating arcs
        new_polys = de.experimental.merge_polygons_uu(original_polys, 5.0)
    else:
        new_polys = de.experimental.merge_polygons_curved_uu(original_polys)

    # Delete old planes and create a new merged plane
    with de.db.Transaction(design, "Merge planes") as trans:
        # Delete the original planes
        for plane in planes:
            plane.delete_object()
        # Make new planes from the merge polygons
        for poly in new_polys:
            design.add_plane(plane_info, poly, "merged plane")
        trans.commit()

def find_first_plane(design: db_uu.Design) -> Optional[db_uu.Plane]:
    # Return the first plane in the design.
    it = db_uu.CompositeDesignIter(design)
    for obj in it:
        if isinstance(obj, db_uu.Plane):
            return obj
    return None

def merge_planes_in_design(design: db_uu.Design) -> None:
    # Get the PlaneInfo from the first plane.  Merge any planes with equivalent PlaneInfo.
    plane = find_first_plane(design)
    if plane is not None:
        plane_info = plane.copy_plane_info()
        merge_equivalent_planes(design, plane_info)
```

The following image shows two overlapping rectangles added as planes on the same net and layer.
It demonstrates how the algorithm merges them into a single unified plane when they share equivalent PlaneInfo.

![../../../../_images/merge_planes_in_design.png](../../../../_images/merge_planes_in_design.png)

Removing Islands:

Example showing how to remove disconnected portions of a plane (islands)

```
def remove_islands_from_plane(design: db_uu.Design) -> None:
    design.clear_design()
    layer_id = design.create_layer_id("cond")

    # Populating plane info for the plane
    plane_info = db_uu.PlaneInfo(design)
    plane_info.use_clearance_rules = False
    plane_info.net_name = "N1"
    plane_info.clearance = 4
    # Set the remove_islands_mode
    plane_info.remove_islands_mode = "RemoveByArea"
    plane_info.min_island_area = 200.0
    # Create a polygon on layer: 'cond'
    square_1 = design.add_polygon(
        layer_id, [(-95.000, -35.000), (20.000, -35.000), (20.000, 55.000), (-95.000, 55.000)]
    )
    # Adding the plane to the design
    plane1 = design.add_plane(plane_info, square_1, "plane1")

    # Place shapes on the plane in such a way that clearance creates disconnected sections(islands),
    # forming portions of the plane that are detached from the rest of the plane.
    points_t1 = [(-75.000, 60.000), (-75.000, 20.000), (-35.000, 20.000), (-35.000, -10.000), (0.000, -10.000)]
    points_t2 = [(-85.000, 60.000), (-85.000, 10.000), (-50.000, 10.000), (-50.000, -20.000), (-15.000, -20.000)]
    polyline_1 = de.GenPolyline(points_t1, 2.0, de.BendStyle.ROUNDED, de.CapStyle.ROUND, 0.0)
    polyline_2 = de.GenPolyline(points_t2, 2.0, de.BendStyle.ROUNDED, de.CapStyle.ROUND, 0.0)
    design.add_trace(layer_id, polyline_1)
    design.add_trace(layer_id, polyline_2)

    design.add_rectangle(layer_id, (-43.506, 25.16), (-38.506, 55.16))

    # place a circle on the plane with the same net as the plane
    circle1 = design.add_circle(layer_id, (-5.0, 40.0), 10.0)
    net1 = design.find_net(plane_info.net_name)
    assert net1 is not None, "Net not found!"
    circle1.net = net1

    # Disconnected sections of the plane, called islands, may appear after rebuilding the plane.
    # In this case, three islands are formed: two small ones and one large one.
    # Since we've enabled the removal_of_islands with an area less than 200, two islands are removed.
    # As a result, only one island remain visible.
    db_uu.Plane.rebuild_plane(plane1)

    # Now one can double click on the plane and can change remove_islands_modes/change area in the edit_plane dialogue and click on apply to see the results.

    # The "RemoveAll" option, removes all the islands
    # except the plane_shapes_touching_other_objects (objects can be other_shapes_in_instances as well)
    # In our case, the shape `circle1` is on the same net as the plane, so the plane it touches is preserved,
    # while all other islands are removed.

    design.save_design()
```

![../../../../_images/ex_remove_islands.png](../../../../_images/ex_remove_islands.png)

On this page

[Previous

Traversing Hierarchy](ex_traversing_hierarchy.md)
[Next

Parameters](../parameters/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top