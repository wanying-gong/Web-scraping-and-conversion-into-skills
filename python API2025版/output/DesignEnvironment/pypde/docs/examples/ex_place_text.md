<!-- 来源: pypde\docs\examples\ex_place_text.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* [Examples](index.md)
* Placing Text

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
    - Placing Text
    - [Paths, Traces, and Polygons](ex_polygon.md)
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
        shape.text_height = 0.16875
        shape.font_name = "Arial Bold"
        shape.orientation = db_uu.Orientation.R180

    # Recreate the ShapeIter and verify the text has been updated
    shape_iter = db_uu.ShapeIter(design)
    shape_iter.limit_layerid(layer_id)
    for shape in shape_iter:
        assert isinstance(shape, db_uu.Text)
        assert shape.text_string == "Hello Keysight 2!"
        assert shape.text_height == 0.16875
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
    text_maker.height = 0.16875
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
        0.16875,
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
            instance, de.db.DesignAttrType.LIB_NAME, layer_id, (0.0, 1.5), "Arial Bold", 0.16875
        )
        main_design.add_inst_attr_display(
            instance, de.db.DesignAttrType.CELL_NAME, layer_id, (0.0, 1.25), "Arial", 0.16875
        )
        main_design.add_inst_attr_display(
            instance,
            de.db.DesignAttrType.LAST_SAVED_TIME,
            layer_id,
            (0.0, 1.0),
            "Arial Italic",
            0.16875,
            display_format=de.db.TextDisplayFormat.NAME_VALUE,
        )
```

On this page

[Previous

Rules](ex_rules.md)
[Next

Paths, Traces, and Polygons](ex_polygon.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top