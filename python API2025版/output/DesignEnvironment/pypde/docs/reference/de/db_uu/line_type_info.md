<!-- 来源: pypde\docs\reference\de\db_uu\line_type_info.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.db\_uu](index.md)
* LineTypeInfo

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

* [Introduction](../../../../../pydocs/intro/index.md)
  + [Licensing](../../../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../../../pydocs/intro/extension.md)
* [Concepts](../../../../../pydocs/concepts/index.md)
  + [Terminology](../../../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../../../pydocs/concepts/execution.md)
* [How-To](../../../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../../../pydocs/howto/pytest.md)

* [Design](../../../index.md)
  + [Reference](../../index.md)
    - [keysight.ads.de](../index.md)
      * [Workspace](../workspace.md)
      * [Library](../library.md)
      * [Cell](../cell.md)
      * [View](../view.md)
      * [CellviewRef](../cellviewref.md)
      * [DesignHierarchy](../design_hierarchy.md)
      * [DMData](../dmdata.md)
      * [ItemInfo](../item_info.md)
      * [Points](../points.md)
      * [Collections](../collections.md)
    - [keysight.ads.de.ael](../ael.md)
    - [keysight.ads.de.app](../app/index.md)
      * [Actions and Menus](../app/action.md)
      * [Addons](../app/addon.md)
      * [Callbacks](../app/callbacks.md)
      * [Windows and Widgets](../app/window.md)
    - [keysight.ads.de.db](../db/index.md)
      * [Callbacks](../db/callbacks.md)
      * [Enumerated Types](../db/enums.md)
      * [Parameter Forms](../db/forms.md)
      * [GenPolyline](../db/genpolyline.md)
      * [Model Definition](../db/model_def.md)
      * [Parameters](../db/parameters.md)
      * [Properties](../db/properties.md)
      * [Transaction](../db/transaction.md)
    - [keysight.ads.de.db\_dbu](../db_dbu/index.md)
    - [keysight.ads.de.db\_uu](index.md)
      * [Design Elements](db_uu.md)
      * [LayerId](layer_id.md)
      * LineTypeInfo
    - [keysight.ads.de.experimental](../experimental/index.md)
      * [CDF](../experimental/cdf/index.md)
      * [Commands](../experimental/commands.md)
      * [Handles](../experimental/handles.md)
      * [Netlist Utilities](../experimental/netlist_helper.md)
      * [Polygon Utilities](../experimental/polygon_utils.md)
      * [Preferences](../experimental/preferences.md)
      * [xxPro View](../experimental/pro_view.md)
      * [Symbol Generator](../experimental/symbol.md)
      * [Text Maker](../experimental/text_maker.md)
    - [keysight.ads.de.tech](../tech/index.md)
      * [Tech](../tech/tech.md)
      * [Padstacks](../tech/pads/pads.md)
      * [Via Rules](../tech/rule/rule.md)
      * [Nested Technology](../tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../app/dds.md)
  + [Examples](../../../examples/index.md)
    - [Calling Between AEL and Python](../../../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../../examples/ex_create_layout.md)
    - [Create Schematic](../../../examples/ex_create_schematic.md)
    - [Create Workspace](../../../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../../examples/ex_cdf.md)
    - [Component Parameters](../../../examples/ex_parameters.md)
    - [Creating an Item Definition](../../../examples/ex_itemdef.md)
    - [Model Definition Properties](../../../examples/ex_model.md)
    - [Adding Instances to a Design](../../../examples/ex_lpf.md)
    - [Properties](../../../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../../examples/ex_padstack.md)
    - [Nested Technology](../../../examples/ex_nested.md)
    - [Rules](../../../examples/ex_rules.md)
    - [Placing Text](../../../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../../examples/ex_polygon.md)
    - [PySide2](../../../examples/ex_pyside.md)
    - [Traversing Hierarchy](../../../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../../examples/ex_working_with_var.md)
    - [XML RPC](../../../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../../examples/ex_translate_gds.md)
* [Technology](../../../../../pysubst/docs/index.md)
  + [Reference](../../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# LineTypeInfo[](#linetypeinfo "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db\_uu.LineTypeInfo[](#keysight.ads.de.db_uu.LineTypeInfo "Link to this definition")
:   Holds the information required to create an advanced Trace or Interconnect.

    It may also hold the information that describes existing traces or interconnect.

    \_\_init\_\_(*library: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de.Library")*, *line\_item\_name: str | None = None*, *width: float | None = None*) → None[](#keysight.ads.de.db_uu.LineTypeInfo.__init__ "Link to this definition")
    :   Create a new LineTypeInfo object.

        LineTypeInfo(library):
        :   Creates an empty LineTypeInfo.

        LineTypeInfo(library, line\_item\_name, width):
        :   Creates a LineTypeInfo using the LineItem found in the library.

    *property* corner\_type*: [LineCornerType](../tech/tech.md#keysight.ads.de.tech.LineCornerType "keysight.ads.de._pde.tech.LineCornerType")*[](#keysight.ads.de.db_uu.LineTypeInfo.corner_type "Link to this definition")

    *property* end\_style*: [LineEndType](../tech/tech.md#keysight.ads.de.tech.LineEndType "keysight.ads.de._pde.tech.LineEndType")*[](#keysight.ads.de.db_uu.LineTypeInfo.end_style "Link to this definition")

    *property* layer\_id*: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*[](#keysight.ads.de.db_uu.LineTypeInfo.layer_id "Link to this definition")
    :   The LayerId used by this LineTypeInfo.

        If line\_item is set, the layer\_id is ignored.
        Setting the layer\_id will clear the LineItem.

    *property* line\_item*: [LineItem](../tech/tech.md#keysight.ads.de.tech.LineItem "keysight.ads.de.tech._tech.LineItem") | None*[](#keysight.ads.de.db_uu.LineTypeInfo.line_item "Link to this definition")
    :   The LineItem (from the technology) used by this LineTypeInfo.

        If line\_item is not None, the layer\_id is ignored.
        Setting the layer\_id will clear the LineItem.

    *property* miter\_or\_radius*: float*[](#keysight.ads.de.db_uu.LineTypeInfo.miter_or_radius "Link to this definition")

    *property* miter\_or\_radius\_db*: int*[](#keysight.ads.de.db_uu.LineTypeInfo.miter_or_radius_db "Link to this definition")

    *property* teardrop\_definition\_back*: [TeardropDefinition](../db/genpolyline.md#keysight.ads.de.db.TeardropDefinition "keysight.ads.de.db._teardrop.TeardropDefinition")*[](#keysight.ads.de.db_uu.LineTypeInfo.teardrop_definition_back "Link to this definition")
    :   Returns a copy of the back teardrop definition.

    *property* teardrop\_definition\_front*: [TeardropDefinition](../db/genpolyline.md#keysight.ads.de.db.TeardropDefinition "keysight.ads.de.db._teardrop.TeardropDefinition")*[](#keysight.ads.de.db_uu.LineTypeInfo.teardrop_definition_front "Link to this definition")
    :   Returns a copy of the front teardrop definition.

    *property* width*: float*[](#keysight.ads.de.db_uu.LineTypeInfo.width "Link to this definition")

    *property* width\_db*: int*[](#keysight.ads.de.db_uu.LineTypeInfo.width_db "Link to this definition")

On this page

[Previous

LayerId](layer_id.md)
[Next

keysight.ads.de.experimental](../experimental/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top