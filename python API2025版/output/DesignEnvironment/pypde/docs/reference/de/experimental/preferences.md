<!-- 来源: pypde\docs\reference\de\experimental\preferences.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.experimental](index.md)
* Preferences

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
    - [keysight.ads.de.experimental](index.md)
      * [CDF](cdf/index.md)
      * [Commands](commands.md)
      * [Handles](handles.md)
      * [Netlist Utilities](netlist_helper.md)
      * [Polygon Utilities](polygon_utils.md)
      * Preferences
      * [xxPro View](pro_view.md)
      * [Symbol Generator](symbol.md)
      * [Text Maker](text_maker.md)
    - [keysight.ads.de.tech](../tech/index.md)
      * [Tech](../tech/tech.md)
      * [Padstacks](../tech/pads/pads.md)
      * [Via Rules](../tech/rule/rule.md)
      * [Nested Technology](../tech/nested/nested.md)
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

On this page

[Previous

Polygon Utilities](polygon_utils.md)
[Next

xxPro View](pro_view.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top