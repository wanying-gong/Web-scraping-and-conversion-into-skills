<!-- 来源: pypde\docs\reference\de\tech\nested\nested.html -->

[![Logo](../../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../../index.md)
* [Design](../../../../index.md)
* [Reference](../../../index.md)
* [keysight.ads.de.tech](../index.md)
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

* [Introduction](../../../../../../pydocs/intro/index.md)
  + [Licensing](../../../../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../../../../pydocs/intro/extension.md)
* [Concepts](../../../../../../pydocs/concepts/index.md)
  + [Terminology](../../../../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../../../../pydocs/concepts/execution.md)
* [How-To](../../../../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../../../../pydocs/howto/pytest.md)

* [Design](../../../../index.md)
  + [Reference](../../../index.md)
    - [keysight.ads.de](../../index.md)
      * [Workspace](../../workspace.md)
      * [Library](../../library.md)
      * [Cell](../../cell.md)
      * [View](../../view.md)
      * [CellviewRef](../../cellviewref.md)
      * [DesignHierarchy](../../design_hierarchy.md)
      * [DMData](../../dmdata.md)
      * [ItemInfo](../../item_info.md)
      * [Points](../../points.md)
      * [Collections](../../collections.md)
    - [keysight.ads.de.ael](../../ael.md)
    - [keysight.ads.de.app](../../app/index.md)
      * [Actions and Menus](../../app/action.md)
      * [Addons](../../app/addon.md)
      * [Callbacks](../../app/callbacks.md)
      * [Windows and Widgets](../../app/window.md)
    - [keysight.ads.de.db](../../db/index.md)
      * [Callbacks](../../db/callbacks.md)
      * [Enumerated Types](../../db/enums.md)
      * [Parameter Forms](../../db/forms.md)
      * [GenPolyline](../../db/genpolyline.md)
      * [Model Definition](../../db/model_def.md)
      * [Parameters](../../db/parameters.md)
      * [Properties](../../db/properties.md)
      * [Transaction](../../db/transaction.md)
    - [keysight.ads.de.db\_dbu](../../db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../../db_uu/index.md)
      * [Design Elements](../../db_uu/db_uu.md)
      * [LayerId](../../db_uu/layer_id.md)
      * [LineTypeInfo](../../db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../../experimental/index.md)
      * [CDF](../../experimental/cdf/index.md)
      * [Commands](../../experimental/commands.md)
      * [Handles](../../experimental/handles.md)
      * [Netlist Utilities](../../experimental/netlist_helper.md)
      * [Polygon Utilities](../../experimental/polygon_utils.md)
      * [Preferences](../../experimental/preferences.md)
      * [xxPro View](../../experimental/pro_view.md)
      * [Symbol Generator](../../experimental/symbol.md)
      * [Text Maker](../../experimental/text_maker.md)
    - [keysight.ads.de.tech](../index.md)
      * [Tech](../tech.md)
      * [Padstacks](../pads/pads.md)
      * [Via Rules](../rule/rule.md)
      * Nested Technology
    - [keysight.ads.de.app.dds](../../app/dds.md)
  + [Examples](../../../../examples/index.md)
    - [Calling Between AEL and Python](../../../../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../../../examples/ex_create_layout.md)
    - [Create Schematic](../../../../examples/ex_create_schematic.md)
    - [Create Workspace](../../../../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../../../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../../../examples/ex_cdf.md)
    - [Component Parameters](../../../../examples/ex_parameters.md)
    - [Creating an Item Definition](../../../../examples/ex_itemdef.md)
    - [Model Definition Properties](../../../../examples/ex_model.md)
    - [Adding Instances to a Design](../../../../examples/ex_lpf.md)
    - [Properties](../../../../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../../../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../../../examples/ex_padstack.md)
    - [Nested Technology](../../../../examples/ex_nested.md)
    - [Rules](../../../../examples/ex_rules.md)
    - [Placing Text](../../../../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../../../examples/ex_polygon.md)
    - [PySide2](../../../../examples/ex_pyside.md)
    - [Traversing Hierarchy](../../../../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../../../examples/ex_working_with_var.md)
    - [XML RPC](../../../../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../../../examples/ex_translate_gds.md)
* [Technology](../../../../../../pysubst/docs/index.md)
  + [Reference](../../../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Nested Technology[](#module-keysight.ads.de.tech.nested "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.tech.nested.LayerMap[](#keysight.ads.de.tech.nested.LayerMap "Link to this definition")
:   LayerMap is a mapping of selected layers in a nested library to layers on the parent library.

    The nested library is assumed to have a different technology than the parent library.
    One or more layers from the nested library can be mapped to equivalent layers in the parent library.

    \_\_init\_\_(*name: str*, *nested\_lib: str | [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de.Library")*, *parent\_lib: str | [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de.Library")*) → None[](#keysight.ads.de.tech.nested.LayerMap.__init__ "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.tech.nested.LayerMap.name "Link to this definition")
    :   The name of the layer mapping. Used on nested substrate items.

    *property* nested\_library\_name*: str*[](#keysight.ads.de.tech.nested.LayerMap.nested_library_name "Link to this definition")

    *property* layer\_map\_library\_name*: str*[](#keysight.ads.de.tech.nested.LayerMap.layer_map_library_name "Link to this definition")
    :   The name of the layer mapped library. Usually the parent library name.

    *property* is\_above*: bool*[](#keysight.ads.de.tech.nested.LayerMap.is_above "Link to this definition")
    :   Are the nested layers above the layers on the parent.

    *property* is\_flipped*: bool*[](#keysight.ads.de.tech.nested.LayerMap.is_flipped "Link to this definition")
    :   Are the nested layers flipped.

    *property* nested\_mapped\_layers*: ListRefAbc[str]*[](#keysight.ads.de.tech.nested.LayerMap.nested_mapped_layers "Link to this definition")
    :   Return the collection of nested mapped layer names in this LayerMap.

        These are the source layers from the nested library that are mapped.

    *property* parent\_mapped\_layers*: ListRefAbc[str]*[](#keysight.ads.de.tech.nested.LayerMap.parent_mapped_layers "Link to this definition")
    :   Return the collection of parent mapped layer names in this LayerMap.

        These are the mapped layers in the parent library.

    map\_nested\_layer(*nested\_layer\_name: str*) → None[](#keysight.ads.de.tech.nested.LayerMap.map_nested_layer "Link to this definition")
    :   Add a mapping between the nested layer and a layer in the parent.

        Note: This does not add the layers to the parent technology.

    unmap\_nested\_layer(*nested\_layer\_name: str*) → None[](#keysight.ads.de.tech.nested.LayerMap.unmap_nested_layer "Link to this definition")
    :   Remove the mapping between for the nested layer.

## Functions[](#functions "Link to this heading")

keysight.ads.de.tech.nested.find\_layer\_map(*libName: str*, *name: str*) → [LayerMap](#keysight.ads.de.tech.nested.LayerMap "keysight.ads.de.tech.nested.LayerMap") | None[](#keysight.ads.de.tech.nested.find_layer_map "Link to this definition")

On this page

[Previous

Via Rules](../rule/rule.md)
[Next

keysight.ads.de.app.dds](../../app/dds.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top