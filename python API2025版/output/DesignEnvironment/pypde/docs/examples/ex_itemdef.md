<!-- 来源: pypde\docs\examples\ex_itemdef.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* [Examples](index.md)
* Creating an Item Definition

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
    - [Component Parameters](ex_parameters.md)
    - Creating an Item Definition
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

# Creating an Item Definition[](#creating-an-item-definition "Link to this heading")

This is an example for creating an item definition for a pcell.

```
# Libraries with item definitions created in Python need to specify Python is enabled for the library in eesof_lib.cfg,
# located in the library directory
# eesof_lib.cfg:
# PYTHON_ENABLED=TRUE

# An item definition written in Python must reside in a module called itemdef.py located in the cell's directory.
# The function create_itemdef will be called by ADS when your item definition is loaded.
from keysight.ads import de

def create_itemdef(cell: de.Cell):
    # Create item definition here
    ...
```

```
# Copyright Keysight Technologies 2023 - 2024
import math

from keysight.ads import de
from keysight.ads.de import db_uu

# Copy and paste this example inside the ADS Python console.

# An item definition resides in the cell's directory, named itemdef.py and contains
# the function called create_itemdef(de.Cell)
def create_itemdef(cell: de.Cell) -> None:
    # The library must have a cell with the name of the item definition
    assert cell.name == "regular_polygon"
    library = cell.library
    # Create and add a point form and formset to the library
    point_form, point_formset = create_point_form_and_formset_and_add_to_library(library)
    # The point represents a design placement offset from the center point of a regular polygon
    param_offset_point = de.db.ModelParam("offset", "Offset from Center", point_formset, de.db.ModelUnitType.LENGTH)
    # Default values for parameters may be set directly, like this:
    default_coordinate_param = de.db.std_string_param("0.0 mil")
    param_offset_point.default_value = de.db.compound_param(
        point_form.name, [default_coordinate_param, default_coordinate_param]
    )
    # Or, default values may be set using a callback, like this:
    # NOTE: When both a default callback and a stored default value are set,
    # the value returned by the callback will take precedence
    default_value_callback = de.db.ModelCb(
        de.db.ModelCbType.PARAMETER_DEFAULT_VALUE,
        lambda param, model_definition, design: get_default_coordinate(param, model_definition, design),
    )
    param_offset_point.callbacks = default_value_callback
    standard_formset = de.db.model_lib.formsets["StdFormSet"]
    assert standard_formset
    # Number of sides for the polygon, octagons by default
    default_sides_param = de.db.std_string_param("8")
    param_number_of_sides = de.db.ModelParam(
        "sides", "number of sides", standard_formset, de.db.ModelUnitType.NO_UNIT, de.db.ModelParamType.INT
    )
    param_number_of_sides.default_value = default_sides_param
    # The distance from the center point to any vertex
    default_radius_param = de.db.std_string_param("100.0 mil")
    param_radius = de.db.ModelParam(
        "radius", "distance from center point to any vertex", standard_formset, de.db.ModelUnitType.LENGTH
    )
    param_radius.default_value = default_radius_param
    # The orientation (rotation angle), in degrees, of the polygon. A 22.5 degree rotated octagon
    # will be placed such that two sides are parallel to both the X and the Y axes
    default_orientation_param = de.db.std_string_param("22.5")
    param_orientation = de.db.ModelParam(
        "orientation", "angle of orientation", standard_formset, de.db.ModelUnitType.ANGLE, de.db.ModelParamType.REAL
    )
    param_orientation.default_value = default_orientation_param
    # Now that the parameters have all been defined, create the model definition for the regular polygon
    regular_polygon = de.db.ModelDef("regular_polygon", "regular_polygon")
    # Each placed instance will be automatically named X1, X2, X3, etc.
    regular_polygon.inst_name_prefix = "X"
    # Append the parameters
    regular_polygon.parameters = [param_offset_point, param_number_of_sides, param_radius, param_orientation]
    # Add a netlist callback, if desired
    netlist_cb = de.db.ModelCb(de.db.ModelCbType.ITEM_NETLIST, netlist_callback)
    regular_polygon.callbacks = netlist_cb
    # And add the model definition to the library
    de.add_model_definition(library, regular_polygon)

def netlist_callback(netlist_inst: de.db.StandardInstance) -> str:
    # Use the NetlistStringBuilder to build up the netlist string
    from keysight.ads.de.experimental.netlist_helper import NetlistStringBuilder

    builder = NetlistStringBuilder(netlist_inst)
    if False:
        # Functionally equivalent to the else clause
        return builder.clear_and_get_default_netlist_str()
    else:
        if False:
            # Functionally equivalent to the else clause
            builder.append_model_and_instance_name()
        else:
            builder.append_model_name()
            builder.append_str(":")
            builder.append_instance_name()

        builder.append_connectivity()
        if False:
            # Functionally equivalent to the else clause
            builder.append_parameters()
        else:
            builder.append_parameter("offset")
            builder.append_parameter("sides")
            builder.append_parameter("radius")
            builder.append_parameter("orientation")
            # append_parameter will raise an exception on a bad parameter name
            try:
                builder.append_parameter("not_a_parameter_name")
            except RuntimeError:
                pass
    return builder.netlist_str

def create_point_form_and_formset_and_add_to_library(
    library: de.Library,
) -> tuple[de.db.CompoundForm, de.db.Formset]:
    formset = de.db.model_lib.formsets["StdFormSet"]
    # Point parameters will use StdForm and are specified using a coordinate system
    default_coordinate_value = de.db.std_string_param("0 mil")
    # A point is a compound form with two parameters, X and Y
    # The first parameter represents the X coordinate
    param_first = de.db.ModelParam("first", "x coordinate", formset, de.db.ModelUnitType.LENGTH)
    param_first.default_value = default_coordinate_value
    # The second parameter represents the Y coordinate
    param_second = de.db.ModelParam("second", "y coordinate", formset, de.db.ModelUnitType.LENGTH)
    param_second.default_value = default_coordinate_value
    # Create a PointForm netlisted and displayed as the value of the first parameter and the second parameter (x,y)
    point_form = de.db.CompoundForm("PointForm", "x,y", [param_first, param_second])
    # Note, the net_format and display_format default to displaying comma separated sub-parameters
    assert "%0s,%1s" == point_form.net_format
    assert "%0s,%1s" == point_form.display_format
    # We want parameters to display in parentheses, so we modify the display format
    point_form.display_format = "(%0s,%1s)"

    # Add the form to the library
    library.forms.add(point_form)
    # Create a formset
    point_formset = de.db.Formset("PointForms", [point_form])
    # Add the formset to the library
    library.formsets.add(point_formset)
    return point_form, point_formset

def get_default_coordinate(
    param: de.db.ModelParam, model_def: de.db.ModelDefBase, design: db_uu.Design
) -> de.db.ParamItemCompound:
    default_coordinate_param = de.db.std_string_param("0.0 mil")
    # NOTE: If the param's formset has more than one form, this callback
    # would need a way to determine which form_name to use for the compound param.
    form_name = param.formset.forms[0].name
    return de.db.compound_param(form_name, [default_coordinate_param, default_coordinate_param])

def create_workspace_and_itemdef() -> None:
    import os

    # Try and create a workspace in the home directory
    home_dir = os.environ["HOME"]
    workspace_path = os.path.join(home_dir, "workspaces/RegularPolygon_wrk")
    # Ensure there is no open workspace
    if de.workspace_is_open():
        de.close_workspace()
    # Create the workspace and library, this will throw if the workspace already exists
    de.create_workspace(workspace_path)
    de.open_workspace(workspace_path)
    library = de.create_new_library("polygon_lib", os.path.join(workspace_path, "polygon_lib"))
    # Create the item definition
    create_itemdef_example(library)

def create_itemdef_example(library: de.Library) -> None:
    from keysight.ads.de.experimental.generate_symbol import SymbolGenerator

    library.setup_schematic_tech()
    # Create the regular_polygon cell and schematic
    assert library.cell_exists("regular_polygon") is False
    cell = library.create_cell("regular_polygon")
    schematic = db_uu.create_symbol(f"{library.name}:regular_polygon:schematic")
    # Create a basic symbol for when an instance is placed in a schematic
    symbol = db_uu.create_symbol(f"{library.name}:regular_polygon:symbol")
    sym_gen = SymbolGenerator(symbol, schematic, 0.25, 0.25)
    sym_gen.is_dual_symbol_type = True
    sym_gen.should_replace = True
    sym_gen.pin_shape = "square"
    sym_gen.generate_symbol()
    symbol.save_design()
    # Create the item definition. This would normally reside itemdef.py inside the
    # cell's directory
    create_itemdef(cell)
    assert library.cell_exists("cell_sch") is False
    library.create_cell("cell_sch")
    schematic = db_uu.create_schematic(f"{library.name}:cell_sch:schematic")
    reg_poly = schematic.add_instance(
        db_uu.LCVName(library.name, "regular_polygon", "symbol"), (0, 0), name="POLY1", angle=0
    )
    reg_poly2 = schematic.add_instance(
        db_uu.LCVName(library.name, "regular_polygon", "symbol"), (3, 0), name="POLY2", angle=0
    )

    # Modify some of the parameter values
    reg_poly.parameters["sides"].value = "12"
    reg_poly.parameters["radius"].value = "150 mil"

    offset = reg_poly2.parameters["offset"]
    assert isinstance(offset, de.db.ParamCompound)
    offset.sub_params[0].value = "2.0 mil"
    offset.sub_params[1].value = "3.0 mil"
    reg_poly2.parameters["sides"].value = "16"
    reg_poly2.parameters["radius"].value = "250 mil"

    schematic.save_design()

# The artwork generation macro specified in the Customize Pcell dialog inside ADS
# The artwork generation function typically appears in a py file inside the layout view of
# your item definition
def generate_artwork_for_regular_polygon_pcell(design: db_uu.Design) -> None:
    # Retrieve the parameters from the design
    params = design.pcell_parameters
    offset_point_mks = params["offset"].value_from_list_app_type()
    number_of_sides = params["sides"].value
    assert isinstance(number_of_sides, int)
    radius = params["radius"].value
    assert isinstance(radius, float)
    orientation = params["orientation"].value
    assert isinstance(orientation, float)
    # Points are stored in MKS and need to be converted to user units
    scale_factor = design.meter_to_uu_factor
    offset_point_uu = (offset_point_mks[0] * scale_factor, offset_point_mks[1] * scale_factor)  # type: ignore
    # Generate the points for the polygon
    polygon_points = []
    for side in range(number_of_sides):
        x = (math.sin((float(side)) / number_of_sides * 2 * math.pi) * radius) * scale_factor
        y = (math.cos((float(side)) / number_of_sides * 2 * math.pi) * radius) * scale_factor
        polygon_points.append((x, y))

    outline = de.Outline(polygon_points)
    transform = de.Transform()
    # Transform the points by the offset
    transform.translate(point=(offset_point_uu[0], offset_point_uu[1]))
    # And the angle of orientation
    transform.rotate_degrees(orientation)
    outline.transform(transform, 0.0)
    layer_id = design.create_layer_id("cond")
    # Place the polygon on the design
    design.add_polygon(layer_id, outline.points)

# Run this example inside the ADS Python console.
# Open up cell_sch:schematic, select Simulate -> Generate Netlist
# TODO: Throws an error if the workspace already exists, fix
# if de.is_pde_app():
#    create_workspace_and_itemdef()
```

On this page

[Previous

Component Parameters](ex_parameters.md)
[Next

Model Definition Properties](ex_model.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top