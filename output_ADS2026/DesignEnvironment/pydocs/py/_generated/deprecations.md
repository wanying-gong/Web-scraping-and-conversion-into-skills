<!-- 来源: pydocs\py\_generated\deprecations.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Reference](../../../reference.md)
* Deprecated APIs

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

* [Introduction](../../intro/index.md)
* [How-To](../../howto/index.md)
  + [Use Python in the ADS Application](../../howto/embedded.md)
  + [Set Up a Python Virtual Environment](../../howto/venv.md)
  + [Set Up Visual Studio Code for Development](../../howto/vscode.md)
  + [Use Pytest](../../howto/pytest.md)
  + [Enable Python Support For Your Library](../../howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../../howto/execution.md)
  + [Export Workspace and Design Objects to Python](../../howto/exporter.md)
  + [Record Actions in ADS as Python Code](../../howto/recorder.md)
  + [Develop a Python Pcell in ADS](../../howto/pcell.md)
* [ADS Concepts](../../concepts/index.md)
  + [Workspace Elements](../../concepts/workspace_elements.md)
  + [Connectivity Objects](../../concepts/connectivity.md)
* [Reference](../../../reference.md)
  + Deprecated APIs
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
  + [Substrate](../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../../pysubst/docs/reference/subst/subst.md)
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
  + [Substrate](../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../../genindex.md)

# Deprecated APIs[](#deprecated-apis "Link to this heading")

The following API’s are deprecated and scheduled for removal in a future release. A deprecated API will be removed in a major release and is given an entire release cycle’s notice before removal. For example, an API initially marked as deprecated in ADS 2025 Update 1 or ADS 2026 will be scheduled for removal in ADS 2027. Removal primarily occurs only in major releases and not in update or patch releases.

## Deprecated APIs to be removed in ADS 2027[](#deprecated-apis-to-be-removed-in-ads-2027 "Link to this heading")

| API | Message |
| --- | --- |
| `keysight.ads.de._list_like._IndexedMutableCollection._append_sequence()` | Use extend(values). |
| `keysight.ads.de._list_like._IndexedMutableCollection._extend_single()` | Use extend([value]). |
| `keysight.ads.de._list_like._IndexedMutableCollection._insert_sequence()` | Use a loop and insert(value) or assign to a slice. |
| [`keysight.ads.de.app.window.main_pyside2_widget()`](../../../pypde/docs/reference/de/app/_autosummary/keysight.ads.de.app.window.main_pyside2_widget.md#keysight.ads.de.app.window.main_pyside2_widget "keysight.ads.de.app.window.main_pyside2_widget") | Use main\_pyside\_widget instead. |
| `keysight.ads.de.db._genpolyline.GenPolyline.teardrop_info()` | Use teardrops or teardrop\_touches. |
| `keysight.ads.de.db._genpolyline.GenPolyline.teardrop_info()` | Use teardrops or teardrop\_touches. |
| `keysight.ads.de.db._parameters.Param.evaluate_no_expr()` | Use evaluate\_without\_expr instead. |
| `keysight.ads.de.db._parameters.ParamBase.evaluate_no_expr()` | Use evaluate\_without\_expr instead. |
| `keysight.ads.de.db._parameters.ParamCompound.evaluate_no_expr()` | Use evaluate\_without\_expr instead. |
| `keysight.ads.de.db._parameters.ParamItem.form_name()` | Replace the ParamItem instead. |
| `keysight.ads.de.db._parameters.ParamNonRepeated.evaluate_no_expr()` | Use evaluate\_without\_expr instead. |
| `keysight.ads.de.db._parameters.ParamRepeated.append_repeat()` | Use: repeat = repeats.clone(value); repeat.value = value. |
| `keysight.ads.de.db._parameters.ParamRepeated.evaluate_no_expr()` | Use evaluate\_without\_expr instead. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.__init__()` | Use GenPolyline.teardrops or GenPolyline.teardrop\_touches. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.definition()` | Use GenPolyline.teardrops. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.has_teardrops()` | Use GenPolyline.teardrop\_touches. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.set_definition()` | Use GenPolyline.teardrops. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.set_touching()` | Use GenPolyline.teardrop\_touches. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.touch()` | Use GenPolyline.teardrop\_touches. |
| `keysight.ads.de.db_dbu._db_x.InstPin.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_dbu._db_x.InstTerm.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_dbu._db_x.Pin.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_dbu._line_type_info.LineTypeInfo.teardrop_definition_back()` | Use teardrop\_back |
| `keysight.ads.de.db_dbu._line_type_info.LineTypeInfo.teardrop_definition_back()` | Use teardrop\_back |
| `keysight.ads.de.db_dbu._line_type_info.LineTypeInfo.teardrop_definition_front()` | Use teardrop\_front |
| `keysight.ads.de.db_dbu._line_type_info.LineTypeInfo.teardrop_definition_front()` | Use teardrop\_front |
| `keysight.ads.de.db_uu._db_x.InstPin.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_uu._db_x.InstTerm.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_uu._db_x.Pin.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_uu._line_type_info.LineTypeInfo.teardrop_definition_back()` | Use teardrop\_back |
| `keysight.ads.de.db_uu._line_type_info.LineTypeInfo.teardrop_definition_back()` | Use teardrop\_back |
| `keysight.ads.de.db_uu._line_type_info.LineTypeInfo.teardrop_definition_front()` | Use teardrop\_front |
| `keysight.ads.de.db_uu._line_type_info.LineTypeInfo.teardrop_definition_front()` | Use teardrop\_front |
| `keysight.ads.de.experimental.preferences._Design_get_preference()` | Use the preferences property instead. |
| `keysight.ads.de.experimental.preferences._Design_set_preference()` | Use the preferences property instead. |
| `keysight.ads.de.experimental.preferences._Library_get_layout_preference()` | Use the layout\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Library_get_schematic_preference()` | Use the schematic\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Library_set_layout_preference()` | Use the layout\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Library_set_schematic_preference()` | Use the schematic\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Workspace_get_layout_preference()` | Use the layout\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Workspace_get_schematic_preference()` | Use the schematic\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Workspace_set_layout_preference()` | Use the layout\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Workspace_set_schematic_preference()` | Use the schematic\_preferences property instead. |
| [`keysight.ads.de.tech._tech.LineBeginEndTypes`](../../../pypde/docs/reference/de/tech/_autosummary/keysight.ads.de.tech.LineBeginEndTypes.md#keysight.ads.de.tech.LineBeginEndTypes "keysight.ads.de.tech._tech.LineBeginEndTypes") | Use LineEndType |
| [`keysight.ads.de.tech._tech.LineCornerTypes`](../../../pypde/docs/reference/de/tech/_autosummary/keysight.ads.de.tech.LineCornerTypes.md#keysight.ads.de.tech.LineCornerTypes "keysight.ads.de.tech._tech.LineCornerTypes") | Use LineCornerType |
| [`keysight.ads.de.tech._tech.LineStripSpacingTypes`](../../../pypde/docs/reference/de/tech/_autosummary/keysight.ads.de.tech.LineStripSpacingTypes.md#keysight.ads.de.tech.LineStripSpacingTypes "keysight.ads.de.tech._tech.LineStripSpacingTypes") | Use LineStripSpacingType |

## Deprecated APIs to be removed in ADS 2028[](#deprecated-apis-to-be-removed-in-ads-2028 "Link to this heading")

| API | Message |
| --- | --- |
| `keysight.ads.de.db._layer_id.LayerId.create_layer_id_from_library()` | Use ‘from\_name’ instead. |
| `keysight.ads.de.db._layer_id.LayerId.create_layer_id_from_library_name()` | Use ‘from\_name’ instead. |
| `keysight.ads.de.db_dbu._db_x.ApolloObject.is_part_of_composite_object()` | Use is\_child\_of\_composite\_object. |
| `keysight.ads.de.db_dbu._design.PCellInfo.function()` | Use ael\_function or python\_function. |
| `keysight.ads.de.db_dbu._design.PCellInfo.function()` | Use ael\_function or python\_function. |
| `keysight.ads.de.db_uu._db_x.ApolloObject.is_part_of_composite_object()` | Use is\_child\_of\_composite\_object. |
| `keysight.ads.de.db_uu._design.PCellInfo.function()` | Use ael\_function or python\_function. |
| `keysight.ads.de.db_uu._design.PCellInfo.function()` | Use ael\_function or python\_function. |

On this page

[Previous

Reference](../../../reference.md)
[Next

Design Environment](../../../pypde/docs/reference/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top