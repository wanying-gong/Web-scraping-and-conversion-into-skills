<!-- 来源: pydocs\concepts\execution.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../index.md)
* [Concepts](index.md)
* Python Script Execution

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
* [Concepts](index.md)
  + [Terminology](terminology.md)
    - [Workspace Elements](workspace_elements.md)
    - [Connectivity Objects](connectivity.md)
  + [OpenAccess Integration](openaccess_integration.md)
  + Python Script Execution
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

# Python Script Execution[](#python-script-execution "Link to this heading")

When developing Python scripts for ADS (or DDS\*), it is important to consider the execution context the script runs in,
as the set of available functionality differs depending on whether or not the script executes within the context
of the application.

When executing scripts from within the ADS application, whether from the Python console, an addon, or menu action, etc.,
application level functionality is available, you can display a message box or access a window, for example.
Scripts executing outside the application context do not have access to ADS application functionality, such as user interface
and interprocess communication. This includes, but is not limited to, the [`keysight.ads.de.app`](../../pypde/docs/reference/de/app/index.md#module-keysight.ads.de.app "keysight.ads.de.app") package and AEL application
functions that interact with the user interface or access the simulator in some manner. Simulation in automation mode can make
use of the `keysight.edatoolbox` package, which is beyond the scope of this document.

To determine if the executing context is the ADS application, the script can check [`keysight.ads.de.is_pde_app()`](../../pypde/docs/reference/de/index.md#keysight.ads.de.is_pde_app "keysight.ads.de.is_pde_app").

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
`is_app` function, for ADS, this is [`keysight.ads.de.is_pde_app()`](../../pypde/docs/reference/de/index.md#keysight.ads.de.is_pde_app "keysight.ads.de.is_pde_app"), and for DDS, this is `keysight.ads.dds.is_dds_app()`.

*Note: The* [`keysight.ads.de.running_automation()`](../../pypde/docs/reference/de/index.md#keysight.ads.de.running_automation "keysight.ads.de.running_automation") *and* `keysight.ads.dds.running_automation()` *functions are misnamed and
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

OpenAccess Integration](openaccess_integration.md)
[Next

How-To](../howto/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top