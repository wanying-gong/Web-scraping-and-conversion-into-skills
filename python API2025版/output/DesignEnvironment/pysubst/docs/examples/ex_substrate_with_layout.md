<!-- 来源: pysubst\docs\examples\ex_substrate_with_layout.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Technology](../index.md)
* [Examples](index.md)
* Substrate with Layout

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

* [Design](../../../pypde/docs/index.md)
  + [Reference](../../../pypde/docs/reference/index.md)
    - [keysight.ads.de](../../../pypde/docs/reference/de/index.md)
      * [Workspace](../../../pypde/docs/reference/de/workspace.md)
      * [Library](../../../pypde/docs/reference/de/library.md)
      * [Cell](../../../pypde/docs/reference/de/cell.md)
      * [View](../../../pypde/docs/reference/de/view.md)
      * [CellviewRef](../../../pypde/docs/reference/de/cellviewref.md)
      * [DesignHierarchy](../../../pypde/docs/reference/de/design_hierarchy.md)
      * [DMData](../../../pypde/docs/reference/de/dmdata.md)
      * [ItemInfo](../../../pypde/docs/reference/de/item_info.md)
      * [Points](../../../pypde/docs/reference/de/points.md)
      * [Collections](../../../pypde/docs/reference/de/collections.md)
    - [keysight.ads.de.ael](../../../pypde/docs/reference/de/ael.md)
    - [keysight.ads.de.app](../../../pypde/docs/reference/de/app/index.md)
      * [Actions and Menus](../../../pypde/docs/reference/de/app/action.md)
      * [Addons](../../../pypde/docs/reference/de/app/addon.md)
      * [Callbacks](../../../pypde/docs/reference/de/app/callbacks.md)
      * [Windows and Widgets](../../../pypde/docs/reference/de/app/window.md)
    - [keysight.ads.de.db](../../../pypde/docs/reference/de/db/index.md)
      * [Callbacks](../../../pypde/docs/reference/de/db/callbacks.md)
      * [Enumerated Types](../../../pypde/docs/reference/de/db/enums.md)
      * [Parameter Forms](../../../pypde/docs/reference/de/db/forms.md)
      * [GenPolyline](../../../pypde/docs/reference/de/db/genpolyline.md)
      * [Model Definition](../../../pypde/docs/reference/de/db/model_def.md)
      * [Parameters](../../../pypde/docs/reference/de/db/parameters.md)
      * [Properties](../../../pypde/docs/reference/de/db/properties.md)
      * [Transaction](../../../pypde/docs/reference/de/db/transaction.md)
    - [keysight.ads.de.db\_dbu](../../../pypde/docs/reference/de/db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../../../pypde/docs/reference/de/db_uu/index.md)
      * [Design Elements](../../../pypde/docs/reference/de/db_uu/db_uu.md)
      * [LayerId](../../../pypde/docs/reference/de/db_uu/layer_id.md)
      * [LineTypeInfo](../../../pypde/docs/reference/de/db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../../../pypde/docs/reference/de/experimental/index.md)
      * [CDF](../../../pypde/docs/reference/de/experimental/cdf/index.md)
      * [Commands](../../../pypde/docs/reference/de/experimental/commands.md)
      * [Handles](../../../pypde/docs/reference/de/experimental/handles.md)
      * [Netlist Utilities](../../../pypde/docs/reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../../pypde/docs/reference/de/experimental/polygon_utils.md)
      * [Preferences](../../../pypde/docs/reference/de/experimental/preferences.md)
      * [xxPro View](../../../pypde/docs/reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../../pypde/docs/reference/de/experimental/symbol.md)
      * [Text Maker](../../../pypde/docs/reference/de/experimental/text_maker.md)
    - [keysight.ads.de.tech](../../../pypde/docs/reference/de/tech/index.md)
      * [Tech](../../../pypde/docs/reference/de/tech/tech.md)
      * [Padstacks](../../../pypde/docs/reference/de/tech/pads/pads.md)
      * [Via Rules](../../../pypde/docs/reference/de/tech/rule/rule.md)
      * [Nested Technology](../../../pypde/docs/reference/de/tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../../../pypde/docs/reference/de/app/dds.md)
  + [Examples](../../../pypde/docs/examples/index.md)
    - [Calling Between AEL and Python](../../../pypde/docs/examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../../pypde/docs/examples/ex_create_layout.md)
    - [Create Schematic](../../../pypde/docs/examples/ex_create_schematic.md)
    - [Create Workspace](../../../pypde/docs/examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../../pypde/docs/examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../../pypde/docs/examples/ex_cdf.md)
    - [Component Parameters](../../../pypde/docs/examples/ex_parameters.md)
    - [Creating an Item Definition](../../../pypde/docs/examples/ex_itemdef.md)
    - [Model Definition Properties](../../../pypde/docs/examples/ex_model.md)
    - [Adding Instances to a Design](../../../pypde/docs/examples/ex_lpf.md)
    - [Properties](../../../pypde/docs/examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../../pypde/docs/examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../../pypde/docs/examples/ex_padstack.md)
    - [Nested Technology](../../../pypde/docs/examples/ex_nested.md)
    - [Rules](../../../pypde/docs/examples/ex_rules.md)
    - [Placing Text](../../../pypde/docs/examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../../pypde/docs/examples/ex_polygon.md)
    - [PySide2](../../../pypde/docs/examples/ex_pyside.md)
    - [Traversing Hierarchy](../../../pypde/docs/examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../../pypde/docs/examples/ex_working_with_var.md)
    - [XML RPC](../../../pypde/docs/examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../../pypde/docs/examples/ex_translate_gds.md)
* [Technology](../index.md)
  + [Reference](../reference/index.md)
    - [keysight.ads.subst](../reference/subst/index.md)
  + [Examples](index.md)
    - [Create Substrate](ex_make_substrate.md)
    - Substrate with Layout

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
    cond = LayerId.create_layer_id_from_library(library, "cond", "drawing")
    layout.add_rectangle(cond, (0, 0), (300, 100))

    # Add a 200x100 rectangle overlapping first rectangle on the right on layer "cond2:drawing"
    cond2 = LayerId.create_layer_id_from_library(library, "cond2", "drawing")
    layout.add_rectangle(cond2, (200, 0), (400, 100))

    # Add a radius 30 circle in the overlapping portion of the two rectangles on layer "hole:drawing"
    hole = LayerId.create_layer_id_from_library(library, "hole", "drawing")
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
    cond.layer_number = LayerId.create_layer_id_from_library(library, "cond", "drawing").layer
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
    cond2.layer_number = LayerId.create_layer_id_from_library(library, "cond2", "drawing").layer
    # Set cond2 to intrude above the interface
    cond2.expand = False
    cond2.sheet = False
    cond2.is_above = True
    # Note this material will need to be defined manually in the library's technology
    cond2.material_name = "Conductor_1"

    # Create the via between the cond and cond2 layers
    via = substrate.insert_conductor_via(cond.interface, cond2.interface)
    # Set the via layer to "hole:drawing" to match the layout
    via.layer_number = LayerId.create_layer_id_from_library(library, "hole", "drawing").layer
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

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top