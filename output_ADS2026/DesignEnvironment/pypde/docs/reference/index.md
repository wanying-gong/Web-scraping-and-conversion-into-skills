<!-- 来源: pypde\docs\reference\index.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Reference](../../../reference.md)
* Design Environment

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

* [Introduction](../../../pydocs/intro/index.md)
* [How-To](../../../pydocs/howto/index.md)
  + [Use Python in the ADS Application](../../../pydocs/howto/embedded.md)
  + [Set Up a Python Virtual Environment](../../../pydocs/howto/venv.md)
  + [Set Up Visual Studio Code for Development](../../../pydocs/howto/vscode.md)
  + [Use Pytest](../../../pydocs/howto/pytest.md)
  + [Enable Python Support For Your Library](../../../pydocs/howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../../../pydocs/howto/execution.md)
  + [Export Workspace and Design Objects to Python](../../../pydocs/howto/exporter.md)
  + [Record Actions in ADS as Python Code](../../../pydocs/howto/recorder.md)
  + [Develop a Python Pcell in ADS](../../../pydocs/howto/pcell.md)
* [ADS Concepts](../../../pydocs/concepts/index.md)
  + [Workspace Elements](../../../pydocs/concepts/workspace_elements.md)
  + [Connectivity Objects](../../../pydocs/concepts/connectivity.md)
* [Reference](../../../reference.md)
  + [Deprecated APIs](../../../pydocs/py/_generated/deprecations.md)
  + Design Environment
    - [keysight.ads.de](de/index.md)
      * [ADS Application Environment](de/ads_environment.md)
      * [ADS Workspace Components](de/workspace_components.md)
      * [Design Hierarchy](de/design_hierarchy.md)
      * [Smart Package](de/package.md)
      * [Geometry](de/geometry.md)
      * [Collections](de/collections.md)
      * [Printer](de/printer.md)
    - [keysight.ads.de.ael](de/ael.md)
    - [keysight.ads.de.app](de/app/index.md)
      * [Application](de/app/application.md)
      * [Actions and Menus](de/app/action.md)
      * [Addons](de/app/addon.md)
      * [Window and Design Callbacks](de/app/callbacks.md)
      * [Windows and Widgets](de/app/window.md)
      * [Experimental](de/app/experimental.md)
    - [keysight.ads.de.app.dds](de/app/dds.md)
      * [exec\_python](de/app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](de/db/index.md)
      * [Models, Parameters, and Forms](de/db/parameters.md)
      * [Properties](de/db/properties.md)
      * [Preferences](de/db/preferences.md)
      * [Transaction](de/db/transaction.md)
      * [Smart Mount](de/db/smart_mount.md)
      * [Geometry](de/db/geometry.md)
      * [Teardrops](de/db/teardrops.md)
    - [keysight.ads.de.db\_dbu](de/db_dbu/index.md)
      * [DbBox](de/db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](de/db_uu/index.md)
      * [Database Objects](de/db_uu/database_objects.md)
      * [Iterators](de/db_uu/iterators.md)
      * [Designs](de/db_uu/design.md)
      * [Teardrops](de/db_uu/teardrop.md)
    - [keysight.ads.de.experimental](de/experimental/index.md)
      * [CDF](de/experimental/cdf.md)
      * [Design Commands](de/experimental/commands.md)
      * [Component Handles](de/experimental/handles.md)
      * [Netlist Utilities](de/experimental/netlist_helper.md)
      * [Polygon Utilities](de/experimental/polygon_utils.md)
      * [xxPro View](de/experimental/pro_view.md)
      * [Symbol Generator](de/experimental/symbol.md)
      * [Text Maker](de/experimental/text_maker.md)
      * [Notebook](de/experimental/notebook.md)
      * [Layer/Purpose Pairs](de/experimental/lpp.md)
    - [keysight.ads.de.tech](de/tech/index.md)
      * [Technology](de/tech/tech.md)
      * [Layers](de/tech/layers.md)
      * [Line Items](de/tech/line_items.md)
      * [Padstacks](de/tech/pads.md)
      * [Rules](de/tech/rule.md)
  + [Substrate](../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../../examples.md)
  + [Design Environment](../examples/index.md)
    - [Workspace Creation](../examples/workspace/ex_workspace.md)
    - [Design Creation](../examples/design_creation/index.md)
      * [Create Layout](../examples/design_creation/ex_create_layout.md)
      * [Create Schematic](../examples/design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../examples/design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../examples/design_elements/index.md)
      * [Placing Text](../examples/design_elements/ex_place_text.md)
      * [Moving Objects](../examples/design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../examples/design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../examples/design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../examples/design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../examples/design_elements/ex_plane_editing.md)
    - [Parameters](../examples/parameters/index.md)
      * [Interoperable Component Parameters](../examples/parameters/ex_cdf.md)
      * [Working with VAR](../examples/parameters/ex_working_with_var.md)
      * [Component Parameters](../examples/parameters/ex_parameters.md)
      * [Creating an Item Definition](../examples/parameters/ex_itemdef.md)
      * [Model Definition Properties](../examples/parameters/ex_model.md)
      * [Creating a Text Form](../examples/parameters/ex_text_form.md)
      * [Properties](../examples/parameters/ex_properties.md)
    - [Technology](../examples/technology/index.md)
      * [Padstacks and Vias](../examples/technology/ex_padstack.md)
      * [Nested Technology](../examples/technology/ex_nested.md)
      * [Rules](../examples/technology/ex_rules.md)
    - [Translators](../examples/translators/index.md)
      * [DXF Import and Export](../examples/translators/ex_translate_dxf.md)
      * [Gerber Export](../examples/translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../examples/translators/ex_translate_gds.md)
    - [UI](../examples/ui/index.md)
      * [Creating Custom Menus Using an Addon](../examples/ui/ex_menu_addon.md)
      * [PySide](../examples/ui/ex_pyside.md)
    - [Utility](../examples/utility/index.md)
      * [Calling Between AEL and Python](../examples/utility/ex_calling_ael_and_python.md)
      * [Smart Package](../examples/utility/ex_smart_pkg.md)
      * [XML RPC](../examples/utility/ex_xml_rpc.md)
  + [Substrate](../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../../genindex.md)

# Design Environment[](#design-environment "Link to this heading")

The following packages are available as part of the ADS Python design environment interface. Note that API’s
residing in the [`keysight.ads.de.app`](de/app/index.md#module-keysight.ads.de.app "keysight.ads.de.app") package are only available when running within the ADS application
context. See [Execute Python Scripts in Different Contexts](../../../pydocs/howto/execution.md#python-script-execution) for more information.

Any entity that begins with an underscore, such as: \_private\_function(), \_PrivateClass or keysight.ads.de.\_private\_module,
is considered a private implementation detail and should not be used directly. Expect any private implementation detail
to change or be removed without notice.

* [keysight.ads.de](de/index.md)
* [keysight.ads.de.ael](de/ael.md)
* [keysight.ads.de.app](de/app/index.md)
* [keysight.ads.de.app.dds](de/app/dds.md)
* [keysight.ads.de.db](de/db/index.md)
* [keysight.ads.de.db\_dbu](de/db_dbu/index.md)
* [keysight.ads.de.db\_uu](de/db_uu/index.md)
* [keysight.ads.de.experimental](de/experimental/index.md)
* [keysight.ads.de.tech](de/tech/index.md)

On this page

[Previous

Deprecated APIs](../../../pydocs/py/_generated/deprecations.md)
[Next

keysight.ads.de](de/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top