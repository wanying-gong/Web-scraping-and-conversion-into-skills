<!-- 来源: pypde\docs\reference\de\db_uu\db_uu.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.db\_uu](index.md)
* Design Elements

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
    - [keysight.ads.de.db\_uu](index.md)
      * Design Elements
      * [LayerId](layer_id.md)
      * [LineTypeInfo](line_type_info.md)
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

# Design Elements[](#design-elements "Link to this heading")

## Classes[](#classes "Link to this heading")

> *class* keysight.ads.de.db\_uu.ApolloObject[](#keysight.ads.de.db_uu.ApolloObject "Link to this definition")
> :   Base class for objects that appear in Designs.
>
>     \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db_uu.ApolloObject.__init__ "Link to this definition")
>     :   Return an error about attempts to initialize objects that don’t support initialization.
>
>     delete\_object() → None[](#keysight.ads.de.db_uu.ApolloObject.delete_object "Link to this definition")
>
>     find\_prop(*name: str*) → [Property](../db/properties.md#keysight.ads.de.db.Property "keysight.ads.de.db.Property") | None[](#keysight.ads.de.db_uu.ApolloObject.find_prop "Link to this definition")
>
>     *property* groups*: NamedReadableCollectionAbc[[Group](#keysight.ads.de.db_uu.Group "keysight.ads.de.db_uu._db_x.Group")]*[](#keysight.ads.de.db_uu.ApolloObject.groups "Link to this definition")
>     :   The collection of groups that contain this object.
>
>     *property* library*: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.de.db_uu.ApolloObject.library "Link to this definition")
>
>     *property* parent*: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*[](#keysight.ads.de.db_uu.ApolloObject.parent "Link to this definition")
>
>     *property* props*: NamedReadableCollectionAbc[[Property](../db/properties.md#keysight.ads.de.db.Property "keysight.ads.de.db.Property")]*[](#keysight.ads.de.db_uu.ApolloObject.props "Link to this definition")
>
>     *property* type*: ApolloType*[](#keysight.ads.de.db_uu.ApolloObject.type "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.AppObject[](#keysight.ads.de.db_uu.AppObject "Link to this definition")
> :   Bases: [`ApolloObject`](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")
>
>     An application defined extension object.
>
>     \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db_uu.AppObject.__init__ "Link to this definition")
>     :   Return an error about attempts to initialize objects that don’t support initialization.
>
> *class* keysight.ads.de.db\_uu.AppObjectIter[](#keysight.ads.de.db_uu.AppObjectIter "Link to this definition")
> :   \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.AppObjectIter.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.Arc[](#keysight.ads.de.db_uu.Arc "Link to this definition")
> :   Bases: [`Shape`](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")
>
> *class* keysight.ads.de.db\_uu.ArrayInst[](#keysight.ads.de.db_uu.ArrayInst "Link to this definition")
> :   Bases: [`Instance`](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")
>
> *class* keysight.ads.de.db\_uu.AttrDisplay[](#keysight.ads.de.db_uu.AttrDisplay "Link to this definition")
> :   Bases: [`TextDisplay`](#keysight.ads.de.db_uu.TextDisplay "keysight.ads.de.db_uu._db_x.TextDisplay")
>
>     Display object that displays an attribute of some other object.
>
>     \_\_init\_\_(*obj: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject") | [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *attr\_type: [DesignAttrType](../db/enums.md#keysight.ads.de.db.DesignAttrType "keysight.ads.de.db._db_types.DesignAttrType") | [InstAttrType](../db/enums.md#keysight.ads.de.db.InstAttrType "keysight.ads.de.db._db_types.InstAttrType") | [InstTermAttrType](../db/enums.md#keysight.ads.de.db.InstTermAttrType "keysight.ads.de.db._db_types.InstTermAttrType") | [NetAttrType](../db/enums.md#keysight.ads.de.db.NetAttrType "keysight.ads.de.db._db_types.NetAttrType") | [TermAttrType](../db/enums.md#keysight.ads.de.db.TermAttrType "keysight.ads.de.db._db_types.TermAttrType")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *font\_name: str*, *height: float*, *align: [TextAlignment](../db/enums.md#keysight.ads.de.db.TextAlignment "keysight.ads.de.db._db_types.TextAlignment") = TextAlignment.CENTER\_LEFT*, *orient: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation") = Orientation.R0*, *display\_format: [TextDisplayFormat](../db/enums.md#keysight.ads.de.db.TextDisplayFormat "keysight.ads.de.db._db_types.TextDisplayFormat") = TextDisplayFormat.VALUE*, *has\_overbar: bool = False*, *is\_visible: bool = True*, *is\_drafting: bool = True*) → None[](#keysight.ads.de.db_uu.AttrDisplay.__init__ "Link to this definition")
>
>     *property* attribute*: [DesignAttrType](../db/enums.md#keysight.ads.de.db.DesignAttrType "keysight.ads.de.db._db_types.DesignAttrType") | [InstAttrType](../db/enums.md#keysight.ads.de.db.InstAttrType "keysight.ads.de.db._db_types.InstAttrType") | [InstTermAttrType](../db/enums.md#keysight.ads.de.db.InstTermAttrType "keysight.ads.de.db._db_types.InstTermAttrType") | [NetAttrType](../db/enums.md#keysight.ads.de.db.NetAttrType "keysight.ads.de.db._db_types.NetAttrType") | [TermAttrType](../db/enums.md#keysight.ads.de.db.TermAttrType "keysight.ads.de.db._db_types.TermAttrType")*[](#keysight.ads.de.db_uu.AttrDisplay.attribute "Link to this definition")
>
>     *property* object*: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject") | [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*[](#keysight.ads.de.db_uu.AttrDisplay.object "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.BlockObject[](#keysight.ads.de.db_uu.BlockObject "Link to this definition")
> :   Bases: [`ApolloObject`](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")
>
> *class* keysight.ads.de.db\_uu.BundleNet[](#keysight.ads.de.db_uu.BundleNet "Link to this definition")
> :   Bases: [`Net`](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")
>
>     A multi-bit net whose name contains commas separating the bits (e.g. “a, b, c”).
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *name: str*) → None[](#keysight.ads.de.db_uu.BundleNet.__init__ "Link to this definition")
>
>     *property* bits*: IndexedReadableCollectionAbc[[Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")]*[](#keysight.ads.de.db_uu.BundleNet.bits "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.BundleTerm[](#keysight.ads.de.db_uu.BundleTerm "Link to this definition")
> :   Bases: [`Term`](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")
>
>     \_\_init\_\_(*net: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*, *name: str*, *term\_type: [TermType](../db/enums.md#keysight.ads.de.db.TermType "keysight.ads.de.db._db_types.TermType") = TermType.INPUT\_OUTPUT*, *\**, *number: int = 0*) → None[](#keysight.ads.de.db_uu.BundleTerm.__init__ "Link to this definition")
>
>     *property* bits*: IndexedReadableCollectionAbc[[Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")]*[](#keysight.ads.de.db_uu.BundleTerm.bits "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.BusNet[](#keysight.ads.de.db_uu.BusNet "Link to this definition")
> :   Bases: [`Net`](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")
>
>     A multi-bit net whose name uses bus syntax (e.g. “A<0:7>”).
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *base\_name: str*, *start: int*, *stop: int*, *step: int = 1*) → None[](#keysight.ads.de.db_uu.BusNet.__init__ "Link to this definition")
>
>     *property* bits*: IndexedReadableCollectionAbc[[Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")]*[](#keysight.ads.de.db_uu.BusNet.bits "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.BusTerm[](#keysight.ads.de.db_uu.BusTerm "Link to this definition")
> :   Bases: [`Term`](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")
>
>     \_\_init\_\_(*net: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*, *base\_name: str*, *start: int*, *stop: int*, *step: int = 1*, *term\_type: [TermType](../db/enums.md#keysight.ads.de.db.TermType "keysight.ads.de.db._db_types.TermType") = TermType.INPUT\_OUTPUT*, *\**, *number: int = 0*) → None[](#keysight.ads.de.db_uu.BusTerm.__init__ "Link to this definition")
>
>     *property* bits*: IndexedReadableCollectionAbc[[Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")]*[](#keysight.ads.de.db_uu.BusTerm.bits "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.BusNetBit[](#keysight.ads.de.db_uu.BusNetBit "Link to this definition")
> :   Bases: [`Net`](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")
>
>     A single bit net whose name uses bus syntax (e.g. “A<0>”).
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *base\_name: str*, *bit: int*) → None[](#keysight.ads.de.db_uu.BusNetBit.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.BusTermBit[](#keysight.ads.de.db_uu.BusTermBit "Link to this definition")
> :   Bases: [`Term`](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")
>
>     \_\_init\_\_(*net: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*, *base\_name: str*, *bit: int*, *term\_type: [TermType](../db/enums.md#keysight.ads.de.db.TermType "keysight.ads.de.db._db_types.TermType") = TermType.INPUT\_OUTPUT*, *\**, *number: int = 0*) → None[](#keysight.ads.de.db_uu.BusTermBit.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.CompositeDesignIter[](#keysight.ads.de.db_uu.CompositeDesignIter "Link to this definition")
> :   \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.CompositeDesignIter.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.CompositeObject[](#keysight.ads.de.db_uu.CompositeObject "Link to this definition")
> :   Bases: [`Group`](#keysight.ads.de.db_uu.Group "keysight.ads.de.db_uu._db_x.Group")
>
>     Base class for composite objects in a design.
>
>     A collection of objects that represent a special purpose object
>     such as a Plane or Interconnect.
>
>     *property* master\_object*: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")*[](#keysight.ads.de.db_uu.CompositeObject.master_object "Link to this definition")
>     :   Returns the master object (which is not in this Composite Group).
>
>     *property* name*: str*[](#keysight.ads.de.db_uu.CompositeObject.name "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.ConstructionLine[](#keysight.ads.de.db_uu.ConstructionLine "Link to this definition")
> :   Bases: [`AppObject`](#keysight.ads.de.db_uu.AppObject "keysight.ads.de.db_uu._db_x.AppObject")
>
>     A construction line used to aid in aligning objects.
>
>     \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db_uu.ConstructionLine.__init__ "Link to this definition")
>     :   Return an error about attempts to initialize objects that don’t support initialization.
>
>     *property* layer\_id*: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*[](#keysight.ads.de.db_uu.ConstructionLine.layer_id "Link to this definition")
>
>     *property* points*: tuple[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float], [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]]*[](#keysight.ads.de.db_uu.ConstructionLine.points "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.CustomVia[](#keysight.ads.de.db_uu.CustomVia "Link to this definition")
> :   Bases: [`Via`](#keysight.ads.de.db_uu.Via "keysight.ads.de.db_uu._db_x.Via")
>
>     A custom OpenAccess Via.
>
>     The via is defined partly by its definition in the technology.
>     The geometry of a custom via is determined by another design.
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *via\_def\_name: str*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → None[](#keysight.ads.de.db_uu.CustomVia.__init__ "Link to this definition")
>
>     *property* via\_master\_lcv\_name*: [LCVName](../cellviewref.md#keysight.ads.de.LCVName "keysight.ads.de.LCVName")*[](#keysight.ads.de.db_uu.CustomVia.via_master_lcv_name "Link to this definition")
>     :   The cellview name of the master design referenced by this custom via.
>
> *class* keysight.ads.de.db\_uu.Design[](#keysight.ads.de.db_uu.Design "Link to this definition")
> :   A database that holds all or part of the data that describes a design.
>
>     Depending on the parent module, the units of geometric values will be user units or database units.
>
>     \_\_init\_\_(*lib: str*, *cell: str*, *view: str*, *mode: [DesignMode](../db/enums.md#keysight.ads.de.db.DesignMode "keysight.ads.de.db._design_mode.DesignMode") = DesignMode.READ\_ONLY*) → None[](#keysight.ads.de.db_uu.Design.__init__ "Link to this definition")
>
>     \_\_init\_\_(*lib: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de.Library")*, *cell: str*, *view: str*, *mode: [DesignMode](../db/enums.md#keysight.ads.de.db.DesignMode "keysight.ads.de.db._design_mode.DesignMode") = DesignMode.READ\_ONLY*) → None
>
>     \_\_init\_\_(*\**, *cell: [Cell](../cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")*, *view: str*, *mode: [DesignMode](../db/enums.md#keysight.ads.de.db.DesignMode "keysight.ads.de.db._design_mode.DesignMode") = DesignMode.READ\_ONLY*) → None
>
>     \_\_init\_\_(*\**, *view: [View](../view.md#keysight.ads.de.View "keysight.ads.de.View")*, *mode: [DesignMode](../db/enums.md#keysight.ads.de.db.DesignMode "keysight.ads.de.db._design_mode.DesignMode") = DesignMode.READ\_ONLY*) → None
>
>     add\_attr\_display(*obj: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu.ApolloObject") | [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*, *attr\_type: AttrType*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *font\_name: str*, *height: float*, *align: [TextAlignment](../db/enums.md#keysight.ads.de.db.TextAlignment "keysight.ads.de.db._db_types.TextAlignment") = TextAlignment.CENTER\_LEFT*, *orient: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation") = Orientation.R0*, *display\_format: [TextDisplayFormat](../db/enums.md#keysight.ads.de.db.TextDisplayFormat "keysight.ads.de.db._db_types.TextDisplayFormat") = TextDisplayFormat.VALUE*, *has\_overbar: bool = False*, *is\_visible: bool = True*, *is\_drafting: bool = True*) → [AttrDisplay](#keysight.ads.de.db_uu.AttrDisplay "keysight.ads.de.db_uu.AttrDisplay")[](#keysight.ads.de.db_uu.Design.add_attr_display "Link to this definition")
>
>     add\_circle(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *center: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *radius: float*) → [Ellipse](#keysight.ads.de.db_uu.Ellipse "keysight.ads.de.db_uu.Ellipse")[](#keysight.ads.de.db_uu.Design.add_circle "Link to this definition")
>
>     add\_constrained\_via(*lib\_rule\_name: str*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [PCBVia](#keysight.ads.de.db_uu.PCBVia "keysight.ads.de.db_uu.PCBVia")[](#keysight.ads.de.db_uu.Design.add_constrained_via "Link to this definition")
>
>     add\_construction\_line(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *pt1: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *pt2: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [ConstructionLine](#keysight.ads.de.db_uu.ConstructionLine "keysight.ads.de.db_uu.ConstructionLine")[](#keysight.ads.de.db_uu.Design.add_construction_line "Link to this definition")
>
>     add\_custom\_via(*via\_def\_name: str*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [CustomVia](#keysight.ads.de.db_uu.CustomVia "keysight.ads.de.db_uu.CustomVia")[](#keysight.ads.de.db_uu.Design.add_custom_via "Link to this definition")
>
>     add\_dot(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [Dot](#keysight.ads.de.db_uu.Dot "keysight.ads.de.db_uu.Dot")[](#keysight.ads.de.db_uu.Design.add_dot "Link to this definition")
>
>     add\_dot\_for\_pin(*loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [Dot](#keysight.ads.de.db_uu.Dot "keysight.ads.de.db_uu.Dot")[](#keysight.ads.de.db_uu.Design.add_dot_for_pin "Link to this definition")
>
>     add\_ellipse(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → [Ellipse](#keysight.ads.de.db_uu.Ellipse "keysight.ads.de.db_uu.Ellipse")[](#keysight.ads.de.db_uu.Design.add_ellipse "Link to this definition")
>
>     add\_inst\_attr\_display(*inst: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*, *master\_attribute: [DesignAttrType](../db/enums.md#keysight.ads.de.db.DesignAttrType "keysight.ads.de.db.DesignAttrType")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *font\_name: str*, *height: float*, *align: [TextAlignment](../db/enums.md#keysight.ads.de.db.TextAlignment "keysight.ads.de.db._db_types.TextAlignment") = TextAlignment.CENTER\_LEFT*, *orient: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation") = Orientation.R0*, *display\_format: [TextDisplayFormat](../db/enums.md#keysight.ads.de.db.TextDisplayFormat "keysight.ads.de.db._db_types.TextDisplayFormat") = TextDisplayFormat.VALUE*, *has\_overbar: bool = False*, *is\_visible: bool = True*, *is\_drafting: bool = True*) → [InstAttrDisplay](#keysight.ads.de.db_uu.InstAttrDisplay "keysight.ads.de.db_uu.InstAttrDisplay")[](#keysight.ads.de.db_uu.Design.add_inst_attr_display "Link to this definition")
>
>     add\_instance(*master: [ItemInfo](../item_info.md#keysight.ads.de.ItemInfo "keysight.ads.de.ItemInfo")*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *\**, *angle: float = 0.0*) → [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")[](#keysight.ads.de.db_uu.Design.add_instance "Link to this definition")
>
>     add\_instance(*master: CellviewRefLike*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *\**, *name: str = ''*, *angle: float = 0.0*) → [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")
>
>     add\_line(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *outline: [Outline](../db/genpolyline.md#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline")*, *arc\_resolution: float = 5.0*) → [Line](#keysight.ads.de.db_uu.Line "keysight.ads.de.db_uu.Line")[](#keysight.ads.de.db_uu.Design.add_line "Link to this definition")
>
>     add\_line(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *outline: Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]]*, *arc\_resolution: float = 5.0*) → [Line](#keysight.ads.de.db_uu.Line "keysight.ads.de.db_uu.Line")
>
>     add\_net(*net\_name: str*) → [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu.Net")[](#keysight.ads.de.db_uu.Design.add_net "Link to this definition")
>
>     add\_net\_connection\_label(*pt: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *prop\_name: str*, *net\_name: str*) → [EvalText](#keysight.ads.de.db_uu.EvalText "keysight.ads.de.db_uu.EvalText")[](#keysight.ads.de.db_uu.Design.add_net_connection_label "Link to this definition")
>
>     add\_numbered\_term(*net: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu.Net")*, *term\_name: str*, *term\_number: int*, *term\_type: [TermType](../db/enums.md#keysight.ads.de.db.TermType "keysight.ads.de.db.TermType") = TermType.INPUT\_OUTPUT*) → [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term")[](#keysight.ads.de.db_uu.Design.add_numbered_term "Link to this definition")
>
>     add\_pad\_with\_drill\_layer(*padstack: [Padstack](../tech/pads/pads.md#keysight.ads.de.tech.pads.Padstack "keysight.ads.de.tech.pads.Padstack") | str*, *drill\_layer: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [PCBPad](#keysight.ads.de.db_uu.PCBPad "keysight.ads.de.db_uu.PCBPad")[](#keysight.ads.de.db_uu.Design.add_pad_with_drill_layer "Link to this definition")
>
>     add\_pad\_with\_specified\_layers(*padstack: [Padstack](../tech/pads/pads.md#keysight.ads.de.tech.pads.Padstack "keysight.ads.de.tech.pads.Padstack") | str*, *top\_layer: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *bottom\_layer: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *minimize\_drills: bool = True*) → [PCBPad](#keysight.ads.de.db_uu.PCBPad "keysight.ads.de.db_uu.PCBPad")[](#keysight.ads.de.db_uu.Design.add_pad_with_specified_layers "Link to this definition")
>
>     add\_path(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *polyline: [GenPolyline](../db/genpolyline.md#keysight.ads.de.db.GenPolyline "keysight.ads.de.db._genpolyline.GenPolyline")*) → [Polygon](#keysight.ads.de.db_uu.Polygon "keysight.ads.de.db_uu.Polygon")[](#keysight.ads.de.db_uu.Design.add_path "Link to this definition")
>
>     add\_path(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *polyline: Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]]*, *width: float*) → [Polygon](#keysight.ads.de.db_uu.Polygon "keysight.ads.de.db_uu.Polygon")
>
>     add\_pathseg(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *begin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *end: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *width: float*, *end\_style: [LineEndType](../tech/tech.md#keysight.ads.de.tech.LineEndType "keysight.ads.de._pde.tech.LineEndType")*) → [PathSeg](#keysight.ads.de.db_uu.PathSeg "keysight.ads.de.db_uu.PathSeg")[](#keysight.ads.de.db_uu.Design.add_pathseg "Link to this definition")
>
>     add\_pin(*term: [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term")*, *pin\_figs: [PinFig](#keysight.ads.de.db_uu.PinFig "keysight.ads.de.db_uu.PinFig")*, *\**, *angle: float = 0.0*) → [Pin](#keysight.ads.de.db_uu.Pin "keysight.ads.de.db_uu.Pin")[](#keysight.ads.de.db_uu.Design.add_pin "Link to this definition")
>
>     add\_pin(*term: [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term")*, *pin\_figs: list['PinFig']*, *\**, *angle: float = 0.0*) → [Pin](#keysight.ads.de.db_uu.Pin "keysight.ads.de.db_uu.Pin")
>
>     add\_pin\_fig\_for\_term\_type(*term\_type: [TermType](../db/enums.md#keysight.ads.de.db.TermType "keysight.ads.de.db.TermType")*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [PinFig](#keysight.ads.de.db_uu.PinFig "keysight.ads.de.db_uu.PinFig")[](#keysight.ads.de.db_uu.Design.add_pin_fig_for_term_type "Link to this definition")
>
>     add\_plane(*plane\_info: [PlaneInfo](#keysight.ads.de.db_uu.PlaneInfo "keysight.ads.de.db_uu.PlaneInfo")*, *shape: [GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")*, *name: str*) → [Plane](#keysight.ads.de.db_uu.Plane "keysight.ads.de.db_uu.Plane")[](#keysight.ads.de.db_uu.Design.add_plane "Link to this definition")
>
>     add\_plane(*plane\_info: [PlaneInfo](#keysight.ads.de.db_uu.PlaneInfo "keysight.ads.de.db_uu.PlaneInfo")*, *shape: [GenPolygon](../db/genpolyline.md#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon")*, *name: str*) → [Plane](#keysight.ads.de.db_uu.Plane "keysight.ads.de.db_uu.Plane")
>
>     add\_plane(*plane\_info: [PlaneInfo](#keysight.ads.de.db_uu.PlaneInfo "keysight.ads.de.db_uu.PlaneInfo")*, *shape: [Shape](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu.Shape")*, *name: str*) → [Plane](#keysight.ads.de.db_uu.Plane "keysight.ads.de.db_uu.Plane")
>
>     add\_polygon(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *polygon: [GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles") | [GenPolygon](../db/genpolyline.md#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon") | Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]]*, *arc\_resolution: float = 5.0*) → [Polygon](#keysight.ads.de.db_uu.Polygon "keysight.ads.de.db_uu.Polygon")[](#keysight.ads.de.db_uu.Design.add_polygon "Link to this definition")
>
>     add\_power\_term(*term\_name: str*, *power: str*, *default\_net: str*) → [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term")[](#keysight.ads.de.db_uu.Design.add_power_term "Link to this definition")
>
>     add\_rectangle(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *ll\_or\_box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → [Rect](#keysight.ads.de.db_uu.Rect "keysight.ads.de.db_uu.Rect")[](#keysight.ads.de.db_uu.Design.add_rectangle "Link to this definition")
>
>     add\_rectangle(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *ll\_or\_box: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *ur: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [Rect](#keysight.ads.de.db_uu.Rect "keysight.ads.de.db_uu.Rect")
>
>     add\_scalar\_net(*name: str | None = None*) → [ScalarNet](#keysight.ads.de.db_uu.ScalarNet "keysight.ads.de.db_uu.ScalarNet")[](#keysight.ads.de.db_uu.Design.add_scalar_net "Link to this definition")
>
>     add\_single\_layer\_pad(*padstack: [Padstack](../tech/pads/pads.md#keysight.ads.de.tech.pads.Padstack "keysight.ads.de.tech.pads.Padstack") | str*, *pad\_layer: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [PCBPad](#keysight.ads.de.db_uu.PCBPad "keysight.ads.de.db_uu.PCBPad")[](#keysight.ads.de.db_uu.Design.add_single_layer_pad "Link to this definition")
>
>     add\_stacked\_via(*lib\_rule\_name: str*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [PCBVia](#keysight.ads.de.db_uu.PCBVia "keysight.ads.de.db_uu.PCBVia")[](#keysight.ads.de.db_uu.Design.add_stacked_via "Link to this definition")
>
>     add\_term(*net: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu.Net")*, *term\_name: str*, *term\_type: [TermType](../db/enums.md#keysight.ads.de.db.TermType "keysight.ads.de.db.TermType") = TermType.INPUT\_OUTPUT*) → [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term")[](#keysight.ads.de.db_uu.Design.add_term "Link to this definition")
>
>     add\_text(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *text: str*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *font\_name: str*, *height: float*, *align: [TextAlignment](../db/enums.md#keysight.ads.de.db.TextAlignment "keysight.ads.de.db._db_types.TextAlignment") = TextAlignment.CENTER\_LEFT*, *orient: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation") = Orientation.R0*, *has\_overbar: bool = False*, *is\_visible: bool = True*, *is\_drafting: bool = True*) → [Text](#keysight.ads.de.db_uu.Text "keysight.ads.de.db_uu.Text")[](#keysight.ads.de.db_uu.Design.add_text "Link to this definition")
>
>     add\_through\_pad(*padstack: [Padstack](../tech/pads/pads.md#keysight.ads.de.tech.pads.Padstack "keysight.ads.de.tech.pads.Padstack") | str*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [PCBPad](#keysight.ads.de.db_uu.PCBPad "keysight.ads.de.db_uu.PCBPad")[](#keysight.ads.de.db_uu.Design.add_through_pad "Link to this definition")
>
>     add\_through\_via(*padstack: [Padstack](../tech/pads/pads.md#keysight.ads.de.tech.pads.Padstack "keysight.ads.de.tech.pads.Padstack") | str*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [PCBVia](#keysight.ads.de.db_uu.PCBVia "keysight.ads.de.db_uu.PCBVia")[](#keysight.ads.de.db_uu.Design.add_through_via "Link to this definition")
>
>     add\_trace(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *polyline: [GenPolyline](../db/genpolyline.md#keysight.ads.de.db.GenPolyline "keysight.ads.de.db._genpolyline.GenPolyline")*) → [Polygon](#keysight.ads.de.db_uu.Polygon "keysight.ads.de.db_uu.Polygon")[](#keysight.ads.de.db_uu.Design.add_trace "Link to this definition")
>
>     add\_trace(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *polyline: Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]]*, *width: float*) → [Polygon](#keysight.ads.de.db_uu.Polygon "keysight.ads.de.db_uu.Polygon")
>
>     add\_var\_instance(*origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *name: str | None = None*) → [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")[](#keysight.ads.de.db_uu.Design.add_var_instance "Link to this definition")
>
>     add\_via\_with\_drill\_layer(*padstack: [Padstack](../tech/pads/pads.md#keysight.ads.de.tech.pads.Padstack "keysight.ads.de.tech.pads.Padstack") | str*, *drill\_layer: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [PCBVia](#keysight.ads.de.db_uu.PCBVia "keysight.ads.de.db_uu.PCBVia")[](#keysight.ads.de.db_uu.Design.add_via_with_drill_layer "Link to this definition")
>
>     add\_via\_with\_specified\_layers(*padstack: [Padstack](../tech/pads/pads.md#keysight.ads.de.tech.pads.Padstack "keysight.ads.de.tech.pads.Padstack") | str*, *top\_layer: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *bottom\_layer: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *minimize\_drills: bool = True*) → [PCBVia](#keysight.ads.de.db_uu.PCBVia "keysight.ads.de.db_uu.PCBVia")[](#keysight.ads.de.db_uu.Design.add_via_with_specified_layers "Link to this definition")
>
>     add\_wire(*outline: [Outline](../db/genpolyline.md#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline")*, *\**, *layer\_id: 'LayerId' | None = None*) → [Line](#keysight.ads.de.db_uu.Line "keysight.ads.de.db_uu.Line")[](#keysight.ads.de.db_uu.Design.add_wire "Link to this definition")
>
>     add\_wire(*outline: Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]]*, *\**, *layer\_id: 'LayerId' | None = None*) → [Line](#keysight.ads.de.db_uu.Line "keysight.ads.de.db_uu.Line")
>
>     *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db_uu.Design.bbox "Link to this definition")
>
>     calculate\_text\_width(*text: str*, *font\_height: float*, *font\_name: str*) → float[](#keysight.ads.de.db_uu.Design.calculate_text_width "Link to this definition")
>
>     *property* cell*: [Cell](../cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")*[](#keysight.ads.de.db_uu.Design.cell "Link to this definition")
>
>     *property* cell\_name*: str*[](#keysight.ads.de.db_uu.Design.cell_name "Link to this definition")
>
>     clear\_design() → None[](#keysight.ads.de.db_uu.Design.clear_design "Link to this definition")
>
>     *property* config\_view\_name*: str*[](#keysight.ads.de.db_uu.Design.config_view_name "Link to this definition")
>
>     create\_layer\_id(*layer\_name: str*, *purpose\_name: str | None = None*) → [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")[](#keysight.ads.de.db_uu.Design.create_layer_id "Link to this definition")
>
>     create\_netlist() → str[](#keysight.ads.de.db_uu.Design.create_netlist "Link to this definition")
>
>     *property* dbu\_to\_meter\_factor*: float*[](#keysight.ads.de.db_uu.Design.dbu_to_meter_factor "Link to this definition")
>
>     dbu\_to\_uu(*arg: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*) → [PointUU](../points.md#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU")[](#keysight.ads.de.db_uu.Design.dbu_to_uu "Link to this definition")
>
>     dbu\_to\_uu(*arg: tuple[int, int]*) → [PointUU](../points.md#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU")
>
>     dbu\_to\_uu(*arg: int*) → float
>     :   Convert a value in database units to an equivalent value in user units.
>
>     *property* dbu\_to\_uu\_factor*: float*[](#keysight.ads.de.db_uu.Design.dbu_to_uu_factor "Link to this definition")
>     :   The ratio of user units to database units in the technology of this design.
>
>     *property* default\_wire\_layer*: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")*[](#keysight.ads.de.db_uu.Design.default_wire_layer "Link to this definition")
>
>     *property* design\_name*: str*[](#keysight.ads.de.db_uu.Design.design_name "Link to this definition")
>
>     *property* fig\_groups*: NamedReadableCollectionAbc[[FigGroup](#keysight.ads.de.db_uu.FigGroup "keysight.ads.de.db_uu.FigGroup")]*[](#keysight.ads.de.db_uu.Design.fig_groups "Link to this definition")
>     :   The collection of fig groups in this design.
>
>     find\_instance(*inst\_name: str*) → [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance") | None[](#keysight.ads.de.db_uu.Design.find_instance "Link to this definition")
>
>     find\_net(*net\_name: str*) → [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu.Net") | None[](#keysight.ads.de.db_uu.Design.find_net "Link to this definition")
>
>     find\_or\_add\_net(*net\_name: str*) → [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu.Net")[](#keysight.ads.de.db_uu.Design.find_or_add_net "Link to this definition")
>
>     find\_prop(*name: str*) → [Property](../db/properties.md#keysight.ads.de.db.Property "keysight.ads.de.db.Property") | None[](#keysight.ads.de.db_uu.Design.find_prop "Link to this definition")
>
>     find\_term(*term\_name: str*) → [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term") | None[](#keysight.ads.de.db_uu.Design.find_term "Link to this definition")
>
>     find\_term\_numbered(*term\_number: int*) → [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term") | None[](#keysight.ads.de.db_uu.Design.find_term_numbered "Link to this definition")
>
>     generate\_netlist(*config\_view: CellviewRefLike | None = None*) → str[](#keysight.ads.de.db_uu.Design.generate_netlist "Link to this definition")
>
>     get\_hierarchy\_for\_netlist(*config\_view: CellviewRefLike | None = None*) → [DesignHierarchy](../design_hierarchy.md#keysight.ads.de.DesignHierarchy "keysight.ads.de.DesignHierarchy")[](#keysight.ads.de.db_uu.Design.get_hierarchy_for_netlist "Link to this definition")
>
>     get\_instance(*inst\_name: str*) → [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")[](#keysight.ads.de.db_uu.Design.get_instance "Link to this definition")
>
>     get\_layer\_for\_pin() → [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")[](#keysight.ads.de.db_uu.Design.get_layer_for_pin "Link to this definition")
>
>     get\_layers() → list[[LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")][](#keysight.ads.de.db_uu.Design.get_layers "Link to this definition")
>
>     get\_net\_iter() → [NetIter](#keysight.ads.de.db_uu.NetIter "keysight.ads.de.db_uu.NetIter")[](#keysight.ads.de.db_uu.Design.get_net_iter "Link to this definition")
>
>     get\_pcell\_parent\_library() → [Library](../library.md#keysight.ads.de.Library "keysight.ads.de.Library")[](#keysight.ads.de.db_uu.Design.get_pcell_parent_library "Link to this definition")
>     :   Use during pcell generation to get the library of the parent design.
>
>     get\_preference(*preference: [WorkspacePreference](../experimental/preferences.md#keysight.ads.de.experimental.preferences.WorkspacePreference "keysight.ads.de.experimental.preferences.WorkspacePreference") | [LibSpecificPreference](../experimental/preferences.md#keysight.ads.de.experimental.preferences.LibSpecificPreference "keysight.ads.de.experimental.preferences.LibSpecificPreference")*) → PreferenceValueType[](#keysight.ads.de.db_uu.Design.get_preference "Link to this definition")
>     :   Use `with de.experimental.preferences():` to work with preferences. The API is subject to change.
>
>     get\_snap\_angle\_for\_new\_pin(*loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → float[](#keysight.ads.de.db_uu.Design.get_snap_angle_for_new_pin "Link to this definition")
>
>     get\_snap\_layer\_for\_new\_pin(*loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db_uu.LayerId")[](#keysight.ads.de.db_uu.Design.get_snap_layer_for_new_pin "Link to this definition")
>
>     get\_term\_iter() → [TermIter](#keysight.ads.de.db_uu.TermIter "keysight.ads.de.db_uu.TermIter")[](#keysight.ads.de.db_uu.Design.get_term_iter "Link to this definition")
>
>     *property* groups*: NamedReadableCollectionAbc[[Group](#keysight.ads.de.db_uu.Group "keysight.ads.de.db_uu.Group")]*[](#keysight.ads.de.db_uu.Design.groups "Link to this definition")
>     :   The collection of groups in this design.
>
>         Note: Some groups are not uniquely named.
>
>     *property* has\_explicit\_hierarchy\_policy*: bool*[](#keysight.ads.de.db_uu.Design.has_explicit_hierarchy_policy "Link to this definition")
>
>     *property* hierarchy\_policy\_name*: str*[](#keysight.ads.de.db_uu.Design.hierarchy_policy_name "Link to this definition")
>
>     in\_database\_units() → DesignDBU[](#keysight.ads.de.db_uu.Design.in_database_units "Link to this definition")
>
>     in\_user\_units() → DesignUU[](#keysight.ads.de.db_uu.Design.in_user_units "Link to this definition")
>
>     *property* instances*: NamedItemCollectionAbc[[Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")]*[](#keysight.ads.de.db_uu.Design.instances "Link to this definition")
>
>     *property* is\_layout*: bool*[](#keysight.ads.de.db_uu.Design.is_layout "Link to this definition")
>
>     *property* is\_schematic*: bool*[](#keysight.ads.de.db_uu.Design.is_schematic "Link to this definition")
>
>     *property* is\_symbol*: bool*[](#keysight.ads.de.db_uu.Design.is_symbol "Link to this definition")
>
>     *property* lib\_name*: str*[](#keysight.ads.de.db_uu.Design.lib_name "Link to this definition")
>
>     *property* library*: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de.Library")*[](#keysight.ads.de.db_uu.Design.library "Link to this definition")
>
>     make\_pcell(*function\_name: str*) → None[](#keysight.ads.de.db_uu.Design.make_pcell "Link to this definition")
>
>     *property* meter\_to\_dbu\_factor*: float*[](#keysight.ads.de.db_uu.Design.meter_to_dbu_factor "Link to this definition")
>
>     *property* meter\_to\_uu\_factor*: float*[](#keysight.ads.de.db_uu.Design.meter_to_uu_factor "Link to this definition")
>
>     *property* model\_def*: [ModelDefBase](../db/model_def.md#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db.ModelDefBase") | None*[](#keysight.ads.de.db_uu.Design.model_def "Link to this definition")
>
>     *property* nets*: NamedItemCollectionAbc[[Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu.Net")]*[](#keysight.ads.de.db_uu.Design.nets "Link to this definition")
>
>     *property* pcell\_parameters*: NamedItemCollectionAbc[[OAParam](../db/parameters.md#keysight.ads.de.db.OAParam "keysight.ads.de.db.OAParam")]*[](#keysight.ads.de.db_uu.Design.pcell_parameters "Link to this definition")
>
>     pick\_object\_at(*loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *tolerance: float | None = None*) → [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu.ApolloObject") | None[](#keysight.ads.de.db_uu.Design.pick_object_at "Link to this definition")
>
>     pick\_objects\_at(*loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *tolerance: float | None = None*) → list[[ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu.ApolloObject")][](#keysight.ads.de.db_uu.Design.pick_objects_at "Link to this definition")
>
>     *property* props*: NamedReadableCollectionAbc[[Property](../db/properties.md#keysight.ads.de.db.Property "keysight.ads.de.db.Property")]*[](#keysight.ads.de.db_uu.Design.props "Link to this definition")
>
>     save\_design() → None[](#keysight.ads.de.db_uu.Design.save_design "Link to this definition")
>
>     save\_design\_as(*destination: CellviewRefLike*) → None[](#keysight.ads.de.db_uu.Design.save_design_as "Link to this definition")
>
>     *property* selected\_objects*: list[[ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu.ApolloObject")]*[](#keysight.ads.de.db_uu.Design.selected_objects "Link to this definition")
>
>     set\_origin(*origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → None[](#keysight.ads.de.db_uu.Design.set_origin "Link to this definition")
>
>     set\_preference(*preference: [WorkspacePreference](../experimental/preferences.md#keysight.ads.de.experimental.preferences.WorkspacePreference "keysight.ads.de.experimental.preferences.WorkspacePreference") | [LibSpecificPreference](../experimental/preferences.md#keysight.ads.de.experimental.preferences.LibSpecificPreference "keysight.ads.de.experimental.preferences.LibSpecificPreference")*, *value: PreferenceValueType*) → None[](#keysight.ads.de.db_uu.Design.set_preference "Link to this definition")
>     :   Use `with de.experimental.preferences():` to work with preferences. The API is subject to change.
>
>     *property* shapes*: [ShapeIter](#keysight.ads.de.db_uu.ShapeIter "keysight.ads.de.db_uu.ShapeIter")*[](#keysight.ads.de.db_uu.Design.shapes "Link to this definition")
>
>     *property* terms*: NamedItemCollectionAbc[[Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term")]*[](#keysight.ads.de.db_uu.Design.terms "Link to this definition")
>
>     *property* unit\_name*: str*[](#keysight.ads.de.db_uu.Design.unit_name "Link to this definition")
>
>     uu\_to\_dbu(*arg: [PointUU](../points.md#keysight.ads.de.PointUU "keysight.ads.de._points.PointUU")*) → [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")[](#keysight.ads.de.db_uu.Design.uu_to_dbu "Link to this definition")
>
>     uu\_to\_dbu(*arg: tuple[float, float]*) → [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")
>
>     uu\_to\_dbu(*arg: float*) → int
>     :   Convert a value in user units to an equivalent value in database units.
>
>     *property* uu\_to\_dbu\_factor*: int*[](#keysight.ads.de.db_uu.Design.uu_to_dbu_factor "Link to this definition")
>     :   The ratio of database units to user units in the technology of this design.
>
>     *property* uu\_to\_meter\_factor*: float*[](#keysight.ads.de.db_uu.Design.uu_to_meter_factor "Link to this definition")
>
>     *property* view*: [View](../view.md#keysight.ads.de.View "keysight.ads.de.View")*[](#keysight.ads.de.db_uu.Design.view "Link to this definition")
>
>     *property* view\_name*: str*[](#keysight.ads.de.db_uu.Design.view_name "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.DesignFigGroupIter[](#keysight.ads.de.db_uu.DesignFigGroupIter "Link to this definition")
> :   \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.DesignFigGroupIter.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.Donut[](#keysight.ads.de.db_uu.Donut "Link to this definition")
> :   Bases: [`Shape`](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")
>
> *class* keysight.ads.de.db\_uu.Dot[](#keysight.ads.de.db_uu.Dot "Link to this definition")
> :   Bases: [`Shape`](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *loc: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → None[](#keysight.ads.de.db_uu.Dot.__init__ "Link to this definition")
>
>     *property* height*: float*[](#keysight.ads.de.db_uu.Dot.height "Link to this definition")
>
>     *property* location*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db_uu.Dot.location "Link to this definition")
>
>     *property* width*: float*[](#keysight.ads.de.db_uu.Dot.width "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.Ellipse[](#keysight.ads.de.db_uu.Ellipse "Link to this definition")
> :   Bases: [`Shape`](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *center\_or\_box: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *radius: float*) → None[](#keysight.ads.de.db_uu.Ellipse.__init__ "Link to this definition")
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *center\_or\_box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → None
>
> *class* keysight.ads.de.db\_uu.EvalText[](#keysight.ads.de.db_uu.EvalText "Link to this definition")
> :   Bases: [`Text`](#keysight.ads.de.db_uu.Text "keysight.ads.de.db_uu._db_x.Text")
>
> *class* keysight.ads.de.db\_uu.Fig[](#keysight.ads.de.db_uu.Fig "Link to this definition")
> :   Bases: [`BlockObject`](#keysight.ads.de.db_uu.BlockObject "keysight.ads.de.db_uu._db_x.BlockObject")
>
>     Base class for all figures.
>
>     \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db_uu.Fig.__init__ "Link to this definition")
>     :   Return an error about attempts to initialize objects that don’t support initialization.
>
>     *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db_uu.Fig.bbox "Link to this definition")
>
>     *property* fig\_group\_mem*: FigGroupMem | None*[](#keysight.ads.de.db_uu.Fig.fig_group_mem "Link to this definition")
>     :   Return the FigGroupMem that references this Fig, if it is a member of a FigGroup.
>
> *class* keysight.ads.de.db\_uu.FigGroup[](#keysight.ads.de.db_uu.FigGroup "Link to this definition")
> :   A collection of figures that can be reused.
>
>     This collection is called a Group in the ADS UI.
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *name: str*) → None[](#keysight.ads.de.db_uu.FigGroup.__init__ "Link to this definition")
>
>     add\_object\_to\_fig\_group(*obj: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")*) → None[](#keysight.ads.de.db_uu.FigGroup.add_object_to_fig_group "Link to this definition")
>     :   Add obj to this FigGroup.
>
>         > If obj is a pin, all of its PinFigs will be added.
>         > If obj is a composite object, all of its Figs will be added.
>
>         add\_object\_to\_fig\_group is deprecated, and will be removed in the 2025 Update 2 release. Use add\_to\_fig\_group
>
>     add\_objects(*objects: Sequence[[ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")]*) → None[](#keysight.ads.de.db_uu.FigGroup.add_objects "Link to this definition")
>     :   Add the objects to this FigGroup if not already a member.
>
>     add\_to\_fig\_group(*obj: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")*) → None[](#keysight.ads.de.db_uu.FigGroup.add_to_fig_group "Link to this definition")
>     :   Add obj to this FigGroup.
>
>         If obj is a pin, all of its PinFigs will be added.
>         If obj is a composite object, all of its Figs will be added.
>
>     contains(*obj: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")*) → bool[](#keysight.ads.de.db_uu.FigGroup.contains "Link to this definition")
>
>     *property* has\_any\_children*: bool*[](#keysight.ads.de.db_uu.FigGroup.has_any_children "Link to this definition")
>
>     *property* members*: ReadableCollectionAbc[FigGroupMem]*[](#keysight.ads.de.db_uu.FigGroup.members "Link to this definition")
>
>     *property* name*: str*[](#keysight.ads.de.db_uu.FigGroup.name "Link to this definition")
>
>     remove\_from\_fig\_group(*obj: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")*) → None[](#keysight.ads.de.db_uu.FigGroup.remove_from_fig_group "Link to this definition")
>     :   Remove obj from this FigGroup.
>
>         If obj is a pin, all of its PinFigs will be removed.
>         If obj is a composite object, all of its Figs will be removed.
>
>     remove\_object\_from\_fig\_group(*obj: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")*) → None[](#keysight.ads.de.db_uu.FigGroup.remove_object_from_fig_group "Link to this definition")
>     :   Remove obj from this FigGroup.
>
>         > If obj is a pin, all of its PinFigs will be removed.
>         > If obj is a composite object, all of its Figs will be removed.
>
>         remove\_object\_from\_fig\_group is deprecated, and will be removed in the 2025 Update 2 release. Use remove\_from\_fig\_group
>
> *class* keysight.ads.de.db\_uu.Group[](#keysight.ads.de.db_uu.Group "Link to this definition")
> :   Bases: [`ApolloObject`](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")
>
>     A named collection of objects from the same database.
>
>     Note: Some groups are not uniquely named.
>
>     add\_to\_group(*obj: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")*) → None[](#keysight.ads.de.db_uu.Group.add_to_group "Link to this definition")
>
>     add\_to\_group\_as\_leader(*obj: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")*) → None[](#keysight.ads.de.db_uu.Group.add_to_group_as_leader "Link to this definition")
>
>     contains(*obj: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")*) → bool[](#keysight.ads.de.db_uu.Group.contains "Link to this definition")
>
>     *property* is\_empty*: bool*[](#keysight.ads.de.db_uu.Group.is_empty "Link to this definition")
>
>     *property* is\_ordered*: bool*[](#keysight.ads.de.db_uu.Group.is_ordered "Link to this definition")
>
>     *property* is\_uniquely\_named*: bool*[](#keysight.ads.de.db_uu.Group.is_uniquely_named "Link to this definition")
>     :   True if the group name must be unique in the database that owns the group.
>
>     *property* leader*: [GroupMember](#keysight.ads.de.db_uu.GroupMember "keysight.ads.de.db_uu._db_x.GroupMember") | None*[](#keysight.ads.de.db_uu.Group.leader "Link to this definition")
>
>     *property* members*: ReadableCollectionAbc[[GroupMember](#keysight.ads.de.db_uu.GroupMember "keysight.ads.de.db_uu._db_x.GroupMember")]*[](#keysight.ads.de.db_uu.Group.members "Link to this definition")
>
>     *property* name*: str*[](#keysight.ads.de.db_uu.Group.name "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.GroupMember[](#keysight.ads.de.db_uu.GroupMember "Link to this definition")
> :   Bases: [`ApolloObject`](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")
>
>     A link between a Group and a member object.
>
>     \_\_init\_\_(*group: [Group](#keysight.ads.de.db_uu.Group "keysight.ads.de.db_uu._db_x.Group")*, *obj: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")*, *is\_leader: bool = False*) → None[](#keysight.ads.de.db_uu.GroupMember.__init__ "Link to this definition")
>     :   Create a GroupMember, adding obj to the group.
>
>     *property* group*: [Group](#keysight.ads.de.db_uu.Group "keysight.ads.de.db_uu._db_x.Group")*[](#keysight.ads.de.db_uu.GroupMember.group "Link to this definition")
>
>     *property* is\_leader*: bool*[](#keysight.ads.de.db_uu.GroupMember.is_leader "Link to this definition")
>
>     *property* object*: [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")*[](#keysight.ads.de.db_uu.GroupMember.object "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.Instance[](#keysight.ads.de.db_uu.Instance "Link to this definition")
> :   Bases: [`Ref`](#keysight.ads.de.db_uu.Ref "keysight.ads.de.db_uu._db_x.Ref")
>
>     Represents an instance of a master cellview in a design.
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *master: [ItemInfo](../item_info.md#keysight.ads.de.ItemInfo "keysight.ads.de.ItemInfo")*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *\**, *angle: float = 0.0*) → None[](#keysight.ads.de.db_uu.Instance.__init__ "Link to this definition")
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *master: CellviewRefLike*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *\**, *name: str = ''*, *angle: float = 0.0*) → None
>
>     activate() → None[](#keysight.ads.de.db_uu.Instance.activate "Link to this definition")
>
>     *property* bbox\_annotation\_only*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db_uu.Instance.bbox_annotation_only "Link to this definition")
>
>     *property* bbox\_with\_annotation*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db_uu.Instance.bbox_with_annotation "Link to this definition")
>
>     *property* cell\_name*: str*[](#keysight.ads.de.db_uu.Instance.cell_name "Link to this definition")
>
>     clear\_scope() → None[](#keysight.ads.de.db_uu.Instance.clear_scope "Link to this definition")
>
>     *property* component\_name*: str*[](#keysight.ads.de.db_uu.Instance.component_name "Link to this definition")
>
>     *static* create(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*, *master: CellviewRefLike*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *\**, *name: str = ''*, *angle: float = 0.0*) → [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")[](#keysight.ads.de.db_uu.Instance.create "Link to this definition")
>
>     *static* create\_from\_item(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*, *master: [ItemInfo](../item_info.md#keysight.ads.de.ItemInfo "keysight.ads.de.ItemInfo")*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *\**, *angle: float = 0.0*) → [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")[](#keysight.ads.de.db_uu.Instance.create_from_item "Link to this definition")
>
>     deactivate() → None[](#keysight.ads.de.db_uu.Instance.deactivate "Link to this definition")
>
>     deactivate\_and\_short() → None[](#keysight.ads.de.db_uu.Instance.deactivate_and_short "Link to this definition")
>
>     get\_inst\_pin\_iter() → [InstPinIter](#keysight.ads.de.db_uu.InstPinIter "keysight.ads.de.db_uu._db_x.InstPinIter")[](#keysight.ads.de.db_uu.Instance.get_inst_pin_iter "Link to this definition")
>
>     get\_inst\_term\_iter() → [InstTermIter](#keysight.ads.de.db_uu.InstTermIter "keysight.ads.de.db_uu._db_x.InstTermIter")[](#keysight.ads.de.db_uu.Instance.get_inst_term_iter "Link to this definition")
>
>     *property* has\_global\_scope*: bool*[](#keysight.ads.de.db_uu.Instance.has_global_scope "Link to this definition")
>
>     *property* has\_nested\_scope*: bool*[](#keysight.ads.de.db_uu.Instance.has_nested_scope "Link to this definition")
>
>     *property* inst\_name*: str*[](#keysight.ads.de.db_uu.Instance.inst_name "Link to this definition")
>
>     *property* inst\_pins*: NamedItemCollectionAbc[[InstPin](#keysight.ads.de.db_uu.InstPin "keysight.ads.de.db_uu._db_x.InstPin")]*[](#keysight.ads.de.db_uu.Instance.inst_pins "Link to this definition")
>
>     *property* inst\_terms*: NamedItemCollectionAbc[[InstTerm](#keysight.ads.de.db_uu.InstTerm "keysight.ads.de.db_uu._db_x.InstTerm")]*[](#keysight.ads.de.db_uu.Instance.inst_terms "Link to this definition")
>
>     invoke\_item\_parameter\_changed\_callback(*parameter\_names: str | Sequence[str]*) → None[](#keysight.ads.de.db_uu.Instance.invoke_item_parameter_changed_callback "Link to this definition")
>
>     *property* is\_deactivated*: bool*[](#keysight.ads.de.db_uu.Instance.is_deactivated "Link to this definition")
>
>     *property* is\_deactivated\_and\_shorted*: bool*[](#keysight.ads.de.db_uu.Instance.is_deactivated_and_shorted "Link to this definition")
>
>     *property* is\_implicit*: bool*[](#keysight.ads.de.db_uu.Instance.is_implicit "Link to this definition")
>
>     is\_primitive\_in\_default\_hierarchy\_context(*view: [View](../view.md#keysight.ads.de.View "keysight.ads.de._core.view.View") | None = None*) → bool[](#keysight.ads.de.db_uu.Instance.is_primitive_in_default_hierarchy_context "Link to this definition")
>
>     is\_primitive\_in\_hierarchy(*hierarchy: [DesignHierarchy](../design_hierarchy.md#keysight.ads.de.DesignHierarchy "keysight.ads.de._core.design_hierarchy.DesignHierarchy")*) → bool[](#keysight.ads.de.db_uu.Instance.is_primitive_in_hierarchy "Link to this definition")
>
>     *property* is\_shorted*: bool*[](#keysight.ads.de.db_uu.Instance.is_shorted "Link to this definition")
>
>     *property* is\_var\_instance*: bool*[](#keysight.ads.de.db_uu.Instance.is_var_instance "Link to this definition")
>
>     *property* item\_model\_is\_bom\_item*: bool*[](#keysight.ads.de.db_uu.Instance.item_model_is_bom_item "Link to this definition")
>     :   model\_def.is\_bom\_item
>
>         Type:
>         :   item\_model\_is\_bom\_item is deprecated, and will be removed in the 2025 Update 2 release. Use
>
>     *property* item\_model\_is\_normal\_or\_undefined*: bool*[](#keysight.ads.de.db_uu.Instance.item_model_is_normal_or_undefined "Link to this definition")
>     :   model\_def is None
>
>         Type:
>         :   item\_model\_is\_normal\_or\_undefined is deprecated, and will be removed in the 2025 Update 2 release. Use
>
>     *property* item\_model\_is\_sub\_design*: bool*[](#keysight.ads.de.db_uu.Instance.item_model_is_sub_design "Link to this definition")
>     :   model\_def.is\_sub\_design
>
>         Type:
>         :   item\_model\_is\_sub\_design is deprecated, and will be removed in the 2025 Update 2 release. Use
>
>     *property* library\_name*: str*[](#keysight.ads.de.db_uu.Instance.library_name "Link to this definition")
>
>     *property* master\_cell*: [Cell](../cell.md#keysight.ads.de.Cell "keysight.ads.de._core.cell.Cell") | None*[](#keysight.ads.de.db_uu.Instance.master_cell "Link to this definition")
>
>     *property* master\_lcv\_name*: [LCVName](../cellviewref.md#keysight.ads.de.LCVName "keysight.ads.de.LCVName")*[](#keysight.ads.de.db_uu.Instance.master_lcv_name "Link to this definition")
>
>     *property* model\_cell\_name*: str*[](#keysight.ads.de.db_uu.Instance.model_cell_name "Link to this definition")
>
>     *property* model\_def*: [ModelDefBase](../db/model_def.md#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db._model_def.ModelDefBase") | None*[](#keysight.ads.de.db_uu.Instance.model_def "Link to this definition")
>
>     *property* model\_library\_name*: str*[](#keysight.ads.de.db_uu.Instance.model_library_name "Link to this definition")
>
>     *property* name*: str*[](#keysight.ads.de.db_uu.Instance.name "Link to this definition")
>
>     *property* net*: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net") | None*[](#keysight.ads.de.db_uu.Instance.net "Link to this definition")
>
>     *property* origin*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db_uu.Instance.origin "Link to this definition")
>
>     *property* parameters*: ParamBaseCollection*[](#keysight.ads.de.db_uu.Instance.parameters "Link to this definition")
>
>     set\_global\_scope() → None[](#keysight.ads.de.db_uu.Instance.set_global_scope "Link to this definition")
>
>     set\_nested\_scope() → None[](#keysight.ads.de.db_uu.Instance.set_nested_scope "Link to this definition")
>
>     *property* specialized\_subview*: str*[](#keysight.ads.de.db_uu.Instance.specialized_subview "Link to this definition")
>
>     update\_item\_annotation() → None[](#keysight.ads.de.db_uu.Instance.update_item_annotation "Link to this definition")
>
>     *property* vars*: VarParamCollection*[](#keysight.ads.de.db_uu.Instance.vars "Link to this definition")
>
>     *property* view\_name*: str*[](#keysight.ads.de.db_uu.Instance.view_name "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.InstanceIter[](#keysight.ads.de.db_uu.InstanceIter "Link to this definition")
> :   \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.InstanceIter.__init__ "Link to this definition")
>
>     *property* design*: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*[](#keysight.ads.de.db_uu.InstanceIter.design "Link to this definition")
>
>     exclude\_composite\_children() → None[](#keysight.ads.de.db_uu.InstanceIter.exclude_composite_children "Link to this definition")
>
>     exclude\_pin\_insts() → None[](#keysight.ads.de.db_uu.InstanceIter.exclude_pin_insts "Link to this definition")
>
>     include\_composite\_children() → None[](#keysight.ads.de.db_uu.InstanceIter.include_composite_children "Link to this definition")
>
>     include\_implicit\_insts() → None[](#keysight.ads.de.db_uu.InstanceIter.include_implicit_insts "Link to this definition")
>
>     include\_pin\_insts() → None[](#keysight.ads.de.db_uu.InstanceIter.include_pin_insts "Link to this definition")
>
>     limit\_region(*region: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*, *allow\_intersect: bool*) → None[](#keysight.ads.de.db_uu.InstanceIter.limit_region "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.InstAttrDisplay[](#keysight.ads.de.db_uu.InstAttrDisplay "Link to this definition")
> :   Bases: [`TextDisplay`](#keysight.ads.de.db_uu.TextDisplay "keysight.ads.de.db_uu._db_x.TextDisplay")
>
>     Display object that displays an attribute of an instance master.
>
>     \_\_init\_\_(*inst: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*, *master\_attribute: [DesignAttrType](../db/enums.md#keysight.ads.de.db.DesignAttrType "keysight.ads.de.db.DesignAttrType")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *font\_name: str*, *height: float*, *align: [TextAlignment](../db/enums.md#keysight.ads.de.db.TextAlignment "keysight.ads.de.db._db_types.TextAlignment") = TextAlignment.CENTER\_LEFT*, *orient: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation") = Orientation.R0*, *display\_format: [TextDisplayFormat](../db/enums.md#keysight.ads.de.db.TextDisplayFormat "keysight.ads.de.db._db_types.TextDisplayFormat") = TextDisplayFormat.VALUE*, *has\_overbar: bool = False*, *is\_visible: bool = True*, *is\_drafting: bool = True*) → None[](#keysight.ads.de.db_uu.InstAttrDisplay.__init__ "Link to this definition")
>
>     *property* instance*: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*[](#keysight.ads.de.db_uu.InstAttrDisplay.instance "Link to this definition")
>
>     *property* master\_attribute*: [DesignAttrType](../db/enums.md#keysight.ads.de.db.DesignAttrType "keysight.ads.de.db.DesignAttrType")*[](#keysight.ads.de.db_uu.InstAttrDisplay.master_attribute "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.InstPin[](#keysight.ads.de.db_uu.InstPin "Link to this definition")
> :   Represents the physical connection between an instance terminal and a pin on the master design.
>
>     \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db_uu.InstPin.__init__ "Link to this definition")
>     :   Return an error about attempts to initialize objects that don’t support initialization.
>
>     add\_label(*label: str*, *pt: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [AttrDisplay](#keysight.ads.de.db_uu.AttrDisplay "keysight.ads.de.db_uu._db_x.AttrDisplay")[](#keysight.ads.de.db_uu.InstPin.add_label "Link to this definition")
>
>     *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF") | None*[](#keysight.ads.de.db_uu.InstPin.bbox "Link to this definition")
>
>     find\_first\_wire\_label() → [AttrDisplay](#keysight.ads.de.db_uu.AttrDisplay "keysight.ads.de.db_uu._db_x.AttrDisplay") | None[](#keysight.ads.de.db_uu.InstPin.find_first_wire_label "Link to this definition")
>
>     get\_angle\_normalized() → int[](#keysight.ads.de.db_uu.InstPin.get_angle_normalized "Link to this definition")
>
>     get\_snap\_layer\_id() → [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")[](#keysight.ads.de.db_uu.InstPin.get_snap_layer_id "Link to this definition")
>
>     *property* inst\_pin\_id*: str*[](#keysight.ads.de.db_uu.InstPin.inst_pin_id "Link to this definition")
>
>     *property* inst\_term*: [InstTerm](#keysight.ads.de.db_uu.InstTerm "keysight.ads.de.db_uu._db_x.InstTerm")*[](#keysight.ads.de.db_uu.InstPin.inst_term "Link to this definition")
>
>     *property* instance*: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*[](#keysight.ads.de.db_uu.InstPin.instance "Link to this definition")
>
>     *property* is\_valid*: bool*[](#keysight.ads.de.db_uu.InstPin.is_valid "Link to this definition")
>
>     *property* master\_pin*: [Pin](#keysight.ads.de.db_uu.Pin "keysight.ads.de.db_uu._db_x.Pin") | None*[](#keysight.ads.de.db_uu.InstPin.master_pin "Link to this definition")
>
>     *property* net*: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net") | None*[](#keysight.ads.de.db_uu.InstPin.net "Link to this definition")
>
>     *property* snap\_point*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | None*[](#keysight.ads.de.db_uu.InstPin.snap_point "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.InstPinIter[](#keysight.ads.de.db_uu.InstPinIter "Link to this definition")
> :   Bases: `object`
>
>     \_\_init\_\_(*obj: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*) → None[](#keysight.ads.de.db_uu.InstPinIter.__init__ "Link to this definition")
>
>     \_\_init\_\_(*obj: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*) → None
>
>     \_\_init\_\_(*obj: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*, *term\_or\_bbox: str*) → None
>
>     \_\_init\_\_(*obj: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*, *term\_or\_bbox: int*) → None
>
>     \_\_init\_\_(*obj: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*, *term\_or\_bbox: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → None
>
>     \_\_init\_\_(*obj: [InstTerm](#keysight.ads.de.db_uu.InstTerm "keysight.ads.de.db_uu._db_x.InstTerm")*) → None
>
> *class* keysight.ads.de.db\_uu.InstPropDisplay[](#keysight.ads.de.db_uu.InstPropDisplay "Link to this definition")
> :   Bases: [`TextDisplay`](#keysight.ads.de.db_uu.TextDisplay "keysight.ads.de.db_uu._db_x.TextDisplay")
>
>     Display object that displays a property value of an instance master.
>
>     *property* instance*: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*[](#keysight.ads.de.db_uu.InstPropDisplay.instance "Link to this definition")
>
>     *property* master\_prop*: [Property](../db/properties.md#keysight.ads.de.db.Property "keysight.ads.de.db.Property")*[](#keysight.ads.de.db_uu.InstPropDisplay.master_prop "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.InstTerm[](#keysight.ads.de.db_uu.InstTerm "Link to this definition")
> :   Bases: [`BlockObject`](#keysight.ads.de.db_uu.BlockObject "keysight.ads.de.db_uu._db_x.BlockObject")
>
>     Represents a connection between a net and a terminal in the master of an instance.
>
>     If either the instance or term is multibit, the number of bits in the net must match
>     the number of bits in the instance times the number of bits in the term.
>
>     InstTerms can exist that do not have a corresponding terminal in the instance master design.
>     In this case, the InstTerm is not bound.
>
>     InstTerms can be bound by name or by number. If bound by number, all InstTerms on the
>     instance must be bound by number. If bound by name, the InstTerm is bound to the terminal
>     in the master design with the same name.
>
>     \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db_uu.InstTerm.__init__ "Link to this definition")
>     :   Return an error about attempts to initialize objects that don’t support initialization.
>
>     add\_label(*label: str*, *pt: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [AttrDisplay](#keysight.ads.de.db_uu.AttrDisplay "keysight.ads.de.db_uu._db_x.AttrDisplay")[](#keysight.ads.de.db_uu.InstTerm.add_label "Link to this definition")
>
>     *property* bits*: IndexedReadableCollectionAbc[[InstTerm](#keysight.ads.de.db_uu.InstTerm "keysight.ads.de.db_uu._db_x.InstTerm")]*[](#keysight.ads.de.db_uu.InstTerm.bits "Link to this definition")
>
>     find\_first\_wire\_label() → [AttrDisplay](#keysight.ads.de.db_uu.AttrDisplay "keysight.ads.de.db_uu._db_x.AttrDisplay") | None[](#keysight.ads.de.db_uu.InstTerm.find_first_wire_label "Link to this definition")
>
>     get\_inst\_pin\_iter() → [InstPinIter](#keysight.ads.de.db_uu.InstPinIter "keysight.ads.de.db_uu._db_x.InstPinIter")[](#keysight.ads.de.db_uu.InstTerm.get_inst_pin_iter "Link to this definition")
>
>     get\_inst\_term\_name() → str[](#keysight.ads.de.db_uu.InstTerm.get_inst_term_name "Link to this definition")
>     :   get\_inst\_term\_name is deprecated, and will be removed in the 2025 Update 2 release. Use term\_name if not numbered or term.name if bound.
>
>     get\_inst\_term\_number() → int[](#keysight.ads.de.db_uu.InstTerm.get_inst_term_number "Link to this definition")
>     :   get\_inst\_term\_number is deprecated, and will be removed in the 2025 Update 2 release. Use term\_number if numbered or term.number if bound.
>
>     *property* inst\_pins*: NamedItemCollectionAbc[[InstPin](#keysight.ads.de.db_uu.InstPin "keysight.ads.de.db_uu._db_x.InstPin")]*[](#keysight.ads.de.db_uu.InstTerm.inst_pins "Link to this definition")
>
>     *property* inst\_term\_id*: str*[](#keysight.ads.de.db_uu.InstTerm.inst_term_id "Link to this definition")
>
>     *property* instance*: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*[](#keysight.ads.de.db_uu.InstTerm.instance "Link to this definition")
>
>     *property* is\_bound*: bool*[](#keysight.ads.de.db_uu.InstTerm.is_bound "Link to this definition")
>     :   Return True if this InstTerm is bound to the matching terminal on the master design.
>
>     *property* is\_implicit*: bool*[](#keysight.ads.de.db_uu.InstTerm.is_implicit "Link to this definition")
>
>     *property* is\_numbered*: bool*[](#keysight.ads.de.db_uu.InstTerm.is_numbered "Link to this definition")
>     :   Return True if this InstTerm uses numbers to bind to the terminal.
>
>     *property* net*: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net") | None*[](#keysight.ads.de.db_uu.InstTerm.net "Link to this definition")
>
>     *property* term*: [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term") | None*[](#keysight.ads.de.db_uu.InstTerm.term "Link to this definition")
>
>     *property* term\_name*: str*[](#keysight.ads.de.db_uu.InstTerm.term_name "Link to this definition")
>     :   Return the term name if this InstTerm uses names to bind the term.
>
>         Otherwise, raise an exception.
>
>     *property* term\_number*: int*[](#keysight.ads.de.db_uu.InstTerm.term_number "Link to this definition")
>     :   Return the term number if this InstTerm uses numbers to bind the term.
>
>         Otherwise, raise an exception.
>
> *class* keysight.ads.de.db\_uu.InstTermIter[](#keysight.ads.de.db_uu.InstTermIter "Link to this definition")
> :   \_\_init\_\_(*obj: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*)[](#keysight.ads.de.db_uu.InstTermIter.__init__ "Link to this definition")
>
>     \_\_init\_\_(*obj: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*)
>
> *class* keysight.ads.de.db\_uu.Interconnect[](#keysight.ads.de.db_uu.Interconnect "Link to this definition")
> :   Bases: [`CompositeObject`](#keysight.ads.de.db_uu.CompositeObject "keysight.ads.de.db_uu._db_x.CompositeObject")
>
>     An Interconnect is a composite object used to implement a Trace.
>
>     *property* interconnect\_info*: [InterconnectInfo](#keysight.ads.de.db_uu.InterconnectInfo "keysight.ads.de.db_uu.InterconnectInfo")*[](#keysight.ads.de.db_uu.Interconnect.interconnect_info "Link to this definition")
>     :   Return a reference to the cached copy of the InterconnectInfo for this Interconnect.
>
> *class* keysight.ads.de.db\_uu.InterconnectDesignIter[](#keysight.ads.de.db_uu.InterconnectDesignIter "Link to this definition")
> :   \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.InterconnectDesignIter.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.InterconnectInfo[](#keysight.ads.de.db_uu.InterconnectInfo "Link to this definition")
> :   Holds the information required to create an Interconnect, trace or path.
>
>     It may also hold the information that describes existing traces, paths and interconnect.
>
>     \_\_init\_\_(*obj: [Tech](../tech/tech.md#keysight.ads.de.tech.Tech "keysight.ads.de.tech._tech.Tech")*)[](#keysight.ads.de.db_uu.InterconnectInfo.__init__ "Link to this definition")
>
>     \_\_init\_\_(*obj: [Interconnect](#keysight.ads.de.db_uu.Interconnect "keysight.ads.de.db_uu._db_x.Interconnect")*)
>
>     \_\_init\_\_(*obj: [Path](#keysight.ads.de.db_uu.Path "keysight.ads.de.db_uu._db_x.Path")*)
>
>     \_\_init\_\_(*obj: [Shape](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")*)
>
>     \_\_init\_\_(*obj: [Tech](../tech/tech.md#keysight.ads.de.tech.Tech "keysight.ads.de.tech._tech.Tech")*, *line: [GenPolyline](../db/genpolyline.md#keysight.ads.de.db.GenPolyline "keysight.ads.de.db._genpolyline.GenPolyline")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*)
>     :   Create a new InterconnectInfo object.
>
>         InterconnectInfo(tech):
>         :   creates an empty InterconnectInfo.
>
>         InterconnectInfo(tech, gen\_polyline, layer\_id):
>         :   creates an InterconnectInfo based on the information from the polyline.
>
>         InterconnectInfo(interconnect):
>         :   creates an InterconnectInfo with a copy of the information from the interconnect object.
>
>         InterconnectInfo(path):
>         :   creates an InterconnectInfo with a copy of the information from the path object.
>
>         InterconnectInfo(shape):
>         :   creates an InterconnectInfo with a copy of the information from the shape object.
>
>     add\_point(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → None[](#keysight.ads.de.db_uu.InterconnectInfo.add_point "Link to this definition")
>
>     add\_point\_with\_bulge(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *bulge: float*) → None[](#keysight.ads.de.db_uu.InterconnectInfo.add_point_with_bulge "Link to this definition")
>
>     add\_points(*points: Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]]*) → None[](#keysight.ads.de.db_uu.InterconnectInfo.add_points "Link to this definition")
>
>     construct\_interconnect(*net: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*) → [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")[](#keysight.ads.de.db_uu.InterconnectInfo.construct_interconnect "Link to this definition")
>
>     construct\_interconnect\_or\_trace\_with\_search\_for\_net(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → [ApolloObject](#keysight.ads.de.db_uu.ApolloObject "keysight.ads.de.db_uu._db_x.ApolloObject")[](#keysight.ads.de.db_uu.InterconnectInfo.construct_interconnect_or_trace_with_search_for_net "Link to this definition")
>
>     construct\_interconnect\_with\_search\_for\_net(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *name\_prefix: str = ''*) → [Interconnect](#keysight.ads.de.db_uu.Interconnect "keysight.ads.de.db_uu._db_x.Interconnect")[](#keysight.ads.de.db_uu.InterconnectInfo.construct_interconnect_with_search_for_net "Link to this definition")
>
>     construct\_trace(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → [Polygon](#keysight.ads.de.db_uu.Polygon "keysight.ads.de.db_uu._db_x.Polygon")[](#keysight.ads.de.db_uu.InterconnectInfo.construct_trace "Link to this definition")
>
>     copy() → [InterconnectInfo](#keysight.ads.de.db_uu.InterconnectInfo "keysight.ads.de.db_uu._interconnect.InterconnectInfo")[](#keysight.ads.de.db_uu.InterconnectInfo.copy "Link to this definition")
>     :   Return a copy of this object.
>
>     data\_matches(*other: [InterconnectInfo](#keysight.ads.de.db_uu.InterconnectInfo "keysight.ads.de.db_uu._interconnect.InterconnectInfo")*, *check\_layers: bool*) → bool[](#keysight.ads.de.db_uu.InterconnectInfo.data_matches "Link to this definition")
>     :   Return true if the other info has matching data.
>
>     *property* first\_line\_info*: [LineTypeInfo](line_type_info.md#keysight.ads.de.db_uu.LineTypeInfo "keysight.ads.de.db_uu._line_type_info.LineTypeInfo")*[](#keysight.ads.de.db_uu.InterconnectInfo.first_line_info "Link to this definition")
>
>     *property* first\_point*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | None*[](#keysight.ads.de.db_uu.InterconnectInfo.first_point "Link to this definition")
>
>     get\_line\_info\_at\_end(*end: WhichConnection*) → [LineTypeInfo](line_type_info.md#keysight.ads.de.db_uu.LineTypeInfo "keysight.ads.de.db_uu._line_type_info.LineTypeInfo")[](#keysight.ads.de.db_uu.InterconnectInfo.get_line_info_at_end "Link to this definition")
>
>     get\_point\_at\_end(*end: WhichConnection*) → [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | None[](#keysight.ads.de.db_uu.InterconnectInfo.get_point_at_end "Link to this definition")
>
>     get\_starting\_index\_of\_segment(*segment\_number: int*) → int[](#keysight.ads.de.db_uu.InterconnectInfo.get_starting_index_of_segment "Link to this definition")
>
>     get\_via\_at\_index(*index: int*) → [ViaElement](#keysight.ads.de.db_uu.ViaElement "keysight.ads.de.db_uu._db_x.ViaElement")[](#keysight.ads.de.db_uu.InterconnectInfo.get_via_at_index "Link to this definition")
>
>     *property* has\_any\_teardrop\_definitions*: bool*[](#keysight.ads.de.db_uu.InterconnectInfo.has_any_teardrop_definitions "Link to this definition")
>
>     *property* has\_any\_vias*: bool*[](#keysight.ads.de.db_uu.InterconnectInfo.has_any_vias "Link to this definition")
>
>     *property* has\_arcs*: bool*[](#keysight.ads.de.db_uu.InterconnectInfo.has_arcs "Link to this definition")
>
>     has\_via\_at\_index(*index: int*) → bool[](#keysight.ads.de.db_uu.InterconnectInfo.has_via_at_index "Link to this definition")
>
>     initialize\_first\_line\_type(*info: [LineTypeInfo](line_type_info.md#keysight.ads.de.db_uu.LineTypeInfo "keysight.ads.de.db_uu._line_type_info.LineTypeInfo")*) → None[](#keysight.ads.de.db_uu.InterconnectInfo.initialize_first_line_type "Link to this definition")
>
>     *property* last\_line\_info*: [LineTypeInfo](line_type_info.md#keysight.ads.de.db_uu.LineTypeInfo "keysight.ads.de.db_uu._line_type_info.LineTypeInfo")*[](#keysight.ads.de.db_uu.InterconnectInfo.last_line_info "Link to this definition")
>
>     *property* last\_point*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | None*[](#keysight.ads.de.db_uu.InterconnectInfo.last_point "Link to this definition")
>
>     *property* outline*: [Outline](../db/genpolyline.md#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline")*[](#keysight.ads.de.db_uu.InterconnectInfo.outline "Link to this definition")
>
>     set\_last\_arc\_angle\_then\_add\_point(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *angle: float*) → None[](#keysight.ads.de.db_uu.InterconnectInfo.set_last_arc_angle_then_add_point "Link to this definition")
>
>     set\_last\_bulge\_then\_add\_point(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *bulge: float*) → None[](#keysight.ads.de.db_uu.InterconnectInfo.set_last_bulge_then_add_point "Link to this definition")
>
>     set\_next\_line\_type(*info: [LineTypeInfo](line_type_info.md#keysight.ads.de.db_uu.LineTypeInfo "keysight.ads.de.db_uu._line_type_info.LineTypeInfo")*) → None[](#keysight.ads.de.db_uu.InterconnectInfo.set_next_line_type "Link to this definition")
>
>     set\_via\_at\_last\_point(*via\_element: [ViaElement](#keysight.ads.de.db_uu.ViaElement "keysight.ads.de.db_uu._db_x.ViaElement")*) → None[](#keysight.ads.de.db_uu.InterconnectInfo.set_via_at_last_point "Link to this definition")
>
>     *property* teardrop\_touch\_back*: [TeardropTouching](../db/genpolyline.md#keysight.ads.de.db.TeardropTouching "keysight.ads.de.db._teardrop.TeardropTouching")*[](#keysight.ads.de.db_uu.InterconnectInfo.teardrop_touch_back "Link to this definition")
>
>     *property* teardrop\_touch\_front*: [TeardropTouching](../db/genpolyline.md#keysight.ads.de.db.TeardropTouching "keysight.ads.de.db._teardrop.TeardropTouching")*[](#keysight.ads.de.db_uu.InterconnectInfo.teardrop_touch_front "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.Line[](#keysight.ads.de.db_uu.Line "Link to this definition")
> :   Bases: [`Shape`](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *outline: [Outline](../db/genpolyline.md#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline")*, *arc\_resolution: float = 5.0*) → None[](#keysight.ads.de.db_uu.Line.__init__ "Link to this definition")
>
>     add\_text\_label(*label: str*, *pt: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float] | None = None*) → [Text](#keysight.ads.de.db_uu.Text "keysight.ads.de.db_uu._db_x.Text")[](#keysight.ads.de.db_uu.Line.add_text_label "Link to this definition")
>
>     add\_wire\_label(*label: str*, *pt: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float] | None = None*) → [AttrDisplay](#keysight.ads.de.db_uu.AttrDisplay "keysight.ads.de.db_uu._db_x.AttrDisplay")[](#keysight.ads.de.db_uu.Line.add_wire_label "Link to this definition")
>
>     *property* interconnect\_info*: [InterconnectInfo](#keysight.ads.de.db_uu.InterconnectInfo "keysight.ads.de.db_uu.InterconnectInfo")*[](#keysight.ads.de.db_uu.Line.interconnect_info "Link to this definition")
>     :   Return a reference to the cached copy of the InterconnectInfo for this Line.
>
> *class* keysight.ads.de.db\_uu.Net[](#keysight.ads.de.db_uu.Net "Link to this definition")
> :   Bases: [`BlockObject`](#keysight.ads.de.db_uu.BlockObject "keysight.ads.de.db_uu._db_x.BlockObject")
>
>     Base class for net objects.
>
>     \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db_uu.Net.__init__ "Link to this definition")
>     :   Return an error about attempts to initialize objects that don’t support initialization.
>
>     are\_all\_bits\_of\_net\_global\_ground() → bool[](#keysight.ads.de.db_uu.Net.are_all_bits_of_net_global_ground "Link to this definition")
>
>     *static* create(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *net\_name: str*) → [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")[](#keysight.ads.de.db_uu.Net.create "Link to this definition")
>     :   Create a derived net object, depending on the type of name.
>
>     get\_bit(*number: int*) → [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")[](#keysight.ads.de.db_uu.Net.get_bit "Link to this definition")
>
>     get\_inst\_pin\_iter() → [InstPinIter](#keysight.ads.de.db_uu.InstPinIter "keysight.ads.de.db_uu._db_x.InstPinIter")[](#keysight.ads.de.db_uu.Net.get_inst_pin_iter "Link to this definition")
>
>     get\_preferred\_net() → [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")[](#keysight.ads.de.db_uu.Net.get_preferred_net "Link to this definition")
>
>     *property* inst\_pins*: NamedItemCollectionAbc[[InstPin](#keysight.ads.de.db_uu.InstPin "keysight.ads.de.db_uu._db_x.InstPin")]*[](#keysight.ads.de.db_uu.Net.inst_pins "Link to this definition")
>
>     is\_empty\_and\_unlabeled() → bool[](#keysight.ads.de.db_uu.Net.is_empty_and_unlabeled "Link to this definition")
>
>     *property* is\_global*: bool*[](#keysight.ads.de.db_uu.Net.is_global "Link to this definition")
>
>     *property* is\_global\_ground*: bool*[](#keysight.ads.de.db_uu.Net.is_global_ground "Link to this definition")
>
>     *property* is\_implicit*: bool*[](#keysight.ads.de.db_uu.Net.is_implicit "Link to this definition")
>
>     *property* name*: str*[](#keysight.ads.de.db_uu.Net.name "Link to this definition")
>     :   Return net name.
>
>         If the net was created without a name, one has been generated for it.
>
>     *property* num\_bits*: int*[](#keysight.ads.de.db_uu.Net.num_bits "Link to this definition")
>
>     *property* shapes*: [ShapeIter](#keysight.ads.de.db_uu.ShapeIter "keysight.ads.de.db_uu._db_x.ShapeIter")*[](#keysight.ads.de.db_uu.Net.shapes "Link to this definition")
>
>     *property* signal\_type*: [SignalType](../db/enums.md#keysight.ads.de.db.SignalType "keysight.ads.de.db._db_types.SignalType")*[](#keysight.ads.de.db_uu.Net.signal_type "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.NetIter[](#keysight.ads.de.db_uu.NetIter "Link to this definition")
> :   \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.NetIter.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.Path[](#keysight.ads.de.db_uu.Path "Link to this definition")
> :   Bases: [`Shape`](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")
>
>     *property* interconnect\_info*: [InterconnectInfo](#keysight.ads.de.db_uu.InterconnectInfo "keysight.ads.de.db_uu.InterconnectInfo")*[](#keysight.ads.de.db_uu.Path.interconnect_info "Link to this definition")
>     :   Return a reference to the cached copy of the InterconnectInfo for this Path.
>
> *class* keysight.ads.de.db\_uu.PathSeg[](#keysight.ads.de.db_uu.PathSeg "Link to this definition")
> :   Bases: [`Shape`](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *begin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *end: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *width: float*, *end\_style: [LineEndType](../tech/tech.md#keysight.ads.de.tech.LineEndType "keysight.ads.de._pde.tech.LineEndType")*) → None[](#keysight.ads.de.db_uu.PathSeg.__init__ "Link to this definition")
>
>     *property* begin\_point*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db_uu.PathSeg.begin_point "Link to this definition")
>
>     *property* end\_point*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db_uu.PathSeg.end_point "Link to this definition")
>
>     set\_points(*begin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *end: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → None[](#keysight.ads.de.db_uu.PathSeg.set_points "Link to this definition")
>
>     *property* width*: float*[](#keysight.ads.de.db_uu.PathSeg.width "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.PCBBase[](#keysight.ads.de.db_uu.PCBBase "Link to this definition")
> :   Bases: [`ScalarInst`](#keysight.ads.de.db_uu.ScalarInst "keysight.ads.de.db_uu._db_x.ScalarInst")
>
>     Base class for PCB Pads and Vias.
>
>     *class* PadViaType[](#keysight.ads.de.db_uu.PCBBase.PadViaType "Link to this definition")
>     :   Bases: `pybind11_object`
>
>         Type of Pad or Via.
>
>         Members:
>
>         > SINGLE\_LAYER\_PAD
>         >
>         > DRILL\_LAYER
>         >
>         > THROUGH
>         >
>         > BLIND\_BURIED\_PAD
>
>         BLIND\_BURIED\_PAD *= <PadViaType.BLIND\_BURIED\_PAD: 3>*[](#keysight.ads.de.db_uu.PCBBase.PadViaType.BLIND_BURIED_PAD "Link to this definition")
>
>         DRILL\_LAYER *= <PadViaType.DRILL\_LAYER: 1>*[](#keysight.ads.de.db_uu.PCBBase.PadViaType.DRILL_LAYER "Link to this definition")
>
>         SINGLE\_LAYER\_PAD *= <PadViaType.SINGLE\_LAYER\_PAD: 0>*[](#keysight.ads.de.db_uu.PCBBase.PadViaType.SINGLE_LAYER_PAD "Link to this definition")
>
>         THROUGH *= <PadViaType.THROUGH: 2>*[](#keysight.ads.de.db_uu.PCBBase.PadViaType.THROUGH "Link to this definition")
>
>         \_\_init\_\_(*self: [keysight.ads.de.\_pde.db.PadViaType](#keysight.ads.de.db_uu.PCBBase.PadViaType "keysight.ads.de._pde.db.PadViaType")*, *value: int*) → None[](#keysight.ads.de.db_uu.PCBBase.PadViaType.__init__ "Link to this definition")
>
>         *property* name[](#keysight.ads.de.db_uu.PCBBase.PadViaType.name "Link to this definition")
>
>         *property* value[](#keysight.ads.de.db_uu.PCBBase.PadViaType.value "Link to this definition")
>
>     *static* is\_pcb\_pad(*inst: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*) → TypeGuard[[PCBPad](#keysight.ads.de.db_uu.PCBPad "keysight.ads.de.db_uu._db_x.PCBPad")][](#keysight.ads.de.db_uu.PCBBase.is_pcb_pad "Link to this definition")
>
>     *static* is\_pcb\_via(*inst: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*) → TypeGuard[[PCBVia](#keysight.ads.de.db_uu.PCBVia "keysight.ads.de.db_uu._db_x.PCBVia")][](#keysight.ads.de.db_uu.PCBBase.is_pcb_via "Link to this definition")
>
>     *static* is\_pcb\_via\_or\_pad(*inst: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*) → TypeGuard[[PCBBase](#keysight.ads.de.db_uu.PCBBase "keysight.ads.de.db_uu._db_x.PCBBase")][](#keysight.ads.de.db_uu.PCBBase.is_pcb_via_or_pad "Link to this definition")
>
>     *static* is\_stacked\_pcb\_via(*inst: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")*) → TypeGuard[[StackedPCBVia](#keysight.ads.de.db_uu.StackedPCBVia "keysight.ads.de.db_uu._db_x.StackedPCBVia")][](#keysight.ads.de.db_uu.PCBBase.is_stacked_pcb_via "Link to this definition")
>
>     *property* pad\_via\_type*: [PadViaType](#keysight.ads.de.db_uu.PCBBase.PadViaType "keysight.ads.de._pde.db.PadViaType")*[](#keysight.ads.de.db_uu.PCBBase.pad_via_type "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.PCBPad[](#keysight.ads.de.db_uu.PCBPad "Link to this definition")
> :   Bases: [`PCBBase`](#keysight.ads.de.db_uu.PCBBase "keysight.ads.de.db_uu._db_x.PCBBase")
>
>     Represents a PCB Pad instance in layout.
>
>     The Pad can be a single layer pad, a pad with a specified drill layer,
>     a pad with specified top and bottom layers, or a through pad.
>
>     *property* bottom\_layer*: int*[](#keysight.ads.de.db_uu.PCBPad.bottom_layer "Link to this definition")
>     :   Bottom layer of this pad.
>
>         Will raise an exception if this is not a pad with top and bottom layers.
>
>     *property* drill\_layer*: int*[](#keysight.ads.de.db_uu.PCBPad.drill_layer "Link to this definition")
>     :   Drill layer of this pad.
>
>         Will raise an exception if this is not a pad with drill.
>
>     *property* pad\_layer*: int*[](#keysight.ads.de.db_uu.PCBPad.pad_layer "Link to this definition")
>     :   Layer of this pad.
>
>         Will raise an exception if this is not a single layer pad.
>
>     *property* padstack\_name*: str*[](#keysight.ads.de.db_uu.PCBPad.padstack_name "Link to this definition")
>     :   Name of the padstack template that defines this pad.
>
>         The name will be in the form lib\_name:padstack\_name.
>
>     *property* top\_layer*: int*[](#keysight.ads.de.db_uu.PCBPad.top_layer "Link to this definition")
>     :   Top layer of this pad.
>
>         Will raise an exception if this is not a pad with top and bottom layers.
>
> *class* keysight.ads.de.db\_uu.PCBVia[](#keysight.ads.de.db_uu.PCBVia "Link to this definition")
> :   Bases: [`PCBBase`](#keysight.ads.de.db_uu.PCBBase "keysight.ads.de.db_uu._db_x.PCBBase")
>
>     Represents a PCB Via instance in layout.
>
>     The Via can be specified by rule or with a Padstack template definition
>     and specified layers.
>     Vias with Padstack definitions can have a specified drill layer,
>     specified top and bottom layers, or be a through via.
>
>     *property* bottom\_layer*: int*[](#keysight.ads.de.db_uu.PCBVia.bottom_layer "Link to this definition")
>     :   Bottom layer of this via.
>
>         Will raise an exception if this is not a via with top and bottom layers.
>
>     *property* drill\_layer*: int*[](#keysight.ads.de.db_uu.PCBVia.drill_layer "Link to this definition")
>     :   Drill layer of this via.
>
>         Will raise an exception if this is not a via with drill.
>
>     *property* padstack\_name*: str*[](#keysight.ads.de.db_uu.PCBVia.padstack_name "Link to this definition")
>     :   Name of the padstack template that defines this via.
>
>         The name will be in the form lib\_name:padstack\_name.
>         This will be empty if the via was defined by a rule.
>
>     *property* rule\_name*: str*[](#keysight.ads.de.db_uu.PCBVia.rule_name "Link to this definition")
>     :   Name of the via rule that defines this via.
>
>         The name will be in the form lib\_name:rule\_name.
>         This will be empty if the via was not defined by a rule.
>
>     *property* top\_layer*: int*[](#keysight.ads.de.db_uu.PCBVia.top_layer "Link to this definition")
>     :   Top layer of this via.
>
>         Will raise an exception if this is not a via with top and bottom layers.
>
> *class* keysight.ads.de.db\_uu.Pin[](#keysight.ads.de.db_uu.Pin "Link to this definition")
> :   Bases: [`BlockObject`](#keysight.ads.de.db_uu.BlockObject "keysight.ads.de.db_uu._db_x.BlockObject")
>
>     Represents the physical connection between a terminal and a net.
>
>     \_\_init\_\_(*term: [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")*, *pin\_figs: [PinFig](#keysight.ads.de.db_uu.PinFig "keysight.ads.de.db_uu._db_x.PinFig")*, *\**, *angle: float = 0.0*) → None[](#keysight.ads.de.db_uu.Pin.__init__ "Link to this definition")
>
>     \_\_init\_\_(*term: [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")*, *pin\_figs: list[[PinFig](#keysight.ads.de.db_uu.PinFig "keysight.ads.de.db_uu._db_x.PinFig")]*, *\**, *angle: float = 0.0*) → None
>
>     add\_label(*label: str*, *pt: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → [AttrDisplay](#keysight.ads.de.db_uu.AttrDisplay "keysight.ads.de.db_uu._db_x.AttrDisplay")[](#keysight.ads.de.db_uu.Pin.add_label "Link to this definition")
>
>     *property* angle*: float*[](#keysight.ads.de.db_uu.Pin.angle "Link to this definition")
>
>     find\_first\_wire\_label() → [AttrDisplay](#keysight.ads.de.db_uu.AttrDisplay "keysight.ads.de.db_uu._db_x.AttrDisplay") | None[](#keysight.ads.de.db_uu.Pin.find_first_wire_label "Link to this definition")
>
>     get\_pin\_artifact\_bbox\_only() → [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")[](#keysight.ads.de.db_uu.Pin.get_pin_artifact_bbox_only "Link to this definition")
>
>     get\_pinfig\_bbox() → [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")[](#keysight.ads.de.db_uu.Pin.get_pinfig_bbox "Link to this definition")
>
>     get\_pinfig\_bbox\_with\_artifact() → [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")[](#keysight.ads.de.db_uu.Pin.get_pinfig_bbox_with_artifact "Link to this definition")
>
>     get\_primary\_pin\_fig() → [PinFig](#keysight.ads.de.db_uu.PinFig "keysight.ads.de.db_uu._db_x.PinFig") | None[](#keysight.ads.de.db_uu.Pin.get_primary_pin_fig "Link to this definition")
>
>     *property* has\_any\_pinfigs*: bool*[](#keysight.ads.de.db_uu.Pin.has_any_pinfigs "Link to this definition")
>
>     *property* name*: str*[](#keysight.ads.de.db_uu.Pin.name "Link to this definition")
>
>     *property* needs\_drawing\_artifact*: bool*[](#keysight.ads.de.db_uu.Pin.needs_drawing_artifact "Link to this definition")
>
>     *property* net*: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*[](#keysight.ads.de.db_uu.Pin.net "Link to this definition")
>
>     *property* snap\_point*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db_uu.Pin.snap_point "Link to this definition")
>
>     *property* term*: [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")*[](#keysight.ads.de.db_uu.Pin.term "Link to this definition")
>
>     *property* term\_name*: str*[](#keysight.ads.de.db_uu.Pin.term_name "Link to this definition")
>
>     *property* term\_number*: int*[](#keysight.ads.de.db_uu.Pin.term_number "Link to this definition")
>
>     update\_pin\_annotation(*preserve\_origin: bool = True*) → None[](#keysight.ads.de.db_uu.Pin.update_pin_annotation "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.PinFig[](#keysight.ads.de.db_uu.PinFig "Link to this definition")
> :   Bases: [`Fig`](#keysight.ads.de.db_uu.Fig "keysight.ads.de.db_uu._db_x.Fig")
>
>     Base class for all figures that can represent pins (instances, shapes and vias).
>
>     add\_to\_pin(*pin: [Pin](#keysight.ads.de.db_uu.Pin "keysight.ads.de.db_uu._db_x.Pin")*) → None[](#keysight.ads.de.db_uu.PinFig.add_to_pin "Link to this definition")
>
>     *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db_uu.PinFig.bbox "Link to this definition")
>
>     find\_first\_wire\_label() → [AttrDisplay](#keysight.ads.de.db_uu.AttrDisplay "keysight.ads.de.db_uu._db_x.AttrDisplay") | None[](#keysight.ads.de.db_uu.PinFig.find_first_wire_label "Link to this definition")
>
>     *property* net*: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net") | None*[](#keysight.ads.de.db_uu.PinFig.net "Link to this definition")
>
>     *property* pin*: [Pin](#keysight.ads.de.db_uu.Pin "keysight.ads.de.db_uu._db_x.Pin") | None*[](#keysight.ads.de.db_uu.PinFig.pin "Link to this definition")
>
>     remove\_from\_pin() → None[](#keysight.ads.de.db_uu.PinFig.remove_from_pin "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.PinIter[](#keysight.ads.de.db_uu.PinIter "Link to this definition")
> :   \_\_init\_\_(*obj: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design") | [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net") | [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")*) → None[](#keysight.ads.de.db_uu.PinIter.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.Plane[](#keysight.ads.de.db_uu.Plane "Link to this definition")
> :   Bases: [`CompositeObject`](#keysight.ads.de.db_uu.CompositeObject "keysight.ads.de.db_uu._db_x.CompositeObject")
>
>     A plane is a large shape (composite) on a single net.
>
>     The layer is usually a conductor (e.g. copper). The net is often ground or power.
>
>     copy\_original\_polygon() → [GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")[](#keysight.ads.de.db_uu.Plane.copy_original_polygon "Link to this definition")
>     :   Get a copy of the original polygon that defines the plane.
>
>         Modifications made to the returned polygon won’t affect this Plane.
>
>     copy\_plane\_info() → [PlaneInfo](#keysight.ads.de.db_uu.PlaneInfo "keysight.ads.de.db_uu._db_x.PlaneInfo")[](#keysight.ads.de.db_uu.Plane.copy_plane_info "Link to this definition")
>     :   Get a copy of the information used to build this plane.
>
>         Modifications made to the returned PlaneInfo won’t affect this Plane.
>
>     *static* rebuild\_plane(*plane: [Plane](#keysight.ads.de.db_uu.Plane "keysight.ads.de.db_uu._db_x.Plane")*) → [Plane](#keysight.ads.de.db_uu.Plane "keysight.ads.de.db_uu._db_x.Plane")[](#keysight.ads.de.db_uu.Plane.rebuild_plane "Link to this definition")
>     :   Rebuild the plane using the current PlaneInfo and polygon.
>
>         The original plane will be deleted and the return value will be the new plane.
>
>     set\_plane\_info(*plane\_info: [PlaneInfo](#keysight.ads.de.db_uu.PlaneInfo "keysight.ads.de.db_uu._db_x.PlaneInfo")*) → None[](#keysight.ads.de.db_uu.Plane.set_plane_info "Link to this definition")
>     :   Set the information required to rebuild this plane.
>
> *class* keysight.ads.de.db\_uu.PlaneInfo[](#keysight.ads.de.db_uu.PlaneInfo "Link to this definition")
> :   Holds the information required to create/recreate a Plane.
>
>     *class* DegasOptions[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions "Link to this definition")
>     :   Options for degassing a plane.
>
>         *class* VentShape[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape "Link to this definition")
>         :   Describes the shape of the perforations used for venting a Plane.
>
>             Members:
>
>             > INVALID : ‘Invalid’: This vent shape is not specified.
>             >
>             > RECTANGLE : ‘Rectangle: The vent shape is a rectangle.
>             >
>             > SQUARE : ‘Square: The vent shape is a square.
>             >
>             > CIRCLE : ‘Circle: The vent shape is a circle.
>             >
>             > OCTAGON : ‘Octagon: The vent shape is an octagon.
>
>             CIRCLE *= <VentShape.CIRCLE: 2>*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape.CIRCLE "Link to this definition")
>
>             INVALID *= <VentShape.INVALID: -1>*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape.INVALID "Link to this definition")
>
>             OCTAGON *= <VentShape.OCTAGON: 3>*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape.OCTAGON "Link to this definition")
>
>             RECTANGLE *= <VentShape.RECTANGLE: 0>*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape.RECTANGLE "Link to this definition")
>
>             SQUARE *= <VentShape.SQUARE: 1>*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape.SQUARE "Link to this definition")
>
>             \_\_init\_\_(*self: [keysight.ads.de.\_pde.db.DegasOptions.VentShape](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape "keysight.ads.de._pde.db.DegasOptions.VentShape")*, *value: int*) → None[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape.__init__ "Link to this definition")
>
>             *property* name[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape.name "Link to this definition")
>
>             *property* str[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape.str "Link to this definition")
>             :   Return the string representation of the vent shape.
>
>             *property* value[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape.value "Link to this definition")
>
>         *class* VentStartingPosition[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentStartingPosition "Link to this definition")
>         :   Describes the location of the initial perforation when venting a plane.
>
>             Members:
>
>             > LOWER\_LEFT : ‘LowerLeft’: Start from the lower left of the bounding box.
>             >
>             > LOWER\_RIGHT : ‘LowerRight’: Start from the lower right of the bounding box.
>             >
>             > UPPER\_LEFT : ‘UpperLeft’: Start from the upper left of the bounding box.
>             >
>             > UPPER\_RIGHT : ‘UpperRight’: Start from the upper right of the bounding box.
>
>             LOWER\_LEFT *= <VentStartingPosition.LOWER\_LEFT: 0>*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentStartingPosition.LOWER_LEFT "Link to this definition")
>
>             LOWER\_RIGHT *= <VentStartingPosition.LOWER\_RIGHT: 1>*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentStartingPosition.LOWER_RIGHT "Link to this definition")
>
>             UPPER\_LEFT *= <VentStartingPosition.UPPER\_LEFT: 2>*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentStartingPosition.UPPER_LEFT "Link to this definition")
>
>             UPPER\_RIGHT *= <VentStartingPosition.UPPER\_RIGHT: 3>*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentStartingPosition.UPPER_RIGHT "Link to this definition")
>
>             \_\_init\_\_(*self: [keysight.ads.de.\_pde.db.DegasOptions.VentStartingPosition](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentStartingPosition "keysight.ads.de._pde.db.DegasOptions.VentStartingPosition")*, *value: int*) → None[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentStartingPosition.__init__ "Link to this definition")
>
>             *property* name[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentStartingPosition.name "Link to this definition")
>
>             *property* str[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentStartingPosition.str "Link to this definition")
>             :   Return the string representation of the vent starting position.
>
>             *property* value[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentStartingPosition.value "Link to this definition")
>
>         \_\_init\_\_(*plane\_or\_design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.__init__ "Link to this definition")
>
>         \_\_init\_\_(*plane\_or\_design: [PlaneInfo](#keysight.ads.de.db_uu.PlaneInfo "keysight.ads.de.db_uu._db_x.PlaneInfo")*) → None
>
>         *property* min\_edge\_distance*: float*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.min_edge_distance "Link to this definition")
>         :   The minimum clearance between a perforation and any clearance or edge.
>
>         *property* min\_venting\_area*: float*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.min_venting_area "Link to this definition")
>         :   The minimum area of a plane shape that will be considered for perforation.
>
>         *property* pitch\_height*: float*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.pitch_height "Link to this definition")
>         :   Specifies vertical separation between the center points of the venting holes.
>
>         *property* pitch\_width*: float*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.pitch_width "Link to this definition")
>         :   Specifies horizontal separation between the center points of the venting holes.
>
>         same\_props(*other: [DegasOptions](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions "keysight.ads.de.db_uu._db_x.PlaneInfo.DegasOptions")*) → bool[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.same_props "Link to this definition")
>         :   Determine if the essential properties are the same.
>
>             This is not the same as equality because properties that are not enabled are ignored.
>
>         *property* starting\_offset\_x*: float*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.starting_offset_x "Link to this definition")
>         :   The horizontal spacing from the starting position to the initial perforation.
>
>         *property* starting\_offset\_y*: float*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.starting_offset_y "Link to this definition")
>         :   The vertical spacing from the starting position to the initial perforation.
>
>         *property* vent\_shape*: [VentShape](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentShape "keysight.ads.de._pde.db.DegasOptions.VentShape")*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.vent_shape "Link to this definition")
>         :   Specifies the shape of the degassing holes.
>
>         *property* vent\_shape\_height*: float*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.vent_shape_height "Link to this definition")
>         :   Specifies the height of the vent shape.
>
>             For Square, Circle and Octagon, this is ignored.
>
>         *property* vent\_shape\_width*: float*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.vent_shape_width "Link to this definition")
>         :   Specifies the width of the vent shape.
>
>             For Square, Circle and Octagon, only the width is used.
>
>         *property* vent\_starting\_position*: [VentStartingPosition](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.VentStartingPosition "keysight.ads.de._pde.db.DegasOptions.VentStartingPosition")*[](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions.vent_starting_position "Link to this definition")
>         :   Describes the location of the initial perforation.
>
>     *class* RemoveIslandsMode[](#keysight.ads.de.db_uu.PlaneInfo.RemoveIslandsMode "Link to this definition")
>     :   Describes island removal.
>
>         Members:
>
>         > REMOVE\_NONE : ‘RemoveNone’: Does not remove any islands.
>         >
>         > REMOVE\_ALL : ‘RemoveAll: Removes all islands.
>         >
>         > REMOVE\_BY\_AREA : ‘RemoveByArea’: Removes islands whose area is less than the min\_island\_area.
>
>         REMOVE\_ALL *= <RemoveIslandsMode.REMOVE\_ALL: 1>*[](#keysight.ads.de.db_uu.PlaneInfo.RemoveIslandsMode.REMOVE_ALL "Link to this definition")
>
>         REMOVE\_BY\_AREA *= <RemoveIslandsMode.REMOVE\_BY\_AREA: 2>*[](#keysight.ads.de.db_uu.PlaneInfo.RemoveIslandsMode.REMOVE_BY_AREA "Link to this definition")
>
>         REMOVE\_NONE *= <RemoveIslandsMode.REMOVE\_NONE: 0>*[](#keysight.ads.de.db_uu.PlaneInfo.RemoveIslandsMode.REMOVE_NONE "Link to this definition")
>
>         \_\_init\_\_(*self: [keysight.ads.de.\_pde.db.PlaneInfo.RemoveIslandsMode](#keysight.ads.de.db_uu.PlaneInfo.RemoveIslandsMode "keysight.ads.de._pde.db.PlaneInfo.RemoveIslandsMode")*, *value: int*) → None[](#keysight.ads.de.db_uu.PlaneInfo.RemoveIslandsMode.__init__ "Link to this definition")
>
>         *property* name[](#keysight.ads.de.db_uu.PlaneInfo.RemoveIslandsMode.name "Link to this definition")
>
>         *property* str[](#keysight.ads.de.db_uu.PlaneInfo.RemoveIslandsMode.str "Link to this definition")
>         :   Return the string representation of the RemoveIslandsMode.
>
>         *property* value[](#keysight.ads.de.db_uu.PlaneInfo.RemoveIslandsMode.value "Link to this definition")
>
>     \_\_init\_\_(*plane\_or\_design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.PlaneInfo.__init__ "Link to this definition")
>
>     \_\_init\_\_(*plane\_or\_design: [Plane](#keysight.ads.de.db_uu.Plane "keysight.ads.de.db_uu._db_x.Plane")*) → None
>
>     *property* clearance*: float*[](#keysight.ads.de.db_uu.PlaneInfo.clearance "Link to this definition")
>     :   Defines the minimum distance between a plane and an object from a different net.
>
>         This is ignored if using clearance rules (use\_clearance\_rules is True).
>
>     *property* degas\_options*: [DegasOptions](#keysight.ads.de.db_uu.PlaneInfo.DegasOptions "keysight.ads.de.db_uu.PlaneInfo.DegasOptions")*[](#keysight.ads.de.db_uu.PlaneInfo.degas_options "Link to this definition")
>
>     *property* degassing\_enabled*: bool*[](#keysight.ads.de.db_uu.PlaneInfo.degassing_enabled "Link to this definition")
>     :   If True, perforate the plane with rows and columns of holes (using the degas\_options).
>
>     *property* layer\_id*: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*[](#keysight.ads.de.db_uu.PlaneInfo.layer_id "Link to this definition")
>     :   Specifies the layer and purpose of the Plane’s shapes.
>
>     *property* min\_feature\_width*: float*[](#keysight.ads.de.db_uu.PlaneInfo.min_feature_width "Link to this definition")
>     :   Specifies the minimum width of a feature or notch that gets preserved when smoothing.
>
>     *property* min\_island\_area*: float*[](#keysight.ads.de.db_uu.PlaneInfo.min_island_area "Link to this definition")
>     :   Specifies the minimum area of an island that gets preserved when removing islands by area.
>
>     *property* net\_name*: str*[](#keysight.ads.de.db_uu.PlaneInfo.net_name "Link to this definition")
>     :   The name of the Plane’s net.
>
>     *property* remove\_islands\_mode*: [RemoveIslandsMode](#keysight.ads.de.db_uu.PlaneInfo.RemoveIslandsMode "keysight.ads.de._pde.db.PlaneInfo.RemoveIslandsMode")*[](#keysight.ads.de.db_uu.PlaneInfo.remove_islands_mode "Link to this definition")
>     :   Determines how unconnected islands within the Plane’s outline get removed.
>
>     same\_props(*other: [PlaneInfo](#keysight.ads.de.db_uu.PlaneInfo "keysight.ads.de.db_uu._db_x.PlaneInfo")*) → bool[](#keysight.ads.de.db_uu.PlaneInfo.same_props "Link to this definition")
>     :   Determine if the essential properties are the same.
>
>         This is not the same as equality because properties that are not enabled are ignored.
>
>     *property* smoothing\_enabled*: bool*[](#keysight.ads.de.db_uu.PlaneInfo.smoothing_enabled "Link to this definition")
>     :   If True, the Plane’s outline gets smoothed, possibly removing small features and rounding corners.
>
>     *property* thermal\_relief\_enabled*: bool*[](#keysight.ads.de.db_uu.PlaneInfo.thermal_relief_enabled "Link to this definition")
>     :   Insert thermal straps (using thermal\_straps\_width) to avoid overheating.
>
>     *property* thermal\_straps\_width*: float*[](#keysight.ads.de.db_uu.PlaneInfo.thermal_straps_width "Link to this definition")
>     :   Specifies the width of thermal straps.
>
>     *property* use\_clearance\_rules*: bool*[](#keysight.ads.de.db_uu.PlaneInfo.use_clearance_rules "Link to this definition")
>     :   If True, use the clearance rules defined in the Constraints Manager and ignore the clearance property.
>
>     *property* use\_round\_corners\_when\_smoothing*: bool*[](#keysight.ads.de.db_uu.PlaneInfo.use_round_corners_when_smoothing "Link to this definition")
>     :   If True, round corners created when features are removed by smoothing. Otherwise bevel the corners.
>
>     *property* use\_rounded\_clearance*: bool*[](#keysight.ads.de.db_uu.PlaneInfo.use_rounded_clearance "Link to this definition")
>     :   Use rounded corners when creating clearance around objects with sharp corners.
>
> *class* keysight.ads.de.db\_uu.Polygon[](#keysight.ads.de.db_uu.Polygon "Link to this definition")
> :   Bases: [`Shape`](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *polygon: [GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")*, *arc\_resolution: float = 5.0*) → None[](#keysight.ads.de.db_uu.Polygon.__init__ "Link to this definition")
>
>     get\_centerline(*allow\_arcs: bool = True*) → [GenPolyline](../db/genpolyline.md#keysight.ads.de.db.GenPolyline "keysight.ads.de.db._genpolyline.GenPolyline")[](#keysight.ads.de.db_uu.Polygon.get_centerline "Link to this definition")
>     :   Return a copy of the centerline of this polygon.
>
>     *property* interconnect\_info*: [InterconnectInfo](#keysight.ads.de.db_uu.InterconnectInfo "keysight.ads.de.db_uu.InterconnectInfo")*[](#keysight.ads.de.db_uu.Polygon.interconnect_info "Link to this definition")
>     :   Return a reference to the cached copy of the InterconnectInfo for this Polygon.
>
> *class* keysight.ads.de.db\_uu.PropDisplay[](#keysight.ads.de.db_uu.PropDisplay "Link to this definition")
> :   Bases: [`TextDisplay`](#keysight.ads.de.db_uu.TextDisplay "keysight.ads.de.db_uu._db_x.TextDisplay")
>
>     Display object that displays a property value.
>
>     *property* prop*: [Property](../db/properties.md#keysight.ads.de.db.Property "keysight.ads.de.db.Property")*[](#keysight.ads.de.db_uu.PropDisplay.prop "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.Rect[](#keysight.ads.de.db_uu.Rect "Link to this definition")
> :   Bases: [`Shape`](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *ll\_or\_box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → None[](#keysight.ads.de.db_uu.Rect.__init__ "Link to this definition")
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *ll\_or\_box: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *ur: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*) → None
>
> *class* keysight.ads.de.db\_uu.Ref[](#keysight.ads.de.db_uu.Ref "Link to this definition")
> :   Bases: [`PinFig`](#keysight.ads.de.db_uu.PinFig "keysight.ads.de.db_uu._db_x.PinFig")
>
>     Base class for all instances and vias.
>
>     \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db_uu.Ref.__init__ "Link to this definition")
>     :   Return an error about attempts to initialize objects that don’t support initialization.
>
>     get\_placement\_transform() → [Transform](../db/genpolyline.md#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")[](#keysight.ads.de.db_uu.Ref.get_placement_transform "Link to this definition")
>
>     *property* is\_bound*: bool*[](#keysight.ads.de.db_uu.Ref.is_bound "Link to this definition")
>
>     *property* master*: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design") | None*[](#keysight.ads.de.db_uu.Ref.master "Link to this definition")
>
>     *property* orient*: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*[](#keysight.ads.de.db_uu.Ref.orient "Link to this definition")
>
>     *property* origin*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db_uu.Ref.origin "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.RefIter[](#keysight.ads.de.db_uu.RefIter "Link to this definition")
> :   \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.RefIter.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.ScalarInst[](#keysight.ads.de.db_uu.ScalarInst "Link to this definition")
> :   Bases: [`Instance`](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")
>
> *class* keysight.ads.de.db\_uu.ScalarNet[](#keysight.ads.de.db_uu.ScalarNet "Link to this definition")
> :   Bases: [`Net`](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")
>
>     A scalar net without bus-name syntax.
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *name: str | None = None*) → None[](#keysight.ads.de.db_uu.ScalarNet.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.ScalarTerm[](#keysight.ads.de.db_uu.ScalarTerm "Link to this definition")
> :   Bases: [`Term`](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")
>
>     \_\_init\_\_(*net: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*, *name: str*, *term\_type: [TermType](../db/enums.md#keysight.ads.de.db.TermType "keysight.ads.de.db._db_types.TermType") = TermType.INPUT\_OUTPUT*, *\**, *number: int = 0*) → None[](#keysight.ads.de.db_uu.ScalarTerm.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.SelectedObjectIter[](#keysight.ads.de.db_uu.SelectedObjectIter "Link to this definition")
> :   Bases: `object`
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.SelectedObjectIter.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.Shape[](#keysight.ads.de.db_uu.Shape "Link to this definition")
> :   Bases: [`PinFig`](#keysight.ads.de.db_uu.PinFig "keysight.ads.de.db_uu._db_x.PinFig")
>
>     Base class for shapes in a design.
>
>     \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db_uu.Shape.__init__ "Link to this definition")
>     :   Return an error about attempts to initialize objects that don’t support initialization.
>
>     get\_gen\_polygon() → [GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")[](#keysight.ads.de.db_uu.Shape.get_gen_polygon "Link to this definition")
>
>     get\_gen\_polygon\_without\_arcs() → [GenPolygonWithHoles](../db/genpolyline.md#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")[](#keysight.ads.de.db_uu.Shape.get_gen_polygon_without_arcs "Link to this definition")
>
>     get\_outline() → [Outline](../db/genpolyline.md#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline")[](#keysight.ads.de.db_uu.Shape.get_outline "Link to this definition")
>
>     *property* is\_closed*: bool*[](#keysight.ads.de.db_uu.Shape.is_closed "Link to this definition")
>
>     *property* is\_filled*: bool*[](#keysight.ads.de.db_uu.Shape.is_filled "Link to this definition")
>
>     *property* layer*: int*[](#keysight.ads.de.db_uu.Shape.layer "Link to this definition")
>
>     *property* layer\_id*: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*[](#keysight.ads.de.db_uu.Shape.layer_id "Link to this definition")
>
>     *property* legacy\_border\_thickness*: float | [LineThickness](#keysight.ads.de.db_uu.LineThickness "keysight.ads.de.db_uu._db_x.LineThickness")*[](#keysight.ads.de.db_uu.Shape.legacy_border_thickness "Link to this definition")
>
>     *property* purpose*: int*[](#keysight.ads.de.db_uu.Shape.purpose "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.ShapeIter[](#keysight.ads.de.db_uu.ShapeIter "Link to this definition")
> :   \_\_init\_\_(*obj: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*)[](#keysight.ads.de.db_uu.ShapeIter.__init__ "Link to this definition")
>
>     \_\_init\_\_(*obj: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *layerid\_or\_net\_option: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*)
>
>     \_\_init\_\_(*obj: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*, *layerid\_or\_net\_option: [ShapeIterNetOption](#keysight.ads.de.db_uu.ShapeIterNetOption "keysight.ads.de.db_uu._db_x.ShapeIterNetOption")*)
>
>     *property* design*: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*[](#keysight.ads.de.db_uu.ShapeIter.design "Link to this definition")
>
>     exclude\_invisible\_layers() → None[](#keysight.ads.de.db_uu.ShapeIter.exclude_invisible_layers "Link to this definition")
>
>     exclude\_protected\_layers() → None[](#keysight.ads.de.db_uu.ShapeIter.exclude_protected_layers "Link to this definition")
>
>     include\_annotation() → None[](#keysight.ads.de.db_uu.ShapeIter.include_annotation "Link to this definition")
>
>     include\_invisible\_layers() → None[](#keysight.ads.de.db_uu.ShapeIter.include_invisible_layers "Link to this definition")
>
>     include\_protected\_layers() → None[](#keysight.ads.de.db_uu.ShapeIter.include_protected_layers "Link to this definition")
>
>     *property* is\_pin\_or\_net\_iteration*: bool*[](#keysight.ads.de.db_uu.ShapeIter.is_pin_or_net_iteration "Link to this definition")
>
>     *property* library*: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*[](#keysight.ads.de.db_uu.ShapeIter.library "Link to this definition")
>
>     limit\_layer(*layer: int*) → None[](#keysight.ads.de.db_uu.ShapeIter.limit_layer "Link to this definition")
>
>     limit\_layerid(*layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*) → None[](#keysight.ads.de.db_uu.ShapeIter.limit_layerid "Link to this definition")
>
>     limit\_purpose(*purpose: int*) → None[](#keysight.ads.de.db_uu.ShapeIter.limit_purpose "Link to this definition")
>
>     limit\_region(*region: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*, *option: [LimitRegionOption](#keysight.ads.de.db_uu.LimitRegionOption "keysight.ads.de.db_uu._db_x.LimitRegionOption")*) → None[](#keysight.ads.de.db_uu.ShapeIter.limit_region "Link to this definition")
>
>     limit\_shapes(*option: [ShapeOption](#keysight.ads.de.db_uu.ShapeOption "keysight.ads.de.db_uu._db_x.ShapeOption")*) → None[](#keysight.ads.de.db_uu.ShapeIter.limit_shapes "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.ShapeIterNetOption[](#keysight.ads.de.db_uu.ShapeIterNetOption "Link to this definition")
> :   Bases: `Enum`
>
>     NET\_SHAPES\_ONLY *= <ShapeIterNetOption.NET\_SHAPES\_ONLY: 0>*[](#keysight.ads.de.db_uu.ShapeIterNetOption.NET_SHAPES_ONLY "Link to this definition")
>
>     PIN\_AND\_NET\_SHAPES *= <ShapeIterNetOption.PIN\_AND\_NET\_SHAPES: 1>*[](#keysight.ads.de.db_uu.ShapeIterNetOption.PIN_AND_NET_SHAPES "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.ShapeOption[](#keysight.ads.de.db_uu.ShapeOption "Link to this definition")
> :   Bases: `Enum`
>
>     ALL\_SHAPES *= <ShapeOption.ALL\_SHAPES: 0>*[](#keysight.ads.de.db_uu.ShapeOption.ALL_SHAPES "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.StackedPCBVia[](#keysight.ads.de.db_uu.StackedPCBVia "Link to this definition")
> :   Bases: [`PCBBase`](#keysight.ads.de.db_uu.PCBBase "keysight.ads.de.db_uu._db_x.PCBBase")
>
>     *property* rule\_name*: str*[](#keysight.ads.de.db_uu.StackedPCBVia.rule_name "Link to this definition")
>     :   Name of the via rule that defines this via.
>
>         The name will be in the form lib\_name:rule\_name.
>         This will be empty if the via was not defined by a rule.
>
> *class* keysight.ads.de.db\_uu.StdVia[](#keysight.ads.de.db_uu.StdVia "Link to this definition")
> :   Bases: [`Via`](#keysight.ads.de.db_uu.Via "keysight.ads.de.db_uu._db_x.Via")
>
>     A standard (rectangular) OpenAccess Via.
>
>     The via is completely defined by its definition in the technology.
>
> *class* keysight.ads.de.db\_uu.Term[](#keysight.ads.de.db_uu.Term "Link to this definition")
> :   Bases: [`BlockObject`](#keysight.ads.de.db_uu.BlockObject "keysight.ads.de.db_uu._db_x.BlockObject")
>
>     Terminals represent a logical connection points for a design.
>
>     The pins associated with terminals represent the physical connection points.
>     The nets associated with terminals through the terminals to the parent design.
>
>     When a terminal connects to a multi-bit net, the terminal must have the same
>     number of bits.
>
>     Terminals on a design are associated with InstTerms on an instance of that design.
>     The association is normally done by name, but can be done by number.
>     When terminals connect by number, all terminals on the design must connect by number.
>
>     \_\_init\_\_(*net: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*, *name: str*, *term\_type: [TermType](../db/enums.md#keysight.ads.de.db.TermType "keysight.ads.de.db._db_types.TermType") = TermType.INPUT\_OUTPUT*, *\**, *number: int = 0*) → None[](#keysight.ads.de.db_uu.Term.__init__ "Link to this definition")
>     :   \_\_init\_\_ is deprecated, and will be removed in the 2025 Update 2 release. Use: Term.create
>
>     *static* create(*net: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*, *name: str*, *term\_type: [TermType](../db/enums.md#keysight.ads.de.db.TermType "keysight.ads.de.db._db_types.TermType") = TermType.INPUT\_OUTPUT*, *\**, *number: int = 0*) → [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")[](#keysight.ads.de.db_uu.Term.create "Link to this definition")
>
>     create\_connect\_def(*net\_expression: str*) → None[](#keysight.ads.de.db_uu.Term.create_connect_def "Link to this definition")
>
>     *property* is\_implicit*: bool*[](#keysight.ads.de.db_uu.Term.is_implicit "Link to this definition")
>
>     *property* name*: str*[](#keysight.ads.de.db_uu.Term.name "Link to this definition")
>
>     *property* net*: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*[](#keysight.ads.de.db_uu.Term.net "Link to this definition")
>
>     *property* number*: int*[](#keysight.ads.de.db_uu.Term.number "Link to this definition")
>     :   By default, terminals connect by name and this number is 0.
>
>         If the number is greater than zero, it represents the netlisting order
>         for this terminal.
>
>     *property* parameters*: ParamBaseCollection*[](#keysight.ads.de.db_uu.Term.parameters "Link to this definition")
>
>     *property* pins*: NamedItemCollectionAbc[[Pin](#keysight.ads.de.db_uu.Pin "keysight.ads.de.db_uu._db_x.Pin")]*[](#keysight.ads.de.db_uu.Term.pins "Link to this definition")
>
>     *property* ref\_plane\_shift\_dbu*: float*[](#keysight.ads.de.db_uu.Term.ref_plane_shift_dbu "Link to this definition")
>
>     *property* ref\_plane\_shift\_meters*: float*[](#keysight.ads.de.db_uu.Term.ref_plane_shift_meters "Link to this definition")
>
>     rename\_term(*name: str*) → [Term](#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu._db_x.Term")[](#keysight.ads.de.db_uu.Term.rename_term "Link to this definition")
>
>     *property* term\_type*: [TermType](../db/enums.md#keysight.ads.de.db.TermType "keysight.ads.de.db._db_types.TermType")*[](#keysight.ads.de.db_uu.Term.term_type "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.TermIter[](#keysight.ads.de.db_uu.TermIter "Link to this definition")
> :   \_\_init\_\_(*obj: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design") | [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*) → None[](#keysight.ads.de.db_uu.TermIter.__init__ "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.Text[](#keysight.ads.de.db_uu.Text "Link to this definition")
> :   Bases: [`TextBase`](#keysight.ads.de.db_uu.TextBase "keysight.ads.de.db_uu._db_x.TextBase")
>
>     \_\_init\_\_(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *layer\_id: [LayerId](layer_id.md#keysight.ads.de.db_uu.LayerId "keysight.ads.de.db._layer_id.LayerId")*, *text: str*, *origin: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float]*, *font\_name: str*, *height: float*, *align: [TextAlignment](../db/enums.md#keysight.ads.de.db.TextAlignment "keysight.ads.de.db._db_types.TextAlignment") = TextAlignment.CENTER\_LEFT*, *orient: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation") = Orientation.R0*, *has\_overbar: bool = False*, *is\_visible: bool = True*, *is\_drafting: bool = True*) → None[](#keysight.ads.de.db_uu.Text.__init__ "Link to this definition")
>
>     *property* alignment*: [TextAlignment](../db/enums.md#keysight.ads.de.db.TextAlignment "keysight.ads.de.db._db_types.TextAlignment")*[](#keysight.ads.de.db_uu.Text.alignment "Link to this definition")
>
>     *property* has\_overbar*: bool*[](#keysight.ads.de.db_uu.Text.has_overbar "Link to this definition")
>
>     *property* is\_drafting*: bool*[](#keysight.ads.de.db_uu.Text.is_drafting "Link to this definition")
>
>     *property* is\_visible*: bool*[](#keysight.ads.de.db_uu.Text.is_visible "Link to this definition")
>
>     *property* orientation*: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*[](#keysight.ads.de.db_uu.Text.orientation "Link to this definition")
>
>     *property* text\_string*: str*[](#keysight.ads.de.db_uu.Text.text_string "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.TextAttributes[](#keysight.ads.de.db_uu.TextAttributes "Link to this definition")
> :   \_\_init\_\_() → None[](#keysight.ads.de.db_uu.TextAttributes.__init__ "Link to this definition")
>
>     \_\_init\_\_(*design\_or\_text: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None
>
>     \_\_init\_\_(*design\_or\_text: [Text](#keysight.ads.de.db_uu.Text "keysight.ads.de.db_uu._db_x.Text")*) → None
>
>     *property* alignment*: [TextAlignment](../db/enums.md#keysight.ads.de.db.TextAlignment "keysight.ads.de.db._db_types.TextAlignment")*[](#keysight.ads.de.db_uu.TextAttributes.alignment "Link to this definition")
>
>     *property* font\_name*: str*[](#keysight.ads.de.db_uu.TextAttributes.font_name "Link to this definition")
>
>     *property* has\_overbar*: bool*[](#keysight.ads.de.db_uu.TextAttributes.has_overbar "Link to this definition")
>
>     *property* height\_dbu*: int*[](#keysight.ads.de.db_uu.TextAttributes.height_dbu "Link to this definition")
>
>     *property* is\_drafting*: bool*[](#keysight.ads.de.db_uu.TextAttributes.is_drafting "Link to this definition")
>
>     *property* is\_visible*: bool*[](#keysight.ads.de.db_uu.TextAttributes.is_visible "Link to this definition")
>
>     *property* orientation*: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*[](#keysight.ads.de.db_uu.TextAttributes.orientation "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.TextBase[](#keysight.ads.de.db_uu.TextBase "Link to this definition")
> :   Bases: [`Shape`](#keysight.ads.de.db_uu.Shape "keysight.ads.de.db_uu._db_x.Shape")
>
>     Base class for text shapes in a design.
>
>     *property* font\_name*: str*[](#keysight.ads.de.db_uu.TextBase.font_name "Link to this definition")
>
>     *property* text\_height*: float*[](#keysight.ads.de.db_uu.TextBase.text_height "Link to this definition")
>
>     *property* text\_origin*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db_uu.TextBase.text_origin "Link to this definition")
>
>     *property* text\_string*: str*[](#keysight.ads.de.db_uu.TextBase.text_string "Link to this definition")
>
>     *property* unevaluated\_text*: str*[](#keysight.ads.de.db_uu.TextBase.unevaluated_text "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.TextDisplay[](#keysight.ads.de.db_uu.TextDisplay "Link to this definition")
> :   Bases: [`TextBase`](#keysight.ads.de.db_uu.TextBase "keysight.ads.de.db_uu._db_x.TextBase")
>
>     Base class for all types of text display objects.
>
>     *property* alignment*: [TextAlignment](../db/enums.md#keysight.ads.de.db.TextAlignment "keysight.ads.de.db._db_types.TextAlignment")*[](#keysight.ads.de.db_uu.TextDisplay.alignment "Link to this definition")
>
>     *property* format*: [TextDisplayFormat](../db/enums.md#keysight.ads.de.db.TextDisplayFormat "keysight.ads.de.db._db_types.TextDisplayFormat")*[](#keysight.ads.de.db_uu.TextDisplay.format "Link to this definition")
>
>     *property* has\_overbar*: bool*[](#keysight.ads.de.db_uu.TextDisplay.has_overbar "Link to this definition")
>
>     *property* is\_drafting*: bool*[](#keysight.ads.de.db_uu.TextDisplay.is_drafting "Link to this definition")
>
>     *property* is\_visible*: bool*[](#keysight.ads.de.db_uu.TextDisplay.is_visible "Link to this definition")
>
>     *property* orientation*: [Orientation](../db/enums.md#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*[](#keysight.ads.de.db_uu.TextDisplay.orientation "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.TextOverride[](#keysight.ads.de.db_uu.TextOverride "Link to this definition")
> :   Bases: [`TextDisplay`](#keysight.ads.de.db_uu.TextDisplay "keysight.ads.de.db_uu._db_x.TextDisplay")
>
>     A text object that supports overriding text from an instance master.
>
> *class* keysight.ads.de.db\_uu.VectorInst[](#keysight.ads.de.db_uu.VectorInst "Link to this definition")
> :   Bases: [`Instance`](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")
>
>     *property* bits*: IndexedReadableCollectionAbc[[Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")]*[](#keysight.ads.de.db_uu.VectorInst.bits "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.VectorInstBit[](#keysight.ads.de.db_uu.VectorInstBit "Link to this definition")
> :   Bases: [`Instance`](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu._db_x.Instance")
>
> *class* keysight.ads.de.db\_uu.Via[](#keysight.ads.de.db_uu.Via "Link to this definition")
> :   Bases: [`Ref`](#keysight.ads.de.db_uu.Ref "keysight.ads.de.db_uu._db_x.Ref")
>
>     Base class for OpenAccess Vias.
>
>     A via represents a physical connection between traces (also PathSegs and Rountes)
>     that are on two different layers. Vias are defined by a definition in the technology.
>
>     *property* name*: str*[](#keysight.ads.de.db_uu.Via.name "Link to this definition")
>     :   The name from the via definition in the technology.
>
> *class* keysight.ads.de.db\_uu.ViaElement[](#keysight.ads.de.db_uu.ViaElement "Link to this definition")
> :   \_\_init\_\_() → None[](#keysight.ads.de.db_uu.ViaElement.__init__ "Link to this definition")
>
>     add\_via\_name(*name: str*) → None[](#keysight.ads.de.db_uu.ViaElement.add_via_name "Link to this definition")
>
>     add\_via\_names(*names: Sequence[str]*) → None[](#keysight.ads.de.db_uu.ViaElement.add_via_names "Link to this definition")
>
>     clear\_vias() → None[](#keysight.ads.de.db_uu.ViaElement.clear_vias "Link to this definition")
>
>     *property* is\_empty*: bool*[](#keysight.ads.de.db_uu.ViaElement.is_empty "Link to this definition")
>
>     *property* via\_names*: list[str]*[](#keysight.ads.de.db_uu.ViaElement.via_names "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.ViaIter[](#keysight.ads.de.db_uu.ViaIter "Link to this definition")
> :   \_\_init\_\_(*obj: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.ViaIter.__init__ "Link to this definition")
>
>     \_\_init\_\_(*obj: [Net](#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu._db_x.Net")*, *options: [ViaIterNetOptions](#keysight.ads.de.db_uu.ViaIterNetOptions "keysight.ads.de.db_uu._db_x.ViaIterNetOptions")*) → None

## Enumerated Types[](#enumerated-types "Link to this heading")

> *class* keysight.ads.de.db\_uu.LimitRegionOption[](#keysight.ads.de.db_uu.LimitRegionOption "Link to this definition")
> :   Bases: `Enum`
>
>     REGION\_MUST\_TOUCH\_ACTUAL\_OBJECT *= <LimitRegionOption.REGION\_MUST\_TOUCH\_ACTUAL\_OBJECT: 1>*[](#keysight.ads.de.db_uu.LimitRegionOption.REGION_MUST_TOUCH_ACTUAL_OBJECT "Link to this definition")
>
>     REGION\_MUST\_TOUCH\_OBJECT\_EDGE *= <LimitRegionOption.REGION\_MUST\_TOUCH\_OBJECT\_EDGE: 2>*[](#keysight.ads.de.db_uu.LimitRegionOption.REGION_MUST_TOUCH_OBJECT_EDGE "Link to this definition")
>
>     REGION\_MUST\_CONTAIN\_OBJECT *= <LimitRegionOption.REGION\_MUST\_CONTAIN\_OBJECT: 0>*[](#keysight.ads.de.db_uu.LimitRegionOption.REGION_MUST_CONTAIN_OBJECT "Link to this definition")
>
>     REGION\_MAY\_TOUCH\_ONLY\_BOUNDING\_BOX *= <LimitRegionOption.REGION\_MAY\_TOUCH\_ONLY\_BOUNDING\_BOX: 3>*[](#keysight.ads.de.db_uu.LimitRegionOption.REGION_MAY_TOUCH_ONLY_BOUNDING_BOX "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.LineThickness[](#keysight.ads.de.db_uu.LineThickness "Link to this definition")
> :   Bases: `Enum`
>
>     THIN *= <LineThickness.THIN: 1>*[](#keysight.ads.de.db_uu.LineThickness.THIN "Link to this definition")
>
>     MEDIUM *= <LineThickness.THICK: 2>*[](#keysight.ads.de.db_uu.LineThickness.MEDIUM "Link to this definition")
>
>     THICK *= <LineThickness.THICKER: 3>*[](#keysight.ads.de.db_uu.LineThickness.THICK "Link to this definition")
>
> *class* keysight.ads.de.db\_uu.ViaIterNetOptions[](#keysight.ads.de.db_uu.ViaIterNetOptions "Link to this definition")
> :   Bases: `Enum`
>
>     NET\_VIAS\_ONLY *= <ViaIterNetOptions.NET\_VIAS\_ONLY: 0>*[](#keysight.ads.de.db_uu.ViaIterNetOptions.NET_VIAS_ONLY "Link to this definition")
>
>     PIN\_AND\_NET\_VIAS *= <ViaIterNetOptions.PIN\_AND\_NET\_VIAS: 1>*[](#keysight.ads.de.db_uu.ViaIterNetOptions.PIN_AND_NET_VIAS "Link to this definition")

## Functions[](#functions "Link to this heading")

> keysight.ads.de.db\_uu.copy\_design(*source: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *destination: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*) → None[](#keysight.ads.de.db_uu.copy_design "Link to this definition")
>
> keysight.ads.de.db\_uu.create\_layout(*name: CellviewRefLike*) → [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")[](#keysight.ads.de.db_uu.create_layout "Link to this definition")
> :   Create a layout from an open library in the active workspace.
>
>     Parameters:
>     :   **name** (*CellviewRefLike*) – The name of the design, usually of the form “LibraryName:CellName:layout”
>
>     Example
>
>     ```
>     >>> design = de.db_uu.create_layout(name=("test_lib", "test_2", "layout"))
>     ```
>
> keysight.ads.de.db\_uu.create\_schematic(*name: CellviewRefLike*) → [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")[](#keysight.ads.de.db_uu.create_schematic "Link to this definition")
> :   Create a schematic from an open library in the active workspace.
>
>     Parameters:
>     :   **name** (*CellviewRefLike*) – The name of the design, usually of the form “LibraryName:CellName:schematic”
>
>     Example
>
>     ```
>     >>> design = de.db_uu.create_layout(name=("test_lib", "test_1", "schematic"))
>     ```
>
> keysight.ads.de.db\_uu.create\_symbol(*name: CellviewRefLike*) → [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")[](#keysight.ads.de.db_uu.create_symbol "Link to this definition")
> :   Create a symbol from an open library in the active workspace.
>
>     Parameters:
>     :   **name** (*CellviewRefLike*) – The name of the design, usually of the form “LibraryName:CellName:symbol”
>
>     Example
>
>     ```
>     >>> design = de.db_uu.create_symbol(name=("test_lib", "test_1", "symbol"))
>     ```
>
> keysight.ads.de.db\_uu.find\_instance(*design: [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")*, *inst\_name: str*) → [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance") | None[](#keysight.ads.de.db_uu.find_instance "Link to this definition")
>
> keysight.ads.de.db\_uu.get\_view\_name\_for\_sub\_design(*instance: [Instance](#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*, *view: [View](../view.md#keysight.ads.de.View "keysight.ads.de.View") | None = None*) → str[](#keysight.ads.de.db_uu.get_view_name_for_sub_design "Link to this definition")
>
> keysight.ads.de.db\_uu.open\_design(*name: CellviewRefLike*, *mode: [DesignMode](../db/enums.md#keysight.ads.de.db.DesignMode "keysight.ads.de.db._design_mode.DesignMode") = DesignMode.READ\_ONLY*) → [Design](#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu._design.Design")[](#keysight.ads.de.db_uu.open_design "Link to this definition")
> :   Open a design from an open library in the active workspace.
>
>     Parameters:
>     :   * **name** (*CellviewRefLike*) – The name of the design, usually of the form “LibraryName:CellName:schematic”
>         * **mode** ([*DesignMode*](../db/enums.md#keysight.ads.de.db.DesignMode "keysight.ads.de.db.DesignMode")) – Specifies the mode in which the design is returned. Defaults to read-only mode.
>
>     Example
>
>     ```
>     >>> design = de.db_uu.open_design(name=("LPFoptim_lib", "LPF1Hz", "schematic"))
>     ```

On this page

[Previous

keysight.ads.de.db\_uu](index.md)
[Next

LayerId](layer_id.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top