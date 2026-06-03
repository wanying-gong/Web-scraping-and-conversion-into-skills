<!-- 来源: pypde\docs\reference\de\tech\index.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* keysight.ads.de.tech

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
    - keysight.ads.de.tech
      * [Tech](tech.md)
      * [Padstacks](pads/pads.md)
      * [Via Rules](rule/rule.md)
      * [Nested Technology](nested/nested.md)
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

# keysight.ads.de.tech[](#module-keysight.ads.de.tech "Link to this heading")

ADS Technology module.

* [Tech](tech.md)
  + [Classes](tech.md#classes)
    - [`DerivedLayer`](tech.md#keysight.ads.de.tech.DerivedLayer)
    - [`Layer`](tech.md#keysight.ads.de.tech.Layer)
    - [`LayerSlice`](tech.md#keysight.ads.de.tech.LayerSlice)
    - [`LineClearance`](tech.md#keysight.ads.de.tech.LineClearance)
    - [`LineCorner`](tech.md#keysight.ads.de.tech.LineCorner)
    - [`LineItem`](tech.md#keysight.ads.de.tech.LineItem)
    - [`LineStripItem`](tech.md#keysight.ads.de.tech.LineStripItem)
    - [`LineTypeSimulationModel`](tech.md#keysight.ads.de.tech.LineTypeSimulationModel)
    - [`PhysicalLayer`](tech.md#keysight.ads.de.tech.PhysicalLayer)
    - [`Purpose`](tech.md#keysight.ads.de.tech.Purpose)
    - [`SmartMountSettings`](tech.md#keysight.ads.de.tech.SmartMountSettings)
    - [`Tech`](tech.md#keysight.ads.de.tech.Tech)
  + [Enumerated Types](tech.md#enumerated-types)
    - [`LayerOp`](tech.md#keysight.ads.de.tech.LayerOp)
    - [`LineEndType`](tech.md#keysight.ads.de.tech.LineEndType)
    - [`LineCornerType`](tech.md#keysight.ads.de.tech.LineCornerType)
    - [`LineStripSpacingType`](tech.md#keysight.ads.de.tech.LineStripSpacingType)
    - [`OAMaterial`](tech.md#keysight.ads.de.tech.OAMaterial)
    - [`ProcessRole`](tech.md#keysight.ads.de.tech.ProcessRole)
    - [`SmartMountSubtype`](tech.md#keysight.ads.de.tech.SmartMountSubtype)
  + [Functions](tech.md#functions)
    - [`create_tech()`](tech.md#keysight.ads.de.tech.create_tech)
    - [`delete_tech()`](tech.md#keysight.ads.de.tech.delete_tech)
* [Padstacks](pads/pads.md)
  + [Classes](pads/pads.md#classes)
    - [`LengthValue`](pads/pads.md#keysight.ads.de.tech.pads.LengthValue)
    - [`LayerMatcher`](pads/pads.md#keysight.ads.de.tech.pads.LayerMatcher)
    - [`MatchLayerById`](pads/pads.md#keysight.ads.de.tech.pads.MatchLayerById)
    - [`MatchLayerByName`](pads/pads.md#keysight.ads.de.tech.pads.MatchLayerByName)
    - [`MatchLayerFromBottomOfBoard`](pads/pads.md#keysight.ads.de.tech.pads.MatchLayerFromBottomOfBoard)
    - [`MatchLayerFromTopOfBoard`](pads/pads.md#keysight.ads.de.tech.pads.MatchLayerFromTopOfBoard)
    - [`Antipad`](pads/pads.md#keysight.ads.de.tech.pads.Antipad)
    - [`MaskExpansion`](pads/pads.md#keysight.ads.de.tech.pads.MaskExpansion)
    - [`Pad`](pads/pads.md#keysight.ads.de.tech.pads.Pad)
    - [`PadLayerEntry`](pads/pads.md#keysight.ads.de.tech.pads.PadLayerEntry)
    - [`Padstack`](pads/pads.md#keysight.ads.de.tech.pads.Padstack)
    - [`Thermal`](pads/pads.md#keysight.ads.de.tech.pads.Thermal)
    - [`ViaPadDrill`](pads/pads.md#keysight.ads.de.tech.pads.ViaPadDrill)
    - [`ChamferedRectPad`](pads/pads.md#keysight.ads.de.tech.pads.ChamferedRectPad)
    - [`CircularPad`](pads/pads.md#keysight.ads.de.tech.pads.CircularPad)
    - [`DonutPad`](pads/pads.md#keysight.ads.de.tech.pads.DonutPad)
    - [`NGonPad`](pads/pads.md#keysight.ads.de.tech.pads.NGonPad)
    - [`NoPad`](pads/pads.md#keysight.ads.de.tech.pads.NoPad)
    - [`OblongPad`](pads/pads.md#keysight.ads.de.tech.pads.OblongPad)
    - [`OctagonalPad`](pads/pads.md#keysight.ads.de.tech.pads.OctagonalPad)
    - [`RectangularPad`](pads/pads.md#keysight.ads.de.tech.pads.RectangularPad)
    - [`RoundedRectPad`](pads/pads.md#keysight.ads.de.tech.pads.RoundedRectPad)
    - [`SquarePad`](pads/pads.md#keysight.ads.de.tech.pads.SquarePad)
* [Via Rules](rule/rule.md)
  + [Classes](rule/rule.md#classes)
    - [`ClearanceRule`](rule/rule.md#keysight.ads.de.tech.rule.ClearanceRule)
    - [`DefaultScope`](rule/rule.md#keysight.ads.de.tech.rule.DefaultScope)
    - [`DifferentNetScope`](rule/rule.md#keysight.ads.de.tech.rule.DifferentNetScope)
    - [`LineTypeScope`](rule/rule.md#keysight.ads.de.tech.rule.LineTypeScope)
    - [`NetClassScope`](rule/rule.md#keysight.ads.de.tech.rule.NetClassScope)
    - [`NetScope`](rule/rule.md#keysight.ads.de.tech.rule.NetScope)
    - [`RuleScope`](rule/rule.md#keysight.ads.de.tech.rule.RuleScope)
    - [`SameNetScope`](rule/rule.md#keysight.ads.de.tech.rule.SameNetScope)
    - [`StackedViaRule`](rule/rule.md#keysight.ads.de.tech.rule.StackedViaRule)
    - [`TeardropRule`](rule/rule.md#keysight.ads.de.tech.rule.TeardropRule)
    - [`ViaRule`](rule/rule.md#keysight.ads.de.tech.rule.ViaRule)
* [Nested Technology](nested/nested.md)
  + [Classes](nested/nested.md#classes)
    - [`LayerMap`](nested/nested.md#keysight.ads.de.tech.nested.LayerMap)
  + [Functions](nested/nested.md#functions)
    - [`find_layer_map()`](nested/nested.md#keysight.ads.de.tech.nested.find_layer_map)

On this page

[Previous

Text Maker](../experimental/text_maker.md)
[Next

Tech](tech.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top