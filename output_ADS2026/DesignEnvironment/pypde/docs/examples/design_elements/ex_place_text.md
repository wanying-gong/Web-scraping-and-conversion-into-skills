<!-- 来源: pypde\docs\examples\design_elements\ex_place_text.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Examples](../../../../examples.md)
* [Design Environment](../index.md)
* [Design Elements](index.md)
* Placing Text

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
      * Placing Text
      * [Moving Objects](ex_move.md)
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

# Placing Text[](#placing-text "Link to this heading")

This example illustrates the various ways of placing text into a design.

```
def placing_text_in_a_design(design: db_uu.Design) -> None:
    from keysight.ads.de import db_uu
    from keysight.ads.de.experimental.text_maker import TextMaker

    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)

    # There are multiple ways to place text on a design.
    # The TextMaker class pulls the text attributes from the design preferences
    # NOTE:
    # `text_height` and all geometric values here are expressed in user units (UU),
    # not in database units (DBU). ADS converts between the two with a fixed grid
    # resolution (design.dbu_to_uu_factor).
    text_maker = TextMaker(design)
    origin = (1.0, 0.5)
    text_maker.add_text(layer_id, "Hello Keysight 1!", origin)

    # Change text attributes as desired
    text_maker.height = 0.225
    text_maker.font_name = "Arial Italic"
    text_maker.align = db_uu.TextAlignment.LOWER_LEFT
    text_maker.orient = db_uu.Orientation.R270
    origin = (1.5, 1.0)
    text = text_maker.add_text(layer_id, "Hello Keysight 2!", origin)
    assert text.text_height == 0.225
    assert text.font_name == "Arial Italic"
    assert text.alignment == db_uu.TextAlignment.LOWER_LEFT
    assert text.orientation == db_uu.Orientation.R270

    # Alternatively, place text using the Text class directly
    origin = (1.5, 1.5)
    text = db_uu.Text(
        design,
        layer_id,
        "Hello Keysight 3!",
        origin,
        "Arial Bold",
        0.225,
        db_uu.TextAlignment.UPPER_RIGHT,
        db_uu.Orientation.R0,
    )
    assert text.text_height == 0.225
    assert text.font_name == "Arial Bold"
    assert text.alignment == db_uu.TextAlignment.UPPER_RIGHT
    assert text.orientation == db_uu.Orientation.R0

    # Or, use the add_text method on the design
    origin = (2.0, 2.0)
    text = design.add_text(
        layer_id,
        "Hello Keysight 4!",
        origin,
        "Arial",
        0.225,
        db_uu.TextAlignment.CENTER_CENTER,
        db_uu.Orientation.R180,
    )
    assert text.text_height == 0.225
    assert text.font_name == "Arial"
    assert text.alignment == db_uu.TextAlignment.CENTER_CENTER
    assert text.orientation == db_uu.Orientation.R180
```

This example uses a shape iterator (ShapeIter) to access text placed in a design.

```
def accessing_placed_text_with_a_shape_iterator(design: db_uu.Design) -> None:
    from keysight.ads.de.experimental.text_maker import TextMaker

    # For this example, ensure the design is empty
    design.clear_design()
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    # Make some text
    # All geometric values here are expressed in user units (UU)
    text_maker = TextMaker(design)
    text_maker.height = 0.225
    text_maker.font_name = "Arial Italic"
    text_maker.align = db_uu.TextAlignment.UPPER_LEFT
    text_maker.orient = db_uu.Orientation.R0
    origin = (1.0, 1.0)
    text_maker.add_text(layer_id, "Hello Keysight 1!", origin)

    # Access the text via a ShapeIter
    shape_iter = db_uu.ShapeIter(design)
    shape_iter.limit_layerid(layer_id)
    # The design was previously cleared, there will be only one shape
    for shape in shape_iter:
        assert isinstance(shape, db_uu.Text)
        assert shape.text_string == "Hello Keysight 1!"
        assert shape.text_height == 0.225
        assert shape.font_name == "Arial Italic"
        assert shape.alignment == db_uu.TextAlignment.UPPER_LEFT
        assert shape.orientation == db_uu.Orientation.R0
        # Change some attributes
        shape.text_string = "Hello Keysight 2!"
        shape.text_height = 0.175
        shape.font_name = "Arial Bold"
        shape.orientation = db_uu.Orientation.R180

    # Recreate the ShapeIter and verify the text has been updated
    shape_iter = db_uu.ShapeIter(design)
    shape_iter.limit_layerid(layer_id)
    for shape in shape_iter:
        assert isinstance(shape, db_uu.Text)
        assert shape.text_string == "Hello Keysight 2!"
        assert math.isclose(shape.text_height, 0.175, rel_tol=1e-6)
        assert shape.font_name == "Arial Bold"
        assert shape.alignment == db_uu.TextAlignment.UPPER_LEFT
        assert shape.orientation == db_uu.Orientation.R180
```

This example illustrates how to place an attribute display into a design.

```
def placing_attribute_displays(design: db_uu.Design) -> None:
    from keysight.ads import de
    from keysight.ads.de.experimental.text_maker import TextMaker

    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    # The TextMaker class pulls the text attributes from the design preferences
    text_maker = TextMaker(design)
    origin = (2.0, 3.0)
    # Change text attributes as desired
    # All geometric values here are expressed in user units (UU)
    text_maker.height = 0.175
    text_maker.orient = db_uu.Orientation.R0
    attr_display = text_maker.add_attr_display(
        design, de.db.DesignAttrType.VIEW_NAME, layer_id, origin, de.db.TextDisplayFormat.NAME_VALUE
    )
    assert attr_display.attribute == de.db.DesignAttrType.VIEW_NAME

    origin = (2.0, 3.5)
    attr_display = text_maker.add_attr_display(
        design, de.db.DesignAttrType.LAST_SAVED_TIME, layer_id, origin, de.db.TextDisplayFormat.NAME_VALUE
    )
    assert attr_display.attribute == de.db.DesignAttrType.LAST_SAVED_TIME

    # An AttrDisplay may also be created directly from the design
    origin = (2.0, 4.0)
    attr_display = design.add_attr_display(
        design,
        de.db.DesignAttrType.LIB_NAME,
        layer_id,
        origin,
        "Arial",
        0.175,
        de.db.TextAlignment.CENTER_CENTER,
        de.db.Orientation.R0,
        de.db.TextDisplayFormat.NAME_VALUE,
    )
    assert attr_display.attribute == de.db.DesignAttrType.LIB_NAME
```

This example places instance attribute displays into a design.

```
def adding_an_inst_attr_display(library: de.Library) -> None:
    # This example assumes the library does not have cells called cell_inst or cell_main
    layer_id = db_uu.LayerId(231)
    inst_design_lcv_name = f"{library.name}:cell_inst:schematic"
    inst_design = db_uu.create_schematic(inst_design_lcv_name)
    # Create a simple design
    with db_uu.design_saving(inst_design):
        inst_design.add_instance(("ads_sources", "V_DC", "symbol"), (0, 0.5), name="SRC1", angle=-90.0)
        inst_design.add_instance(("ads_rflib", "R", "symbol"), (3.0, 0.5), name="R1", angle=-90.0)
        inst_design.add_instance(("ads_rflib", "GROUND", "symbol"), (1.5, -0.875), angle=-90)
        inst_design.add_wire([(0.0, -0.5), (1.5, -0.875)])
        inst_design.add_wire([(1.5, -0.875), (3.0, -0.50)])
        inst_design.add_wire([(0.0, 0.5), (3.0, 0.5)])

    main_design = db_uu.create_schematic(f"{library.name}:cell_main:schematic")
    with db_uu.design_saving(main_design):
        # Insert an instance of the simple design into a new design
        instance = main_design.add_instance(inst_design_lcv_name, (0.0, 0.0), name="INST1", angle=0.0)
        # And add instance attributes displays to the design
        main_design.add_inst_attr_display(
            instance, de.db.DesignAttrType.LIB_NAME, layer_id, (0.0, 1.5), "Arial Bold", 0.175
        )
        main_design.add_inst_attr_display(
            instance, de.db.DesignAttrType.CELL_NAME, layer_id, (0.0, 1.25), "Arial", 0.175
        )
        main_design.add_inst_attr_display(
            instance,
            de.db.DesignAttrType.LAST_SAVED_TIME,
            layer_id,
            (0.0, 1.0),
            "Arial Italic",
            0.175,
            display_format=de.db.TextDisplayFormat.NAME_VALUE,
        )
```

On this page

[Previous

Design Elements](index.md)
[Next

Moving Objects](ex_move.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top