<!-- 来源: pysubst\docs\examples\ex_substrate_with_layout.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Examples](../../../examples.md)
* [Substrate](index.md)
* Substrate with Layout

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

* [Introduction](../../../pydocs/intro/index.md)
* [How-To](../../../pydocs/howto/index.md)
  + [Use Python in the ADS Application](../../../pydocs/howto/embedded.md)
  + [Set Up a Python Virtual Environment](../../../pydocs/howto/venv.md)
  + [Set Up Visual Studio Code for Development](../../../pydocs/howto/vscode.md)
  + [Use Pytest](../../../pydocs/howto/pytest.md)
  + [Enable Python Support For Your Library](../../../pydocs/howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../../../pydocs/howto/execution.md)
  + [Export Workspace and Design Objects to Python](../../../pydocs/howto/exporter.md)
  + [Record Actions in ADS as Python Code](../../../pydocs/howto/recorder.md)
  + [Develop a Python Pcell in ADS](../../../pydocs/howto/pcell.md)
* [ADS Concepts](../../../pydocs/concepts/index.md)
  + [Workspace Elements](../../../pydocs/concepts/workspace_elements.md)
  + [Connectivity Objects](../../../pydocs/concepts/connectivity.md)
* [Reference](../../../reference.md)
  + [Deprecated APIs](../../../pydocs/py/_generated/deprecations.md)
  + [Design Environment](../../../pypde/docs/reference/index.md)
    - [keysight.ads.de](../../../pypde/docs/reference/de/index.md)
      * [ADS Application Environment](../../../pypde/docs/reference/de/ads_environment.md)
      * [ADS Workspace Components](../../../pypde/docs/reference/de/workspace_components.md)
      * [Design Hierarchy](../../../pypde/docs/reference/de/design_hierarchy.md)
      * [Smart Package](../../../pypde/docs/reference/de/package.md)
      * [Geometry](../../../pypde/docs/reference/de/geometry.md)
      * [Collections](../../../pypde/docs/reference/de/collections.md)
      * [Printer](../../../pypde/docs/reference/de/printer.md)
    - [keysight.ads.de.ael](../../../pypde/docs/reference/de/ael.md)
    - [keysight.ads.de.app](../../../pypde/docs/reference/de/app/index.md)
      * [Application](../../../pypde/docs/reference/de/app/application.md)
      * [Actions and Menus](../../../pypde/docs/reference/de/app/action.md)
      * [Addons](../../../pypde/docs/reference/de/app/addon.md)
      * [Window and Design Callbacks](../../../pypde/docs/reference/de/app/callbacks.md)
      * [Windows and Widgets](../../../pypde/docs/reference/de/app/window.md)
      * [Experimental](../../../pypde/docs/reference/de/app/experimental.md)
    - [keysight.ads.de.app.dds](../../../pypde/docs/reference/de/app/dds.md)
      * [exec\_python](../../../pypde/docs/reference/de/app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../../pypde/docs/reference/de/db/index.md)
      * [Models, Parameters, and Forms](../../../pypde/docs/reference/de/db/parameters.md)
      * [Properties](../../../pypde/docs/reference/de/db/properties.md)
      * [Preferences](../../../pypde/docs/reference/de/db/preferences.md)
      * [Transaction](../../../pypde/docs/reference/de/db/transaction.md)
      * [Smart Mount](../../../pypde/docs/reference/de/db/smart_mount.md)
      * [Geometry](../../../pypde/docs/reference/de/db/geometry.md)
      * [Teardrops](../../../pypde/docs/reference/de/db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../../pypde/docs/reference/de/db_dbu/index.md)
      * [DbBox](../../../pypde/docs/reference/de/db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../../pypde/docs/reference/de/db_uu/index.md)
      * [Database Objects](../../../pypde/docs/reference/de/db_uu/database_objects.md)
      * [Iterators](../../../pypde/docs/reference/de/db_uu/iterators.md)
      * [Designs](../../../pypde/docs/reference/de/db_uu/design.md)
      * [Teardrops](../../../pypde/docs/reference/de/db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../../../pypde/docs/reference/de/experimental/index.md)
      * [CDF](../../../pypde/docs/reference/de/experimental/cdf.md)
      * [Design Commands](../../../pypde/docs/reference/de/experimental/commands.md)
      * [Component Handles](../../../pypde/docs/reference/de/experimental/handles.md)
      * [Netlist Utilities](../../../pypde/docs/reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../../pypde/docs/reference/de/experimental/polygon_utils.md)
      * [xxPro View](../../../pypde/docs/reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../../pypde/docs/reference/de/experimental/symbol.md)
      * [Text Maker](../../../pypde/docs/reference/de/experimental/text_maker.md)
      * [Notebook](../../../pypde/docs/reference/de/experimental/notebook.md)
      * [Layer/Purpose Pairs](../../../pypde/docs/reference/de/experimental/lpp.md)
    - [keysight.ads.de.tech](../../../pypde/docs/reference/de/tech/index.md)
      * [Technology](../../../pypde/docs/reference/de/tech/tech.md)
      * [Layers](../../../pypde/docs/reference/de/tech/layers.md)
      * [Line Items](../../../pypde/docs/reference/de/tech/line_items.md)
      * [Padstacks](../../../pypde/docs/reference/de/tech/pads.md)
      * [Rules](../../../pypde/docs/reference/de/tech/rule.md)
  + [Substrate](../reference/index.md)
    - [keysight.ads.subst](../reference/subst/index.md)
      * [Substrate and Materials](../reference/subst/subst.md)
* [Examples](../../../examples.md)
  + [Design Environment](../../../pypde/docs/examples/index.md)
    - [Workspace Creation](../../../pypde/docs/examples/workspace/ex_workspace.md)
    - [Design Creation](../../../pypde/docs/examples/design_creation/index.md)
      * [Create Layout](../../../pypde/docs/examples/design_creation/ex_create_layout.md)
      * [Create Schematic](../../../pypde/docs/examples/design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../../../pypde/docs/examples/design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../../../pypde/docs/examples/design_elements/index.md)
      * [Placing Text](../../../pypde/docs/examples/design_elements/ex_place_text.md)
      * [Moving Objects](../../../pypde/docs/examples/design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../../../pypde/docs/examples/design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../../../pypde/docs/examples/design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../../../pypde/docs/examples/design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../../../pypde/docs/examples/design_elements/ex_plane_editing.md)
    - [Parameters](../../../pypde/docs/examples/parameters/index.md)
      * [Interoperable Component Parameters](../../../pypde/docs/examples/parameters/ex_cdf.md)
      * [Working with VAR](../../../pypde/docs/examples/parameters/ex_working_with_var.md)
      * [Component Parameters](../../../pypde/docs/examples/parameters/ex_parameters.md)
      * [Creating an Item Definition](../../../pypde/docs/examples/parameters/ex_itemdef.md)
      * [Model Definition Properties](../../../pypde/docs/examples/parameters/ex_model.md)
      * [Creating a Text Form](../../../pypde/docs/examples/parameters/ex_text_form.md)
      * [Properties](../../../pypde/docs/examples/parameters/ex_properties.md)
    - [Technology](../../../pypde/docs/examples/technology/index.md)
      * [Padstacks and Vias](../../../pypde/docs/examples/technology/ex_padstack.md)
      * [Nested Technology](../../../pypde/docs/examples/technology/ex_nested.md)
      * [Rules](../../../pypde/docs/examples/technology/ex_rules.md)
    - [Translators](../../../pypde/docs/examples/translators/index.md)
      * [DXF Import and Export](../../../pypde/docs/examples/translators/ex_translate_dxf.md)
      * [Gerber Export](../../../pypde/docs/examples/translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../../../pypde/docs/examples/translators/ex_translate_gds.md)
    - [UI](../../../pypde/docs/examples/ui/index.md)
      * [Creating Custom Menus Using an Addon](../../../pypde/docs/examples/ui/ex_menu_addon.md)
      * [PySide](../../../pypde/docs/examples/ui/ex_pyside.md)
    - [Utility](../../../pypde/docs/examples/utility/index.md)
      * [Calling Between AEL and Python](../../../pypde/docs/examples/utility/ex_calling_ael_and_python.md)
      * [Smart Package](../../../pypde/docs/examples/utility/ex_smart_pkg.md)
      * [XML RPC](../../../pypde/docs/examples/utility/ex_xml_rpc.md)
  + [Substrate](index.md)
    - [Create Substrate](ex_make_substrate.md)
    - Substrate with Layout
    - [Z-Height of a Strip Conductor in a Substrate](ex_substrate_strip_height.md)
* [Index](../../../genindex.md)

# Substrate with Layout[](#substrate-with-layout "Link to this heading")

This example demonstrates creating a simple layout with its associated substrate.

```
# Copyright Keysight Technologies 2024 - 2024
from keysight.ads import de
from keysight.ads import subst as subst
from keysight.ads.de import db_uu
from keysight.ads.de.db import LayerId

def configure_library_tech(library: de.Library) -> None:
    # Configures the library for the example by copying the tech from standard ADS libraries
    library.setup_schematic_tech()
    library.create_layout_tech_std_ads("mil", 10000, True)

def create_layout(library: de.Library) -> db_uu.Design:
    layout = db_uu.create_layout(f"{library.name}:My_Substrate_Example:layout")

    # Add a 300x100 rectangle on the left on layer "cond:drawing"
    cond = LayerId.from_name(library, "cond", "drawing")
    layout.add_rectangle(cond, (0, 0), (300, 100))

    # Add a 200x100 rectangle overlapping first rectangle on the right on layer "cond2:drawing"
    cond2 = LayerId.from_name(library, "cond2", "drawing")
    layout.add_rectangle(cond2, (200, 0), (400, 100))

    # Add a radius 30 circle in the overlapping portion of the two rectangles on layer "hole:drawing"
    hole = LayerId.from_name(library, "hole", "drawing")
    layout.add_circle(hole, (250, 50), 30)

    # Add a pin on the ground net on the left side of the cond layer's rectangle
    gnd_net = layout.find_or_add_net("gnd!")
    term_1 = layout.add_term(gnd_net, "P1")
    pin1_pinfig = layout.add_dot(cond, (0, 50))
    layout.add_pin(term_1, pin1_pinfig, angle=180.0)

    # Add a pin on the ground net on the right side of the cond2 layer's rectangle
    term_2 = layout.add_term(gnd_net, "P2")
    pin2_pinfig = layout.add_dot(cond2, (400, 50))
    layout.add_pin(term_2, pin2_pinfig)

    # Save changes to the layout file
    layout.save_design()

    return layout

def create_substrate(library: de.Library) -> subst.Substrate:
    # Create a new substrate using "25milAlumina" as a starting point
    substrate = subst.create_substrate_from_template(library, "example_substrate", "25milAlumina")

    # Configure the cond layer to be a Gold sheet
    cond = substrate.layers[0]
    cond.layer_number = LayerId.from_name(library, "cond", "drawing").layer
    cond.sheet = True
    cond.material_name = "Gold"

    # Inserts a new material at the given index with an interface directly above it
    substrate.insert_material_and_interface_above(substrate.top_material_index)
    # Find the newly created material and set its properties
    dielectric = substrate.get_material_above(cond.interface)
    # Note this material will need to be defined manually in the library's technology
    dielectric.material_name = "Dielectric_1"
    dielectric.thickness = 30

    # Insert the cond2 layer
    cond2_interface = substrate.get_interface_above(dielectric)
    cond2 = substrate.insert_layer(cond2_interface, de.ProcessRole.CONDUCTOR)
    cond2.layer_number = LayerId.from_name(library, "cond2", "drawing").layer
    # Set cond2 to intrude above the interface
    cond2.expand = False
    cond2.sheet = False
    cond2.is_above = True
    # Note this material will need to be defined manually in the library's technology
    cond2.material_name = "Conductor_1"

    # Create the via between the cond and cond2 layers
    via = substrate.insert_conductor_via(cond.interface, cond2.interface)
    # Set the via layer to "hole:drawing" to match the layout
    via.layer_number = LayerId.from_name(library, "hole", "drawing").layer
    via.material_name = "PERFECT_CONDUCTOR"

    # Save all our changes to the substrate file
    substrate.save_substrate()
    return substrate
```

The layout includes two metal conductors on differing layers connected by a via:

![../../../_images/ex_substrate_with_layout_layout.png](../../../_images/ex_substrate_with_layout_layout.png)

![../../../_images/ex_substrate_with_layout_3d_layout.png](../../../_images/ex_substrate_with_layout_3d_layout.png)

The substrate defines the materials and thicknesses of the design created in the layout:

![../../../_images/ex_substrate_with_layout_substrate.png](../../../_images/ex_substrate_with_layout_substrate.png)

On this page

[Previous

Create Substrate](ex_make_substrate.md)
[Next

Z-Height of a Strip Conductor in a Substrate](ex_substrate_strip_height.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top