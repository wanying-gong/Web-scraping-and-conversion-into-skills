<!-- 来源: pypde\docs\examples\ex_menu_addon.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* [Examples](index.md)
* Creating Custom Menus Using an Addon

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
  + [Reference](../reference/index.md)
    - [keysight.ads.de](../reference/de/index.md)
      * [Workspace](../reference/de/workspace.md)
      * [Library](../reference/de/library.md)
      * [Cell](../reference/de/cell.md)
      * [View](../reference/de/view.md)
      * [CellviewRef](../reference/de/cellviewref.md)
      * [DesignHierarchy](../reference/de/design_hierarchy.md)
      * [DMData](../reference/de/dmdata.md)
      * [ItemInfo](../reference/de/item_info.md)
      * [Points](../reference/de/points.md)
      * [Collections](../reference/de/collections.md)
    - [keysight.ads.de.ael](../reference/de/ael.md)
    - [keysight.ads.de.app](../reference/de/app/index.md)
      * [Actions and Menus](../reference/de/app/action.md)
      * [Addons](../reference/de/app/addon.md)
      * [Callbacks](../reference/de/app/callbacks.md)
      * [Windows and Widgets](../reference/de/app/window.md)
    - [keysight.ads.de.db](../reference/de/db/index.md)
      * [Callbacks](../reference/de/db/callbacks.md)
      * [Enumerated Types](../reference/de/db/enums.md)
      * [Parameter Forms](../reference/de/db/forms.md)
      * [GenPolyline](../reference/de/db/genpolyline.md)
      * [Model Definition](../reference/de/db/model_def.md)
      * [Parameters](../reference/de/db/parameters.md)
      * [Properties](../reference/de/db/properties.md)
      * [Transaction](../reference/de/db/transaction.md)
    - [keysight.ads.de.db\_dbu](../reference/de/db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../reference/de/db_uu/index.md)
      * [Design Elements](../reference/de/db_uu/db_uu.md)
      * [LayerId](../reference/de/db_uu/layer_id.md)
      * [LineTypeInfo](../reference/de/db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../reference/de/experimental/index.md)
      * [CDF](../reference/de/experimental/cdf/index.md)
      * [Commands](../reference/de/experimental/commands.md)
      * [Handles](../reference/de/experimental/handles.md)
      * [Netlist Utilities](../reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../reference/de/experimental/polygon_utils.md)
      * [Preferences](../reference/de/experimental/preferences.md)
      * [xxPro View](../reference/de/experimental/pro_view.md)
      * [Symbol Generator](../reference/de/experimental/symbol.md)
      * [Text Maker](../reference/de/experimental/text_maker.md)
    - [keysight.ads.de.tech](../reference/de/tech/index.md)
      * [Tech](../reference/de/tech/tech.md)
      * [Padstacks](../reference/de/tech/pads/pads.md)
      * [Via Rules](../reference/de/tech/rule/rule.md)
      * [Nested Technology](../reference/de/tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../reference/de/app/dds.md)
  + [Examples](index.md)
    - [Calling Between AEL and Python](ex_calling_ael_and_python.md)
    - [Create Layout](ex_create_layout.md)
    - [Create Schematic](ex_create_schematic.md)
    - [Create Workspace](ex_workspace.md)
    - [Create, Simulate, and Plot](ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](ex_cdf.md)
    - [Component Parameters](ex_parameters.md)
    - [Creating an Item Definition](ex_itemdef.md)
    - [Model Definition Properties](ex_model.md)
    - [Adding Instances to a Design](ex_lpf.md)
    - [Properties](ex_properties.md)
    - Creating Custom Menus Using an Addon
    - [Padstacks and Vias](ex_padstack.md)
    - [Nested Technology](ex_nested.md)
    - [Rules](ex_rules.md)
    - [Placing Text](ex_place_text.md)
    - [Paths, Traces, and Polygons](ex_polygon.md)
    - [PySide2](ex_pyside.md)
    - [Traversing Hierarchy](ex_traversing_hierarchy.md)
    - [Working with VAR](ex_working_with_var.md)
    - [XML RPC](ex_xml_rpc.md)
    - [GDSII Import and Export](ex_translate_gds.md)
* [Technology](../../../pysubst/docs/index.md)
  + [Reference](../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Creating Custom Menus Using an Addon[](#creating-custom-menus-using-an-addon "Link to this heading")

Addons in ADS may be implemented in Python and enabled using the App Manager in the Tools menu of ADS.

![../../../_images/addons_app_manager.png](../../../_images/addons_app_manager.png)

To select an addon that is written in Python, change the file type filter to show Python files and navigate to your addon package:

![../../../_images/addons_file_type_selector.png](../../../_images/addons_file_type_selector.png)

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

![../../../_images/addons_menus.png](../../../_images/addons_menus.png)

While the entirety of your addon does not need to be implemented in \_\_init\_\_.py, its presence is necessary to define
a namespace for your module and allows for the export of symbols accessible by other Python modules.

Access to API’s in your module can be done like:

```
# This code snippet will call the identify() method defined in the menus module above
from keysight.ads.de import app
my_addon = app.import_addon_as_module("menus")
my_addon.identify()
```

![../../../_images/addons_apis_accessible.png](../../../_images/addons_apis_accessible.png)

On this page

[Previous

Properties](ex_properties.md)
[Next

Padstacks and Vias](ex_padstack.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top