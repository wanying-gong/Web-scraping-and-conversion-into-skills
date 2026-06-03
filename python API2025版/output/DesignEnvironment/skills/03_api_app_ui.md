# App/UI API: keysight.ads.de.app
> **说明：** 应用层/UI API：Actions（动作）、Menus（菜单）、Addons（插件）、Callbacks（回调）、Windows/Widgets（窗口控件）、DDS 接口。

> **何时使用：** 当你需要创建自定义菜单、窗口、插件、或响应 UI 事件时

---

## 本文件目录

- **keysight.ads.de.app** (`pypde/docs/reference/de/app/index.md`)
- **Actions and Menus** (`pypde/docs/reference/de/app/action.md`)
- **Addons** (`pypde/docs/reference/de/app/addon.md`)
- **Callbacks** (`pypde/docs/reference/de/app/callbacks.md`)
- **Windows and Widgets** (`pypde/docs/reference/de/app/window.md`)
- **keysight.ads.de.app.dds** (`pypde/docs/reference/de/app/dds.md`)

---

<!-- === 来源: pypde/docs/reference/de/app/index.md === -->

# keysight.ads.de.app[](#module-keysight.ads.de.app "Link to this heading")

ADS Design Environment UI scripting.

## Classes[](#classes "Link to this heading")

* [Actions and Menus](action.md)
  + [Classes](action.md#classes)
  + [Enumerated Types](action.md#enumerated-types)
* [Addons](addon.md)
  + [Classes](addon.md#classes)
  + [Enumerated Types](addon.md#enumerated-types)
  + [Functions](addon.md#functions)
* [Callbacks](callbacks.md)
  + [Classes](callbacks.md#classes)
  + [Enumerated Types](callbacks.md#enumerated-types)
  + [Functions](callbacks.md#functions)
* [Windows and Widgets](window.md)
  + [Classes](window.md#classes)
  + [Enumerated Types](window.md#enumerated-types)
  + [Functions](window.md#functions)

keysight.ads.de.app.Application[](#keysight.ads.de.app.Application "Link to this definition")
:   alias of `getinstance`

## Functions[](#functions "Link to this heading")

keysight.ads.de.app.create\_layout\_palette(*lib\_name: str*, *group\_name: str*, *items: Sequence[Sequence[str]]*) → None[](#keysight.ads.de.app.create_layout_palette "Link to this definition")
:   Create a palette for the layout window.

    Parameters:
    :   * **lib\_name** (*str*) – The name of the library for this palette.
        * **group\_name** (*str*) – Name of the palette group that will appear in the list of palettes.
        * **items** (*Sequence*) – Each item is a list of the form
          [name, label, bitmap]
          name can be of the form “lib:cell:view” or “lib:cell” or “cell”

    ### Example:[](#example "Link to this heading")

    > bitmap\_path: str # has path to the bitmaps
    > items = [
    > [“demo\_mmWave\_TECHINCLUDE”, “Technology include component”, f”{bitmap\_path}/demo\_mmWave\_TECHINCLUDE\_BITMAP”],
    > [“demo\_mmWave\_Res”, “Resistor”, f”{bitmap\_path}/demo\_mmWave\_Res\_BITMAP”],
    > [“demo\_mmWave\_Cap”, “Capacitor”, f”{bitmap\_path}/demo\_mmWave\_Cap\_BITMAP”]
    > [“demo\_mmWave\_Ind”, “Inductor”, f”{bitmap\_path}/demo\_mmWave\_Ind\_BITMAP”],
    > [“demo\_mmWave\_FET”, “FET”, f”{bitmap\_path}/demo\_mmWave\_FET\_BITMAP”],
    > [“demo\_mmWave\_Tline”, “Tline”, f”{bitmap\_path}/demo\_mmWave\_Tline\_BITMAP”]
    > ]
    > app.create\_schematic\_palette(“DemoKit\_mmWave”, “MM Wave PDK”, items)

keysight.ads.de.app.create\_schematic\_palette(*lib\_name: str*, *group\_name: str*, *items: Sequence[Sequence[str]]*) → None[](#keysight.ads.de.app.create_schematic_palette "Link to this definition")
:   Create a palette for the schematic window.

    Parameters:
    :   * **lib\_name** (*str*) – The name of the library for this palette.
        * **group\_name** (*str*) – Name of the palette group that will appear in the list of palettes.
        * **items** (*Sequence*) – Each item is a list of the form
          [name, label, bitmap]
          name can be of the form “lib:cell:view” or “lib:cell” or “cell”

    ### Example:[](#id1 "Link to this heading")

    > bitmap\_path: str # has path to the bitmaps
    > items = [
    > [“demo\_mmWave\_TECHINCLUDE”, “Technology include component”, f”{bitmap\_path}/demo\_mmWave\_TECHINCLUDE\_BITMAP”],
    > [“demo\_mmWave\_Res”, “Resistor”, f”{bitmap\_path}/demo\_mmWave\_Res\_BITMAP”],
    > [“demo\_mmWave\_Cap”, “Capacitor”, f”{bitmap\_path}/demo\_mmWave\_Cap\_BITMAP”]
    > [“demo\_mmWave\_Ind”, “Inductor”, f”{bitmap\_path}/demo\_mmWave\_Ind\_BITMAP”],
    > [“demo\_mmWave\_FET”, “FET”, f”{bitmap\_path}/demo\_mmWave\_FET\_BITMAP”],
    > [“demo\_mmWave\_Tline”, “Tline”, f”{bitmap\_path}/demo\_mmWave\_Tline\_BITMAP”]
    > ]
    > app.create\_schematic\_palette(“DemoKit\_mmWave”, “MM Wave PDK”, items)

keysight.ads.de.app.exit\_application(*exit\_code: int = 0*) → None[](#keysight.ads.de.app.exit_application "Link to this definition")
:   Exit the application.


---

<!-- === 来源: pypde/docs/reference/de/app/action.md === -->

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


---

<!-- === 来源: pypde/docs/reference/de/app/addon.md === -->

# Addons[](#addons "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.app.Addon[](#keysight.ads.de.app.Addon "Link to this definition")
:   Used to extend the functionality of ADS by adding code that is loaded at startup.

    \_\_init\_\_(*name: str*, *path: str*, *enabled: bool = True*, *location: [AddonLocale](#keysight.ads.de.app.AddonLocale "keysight.ads.de.app.addon.AddonLocale") = AddonLocale.USER*) → None[](#keysight.ads.de.app.Addon.__init__ "Link to this definition")

    *property* enabled*: bool*[](#keysight.ads.de.app.Addon.enabled "Link to this definition")

    *property* location*: [AddonLocale](#keysight.ads.de.app.AddonLocale "keysight.ads.de.app.addon.AddonLocale")*[](#keysight.ads.de.app.Addon.location "Link to this definition")
    :   Specifies the location of the xml configuration file that references this Addon.

    module\_name() → str[](#keysight.ads.de.app.Addon.module_name "Link to this definition")
    :   Return the full name of the Python module for this Addon.

        Will raise an exception if this Addon does not have a Python module.

    *property* name*: str*[](#keysight.ads.de.app.Addon.name "Link to this definition")

    *property* raw\_startup\_file*: str*[](#keysight.ads.de.app.Addon.raw_startup_file "Link to this definition")
    :   The startup file for this Addon - possibly including environment variables.

    *property* root\_directory*: str*[](#keysight.ads.de.app.Addon.root_directory "Link to this definition")
    :   The directory containing the startup file.

    *property* startup\_file*: str*[](#keysight.ads.de.app.Addon.startup_file "Link to this definition")
    :   The startup file for this Addon.

    *property* sync\_location*: str*[](#keysight.ads.de.app.Addon.sync_location "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.app.AddonLocale[](#keysight.ads.de.app.AddonLocale "Link to this definition")
:   Bases: `Enum`

    Specifies the location of the xml configuration file.

    MEMORY *= <AddonLocale.MEMORY: 0>*[](#keysight.ads.de.app.AddonLocale.MEMORY "Link to this definition")
    :   The Addon is not stored in any file.

    USER *= <AddonLocale.USER: 1>*[](#keysight.ads.de.app.AddonLocale.USER "Link to this definition")
    :   The Addon location in the HOME directory for Addon’s installed by the user.

    SITE *= <AddonLocale.SITE: 2>*[](#keysight.ads.de.app.AddonLocale.SITE "Link to this definition")
    :   The Addon location for custom Addon’s installed at the user’s site.

    INSTALLATION *= <AddonLocale.INSTALLATION: 3>*[](#keysight.ads.de.app.AddonLocale.INSTALLATION "Link to this definition")
    :   The Addon location in the product directory for Addon’s installed by ADS.

## Functions[](#functions "Link to this heading")

> keysight.ads.de.app.add\_memory\_addon(*addon: [Addon](#keysight.ads.de.app.Addon "keysight.ads.de.app.addon.Addon")*) → None[](#keysight.ads.de.app.add_memory_addon "Link to this definition")
> :   Add addon to the set of memory Addons (load if enabled).
>
> keysight.ads.de.app.add\_user\_addon(*addon: [Addon](#keysight.ads.de.app.Addon "keysight.ads.de.app.addon.Addon")*) → None[](#keysight.ads.de.app.add_user_addon "Link to this definition")
> :   Add addon to the list of user Addons (load if enabled).
>
> keysight.ads.de.app.addon(*addon\_name: str*) → [Addon](#keysight.ads.de.app.Addon "keysight.ads.de.app.addon.Addon")[](#keysight.ads.de.app.addon "Link to this definition")
> :   Search all the locations for an Addon with the given name.
>
>     Raises an exception if no enabled Addon was found.
>
> keysight.ads.de.app.enable\_addon(*addon: [Addon](#keysight.ads.de.app.Addon "keysight.ads.de.app.addon.Addon")*, *enable: bool*) → [Addon](#keysight.ads.de.app.Addon "keysight.ads.de.app.addon.Addon")[](#keysight.ads.de.app.enable_addon "Link to this definition")
> :   Enable or disable the addon.
>
>     If this is overriding the state of an installation or site
>     addon, this will return a different Addon (either a new override
>     or the original whose override we just removed).
>
> keysight.ads.de.app.find\_addon(*addon\_name: str*) → [Addon](#keysight.ads.de.app.Addon "keysight.ads.de.app.addon.Addon") | None[](#keysight.ads.de.app.find_addon "Link to this definition")
> :   Search all the locations for an Addon with the given name.
>
>     Returns None if no Addon was found.
>
> keysight.ads.de.app.get\_addon\_module(*addon\_name: str*) → module[](#keysight.ads.de.app.get_addon_module "Link to this definition")
> :   get\_addon\_module is deprecated, and will be removed in the 2025 Update 2 release. Use: import\_addon\_as\_module
>
> keysight.ads.de.app.import\_addon\_as\_module(*addon\_name: str*) → module[](#keysight.ads.de.app.import_addon_as_module "Link to this definition")
> :   Import the Python module for an ADS Addon.
>
> keysight.ads.de.app.remove\_memory\_addon(*addon: [Addon](#keysight.ads.de.app.Addon "keysight.ads.de.app.addon.Addon")*) → None[](#keysight.ads.de.app.remove_memory_addon "Link to this definition")
> :   Remove addon from the set of memory Addons (unload if enabled).
>
> keysight.ads.de.app.remove\_user\_addon(*addon: [Addon](#keysight.ads.de.app.Addon "keysight.ads.de.app.addon.Addon")*) → None[](#keysight.ads.de.app.remove_user_addon "Link to this definition")
> :   Remove addon from the list of user Addons (unload if enabled).


---

<!-- === 来源: pypde/docs/reference/de/app/callbacks.md === -->

# Callbacks[](#callbacks "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.app.DesignModifiedCallback[](#keysight.ads.de.app.DesignModifiedCallback "Link to this definition")
:   Bases: `object`

    Holds a callback function to be called when a design in a window is modified.

*class* keysight.ads.de.app.DesignOpenedCallback[](#keysight.ads.de.app.DesignOpenedCallback "Link to this definition")
:   Bases: `object`

    Holds a callback function to be called when a design is opened in a window.

*class* keysight.ads.de.app.DesignWindowCallback[](#keysight.ads.de.app.DesignWindowCallback "Link to this definition")
:   Bases: `object`

    Holds a callback function to be called whenever a design-window relationship changes.

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.app.DesignWindowChange[](#keysight.ads.de.app.DesignWindowChange "Link to this definition")
:   Bases: `Enum`

    Specifies the type of change that triggered a DesignWindowCallback.

    OPENED *= <DesignWindowChange.OPENED: 0>*[](#keysight.ads.de.app.DesignWindowChange.OPENED "Link to this definition")
    :   A design was opened in a new window.

    CLOSED *= <DesignWindowChange.CLOSED: 1>*[](#keysight.ads.de.app.DesignWindowChange.CLOSED "Link to this definition")
    :   A design window closed.

    SAVED\_AS *= <DesignWindowChange.SAVED\_AS: 2>*[](#keysight.ads.de.app.DesignWindowChange.SAVED_AS "Link to this definition")
    :   The design in the window was just saved to a new name.
        The design with the old name will remain open if modified.

    PUSHED *= <DesignWindowChange.PUSHED: 3>*[](#keysight.ads.de.app.DesignWindowChange.PUSHED "Link to this definition")
    :   The design in the window has just been pushed.

    POPPED *= <DesignWindowChange.POPPED: 4>*[](#keysight.ads.de.app.DesignWindowChange.POPPED "Link to this definition")
    :   The design in the window has just been popped.

## Functions[](#functions "Link to this heading")

> keysight.ads.de.app.register\_design\_modified\_callback(*cb: Callable*) → [DesignModifiedCallback](#keysight.ads.de.app.DesignModifiedCallback "keysight.ads.de.app.callbacks.DesignModifiedCallback")[](#keysight.ads.de.app.register_design_modified_callback "Link to this definition")
>
> keysight.ads.de.app.register\_design\_opened\_callback(*cb: Callable*) → [DesignOpenedCallback](#keysight.ads.de.app.DesignOpenedCallback "keysight.ads.de.app.callbacks.DesignOpenedCallback")[](#keysight.ads.de.app.register_design_opened_callback "Link to this definition")
>
> keysight.ads.de.app.register\_design\_window\_callback(*cb: Callable*) → [DesignWindowCallback](#keysight.ads.de.app.DesignWindowCallback "keysight.ads.de.app.callbacks.DesignWindowCallback")[](#keysight.ads.de.app.register_design_window_callback "Link to this definition")
>
> keysight.ads.de.app.unregister\_design\_modified\_callback(*callback: [DesignModifiedCallback](#keysight.ads.de.app.DesignModifiedCallback "keysight.ads.de.app.callbacks.DesignModifiedCallback")*) → None[](#keysight.ads.de.app.unregister_design_modified_callback "Link to this definition")
> :   Unregister a registered design modified callback.
>
>     callback: Should be the object returned by register\_design\_modified\_callback.
>
> keysight.ads.de.app.unregister\_design\_opened\_callback(*callback: [DesignOpenedCallback](#keysight.ads.de.app.DesignOpenedCallback "keysight.ads.de.app.callbacks.DesignOpenedCallback")*) → None[](#keysight.ads.de.app.unregister_design_opened_callback "Link to this definition")
> :   Unregister a registered design opened callback.
>
>     callback: Should be the object returned by register\_design\_opened\_callback.
>
> keysight.ads.de.app.unregister\_design\_window\_callback(*callback: [DesignWindowCallback](#keysight.ads.de.app.DesignWindowCallback "keysight.ads.de.app.callbacks.DesignWindowCallback")*) → None[](#keysight.ads.de.app.unregister_design_window_callback "Link to this definition")
> :   Unregister a registered design window callback.
>
>     callback: Should be the object returned by register\_design\_window\_callback.


---

<!-- === 来源: pypde/docs/reference/de/app/window.md === -->

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


---

<!-- === 来源: pypde/docs/reference/de/app/dds.md === -->

# keysight.ads.de.app.dds[](#keysight-ads-de-app-dds "Link to this heading")

## Functions[](#functions "Link to this heading")

keysight.ads.de.app.dds.exec\_python(*statements: str*, *expr: str = ''*) → Any[](#keysight.ads.de.app.dds.exec_python "Link to this definition")
:   Execute the statements and evaluate the expression in the dds app.


---

