<!-- 来源: pydocs\concepts\connectivity.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../index.md)
* [ADS Concepts](index.md)
* Connectivity Objects

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

* [Introduction](../intro/index.md)
* [How-To](../howto/index.md)
  + [Use Python in the ADS Application](../howto/embedded.md)
  + [Set Up a Python Virtual Environment](../howto/venv.md)
  + [Set Up Visual Studio Code for Development](../howto/vscode.md)
  + [Use Pytest](../howto/pytest.md)
  + [Enable Python Support For Your Library](../howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../howto/execution.md)
  + [Export Workspace and Design Objects to Python](../howto/exporter.md)
  + [Record Actions in ADS as Python Code](../howto/recorder.md)
  + [Develop a Python Pcell in ADS](../howto/pcell.md)
* [ADS Concepts](index.md)
  + [Workspace Elements](workspace_elements.md)
  + Connectivity Objects
* [Reference](../../reference.md)
  + [Deprecated APIs](../py/_generated/deprecations.md)
  + [Design Environment](../../pypde/docs/reference/index.md)
    - [keysight.ads.de](../../pypde/docs/reference/de/index.md)
      * [ADS Application Environment](../../pypde/docs/reference/de/ads_environment.md)
      * [ADS Workspace Components](../../pypde/docs/reference/de/workspace_components.md)
      * [Design Hierarchy](../../pypde/docs/reference/de/design_hierarchy.md)
      * [Smart Package](../../pypde/docs/reference/de/package.md)
      * [Geometry](../../pypde/docs/reference/de/geometry.md)
      * [Collections](../../pypde/docs/reference/de/collections.md)
      * [Printer](../../pypde/docs/reference/de/printer.md)
    - [keysight.ads.de.ael](../../pypde/docs/reference/de/ael.md)
    - [keysight.ads.de.app](../../pypde/docs/reference/de/app/index.md)
      * [Application](../../pypde/docs/reference/de/app/application.md)
      * [Actions and Menus](../../pypde/docs/reference/de/app/action.md)
      * [Addons](../../pypde/docs/reference/de/app/addon.md)
      * [Window and Design Callbacks](../../pypde/docs/reference/de/app/callbacks.md)
      * [Windows and Widgets](../../pypde/docs/reference/de/app/window.md)
      * [Experimental](../../pypde/docs/reference/de/app/experimental.md)
    - [keysight.ads.de.app.dds](../../pypde/docs/reference/de/app/dds.md)
      * [exec\_python](../../pypde/docs/reference/de/app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../pypde/docs/reference/de/db/index.md)
      * [Models, Parameters, and Forms](../../pypde/docs/reference/de/db/parameters.md)
      * [Properties](../../pypde/docs/reference/de/db/properties.md)
      * [Preferences](../../pypde/docs/reference/de/db/preferences.md)
      * [Transaction](../../pypde/docs/reference/de/db/transaction.md)
      * [Smart Mount](../../pypde/docs/reference/de/db/smart_mount.md)
      * [Geometry](../../pypde/docs/reference/de/db/geometry.md)
      * [Teardrops](../../pypde/docs/reference/de/db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../pypde/docs/reference/de/db_dbu/index.md)
      * [DbBox](../../pypde/docs/reference/de/db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../pypde/docs/reference/de/db_uu/index.md)
      * [Database Objects](../../pypde/docs/reference/de/db_uu/database_objects.md)
      * [Iterators](../../pypde/docs/reference/de/db_uu/iterators.md)
      * [Designs](../../pypde/docs/reference/de/db_uu/design.md)
      * [Teardrops](../../pypde/docs/reference/de/db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../../pypde/docs/reference/de/experimental/index.md)
      * [CDF](../../pypde/docs/reference/de/experimental/cdf.md)
      * [Design Commands](../../pypde/docs/reference/de/experimental/commands.md)
      * [Component Handles](../../pypde/docs/reference/de/experimental/handles.md)
      * [Netlist Utilities](../../pypde/docs/reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../pypde/docs/reference/de/experimental/polygon_utils.md)
      * [xxPro View](../../pypde/docs/reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../pypde/docs/reference/de/experimental/symbol.md)
      * [Text Maker](../../pypde/docs/reference/de/experimental/text_maker.md)
      * [Notebook](../../pypde/docs/reference/de/experimental/notebook.md)
      * [Layer/Purpose Pairs](../../pypde/docs/reference/de/experimental/lpp.md)
    - [keysight.ads.de.tech](../../pypde/docs/reference/de/tech/index.md)
      * [Technology](../../pypde/docs/reference/de/tech/tech.md)
      * [Layers](../../pypde/docs/reference/de/tech/layers.md)
      * [Line Items](../../pypde/docs/reference/de/tech/line_items.md)
      * [Padstacks](../../pypde/docs/reference/de/tech/pads.md)
      * [Rules](../../pypde/docs/reference/de/tech/rule.md)
  + [Substrate](../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../examples.md)
  + [Design Environment](../../pypde/docs/examples/index.md)
    - [Workspace Creation](../../pypde/docs/examples/workspace/ex_workspace.md)
    - [Design Creation](../../pypde/docs/examples/design_creation/index.md)
      * [Create Layout](../../pypde/docs/examples/design_creation/ex_create_layout.md)
      * [Create Schematic](../../pypde/docs/examples/design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../../pypde/docs/examples/design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../../pypde/docs/examples/design_elements/index.md)
      * [Placing Text](../../pypde/docs/examples/design_elements/ex_place_text.md)
      * [Moving Objects](../../pypde/docs/examples/design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../../pypde/docs/examples/design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../../pypde/docs/examples/design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../../pypde/docs/examples/design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../../pypde/docs/examples/design_elements/ex_plane_editing.md)
    - [Parameters](../../pypde/docs/examples/parameters/index.md)
      * [Interoperable Component Parameters](../../pypde/docs/examples/parameters/ex_cdf.md)
      * [Working with VAR](../../pypde/docs/examples/parameters/ex_working_with_var.md)
      * [Component Parameters](../../pypde/docs/examples/parameters/ex_parameters.md)
      * [Creating an Item Definition](../../pypde/docs/examples/parameters/ex_itemdef.md)
      * [Model Definition Properties](../../pypde/docs/examples/parameters/ex_model.md)
      * [Creating a Text Form](../../pypde/docs/examples/parameters/ex_text_form.md)
      * [Properties](../../pypde/docs/examples/parameters/ex_properties.md)
    - [Technology](../../pypde/docs/examples/technology/index.md)
      * [Padstacks and Vias](../../pypde/docs/examples/technology/ex_padstack.md)
      * [Nested Technology](../../pypde/docs/examples/technology/ex_nested.md)
      * [Rules](../../pypde/docs/examples/technology/ex_rules.md)
    - [Translators](../../pypde/docs/examples/translators/index.md)
      * [DXF Import and Export](../../pypde/docs/examples/translators/ex_translate_dxf.md)
      * [Gerber Export](../../pypde/docs/examples/translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../../pypde/docs/examples/translators/ex_translate_gds.md)
    - [UI](../../pypde/docs/examples/ui/index.md)
      * [Creating Custom Menus Using an Addon](../../pypde/docs/examples/ui/ex_menu_addon.md)
      * [PySide](../../pypde/docs/examples/ui/ex_pyside.md)
    - [Utility](../../pypde/docs/examples/utility/index.md)
      * [Calling Between AEL and Python](../../pypde/docs/examples/utility/ex_calling_ael_and_python.md)
      * [Smart Package](../../pypde/docs/examples/utility/ex_smart_pkg.md)
      * [XML RPC](../../pypde/docs/examples/utility/ex_xml_rpc.md)
  + [Substrate](../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../genindex.md)

# Connectivity Objects[](#connectivity-objects "Link to this heading")

Connectivity objects in ADS Python represent the logical and physical connections between components.
They include Nets, Terms, Pins, InstTerms, and InstPins.

To learn more about connectivity objects available within an ADS design, see [Connectivity Objects](..%5C..%5C..%5C..%5C..%5Cads%5CContent%5Cads2026update2%5Cael%5CConnectivity_Objects.md).

## Net[](#net "Link to this heading")

A [`Net`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.Net.md#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu.Net") represents the logical connectivity within a design, the
electrical path in a circuit. A collection of wires or interconnects that carry the same signal is
considered to be on the same net. Nets connect to Terms and InstTerms.

ADS Python supports multiple types of Nets:

[`ScalarNet`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.ScalarNet.md#keysight.ads.de.db_uu.ScalarNet "keysight.ads.de.db_uu.ScalarNet"): A single-bit net that is not part of a BusNet and
does not use bus-name syntax. Generally speaking, ScalarNet is the most common type of Net.

[`BusNet`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.BusNet.md#keysight.ads.de.db_uu.BusNet "keysight.ads.de.db_uu.BusNet"): A multi-bit Net that shares a common base name and uses
bus-name syntax (e.g. “A<0:7>”). A BusNet can be viewed as a collection of single-bit logical connections.

[`BusNetBit`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.BusNetBit.md#keysight.ads.de.db_uu.BusNetBit "keysight.ads.de.db_uu.BusNetBit"): A single-bit of a BusNet and uses bus-name syntax
(e.g. “A<0>”).

[`BundleNet`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.BundleNet.md#keysight.ads.de.db_uu.BundleNet "keysight.ads.de.db_uu.BundleNet"). A multi-bit Net that does not share a common base
name, but instead uses comma separated names for each bit (e.g., “A, B, C”)

The following image shows a schematic with the net, Net1. The three wires and the InstTerms they are
connected to are all on Net1.

![../../_images/net.png](../../_images/net.png)

## Term[](#term "Link to this heading")

A [`Term`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.Term.md#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term") (terminal) represents a logical connection point for a design.
Nets associated with the terminals are logically made available to the next higher level in a design hierarchy.
Pins associated with a Term represent the physical connection point for the design.

## Pin[](#pin "Link to this heading")

A [`Pin`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.Pin.md#keysight.ads.de.db_uu.Pin "keysight.ads.de.db_uu.Pin") represents a physical connection point of terminals to
nets. A term can have multiple pins, where multiple physical connections can correspond to a
single logical connection. A pin is associated with one or more physical figures and holds information
on the term it represents and physical properties, such as its location and angle.

```
def adding_a_pin_to_a_design(design: db_uu.Design) -> None:
    with de.db.Transaction(design) as transaction:
        net = design.find_or_add_net("P1")
        term = design.add_term(net, "P1")
        layer_id = design.create_layer_id("cond")
        dot = design.add_dot(layer_id, (0.0, 0.0))
        # Pins are associated with a term and a pinfig, often just a dot
        design.add_pin(term, dot)
        transaction.commit()
```

## InstTerm[](#instterm "Link to this heading")

An [`InstTerm`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.InstTerm.md#keysight.ads.de.db_uu.InstTerm "keysight.ads.de.db_uu.InstTerm") represents a logical connection point between
a net and a term in the master of an instance. An InstTerm with a corresponding Term in the master
design is considered bound to the term, and is bound by either number or by name. All bound InstTerms
of an instance must be bound the same way (either all by number or all by name). An InstTerm that does
not have a corresponding Term in the master design (if, for example, the master design was modified
and the term removed after an instance of the master was placed into a parent design) is said to be
unbound.

```
def checking_inst_term_properties(design: db_uu.Design) -> None:
    for instance in design.instances:
        for inst_term in instance.inst_terms:
            if inst_term.is_bound:
                # Obtain either the number or name from the bound InstTerm
                if inst_term.is_numbered:
                    print(f"Term is numbered: {inst_term.term_number}")
                else:
                    print(f"Term is named: {inst_term.term_name}")

            # More than one InstPin may be associated with an InstTerm:
            for inst_pin in inst_term.inst_pins:
                print(inst_pin)

            # Obtain the net from the InstTerm, which may be None
            net = inst_term.net
            print(net)
```

## InstPin[](#instpin "Link to this heading")

An [`InstPin`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.InstPin.md#keysight.ads.de.db_uu.InstPin "keysight.ads.de.db_uu.InstPin") represents a pin in the master design of an instance
mapped into the parent design. When a wire is connected to an InstPin, the net associated with the
wire connects to the InstTerm associated with the InstPin.

```
def connecting_a_wire_to_an_inst_term(design: db_uu.Design) -> None:
    # Create an instance of a resistor symbol and place it in the schematic at (0, 0)
    cellview_ref: de.CellviewRef = de.CellviewRef("ads_rflib", "R", "symbol")
    r1: db_uu.Instance = design.add_instance(cellview_ref, (0, 0), name="R1")
    r2: db_uu.Instance = design.add_instance(cellview_ref, (3, 0), name="R2")

    # Anytime connectivity is modified, it should be done within a transaction. Committing a transaction
    # will check, and potentially repair, the design for connectivity errors.
    with de.db.Transaction(design) as transaction:
        # Note: You can use the snap_point property for making connections
        r1_snap_point = r1.inst_pins[1].snap_point
        r2_snap_point = r2.inst_pins[0].snap_point
        assert r1_snap_point is not None and r2_snap_point is not None
        # Connecting a wire to an InstPin will propagate the Net to the InstPin
        wire = design.add_wire([r1_snap_point, r2_snap_point])
        # Setting the wire label will also set its net, which will propagate to the InstPin
        wire.add_wire_label("N1")
        assert r1.inst_pins[1].net is not None and r1.inst_pins[1].net.name == "N1"
        assert r2.inst_pins[0].net is not None and r2.inst_pins[0].net.name == "N1"

        transaction.commit()
```

In the following image, we have a schematic with two pins, each of them connecting to a component on
a net. The P1 Term is connected to the P1 Net and the P2 Term is connected to the P2 Net.

![../../_images/pin_term_net.png](../../_images/pin_term_net.png)

In this image, the symbol View of the above design was placed into a parent design as an Instance.
Connections to the pins in the master design are made through the corresponding InstTerms in the
parent design.

The P1 InstTerm is the connection point between the Net on the parent design and the Term on the master
design of the instance.

![../../_images/inst_term.png](../../_images/inst_term.png)

On this page

[Previous

Workspace Elements](workspace_elements.md)
[Next

Reference](../../reference.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top