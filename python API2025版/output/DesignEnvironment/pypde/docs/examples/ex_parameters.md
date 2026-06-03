<!-- 来源: pypde\docs\examples\ex_parameters.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* [Examples](index.md)
* Component Parameters

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

* [Introduction](../../../pydocs/intro/index.md)
  + [Licensing](../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../pydocs/intro/extension.md)
* [Concepts](../../../pydocs/concepts/index.md)
  + [Terminology](../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../pydocs/concepts/execution.md)
* [How-To](../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../pydocs/howto/pytest.md)

* [Design](../index.md)
  + [Reference](../reference/index.md)
    - [keysight.ads.de](../reference/de/index.md)
      * [Workspace](../reference/de/workspace.md)
      * [Library](../reference/de/library.md)
      * [Cell](../reference/de/cell.md)
      * [View](../reference/de/view.md)
      * [CellviewRef](../reference/de/cellviewref.md)
      * [DesignHierarchy](../reference/de/design_hierarchy.md)
      * [DMData](../reference/de/dmdata.md)
      * [ItemInfo](../reference/de/item_info.md)
      * [Points](../reference/de/points.md)
      * [Collections](../reference/de/collections.md)
    - [keysight.ads.de.ael](../reference/de/ael.md)
    - [keysight.ads.de.app](../reference/de/app/index.md)
      * [Actions and Menus](../reference/de/app/action.md)
      * [Addons](../reference/de/app/addon.md)
      * [Callbacks](../reference/de/app/callbacks.md)
      * [Windows and Widgets](../reference/de/app/window.md)
    - [keysight.ads.de.db](../reference/de/db/index.md)
      * [Callbacks](../reference/de/db/callbacks.md)
      * [Enumerated Types](../reference/de/db/enums.md)
      * [Parameter Forms](../reference/de/db/forms.md)
      * [GenPolyline](../reference/de/db/genpolyline.md)
      * [Model Definition](../reference/de/db/model_def.md)
      * [Parameters](../reference/de/db/parameters.md)
      * [Properties](../reference/de/db/properties.md)
      * [Transaction](../reference/de/db/transaction.md)
    - [keysight.ads.de.db\_dbu](../reference/de/db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../reference/de/db_uu/index.md)
      * [Design Elements](../reference/de/db_uu/db_uu.md)
      * [LayerId](../reference/de/db_uu/layer_id.md)
      * [LineTypeInfo](../reference/de/db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../reference/de/experimental/index.md)
      * [CDF](../reference/de/experimental/cdf/index.md)
      * [Commands](../reference/de/experimental/commands.md)
      * [Handles](../reference/de/experimental/handles.md)
      * [Netlist Utilities](../reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../reference/de/experimental/polygon_utils.md)
      * [Preferences](../reference/de/experimental/preferences.md)
      * [xxPro View](../reference/de/experimental/pro_view.md)
      * [Symbol Generator](../reference/de/experimental/symbol.md)
      * [Text Maker](../reference/de/experimental/text_maker.md)
    - [keysight.ads.de.tech](../reference/de/tech/index.md)
      * [Tech](../reference/de/tech/tech.md)
      * [Padstacks](../reference/de/tech/pads/pads.md)
      * [Via Rules](../reference/de/tech/rule/rule.md)
      * [Nested Technology](../reference/de/tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../reference/de/app/dds.md)
  + [Examples](index.md)
    - [Calling Between AEL and Python](ex_calling_ael_and_python.md)
    - [Create Layout](ex_create_layout.md)
    - [Create Schematic](ex_create_schematic.md)
    - [Create Workspace](ex_workspace.md)
    - [Create, Simulate, and Plot](ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](ex_cdf.md)
    - Component Parameters
    - [Creating an Item Definition](ex_itemdef.md)
    - [Model Definition Properties](ex_model.md)
    - [Adding Instances to a Design](ex_lpf.md)
    - [Properties](ex_properties.md)
    - [Creating Custom Menus Using an Addon](ex_menu_addon.md)
    - [Padstacks and Vias](ex_padstack.md)
    - [Nested Technology](ex_nested.md)
    - [Rules](ex_rules.md)
    - [Placing Text](ex_place_text.md)
    - [Paths, Traces, and Polygons](ex_polygon.md)
    - [PySide2](ex_pyside.md)
    - [Traversing Hierarchy](ex_traversing_hierarchy.md)
    - [Working with VAR](ex_working_with_var.md)
    - [XML RPC](ex_xml_rpc.md)
    - [GDSII Import and Export](ex_translate_gds.md)
* [Technology](../../../pysubst/docs/index.md)
  + [Reference](../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Component Parameters[](#component-parameters "Link to this heading")

Components are represented by the [`ModelDef`](../reference/de/db/model_def.md#keysight.ads.de.db.ModelDef "keysight.ads.de.db.ModelDef") class. The model definition has a name (often the name of the [`Cell`](../reference/de/cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell"))
and holds parameter definitions ([`ModelParam`](../reference/de/db/model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db.ModelParam")) and callbacks ([`ModelCbBase`](../reference/de/db/callbacks.md#keysight.ads.de.db.ModelCbBase "keysight.ads.de.db.ModelCbBase")), whose types are defined in [`ModelCbType`](../reference/de/db/callbacks.md#keysight.ads.de.db.ModelCbType "keysight.ads.de.db.ModelCbType").

When defining a parameter for your component, create a [`ModelParam`](../reference/de/db/model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db.ModelParam"), which represents the definition of your parameter. The [`ModelParam`](../reference/de/db/model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db.ModelParam") has a name,
a label for display within ADS, an optional [`ModelUnitType`](../reference/de/db/parameters.md#keysight.ads.de.db.ModelUnitType "keysight.ads.de.db.ModelUnitType"), an optional [`ModelParamType`](../reference/de/db/parameters.md#keysight.ads.de.db.ModelParamType "keysight.ads.de.db.ModelParamType"), and the [`Forms`](../reference/de/db/forms.md#keysight.ads.de.db.Form "keysight.ads.de.db.Form") (held in a [`Formset`](../reference/de/db/forms.md#keysight.ads.de.db.Formset "keysight.ads.de.db.Formset")) that describe how the parameter is displayed and netlisted.
After instantiating a [`ModelParam`](../reference/de/db/model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db.ModelParam"), you will typically want to provide a default value ([`ParamItem`](../reference/de/db/parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem")) and/or callbacks ([`ModelCbBase`](../reference/de/db/callbacks.md#keysight.ads.de.db.ModelCbBase "keysight.ads.de.db.ModelCbBase")) for the parameter.
All the parameter definitions for your component will then need to be added to the model definition by calling [`append_parameter`](../reference/de/db/model_def.md#keysight.ads.de.db.ModelDefBase.append_parameter "keysight.ads.de.db.ModelDefBase.append_parameter") or [`insert_parameter`](../reference/de/db/model_def.md#keysight.ads.de.db.ModelDefBase.insert_parameter "keysight.ads.de.db.ModelDefBase.insert_parameter").

When you are satisfied with the definition of your component, add it to a [`Library`](../reference/de/library.md#keysight.ads.de.Library "keysight.ads.de.Library") by calling [`add_model_definition`](../reference/de/index.md#keysight.ads.de.add_model_definition "keysight.ads.de.add_model_definition").

In summary, default parameter values and callbacks are added to a parameter definition, parameter definitions are added to a model definition, and the model definition is added to a library. The components represented by the model definition can then be placed in a design.

ADS will automatically attempt to create the definition of your component when a [`Cell`](../reference/de/cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell") is first accessed by executing the well-known function create\_itemdef inside the well-known file called itemdef.py located in the directory of your [`Cell`](../reference/de/cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell")

See [Enabling Python Support For Your Library](../../../pydocs/concepts/openaccess_integration.md#enabling-python-support) for more information on initialization of Python enabled libraries.

```
# itemdef.py is imported by ADS when the cell is first accessed and ADS will attempt to call the function create_itemdef
```

```
def create_itemdef(cell: de.Cell) -> None:
    def creating_a_string_parameter(cell: de.Cell) -> None:
        # Create the parameter definition using the StdFormSet formset provided by ADS.
        formset = de.db.model_lib.formsets["StdFormSet"]
        string_param = de.db.ModelParam("string", "String", formset, de.db.ModelUnitType.NO_UNIT)
        # Set the default value of the parameter to "Hello, World!"
        string_param.default_value = de.db.ParamItemString("", "StdForm", "Hello, World!")
        # Create the model definition representing the component
        model_def = de.db.ModelDef(cell.name, cell.name)
        # Placed component names will be X1, X2, etc.
        model_def.inst_name_prefix = "X"
        model_def.is_sub_design = False
        # Add the parameter definition to the model definition
        model_def.parameters = string_param
        # And add the model definition to the library
        de.add_model_definition(cell.library, model_def)

    creating_a_string_parameter(cell)
```

When an [`Instance`](../reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance") of your component has been placed in a [`Design`](../reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design"), you can access the parameters via the [`parameters`](../reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Instance.parameters "keysight.ads.de.db_uu.Instance.parameters") property of the [`Instance`](../reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance").
The [`parameters`](../reference/de/db/parameters.md#keysight.ads.de.db.ParamBase "keysight.ads.de.db.ParamBase") attached to an [`Instance`](../reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance") are of type [`ParamBase`](../reference/de/db/parameters.md#keysight.ads.de.db.ParamBase "keysight.ads.de.db.ParamBase") and provide accessors to the parameter’s value ([`ParamItem`](../reference/de/db/parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem")) and definition ([`ModelParam`](../reference/de/db/model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db.ModelParam"))

Example illustrating how to create and modify a repeated parameter.

```
def creating_a_repeated_parameter(cell: de.Cell) -> None:
    formset = de.db.model_lib.formsets["StdFormSet"]
    # You can use the make_string_param function to create a string parameter value
    if True:
        default_repeats = [
            de.db.std_string_param("0"),
            de.db.std_string_param("2"),
        ]
    # Or call the ParamItemString constructor directly
    else:
        default_repeats = [
            de.db.ParamItemString("", "StdForm", "0"),
            de.db.ParamItemString("", "StdForm", "2"),
        ]
    # Create a repeated parameter value using a list of values
    # Like make_string_param, you can use repeated_param to create a repeated parameter value
    if True:
        default_repeated_param = de.db.repeated_param(default_repeats)
    # Or call the ParamItemRepeated constructor directly
    else:
        default_repeated_param = de.db.ParamItemRepeated("", default_repeats)
    # Append a repeated parameter value to the end (using either append or +=)
    if True:
        default_repeated_param.repeats.append(de.db.std_string_param("3"))
    else:
        default_repeated_param.repeats += de.db.std_string_param("3")

    # Insert a repeated value at the specified index
    default_repeated_param.repeats.insert(1, de.db.std_string_param("1"))

    repeats = default_repeated_param.repeats
    assert [de.db.ParamItem.is_string(repeat) and repeat.value for repeat in repeats] == ["0", "1", "2", "3"]

    # Remove the repeat at the specified index
    extracted_repeat = default_repeated_param.repeats.pop(2)
    assert de.db.ParamItem.is_string(extracted_repeat) and extracted_repeat.value == "2"

    # Verify it has been removed
    repeats = default_repeated_param.repeats
    assert [de.db.ParamItem.is_string(repeat) and repeat.value for repeat in repeats] == ["0", "1", "3"]

    # Clear the repeated values and set new repeated values.
    default_repeated_param.repeats = default_repeats

    repeats = default_repeated_param.repeats
    assert [de.db.ParamItem.is_string(repeat) and repeat.value for repeat in repeats] == ["0", "2"]

    repeated_param = de.db.ModelParam("repeat", "Repeat", formset, de.db.ModelUnitType.NO_UNIT)
    repeated_param.is_repeated = True
    repeated_param.default_value = default_repeated_param

    model_def = de.db.ModelDef(cell.name, cell.name)
    model_def.inst_name_prefix = "X"
    model_def.is_sub_design = False
    model_def.parameters = repeated_param
    de.add_model_definition(cell.library, model_def)
```

Example illustrating how to create a repeated compound parameter.

```
def creating_a_repeated_compound_parameter(cell: de.Cell, design: db_uu.Design) -> None:
    # Create the form for the compound parameter
    def create_compound_form(library: de.Library) -> de.db.CompoundForm:
        formset = de.db.model_lib.formsets["StdFormSet"]
        parm_first = de.db.ModelParam("first", "x val", formset, de.db.ModelUnitType.NO_UNIT)
        parm_second = de.db.ModelParam("second", "y val", formset, de.db.ModelUnitType.NO_UNIT)
        parm_third = de.db.ModelParam("third", "z val", formset, de.db.ModelUnitType.NO_UNIT)
        params = [parm_first, parm_second, parm_third]
        # See 'Creating New Component Definitions' in ADS documentation for percent string syntax.
        compound_form = de.db.CompoundForm("CompoundForm", "x,y,z", params, display_format="(%0s,%1s,%2s)")
        library.forms.add(compound_form)
        return compound_form

    compound_form = create_compound_form(cell.library)
    compound_formset = de.db.Formset("CompoundForm", [compound_form])
    cell.library.formsets.add(compound_formset)

    # We'll have a repeated parameter where each parameter repeat is a compound parameter
    default_compound_value_1 = [
        de.db.ParamItemString("X", "StdForm", "1"),
        de.db.ParamItemString("Y", "StdForm", "2"),
        de.db.ParamItemString("Z", "StdForm", "3"),
    ]

    default_compound_value_2 = [
        de.db.ParamItemString("X", "StdForm", "10"),
        de.db.ParamItemString("Y", "StdForm", "20"),
        de.db.ParamItemString("Z", "StdForm", "30"),
    ]
    # Default value, a repeated parameter with two compound parameter values
    default_compound_param_value_1 = de.db.compound_param("StdForm", default_compound_value_1)
    default_compound_param_value_2 = de.db.compound_param("StdForm", default_compound_value_2)
    default_param_value = de.db.repeated_param([default_compound_param_value_1, default_compound_param_value_2])

    repeated_compound_param = de.db.ModelParam(
        "repeat_compound", "Repeat Compound", compound_formset, de.db.ModelUnitType.NO_UNIT
    )

    repeated_compound_param.is_repeated = True
    repeated_compound_param.default_value = default_param_value

    repeats = default_param_value.repeats
    repeat_0 = repeats[0]
    repeat_1 = repeats[1]
    assert de.db.ParamItem.is_compound(repeat_0) and len(repeat_0.sub_params) == 3
    assert de.db.ParamItem.is_compound(repeat_1) and len(repeat_1.sub_params) == 3
    assert [de.db.ParamItem.is_string(param) and param.value for param in repeat_0.sub_params] == ["1", "2", "3"]
    assert [de.db.ParamItem.is_string(param) and param.value for param in repeat_1.sub_params] == ["10", "20", "30"]

    model_def = de.db.ModelDef(cell.name, cell.name)
    model_def.inst_name_prefix = "X"
    model_def.is_sub_design = False
    model_def.parameters = repeated_compound_param
    de.add_model_definition(cell.library, model_def)

    # Place an instance of the component into a design and validate the default parameter values
    def place_instance_and_validate_default_parameter_values(design: db_uu.Design) -> None:
        assert design.is_layout
        design.clear_design()
        inst = design.add_instance(db_uu.LCVName(design.library, cell, None), (0, 0))
        # The parameter is a repeated parameter with the repeats being compound parameters
        repeat_compund_param = inst.parameters["repeat_compound"]
        assert de.db.ParamBase.is_repeated(repeat_compund_param)

        repeats = repeat_compund_param.repeats
        # Verify first repeat
        compound_0 = repeats[0]
        assert de.db.ParamBase.is_compound(compound_0)
        assert de.db.ParamBase.is_string(compound_0.sub_params[0])
        assert de.db.ParamBase.is_string(compound_0.sub_params[1])
        assert de.db.ParamBase.is_string(compound_0.sub_params[2])
        assert compound_0.sub_params[0].value == "1"
        assert compound_0.sub_params[1].value == "2"
        assert compound_0.sub_params[2].value == "3"

        # Verify second repeat
        compound_1 = repeats[1]
        assert de.db.ParamBase.is_compound(compound_1)
        sub_params_1 = compound_1.sub_params
        assert all(de.db.ParamBase.is_string(sub_param) for sub_param in sub_params_1)
        assert [sub_param.value for sub_param in sub_params_1] == ["10", "20", "30"]
        design.save_design()

    place_instance_and_validate_default_parameter_values(design)
```

Example illustrating how to append and remove repeats to and from a repeated parameter.

```
def appending_and_removing_repeats_to_a_repeated_parameter(cell: de.Cell, design: db_uu.Design) -> None:
    # create_itemdef below is a bit of setup for creating a model definition that has a parameter
    # that represents the vertices of a shape.
    # It consists of a repeated parameter where each repeat is a compound parameter, made up
    # of two string parameters representing the x and y coordinates.
    # [shape]                  repeat
    # [point]           compound    compound     ...
    # [x,y]     string,  string      string,   string    ..., ...

    def create_itemdef(cell: de.Cell) -> None:
        def create_point_form(lib: de.Library) -> de.db.CompoundForm:
            formset = de.db.model_lib.formsets["StdFormSet"]
            parm_first = de.db.ModelParam("first", "x coordinate", formset, de.db.ModelUnitType.LENGTH)
            parm_second = de.db.ModelParam("second", "y coordinate", formset, de.db.ModelUnitType.LENGTH)
            params = [parm_first, parm_second]
            point_form = de.db.CompoundForm("PointForm", "x,y", params, display_format="(%0s,%1s)")
            lib.forms.add(point_form)
            return point_form

        library = cell.library
        point_form = create_point_form(library)
        point_formset = de.db.Formset("PointForms", [point_form])
        library.formsets.add(point_formset)
        # Setting up an initial point at 0.0, 0.0
        initial_point = de.db.compound_param(
            "PointForm", [de.db.std_string_param("0.0 mil"), de.db.std_string_param("0.0 mil")]
        )
        param_vertices = de.db.ModelParam("vertices", "vertex coordinates", point_formset, de.db.ModelUnitType.NO_UNIT)
        param_vertices.default_value = de.db.repeated_param([initial_point])
        # Vertices is a repeated parameter
        param_vertices.is_repeated = True
        shape = de.db.ModelDef(cell.name, cell.name)
        shape.inst_name_prefix = "X"
        shape.is_sub_design = False
        shape.parameters = param_vertices
        de.add_model_definition(library, shape)

    create_itemdef(cell)

    # Place an instance of the component and work with the vertices parameter
    inst = design.add_instance(db_uu.LCVName(cell.library, cell, None), (0, 0))
    param = inst.parameters["vertices"]

    assert de.db.ParamBase.is_repeated(param)
    assert len(param.repeats) == 1
    compound_0 = param.repeats[0]
    assert de.db.Param.is_compound(compound_0)
    assert compound_0.sub_params[0].value == "0.0 mil"
    assert compound_0.sub_params[1].value == "0.0 mil"

    # Additional repeats can be added in a variety of ways:
    # You can clone a repeat at the specified index and modify its values.
    param.repeats.clone(0)
    assert len(param.repeats) == 2
    compound_1 = param.repeats[1]
    assert de.db.Param.is_compound(compound_1)
    # Verify the cloned repeat has the same values as the original
    assert compound_1.sub_params[0].value == "0.0 mil"
    assert compound_1.sub_params[1].value == "0.0 mil"
    # And update the values
    compound_1.sub_params[0].value = "10.0 mil"
    compound_1.sub_params[1].value = "0.0 mil"
    # You can call append to append a new repeat
    next_point = de.db.compound_param(
        "PointForm", [de.db.std_string_param("10.0 mil"), de.db.std_string_param("10.0 mil")]
    )
    param.repeats.append(next_point)
    assert len(param.repeats) == 3
    compound_2 = param.repeats[2]
    assert de.db.Param.is_compound(compound_2)
    assert compound_2.sub_params[0].value == "10.0 mil"
    assert compound_2.sub_params[1].value == "10.0 mil"

    next_point = de.db.compound_param(
        "PointForm", [de.db.std_string_param("0.0 mil"), de.db.std_string_param("10.0 mil")]
    )
    # You can also use the += operator to append a new repeat
    param.repeats += next_point
    assert len(param.repeats) == 4
    compound_3 = param.repeats[3]
    assert de.db.Param.is_compound(compound_3)
    assert compound_3.sub_params[0].value == "0.0 mil"
    assert compound_3.sub_params[1].value == "10.0 mil"

    # New repeats may also be inserted at a specified index
    new_point = de.db.compound_param(
        "PointForm", [de.db.std_string_param("5.0 mil"), de.db.std_string_param("15.0 mil")]
    )
    param.repeats.insert(3, new_point)
    assert len(param.repeats) == 5
    compound_3 = param.repeats[3]
    assert de.db.Param.is_compound(compound_3)
    assert compound_3.sub_params[0].value == "5.0 mil"
    assert compound_3.sub_params[1].value == "15.0 mil"
    compound_4 = param.repeats[4]
    assert de.db.Param.is_compound(compound_4)
    assert compound_4.sub_params[0].value == "0.0 mil"
    assert compound_4.sub_params[1].value == "10.0 mil"

    # You can remove a repeat at the specified index a couple of different ways
    # remove will simply remove the repeat at the specified index
    param.repeats.remove(3)
    assert len(param.repeats) == 4
    compound_3 = param.repeats[3]
    assert de.db.Param.is_compound(compound_4)
    assert compound_4.sub_params[0].value == "0.0 mil"
    assert compound_4.sub_params[1].value == "10.0 mil"

    # whereas pop will remove the item and return it
    removed = param.repeats.pop(-1)
    assert de.db.Param.is_compound(removed)
    assert removed.sub_params[0].value == "0.0 mil"
    assert removed.sub_params[1].value == "10.0 mil"
    assert len(param.repeats) == 3
    compound_2 = param.repeats[2]
    assert de.db.Param.is_compound(compound_2)
    assert compound_2.sub_params[0].value == "10.0 mil"
    assert compound_2.sub_params[1].value == "10.0 mil"
```

Example illustrating how to create a Formset with constant Forms and a parameter using the Formset

```
def creating_and_using_a_constant_form(cell: de.Cell, design: db_uu.Design) -> None:
    library = cell.library
    # Create yes/no forms and formset and add them to the library
    # We want these forms to be netlisted as "yes" and "no"
    yes_form = de.db.ConstForm("Yes", "YES", "yes")
    no_form = de.db.ConstForm("No", "NO", "no")
    library.forms.add(yes_form)
    library.forms.add(no_form)
    yes_no_formset = de.db.Formset("Yes/No", [yes_form, no_form])
    library.formsets.add(yes_no_formset)

    # Create a parameter with the yes/no formset and a default value of yes
    decision_param = de.db.ModelParam("decision", "Yes or No", yes_no_formset)
    assert "real" == decision_param.param_type.value
    assert decision_param.unit_type == de.db.ModelUnitType.NO_UNIT
    decision_param.default_value = de.db.const_param("Yes")

    # Add the model definition to the library
    model_def = de.db.ModelDef(cell.name, cell.name)
    model_def.inst_name_prefix = "X"
    model_def.is_sub_design = False
    model_def.parameters = decision_param
    de.add_model_definition(library, model_def)

    # Place an instance and modify the constant form parameter value
    def place_instance_and_validate_parameter_values(design: db_uu.Design) -> None:
        assert design.is_layout
        design.clear_design()
        inst = design.add_instance(db_uu.LCVName(design.library, cell, None), (0, 0))
        # The parameter is a repeated parameter with the repeats being compound parameters
        decision_parameter = inst.parameters["decision"]
        assert de.db.ParamBase.is_const(decision_parameter)
        # ConstForm parameter values are the netlisted value (net_format)
        assert decision_parameter.value == "yes"
        # Assignment of a value to a parameter will attempt to find a matching form.
        # This matching will look at name, label, net_format and display_format for ConstForm.
        decision_parameter.value = "NO"
        ael.call.de_edit_inst_param_value(inst, "decision", "No", "NO", (0, 0))
        assert design.instances["X1"].parameters["decision"].value == "no"

        decision_parameter = design.instances["X1"].parameters["decision"]
        # Setting to an invalid value will revert to the default value
        decision_parameter.value = "Not Valid"
        assert decision_parameter.value == "yes"

        decision_parameter.value = "NO"
        assert decision_parameter.value == "no"

        # Setting to an invalid value will revert to the default value
        ael.call.de_edit_inst_param_value(inst, "decision", "No", "Not Valid", (0, 0))
        assert design.instances["X1"].parameters["decision"].value == "yes"

        design.save_design()

    place_instance_and_validate_parameter_values(design)
```

Example illustrating how to evaluate the value of a parameter.

```
def evaluating_a_parameter(cell: de.Cell, design: db_uu.Design) -> None:
    # Item definition with a couple length values in different units
    def create_itemdef(cell: de.Cell) -> None:
        formset = de.db.model_lib.formsets["StdFormSet"]
        # Length parameter in mils
        length_param_in_mils = de.db.ModelParam("l_in_mils", "L in mils", formset, de.db.ModelUnitType.LENGTH)
        length_param_in_mils.default_value = de.db.ParamItemString("", "StdForm", "25 mil")

        # Length parameter in microns
        length_param_in_microns = de.db.ModelParam("l_in_microns", "L in microns", formset, de.db.ModelUnitType.LENGTH)
        length_param_in_microns.default_value = de.db.ParamItemString("", "StdForm", "25 um")

        # Length parameter with an expression
        length_with_expr = de.db.ModelParam("l_with_expr", "L with expr", formset, de.db.ModelUnitType.LENGTH)
        length_with_expr.default_value = de.db.ParamItemString("", "StdForm", "10 * 25 mil")

        model_def = de.db.ModelDef(cell.name, cell.name)
        model_def.inst_name_prefix = "X"
        model_def.is_sub_design = False
        model_def.parameters = [length_param_in_mils, length_param_in_microns, length_with_expr]
        de.add_model_definition(cell.library, model_def)

    def place_instance_and_evaluate_parameter_value(design: db_uu.Design) -> None:
        assert design.is_layout
        design.clear_design()
        inst = design.add_instance(db_uu.LCVName(design.library, cell, None), (0, 0))

        l_in_mils = inst.parameters["l_in_mils"]
        assert de.db.ParamBase.is_string(l_in_mils)
        # Value before evaluation
        assert l_in_mils.value == "25 mil"

        l_in_ums = inst.parameters["l_in_microns"]
        assert de.db.ParamBase.is_string(l_in_ums)
        # Value before evaluation
        assert l_in_ums.value == "25 um"

        # Evaluating a parameter with a LENGTH ModelUnitType returns the value in meters
        val_in_meters = float(l_in_mils.evaluate_no_expr())
        assert val_in_meters == 0.000635  # 25 mil * 2.54e-5 m/mil == 0.000635 m
        val_in_meters = float(l_in_ums.evaluate_no_expr())
        assert val_in_meters == 0.000025  # 25 um * 1e-6 um/m == 0.000025 m

        l_with_expr = inst.parameters["l_with_expr"]
        assert de.db.ParamBase.is_string(l_with_expr)
        assert l_with_expr.value == "10 * 25 mil"

        # Cannot call evaluate_no_expr on a parameter with an expression
        try:
            l_with_expr.evaluate_no_expr()
        except RuntimeError as e:
            assert (
                str(e)
                == 'Error processing the value for parameter "l_with_expr": Could not evaluate value without simulation'
            )
            expr_context = de.db.ExpressionContext()
            expr_context.setup_hierarchy_for_design(design)
            expr_val_in_meters = l_with_expr.evaluate(expr_context)
            assert isinstance(expr_val_in_meters, float)

        import math

        assert math.isclose(expr_val_in_meters, 0.00635, rel_tol=1e-6)  # 10 * 25 mil == 25 * 10 * 2.54e-5 == 0.00635

    create_itemdef(cell)
    place_instance_and_evaluate_parameter_value(design)
```

Example illustrating how to add a callback to an existing ADS component.

```
def adding_a_callback_to_existing_component(design: db_uu.Design) -> None:
    # Open the design of an ADS component
    snp_design = db_uu.open_design("ads_datacmps:SnP:symbol", de.db.DesignMode.READ_ONLY)
    # Create an item info object to obtain the model definition of the SnP component
    if True:
        item_info = de.ItemInfo(design, de.LCVName("ads_datacmps", "SnP", "symbol"), de.ItemEditMode.TEMP)
        model_def = item_info.model_def
    # Model definition can be retrieved in more than one way
    else:
        model_def = de.db.ModelDef.find_model_def(snp_design.library, "SnP")

    assert model_def is not None
    # ModelParam of the NumPorts parameter
    num_ports_model_param = model_def.parameters.get("NumPorts")
    # Default number of ports is 1
    def_num_ports_value = num_ports_model_param.get_default_value_copy(snp_design, model_def)
    assert def_num_ports_value and de.db.ParamItem.is_string(def_num_ports_value) and def_num_ports_value.value == "1"
    # Starting fresh, just in case
    design.clear_design()
    # Add the SnP component to the design
    inst_1_port = design.add_instance(("ads_datacmps", "SnP", "symbol"), (0, 0), name="SnP_1Port")
    assert inst_1_port.parameters["NumPorts"].value == "1"

    # Default value callback for the NumPorts parameter
    def snp_num_ports_default_value(
        param: de.db.ModelParam, model_def: de.db.ModelDefBase, design: db_uu.Design
    ) -> de.db.ParamItemString:
        assert param.name == "NumPorts"
        assert model_def.name == "SnP"
        return de.db.std_string_param("8")

    default_num_ports_value_callback = de.db.ModelCb(
        de.db.ModelCbType.PARAMETER_DEFAULT_VALUE,
        snp_num_ports_default_value,
    )
    # Add the callback to the NumPorts ModelParam
    num_ports_model_param.callbacks = default_num_ports_value_callback
    # Add another instance of SnP and validate the default value for NumPorts is now 8
    inst_8_port = design.add_instance(("ads_datacmps", "SnP", "symbol"), (2, 0), name="SnP_8Port")
    assert inst_8_port.parameters["NumPorts"].value == "8"
    # Don't forget to save
    design.save_design()
```

Example illustrating how to add a callback to an existing component instance placed in a design

```
def adding_a_callback_to_a_placed_component_instance(design: db_uu.Design) -> None:
    design.clear_design()
    # Set up the design with a resistor
    design.add_instance(("ads_rflib", "R", "symbol"), (0, 0), name="R1")

    inst_r1 = design.instances["R1"]

    assert inst_r1.parameters["Width"].value == ""
    assert inst_r1.parameters["Length"].value == ""

    model_def = inst_r1.model_def
    assert model_def

    def width_modified_callback(item_info: de.ItemInfo, param_name: str) -> bool:
        inst = item_info.instance
        assert inst
        assert param_name == "Width"
        assert inst.name == "R1"
        assert inst.parameters["Width"].value == "10"
        dependent_parm_data = ael.call.pcb_set_mks(None, "Length", 25)
        ael.call.pcb_store_parm_callback_data(item_info, dependent_parm_data)
        return True

    # Add a parameter modified callback for the Width parameter
    width_model_param = model_def.parameters.get("Width")
    modified_width_cb = de.db.ModelCb(
        de.db.ModelCbType.PARAMETER_MODIFIED, lambda item_info: width_modified_callback(item_info, "Width")
    )
    width_model_param.callbacks = modified_width_cb

    ael.call.de_edit_inst_param_value(inst_r1, "Width", "StdForm", "10", (0, 0))
    design.save_design()
```

Example illustrating how to access the default value of one parameter from the default value callback of another parameter.

```
def accessing_default_value_of_parameter_from_different_parameter_callback(cell: de.Cell) -> None:
    formset = de.db.model_lib.formsets["StdFormSet"]
    # Length parameter with a default value of 25
    length_param = de.db.ModelParam("length", "Length", formset, de.db.ModelUnitType.NO_UNIT, de.db.ModelParamType.INT)
    length_param.default_value = de.db.std_string_param("25")

    # Width parameter with a default value of 4
    width_param = de.db.ModelParam("width", "Width", formset, de.db.ModelUnitType.NO_UNIT, de.db.ModelParamType.INT)
    width_param.default_value = de.db.std_string_param("4")

    # Area parameter whose value will be computed in its default value callback based on the default
    # values of length and width
    area_param = de.db.ModelParam("area", "Area", formset, de.db.ModelUnitType.NO_UNIT, de.db.ModelParamType.INT)

    # Default value callback for the area parameter. It uses the default values of the
    # width and length parameters to compute the area.
    def calculate_default_area_value(
        param: de.db.ModelParam, model_def: de.db.ModelDefBase, design: db_uu.Design
    ) -> de.db.ParamItemString:
        # Ensure that the callback is being called for the area parameter
        assert param.name == "area"

        # Validate that the default values of the length and width parameters are being used
        length_param = model_def.parameters.get("length")
        default_length_param = length_param.get_default_value_copy(design, model_def)
        assert default_length_param and de.db.ParamItem.is_string(default_length_param)
        length_val = int(default_length_param.value)
        assert length_val == 25

        width_param = model_def.parameters.get("width")
        default_width_param = width_param.get_default_value_copy(design, model_def)
        assert default_width_param and de.db.ParamItem.is_string(default_width_param)
        width_val = int(default_width_param.value)
        assert width_val == 4

        # Calculate the area using the default values of the length and width parameters
        area = length_val * width_val
        return de.db.std_string_param(str(area))

    default_area_value_callback = de.db.ModelCb(
        de.db.ModelCbType.PARAMETER_DEFAULT_VALUE,
        calculate_default_area_value,
    )

    area_param.callbacks = default_area_value_callback

    model_def = de.db.ModelDef(cell.name, cell.name)
    model_def.inst_name_prefix = "X"
    model_def.is_sub_design = False
    model_def.parameters = [length_param, width_param, area_param]
    de.add_model_definition(cell.library, model_def)
```

On this page

[Previous

Interoperable Component Parameters](ex_cdf.md)
[Next

Creating an Item Definition](ex_itemdef.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top