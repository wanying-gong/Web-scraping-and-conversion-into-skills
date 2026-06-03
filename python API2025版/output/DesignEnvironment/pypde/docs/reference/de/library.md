<!-- 来源: pypde\docs\reference\de\library.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Design](../../index.md)
* [Reference](../index.md)
* [keysight.ads.de](index.md)
* Library

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
      * [Workspace](workspace.md)
      * Library
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

# Library[](#library "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.Library[](#keysight.ads.de.Library "Link to this definition")
:   \_\_init\_\_(*name: str*) → None[](#keysight.ads.de.Library.__init__ "Link to this definition")
    :   \_\_init\_\_ is deprecated, and will be removed in the 2025 Update 2 release. Use Library.get(name).

    *property* attached\_tech\_lib\_name*: str*[](#keysight.ads.de.Library.attached_tech_lib_name "Link to this definition")

    cell(*cell\_name: str*) → [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")[](#keysight.ads.de.Library.cell "Link to this definition")

    cell\_exists(*cell\_name: str*) → bool[](#keysight.ads.de.Library.cell_exists "Link to this definition")

    *property* cells*: NamedItemCollectionAbc[[Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")]*[](#keysight.ads.de.Library.cells "Link to this definition")
    :   The collection of cells in this library.

        A cell may be accessed by using the [] operator, indexed by the cell name.

    close() → None[](#keysight.ads.de.Library.close "Link to this definition")

    *static* create(*name: str*, *path: str | Path*) → [Library](#keysight.ads.de.Library "keysight.ads.de._core.library.Library")[](#keysight.ads.de.Library.create "Link to this definition")

    create\_cell(*cell\_name: str*) → [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")[](#keysight.ads.de.Library.create_cell "Link to this definition")

    create\_layout\_tech\_from\_library(*library: [Library](#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *copy\_tech: bool = False*) → None[](#keysight.ads.de.Library.create_layout_tech_from_library "Link to this definition")

    create\_layout\_tech\_from\_pdk(*pdk: [Library](#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *copy\_tech: bool = False*) → None[](#keysight.ads.de.Library.create_layout_tech_from_pdk "Link to this definition")

    create\_layout\_tech\_std\_ads(*unit\_name: str*, *dbu\_per\_uu: int*, *copy\_tech: bool = False*) → None[](#keysight.ads.de.Library.create_layout_tech_std_ads "Link to this definition")

    create\_tech() → [Tech](tech/tech.md#keysight.ads.de.tech.Tech "keysight.ads.de.tech.Tech")[](#keysight.ads.de.Library.create_tech "Link to this definition")
    :   Create technology for this library.

    delete\_cell(*cell\_name: str*) → None[](#keysight.ads.de.Library.delete_cell "Link to this definition")

    delete\_dm\_data() → None[](#keysight.ads.de.Library.delete_dm_data "Link to this definition")

    delete\_tech() → None[](#keysight.ads.de.Library.delete_tech "Link to this definition")
    :   Delete the technology in this library.

    dm\_data(*mode: str*) → [DMData](dmdata.md#keysight.ads.de.DMData "keysight.ads.de.DMData")[](#keysight.ads.de.Library.dm_data "Link to this definition")

    *property* forms*: [NamedMutableCollectionAbc](collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[Form](db/forms.md#keysight.ads.de.db.Form "keysight.ads.de.db.Form")]*[](#keysight.ads.de.Library.forms "Link to this definition")

    *property* formsets*: [NamedMutableCollectionAbc](collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[Formset](db/forms.md#keysight.ads.de.db.Formset "keysight.ads.de.db.Formset")]*[](#keysight.ads.de.Library.formsets "Link to this definition")

    *static* get(*name: str*) → [Library](#keysight.ads.de.Library "keysight.ads.de._core.library.Library")[](#keysight.ads.de.Library.get "Link to this definition")

    get\_cell\_if\_exists(*cell\_name: str*) → [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell") | None[](#keysight.ads.de.Library.get_cell_if_exists "Link to this definition")

    get\_layout\_preference(*index: [LibSpecificPreference](experimental/preferences.md#keysight.ads.de.experimental.preferences.LibSpecificPreference "keysight.ads.de.experimental.preferences.LibSpecificPreference")*) → PreferenceValueType[](#keysight.ads.de.Library.get_layout_preference "Link to this definition")
    :   Use `with de.experimental.preferences():` to work with preferences. The API is subject to change.

    get\_schematic\_preference(*index: [LibSpecificPreference](experimental/preferences.md#keysight.ads.de.experimental.preferences.LibSpecificPreference "keysight.ads.de.experimental.preferences.LibSpecificPreference")*) → PreferenceValueType[](#keysight.ads.de.Library.get_schematic_preference "Link to this definition")
    :   Use `with de.experimental.preferences():` to work with preferences. The API is subject to change.

    *property* has\_attached\_tech*: bool*[](#keysight.ads.de.Library.has_attached_tech "Link to this definition")
    :   Return True if this library attaches technology from another library.

    *property* has\_dm\_data*: bool*[](#keysight.ads.de.Library.has_dm_data "Link to this definition")

    *property* has\_tech*: bool*[](#keysight.ads.de.Library.has_tech "Link to this definition")
    :   Return True if this library has technology or if it uses attached technology.

    *property* is\_an\_ads\_library*: bool*[](#keysight.ads.de.Library.is_an_ads_library "Link to this definition")

    *property* is\_open*: bool*[](#keysight.ads.de.Library.is_open "Link to this definition")

    *property* is\_read\_only*: bool*[](#keysight.ads.de.Library.is_read_only "Link to this definition")

    *property* is\_writable*: bool*[](#keysight.ads.de.Library.is_writable "Link to this definition")

    *property* lib\_name*: str*[](#keysight.ads.de.Library.lib_name "Link to this definition")

    *property* lib\_path*: Path*[](#keysight.ads.de.Library.lib_path "Link to this definition")

    module\_name() → str[](#keysight.ads.de.Library.module_name "Link to this definition")
    :   Return the full name of the Python module for this Library.

        Will raise an exception if this Library does not have a Python module.

    *property* name*: str*[](#keysight.ads.de.Library.name "Link to this definition")

    *static* open(*name: str*, *path: str | Path*, *mode: [LibraryMode](#keysight.ads.de.LibraryMode "keysight.ads.de._core.library.LibraryMode") = LibraryMode.READ\_ONLY*) → [Library](#keysight.ads.de.Library "keysight.ads.de._core.library.Library")[](#keysight.ads.de.Library.open "Link to this definition")

    *property* path*: Path*[](#keysight.ads.de.Library.path "Link to this definition")

    *property* physical\_layer\_names*: list[str]*[](#keysight.ads.de.Library.physical_layer_names "Link to this definition")

    set\_layout\_preference(*index: [LibSpecificPreference](experimental/preferences.md#keysight.ads.de.experimental.preferences.LibSpecificPreference "keysight.ads.de.experimental.preferences.LibSpecificPreference")*, *value: PreferenceValueType*) → None[](#keysight.ads.de.Library.set_layout_preference "Link to this definition")
    :   Use `with de.experimental.preferences():` to work with preferences. The API is subject to change.

    set\_schematic\_preference(*index: [LibSpecificPreference](experimental/preferences.md#keysight.ads.de.experimental.preferences.LibSpecificPreference "keysight.ads.de.experimental.preferences.LibSpecificPreference")*, *value: PreferenceValueType*) → None[](#keysight.ads.de.Library.set_schematic_preference "Link to this definition")
    :   Use `with de.experimental.preferences():` to work with preferences. The API is subject to change.

    setup\_schematic\_tech(*interoperable: bool = False*) → None[](#keysight.ads.de.Library.setup_schematic_tech "Link to this definition")

    *property* tech*: [Tech](tech/tech.md#keysight.ads.de.tech.Tech "keysight.ads.de.tech.Tech")*[](#keysight.ads.de.Library.tech "Link to this definition")
    :   Return the technology for this library (or raise an exception if none).

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.LibraryMode[](#keysight.ads.de.LibraryMode "Link to this definition")
:   Bases: `Enum`

    An enumeration specifying the mode for how a library is to be opened.

    SHARED *= <LibraryMode.SHARED: 0>*[](#keysight.ads.de.LibraryMode.SHARED "Link to this definition")
    :   Open the library for read-write, using lock files to support multiple processes concurrently using the library.

    NON\_SHARED *= <LibraryMode.NON\_SHARED: 1>*[](#keysight.ads.de.LibraryMode.NON_SHARED "Link to this definition")
    :   Open the library for read-write, with no lock files.

    READ\_ONLY *= <LibraryMode.READ\_ONLY: 2>*[](#keysight.ads.de.LibraryMode.READ_ONLY "Link to this definition")
    :   Open the library for read only.

    UNKNOWN *= <LibraryMode.UNKNOWN: -1>*[](#keysight.ads.de.LibraryMode.UNKNOWN "Link to this definition")
    :   No mode specified.

On this page

[Previous

Workspace](workspace.md)
[Next

Cell](cell.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top