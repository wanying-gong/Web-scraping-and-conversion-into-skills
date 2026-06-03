<!-- 来源: pypde\docs\examples\design_elements\ex_lpf.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Examples](../../../../examples.md)
* [Design Environment](../index.md)
* [Design Elements](index.md)
* Adding Instances to a Design

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
      * Adding Instances to a Design
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

# Adding Instances to a Design[](#adding-instances-to-a-design "Link to this heading")

This example adds instances of components to a design and then adds that design as an instance to another design

```
# Copyright Keysight Technologies 2023 - 2023
import os

from keysight.ads import ael, de
from keysight.ads.de import ArcOrientation, GenPolyline, PointF, db_uu
from keysight.ads.de.experimental import generate_symbol as gs

def create_lpf_circuit_workspace_design_and_simulate() -> None:
    # This workspace will reside in the user's home directory under workspaces/Instances_example_wrk
    home_dir = os.environ["HOME"]
    workspace_path = os.path.join(home_dir, "workspaces/Instances_example_wrk")

    # Ensure there is no open workspace
    if de.workspace_is_open():
        de.close_workspace()
    # Create the workspace
    de.create_workspace(workspace_path)
    workspace = de.open_workspace(workspace_path)
    # Create the library
    de.create_new_library("LPF_lib", os.path.join(workspace_path, "LPF_lib"))
    # And add it to the workspace
    workspace.add_library("LPF_lib", os.path.join(workspace_path, "LPF_lib"), de.LibraryMode.SHARED)
    # Create an empty schematic
    schematic_lpf = db_uu.create_schematic("LPF_lib:LPF:schematic")
    assert schematic_lpf is not None
    # And write out the design
    # By creating and committing a transaction, we force a connectivitiy check on the design
    transaction = de.db.Transaction(schematic_lpf, "Create schematic")
    create_an_ideal_lpf_circuit(schematic_lpf)
    transaction.commit()
    schematic_lpf.save_design()

    # Generate a symbol for the design
    symbol_lpf = create_symbol_for_ideal_lpf_circuit(schematic_lpf)

    # Create a new design in a new cell
    schematic_sp = db_uu.create_schematic("LPF_lib:LPF_SP:schematic")
    assert schematic_sp is not None
    # Designs may be referenced in multiple ways, such as with a CellviewRef
    cvr = de.CellviewRef(view=symbol_lpf.view)
    assert cvr is not None
    # Write out the new design
    transaction = de.db.Transaction(schematic_sp, "Create schematic")
    add_subcircuit_to_design_and_create_lpf_circuit(schematic_sp, cvr)
    transaction.commit()
    schematic_sp.save_design()

    # qthelp://ads.2024/doc/appguide/Designing_a_Simple_Low_Pass_Filter.html
    # TODO: Specify hierarchy policy
    # TODO: Perform schematic simulation
    # TODO: Add Parameters Sweep/Values
    # TODO: Simulate

def create_an_ideal_lpf_circuit(design: db_uu.Design) -> None:
    # ensure the design is empty
    design.clear_design()
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)

    # Add an input pin to the design
    net = design.find_or_add_net("P1")
    term = design.add_term(net, "P1", db_uu.TermType.INPUT)
    dot = design.add_dot(layer_id, (0.0, 0.0))
    # Pin angle may be passed into the constructor, or
    pin = design.add_pin(term, dot, angle=0.0)
    # The pin angle may be modified after being placed
    pin.angle = 180.0
    # And when setting the pin angle this way, update the annotation position, if desired
    pin.update_pin_annotation(preserve_origin=False)
    assert pin.term.name == "P1"

    # Add an output pin to the design
    net = design.find_or_add_net("P2")
    term = design.add_term(net, "P2", db_uu.TermType.OUTPUT)
    dot = design.add_dot(layer_id, (5.0, 0.0))
    pin = design.add_pin(term, dot)
    assert pin.term.name == "P2"

    # Add a couple instances of an inductor to the design
    # An instance may be referred by using the Library, Cell, and View name directly
    inductor = design.add_instance(de.LCVName("ads_rflib", "L", "symbol"), (0.750, 0.0), name="L1", angle=0.0)
    assert inductor is not None and inductor.name == "L1"
    # Or an instance may be referred by using a CellviewRef
    cell_view_ref = de.CellviewRef("ads_rflib", "L", "symbol")
    inductor = design.add_instance(cell_view_ref, (3.250, 0.0), name="L2", angle=0.0)
    assert inductor is not None and inductor.name == "L2"
    # Add a capacitor to the design at a -90 degree angle
    capacitor = design.add_instance(de.LCVName("ads_rflib", "C", "symbol"), (2.50, -1.25), name="C1", angle=-90.0)
    assert capacitor is not None and capacitor.name == "C1"
    # Add a ground to the design at a -90 degree angle
    ground = design.add_instance(de.LCVName("ads_rflib", "GROUND", "symbol"), (2.50, -2.25), name="GND", angle=-90.0)
    assert ground is not None and ground.name == "GND"
    # Wire them up
    # P1 to L1
    design.add_wire([(0.0, 0.0), (0.750, 0.0)])
    # L1 to L2
    design.add_wire([(1.750, 0.0), (3.250, 0.0)])
    # L2 to P2
    design.add_wire([(4.250, 0.0), (5.0, 0.0)])
    # C1 to L1 and L2
    design.add_wire([(2.50, 0.0), (2.50, -1.250)])

def create_symbol_for_ideal_lpf_circuit(schematic_lpf: db_uu.Design) -> db_uu.Design:
    symbol_lpf = db_uu.create_symbol("LPF_lib:LPF:symbol")
    # Create the symbol in LPF using SymbolGenerator
    symbol_generator = gs.SymbolGenerator(symbol_lpf, schematic_lpf, 0.25, 0.25)
    symbol_generator.is_dual_symbol_type = True
    symbol_generator.should_replace = True
    symbol_generator.pin_shape = "square"
    symbol_generator.generate_symbol()
    points_l = [(0.3, 0.2), (0.5, 0)]
    polyline_l = GenPolyline(points_l)
    polyline_l.set_segment_as_arc(0, PointF(0.375, 0), ArcOrientation.CLOCKWISE)
    symbol_layer_id = ael.call.db_get_layerid_for_symbol_body(symbol_lpf)
    symbol_lpf.add_line(symbol_layer_id, polyline_l.outline)
    points_r = [(0.7, -0.2), (0.5, 0)]
    polyline_r = GenPolyline(points_r)
    polyline_r.set_segment_as_arc(0, PointF(0.625, 0), ArcOrientation.CLOCKWISE)
    symbol_lpf.add_line(symbol_layer_id, polyline_r.outline)
    symbol_lpf.add_text(symbol_layer_id, "Input", (0.3, 0.125), "Ariel for CAE", 0.069, db_uu.TextAlignment.LOWER_LEFT)
    symbol_lpf.add_text(
        symbol_layer_id, "Output", (0.7, -0.125), "Ariel for CAE", 0.069, db_uu.TextAlignment.UPPER_RIGHT
    )
    symbol_lpf.save_design()
    return symbol_lpf

def add_subcircuit_to_design_and_create_lpf_circuit(design: db_uu.Design, sub_circuit: de.CellviewRef) -> None:
    # Add an instance of sub_circuit to design
    design.add_instance(sub_circuit, (2.50, 0.0))
    # Add some terms
    design.add_instance(de.LCVName("ads_simulation", "Term", "symbol"), (0.0, 0.0), name="Term1", angle=-90.0)
    design.add_instance(de.LCVName("ads_simulation", "Term", "symbol"), (6.0, 0.0), name="Term2", angle=-90.0)
    # Add some ground
    design.add_instance(de.LCVName("ads_rflib", "GROUND", "symbol"), (0.0, -1.0), name="GND1", angle=-90.0)
    design.add_instance(de.LCVName("ads_rflib", "GROUND", "symbol"), (6.0, -1.0), name="GND2", angle=-90.0)
    # Add an S-Param
    design.add_instance(de.LCVName("ads_simulation", "S_Param", "symbol"), (0.0, -3.0), name="S_Param", angle=0.0)
    # Wire up the terms to the sub_circuit
    design.add_wire([(0.0, 0.0), (2.50, 0.0)])
    design.add_wire([(3.50, 0.0), (6.0, 0.0)])
```

On this page

[Previous

Paths, Traces, and Polygons](ex_polygon.md)
[Next

Traversing Hierarchy](ex_traversing_hierarchy.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top