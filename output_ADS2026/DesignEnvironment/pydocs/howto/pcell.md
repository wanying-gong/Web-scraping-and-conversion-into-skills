<!-- 来源: pydocs\howto\pcell.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../index.md)
* [How-To](index.md)
* Develop a Python Pcell in ADS

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../intro/index.md)
* [How-To](index.md)
  + [Use Python in the ADS Application](embedded.md)
  + [Set Up a Python Virtual Environment](venv.md)
  + [Set Up Visual Studio Code for Development](vscode.md)
  + [Use Pytest](pytest.md)
  + [Enable Python Support For Your Library](python_integration.md)
  + [Execute Python Scripts in Different Contexts](execution.md)
  + [Export Workspace and Design Objects to Python](exporter.md)
  + [Record Actions in ADS as Python Code](recorder.md)
  + Develop a Python Pcell in ADS
* [ADS Concepts](../concepts/index.md)
  + [Workspace Elements](../concepts/workspace_elements.md)
  + [Connectivity Objects](../concepts/connectivity.md)
* [Reference](../../reference.md)
  + [Deprecated APIs](../py/_generated/deprecations.md)
  + [Design Environment](../../pypde/docs/reference/index.md)
    - [keysight.ads.de](../../pypde/docs/reference/de/index.md)
      * [ADS Application Environment](../../pypde/docs/reference/de/ads_environment.md)
      * [ADS Workspace Components](../../pypde/docs/reference/de/workspace_components.md)
      * [Design Hierarchy](../../pypde/docs/reference/de/design_hierarchy.md)
      * [Smart Package](../../pypde/docs/reference/de/package.md)
      * [Geometry](../../pypde/docs/reference/de/geometry.md)
      * [Collections](../../pypde/docs/reference/de/collections.md)
      * [Printer](../../pypde/docs/reference/de/printer.md)
    - [keysight.ads.de.ael](../../pypde/docs/reference/de/ael.md)
    - [keysight.ads.de.app](../../pypde/docs/reference/de/app/index.md)
      * [Application](../../pypde/docs/reference/de/app/application.md)
      * [Actions and Menus](../../pypde/docs/reference/de/app/action.md)
      * [Addons](../../pypde/docs/reference/de/app/addon.md)
      * [Window and Design Callbacks](../../pypde/docs/reference/de/app/callbacks.md)
      * [Windows and Widgets](../../pypde/docs/reference/de/app/window.md)
      * [Experimental](../../pypde/docs/reference/de/app/experimental.md)
    - [keysight.ads.de.app.dds](../../pypde/docs/reference/de/app/dds.md)
      * [exec\_python](../../pypde/docs/reference/de/app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../pypde/docs/reference/de/db/index.md)
      * [Models, Parameters, and Forms](../../pypde/docs/reference/de/db/parameters.md)
      * [Properties](../../pypde/docs/reference/de/db/properties.md)
      * [Preferences](../../pypde/docs/reference/de/db/preferences.md)
      * [Transaction](../../pypde/docs/reference/de/db/transaction.md)
      * [Smart Mount](../../pypde/docs/reference/de/db/smart_mount.md)
      * [Geometry](../../pypde/docs/reference/de/db/geometry.md)
      * [Teardrops](../../pypde/docs/reference/de/db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../pypde/docs/reference/de/db_dbu/index.md)
      * [DbBox](../../pypde/docs/reference/de/db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../pypde/docs/reference/de/db_uu/index.md)
      * [Database Objects](../../pypde/docs/reference/de/db_uu/database_objects.md)
      * [Iterators](../../pypde/docs/reference/de/db_uu/iterators.md)
      * [Designs](../../pypde/docs/reference/de/db_uu/design.md)
      * [Teardrops](../../pypde/docs/reference/de/db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../../pypde/docs/reference/de/experimental/index.md)
      * [CDF](../../pypde/docs/reference/de/experimental/cdf.md)
      * [Design Commands](../../pypde/docs/reference/de/experimental/commands.md)
      * [Component Handles](../../pypde/docs/reference/de/experimental/handles.md)
      * [Netlist Utilities](../../pypde/docs/reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../pypde/docs/reference/de/experimental/polygon_utils.md)
      * [xxPro View](../../pypde/docs/reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../pypde/docs/reference/de/experimental/symbol.md)
      * [Text Maker](../../pypde/docs/reference/de/experimental/text_maker.md)
      * [Notebook](../../pypde/docs/reference/de/experimental/notebook.md)
      * [Layer/Purpose Pairs](../../pypde/docs/reference/de/experimental/lpp.md)
    - [keysight.ads.de.tech](../../pypde/docs/reference/de/tech/index.md)
      * [Technology](../../pypde/docs/reference/de/tech/tech.md)
      * [Layers](../../pypde/docs/reference/de/tech/layers.md)
      * [Line Items](../../pypde/docs/reference/de/tech/line_items.md)
      * [Padstacks](../../pypde/docs/reference/de/tech/pads.md)
      * [Rules](../../pypde/docs/reference/de/tech/rule.md)
  + [Substrate](../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../examples.md)
  + [Design Environment](../../pypde/docs/examples/index.md)
    - [Workspace Creation](../../pypde/docs/examples/workspace/ex_workspace.md)
    - [Design Creation](../../pypde/docs/examples/design_creation/index.md)
      * [Create Layout](../../pypde/docs/examples/design_creation/ex_create_layout.md)
      * [Create Schematic](../../pypde/docs/examples/design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../../pypde/docs/examples/design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../../pypde/docs/examples/design_elements/index.md)
      * [Placing Text](../../pypde/docs/examples/design_elements/ex_place_text.md)
      * [Moving Objects](../../pypde/docs/examples/design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../../pypde/docs/examples/design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../../pypde/docs/examples/design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../../pypde/docs/examples/design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../../pypde/docs/examples/design_elements/ex_plane_editing.md)
    - [Parameters](../../pypde/docs/examples/parameters/index.md)
      * [Interoperable Component Parameters](../../pypde/docs/examples/parameters/ex_cdf.md)
      * [Working with VAR](../../pypde/docs/examples/parameters/ex_working_with_var.md)
      * [Component Parameters](../../pypde/docs/examples/parameters/ex_parameters.md)
      * [Creating an Item Definition](../../pypde/docs/examples/parameters/ex_itemdef.md)
      * [Model Definition Properties](../../pypde/docs/examples/parameters/ex_model.md)
      * [Creating a Text Form](../../pypde/docs/examples/parameters/ex_text_form.md)
      * [Properties](../../pypde/docs/examples/parameters/ex_properties.md)
    - [Technology](../../pypde/docs/examples/technology/index.md)
      * [Padstacks and Vias](../../pypde/docs/examples/technology/ex_padstack.md)
      * [Nested Technology](../../pypde/docs/examples/technology/ex_nested.md)
      * [Rules](../../pypde/docs/examples/technology/ex_rules.md)
    - [Translators](../../pypde/docs/examples/translators/index.md)
      * [DXF Import and Export](../../pypde/docs/examples/translators/ex_translate_dxf.md)
      * [Gerber Export](../../pypde/docs/examples/translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../../pypde/docs/examples/translators/ex_translate_gds.md)
    - [UI](../../pypde/docs/examples/ui/index.md)
      * [Creating Custom Menus Using an Addon](../../pypde/docs/examples/ui/ex_menu_addon.md)
      * [PySide](../../pypde/docs/examples/ui/ex_pyside.md)
    - [Utility](../../pypde/docs/examples/utility/index.md)
      * [Calling Between AEL and Python](../../pypde/docs/examples/utility/ex_calling_ael_and_python.md)
      * [Smart Package](../../pypde/docs/examples/utility/ex_smart_pkg.md)
      * [XML RPC](../../pypde/docs/examples/utility/ex_xml_rpc.md)
  + [Substrate](../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../genindex.md)

# Develop a Python Pcell in ADS[](#develop-a-python-pcell-in-ads "Link to this heading")

A Pcell allows a specific view to be created programmatically based on parameters of the cell. The parameters often alter the appearance of the Pcell by specifying a size or shape.

Below is a list of steps to create a Pcell in ADS using Python. As you become more proficient with developing Pcells, you may be able to automate, skip and/or streamline some of the steps described below.

The workspace for this example is located at `%HPEESOF_DIR%\doc\python\de\examples\pcell`.

1. In this example, we create a new layout in a cell called “pcell\_example” and manually draw the artwork for the component. Before programming how things should look, use the ADS GUI to draw the artwork and get a feel for how the component should look.

> [![../../_images/Pcell_draw_artwork-1.gif](../../_images/Pcell_draw_artwork-1.gif)](../../_images/Pcell_draw_artwork-1.gif)

2. Use the `Python Exporter` to generate the Python that draws the artwork for you. See [Export Workspace and Design Objects to Python](exporter.md#python-exporter) for more information on how to use the Python Exporter.

> ```
> # fmt: off
> # This script was generated during the creation of the pcell_example documentation and doesn't represent
> # the final state of the design as included in the pcell_example layout.
> # These comments were manually added to this script; the below code was generated by the ADS Python Exporter.
> from pathlib import Path
>
> from keysight.ads import de
> from keysight.ads.de import PointF
> from keysight.ads.de import db_uu as db
>
> # This script was exported from the original design: "Pcell_Example_lib:pcell_example:layout"
> assert de.version() >= 630
>
> lib = de.get_open_library("Pcell_Example_lib")
> cell = lib.get_cell_if_exists("pcell_example_script")
> if cell is None:
>     cell = lib.create_cell("pcell_example_script")
> view = cell.create_view("layout", "maskLayout")
> # View files
>
> original_view_path = Path("C:/Program Files/Keysight/ADS2026/doc/python/de/examples/pcell/Pcell_Example_wrk/Pcell_Example_lib/pcell_example/layout")
> view.copy_file(original_view_path / "pcell.py")
>
> design = db.create_layout("Pcell_Example_lib:pcell_example_script:layout")
> design = db.open_design("Pcell_Example_lib:pcell_example_script:layout")
>
> # Terms
> net = design.add_net("P1")
> term = design.add_term(net, "P1")
> shape = design.add_dot(db.LayerId(4), loc=PointF(-40.0, 0.0))
> pin = design.add_pin(term, shape, angle=180.0, add_annot=False)
>
> net = design.nets["P1"]
> term = design.add_term(net, "P2")
> shape = design.add_dot(db.LayerId(4), loc=PointF(40.0, 0.0))
> pin = design.add_pin(term, shape, add_annot=False)
>
> net = design.nets["P1"]
> term = design.add_term(net, "P3")
> shape = design.add_dot(db.LayerId(4), loc=PointF(0.0, -50.0))
> pin = design.add_pin(term, shape, angle=-90.0, add_annot=False)
>
> # Shapes
> points = [PointF(x=-40.0, y=10.0), PointF(x=-40.0, y=-10.0), PointF(x=-10.0, y=-10.0), PointF(x=-10.0, y=-50.0), PointF(x=10.0, y=-50.0), PointF(x=10.0, y=-10.0), PointF(x=40.0, y=-10.0), PointF(x=40.0, y=10.0)]
> shape = design.add_polygon(db.LayerId(4), polygon=points)
> shape.net = design.nets["P1"]
>
> design.save_design()
> design = None
> ```

3. Take the above code and wrap the drawing portion inside a function (ignore the pin placement code for now). Initially, this function will take no parameters from your component as we are not yet ready to add parameters to our Pcell. Save this code into a file called `pcell.py` in the directory for your cell. For this example, it is located as `pcell_example\layout\pcell.py`.

> **NOTE:** You can name the file and function whatever you want, but it needs to be located in the library containing the cell, and for this example we use `pcell.py`.
>
> ```
> def generate_hardcoded_artwork(design: db.Design) -> None:
>     """Generate the pcell artwork as a T-shaped polygon with hardcoded values.
>
>     This function is for illustration purposes and uses hardcoded values for the T shape.
>     """
>     points = [
>         PointF(x=-40.0, y=10.0),
>         PointF(x=-40.0, y=-10.0),
>         PointF(x=-10.0, y=-10.0),
>         PointF(x=-10.0, y=-50.0),
>         PointF(x=10.0, y=-50.0),
>         PointF(x=10.0, y=-10.0),
>         PointF(x=40.0, y=-10.0),
>         PointF(x=40.0, y=10.0),
>     ]
>     design.add_polygon(db.LayerId(4), polygon=points)
> ```

4. You’ll find that development and verification of your code is much easier using a debugger in an IDE, so you may want to separate the implementation of your artwork function such that is can be called from test code outside the restrictions of Pcell evaluation inside ADS.

> See [Set Up Visual Studio Code for Development](vscode.md#setup-vscode) for more information on how to set up a Python IDE to work with ADS.
>
> Split the above code into two parts: the first part will be test code that calls the function to generate the artwork, and the second part will be the artwork generation function.
>
> **NOTE:** For your testing, you will need a workspace and library to work with. The below code uses the provided workspace and assumes it is already open, but you will likely want to use a test workspace specific to your development environment. While you can copy and paste code into the Python console in ADS, you’ll discover that automation mode is much more efficient for development and debugging.
> Additionally, your ADS installation directory may be in a read-only area, so you may want to copy the pcell\_example library to a writable location before running this code.
>
> **NOTE:** [Smart Package](../../pypde/docs/examples/utility/ex_smart_pkg.md#ex-smart-pkg) is the recommended mechanism for importing your custom modules in ADS.
>
> ```
> import os
> from keysight.ads import de
> from keysight.ads.de import PointF
> from keysight.ads.de import db_uu as db
>
> assert de.version() >= 630
>
> design = db.create_layout("Pcell_Example_lib:pcell_example_script:layout")
> design = db.open_design("Pcell_Example_lib:pcell_example_script:layout")
>
> # NOTE: Your ADS installation directory may be in a read-only area, so you may want to copy the pcell_example library to a writable location before running this code.
> path_to_pcell = de.hpeesof_path() + "/doc/python/de/examples/pcell/Pcell_Example_wrk/Pcell_Example_lib/pcell_example/layout"
> de.add_smart_package("layout", path_to_pcell)
> pcell_module = de.get_smart_package_module("layout.pcell")
>
> # generate_hardcoded_artwork contains the polygon generated by the Python Exporter.
> # Eventually, this will be replaced with a function that generates the artwork based on parameters.
> pcell_module.generate_hardcoded_artwork(design)
>
> design.save_design()
> design = None
> ```

5. Now that you have an environment to test your code, you can begin to parameterize your implementation:

> ```
> def compute_T(vertW: float, vertH: float, horizW: float, horizH: float) -> list[tuple[float, float]]:
>     """Compute the points of a T-shaped figure composed of two rectangles.
>
>     Parameters
>     ----------
>         vertW (float): Width of the vertical rectangle.
>         vertH (float): Height of the vertical rectangle.
>         horizW (float): Width of the horizontal rectangle.
>         horizH (float): Height of the horizontal rectangle.
>
>     The origin (0, 0) is at the center of the vertical rectangle and the center of the total T height.
>
>     Returns
>     -------
>         List of (x, y) tuples representing the polygon points in counter-clockwise order.
>
>     """
>     half_vertW = vertW / 2
>     half_vertH = vertH / 2
>     half_horizW = horizW / 2
>
>     # Vertical offset to center the T at (0, 0)
>     shift_y = -(vertH + horizH) / 2
>
>     return [
>         (-half_vertW, -half_vertH + shift_y),  # Bottom-left of vertical
>         (half_vertW, -half_vertH + shift_y),  # Bottom-right of vertical
>         (half_vertW, half_vertH + shift_y),  # Top-right of vertical
>         (half_horizW, half_vertH + shift_y),  # Bottom-right of horizontal
>         (half_horizW, half_vertH + horizH + shift_y),  # Top-right of horizontal
>         (-half_horizW, half_vertH + horizH + shift_y),  # Top-left of horizontal
>         (-half_horizW, half_vertH + shift_y),  # Bottom-left of horizontal
>         (-half_vertW, half_vertH + shift_y),  # Top-left of vertical
>     ]
> ```
>
> Continue the process of development and testing, periodically checking your design in ADS to verify it looks as expected.

6. There are different ways to create the item definition for your component. You can use the ADS GUI (**File -> Design Parameters…**), which will save it in an AEL file, called itemdef.ael.

> See [Cell Parameters](..%5C..%5C..%5C..%5C..%5Cads%5CContent%5Cads2026update2%5Cusrguide%5CDefining_and_Editing_Item_Definition.md#DefiningandEditingItemDefinition-DefiningDesignCharacteristics) for more information and adding parameters to your component inside ADS.
>
> This is useful for components that you only wish to implement the artwork generation in Python and don’t need or want to programmatically generate the item definition in Python.
>
> For other situations, where you want more programmatic control over the item definition, you can use the ADS Python API to create them.
>
> The following code is located in a file called `itemdef.py` in the same directory as your cell. The create\_itemdef function is automatically called by ADS.
> See [Cell Initialization](python_integration.md#cell-initialization) for more information on cell initialization.
>
> ```
> from keysight.ads import de
>
>
> # Simple item definition for a component that has two dimensions of rectangles representing the T shape.
> def create_itemdef(cell: de.Cell) -> None:
>     """Create the item definition for a line-like pcell."""
>     lib = cell.library
>
>     param_horizW = de.db.ModelParam(
>         "horizW", "Horizontal Width", unit_type=de.db.ModelUnitType.NO_UNIT, param_type=de.db.ModelParamType.REAL
>     )
>     param_horizW.default_value = de.db.std_string_param("100.0")
>     param_horizW.is_optimizable = True
>     param_horizW.is_statistical = True
>
>     param_horizH = de.db.ModelParam(
>         "horizH", "Horizontal Height", unit_type=de.db.ModelUnitType.NO_UNIT, param_type=de.db.ModelParamType.REAL
>     )
>     param_horizH.default_value = de.db.std_string_param("20.0")
>     param_horizH.is_optimizable = True
>     param_horizH.is_statistical = True
>
>     param_vertW = de.db.ModelParam(
>         "vertW", "Vertical Width", unit_type=de.db.ModelUnitType.NO_UNIT, param_type=de.db.ModelParamType.REAL
>     )
>     param_vertW.default_value = de.db.std_string_param("20.0")
>     param_vertW.is_optimizable = True
>     param_vertW.is_statistical = True
>
>     param_vertH = de.db.ModelParam(
>         "vertH", "Vertical Height", unit_type=de.db.ModelUnitType.NO_UNIT, param_type=de.db.ModelParamType.REAL
>     )
>     param_vertH.default_value = de.db.std_string_param("60.0")
>     param_vertH.is_optimizable = True
>     param_vertH.is_statistical = True
>
>     tee_item = de.db.ModelDef(cell.name, cell.name)
>     tee_item.inst_name_prefix = "T"
>     tee_item.is_sub_design = False
>     tee_item.parameters = [param_horizW, param_horizH, param_vertW, param_vertH]
>     de.add_model_definition(lib, tee_item)
> ```

7. Now that the parameters for your component have been defined, you can specify which ones will be considered pcell parameters. Pcell parameters are accessed via the pcell\_parameters property from `Design`.

> To specify the parameters via Python, create an instance of `PCellInfo`. By default, PCellInfo will treat every parameter in your component as a Pcell parameter, but you can itemize them with the `artwork_arg_list` property.
>
> ```
> def make_design_a_pcell() -> None:
>     # NOTE: This code assumes the library containing your cell is open.
>     from keysight.ads.de import db_uu as db
>
>     design = db.open_design("Pcell_Example_lib:pcell_example:layout", de.db.DesignMode.APPEND) # or WRITE mode
>
>     pcell_info = db.PCellInfo("PythonMacro")
>     pcell_info.python_function = "__cell__.__view__.pcell.generate_pcell_artwork" # Alternatively, you can use the cell and view names directly, "pcell_example.layout.pcell.generate_pcell_artwork"
>     pcell_info.artwork_args = ["vertW, vertH, horizW, horizH"] # If you want all parameters as pcell parameters, you can omit this line.
>     pcell_info.make_pcell(design)
>
>     design.save_design() # Save the design to make the changes permanent
> ```
>
> To manually specify which parameters are pcell parameters, you can do so using the **File -> Customize Pcell…** menu option. From there, you can copy the parameters from the item definition, or another design, or add or remove parameters from the list of pcell parameters. When you are satisfied, click **OK** and save the changes.
>
> [![../../_images/Pcell_draw_artwork-2.gif](../../_images/Pcell_draw_artwork-2.gif)](../../_images/Pcell_draw_artwork-2.gif)

8. Now that you have an item definition and your Pcell parameters have been defined, you can now update your artwork generation function to use the parameters from your pcell.

> ```
> from keysight.ads import de
> from keysight.ads.de import PointF
> from keysight.ads.de import db_uu as db
>
>
> def generate_pcell_artwork(design: db.Design) -> None:
>     """Generate the pcell artwork as a T-shaped polygon in the specified layer.
>
>     This function is called by ADS when the Pcell is evaluated.
>
>     The T shape is defined by two rectangles:
>     - A vertical rectangle (vertW x vertH)
>     - A horizontal rectangle (horizW x horizH) sitting on top of the vertical one
>
>     The origin (0, 0) is at the center of the vertical rectangle and the center of the total T height.
>
>     Pins are placed at the center of the ends of the horizontal rectangle and the center of the bottom of the vertical rectangle.
>     """
>     params = design.pcell_parameters
>
>     vertW = params["vertW"].value
>     vertH = params["vertH"].value
>     horizW = params["horizW"].value
>     horizH = params["horizH"].value
>
>     assert isinstance(vertW, float), "vertW must be a float"
>     assert isinstance(vertH, float), "vertH must be a float"
>     assert isinstance(horizW, float), "horizW must be a float"
>     assert isinstance(horizH, float), "horizH must be a float"
>
>     # Common function to generate artwork, which can be used in both pcell and non-pcell contexts
>     _generate_artwork(design, vertW, vertH, horizW, horizH)
>
>
> def generate_artwork_from_instance(instance: db.Instance, design: db.Design) -> None:
>     """Generate artwork for the instance into the specified design.
>
>     This is a function that can be used for testing your pcell artwork generation function.
>
>     You can also call the artwork function directly, varying the values of the parameters, as needed.
>     """
>     vertW_param = instance.parameters["vertW"]
>     vertH_param = instance.parameters["vertH"]
>     horizW_param = instance.parameters["horizW"]
>     horizH_param = instance.parameters["horizH"]
>
>     assert de.db.Param.is_string(vertW_param)
>     assert de.db.Param.is_string(vertH_param)
>     assert de.db.Param.is_string(horizW_param)
>     assert de.db.Param.is_string(horizH_param)
>
>     # Parameters from an instance have not been evaluated, so we need to evaluate them
>     parent = instance.parent
>     expr_context = de.db.ExpressionContext()
>     expr_context.setup_hierarchy_for_layout_only(parent)
>
>     vertW = float(expr_context.evaluate_expression(vertW_param.value))
>     vertH = float(expr_context.evaluate_expression(vertH_param.value))
>     horizW = float(expr_context.evaluate_expression(horizW_param.value))
>     horizH = float(expr_context.evaluate_expression(horizH_param.value))
>
>     _generate_artwork(design, vertW, vertH, horizW, horizH)
>
>
> def _generate_artwork(design: db.Design, vertW: float, vertH: float, horizW: float, horizH: float) -> None:
>     """Compute the T-shaped figure, and add it and some pins to the design."""
>     points = compute_T(vertW, vertH, horizW, horizH)
>     layer_id = db.LayerId(4)
>     design.add_polygon(layer_id, points)
>
>     # Add pins to the design
>     pin_locs = compute_pin_locations(vertW, vertH, horizW, horizH)
>     # The Terms for the Pins will be named P1, P2, P3
>     with de.db.Transaction(design) as trans:
>         for term_number, pin_loc in enumerate(pin_locs, start=1):
>             term_name = "P" + str(term_number)
>             dot = design.add_dot(layer_id, pin_loc)
>             net = design.find_or_add_net(term_name)
>             term = design.add_term(net, term_name)
>             design.add_pin(term, dot)
>         trans.commit()
>
>
> def compute_T(vertW: float, vertH: float, horizW: float, horizH: float) -> list[tuple[float, float]]:
>     """Compute the points of a T-shaped figure composed of two rectangles.
>
>     Parameters
>     ----------
>         vertW (float): Width of the vertical rectangle.
>         vertH (float): Height of the vertical rectangle.
>         horizW (float): Width of the horizontal rectangle.
>         horizH (float): Height of the horizontal rectangle.
>
>     The origin (0, 0) is at the center of the vertical rectangle and the center of the total T height.
>
>     Returns
>     -------
>         List of (x, y) tuples representing the polygon points in counter-clockwise order.
>
>     """
>     half_vertW = vertW / 2
>     half_vertH = vertH / 2
>     half_horizW = horizW / 2
>
>     # Vertical offset to center the T at (0, 0)
>     shift_y = -(vertH + horizH) / 2
>
>     return [
>         (-half_vertW, -half_vertH + shift_y),  # Bottom-left of vertical
>         (half_vertW, -half_vertH + shift_y),  # Bottom-right of vertical
>         (half_vertW, half_vertH + shift_y),  # Top-right of vertical
>         (half_horizW, half_vertH + shift_y),  # Bottom-right of horizontal
>         (half_horizW, half_vertH + horizH + shift_y),  # Top-right of horizontal
>         (-half_horizW, half_vertH + horizH + shift_y),  # Top-left of horizontal
>         (-half_horizW, half_vertH + shift_y),  # Bottom-left of horizontal
>         (-half_vertW, half_vertH + shift_y),  # Top-left of vertical
>     ]
>
>
> def compute_pin_locations(vertW: float, vertH: float, horizW: float, horizH: float) -> list[tuple[float, float]]:
>     """Compute the pin locations for the T-shaped figure.
>
>     The pins are placed at the center of the ends of the horizontal rectangle and the center of the bottom of the vertical rectangle.
>     """
>     half_vertH = vertH / 2
>     half_horizW = horizW / 2
>     half_horizH = horizH / 2
>
>     # Vertical offset to center the T at (0, 0)
>     shift_y = -(vertH + horizH) / 2
>
>     return [
>         (half_horizW, half_vertH + half_horizH + shift_y),  # Center of horizontal right
>         (-half_horizW, half_vertH + half_horizH + shift_y),  # Center of horizontal left
>         (0.0, -half_vertH + shift_y),  # Center of vertical bottom
>     ]
>
>
> # This function is for illustration purposes and uses hardcoded values for the T shape, as shown in the ADS Python documentation.
> def generate_hardcoded_artwork(design: db.Design) -> None:
>     """Generate the pcell artwork as a T-shaped polygon with hardcoded values.
>
>     This function is for illustration purposes and uses hardcoded values for the T shape.
>     """
>     points = [
>         PointF(x=-40.0, y=10.0),
>         PointF(x=-40.0, y=-10.0),
>         PointF(x=-10.0, y=-10.0),
>         PointF(x=-10.0, y=-50.0),
>         PointF(x=10.0, y=-50.0),
>         PointF(x=10.0, y=-10.0),
>         PointF(x=40.0, y=-10.0),
>         PointF(x=40.0, y=10.0),
>     ]
>     design.add_polygon(db.LayerId(4), polygon=points)
>
>
> # fmt: off
> def make_design_a_pcell() -> None:
>     # NOTE: This code assumes the library containing your cell is open.
>     from keysight.ads.de import db_uu as db
>
>     design = db.open_design("Pcell_Example_lib:pcell_example:layout", de.db.DesignMode.APPEND) # or WRITE mode
>
>     pcell_info = db.PCellInfo("PythonMacro")
>     pcell_info.python_function = "__cell__.__view__.pcell.generate_pcell_artwork" # Alternatively, you can use the cell and view names directly, "pcell_example.layout.pcell.generate_pcell_artwork"
>     pcell_info.artwork_args = ["vertW, vertH, horizW, horizH"] # If you want all parameters as pcell parameters, you can omit this line.
>     pcell_info.make_pcell(design)
>
>     design.save_design() # Save the design to make the changes permanent
> # fmt: on
> ```

9. At this point, you are able to place your component in a new layout. From the `Parts` panel, search for your component and place one or more in a design.

> [![../../_images/Pcell_draw_artwork-3.gif](../../_images/Pcell_draw_artwork-3.gif)](../../_images/Pcell_draw_artwork-3.gif)

10. As validation of your component artwork inside ADS, you can double-click on the component and modify the values of the parameters. Click **OK** to apply the changes and see the updated artwork in the layout.

> [![../../_images/Pcell_draw_artwork-4.gif](../../_images/Pcell_draw_artwork-4.gif)](../../_images/Pcell_draw_artwork-4.gif)

On this page

[Previous

Record Actions in ADS as Python Code](recorder.md)
[Next

ADS Concepts](../concepts/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top