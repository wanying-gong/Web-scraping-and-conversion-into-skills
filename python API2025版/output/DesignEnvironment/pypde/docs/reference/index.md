<!-- 来源: pypde\docs\reference\index.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* Reference

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

* [Introduction](../../../pydocs/intro/index.md)
  + [Licensing](../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../pydocs/intro/extension.md)
* [Concepts](../../../pydocs/concepts/index.md)
  + [Terminology](../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../pydocs/concepts/execution.md)
* [How-To](../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../pydocs/howto/pytest.md)

* [Design](../index.md)
  + Reference
    - [keysight.ads.de](de/index.md)
      * [Workspace](de/workspace.md)
      * [Library](de/library.md)
      * [Cell](de/cell.md)
      * [View](de/view.md)
      * [CellviewRef](de/cellviewref.md)
      * [DesignHierarchy](de/design_hierarchy.md)
      * [DMData](de/dmdata.md)
      * [ItemInfo](de/item_info.md)
      * [Points](de/points.md)
      * [Collections](de/collections.md)
    - [keysight.ads.de.ael](de/ael.md)
    - [keysight.ads.de.app](de/app/index.md)
      * [Actions and Menus](de/app/action.md)
      * [Addons](de/app/addon.md)
      * [Callbacks](de/app/callbacks.md)
      * [Windows and Widgets](de/app/window.md)
    - [keysight.ads.de.db](de/db/index.md)
      * [Callbacks](de/db/callbacks.md)
      * [Enumerated Types](de/db/enums.md)
      * [Parameter Forms](de/db/forms.md)
      * [GenPolyline](de/db/genpolyline.md)
      * [Model Definition](de/db/model_def.md)
      * [Parameters](de/db/parameters.md)
      * [Properties](de/db/properties.md)
      * [Transaction](de/db/transaction.md)
    - [keysight.ads.de.db\_dbu](de/db_dbu/index.md)
    - [keysight.ads.de.db\_uu](de/db_uu/index.md)
      * [Design Elements](de/db_uu/db_uu.md)
      * [LayerId](de/db_uu/layer_id.md)
      * [LineTypeInfo](de/db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](de/experimental/index.md)
      * [CDF](de/experimental/cdf/index.md)
      * [Commands](de/experimental/commands.md)
      * [Handles](de/experimental/handles.md)
      * [Netlist Utilities](de/experimental/netlist_helper.md)
      * [Polygon Utilities](de/experimental/polygon_utils.md)
      * [Preferences](de/experimental/preferences.md)
      * [xxPro View](de/experimental/pro_view.md)
      * [Symbol Generator](de/experimental/symbol.md)
      * [Text Maker](de/experimental/text_maker.md)
    - [keysight.ads.de.tech](de/tech/index.md)
      * [Tech](de/tech/tech.md)
      * [Padstacks](de/tech/pads/pads.md)
      * [Via Rules](de/tech/rule/rule.md)
      * [Nested Technology](de/tech/nested/nested.md)
    - [keysight.ads.de.app.dds](de/app/dds.md)
  + [Examples](../examples/index.md)
    - [Calling Between AEL and Python](../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../examples/ex_create_layout.md)
    - [Create Schematic](../examples/ex_create_schematic.md)
    - [Create Workspace](../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../examples/ex_cdf.md)
    - [Component Parameters](../examples/ex_parameters.md)
    - [Creating an Item Definition](../examples/ex_itemdef.md)
    - [Model Definition Properties](../examples/ex_model.md)
    - [Adding Instances to a Design](../examples/ex_lpf.md)
    - [Properties](../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../examples/ex_padstack.md)
    - [Nested Technology](../examples/ex_nested.md)
    - [Rules](../examples/ex_rules.md)
    - [Placing Text](../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../examples/ex_polygon.md)
    - [PySide2](../examples/ex_pyside.md)
    - [Traversing Hierarchy](../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../examples/ex_working_with_var.md)
    - [XML RPC](../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../examples/ex_translate_gds.md)
* [Technology](../../../pysubst/docs/index.md)
  + [Reference](../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Reference[](#reference "Link to this heading")

The following packages are available as part of the ADS Python design environment interface. Note that API’s
residing in the [`keysight.ads.de.app`](de/app/index.md#module-keysight.ads.de.app "keysight.ads.de.app") package are only available when running within the ADS application
context. See [Python Script Execution](../../../pydocs/concepts/execution.md#python-script-execution) for more information.

Any entity that begins with an underscore, such as: \_private\_function(), \_PrivateClass or keysight.ads.de.\_private\_module,
is considered a private implementation detail and should not be used directly. Expect any private implementation detail
to change or be removed without notice.

* [keysight.ads.de](de/index.md)
* [keysight.ads.de.ael](de/ael.md)
* [keysight.ads.de.app](de/app/index.md)
* [keysight.ads.de.db](de/db/index.md)
* [keysight.ads.de.db\_dbu](de/db_dbu/index.md)
* [keysight.ads.de.db\_uu](de/db_uu/index.md)
* [keysight.ads.de.experimental](de/experimental/index.md)
* [keysight.ads.de.tech](de/tech/index.md)
* [keysight.ads.de.app.dds](de/app/dds.md)

**Indices**

* [Index](../../../genindex.md)
* [Module Index](../../../py-modindex.md)

On this page

[Previous

Design](../index.md)
[Next

keysight.ads.de](de/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top