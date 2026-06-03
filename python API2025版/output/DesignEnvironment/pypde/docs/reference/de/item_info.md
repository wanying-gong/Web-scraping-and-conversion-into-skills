<!-- 来源: pypde\docs\reference\de\item_info.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Design](../../index.md)
* [Reference](../index.md)
* [keysight.ads.de](index.md)
* ItemInfo

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

* [Introduction](../../../../pydocs/intro/index.md)
  + [Licensing](../../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../../pydocs/intro/extension.md)
* [Concepts](../../../../pydocs/concepts/index.md)
  + [Terminology](../../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../../pydocs/concepts/execution.md)
* [How-To](../../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../../pydocs/howto/pytest.md)

* [Design](../../index.md)
  + [Reference](../index.md)
    - [keysight.ads.de](index.md)
      * [Workspace](workspace.md)
      * [Library](library.md)
      * [Cell](cell.md)
      * [View](view.md)
      * [CellviewRef](cellviewref.md)
      * [DesignHierarchy](design_hierarchy.md)
      * [DMData](dmdata.md)
      * ItemInfo
      * [Points](points.md)
      * [Collections](collections.md)
    - [keysight.ads.de.ael](ael.md)
    - [keysight.ads.de.app](app/index.md)
      * [Actions and Menus](app/action.md)
      * [Addons](app/addon.md)
      * [Callbacks](app/callbacks.md)
      * [Windows and Widgets](app/window.md)
    - [keysight.ads.de.db](db/index.md)
      * [Callbacks](db/callbacks.md)
      * [Enumerated Types](db/enums.md)
      * [Parameter Forms](db/forms.md)
      * [GenPolyline](db/genpolyline.md)
      * [Model Definition](db/model_def.md)
      * [Parameters](db/parameters.md)
      * [Properties](db/properties.md)
      * [Transaction](db/transaction.md)
    - [keysight.ads.de.db\_dbu](db_dbu/index.md)
    - [keysight.ads.de.db\_uu](db_uu/index.md)
      * [Design Elements](db_uu/db_uu.md)
      * [LayerId](db_uu/layer_id.md)
      * [LineTypeInfo](db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](experimental/index.md)
      * [CDF](experimental/cdf/index.md)
      * [Commands](experimental/commands.md)
      * [Handles](experimental/handles.md)
      * [Netlist Utilities](experimental/netlist_helper.md)
      * [Polygon Utilities](experimental/polygon_utils.md)
      * [Preferences](experimental/preferences.md)
      * [xxPro View](experimental/pro_view.md)
      * [Symbol Generator](experimental/symbol.md)
      * [Text Maker](experimental/text_maker.md)
    - [keysight.ads.de.tech](tech/index.md)
      * [Tech](tech/tech.md)
      * [Padstacks](tech/pads/pads.md)
      * [Via Rules](tech/rule/rule.md)
      * [Nested Technology](tech/nested/nested.md)
    - [keysight.ads.de.app.dds](app/dds.md)
  + [Examples](../../examples/index.md)
    - [Calling Between AEL and Python](../../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../examples/ex_create_layout.md)
    - [Create Schematic](../../examples/ex_create_schematic.md)
    - [Create Workspace](../../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../examples/ex_cdf.md)
    - [Component Parameters](../../examples/ex_parameters.md)
    - [Creating an Item Definition](../../examples/ex_itemdef.md)
    - [Model Definition Properties](../../examples/ex_model.md)
    - [Adding Instances to a Design](../../examples/ex_lpf.md)
    - [Properties](../../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../examples/ex_padstack.md)
    - [Nested Technology](../../examples/ex_nested.md)
    - [Rules](../../examples/ex_rules.md)
    - [Placing Text](../../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../examples/ex_polygon.md)
    - [PySide2](../../examples/ex_pyside.md)
    - [Traversing Hierarchy](../../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../examples/ex_working_with_var.md)
    - [XML RPC](../../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../examples/ex_translate_gds.md)
* [Technology](../../../../pysubst/docs/index.md)
  + [Reference](../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# ItemInfo[](#iteminfo "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.ItemInfo[](#keysight.ads.de.ItemInfo "Link to this definition")
:   \_\_init\_\_(*design: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*, *lcv\_name: [LCVName](cellviewref.md#keysight.ads.de.LCVName "keysight.ads.de.LCVName")*, *edit\_mode: [ItemEditMode](#keysight.ads.de.ItemEditMode "keysight.ads.de._core._item_info.ItemEditMode")*) → None[](#keysight.ads.de.ItemInfo.__init__ "Link to this definition")

    *property* cell\_name*: str*[](#keysight.ads.de.ItemInfo.cell_name "Link to this definition")

    create\_new\_instance(*location: [PointF](points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *auto\_connect: bool = False*) → [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")[](#keysight.ads.de.ItemInfo.create_new_instance "Link to this definition")

    *property* design\_name*: str*[](#keysight.ads.de.ItemInfo.design_name "Link to this definition")

    *property* display\_name*: str*[](#keysight.ads.de.ItemInfo.display_name "Link to this definition")

    *property* inst\_name*: str*[](#keysight.ads.de.ItemInfo.inst_name "Link to this definition")

    *property* instance*: [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance") | None*[](#keysight.ads.de.ItemInfo.instance "Link to this definition")

    *property* is\_scope\_global*: bool*[](#keysight.ads.de.ItemInfo.is_scope_global "Link to this definition")

    *property* is\_scope\_nested*: bool*[](#keysight.ads.de.ItemInfo.is_scope_nested "Link to this definition")

    *property* lib\_name*: str*[](#keysight.ads.de.ItemInfo.lib_name "Link to this definition")

    *property* model\_def*: [ModelDefBase](db/model_def.md#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db.ModelDefBase") | None*[](#keysight.ads.de.ItemInfo.model_def "Link to this definition")

    *property* owner\_design*: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*[](#keysight.ads.de.ItemInfo.owner_design "Link to this definition")

    set\_scope\_global() → None[](#keysight.ads.de.ItemInfo.set_scope_global "Link to this definition")

    set\_scope\_nested() → None[](#keysight.ads.de.ItemInfo.set_scope_nested "Link to this definition")

    setup\_instance\_for\_edit(*instance: [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*, *mod\_inst\_name\_pref: bool = False*) → None[](#keysight.ads.de.ItemInfo.setup_instance_for_edit "Link to this definition")

    *property* view\_name*: str*[](#keysight.ads.de.ItemInfo.view_name "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.ItemEditMode[](#keysight.ads.de.ItemEditMode "Link to this definition")
:   DIALOG *= <ItemEditMode.DIALOG: 0>*[](#keysight.ads.de.ItemEditMode.DIALOG "Link to this definition")

    NEW *= <ItemEditMode.NEW: 1>*[](#keysight.ads.de.ItemEditMode.NEW "Link to this definition")

    ON\_SCREEN *= <ItemEditMode.ON\_SCREEN: 2>*[](#keysight.ads.de.ItemEditMode.ON_SCREEN "Link to this definition")

    TEMP *= <ItemEditMode.TEMP: 3>*[](#keysight.ads.de.ItemEditMode.TEMP "Link to this definition")

On this page

[Previous

DMData](dmdata.md)
[Next

Points](points.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top