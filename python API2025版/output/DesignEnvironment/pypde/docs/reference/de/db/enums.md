<!-- 来源: pypde\docs\reference\de\db\enums.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.db](index.md)
* Enumerated Types

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
    - [keysight.ads.de.db](index.md)
      * [Callbacks](callbacks.md)
      * Enumerated Types
      * [Parameter Forms](forms.md)
      * [GenPolyline](genpolyline.md)
      * [Model Definition](model_def.md)
      * [Parameters](parameters.md)
      * [Properties](properties.md)
      * [Transaction](transaction.md)
    - [keysight.ads.de.db\_dbu](../db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../db_uu/index.md)
      * [Design Elements](../db_uu/db_uu.md)
      * [LayerId](../db_uu/layer_id.md)
      * [LineTypeInfo](../db_uu/line_type_info.md)
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

# Enumerated Types[](#enumerated-types "Link to this heading")

keysight.ads.de.db.AttrType[](#keysight.ads.de.db.AttrType "Link to this definition")
:   alias of `Union`[[`DesignAttrType`](#keysight.ads.de.db.DesignAttrType "keysight.ads.de.db._db_types.DesignAttrType"), [`InstAttrType`](#keysight.ads.de.db.InstAttrType "keysight.ads.de.db._db_types.InstAttrType"), [`InstTermAttrType`](#keysight.ads.de.db.InstTermAttrType "keysight.ads.de.db._db_types.InstTermAttrType"), [`NetAttrType`](#keysight.ads.de.db.NetAttrType "keysight.ads.de.db._db_types.NetAttrType"), [`TermAttrType`](#keysight.ads.de.db.TermAttrType "keysight.ads.de.db._db_types.TermAttrType")]

*class* keysight.ads.de.db.DesignAttrType[](#keysight.ads.de.db.DesignAttrType "Link to this definition")
:   LIB\_NAME *= <DesignAttrType.LIB\_NAME: 0>*[](#keysight.ads.de.db.DesignAttrType.LIB_NAME "Link to this definition")

    CELL\_NAME *= <DesignAttrType.CELL\_NAME: 1>*[](#keysight.ads.de.db.DesignAttrType.CELL_NAME "Link to this definition")

    VIEW\_NAME *= <DesignAttrType.VIEW\_NAME: 2>*[](#keysight.ads.de.db.DesignAttrType.VIEW_NAME "Link to this definition")

    CELL\_TYPE *= <DesignAttrType.CELL\_TYPE: 3>*[](#keysight.ads.de.db.DesignAttrType.CELL_TYPE "Link to this definition")

    LAST\_SAVED\_TIME *= <DesignAttrType.LAST\_SAVED\_TIME: 4>*[](#keysight.ads.de.db.DesignAttrType.LAST_SAVED_TIME "Link to this definition")

*class* keysight.ads.de.db.DesignMode[](#keysight.ads.de.db.DesignMode "Link to this definition")
:   READ\_ONLY *= <DesignMode.READ\_ONLY: 0>*[](#keysight.ads.de.db.DesignMode.READ_ONLY "Link to this definition")

    WRITE *= <DesignMode.WRITE: 1>*[](#keysight.ads.de.db.DesignMode.WRITE "Link to this definition")

    APPEND *= <DesignMode.APPEND: 2>*[](#keysight.ads.de.db.DesignMode.APPEND "Link to this definition")

*class* keysight.ads.de.db.InstAttrType[](#keysight.ads.de.db.InstAttrType "Link to this definition")
:   LIB\_NAME *= <InstAttrType.LIB\_NAME: 0>*[](#keysight.ads.de.db.InstAttrType.LIB_NAME "Link to this definition")

    CELL\_NAME *= <InstAttrType.CELL\_NAME: 1>*[](#keysight.ads.de.db.InstAttrType.CELL_NAME "Link to this definition")

    VIEW\_NAME *= <InstAttrType.VIEW\_NAME: 2>*[](#keysight.ads.de.db.InstAttrType.VIEW_NAME "Link to this definition")

    NAME *= <InstAttrType.NAME: 3>*[](#keysight.ads.de.db.InstAttrType.NAME "Link to this definition")

    NUM\_BITS *= <InstAttrType.NUM\_BITS: 4>*[](#keysight.ads.de.db.InstAttrType.NUM_BITS "Link to this definition")

    IS\_BOUND *= <InstAttrType.IS\_BOUND: 5>*[](#keysight.ads.de.db.InstAttrType.IS_BOUND "Link to this definition")

*class* keysight.ads.de.db.InstTermAttrType[](#keysight.ads.de.db.InstTermAttrType "Link to this definition")
:   NAME *= <InstTermAttrType.NAME: 0>*[](#keysight.ads.de.db.InstTermAttrType.NAME "Link to this definition")

*class* keysight.ads.de.db.NetAttrType[](#keysight.ads.de.db.NetAttrType "Link to this definition")
:   NAME *= <NetAttrType.NAME: 0>*[](#keysight.ads.de.db.NetAttrType.NAME "Link to this definition")

    SIG\_TYPE *= <NetAttrType.SIG\_TYPE: 1>*[](#keysight.ads.de.db.NetAttrType.SIG_TYPE "Link to this definition")

    IS\_GLOBAL *= <NetAttrType.IS\_GLOBAL: 2>*[](#keysight.ads.de.db.NetAttrType.IS_GLOBAL "Link to this definition")

    IS\_IMPLICIT *= <NetAttrType.IS\_IMPLICIT: 3>*[](#keysight.ads.de.db.NetAttrType.IS_IMPLICIT "Link to this definition")

    IS\_EMPTY *= <NetAttrType.IS\_EMPTY: 4>*[](#keysight.ads.de.db.NetAttrType.IS_EMPTY "Link to this definition")

    NUM\_BITS *= <NetAttrType.NUM\_BITS: 5>*[](#keysight.ads.de.db.NetAttrType.NUM_BITS "Link to this definition")

*class* keysight.ads.de.db.Orientation[](#keysight.ads.de.db.Orientation "Link to this definition")
:   R0 *= <OrientEnum.R0: 0>*[](#keysight.ads.de.db.Orientation.R0 "Link to this definition")

    R90 *= <OrientEnum.R90: 1>*[](#keysight.ads.de.db.Orientation.R90 "Link to this definition")

    R180 *= <OrientEnum.R180: 2>*[](#keysight.ads.de.db.Orientation.R180 "Link to this definition")

    R270 *= <OrientEnum.R270: 3>*[](#keysight.ads.de.db.Orientation.R270 "Link to this definition")

    MY *= <OrientEnum.MY: 4>*[](#keysight.ads.de.db.Orientation.MY "Link to this definition")

    MYR90 *= <OrientEnum.MYR90: 5>*[](#keysight.ads.de.db.Orientation.MYR90 "Link to this definition")

    MX *= <OrientEnum.MX: 6>*[](#keysight.ads.de.db.Orientation.MX "Link to this definition")

    MXR90 *= <OrientEnum.MXR90: 7>*[](#keysight.ads.de.db.Orientation.MXR90 "Link to this definition")

    *static* concat\_orientations(*first: [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*, *second: [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*) → [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")[](#keysight.ads.de.db.Orientation.concat_orientations "Link to this definition")

    *static* get\_relative\_orientation(*first: [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*, *second: [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*) → [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")[](#keysight.ads.de.db.Orientation.get_relative_orientation "Link to this definition")

*class* keysight.ads.de.db.SignalType[](#keysight.ads.de.db.SignalType "Link to this definition")
:   SIGNAL *= <SignalType.SIGNAL: 0>*[](#keysight.ads.de.db.SignalType.SIGNAL "Link to this definition")

    POWER *= <SignalType.POWER: 1>*[](#keysight.ads.de.db.SignalType.POWER "Link to this definition")

    GROUND *= <SignalType.GROUND: 2>*[](#keysight.ads.de.db.SignalType.GROUND "Link to this definition")

    CLOCK *= <SignalType.CLOCK: 3>*[](#keysight.ads.de.db.SignalType.CLOCK "Link to this definition")

    TIE\_OFF *= <SignalType.TIE\_OFF: 4>*[](#keysight.ads.de.db.SignalType.TIE_OFF "Link to this definition")

    TIE\_HI *= <SignalType.TIE\_HI: 5>*[](#keysight.ads.de.db.SignalType.TIE_HI "Link to this definition")

    TIE\_LO *= <SignalType.TIE\_LO: 6>*[](#keysight.ads.de.db.SignalType.TIE_LO "Link to this definition")

    ANALOG *= <SignalType.ANALOG: 7>*[](#keysight.ads.de.db.SignalType.ANALOG "Link to this definition")

    SCAN *= <SignalType.SCAN: 8>*[](#keysight.ads.de.db.SignalType.SCAN "Link to this definition")

    RESET *= <SignalType.RESET: 9>*[](#keysight.ads.de.db.SignalType.RESET "Link to this definition")

*class* keysight.ads.de.db.TermAttrType[](#keysight.ads.de.db.TermAttrType "Link to this definition")
:   NAME *= <TermAttrType.NAME: 0>*[](#keysight.ads.de.db.TermAttrType.NAME "Link to this definition")

    HAS\_PINS *= <TermAttrType.HAS\_PINS: 1>*[](#keysight.ads.de.db.TermAttrType.HAS_PINS "Link to this definition")

    NUM\_BITS *= <TermAttrType.NUM\_BITS: 2>*[](#keysight.ads.de.db.TermAttrType.NUM_BITS "Link to this definition")

*class* keysight.ads.de.db.TermType[](#keysight.ads.de.db.TermType "Link to this definition")
:   INPUT *= <TermType.INPUT: 0>*[](#keysight.ads.de.db.TermType.INPUT "Link to this definition")

    OUTPUT *= <TermType.OUTPUT: 1>*[](#keysight.ads.de.db.TermType.OUTPUT "Link to this definition")

    INPUT\_OUTPUT *= <TermType.INPUT\_OUTPUT: 2>*[](#keysight.ads.de.db.TermType.INPUT_OUTPUT "Link to this definition")

    SWITCH *= <TermType.SWITCH: 3>*[](#keysight.ads.de.db.TermType.SWITCH "Link to this definition")

    JUMPER *= <TermType.JUMPER: 4>*[](#keysight.ads.de.db.TermType.JUMPER "Link to this definition")

    UNUSED *= <TermType.UNUSED: 5>*[](#keysight.ads.de.db.TermType.UNUSED "Link to this definition")

    TRISTATE *= <TermType.TRISTATE: 6>*[](#keysight.ads.de.db.TermType.TRISTATE "Link to this definition")

*class* keysight.ads.de.db.TextAlignment[](#keysight.ads.de.db.TextAlignment "Link to this definition")
:   UPPER\_LEFT *= <TextAlignment.UPPER\_LEFT: 0>*[](#keysight.ads.de.db.TextAlignment.UPPER_LEFT "Link to this definition")

    CENTER\_LEFT *= <TextAlignment.CENTER\_LEFT: 1>*[](#keysight.ads.de.db.TextAlignment.CENTER_LEFT "Link to this definition")

    LOWER\_LEFT *= <TextAlignment.LOWER\_LEFT: 2>*[](#keysight.ads.de.db.TextAlignment.LOWER_LEFT "Link to this definition")

    UPPER\_CENTER *= <TextAlignment.UPPER\_CENTER: 3>*[](#keysight.ads.de.db.TextAlignment.UPPER_CENTER "Link to this definition")

    CENTER\_CENTER *= <TextAlignment.CENTER\_CENTER: 4>*[](#keysight.ads.de.db.TextAlignment.CENTER_CENTER "Link to this definition")

    LOWER\_CENTER *= <TextAlignment.LOWER\_CENTER: 5>*[](#keysight.ads.de.db.TextAlignment.LOWER_CENTER "Link to this definition")

    UPPER\_RIGHT *= <TextAlignment.UPPER\_RIGHT: 6>*[](#keysight.ads.de.db.TextAlignment.UPPER_RIGHT "Link to this definition")

    CENTER\_RIGHT *= <TextAlignment.CENTER\_RIGHT: 7>*[](#keysight.ads.de.db.TextAlignment.CENTER_RIGHT "Link to this definition")

    LOWER\_RIGHT *= <TextAlignment.LOWER\_RIGHT: 8>*[](#keysight.ads.de.db.TextAlignment.LOWER_RIGHT "Link to this definition")

*class* keysight.ads.de.db.TextDisplayFormat[](#keysight.ads.de.db.TextDisplayFormat "Link to this definition")
:   NAME *= <TextDisplayFormat.NAME: 0>*[](#keysight.ads.de.db.TextDisplayFormat.NAME "Link to this definition")

    VALUE *= <TextDisplayFormat.VALUE: 1>*[](#keysight.ads.de.db.TextDisplayFormat.VALUE "Link to this definition")

    NAME\_VALUE *= <TextDisplayFormat.NAME\_VALUE: 2>*[](#keysight.ads.de.db.TextDisplayFormat.NAME_VALUE "Link to this definition")

On this page

[Previous

Callbacks](callbacks.md)
[Next

Parameter Forms](forms.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top