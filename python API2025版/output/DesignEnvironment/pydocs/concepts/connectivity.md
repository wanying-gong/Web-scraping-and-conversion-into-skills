<!-- 来源: pydocs\concepts\connectivity.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../index.md)
* [Concepts](index.md)
* [Terminology](terminology.md)
* Connectivity Objects

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

* [Introduction](../intro/index.md)
  + [Licensing](../intro/licensing.md)
  + [Using Python in ADS Design Environment](../intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../intro/extension.md)
* [Concepts](index.md)
  + [Terminology](terminology.md)
    - [Workspace Elements](workspace_elements.md)
    - Connectivity Objects
  + [OpenAccess Integration](openaccess_integration.md)
  + [Python Script Execution](execution.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
  + [How to Use Pytest](../howto/pytest.md)

* [Design](../../pypde/docs/index.md)
  + [Reference](../../pypde/docs/reference/index.md)
    - [keysight.ads.de](../../pypde/docs/reference/de/index.md)
      * [Workspace](../../pypde/docs/reference/de/workspace.md)
      * [Library](../../pypde/docs/reference/de/library.md)
      * [Cell](../../pypde/docs/reference/de/cell.md)
      * [View](../../pypde/docs/reference/de/view.md)
      * [CellviewRef](../../pypde/docs/reference/de/cellviewref.md)
      * [DesignHierarchy](../../pypde/docs/reference/de/design_hierarchy.md)
      * [DMData](../../pypde/docs/reference/de/dmdata.md)
      * [ItemInfo](../../pypde/docs/reference/de/item_info.md)
      * [Points](../../pypde/docs/reference/de/points.md)
      * [Collections](../../pypde/docs/reference/de/collections.md)
    - [keysight.ads.de.ael](../../pypde/docs/reference/de/ael.md)
    - [keysight.ads.de.app](../../pypde/docs/reference/de/app/index.md)
      * [Actions and Menus](../../pypde/docs/reference/de/app/action.md)
      * [Addons](../../pypde/docs/reference/de/app/addon.md)
      * [Callbacks](../../pypde/docs/reference/de/app/callbacks.md)
      * [Windows and Widgets](../../pypde/docs/reference/de/app/window.md)
    - [keysight.ads.de.db](../../pypde/docs/reference/de/db/index.md)
      * [Callbacks](../../pypde/docs/reference/de/db/callbacks.md)
      * [Enumerated Types](../../pypde/docs/reference/de/db/enums.md)
      * [Parameter Forms](../../pypde/docs/reference/de/db/forms.md)
      * [GenPolyline](../../pypde/docs/reference/de/db/genpolyline.md)
      * [Model Definition](../../pypde/docs/reference/de/db/model_def.md)
      * [Parameters](../../pypde/docs/reference/de/db/parameters.md)
      * [Properties](../../pypde/docs/reference/de/db/properties.md)
      * [Transaction](../../pypde/docs/reference/de/db/transaction.md)
    - [keysight.ads.de.db\_dbu](../../pypde/docs/reference/de/db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../../pypde/docs/reference/de/db_uu/index.md)
      * [Design Elements](../../pypde/docs/reference/de/db_uu/db_uu.md)
      * [LayerId](../../pypde/docs/reference/de/db_uu/layer_id.md)
      * [LineTypeInfo](../../pypde/docs/reference/de/db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../../pypde/docs/reference/de/experimental/index.md)
      * [CDF](../../pypde/docs/reference/de/experimental/cdf/index.md)
      * [Commands](../../pypde/docs/reference/de/experimental/commands.md)
      * [Handles](../../pypde/docs/reference/de/experimental/handles.md)
      * [Netlist Utilities](../../pypde/docs/reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../pypde/docs/reference/de/experimental/polygon_utils.md)
      * [Preferences](../../pypde/docs/reference/de/experimental/preferences.md)
      * [xxPro View](../../pypde/docs/reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../pypde/docs/reference/de/experimental/symbol.md)
      * [Text Maker](../../pypde/docs/reference/de/experimental/text_maker.md)
    - [keysight.ads.de.tech](../../pypde/docs/reference/de/tech/index.md)
      * [Tech](../../pypde/docs/reference/de/tech/tech.md)
      * [Padstacks](../../pypde/docs/reference/de/tech/pads/pads.md)
      * [Via Rules](../../pypde/docs/reference/de/tech/rule/rule.md)
      * [Nested Technology](../../pypde/docs/reference/de/tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../../pypde/docs/reference/de/app/dds.md)
  + [Examples](../../pypde/docs/examples/index.md)
    - [Calling Between AEL and Python](../../pypde/docs/examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../pypde/docs/examples/ex_create_layout.md)
    - [Create Schematic](../../pypde/docs/examples/ex_create_schematic.md)
    - [Create Workspace](../../pypde/docs/examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../pypde/docs/examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../pypde/docs/examples/ex_cdf.md)
    - [Component Parameters](../../pypde/docs/examples/ex_parameters.md)
    - [Creating an Item Definition](../../pypde/docs/examples/ex_itemdef.md)
    - [Model Definition Properties](../../pypde/docs/examples/ex_model.md)
    - [Adding Instances to a Design](../../pypde/docs/examples/ex_lpf.md)
    - [Properties](../../pypde/docs/examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../pypde/docs/examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../pypde/docs/examples/ex_padstack.md)
    - [Nested Technology](../../pypde/docs/examples/ex_nested.md)
    - [Rules](../../pypde/docs/examples/ex_rules.md)
    - [Placing Text](../../pypde/docs/examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../pypde/docs/examples/ex_polygon.md)
    - [PySide2](../../pypde/docs/examples/ex_pyside.md)
    - [Traversing Hierarchy](../../pypde/docs/examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../pypde/docs/examples/ex_working_with_var.md)
    - [XML RPC](../../pypde/docs/examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../pypde/docs/examples/ex_translate_gds.md)
* [Technology](../../pysubst/docs/index.md)
  + [Reference](../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Connectivity Objects[](#connectivity-objects "Link to this heading")

Connectivity objects in ADS Python represent the logical and physical connections between components.
They include Nets, Terms, Pins, InstTerms, and InstPins.

## Net[](#net "Link to this heading")

A [`Net`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu.Net") represents the logical connectivity within a design, the
electrical path in a circuit. A collection of wires or interconnects that carry the same signal is
considered to be on the same net. Nets connect to Terms and InstTerms.

ADS Python supports multiple types of Nets:

[`ScalarNet`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.ScalarNet "keysight.ads.de.db_uu.ScalarNet"): A single-bit net that is not part of a BusNet and
does not use bus-name syntax. Generally speaking, ScalarNet is the most common type of Net.

[`BusNet`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.BusNet "keysight.ads.de.db_uu.BusNet"): A multi-bit Net that shares a common base name and uses
bus-name syntax (e.g. “A<0:7>”). A BusNet can be viewed as a collection of single-bit logical connections.

[`BusNetBit`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.BusNetBit "keysight.ads.de.db_uu.BusNetBit"): A single-bit of a BusNet and uses bus-name syntax
(e.g. “A<0>”).

[`BundleNet`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.BundleNet "keysight.ads.de.db_uu.BundleNet"). A multi-bit Net that does not share a common base
name, but instead uses comma separated names for each bit (e.g., “A, B, C”)

The following image shows a schematic with the net, Net1. The three wires and the InstTerms they are
connected to are all on Net1.

![../../_images/net.png](../../_images/net.png)

## Term[](#term "Link to this heading")

A [`Term`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term") (terminal) represents a logical connection point for a design.
Nets associated with the terminals are logically made available to the next higher level in a design hierarchy.
Pins associated with a Term represent the physical connection point for the design.

## Pin[](#pin "Link to this heading")

A [`Pin`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Pin "keysight.ads.de.db_uu.Pin") represents a physical connection point of terminals to
nets. A term can have multiple pins, where multiple physical connections can correspond to a
single logical connection. A pin is associated with one or more phsyical figures and holds information
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

An [`InstTerm`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.InstTerm "keysight.ads.de.db_uu.InstTerm") represents a logical connection point between
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

An [`InstPin`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.InstPin "keysight.ads.de.db_uu.InstPin") represents a pin in the master design of an instance
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

OpenAccess Integration](openaccess_integration.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top