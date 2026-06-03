<!-- 来源: pypde\docs\reference\de\app\callbacks.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.app](index.md)
* Callbacks

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
      * Callbacks
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

On this page

[Previous

Addons](addon.md)
[Next

Windows and Widgets](window.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top