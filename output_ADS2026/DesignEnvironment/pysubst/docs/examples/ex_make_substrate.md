<!-- 来源: pysubst\docs\examples\ex_make_substrate.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Examples](../../../examples.md)
* [Substrate](index.md)
* Create Substrate

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
    - Create Substrate
    - [Substrate with Layout](ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](ex_substrate_strip_height.md)
* [Index](../../../genindex.md)

# Create Substrate[](#create-substrate "Link to this heading")

For more on substrates, see [Substrates in ADS](..%5C..%5C..%5C..%5C..%5C..%5Cads%5CContent%5Cads2026update2%5Cusrguide%5CSubstrates_in_ADS.md).

This example shows how to create a simple substrate in your library

```
# Copyright Keysight Technologies 2024 - 2024
import keysight.ads.de as de
from keysight.ads import subst as substrate

# Example usage:
# wrk = de.open_workspace(path_to_workspace)
# lib = wrk.open_library("MyLibrary_lib", path_to_library, de.LibraryMode.SHARED)
# make_simple_substrate(lib, "my_substrate")

def make_simple_substrate(library: de.Library, subst_name: str) -> None:
    assert not library.is_read_only

    # Start by creating an "empty" substrate.
    subst = substrate.create_substrate(library, subst_name)
    assert substrate.substrate_exists(library, subst_name)
    assert not subst.is_read_only
    assert subst.is_writable

    # See what materials are available
    if False:
        names = substrate.get_conductor_names(library)
        assert len(names) != 0
        names = substrate.get_semiconductor_names(library)
        names = substrate.get_superconductor_names(library)
        names = substrate.get_dielectric_names(library)
        names = substrate.get_roughness_names(library)

    # If you need to specify a list of purposes to ignore, use this
    if True:
        subst.purposes_to_exclude = ["Dummy"]
        assert not subst.purposes_to_include
    else:
        subst.purposes_to_include = ["Drawing"]
        assert not subst.purposes_to_exclude

    # This substrate will have two infinite materials and three interfaces
    assert len(subst.materials) == 2
    assert len(subst.interfaces) == 3
    assert subst.materials[0].is_infinite_material
    top_material_index = subst.top_material_index
    assert subst.materials[top_material_index].is_infinite_material
    assert not subst.has_top_cover
    interface0 = subst.interfaces[0]
    assert not interface0.is_cover
    assert interface0.is_non_cover_placeholder

    # Convert the bottom interface to a cover
    if False:
        # The hard way
        interface0.purpose = substrate.InterfaceItem.Purpose.COVER
        interface0.material_name = "PERFECT_CONDUCTOR"
    else:
        interface0.convert_to_cover()
    interface0.thickness_expr = "0.0123"  # just so we can identify this interface
    assert interface0.is_cover
    assert not interface0.is_non_cover_placeholder
    assert subst.has_bottom_cover

    material0 = subst.materials[0]
    # Since the bottom interface is now a cover, material0 won't be infinite
    assert not material0.is_infinite_material
    material0.thickness_expr = "100"
    material0.thickness_unit = substrate.Unit.MICRON
    material0.material_name = "SiliconNitride"

    interface1 = subst.interfaces[1]
    if True:
        # You can specify interface by index
        layer = subst.insert_layer(1, de.ProcessRole.CONDUCTOR)
    else:
        # You can can also pass interfaces
        layer = subst.insert_layer(interface1, de.ProcessRole.CONDUCTOR)
    layer.layer_number = 2
    layer.material_name = "Au"
    layer.thickness_expr = "0.01"
    layer.thickness_unit = substrate.Unit.MIL
    # The layer item can represent a sheet that neither expands nor intrudes into the material.
    assert layer.sheet is True
    layer.sheet = False
    layer.expand = True  # Otherwise we intrude
    # Note that setting is_above to False sets the thickness negative
    layer.is_above = False  # so it expands the material below the interface
    assert layer.thickness_expr == "-0.01"
    subst.save_substrate()

    if True:
        # This will leave the bottom material and layer alone
        subst.insert_material_and_interface_above(1)
    elif False:
        # This will shove the layer up to interface 2 and the bottom material up to material 1
        subst.insert_material_and_interface_above(0)
    else:
        # This will shove the layer up to interface 2
        subst.insert_material_and_interface_below(1)
    # There is now one more material and one more interface than before
    assert len(subst.materials) == 3
    assert len(subst.interfaces) == 4
    material1 = subst.materials[1]
    material1.material_name = "Alumina"

    subst.save_substrate()

    # If we set the thickness of the top material, it won't
    # be relevant because there is no top cover so the material is infinite.
    material2 = subst.materials[2]
    material2.thickness_expr = "2000"
    material2.thickness_unit = substrate.Unit.MICRON
    assert material2.is_infinite_material
    subst.save_substrate()

    # If we add one more material and interface, material2 won't be infinite.
    subst.insert_material_and_interface_below(3)
    assert not material2.is_infinite_material
    assert material2.thickness == 2000

    if False:
        # The basic function...
        via = subst.insert_via(1, 2, de.ProcessRole.CONDUCTOR_VIA)
    elif False:
        # You can specify interface by index
        via = subst.insert_conductor_via(1, 2)
    else:
        # You can can also pass interfaces
        interface2 = subst.interfaces[2]
        via = subst.insert_conductor_via(interface1, interface2)

    via.layer_number = 2  # cond2
    via.material_name = "nicr"
    assert via.process_role == de.ProcessRole.CONDUCTOR_VIA
    via.is_plating_enabled = True
    via.plating_dielectric_material_name = "SiliconNitride"
    via.plating_thickness = 0.1
    via.plating_thickness_unit = substrate.Unit.MILLIMETER
    subst.save_substrate()

    nested_subst = subst.insert_substrate(interface2)
    nested_subst.set_library_and_substrate_names(library.name, "empty")
    assert nested_subst.library_name == library.name
    assert nested_subst.substrate_name == "empty"

    # There are three choices for alignment
    if False:
        nested_subst.align_type = substrate.SubstrateItem.AlignType.BOTTOM
    elif False:
        nested_subst.align_type = substrate.SubstrateItem.AlignType.TOP
    else:
        nested_subst.align_type = substrate.SubstrateItem.AlignType.LAYER
    # When aligning with a layer, we have to specify which part of the layer aligns
    nested_subst.alignment_position = substrate.SubstrateItem.AlignPosition.TOP_OF_LAYER
    nested_subst.align_layer_name = "cond2"
    subst.save_substrate()

    # If you don't need it any more, you can delete it
    if False:
        substrate.delete_substrate(library, subst_name)
```

On this page

[Previous

Substrate](index.md)
[Next

Substrate with Layout](ex_substrate_with_layout.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top