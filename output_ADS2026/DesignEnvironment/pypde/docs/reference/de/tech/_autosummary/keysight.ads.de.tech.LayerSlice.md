<!-- 来源: pypde\docs\reference\de\tech\_autosummary\keysight.ads.de.tech.LayerSlice.html -->

[![Logo](../../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../../index.md)
* [Reference](../../../../../../reference.md)
* [Design Environment](../../../index.md)
* [keysight.ads.de.tech](../index.md)
* [Layers](../layers.md)
* LayerSlice

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
    - [keysight.ads.de.db](../../db/index.md)
      * [Models, Parameters, and Forms](../../db/parameters.md)
      * [Properties](../../db/properties.md)
      * [Preferences](../../db/preferences.md)
      * [Transaction](../../db/transaction.md)
      * [Smart Mount](../../db/smart_mount.md)
      * [Geometry](../../db/geometry.md)
      * [Teardrops](../../db/teardrops.md)
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
    - [keysight.ads.de.tech](../index.md)
      * [Technology](../tech.md)
      * [Layers](../layers.md)
      * [Line Items](../line_items.md)
      * [Padstacks](../pads.md)
      * [Rules](../rule.md)
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

# LayerSlice[](#layerslice "Link to this heading")

*class* LayerSlice[](#keysight.ads.de.tech.LayerSlice "Link to this definition")
:   Bases: `object`

    Represents a single slice of a LineStrip.

    Identifies the layer for this slice and its enclosure.

    Methods

    |  |  |
    | --- | --- |
    | [`__init__`](#keysight.ads.de.tech.LayerSlice.__init__ "keysight.ads.de.tech.LayerSlice.__init__")() |  |
    | [`create_from_layer_id`](#keysight.ads.de.tech.LayerSlice.create_from_layer_id "keysight.ads.de.tech.LayerSlice.create_from_layer_id")(library, layer\_id, ...) |  |
    | [`create_from_names`](#keysight.ads.de.tech.LayerSlice.create_from_names "keysight.ads.de.tech.LayerSlice.create_from_names")(library, layer\_name, ...) |  |
    | [`validate_names_and_id`](#keysight.ads.de.tech.LayerSlice.validate_names_and_id "keysight.ads.de.tech.LayerSlice.validate_names_and_id")(library) | Check that the layer\_id matches the layer and purpose names. |

    Attributes

    |  |  |
    | --- | --- |
    | [`enclosure_width_uu`](#keysight.ads.de.tech.LayerSlice.enclosure_width_uu "keysight.ads.de.tech.LayerSlice.enclosure_width_uu") | Return the difference in width (in user units) between this slice and the default width of the strip. |
    | [`layer_id`](#keysight.ads.de.tech.LayerSlice.layer_id "keysight.ads.de.tech.LayerSlice.layer_id") |  |
    | [`layer_name`](#keysight.ads.de.tech.LayerSlice.layer_name "keysight.ads.de.tech.LayerSlice.layer_name") |  |
    | [`purpose_name`](#keysight.ads.de.tech.LayerSlice.purpose_name "keysight.ads.de.tech.LayerSlice.purpose_name") |  |

    \_\_init\_\_() → None[](#keysight.ads.de.tech.LayerSlice.__init__ "Link to this definition")

    \_\_init\_\_(*library: [Library](../../_autosummary/keysight.ads.de.Library.md#keysight.ads.de.Library "keysight.ads.de.Library")*, *layer: str | [LayerId](../../db_uu/_autosummary/keysight.ads.de.db_uu.LayerId.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *enclosure\_width\_uu: float | None = None*) → None

    *classmethod* create\_from\_names(*library: [Library](../../_autosummary/keysight.ads.de.Library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *layer\_name: str*, *purpose\_name: str*, *enclosure\_width: float*) → [LayerSlice](#keysight.ads.de.tech.LayerSlice "keysight.ads.de.tech._tech.LayerSlice")[](#keysight.ads.de.tech.LayerSlice.create_from_names "Link to this definition")

    *classmethod* create\_from\_layer\_id(*library: [Library](../../_autosummary/keysight.ads.de.Library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *layer\_id: [LayerId](../../db_uu/_autosummary/keysight.ads.de.db_uu.LayerId.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *enclosure\_width: float*) → [LayerSlice](#keysight.ads.de.tech.LayerSlice "keysight.ads.de.tech._tech.LayerSlice")[](#keysight.ads.de.tech.LayerSlice.create_from_layer_id "Link to this definition")

    *property* layer\_id*: [LayerId](../../db_uu/_autosummary/keysight.ads.de.db_uu.LayerId.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*[](#keysight.ads.de.tech.LayerSlice.layer_id "Link to this definition")

    *property* layer\_name*: str*[](#keysight.ads.de.tech.LayerSlice.layer_name "Link to this definition")

    *property* purpose\_name*: str*[](#keysight.ads.de.tech.LayerSlice.purpose_name "Link to this definition")

    *property* enclosure\_width\_uu*: float*[](#keysight.ads.de.tech.LayerSlice.enclosure_width_uu "Link to this definition")
    :   Return the difference in width (in user units) between this slice and the default width of the strip.

    validate\_names\_and\_id(*library: [Library](../../_autosummary/keysight.ads.de.Library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*) → None[](#keysight.ads.de.tech.LayerSlice.validate_names_and_id "Link to this definition")
    :   Check that the layer\_id matches the layer and purpose names.

On this page

[Previous

Layer](keysight.ads.de.tech.Layer.md)
[Next

PhysicalLayer](keysight.ads.de.tech.PhysicalLayer.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top