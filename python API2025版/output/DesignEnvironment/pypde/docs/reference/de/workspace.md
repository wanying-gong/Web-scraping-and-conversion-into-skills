<!-- 来源: pypde\docs\reference\de\workspace.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Design](../../index.md)
* [Reference](../index.md)
* [keysight.ads.de](index.md)
* Workspace

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

* [Introduction](../../../../pydocs/intro/index.md)
  + [Licensing](../../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../../pydocs/intro/extension.md)
* [Concepts](../../../../pydocs/concepts/index.md)
  + [Terminology](../../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../../pydocs/concepts/execution.md)
* [How-To](../../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../../pydocs/howto/pytest.md)

* [Design](../../index.md)
  + [Reference](../index.md)
    - [keysight.ads.de](index.md)
      * Workspace
      * [Library](library.md)
      * [Cell](cell.md)
      * [View](view.md)
      * [CellviewRef](cellviewref.md)
      * [DesignHierarchy](design_hierarchy.md)
      * [DMData](dmdata.md)
      * [ItemInfo](item_info.md)
      * [Points](points.md)
      * [Collections](collections.md)
    - [keysight.ads.de.ael](ael.md)
    - [keysight.ads.de.app](app/index.md)
      * [Actions and Menus](app/action.md)
      * [Addons](app/addon.md)
      * [Callbacks](app/callbacks.md)
      * [Windows and Widgets](app/window.md)
    - [keysight.ads.de.db](db/index.md)
      * [Callbacks](db/callbacks.md)
      * [Enumerated Types](db/enums.md)
      * [Parameter Forms](db/forms.md)
      * [GenPolyline](db/genpolyline.md)
      * [Model Definition](db/model_def.md)
      * [Parameters](db/parameters.md)
      * [Properties](db/properties.md)
      * [Transaction](db/transaction.md)
    - [keysight.ads.de.db\_dbu](db_dbu/index.md)
    - [keysight.ads.de.db\_uu](db_uu/index.md)
      * [Design Elements](db_uu/db_uu.md)
      * [LayerId](db_uu/layer_id.md)
      * [LineTypeInfo](db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](experimental/index.md)
      * [CDF](experimental/cdf/index.md)
      * [Commands](experimental/commands.md)
      * [Handles](experimental/handles.md)
      * [Netlist Utilities](experimental/netlist_helper.md)
      * [Polygon Utilities](experimental/polygon_utils.md)
      * [Preferences](experimental/preferences.md)
      * [xxPro View](experimental/pro_view.md)
      * [Symbol Generator](experimental/symbol.md)
      * [Text Maker](experimental/text_maker.md)
    - [keysight.ads.de.tech](tech/index.md)
      * [Tech](tech/tech.md)
      * [Padstacks](tech/pads/pads.md)
      * [Via Rules](tech/rule/rule.md)
      * [Nested Technology](tech/nested/nested.md)
    - [keysight.ads.de.app.dds](app/dds.md)
  + [Examples](../../examples/index.md)
    - [Calling Between AEL and Python](../../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../examples/ex_create_layout.md)
    - [Create Schematic](../../examples/ex_create_schematic.md)
    - [Create Workspace](../../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../examples/ex_cdf.md)
    - [Component Parameters](../../examples/ex_parameters.md)
    - [Creating an Item Definition](../../examples/ex_itemdef.md)
    - [Model Definition Properties](../../examples/ex_model.md)
    - [Adding Instances to a Design](../../examples/ex_lpf.md)
    - [Properties](../../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../examples/ex_padstack.md)
    - [Nested Technology](../../examples/ex_nested.md)
    - [Rules](../../examples/ex_rules.md)
    - [Placing Text](../../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../examples/ex_polygon.md)
    - [PySide2](../../examples/ex_pyside.md)
    - [Traversing Hierarchy](../../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../examples/ex_working_with_var.md)
    - [XML RPC](../../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../examples/ex_translate_gds.md)
* [Technology](../../../../pysubst/docs/index.md)
  + [Reference](../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Workspace[](#workspace "Link to this heading")

*class* keysight.ads.de.Workspace[](#keysight.ads.de.Workspace "Link to this definition")
:   \_\_init\_\_(*path: str | PathLike*)[](#keysight.ads.de.Workspace.__init__ "Link to this definition")

    add\_library(*library\_name: str*, *library\_path: Path | str*, *mode: [LibraryMode](library.md#keysight.ads.de.LibraryMode "keysight.ads.de._core.library.LibraryMode") = LibraryMode.READ\_ONLY*) → None[](#keysight.ads.de.Workspace.add_library "Link to this definition")

    close() → None[](#keysight.ads.de.Workspace.close "Link to this definition")

    close\_library(*library: str | [Library](library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*) → None[](#keysight.ads.de.Workspace.close_library "Link to this definition")

    design(*name: CellviewRefLike*, *mode: [DesignMode](db/enums.md#keysight.ads.de.db.DesignMode "keysight.ads.de.db._design_mode.DesignMode") = DesignMode.READ\_ONLY*) → [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")[](#keysight.ads.de.Workspace.design "Link to this definition")

    get\_layout\_preference(*index: [WorkspacePreference](experimental/preferences.md#keysight.ads.de.experimental.preferences.WorkspacePreference "keysight.ads.de.experimental.preferences.WorkspacePreference")*) → PreferenceValueType[](#keysight.ads.de.Workspace.get_layout_preference "Link to this definition")
    :   Use `with de.experimental.preferences():` to work with preferences. The API is subject to change.

    get\_schematic\_preference(*index: [WorkspacePreference](experimental/preferences.md#keysight.ads.de.experimental.preferences.WorkspacePreference "keysight.ads.de.experimental.preferences.WorkspacePreference")*) → PreferenceValueType[](#keysight.ads.de.Workspace.get_schematic_preference "Link to this definition")
    :   Use `with de.experimental.preferences():` to work with preferences. The API is subject to change.

    *property* is\_open*: bool*[](#keysight.ads.de.Workspace.is_open "Link to this definition")

    *property* lib\_defs\_file*: Path*[](#keysight.ads.de.Workspace.lib_defs_file "Link to this definition")

    *property* libraries*: NamedItemCollectionAbc[[Library](library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")]*[](#keysight.ads.de.Workspace.libraries "Link to this definition")
    :   All open libraries, including read-only libraries.

        A library may be accessed by using the [] operator, indexed by the library name.

        See [`writable_libraries()`](#keysight.ads.de.Workspace.writable_libraries "keysight.ads.de.Workspace.writable_libraries") for a narrower collection.

    *property* library\_names*: set[str]*[](#keysight.ads.de.Workspace.library_names "Link to this definition")

    open(*\**, *force: bool = False*) → None[](#keysight.ads.de.Workspace.open "Link to this definition")
    :   Open an ADS workspace.

        This object’s path property is updated to show the workspace path used by ADS.

        forcebool [optional, default = False]
        :   If False, raises a RuntimeError if a workspace is already open.
            If True, will first close any open workspace, losing unsaved changes.

    open\_library(*lib\_name: str*, *lib\_path: str | PathLike | None = None*, *mode: [LibraryMode](library.md#keysight.ads.de.LibraryMode "keysight.ads.de._core.library.LibraryMode") = LibraryMode.READ\_ONLY*) → [Library](library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")[](#keysight.ads.de.Workspace.open_library "Link to this definition")

    *property* path*: Path*[](#keysight.ads.de.Workspace.path "Link to this definition")

    remove\_library(*library\_name: str*, *library\_path: Path | str*) → None[](#keysight.ads.de.Workspace.remove_library "Link to this definition")

    set\_layout\_preference(*index: [WorkspacePreference](experimental/preferences.md#keysight.ads.de.experimental.preferences.WorkspacePreference "keysight.ads.de.experimental.preferences.WorkspacePreference")*, *value: PreferenceValueType*) → None[](#keysight.ads.de.Workspace.set_layout_preference "Link to this definition")
    :   Use `with de.experimental.preferences():` to work with preferences. The API is subject to change.

    set\_schematic\_preference(*index: [WorkspacePreference](experimental/preferences.md#keysight.ads.de.experimental.preferences.WorkspacePreference "keysight.ads.de.experimental.preferences.WorkspacePreference")*, *value: PreferenceValueType*) → None[](#keysight.ads.de.Workspace.set_schematic_preference "Link to this definition")
    :   Use `with de.experimental.preferences():` to work with preferences. The API is subject to change.

    *property* writable\_libraries*: NamedItemCollectionAbc[[Library](library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")]*[](#keysight.ads.de.Workspace.writable_libraries "Link to this definition")
    :   The libraries that are open for modification.

        A library may be accessed by using the [] operator, indexed by the library name.

        See [`libraries()`](#keysight.ads.de.Workspace.libraries "keysight.ads.de.Workspace.libraries") for a broader collection.

    *property* writable\_library\_names*: set[str]*[](#keysight.ads.de.Workspace.writable_library_names "Link to this definition")

On this page

[Previous

keysight.ads.de](index.md)
[Next

Library](library.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top