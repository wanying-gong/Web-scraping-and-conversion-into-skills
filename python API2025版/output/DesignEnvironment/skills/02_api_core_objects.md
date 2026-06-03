# Core API: keysight.ads.de
> **说明：** 核心 API 参考：Workspace（工作区）、Library（库）、Cell（单元）、View（视图）、CellviewRef（引用）、DesignHierarchy（层级）、DMData、ItemInfo、Points、Collections、AEL 接口。

> **何时使用：** 当你需要操作工作区、库、单元格、视图等核心设计对象时

---

## 本文件目录

- **keysight.ads.de** (`pypde/docs/reference/de/index.md`)
- **Workspace** (`pypde/docs/reference/de/workspace.md`)
- **Library** (`pypde/docs/reference/de/library.md`)
- **Cell** (`pypde/docs/reference/de/cell.md`)
- **View** (`pypde/docs/reference/de/view.md`)
- **CellviewRef** (`pypde/docs/reference/de/cellviewref.md`)
- **DesignHierarchy** (`pypde/docs/reference/de/design_hierarchy.md`)
- **DMData** (`pypde/docs/reference/de/dmdata.md`)
- **ItemInfo** (`pypde/docs/reference/de/item_info.md`)
- **Points** (`pypde/docs/reference/de/points.md`)
- **Collections** (`pypde/docs/reference/de/collections.md`)
- **keysight.ads.de.ael** (`pypde/docs/reference/de/ael.md`)

---

<!-- === 来源: pypde/docs/reference/de/index.md === -->

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


---

<!-- === 来源: pypde/docs/reference/de/workspace.md === -->

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


---

<!-- === 来源: pypde/docs/reference/de/library.md === -->

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


---

<!-- === 来源: pypde/docs/reference/de/cell.md === -->

# Cell[](#cell "Link to this heading")

*class* keysight.ads.de.Cell[](#keysight.ads.de.Cell "Link to this definition")
:   \_\_init\_\_(*library: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library")*, *cell\_name: str*) → None[](#keysight.ads.de.Cell.__init__ "Link to this definition")
    :   \_\_init\_\_ is deprecated, and will be removed in the 2025 Update 2 release. Use Cell.get(library, cell\_name) or library.cell(cell\_name).

    *property* cell\_name*: str*[](#keysight.ads.de.Cell.cell_name "Link to this definition")

    *static* create(*library: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library")*, *cell\_name: str*) → [Cell](#keysight.ads.de.Cell "keysight.ads.de.Cell")[](#keysight.ads.de.Cell.create "Link to this definition")

    create\_view(*view\_name: str*, *view\_type\_name: str*) → [View](view.md#keysight.ads.de.View "keysight.ads.de.View")[](#keysight.ads.de.Cell.create_view "Link to this definition")

    delete\_design\_variables() → None[](#keysight.ads.de.Cell.delete_design_variables "Link to this definition")

    delete\_dm\_data() → None[](#keysight.ads.de.Cell.delete_dm_data "Link to this definition")

    delete\_view(*view\_name: str*) → None[](#keysight.ads.de.Cell.delete_view "Link to this definition")

    dm\_data(*mode: str*) → [DMData](dmdata.md#keysight.ads.de.DMData "keysight.ads.de.DMData")[](#keysight.ads.de.Cell.dm_data "Link to this definition")

    *static* get(*library: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library")*, *cell\_name: str*) → [Cell](#keysight.ads.de.Cell "keysight.ads.de.Cell")[](#keysight.ads.de.Cell.get "Link to this definition")

    get\_view\_if\_exists(*view\_name: str*) → [View](view.md#keysight.ads.de.View "keysight.ads.de.View") | None[](#keysight.ads.de.Cell.get_view_if_exists "Link to this definition")

    *property* has\_dm\_data*: bool*[](#keysight.ads.de.Cell.has_dm_data "Link to this definition")

    *property* lib\_name*: str*[](#keysight.ads.de.Cell.lib_name "Link to this definition")

    *property* library*: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library")*[](#keysight.ads.de.Cell.library "Link to this definition")

    *property* model\_def*: [ModelDefBase](db/model_def.md#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db.ModelDefBase") | None*[](#keysight.ads.de.Cell.model_def "Link to this definition")

    module\_name() → str[](#keysight.ads.de.Cell.module_name "Link to this definition")
    :   Return the full name of the Python module for this Cell.

        Will raise an exception if this Cell does not have a Python module.

    *property* name*: str*[](#keysight.ads.de.Cell.name "Link to this definition")

    *property* path*: Path*[](#keysight.ads.de.Cell.path "Link to this definition")

    read\_design\_variables() → list[tuple[str, str]][](#keysight.ads.de.Cell.read_design_variables "Link to this definition")

    view(*view\_name: str*) → [View](view.md#keysight.ads.de.View "keysight.ads.de.View")[](#keysight.ads.de.Cell.view "Link to this definition")

    view\_exists(*view\_name: str*) → bool[](#keysight.ads.de.Cell.view_exists "Link to this definition")

    *property* views*: NamedItemCollectionAbc[[View](view.md#keysight.ads.de.View "keysight.ads.de.View")]*[](#keysight.ads.de.Cell.views "Link to this definition")
    :   The collection of views in this cell.

        A view may be accessed by using the [] operator, indexed by the view name.

    write\_design\_variables(*variables: list[tuple[str, str]]*) → None[](#keysight.ads.de.Cell.write_design_variables "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/view.md === -->

# View[](#view "Link to this heading")

*class* keysight.ads.de.View[](#keysight.ads.de.View "Link to this definition")
:   \_\_init\_\_(*lib: str*, *cell: str*, *view: str*) → None[](#keysight.ads.de.View.__init__ "Link to this definition")

    \_\_init\_\_(*lib: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library")*, *cell: str*, *view: str*) → None

    \_\_init\_\_(*\**, *cell: [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")*, *view: str*) → None
    :   \_\_init\_\_ is deprecated, and will be removed in the 2025 Update 2 release. Use View.get(cell, view\_name) or cell.view(view\_name).

    *property* cell*: [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")*[](#keysight.ads.de.View.cell "Link to this definition")

    *property* cell\_name*: str*[](#keysight.ads.de.View.cell_name "Link to this definition")

    delete\_dm\_data() → None[](#keysight.ads.de.View.delete_dm_data "Link to this definition")

    dm\_data(*mode: str*) → [DMData](dmdata.md#keysight.ads.de.DMData "keysight.ads.de.DMData")[](#keysight.ads.de.View.dm_data "Link to this definition")

    *static* get(*cell: [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")*, *view\_name: str*) → [View](#keysight.ads.de.View "keysight.ads.de.View")[](#keysight.ads.de.View.get "Link to this definition")

    get\_design(*mode: [DesignMode](db/enums.md#keysight.ads.de.db.DesignMode "keysight.ads.de.db._design_mode.DesignMode") = DesignMode.READ\_ONLY*) → [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")[](#keysight.ads.de.View.get_design "Link to this definition")

    *property* has\_dm\_data*: bool*[](#keysight.ads.de.View.has_dm_data "Link to this definition")

    *property* is\_any\_verilog\_view*: bool*[](#keysight.ads.de.View.is_any_verilog_view "Link to this definition")

    *property* is\_config\_view*: bool*[](#keysight.ads.de.View.is_config_view "Link to this definition")

    *property* is\_design\_view*: bool*[](#keysight.ads.de.View.is_design_view "Link to this definition")

    *property* is\_layout\_view*: bool*[](#keysight.ads.de.View.is_layout_view "Link to this definition")

    *property* is\_schematic\_view*: bool*[](#keysight.ads.de.View.is_schematic_view "Link to this definition")

    *property* is\_symbol\_view*: bool*[](#keysight.ads.de.View.is_symbol_view "Link to this definition")

    *property* is\_verilog\_view*: bool*[](#keysight.ads.de.View.is_verilog_view "Link to this definition")

    *property* is\_veriloga\_view*: bool*[](#keysight.ads.de.View.is_veriloga_view "Link to this definition")

    *property* is\_verilogams\_view*: bool*[](#keysight.ads.de.View.is_verilogams_view "Link to this definition")

    *property* lcv\_name*: str*[](#keysight.ads.de.View.lcv_name "Link to this definition")

    *property* lib\_name*: str*[](#keysight.ads.de.View.lib_name "Link to this definition")

    *property* library*: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library")*[](#keysight.ads.de.View.library "Link to this definition")

    module\_name() → str[](#keysight.ads.de.View.module_name "Link to this definition")
    :   Return the full name of the Python module for this View.

        Will raise an exception if this View does not have a Python module.

    *property* name*: str*[](#keysight.ads.de.View.name "Link to this definition")

    *property* path*: Path*[](#keysight.ads.de.View.path "Link to this definition")

    *property* view\_name*: str*[](#keysight.ads.de.View.view_name "Link to this definition")

    *property* view\_type\_name*: str*[](#keysight.ads.de.View.view_type_name "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/cellviewref.md === -->

# CellviewRef[](#cellviewref "Link to this heading")

*class* keysight.ads.de.CellviewRef[](#keysight.ads.de.CellviewRef "Link to this definition")
:   Provides flexibility in identifying a cellview.

    \_\_init\_\_(*lib: str*, *cell: str*, *view: str*) → None[](#keysight.ads.de.CellviewRef.__init__ "Link to this definition")

    \_\_init\_\_(*lib: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library")*, *cell: str*, *view: str*) → None

    \_\_init\_\_(*\**, *cell: [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")*, *view: str*) → None

    \_\_init\_\_(*\**, *view: [View](view.md#keysight.ads.de.View "keysight.ads.de.View")*) → None
    :   Initialize with 3 strings – library name, cell name, and view name – or use an object to replace 1 or more of those names.

    *property* cell*: [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell") | None*[](#keysight.ads.de.CellviewRef.cell "Link to this definition")
    :   The referenced cell.

        Read-only. Might be `None` if not specified.

    *property* cell\_name*: str*[](#keysight.ads.de.CellviewRef.cell_name "Link to this definition")
    :   The name of the referenced cell.

        Read-only. Might be empty if not specified.

    lcv\_string() → str[](#keysight.ads.de.CellviewRef.lcv_string "Link to this definition")
    :   Join the “lib:cell:view” names together in one colon-separated string.

    *property* lib*: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library") | None*[](#keysight.ads.de.CellviewRef.lib "Link to this definition")
    :   The referenced library.

        Read-only. Might be `None` if not specified.

    *property* lib\_name*: str*[](#keysight.ads.de.CellviewRef.lib_name "Link to this definition")
    :   The name of the referenced library.

        Read-only. Might be empty if not specified.

    *static* make(*arg: CellviewRefLike*) → [CellviewRef](#keysight.ads.de.CellviewRef "keysight.ads.de.CellviewRef")[](#keysight.ads.de.CellviewRef.make "Link to this definition")

    resolve() → [View](view.md#keysight.ads.de.View "keysight.ads.de.View")[](#keysight.ads.de.CellviewRef.resolve "Link to this definition")
    :   Look up the library, cell, and view names to find the [`View`](view.md#keysight.ads.de.View "keysight.ads.de.View").

        The properties like [`cell`](#keysight.ads.de.CellviewRef.cell "keysight.ads.de.CellviewRef.cell"), [`cell_name`](#keysight.ads.de.CellviewRef.cell_name "keysight.ads.de.CellviewRef.cell_name"), and so on may be set
        during the resolution process.

        Raise an exception if the View is not found.

    *property* view*: [View](view.md#keysight.ads.de.View "keysight.ads.de.View") | None*[](#keysight.ads.de.CellviewRef.view "Link to this definition")
    :   The referenced view.

        Read-only. Might be `None` if not specified.

    *property* view\_name*: str*[](#keysight.ads.de.CellviewRef.view_name "Link to this definition")
    :   The name of the referenced view.

        Read-only. Might be empty if not specified.

keysight.ads.de.CellviewRefLike[](#keysight.ads.de.CellviewRefLike "Link to this definition")
:   alias of `Union`[[`CellviewRef`](#keysight.ads.de.CellviewRef "keysight.ads.de._core.cellviewref.CellviewRef"), [`LCVName`](#keysight.ads.de.LCVName "keysight.ads.de._core.cellviewref.LCVName"), `str`, [`View`](view.md#keysight.ads.de.View "keysight.ads.de.View"), `Sequence`[`Union`[[`Library`](library.md#keysight.ads.de.Library "keysight.ads.de.Library"), [`Cell`](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell"), [`View`](view.md#keysight.ads.de.View "keysight.ads.de.View"), `str`]], `Mapping`[`str`, `Union`[[`Library`](library.md#keysight.ads.de.Library "keysight.ads.de.Library"), [`Cell`](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell"), [`View`](view.md#keysight.ads.de.View "keysight.ads.de.View"), `str`]]]

*class* keysight.ads.de.LCVName[](#keysight.ads.de.LCVName "Link to this definition")
:   Holds the library, cell, and view names that represent a cellview.

    \_\_init\_\_(*lib: str | [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library") | None = None*, *cell: str | [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell") | None = None*, *view: str | [View](view.md#keysight.ads.de.View "keysight.ads.de.View") | None = None*) → None[](#keysight.ads.de.LCVName.__init__ "Link to this definition")

    *property* cell\_name*: str*[](#keysight.ads.de.LCVName.cell_name "Link to this definition")

    *property* component\_name*: str*[](#keysight.ads.de.LCVName.component_name "Link to this definition")

    *property* design\_name*: str*[](#keysight.ads.de.LCVName.design_name "Link to this definition")

    *property* is\_empty*: bool*[](#keysight.ads.de.LCVName.is_empty "Link to this definition")

    *property* is\_valid*: bool*[](#keysight.ads.de.LCVName.is_valid "Link to this definition")

    *property* library\_name*: str*[](#keysight.ads.de.LCVName.library_name "Link to this definition")

    *static* make(*arg: CellviewRefLike*) → [LCVName](#keysight.ads.de.LCVName "keysight.ads.de.LCVName")[](#keysight.ads.de.LCVName.make "Link to this definition")

    *classmethod* parse(*lcv: str*) → [LCVName](#keysight.ads.de.LCVName "keysight.ads.de._core.cellviewref.LCVName")[](#keysight.ads.de.LCVName.parse "Link to this definition")

    *property* view\_name*: str*[](#keysight.ads.de.LCVName.view_name "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/design_hierarchy.md === -->

# DesignHierarchy[](#designhierarchy "Link to this heading")

*class* keysight.ads.de.DesignHierarchy[](#keysight.ads.de.DesignHierarchy "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.DesignHierarchy.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* depth*: int*[](#keysight.ads.de.DesignHierarchy.depth "Link to this definition")

    *property* design*: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*[](#keysight.ads.de.DesignHierarchy.design "Link to this definition")

    *property* is\_at\_root*: bool*[](#keysight.ads.de.DesignHierarchy.is_at_root "Link to this definition")

    is\_primitive\_instance(*inst: [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*) → bool[](#keysight.ads.de.DesignHierarchy.is_primitive_instance "Link to this definition")

    parent\_designs() → Iterable[[Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")][](#keysight.ads.de.DesignHierarchy.parent_designs "Link to this definition")

    parent\_instance\_names() → Iterable[str][](#keysight.ads.de.DesignHierarchy.parent_instance_names "Link to this definition")

    pop() → [DesignHierarchy](#keysight.ads.de.DesignHierarchy "keysight.ads.de._core.design_hierarchy.DesignHierarchy")[](#keysight.ads.de.DesignHierarchy.pop "Link to this definition")

    push\_instance\_for\_reading(*inst: [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*) → [DesignHierarchy](#keysight.ads.de.DesignHierarchy "keysight.ads.de.DesignHierarchy")[](#keysight.ads.de.DesignHierarchy.push_instance_for_reading "Link to this definition")
    :   Push into the instance in read-only mode.

        Modifications of a read-only design may only be saved to a new cellview.

    push\_instance\_for\_writing(*inst: [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*) → [DesignHierarchy](#keysight.ads.de.DesignHierarchy "keysight.ads.de.DesignHierarchy")[](#keysight.ads.de.DesignHierarchy.push_instance_for_writing "Link to this definition")
    :   Push into the instance in edit mode.

    *property* root\_design*: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*[](#keysight.ads.de.DesignHierarchy.root_design "Link to this definition")

    traverse\_instances(*include\_implicit: bool = False*, *include\_pin\_insts: bool = True*, *limit\_box: [BoxF](points.md#keysight.ads.de.BoxF "keysight.ads.de.BoxF") | None = None*, *allow\_box\_intersect: bool = True*) → Iterable[tuple[[Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance"), [DesignHierarchy](#keysight.ads.de.DesignHierarchy "keysight.ads.de.DesignHierarchy")]][](#keysight.ads.de.DesignHierarchy.traverse_instances "Link to this definition")
    :   Iterate through design hierarchically.

        Parameters:
        :   * **include\_implicit** (*bool*) – Defaults to false and will include implicit shapes individually when set. For example
              bus nets will show up as one when set to false, but will be enumerated individually
              when set to True.
            * **include\_pin\_insts** (*bool*) – Defaults to True and will include PinInst objects during the traversal.
            * **limit\_box** ([*BoxF*](points.md#keysight.ads.de.BoxF "keysight.ads.de.BoxF")) – Default to None and when set will limit the traversal to the specified region in user units.
            * **allow\_box\_intersect** (*bool*) – Defaults to True and when set includes instances that intersect the specified box to be part
              of the traversal, otherwise only instances wholly inside the box are returned.

        Example

        ```
        >>> for x, _ in topdsn.get_hierarchy_for_netlist().traverse_instances(include_implicit = True):
        ...     print(f"Inst = {x}")
        ```


---

<!-- === 来源: pypde/docs/reference/de/dmdata.md === -->

# DMData[](#dmdata "Link to this heading")

*class* keysight.ads.de.DMData[](#keysight.ads.de.DMData "Link to this definition")
:   DMData is an optional database that can hold properties for Library, Cell, and View.

    If you add properties to the DMData, you must save it.

    find\_prop(*name: str*) → [Property](db/properties.md#keysight.ads.de.db.Property "keysight.ads.de.db.Property") | None[](#keysight.ads.de.DMData.find_prop "Link to this definition")

    *property* is\_cell*: bool*[](#keysight.ads.de.DMData.is_cell "Link to this definition")

    *property* is\_library*: bool*[](#keysight.ads.de.DMData.is_library "Link to this definition")

    *property* is\_view*: bool*[](#keysight.ads.de.DMData.is_view "Link to this definition")

    make\_writable() → None[](#keysight.ads.de.DMData.make_writable "Link to this definition")

    *property* modified*: bool*[](#keysight.ads.de.DMData.modified "Link to this definition")

    *static* open(*owner: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library") | [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell") | [View](view.md#keysight.ads.de.View "keysight.ads.de.View")*, *mode: str*) → [DMData](#keysight.ads.de.DMData "keysight.ads.de.DMData")[](#keysight.ads.de.DMData.open "Link to this definition")
    :   Open a DM database for the given owner.

        The mode determines how the database is opened:
        “r” - Open the database read-only. The database must exist.
        “a” - Open the database for appending data or create a new one.
        “w” - Open for writing or create a new one. Deletes all existing objects.

    *property* owner*: [Library](library.md#keysight.ads.de.Library "keysight.ads.de.Library") | [Cell](cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell") | [View](view.md#keysight.ads.de.View "keysight.ads.de.View")*[](#keysight.ads.de.DMData.owner "Link to this definition")

    *property* props*: NamedReadableCollectionAbc[[Property](db/properties.md#keysight.ads.de.db.Property "keysight.ads.de.db.Property")]*[](#keysight.ads.de.DMData.props "Link to this definition")

    *property* read\_only*: bool*[](#keysight.ads.de.DMData.read_only "Link to this definition")

    revert() → None[](#keysight.ads.de.DMData.revert "Link to this definition")
    :   Revert all changes to the database - deleting new objects.

    save() → None[](#keysight.ads.de.DMData.save "Link to this definition")

    truncate() → None[](#keysight.ads.de.DMData.truncate "Link to this definition")
    :   Truncate the entire database - deleting all objects.


---

<!-- === 来源: pypde/docs/reference/de/item_info.md === -->

# ItemInfo[](#iteminfo "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.ItemInfo[](#keysight.ads.de.ItemInfo "Link to this definition")
:   \_\_init\_\_(*design: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*, *lcv\_name: [LCVName](cellviewref.md#keysight.ads.de.LCVName "keysight.ads.de.LCVName")*, *edit\_mode: [ItemEditMode](#keysight.ads.de.ItemEditMode "keysight.ads.de._core._item_info.ItemEditMode")*) → None[](#keysight.ads.de.ItemInfo.__init__ "Link to this definition")

    *property* cell\_name*: str*[](#keysight.ads.de.ItemInfo.cell_name "Link to this definition")

    create\_new\_instance(*location: [PointF](points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *auto\_connect: bool = False*) → [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")[](#keysight.ads.de.ItemInfo.create_new_instance "Link to this definition")

    *property* design\_name*: str*[](#keysight.ads.de.ItemInfo.design_name "Link to this definition")

    *property* display\_name*: str*[](#keysight.ads.de.ItemInfo.display_name "Link to this definition")

    *property* inst\_name*: str*[](#keysight.ads.de.ItemInfo.inst_name "Link to this definition")

    *property* instance*: [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance") | None*[](#keysight.ads.de.ItemInfo.instance "Link to this definition")

    *property* is\_scope\_global*: bool*[](#keysight.ads.de.ItemInfo.is_scope_global "Link to this definition")

    *property* is\_scope\_nested*: bool*[](#keysight.ads.de.ItemInfo.is_scope_nested "Link to this definition")

    *property* lib\_name*: str*[](#keysight.ads.de.ItemInfo.lib_name "Link to this definition")

    *property* model\_def*: [ModelDefBase](db/model_def.md#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db.ModelDefBase") | None*[](#keysight.ads.de.ItemInfo.model_def "Link to this definition")

    *property* owner\_design*: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*[](#keysight.ads.de.ItemInfo.owner_design "Link to this definition")

    set\_scope\_global() → None[](#keysight.ads.de.ItemInfo.set_scope_global "Link to this definition")

    set\_scope\_nested() → None[](#keysight.ads.de.ItemInfo.set_scope_nested "Link to this definition")

    setup\_instance\_for\_edit(*instance: [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*, *mod\_inst\_name\_pref: bool = False*) → None[](#keysight.ads.de.ItemInfo.setup_instance_for_edit "Link to this definition")

    *property* view\_name*: str*[](#keysight.ads.de.ItemInfo.view_name "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.ItemEditMode[](#keysight.ads.de.ItemEditMode "Link to this definition")
:   DIALOG *= <ItemEditMode.DIALOG: 0>*[](#keysight.ads.de.ItemEditMode.DIALOG "Link to this definition")

    NEW *= <ItemEditMode.NEW: 1>*[](#keysight.ads.de.ItemEditMode.NEW "Link to this definition")

    ON\_SCREEN *= <ItemEditMode.ON\_SCREEN: 2>*[](#keysight.ads.de.ItemEditMode.ON_SCREEN "Link to this definition")

    TEMP *= <ItemEditMode.TEMP: 3>*[](#keysight.ads.de.ItemEditMode.TEMP "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/points.md === -->

# Points[](#points "Link to this heading")

*class* keysight.ads.de.BoxF[](#keysight.ads.de.BoxF "Link to this definition")
:   TFloatTuple[](#keysight.ads.de.BoxF.TFloatTuple "Link to this definition")
    :   alias of `tuple`[`float`, `float`]

    TPoint[](#keysight.ads.de.BoxF.TPoint "Link to this definition")
    :   alias of `Union`[[`PointF`](#keysight.ads.de.PointF "keysight.ads.de._points.PointF"), `tuple`[`float`, `float`]]

    \_\_init\_\_(*\**, *lower\_left: [PointF](#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float] | None = None*, *upper\_right: [PointF](#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float] | None = None*, *x1: float | None = None*, *y1: float | None = None*, *x2: float | None = None*, *y2: float | None = None*) → None[](#keysight.ads.de.BoxF.__init__ "Link to this definition")

    contains(*obj: [PointF](#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | [BoxF](#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → bool[](#keysight.ads.de.BoxF.contains "Link to this definition")

    expand(*obj: [PointF](#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | [BoxF](#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → None[](#keysight.ads.de.BoxF.expand "Link to this definition")

    *property* lower\_left*: [PointF](#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.BoxF.lower_left "Link to this definition")

    overlaps(*obj: [PointF](#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | [BoxF](#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → bool[](#keysight.ads.de.BoxF.overlaps "Link to this definition")

    *property* upper\_right*: [PointF](#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.BoxF.upper_right "Link to this definition")

    *property* x1*: float*[](#keysight.ads.de.BoxF.x1 "Link to this definition")

    *property* x2*: float*[](#keysight.ads.de.BoxF.x2 "Link to this definition")

    *property* y1*: float*[](#keysight.ads.de.BoxF.y1 "Link to this definition")

    *property* y2*: float*[](#keysight.ads.de.BoxF.y2 "Link to this definition")

*class* keysight.ads.de.PointDBU[](#keysight.ads.de.PointDBU "Link to this definition")
:   Represents a 2-D point in database units, using int data.

    \_\_init\_\_(*x: ~keysight.ads.de.\_points.CoordinateType*, *y: ~keysight.ads.de.\_points.CoordinateType*, *\_coordinate\_type: dataclasses.InitVar[type] = <class 'int'>*) → None[](#keysight.ads.de.PointDBU.__init__ "Link to this definition")

    astuple() → tuple[CoordinateType, CoordinateType][](#keysight.ads.de.PointDBU.astuple "Link to this definition")

    *classmethod* from\_point(*pt: Point2d*) → Point2dType[](#keysight.ads.de.PointDBU.from_point "Link to this definition")
    :   Casts the values from “pt” to the point type specified by “cls”.

        Note that this does not do any conversions or other changes to the
        coordinate values! This function simply copies the numeric values to
        a point object of a different class.

    x*: CoordinateType*[](#keysight.ads.de.PointDBU.x "Link to this definition")

    y*: CoordinateType*[](#keysight.ads.de.PointDBU.y "Link to this definition")

*class* keysight.ads.de.PointF[](#keysight.ads.de.PointF "Link to this definition")
:   Represents a 2-D point using float data. The units are not defined.

    \_\_init\_\_(*x: ~keysight.ads.de.\_points.CoordinateType*, *y: ~keysight.ads.de.\_points.CoordinateType*, *\_coordinate\_type: dataclasses.InitVar[type] = <class 'float'>*) → None[](#keysight.ads.de.PointF.__init__ "Link to this definition")

    astuple() → tuple[CoordinateType, CoordinateType][](#keysight.ads.de.PointF.astuple "Link to this definition")

    *classmethod* from\_point(*pt: Point2d*) → Point2dType[](#keysight.ads.de.PointF.from_point "Link to this definition")
    :   Casts the values from “pt” to the point type specified by “cls”.

        Note that this does not do any conversions or other changes to the
        coordinate values! This function simply copies the numeric values to
        a point object of a different class.

    x*: CoordinateType*[](#keysight.ads.de.PointF.x "Link to this definition")

    y*: CoordinateType*[](#keysight.ads.de.PointF.y "Link to this definition")

*class* keysight.ads.de.PointMKS[](#keysight.ads.de.PointMKS "Link to this definition")
:   Represents a 2-D point in MKS units, using float data.

    \_\_init\_\_(*x: ~keysight.ads.de.\_points.CoordinateType*, *y: ~keysight.ads.de.\_points.CoordinateType*, *\_coordinate\_type: dataclasses.InitVar[type] = <class 'float'>*) → None[](#keysight.ads.de.PointMKS.__init__ "Link to this definition")

    astuple() → tuple[CoordinateType, CoordinateType][](#keysight.ads.de.PointMKS.astuple "Link to this definition")

    *classmethod* from\_point(*pt: Point2d*) → Point2dType[](#keysight.ads.de.PointMKS.from_point "Link to this definition")
    :   Casts the values from “pt” to the point type specified by “cls”.

        Note that this does not do any conversions or other changes to the
        coordinate values! This function simply copies the numeric values to
        a point object of a different class.

    x*: CoordinateType*[](#keysight.ads.de.PointMKS.x "Link to this definition")

    y*: CoordinateType*[](#keysight.ads.de.PointMKS.y "Link to this definition")

*class* keysight.ads.de.PointUU[](#keysight.ads.de.PointUU "Link to this definition")
:   Represents a 2-D point in user units, using float data.

    \_\_init\_\_(*x: ~keysight.ads.de.\_points.CoordinateType*, *y: ~keysight.ads.de.\_points.CoordinateType*, *\_coordinate\_type: dataclasses.InitVar[type] = <class 'float'>*) → None[](#keysight.ads.de.PointUU.__init__ "Link to this definition")

    astuple() → tuple[CoordinateType, CoordinateType][](#keysight.ads.de.PointUU.astuple "Link to this definition")

    *classmethod* from\_point(*pt: Point2d*) → Point2dType[](#keysight.ads.de.PointUU.from_point "Link to this definition")
    :   Casts the values from “pt” to the point type specified by “cls”.

        Note that this does not do any conversions or other changes to the
        coordinate values! This function simply copies the numeric values to
        a point object of a different class.

    x*: CoordinateType*[](#keysight.ads.de.PointUU.x "Link to this definition")

    y*: CoordinateType*[](#keysight.ads.de.PointUU.y "Link to this definition")

keysight.ads.de.dbu(*arg: Point2d | tuple[CoordinateType, CoordinateType]*) → [PointDBU](#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")[](#keysight.ads.de.dbu "Link to this definition")

keysight.ads.de.dbu(*arg: Sequence[Point2d | tuple[CoordinateType, CoordinateType]]*) → list[[PointDBU](#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")]

keysight.ads.de.uu(*arg: Point2d | tuple[CoordinateType, CoordinateType]*) → [PointUU](#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU")[](#keysight.ads.de.uu "Link to this definition")

keysight.ads.de.uu(*arg: Sequence[Point2d | tuple[CoordinateType, CoordinateType]]*) → list[[PointUU](#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU")]


---

<!-- === 来源: pypde/docs/reference/de/collections.md === -->

# Collections[](#collections "Link to this heading")

Collection classes are not intended to be instantiated directly and are used as accessors to the individual elements of a collection returned in various classes.

*class* keysight.ads.de.\_list\_like.IndexedMutableCollectionAbc[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc "Link to this definition")
:   An abstract base class (ABC) for a list-like collection of elements.

    This is used to support cases where the elements are controlled
    by the owner.
    Assigning elements will assign the new objects to the owner.
    Inserting or appending new elements will add the new objects to the owner.
    Deleting an element from the collection will remove it from the owner.

    *abstract* \_\_delitem\_\_(*index: int*) → None[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__delitem__ "Link to this definition")

    *abstract* \_\_getitem\_\_(*index*)[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__getitem__ "Link to this definition")

    *abstract* \_\_iadd\_\_(*values: T | Sequence[T]*) → [IndexedMutableCollectionAbc](#keysight.ads.de._list_like.IndexedMutableCollectionAbc "keysight.ads.de._list_like.IndexedMutableCollectionAbc")[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__iadd__ "Link to this definition")

    \_\_iter\_\_()[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__iter__ "Link to this definition")

    *abstract* \_\_len\_\_()[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__len__ "Link to this definition")

    *abstract* \_\_setitem\_\_(*index: int*, *value: T*) → None[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__setitem__ "Link to this definition")

    *abstract* \_\_setitem\_\_(*index: slice*, *value: Sequence[T]*) → None

    *abstract* append(*values: T | Sequence[T]*) → None[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.append "Link to this definition")

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.count "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    *abstract* insert(*index: int*, *values: T | Sequence[T]*) → None[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.insert "Link to this definition")

    *abstract* pop(*index: int = -1*) → T[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.pop "Link to this definition")

    *abstract* remove(*index: int*) → None[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.remove "Link to this definition")

*class* keysight.ads.de.\_list\_like.NamedMutableCollectionAbc[](#keysight.ads.de._list_like.NamedMutableCollectionAbc "Link to this definition")
:   An abstract base class (ABC) for a mutable collection of named wrapper objects.

    This is used to support cases where the elements are controlled
    by the owner.

    *abstract* \_\_delitem\_\_(*key: str*) → None[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.__delitem__ "Link to this definition")

    *abstract* \_\_getitem\_\_(*key: str*) → T[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.__getitem__ "Link to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.__init__ "Link to this definition")

    *abstract* \_\_iter\_\_() → Iterator[T][](#keysight.ads.de._list_like.NamedMutableCollectionAbc.__iter__ "Link to this definition")

    *abstract* \_\_len\_\_() → int[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.__len__ "Link to this definition")

    *abstract* add(*value: T*) → None[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.add "Link to this definition")

    *abstract* find(*key: str*) → T | None[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.find "Link to this definition")
    :   Find an item by name. Returns None if not found.

    *abstract* get(*key: str*) → T | None[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.get "Link to this definition")
    :   Find an item by name. Returns None if not found.

    *abstract* names() → list[str][](#keysight.ads.de._list_like.NamedMutableCollectionAbc.names "Link to this definition")
    :   Return the names in this collection.

    *abstract* remove(*value: T*) → None[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.remove "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/ael.md === -->

# keysight.ads.de.ael[](#keysight-ads-de-ael "Link to this heading")

keysight.ads.de.ael is deprecated. Please use [keysight.ads.ael](../../../../../../../../ael/python/docs/html/reference/ael.md) instead.

AEL Python Documentation is located [here](../../../../../../../../ael/python/docs/html/index.md).


---

