<!-- 来源: pysubst\docs\examples\ex_substrate_strip_height.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Examples](../../../examples.md)
* [Substrate](index.md)
* Z-Height of a Strip Conductor in a Substrate

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
    - [Substrate with Layout](ex_substrate_with_layout.md)
    - Z-Height of a Strip Conductor in a Substrate
* [Index](../../../genindex.md)

# Z-Height of a Strip Conductor in a Substrate[](#z-height-of-a-strip-conductor-in-a-substrate "Link to this heading")

This example demonstrates how to determine the Z-height of a strip conductor layer in a substate.

Using the substrate editor, you can see the different Z heights in the substrate of the mapped conductors, metal layers in the stackup.
The example function below uses the ADS Python substrate module ([`Substrate`](../reference/subst/_autosummary/keysight.ads.subst.Substrate.md#keysight.ads.subst.Substrate "keysight.ads.subst.Substrate")) to open the substrate, look up the various thicknesses,
and return the Z height of the specified mapped strip conductor layer.

![../../../_images/ex_substrate_strip_height_1.png](../../../_images/ex_substrate_strip_height_1.png)

**NOTE:** The image of the above substrate was taken from the example library located in `%HPEESOF_DIR%/doc/python/de/examples/libs/subst_lib`.

From the substrate editor in which the stackup is visualized, you can see that, for example, the mapped layer `pc1` has a Z height of 623um (500 + 2 + 21 + 100).
When determining the Z height of a strip conductor layer in a substrate, there are some things to consider: Layers that intrude up or down will not modify the substrate thickness,
however, layers that expand down will increase the dielectric layer below with their thickness, whereas layers that expand up will increase the dielectric layer above with their metal thickness.
Sheet layers do not have any impact on the substrate thickness above or below. Note that multiple layers can be mapped onto the same interface, such as the layers `leads`, `ports`, and `pc1` in the above image.
Each layer may be an individual expand, intruded or strip layer. The logic for handling this is implemented in the script below.

When a mapped layer on an interface is of type “expanding”, the substrate layer, dielectric below (downward expansion) or above (upward expansion) will become thicker.
The strip layer thickness will be added to the substrate, dielectric thickness. This is explained in detail in the ADS manual (See: [Substrates in ADS](..%5C..%5C..%5C..%5C..%5C..%5Cads%5CContent%5Cads2026update2%5Cusrguide%5CSubstrates_in_ADS.md)),
but can also be observed from the substrate visualization:

![../../../_images/ex_substrate_strip_height_2.png](../../../_images/ex_substrate_strip_height_2.png)

The variable `max_expand_down_thickness_mks` will contain the value of the thickest downward expanded layer on a given interface. Note that multiple strip layers can be mapped on the same interface and they can have a different thicknesses.
Notice the `leads` and `pc1` layers; both are expanded upward, with the `leads` layer being 10um thick and the `pc1` layer only 5um.
As such, the `FR_4_Core` dielectric, with default thickness of 100um, gets expanded by 10um (the value of the thickest expanded layer on the same interface).

```
from keysight.ads.subst import Substrate

def get_strip_Z_height_in_substrate(substrate: Substrate, layer_lookup: str) -> float:
    """Calculate the cumulative height of the substrate stack up to the specified layer.

    Parameters
    ----------
    - substrate: Substrate object from ADS
    - layer_lookup: Name of the layer to find

    Returns
    -------
    - cumulative_layer_height: Total height up to the specified layer, in meters (MKS)

    """
    cumulative_layer_height = 0.0
    layer_found_on_interface = False

    # Loop through each interface in the substrate
    for interface in substrate.interfaces:

        # only expand up or down has an effect on the substrate height, intrude does not
        max_expand_down_thickness_mks = 0.0
        max_expand_up_thickness_mks = 0.0

        # we check only on STRIP (not cover or SLOT)
        if interface.purpose.name == "STRIP":
            layers_on_interface = substrate.get_layers_on_interface(interface)
            max_expand_down_thickness_mks = 0.0
            max_expand_up_thickness_mks = 0.0

            # Loop through each layer item on the interface
            for layer_item in layers_on_interface:
                layer_name = substrate.find_layer_name_from_number(layer_item.layer_number)

                # if layer_item is sheet, then there's no impact on the substrate height, and no handling is needed
                # if layer thickness is negative then it's downward expansion and take it into account
                # if layer thickness is positive then it's upward expansion and take it into account for the next dielectric

                # note: we only check expanded layers, as intrude has no effect on the substrate height
                # the strip only intrudes in substrate

                layer_item_thickness = layer_item.get_thickness_mks()

                # check to keep the thickest DOWN expanded layer of the multiple conductors on the same interface
                if layer_item.expand and layer_item_thickness < 0:
                    if abs(layer_item_thickness) > max_expand_down_thickness_mks:
                        max_expand_down_thickness_mks = abs(layer_item_thickness)

                if layer_item.expand and layer_item_thickness > 0:
                    if abs(layer_item_thickness) > max_expand_up_thickness_mks:
                        max_expand_up_thickness_mks = abs(layer_item_thickness)

                # Found the layer we are looking for
                if layer_name == layer_lookup:
                    layer_found_on_interface = True

            cumulative_layer_height += max_expand_down_thickness_mks

            if layer_found_on_interface:
                return cumulative_layer_height

        try:
            above_mat = substrate.get_material_above(interface)
        except RuntimeError:
            # "No material found above interface."
            pass

        else:
            if above_mat:
                # here we need to check for multiple positive expanded layers,
                cumulative_layer_height += above_mat.get_thickness_mks()
                cumulative_layer_height += max_expand_up_thickness_mks

    return cumulative_layer_height
```

On this page

[Previous

Substrate with Layout](ex_substrate_with_layout.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top