<!-- 来源: pypde\docs\reference\de\tech\tech.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.tech](index.md)
* Tech

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
    - [keysight.ads.de.app](../app/index.md)
      * [Actions and Menus](../app/action.md)
      * [Addons](../app/addon.md)
      * [Callbacks](../app/callbacks.md)
      * [Windows and Widgets](../app/window.md)
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
    - [keysight.ads.de.tech](index.md)
      * Tech
      * [Padstacks](pads/pads.md)
      * [Via Rules](rule/rule.md)
      * [Nested Technology](nested/nested.md)
    - [keysight.ads.de.app.dds](../app/dds.md)
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

# Tech[](#tech "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.tech.DerivedLayer[](#keysight.ads.de.tech.DerivedLayer "Link to this definition")
:   Represents a derived layer.

    A derived layer is a (virtual) layer that is formed by operations on shapes
    from one or more other layers. Derived layers typically don’t have any shapes.

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.tech.DerivedLayer.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *static* create\_sizing\_layer(*tech: [Tech](#keysight.ads.de.tech.Tech "keysight.ads.de.tech._tech.Tech")*, *layer\_name: str*, *layer\_num: int*, *operation: [LayerOp](#keysight.ads.de.tech.LayerOp "keysight.ads.de._pde.tech.LayerOp") | str*, *layer1: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer") | str*, *distance: int*) → [DerivedLayer](#keysight.ads.de.tech.DerivedLayer "keysight.ads.de.tech._tech.DerivedLayer")[](#keysight.ads.de.tech.DerivedLayer.create_sizing_layer "Link to this definition")
    :   Create a derived layer from a single source layer, a sizing operation, and a distance parameter.

        The derived layer contains all the shapes that result by performing
        the sizing operation on all the shapes from the source layer.
        The sizing operation uses the distance parameter to change the size
        of each shape from the source layer.

    *static* create\_boolean\_layer(*tech: [Tech](#keysight.ads.de.tech.Tech "keysight.ads.de.tech._tech.Tech")*, *layer\_name: str*, *layer\_num: int*, *operation: [LayerOp](#keysight.ads.de.tech.LayerOp "keysight.ads.de._pde.tech.LayerOp") | str*, *layer1: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer") | str*, *layer2: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer") | str*) → [DerivedLayer](#keysight.ads.de.tech.DerivedLayer "keysight.ads.de.tech._tech.DerivedLayer")[](#keysight.ads.de.tech.DerivedLayer.create_boolean_layer "Link to this definition")
    :   Create a derived layer from two source layers and boolean operation.

        The derived layer contains all the shapes that result by performing
        the boolean operation on all the shapes from the two source layers.

    *property* layer1*: int*[](#keysight.ads.de.tech.DerivedLayer.layer1 "Link to this definition")

    *property* layer2*: int*[](#keysight.ads.de.tech.DerivedLayer.layer2 "Link to this definition")

    *property* layer1\_num*: int*[](#keysight.ads.de.tech.DerivedLayer.layer1_num "Link to this definition")

    *property* layer2\_num*: int*[](#keysight.ads.de.tech.DerivedLayer.layer2_num "Link to this definition")

    *property* operation\_name*: str*[](#keysight.ads.de.tech.DerivedLayer.operation_name "Link to this definition")
    :   Returns the name of the derived layer operation.

    *property* operation*: [LayerOp](#keysight.ads.de.tech.LayerOp "keysight.ads.de._pde.tech.LayerOp")*[](#keysight.ads.de.tech.DerivedLayer.operation "Link to this definition")
    :   Returns the derived layer operation.

        NOTE: If this is a user defined operation (USER\_DEFINED),
        you must use operation\_name to get the name of the operation.

    get\_distance\_param() → int[](#keysight.ads.de.tech.DerivedLayer.get_distance_param "Link to this definition")
    :   Return the distance parameter from this derived layer.

        This only works for derived layers that use a sizing operation.
        If you call this function on a derived layer that does not have a
        distance parameter, it will raise an exception.

    *property* abbreviation*: str*[](#keysight.ads.de.tech.DerivedLayer.abbreviation "Link to this definition")

    *static* is\_derived(*layer: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer")*) → TypeGuard[[DerivedLayer](#keysight.ads.de.tech.DerivedLayer "keysight.ads.de.tech._tech.DerivedLayer")][](#keysight.ads.de.tech.DerivedLayer.is_derived "Link to this definition")

    *static* is\_physical(*layer: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer")*) → TypeGuard[[PhysicalLayer](#keysight.ads.de.tech.PhysicalLayer "keysight.ads.de.tech._tech.PhysicalLayer")][](#keysight.ads.de.tech.DerivedLayer.is_physical "Link to this definition")

    *property* layer\_binding*: str*[](#keysight.ads.de.tech.DerivedLayer.layer_binding "Link to this definition")

    *property* library*: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.de.tech.DerivedLayer.library "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.tech.DerivedLayer.name "Link to this definition")

    *property* number*: int*[](#keysight.ads.de.tech.DerivedLayer.number "Link to this definition")

    *property* process\_role*: [ProcessRole](#keysight.ads.de.tech.ProcessRole "keysight.ads.de.tech._tech.ProcessRole")*[](#keysight.ads.de.tech.DerivedLayer.process_role "Link to this definition")

    *property* tech*: [Tech](#keysight.ads.de.tech.Tech "keysight.ads.de.tech._tech.Tech")*[](#keysight.ads.de.tech.DerivedLayer.tech "Link to this definition")

*class* keysight.ads.de.tech.Layer[](#keysight.ads.de.tech.Layer "Link to this definition")
:   Base class for Layer objects in Tech.

    Layer objects become invalid when the technology is modified.
    So the Python objects should have a short lifetime.

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.tech.Layer.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *static* is\_derived(*layer: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer")*) → TypeGuard[[DerivedLayer](#keysight.ads.de.tech.DerivedLayer "keysight.ads.de.tech._tech.DerivedLayer")][](#keysight.ads.de.tech.Layer.is_derived "Link to this definition")

    *static* is\_physical(*layer: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer")*) → TypeGuard[[PhysicalLayer](#keysight.ads.de.tech.PhysicalLayer "keysight.ads.de.tech._tech.PhysicalLayer")][](#keysight.ads.de.tech.Layer.is_physical "Link to this definition")

    *property* number*: int*[](#keysight.ads.de.tech.Layer.number "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.tech.Layer.name "Link to this definition")

    *property* tech*: [Tech](#keysight.ads.de.tech.Tech "keysight.ads.de.tech._tech.Tech")*[](#keysight.ads.de.tech.Layer.tech "Link to this definition")

    *property* library*: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.de.tech.Layer.library "Link to this definition")

    *property* abbreviation*: str*[](#keysight.ads.de.tech.Layer.abbreviation "Link to this definition")

    *property* process\_role*: [ProcessRole](#keysight.ads.de.tech.ProcessRole "keysight.ads.de.tech._tech.ProcessRole")*[](#keysight.ads.de.tech.Layer.process_role "Link to this definition")

    *property* layer\_binding*: str*[](#keysight.ads.de.tech.Layer.layer_binding "Link to this definition")

*class* keysight.ads.de.tech.LayerSlice[](#keysight.ads.de.tech.LayerSlice "Link to this definition")
:   Represents a single slice of a LineStrip.

    Identifies the layer for this slice and its enclosure.

    \_\_init\_\_() → None[](#keysight.ads.de.tech.LayerSlice.__init__ "Link to this definition")

    *classmethod* create\_from\_names(*library: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *layer\_name: str*, *purpose\_name: str*, *enclosure\_width: float*) → [LayerSlice](#keysight.ads.de.tech.LayerSlice "keysight.ads.de.tech._tech.LayerSlice")[](#keysight.ads.de.tech.LayerSlice.create_from_names "Link to this definition")

    *classmethod* create\_from\_layer\_id(*library: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *layer\_id: [LayerId](../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *enclosure\_width: float*) → [LayerSlice](#keysight.ads.de.tech.LayerSlice "keysight.ads.de.tech._tech.LayerSlice")[](#keysight.ads.de.tech.LayerSlice.create_from_layer_id "Link to this definition")

    *property* layer\_id*: [LayerId](../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*[](#keysight.ads.de.tech.LayerSlice.layer_id "Link to this definition")

    *property* layer\_name*: str*[](#keysight.ads.de.tech.LayerSlice.layer_name "Link to this definition")

    *property* purpose\_name*: str*[](#keysight.ads.de.tech.LayerSlice.purpose_name "Link to this definition")

    *property* enclosure\_width\_uu*: float*[](#keysight.ads.de.tech.LayerSlice.enclosure_width_uu "Link to this definition")
    :   Return the difference in width (in user units) between this slice and the default width of the strip.

    validate\_names\_and\_id(*library: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*) → None[](#keysight.ads.de.tech.LayerSlice.validate_names_and_id "Link to this definition")
    :   Check that the layer\_id matches the layer and purpose names.

*class* keysight.ads.de.tech.LineClearance[](#keysight.ads.de.tech.LineClearance "Link to this definition")
:   \_\_init\_\_(*layer\_name: str | None = None*, *clearance: float | None = None*) → None[](#keysight.ads.de.tech.LineClearance.__init__ "Link to this definition")

    *property* layer\_name*: str*[](#keysight.ads.de.tech.LineClearance.layer_name "Link to this definition")

    *property* clearance*: float*[](#keysight.ads.de.tech.LineClearance.clearance "Link to this definition")

*class* keysight.ads.de.tech.LineCorner[](#keysight.ads.de.tech.LineCorner "Link to this definition")
:   Defines the corners used by Line Types.

    \_\_init\_\_(*corner\_type: [LineCornerType](#keysight.ads.de.tech.LineCornerType "keysight.ads.de._pde.tech.LineCornerType") | None = None*) → None[](#keysight.ads.de.tech.LineCorner.__init__ "Link to this definition")

    *property* type*: [LineCornerType](#keysight.ads.de.tech.LineCornerType "keysight.ads.de._pde.tech.LineCornerType")*[](#keysight.ads.de.tech.LineCorner.type "Link to this definition")

    *property* mitered\_cutoff*: int*[](#keysight.ads.de.tech.LineCorner.mitered_cutoff "Link to this definition")
    :   Mitered cutoff ration % - used only for Mitered corners.

    *property* curve\_radius\_uu*: float*[](#keysight.ads.de.tech.LineCorner.curve_radius_uu "Link to this definition")
    :   Radius of the curve - used only for Curved corners.

*class* keysight.ads.de.tech.LineItem[](#keysight.ads.de.tech.LineItem "Link to this definition")
:   Defines transmission line types.

    A LineItem must be saved in a library in order to be used by layout designs.

    \_\_init\_\_(*name: str | None = None*) → None[](#keysight.ads.de.tech.LineItem.__init__ "Link to this definition")
    :   Create a new LineItem object.

        LineItem():
        :   Creates a new LineItem object with no name.

        LineItem(name):
        :   Creates a new LineItem object the given name.

        To be used by designs or other technology objects, a LineItem must be
        named and saved in a library (see Tech.save\_line\_types).

    *property* name*: str*[](#keysight.ads.de.tech.LineItem.name "Link to this definition")
    :   Name of this line type definition.

        References to line items by layout objects use this name.

    *property* type*: str*[](#keysight.ads.de.tech.LineItem.type "Link to this definition")
    :   Legacy type - not really used now.

    *property* description*: str*[](#keysight.ads.de.tech.LineItem.description "Link to this definition")
    :   Description of this line type definition used by tooltips.

    *property* substrate*: str*[](#keysight.ads.de.tech.LineItem.substrate "Link to this definition")
    :   Name of the substrate used by this Line type definition.

    *property* begin\_end\_type*: [LineEndType](#keysight.ads.de.tech.LineEndType "keysight.ads.de._pde.tech.LineEndType")*[](#keysight.ads.de.tech.LineItem.begin_end_type "Link to this definition")
    :   The type of ending (and beginning) of lines defined by this line item.

    *property* corner*: [LineCorner](#keysight.ads.de.tech.LineCorner "keysight.ads.de.tech._tech.LineCorner")*[](#keysight.ads.de.tech.LineItem.corner "Link to this definition")
    :   Defines the corners (bends) of lines defined by this line item.

    *property* strip\_items*: ListRefAbc[[LineStripItem](#keysight.ads.de.tech.LineStripItem "keysight.ads.de.tech._tech.LineStripItem")]*[](#keysight.ads.de.tech.LineItem.strip_items "Link to this definition")
    :   The collection of line strips in this LineItem.

    *property* plane\_layer\_names*: ListRefAbc[str]*[](#keysight.ads.de.tech.LineItem.plane_layer_names "Link to this definition")
    :   The collection of plane layer names used by this line item.

    *property* simulation\_model*: [LineTypeSimulationModel](#keysight.ads.de.tech.LineTypeSimulationModel "keysight.ads.de.tech._tech.LineTypeSimulationModel")*[](#keysight.ads.de.tech.LineItem.simulation_model "Link to this definition")

    *property* single\_strip\_line*: [LineStripItem](#keysight.ads.de.tech.LineStripItem "keysight.ads.de.tech._tech.LineStripItem")*[](#keysight.ads.de.tech.LineItem.single_strip_line "Link to this definition")
    :   The only strip item if this line is single-strip.

        Will raise an exception if this line is not single-strip.

    *property* is\_single\_strip\_line*: bool*[](#keysight.ads.de.tech.LineItem.is_single_strip_line "Link to this definition")

    *property* clearances*: ListRefAbc[[LineClearance](#keysight.ads.de.tech.LineClearance "keysight.ads.de.tech._tech.LineClearance")]*[](#keysight.ads.de.tech.LineItem.clearances "Link to this definition")
    :   The collection of line clearances in this LineItem.

    get\_calculated\_type\_deprecated() → str[](#keysight.ads.de.tech.LineItem.get_calculated_type_deprecated "Link to this definition")

    uses\_layer\_id(*layer\_id: [LayerId](../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*) → bool[](#keysight.ads.de.tech.LineItem.uses_layer_id "Link to this definition")

    add\_clearance(*clearance: [LineClearance](#keysight.ads.de.tech.LineClearance "keysight.ads.de.tech._tech.LineClearance")*) → None[](#keysight.ads.de.tech.LineItem.add_clearance "Link to this definition")

*class* keysight.ads.de.tech.LineStripItem[](#keysight.ads.de.tech.LineStripItem "Link to this definition")
:   Represents a single strip of a line type.

    \_\_init\_\_(*library: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library") | None = None*, *layer\_name: str | None = None*, *purpose\_name: str | None = None*, *layer\_id: [LayerId](../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId") | None = None*) → None[](#keysight.ads.de.tech.LineStripItem.__init__ "Link to this definition")

    *property* strip\_id*: str*[](#keysight.ads.de.tech.LineStripItem.strip_id "Link to this definition")

    *property* default\_width*: float*[](#keysight.ads.de.tech.LineStripItem.default_width "Link to this definition")
    :   The default width (in user units) of the layer slices.

    *property* strip\_spacing\_type*: [LineStripSpacingType](#keysight.ads.de.tech.LineStripSpacingType "keysight.ads.de._pde.tech.LineStripSpacingType")*[](#keysight.ads.de.tech.LineStripItem.strip_spacing_type "Link to this definition")
    :   Returns the type of spacing required between this strip and the next strip.

    *property* strip\_spacing\_value*: float*[](#keysight.ads.de.tech.LineStripItem.strip_spacing_value "Link to this definition")
    :   Returns the spacing required between this strip and the next strip.

    *property* layer\_slices*: ListRefAbc[[LayerSlice](#keysight.ads.de.tech.LayerSlice "keysight.ads.de.tech._tech.LayerSlice")]*[](#keysight.ads.de.tech.LineStripItem.layer_slices "Link to this definition")
    :   Return the collection of layer slices in this LineStripItem.

    *property* has\_multiple\_slices*: bool*[](#keysight.ads.de.tech.LineStripItem.has_multiple_slices "Link to this definition")

    add\_layer\_slice(*library: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *layer\_name: str*, *purpose\_name: str*, *width: float = 0.0*) → None[](#keysight.ads.de.tech.LineStripItem.add_layer_slice "Link to this definition")
    :   Create a LayerSlice and append it to layer\_slices.

    uses\_layer\_id(*layer\_id: [LayerId](../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*) → bool[](#keysight.ads.de.tech.LineStripItem.uses_layer_id "Link to this definition")
    :   Return True if any LayerSlice is on the given layer.

*class* keysight.ads.de.tech.LineTypeSimulationModel[](#keysight.ads.de.tech.LineTypeSimulationModel "Link to this definition")
:   Describes how to simulate a line type.

    \_\_init\_\_(*model\_set: str = ''*, *substrate\_instance\_name: str = ''*) → None[](#keysight.ads.de.tech.LineTypeSimulationModel.__init__ "Link to this definition")

    *property* model\_set*: str*[](#keysight.ads.de.tech.LineTypeSimulationModel.model_set "Link to this definition")

    *property* use\_single\_tline\_element\_to\_model\_a\_trace*: bool*[](#keysight.ads.de.tech.LineTypeSimulationModel.use_single_tline_element_to_model_a_trace "Link to this definition")

    *property* autogenerate\_substrate*: bool*[](#keysight.ads.de.tech.LineTypeSimulationModel.autogenerate_substrate "Link to this definition")

    *property* substrate\_instance\_name*: str*[](#keysight.ads.de.tech.LineTypeSimulationModel.substrate_instance_name "Link to this definition")

*class* keysight.ads.de.tech.PhysicalLayer[](#keysight.ads.de.tech.PhysicalLayer "Link to this definition")
:   Represents a physical layer (one that contains shapes and figures).

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.tech.PhysicalLayer.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *static* create(*tech: [Tech](#keysight.ads.de.tech.Tech "keysight.ads.de.tech._tech.Tech")*, *layer\_name: str*, *layer\_num: int*) → [PhysicalLayer](#keysight.ads.de.tech.PhysicalLayer "keysight.ads.de.tech._tech.PhysicalLayer")[](#keysight.ads.de.tech.PhysicalLayer.create "Link to this definition")

    *property* mask\_number*: int*[](#keysight.ads.de.tech.PhysicalLayer.mask_number "Link to this definition")

    *property* mfg\_grid*: int*[](#keysight.ads.de.tech.PhysicalLayer.mfg_grid "Link to this definition")

    *property* material*: [OAMaterial](#keysight.ads.de.tech.OAMaterial "keysight.ads.de._pde.tech.OAMaterial")*[](#keysight.ads.de.tech.PhysicalLayer.material "Link to this definition")

    *property* abbreviation*: str*[](#keysight.ads.de.tech.PhysicalLayer.abbreviation "Link to this definition")

    *static* is\_derived(*layer: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer")*) → TypeGuard[[DerivedLayer](#keysight.ads.de.tech.DerivedLayer "keysight.ads.de.tech._tech.DerivedLayer")][](#keysight.ads.de.tech.PhysicalLayer.is_derived "Link to this definition")

    *static* is\_physical(*layer: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer")*) → TypeGuard[[PhysicalLayer](#keysight.ads.de.tech.PhysicalLayer "keysight.ads.de.tech._tech.PhysicalLayer")][](#keysight.ads.de.tech.PhysicalLayer.is_physical "Link to this definition")

    *property* layer\_binding*: str*[](#keysight.ads.de.tech.PhysicalLayer.layer_binding "Link to this definition")

    *property* library*: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.de.tech.PhysicalLayer.library "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.tech.PhysicalLayer.name "Link to this definition")

    *property* number*: int*[](#keysight.ads.de.tech.PhysicalLayer.number "Link to this definition")

    *property* process\_role*: [ProcessRole](#keysight.ads.de.tech.ProcessRole "keysight.ads.de.tech._tech.ProcessRole")*[](#keysight.ads.de.tech.PhysicalLayer.process_role "Link to this definition")

    *property* tech*: [Tech](#keysight.ads.de.tech.Tech "keysight.ads.de.tech._tech.Tech")*[](#keysight.ads.de.tech.PhysicalLayer.tech "Link to this definition")

*class* keysight.ads.de.tech.Purpose[](#keysight.ads.de.tech.Purpose "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.tech.Purpose.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* number*: int*[](#keysight.ads.de.tech.Purpose.number "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.tech.Purpose.name "Link to this definition")

    *property* tech*: [Tech](#keysight.ads.de.tech.Tech "keysight.ads.de.tech._tech.Tech")*[](#keysight.ads.de.tech.Purpose.tech "Link to this definition")

    *property* library*: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.de.tech.Purpose.library "Link to this definition")

    *property* abbreviation*: str*[](#keysight.ads.de.tech.Purpose.abbreviation "Link to this definition")

    *property* purpose\_type*: str*[](#keysight.ads.de.tech.Purpose.purpose_type "Link to this definition")

    *property* is\_reserved*: bool*[](#keysight.ads.de.tech.Purpose.is_reserved "Link to this definition")

*class* keysight.ads.de.tech.SmartMountSettings[](#keysight.ads.de.tech.SmartMountSettings "Link to this definition")
:   Holds the settings used to configure a SmartMount pcell or the default settings for a library.

    \_\_init\_\_(*tech: [Tech](#keysight.ads.de.tech.Tech "keysight.ads.de.tech._tech.Tech")*) → None[](#keysight.ads.de.tech.SmartMountSettings.__init__ "Link to this definition")

    *property* apply\_to\_all\_designs*: bool*[](#keysight.ads.de.tech.SmartMountSettings.apply_to_all_designs "Link to this definition")
    :   True if the settings are the applied automatically to all designs in the library.

    *property* subtype*: [SmartMountSubtype](#keysight.ads.de.tech.SmartMountSubtype "keysight.ads.de._pde.tech.SmartMountSubtype") | None*[](#keysight.ads.de.tech.SmartMountSettings.subtype "Link to this definition")
    :   The SmartMount subtype of the SmartMount pcell.

    *property* mapping\_option*: SmartMountMappingOption*[](#keysight.ads.de.tech.SmartMountSettings.mapping_option "Link to this definition")
    :   Specify mapping and alignment for the SmartMount pcell.

    *property* alignment\_type*: SmartMountAlignmentType*[](#keysight.ads.de.tech.SmartMountSettings.alignment_type "Link to this definition")
    :   The alignment type of the SmartMount pcell.

        This is only applicable if the mapping\_option is set to SmartMountMappingOption.NO\_MAPPING.

    *property* ael\_function*: str*[](#keysight.ads.de.tech.SmartMountSettings.ael_function "Link to this definition")
    :   The AEL function used to customize the SmartMount pcell.

    *property* ael\_parameters*: str*[](#keysight.ads.de.tech.SmartMountSettings.ael_parameters "Link to this definition")
    :   The AEL arguments to pass to the AEL function used to customize the SmartMount pcell.

    *property* scale\_factor*: float | None*[](#keysight.ads.de.tech.SmartMountSettings.scale_factor "Link to this definition")
    :   Optional scale factor applied to the SmartMount pcell or to all designs in the library.

*class* keysight.ads.de.tech.Tech[](#keysight.ads.de.tech.Tech "Link to this definition")
:   Represents a technology database for a library.

    This Tech can reference (i.e. inherit) the technology from other libraries.

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.tech.Tech.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* library*: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.de.tech.Tech.library "Link to this definition")

    *property* referenced\_lib\_names*: list[str]*[](#keysight.ads.de.tech.Tech.referenced_lib_names "Link to this definition")
    :   The names of the libraries directly referenced by this Tech.

    *property* all\_tech\_libs*: list[[Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")]*[](#keysight.ads.de.tech.Tech.all_tech_libs "Link to this definition")
    :   Return the complete collection of tech libraries.

    *property* default\_tech\_lib*: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library") | None*[](#keysight.ads.de.tech.Tech.default_tech_lib "Link to this definition")

    *property* is\_modified*: bool*[](#keysight.ads.de.tech.Tech.is_modified "Link to this definition")

    *property* dbu\_per\_uu*: int | None*[](#keysight.ads.de.tech.Tech.dbu_per_uu "Link to this definition")
    :   The ratio of database units to user units in layout views.

    *property* dbu\_per\_uu\_sch*: int | None*[](#keysight.ads.de.tech.Tech.dbu_per_uu_sch "Link to this definition")
    :   The ratio of database units to user units in schematic and symbol views.

    *property* user\_units*: str | None*[](#keysight.ads.de.tech.Tech.user_units "Link to this definition")
    :   The name of the user units used in layout views.

    *property* user\_units\_sch*: str | None*[](#keysight.ads.de.tech.Tech.user_units_sch "Link to this definition")
    :   The name of the user units used in schematic and symbol views.

    *property* default\_manufacturing\_grid*: int | None*[](#keysight.ads.de.tech.Tech.default_manufacturing_grid "Link to this definition")

    get\_default\_manufacturing\_grid(*local: bool = False*) → int[](#keysight.ads.de.tech.Tech.get_default_manufacturing_grid "Link to this definition")

    *property* multi\_tech\_scale\_factor*: float | None*[](#keysight.ads.de.tech.Tech.multi_tech_scale_factor "Link to this definition")
    :   The optional scale factor for multi-technology designs.

    create\_layer(*layer\_name: str*, *layer\_num: int*) → [PhysicalLayer](#keysight.ads.de.tech.PhysicalLayer "keysight.ads.de.tech._tech.PhysicalLayer")[](#keysight.ads.de.tech.Tech.create_layer "Link to this definition")
    :   Create a physical layer with the given name and number.

        create\_layer is deprecated, and will be removed in the 2025 Update 2 release. Use create\_physical\_layer() or PhysicalLayer.create().

    create\_physical\_layer(*layer\_name: str*, *layer\_num: int*) → [PhysicalLayer](#keysight.ads.de.tech.PhysicalLayer "keysight.ads.de.tech._tech.PhysicalLayer")[](#keysight.ads.de.tech.Tech.create_physical_layer "Link to this definition")

    create\_derived\_layer\_sizing(*layer\_name: str*, *layer\_num: int*, *operation: [LayerOp](#keysight.ads.de.tech.LayerOp "keysight.ads.de._pde.tech.LayerOp") | str*, *layer1: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer") | str*, *distance: int*) → [DerivedLayer](#keysight.ads.de.tech.DerivedLayer "keysight.ads.de.tech._tech.DerivedLayer")[](#keysight.ads.de.tech.Tech.create_derived_layer_sizing "Link to this definition")
    :   Create a derived layer from a single source layer, a sizing operation, and a distance parameter.

        The derived layer contains all the shapes that result by performing
        the sizing operation on all the shapes from the source layer.
        The sizing operation uses the distance parameter to change the size
        of each shape from the source layer.

    create\_derived\_layer\_boolean(*layer\_name: str*, *layer\_num: int*, *operation: [LayerOp](#keysight.ads.de.tech.LayerOp "keysight.ads.de._pde.tech.LayerOp") | str*, *layer1: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer") | str*, *layer2: [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer") | str*) → [DerivedLayer](#keysight.ads.de.tech.DerivedLayer "keysight.ads.de.tech._tech.DerivedLayer")[](#keysight.ads.de.tech.Tech.create_derived_layer_boolean "Link to this definition")
    :   Create a derived layer from two source layers and boolean operation.

        The derived layer contains all the shapes that result by performing
        the boolean operation on all the shapes from the two source layers.

    delete\_layer(*layer: str | int | [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer")*) → None[](#keysight.ads.de.tech.Tech.delete_layer "Link to this definition")

    delete\_all\_layers() → None[](#keysight.ads.de.tech.Tech.delete_all_layers "Link to this definition")

    find\_layer(*layer: int | str*, *local: bool = False*) → [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer") | None[](#keysight.ads.de.tech.Tech.find_layer "Link to this definition")

    layer(*layer: int | str*, *local: bool = False*) → [Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer")[](#keysight.ads.de.tech.Tech.layer "Link to this definition")

    layer\_numbers(*local: bool = False*) → list[int][](#keysight.ads.de.tech.Tech.layer_numbers "Link to this definition")
    :   Get the numbers of all the physical layers.

    layer\_names(*local: bool = False*) → list[str][](#keysight.ads.de.tech.Tech.layer_names "Link to this definition")
    :   Get the names of all the physical layers.

    *property* layers*: \_ReadOnlyNamedNumberedCollectionAbc[[Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer")]*[](#keysight.ads.de.tech.Tech.layers "Link to this definition")
    :   Return the collection of layers in this Tech database.

        The collection only includes Layers defined in this tech.

    *property* all\_layers*: \_ReadOnlyNamedNumberedCollectionAbc[[Layer](#keysight.ads.de.tech.Layer "keysight.ads.de.tech._tech.Layer")]*[](#keysight.ads.de.tech.Tech.all_layers "Link to this definition")
    :   Return the complete collection of layers in this Tech database.

        The collection also includes Layers from referenced technology.

    create\_purpose(*purpose\_name: str*, *purpose\_num: int*) → [Purpose](#keysight.ads.de.tech.Purpose "keysight.ads.de.tech._tech.Purpose")[](#keysight.ads.de.tech.Tech.create_purpose "Link to this definition")

    delete\_purpose(*purpose: [Purpose](#keysight.ads.de.tech.Purpose "keysight.ads.de.tech._tech.Purpose") | int | str*) → None[](#keysight.ads.de.tech.Tech.delete_purpose "Link to this definition")

    find\_purpose(*purpose: int | str*, *local: bool = False*) → [Purpose](#keysight.ads.de.tech.Purpose "keysight.ads.de.tech._tech.Purpose") | None[](#keysight.ads.de.tech.Tech.find_purpose "Link to this definition")

    purpose(*purpose: int | str*, *local: bool = False*) → [Purpose](#keysight.ads.de.tech.Purpose "keysight.ads.de.tech._tech.Purpose")[](#keysight.ads.de.tech.Tech.purpose "Link to this definition")

    purpose\_numbers(*local: bool = False*) → list[int][](#keysight.ads.de.tech.Tech.purpose_numbers "Link to this definition")
    :   Get the numbers of all the purposes.

    purpose\_names(*local: bool = False*) → list[str][](#keysight.ads.de.tech.Tech.purpose_names "Link to this definition")
    :   Get the names of all the purposes.

    *property* purposes*: \_ReadOnlyNamedNumberedCollectionAbc[[Purpose](#keysight.ads.de.tech.Purpose "keysight.ads.de.tech._tech.Purpose")]*[](#keysight.ads.de.tech.Tech.purposes "Link to this definition")
    :   Return the collection of Purposes in this Tech database.

        The collection only includes Purposes defined in this tech.

    *property* all\_purposes*: \_ReadOnlyNamedNumberedCollectionAbc[[Purpose](#keysight.ads.de.tech.Purpose "keysight.ads.de.tech._tech.Purpose")]*[](#keysight.ads.de.tech.Tech.all_purposes "Link to this definition")
    :   Return the complete collection of Purposes in this Tech database.

        The collection also includes Purposes from referenced technology.

    *property* padstacks*: [NamedMutableCollectionAbc](../collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[Padstack](pads/pads.md#keysight.ads.de.tech.pads.Padstack "keysight.ads.de.tech.pads.Padstack")]*[](#keysight.ads.de.tech.Tech.padstacks "Link to this definition")
    :   Return the collection of padstacks in this Tech database.

        The collection only includes padstacks defined in this tech.

    *static* get\_padstack\_from\_lib(*lib\_padstack\_name: str*) → [Padstack](pads/pads.md#keysight.ads.de.tech.pads.Padstack "keysight.ads.de.tech.pads.Padstack")[](#keysight.ads.de.tech.Tech.get_padstack_from_lib "Link to this definition")
    :   Return the specified Padstack.

        The name must be of the form ‘lib:padstack’. Both the library
        and the Padstack must exist.

    create\_padstack(*name: str*) → [Padstack](pads/pads.md#keysight.ads.de.tech.pads.Padstack "keysight.ads.de.tech.pads.Padstack")[](#keysight.ads.de.tech.Tech.create_padstack "Link to this definition")

    delete\_padstack(*padstack: [Padstack](pads/pads.md#keysight.ads.de.tech.pads.Padstack "keysight.ads.de.tech.pads.Padstack")*) → None[](#keysight.ads.de.tech.Tech.delete_padstack "Link to this definition")
    :   Delete the padstack.

        > The padstack must be defined in this Tech.
        > The padstack object will be invalid after it has been deleted.

        delete\_padstack is deprecated, and will be removed in the 2025 Update 2 release. del(padstacks[name]).

    save\_padstacks() → None[](#keysight.ads.de.tech.Tech.save_padstacks "Link to this definition")
    :   Save the Padstack definitions to this Tech’s library.

    *property* via\_rules*: [NamedMutableCollectionAbc](../collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[ViaRule](rule/rule.md#keysight.ads.de.tech.rule.ViaRule "keysight.ads.de.tech.rule.ViaRule")]*[](#keysight.ads.de.tech.Tech.via_rules "Link to this definition")
    :   Return the collection of via rules in this Tech database.

        The collection only includes via rules defined in this tech.

    *property* stacked\_via\_rules*: [NamedMutableCollectionAbc](../collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[StackedViaRule](rule/rule.md#keysight.ads.de.tech.rule.StackedViaRule "keysight.ads.de.tech.rule.StackedViaRule")]*[](#keysight.ads.de.tech.Tech.stacked_via_rules "Link to this definition")
    :   Return the collection of stacked via rules in this Tech database.

        The collection only includes stacked via rules defined in this tech.

    *property* teardrop\_rules*: [NamedMutableCollectionAbc](../collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[TeardropRule](rule/rule.md#keysight.ads.de.tech.rule.TeardropRule "keysight.ads.de.tech.rule.TeardropRule")]*[](#keysight.ads.de.tech.Tech.teardrop_rules "Link to this definition")
    :   Return the collection of teardrop rules in this Tech database.

        The collection only includes teardrop rules defined in this tech.

    *property* clearance\_rules*: [NamedMutableCollectionAbc](../collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[ClearanceRule](rule/rule.md#keysight.ads.de.tech.rule.ClearanceRule "keysight.ads.de.tech.rule.ClearanceRule")]*[](#keysight.ads.de.tech.Tech.clearance_rules "Link to this definition")
    :   Return the collection of clearance rules in this Tech database.

        The collection only includes clearance rules defined in this tech.

    *property* line\_types*: [NamedMutableCollectionAbc](../collections.md#keysight.ads.de._list_like.NamedMutableCollectionAbc "keysight.ads.de._list_like.NamedMutableCollectionAbc")[[LineItem](#keysight.ads.de.tech.LineItem "keysight.ads.de.tech._tech.LineItem")]*[](#keysight.ads.de.tech.Tech.line_types "Link to this definition")
    :   Return the collection of line types in this Tech database.

        The collection only includes line types defined in this tech.

    *property* layer\_maps*: NamedListRefAbc[[LayerMap](nested/nested.md#keysight.ads.de.tech.nested.LayerMap "keysight.ads.de.tech.nested.LayerMap")]*[](#keysight.ads.de.tech.Tech.layer_maps "Link to this definition")
    :   Return the collection of layer maps in this Tech database.

    *property* props*: NamedReadableCollectionAbc[[Property](../db/properties.md#keysight.ads.de.db.Property "keysight.ads.de.db.Property")]*[](#keysight.ads.de.tech.Tech.props "Link to this definition")

    find\_prop(*name: str*) → [Property](../db/properties.md#keysight.ads.de.db.Property "keysight.ads.de.db.Property") | None[](#keysight.ads.de.tech.Tech.find_prop "Link to this definition")

    save\_rules() → None[](#keysight.ads.de.tech.Tech.save_rules "Link to this definition")
    :   Save the design rules to this Tech’s library.

    save\_line\_types() → None[](#keysight.ads.de.tech.Tech.save_line_types "Link to this definition")
    :   Save the line types to this Tech’s library.

    save\_layer\_maps() → None[](#keysight.ads.de.tech.Tech.save_layer_maps "Link to this definition")
    :   Save the layer maps to this Tech’s library.

    save() → None[](#keysight.ads.de.tech.Tech.save "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.tech.LayerOp[](#keysight.ads.de.tech.LayerOp "Link to this definition")
:   Defines the type of a derived layer operation.

    Members:

    > AND : Boolean operation
    >
    > OR : Boolean operation
    >
    > NOT : Boolean operation
    >
    > XOR : Boolean operation
    >
    > TOUCHING
    >
    > BUTTONLY
    >
    > USER\_DEFINED : Don’t use this for a derived layer operation - use the name instead.
    >
    > INSIDE
    >
    > OUTSIDE
    >
    > OVERLAPPING
    >
    > STRADDLING
    >
    > AVOIDING
    >
    > BUTTING
    >
    > COINCIDENT
    >
    > COINCIDENT\_ONLY
    >
    > BUTTING\_OR\_COINCIDENT
    >
    > BUTTING\_OR\_OVERLAPPING
    >
    > AREA
    >
    > GROW : Sizing operation
    >
    > SHRINK : Sizing operation
    >
    > GROW\_VERTICAL : Sizing operation
    >
    > GROW\_HORIZONTAL : Sizing operation
    >
    > SHRINK\_VERTICAL : Sizing operation
    >
    > SHRINK\_HORIZONTAL : Sizing operation
    >
    > SELECT

    AND *= <LayerOp.AND: 0>*[](#keysight.ads.de.tech.LayerOp.AND "Link to this definition")

    AREA *= <LayerOp.AREA: 18>*[](#keysight.ads.de.tech.LayerOp.AREA "Link to this definition")

    AVOIDING *= <LayerOp.AVOIDING: 11>*[](#keysight.ads.de.tech.LayerOp.AVOIDING "Link to this definition")

    BUTTING *= <LayerOp.BUTTING: 12>*[](#keysight.ads.de.tech.LayerOp.BUTTING "Link to this definition")

    BUTTING\_OR\_COINCIDENT *= <LayerOp.BUTTING\_OR\_COINCIDENT: 16>*[](#keysight.ads.de.tech.LayerOp.BUTTING_OR_COINCIDENT "Link to this definition")

    BUTTING\_OR\_OVERLAPPING *= <LayerOp.BUTTING\_OR\_OVERLAPPING: 17>*[](#keysight.ads.de.tech.LayerOp.BUTTING_OR_OVERLAPPING "Link to this definition")

    BUTTONLY *= <LayerOp.BUTTONLY: 5>*[](#keysight.ads.de.tech.LayerOp.BUTTONLY "Link to this definition")

    COINCIDENT *= <LayerOp.COINCIDENT: 13>*[](#keysight.ads.de.tech.LayerOp.COINCIDENT "Link to this definition")

    COINCIDENT\_ONLY *= <LayerOp.COINCIDENT\_ONLY: 14>*[](#keysight.ads.de.tech.LayerOp.COINCIDENT_ONLY "Link to this definition")

    GROW *= <LayerOp.GROW: 19>*[](#keysight.ads.de.tech.LayerOp.GROW "Link to this definition")

    GROW\_HORIZONTAL *= <LayerOp.GROW\_HORIZONTAL: 22>*[](#keysight.ads.de.tech.LayerOp.GROW_HORIZONTAL "Link to this definition")

    GROW\_VERTICAL *= <LayerOp.GROW\_VERTICAL: 21>*[](#keysight.ads.de.tech.LayerOp.GROW_VERTICAL "Link to this definition")

    INSIDE *= <LayerOp.INSIDE: 7>*[](#keysight.ads.de.tech.LayerOp.INSIDE "Link to this definition")

    NOT *= <LayerOp.NOT: 2>*[](#keysight.ads.de.tech.LayerOp.NOT "Link to this definition")

    OR *= <LayerOp.OR: 1>*[](#keysight.ads.de.tech.LayerOp.OR "Link to this definition")

    OUTSIDE *= <LayerOp.OUTSIDE: 8>*[](#keysight.ads.de.tech.LayerOp.OUTSIDE "Link to this definition")

    OVERLAPPING *= <LayerOp.OVERLAPPING: 9>*[](#keysight.ads.de.tech.LayerOp.OVERLAPPING "Link to this definition")

    SELECT *= <LayerOp.SELECT: 25>*[](#keysight.ads.de.tech.LayerOp.SELECT "Link to this definition")

    SHRINK *= <LayerOp.SHRINK: 20>*[](#keysight.ads.de.tech.LayerOp.SHRINK "Link to this definition")

    SHRINK\_HORIZONTAL *= <LayerOp.SHRINK\_HORIZONTAL: 24>*[](#keysight.ads.de.tech.LayerOp.SHRINK_HORIZONTAL "Link to this definition")

    SHRINK\_VERTICAL *= <LayerOp.SHRINK\_VERTICAL: 23>*[](#keysight.ads.de.tech.LayerOp.SHRINK_VERTICAL "Link to this definition")

    STRADDLING *= <LayerOp.STRADDLING: 10>*[](#keysight.ads.de.tech.LayerOp.STRADDLING "Link to this definition")

    TOUCHING *= <LayerOp.TOUCHING: 4>*[](#keysight.ads.de.tech.LayerOp.TOUCHING "Link to this definition")

    USER\_DEFINED *= <LayerOp.USER\_DEFINED: 6>*[](#keysight.ads.de.tech.LayerOp.USER_DEFINED "Link to this definition")

    XOR *= <LayerOp.XOR: 3>*[](#keysight.ads.de.tech.LayerOp.XOR "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.tech.LayerOp](#keysight.ads.de.tech.LayerOp "keysight.ads.de._pde.tech.LayerOp")*, *value: int*) → None[](#keysight.ads.de.tech.LayerOp.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.tech.LayerOp.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.tech.LayerOp.name "Link to this definition")

    *property* str[](#keysight.ads.de.tech.LayerOp.str "Link to this definition")
    :   Return the string used as the operation name.

    *property* value[](#keysight.ads.de.tech.LayerOp.value "Link to this definition")

*class* keysight.ads.de.tech.LineEndType[](#keysight.ads.de.tech.LineEndType "Link to this definition")
:   Defines the type of ending used by a LineItem.

    Members:

    > TRUNCATED : ‘Truncated’: The line ends are truncated.
    >
    > EXTENDED : ‘Extended’: The line ends are extended.
    >
    > CHAMFERED : ‘Chamfered’: The line ends are chamfered.
    >
    > ROUNDED : ‘Rounded’: The line ends are rounded.

    CHAMFERED *= <LineEndType.CHAMFERED: 2>*[](#keysight.ads.de.tech.LineEndType.CHAMFERED "Link to this definition")

    EXTENDED *= <LineEndType.EXTENDED: 1>*[](#keysight.ads.de.tech.LineEndType.EXTENDED "Link to this definition")

    ROUNDED *= <LineEndType.ROUNDED: 3>*[](#keysight.ads.de.tech.LineEndType.ROUNDED "Link to this definition")

    TRUNCATED *= <LineEndType.TRUNCATED: 0>*[](#keysight.ads.de.tech.LineEndType.TRUNCATED "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.tech.LineEndType](#keysight.ads.de.tech.LineEndType "keysight.ads.de._pde.tech.LineEndType")*, *value: int*) → None[](#keysight.ads.de.tech.LineEndType.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.tech.LineEndType.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.tech.LineEndType.name "Link to this definition")

    *property* str[](#keysight.ads.de.tech.LineEndType.str "Link to this definition")
    :   Return the string representation of the LineEndType.

    *property* value[](#keysight.ads.de.tech.LineEndType.value "Link to this definition")

*class* keysight.ads.de.tech.LineCornerType[](#keysight.ads.de.tech.LineCornerType "Link to this definition")
:   Defines the type of corner used by LineTypeInfo.

    Members:

    > SQUARE : ‘Square’: The line has square corners.
    >
    > MITERED : ‘Mitered’: The line has mitered corners - prefer ADAPTIVE\_MITERED.
    >
    > ADAPTIVE\_MITERED : ‘AdaptiveMitered’: The line has mitered corners with consistent cut length.
    >
    > CURVED : ‘Curved’: The line has curved corners with a specified radius.
    >
    > ROUND : ‘Round’: The line has rounded corners.

    ADAPTIVE\_MITERED *= <LineCornerType.ADAPTIVE\_MITERED: 2>*[](#keysight.ads.de.tech.LineCornerType.ADAPTIVE_MITERED "Link to this definition")

    CURVED *= <LineCornerType.CURVED: 3>*[](#keysight.ads.de.tech.LineCornerType.CURVED "Link to this definition")

    MITERED *= <LineCornerType.MITERED: 1>*[](#keysight.ads.de.tech.LineCornerType.MITERED "Link to this definition")

    ROUND *= <LineCornerType.ROUND: 4>*[](#keysight.ads.de.tech.LineCornerType.ROUND "Link to this definition")

    SQUARE *= <LineCornerType.SQUARE: 0>*[](#keysight.ads.de.tech.LineCornerType.SQUARE "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.tech.LineCornerType](#keysight.ads.de.tech.LineCornerType "keysight.ads.de._pde.tech.LineCornerType")*, *value: int*) → None[](#keysight.ads.de.tech.LineCornerType.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.tech.LineCornerType.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.tech.LineCornerType.name "Link to this definition")

    *property* str[](#keysight.ads.de.tech.LineCornerType.str "Link to this definition")
    :   Return the string representation of the Line Corner Type.

    *property* value[](#keysight.ads.de.tech.LineCornerType.value "Link to this definition")

*class* keysight.ads.de.tech.LineStripSpacingType[](#keysight.ads.de.tech.LineStripSpacingType "Link to this definition")
:   Defines the type of spacing between line strips.

    Members:

    > NO\_SPACING : ‘NoSpacing’: The line strip items have no spacing.
    >
    > EDGE\_TO\_EDGE : ‘EdgeToEdge’: The line strips use edge-to-edge spacing.
    >
    > CENTER\_LINE : ‘CenterLine’: The line strips use center-line-to-center-line spacing.

    CENTER\_LINE *= <LineStripSpacingType.CENTER\_LINE: 2>*[](#keysight.ads.de.tech.LineStripSpacingType.CENTER_LINE "Link to this definition")

    EDGE\_TO\_EDGE *= <LineStripSpacingType.EDGE\_TO\_EDGE: 1>*[](#keysight.ads.de.tech.LineStripSpacingType.EDGE_TO_EDGE "Link to this definition")

    NO\_SPACING *= <LineStripSpacingType.NO\_SPACING: 0>*[](#keysight.ads.de.tech.LineStripSpacingType.NO_SPACING "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.tech.LineStripSpacingType](#keysight.ads.de.tech.LineStripSpacingType "keysight.ads.de._pde.tech.LineStripSpacingType")*, *value: int*) → None[](#keysight.ads.de.tech.LineStripSpacingType.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.tech.LineStripSpacingType.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.tech.LineStripSpacingType.name "Link to this definition")

    *property* str[](#keysight.ads.de.tech.LineStripSpacingType.str "Link to this definition")
    :   Return the string representation of the LineEndType.

    *property* value[](#keysight.ads.de.tech.LineStripSpacingType.value "Link to this definition")

*class* keysight.ads.de.tech.OAMaterial[](#keysight.ads.de.tech.OAMaterial "Link to this definition")
:   Members:

    OTHER

    N\_WELL

    P\_WELL

    N\_DIFF

    P\_DIFF

    N\_IMPLANT

    P\_IMPLANT

    POLY

    CUT

    METAL

    CONTACTLESS\_METAL

    DIFF

    RECOGNITION

    PASSIVATION\_CUT

    CONTACTLESS\_METAL *= <OAMaterial.CONTACTLESS\_METAL: 10>*[](#keysight.ads.de.tech.OAMaterial.CONTACTLESS_METAL "Link to this definition")

    CUT *= <OAMaterial.CUT: 8>*[](#keysight.ads.de.tech.OAMaterial.CUT "Link to this definition")

    DIFF *= <OAMaterial.DIFF: 11>*[](#keysight.ads.de.tech.OAMaterial.DIFF "Link to this definition")

    METAL *= <OAMaterial.METAL: 9>*[](#keysight.ads.de.tech.OAMaterial.METAL "Link to this definition")

    N\_DIFF *= <OAMaterial.N\_DIFF: 3>*[](#keysight.ads.de.tech.OAMaterial.N_DIFF "Link to this definition")

    N\_IMPLANT *= <OAMaterial.N\_IMPLANT: 5>*[](#keysight.ads.de.tech.OAMaterial.N_IMPLANT "Link to this definition")

    N\_WELL *= <OAMaterial.N\_WELL: 1>*[](#keysight.ads.de.tech.OAMaterial.N_WELL "Link to this definition")

    OTHER *= <OAMaterial.OTHER: 0>*[](#keysight.ads.de.tech.OAMaterial.OTHER "Link to this definition")

    PASSIVATION\_CUT *= <OAMaterial.PASSIVATION\_CUT: 13>*[](#keysight.ads.de.tech.OAMaterial.PASSIVATION_CUT "Link to this definition")

    POLY *= <OAMaterial.POLY: 7>*[](#keysight.ads.de.tech.OAMaterial.POLY "Link to this definition")

    P\_DIFF *= <OAMaterial.P\_DIFF: 4>*[](#keysight.ads.de.tech.OAMaterial.P_DIFF "Link to this definition")

    P\_IMPLANT *= <OAMaterial.P\_IMPLANT: 6>*[](#keysight.ads.de.tech.OAMaterial.P_IMPLANT "Link to this definition")

    P\_WELL *= <OAMaterial.P\_WELL: 2>*[](#keysight.ads.de.tech.OAMaterial.P_WELL "Link to this definition")

    RECOGNITION *= <OAMaterial.RECOGNITION: 12>*[](#keysight.ads.de.tech.OAMaterial.RECOGNITION "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.tech.OAMaterial](#keysight.ads.de.tech.OAMaterial "keysight.ads.de._pde.tech.OAMaterial")*, *value: int*) → None[](#keysight.ads.de.tech.OAMaterial.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.tech.OAMaterial.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.tech.OAMaterial.name "Link to this definition")

    *property* str[](#keysight.ads.de.tech.OAMaterial.str "Link to this definition")

    *property* value[](#keysight.ads.de.tech.OAMaterial.value "Link to this definition")

*class* keysight.ads.de.tech.ProcessRole[](#keysight.ads.de.tech.ProcessRole "Link to this definition")
:   NOT\_DEFINED *= <ProcessRole.NOT\_DEFINED: 0>*[](#keysight.ads.de.tech.ProcessRole.NOT_DEFINED "Link to this definition")

    NONE *= <ProcessRole.NOT\_DEFINED: 0>*[](#keysight.ads.de.tech.ProcessRole.NONE "Link to this definition")

    CONDUCTOR *= <ProcessRole.CONDUCTOR: 1>*[](#keysight.ads.de.tech.ProcessRole.CONDUCTOR "Link to this definition")

    SEMICONDUCTOR *= <ProcessRole.SEMICONDUCTOR: 2>*[](#keysight.ads.de.tech.ProcessRole.SEMICONDUCTOR "Link to this definition")

    DIELECTRIC *= <ProcessRole.DIELECTRIC: 3>*[](#keysight.ads.de.tech.ProcessRole.DIELECTRIC "Link to this definition")

    CONDUCTOR\_VIA *= <ProcessRole.CONDUCTOR\_VIA: 4>*[](#keysight.ads.de.tech.ProcessRole.CONDUCTOR_VIA "Link to this definition")

    SEMICONDUCTOR\_VIA *= <ProcessRole.SEMICONDUCTOR\_VIA: 5>*[](#keysight.ads.de.tech.ProcessRole.SEMICONDUCTOR_VIA "Link to this definition")

    DIELECTRIC\_VIA *= <ProcessRole.DIELECTRIC\_VIA: 6>*[](#keysight.ads.de.tech.ProcessRole.DIELECTRIC_VIA "Link to this definition")

    CONDUCTOR\_SLOT *= <ProcessRole.CONDUCTOR\_SLOT: 7>*[](#keysight.ads.de.tech.ProcessRole.CONDUCTOR_SLOT "Link to this definition")

    SEMICONDUCTOR\_SLOT *= <ProcessRole.SEMICONDUCTOR\_SLOT: 8>*[](#keysight.ads.de.tech.ProcessRole.SEMICONDUCTOR_SLOT "Link to this definition")

    DIELECTRIC\_SLOT *= <ProcessRole.DIELECTRIC\_SLOT: 9>*[](#keysight.ads.de.tech.ProcessRole.DIELECTRIC_SLOT "Link to this definition")

    DRC *= <ProcessRole.DRC: 10>*[](#keysight.ads.de.tech.ProcessRole.DRC "Link to this definition")

    BOUNDARY *= <ProcessRole.BOUNDARY: 11>*[](#keysight.ads.de.tech.ProcessRole.BOUNDARY "Link to this definition")

    HEAT\_SOURCE *= <ProcessRole.HEAT\_SOURCE: 12>*[](#keysight.ads.de.tech.ProcessRole.HEAT_SOURCE "Link to this definition")

    COMPONENT\_BODY *= <ProcessRole.COMPONENT\_BODY: 13>*[](#keysight.ads.de.tech.ProcessRole.COMPONENT_BODY "Link to this definition")

    ANNOT\_INSTANCE\_NAME *= <ProcessRole.ANNOT\_INSTANCE\_NAME: 15>*[](#keysight.ads.de.tech.ProcessRole.ANNOT_INSTANCE_NAME "Link to this definition")

    ANNOT\_COMPONENT\_NAME *= <ProcessRole.ANNOT\_COMPONENT\_NAME: 16>*[](#keysight.ads.de.tech.ProcessRole.ANNOT_COMPONENT_NAME "Link to this definition")

    ANNOT\_OTHER *= <ProcessRole.ANNOT\_OTHER: 17>*[](#keysight.ads.de.tech.ProcessRole.ANNOT_OTHER "Link to this definition")

    SOLDER\_MASK *= <ProcessRole.SOLDER\_MASK: 18>*[](#keysight.ads.de.tech.ProcessRole.SOLDER_MASK "Link to this definition")

    SOLDER\_PASTE *= <ProcessRole.SOLDER\_PASTE: 19>*[](#keysight.ads.de.tech.ProcessRole.SOLDER_PASTE "Link to this definition")

    SILK\_SCREEN *= <ProcessRole.SILK\_SCREEN: 20>*[](#keysight.ads.de.tech.ProcessRole.SILK_SCREEN "Link to this definition")

    SCRATCH *= <ProcessRole.SCRATCH: 21>*[](#keysight.ads.de.tech.ProcessRole.SCRATCH "Link to this definition")

    OTHER *= <ProcessRole.OTHER: 22>*[](#keysight.ads.de.tech.ProcessRole.OTHER "Link to this definition")

    *property* str*: str*[](#keysight.ads.de.tech.ProcessRole.str "Link to this definition")
    :   Return the string displayed in the UI.

*class* keysight.ads.de.tech.SmartMountSubtype[](#keysight.ads.de.tech.SmartMountSubtype "Link to this definition")
:   Defines the subtype of a SmartMount PCell.

    Members:

    > NONE : ‘None’: No subtype.
    >
    > BOTTOM\_MOUNT : ‘BottomMount’: The bottom metal layers of the chip are mapped to the mount layer on the module.
    >
    > FLIP\_CHIP : ‘FlipChip’: The top metal layers of the chip are mapped to the mount layer on the module.
    >
    > CUSTOM : ‘Custom’: The mapped layers are determined by a custom function.
    >
    > MULTI\_MOUNT : ‘MultiMount’: The chip has multiple mount layers.

    BOTTOM\_MOUNT *= <SmartMountSubtype.BOTTOM\_MOUNT: 1>*[](#keysight.ads.de.tech.SmartMountSubtype.BOTTOM_MOUNT "Link to this definition")

    CUSTOM *= <SmartMountSubtype.CUSTOM: 3>*[](#keysight.ads.de.tech.SmartMountSubtype.CUSTOM "Link to this definition")

    FLIP\_CHIP *= <SmartMountSubtype.FLIP\_CHIP: 2>*[](#keysight.ads.de.tech.SmartMountSubtype.FLIP_CHIP "Link to this definition")

    MULTI\_MOUNT *= <SmartMountSubtype.MULTI\_MOUNT: 4>*[](#keysight.ads.de.tech.SmartMountSubtype.MULTI_MOUNT "Link to this definition")

    NONE *= <SmartMountSubtype.NONE: 0>*[](#keysight.ads.de.tech.SmartMountSubtype.NONE "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.tech.SmartMountSubtype](#keysight.ads.de.tech.SmartMountSubtype "keysight.ads.de._pde.tech.SmartMountSubtype")*, *value: int*) → None[](#keysight.ads.de.tech.SmartMountSubtype.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.tech.SmartMountSubtype.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.tech.SmartMountSubtype.name "Link to this definition")

    *property* str[](#keysight.ads.de.tech.SmartMountSubtype.str "Link to this definition")

    *property* value[](#keysight.ads.de.tech.SmartMountSubtype.value "Link to this definition")

## Functions[](#functions "Link to this heading")

> keysight.ads.de.tech.create\_tech(*lib: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*) → [Tech](#keysight.ads.de.tech.Tech "keysight.ads.de.tech._tech.Tech")[](#keysight.ads.de.tech.create_tech "Link to this definition")
>
> keysight.ads.de.tech.delete\_tech(*lib: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*) → None[](#keysight.ads.de.tech.delete_tech "Link to this definition")

On this page

[Previous

keysight.ads.de.tech](index.md)
[Next

Padstacks](pads/pads.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top