<!-- 来源: pypde\docs\reference\de\tech\pads\pads.html -->

[![Logo](../../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../../index.md)
* [Design](../../../../index.md)
* [Reference](../../../index.md)
* [keysight.ads.de.tech](../index.md)
* Padstacks

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

* [Introduction](../../../../../../pydocs/intro/index.md)
  + [Licensing](../../../../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../../../../pydocs/intro/extension.md)
* [Concepts](../../../../../../pydocs/concepts/index.md)
  + [Terminology](../../../../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../../../../pydocs/concepts/execution.md)
* [How-To](../../../../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../../../../pydocs/howto/pytest.md)

* [Design](../../../../index.md)
  + [Reference](../../../index.md)
    - [keysight.ads.de](../../index.md)
      * [Workspace](../../workspace.md)
      * [Library](../../library.md)
      * [Cell](../../cell.md)
      * [View](../../view.md)
      * [CellviewRef](../../cellviewref.md)
      * [DesignHierarchy](../../design_hierarchy.md)
      * [DMData](../../dmdata.md)
      * [ItemInfo](../../item_info.md)
      * [Points](../../points.md)
      * [Collections](../../collections.md)
    - [keysight.ads.de.ael](../../ael.md)
    - [keysight.ads.de.app](../../app/index.md)
      * [Actions and Menus](../../app/action.md)
      * [Addons](../../app/addon.md)
      * [Callbacks](../../app/callbacks.md)
      * [Windows and Widgets](../../app/window.md)
    - [keysight.ads.de.db](../../db/index.md)
      * [Callbacks](../../db/callbacks.md)
      * [Enumerated Types](../../db/enums.md)
      * [Parameter Forms](../../db/forms.md)
      * [GenPolyline](../../db/genpolyline.md)
      * [Model Definition](../../db/model_def.md)
      * [Parameters](../../db/parameters.md)
      * [Properties](../../db/properties.md)
      * [Transaction](../../db/transaction.md)
    - [keysight.ads.de.db\_dbu](../../db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../../db_uu/index.md)
      * [Design Elements](../../db_uu/db_uu.md)
      * [LayerId](../../db_uu/layer_id.md)
      * [LineTypeInfo](../../db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../../experimental/index.md)
      * [CDF](../../experimental/cdf/index.md)
      * [Commands](../../experimental/commands.md)
      * [Handles](../../experimental/handles.md)
      * [Netlist Utilities](../../experimental/netlist_helper.md)
      * [Polygon Utilities](../../experimental/polygon_utils.md)
      * [Preferences](../../experimental/preferences.md)
      * [xxPro View](../../experimental/pro_view.md)
      * [Symbol Generator](../../experimental/symbol.md)
      * [Text Maker](../../experimental/text_maker.md)
    - [keysight.ads.de.tech](../index.md)
      * [Tech](../tech.md)
      * Padstacks
      * [Via Rules](../rule/rule.md)
      * [Nested Technology](../nested/nested.md)
    - [keysight.ads.de.app.dds](../../app/dds.md)
  + [Examples](../../../../examples/index.md)
    - [Calling Between AEL and Python](../../../../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../../../examples/ex_create_layout.md)
    - [Create Schematic](../../../../examples/ex_create_schematic.md)
    - [Create Workspace](../../../../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../../../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../../../examples/ex_cdf.md)
    - [Component Parameters](../../../../examples/ex_parameters.md)
    - [Creating an Item Definition](../../../../examples/ex_itemdef.md)
    - [Model Definition Properties](../../../../examples/ex_model.md)
    - [Adding Instances to a Design](../../../../examples/ex_lpf.md)
    - [Properties](../../../../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../../../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../../../examples/ex_padstack.md)
    - [Nested Technology](../../../../examples/ex_nested.md)
    - [Rules](../../../../examples/ex_rules.md)
    - [Placing Text](../../../../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../../../examples/ex_polygon.md)
    - [PySide2](../../../../examples/ex_pyside.md)
    - [Traversing Hierarchy](../../../../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../../../examples/ex_working_with_var.md)
    - [XML RPC](../../../../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../../../examples/ex_translate_gds.md)
* [Technology](../../../../../../pysubst/docs/index.md)
  + [Reference](../../../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Padstacks[](#padstacks "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.tech.pads.LengthValue[](#keysight.ads.de.tech.pads.LengthValue "Link to this definition")
:   A length value with units.

    Supports the following units: ‘mil’, ‘in’, ‘um’, ‘mm’, ‘cm’, ‘meter’, ‘ft’, ‘nm’.
    A value that does not have units is assumed to be in meters.

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[](#keysight.ads.de.tech.pads.LengthValue.__init__ "Link to this definition")
    :   Overloaded function.

        1. \_\_init\_\_(self: keysight.ads.de.\_pde.tech.LengthValue, arg0: str) -> None
        2. \_\_init\_\_(self: keysight.ads.de.\_pde.tech.LengthValue, arg0: str, arg1: str) -> None

    mks(*self: [keysight.ads.de.\_pde.tech.LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*) → float[](#keysight.ads.de.tech.pads.LengthValue.mks "Link to this definition")

    *property* value[](#keysight.ads.de.tech.pads.LengthValue.value "Link to this definition")

*class* keysight.ads.de.tech.pads.LayerMatcher[](#keysight.ads.de.tech.pads.LayerMatcher "Link to this definition")
:   Base class for classes that determine which layer to use for pads in Padstacks.

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.tech.pads.LayerMatcher.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *static* is\_id\_matcher(*o: [LayerMatcher](#keysight.ads.de.tech.pads.LayerMatcher "keysight.ads.de.tech.pads.LayerMatcher")*) → TypeGuard[[MatchLayerById](#keysight.ads.de.tech.pads.MatchLayerById "keysight.ads.de.tech.pads.MatchLayerById")][](#keysight.ads.de.tech.pads.LayerMatcher.is_id_matcher "Link to this definition")

    *static* is\_name\_matcher(*o: [LayerMatcher](#keysight.ads.de.tech.pads.LayerMatcher "keysight.ads.de.tech.pads.LayerMatcher")*) → TypeGuard[[MatchLayerByName](#keysight.ads.de.tech.pads.MatchLayerByName "keysight.ads.de.tech.pads.MatchLayerByName")][](#keysight.ads.de.tech.pads.LayerMatcher.is_name_matcher "Link to this definition")

    *static* is\_from\_top\_matcher(*o: [LayerMatcher](#keysight.ads.de.tech.pads.LayerMatcher "keysight.ads.de.tech.pads.LayerMatcher")*) → TypeGuard[[MatchLayerFromTopOfBoard](#keysight.ads.de.tech.pads.MatchLayerFromTopOfBoard "keysight.ads.de.tech.pads.MatchLayerFromTopOfBoard")][](#keysight.ads.de.tech.pads.LayerMatcher.is_from_top_matcher "Link to this definition")

    *static* is\_from\_bottom\_matcher(*o: [LayerMatcher](#keysight.ads.de.tech.pads.LayerMatcher "keysight.ads.de.tech.pads.LayerMatcher")*) → TypeGuard[[MatchLayerFromBottomOfBoard](#keysight.ads.de.tech.pads.MatchLayerFromBottomOfBoard "keysight.ads.de.tech.pads.MatchLayerFromBottomOfBoard")][](#keysight.ads.de.tech.pads.LayerMatcher.is_from_bottom_matcher "Link to this definition")

*class* keysight.ads.de.tech.pads.MatchLayerById[](#keysight.ads.de.tech.pads.MatchLayerById "Link to this definition")
:   Matches the layers by LayerId.

    \_\_init\_\_(*layer\_id: [LayerId](../../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*) → None[](#keysight.ads.de.tech.pads.MatchLayerById.__init__ "Link to this definition")

    *property* id*: [LayerId](../../db_uu/layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*[](#keysight.ads.de.tech.pads.MatchLayerById.id "Link to this definition")

*class* keysight.ads.de.tech.pads.MatchLayerByName[](#keysight.ads.de.tech.pads.MatchLayerByName "Link to this definition")
:   Matches the layers by layer name.

    \_\_init\_\_(*name: str*) → None[](#keysight.ads.de.tech.pads.MatchLayerByName.__init__ "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.tech.pads.MatchLayerByName.name "Link to this definition")

*class* keysight.ads.de.tech.pads.MatchLayerFromBottomOfBoard[](#keysight.ads.de.tech.pads.MatchLayerFromBottomOfBoard "Link to this definition")
:   Matches the layer relative to the bottom of the board.

    \_\_init\_\_(*offset: int*, *role: str | [ProcessRole](../tech.md#keysight.ads.de.tech.ProcessRole "keysight.ads.de.tech.ProcessRole")*) → None[](#keysight.ads.de.tech.pads.MatchLayerFromBottomOfBoard.__init__ "Link to this definition")

    *property* offset*: int*[](#keysight.ads.de.tech.pads.MatchLayerFromBottomOfBoard.offset "Link to this definition")

    *property* process\_role*: [ProcessRole](../tech.md#keysight.ads.de.tech.ProcessRole "keysight.ads.de.tech.ProcessRole")*[](#keysight.ads.de.tech.pads.MatchLayerFromBottomOfBoard.process_role "Link to this definition")

*class* keysight.ads.de.tech.pads.MatchLayerFromTopOfBoard[](#keysight.ads.de.tech.pads.MatchLayerFromTopOfBoard "Link to this definition")
:   Matches the layer relative to the top of the board.

    \_\_init\_\_(*offset: int*, *role: str | [ProcessRole](../tech.md#keysight.ads.de.tech.ProcessRole "keysight.ads.de.tech.ProcessRole")*) → None[](#keysight.ads.de.tech.pads.MatchLayerFromTopOfBoard.__init__ "Link to this definition")

    *property* offset*: int*[](#keysight.ads.de.tech.pads.MatchLayerFromTopOfBoard.offset "Link to this definition")

    *property* process\_role*: [ProcessRole](../tech.md#keysight.ads.de.tech.ProcessRole "keysight.ads.de.tech.ProcessRole")*[](#keysight.ads.de.tech.pads.MatchLayerFromTopOfBoard.process_role "Link to this definition")

*class* keysight.ads.de.tech.pads.Antipad[](#keysight.ads.de.tech.pads.Antipad "Link to this definition")
:   *class* Mode
    :   Defines the mode of an Antipad.

        Members:

        > USE\_DEFAULT : ‘UseDefault’: Use the antipad mode defined in the default PadLayerEntry.
        >
        > NONE : ‘None’: Only for Clearance
        >
        > ADD\_CLEARANCE : ‘AddClearance’: Use the distance from the pad.
        >
        > ADD\_CLEARANCE\_EXACT : ‘AddClearanceExact’: Use the distance from the pad and keep the same distance around corners.
        >
        > CUSTOM : ‘Custom’: Use the shape specified.
        >
        > SAME\_AS\_CLEARANCE : ‘SameAsClearance’: Only for Antipad - Use the Clearance rule

        *property* Mode.str
        :   Return the string representation of the Antipad Mode.

        Mode.\_\_new\_\_(*\*\*kwargs*)

        Mode.\_\_init\_\_(*self: keysight.ads.de.\_pde.tech.Antipad.Mode*, *value: int*) → None

    \_\_init\_\_() → None[](#keysight.ads.de.tech.pads.Antipad.__init__ "Link to this definition")

    *property* mode*: Mode*[](#keysight.ads.de.tech.pads.Antipad.mode "Link to this definition")

    *property* use\_clearance\_rule\_with\_custom\_antipad*: bool*[](#keysight.ads.de.tech.pads.Antipad.use_clearance_rule_with_custom_antipad "Link to this definition")
    :   Use a clearance rule with a custom antipad shape.

    *property* expansion*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.Antipad.expansion "Link to this definition")
    :   The expansion when the mode is CLEARANCE or CLEARANCE\_EXACT.

    *property* custom\_antipad*: [Pad](#keysight.ads.de.tech.pads.Pad "keysight.ads.de.tech.pads.Pad") | None*[](#keysight.ads.de.tech.pads.Antipad.custom_antipad "Link to this definition")
    :   The shape of the antipad when the mode is CUSTOM.

*class* keysight.ads.de.tech.pads.MaskExpansion[](#keysight.ads.de.tech.pads.MaskExpansion "Link to this definition")
:   Defines the expansion on the solder mask and solder paste layers.

    *class* AffectsLayers
    :   Tells which layers are affected by a MaskExpansion.

        Members:

        > NONE : ‘None’: Does not affect a layer.
        >
        > TOP\_OF\_BOARD : ‘TopOfBoard’: Affects the layer on the top of the board.
        >
        > BOTTOM\_OF\_BOARD : ‘BottomOfBoard’: Affects the layer on the bottom of the board.
        >
        > TOP\_AND\_BOTTOM\_BOARD : ‘TopAndBottomBoard’: Affects the layers on the top and bottom of the board.

        *property* AffectsLayers.str
        :   Return the string representation of the AffectsLayers Mode.

        AffectsLayers.\_\_new\_\_(*\*\*kwargs*)

        AffectsLayers.\_\_init\_\_(*self: keysight.ads.de.\_pde.tech.MaskExpansion.AffectsLayers*, *value: int*) → None

    *class* Mode
    :   Describes the direction of expansion.

        Members:

        > SIZE : Expansion is linear.
        >
        > CUSTOM : Expansion is descibed by the Pad.

        Mode.\_\_init\_\_(*self: keysight.ads.de.\_pde.tech.MaskExpansion.Mode*, *value: int*) → None

        *property* Mode.name

    \_\_init\_\_(*affects\_layers: str | AffectsLayers*, *expansion: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue") | [Pad](#keysight.ads.de.tech.pads.Pad "keysight.ads.de.tech.pads.Pad") | None = None*) → None[](#keysight.ads.de.tech.pads.MaskExpansion.__init__ "Link to this definition")

    *property* affects\_layers*: AffectsLayers*[](#keysight.ads.de.tech.pads.MaskExpansion.affects_layers "Link to this definition")

    *property* mode*: Mode*[](#keysight.ads.de.tech.pads.MaskExpansion.mode "Link to this definition")

    *property* is\_default*: bool*[](#keysight.ads.de.tech.pads.MaskExpansion.is_default "Link to this definition")

    *property* expansion*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.MaskExpansion.expansion "Link to this definition")
    :   The expansion when the mode is SIZE.

    *property* expansion\_pad*: [Pad](#keysight.ads.de.tech.pads.Pad "keysight.ads.de.tech.pads.Pad") | None*[](#keysight.ads.de.tech.pads.MaskExpansion.expansion_pad "Link to this definition")
    :   The expansion when the mode is CUSTOM.

*class* keysight.ads.de.tech.pads.Pad[](#keysight.ads.de.tech.pads.Pad "Link to this definition")
:   Base class for pads used in Padstacks.

    Defines the size and shape of pads used in Padstacks.
    This information will be used by the generators
    that create Pad and Via objects in layout.

    *class* Shape
    :   Defines the shape of a Pad.

        Members:

        > NONE
        >
        > CIRCLE
        >
        > SQUARE
        >
        > RECTANGLE
        >
        > OBLONG
        >
        > ROUNDED\_RECT
        >
        > CHAMFERED\_RECT
        >
        > OCTAGON
        >
        > DONUT
        >
        > N\_GON

        *property* Shape.str
        :   Return the string representation of the Shape.

        Shape.\_\_new\_\_(*\*\*kwargs*)

        Shape.\_\_init\_\_(*self: keysight.ads.de.\_pde.tech.Pad.Shape*, *value: int*) → None

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.tech.pads.Pad.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* shape*: Shape*[](#keysight.ads.de.tech.pads.Pad.shape "Link to this definition")

    *property* x\_offset*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.Pad.x_offset "Link to this definition")
    :   The horizontal offset from the via placement of the pad center.

    *property* y\_offset*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.Pad.y_offset "Link to this definition")
    :   The vertical offset from the via placement of the pad center.

    *property* rotate\_degrees*: str*[](#keysight.ads.de.tech.pads.Pad.rotate_degrees "Link to this definition")
    :   The counterclockwise rotation of the pad.

        Note: This is also the angle for the spokes of a thermal on a circular pad.

*class* keysight.ads.de.tech.pads.PadLayerEntry[](#keysight.ads.de.tech.pads.PadLayerEntry "Link to this definition")
:   \_\_init\_\_() → None[](#keysight.ads.de.tech.pads.PadLayerEntry.__init__ "Link to this definition")

    *property* layer\_matcher*: [LayerMatcher](#keysight.ads.de.tech.pads.LayerMatcher "keysight.ads.de.tech.pads.LayerMatcher") | None*[](#keysight.ads.de.tech.pads.PadLayerEntry.layer_matcher "Link to this definition")

    *property* pad*: [Pad](#keysight.ads.de.tech.pads.Pad "keysight.ads.de.tech.pads.Pad") | None*[](#keysight.ads.de.tech.pads.PadLayerEntry.pad "Link to this definition")

    *property* thermal*: [Thermal](#keysight.ads.de.tech.pads.Thermal "keysight.ads.de.tech.pads.Thermal") | None*[](#keysight.ads.de.tech.pads.PadLayerEntry.thermal "Link to this definition")
    :   Defines how the pad connects to a plane on the same net.

    *property* clearance*: [Antipad](#keysight.ads.de.tech.pads.Antipad "keysight.ads.de.tech.pads.Antipad") | None*[](#keysight.ads.de.tech.pads.PadLayerEntry.clearance "Link to this definition")
    :   Defines an area around the pad which is used by avoidance routing to keep clear of different traces on a different net from the pad.

        If the clearance is None, the trace routing spacing rules are used.

    *property* antipad*: [Antipad](#keysight.ads.de.tech.pads.Antipad "keysight.ads.de.tech.pads.Antipad") | None*[](#keysight.ads.de.tech.pads.PadLayerEntry.antipad "Link to this definition")
    :   Defines a keepout area around the pad where a plane on a different net will not intrude.

*class* keysight.ads.de.tech.pads.Padstack[](#keysight.ads.de.tech.pads.Padstack "Link to this definition")
:   \_\_init\_\_(*name: str*) → None[](#keysight.ads.de.tech.pads.Padstack.__init__ "Link to this definition")

    *property* library*: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library") | None*[](#keysight.ads.de.tech.pads.Padstack.library "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.tech.pads.Padstack.name "Link to this definition")

    *property* default\_pad\_layer*: [PadLayerEntry](#keysight.ads.de.tech.pads.PadLayerEntry "keysight.ads.de.tech.pads.PadLayerEntry")*[](#keysight.ads.de.tech.pads.Padstack.default_pad_layer "Link to this definition")
    :   Return a reference to the default PadLayerEntry.

    *property* pad\_layers*: ListRefAbc[[PadLayerEntry](#keysight.ads.de.tech.pads.PadLayerEntry "keysight.ads.de.tech.pads.PadLayerEntry")]*[](#keysight.ads.de.tech.pads.Padstack.pad_layers "Link to this definition")
    :   Return the collection of PadLayerEntry other than the default pad layer entry.

    *property* drill*: [ViaPadDrill](#keysight.ads.de.tech.pads.ViaPadDrill "keysight.ads.de.tech.pads.ViaPadDrill")*[](#keysight.ads.de.tech.pads.Padstack.drill "Link to this definition")
    :   Return a reference to the ViaPadDrill.

    *property* mask\_expansion*: [MaskExpansion](#keysight.ads.de.tech.pads.MaskExpansion "keysight.ads.de.tech.pads.MaskExpansion")*[](#keysight.ads.de.tech.pads.Padstack.mask_expansion "Link to this definition")
    :   Return a reference to the solder mask expansion.

    *property* paste\_expansion*: [MaskExpansion](#keysight.ads.de.tech.pads.MaskExpansion "keysight.ads.de.tech.pads.MaskExpansion")*[](#keysight.ads.de.tech.pads.Padstack.paste_expansion "Link to this definition")
    :   Return a reference to the solder paste expansion.

*class* keysight.ads.de.tech.pads.Thermal[](#keysight.ads.de.tech.pads.Thermal "Link to this definition")
:   *class* Mode
    :   Defines the mode of a Thermal Relief.

        Members:

        > USE\_DEFAULT : ‘UseDefault’: Use the thermal mode defined in the default PadLayerEntry.
        >
        > FULL\_CONNECT : ‘FullConnect’: The pad is fully connected to the plane. There is no thermal relief.
        >
        > STRAIGHT : ‘Straight’: The thermal has 4 spokes. The clearance is drawn with straight lines.
        >
        > EXACT : ‘Exact’: The thermal has 4 spokes. The clearance is drawn with with rounded corners to keep exact distance.
        >
        > STRAIGHT\_2 : ‘Straight2’: The thermal has 2 spokes. The clearance is drawn with straight lines.
        >
        > EXACT\_2 : ‘Exact2’: The thermal has 2 spokes. The clearance is drawn with with rounded corners to keep exact distance.

        *property* Mode.str
        :   Return the string representation of the Thermal Mode.

        Mode.\_\_new\_\_(*\*\*kwargs*)

        Mode.\_\_init\_\_(*self: keysight.ads.de.\_pde.tech.Thermal.Mode*, *value: int*) → None

    \_\_init\_\_(*mode: str | Mode*) → None[](#keysight.ads.de.tech.pads.Thermal.__init__ "Link to this definition")

    *property* mode*: Mode*[](#keysight.ads.de.tech.pads.Thermal.mode "Link to this definition")

    *property* clearance*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.Thermal.clearance "Link to this definition")
    :   Distance from the pad to the surrounding plane, ignored for FULL\_CONNECT mode.

    *property* connection\_width*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.Thermal.connection_width "Link to this definition")
    :   Thickness of the thermal connection, ignored for FULL\_CONNECT mode.

*class* keysight.ads.de.tech.pads.ViaPadDrill[](#keysight.ads.de.tech.pads.ViaPadDrill "Link to this definition")
:   \_\_init\_\_(*drill\_type: str | DrillType*) → None[](#keysight.ads.de.tech.pads.ViaPadDrill.__init__ "Link to this definition")

    *property* drill\_type*: DrillType*[](#keysight.ads.de.tech.pads.ViaPadDrill.drill_type "Link to this definition")
    :   Circle or Square drill.

    *property* drill\_size*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.ViaPadDrill.drill_size "Link to this definition")
    :   For a circular drill, the diameter. For a square drill, the side length.

    *property* x\_offset*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.ViaPadDrill.x_offset "Link to this definition")
    :   The horizontal offset from the via placement to the center of the barrel.

    *property* y\_offset*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.ViaPadDrill.y_offset "Link to this definition")
    :   The vertical offset from the via placement to the center of the barrel.

    *property* slot\_length*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.ViaPadDrill.slot_length "Link to this definition")
    :   The distance the drill is moved in cutting a slot.

    *property* rotate\_degrees*: str*[](#keysight.ads.de.tech.pads.ViaPadDrill.rotate_degrees "Link to this definition")
    :   The counterclockwise rotation of the barrel.

*class* keysight.ads.de.tech.pads.ChamferedRectPad[](#keysight.ads.de.tech.pads.ChamferedRectPad "Link to this definition")
:   Holds shape and size information for a rectagular pad with chamfered corners.

    \_\_init\_\_(*width: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*, *height: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*, *chamfer: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*) → None[](#keysight.ads.de.tech.pads.ChamferedRectPad.__init__ "Link to this definition")

    *property* width*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.ChamferedRectPad.width "Link to this definition")

    *property* height*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.ChamferedRectPad.height "Link to this definition")

    *property* chamfer*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.ChamferedRectPad.chamfer "Link to this definition")
    :   The length (vertical or horizontal) of the chamfer cut in the corner.

    *property* ll\_chamfered*: bool*[](#keysight.ads.de.tech.pads.ChamferedRectPad.ll_chamfered "Link to this definition")
    :   Whether lower left corner is chamfered.

    *property* lr\_chamfered*: bool*[](#keysight.ads.de.tech.pads.ChamferedRectPad.lr_chamfered "Link to this definition")
    :   Whether lower right corner is chamfered.

    *property* ur\_chamfered*: bool*[](#keysight.ads.de.tech.pads.ChamferedRectPad.ur_chamfered "Link to this definition")
    :   Whether upper right corner is chamfered.

    *property* ul\_chamfered*: bool*[](#keysight.ads.de.tech.pads.ChamferedRectPad.ul_chamfered "Link to this definition")
    :   Whether upper left corner is chamfered.

*class* keysight.ads.de.tech.pads.CircularPad[](#keysight.ads.de.tech.pads.CircularPad "Link to this definition")
:   Holds shape and size information for a circular pad.

    \_\_init\_\_(*diameter: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*) → None[](#keysight.ads.de.tech.pads.CircularPad.__init__ "Link to this definition")

    *property* diameter*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.CircularPad.diameter "Link to this definition")

*class* keysight.ads.de.tech.pads.DonutPad[](#keysight.ads.de.tech.pads.DonutPad "Link to this definition")
:   Holds shape and size information for a donut shaped pad.

    \_\_init\_\_(*outer\_diameter: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*, *inner\_diameter: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*) → None[](#keysight.ads.de.tech.pads.DonutPad.__init__ "Link to this definition")

    *property* outer\_diameter*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.DonutPad.outer_diameter "Link to this definition")

    *property* inner\_diameter*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.DonutPad.inner_diameter "Link to this definition")

*class* keysight.ads.de.tech.pads.NGonPad[](#keysight.ads.de.tech.pads.NGonPad "Link to this definition")
:   Holds shape and size information for an n-sided polygonal pad.

    \_\_init\_\_(*width: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*, *num\_sides: str*) → None[](#keysight.ads.de.tech.pads.NGonPad.__init__ "Link to this definition")

    *property* width*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.NGonPad.width "Link to this definition")

    *property* num\_sides*: str*[](#keysight.ads.de.tech.pads.NGonPad.num_sides "Link to this definition")

*class* keysight.ads.de.tech.pads.NoPad[](#keysight.ads.de.tech.pads.NoPad "Link to this definition")
:   Used for cases where there is no pad.

    This is essentially an explicit alternative to None.

    \_\_init\_\_() → None[](#keysight.ads.de.tech.pads.NoPad.__init__ "Link to this definition")

*class* keysight.ads.de.tech.pads.OblongPad[](#keysight.ads.de.tech.pads.OblongPad "Link to this definition")
:   Holds shape and size information for an oblong pad (rectangle with very rounded corners).

    \_\_init\_\_(*width: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*, *height: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*) → None[](#keysight.ads.de.tech.pads.OblongPad.__init__ "Link to this definition")

    *property* width*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.OblongPad.width "Link to this definition")

    *property* height*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.OblongPad.height "Link to this definition")

*class* keysight.ads.de.tech.pads.OctagonalPad[](#keysight.ads.de.tech.pads.OctagonalPad "Link to this definition")
:   Holds shape and size information for an octagonal pad.

    \_\_init\_\_(*width: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*) → None[](#keysight.ads.de.tech.pads.OctagonalPad.__init__ "Link to this definition")

    *property* width*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.OctagonalPad.width "Link to this definition")

*class* keysight.ads.de.tech.pads.RectangularPad[](#keysight.ads.de.tech.pads.RectangularPad "Link to this definition")
:   Holds shape and size information for a rectangular pad.

    \_\_init\_\_(*width: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*, *height: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*) → None[](#keysight.ads.de.tech.pads.RectangularPad.__init__ "Link to this definition")

    *property* width*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.RectangularPad.width "Link to this definition")

    *property* height*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.RectangularPad.height "Link to this definition")

*class* keysight.ads.de.tech.pads.RoundedRectPad[](#keysight.ads.de.tech.pads.RoundedRectPad "Link to this definition")
:   Holds shape and size information for a rectagular pad that can have rounded corners.

    \_\_init\_\_(*width: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*, *height: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*, *radius: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*) → None[](#keysight.ads.de.tech.pads.RoundedRectPad.__init__ "Link to this definition")

    *property* width*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.RoundedRectPad.width "Link to this definition")

    *property* height*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.RoundedRectPad.height "Link to this definition")

    *property* radius*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.RoundedRectPad.radius "Link to this definition")
    :   The radius of the rounded corners.

    *property* ll\_rounded*: bool*[](#keysight.ads.de.tech.pads.RoundedRectPad.ll_rounded "Link to this definition")
    :   Whether lower left corner is rounded.

    *property* lr\_rounded*: bool*[](#keysight.ads.de.tech.pads.RoundedRectPad.lr_rounded "Link to this definition")
    :   Whether lower right corner is rounded.

    *property* ur\_rounded*: bool*[](#keysight.ads.de.tech.pads.RoundedRectPad.ur_rounded "Link to this definition")
    :   Whether upper right corner is rounded.

    *property* ul\_rounded*: bool*[](#keysight.ads.de.tech.pads.RoundedRectPad.ul_rounded "Link to this definition")
    :   Whether upper left corner is rounded.

*class* keysight.ads.de.tech.pads.SquarePad[](#keysight.ads.de.tech.pads.SquarePad "Link to this definition")
:   Holds shape and size information for a square pad.

    \_\_init\_\_(*width: str | [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*) → None[](#keysight.ads.de.tech.pads.SquarePad.__init__ "Link to this definition")

    *property* width*: [LengthValue](#keysight.ads.de.tech.pads.LengthValue "keysight.ads.de._pde.tech.LengthValue")*[](#keysight.ads.de.tech.pads.SquarePad.width "Link to this definition")

On this page

[Previous

Tech](../tech.md)
[Next

Via Rules](../rule/rule.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top