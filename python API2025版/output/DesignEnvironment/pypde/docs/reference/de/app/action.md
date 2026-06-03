<!-- 来源: pypde\docs\reference\de\app\action.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.app](index.md)
* Actions and Menus

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
    - [keysight.ads.de.app](index.md)
      * Actions and Menus
      * [Addons](addon.md)
      * [Callbacks](callbacks.md)
      * [Windows and Widgets](window.md)
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
    - [keysight.ads.de.tech](../tech/index.md)
      * [Tech](../tech/tech.md)
      * [Padstacks](../tech/pads/pads.md)
      * [Via Rules](../tech/rule/rule.md)
      * [Nested Technology](../tech/nested/nested.md)
    - [keysight.ads.de.app.dds](dds.md)
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

# Actions and Menus[](#actions-and-menus "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.app.Action[](#keysight.ads.de.app.Action "Link to this definition")
:   Bases: `object`

    \_\_init\_\_(*title: str*, *callback: Callable[[[Action](#keysight.ads.de.app.Action "keysight.ads.de.app.Action"), [Window](window.md#keysight.ads.de.app.Window "keysight.ads.de.app.Window")], None]*, *ui\_callback: Callable[[[Action](#keysight.ads.de.app.Action "keysight.ads.de.app.Action"), [Window](window.md#keysight.ads.de.app.Window "keysight.ads.de.app.Window")], [MenuState](#keysight.ads.de.app.MenuState "keysight.ads.de.app.MenuState")] | None = None*)[](#keysight.ads.de.app.Action.__init__ "Link to this definition")
    :   Create an action item.

        Parameters:
        :   * **title** (*str*) – The title of the action item
            * **callback** (*function*) – A function to be called when the menu/action is triggered of signature
              function(arg : Action, win : Window)
            * **ui\_callback** (*function*) – A function called to set the menu/action state
              function(arg : Action, win : Window)

        ### Example:[](#example "Link to this heading")

        ```
        >>> def my_callback(action, window_handle):
        ...     print(f'Called from {action} with {window_handle}')
        >>> menu = Action('Test', my_callback, None)
        ```

    is\_checkable() → bool[](#keysight.ads.de.app.Action.is_checkable "Link to this definition")

    is\_separator() → bool[](#keysight.ads.de.app.Action.is_separator "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.app.Action.name "Link to this definition")

    *property* original\_shortcut*: str*[](#keysight.ads.de.app.Action.original_shortcut "Link to this definition")

    *property* shortcut*: str*[](#keysight.ads.de.app.Action.shortcut "Link to this definition")

    *property* tooltip*: str*[](#keysight.ads.de.app.Action.tooltip "Link to this definition")

*class* keysight.ads.de.app.Separator[](#keysight.ads.de.app.Separator "Link to this definition")
:   Bases: [`Action`](#keysight.ads.de.app.Action "keysight.ads.de.app.action.Action")

    \_\_init\_\_()[](#keysight.ads.de.app.Separator.__init__ "Link to this definition")
    :   Create a separator.

        ### Example:[](#id1 "Link to this heading")

        ```
        >>> sep = Separator()
        ```

*class* keysight.ads.de.app.Menu[](#keysight.ads.de.app.Menu "Link to this definition")
:   Bases: [`Action`](#keysight.ads.de.app.Action "keysight.ads.de.app.action.Action")

    \_\_init\_\_(*title: str*)[](#keysight.ads.de.app.Menu.__init__ "Link to this definition")
    :   Create a menu.

        Parameters:
        :   **title** (*str*) – The title of the action item

        ### Example:[](#id2 "Link to this heading")

        ```
        >>> menu = Menu('Test')
        ```

    *property* actions*: NamedItemCollectionAbc[[Action](#keysight.ads.de.app.Action "keysight.ads.de.app.action.Action")]*[](#keysight.ads.de.app.Menu.actions "Link to this definition")

    add\_action(*new\_action: [Action](#keysight.ads.de.app.Action "keysight.ads.de.app.action.Action")*) → None[](#keysight.ads.de.app.Menu.add_action "Link to this definition")

    add\_menu(*new\_menu: [Menu](#keysight.ads.de.app.Menu "keysight.ads.de.app.menu.Menu")*) → None[](#keysight.ads.de.app.Menu.add_menu "Link to this definition")

    find\_action(*name: str*) → [Action](#keysight.ads.de.app.Action "keysight.ads.de.app.action.Action") | None[](#keysight.ads.de.app.Menu.find_action "Link to this definition")

    find\_menu(*name: str*) → [Menu](#keysight.ads.de.app.Menu "keysight.ads.de.app.menu.Menu") | None[](#keysight.ads.de.app.Menu.find_menu "Link to this definition")

    insert\_action(*new\_action: [Action](#keysight.ads.de.app.Action "keysight.ads.de.app.action.Action")*, *index: int*) → bool[](#keysight.ads.de.app.Menu.insert_action "Link to this definition")

    insert\_menu(*new\_menu: [Menu](#keysight.ads.de.app.Menu "keysight.ads.de.app.menu.Menu")*, *index: int*) → bool[](#keysight.ads.de.app.Menu.insert_menu "Link to this definition")

    *property* menus*: NamedItemCollectionAbc[[Menu](#keysight.ads.de.app.Menu "keysight.ads.de.app.menu.Menu")]*[](#keysight.ads.de.app.Menu.menus "Link to this definition")

    remove\_action(*existing\_action: [Action](#keysight.ads.de.app.Action "keysight.ads.de.app.action.Action")*) → None[](#keysight.ads.de.app.Menu.remove_action "Link to this definition")

    remove\_all\_menus() → None[](#keysight.ads.de.app.Menu.remove_all_menus "Link to this definition")

    remove\_menu(*existing\_menu: [Menu](#keysight.ads.de.app.Menu "keysight.ads.de.app.menu.Menu")*) → None[](#keysight.ads.de.app.Menu.remove_menu "Link to this definition")

*class* keysight.ads.de.app.MenuBar[](#keysight.ads.de.app.MenuBar "Link to this definition")
:   Bases: [`Menu`](#keysight.ads.de.app.Menu "keysight.ads.de.app.menu.Menu")

    A menubar, usually at the top of a window.

*class* keysight.ads.de.app.PopupMenu[](#keysight.ads.de.app.PopupMenu "Link to this definition")
:   Bases: [`Menu`](#keysight.ads.de.app.Menu "keysight.ads.de.app.menu.Menu")

    \_\_init\_\_()[](#keysight.ads.de.app.PopupMenu.__init__ "Link to this definition")
    :   Create a pop-up menu.

        ### Example:[](#id3 "Link to this heading")

        ```
        >>> menu = PopupMenu()
        >>> menu.add_action(...)
        >>> menu.add_menu(..)
        ```

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.app.MenuState[](#keysight.ads.de.app.MenuState "Link to this definition")
:   Bases: `IntFlag`

    SENSITIVE *= 1*[](#keysight.ads.de.app.MenuState.SENSITIVE "Link to this definition")

    INSENSITIVE *= 2*[](#keysight.ads.de.app.MenuState.INSENSITIVE "Link to this definition")

    TOGGLE\_ON *= 4*[](#keysight.ads.de.app.MenuState.TOGGLE_ON "Link to this definition")

    TOGGLE\_OFF *= 8*[](#keysight.ads.de.app.MenuState.TOGGLE_OFF "Link to this definition")

    \_\_new\_\_(*value*)[](#keysight.ads.de.app.MenuState.__new__ "Link to this definition")

On this page

[Previous

keysight.ads.de.app](index.md)
[Next

Addons](addon.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top