[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Design](../../index.md)
* [Reference](../index.md)
* keysight.ads.de

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
    - keysight.ads.de
      * [Workspace](workspace.md)
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

# keysight.ads.de[](#module-keysight.ads.de "Link to this heading")

ADS Design Environment scripting.

Automate the ADS Design Environment using the `keysight.ads.de` package. This is typically
imported as:

```
from keysight.ads import de
```

## Classes[](#classes "Link to this heading")

* [Workspace](workspace.md)
  + [`Workspace`](workspace.md#keysight.ads.de.Workspace)
* [Library](library.md)
  + [Classes](library.md#classes)
  + [Enumerated Types](library.md#enumerated-types)
* [Cell](cell.md)
  + [`Cell`](cell.md#keysight.ads.de.Cell)
* [View](view.md)
  + [`View`](view.md#keysight.ads.de.View)

* [CellviewRef](cellviewref.md)
  + [`CellviewRef`](cellviewref.md#keysight.ads.de.CellviewRef)
  + [`CellviewRefLike`](cellviewref.md#keysight.ads.de.CellviewRefLike)
  + [`LCVName`](cellviewref.md#keysight.ads.de.LCVName)
* [DesignHierarchy](design_hierarchy.md)
  + [`DesignHierarchy`](design_hierarchy.md#keysight.ads.de.DesignHierarchy)
* [DMData](dmdata.md)
  + [`DMData`](dmdata.md#keysight.ads.de.DMData)
* [ItemInfo](item_info.md)
  + [Classes](item_info.md#classes)
  + [Enumerated Types](item_info.md#enumerated-types)
* [Points](points.md)
  + [`BoxF`](points.md#keysight.ads.de.BoxF)
  + [`PointDBU`](points.md#keysight.ads.de.PointDBU)
  + [`PointF`](points.md#keysight.ads.de.PointF)
  + [`PointMKS`](points.md#keysight.ads.de.PointMKS)
  + [`PointUU`](points.md#keysight.ads.de.PointUU)
  + [`dbu()`](points.md#keysight.ads.de.dbu)
  + [`uu()`](points.md#keysight.ads.de.uu)
* [Collections](collections.md)
  + [`IndexedMutableCollectionAbc`](collections.md#keysight.ads.de._list_like.IndexedMutableCollectionAbc)
  + [`NamedMutableCollectionAbc`](collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc)

## Functions[](#functions "Link to this heading")

keysight.ads.de.active\_workspace() → [Workspace](workspace.md#keysight.ads.de.Workspace "keysight.ads.de._core.workspace.Workspace")[](#keysight.ads.de.active_workspace "Link to this definition")
:   Return the currently opened workspace.

    This method raises a RuntimeError if there is no workspace open.

keysight.ads.de.add\_model\_definition(*library: [Library](library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *model\_def: [ModelDefBase](db/model_def.md#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db.ModelDefBase")*) → None[](#keysight.ads.de.add_model_definition "Link to this definition")

keysight.ads.de.add\_smart\_package(*package\_name: str*, *path: str | Path*) → None[](#keysight.ads.de.add_smart_package "Link to this definition")
:   Create an ADS Smart Package.

keysight.ads.de.cellview\_exists(*library\_name: str*, *cell\_name: str*, *view\_name: str*) → bool[](#keysight.ads.de.cellview_exists "Link to this definition")

keysight.ads.de.close\_library(*library\_name: str*) → None[](#keysight.ads.de.close_library "Link to this definition")

keysight.ads.de.close\_library\_if\_open(*library\_name: str*) → None[](#keysight.ads.de.close_library_if_open "Link to this definition")

keysight.ads.de.close\_workspace() → None[](#keysight.ads.de.close_workspace "Link to this definition")

keysight.ads.de.create\_new\_library(*library\_name: str*, *library\_path: Path | str*) → [Library](library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")[](#keysight.ads.de.create_new_library "Link to this definition")

keysight.ads.de.create\_workspace(*wrk\_path: str | PathLike*) → [Workspace](workspace.md#keysight.ads.de.Workspace "keysight.ads.de._core.workspace.Workspace")[](#keysight.ads.de.create_workspace "Link to this definition")
:   Create a new workspace at the specified path.

    Raises a RuntimeError if the path already exists.

keysight.ads.de.designs\_have\_different\_parameters(*this\_design: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*, *equiv\_design: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*) → bool[](#keysight.ads.de.designs_have_different_parameters "Link to this definition")

keysight.ads.de.directory\_is\_workspace(*path: Path | PathLike*) → bool[](#keysight.ads.de.directory_is_workspace "Link to this definition")

keysight.ads.de.directory\_might\_be\_workspace(*path: Path | PathLike*) → bool[](#keysight.ads.de.directory_might_be_workspace "Link to this definition")

keysight.ads.de.find\_equivalent\_design(*design: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*) → [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design") | None[](#keysight.ads.de.find_equivalent_design "Link to this definition")
:   Return the equivalent design.

    If design is the ‘schematic’ view, return the ‘layout’ view.
    If design is the ‘layout’ view, return the ‘schematic’ view.

keysight.ads.de.find\_inst\_in\_associated\_schematic(*inst\_name: str*, *design: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*) → tuple[[Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance"), [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")][](#keysight.ads.de.find_inst_in_associated_schematic "Link to this definition")
:   Find the named instance in the associated schematic of the given design.

    Typically used to find the substrate or process block referenced by parameters of layout instances.
    The value returned is a tuple containing the instance and its parent design.
    The parent design is only used to keep the design open so the instance won’t be deleted.
    Will raise an exception if there is no associated schematic or if the instance is not found or is deactivated.

keysight.ads.de.find\_inst\_in\_schematic\_hierarchy(*inst\_name: str*, *hierarchy: [DesignHierarchy](design_hierarchy.md#keysight.ads.de.DesignHierarchy "keysight.ads.de.DesignHierarchy")*) → tuple[[Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance"), [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")][](#keysight.ads.de.find_inst_in_schematic_hierarchy "Link to this definition")
:   Search up the hierarchy to find the named instance in the associated schematics of the designs in the hierarchy.

    Typically used to find the substrate or process block referenced by parameters of layout instances.
    The value returned is a tuple containing the instance and its parent design.
    The parent design is only used to keep the design open so the instance won’t be deleted.
    Will raise an exception if no activated instance is found in the schematics of the hierarchy.

keysight.ads.de.format\_number(*number: int | float | complex | str | None*, *width: int = 10*, *precision: int | None = None*) → str[](#keysight.ads.de.format_number "Link to this definition")

keysight.ads.de.generate\_netlist(*hierarchy: [DesignHierarchy](design_hierarchy.md#keysight.ads.de.DesignHierarchy "keysight.ads.de._core.design_hierarchy.DesignHierarchy")*) → str[](#keysight.ads.de.generate_netlist "Link to this definition")

keysight.ads.de.get\_cell\_module(*lib\_name: str*, *cell\_name: str*) → module[](#keysight.ads.de.get_cell_module "Link to this definition")
:   Import the Python module for an OpenAccess cell.

keysight.ads.de.get\_hierarchy\_from\_current\_expr\_context() → [DesignHierarchy](design_hierarchy.md#keysight.ads.de.DesignHierarchy "keysight.ads.de._core.design_hierarchy.DesignHierarchy")[](#keysight.ads.de.get_hierarchy_from_current_expr_context "Link to this definition")
:   Get the DesignHierarchy from the current ExpressionContext.

    Intended for use during layout pcell generation or custom callbacks.
    Will raise an exception if there is no current ExpressionContext or if the hierarchy is not valid.

keysight.ads.de.get\_library\_module(*lib\_name: str*) → module[](#keysight.ads.de.get_library_module "Link to this definition")
:   Import the Python module for an OpenAccess library.

keysight.ads.de.get\_open\_library(*library\_name: str*) → [Library](library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")[](#keysight.ads.de.get_open_library "Link to this definition")

keysight.ads.de.get\_open\_writable\_library\_names() → set[str][](#keysight.ads.de.get_open_writable_library_names "Link to this definition")

keysight.ads.de.get\_path\_to\_open\_library(*library\_name: str*) → Path | None[](#keysight.ads.de.get_path_to_open_library "Link to this definition")

keysight.ads.de.get\_smart\_package\_module(*package\_name: str*) → module[](#keysight.ads.de.get_smart_package_module "Link to this definition")
:   Import the Python module for an ADS Smart Package.

keysight.ads.de.get\_view\_module(*lib\_name: str*, *cell\_name: str*, *view\_name: str*) → module[](#keysight.ads.de.get_view_module "Link to this definition")
:   Import the Python module for an OpenAccess cellview.

keysight.ads.de.get\_view\_name\_for\_sub\_design\_from\_hierarchy(*hierarchy: [DesignHierarchy](design_hierarchy.md#keysight.ads.de.DesignHierarchy "keysight.ads.de._core.design_hierarchy.DesignHierarchy")*, *instance: [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*) → str[](#keysight.ads.de.get_view_name_for_sub_design_from_hierarchy "Link to this definition")

keysight.ads.de.hpeesof\_path() → str[](#keysight.ads.de.hpeesof_path "Link to this definition")

keysight.ads.de.is\_open\_library\_in\_workspace(*library: str | [Library](library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*) → bool[](#keysight.ads.de.is_open_library_in_workspace "Link to this definition")

keysight.ads.de.is\_pde\_app() → bool[](#keysight.ads.de.is_pde_app "Link to this definition")
:   Return True if the ADS application is running.

keysight.ads.de.library\_exists\_at\_path(*path: Path | str*) → bool[](#keysight.ads.de.library_exists_at_path "Link to this definition")

keysight.ads.de.library\_is\_open(*library\_name: str*) → bool[](#keysight.ads.de.library_is_open "Link to this definition")

keysight.ads.de.library\_is\_read\_only(*library\_name: str*) → bool[](#keysight.ads.de.library_is_read_only "Link to this definition")

keysight.ads.de.open\_workspace(*wrk\_path: str | PathLike*, *\**, *force: bool = False*) → [Workspace](workspace.md#keysight.ads.de.Workspace "keysight.ads.de._core.workspace.Workspace")[](#keysight.ads.de.open_workspace "Link to this definition")
:   Open the specified ADS workspace.

    forcebool [optional, default = False]
    :   If False, raises a RuntimeErro if a workspace is already open.
        If True, will first close any open workspace, losing unsaved changes.

keysight.ads.de.product\_version() → str[](#keysight.ads.de.product_version "Link to this definition")

keysight.ads.de.remove\_smart\_package(*package\_name: str*) → None[](#keysight.ads.de.remove_smart_package "Link to this definition")
:   Remove the named ADS Smart Package.

keysight.ads.de.running\_automation() → bool[](#keysight.ads.de.running_automation "Link to this definition")
:   Return True if the running application is Python.

    If True, then both `keysight.ads.de.is_pde_app()` and `keysight.ads.dds.is_dds_app()` will return False.

keysight.ads.de.unarchive\_file(*zap\_file\_path: str | Path | PathLike*, *dest\_path: str | Path | PathLike*, *\**, *exclude\_em\_files: bool = False*) → None[](#keysight.ads.de.unarchive_file "Link to this definition")
:   Unarchive a workspace 7zads file.

    Usage:
    de.unarchive\_file(zap\_name, dest\_path)
    de.unarchive\_file(zap\_name, dest\_path, exclude\_em\_files=True)

keysight.ads.de.update\_design\_parameters\_to\_match\_other\_design(*this\_design: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*, *other\_design: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*) → None[](#keysight.ads.de.update_design_parameters_to_match_other_design "Link to this definition")

keysight.ads.de.version() → int[](#keysight.ads.de.version "Link to this definition")

keysight.ads.de.workspace\_is\_open() → bool[](#keysight.ads.de.workspace_is_open "Link to this definition")
:   Check if a workspace is currently open.

On this page

[Previous

Reference](../index.md)
[Next

Workspace](workspace.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top