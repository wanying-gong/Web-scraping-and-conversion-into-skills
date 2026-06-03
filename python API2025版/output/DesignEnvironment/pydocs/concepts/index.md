<!-- 来源: pydocs\concepts\index.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../index.md)
* Concepts

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

* [Introduction](../intro/index.md)
  + [Licensing](../intro/licensing.md)
  + [Using Python in ADS Design Environment](../intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../intro/extension.md)
* Concepts
  + [Terminology](terminology.md)
    - [Workspace Elements](workspace_elements.md)
    - [Connectivity Objects](connectivity.md)
  + [OpenAccess Integration](openaccess_integration.md)
  + [Python Script Execution](execution.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
  + [How to Use Pytest](../howto/pytest.md)

* [Design](../../pypde/docs/index.md)
  + [Reference](../../pypde/docs/reference/index.md)
    - [keysight.ads.de](../../pypde/docs/reference/de/index.md)
      * [Workspace](../../pypde/docs/reference/de/workspace.md)
      * [Library](../../pypde/docs/reference/de/library.md)
      * [Cell](../../pypde/docs/reference/de/cell.md)
      * [View](../../pypde/docs/reference/de/view.md)
      * [CellviewRef](../../pypde/docs/reference/de/cellviewref.md)
      * [DesignHierarchy](../../pypde/docs/reference/de/design_hierarchy.md)
      * [DMData](../../pypde/docs/reference/de/dmdata.md)
      * [ItemInfo](../../pypde/docs/reference/de/item_info.md)
      * [Points](../../pypde/docs/reference/de/points.md)
      * [Collections](../../pypde/docs/reference/de/collections.md)
    - [keysight.ads.de.ael](../../pypde/docs/reference/de/ael.md)
    - [keysight.ads.de.app](../../pypde/docs/reference/de/app/index.md)
      * [Actions and Menus](../../pypde/docs/reference/de/app/action.md)
      * [Addons](../../pypde/docs/reference/de/app/addon.md)
      * [Callbacks](../../pypde/docs/reference/de/app/callbacks.md)
      * [Windows and Widgets](../../pypde/docs/reference/de/app/window.md)
    - [keysight.ads.de.db](../../pypde/docs/reference/de/db/index.md)
      * [Callbacks](../../pypde/docs/reference/de/db/callbacks.md)
      * [Enumerated Types](../../pypde/docs/reference/de/db/enums.md)
      * [Parameter Forms](../../pypde/docs/reference/de/db/forms.md)
      * [GenPolyline](../../pypde/docs/reference/de/db/genpolyline.md)
      * [Model Definition](../../pypde/docs/reference/de/db/model_def.md)
      * [Parameters](../../pypde/docs/reference/de/db/parameters.md)
      * [Properties](../../pypde/docs/reference/de/db/properties.md)
      * [Transaction](../../pypde/docs/reference/de/db/transaction.md)
    - [keysight.ads.de.db\_dbu](../../pypde/docs/reference/de/db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../../pypde/docs/reference/de/db_uu/index.md)
      * [Design Elements](../../pypde/docs/reference/de/db_uu/db_uu.md)
      * [LayerId](../../pypde/docs/reference/de/db_uu/layer_id.md)
      * [LineTypeInfo](../../pypde/docs/reference/de/db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../../pypde/docs/reference/de/experimental/index.md)
      * [CDF](../../pypde/docs/reference/de/experimental/cdf/index.md)
      * [Commands](../../pypde/docs/reference/de/experimental/commands.md)
      * [Handles](../../pypde/docs/reference/de/experimental/handles.md)
      * [Netlist Utilities](../../pypde/docs/reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../pypde/docs/reference/de/experimental/polygon_utils.md)
      * [Preferences](../../pypde/docs/reference/de/experimental/preferences.md)
      * [xxPro View](../../pypde/docs/reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../pypde/docs/reference/de/experimental/symbol.md)
      * [Text Maker](../../pypde/docs/reference/de/experimental/text_maker.md)
    - [keysight.ads.de.tech](../../pypde/docs/reference/de/tech/index.md)
      * [Tech](../../pypde/docs/reference/de/tech/tech.md)
      * [Padstacks](../../pypde/docs/reference/de/tech/pads/pads.md)
      * [Via Rules](../../pypde/docs/reference/de/tech/rule/rule.md)
      * [Nested Technology](../../pypde/docs/reference/de/tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../../pypde/docs/reference/de/app/dds.md)
  + [Examples](../../pypde/docs/examples/index.md)
    - [Calling Between AEL and Python](../../pypde/docs/examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../pypde/docs/examples/ex_create_layout.md)
    - [Create Schematic](../../pypde/docs/examples/ex_create_schematic.md)
    - [Create Workspace](../../pypde/docs/examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../pypde/docs/examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../pypde/docs/examples/ex_cdf.md)
    - [Component Parameters](../../pypde/docs/examples/ex_parameters.md)
    - [Creating an Item Definition](../../pypde/docs/examples/ex_itemdef.md)
    - [Model Definition Properties](../../pypde/docs/examples/ex_model.md)
    - [Adding Instances to a Design](../../pypde/docs/examples/ex_lpf.md)
    - [Properties](../../pypde/docs/examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../pypde/docs/examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../pypde/docs/examples/ex_padstack.md)
    - [Nested Technology](../../pypde/docs/examples/ex_nested.md)
    - [Rules](../../pypde/docs/examples/ex_rules.md)
    - [Placing Text](../../pypde/docs/examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../pypde/docs/examples/ex_polygon.md)
    - [PySide2](../../pypde/docs/examples/ex_pyside.md)
    - [Traversing Hierarchy](../../pypde/docs/examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../pypde/docs/examples/ex_working_with_var.md)
    - [XML RPC](../../pypde/docs/examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../pypde/docs/examples/ex_translate_gds.md)
* [Technology](../../pysubst/docs/index.md)
  + [Reference](../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Concepts[](#concepts "Link to this heading")

* [Terminology](terminology.md)
  + [Workspace Elements](workspace_elements.md)
  + [Connectivity Objects](connectivity.md)
* [OpenAccess Integration](openaccess_integration.md)
  + [Enabling Python Support For Your Library](openaccess_integration.md#enabling-python-support-for-your-library)
  + [Library Initialization](openaccess_integration.md#library-initialization)
  + [Cell Initialization](openaccess_integration.md#cell-initialization)
  + [View Initialization](openaccess_integration.md#view-initialization)
* [Python Script Execution](execution.md)
  + [Automation](execution.md#automation)

On this page

[Previous

Using ADS Design Environment Functionality in Python](../intro/extension.md)
[Next

Terminology](terminology.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top