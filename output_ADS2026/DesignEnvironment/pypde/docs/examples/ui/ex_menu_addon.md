<!-- 来源: pypde\docs\examples\ui\ex_menu_addon.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Examples](../../../../examples.md)
* [Design Environment](../index.md)
* [UI](index.md)
* Creating Custom Menus Using an Addon

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

* [Introduction](../../../../pydocs/intro/index.md)
* [How-To](../../../../pydocs/howto/index.md)
  + [Use Python in the ADS Application](../../../../pydocs/howto/embedded.md)
  + [Set Up a Python Virtual Environment](../../../../pydocs/howto/venv.md)
  + [Set Up Visual Studio Code for Development](../../../../pydocs/howto/vscode.md)
  + [Use Pytest](../../../../pydocs/howto/pytest.md)
  + [Enable Python Support For Your Library](../../../../pydocs/howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../../../../pydocs/howto/execution.md)
  + [Export Workspace and Design Objects to Python](../../../../pydocs/howto/exporter.md)
  + [Record Actions in ADS as Python Code](../../../../pydocs/howto/recorder.md)
  + [Develop a Python Pcell in ADS](../../../../pydocs/howto/pcell.md)
* [ADS Concepts](../../../../pydocs/concepts/index.md)
  + [Workspace Elements](../../../../pydocs/concepts/workspace_elements.md)
  + [Connectivity Objects](../../../../pydocs/concepts/connectivity.md)
* [Reference](../../../../reference.md)
  + [Deprecated APIs](../../../../pydocs/py/_generated/deprecations.md)
  + [Design Environment](../../reference/index.md)
    - [keysight.ads.de](../../reference/de/index.md)
      * [ADS Application Environment](../../reference/de/ads_environment.md)
      * [ADS Workspace Components](../../reference/de/workspace_components.md)
      * [Design Hierarchy](../../reference/de/design_hierarchy.md)
      * [Smart Package](../../reference/de/package.md)
      * [Geometry](../../reference/de/geometry.md)
      * [Collections](../../reference/de/collections.md)
      * [Printer](../../reference/de/printer.md)
    - [keysight.ads.de.ael](../../reference/de/ael.md)
    - [keysight.ads.de.app](../../reference/de/app/index.md)
      * [Application](../../reference/de/app/application.md)
      * [Actions and Menus](../../reference/de/app/action.md)
      * [Addons](../../reference/de/app/addon.md)
      * [Window and Design Callbacks](../../reference/de/app/callbacks.md)
      * [Windows and Widgets](../../reference/de/app/window.md)
      * [Experimental](../../reference/de/app/experimental.md)
    - [keysight.ads.de.app.dds](../../reference/de/app/dds.md)
      * [exec\_python](../../reference/de/app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../reference/de/db/index.md)
      * [Models, Parameters, and Forms](../../reference/de/db/parameters.md)
      * [Properties](../../reference/de/db/properties.md)
      * [Preferences](../../reference/de/db/preferences.md)
      * [Transaction](../../reference/de/db/transaction.md)
      * [Smart Mount](../../reference/de/db/smart_mount.md)
      * [Geometry](../../reference/de/db/geometry.md)
      * [Teardrops](../../reference/de/db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../reference/de/db_dbu/index.md)
      * [DbBox](../../reference/de/db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../reference/de/db_uu/index.md)
      * [Database Objects](../../reference/de/db_uu/database_objects.md)
      * [Iterators](../../reference/de/db_uu/iterators.md)
      * [Designs](../../reference/de/db_uu/design.md)
      * [Teardrops](../../reference/de/db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../../reference/de/experimental/index.md)
      * [CDF](../../reference/de/experimental/cdf.md)
      * [Design Commands](../../reference/de/experimental/commands.md)
      * [Component Handles](../../reference/de/experimental/handles.md)
      * [Netlist Utilities](../../reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../reference/de/experimental/polygon_utils.md)
      * [xxPro View](../../reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../reference/de/experimental/symbol.md)
      * [Text Maker](../../reference/de/experimental/text_maker.md)
      * [Notebook](../../reference/de/experimental/notebook.md)
      * [Layer/Purpose Pairs](../../reference/de/experimental/lpp.md)
    - [keysight.ads.de.tech](../../reference/de/tech/index.md)
      * [Technology](../../reference/de/tech/tech.md)
      * [Layers](../../reference/de/tech/layers.md)
      * [Line Items](../../reference/de/tech/line_items.md)
      * [Padstacks](../../reference/de/tech/pads.md)
      * [Rules](../../reference/de/tech/rule.md)
  + [Substrate](../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../../../examples.md)
  + [Design Environment](../index.md)
    - [Workspace Creation](../workspace/ex_workspace.md)
    - [Design Creation](../design_creation/index.md)
      * [Create Layout](../design_creation/ex_create_layout.md)
      * [Create Schematic](../design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../design_elements/index.md)
      * [Placing Text](../design_elements/ex_place_text.md)
      * [Moving Objects](../design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../design_elements/ex_plane_editing.md)
    - [Parameters](../parameters/index.md)
      * [Interoperable Component Parameters](../parameters/ex_cdf.md)
      * [Working with VAR](../parameters/ex_working_with_var.md)
      * [Component Parameters](../parameters/ex_parameters.md)
      * [Creating an Item Definition](../parameters/ex_itemdef.md)
      * [Model Definition Properties](../parameters/ex_model.md)
      * [Creating a Text Form](../parameters/ex_text_form.md)
      * [Properties](../parameters/ex_properties.md)
    - [Technology](../technology/index.md)
      * [Padstacks and Vias](../technology/ex_padstack.md)
      * [Nested Technology](../technology/ex_nested.md)
      * [Rules](../technology/ex_rules.md)
    - [Translators](../translators/index.md)
      * [DXF Import and Export](../translators/ex_translate_dxf.md)
      * [Gerber Export](../translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../translators/ex_translate_gds.md)
    - [UI](index.md)
      * Creating Custom Menus Using an Addon
      * [PySide](ex_pyside.md)
    - [Utility](../utility/index.md)
      * [Calling Between AEL and Python](../utility/ex_calling_ael_and_python.md)
      * [Smart Package](../utility/ex_smart_pkg.md)
      * [XML RPC](../utility/ex_xml_rpc.md)
  + [Substrate](../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../../../genindex.md)

# Creating Custom Menus Using an Addon[](#creating-custom-menus-using-an-addon "Link to this heading")

Addons in ADS may be implemented in Python and enabled using the App Manager in the Tools menu of ADS.

![../../../../_images/addons_app_manager.png](../../../../_images/addons_app_manager.png)

To select an addon that is written in Python, change the file type filter to show Python files and navigate to your addon package:

![../../../../_images/addons_file_type_selector.png](../../../../_images/addons_file_type_selector.png)

The following example demonstrates how to create custom menus using an addon implemented in Python.

```
# Copyright Keysight Technologies 2024 - 2024
"""Addon example that will generate menus based on window type."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from keysight.ads.de.app import Action, Addon, Window, WindowDefinition

def setup_addon(addon: "Addon") -> None:
    ...
    """This is the setup function for the Addon."""

    # Implementation of this method is optional but if you do, DO NOT invoke UI from this function!

def shutdown_addon(addon: "Addon") -> None:
    ...
    """This is the shutdown function for the Addon."""

    # Implementation of this method is optional but if you do, DO NOT invoke UI from this function!

    # Menus and Actions that are generated inside the generate_menu function do not need
    # to be explicitly removed, they will be automatically removed when the Addon is disabled
    # or unloaded (after this function returns).

    # Should you wish to remove menus yourself, you can do so using the Menu.remove_ API's.

def identify() -> None:
    print("My Menu Addon.")

def generate_menu(addon: "Addon", win_def: "WindowDefinition") -> None:
    """Menu generator for the Addon."""
    import keysight.ads.de.app as app

    win_type = win_def.window_type
    # We'll add menus to the main window, layout window, and schematic window
    if (
        win_type == app.WindowType.MAIN_WINDOW
        or win_type == app.WindowType.LAYOUT_WINDOW
        or win_type == app.WindowType.SCHEMATIC_WINDOW
    ):
        # Retrieve the window menu bar and add a new menu and actions under the Tools menu
        menu_bar = win_def.menubar
        assert menu_bar
        tools_menu = menu_bar.find_menu("Tools")
        if tools_menu:

            def add_separator_to_tools_menu() -> None:
                separator = app.Separator()
                tools_menu.add_action(separator)

            # We need to add the menu just once per WindowType we're interested in
            if win_type == app.WindowType.MAIN_WINDOW:
                my_addon_menu = tools_menu.find_menu("My Python Addon Menu")
                # Add a new menu and an action to the Tools menu on the Main Window
                if my_addon_menu is None:
                    add_separator_to_tools_menu()
                    my_addon_menu = app.Menu("My Python Addon Menu")
                    tools_menu.add_menu(my_addon_menu)
                    main_menu_action = app.Action("My Main Menu Action", my_addon_main_menu_handler, None)
                    # The shortcut for the action; functional and displays alongside the action title
                    main_menu_action.shortcut = "Ctrl+O"
                    my_addon_menu.add_action(main_menu_action)

            # For layout and schematic windows, we'll add an action directly to the Tools menu
            elif win_type == app.WindowType.LAYOUT_WINDOW:
                if tools_menu.find_action("My Layout Action") is None:
                    add_separator_to_tools_menu()
                    tools_menu.add_action(app.Action("My Layout Action", my_addon_shared_menu_handler, None))
            elif win_type == app.WindowType.SCHEMATIC_WINDOW:
                if tools_menu.find_action("My Schematic Action") is None:
                    add_separator_to_tools_menu()
                    tools_menu.add_action(app.Action("My Schematic Action", my_addon_shared_menu_handler, None))
            else:
                # not possible
                ...

def my_addon_main_menu_handler(action: "Action", window: "Window") -> None:
    from keysight.ads import ael

    # Display a message box when the menu action is triggered
    ael.call.de_info(f"Shortcut ({action.shortcut}) from {action.name} in {str(window.window_type)}")

def my_addon_shared_menu_handler(action: "Action", window: "Window") -> None:
    from keysight.ads import ael
    from keysight.ads.de import app

    if action.name == "My Layout Action":
        assert window.window_type == app.WindowType.LAYOUT_WINDOW
        ael.call.de_info("Layout window type callback handler called.")
    elif action.name == "My Schematic Action":
        assert window.window_type == app.WindowType.SCHEMATIC_WINDOW
        ael.call.de_info("Schematic window type callback handler called.")
    else:
        # not possible
        ...
```

The code above created menus listed in the Tools menu of ADS, as shown below:

![../../../../_images/addons_menus.png](../../../../_images/addons_menus.png)

While the entirety of your addon does not need to be implemented in \_\_init\_\_.py, its presence is necessary to define
a namespace for your module and allows for the export of symbols accessible by other Python modules.

Access to API’s in your module can be done like:

```
# This code snippet will call the identify() method defined in the menus module above
from keysight.ads.de import app
my_addon = app.import_addon_as_module("menus")
my_addon.identify()
```

![../../../../_images/addons_apis_accessible.png](../../../../_images/addons_apis_accessible.png)

On this page

[Previous

UI](index.md)
[Next

PySide](ex_pyside.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top