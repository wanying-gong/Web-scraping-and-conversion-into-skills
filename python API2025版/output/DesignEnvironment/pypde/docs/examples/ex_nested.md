<!-- 来源: pypde\docs\examples\ex_nested.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* [Examples](index.md)
* Nested Technology

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
    - Nested Technology
    - [Rules](ex_rules.md)
    - [Placing Text](ex_place_text.md)
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

# Nested Technology[](#nested-technology "Link to this heading")

The following example shows how to create nested technology and layer maps from the nested library to the parent library.

```
# Copyright Keysight Technologies 2025

"""Example nested technology using the Python API."""

from keysight.ads import de

def map_nested_technology(workspace: de.Workspace) -> None:
    """Create nested technology and map layers.

    Creates RF_Board_lib and maps layers from the nested technology library smt_lib.
    """
    # create the smt_lib with technology using millimeter units
    smt_lib = create_smt_lib(workspace)
    # create the RF_Board_lib with technology using mil units and using smt_lib as nested technology
    board_lib = create_rf_board_lib(workspace, smt_lib)
    # Different ways to look up the same layer map
    layer_map1 = board_lib.tech.layer_maps[0]
    layer_map2 = board_lib.tech.layer_maps.find("smt_top")
    layer_map = de.tech.nested.find_layer_map("RF_Board_lib", "smt_top")
    assert layer_map is not None
    assert layer_map == layer_map1
    assert layer_map == layer_map2
    assert layer_map.name == "smt_top"
    assert layer_map.nested_library_name == "smt_lib"
    # The parent library is the layer_map_library
    assert layer_map.layer_map_library_name == "RF_Board_lib"
    assert layer_map.nested_mapped_layers[0] == "cond"
    # Mapped layers default to {layer_map_name}_{nested_lib_name}_{nested_layer_name}
    assert layer_map.parent_mapped_layers[0] == "smt_top_smt_lib_cond"

    # find_layer_map returns None if the named layer map is not found
    bottom_layer_map = de.tech.nested.find_layer_map("RF_Board_lib", "smt_bottom")
    if bottom_layer_map is None:
        new_layer_map = de.tech.nested.LayerMap("smt_bottom", "smt_lib", "RF_Board_lib")
        new_layer_map.is_above = False
        new_layer_map.is_flipped = True
        new_layer_map.map_nested_layer("cond")
        # new_layer_map.nested_mapped_layers.append("cond")
        # new_layer_map.parent_mapped_layers = ["smt_bottom_smt_lib_cond"]
        board_lib.tech.layer_maps.append(new_layer_map)
        board_lib.tech.save_layer_maps()
    layer_map.unmap_nested_layer("ports")

def create_smt_lib(workspace: de.Workspace) -> de.Library:
    # Create a "smt_lib" library with tech using millimeters
    smt_lib = de.create_new_library("smt_lib", workspace.path / "smt_lib")
    workspace.add_library(smt_lib.name, smt_lib.path, de.LibraryMode.SHARED)
    smt_lib.setup_schematic_tech()
    smt_lib.create_layout_tech_std_ads("millimeter", 1000)
    return smt_lib

def create_rf_board_lib(workspace: de.Workspace, smt_lib: de.Library) -> de.Library:
    # Create a "RF_Board_lib" library with tech using mils
    rf_lib = de.create_new_library("RF_Board_lib", workspace.path / "RF_Board_lib")
    workspace.add_library(rf_lib.name, rf_lib.path, de.LibraryMode.SHARED)
    rf_lib.setup_schematic_tech()
    rf_lib.create_layout_tech_std_ads("mil", 1000)

    # Create a layer map between "RF_Board_lib" and "smt_lib" for the "cond" and "ports" layers
    layer_map = de.tech.nested.LayerMap("smt_top", smt_lib, rf_lib)
    layer_map.map_nested_layer("cond")
    layer_map.map_nested_layer("ports")
    rf_lib.tech.layer_maps.append(layer_map)
    return rf_lib
```

The following image shows the nested technology settings for the RF\_Board\_lib library created in the example above.

![../../../_images/nested_technology.png](../../../_images/nested_technology.png)

The following image shows the layer mapping created for layers between RF\_Board\_lib and smt\_lib in the smt\_top layer map from the previous example.
Note that the default orientation and positioning is above pointing up.

![../../../_images/nested_mapped_layers_smt_top.png](../../../_images/nested_mapped_layers_smt_top.png)

The following image shows the layer mapping created for layers between RF\_Board\_lib and smt\_lib in the smt\_bottom layer map from the previous example.
Note that the orientation and positioning is below pointing down as set in the example using the [`is_above`](../reference/de/tech/nested/nested.md#keysight.ads.de.tech.nested.LayerMap "keysight.ads.de.tech.nested.LayerMap") and [`is_flipped`](../reference/de/tech/nested/nested.md#keysight.ads.de.tech.nested.LayerMap "keysight.ads.de.tech.nested.LayerMap") properties.

![../../../_images/nested_mapped_layers_smt_bottom.png](../../../_images/nested_mapped_layers_smt_bottom.png)

On this page

[Previous

Padstacks and Vias](ex_padstack.md)
[Next

Rules](ex_rules.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top