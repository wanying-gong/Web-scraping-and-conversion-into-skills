<!-- 来源: pypde\docs\examples\design_elements\ex_move.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Examples](../../../../examples.md)
* [Design Environment](../index.md)
* [Design Elements](index.md)
* Moving Objects

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
      * Moving Objects
      * [Paths, Traces, and Polygons](ex_polygon.md)
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

# Moving Objects[](#moving-objects "Link to this heading")

The following examples shows how to move an instances, shapes, and app objects in a layout.

Move an instance in a design:

```
def move_an_instance(design: db.Design) -> None:

    # Assume we are in layout
    assert design.is_layout
    design.clear_design()

    c1 = design.add_instance(("ads_rflib:C_Pad1:layout"), (10.0, 10.0))
    assert c1.origin == de.PointF(10.0, 10.0)

    # Moving an instance is pretty straightforward, pass in a point relative to the current origin
    c1.move((-10.0, -10.0))
    assert c1.origin == de.PointF(0.0, 0.0)

    # If you want your move call to be on the undo stack, wrap it in a transaction
    with db.Transaction(design) as t:
        c1.move((25.0, 25.0))
        t.commit()

    assert c1.origin == de.PointF(25.0, 25.0)
```

Move shapes in a design:

```
def move_shapes(design: db.Design) -> None:

    # Assume we are in layout
    assert design.is_layout
    design.clear_design()

    cond_layer = db.LayerId.from_name(design.library, "cond")

    # Add some shapes
    rect = design.add_rectangle(cond_layer, (0, 0), (20, 10))
    assert rect.bbox == de.BoxF(x1=0.0, y1=0.0, x2=20.0, y2=10.0)

    circle = design.add_circle(cond_layer, (30, 30), 10)
    assert circle.bbox == de.BoxF(x1=20.0, y1=20.0, x2=40.0, y2=40.0)

    # Moving shapes is similar to moving instances; call move on each shape
    # Transactions aren't required, but if you want the move added to the undo stack, wrap it in a transaction
    with db.Transaction(design) as t:
        for shape in design.shapes:
            shape.move((5.0, 5.0))
        t.commit()

    assert rect.bbox == de.BoxF(x1=5.0, y1=5.0, x2=25.0, y2=15.0)
    assert circle.bbox == de.BoxF(x1=25.0, y1=25.0, x2=45.0, y2=45.0)
```

Move AppObjects in a design:

```
def move_app_objects(design: db.Design) -> None:

    # Assume we are in layout
    assert design.is_layout
    design.clear_design()

    layer_id = db.LayerId.from_name(design.library, "cond")
    # There are different types of AppObjects; here we create a construction line and a keepout
    line = design.add_construction_line(layer_id, (0, 0), (10, 0))
    assert line.points == (de.PointF(0.0, 0.0), de.PointF(10.0, 0.0))

    polygon = de.GenPolygon(
        [de.PointF(x=0.0, y=0.0), de.PointF(x=50.0, y=0.0), de.PointF(x=50.0, y=50.0), de.PointF(x=0.0, y=-50.0)]
    )
    keepout = db.Keepout.create(design, layer_id, polygon)

    # You can find AppObjects using the AppObjectIter
    with db.Transaction(design) as t:
        for obj in db.AppObjectIter(design):
            if isinstance(obj, db.ConstructionLine):
                obj.move((5.0, 0.0))
                assert obj == line
                assert obj.points == (de.PointF(5.0, 0.0), de.PointF(15.0, 0.0))
            if isinstance(obj, db.Keepout):
                obj.move((0.0, 10.0))
                assert obj == keepout
                assert obj.polygon.bbox == de.BoxF(x1=0.0, y1=-40.0, x2=50.0, y2=60.0)

        t.commit()
```

The following example demonstrates trace avoidance routing when moving objects.

```
def move_selected_items(design: db.Design) -> None:

    assert design.is_layout
    design.clear_design()

    # When you want trace avoidance routing when moving objects, you need a clearance rule in your technology.
    assert design.library.has_tech
    tech = design.library.tech

    try:
        clearance_rule = de.tech.rule.ClearanceRule(design.library, "clearance_1", 10.0)
        tech.clearance_rules.add(clearance_rule)
        tech.save_rules()
    except ValueError:
        # Rule already exists
        pass

    # Add a couple capacitors connected with a trace
    c1 = design.add_instance("ads_rflib:C_Pad1", name="C1", origin=(0.0, 0.0))
    c2 = design.add_instance("ads_rflib:C_Pad1", name="C2", origin=(200.0, 0.0))

    # Add a trace connecting the two capacitors
    points = [de.PointF(x=50.0, y=0.0), de.PointF(x=200.0, y=0.0)]
    tech = design.library.tech
    polyline = db.Polyline(tech, points, 10.0, "Rounded")
    teardrop = db.Teardrop(tech, ("Ratio", 0.2), height=("Ratio", 0.7))
    polyline.teardrop_front = teardrop
    polyline.teardrop_back = teardrop
    trace = design.add_trace(db.LayerId(4), polyline=polyline)

    # Place a shape that will force avoidance routing of the trace when we move the selected objects
    design.add_rectangle(db.LayerId(4), de.PointF(85.0, 25.0), de.PointF(170.0, 100.0))

    from keysight.ads import ael

    ael.call.db_select(c1, True)
    ael.call.db_select(c2, True)
    ael.call.db_select(trace, True)

    design.edit.move_selected((0.0, 50.0), route_trace=True)
    assert c1.origin == de.PointF(0.0, 50.0)
    assert c2.origin == de.PointF(200.0, 50.0)
```

Before moving the selected items:

![../../../../_images/ex_move_selected_items_before.png](../../../../_images/ex_move_selected_items_before.png)

After moving the selected items:

![../../../../_images/ex_move_selected_items_after.png](../../../../_images/ex_move_selected_items_after.png)

On this page

[Previous

Placing Text](ex_place_text.md)
[Next

Paths, Traces, and Polygons](ex_polygon.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top