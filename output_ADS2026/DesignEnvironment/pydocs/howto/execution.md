<!-- 来源: pydocs\howto\execution.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../index.md)
* [How-To](index.md)
* Execute Python Scripts in Different Contexts

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

* [Introduction](../intro/index.md)
* [How-To](index.md)
  + [Use Python in the ADS Application](embedded.md)
  + [Set Up a Python Virtual Environment](venv.md)
  + [Set Up Visual Studio Code for Development](vscode.md)
  + [Use Pytest](pytest.md)
  + [Enable Python Support For Your Library](python_integration.md)
  + Execute Python Scripts in Different Contexts
  + [Export Workspace and Design Objects to Python](exporter.md)
  + [Record Actions in ADS as Python Code](recorder.md)
  + [Develop a Python Pcell in ADS](pcell.md)
* [ADS Concepts](../concepts/index.md)
  + [Workspace Elements](../concepts/workspace_elements.md)
  + [Connectivity Objects](../concepts/connectivity.md)
* [Reference](../../reference.md)
  + [Deprecated APIs](../py/_generated/deprecations.md)
  + [Design Environment](../../pypde/docs/reference/index.md)
    - [keysight.ads.de](../../pypde/docs/reference/de/index.md)
      * [ADS Application Environment](../../pypde/docs/reference/de/ads_environment.md)
      * [ADS Workspace Components](../../pypde/docs/reference/de/workspace_components.md)
      * [Design Hierarchy](../../pypde/docs/reference/de/design_hierarchy.md)
      * [Smart Package](../../pypde/docs/reference/de/package.md)
      * [Geometry](../../pypde/docs/reference/de/geometry.md)
      * [Collections](../../pypde/docs/reference/de/collections.md)
      * [Printer](../../pypde/docs/reference/de/printer.md)
    - [keysight.ads.de.ael](../../pypde/docs/reference/de/ael.md)
    - [keysight.ads.de.app](../../pypde/docs/reference/de/app/index.md)
      * [Application](../../pypde/docs/reference/de/app/application.md)
      * [Actions and Menus](../../pypde/docs/reference/de/app/action.md)
      * [Addons](../../pypde/docs/reference/de/app/addon.md)
      * [Window and Design Callbacks](../../pypde/docs/reference/de/app/callbacks.md)
      * [Windows and Widgets](../../pypde/docs/reference/de/app/window.md)
      * [Experimental](../../pypde/docs/reference/de/app/experimental.md)
    - [keysight.ads.de.app.dds](../../pypde/docs/reference/de/app/dds.md)
      * [exec\_python](../../pypde/docs/reference/de/app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../pypde/docs/reference/de/db/index.md)
      * [Models, Parameters, and Forms](../../pypde/docs/reference/de/db/parameters.md)
      * [Properties](../../pypde/docs/reference/de/db/properties.md)
      * [Preferences](../../pypde/docs/reference/de/db/preferences.md)
      * [Transaction](../../pypde/docs/reference/de/db/transaction.md)
      * [Smart Mount](../../pypde/docs/reference/de/db/smart_mount.md)
      * [Geometry](../../pypde/docs/reference/de/db/geometry.md)
      * [Teardrops](../../pypde/docs/reference/de/db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../pypde/docs/reference/de/db_dbu/index.md)
      * [DbBox](../../pypde/docs/reference/de/db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../pypde/docs/reference/de/db_uu/index.md)
      * [Database Objects](../../pypde/docs/reference/de/db_uu/database_objects.md)
      * [Iterators](../../pypde/docs/reference/de/db_uu/iterators.md)
      * [Designs](../../pypde/docs/reference/de/db_uu/design.md)
      * [Teardrops](../../pypde/docs/reference/de/db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../../pypde/docs/reference/de/experimental/index.md)
      * [CDF](../../pypde/docs/reference/de/experimental/cdf.md)
      * [Design Commands](../../pypde/docs/reference/de/experimental/commands.md)
      * [Component Handles](../../pypde/docs/reference/de/experimental/handles.md)
      * [Netlist Utilities](../../pypde/docs/reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../pypde/docs/reference/de/experimental/polygon_utils.md)
      * [xxPro View](../../pypde/docs/reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../pypde/docs/reference/de/experimental/symbol.md)
      * [Text Maker](../../pypde/docs/reference/de/experimental/text_maker.md)
      * [Notebook](../../pypde/docs/reference/de/experimental/notebook.md)
      * [Layer/Purpose Pairs](../../pypde/docs/reference/de/experimental/lpp.md)
    - [keysight.ads.de.tech](../../pypde/docs/reference/de/tech/index.md)
      * [Technology](../../pypde/docs/reference/de/tech/tech.md)
      * [Layers](../../pypde/docs/reference/de/tech/layers.md)
      * [Line Items](../../pypde/docs/reference/de/tech/line_items.md)
      * [Padstacks](../../pypde/docs/reference/de/tech/pads.md)
      * [Rules](../../pypde/docs/reference/de/tech/rule.md)
  + [Substrate](../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../examples.md)
  + [Design Environment](../../pypde/docs/examples/index.md)
    - [Workspace Creation](../../pypde/docs/examples/workspace/ex_workspace.md)
    - [Design Creation](../../pypde/docs/examples/design_creation/index.md)
      * [Create Layout](../../pypde/docs/examples/design_creation/ex_create_layout.md)
      * [Create Schematic](../../pypde/docs/examples/design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../../pypde/docs/examples/design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../../pypde/docs/examples/design_elements/index.md)
      * [Placing Text](../../pypde/docs/examples/design_elements/ex_place_text.md)
      * [Moving Objects](../../pypde/docs/examples/design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../../pypde/docs/examples/design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../../pypde/docs/examples/design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../../pypde/docs/examples/design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../../pypde/docs/examples/design_elements/ex_plane_editing.md)
    - [Parameters](../../pypde/docs/examples/parameters/index.md)
      * [Interoperable Component Parameters](../../pypde/docs/examples/parameters/ex_cdf.md)
      * [Working with VAR](../../pypde/docs/examples/parameters/ex_working_with_var.md)
      * [Component Parameters](../../pypde/docs/examples/parameters/ex_parameters.md)
      * [Creating an Item Definition](../../pypde/docs/examples/parameters/ex_itemdef.md)
      * [Model Definition Properties](../../pypde/docs/examples/parameters/ex_model.md)
      * [Creating a Text Form](../../pypde/docs/examples/parameters/ex_text_form.md)
      * [Properties](../../pypde/docs/examples/parameters/ex_properties.md)
    - [Technology](../../pypde/docs/examples/technology/index.md)
      * [Padstacks and Vias](../../pypde/docs/examples/technology/ex_padstack.md)
      * [Nested Technology](../../pypde/docs/examples/technology/ex_nested.md)
      * [Rules](../../pypde/docs/examples/technology/ex_rules.md)
    - [Translators](../../pypde/docs/examples/translators/index.md)
      * [DXF Import and Export](../../pypde/docs/examples/translators/ex_translate_dxf.md)
      * [Gerber Export](../../pypde/docs/examples/translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../../pypde/docs/examples/translators/ex_translate_gds.md)
    - [UI](../../pypde/docs/examples/ui/index.md)
      * [Creating Custom Menus Using an Addon](../../pypde/docs/examples/ui/ex_menu_addon.md)
      * [PySide](../../pypde/docs/examples/ui/ex_pyside.md)
    - [Utility](../../pypde/docs/examples/utility/index.md)
      * [Calling Between AEL and Python](../../pypde/docs/examples/utility/ex_calling_ael_and_python.md)
      * [Smart Package](../../pypde/docs/examples/utility/ex_smart_pkg.md)
      * [XML RPC](../../pypde/docs/examples/utility/ex_xml_rpc.md)
  + [Substrate](../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../genindex.md)

# Execute Python Scripts in Different Contexts[](#execute-python-scripts-in-different-contexts "Link to this heading")

When developing Python scripts for ADS (or DDS\*), it is important to consider the execution context the script runs in,
as the set of available functionality differs depending on whether or not the script executes within the context
of the application.

When executing scripts from within the ADS application, whether from the Python console, an addon, or menu action, etc.,
application level functionality is available, you can display a message box or access a window, for example.
Scripts executing outside the application context do not have access to ADS application functionality, such as user interface
and interprocess communication. This includes, but is not limited to, the [`keysight.ads.de.app`](../../pypde/docs/reference/de/app/index.md#module-keysight.ads.de.app "keysight.ads.de.app") package and AEL application
functions that interact with the user interface or access the simulator in some manner. Simulation in automation mode can make
use of the `keysight.edatoolbox` package, which is beyond the scope of this document.

To determine if the executing context is the ADS application, the script can check [`keysight.ads.de.is_pde_app()`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.is_pde_app.md#keysight.ads.de.is_pde_app "keysight.ads.de.is_pde_app").

*\*Note: DDS is the Data Display application, which is a separate application that can be launched from the command line or
from within ADS. Both ADS and DDS have their own embedded Python interpreter and are separate execution contexts.*

## Automation[](#automation "Link to this heading")

‘Automation’ is a term used to describe when the execution context of an extension module is not the owning application.
Importing the [`keysight.ads.de`](../../pypde/docs/reference/de/index.md#module-keysight.ads.de "keysight.ads.de") or `keysight.ads.dds` packages directly into a Python process is considered
ADS or DDS automation, respectively. Additionally, importing the `keysight.ads.dds` package from within the
ADS application is considered DDS automation, just as importing [`keysight.ads.de`](../../pypde/docs/reference/de/index.md#module-keysight.ads.de "keysight.ads.de") from within the DDS application
is considered ADS automation.

When running in an automation mode (ADS, DDS, or both), scripts are not able to access the associated application’s user
interface. For example, when running scripts inside ADS, the DDS user interface APIs are not available, and vice versa.
Examples of UI functionality include, but are not limited to: windows, message boxes, palettes, menus, and toolbars.

To determine if a particular execution context is automation, the script can check the return value of the appropriate
`is_app` function, for ADS, this is [`keysight.ads.de.is_pde_app()`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.is_pde_app.md#keysight.ads.de.is_pde_app "keysight.ads.de.is_pde_app"), and for DDS, this is `keysight.ads.dds.is_dds_app()`.

*Note: The* [`keysight.ads.de.running_automation()`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.running_automation.md#keysight.ads.de.running_automation "keysight.ads.de.running_automation") *and* `keysight.ads.dds.running_automation()` *functions are misnamed and
those names will be deprecated in a future release. Both functions mean the same thing, that the script is not executing in
either the ADS or DDS application context, but a Python application context.*

The following examples demonstrate the different results of the `is_pde_app`, `is_dds_app`, and `running_automation`
functions when executed from different contexts:

From within the ADS application:

![../../_images/ADS_app_automation_modes.png](../../_images/ADS_app_automation_modes.png)

From within the DDS application:

![../../_images/DDS_app_automation_modes.png](../../_images/DDS_app_automation_modes.png)

From the command line:

![../../_images/Automation_mode.png](../../_images/Automation_mode.png)

On this page

[Previous

Enable Python Support For Your Library](python_integration.md)
[Next

Export Workspace and Design Objects to Python](exporter.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top