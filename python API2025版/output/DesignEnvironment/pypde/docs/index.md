<!-- 来源: pypde\docs\index.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../index.md)
* Design

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

* [Introduction](../../pydocs/intro/index.md)
  + [Licensing](../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../pydocs/intro/extension.md)
* [Concepts](../../pydocs/concepts/index.md)
  + [Terminology](../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../pydocs/concepts/execution.md)
* [How-To](../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../pydocs/howto/pytest.md)

* Design
  + [Reference](reference/index.md)
    - [keysight.ads.de](reference/de/index.md)
      * [Workspace](reference/de/workspace.md)
      * [Library](reference/de/library.md)
      * [Cell](reference/de/cell.md)
      * [View](reference/de/view.md)
      * [CellviewRef](reference/de/cellviewref.md)
      * [DesignHierarchy](reference/de/design_hierarchy.md)
      * [DMData](reference/de/dmdata.md)
      * [ItemInfo](reference/de/item_info.md)
      * [Points](reference/de/points.md)
      * [Collections](reference/de/collections.md)
    - [keysight.ads.de.ael](reference/de/ael.md)
    - [keysight.ads.de.app](reference/de/app/index.md)
      * [Actions and Menus](reference/de/app/action.md)
      * [Addons](reference/de/app/addon.md)
      * [Callbacks](reference/de/app/callbacks.md)
      * [Windows and Widgets](reference/de/app/window.md)
    - [keysight.ads.de.db](reference/de/db/index.md)
      * [Callbacks](reference/de/db/callbacks.md)
      * [Enumerated Types](reference/de/db/enums.md)
      * [Parameter Forms](reference/de/db/forms.md)
      * [GenPolyline](reference/de/db/genpolyline.md)
      * [Model Definition](reference/de/db/model_def.md)
      * [Parameters](reference/de/db/parameters.md)
      * [Properties](reference/de/db/properties.md)
      * [Transaction](reference/de/db/transaction.md)
    - [keysight.ads.de.db\_dbu](reference/de/db_dbu/index.md)
    - [keysight.ads.de.db\_uu](reference/de/db_uu/index.md)
      * [Design Elements](reference/de/db_uu/db_uu.md)
      * [LayerId](reference/de/db_uu/layer_id.md)
      * [LineTypeInfo](reference/de/db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](reference/de/experimental/index.md)
      * [CDF](reference/de/experimental/cdf/index.md)
      * [Commands](reference/de/experimental/commands.md)
      * [Handles](reference/de/experimental/handles.md)
      * [Netlist Utilities](reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](reference/de/experimental/polygon_utils.md)
      * [Preferences](reference/de/experimental/preferences.md)
      * [xxPro View](reference/de/experimental/pro_view.md)
      * [Symbol Generator](reference/de/experimental/symbol.md)
      * [Text Maker](reference/de/experimental/text_maker.md)
    - [keysight.ads.de.tech](reference/de/tech/index.md)
      * [Tech](reference/de/tech/tech.md)
      * [Padstacks](reference/de/tech/pads/pads.md)
      * [Via Rules](reference/de/tech/rule/rule.md)
      * [Nested Technology](reference/de/tech/nested/nested.md)
    - [keysight.ads.de.app.dds](reference/de/app/dds.md)
  + [Examples](examples/index.md)
    - [Calling Between AEL and Python](examples/ex_calling_ael_and_python.md)
    - [Create Layout](examples/ex_create_layout.md)
    - [Create Schematic](examples/ex_create_schematic.md)
    - [Create Workspace](examples/ex_workspace.md)
    - [Create, Simulate, and Plot](examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](examples/ex_cdf.md)
    - [Component Parameters](examples/ex_parameters.md)
    - [Creating an Item Definition](examples/ex_itemdef.md)
    - [Model Definition Properties](examples/ex_model.md)
    - [Adding Instances to a Design](examples/ex_lpf.md)
    - [Properties](examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](examples/ex_menu_addon.md)
    - [Padstacks and Vias](examples/ex_padstack.md)
    - [Nested Technology](examples/ex_nested.md)
    - [Rules](examples/ex_rules.md)
    - [Placing Text](examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](examples/ex_polygon.md)
    - [PySide2](examples/ex_pyside.md)
    - [Traversing Hierarchy](examples/ex_traversing_hierarchy.md)
    - [Working with VAR](examples/ex_working_with_var.md)
    - [XML RPC](examples/ex_xml_rpc.md)
    - [GDSII Import and Export](examples/ex_translate_gds.md)
* [Technology](../../pysubst/docs/index.md)
  + [Reference](../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Design[](#design "Link to this heading")

Contents:

* [Reference](reference/index.md)
  + [keysight.ads.de](reference/de/index.md)
  + [keysight.ads.de.ael](reference/de/ael.md)
  + [keysight.ads.de.app](reference/de/app/index.md)
  + [keysight.ads.de.db](reference/de/db/index.md)
  + [keysight.ads.de.db\_dbu](reference/de/db_dbu/index.md)
  + [keysight.ads.de.db\_uu](reference/de/db_uu/index.md)
  + [keysight.ads.de.experimental](reference/de/experimental/index.md)
  + [keysight.ads.de.tech](reference/de/tech/index.md)
  + [keysight.ads.de.app.dds](reference/de/app/dds.md)
* [Examples](examples/index.md)
  + [Calling Between AEL and Python](examples/ex_calling_ael_and_python.md)
  + [Create Layout](examples/ex_create_layout.md)
  + [Create Schematic](examples/ex_create_schematic.md)
  + [Create Workspace](examples/ex_workspace.md)
  + [Create, Simulate, and Plot](examples/ex_create_sim_and_plot.md)
  + [Interoperable Component Parameters](examples/ex_cdf.md)
  + [Component Parameters](examples/ex_parameters.md)
  + [Creating an Item Definition](examples/ex_itemdef.md)
  + [Model Definition Properties](examples/ex_model.md)
  + [Adding Instances to a Design](examples/ex_lpf.md)
  + [Properties](examples/ex_properties.md)
  + [Creating Custom Menus Using an Addon](examples/ex_menu_addon.md)
  + [Padstacks and Vias](examples/ex_padstack.md)
  + [Nested Technology](examples/ex_nested.md)
  + [Rules](examples/ex_rules.md)
  + [Placing Text](examples/ex_place_text.md)
  + [Paths, Traces, and Polygons](examples/ex_polygon.md)
  + [PySide2](examples/ex_pyside.md)
  + [Traversing Hierarchy](examples/ex_traversing_hierarchy.md)
  + [Working with VAR](examples/ex_working_with_var.md)
  + [XML RPC](examples/ex_xml_rpc.md)
  + [GDSII Import and Export](examples/ex_translate_gds.md)

On this page

[Previous

How to Use Pytest](../../pydocs/howto/pytest.md)
[Next

Reference](reference/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top