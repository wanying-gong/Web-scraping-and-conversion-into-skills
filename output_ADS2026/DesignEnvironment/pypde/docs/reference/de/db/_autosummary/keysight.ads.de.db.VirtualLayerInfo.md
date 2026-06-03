<!-- 来源: pypde\docs\reference\de\db\_autosummary\keysight.ads.de.db.VirtualLayerInfo.html -->

[![Logo](../../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../../index.md)
* [Reference](../../../../../../reference.md)
* [Design Environment](../../../index.md)
* [keysight.ads.de.db](../index.md)
* [Smart Mount](../smart_mount.md)
* VirtualLayerInfo

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

* [Introduction](../../../../../../pydocs/intro/index.md)
* [How-To](../../../../../../pydocs/howto/index.md)
  + [Use Python in the ADS Application](../../../../../../pydocs/howto/embedded.md)
  + [Set Up a Python Virtual Environment](../../../../../../pydocs/howto/venv.md)
  + [Set Up Visual Studio Code for Development](../../../../../../pydocs/howto/vscode.md)
  + [Use Pytest](../../../../../../pydocs/howto/pytest.md)
  + [Enable Python Support For Your Library](../../../../../../pydocs/howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../../../../../../pydocs/howto/execution.md)
  + [Export Workspace and Design Objects to Python](../../../../../../pydocs/howto/exporter.md)
  + [Record Actions in ADS as Python Code](../../../../../../pydocs/howto/recorder.md)
  + [Develop a Python Pcell in ADS](../../../../../../pydocs/howto/pcell.md)
* [ADS Concepts](../../../../../../pydocs/concepts/index.md)
  + [Workspace Elements](../../../../../../pydocs/concepts/workspace_elements.md)
  + [Connectivity Objects](../../../../../../pydocs/concepts/connectivity.md)
* [Reference](../../../../../../reference.md)
  + [Deprecated APIs](../../../../../../pydocs/py/_generated/deprecations.md)
  + [Design Environment](../../../index.md)
    - [keysight.ads.de](../../index.md)
      * [ADS Application Environment](../../ads_environment.md)
      * [ADS Workspace Components](../../workspace_components.md)
      * [Design Hierarchy](../../design_hierarchy.md)
      * [Smart Package](../../package.md)
      * [Geometry](../../geometry.md)
      * [Collections](../../collections.md)
      * [Printer](../../printer.md)
    - [keysight.ads.de.ael](../../ael.md)
    - [keysight.ads.de.app](../../app/index.md)
      * [Application](../../app/application.md)
      * [Actions and Menus](../../app/action.md)
      * [Addons](../../app/addon.md)
      * [Window and Design Callbacks](../../app/callbacks.md)
      * [Windows and Widgets](../../app/window.md)
      * [Experimental](../../app/experimental.md)
    - [keysight.ads.de.app.dds](../../app/dds.md)
      * [exec\_python](../../app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../index.md)
      * [Models, Parameters, and Forms](../parameters.md)
      * [Properties](../properties.md)
      * [Preferences](../preferences.md)
      * [Transaction](../transaction.md)
      * [Smart Mount](../smart_mount.md)
      * [Geometry](../geometry.md)
      * [Teardrops](../teardrops.md)
    - [keysight.ads.de.db\_dbu](../../db_dbu/index.md)
      * [DbBox](../../db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../db_uu/index.md)
      * [Database Objects](../../db_uu/database_objects.md)
      * [Iterators](../../db_uu/iterators.md)
      * [Designs](../../db_uu/design.md)
      * [Teardrops](../../db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../../experimental/index.md)
      * [CDF](../../experimental/cdf.md)
      * [Design Commands](../../experimental/commands.md)
      * [Component Handles](../../experimental/handles.md)
      * [Netlist Utilities](../../experimental/netlist_helper.md)
      * [Polygon Utilities](../../experimental/polygon_utils.md)
      * [xxPro View](../../experimental/pro_view.md)
      * [Symbol Generator](../../experimental/symbol.md)
      * [Text Maker](../../experimental/text_maker.md)
      * [Notebook](../../experimental/notebook.md)
      * [Layer/Purpose Pairs](../../experimental/lpp.md)
    - [keysight.ads.de.tech](../../tech/index.md)
      * [Technology](../../tech/tech.md)
      * [Layers](../../tech/layers.md)
      * [Line Items](../../tech/line_items.md)
      * [Padstacks](../../tech/pads.md)
      * [Rules](../../tech/rule.md)
  + [Substrate](../../../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../../../../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../../../../../examples.md)
  + [Design Environment](../../../../examples/index.md)
    - [Workspace Creation](../../../../examples/workspace/ex_workspace.md)
    - [Design Creation](../../../../examples/design_creation/index.md)
      * [Create Layout](../../../../examples/design_creation/ex_create_layout.md)
      * [Create Schematic](../../../../examples/design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../../../../examples/design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../../../../examples/design_elements/index.md)
      * [Placing Text](../../../../examples/design_elements/ex_place_text.md)
      * [Moving Objects](../../../../examples/design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../../../../examples/design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../../../../examples/design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../../../../examples/design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../../../../examples/design_elements/ex_plane_editing.md)
    - [Parameters](../../../../examples/parameters/index.md)
      * [Interoperable Component Parameters](../../../../examples/parameters/ex_cdf.md)
      * [Working with VAR](../../../../examples/parameters/ex_working_with_var.md)
      * [Component Parameters](../../../../examples/parameters/ex_parameters.md)
      * [Creating an Item Definition](../../../../examples/parameters/ex_itemdef.md)
      * [Model Definition Properties](../../../../examples/parameters/ex_model.md)
      * [Creating a Text Form](../../../../examples/parameters/ex_text_form.md)
      * [Properties](../../../../examples/parameters/ex_properties.md)
    - [Technology](../../../../examples/technology/index.md)
      * [Padstacks and Vias](../../../../examples/technology/ex_padstack.md)
      * [Nested Technology](../../../../examples/technology/ex_nested.md)
      * [Rules](../../../../examples/technology/ex_rules.md)
    - [Translators](../../../../examples/translators/index.md)
      * [DXF Import and Export](../../../../examples/translators/ex_translate_dxf.md)
      * [Gerber Export](../../../../examples/translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../../../../examples/translators/ex_translate_gds.md)
    - [UI](../../../../examples/ui/index.md)
      * [Creating Custom Menus Using an Addon](../../../../examples/ui/ex_menu_addon.md)
      * [PySide](../../../../examples/ui/ex_pyside.md)
    - [Utility](../../../../examples/utility/index.md)
      * [Calling Between AEL and Python](../../../../examples/utility/ex_calling_ael_and_python.md)
      * [Smart Package](../../../../examples/utility/ex_smart_pkg.md)
      * [XML RPC](../../../../examples/utility/ex_xml_rpc.md)
  + [Substrate](../../../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../../../../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../../../../../genindex.md)

# VirtualLayerInfo[](#virtuallayerinfo "Link to this heading")

*class* VirtualLayerInfo[](#keysight.ads.de.db.VirtualLayerInfo "Link to this definition")
:   Bases: `object`

    The virtual layer information for a layer in a multi-chip mounting.

    Methods

    |  |  |
    | --- | --- |
    | [`find_virtual_layer`](#keysight.ads.de.db.VirtualLayerInfo.find_virtual_layer "keysight.ads.de.db.VirtualLayerInfo.find_virtual_layer")(lib, virtual\_layer) | Find the virtual layer information for the specified virtual layer number. |

    Attributes

    |  |  |
    | --- | --- |
    | [`alignment_adjustment`](#keysight.ads.de.db.VirtualLayerInfo.alignment_adjustment "keysight.ads.de.db.VirtualLayerInfo.alignment_adjustment") | The custom alignment adjustment value in meters. |
    | [`chip_alignment`](#keysight.ads.de.db.VirtualLayerInfo.chip_alignment "keysight.ads.de.db.VirtualLayerInfo.chip_alignment") | The alignment information for the chip layer in this mounting. |
    | [`chip_layer`](#keysight.ads.de.db.VirtualLayerInfo.chip_layer "keysight.ads.de.db.VirtualLayerInfo.chip_layer") | The layer number on the chip that is mapped to this virtual layer. |
    | [`chip_library`](#keysight.ads.de.db.VirtualLayerInfo.chip_library "keysight.ads.de.db.VirtualLayerInfo.chip_library") | The library containing the chip design mounted on this virtual layer. |
    | [`is_flipped`](#keysight.ads.de.db.VirtualLayerInfo.is_flipped "keysight.ads.de.db.VirtualLayerInfo.is_flipped") | True if the chip is flipped in this mounting. |
    | [`mount_alignment`](#keysight.ads.de.db.VirtualLayerInfo.mount_alignment "keysight.ads.de.db.VirtualLayerInfo.mount_alignment") | The alignment information for the module layer in this mounting. |
    | [`sm_instance_z_offset`](#keysight.ads.de.db.VirtualLayerInfo.sm_instance_z_offset "keysight.ads.de.db.VirtualLayerInfo.sm_instance_z_offset") | The z-offset of the SmartMount instance in meters. |
    | [`virtual_layer`](#keysight.ads.de.db.VirtualLayerInfo.virtual_layer "keysight.ads.de.db.VirtualLayerInfo.virtual_layer") | The number of this virtual layer on the module side of the mounting. |

    Inherited Methods

    |  |  |
    | --- | --- |
    | `__init__`() |  |

    *property* chip\_library*: [Library](../../_autosummary/keysight.ads.de.Library.md#keysight.ads.de.Library "keysight.ads.de.Library")*[](#keysight.ads.de.db.VirtualLayerInfo.chip_library "Link to this definition")
    :   The library containing the chip design mounted on this virtual layer.

    *property* virtual\_layer*: int*[](#keysight.ads.de.db.VirtualLayerInfo.virtual_layer "Link to this definition")
    :   The number of this virtual layer on the module side of the mounting.

    *property* chip\_layer*: int*[](#keysight.ads.de.db.VirtualLayerInfo.chip_layer "Link to this definition")
    :   The layer number on the chip that is mapped to this virtual layer.

    *property* is\_flipped*: bool*[](#keysight.ads.de.db.VirtualLayerInfo.is_flipped "Link to this definition")
    :   True if the chip is flipped in this mounting.

    *property* mount\_alignment*: [LayerAlignmentInfo](keysight.ads.de.db.LayerAlignmentInfo.md#keysight.ads.de.db.LayerAlignmentInfo "keysight.ads.de.db._layer.LayerAlignmentInfo")*[](#keysight.ads.de.db.VirtualLayerInfo.mount_alignment "Link to this definition")
    :   The alignment information for the module layer in this mounting.

    *property* chip\_alignment*: [LayerAlignmentInfo](keysight.ads.de.db.LayerAlignmentInfo.md#keysight.ads.de.db.LayerAlignmentInfo "keysight.ads.de.db._layer.LayerAlignmentInfo")*[](#keysight.ads.de.db.VirtualLayerInfo.chip_alignment "Link to this definition")
    :   The alignment information for the chip layer in this mounting.

    *property* alignment\_adjustment*: float*[](#keysight.ads.de.db.VirtualLayerInfo.alignment_adjustment "Link to this definition")
    :   The custom alignment adjustment value in meters.

    *property* sm\_instance\_z\_offset*: float*[](#keysight.ads.de.db.VirtualLayerInfo.sm_instance_z_offset "Link to this definition")
    :   The z-offset of the SmartMount instance in meters.

    *static* find\_virtual\_layer(*lib: [Library](../../_autosummary/keysight.ads.de.Library.md#keysight.ads.de.Library "keysight.ads.de.Library")*, *virtual\_layer: int*) → [VirtualLayerInfo](#keysight.ads.de.db.VirtualLayerInfo "keysight.ads.de.db.VirtualLayerInfo") | None[](#keysight.ads.de.db.VirtualLayerInfo.find_virtual_layer "Link to this definition")
    :   Find the virtual layer information for the specified virtual layer number.

        library:
        :   The library of the top design containing the multi-tech instance.

        virtual\_layer:
        :   The virtual layer number to find.
            These numbers are generated by ADS when a multi-chip mounting is created.

        Returns None if the given layer is not virtual or if the virtual layer does not exist.

On this page

[Previous

SmartMountPCellDesignInfo](keysight.ads.de.db.SmartMountPCellDesignInfo.md)
[Next

AlignmentType](keysight.ads.de._pde.db.AlignmentType.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top