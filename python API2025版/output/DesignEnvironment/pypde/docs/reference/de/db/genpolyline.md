<!-- 来源: pypde\docs\reference\de\db\genpolyline.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.db](index.md)
* GenPolyline

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
    - [keysight.ads.de.db](index.md)
      * [Callbacks](callbacks.md)
      * [Enumerated Types](enums.md)
      * [Parameter Forms](forms.md)
      * GenPolyline
      * [Model Definition](model_def.md)
      * [Parameters](parameters.md)
      * [Properties](properties.md)
      * [Transaction](transaction.md)
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

# GenPolyline[](#genpolyline "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.CurveInfo[](#keysight.ads.de.db.CurveInfo "Link to this definition")
:   *property* start\_pt*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db.CurveInfo.start_pt "Link to this definition")

    *property* end\_pt*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db.CurveInfo.end_pt "Link to this definition")

    *property* center\_pt*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db.CurveInfo.center_pt "Link to this definition")

    *property* bulge*: float*[](#keysight.ads.de.db.CurveInfo.bulge "Link to this definition")

    *property* angle\_radians*: float*[](#keysight.ads.de.db.CurveInfo.angle_radians "Link to this definition")

    *property* start\_angle\_radians*: float*[](#keysight.ads.de.db.CurveInfo.start_angle_radians "Link to this definition")

    *property* angle\_degrees*: float*[](#keysight.ads.de.db.CurveInfo.angle_degrees "Link to this definition")

    *property* start\_angle\_degrees*: float*[](#keysight.ads.de.db.CurveInfo.start_angle_degrees "Link to this definition")

    *property* radius*: float*[](#keysight.ads.de.db.CurveInfo.radius "Link to this definition")

    *property* arc\_orientation*: [ArcOrientation](#keysight.ads.de.db.ArcOrientation "keysight.ads.de._pde.ArcOrientation")*[](#keysight.ads.de.db.CurveInfo.arc_orientation "Link to this definition")

    *property* is\_clockwise*: bool*[](#keysight.ads.de.db.CurveInfo.is_clockwise "Link to this definition")

    *property* is\_counter\_clockwise*: bool*[](#keysight.ads.de.db.CurveInfo.is_counter_clockwise "Link to this definition")

    *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db.CurveInfo.bbox "Link to this definition")

*class* keysight.ads.de.db.Edge[](#keysight.ads.de.db.Edge "Link to this definition")
:   A temporary object that represents the edge of an Outline.

    This edge should only be used as a temporary object. Any modifications
    to the Outline will invalidate the Edge object.

    *property* start\_pt*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db.Edge.start_pt "Link to this definition")

    *property* end\_pt*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db.Edge.end_pt "Link to this definition")

    *property* is\_arc*: bool*[](#keysight.ads.de.db.Edge.is_arc "Link to this definition")

    *property* curve\_info*: [CurveInfo](#keysight.ads.de.db.CurveInfo "keysight.ads.de.db._genpolyline.CurveInfo") | None*[](#keysight.ads.de.db.Edge.curve_info "Link to this definition")

*class* keysight.ads.de.db.GenPolygon[](#keysight.ads.de.db.GenPolygon "Link to this definition")
:   TPoint[](#keysight.ads.de.db.GenPolygon.TPoint "Link to this definition")
    :   alias of `Union`[[`PointF`](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF"), `tuple`[`float`, `float`], [`PointDBU`](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU"), `tuple`[`int`, `int`]]

    \_\_init\_\_(*points: Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float] | [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU") | tuple[int, int]] | None = None*, *outline: [Outline](#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline") | None = None*) → None[](#keysight.ads.de.db.GenPolygon.__init__ "Link to this definition")

    *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db.GenPolygon.bbox "Link to this definition")

    *property* empty*: bool*[](#keysight.ads.de.db.GenPolygon.empty "Link to this definition")

    *property* has\_arcs*: bool*[](#keysight.ads.de.db.GenPolygon.has_arcs "Link to this definition")

    *property* points*: list[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")]*[](#keysight.ads.de.db.GenPolygon.points "Link to this definition")

    *property* outline*: [Outline](#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline")*[](#keysight.ads.de.db.GenPolygon.outline "Link to this definition")

    box\_intersects\_or\_contains\_edge(*box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → bool[](#keysight.ads.de.db.GenPolygon.box_intersects_or_contains_edge "Link to this definition")

    overlaps(*box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → bool[](#keysight.ads.de.db.GenPolygon.overlaps "Link to this definition")

    contains(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → bool[](#keysight.ads.de.db.GenPolygon.contains "Link to this definition")

    add\_point(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → None[](#keysight.ads.de.db.GenPolygon.add_point "Link to this definition")

    set\_segment\_as\_arc(*index: int*, *point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*, *arc\_orientation: [ArcOrientation](#keysight.ads.de.db.ArcOrientation "keysight.ads.de._pde.ArcOrientation") | str*) → None[](#keysight.ads.de.db.GenPolygon.set_segment_as_arc "Link to this definition")

    set\_segment\_as\_arc\_bulge(*index: int*, *bulge: float*) → None[](#keysight.ads.de.db.GenPolygon.set_segment_as_arc_bulge "Link to this definition")

    remove\_arcs(*arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.GenPolygon.remove_arcs "Link to this definition")

    transform(*transformation: [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")*, *arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.GenPolygon.transform "Link to this definition")

*class* keysight.ads.de.db.GenPolygonWithHoles[](#keysight.ads.de.db.GenPolygonWithHoles "Link to this definition")
:   TPoint[](#keysight.ads.de.db.GenPolygonWithHoles.TPoint "Link to this definition")
    :   alias of `Union`[[`PointF`](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF"), `tuple`[`float`, `float`], [`PointDBU`](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU"), `tuple`[`int`, `int`]]

    \_\_init\_\_(*points: Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float] | [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU") | tuple[int, int]] | None = None*, *outer\_boundary: [GenPolygon](#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon") | None = None*, *inner\_boundaries: Sequence[[GenPolygon](#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon")] | None = None*) → None[](#keysight.ads.de.db.GenPolygonWithHoles.__init__ "Link to this definition")

    *property* outer\_boundary*: [GenPolygon](#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon")*[](#keysight.ads.de.db.GenPolygonWithHoles.outer_boundary "Link to this definition")

    *property* inner\_boundaries*: list[[GenPolygon](#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon")]*[](#keysight.ads.de.db.GenPolygonWithHoles.inner_boundaries "Link to this definition")
    :   A copy of the collection of holes in this polygon.

        inner\_boundaries is deprecated, and will be removed in the 2026 release. Use: GenPolygonWithHoles.holes.

    *property* holes*: ReadableListRefAbc[[GenPolygon](#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon")]*[](#keysight.ads.de.db.GenPolygonWithHoles.holes "Link to this definition")
    :   The collection of holes in this polygon.

    *property* num\_holes*: int*[](#keysight.ads.de.db.GenPolygonWithHoles.num_holes "Link to this definition")

    *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db.GenPolygonWithHoles.bbox "Link to this definition")

    *property* empty*: bool*[](#keysight.ads.de.db.GenPolygonWithHoles.empty "Link to this definition")

    *property* has\_arcs*: bool*[](#keysight.ads.de.db.GenPolygonWithHoles.has_arcs "Link to this definition")

    contains(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → bool[](#keysight.ads.de.db.GenPolygonWithHoles.contains "Link to this definition")

    box\_intersects\_or\_contains\_edge(*box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → bool[](#keysight.ads.de.db.GenPolygonWithHoles.box_intersects_or_contains_edge "Link to this definition")

    overlaps\_box(*box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → bool[](#keysight.ads.de.db.GenPolygonWithHoles.overlaps_box "Link to this definition")

    overlaps\_polygon(*is\_closed: bool*, *other: [GenPolygonWithHoles](#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")*, *other\_is\_closed: bool*) → bool[](#keysight.ads.de.db.GenPolygonWithHoles.overlaps_polygon "Link to this definition")

    self\_intersects(*arc\_resolution\_degrees: float*) → bool[](#keysight.ads.de.db.GenPolygonWithHoles.self_intersects "Link to this definition")

    remove\_arcs(*arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.GenPolygonWithHoles.remove_arcs "Link to this definition")

    transform(*transformation: [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")*, *arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.GenPolygonWithHoles.transform "Link to this definition")

    convert\_vertices\_to\_arcs(*radius: float*, *arc\_resolution\_degrees: float = 5.0*, *minimum\_vertex\_distance: float = 0.0*) → list[[GenPolygonWithHoles](#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")][](#keysight.ads.de.db.GenPolygonWithHoles.convert_vertices_to_arcs "Link to this definition")

    oversize(*oversize\_amount: float*, *miter\_angle\_degrees: float = 0.0*, *minimum\_vertex\_distance: float = 0.0*) → list[[GenPolygonWithHoles](#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")][](#keysight.ads.de.db.GenPolygonWithHoles.oversize "Link to this definition")

*class* keysight.ads.de.db.GenPolyline[](#keysight.ads.de.db.GenPolyline "Link to this definition")
:   TPoint[](#keysight.ads.de.db.GenPolyline.TPoint "Link to this definition")
    :   alias of `Union`[[`PointF`](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF"), `tuple`[`float`, `float`], [`PointDBU`](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU"), `tuple`[`int`, `int`]]

    \_\_init\_\_(*points: ~collections.abc.Sequence[~keysight.ads.de.\_points.PointF | tuple[float*, *float] | ~keysight.ads.de.\_points.PointDBU | tuple[int*, *int]] | None = None*, *width: float = 0.0*, *bend\_style: ~keysight.ads.de.\_pde.BendStyle | str = <BendStyle.SQUARE: 0>*, *cap\_style: ~keysight.ads.de.\_pde.CapStyle | str = <CapStyle.ROUND: 1>*, *miter\_radius: float = 0.0*) → None[](#keysight.ads.de.db.GenPolyline.__init__ "Link to this definition")

    copy() → [GenPolyline](#keysight.ads.de.db.GenPolyline "keysight.ads.de.db._genpolyline.GenPolyline")[](#keysight.ads.de.db.GenPolyline.copy "Link to this definition")
    :   Return a copy of this object.

    *property* points*: list[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")]*[](#keysight.ads.de.db.GenPolyline.points "Link to this definition")

    *property* outline*: [Outline](#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline")*[](#keysight.ads.de.db.GenPolyline.outline "Link to this definition")

    *property* width*: float*[](#keysight.ads.de.db.GenPolyline.width "Link to this definition")

    *property* bend\_style*: [BendStyle](#keysight.ads.de.db.BendStyle "keysight.ads.de._pde.BendStyle")*[](#keysight.ads.de.db.GenPolyline.bend_style "Link to this definition")

    *property* cap\_style*: [CapStyle](#keysight.ads.de.db.CapStyle "keysight.ads.de._pde.CapStyle")*[](#keysight.ads.de.db.GenPolyline.cap_style "Link to this definition")

    *property* miter\_radius*: float*[](#keysight.ads.de.db.GenPolyline.miter_radius "Link to this definition")

    *property* teardrop\_info*: [TeardropLineInfo](#keysight.ads.de.db.TeardropLineInfo "keysight.ads.de.db._teardrop.TeardropLineInfo")*[](#keysight.ads.de.db.GenPolyline.teardrop_info "Link to this definition")

    *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db.GenPolyline.bbox "Link to this definition")

    *property* empty*: bool*[](#keysight.ads.de.db.GenPolyline.empty "Link to this definition")

    *property* has\_arcs*: bool*[](#keysight.ads.de.db.GenPolyline.has_arcs "Link to this definition")

    add\_point(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → None[](#keysight.ads.de.db.GenPolyline.add_point "Link to this definition")

    set\_segment\_as\_arc(*index: int*, *point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*, *arc\_orientation: [ArcOrientation](#keysight.ads.de.db.ArcOrientation "keysight.ads.de._pde.ArcOrientation") | str*) → None[](#keysight.ads.de.db.GenPolyline.set_segment_as_arc "Link to this definition")

    set\_segment\_as\_arc\_bulge(*index: int*, *bulge: float*) → None[](#keysight.ads.de.db.GenPolyline.set_segment_as_arc_bulge "Link to this definition")

    transform(*transformation: [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")*) → None[](#keysight.ads.de.db.GenPolyline.transform "Link to this definition")

*class* keysight.ads.de.db.MatrixForTransform[](#keysight.ads.de.db.MatrixForTransform "Link to this definition")
:   \_\_init\_\_() → None[](#keysight.ads.de.db.MatrixForTransform.__init__ "Link to this definition")

    translate(*dx: float*, *dy: float*) → None[](#keysight.ads.de.db.MatrixForTransform.translate "Link to this definition")

    rotate\_degrees(*degrees: float*) → None[](#keysight.ads.de.db.MatrixForTransform.rotate_degrees "Link to this definition")

    scale(*dx: float*, *dy: float*) → None[](#keysight.ads.de.db.MatrixForTransform.scale "Link to this definition")

    invert() → None[](#keysight.ads.de.db.MatrixForTransform.invert "Link to this definition")

    *property* dx*: float*[](#keysight.ads.de.db.MatrixForTransform.dx "Link to this definition")

    *property* dy*: float*[](#keysight.ads.de.db.MatrixForTransform.dy "Link to this definition")

    *property* m11*: float*[](#keysight.ads.de.db.MatrixForTransform.m11 "Link to this definition")

    *property* m12*: float*[](#keysight.ads.de.db.MatrixForTransform.m12 "Link to this definition")

    *property* m21*: float*[](#keysight.ads.de.db.MatrixForTransform.m21 "Link to this definition")

    *property* m22*: float*[](#keysight.ads.de.db.MatrixForTransform.m22 "Link to this definition")

*class* keysight.ads.de.db.Outline[](#keysight.ads.de.db.Outline "Link to this definition")
:   Represents a polyline composed of line and/or arc segments.

    It may represent either an open or closed shape.
    GenPolyline uses an Outline to represent an open shape.
    GenPolygonF and GenPolygonF\_with\_holes use an Outline to represent a closed shape.
    The points (vertices) and bulges control the shape of the outline.
    The edges are temporary objects that get invalidated whenever the Outline is modified.

    TPoint[](#keysight.ads.de.db.Outline.TPoint "Link to this definition")
    :   alias of `Union`[[`PointF`](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF"), `tuple`[`float`, `float`], [`PointDBU`](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU"), `tuple`[`int`, `int`]]

    \_\_init\_\_(*points: Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float] | [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU") | tuple[int, int]] | None = None*, *bulges: Sequence[float] | None = None*) → None[](#keysight.ads.de.db.Outline.__init__ "Link to this definition")

    *property* points*: [IndexedMutableCollectionAbc](../collections.md#keysight.ads.de._list_like.IndexedMutableCollectionAbc "keysight.ads.de._list_like.IndexedMutableCollectionAbc")[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")]*[](#keysight.ads.de.db.Outline.points "Link to this definition")
    :   The collection of vertices for this outline.

    *property* edges*: IndexedReadableCollectionAbc[[Edge](#keysight.ads.de.db.Edge "keysight.ads.de.db._genpolyline.Edge")]*[](#keysight.ads.de.db.Outline.edges "Link to this definition")
    :   The collection of edges for this outline. The edges are only for short term use.

    *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db.Outline.bbox "Link to this definition")

    *property* empty*: bool*[](#keysight.ads.de.db.Outline.empty "Link to this definition")
    :   True if the outline has no points.

    *property* has\_arcs*: bool*[](#keysight.ads.de.db.Outline.has_arcs "Link to this definition")
    :   True if none of the edges are arcs.

    box\_intersects\_or\_contains\_edge(*box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*, *is\_closed: bool*) → bool[](#keysight.ads.de.db.Outline.box_intersects_or_contains_edge "Link to this definition")

    edges\_intersect(*is\_closed: bool*, *other: [Outline](#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline")*, *other\_is\_closed: bool*) → bool[](#keysight.ads.de.db.Outline.edges_intersect "Link to this definition")

    contains(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → bool[](#keysight.ads.de.db.Outline.contains "Link to this definition")

    contains\_and\_not\_on\_edge(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → bool[](#keysight.ads.de.db.Outline.contains_and_not_on_edge "Link to this definition")

    add\_point(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → None[](#keysight.ads.de.db.Outline.add_point "Link to this definition")

    insert\_point(*index: int*, *point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → None[](#keysight.ads.de.db.Outline.insert_point "Link to this definition")

    delete\_point(*index: int*) → None[](#keysight.ads.de.db.Outline.delete_point "Link to this definition")

    set\_point(*index: int*, *point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → None[](#keysight.ads.de.db.Outline.set_point "Link to this definition")

    set\_segment\_as\_arc(*index: int*, *point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*, *arc\_orientation: [ArcOrientation](#keysight.ads.de.db.ArcOrientation "keysight.ads.de._pde.ArcOrientation") | str*) → None[](#keysight.ads.de.db.Outline.set_segment_as_arc "Link to this definition")

    set\_segment\_as\_arc\_bulge(*index: int*, *bulge: float*) → None[](#keysight.ads.de.db.Outline.set_segment_as_arc_bulge "Link to this definition")

    remove\_arcs(*arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.Outline.remove_arcs "Link to this definition")

    transform(*transform: [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")*, *arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.Outline.transform "Link to this definition")

    curve\_info(*index: int*) → [CurveInfo](#keysight.ads.de.db.CurveInfo "keysight.ads.de.db._genpolyline.CurveInfo") | None[](#keysight.ads.de.db.Outline.curve_info "Link to this definition")

*class* keysight.ads.de.db.TeardropDefinition[](#keysight.ads.de.db.TeardropDefinition "Link to this definition")
:   \_\_init\_\_(*width: [TeardropDefinitionWidth](#keysight.ads.de.db.TeardropDefinitionWidth "keysight.ads.de.db._teardrop.TeardropDefinitionWidth") | None = None*, *\**, *height: [TeardropDefinitionHeight](#keysight.ads.de.db.TeardropDefinitionHeight "keysight.ads.de.db._teardrop.TeardropDefinitionHeight") | None = None*, *angle: [TeardropDefinitionAngle](#keysight.ads.de.db.TeardropDefinitionAngle "keysight.ads.de.db._teardrop.TeardropDefinitionAngle") | None = None*) → None[](#keysight.ads.de.db.TeardropDefinition.__init__ "Link to this definition")

    *property* style*: [TeardropDefinitionStyle](#keysight.ads.de.db.TeardropDefinitionStyle "keysight.ads.de._pde.TeardropDefinitionStyle")*[](#keysight.ads.de.db.TeardropDefinition.style "Link to this definition")

    *property* width*: [TeardropDefinitionWidth](#keysight.ads.de.db.TeardropDefinitionWidth "keysight.ads.de.db._teardrop.TeardropDefinitionWidth") | None*[](#keysight.ads.de.db.TeardropDefinition.width "Link to this definition")

    *property* height*: [TeardropDefinitionHeight](#keysight.ads.de.db.TeardropDefinitionHeight "keysight.ads.de.db._teardrop.TeardropDefinitionHeight") | None*[](#keysight.ads.de.db.TeardropDefinition.height "Link to this definition")

    *property* angle*: [TeardropDefinitionAngle](#keysight.ads.de.db.TeardropDefinitionAngle "keysight.ads.de.db._teardrop.TeardropDefinitionAngle") | None*[](#keysight.ads.de.db.TeardropDefinition.angle "Link to this definition")

*class* keysight.ads.de.db.TeardropDefinitionAngle[](#keysight.ads.de.db.TeardropDefinitionAngle "Link to this definition")
:   Bases: `object`

*class* keysight.ads.de.db.TeardropDefinitionHeight[](#keysight.ads.de.db.TeardropDefinitionHeight "Link to this definition")
:   Bases: `object`

*class* keysight.ads.de.db.TeardropDefinitionWidth[](#keysight.ads.de.db.TeardropDefinitionWidth "Link to this definition")
:   Bases: `object`

*class* keysight.ads.de.db.TeardropLineInfo[](#keysight.ads.de.db.TeardropLineInfo "Link to this definition")
:   Bases: `object`

*class* keysight.ads.de.db.TeardropTouching[](#keysight.ads.de.db.TeardropTouching "Link to this definition")
:   Bases: `object`

    *property* was\_set\_manually*: bool*[](#keysight.ads.de.db.TeardropTouching.was_set_manually "Link to this definition")
    :   For testing.

    copy() → [TeardropTouching](#keysight.ads.de.db.TeardropTouching "keysight.ads.de.db._teardrop.TeardropTouching")[](#keysight.ads.de.db.TeardropTouching.copy "Link to this definition")
    :   Return a copy of this object.

*class* keysight.ads.de.db.Transform[](#keysight.ads.de.db.Transform "Link to this definition")
:   \_\_init\_\_() → None[](#keysight.ads.de.db.Transform.__init__ "Link to this definition")

    *property* matrix*: [MatrixForTransform](#keysight.ads.de.db.MatrixForTransform "keysight.ads.de.db._genpolyline.MatrixForTransform")*[](#keysight.ads.de.db.Transform.matrix "Link to this definition")

    *property* preserves\_aspect\_ratio*: bool*[](#keysight.ads.de.db.Transform.preserves_aspect_ratio "Link to this definition")

    *property* preserves\_mirroring*: bool*[](#keysight.ads.de.db.Transform.preserves_mirroring "Link to this definition")

    *property* is\_orthogonal*: bool*[](#keysight.ads.de.db.Transform.is_orthogonal "Link to this definition")

    *property* mirrored\_in\_x*: bool*[](#keysight.ads.de.db.Transform.mirrored_in_x "Link to this definition")

    *property* mirrored\_in\_y*: bool*[](#keysight.ads.de.db.Transform.mirrored_in_y "Link to this definition")

    scale(*dx: float*, *dy: float*) → None[](#keysight.ads.de.db.Transform.scale "Link to this definition")

    mirror\_x(*mirror: bool = True*) → None[](#keysight.ads.de.db.Transform.mirror_x "Link to this definition")

    mirror\_y(*mirror: bool = True*) → None[](#keysight.ads.de.db.Transform.mirror_y "Link to this definition")

    clear() → None[](#keysight.ads.de.db.Transform.clear "Link to this definition")

    translate(*point: tuple[float, float] | [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | None = None*, *\**, *dx: float | None = None*, *dy: float | None = None*) → None[](#keysight.ads.de.db.Transform.translate "Link to this definition")

    rotate\_radians(*radians: float*) → None[](#keysight.ads.de.db.Transform.rotate_radians "Link to this definition")

    rotate\_degrees(*degrees: float*) → None[](#keysight.ads.de.db.Transform.rotate_degrees "Link to this definition")

    reverse() → None[](#keysight.ads.de.db.Transform.reverse "Link to this definition")

    multiply\_transform(*other: [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")*) → [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")[](#keysight.ads.de.db.Transform.multiply_transform "Link to this definition")

    transform\_user\_point(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")[](#keysight.ads.de.db.Transform.transform_user_point "Link to this definition")

    transform\_point(*point: tuple[float, float]*) → tuple[float, float][](#keysight.ads.de.db.Transform.transform_point "Link to this definition")

    transform\_distance(*distance: float*) → float[](#keysight.ads.de.db.Transform.transform_distance "Link to this definition")

    transform\_angle\_radians(*radians: float*) → float[](#keysight.ads.de.db.Transform.transform_angle_radians "Link to this definition")

    transform\_angle\_degrees(*degrees: float*) → float[](#keysight.ads.de.db.Transform.transform_angle_degrees "Link to this definition")

    get\_transform\_angle() → int[](#keysight.ads.de.db.Transform.get_transform_angle "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.db.ArcOrientation[](#keysight.ads.de.db.ArcOrientation "Link to this definition")
:   Defines the orientation of an arc or sequence of points.

    Members:

    > CLOCKWISE : ‘Clockwise’: The orientation is clockwise.
    >
    > ZERO : ‘Zero’: The orientation is unspecified or we don’t care.
    >
    > COUNTER\_CLOCKWISE : ‘CounterClockwise’: The orientation is counter-clockwise.

    CLOCKWISE *= <ArcOrientation.CLOCKWISE: -1>*[](#keysight.ads.de.db.ArcOrientation.CLOCKWISE "Link to this definition")

    COUNTER\_CLOCKWISE *= <ArcOrientation.COUNTER\_CLOCKWISE: 1>*[](#keysight.ads.de.db.ArcOrientation.COUNTER_CLOCKWISE "Link to this definition")

    ZERO *= <ArcOrientation.ZERO: 0>*[](#keysight.ads.de.db.ArcOrientation.ZERO "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.ArcOrientation](#keysight.ads.de.db.ArcOrientation "keysight.ads.de._pde.ArcOrientation")*, *value: int*) → None[](#keysight.ads.de.db.ArcOrientation.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.ArcOrientation.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.ArcOrientation.name "Link to this definition")

    *property* str[](#keysight.ads.de.db.ArcOrientation.str "Link to this definition")
    :   Return the string representation of the orientation.

    *property* value[](#keysight.ads.de.db.ArcOrientation.value "Link to this definition")

*class* keysight.ads.de.db.BendStyle[](#keysight.ads.de.db.BendStyle "Link to this definition")
:   Defines the style of a bend in a polyline or polygon.

    Members:

    > SQUARE : ‘Square’: The bend has square corners.
    >
    > CURVED : ‘Curved’: The bend has curved corners with a specified radius.
    >
    > MITERED : ‘Mitered’: The bend has mitered corners - prefer AdaptiveMitered.
    >
    > NEW\_MITERED : ‘AdaptiveMitered’: Deprecated alias for ADAPTIVE\_MITERED.
    >
    > ADAPTIVE\_MITERED : ‘AdaptiveMitered’: The bend has mitered corners with consistent cut length.
    >
    > ROUNDED : ‘Rounded’: The bend has rounded corners.
    >
    > EXACT\_MITERED : ‘ExactMitered’: The bend has miter specified exactly - for internal use only.

    ADAPTIVE\_MITERED *= <BendStyle.NEW\_MITERED: 3>*[](#keysight.ads.de.db.BendStyle.ADAPTIVE_MITERED "Link to this definition")

    CURVED *= <BendStyle.CURVED: 1>*[](#keysight.ads.de.db.BendStyle.CURVED "Link to this definition")

    EXACT\_MITERED *= <BendStyle.EXACT\_MITERED: 5>*[](#keysight.ads.de.db.BendStyle.EXACT_MITERED "Link to this definition")

    MITERED *= <BendStyle.MITERED: 2>*[](#keysight.ads.de.db.BendStyle.MITERED "Link to this definition")

    NEW\_MITERED *= <BendStyle.NEW\_MITERED: 3>*[](#keysight.ads.de.db.BendStyle.NEW_MITERED "Link to this definition")

    ROUNDED *= <BendStyle.ROUNDED: 4>*[](#keysight.ads.de.db.BendStyle.ROUNDED "Link to this definition")

    SQUARE *= <BendStyle.SQUARE: 0>*[](#keysight.ads.de.db.BendStyle.SQUARE "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.BendStyle](#keysight.ads.de.db.BendStyle "keysight.ads.de._pde.BendStyle")*, *value: int*) → None[](#keysight.ads.de.db.BendStyle.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.BendStyle.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.BendStyle.name "Link to this definition")

    *property* str[](#keysight.ads.de.db.BendStyle.str "Link to this definition")
    :   Return the string representation of the bend style.

    *property* value[](#keysight.ads.de.db.BendStyle.value "Link to this definition")

*class* keysight.ads.de.db.CapStyle[](#keysight.ads.de.db.CapStyle "Link to this definition")
:   Defines the style of polyline end caps.

    Members:

    > SQUARE : ‘Square’: The end cap is square.
    >
    > ROUND : ‘Round’: The end cap is round.
    >
    > SQUARE\_EXTENDED : ‘SquareExtended’: The end cap is square and extended by half the width.
    >
    > CHAMFER : ‘Chamfer’: The end cap is chamfered.

    CHAMFER *= <CapStyle.CHAMFER: 3>*[](#keysight.ads.de.db.CapStyle.CHAMFER "Link to this definition")

    ROUND *= <CapStyle.ROUND: 1>*[](#keysight.ads.de.db.CapStyle.ROUND "Link to this definition")

    SQUARE *= <CapStyle.SQUARE: 0>*[](#keysight.ads.de.db.CapStyle.SQUARE "Link to this definition")

    SQUARE\_EXTENDED *= <CapStyle.SQUARE\_EXTENDED: 2>*[](#keysight.ads.de.db.CapStyle.SQUARE_EXTENDED "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.CapStyle](#keysight.ads.de.db.CapStyle "keysight.ads.de._pde.CapStyle")*, *value: int*) → None[](#keysight.ads.de.db.CapStyle.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.CapStyle.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.CapStyle.name "Link to this definition")

    *property* str[](#keysight.ads.de.db.CapStyle.str "Link to this definition")
    :   Return the string representation of the end cap style.

    *property* value[](#keysight.ads.de.db.CapStyle.value "Link to this definition")

keysight.ads.de.db.LineInfoEnd[](#keysight.ads.de.db.LineInfoEnd "Link to this definition")
:   alias of `End`

*class* keysight.ads.de.db.TeardropDefinitionStyle[](#keysight.ads.de.db.TeardropDefinitionStyle "Link to this definition")
:   Bases: `pybind11_object`

    Members:

    NONE

    WIDTH\_AND\_HEIGHT

    WIDTH\_TANGENT

    TEARDROP\_ANGLE

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.TeardropDefinitionStyle](#keysight.ads.de.db.TeardropDefinitionStyle "keysight.ads.de._pde.TeardropDefinitionStyle")*, *value: int*) → None[](#keysight.ads.de.db.TeardropDefinitionStyle.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.TeardropDefinitionStyle.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.TeardropDefinitionStyle.name "Link to this definition")

*class* keysight.ads.de.db.TeardropValueUnits[](#keysight.ads.de.db.TeardropValueUnits "Link to this definition")
:   Bases: `pybind11_object`

    Determines how a teardrop value is specified (ratio or absolute value).

    Members:

    > VALUE : ‘Value’: The value is specified as an absolute value.
    >
    > DB\_UNITS : ‘Value’: Deprecated alias for VALUE.
    >
    > RATIO : ‘Ratio’: The value is specified as a ratio.

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.TeardropValueUnits](#keysight.ads.de.db.TeardropValueUnits "keysight.ads.de._pde.TeardropValueUnits")*, *value: int*) → None[](#keysight.ads.de.db.TeardropValueUnits.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.TeardropValueUnits.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.TeardropValueUnits.name "Link to this definition")

    *property* str[](#keysight.ads.de.db.TeardropValueUnits.str "Link to this definition")
    :   Return the string representation of the TeardropValueUnits.

*class* keysight.ads.de.db.TouchType[](#keysight.ads.de.db.TouchType "Link to this definition")
:   Members:

    NONE

    CIRCLE

    CIRCLE *= <TouchType.CIRCLE: 1>*[](#keysight.ads.de.db.TouchType.CIRCLE "Link to this definition")

    NONE *= <TouchType.NONE: 0>*[](#keysight.ads.de.db.TouchType.NONE "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.TouchType](#keysight.ads.de.db.TouchType "keysight.ads.de._pde.TouchType")*, *value: int*) → None[](#keysight.ads.de.db.TouchType.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.TouchType.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.TouchType.name "Link to this definition")

    *property* value[](#keysight.ads.de.db.TouchType.value "Link to this definition")

On this page

[Previous

Parameter Forms](forms.md)
[Next

Model Definition](model_def.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top