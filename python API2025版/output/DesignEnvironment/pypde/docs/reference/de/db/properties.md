<!-- 来源: pypde\docs\reference\de\db\properties.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.db](index.md)
* Properties

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
      * [GenPolyline](genpolyline.md)
      * [Model Definition](model_def.md)
      * [Parameters](parameters.md)
      * Properties
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

# Properties[](#properties "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.AppProp[](#keysight.ads.de.db.AppProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    An application specific property.

    These properties have an app\_type and then arbitrary data.
    The data can be anything, including a string.

    *property* app\_type*: str*[](#keysight.ads.de.db.AppProp.app_type "Link to this definition")

    *static* create(*owner: OwnerT*, *name: str*, *app\_type: str*, *value: ndarray | str*) → [AppProp](#keysight.ads.de.db.AppProp "keysight.ads.de.db.AppProp")[](#keysight.ads.de.db.AppProp.create "Link to this definition")

    set\_value\_from\_string(*value: str*) → None[](#keysight.ads.de.db.AppProp.set_value_from_string "Link to this definition")

    *property* value*: ndarray*[](#keysight.ads.de.db.AppProp.value "Link to this definition")

    value\_as\_string() → str[](#keysight.ads.de.db.AppProp.value_as_string "Link to this definition")
    :   Return the value as a string (assumes it is a string).

*class* keysight.ads.de.db.BooleanProp[](#keysight.ads.de.db.BooleanProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: int*) → [BooleanProp](#keysight.ads.de.db.BooleanProp "keysight.ads.de.db.BooleanProp")[](#keysight.ads.de.db.BooleanProp.create "Link to this definition")

    *property* value*: int*[](#keysight.ads.de.db.BooleanProp.value "Link to this definition")

*class* keysight.ads.de.db.DoubleProp[](#keysight.ads.de.db.DoubleProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: float*) → [DoubleProp](#keysight.ads.de.db.DoubleProp "keysight.ads.de.db.DoubleProp")[](#keysight.ads.de.db.DoubleProp.create "Link to this definition")

    *property* value*: float*[](#keysight.ads.de.db.DoubleProp.value "Link to this definition")

*class* keysight.ads.de.db.DoubleRangeProp[](#keysight.ads.de.db.DoubleRangeProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *lower\_bound: float*, *value: float*, *upper\_bound: float*) → [DoubleRangeProp](#keysight.ads.de.db.DoubleRangeProp "keysight.ads.de.db.DoubleRangeProp")[](#keysight.ads.de.db.DoubleRangeProp.create "Link to this definition")

    *property* lower\_bound*: float*[](#keysight.ads.de.db.DoubleRangeProp.lower_bound "Link to this definition")

    set\_range(*lower\_bound: float*, *value: float*, *upper\_bound: float*) → None[](#keysight.ads.de.db.DoubleRangeProp.set_range "Link to this definition")

    *property* upper\_bound*: float*[](#keysight.ads.de.db.DoubleRangeProp.upper_bound "Link to this definition")

    *property* value*: float*[](#keysight.ads.de.db.DoubleRangeProp.value "Link to this definition")

*class* keysight.ads.de.db.EnumProp[](#keysight.ads.de.db.EnumProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    An Enum property - holds a string chosen from a list of strings.

    *static* create(*owner: OwnerT*, *name: str*, *value: str*, *enums: Sequence[str]*) → [EnumProp](#keysight.ads.de.db.EnumProp "keysight.ads.de.db.EnumProp")[](#keysight.ads.de.db.EnumProp.create "Link to this definition")

    *property* enums*: list[str]*[](#keysight.ads.de.db.EnumProp.enums "Link to this definition")

    *property* value*: str*[](#keysight.ads.de.db.EnumProp.value "Link to this definition")

*class* keysight.ads.de.db.FloatProp[](#keysight.ads.de.db.FloatProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: float*) → [FloatProp](#keysight.ads.de.db.FloatProp "keysight.ads.de.db.FloatProp")[](#keysight.ads.de.db.FloatProp.create "Link to this definition")

    *property* value*: float*[](#keysight.ads.de.db.FloatProp.value "Link to this definition")

*class* keysight.ads.de.db.FloatRangeProp[](#keysight.ads.de.db.FloatRangeProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *lower\_bound: float*, *value: float*, *upper\_bound: float*) → [FloatRangeProp](#keysight.ads.de.db.FloatRangeProp "keysight.ads.de.db.FloatRangeProp")[](#keysight.ads.de.db.FloatRangeProp.create "Link to this definition")

    *property* lower\_bound*: float*[](#keysight.ads.de.db.FloatRangeProp.lower_bound "Link to this definition")

    set\_range(*lower\_bound: float*, *value: float*, *upper\_bound: float*) → None[](#keysight.ads.de.db.FloatRangeProp.set_range "Link to this definition")

    *property* upper\_bound*: float*[](#keysight.ads.de.db.FloatRangeProp.upper_bound "Link to this definition")

    *property* value*: float*[](#keysight.ads.de.db.FloatRangeProp.value "Link to this definition")

*class* keysight.ads.de.db.HierProp[](#keysight.ads.de.db.HierProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    An hierarchical property - intended to have properties.

    *static* create(*owner: OwnerT*, *name: str*) → [HierProp](#keysight.ads.de.db.HierProp "keysight.ads.de.db.HierProp")[](#keysight.ads.de.db.HierProp.create "Link to this definition")

*class* keysight.ads.de.db.IntProp[](#keysight.ads.de.db.IntProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: int*) → [IntProp](#keysight.ads.de.db.IntProp "keysight.ads.de.db.IntProp")[](#keysight.ads.de.db.IntProp.create "Link to this definition")

    *property* value*: int*[](#keysight.ads.de.db.IntProp.value "Link to this definition")

*class* keysight.ads.de.db.IntRangeProp[](#keysight.ads.de.db.IntRangeProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *lower\_bound: int*, *value: int*, *upper\_bound: int*) → [IntRangeProp](#keysight.ads.de.db.IntRangeProp "keysight.ads.de.db.IntRangeProp")[](#keysight.ads.de.db.IntRangeProp.create "Link to this definition")

    *property* lower\_bound*: int*[](#keysight.ads.de.db.IntRangeProp.lower_bound "Link to this definition")

    set\_range(*lower\_bound: int*, *value: int*, *upper\_bound: int*) → None[](#keysight.ads.de.db.IntRangeProp.set_range "Link to this definition")

    *property* upper\_bound*: int*[](#keysight.ads.de.db.IntRangeProp.upper_bound "Link to this definition")

    *property* value*: int*[](#keysight.ads.de.db.IntRangeProp.value "Link to this definition")

*class* keysight.ads.de.db.Property[](#keysight.ads.de.db.Property "Link to this definition")
:   Bases: `object`

    The base class for all properties.

    These properties live in a database, typically a design, but can also
    live in DM data files for Library, Cell, and View.

    To add a property to an object, you first choose the class for the Property,
    then initialize an object on the desired property owner.
    For example:
    de.db.StringProp(inst, “name”, “value”)

    To delete a property use delete\_prop.

    delete\_prop() → None[](#keysight.ads.de.db.Property.delete_prop "Link to this definition")

    find\_prop(*name: str*) → [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property") | None[](#keysight.ads.de.db.Property.find_prop "Link to this definition")

    *static* is\_app(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[AppProp](#keysight.ads.de.db.AppProp "keysight.ads.de.db._prop.AppProp")][](#keysight.ads.de.db.Property.is_app "Link to this definition")

    *static* is\_boolean(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[BooleanProp](#keysight.ads.de.db.BooleanProp "keysight.ads.de.db._prop.BooleanProp")][](#keysight.ads.de.db.Property.is_boolean "Link to this definition")

    *static* is\_double(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[DoubleProp](#keysight.ads.de.db.DoubleProp "keysight.ads.de.db._prop.DoubleProp")][](#keysight.ads.de.db.Property.is_double "Link to this definition")

    *static* is\_double\_range(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[DoubleRangeProp](#keysight.ads.de.db.DoubleRangeProp "keysight.ads.de.db._prop.DoubleRangeProp")][](#keysight.ads.de.db.Property.is_double_range "Link to this definition")

    *static* is\_enum(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[EnumProp](#keysight.ads.de.db.EnumProp "keysight.ads.de.db._prop.EnumProp")][](#keysight.ads.de.db.Property.is_enum "Link to this definition")

    *static* is\_float(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[FloatProp](#keysight.ads.de.db.FloatProp "keysight.ads.de.db._prop.FloatProp")][](#keysight.ads.de.db.Property.is_float "Link to this definition")

    *static* is\_float\_range(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[FloatRangeProp](#keysight.ads.de.db.FloatRangeProp "keysight.ads.de.db._prop.FloatRangeProp")][](#keysight.ads.de.db.Property.is_float_range "Link to this definition")

    *static* is\_hier(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[HierProp](#keysight.ads.de.db.HierProp "keysight.ads.de.db._prop.HierProp")][](#keysight.ads.de.db.Property.is_hier "Link to this definition")

    *static* is\_int(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[IntProp](#keysight.ads.de.db.IntProp "keysight.ads.de.db._prop.IntProp")][](#keysight.ads.de.db.Property.is_int "Link to this definition")

    *static* is\_int\_range(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[IntRangeProp](#keysight.ads.de.db.IntRangeProp "keysight.ads.de.db._prop.IntRangeProp")][](#keysight.ads.de.db.Property.is_int_range "Link to this definition")

    *static* is\_string(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[StringProp](#keysight.ads.de.db.StringProp "keysight.ads.de.db._prop.StringProp")][](#keysight.ads.de.db.Property.is_string "Link to this definition")

    *static* is\_time(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[TimeProp](#keysight.ads.de.db.TimeProp "keysight.ads.de.db._prop.TimeProp")][](#keysight.ads.de.db.Property.is_time "Link to this definition")

    *static* is\_time\_range(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[TimeRangeProp](#keysight.ads.de.db.TimeRangeProp "keysight.ads.de.db._prop.TimeRangeProp")][](#keysight.ads.de.db.Property.is_time_range "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.Property.name "Link to this definition")

    *property* owner*: OwnerT*[](#keysight.ads.de.db.Property.owner "Link to this definition")

    *property* props*: NamedReadableCollectionAbc[[Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")]*[](#keysight.ads.de.db.Property.props "Link to this definition")

    *property* type*: [PropType](#keysight.ads.de.db.PropType "keysight.ads.de.db._prop.PropType")*[](#keysight.ads.de.db.Property.type "Link to this definition")

    *property* value*: str*[](#keysight.ads.de.db.Property.value "Link to this definition")

*class* keysight.ads.de.db.PropIter[](#keysight.ads.de.db.PropIter "Link to this definition")
:   Bases: `object`

    \_\_init\_\_(*owner: OwnerT*) → None[](#keysight.ads.de.db.PropIter.__init__ "Link to this definition")

*class* keysight.ads.de.db.StringProp[](#keysight.ads.de.db.StringProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: str*) → [StringProp](#keysight.ads.de.db.StringProp "keysight.ads.de.db.StringProp")[](#keysight.ads.de.db.StringProp.create "Link to this definition")

    *property* value*: str*[](#keysight.ads.de.db.StringProp.value "Link to this definition")

*class* keysight.ads.de.db.TimeProp[](#keysight.ads.de.db.TimeProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: int*) → [TimeProp](#keysight.ads.de.db.TimeProp "keysight.ads.de.db.TimeProp")[](#keysight.ads.de.db.TimeProp.create "Link to this definition")

    *property* value*: int*[](#keysight.ads.de.db.TimeProp.value "Link to this definition")

*class* keysight.ads.de.db.TimeRangeProp[](#keysight.ads.de.db.TimeRangeProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *lower\_bound: int*, *value: int*, *upper\_bound: int*) → [TimeRangeProp](#keysight.ads.de.db.TimeRangeProp "keysight.ads.de.db.TimeRangeProp")[](#keysight.ads.de.db.TimeRangeProp.create "Link to this definition")

    *property* lower\_bound*: int*[](#keysight.ads.de.db.TimeRangeProp.lower_bound "Link to this definition")

    set\_range(*lower\_bound: int*, *value: int*, *upper\_bound: int*) → None[](#keysight.ads.de.db.TimeRangeProp.set_range "Link to this definition")

    *property* upper\_bound*: int*[](#keysight.ads.de.db.TimeRangeProp.upper_bound "Link to this definition")

    *property* value*: int*[](#keysight.ads.de.db.TimeRangeProp.value "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.db.PropType[](#keysight.ads.de.db.PropType "Link to this definition")
:   The type of a Property.

    INT *= <PropType.INT: 166>*[](#keysight.ads.de.db.PropType.INT "Link to this definition")

    INT\_RANGE *= <PropType.INT\_RANGE: 167>*[](#keysight.ads.de.db.PropType.INT_RANGE "Link to this definition")

    FLOAT *= <PropType.FLOAT: 168>*[](#keysight.ads.de.db.PropType.FLOAT "Link to this definition")

    FLOAT\_RANGE *= <PropType.FLOAT\_RANGE: 169>*[](#keysight.ads.de.db.PropType.FLOAT_RANGE "Link to this definition")

    STRING *= <PropType.STRING: 170>*[](#keysight.ads.de.db.PropType.STRING "Link to this definition")

    APP *= <PropType.APP: 171>*[](#keysight.ads.de.db.PropType.APP "Link to this definition")

    DOUBLE *= <PropType.DOUBLE: 172>*[](#keysight.ads.de.db.PropType.DOUBLE "Link to this definition")

    DOUBLE\_RANGE *= <PropType.DOUBLE\_RANGE: 173>*[](#keysight.ads.de.db.PropType.DOUBLE_RANGE "Link to this definition")

    BOOLEAN *= <PropType.BOOLEAN: 174>*[](#keysight.ads.de.db.PropType.BOOLEAN "Link to this definition")

    HIER *= <PropType.HIER: 175>*[](#keysight.ads.de.db.PropType.HIER "Link to this definition")

    TIME *= <PropType.TIME: 176>*[](#keysight.ads.de.db.PropType.TIME "Link to this definition")

    TIME\_RANGE *= <PropType.TIME\_RANGE: 177>*[](#keysight.ads.de.db.PropType.TIME_RANGE "Link to this definition")

    ENUM *= <PropType.ENUM: 178>*[](#keysight.ads.de.db.PropType.ENUM "Link to this definition")

On this page

[Previous

Parameters](parameters.md)
[Next

Transaction](transaction.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top