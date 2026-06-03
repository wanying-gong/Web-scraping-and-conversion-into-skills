# Experimental API: keysight.ads.de.experimental
> **说明：** 实验性 API（不保证向后兼容）：CDF（组件数据格式）、Commands（命令）、Handles（句柄）、Symbol Generator（符号生成器）、ProView、Polygon Utilities（多边形工具）、TextMaker、Preferences（偏好设置）、Netlist Helper（网表工具）。

> **何时使用：** 当你需要使用高级/实验性功能，如符号生成、多边形操作、CDF 访问时

---

## 本文件目录

- **keysight.ads.de.experimental** (`pypde/docs/reference/de/experimental/index.md`)
- **CDF** (`pypde/docs/reference/de/experimental/cdf/index.md`)
- **Commands** (`pypde/docs/reference/de/experimental/commands.md`)
- **Handles** (`pypde/docs/reference/de/experimental/handles.md`)
- **Symbol Generator** (`pypde/docs/reference/de/experimental/symbol.md`)
- **xxPro View** (`pypde/docs/reference/de/experimental/pro_view.md`)
- **Polygon Utilities** (`pypde/docs/reference/de/experimental/polygon_utils.md`)
- **Text Maker** (`pypde/docs/reference/de/experimental/text_maker.md`)
- **Preferences** (`pypde/docs/reference/de/experimental/preferences.md`)
- **Netlist Utilities** (`pypde/docs/reference/de/experimental/netlist_helper.md`)

---

<!-- === 来源: pypde/docs/reference/de/experimental/index.md === -->

# keysight.ads.de.experimental[](#module-keysight.ads.de.experimental "Link to this heading")

Experimental additions to the API.

* [CDF](cdf/index.md)
  + [Classes](cdf/index.md#classes)
    - [`CDFBase`](cdf/index.md#keysight.ads.de.experimental.cdf.CDFBase)
    - [`CellCDF`](cdf/index.md#keysight.ads.de.experimental.cdf.CellCDF)
    - [`InstanceParams`](cdf/index.md#keysight.ads.de.experimental.cdf.InstanceParams)
    - [`LibraryCDF`](cdf/index.md#keysight.ads.de.experimental.cdf.LibraryCDF)
    - [`ManagedCDF`](cdf/index.md#keysight.ads.de.experimental.cdf.ManagedCDF)
    - [`ParamDef`](cdf/index.md#keysight.ads.de.experimental.cdf.ParamDef)
    - [`ScratchCDF`](cdf/index.md#keysight.ads.de.experimental.cdf.ScratchCDF)
    - [`SimInfo`](cdf/index.md#keysight.ads.de.experimental.cdf.SimInfo)
    - [`ViewInfo`](cdf/index.md#keysight.ads.de.experimental.cdf.ViewInfo)
  + [Enumerated Types](cdf/index.md#enumerated-types)
    - [`ParamType`](cdf/index.md#keysight.ads.de.experimental.cdf.ParamType)
    - [`ParamUnits`](cdf/index.md#keysight.ads.de.experimental.cdf.ParamUnits)
  + [Functions](cdf/index.md#functions)
    - [`cell_cdf()`](cdf/index.md#keysight.ads.de.experimental.cdf.cell_cdf)
    - [`find_cell_cdf()`](cdf/index.md#keysight.ads.de.experimental.cdf.find_cell_cdf)
    - [`find_library_cdf()`](cdf/index.md#keysight.ads.de.experimental.cdf.find_library_cdf)
    - [`library_cdf()`](cdf/index.md#keysight.ads.de.experimental.cdf.library_cdf)
* [Commands](commands.md)
  + [Classes](commands.md#classes)
    - [`DesignTrackingPainter`](commands.md#keysight.ads.de.experimental.commands.DesignTrackingPainter)
    - [`CommandInfo`](commands.md#keysight.ads.de.experimental.commands.CommandInfo)
  + [Functions](commands.md#functions)
    - [`start_design_command()`](commands.md#keysight.ads.de.experimental.commands.start_design_command)
* [Handles](handles.md)
  + [Classes](handles.md#classes)
    - [`Handle`](handles.md#keysight.ads.de.experimental.handles.Handle)
    - [`DesignWidget`](handles.md#keysight.ads.de.experimental.handles.DesignWidget)
  + [Enumerated Types](handles.md#enumerated-types)
    - [`HandleType`](handles.md#keysight.ads.de.experimental.handles.HandleType)
  + [Functions](handles.md#functions)
    - [`create_custom_handle_for_instance()`](handles.md#keysight.ads.de.experimental.handles.create_custom_handle_for_instance)
    - [`register_handle_generator()`](handles.md#keysight.ads.de.experimental.handles.register_handle_generator)
    - [`unregister_handle_generators_for_library()`](handles.md#keysight.ads.de.experimental.handles.unregister_handle_generators_for_library)
* [Netlist Utilities](netlist_helper.md)
  + [Classes](netlist_helper.md#classes)
    - [`NetlistStringBuilder`](netlist_helper.md#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder)
* [Polygon Utilities](polygon_utils.md)
  + [Classes](polygon_utils.md#classes)
    - [`Oversizer`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.Oversizer)
    - [`PolygonOversizer`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.PolygonOversizer)
    - [`PolygonVertexToArcConverter`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.PolygonVertexToArcConverter)
    - [`ShapeOversizer`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.ShapeOversizer)
    - [`ShapeVertexToArcConverter`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.ShapeVertexToArcConverter)
    - [`VertexToArcConverter`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter)
  + [Functions](polygon_utils.md#functions)
    - [`convert_vertices_to_arcs()`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.convert_vertices_to_arcs)
    - [`oversize()`](polygon_utils.md#keysight.ads.de.experimental.polygon_utils.oversize)
* [Preferences](preferences.md)
  + [Enumerated Types](preferences.md#enumerated-types)
    - [`WorkspacePreference`](preferences.md#keysight.ads.de.experimental.preferences.WorkspacePreference)
    - [`LibSpecificPreference`](preferences.md#keysight.ads.de.experimental.preferences.LibSpecificPreference)
* [xxPro View](pro_view.md)
  + [Functions](pro_view.md#functions)
    - [`create_pro_view()`](pro_view.md#keysight.ads.de.experimental.pro_view.create_pro_view)
* [Symbol Generator](symbol.md)
  + [Classes](symbol.md#classes)
    - [`SymbolGenerator`](symbol.md#keysight.ads.de.experimental.generate_symbol.SymbolGenerator)
  + [Enumerated Types](symbol.md#enumerated-types)
    - [`OrderType`](symbol.md#keysight.ads.de.experimental.generate_symbol.OrderType)
* [Text Maker](text_maker.md)
  + [Classes](text_maker.md#classes)
    - [`TextMaker`](text_maker.md#keysight.ads.de.experimental.text_maker.TextMaker)


---

<!-- === 来源: pypde/docs/reference/de/experimental/cdf/index.md === -->

# CDF[](#module-keysight.ads.de.experimental.cdf "Link to this heading")

CDF module contains the API for interoperable components.

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.cdf.CDFBase[](#keysight.ads.de.experimental.cdf.CDFBase "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.cdf.CDFBase.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    add\_param(*param: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*) → None[](#keysight.ads.de.experimental.cdf.CDFBase.add_param "Link to this definition")

    delete\_param(*index: int*) → None[](#keysight.ads.de.experimental.cdf.CDFBase.delete_param "Link to this definition")

    *property* done\_proc*: str*[](#keysight.ads.de.experimental.cdf.CDFBase.done_proc "Link to this definition")

    find\_param(*name: str*) → [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef") | None[](#keysight.ads.de.experimental.cdf.CDFBase.find_param "Link to this definition")

    find\_sim\_info(*sim\_name: str*) → [SimInfo](#keysight.ads.de.experimental.cdf.SimInfo "keysight.ads.de.experimental.cdf.sim_info.SimInfo") | None[](#keysight.ads.de.experimental.cdf.CDFBase.find_sim_info "Link to this definition")

    find\_view\_info(*view\_name: str*) → [ViewInfo](#keysight.ads.de.experimental.cdf.ViewInfo "keysight.ads.de.experimental.cdf.view_info.ViewInfo") | None[](#keysight.ads.de.experimental.cdf.CDFBase.find_view_info "Link to this definition")

    *property* form\_init\_proc*: str*[](#keysight.ads.de.experimental.cdf.CDFBase.form_init_proc "Link to this definition")

    insert\_param(*param: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*, *index: int*) → None[](#keysight.ads.de.experimental.cdf.CDFBase.insert_param "Link to this definition")

    *property* num\_params*: int*[](#keysight.ads.de.experimental.cdf.CDFBase.num_params "Link to this definition")

    param(*id\_: int*) → [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")[](#keysight.ads.de.experimental.cdf.CDFBase.param "Link to this definition")

    param(*id\_: str*) → [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")

    *property* params*: NamedItemCollectionAbc[[ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")]*[](#keysight.ads.de.experimental.cdf.CDFBase.params "Link to this definition")

    sim\_info(*sim\_name: str*) → [SimInfo](#keysight.ads.de.experimental.cdf.SimInfo "keysight.ads.de.experimental.cdf.sim_info.SimInfo")[](#keysight.ads.de.experimental.cdf.CDFBase.sim_info "Link to this definition")

    view\_info(*view\_name: str*) → [ViewInfo](#keysight.ads.de.experimental.cdf.ViewInfo "keysight.ads.de.experimental.cdf.view_info.ViewInfo")[](#keysight.ads.de.experimental.cdf.CDFBase.view_info "Link to this definition")

*class* keysight.ads.de.experimental.cdf.CellCDF[](#keysight.ads.de.experimental.cdf.CellCDF "Link to this definition")
:   Bases: [`ManagedCDF`](#keysight.ads.de.experimental.cdf.ManagedCDF "keysight.ads.de.experimental.cdf.comp_def.ManagedCDF")

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.cdf.CellCDF.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* cell*: [Cell](../../cell.md#keysight.ads.de.Cell "keysight.ads.de._core.cell.Cell")*[](#keysight.ads.de.experimental.cdf.CellCDF.cell "Link to this definition")

    *property* library*: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.de.experimental.cdf.CellCDF.library "Link to this definition")

*class* keysight.ads.de.experimental.cdf.InstanceParams[](#keysight.ads.de.experimental.cdf.InstanceParams "Link to this definition")
:   Supports editing parameter values for interoperable instances.

    \_\_init\_\_(*inst\_or\_design: Instance | [Instance](../../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*, *cdf: 'CellCDF' | None = None*) → None[](#keysight.ads.de.experimental.cdf.InstanceParams.__init__ "Link to this definition")

    \_\_init\_\_(*inst\_or\_design: Design | [Design](../../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *cdf: [CellCDF](#keysight.ads.de.experimental.cdf.CellCDF "keysight.ads.de.experimental.cdf.CellCDF")*) → None

    *property* cell\_cdf*: [CellCDF](#keysight.ads.de.experimental.cdf.CellCDF "keysight.ads.de.experimental.cdf.CellCDF")*[](#keysight.ads.de.experimental.cdf.InstanceParams.cell_cdf "Link to this definition")

    execute\_callback(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*) → None[](#keysight.ads.de.experimental.cdf.InstanceParams.execute_callback "Link to this definition")

    execute\_callback(*id\_: str*) → None

    find\_param(*param\_name: str*) → Parameter | None[](#keysight.ads.de.experimental.cdf.InstanceParams.find_param "Link to this definition")

    find\_param\_def(*param\_name: str*) → [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef") | None[](#keysight.ads.de.experimental.cdf.InstanceParams.find_param_def "Link to this definition")

    *property* instance\_dbu*: Instance | None*[](#keysight.ads.de.experimental.cdf.InstanceParams.instance_dbu "Link to this definition")

    *property* instance\_uu*: [Instance](../../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance") | None*[](#keysight.ads.de.experimental.cdf.InstanceParams.instance_uu "Link to this definition")

    *property* is\_modified*: bool*[](#keysight.ads.de.experimental.cdf.InstanceParams.is_modified "Link to this definition")

    param(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*) → Parameter[](#keysight.ads.de.experimental.cdf.InstanceParams.param "Link to this definition")

    param(*id\_: str*) → Parameter

    param\_def(*param\_name: str*) → [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")[](#keysight.ads.de.experimental.cdf.InstanceParams.param_def "Link to this definition")

    param\_value(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*) → bool | int | float | str[](#keysight.ads.de.experimental.cdf.InstanceParams.param_value "Link to this definition")

    param\_value(*id\_: str*) → bool | int | float | str

    param\_value\_no\_default(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*) → bool | int | float | str | None[](#keysight.ads.de.experimental.cdf.InstanceParams.param_value_no_default "Link to this definition")

    param\_value\_no\_default(*id\_: str*) → bool | int | float | str | None

    *property* params*: NamedItemCollectionAbc[Parameter]*[](#keysight.ads.de.experimental.cdf.InstanceParams.params "Link to this definition")

    *property* parent\_design\_dbu*: Design*[](#keysight.ads.de.experimental.cdf.InstanceParams.parent_design_dbu "Link to this definition")

    *property* parent\_design\_uu*: [Design](../../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*[](#keysight.ads.de.experimental.cdf.InstanceParams.parent_design_uu "Link to this definition")

    reset\_to\_defaults() → None[](#keysight.ads.de.experimental.cdf.InstanceParams.reset_to_defaults "Link to this definition")

    set\_param\_value(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*, *value: bool | int | float | str*) → None[](#keysight.ads.de.experimental.cdf.InstanceParams.set_param_value "Link to this definition")

    set\_param\_value(*id\_: str*, *value: bool | int | float | str*) → None
    :   Set the parameter value and call the callback if one exists.

    set\_param\_value\_no\_callback(*id\_: [ParamDef](#keysight.ads.de.experimental.cdf.ParamDef "keysight.ads.de.experimental.cdf.params.ParamDef")*, *value: bool | int | float | str*) → None[](#keysight.ads.de.experimental.cdf.InstanceParams.set_param_value_no_callback "Link to this definition")

    set\_param\_value\_no\_callback(*id\_: str*, *value: bool | int | float | str*) → None
    :   Set the parameter value without calling any callback.

    update\_instance(*inst: Instance | [Instance](../../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance") | None*) → None[](#keysight.ads.de.experimental.cdf.InstanceParams.update_instance "Link to this definition")
    :   Assign all the modified parameter values to the instance.

*class* keysight.ads.de.experimental.cdf.LibraryCDF[](#keysight.ads.de.experimental.cdf.LibraryCDF "Link to this definition")
:   Bases: [`ManagedCDF`](#keysight.ads.de.experimental.cdf.ManagedCDF "keysight.ads.de.experimental.cdf.comp_def.ManagedCDF")

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.cdf.LibraryCDF.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* library*: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.de.experimental.cdf.LibraryCDF.library "Link to this definition")

*class* keysight.ads.de.experimental.cdf.ManagedCDF[](#keysight.ads.de.experimental.cdf.ManagedCDF "Link to this definition")
:   Bases: [`CDFBase`](#keysight.ads.de.experimental.cdf.CDFBase "keysight.ads.de.experimental.cdf.comp_def.CDFBase")

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.cdf.ManagedCDF.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* library\_name*: str*[](#keysight.ads.de.experimental.cdf.ManagedCDF.library_name "Link to this definition")

*class* keysight.ads.de.experimental.cdf.ParamDef[](#keysight.ads.de.experimental.cdf.ParamDef "Link to this definition")
:   \_\_init\_\_(*name: str*, *param\_type: [ParamType](#keysight.ads.de.experimental.cdf.ParamType "keysight.ads.de.experimental.cdf.params.ParamType")*) → None[](#keysight.ads.de.experimental.cdf.ParamDef.__init__ "Link to this definition")

    *property* callback*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.callback "Link to this definition")

    change\_type(*param\_type: [ParamType](#keysight.ads.de.experimental.cdf.ParamType "keysight.ads.de.experimental.cdf.params.ParamType")*) → None[](#keysight.ads.de.experimental.cdf.ParamDef.change_type "Link to this definition")
    :   Change the type of a parameter. This may require changing the default value.

    *property* choices*: list[str]*[](#keysight.ads.de.experimental.cdf.ParamDef.choices "Link to this definition")

    *property* default\_oa\_param*: [OAParam](../../db/parameters.md#keysight.ads.de.db.OAParam "keysight.ads.de.db._pcell_parameters.OAParam")*[](#keysight.ads.de.experimental.cdf.ParamDef.default_oa_param "Link to this definition")
    :   Mainly for testing. Use default\_value.

    *property* default\_value*: bool | int | float | str*[](#keysight.ads.de.experimental.cdf.ParamDef.default_value "Link to this definition")

    *property* display\_condition*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.display_condition "Link to this definition")

    *property* dont\_save\_condition*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.dont_save_condition "Link to this definition")

    *property* editable\_condition*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.editable_condition "Link to this definition")

    *property* has\_callback*: bool*[](#keysight.ads.de.experimental.cdf.ParamDef.has_callback "Link to this definition")

    *property* has\_choices*: bool*[](#keysight.ads.de.experimental.cdf.ParamDef.has_choices "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.name "Link to this definition")

    *property* param\_type*: [ParamType](#keysight.ads.de.experimental.cdf.ParamType "keysight.ads.de.experimental.cdf.params.ParamType")*[](#keysight.ads.de.experimental.cdf.ParamDef.param_type "Link to this definition")

    *property* parse\_as\_cel*: bool | None*[](#keysight.ads.de.experimental.cdf.ParamDef.parse_as_cel "Link to this definition")

    *property* parse\_as\_cel\_expr*: str | None*[](#keysight.ads.de.experimental.cdf.ParamDef.parse_as_cel_expr "Link to this definition")

    *property* parse\_as\_number*: bool | None*[](#keysight.ads.de.experimental.cdf.ParamDef.parse_as_number "Link to this definition")

    *property* parse\_as\_number\_expr*: str | None*[](#keysight.ads.de.experimental.cdf.ParamDef.parse_as_number_expr "Link to this definition")

    *property* prompt*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.prompt "Link to this definition")

    set\_choices(*choices: str*) → None[](#keysight.ads.de.experimental.cdf.ParamDef.set_choices "Link to this definition")

    *property* store\_default*: bool | None*[](#keysight.ads.de.experimental.cdf.ParamDef.store_default "Link to this definition")

    *property* store\_default\_expr*: str | None*[](#keysight.ads.de.experimental.cdf.ParamDef.store_default_expr "Link to this definition")

    *property* units*: [ParamUnits](#keysight.ads.de.experimental.cdf.ParamUnits "keysight.ads.de.experimental.cdf.params.ParamUnits")*[](#keysight.ads.de.experimental.cdf.ParamDef.units "Link to this definition")

    *property* use\_condition*: str*[](#keysight.ads.de.experimental.cdf.ParamDef.use_condition "Link to this definition")

*class* keysight.ads.de.experimental.cdf.ScratchCDF[](#keysight.ads.de.experimental.cdf.ScratchCDF "Link to this definition")
:   Bases: [`CDFBase`](#keysight.ads.de.experimental.cdf.CDFBase "keysight.ads.de.experimental.cdf.comp_def.CDFBase")

    \_\_init\_\_() → None[](#keysight.ads.de.experimental.cdf.ScratchCDF.__init__ "Link to this definition")

*class* keysight.ads.de.experimental.cdf.SimInfo[](#keysight.ads.de.experimental.cdf.SimInfo "Link to this definition")
:   \_\_init\_\_(*name: str*) → None[](#keysight.ads.de.experimental.cdf.SimInfo.__init__ "Link to this definition")

    cdf\_name\_from\_sim\_param\_name(*sim\_param\_name: str*) → str[](#keysight.ads.de.experimental.cdf.SimInfo.cdf_name_from_sim_param_name "Link to this definition")

    *property* comp\_name*: str*[](#keysight.ads.de.experimental.cdf.SimInfo.comp_name "Link to this definition")

    *property* inst\_parameters*: list[str]*[](#keysight.ads.de.experimental.cdf.SimInfo.inst_parameters "Link to this definition")

    is\_cdf\_param\_in\_inst\_parameters(*cdf\_param\_name: str*) → bool[](#keysight.ads.de.experimental.cdf.SimInfo.is_cdf_param_in_inst_parameters "Link to this definition")

    is\_cdf\_param\_in\_other\_parameters(*cdf\_param\_name: str*) → bool[](#keysight.ads.de.experimental.cdf.SimInfo.is_cdf_param_in_other_parameters "Link to this definition")

    *property* is\_empty*: bool*[](#keysight.ads.de.experimental.cdf.SimInfo.is_empty "Link to this definition")

    *property* netlist\_procedure*: str*[](#keysight.ads.de.experimental.cdf.SimInfo.netlist_procedure "Link to this definition")

    *property* other\_parameters*: list[str]*[](#keysight.ads.de.experimental.cdf.SimInfo.other_parameters "Link to this definition")

    *property* prop\_mapping*: dict[str, str]*[](#keysight.ads.de.experimental.cdf.SimInfo.prop_mapping "Link to this definition")

    set\_prop\_mapping(*prop\_mapping: str*) → None[](#keysight.ads.de.experimental.cdf.SimInfo.set_prop_mapping "Link to this definition")

    set\_term\_mapping(*term\_mapping: str*) → None[](#keysight.ads.de.experimental.cdf.SimInfo.set_term_mapping "Link to this definition")

    set\_term\_order(*term\_order: str*) → None[](#keysight.ads.de.experimental.cdf.SimInfo.set_term_order "Link to this definition")

    *property* sim\_name*: str*[](#keysight.ads.de.experimental.cdf.SimInfo.sim_name "Link to this definition")

    sim\_term\_name\_from\_term\_name(*term\_name: str*) → str[](#keysight.ads.de.experimental.cdf.SimInfo.sim_term_name_from_term_name "Link to this definition")

    *property* term\_mapping*: dict[str, str]*[](#keysight.ads.de.experimental.cdf.SimInfo.term_mapping "Link to this definition")

    *property* term\_order*: list[str]*[](#keysight.ads.de.experimental.cdf.SimInfo.term_order "Link to this definition")

*class* keysight.ads.de.experimental.cdf.ViewInfo[](#keysight.ads.de.experimental.cdf.ViewInfo "Link to this definition")
:   \_\_init\_\_(*name: str*) → None[](#keysight.ads.de.experimental.cdf.ViewInfo.__init__ "Link to this definition")

    cdf\_name\_from\_sim\_param\_name(*sim\_param\_name: str*) → str[](#keysight.ads.de.experimental.cdf.ViewInfo.cdf_name_from_sim_param_name "Link to this definition")

    *property* inst\_parameters*: list[str]*[](#keysight.ads.de.experimental.cdf.ViewInfo.inst_parameters "Link to this definition")

    is\_cdf\_param\_in\_parameters(*cdf\_param\_name: str*) → bool[](#keysight.ads.de.experimental.cdf.ViewInfo.is_cdf_param_in_parameters "Link to this definition")

    *property* is\_empty*: bool*[](#keysight.ads.de.experimental.cdf.ViewInfo.is_empty "Link to this definition")

    *property* module\_name*: str*[](#keysight.ads.de.experimental.cdf.ViewInfo.module_name "Link to this definition")

    *property* netlist\_procedure*: str*[](#keysight.ads.de.experimental.cdf.ViewInfo.netlist_procedure "Link to this definition")

    *property* parameters*: list[str]*[](#keysight.ads.de.experimental.cdf.ViewInfo.parameters "Link to this definition")

    *property* prop\_mapping*: dict[str, str]*[](#keysight.ads.de.experimental.cdf.ViewInfo.prop_mapping "Link to this definition")

    set\_prop\_mapping(*prop\_mapping: str*) → None[](#keysight.ads.de.experimental.cdf.ViewInfo.set_prop_mapping "Link to this definition")

    set\_term\_mapping(*term\_mapping: str*) → None[](#keysight.ads.de.experimental.cdf.ViewInfo.set_term_mapping "Link to this definition")

    set\_term\_order(*term\_order: str*) → None[](#keysight.ads.de.experimental.cdf.ViewInfo.set_term_order "Link to this definition")

    sim\_term\_name\_from\_term\_name(*term\_name: str*) → str[](#keysight.ads.de.experimental.cdf.ViewInfo.sim_term_name_from_term_name "Link to this definition")

    *property* term\_mapping*: dict[str, str]*[](#keysight.ads.de.experimental.cdf.ViewInfo.term_mapping "Link to this definition")

    *property* term\_order*: list[str]*[](#keysight.ads.de.experimental.cdf.ViewInfo.term_order "Link to this definition")

    *property* view\_name*: str*[](#keysight.ads.de.experimental.cdf.ViewInfo.view_name "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.experimental.cdf.ParamType[](#keysight.ads.de.experimental.cdf.ParamType "Link to this definition")
:   Bases: `Enum`

    The type of a CDF Parameter - determines how values are stored.

    UNKNOWN *= <ParamType.UNKNOWN: -1>*[](#keysight.ads.de.experimental.cdf.ParamType.UNKNOWN "Link to this definition")

    STRING *= <ParamType.STRING: 0>*[](#keysight.ads.de.experimental.cdf.ParamType.STRING "Link to this definition")

    INT *= <ParamType.INT: 1>*[](#keysight.ads.de.experimental.cdf.ParamType.INT "Link to this definition")

    FLOAT *= <ParamType.FLOAT: 2>*[](#keysight.ads.de.experimental.cdf.ParamType.FLOAT "Link to this definition")

    RADIO *= <ParamType.RADIO: 3>*[](#keysight.ads.de.experimental.cdf.ParamType.RADIO "Link to this definition")
    :   Has choices - stored as a string.

    CYCLIC *= <ParamType.CYCLIC: 4>*[](#keysight.ads.de.experimental.cdf.ParamType.CYCLIC "Link to this definition")
    :   Has choices - stored as a string.

    BOOLEAN *= <ParamType.BOOLEAN: 5>*[](#keysight.ads.de.experimental.cdf.ParamType.BOOLEAN "Link to this definition")
    :   Should be True/False, but stored as an int.

    BUTTON *= <ParamType.BUTTON: 6>*[](#keysight.ads.de.experimental.cdf.ParamType.BUTTON "Link to this definition")
    :   Not stored as a value.

    NETSET *= <ParamType.NETSET: 7>*[](#keysight.ads.de.experimental.cdf.ParamType.NETSET "Link to this definition")
    :   Not stored as a value. Used for net connections.

*class* keysight.ads.de.experimental.cdf.ParamUnits[](#keysight.ads.de.experimental.cdf.ParamUnits "Link to this definition")
:   Bases: `Enum`

    The units used for a CDF Parameter.

    UNKNOWN *= <ParamUnits.UNKNOWN: -1>*[](#keysight.ads.de.experimental.cdf.ParamUnits.UNKNOWN "Link to this definition")

    RESISTANCE *= <ParamUnits.RESISTANCE: 0>*[](#keysight.ads.de.experimental.cdf.ParamUnits.RESISTANCE "Link to this definition")

    CAPACITANCE *= <ParamUnits.CAPACITANCE: 1>*[](#keysight.ads.de.experimental.cdf.ParamUnits.CAPACITANCE "Link to this definition")

    INDUCTANCE *= <ParamUnits.INDUCTANCE: 2>*[](#keysight.ads.de.experimental.cdf.ParamUnits.INDUCTANCE "Link to this definition")

    CONDUCTANCE *= <ParamUnits.CONDUCTANCE: 3>*[](#keysight.ads.de.experimental.cdf.ParamUnits.CONDUCTANCE "Link to this definition")

    TIME *= <ParamUnits.TIME: 4>*[](#keysight.ads.de.experimental.cdf.ParamUnits.TIME "Link to this definition")

    FREQUENCY *= <ParamUnits.FREQUENCY: 5>*[](#keysight.ads.de.experimental.cdf.ParamUnits.FREQUENCY "Link to this definition")

    POWER *= <ParamUnits.POWER: 6>*[](#keysight.ads.de.experimental.cdf.ParamUnits.POWER "Link to this definition")

    POWER\_DB *= <ParamUnits.POWER\_DB: 7>*[](#keysight.ads.de.experimental.cdf.ParamUnits.POWER_DB "Link to this definition")

    LENGTH *= <ParamUnits.LENGTH: 8>*[](#keysight.ads.de.experimental.cdf.ParamUnits.LENGTH "Link to this definition")

    LENGTH\_ENGLISH *= <ParamUnits.LENGTH\_ENGLISH: 9>*[](#keysight.ads.de.experimental.cdf.ParamUnits.LENGTH_ENGLISH "Link to this definition")

    ANGLE *= <ParamUnits.ANGLE: 10>*[](#keysight.ads.de.experimental.cdf.ParamUnits.ANGLE "Link to this definition")

    VOLTAGE *= <ParamUnits.VOLTAGE: 11>*[](#keysight.ads.de.experimental.cdf.ParamUnits.VOLTAGE "Link to this definition")

    CURRENT *= <ParamUnits.CURRENT: 12>*[](#keysight.ads.de.experimental.cdf.ParamUnits.CURRENT "Link to this definition")

    TEMPERATURE *= <ParamUnits.TEMPERATURE: 13>*[](#keysight.ads.de.experimental.cdf.ParamUnits.TEMPERATURE "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.de.experimental.cdf.cell\_cdf(*lib\_or\_cell: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library") | [Cell](../../cell.md#keysight.ads.de.Cell "keysight.ads.de._core.cell.Cell")*, *cell\_name: str | None = None*) → [CellCDF](#keysight.ads.de.experimental.cdf.CellCDF "keysight.ads.de.experimental.cdf.comp_def.CellCDF")[](#keysight.ads.de.experimental.cdf.cell_cdf "Link to this definition")

keysight.ads.de.experimental.cdf.find\_cell\_cdf(*lib\_or\_cell: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *cell\_name: str*) → [CellCDF](#keysight.ads.de.experimental.cdf.CellCDF "keysight.ads.de.experimental.cdf.comp_def.CellCDF") | None[](#keysight.ads.de.experimental.cdf.find_cell_cdf "Link to this definition")

keysight.ads.de.experimental.cdf.find\_cell\_cdf(*lib\_or\_cell: [Cell](../../cell.md#keysight.ads.de.Cell "keysight.ads.de._core.cell.Cell")*) → [CellCDF](#keysight.ads.de.experimental.cdf.CellCDF "keysight.ads.de.experimental.cdf.comp_def.CellCDF") | None

keysight.ads.de.experimental.cdf.find\_library\_cdf(*lib: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*) → [LibraryCDF](#keysight.ads.de.experimental.cdf.LibraryCDF "keysight.ads.de.experimental.cdf.comp_def.LibraryCDF") | None[](#keysight.ads.de.experimental.cdf.find_library_cdf "Link to this definition")

keysight.ads.de.experimental.cdf.library\_cdf(*lib: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*) → [LibraryCDF](#keysight.ads.de.experimental.cdf.LibraryCDF "keysight.ads.de.experimental.cdf.comp_def.LibraryCDF")[](#keysight.ads.de.experimental.cdf.library_cdf "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/experimental/commands.md === -->

# Commands[](#module-keysight.ads.de.experimental.commands "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.commands.DesignTrackingPainter[](#keysight.ads.de.experimental.commands.DesignTrackingPainter "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.commands.DesignTrackingPainter.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    display\_message\_box\_text(*text: str*) → None[](#keysight.ads.de.experimental.commands.DesignTrackingPainter.display_message_box_text "Link to this definition")

    display\_tracking\_text(*text: str*) → None[](#keysight.ads.de.experimental.commands.DesignTrackingPainter.display_tracking_text "Link to this definition")

    draw\_polygon(*polygon: [GenPolygon](../db/genpolyline.md#keysight.ads.de.db.GenPolygon "keysight.ads.de.db.GenPolygon")*) → None[](#keysight.ads.de.experimental.commands.DesignTrackingPainter.draw_polygon "Link to this definition")

    draw\_polygon(*polygon: [GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db.GenPolygonWithHoles")*) → None

    draw\_polygon\_points(*points: list[tuple[float, float]]*) → None[](#keysight.ads.de.experimental.commands.DesignTrackingPainter.draw_polygon_points "Link to this definition")

    draw\_polygon\_points(*points: list['PointUU']*) → None

    draw\_polyline\_points(*points: list[tuple[float, float]]*) → None[](#keysight.ads.de.experimental.commands.DesignTrackingPainter.draw_polyline_points "Link to this definition")

    draw\_polyline\_points(*points: list['PointUU']*) → None

*class* keysight.ads.de.experimental.commands.CommandInfo[](#keysight.ads.de.experimental.commands.CommandInfo "Link to this definition")
:   \_\_init\_\_(*cmdName: str | None = None*)[](#keysight.ads.de.experimental.commands.CommandInfo.__init__ "Link to this definition")

    *property* click\_callback*: object*[](#keysight.ads.de.experimental.commands.CommandInfo.click_callback "Link to this definition")

    *property* command\_name*: str*[](#keysight.ads.de.experimental.commands.CommandInfo.command_name "Link to this definition")

    *property* keypress\_callback*: object*[](#keysight.ads.de.experimental.commands.CommandInfo.keypress_callback "Link to this definition")

    *property* quick\_help\_text*: str*[](#keysight.ads.de.experimental.commands.CommandInfo.quick_help_text "Link to this definition")

    *property* tracking\_callback*: object*[](#keysight.ads.de.experimental.commands.CommandInfo.tracking_callback "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.de.experimental.commands.start\_design\_command(*design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*, *cmdInfo: [CommandInfo](#keysight.ads.de.experimental.commands.CommandInfo "keysight.ads.de.experimental.commands.CommandInfo")*) → None[](#keysight.ads.de.experimental.commands.start_design_command "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/experimental/handles.md === -->

# Handles[](#module-keysight.ads.de.experimental.handles "Link to this heading")

Extensions used by custom handles.

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.handles.Handle[](#keysight.ads.de.experimental.handles.Handle "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.handles.Handle.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* design*: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*[](#keysight.ads.de.experimental.handles.Handle.design "Link to this definition")

    *property* design\_widget*: [DesignWidget](#keysight.ads.de.experimental.handles.DesignWidget "keysight.ads.de.experimental.handles.DesignWidget")*[](#keysight.ads.de.experimental.handles.Handle.design_widget "Link to this definition")

    *property* handle\_id*: int*[](#keysight.ads.de.experimental.handles.Handle.handle_id "Link to this definition")

    *property* handle\_type*: [HandleType](#keysight.ads.de.experimental.handles.HandleType "keysight.ads.de.experimental.handles.HandleType")*[](#keysight.ads.de.experimental.handles.Handle.handle_type "Link to this definition")

    *property* location*: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*[](#keysight.ads.de.experimental.handles.Handle.location "Link to this definition")

*class* keysight.ads.de.experimental.handles.DesignWidget[](#keysight.ads.de.experimental.handles.DesignWidget "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.handles.DesignWidget.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *static* from\_window(*window: [Window](../app/window.md#keysight.ads.de.app.Window "keysight.ads.de.app.Window")*) → [DesignWidget](#keysight.ads.de.experimental.handles.DesignWidget "keysight.ads.de.experimental.handles.DesignWidget")[](#keysight.ads.de.experimental.handles.DesignWidget.from_window "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.experimental.handles.HandleType[](#keysight.ads.de.experimental.handles.HandleType "Link to this definition")
:   Bases: `Enum`

    COMPONENT\_TEXT\_HANDLE *= <HandleType.COMPONENT\_TEXT\_HANDLE: 5>*[](#keysight.ads.de.experimental.handles.HandleType.COMPONENT_TEXT_HANDLE "Link to this definition")

    EDGE\_HANDLE *= <HandleType.EDGE\_HANDLE: 2>*[](#keysight.ads.de.experimental.handles.HandleType.EDGE_HANDLE "Link to this definition")

    ENDPOINT\_HANDLE *= <HandleType.ENDPOINT\_HANDLE: 4>*[](#keysight.ads.de.experimental.handles.HandleType.ENDPOINT_HANDLE "Link to this definition")

    MOVE\_HANDLE *= <HandleType.MOVE\_HANDLE: 0>*[](#keysight.ads.de.experimental.handles.HandleType.MOVE_HANDLE "Link to this definition")

    OVERLAP\_ZONE\_HANDLE *= <HandleType.OVERLAP\_ZONE\_HANDLE: 6>*[](#keysight.ads.de.experimental.handles.HandleType.OVERLAP_ZONE_HANDLE "Link to this definition")

    ROTATION\_HANDLE *= <HandleType.ROTATION\_HANDLE: 1>*[](#keysight.ads.de.experimental.handles.HandleType.ROTATION_HANDLE "Link to this definition")

    VERTEX\_HANDLE *= <HandleType.VERTEX\_HANDLE: 3>*[](#keysight.ads.de.experimental.handles.HandleType.VERTEX_HANDLE "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.de.experimental.handles.create\_custom\_handle\_for\_instance(*inst: [Instance](../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*, *h\_id: int*, *handle\_type: [HandleType](#keysight.ads.de.experimental.handles.HandleType "keysight.ads.de.experimental.handles.HandleType")*, *pt: tuple[float, float]*, *widget: [DesignWidget](#keysight.ads.de.experimental.handles.DesignWidget "keysight.ads.de.experimental.handles.DesignWidget")*, *clickHandler: Callable[[[Window](../app/window.md#keysight.ads.de.app.Window "keysight.ads.de.app.Window"), [Instance](../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance"), [Handle](#keysight.ads.de.experimental.handles.Handle "keysight.ads.de.experimental.handles.Handle")], None]*, *menuGenerator: Callable[[[Window](../app/window.md#keysight.ads.de.app.Window "keysight.ads.de.app.Window"), [Instance](../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance"), [Handle](#keysight.ads.de.experimental.handles.Handle "keysight.ads.de.experimental.handles.Handle")], [PopupMenu](../app/action.md#keysight.ads.de.app.PopupMenu "keysight.ads.de.app.PopupMenu")] | None*) → [Handle](#keysight.ads.de.experimental.handles.Handle "keysight.ads.de.experimental.handles.Handle")[](#keysight.ads.de.experimental.handles.create_custom_handle_for_instance "Link to this definition")

keysight.ads.de.experimental.handles.register\_handle\_generator(*lib\_name: str*, *cell\_name: str*, *generator: Callable[[[Instance](../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance"), [DesignWidget](#keysight.ads.de.experimental.handles.DesignWidget "keysight.ads.de.experimental.handles.DesignWidget")], None]*) → None[](#keysight.ads.de.experimental.handles.register_handle_generator "Link to this definition")

keysight.ads.de.experimental.handles.unregister\_handle\_generators\_for\_library(*lib\_name: str*) → None[](#keysight.ads.de.experimental.handles.unregister_handle_generators_for_library "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/experimental/symbol.md === -->

# Symbol Generator[](#module-keysight.ads.de.experimental.generate_symbol "Link to this heading")

Functions for Generate Symbol.

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.generate\_symbol.SymbolGenerator[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator "Link to this definition")
:   \_\_init\_\_(*symbol\_design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *source\_design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *lead\_len: float*, *lead\_spacing: float*)[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.__init__ "Link to this definition")

    generate\_symbol() → None[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.generate_symbol "Link to this definition")

    *property* is\_add\_ref\_pin*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_add_ref_pin "Link to this definition")

    *property* is\_dual\_symbol\_type*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_dual_symbol_type "Link to this definition")

    *property* is\_pin\_one\_warn\_off*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_pin_one_warn_off "Link to this definition")

    *property* is\_use\_one\_pin\_per\_em\_port*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_use_one_pin_per_em_port "Link to this definition")

    *property* is\_use\_pin\_net\_text\_label*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_use_pin_net_text_label "Link to this definition")

    *property* is\_use\_single\_line\_body*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.is_use_single_line_body "Link to this definition")

    *property* order*: [OrderType](#keysight.ads.de.experimental.generate_symbol.OrderType "keysight.ads.de.experimental.generate_symbol.OrderType")*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.order "Link to this definition")

    *property* pin\_shape*: str*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.pin_shape "Link to this definition")

    *property* should\_replace*: bool*[](#keysight.ads.de.experimental.generate_symbol.SymbolGenerator.should_replace "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.experimental.generate\_symbol.OrderType[](#keysight.ads.de.experimental.generate_symbol.OrderType "Link to this definition")
:   Bases: `Enum`

    ORDER\_LOCATION *= 0*[](#keysight.ads.de.experimental.generate_symbol.OrderType.ORDER_LOCATION "Link to this definition")

    ORDER\_NUMBER1 *= 1*[](#keysight.ads.de.experimental.generate_symbol.OrderType.ORDER_NUMBER1 "Link to this definition")

    ORDER\_NUMBER2 *= 2*[](#keysight.ads.de.experimental.generate_symbol.OrderType.ORDER_NUMBER2 "Link to this definition")

    ORDER\_NUMBER3 *= 3*[](#keysight.ads.de.experimental.generate_symbol.OrderType.ORDER_NUMBER3 "Link to this definition")

    ORDER\_NUMBER4 *= 4*[](#keysight.ads.de.experimental.generate_symbol.OrderType.ORDER_NUMBER4 "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/experimental/pro_view.md === -->

# xxPro View[](#module-keysight.ads.de.experimental.pro_view "Link to this heading")

## Functions[](#functions "Link to this heading")

keysight.ads.de.experimental.pro\_view.create\_pro\_view(*pro\_lcv: [de.LCVName](../cellviewref.md#keysight.ads.de.LCVName "keysight.ads.de.LCVName")*, *tool: str*, *input\_lcv: [de.LCVName](../cellviewref.md#keysight.ads.de.LCVName "keysight.ads.de.LCVName")*, *substr: str*) → None[](#keysight.ads.de.experimental.pro_view.create_pro_view "Link to this definition")
:   Create an SI/PE/RFpro view.


---

<!-- === 来源: pypde/docs/reference/de/experimental/polygon_utils.md === -->

# Polygon Utilities[](#module-keysight.ads.de.experimental.polygon_utils "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.polygon\_utils.Oversizer[](#keysight.ads.de.experimental.polygon_utils.Oversizer "Link to this definition")
:   *property* minimum\_vertex\_distance*: float*[](#keysight.ads.de.experimental.polygon_utils.Oversizer.minimum_vertex_distance "Link to this definition")

    *property* miter\_angle\_degrees*: float*[](#keysight.ads.de.experimental.polygon_utils.Oversizer.miter_angle_degrees "Link to this definition")

    *property* oversize\_amount*: float*[](#keysight.ads.de.experimental.polygon_utils.Oversizer.oversize_amount "Link to this definition")

*class* keysight.ads.de.experimental.polygon\_utils.PolygonOversizer[](#keysight.ads.de.experimental.polygon_utils.PolygonOversizer "Link to this definition")
:   Bases: [`Oversizer`](#keysight.ads.de.experimental.polygon_utils.Oversizer "keysight.ads.de.experimental.polygon_utils.Oversizer")

    \_\_init\_\_(*polygon: [GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")*, *design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design") | None = None*, *oversize\_amount: float = 0.0*, *miter\_angle\_degrees: float = 0.0*, *minimum\_vertex\_distance: float = 0.0*)[](#keysight.ads.de.experimental.polygon_utils.PolygonOversizer.__init__ "Link to this definition")

    oversize() → list[[GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")][](#keysight.ads.de.experimental.polygon_utils.PolygonOversizer.oversize "Link to this definition")

*class* keysight.ads.de.experimental.polygon\_utils.PolygonVertexToArcConverter[](#keysight.ads.de.experimental.polygon_utils.PolygonVertexToArcConverter "Link to this definition")
:   Bases: [`VertexToArcConverter`](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter "keysight.ads.de.experimental.polygon_utils.VertexToArcConverter")

    \_\_init\_\_(*polygon: [GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")*, *design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design") | None = None*, *radius: float = 0.0*, *arc\_resolution\_degrees: float = 5.0*, *minimum\_vertex\_distance: float = 0.0*)[](#keysight.ads.de.experimental.polygon_utils.PolygonVertexToArcConverter.__init__ "Link to this definition")

    convert() → list[[GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")][](#keysight.ads.de.experimental.polygon_utils.PolygonVertexToArcConverter.convert "Link to this definition")

*class* keysight.ads.de.experimental.polygon\_utils.ShapeOversizer[](#keysight.ads.de.experimental.polygon_utils.ShapeOversizer "Link to this definition")
:   Bases: [`Oversizer`](#keysight.ads.de.experimental.polygon_utils.Oversizer "keysight.ads.de.experimental.polygon_utils.Oversizer")

    \_\_init\_\_(*shape: [Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")*, *oversizeAmount: float | None = None*, *miter\_angle\_degrees: float = 0.0*, *minimum\_vertex\_distance: float = 0.0*, *make\_copy: bool = False*)[](#keysight.ads.de.experimental.polygon_utils.ShapeOversizer.__init__ "Link to this definition")

    *property* make\_copy*: bool*[](#keysight.ads.de.experimental.polygon_utils.ShapeOversizer.make_copy "Link to this definition")

    oversize() → list[[Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")][](#keysight.ads.de.experimental.polygon_utils.ShapeOversizer.oversize "Link to this definition")

*class* keysight.ads.de.experimental.polygon\_utils.ShapeVertexToArcConverter[](#keysight.ads.de.experimental.polygon_utils.ShapeVertexToArcConverter "Link to this definition")
:   Bases: [`VertexToArcConverter`](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter "keysight.ads.de.experimental.polygon_utils.VertexToArcConverter")

    \_\_init\_\_(*shape: [Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")*, *radius: float | None = None*, *arc\_resolution\_degrees: float = 5.0*, *minimum\_vertex\_distance: float = 0.0*)[](#keysight.ads.de.experimental.polygon_utils.ShapeVertexToArcConverter.__init__ "Link to this definition")

    convert() → list[[Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")][](#keysight.ads.de.experimental.polygon_utils.ShapeVertexToArcConverter.convert "Link to this definition")

*class* keysight.ads.de.experimental.polygon\_utils.VertexToArcConverter[](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* arc\_resolution*: float*[](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter.arc_resolution "Link to this definition")

    *property* minimum\_vertex\_distance*: float*[](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter.minimum_vertex_distance "Link to this definition")

    *property* radius*: float*[](#keysight.ads.de.experimental.polygon_utils.VertexToArcConverter.radius "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.de.experimental.polygon\_utils.convert\_vertices\_to\_arcs(*shape: [Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")*, *radius: float = 0*) → list[[Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")][](#keysight.ads.de.experimental.polygon_utils.convert_vertices_to_arcs "Link to this definition")

keysight.ads.de.experimental.polygon\_utils.oversize(*shape: [Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")*, *oversize\_amount: float = 0*, *make\_copy: bool = False*) → list[[Shape](../db_uu/db_uu.md#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")][](#keysight.ads.de.experimental.polygon_utils.oversize "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/experimental/text_maker.md === -->

# Text Maker[](#module-keysight.ads.de.experimental.text_maker "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.text\_maker.TextMaker[](#keysight.ads.de.experimental.text_maker.TextMaker "Link to this definition")
:   TFloatTuple[](#keysight.ads.de.experimental.text_maker.TextMaker.TFloatTuple "Link to this definition")
    :   alias of `tuple`[`float`, `float`]

    TUserPoint[](#keysight.ads.de.experimental.text_maker.TextMaker.TUserPoint "Link to this definition")
    :   alias of `Union`[[`PointUU`](../points.md#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU"), `tuple`[`float`, `float`]]

    \_\_init\_\_(*design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.experimental.text_maker.TextMaker.__init__ "Link to this definition")

    add\_attr\_display(*obj: [ApolloObject](../db_uu/db_uu.md#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject") | [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *attr\_type: [DesignAttrType](../db/enums.md#keysight.ads.de.db.DesignAttrType "keysight.ads.de.db._db_types.DesignAttrType") | [InstAttrType](../db/enums.md#keysight.ads.de.db.InstAttrType "keysight.ads.de.db._db_types.InstAttrType") | [InstTermAttrType](../db/enums.md#keysight.ads.de.db.InstTermAttrType "keysight.ads.de.db._db_types.InstTermAttrType") | [NetAttrType](../db/enums.md#keysight.ads.de.db.NetAttrType "keysight.ads.de.db._db_types.NetAttrType") | [TermAttrType](../db/enums.md#keysight.ads.de.db.TermAttrType "keysight.ads.de.db._db_types.TermAttrType")*, *layer\_id: [LayerId](../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *origin: [PointUU](../points.md#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU") | tuple[float, float]*, *display\_format: [TextDisplayFormat](../db/enums.md#keysight.ads.de.db.TextDisplayFormat "keysight.ads.de.db._db_types.TextDisplayFormat") = TextDisplayFormat.VALUE*) → [AttrDisplay](../db_uu/db_uu.md#keysight.ads.de.db_uu.AttrDisplay "keysight.ads.de.db_uu._db_x.AttrDisplay")[](#keysight.ads.de.experimental.text_maker.TextMaker.add_attr_display "Link to this definition")

    add\_inst\_attr\_display(*inst: [Instance](../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*, *master\_attribute: [DesignAttrType](../db/enums.md#keysight.ads.de.db.DesignAttrType "keysight.ads.de.db._db_types.DesignAttrType")*, *layer\_id: [LayerId](../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *origin: [PointUU](../points.md#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU") | tuple[float, float]*, *display\_format: [TextDisplayFormat](../db/enums.md#keysight.ads.de.db.TextDisplayFormat "keysight.ads.de.db._db_types.TextDisplayFormat") = TextDisplayFormat.VALUE*) → [InstAttrDisplay](../db_uu/db_uu.md#keysight.ads.de.db_uu.InstAttrDisplay "keysight.ads.de.db_uu._db_x.InstAttrDisplay")[](#keysight.ads.de.experimental.text_maker.TextMaker.add_inst_attr_display "Link to this definition")

    add\_text(*layer\_id: [LayerId](../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *text: str*, *origin: [PointUU](../points.md#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU") | tuple[float, float]*) → [Text](../db_uu/db_uu.md#keysight.ads.de.db_uu.Text "keysight.ads.de.db_uu._db_x.Text")[](#keysight.ads.de.experimental.text_maker.TextMaker.add_text "Link to this definition")

    *property* align*: [TextAlignment](../db/enums.md#keysight.ads.de.db.TextAlignment "keysight.ads.de.db._db_types.TextAlignment")*[](#keysight.ads.de.experimental.text_maker.TextMaker.align "Link to this definition")

    *property* font\_name*: str*[](#keysight.ads.de.experimental.text_maker.TextMaker.font_name "Link to this definition")

    *property* height*: float*[](#keysight.ads.de.experimental.text_maker.TextMaker.height "Link to this definition")

    *property* is\_drafting*: bool*[](#keysight.ads.de.experimental.text_maker.TextMaker.is_drafting "Link to this definition")

    *property* orient*: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*[](#keysight.ads.de.experimental.text_maker.TextMaker.orient "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/experimental/preferences.md === -->

# Preferences[](#module-keysight.ads.de.experimental.preferences "Link to this heading")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.experimental.preferences.WorkspacePreference[](#keysight.ads.de.experimental.preferences.WorkspacePreference "Link to this definition")
:   Bases: `pybind11_object`

    Members:

    PATH\_BEND

    PATH\_MITER\_PERCENT

    PATH\_ENDCAP

    PATH\_LAYER

    TEXT\_STRING

    TEXT\_FONT

    TEXT\_POINT

    TEXT\_JUST

    TEXT\_ANGLE

    TEXT\_ABSOLUTE

    INST\_NAME\_LAYER

    INST\_ID\_LAYER

    INST\_PARAM1\_LAYER

    INST\_TEXT\_FONT

    INST\_TEXT\_POINT

    INST\_TEXT\_ROWS

    INST\_TEXT\_ADD\_OPT

    INST\_TEXT\_PREC

    WIRE\_LABEL\_FONT

    WIRE\_LABEL\_POINT

    WIRE\_LABEL\_COLOR

    FIXED\_INST\_HIGHLIGHT\_COLOR

    LOCKED\_INST\_HIGHLIGHT\_COLOR

    OVERSIZE

    MITER\_ANGLE

    SCALE\_X

    SCALE\_Y

    TO\_ARC\_RADIUS

    MITER\_VERTEX\_LENGTH

    PORT\_NAME

    PORT\_TYPE

    PORT\_NUMBER

    PORT\_ORIENT

    PORT\_POWER

    PLOTTING\_DEPTH

    BBOX\_COLOR

    SELECT\_COLOR

    HIGHLIGHT\_COLOR

    PIN\_COLOR

    PIN\_SIZE

    TEE\_COLOR

    TEE\_SIZE

    PORT\_COLOR

    BG\_COLOR

    FG\_COLOR

    SELECT\_FILTER

    SELECT\_MODE

    SELECT\_BOX\_SIZE

    SELECT\_POINT\_SIZE

    ENTRY\_MODE

    ROTATION\_INC

    GRID\_DISPLAY\_X

    GRID\_DISPLAY\_Y

    GRID\_DISPLAY

    GRID\_DISPLAY\_SAME\_XY

    MAJOR\_GRID\_DISPLAY\_X

    MAJOR\_GRID\_DISPLAY\_Y

    MAJOR\_GRID\_DISPLAY

    GRID\_DISPLAY\_MODE

    GRID\_SNAP

    GRID\_SNAP\_MODE

    GRID\_COLOR

    WINDOW\_LOWER\_LEFT\_X

    WINDOW\_LOWER\_LEFT\_Y

    WINDOW\_UPPER\_RIGHT\_X

    WINDOW\_UPPER\_RIGHT\_Y

    BACKUP\_COUNT

    PLACE\_POPUP

    PLACE\_PIN\_POPUP

    CHECK\_INTERSECTION

    CHECK\_BINDING

    SHOVE\_CONNECTIONS\_ON\_COMPONENT\_PARAM\_CHANGE

    PLOT\_PIN\_NUMBERS

    PLOT\_PIN\_NAMES

    PLOT\_PIN\_NET\_NAMES

    PLOT\_PINS

    REROUTE\_WIRES

    TRACE\_TLINE\_FAMILY

    TRACE\_SIM\_MODE

    TRACE\_SINGLE\_ELEM

    TRACE\_TRAVERSE

    TRACE\_MSUB\_ID

    DSE\_SYMB\_X\_DISTANCE

    DSE\_SYMB\_Y\_DISTANCE

    DSE\_ART\_X\_DISTANCE

    DSE\_ART\_Y\_DISTANCE

    DSE\_S2L\_REPORT

    DSE\_LS2\_REPORT

    FORCE\_DELETE

    DUAL\_PLACEMENT

    CHECK\_UNCONNECTED\_PINS

    CHECK\_NODAL\_MISMATCH

    CHECK\_WIRES\_IN\_LAYOUT

    CHECK\_PIN\_VS\_PORT

    SHOW\_CONNECTED\_SCHEM

    SHOW\_CONNECTED\_LAY

    SHOW\_FIXED\_SCHEM

    SHOW\_FIXED\_LAY

    UNDO\_EDIT\_COUNT

    STEP\_REPEAT\_XSPACE

    STEP\_REPEAT\_YSPACE

    STEP\_REPEAT\_NUMROWS

    STEP\_REPEAT\_NUMCOLS

    SELECT\_BOX\_UNITS

    PIN\_SIZE\_UNITS

    TEE\_SIZE\_UNITS

    SELECT\_POINT\_UNITS

    PIN\_SNAP\_UNITS

    PIN\_SNAP\_SIZE

    KEEPOUT\_OUTLINE\_THICKNESS

    PLACE\_POPUP\_ON\_ZERO\_PARM

    AUTO\_REPEATABLE\_COMP\_PLCMNT

    DRAG\_MOVE

    DRAG\_MOVE\_THRESHOLD\_UNITS

    DRAG\_MOVE\_THRESHOLD\_SIZE

    DVE\_EPSILON

    DVE\_ARC\_CIRCLE\_RESOLUTION

    DVE\_MAX\_ERROR

    NODE\_VOLT\_COLOR

    PIN\_CURRENT\_COLOR

    NODE\_NAME\_COLOR

    COORD\_ENTRY\_POPUP

    DISP\_SUBNET\_INST\_NAMES

    SWAP\_KEEP\_INST\_NAME

    KEEP\_NODE\_NAMES

    TUNE\_SIM\_MODE

    TUNE\_RESTORE\_DDS

    TUNE\_RANGE

    TUNE\_STEP\_SIZE

    TUNE\_SCALE

    TUNE\_SNAP

    TUNE\_PARAMETER\_DISPLAY\_LONG\_NAME

    OPTIM\_COCKPIT\_UPDATE\_SCHEMATIC

    OPTIM\_COCKPIT\_SAVE\_STATE

    SET\_PASTE\_ORIGIN\_POPUP

    PRESERVE\_COPY\_PASTE\_NET\_NAMES

    MAINTAIN\_ANGLE

    DISP\_TEXT\_ORIGIN

    MIN\_PIXEL\_DISPLAY\_SIZE

    REROUTE\_TRACES

    PREF\_VERSION

    GENERIC\_ARTWORK\_SIZE

    PLOT\_LESS\_THAN\_MIN\_PIXELS

    PLOT\_DEPTH\_FOR\_LESS\_THAN\_MIN\_PIXELS

    NEW\_ROUTE\_AROUND\_INST\_TEXT

    DSE\_PREF\_LAYOUT\_LAYER

    NEW\_ROUTE\_AROUND\_INST\_SYM

    DISP\_ONSCREEN\_COORD\_MODE

    EDIT\_IN\_PLACE\_BOX\_COLOR

    DSE\_FIX\_ALL

    DSE\_KEEP\_NETS

    INST\_TEXT\_TUNE\_FORMAT

    INST\_TEXT\_OPT\_FORMAT

    INST\_TEXT\_STAT\_FORMAT

    INST\_TEXT\_DOE\_FORMAT

    INST\_TEXT\_DEACTIVE\_COLOR

    MOVE\_VERTEX\_KEEP\_RECT

    USE\_CROSS\_HAIR\_CURSOR

    DRAG\_MOVE\_HANDLE

    ORIGIN\_DISPLAY

    ORIGIN\_COLOR

    PHYSICAL\_CONN\_HIGHLIGHT\_COLOR

    LOGICAL\_CONN\_HIGHLIGHT\_COLOR

    PHYSICAL\_CONN\_DIFF\_NET\_HIGHLIGHT\_COLOR

    PLOT\_SYMB\_PIN\_ANNOT

    WORKSPACE\_LAYOUT\_PRF\_IS\_UNINITIALIZED

    AUTO\_REPEATABLE\_COMP\_PLCMNT *= <WorkspacePreference.AUTO\_REPEATABLE\_COMP\_PLCMNT: 124>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.AUTO_REPEATABLE_COMP_PLCMNT "Link to this definition")

    BACKUP\_COUNT *= <WorkspacePreference.BACKUP\_COUNT: 78>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.BACKUP_COUNT "Link to this definition")

    BBOX\_COLOR *= <WorkspacePreference.BBOX\_COLOR: 39>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.BBOX_COLOR "Link to this definition")

    BG\_COLOR *= <WorkspacePreference.BG\_COLOR: 47>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.BG_COLOR "Link to this definition")

    CHECK\_BINDING *= <WorkspacePreference.CHECK\_BINDING: 82>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.CHECK_BINDING "Link to this definition")

    CHECK\_INTERSECTION *= <WorkspacePreference.CHECK\_INTERSECTION: 81>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.CHECK_INTERSECTION "Link to this definition")

    CHECK\_NODAL\_MISMATCH *= <WorkspacePreference.CHECK\_NODAL\_MISMATCH: 103>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.CHECK_NODAL_MISMATCH "Link to this definition")

    CHECK\_PIN\_VS\_PORT *= <WorkspacePreference.CHECK\_PIN\_VS\_PORT: 105>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.CHECK_PIN_VS_PORT "Link to this definition")

    CHECK\_UNCONNECTED\_PINS *= <WorkspacePreference.CHECK\_UNCONNECTED\_PINS: 102>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.CHECK_UNCONNECTED_PINS "Link to this definition")

    CHECK\_WIRES\_IN\_LAYOUT *= <WorkspacePreference.CHECK\_WIRES\_IN\_LAYOUT: 104>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.CHECK_WIRES_IN_LAYOUT "Link to this definition")

    COORD\_ENTRY\_POPUP *= <WorkspacePreference.COORD\_ENTRY\_POPUP: 135>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.COORD_ENTRY_POPUP "Link to this definition")

    DISP\_ONSCREEN\_COORD\_MODE *= <WorkspacePreference.DISP\_ONSCREEN\_COORD\_MODE: 161>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DISP_ONSCREEN_COORD_MODE "Link to this definition")

    DISP\_SUBNET\_INST\_NAMES *= <WorkspacePreference.DISP\_SUBNET\_INST\_NAMES: 136>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DISP_SUBNET_INST_NAMES "Link to this definition")

    DISP\_TEXT\_ORIGIN *= <WorkspacePreference.DISP\_TEXT\_ORIGIN: 151>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DISP_TEXT_ORIGIN "Link to this definition")

    DRAG\_MOVE *= <WorkspacePreference.DRAG\_MOVE: 125>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DRAG_MOVE "Link to this definition")

    DRAG\_MOVE\_HANDLE *= <WorkspacePreference.DRAG\_MOVE\_HANDLE: 173>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DRAG_MOVE_HANDLE "Link to this definition")

    DRAG\_MOVE\_THRESHOLD\_SIZE *= <WorkspacePreference.DRAG\_MOVE\_THRESHOLD\_SIZE: 127>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DRAG_MOVE_THRESHOLD_SIZE "Link to this definition")

    DRAG\_MOVE\_THRESHOLD\_UNITS *= <WorkspacePreference.DRAG\_MOVE\_THRESHOLD\_UNITS: 126>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DRAG_MOVE_THRESHOLD_UNITS "Link to this definition")

    DSE\_ART\_X\_DISTANCE *= <WorkspacePreference.DSE\_ART\_X\_DISTANCE: 96>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DSE_ART_X_DISTANCE "Link to this definition")

    DSE\_ART\_Y\_DISTANCE *= <WorkspacePreference.DSE\_ART\_Y\_DISTANCE: 97>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DSE_ART_Y_DISTANCE "Link to this definition")

    DSE\_FIX\_ALL *= <WorkspacePreference.DSE\_FIX\_ALL: 163>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DSE_FIX_ALL "Link to this definition")

    DSE\_KEEP\_NETS *= <WorkspacePreference.DSE\_KEEP\_NETS: 164>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DSE_KEEP_NETS "Link to this definition")

    DSE\_LS2\_REPORT *= <WorkspacePreference.DSE\_LS2\_REPORT: 99>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DSE_LS2_REPORT "Link to this definition")

    DSE\_PREF\_LAYOUT\_LAYER *= <WorkspacePreference.DSE\_PREF\_LAYOUT\_LAYER: 159>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DSE_PREF_LAYOUT_LAYER "Link to this definition")

    DSE\_S2L\_REPORT *= <WorkspacePreference.DSE\_S2L\_REPORT: 98>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DSE_S2L_REPORT "Link to this definition")

    DSE\_SYMB\_X\_DISTANCE *= <WorkspacePreference.DSE\_SYMB\_X\_DISTANCE: 94>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DSE_SYMB_X_DISTANCE "Link to this definition")

    DSE\_SYMB\_Y\_DISTANCE *= <WorkspacePreference.DSE\_SYMB\_Y\_DISTANCE: 95>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DSE_SYMB_Y_DISTANCE "Link to this definition")

    DUAL\_PLACEMENT *= <WorkspacePreference.DUAL\_PLACEMENT: 101>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DUAL_PLACEMENT "Link to this definition")

    DVE\_ARC\_CIRCLE\_RESOLUTION *= <WorkspacePreference.DVE\_ARC\_CIRCLE\_RESOLUTION: 130>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DVE_ARC_CIRCLE_RESOLUTION "Link to this definition")

    DVE\_EPSILON *= <WorkspacePreference.DVE\_EPSILON: 128>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DVE_EPSILON "Link to this definition")

    DVE\_MAX\_ERROR *= <WorkspacePreference.DVE\_MAX\_ERROR: 131>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.DVE_MAX_ERROR "Link to this definition")

    EDIT\_IN\_PLACE\_BOX\_COLOR *= <WorkspacePreference.EDIT\_IN\_PLACE\_BOX\_COLOR: 162>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.EDIT_IN_PLACE_BOX_COLOR "Link to this definition")

    ENTRY\_MODE *= <WorkspacePreference.ENTRY\_MODE: 55>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.ENTRY_MODE "Link to this definition")

    FG\_COLOR *= <WorkspacePreference.FG\_COLOR: 48>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.FG_COLOR "Link to this definition")

    FIXED\_INST\_HIGHLIGHT\_COLOR *= <WorkspacePreference.FIXED\_INST\_HIGHLIGHT\_COLOR: 21>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.FIXED_INST_HIGHLIGHT_COLOR "Link to this definition")

    FORCE\_DELETE *= <WorkspacePreference.FORCE\_DELETE: 100>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.FORCE_DELETE "Link to this definition")

    GENERIC\_ARTWORK\_SIZE *= <WorkspacePreference.GENERIC\_ARTWORK\_SIZE: 155>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.GENERIC_ARTWORK_SIZE "Link to this definition")

    GRID\_COLOR *= <WorkspacePreference.GRID\_COLOR: 67>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.GRID_COLOR "Link to this definition")

    GRID\_DISPLAY *= <WorkspacePreference.GRID\_DISPLAY: 59>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.GRID_DISPLAY "Link to this definition")

    GRID\_DISPLAY\_MODE *= <WorkspacePreference.GRID\_DISPLAY\_MODE: 64>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.GRID_DISPLAY_MODE "Link to this definition")

    GRID\_DISPLAY\_SAME\_XY *= <WorkspacePreference.GRID\_DISPLAY\_SAME\_XY: 60>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.GRID_DISPLAY_SAME_XY "Link to this definition")

    GRID\_DISPLAY\_X *= <WorkspacePreference.GRID\_DISPLAY\_X: 57>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.GRID_DISPLAY_X "Link to this definition")

    GRID\_DISPLAY\_Y *= <WorkspacePreference.GRID\_DISPLAY\_Y: 58>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.GRID_DISPLAY_Y "Link to this definition")

    GRID\_SNAP *= <WorkspacePreference.GRID\_SNAP: 65>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.GRID_SNAP "Link to this definition")

    GRID\_SNAP\_MODE *= <WorkspacePreference.GRID\_SNAP\_MODE: 66>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.GRID_SNAP_MODE "Link to this definition")

    HIGHLIGHT\_COLOR *= <WorkspacePreference.HIGHLIGHT\_COLOR: 41>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.HIGHLIGHT_COLOR "Link to this definition")

    INST\_ID\_LAYER *= <WorkspacePreference.INST\_ID\_LAYER: 11>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_ID_LAYER "Link to this definition")

    INST\_NAME\_LAYER *= <WorkspacePreference.INST\_NAME\_LAYER: 10>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_NAME_LAYER "Link to this definition")

    INST\_PARAM1\_LAYER *= <WorkspacePreference.INST\_PARAM1\_LAYER: 12>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_PARAM1_LAYER "Link to this definition")

    INST\_TEXT\_ADD\_OPT *= <WorkspacePreference.INST\_TEXT\_ADD\_OPT: 16>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_TEXT_ADD_OPT "Link to this definition")

    INST\_TEXT\_DEACTIVE\_COLOR *= <WorkspacePreference.INST\_TEXT\_DEACTIVE\_COLOR: 170>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_TEXT_DEACTIVE_COLOR "Link to this definition")

    INST\_TEXT\_DOE\_FORMAT *= <WorkspacePreference.INST\_TEXT\_DOE\_FORMAT: 169>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_TEXT_DOE_FORMAT "Link to this definition")

    INST\_TEXT\_FONT *= <WorkspacePreference.INST\_TEXT\_FONT: 13>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_TEXT_FONT "Link to this definition")

    INST\_TEXT\_OPT\_FORMAT *= <WorkspacePreference.INST\_TEXT\_OPT\_FORMAT: 167>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_TEXT_OPT_FORMAT "Link to this definition")

    INST\_TEXT\_POINT *= <WorkspacePreference.INST\_TEXT\_POINT: 14>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_TEXT_POINT "Link to this definition")

    INST\_TEXT\_PREC *= <WorkspacePreference.INST\_TEXT\_PREC: 17>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_TEXT_PREC "Link to this definition")

    INST\_TEXT\_ROWS *= <WorkspacePreference.INST\_TEXT\_ROWS: 15>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_TEXT_ROWS "Link to this definition")

    INST\_TEXT\_STAT\_FORMAT *= <WorkspacePreference.INST\_TEXT\_STAT\_FORMAT: 168>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_TEXT_STAT_FORMAT "Link to this definition")

    INST\_TEXT\_TUNE\_FORMAT *= <WorkspacePreference.INST\_TEXT\_TUNE\_FORMAT: 166>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.INST_TEXT_TUNE_FORMAT "Link to this definition")

    KEEPOUT\_OUTLINE\_THICKNESS *= <WorkspacePreference.KEEPOUT\_OUTLINE\_THICKNESS: 122>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.KEEPOUT_OUTLINE_THICKNESS "Link to this definition")

    KEEP\_NODE\_NAMES *= <WorkspacePreference.KEEP\_NODE\_NAMES: 138>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.KEEP_NODE_NAMES "Link to this definition")

    LOCKED\_INST\_HIGHLIGHT\_COLOR *= <WorkspacePreference.LOCKED\_INST\_HIGHLIGHT\_COLOR: 22>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.LOCKED_INST_HIGHLIGHT_COLOR "Link to this definition")

    LOGICAL\_CONN\_HIGHLIGHT\_COLOR *= <WorkspacePreference.LOGICAL\_CONN\_HIGHLIGHT\_COLOR: 177>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.LOGICAL_CONN_HIGHLIGHT_COLOR "Link to this definition")

    MAINTAIN\_ANGLE *= <WorkspacePreference.MAINTAIN\_ANGLE: 150>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.MAINTAIN_ANGLE "Link to this definition")

    MAJOR\_GRID\_DISPLAY *= <WorkspacePreference.MAJOR\_GRID\_DISPLAY: 63>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.MAJOR_GRID_DISPLAY "Link to this definition")

    MAJOR\_GRID\_DISPLAY\_X *= <WorkspacePreference.MAJOR\_GRID\_DISPLAY\_X: 61>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.MAJOR_GRID_DISPLAY_X "Link to this definition")

    MAJOR\_GRID\_DISPLAY\_Y *= <WorkspacePreference.MAJOR\_GRID\_DISPLAY\_Y: 62>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.MAJOR_GRID_DISPLAY_Y "Link to this definition")

    MIN\_PIXEL\_DISPLAY\_SIZE *= <WorkspacePreference.MIN\_PIXEL\_DISPLAY\_SIZE: 152>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.MIN_PIXEL_DISPLAY_SIZE "Link to this definition")

    MITER\_ANGLE *= <WorkspacePreference.MITER\_ANGLE: 24>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.MITER_ANGLE "Link to this definition")

    MITER\_VERTEX\_LENGTH *= <WorkspacePreference.MITER\_VERTEX\_LENGTH: 28>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.MITER_VERTEX_LENGTH "Link to this definition")

    MOVE\_VERTEX\_KEEP\_RECT *= <WorkspacePreference.MOVE\_VERTEX\_KEEP\_RECT: 171>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.MOVE_VERTEX_KEEP_RECT "Link to this definition")

    NEW\_ROUTE\_AROUND\_INST\_SYM *= <WorkspacePreference.NEW\_ROUTE\_AROUND\_INST\_SYM: 160>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.NEW_ROUTE_AROUND_INST_SYM "Link to this definition")

    NEW\_ROUTE\_AROUND\_INST\_TEXT *= <WorkspacePreference.NEW\_ROUTE\_AROUND\_INST\_TEXT: 158>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.NEW_ROUTE_AROUND_INST_TEXT "Link to this definition")

    NODE\_NAME\_COLOR *= <WorkspacePreference.NODE\_NAME\_COLOR: 134>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.NODE_NAME_COLOR "Link to this definition")

    NODE\_VOLT\_COLOR *= <WorkspacePreference.NODE\_VOLT\_COLOR: 132>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.NODE_VOLT_COLOR "Link to this definition")

    OPTIM\_COCKPIT\_SAVE\_STATE *= <WorkspacePreference.OPTIM\_COCKPIT\_SAVE\_STATE: 147>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.OPTIM_COCKPIT_SAVE_STATE "Link to this definition")

    OPTIM\_COCKPIT\_UPDATE\_SCHEMATIC *= <WorkspacePreference.OPTIM\_COCKPIT\_UPDATE\_SCHEMATIC: 146>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.OPTIM_COCKPIT_UPDATE_SCHEMATIC "Link to this definition")

    ORIGIN\_COLOR *= <WorkspacePreference.ORIGIN\_COLOR: 175>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.ORIGIN_COLOR "Link to this definition")

    ORIGIN\_DISPLAY *= <WorkspacePreference.ORIGIN\_DISPLAY: 174>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.ORIGIN_DISPLAY "Link to this definition")

    OVERSIZE *= <WorkspacePreference.OVERSIZE: 23>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.OVERSIZE "Link to this definition")

    PATH\_BEND *= <WorkspacePreference.PATH\_BEND: 0>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PATH_BEND "Link to this definition")

    PATH\_ENDCAP *= <WorkspacePreference.PATH\_ENDCAP: 2>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PATH_ENDCAP "Link to this definition")

    PATH\_LAYER *= <WorkspacePreference.PATH\_LAYER: 3>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PATH_LAYER "Link to this definition")

    PATH\_MITER\_PERCENT *= <WorkspacePreference.PATH\_MITER\_PERCENT: 1>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PATH_MITER_PERCENT "Link to this definition")

    PHYSICAL\_CONN\_DIFF\_NET\_HIGHLIGHT\_COLOR *= <WorkspacePreference.PHYSICAL\_CONN\_DIFF\_NET\_HIGHLIGHT\_COLOR: 178>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PHYSICAL_CONN_DIFF_NET_HIGHLIGHT_COLOR "Link to this definition")

    PHYSICAL\_CONN\_HIGHLIGHT\_COLOR *= <WorkspacePreference.PHYSICAL\_CONN\_HIGHLIGHT\_COLOR: 176>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PHYSICAL_CONN_HIGHLIGHT_COLOR "Link to this definition")

    PIN\_COLOR *= <WorkspacePreference.PIN\_COLOR: 42>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PIN_COLOR "Link to this definition")

    PIN\_CURRENT\_COLOR *= <WorkspacePreference.PIN\_CURRENT\_COLOR: 133>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PIN_CURRENT_COLOR "Link to this definition")

    PIN\_SIZE *= <WorkspacePreference.PIN\_SIZE: 43>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PIN_SIZE "Link to this definition")

    PIN\_SIZE\_UNITS *= <WorkspacePreference.PIN\_SIZE\_UNITS: 116>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PIN_SIZE_UNITS "Link to this definition")

    PIN\_SNAP\_SIZE *= <WorkspacePreference.PIN\_SNAP\_SIZE: 121>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PIN_SNAP_SIZE "Link to this definition")

    PIN\_SNAP\_UNITS *= <WorkspacePreference.PIN\_SNAP\_UNITS: 120>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PIN_SNAP_UNITS "Link to this definition")

    PLACE\_PIN\_POPUP *= <WorkspacePreference.PLACE\_PIN\_POPUP: 80>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PLACE_PIN_POPUP "Link to this definition")

    PLACE\_POPUP *= <WorkspacePreference.PLACE\_POPUP: 79>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PLACE_POPUP "Link to this definition")

    PLACE\_POPUP\_ON\_ZERO\_PARM *= <WorkspacePreference.PLACE\_POPUP\_ON\_ZERO\_PARM: 123>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PLACE_POPUP_ON_ZERO_PARM "Link to this definition")

    PLOTTING\_DEPTH *= <WorkspacePreference.PLOTTING\_DEPTH: 38>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PLOTTING_DEPTH "Link to this definition")

    PLOT\_DEPTH\_FOR\_LESS\_THAN\_MIN\_PIXELS *= <WorkspacePreference.PLOT\_DEPTH\_FOR\_LESS\_THAN\_MIN\_PIXELS: 157>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PLOT_DEPTH_FOR_LESS_THAN_MIN_PIXELS "Link to this definition")

    PLOT\_LESS\_THAN\_MIN\_PIXELS *= <WorkspacePreference.PLOT\_LESS\_THAN\_MIN\_PIXELS: 156>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PLOT_LESS_THAN_MIN_PIXELS "Link to this definition")

    PLOT\_PINS *= <WorkspacePreference.PLOT\_PINS: 87>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PLOT_PINS "Link to this definition")

    PLOT\_PIN\_NAMES *= <WorkspacePreference.PLOT\_PIN\_NAMES: 85>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PLOT_PIN_NAMES "Link to this definition")

    PLOT\_PIN\_NET\_NAMES *= <WorkspacePreference.PLOT\_PIN\_NET\_NAMES: 86>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PLOT_PIN_NET_NAMES "Link to this definition")

    PLOT\_PIN\_NUMBERS *= <WorkspacePreference.PLOT\_PIN\_NUMBERS: 84>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PLOT_PIN_NUMBERS "Link to this definition")

    PLOT\_SYMB\_PIN\_ANNOT *= <WorkspacePreference.PLOT\_SYMB\_PIN\_ANNOT: 179>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PLOT_SYMB_PIN_ANNOT "Link to this definition")

    PORT\_COLOR *= <WorkspacePreference.PORT\_COLOR: 46>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PORT_COLOR "Link to this definition")

    PORT\_NAME *= <WorkspacePreference.PORT\_NAME: 33>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PORT_NAME "Link to this definition")

    PORT\_NUMBER *= <WorkspacePreference.PORT\_NUMBER: 35>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PORT_NUMBER "Link to this definition")

    PORT\_ORIENT *= <WorkspacePreference.PORT\_ORIENT: 36>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PORT_ORIENT "Link to this definition")

    PORT\_POWER *= <WorkspacePreference.PORT\_POWER: 37>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PORT_POWER "Link to this definition")

    PORT\_TYPE *= <WorkspacePreference.PORT\_TYPE: 34>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PORT_TYPE "Link to this definition")

    PREF\_VERSION *= <WorkspacePreference.PREF\_VERSION: 154>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PREF_VERSION "Link to this definition")

    PRESERVE\_COPY\_PASTE\_NET\_NAMES *= <WorkspacePreference.PRESERVE\_COPY\_PASTE\_NET\_NAMES: 149>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.PRESERVE_COPY_PASTE_NET_NAMES "Link to this definition")

    REROUTE\_TRACES *= <WorkspacePreference.REROUTE\_TRACES: 153>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.REROUTE_TRACES "Link to this definition")

    REROUTE\_WIRES *= <WorkspacePreference.REROUTE\_WIRES: 88>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.REROUTE_WIRES "Link to this definition")

    ROTATION\_INC *= <WorkspacePreference.ROTATION\_INC: 56>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.ROTATION_INC "Link to this definition")

    SCALE\_X *= <WorkspacePreference.SCALE\_X: 25>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SCALE_X "Link to this definition")

    SCALE\_Y *= <WorkspacePreference.SCALE\_Y: 26>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SCALE_Y "Link to this definition")

    SELECT\_BOX\_SIZE *= <WorkspacePreference.SELECT\_BOX\_SIZE: 53>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SELECT_BOX_SIZE "Link to this definition")

    SELECT\_BOX\_UNITS *= <WorkspacePreference.SELECT\_BOX\_UNITS: 115>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SELECT_BOX_UNITS "Link to this definition")

    SELECT\_COLOR *= <WorkspacePreference.SELECT\_COLOR: 40>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SELECT_COLOR "Link to this definition")

    SELECT\_FILTER *= <WorkspacePreference.SELECT\_FILTER: 51>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SELECT_FILTER "Link to this definition")

    SELECT\_MODE *= <WorkspacePreference.SELECT\_MODE: 52>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SELECT_MODE "Link to this definition")

    SELECT\_POINT\_SIZE *= <WorkspacePreference.SELECT\_POINT\_SIZE: 54>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SELECT_POINT_SIZE "Link to this definition")

    SELECT\_POINT\_UNITS *= <WorkspacePreference.SELECT\_POINT\_UNITS: 118>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SELECT_POINT_UNITS "Link to this definition")

    SET\_PASTE\_ORIGIN\_POPUP *= <WorkspacePreference.SET\_PASTE\_ORIGIN\_POPUP: 148>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SET_PASTE_ORIGIN_POPUP "Link to this definition")

    SHOVE\_CONNECTIONS\_ON\_COMPONENT\_PARAM\_CHANGE *= <WorkspacePreference.SHOVE\_CONNECTIONS\_ON\_COMPONENT\_PARAM\_CHANGE: 83>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SHOVE_CONNECTIONS_ON_COMPONENT_PARAM_CHANGE "Link to this definition")

    SHOW\_CONNECTED\_LAY *= <WorkspacePreference.SHOW\_CONNECTED\_LAY: 107>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SHOW_CONNECTED_LAY "Link to this definition")

    SHOW\_CONNECTED\_SCHEM *= <WorkspacePreference.SHOW\_CONNECTED\_SCHEM: 106>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SHOW_CONNECTED_SCHEM "Link to this definition")

    SHOW\_FIXED\_LAY *= <WorkspacePreference.SHOW\_FIXED\_LAY: 109>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SHOW_FIXED_LAY "Link to this definition")

    SHOW\_FIXED\_SCHEM *= <WorkspacePreference.SHOW\_FIXED\_SCHEM: 108>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SHOW_FIXED_SCHEM "Link to this definition")

    STEP\_REPEAT\_NUMCOLS *= <WorkspacePreference.STEP\_REPEAT\_NUMCOLS: 114>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.STEP_REPEAT_NUMCOLS "Link to this definition")

    STEP\_REPEAT\_NUMROWS *= <WorkspacePreference.STEP\_REPEAT\_NUMROWS: 113>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.STEP_REPEAT_NUMROWS "Link to this definition")

    STEP\_REPEAT\_XSPACE *= <WorkspacePreference.STEP\_REPEAT\_XSPACE: 111>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.STEP_REPEAT_XSPACE "Link to this definition")

    STEP\_REPEAT\_YSPACE *= <WorkspacePreference.STEP\_REPEAT\_YSPACE: 112>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.STEP_REPEAT_YSPACE "Link to this definition")

    SWAP\_KEEP\_INST\_NAME *= <WorkspacePreference.SWAP\_KEEP\_INST\_NAME: 137>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.SWAP_KEEP_INST_NAME "Link to this definition")

    TEE\_COLOR *= <WorkspacePreference.TEE\_COLOR: 44>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TEE_COLOR "Link to this definition")

    TEE\_SIZE *= <WorkspacePreference.TEE\_SIZE: 45>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TEE_SIZE "Link to this definition")

    TEE\_SIZE\_UNITS *= <WorkspacePreference.TEE\_SIZE\_UNITS: 117>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TEE_SIZE_UNITS "Link to this definition")

    TEXT\_ABSOLUTE *= <WorkspacePreference.TEXT\_ABSOLUTE: 9>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TEXT_ABSOLUTE "Link to this definition")

    TEXT\_ANGLE *= <WorkspacePreference.TEXT\_ANGLE: 8>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TEXT_ANGLE "Link to this definition")

    TEXT\_FONT *= <WorkspacePreference.TEXT\_FONT: 5>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TEXT_FONT "Link to this definition")

    TEXT\_JUST *= <WorkspacePreference.TEXT\_JUST: 7>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TEXT_JUST "Link to this definition")

    TEXT\_POINT *= <WorkspacePreference.TEXT\_POINT: 6>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TEXT_POINT "Link to this definition")

    TEXT\_STRING *= <WorkspacePreference.TEXT\_STRING: 4>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TEXT_STRING "Link to this definition")

    TO\_ARC\_RADIUS *= <WorkspacePreference.TO\_ARC\_RADIUS: 27>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TO_ARC_RADIUS "Link to this definition")

    TRACE\_MSUB\_ID *= <WorkspacePreference.TRACE\_MSUB\_ID: 93>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TRACE_MSUB_ID "Link to this definition")

    TRACE\_SIM\_MODE *= <WorkspacePreference.TRACE\_SIM\_MODE: 90>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TRACE_SIM_MODE "Link to this definition")

    TRACE\_SINGLE\_ELEM *= <WorkspacePreference.TRACE\_SINGLE\_ELEM: 91>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TRACE_SINGLE_ELEM "Link to this definition")

    TRACE\_TLINE\_FAMILY *= <WorkspacePreference.TRACE\_TLINE\_FAMILY: 89>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TRACE_TLINE_FAMILY "Link to this definition")

    TRACE\_TRAVERSE *= <WorkspacePreference.TRACE\_TRAVERSE: 92>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TRACE_TRAVERSE "Link to this definition")

    TUNE\_PARAMETER\_DISPLAY\_LONG\_NAME *= <WorkspacePreference.TUNE\_PARAMETER\_DISPLAY\_LONG\_NAME: 145>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TUNE_PARAMETER_DISPLAY_LONG_NAME "Link to this definition")

    TUNE\_RANGE *= <WorkspacePreference.TUNE\_RANGE: 141>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TUNE_RANGE "Link to this definition")

    TUNE\_RESTORE\_DDS *= <WorkspacePreference.TUNE\_RESTORE\_DDS: 140>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TUNE_RESTORE_DDS "Link to this definition")

    TUNE\_SCALE *= <WorkspacePreference.TUNE\_SCALE: 143>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TUNE_SCALE "Link to this definition")

    TUNE\_SIM\_MODE *= <WorkspacePreference.TUNE\_SIM\_MODE: 139>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TUNE_SIM_MODE "Link to this definition")

    TUNE\_SNAP *= <WorkspacePreference.TUNE\_SNAP: 144>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TUNE_SNAP "Link to this definition")

    TUNE\_STEP\_SIZE *= <WorkspacePreference.TUNE\_STEP\_SIZE: 142>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.TUNE_STEP_SIZE "Link to this definition")

    UNDO\_EDIT\_COUNT *= <WorkspacePreference.UNDO\_EDIT\_COUNT: 110>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.UNDO_EDIT_COUNT "Link to this definition")

    USE\_CROSS\_HAIR\_CURSOR *= <WorkspacePreference.USE\_CROSS\_HAIR\_CURSOR: 172>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.USE_CROSS_HAIR_CURSOR "Link to this definition")

    WINDOW\_LOWER\_LEFT\_X *= <WorkspacePreference.WINDOW\_LOWER\_LEFT\_X: 68>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.WINDOW_LOWER_LEFT_X "Link to this definition")

    WINDOW\_LOWER\_LEFT\_Y *= <WorkspacePreference.WINDOW\_LOWER\_LEFT\_Y: 69>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.WINDOW_LOWER_LEFT_Y "Link to this definition")

    WINDOW\_UPPER\_RIGHT\_X *= <WorkspacePreference.WINDOW\_UPPER\_RIGHT\_X: 70>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.WINDOW_UPPER_RIGHT_X "Link to this definition")

    WINDOW\_UPPER\_RIGHT\_Y *= <WorkspacePreference.WINDOW\_UPPER\_RIGHT\_Y: 71>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.WINDOW_UPPER_RIGHT_Y "Link to this definition")

    WIRE\_LABEL\_COLOR *= <WorkspacePreference.WIRE\_LABEL\_COLOR: 20>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.WIRE_LABEL_COLOR "Link to this definition")

    WIRE\_LABEL\_FONT *= <WorkspacePreference.WIRE\_LABEL\_FONT: 18>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.WIRE_LABEL_FONT "Link to this definition")

    WIRE\_LABEL\_POINT *= <WorkspacePreference.WIRE\_LABEL\_POINT: 19>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.WIRE_LABEL_POINT "Link to this definition")

    WORKSPACE\_LAYOUT\_PRF\_IS\_UNINITIALIZED *= <WorkspacePreference.WORKSPACE\_LAYOUT\_PRF\_IS\_UNINITIALIZED: 180>*[](#keysight.ads.de.experimental.preferences.WorkspacePreference.WORKSPACE_LAYOUT_PRF_IS_UNINITIALIZED "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.WorkspacePreference](#keysight.ads.de.experimental.preferences.WorkspacePreference "keysight.ads.de._pde.WorkspacePreference")*, *value: int*) → None[](#keysight.ads.de.experimental.preferences.WorkspacePreference.__init__ "Link to this definition")

    *property* name[](#keysight.ads.de.experimental.preferences.WorkspacePreference.name "Link to this definition")

    *property* value[](#keysight.ads.de.experimental.preferences.WorkspacePreference.value "Link to this definition")

*class* keysight.ads.de.experimental.preferences.LibSpecificPreference[](#keysight.ads.de.experimental.preferences.LibSpecificPreference "Link to this definition")
:   Bases: `pybind11_object`

    Members:

    PATH\_WIDTH

    PATH\_RADIUS

    TEXT\_HEIGHT

    INST\_NAME\_LAYER\_ID

    INST\_ID\_LAYER\_ID

    INST\_PARAM1\_LAYER\_ID

    INST\_TEXT\_HEIGHT

    GRID\_SNAP\_X

    GRID\_SNAP\_Y

    TAP\_LENGTH

    PORT\_SIZE

    MIN\_VERTEX\_DIST

    UNITS\_FREQ

    UNITS\_RES

    UNITS\_COND

    UNITS\_IND

    UNITS\_CAP

    UNITS\_LNG

    UNITS\_TIME

    UNITS\_ANG

    UNITS\_POWER

    UNITS\_VOLT

    UNITS\_CUR

    UNITS\_DIST

    PIN\_ANNOT\_LAYER\_ID

    GRID\_SNAP\_X *= <LibSpecificPreference.GRID\_SNAP\_X: 193>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.GRID_SNAP_X "Link to this definition")

    GRID\_SNAP\_Y *= <LibSpecificPreference.GRID\_SNAP\_Y: 194>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.GRID_SNAP_Y "Link to this definition")

    INST\_ID\_LAYER\_ID *= <LibSpecificPreference.INST\_ID\_LAYER\_ID: 190>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.INST_ID_LAYER_ID "Link to this definition")

    INST\_NAME\_LAYER\_ID *= <LibSpecificPreference.INST\_NAME\_LAYER\_ID: 189>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.INST_NAME_LAYER_ID "Link to this definition")

    INST\_PARAM1\_LAYER\_ID *= <LibSpecificPreference.INST\_PARAM1\_LAYER\_ID: 191>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.INST_PARAM1_LAYER_ID "Link to this definition")

    INST\_TEXT\_HEIGHT *= <LibSpecificPreference.INST\_TEXT\_HEIGHT: 192>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.INST_TEXT_HEIGHT "Link to this definition")

    MIN\_VERTEX\_DIST *= <LibSpecificPreference.MIN\_VERTEX\_DIST: 197>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.MIN_VERTEX_DIST "Link to this definition")

    PATH\_RADIUS *= <LibSpecificPreference.PATH\_RADIUS: 187>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.PATH_RADIUS "Link to this definition")

    PATH\_WIDTH *= <LibSpecificPreference.PATH\_WIDTH: 186>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.PATH_WIDTH "Link to this definition")

    PIN\_ANNOT\_LAYER\_ID *= <LibSpecificPreference.PIN\_ANNOT\_LAYER\_ID: 210>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.PIN_ANNOT_LAYER_ID "Link to this definition")

    PORT\_SIZE *= <LibSpecificPreference.PORT\_SIZE: 196>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.PORT_SIZE "Link to this definition")

    TAP\_LENGTH *= <LibSpecificPreference.TAP\_LENGTH: 195>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.TAP_LENGTH "Link to this definition")

    TEXT\_HEIGHT *= <LibSpecificPreference.TEXT\_HEIGHT: 188>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.TEXT_HEIGHT "Link to this definition")

    UNITS\_ANG *= <LibSpecificPreference.UNITS\_ANG: 205>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_ANG "Link to this definition")

    UNITS\_CAP *= <LibSpecificPreference.UNITS\_CAP: 202>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_CAP "Link to this definition")

    UNITS\_COND *= <LibSpecificPreference.UNITS\_COND: 200>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_COND "Link to this definition")

    UNITS\_CUR *= <LibSpecificPreference.UNITS\_CUR: 208>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_CUR "Link to this definition")

    UNITS\_DIST *= <LibSpecificPreference.UNITS\_DIST: 209>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_DIST "Link to this definition")

    UNITS\_FREQ *= <LibSpecificPreference.UNITS\_FREQ: 198>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_FREQ "Link to this definition")

    UNITS\_IND *= <LibSpecificPreference.UNITS\_IND: 201>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_IND "Link to this definition")

    UNITS\_LNG *= <LibSpecificPreference.UNITS\_LNG: 203>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_LNG "Link to this definition")

    UNITS\_POWER *= <LibSpecificPreference.UNITS\_POWER: 206>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_POWER "Link to this definition")

    UNITS\_RES *= <LibSpecificPreference.UNITS\_RES: 199>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_RES "Link to this definition")

    UNITS\_TIME *= <LibSpecificPreference.UNITS\_TIME: 204>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_TIME "Link to this definition")

    UNITS\_VOLT *= <LibSpecificPreference.UNITS\_VOLT: 207>*[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.UNITS_VOLT "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.LibSpecificPreference](#keysight.ads.de.experimental.preferences.LibSpecificPreference "keysight.ads.de._pde.LibSpecificPreference")*, *value: int*) → None[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.__init__ "Link to this definition")

    *property* name[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.name "Link to this definition")

    *property* value[](#keysight.ads.de.experimental.preferences.LibSpecificPreference.value "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/experimental/netlist_helper.md === -->

# Netlist Utilities[](#module-keysight.ads.de.experimental.netlist_helper "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.experimental.netlist\_helper.NetlistStringBuilder[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder "Link to this definition")
:   \_\_init\_\_(*instance: [StandardInstance](../db/callbacks.md#keysight.ads.de.db.StandardInstance "keysight.ads.de.db._callbacks.StandardInstance")*) → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.__init__ "Link to this definition")
    :   Class to help with creating a custom netlist string for use in a netlist callback.

        Provides methods for adding the model name, instance name, connectivity, parameters, and
        custom strings.

        instance: The StandardInstance passed to the netlist callback

    append\_connectivity() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_connectivity "Link to this definition")

    append\_instance\_name() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_instance_name "Link to this definition")

    append\_model\_and\_instance\_name() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_model_and_instance_name "Link to this definition")
    :   Append the model and instance name with a : separator (<model\_name:instance\_name>).

        Equivalent to calling:
        append\_model\_name()
        append\_str(“:”)
        append\_instance\_name()

    append\_model\_name() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_model_name "Link to this definition")

    append\_parameter(*param\_name: str*) → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_parameter "Link to this definition")

    append\_parameters() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_parameters "Link to this definition")

    append\_str(*to\_append: str*) → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.append_str "Link to this definition")
    :   Append a custom string.

    clear() → None[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.clear "Link to this definition")
    :   Clear any previously created string.

    clear\_and\_get\_default\_netlist\_str() → str[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.clear_and_get_default_netlist_str "Link to this definition")
    :   Clear out any existing string and return the default netlist string.

        This function will use the format string associated with the component.
        If no format string has been defined, will use an internally defined default
        format string, functionally equivalent to the below:

        builder.clear()
        builder.append\_model\_name()
        builder.append\_str(“:”)
        builder.append\_instance\_name()
        builder.append\_connectivity()
        builder.append\_parameters()
        netlist\_str = builder.netlist\_str

        OR:
        builder.clear()
        builder.append\_model\_and\_instance\_name()
        builder.append\_connectivity()
        builder.append\_parameters()
        netlist\_str = builder.netlist\_str

    *property* netlist\_str*: str*[](#keysight.ads.de.experimental.netlist_helper.NetlistStringBuilder.netlist_str "Link to this definition")
    :   The built-up netlist string; default is an empty string.


---

