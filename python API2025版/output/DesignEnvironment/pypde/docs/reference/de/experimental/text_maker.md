<!-- 来源: pypde\docs\reference\de\experimental\text_maker.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.experimental](index.md)
* Text Maker

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
    - [keysight.ads.de.db\_uu](../db_uu/index.md)
      * [Design Elements](../db_uu/db_uu.md)
      * [LayerId](../db_uu/layer_id.md)
      * [LineTypeInfo](../db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](index.md)
      * [CDF](cdf/index.md)
      * [Commands](commands.md)
      * [Handles](handles.md)
      * [Netlist Utilities](netlist_helper.md)
      * [Polygon Utilities](polygon_utils.md)
      * [Preferences](preferences.md)
      * [xxPro View](pro_view.md)
      * [Symbol Generator](symbol.md)
      * Text Maker
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

# Text Maker[](#module-keysight.ads.de.experimental.text_maker "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.text\_maker.TextMaker[](#keysight.ads.de.experimental.text_maker.TextMaker "Link to this definition")
:   TFloatTuple[](#keysight.ads.de.experimental.text_maker.TextMaker.TFloatTuple "Link to this definition")
    :   alias of `tuple`[`float`, `float`]

    TUserPoint[](#keysight.ads.de.experimental.text_maker.TextMaker.TUserPoint "Link to this definition")
    :   alias of `Union`[[`PointUU`](../points.md#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU"), `tuple`[`float`, `float`]]

    \_\_init\_\_(*design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.experimental.text_maker.TextMaker.__init__ "Link to this definition")

    add\_attr\_display(*obj: [ApolloObject](../db_uu/db_uu.md#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject") | [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *attr\_type: [DesignAttrType](../db/enums.md#keysight.ads.de.db.DesignAttrType "keysight.ads.de.db._db_types.DesignAttrType") | [InstAttrType](../db/enums.md#keysight.ads.de.db.InstAttrType "keysight.ads.de.db._db_types.InstAttrType") | [InstTermAttrType](../db/enums.md#keysight.ads.de.db.InstTermAttrType "keysight.ads.de.db._db_types.InstTermAttrType") | [NetAttrType](../db/enums.md#keysight.ads.de.db.NetAttrType "keysight.ads.de.db._db_types.NetAttrType") | [TermAttrType](../db/enums.md#keysight.ads.de.db.TermAttrType "keysight.ads.de.db._db_types.TermAttrType")*, *layer\_id: [LayerId](../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *origin: [PointUU](../points.md#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU") | tuple[float, float]*, *display\_format: [TextDisplayFormat](../db/enums.md#keysight.ads.de.db.TextDisplayFormat "keysight.ads.de.db._db_types.TextDisplayFormat") = TextDisplayFormat.VALUE*) → [AttrDisplay](../db_uu/db_uu.md#keysight.ads.de.db_uu.AttrDisplay "keysight.ads.de.db_uu._db_x.AttrDisplay")[](#keysight.ads.de.experimental.text_maker.TextMaker.add_attr_display "Link to this definition")

    add\_inst\_attr\_display(*inst: [Instance](../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*, *master\_attribute: [DesignAttrType](../db/enums.md#keysight.ads.de.db.DesignAttrType "keysight.ads.de.db._db_types.DesignAttrType")*, *layer\_id: [LayerId](../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *origin: [PointUU](../points.md#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU") | tuple[float, float]*, *display\_format: [TextDisplayFormat](../db/enums.md#keysight.ads.de.db.TextDisplayFormat "keysight.ads.de.db._db_types.TextDisplayFormat") = TextDisplayFormat.VALUE*) → [InstAttrDisplay](../db_uu/db_uu.md#keysight.ads.de.db_uu.InstAttrDisplay "keysight.ads.de.db_uu._db_x.InstAttrDisplay")[](#keysight.ads.de.experimental.text_maker.TextMaker.add_inst_attr_display "Link to this definition")

    add\_text(*layer\_id: [LayerId](../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *text: str*, *origin: [PointUU](../points.md#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU") | tuple[float, float]*) → [Text](../db_uu/db_uu.md#keysight.ads.de.db_uu.Text "keysight.ads.de.db_uu._db_x.Text")[](#keysight.ads.de.experimental.text_maker.TextMaker.add_text "Link to this definition")

    *property* align*: [TextAlignment](../db/enums.md#keysight.ads.de.db.TextAlignment "keysight.ads.de.db._db_types.TextAlignment")*[](#keysight.ads.de.experimental.text_maker.TextMaker.align "Link to this definition")

    *property* font\_name*: str*[](#keysight.ads.de.experimental.text_maker.TextMaker.font_name "Link to this definition")

    *property* height*: float*[](#keysight.ads.de.experimental.text_maker.TextMaker.height "Link to this definition")

    *property* is\_drafting*: bool*[](#keysight.ads.de.experimental.text_maker.TextMaker.is_drafting "Link to this definition")

    *property* orient*: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*[](#keysight.ads.de.experimental.text_maker.TextMaker.orient "Link to this definition")

On this page

[Previous

Symbol Generator](symbol.md)
[Next

keysight.ads.de.tech](../tech/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top