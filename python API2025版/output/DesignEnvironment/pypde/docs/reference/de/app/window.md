<!-- 来源: pypde\docs\reference\de\app\window.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.app](index.md)
* Windows and Widgets

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
      * [Actions and Menus](action.md)
      * [Addons](addon.md)
      * [Callbacks](callbacks.md)
      * Windows and Widgets
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

# Windows and Widgets[](#windows-and-widgets "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.app.Button[](#keysight.ads.de.app.Button "Link to this definition")
:   Bases: [`Widget`](#keysight.ads.de.app.Widget "keysight.ads.de.app.widget.Widget")

    A button.

    \_\_init\_\_(*label: str*, *callback: Callable[[], None]*, *parent: [Widget](#keysight.ads.de.app.Widget "keysight.ads.de.app.widget.Widget") | None = None*, *name: str | None = None*)[](#keysight.ads.de.app.Button.__init__ "Link to this definition")
    :   Create a button.

        Parameters:
        :   * **label** (*str*) – The label to display on the button
            * **callback** (*function*) – A function to be called when the button is pressed
              function()
            * **parent** ([*Widget*](#keysight.ads.de.app.Widget "keysight.ads.de.app.Widget")) – The parent widget
            * **name** (*str*) – The name of the button, to later recall it

        Example

        ```
        >>> btn = Button('Press Me!', lambda:print('Button pressed'))
        ```

    *property* is\_managed*: bool*[](#keysight.ads.de.app.Button.is_managed "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.app.Button.name "Link to this definition")

*class* keysight.ads.de.app.Dialog[](#keysight.ads.de.app.Dialog "Link to this definition")
:   A dialog.

    \_\_init\_\_(*parent\_window: [Window](#keysight.ads.de.app.Window "keysight.ads.de.app.window.Window") | None = None*, *name: str | None = None*)[](#keysight.ads.de.app.Dialog.__init__ "Link to this definition")
    :   Create a dialog.

        Parameters:
        :   * **parent\_window** ([*Window*](#keysight.ads.de.app.Window "keysight.ads.de.app.Window")) – The parent window.
            * **name** (*str*) – The name of the dialog, to later recall it

        Example

        ```
        >>> dlg = Dialog(ui.main_window())
        ... dlg.manage()
        ```

        ```
        >>> dlg = Dialog()
        ... dlg.manage()
        ```

    add\_item(*item: [Widget](#keysight.ads.de.app.Widget "keysight.ads.de.app.widget.Widget")*) → None[](#keysight.ads.de.app.Dialog.add_item "Link to this definition")

    *property* is\_managed*: bool*[](#keysight.ads.de.app.Dialog.is_managed "Link to this definition")

    manage() → None[](#keysight.ads.de.app.Dialog.manage "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.app.Dialog.name "Link to this definition")

    unmanage() → None[](#keysight.ads.de.app.Dialog.unmanage "Link to this definition")

*class* keysight.ads.de.app.Widget[](#keysight.ads.de.app.Widget "Link to this definition")

*class* keysight.ads.de.app.Window[](#keysight.ads.de.app.Window "Link to this definition")
:   is\_valid() → bool[](#keysight.ads.de.app.Window.is_valid "Link to this definition")

    *property* menubar*: [MenuBar](action.md#keysight.ads.de.app.MenuBar "keysight.ads.de.app.menu.MenuBar")*[](#keysight.ads.de.app.Window.menubar "Link to this definition")

    show() → None[](#keysight.ads.de.app.Window.show "Link to this definition")

    *property* title*: str*[](#keysight.ads.de.app.Window.title "Link to this definition")

    *property* window\_definition*: [WindowDefinition](#keysight.ads.de.app.WindowDefinition "keysight.ads.de.app.window.WindowDefinition")*[](#keysight.ads.de.app.Window.window_definition "Link to this definition")

    *property* window\_type*: [WindowType](#keysight.ads.de.app.WindowType "keysight.ads.de.app.window.WindowType")*[](#keysight.ads.de.app.Window.window_type "Link to this definition")

*class* keysight.ads.de.app.WindowDefinition[](#keysight.ads.de.app.WindowDefinition "Link to this definition")
:   *property* menubar*: [MenuBar](action.md#keysight.ads.de.app.MenuBar "keysight.ads.de.app.menu.MenuBar") | None*[](#keysight.ads.de.app.WindowDefinition.menubar "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.app.WindowDefinition.name "Link to this definition")

    register\_top\_level\_action(*action: [Action](action.md#keysight.ads.de.app.Action "keysight.ads.de.app.Action")*) → None[](#keysight.ads.de.app.WindowDefinition.register_top_level_action "Link to this definition")

    *property* window\_type*: [WindowType](#keysight.ads.de.app.WindowType "keysight.ads.de.app.window.WindowType")*[](#keysight.ads.de.app.WindowDefinition.window_type "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.app.WindowType[](#keysight.ads.de.app.WindowType "Link to this definition")
:   Bases: `IntEnum`

    MAIN\_WINDOW *= 0*[](#keysight.ads.de.app.WindowType.MAIN_WINDOW "Link to this definition")

    SCHEMATIC\_WINDOW *= 1*[](#keysight.ads.de.app.WindowType.SCHEMATIC_WINDOW "Link to this definition")

    LAYOUT\_WINDOW *= 2*[](#keysight.ads.de.app.WindowType.LAYOUT_WINDOW "Link to this definition")

    SYMBOL\_WINDOW *= 3*[](#keysight.ads.de.app.WindowType.SYMBOL_WINDOW "Link to this definition")

    BROWSER\_WINDOW *= 4*[](#keysight.ads.de.app.WindowType.BROWSER_WINDOW "Link to this definition")

    SUBSTRATE\_WINDOW *= 5*[](#keysight.ads.de.app.WindowType.SUBSTRATE_WINDOW "Link to this definition")

    NOTEBOOK\_WINDOW *= 6*[](#keysight.ads.de.app.WindowType.NOTEBOOK_WINDOW "Link to this definition")

    CONFIG\_VIEW\_WINDOW *= 7*[](#keysight.ads.de.app.WindowType.CONFIG_VIEW_WINDOW "Link to this definition")

    \_\_new\_\_(*value*)[](#keysight.ads.de.app.WindowType.__new__ "Link to this definition")

## Functions[](#functions "Link to this heading")

> keysight.ads.de.app.current\_window() → [Window](#keysight.ads.de.app.Window "keysight.ads.de.app.window.Window") | None[](#keysight.ads.de.app.current_window "Link to this definition")
>
> keysight.ads.de.app.current\_window\_definition() → [WindowDefinition](#keysight.ads.de.app.WindowDefinition "keysight.ads.de.app.window.WindowDefinition") | None[](#keysight.ads.de.app.current_window_definition "Link to this definition")
>
> keysight.ads.de.app.find\_windows\_by\_type(*win\_type: int*) → list[[Window](#keysight.ads.de.app.Window "keysight.ads.de.app.window.Window")][](#keysight.ads.de.app.find_windows_by_type "Link to this definition")
>
> keysight.ads.de.app.main\_window() → [Window](#keysight.ads.de.app.Window "keysight.ads.de.app.window.Window")[](#keysight.ads.de.app.main_window "Link to this definition")
>
> keysight.ads.de.app.window\_definition\_by\_type(*win\_type: int*) → [WindowDefinition](#keysight.ads.de.app.WindowDefinition "keysight.ads.de.app.window.WindowDefinition") | None[](#keysight.ads.de.app.window_definition_by_type "Link to this definition")

On this page

[Previous

Callbacks](callbacks.md)
[Next

keysight.ads.de.db](../db/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top