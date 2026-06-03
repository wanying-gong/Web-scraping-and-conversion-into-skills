<!-- 来源: pypde\docs\reference\de\app\addon.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.app](index.md)
* Addons

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
      * Addons
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

On this page

[Previous

Actions and Menus](action.md)
[Next

Callbacks](callbacks.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top