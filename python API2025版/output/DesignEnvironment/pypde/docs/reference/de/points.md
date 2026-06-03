<!-- 来源: pypde\docs\reference\de\points.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Design](../../index.md)
* [Reference](../index.md)
* [keysight.ads.de](index.md)
* Points

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
      * [Library](library.md)
      * [Cell](cell.md)
      * [View](view.md)
      * [CellviewRef](cellviewref.md)
      * [DesignHierarchy](design_hierarchy.md)
      * [DMData](dmdata.md)
      * [ItemInfo](item_info.md)
      * Points
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

On this page

[Previous

ItemInfo](item_info.md)
[Next

Collections](collections.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top