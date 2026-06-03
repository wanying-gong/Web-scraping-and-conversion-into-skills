<!-- 来源: pysubst\docs\reference\subst\index.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Technology](../../index.md)
* [Reference](../index.md)
* keysight.ads.subst

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

* [Design](../../../../pypde/docs/index.md)
  + [Reference](../../../../pypde/docs/reference/index.md)
    - [keysight.ads.de](../../../../pypde/docs/reference/de/index.md)
      * [Workspace](../../../../pypde/docs/reference/de/workspace.md)
      * [Library](../../../../pypde/docs/reference/de/library.md)
      * [Cell](../../../../pypde/docs/reference/de/cell.md)
      * [View](../../../../pypde/docs/reference/de/view.md)
      * [CellviewRef](../../../../pypde/docs/reference/de/cellviewref.md)
      * [DesignHierarchy](../../../../pypde/docs/reference/de/design_hierarchy.md)
      * [DMData](../../../../pypde/docs/reference/de/dmdata.md)
      * [ItemInfo](../../../../pypde/docs/reference/de/item_info.md)
      * [Points](../../../../pypde/docs/reference/de/points.md)
      * [Collections](../../../../pypde/docs/reference/de/collections.md)
    - [keysight.ads.de.ael](../../../../pypde/docs/reference/de/ael.md)
    - [keysight.ads.de.app](../../../../pypde/docs/reference/de/app/index.md)
      * [Actions and Menus](../../../../pypde/docs/reference/de/app/action.md)
      * [Addons](../../../../pypde/docs/reference/de/app/addon.md)
      * [Callbacks](../../../../pypde/docs/reference/de/app/callbacks.md)
      * [Windows and Widgets](../../../../pypde/docs/reference/de/app/window.md)
    - [keysight.ads.de.db](../../../../pypde/docs/reference/de/db/index.md)
      * [Callbacks](../../../../pypde/docs/reference/de/db/callbacks.md)
      * [Enumerated Types](../../../../pypde/docs/reference/de/db/enums.md)
      * [Parameter Forms](../../../../pypde/docs/reference/de/db/forms.md)
      * [GenPolyline](../../../../pypde/docs/reference/de/db/genpolyline.md)
      * [Model Definition](../../../../pypde/docs/reference/de/db/model_def.md)
      * [Parameters](../../../../pypde/docs/reference/de/db/parameters.md)
      * [Properties](../../../../pypde/docs/reference/de/db/properties.md)
      * [Transaction](../../../../pypde/docs/reference/de/db/transaction.md)
    - [keysight.ads.de.db\_dbu](../../../../pypde/docs/reference/de/db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../../../../pypde/docs/reference/de/db_uu/index.md)
      * [Design Elements](../../../../pypde/docs/reference/de/db_uu/db_uu.md)
      * [LayerId](../../../../pypde/docs/reference/de/db_uu/layer_id.md)
      * [LineTypeInfo](../../../../pypde/docs/reference/de/db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../../../../pypde/docs/reference/de/experimental/index.md)
      * [CDF](../../../../pypde/docs/reference/de/experimental/cdf/index.md)
      * [Commands](../../../../pypde/docs/reference/de/experimental/commands.md)
      * [Handles](../../../../pypde/docs/reference/de/experimental/handles.md)
      * [Netlist Utilities](../../../../pypde/docs/reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../../../pypde/docs/reference/de/experimental/polygon_utils.md)
      * [Preferences](../../../../pypde/docs/reference/de/experimental/preferences.md)
      * [xxPro View](../../../../pypde/docs/reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../../../pypde/docs/reference/de/experimental/symbol.md)
      * [Text Maker](../../../../pypde/docs/reference/de/experimental/text_maker.md)
    - [keysight.ads.de.tech](../../../../pypde/docs/reference/de/tech/index.md)
      * [Tech](../../../../pypde/docs/reference/de/tech/tech.md)
      * [Padstacks](../../../../pypde/docs/reference/de/tech/pads/pads.md)
      * [Via Rules](../../../../pypde/docs/reference/de/tech/rule/rule.md)
      * [Nested Technology](../../../../pypde/docs/reference/de/tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../../../../pypde/docs/reference/de/app/dds.md)
  + [Examples](../../../../pypde/docs/examples/index.md)
    - [Calling Between AEL and Python](../../../../pypde/docs/examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../../../pypde/docs/examples/ex_create_layout.md)
    - [Create Schematic](../../../../pypde/docs/examples/ex_create_schematic.md)
    - [Create Workspace](../../../../pypde/docs/examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../../../pypde/docs/examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../../../pypde/docs/examples/ex_cdf.md)
    - [Component Parameters](../../../../pypde/docs/examples/ex_parameters.md)
    - [Creating an Item Definition](../../../../pypde/docs/examples/ex_itemdef.md)
    - [Model Definition Properties](../../../../pypde/docs/examples/ex_model.md)
    - [Adding Instances to a Design](../../../../pypde/docs/examples/ex_lpf.md)
    - [Properties](../../../../pypde/docs/examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../../../pypde/docs/examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../../../pypde/docs/examples/ex_padstack.md)
    - [Nested Technology](../../../../pypde/docs/examples/ex_nested.md)
    - [Rules](../../../../pypde/docs/examples/ex_rules.md)
    - [Placing Text](../../../../pypde/docs/examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../../../pypde/docs/examples/ex_polygon.md)
    - [PySide2](../../../../pypde/docs/examples/ex_pyside.md)
    - [Traversing Hierarchy](../../../../pypde/docs/examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../../../pypde/docs/examples/ex_working_with_var.md)
    - [XML RPC](../../../../pypde/docs/examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../../../pypde/docs/examples/ex_translate_gds.md)
* [Technology](../../index.md)
  + [Reference](../index.md)
    - keysight.ads.subst
  + [Examples](../../examples/index.md)
    - [Create Substrate](../../examples/ex_make_substrate.md)
    - [Substrate with Layout](../../examples/ex_substrate_with_layout.md)

# keysight.ads.subst[](#module-keysight.ads.subst "Link to this heading")

Substrate module.

Automate substrate creation and editing using the `keysight.ads.subst` package. This is typically
imported as:

```
from keysight.ads import subst
```

## Classes[](#classes "Link to this heading")

*class* keysight.ads.subst.BoundingAreaLayerType[](#keysight.ads.subst.BoundingAreaLayerType "Link to this definition")
:   Specifies whether an object has a bounding area layer.

    INHERIT *= <BoundingAreaLayerType.INHERIT: 1>*[](#keysight.ads.subst.BoundingAreaLayerType.INHERIT "Link to this definition")
    :   This object does inherits the bounding area layer (if defined) from the substrate.

    NONE *= <BoundingAreaLayerType.NONE: 0>*[](#keysight.ads.subst.BoundingAreaLayerType.NONE "Link to this definition")
    :   This object does not have a bounding area layer.

    SPECIFIED *= <BoundingAreaLayerType.SPECIFIED: 2>*[](#keysight.ads.subst.BoundingAreaLayerType.SPECIFIED "Link to this definition")
    :   This object does have a bounding area layer.

*class* keysight.ads.subst.HorizontalItem[](#keysight.ads.subst.HorizontalItem "Link to this definition")
:   Base class for MaterialItem and InterfaceItem.

    *property* bounding\_area\_layer*: int*[](#keysight.ads.subst.HorizontalItem.bounding_area_layer "Link to this definition")
    :   Specifies the bounding area layer of this object if the type is specified.

    *property* bounding\_area\_layer\_type*: [BoundingAreaLayerType](#keysight.ads.subst.BoundingAreaLayerType "keysight.ads.subst.substrate.BoundingAreaLayerType")*[](#keysight.ads.subst.HorizontalItem.bounding_area_layer_type "Link to this definition")

    *property* effective\_bound\_layer*: int*[](#keysight.ads.subst.HorizontalItem.effective_bound_layer "Link to this definition")

    get\_thickness\_mks() → float[](#keysight.ads.subst.HorizontalItem.get_thickness_mks "Link to this definition")

    get\_thickness\_mks\_expr() → str[](#keysight.ads.subst.HorizontalItem.get_thickness_mks_expr "Link to this definition")

    *property* is\_bound*: bool*[](#keysight.ads.subst.HorizontalItem.is_bound "Link to this definition")

    *property* material\_name*: str*[](#keysight.ads.subst.HorizontalItem.material_name "Link to this definition")

    *property* substrate*: [Substrate](#keysight.ads.subst.Substrate "keysight.ads.subst.substrate.Substrate")*[](#keysight.ads.subst.HorizontalItem.substrate "Link to this definition")

    *property* thickness*: float | None*[](#keysight.ads.subst.HorizontalItem.thickness "Link to this definition")

    *property* thickness\_expr*: str*[](#keysight.ads.subst.HorizontalItem.thickness_expr "Link to this definition")

    *property* thickness\_is\_number*: bool*[](#keysight.ads.subst.HorizontalItem.thickness_is_number "Link to this definition")

    *property* thickness\_unit*: [Unit](#keysight.ads.subst.Unit "keysight.ads.subst.unit.Unit")*[](#keysight.ads.subst.HorizontalItem.thickness_unit "Link to this definition")

*class* keysight.ads.subst.InterfaceItem[](#keysight.ads.subst.InterfaceItem "Link to this definition")
:   Represents an infinitely thin interface sandwiched between two materials.

    *class* Purpose[](#keysight.ads.subst.InterfaceItem.Purpose "Link to this definition")
    :   Specifies how this interface is used.

        COVER *= <Purpose.COVER: 2>*[](#keysight.ads.subst.InterfaceItem.Purpose.COVER "Link to this definition")

        SLOT *= <Purpose.SLOT: 1>*[](#keysight.ads.subst.InterfaceItem.Purpose.SLOT "Link to this definition")

        STRIP *= <Purpose.STRIP: 0>*[](#keysight.ads.subst.InterfaceItem.Purpose.STRIP "Link to this definition")

    convert\_to\_cover() → None[](#keysight.ads.subst.InterfaceItem.convert_to_cover "Link to this definition")

    *property* is\_cover*: bool*[](#keysight.ads.subst.InterfaceItem.is_cover "Link to this definition")

    *property* is\_non\_cover\_placeholder*: bool*[](#keysight.ads.subst.InterfaceItem.is_non_cover_placeholder "Link to this definition")
    :   Is this interface a placeholder for a cover?

    *property* is\_termination*: bool*[](#keysight.ads.subst.InterfaceItem.is_termination "Link to this definition")
    :   Is this cover a 377 Ohm termination?

    *property* purpose*: [Purpose](#keysight.ads.subst.InterfaceItem.Purpose "keysight.ads.subst.InterfaceItem.Purpose")*[](#keysight.ads.subst.InterfaceItem.purpose "Link to this definition")

    remove\_cover() → None[](#keysight.ads.subst.InterfaceItem.remove_cover "Link to this definition")

*class* keysight.ads.subst.LayerItem[](#keysight.ads.subst.LayerItem "Link to this definition")
:   Represents a layer of metal defined on an interface.

    *property* bottom\_roughness*: str*[](#keysight.ads.subst.LayerItem.bottom_roughness "Link to this definition")

    *property* expand*: bool*[](#keysight.ads.subst.LayerItem.expand "Link to this definition")
    :   Does this expand the material above or below?

    *property* interface*: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*[](#keysight.ads.subst.LayerItem.interface "Link to this definition")

    *property* interface\_index*: int*[](#keysight.ads.subst.LayerItem.interface_index "Link to this definition")

    interface\_is\_forbidden(*interface: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → bool[](#keysight.ads.subst.LayerItem.interface_is_forbidden "Link to this definition")
    :   Is this layer allowed not allowed on the interface?

    *property* is\_above*: bool*[](#keysight.ads.subst.LayerItem.is_above "Link to this definition")
    :   Is this layer item above the interface?

    *property* negative*: bool*[](#keysight.ads.subst.LayerItem.negative "Link to this definition")
    :   Is this a slot layer item?

    *property* pins\_only*: bool*[](#keysight.ads.subst.LayerItem.pins_only "Link to this definition")

    *property* sheet*: bool*[](#keysight.ads.subst.LayerItem.sheet "Link to this definition")
    :   Is this a sheet that does not expand or intrude into the material above or below?

    *property* thermal\_layer\_name*: str*[](#keysight.ads.subst.LayerItem.thermal_layer_name "Link to this definition")

    *property* top\_roughness*: str*[](#keysight.ads.subst.LayerItem.top_roughness "Link to this definition")

*class* keysight.ads.subst.MaterialItem[](#keysight.ads.subst.MaterialItem "Link to this definition")
:   Represents a slab of material (typically a dielectric) separated from the next slab by an interface.

    *property* is\_bottom\_infinite\_material*: bool*[](#keysight.ads.subst.MaterialItem.is_bottom_infinite_material "Link to this definition")
    :   Is this material the bottom material and is it covered?

    *property* is\_infinite\_material*: bool*[](#keysight.ads.subst.MaterialItem.is_infinite_material "Link to this definition")
    :   Is this material the bottom or top material and is it covered?

    *property* is\_top\_infinite\_material*: bool*[](#keysight.ads.subst.MaterialItem.is_top_infinite_material "Link to this definition")
    :   Is this material the top material and is it covered?

*class* keysight.ads.subst.Materials[](#keysight.ads.subst.Materials "Link to this definition")
:   \_\_init\_\_() → None[](#keysight.ads.subst.Materials.__init__ "Link to this definition")

    *property* conductors*: [NamedMutableCollectionAbc](../../../../pypde/docs/reference/de/collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[SubstrateConductor](#keysight.ads.subst.SubstrateConductor "keysight.ads.subst._materials.SubstrateConductor")]*[](#keysight.ads.subst.Materials.conductors "Link to this definition")

    *property* dielectrics*: [NamedMutableCollectionAbc](../../../../pypde/docs/reference/de/collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[SubstrateDielectric](#keysight.ads.subst.SubstrateDielectric "keysight.ads.subst._materials.SubstrateDielectric")]*[](#keysight.ads.subst.Materials.dielectrics "Link to this definition")

    *property* roughness*: [NamedMutableCollectionAbc](../../../../pypde/docs/reference/de/collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[Roughness](#keysight.ads.subst.Roughness "keysight.ads.subst._materials.Roughness")]*[](#keysight.ads.subst.Materials.roughness "Link to this definition")

    *property* semiconductors*: [NamedMutableCollectionAbc](../../../../pypde/docs/reference/de/collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[SubstrateSemiconductor](#keysight.ads.subst.SubstrateSemiconductor "keysight.ads.subst._materials.SubstrateSemiconductor")]*[](#keysight.ads.subst.Materials.semiconductors "Link to this definition")

    *property* superconductors*: [NamedMutableCollectionAbc](../../../../pypde/docs/reference/de/collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[SubstrateSuperconductor](#keysight.ads.subst.SubstrateSuperconductor "keysight.ads.subst._materials.SubstrateSuperconductor")]*[](#keysight.ads.subst.Materials.superconductors "Link to this definition")

*class* keysight.ads.subst.Roughness[](#keysight.ads.subst.Roughness "Link to this definition")
:   \_\_init\_\_(*name: str*) → None[](#keysight.ads.subst.Roughness.__init__ "Link to this definition")

    *property* bbase*: str*[](#keysight.ads.subst.Roughness.bbase "Link to this definition")

    *property* dpeaks*: str*[](#keysight.ads.subst.Roughness.dpeaks "Link to this definition")

    *property* huray\_a\_flat*: str*[](#keysight.ads.subst.Roughness.huray_a_flat "Link to this definition")

    *property* huray\_n*: str*[](#keysight.ads.subst.Roughness.huray_n "Link to this definition")

    *property* huray\_r*: str*[](#keysight.ads.subst.Roughness.huray_r "Link to this definition")

    *property* huray\_ratio\_of\_a*: str*[](#keysight.ads.subst.Roughness.huray_ratio_of_a "Link to this definition")

    *property* is\_encrypted*: bool*[](#keysight.ads.subst.Roughness.is_encrypted "Link to this definition")

    *property* is\_foreign*: bool*[](#keysight.ads.subst.Roughness.is_foreign "Link to this definition")

    *property* l2bbase*: str*[](#keysight.ads.subst.Roughness.l2bbase "Link to this definition")

    *property* l2dpeaks*: str*[](#keysight.ads.subst.Roughness.l2dpeaks "Link to this definition")

    *property* l2rough*: str*[](#keysight.ads.subst.Roughness.l2rough "Link to this definition")

    *property* l3bbase*: str*[](#keysight.ads.subst.Roughness.l3bbase "Link to this definition")

    *property* l3dpeaks*: str*[](#keysight.ads.subst.Roughness.l3dpeaks "Link to this definition")

    *property* l3rough*: str*[](#keysight.ads.subst.Roughness.l3rough "Link to this definition")

    *property* model\_type*: [RoughnessModelType](#keysight.ads.subst.RoughnessModelType "keysight.ads.subst._materials.RoughnessModelType")*[](#keysight.ads.subst.Roughness.model_type "Link to this definition")

    *property* name*: str*[](#keysight.ads.subst.Roughness.name "Link to this definition")

    *property* rough*: str*[](#keysight.ads.subst.Roughness.rough "Link to this definition")

*class* keysight.ads.subst.Substrate[](#keysight.ads.subst.Substrate "Link to this definition")
:   The main class for substrate data.

    *property* all\_layer\_numbers*: list[int]*[](#keysight.ads.subst.Substrate.all_layer_numbers "Link to this definition")

    *property* all\_material\_names*: list[str]*[](#keysight.ads.subst.Substrate.all_material_names "Link to this definition")

    *property* bottom\_of\_board\_interface\_index*: int*[](#keysight.ads.subst.Substrate.bottom_of_board_interface_index "Link to this definition")

    *property* bounding\_area\_layer*: int*[](#keysight.ads.subst.Substrate.bounding_area_layer "Link to this definition")
    :   Specifies the bounding area layer of this substrate if the type is specified.

    *property* bounding\_area\_layer\_type*: [BoundingAreaLayerType](#keysight.ads.subst.BoundingAreaLayerType "keysight.ads.subst.substrate.BoundingAreaLayerType")*[](#keysight.ads.subst.Substrate.bounding_area_layer_type "Link to this definition")

    delete\_layer\_indexed(*index: int*) → None[](#keysight.ads.subst.Substrate.delete_layer_indexed "Link to this definition")

    delete\_material\_and\_interface\_indexed(*material\_index: int*, *interface\_index: int*) → None[](#keysight.ads.subst.Substrate.delete_material_and_interface_indexed "Link to this definition")

    delete\_substrate\_indexed(*index: int*) → None[](#keysight.ads.subst.Substrate.delete_substrate_indexed "Link to this definition")

    delete\_via\_indexed(*index: int*) → None[](#keysight.ads.subst.Substrate.delete_via_indexed "Link to this definition")

    find\_layer\_name\_from\_number(*number: int*) → str[](#keysight.ads.subst.Substrate.find_layer_name_from_number "Link to this definition")

    find\_layer\_number\_from\_name(*name: str*) → int[](#keysight.ads.subst.Substrate.find_layer_number_from_name "Link to this definition")

    get\_interface(*index: int*) → [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")[](#keysight.ads.subst.Substrate.get_interface "Link to this definition")

    get\_interface\_above(*material: [MaterialItem](#keysight.ads.subst.MaterialItem "keysight.ads.subst.substrate.MaterialItem")*) → [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")[](#keysight.ads.subst.Substrate.get_interface_above "Link to this definition")

    get\_interface\_below(*material: [MaterialItem](#keysight.ads.subst.MaterialItem "keysight.ads.subst.substrate.MaterialItem")*) → [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")[](#keysight.ads.subst.Substrate.get_interface_below "Link to this definition")

    get\_interface\_index(*interface: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → int[](#keysight.ads.subst.Substrate.get_interface_index "Link to this definition")

    get\_layer\_index(*layer: [LayerItem](#keysight.ads.subst.LayerItem "keysight.ads.subst.substrate.LayerItem")*) → int[](#keysight.ads.subst.Substrate.get_layer_index "Link to this definition")

    get\_layers\_on\_interface(*interface: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → list[[LayerItem](#keysight.ads.subst.LayerItem "keysight.ads.subst.substrate.LayerItem")][](#keysight.ads.subst.Substrate.get_layers_on_interface "Link to this definition")

    get\_layers\_on\_interface\_matching\_role(*interface: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*, *role: [ProcessRole](../../../../pypde/docs/reference/de/tech/tech.md#keysight.ads.de.tech.ProcessRole "keysight.ads.de.tech._tech.ProcessRole")*) → list[[LayerItem](#keysight.ads.subst.LayerItem "keysight.ads.subst.substrate.LayerItem")][](#keysight.ads.subst.Substrate.get_layers_on_interface_matching_role "Link to this definition")

    get\_material(*index: int*) → [MaterialItem](#keysight.ads.subst.MaterialItem "keysight.ads.subst.substrate.MaterialItem")[](#keysight.ads.subst.Substrate.get_material "Link to this definition")

    get\_material\_above(*interface: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → [MaterialItem](#keysight.ads.subst.MaterialItem "keysight.ads.subst.substrate.MaterialItem")[](#keysight.ads.subst.Substrate.get_material_above "Link to this definition")

    get\_material\_below(*interface: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → [MaterialItem](#keysight.ads.subst.MaterialItem "keysight.ads.subst.substrate.MaterialItem")[](#keysight.ads.subst.Substrate.get_material_below "Link to this definition")

    get\_material\_index(*material: [MaterialItem](#keysight.ads.subst.MaterialItem "keysight.ads.subst.substrate.MaterialItem")*) → int[](#keysight.ads.subst.Substrate.get_material_index "Link to this definition")

    get\_substrates\_on\_interface(*interface: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → list[[SubstrateItem](#keysight.ads.subst.SubstrateItem "keysight.ads.subst.substrate.SubstrateItem")][](#keysight.ads.subst.Substrate.get_substrates_on_interface "Link to this definition")

    get\_via\_index(*via: [ViaItem](#keysight.ads.subst.ViaItem "keysight.ads.subst.substrate.ViaItem")*) → int[](#keysight.ads.subst.Substrate.get_via_index "Link to this definition")

    get\_vias\_intersecting\_material(*material: [MaterialItem](#keysight.ads.subst.MaterialItem "keysight.ads.subst.substrate.MaterialItem")*) → list[[ViaItem](#keysight.ads.subst.ViaItem "keysight.ads.subst.substrate.ViaItem")][](#keysight.ads.subst.Substrate.get_vias_intersecting_material "Link to this definition")

    *property* has\_bottom\_cover*: bool*[](#keysight.ads.subst.Substrate.has_bottom_cover "Link to this definition")

    *property* has\_top\_cover*: bool*[](#keysight.ads.subst.Substrate.has_top_cover "Link to this definition")

    insert\_conductor\_via(*index\_or\_interface\_1: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*, *index\_or\_interface\_2: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → [ViaItem](#keysight.ads.subst.ViaItem "keysight.ads.subst.substrate.ViaItem")[](#keysight.ads.subst.Substrate.insert_conductor_via "Link to this definition")

    insert\_dielectric\_via(*index\_or\_interface\_1: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*, *index\_or\_interface\_2: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → [ViaItem](#keysight.ads.subst.ViaItem "keysight.ads.subst.substrate.ViaItem")[](#keysight.ads.subst.Substrate.insert_dielectric_via "Link to this definition")

    insert\_layer(*index\_or\_interface: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*, *process\_role: [ProcessRole](../../../../pypde/docs/reference/de/tech/tech.md#keysight.ads.de.tech.ProcessRole "keysight.ads.de.tech._tech.ProcessRole")*, *model\_type: [ModelType](#keysight.ads.subst.VerticalItem.ModelType "keysight.ads.subst.substrate.VerticalItem.ModelType") = ModelType.USE\_DEFAULT*) → [LayerItem](#keysight.ads.subst.LayerItem "keysight.ads.subst.substrate.LayerItem")[](#keysight.ads.subst.Substrate.insert_layer "Link to this definition")

    insert\_material\_and\_interface\_above(*material\_index: int*) → None[](#keysight.ads.subst.Substrate.insert_material_and_interface_above "Link to this definition")

    insert\_material\_and\_interface\_below(*material\_index: int*) → None[](#keysight.ads.subst.Substrate.insert_material_and_interface_below "Link to this definition")

    insert\_semiconductor\_via(*index\_or\_interface\_1: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*, *index\_or\_interface\_2: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → [ViaItem](#keysight.ads.subst.ViaItem "keysight.ads.subst.substrate.ViaItem")[](#keysight.ads.subst.Substrate.insert_semiconductor_via "Link to this definition")

    insert\_substrate(*index\_or\_interface: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → [SubstrateItem](#keysight.ads.subst.SubstrateItem "keysight.ads.subst.substrate.SubstrateItem")[](#keysight.ads.subst.Substrate.insert_substrate "Link to this definition")

    insert\_through\_silicon\_via(*index\_or\_interface\_1: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*, *index\_or\_interface\_2: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → [ViaItem](#keysight.ads.subst.ViaItem "keysight.ads.subst.substrate.ViaItem")[](#keysight.ads.subst.Substrate.insert_through_silicon_via "Link to this definition")

    insert\_via(*index\_or\_interface\_1: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*, *index\_or\_interface\_2: int | [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*, *process\_role: [ProcessRole](../../../../pypde/docs/reference/de/tech/tech.md#keysight.ads.de.tech.ProcessRole "keysight.ads.de.tech._tech.ProcessRole")*, *model\_type: [ModelType](#keysight.ads.subst.VerticalItem.ModelType "keysight.ads.subst.substrate.VerticalItem.ModelType") = ModelType.USE\_DEFAULT*) → [ViaItem](#keysight.ads.subst.ViaItem "keysight.ads.subst.substrate.ViaItem")[](#keysight.ads.subst.Substrate.insert_via "Link to this definition")

    interface\_index\_in\_use(*index: int*) → bool[](#keysight.ads.subst.Substrate.interface_index_in_use "Link to this definition")

    *property* interfaces*: list[[InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")]*[](#keysight.ads.subst.Substrate.interfaces "Link to this definition")

    is\_bottom\_interface(*interface: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → bool[](#keysight.ads.subst.Substrate.is_bottom_interface "Link to this definition")

    *property* is\_modified*: bool*[](#keysight.ads.subst.Substrate.is_modified "Link to this definition")

    *property* is\_read\_only*: bool*[](#keysight.ads.subst.Substrate.is_read_only "Link to this definition")

    is\_top\_interface(*interface: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*) → bool[](#keysight.ads.subst.Substrate.is_top_interface "Link to this definition")

    *property* is\_writable*: bool*[](#keysight.ads.subst.Substrate.is_writable "Link to this definition")
    :   Is the library file for this substrate writable?

    *property* layers*: list[[LayerItem](#keysight.ads.subst.LayerItem "keysight.ads.subst.substrate.LayerItem")]*[](#keysight.ads.subst.Substrate.layers "Link to this definition")

    *property* library*: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.subst.Substrate.library "Link to this definition")

    *property* materials*: list[[MaterialItem](#keysight.ads.subst.MaterialItem "keysight.ads.subst.substrate.MaterialItem")]*[](#keysight.ads.subst.Substrate.materials "Link to this definition")

    merge\_vias\_on\_same\_layer() → None[](#keysight.ads.subst.Substrate.merge_vias_on_same_layer "Link to this definition")

    *property* name*: str*[](#keysight.ads.subst.Substrate.name "Link to this definition")
    :   Name of the substrate (must be unique in the library).

    *property* purposes\_to\_exclude*: list[str] | None*[](#keysight.ads.subst.Substrate.purposes_to_exclude "Link to this definition")
    :   Shapes using these purposes will be excluded by EM simulations.

    *property* purposes\_to\_include*: list[str] | None*[](#keysight.ads.subst.Substrate.purposes_to_include "Link to this definition")
    :   Shapes using only these purposes will be included by EM simulations.

    *property* roughness\_models*: list[str]*[](#keysight.ads.subst.Substrate.roughness_models "Link to this definition")

    save\_substrate() → None[](#keysight.ads.subst.Substrate.save_substrate "Link to this definition")

    save\_substrate\_as(*new\_library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *new\_subst\_name: str*) → None[](#keysight.ads.subst.Substrate.save_substrate_as "Link to this definition")

    *property* substrates*: list[[SubstrateItem](#keysight.ads.subst.SubstrateItem "keysight.ads.subst.substrate.SubstrateItem")]*[](#keysight.ads.subst.Substrate.substrates "Link to this definition")

    *property* top\_interface*: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*[](#keysight.ads.subst.Substrate.top_interface "Link to this definition")

    *property* top\_interface\_index*: int*[](#keysight.ads.subst.Substrate.top_interface_index "Link to this definition")

    *property* top\_material*: [MaterialItem](#keysight.ads.subst.MaterialItem "keysight.ads.subst.substrate.MaterialItem")*[](#keysight.ads.subst.Substrate.top_material "Link to this definition")

    *property* top\_material\_index*: int*[](#keysight.ads.subst.Substrate.top_material_index "Link to this definition")

    *property* top\_of\_board\_interface\_index*: int*[](#keysight.ads.subst.Substrate.top_of_board_interface_index "Link to this definition")

    *property* unit*: [Unit](#keysight.ads.subst.Unit "keysight.ads.subst.unit.Unit")*[](#keysight.ads.subst.Substrate.unit "Link to this definition")
    :   Unit for this substrate.

    *property* vias*: list[[ViaItem](#keysight.ads.subst.ViaItem "keysight.ads.subst.substrate.ViaItem")]*[](#keysight.ads.subst.Substrate.vias "Link to this definition")

*class* keysight.ads.subst.SubstrateConductor[](#keysight.ads.subst.SubstrateConductor "Link to this definition")
:   \_\_init\_\_(*name: str*) → None[](#keysight.ads.subst.SubstrateConductor.__init__ "Link to this definition")

    *property* imag*: str*[](#keysight.ads.subst.SubstrateConductor.imag "Link to this definition")

    *property* mur\_imag*: str*[](#keysight.ads.subst.SubstrateConductor.mur_imag "Link to this definition")

    *property* mur\_real*: str*[](#keysight.ads.subst.SubstrateConductor.mur_real "Link to this definition")

    *property* parameter\_type*: [ConductorParamType](#keysight.ads.subst.ConductorParamType "keysight.ads.subst._materials.ConductorParamType")*[](#keysight.ads.subst.SubstrateConductor.parameter_type "Link to this definition")

    *property* real*: str*[](#keysight.ads.subst.SubstrateConductor.real "Link to this definition")

    *property* tc1*: str*[](#keysight.ads.subst.SubstrateConductor.tc1 "Link to this definition")

    *property* tc2*: str*[](#keysight.ads.subst.SubstrateConductor.tc2 "Link to this definition")

    *property* tnom*: str*[](#keysight.ads.subst.SubstrateConductor.tnom "Link to this definition")

*class* keysight.ads.subst.SubstrateDielectric[](#keysight.ads.subst.SubstrateDielectric "Link to this definition")
:   \_\_init\_\_(*name: str*) → None[](#keysight.ads.subst.SubstrateDielectric.__init__ "Link to this definition")

    *property* er\_imag*: str*[](#keysight.ads.subst.SubstrateDielectric.er_imag "Link to this definition")

    *property* er\_loss\_tangent*: str*[](#keysight.ads.subst.SubstrateDielectric.er_loss_tangent "Link to this definition")

    *property* er\_real*: str*[](#keysight.ads.subst.SubstrateDielectric.er_real "Link to this definition")

    *property* high\_freq*: str*[](#keysight.ads.subst.SubstrateDielectric.high_freq "Link to this definition")

    *property* loss\_type*: [DielectricLossType](#keysight.ads.subst.DielectricLossType "keysight.ads.subst._materials.DielectricLossType")*[](#keysight.ads.subst.SubstrateDielectric.loss_type "Link to this definition")

    *property* low\_freq*: str*[](#keysight.ads.subst.SubstrateDielectric.low_freq "Link to this definition")

    *property* mur\_imag*: str*[](#keysight.ads.subst.SubstrateDielectric.mur_imag "Link to this definition")

    *property* mur\_real*: str*[](#keysight.ads.subst.SubstrateDielectric.mur_real "Link to this definition")

    *property* value\_freq*: str*[](#keysight.ads.subst.SubstrateDielectric.value_freq "Link to this definition")

*class* keysight.ads.subst.SubstrateItem[](#keysight.ads.subst.SubstrateItem "Link to this definition")
:   Represents a nested substrate defined on an interface.

    *class* AlignPosition[](#keysight.ads.subst.SubstrateItem.AlignPosition "Link to this definition")
    :   When aligning by layer, specifies what part of the layer on the nested substrate item aligns with the parent substrate interface.

        BOTTOM\_OF\_LAYER *= <AlignPosition.BOTTOM\_OF\_LAYER: 1>*[](#keysight.ads.subst.SubstrateItem.AlignPosition.BOTTOM_OF_LAYER "Link to this definition")

        TOP\_OF\_LAYER *= <AlignPosition.TOP\_OF\_LAYER: 0>*[](#keysight.ads.subst.SubstrateItem.AlignPosition.TOP_OF_LAYER "Link to this definition")

    *class* AlignType[](#keysight.ads.subst.SubstrateItem.AlignType "Link to this definition")
    :   Specifies how the nested substrate item aligns with the interface on which it lives.

        BOTTOM *= <AlignType.BOTTOM: 0>*[](#keysight.ads.subst.SubstrateItem.AlignType.BOTTOM "Link to this definition")
        :   The bottom interface of the nested substrate item aligns with the parent substrate interface.

        LAYER *= <AlignType.LAYER: 2>*[](#keysight.ads.subst.SubstrateItem.AlignType.LAYER "Link to this definition")
        :   A layer on the nested substrate item aligns with the parent substrate interface.

        TOP *= <AlignType.TOP: 1>*[](#keysight.ads.subst.SubstrateItem.AlignType.TOP "Link to this definition")
        :   The top interface of the nested substrate item aligns with the parent substrate interface.

    *property* align\_layer\_name*: str*[](#keysight.ads.subst.SubstrateItem.align_layer_name "Link to this definition")
    :   Name of the layer to use for alignment if this item aligns by layer.

    *property* align\_type*: [AlignType](#keysight.ads.subst.SubstrateItem.AlignType "keysight.ads.subst.SubstrateItem.AlignType")*[](#keysight.ads.subst.SubstrateItem.align_type "Link to this definition")

    *property* alignment\_position*: [AlignPosition](#keysight.ads.subst.SubstrateItem.AlignPosition "keysight.ads.subst.SubstrateItem.AlignPosition")*[](#keysight.ads.subst.SubstrateItem.alignment_position "Link to this definition")
    :   Specifies whether this substrate item is above or below the layer when aligning by layer.

    *property* interface*: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*[](#keysight.ads.subst.SubstrateItem.interface "Link to this definition")

    *property* interface\_index*: int*[](#keysight.ads.subst.SubstrateItem.interface_index "Link to this definition")

    *property* is\_flipped*: bool*[](#keysight.ads.subst.SubstrateItem.is_flipped "Link to this definition")

    *property* is\_nested\_tech\_enabled*: bool*[](#keysight.ads.subst.SubstrateItem.is_nested_tech_enabled "Link to this definition")
    :   Can this substrate item use nested technology?

    *property* layer\_map*: str*[](#keysight.ads.subst.SubstrateItem.layer_map "Link to this definition")

    *property* layer\_map\_lib\_name*: str*[](#keysight.ads.subst.SubstrateItem.layer_map_lib_name "Link to this definition")

    *property* library\_name*: str*[](#keysight.ads.subst.SubstrateItem.library_name "Link to this definition")
    :   Name of the nested technology library for this substrate item.

    *property* offset*: float*[](#keysight.ads.subst.SubstrateItem.offset "Link to this definition")

    *property* offset\_unit*: [Unit](#keysight.ads.subst.Unit "keysight.ads.subst.unit.Unit")*[](#keysight.ads.subst.SubstrateItem.offset_unit "Link to this definition")

    *property* precedence*: int*[](#keysight.ads.subst.SubstrateItem.precedence "Link to this definition")
    :   Specifies the increase in precedence for the items on this substrate item.

    set\_library\_and\_substrate\_names(*library\_name: str*, *substrate\_name: str*) → None[](#keysight.ads.subst.SubstrateItem.set_library_and_substrate_names "Link to this definition")

    *property* substrate\_name*: str*[](#keysight.ads.subst.SubstrateItem.substrate_name "Link to this definition")
    :   Name of the nested technology substrate for this substrate item.

*class* keysight.ads.subst.SubstrateMaterial[](#keysight.ads.subst.SubstrateMaterial "Link to this definition")
:   Base class for materials.

    *property* is\_encrypted*: bool*[](#keysight.ads.subst.SubstrateMaterial.is_encrypted "Link to this definition")

    *property* is\_foreign*: bool*[](#keysight.ads.subst.SubstrateMaterial.is_foreign "Link to this definition")

    *property* material\_type*: [Material](#keysight.ads.subst.Material "keysight.ads.subst._materials.Material")*[](#keysight.ads.subst.SubstrateMaterial.material_type "Link to this definition")

    *property* mean\_free\_electron\_path*: str*[](#keysight.ads.subst.SubstrateMaterial.mean_free_electron_path "Link to this definition")

    *property* name*: str*[](#keysight.ads.subst.SubstrateMaterial.name "Link to this definition")

    *property* thermal\_conductivity*: str*[](#keysight.ads.subst.SubstrateMaterial.thermal_conductivity "Link to this definition")

    *property* thermal\_conductivity\_in\_z*: str*[](#keysight.ads.subst.SubstrateMaterial.thermal_conductivity_in_z "Link to this definition")

    *property* volumetric\_heat\_capacity*: str*[](#keysight.ads.subst.SubstrateMaterial.volumetric_heat_capacity "Link to this definition")

*class* keysight.ads.subst.SubstrateSemiconductor[](#keysight.ads.subst.SubstrateSemiconductor "Link to this definition")
:   \_\_init\_\_(*name: str*) → None[](#keysight.ads.subst.SubstrateSemiconductor.__init__ "Link to this definition")

    *property* doping*: [SemiconductorDoping](#keysight.ads.subst.SemiconductorDoping "keysight.ads.subst._materials.SemiconductorDoping")*[](#keysight.ads.subst.SubstrateSemiconductor.doping "Link to this definition")

    *property* er\_real*: str*[](#keysight.ads.subst.SubstrateSemiconductor.er_real "Link to this definition")

    *property* mur\_imag*: str*[](#keysight.ads.subst.SubstrateSemiconductor.mur_imag "Link to this definition")

    *property* mur\_real*: str*[](#keysight.ads.subst.SubstrateSemiconductor.mur_real "Link to this definition")

    *property* resistivity*: str*[](#keysight.ads.subst.SubstrateSemiconductor.resistivity "Link to this definition")

*class* keysight.ads.subst.SubstrateSuperconductor[](#keysight.ads.subst.SubstrateSuperconductor "Link to this definition")
:   \_\_init\_\_(*name: str*) → None[](#keysight.ads.subst.SubstrateSuperconductor.__init__ "Link to this definition")

    *property* critical\_temp*: str*[](#keysight.ads.subst.SubstrateSuperconductor.critical_temp "Link to this definition")

    *property* london\_depth\_at\_0\_k*: str*[](#keysight.ads.subst.SubstrateSuperconductor.london_depth_at_0_k "Link to this definition")

    *property* mur\_imag*: str*[](#keysight.ads.subst.SubstrateSuperconductor.mur_imag "Link to this definition")

    *property* mur\_real*: str*[](#keysight.ads.subst.SubstrateSuperconductor.mur_real "Link to this definition")

    *property* parameter\_type*: [ConductorParamType](#keysight.ads.subst.ConductorParamType "keysight.ads.subst._materials.ConductorParamType")*[](#keysight.ads.subst.SubstrateSuperconductor.parameter_type "Link to this definition")

    *property* real*: str*[](#keysight.ads.subst.SubstrateSuperconductor.real "Link to this definition")

*class* keysight.ads.subst.VerticalItem[](#keysight.ads.subst.VerticalItem "Link to this definition")
:   Base class for LayerItem, ViaItem and SubstrateItem.

    *class* ModelType[](#keysight.ads.subst.VerticalItem.ModelType "Link to this definition")
    :   Specifies different ways that Vias can be modeled.

        CONDUCTOR\_VIA\_AS\_THROUGH\_SILICON\_VIA *= <ModelType.CONDUCTOR\_VIA\_AS\_THROUGH\_SILICON\_VIA: 1>*[](#keysight.ads.subst.VerticalItem.ModelType.CONDUCTOR_VIA_AS_THROUGH_SILICON_VIA "Link to this definition")

        THICK\_CONDUCTOR *= <ModelType.THICK\_CONDUCTOR: 2>*[](#keysight.ads.subst.VerticalItem.ModelType.THICK_CONDUCTOR "Link to this definition")

        USE\_DEFAULT *= <ModelType.USE\_DEFAULT: 0>*[](#keysight.ads.subst.VerticalItem.ModelType.USE_DEFAULT "Link to this definition")

    *property* angle\_expr*: str*[](#keysight.ads.subst.VerticalItem.angle_expr "Link to this definition")

    *property* angle\_is\_number*: bool*[](#keysight.ads.subst.VerticalItem.angle_is_number "Link to this definition")

    get\_thickness\_mks() → float[](#keysight.ads.subst.VerticalItem.get_thickness_mks "Link to this definition")

    get\_thickness\_mks\_expr() → str[](#keysight.ads.subst.VerticalItem.get_thickness_mks_expr "Link to this definition")

    *property* layer\_number*: int*[](#keysight.ads.subst.VerticalItem.layer_number "Link to this definition")

    *property* material\_name*: str*[](#keysight.ads.subst.VerticalItem.material_name "Link to this definition")

    *property* model\_type*: [ModelType](#keysight.ads.subst.VerticalItem.ModelType "keysight.ads.subst.VerticalItem.ModelType")*[](#keysight.ads.subst.VerticalItem.model_type "Link to this definition")

    *property* precedence*: int*[](#keysight.ads.subst.VerticalItem.precedence "Link to this definition")

    *property* process\_role*: [ProcessRole](../../../../pypde/docs/reference/de/tech/tech.md#keysight.ads.de.tech.ProcessRole "keysight.ads.de.tech._tech.ProcessRole")*[](#keysight.ads.subst.VerticalItem.process_role "Link to this definition")

    *property* substrate*: [Substrate](#keysight.ads.subst.Substrate "keysight.ads.subst.substrate.Substrate")*[](#keysight.ads.subst.VerticalItem.substrate "Link to this definition")

    *property* thickness*: float | None*[](#keysight.ads.subst.VerticalItem.thickness "Link to this definition")

    *property* thickness\_expr*: str*[](#keysight.ads.subst.VerticalItem.thickness_expr "Link to this definition")

    *property* thickness\_is\_number*: bool*[](#keysight.ads.subst.VerticalItem.thickness_is_number "Link to this definition")

    *property* thickness\_unit*: [Unit](#keysight.ads.subst.Unit "keysight.ads.subst.unit.Unit")*[](#keysight.ads.subst.VerticalItem.thickness_unit "Link to this definition")

    *property* used\_for\_em\_simulation*: bool*[](#keysight.ads.subst.VerticalItem.used_for_em_simulation "Link to this definition")

*class* keysight.ads.subst.ViaItem[](#keysight.ads.subst.ViaItem "Link to this definition")
:   Represents a via connecting two interfaces.

    *class* DepletionMode[](#keysight.ads.subst.ViaItem.DepletionMode "Link to this definition")
    :   Specifies how the depletion mode is modeled for through silicon vias.

        DEEP *= <DepletionMode.DEEP: 3>*[](#keysight.ads.subst.ViaItem.DepletionMode.DEEP "Link to this definition")

        HF *= <DepletionMode.HF: 1>*[](#keysight.ads.subst.ViaItem.DepletionMode.HF "Link to this definition")

        LF *= <DepletionMode.LF: 2>*[](#keysight.ads.subst.ViaItem.DepletionMode.LF "Link to this definition")

        NONE *= <DepletionMode.NONE: 0>*[](#keysight.ads.subst.ViaItem.DepletionMode.NONE "Link to this definition")

    *class* PinSide[](#keysight.ads.subst.ViaItem.PinSide "Link to this definition")
    :   Specifies the pin side for thick conductors.

        BOTTOM *= <PinSide.BOTTOM: 1>*[](#keysight.ads.subst.ViaItem.PinSide.BOTTOM "Link to this definition")

        TOP *= <PinSide.TOP: 0>*[](#keysight.ads.subst.ViaItem.PinSide.TOP "Link to this definition")

    *property* bias\_voltage*: float | None*[](#keysight.ads.subst.ViaItem.bias_voltage "Link to this definition")
    :   Bias voltage if this is a through silicon via.

    *property* bias\_voltage\_expr*: str | None*[](#keysight.ads.subst.ViaItem.bias_voltage_expr "Link to this definition")

    *property* bias\_voltage\_is\_number*: bool*[](#keysight.ads.subst.ViaItem.bias_voltage_is_number "Link to this definition")

    *property* depletion\_mode*: [DepletionMode](#keysight.ads.subst.ViaItem.DepletionMode "keysight.ads.subst.substrate.ViaItem.DepletionMode") | None*[](#keysight.ads.subst.ViaItem.depletion_mode "Link to this definition")
    :   Depletion mode if this is a through silicon via.

    *property* fixed\_charge*: float | None*[](#keysight.ads.subst.ViaItem.fixed_charge "Link to this definition")
    :   Fixed charge if this is a through silicon via.

    *property* fixed\_charge\_expr*: str | None*[](#keysight.ads.subst.ViaItem.fixed_charge_expr "Link to this definition")

    *property* fixed\_charge\_is\_number*: bool*[](#keysight.ads.subst.ViaItem.fixed_charge_is_number "Link to this definition")

    get\_liner\_thickness\_mks() → float[](#keysight.ads.subst.ViaItem.get_liner_thickness_mks "Link to this definition")

    get\_liner\_thickness\_mks\_expr() → str[](#keysight.ads.subst.ViaItem.get_liner_thickness_mks_expr "Link to this definition")

    get\_plating\_thickness\_mks() → float[](#keysight.ads.subst.ViaItem.get_plating_thickness_mks "Link to this definition")

    get\_plating\_thickness\_mks\_expr() → str[](#keysight.ads.subst.ViaItem.get_plating_thickness_mks_expr "Link to this definition")

    *property* is\_conductor\_via*: bool*[](#keysight.ads.subst.ViaItem.is_conductor_via "Link to this definition")

    *property* is\_plating\_enabled*: bool*[](#keysight.ads.subst.ViaItem.is_plating_enabled "Link to this definition")
    :   Is this a plated via?

    *property* is\_thick\_conductor*: bool*[](#keysight.ads.subst.ViaItem.is_thick_conductor "Link to this definition")

    *property* is\_through\_silicon\_via*: bool*[](#keysight.ads.subst.ViaItem.is_through_silicon_via "Link to this definition")
    :   Is this a through silicon via?

    *property* liner\_material\_name*: str | None*[](#keysight.ads.subst.ViaItem.liner_material_name "Link to this definition")
    :   Name of the liner material if this is a plated via.

    *property* liner\_thickness*: float | None*[](#keysight.ads.subst.ViaItem.liner_thickness "Link to this definition")

    *property* liner\_thickness\_expr*: str | None*[](#keysight.ads.subst.ViaItem.liner_thickness_expr "Link to this definition")

    *property* liner\_thickness\_is\_number*: bool*[](#keysight.ads.subst.ViaItem.liner_thickness_is_number "Link to this definition")
    :   Thickness of the liner if this is a through silicon via.

    *property* liner\_thickness\_unit*: [Unit](#keysight.ads.subst.Unit "keysight.ads.subst.unit.Unit") | None*[](#keysight.ads.subst.ViaItem.liner_thickness_unit "Link to this definition")
    :   Unit for liner thickness if this is a through silicon via.

    *property* lower\_interface*: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*[](#keysight.ads.subst.ViaItem.lower_interface "Link to this definition")

    *property* lower\_interface\_index*: int*[](#keysight.ads.subst.ViaItem.lower_interface_index "Link to this definition")

    *property* pin\_side*: [PinSide](#keysight.ads.subst.ViaItem.PinSide "keysight.ads.subst.substrate.ViaItem.PinSide") | None*[](#keysight.ads.subst.ViaItem.pin_side "Link to this definition")
    :   Pin side if this is a thick conductor.

    *property* plating\_dielectric\_material\_name*: str | None*[](#keysight.ads.subst.ViaItem.plating_dielectric_material_name "Link to this definition")
    :   Name of the plating dielectric material if this is a plated via.

    *property* plating\_thickness*: float | None*[](#keysight.ads.subst.ViaItem.plating_thickness "Link to this definition")
    :   Thickness of the plating if this is a plated via.

    *property* plating\_thickness\_expr*: str | None*[](#keysight.ads.subst.ViaItem.plating_thickness_expr "Link to this definition")

    *property* plating\_thickness\_is\_number*: bool*[](#keysight.ads.subst.ViaItem.plating_thickness_is_number "Link to this definition")

    *property* plating\_thickness\_unit*: [Unit](#keysight.ads.subst.Unit "keysight.ads.subst.unit.Unit") | None*[](#keysight.ads.subst.ViaItem.plating_thickness_unit "Link to this definition")
    :   Unit for plating thickness if this is a plated via.

    *property* roughness*: str*[](#keysight.ads.subst.ViaItem.roughness "Link to this definition")

    swap\_interfaces() → None[](#keysight.ads.subst.ViaItem.swap_interfaces "Link to this definition")

    *property* upper\_interface*: [InterfaceItem](#keysight.ads.subst.InterfaceItem "keysight.ads.subst.substrate.InterfaceItem")*[](#keysight.ads.subst.ViaItem.upper_interface "Link to this definition")

    *property* upper\_interface\_index*: int*[](#keysight.ads.subst.ViaItem.upper_interface_index "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.subst.ConductorParamType[](#keysight.ads.subst.ConductorParamType "Link to this definition")
:   RESISTANCE *= <ConductorParamType.RESISTANCE: 0>*[](#keysight.ads.subst.ConductorParamType.RESISTANCE "Link to this definition")

    CONDUCTANCE *= <ConductorParamType.CONDUCTANCE: 1>*[](#keysight.ads.subst.ConductorParamType.CONDUCTANCE "Link to this definition")

    RESISTIVITY *= <ConductorParamType.RESISTIVITY: 2>*[](#keysight.ads.subst.ConductorParamType.RESISTIVITY "Link to this definition")

*class* keysight.ads.subst.DielectricLossType[](#keysight.ads.subst.DielectricLossType "Link to this definition")
:   FREQUENCY\_INDEPENDENT *= <DielectricLossType.FREQUENCY\_INDEPENDENT: 0>*[](#keysight.ads.subst.DielectricLossType.FREQUENCY_INDEPENDENT "Link to this definition")

    SVENSSON\_DJORDJEVIC *= <DielectricLossType.SVENSSON\_DJORDJEVIC: 1>*[](#keysight.ads.subst.DielectricLossType.SVENSSON_DJORDJEVIC "Link to this definition")

*class* keysight.ads.subst.Material[](#keysight.ads.subst.Material "Link to this definition")
:   Specifies the type of material.

    CONDUCTOR *= <Material.CONDUCTOR: 0>*[](#keysight.ads.subst.Material.CONDUCTOR "Link to this definition")

    SEMICONDUCTOR *= <Material.SEMICONDUCTOR: 1>*[](#keysight.ads.subst.Material.SEMICONDUCTOR "Link to this definition")

    SUPERCONDUCTOR *= <Material.SUPERCONDUCTOR: 2>*[](#keysight.ads.subst.Material.SUPERCONDUCTOR "Link to this definition")

    DIELECTRIC *= <Material.DIELECTRIC: 3>*[](#keysight.ads.subst.Material.DIELECTRIC "Link to this definition")

*class* keysight.ads.subst.RoughnessModelType[](#keysight.ads.subst.RoughnessModelType "Link to this definition")
:   SMOOTH *= <RoughnessModelType.SMOOTH: 0>*[](#keysight.ads.subst.RoughnessModelType.SMOOTH "Link to this definition")

    HAMMERSTAD *= <RoughnessModelType.HAMMERSTAD: 1>*[](#keysight.ads.subst.RoughnessModelType.HAMMERSTAD "Link to this definition")

    HEMISPHERICAL *= <RoughnessModelType.HEMISPHERICAL: 2>*[](#keysight.ads.subst.RoughnessModelType.HEMISPHERICAL "Link to this definition")

    HURAY *= <RoughnessModelType.HURAY: 3>*[](#keysight.ads.subst.RoughnessModelType.HURAY "Link to this definition")

*class* keysight.ads.subst.SemiconductorDoping[](#keysight.ads.subst.SemiconductorDoping "Link to this definition")
:   N\_TYPE *= <SemiconductorDoping.N\_TYPE: 0>*[](#keysight.ads.subst.SemiconductorDoping.N_TYPE "Link to this definition")

    P\_TYPE *= <SemiconductorDoping.P\_TYPE: 1>*[](#keysight.ads.subst.SemiconductorDoping.P_TYPE "Link to this definition")

*class* keysight.ads.subst.Unit[](#keysight.ads.subst.Unit "Link to this definition")
:   BAD *= <Unit.BAD: 0>*[](#keysight.ads.subst.Unit.BAD "Link to this definition")

    MICRON *= <Unit.MICRON: 1>*[](#keysight.ads.subst.Unit.MICRON "Link to this definition")

    MILLIMETER *= <Unit.MILLIMETER: 2>*[](#keysight.ads.subst.Unit.MILLIMETER "Link to this definition")

    CENTIMETER *= <Unit.CENTIMETER: 3>*[](#keysight.ads.subst.Unit.CENTIMETER "Link to this definition")

    METER *= <Unit.METER: 4>*[](#keysight.ads.subst.Unit.METER "Link to this definition")

    MIL *= <Unit.MIL: 5>*[](#keysight.ads.subst.Unit.MIL "Link to this definition")

    INCH *= <Unit.INCH: 6>*[](#keysight.ads.subst.Unit.INCH "Link to this definition")

    FOOT *= <Unit.FOOT: 7>*[](#keysight.ads.subst.Unit.FOOT "Link to this definition")

    NANOMETER *= <Unit.NANOMETER: 8>*[](#keysight.ads.subst.Unit.NANOMETER "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.subst.close\_substrate(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *subst\_name: str*) → None[](#keysight.ads.subst.close_substrate "Link to this definition")

keysight.ads.subst.copy\_predefined\_materials() → [Materials](#keysight.ads.subst.Materials "keysight.ads.subst._materials.Materials")[](#keysight.ads.subst.copy_predefined_materials "Link to this definition")
:   Return a copy of the predefined materials database.

keysight.ads.subst.create\_substrate\_from\_template(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *subst\_name: str*, *template\_name: str | None = None*) → [Substrate](#keysight.ads.subst.Substrate "keysight.ads.subst.substrate.Substrate")[](#keysight.ads.subst.create_substrate_from_template "Link to this definition")

keysight.ads.subst.create\_substrate(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *subst\_name: str*) → [Substrate](#keysight.ads.subst.Substrate "keysight.ads.subst.substrate.Substrate")[](#keysight.ads.subst.create_substrate "Link to this definition")

keysight.ads.subst.delete\_substrate(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *subst\_name: str*) → None[](#keysight.ads.subst.delete_substrate "Link to this definition")

keysight.ads.subst.save\_substrate(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *subst\_name: str*) → None[](#keysight.ads.subst.save_substrate "Link to this definition")

keysight.ads.subst.get\_conductor\_names(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *this\_lib\_only: bool = True*) → list[str][](#keysight.ads.subst.get_conductor_names "Link to this definition")

keysight.ads.subst.get\_dielectric\_names(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *this\_lib\_only: bool = True*) → list[str][](#keysight.ads.subst.get_dielectric_names "Link to this definition")

keysight.ads.subst.get\_roughness\_names(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *this\_lib\_only: bool = True*) → list[str][](#keysight.ads.subst.get_roughness_names "Link to this definition")

keysight.ads.subst.get\_semiconductor\_names(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *this\_lib\_only: bool = True*) → list[str][](#keysight.ads.subst.get_semiconductor_names "Link to this definition")

keysight.ads.subst.get\_superconductor\_names(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *this\_lib\_only: bool = True*) → list[str][](#keysight.ads.subst.get_superconductor_names "Link to this definition")

keysight.ads.subst.get\_unit(*unit\_name: str*) → [Unit](#keysight.ads.subst.Unit "keysight.ads.subst.unit.Unit")[](#keysight.ads.subst.get_unit "Link to this definition")

keysight.ads.subst.load\_materials(*filename: str*) → [Materials](#keysight.ads.subst.Materials "keysight.ads.subst._materials.Materials")[](#keysight.ads.subst.load_materials "Link to this definition")
:   Return a copy of the materials database.

keysight.ads.subst.open\_substrate(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *subst\_name: str*, *mode: str = 'r'*) → [Substrate](#keysight.ads.subst.Substrate "keysight.ads.subst.substrate.Substrate")[](#keysight.ads.subst.open_substrate "Link to this definition")

keysight.ads.subst.save\_materials(*filename: str*, *materials: [Materials](#keysight.ads.subst.Materials "keysight.ads.subst._materials.Materials")*) → None[](#keysight.ads.subst.save_materials "Link to this definition")
:   Save the materials database.

keysight.ads.subst.substrate\_exists(*library: [Library](../../../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *subst\_name: str*) → bool[](#keysight.ads.subst.substrate_exists "Link to this definition")

keysight.ads.subst.ui\_unit\_name(*unit: [Unit](#keysight.ads.subst.Unit "keysight.ads.subst.unit.Unit")*) → str[](#keysight.ads.subst.ui_unit_name "Link to this definition")

keysight.ads.subst.unit\_conversion\_factor(*unit: [Unit](#keysight.ads.subst.Unit "keysight.ads.subst.unit.Unit")*) → float[](#keysight.ads.subst.unit_conversion_factor "Link to this definition")

keysight.ads.subst.unit\_name(*unit: [Unit](#keysight.ads.subst.Unit "keysight.ads.subst.unit.Unit")*) → str[](#keysight.ads.subst.unit_name "Link to this definition")

On this page

[Previous

Reference](../index.md)
[Next

Examples](../../examples/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top