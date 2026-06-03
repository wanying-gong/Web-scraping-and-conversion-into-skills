# Design Examples (pypde)
> **说明：** 完整示例代码（23 个）：创建原理图、布局、工作区、仿真+绘图、调用 AEL、CDF 组件参数、模型定义、LPF、属性、自定义菜单/插件、焊盘/过孔、嵌套工艺、规则、放置文字、多边形、PySide2 UI、层级遍历、VAR 变量、XML-RPC、GDS 导入导出。

> **何时使用：** 当你需要参考完整的可运行示例代码时

---

## 本文件目录

- **Examples** (`pypde/docs/examples/index.md`)
- **Calling Between AEL and Python** (`pypde/docs/examples/ex_calling_ael_and_python.md`)
- **Create Layout** (`pypde/docs/examples/ex_create_layout.md`)
- **Create Schematic** (`pypde/docs/examples/ex_create_schematic.md`)
- **Create Workspace** (`pypde/docs/examples/ex_workspace.md`)
- **Create, Simulate, and Plot** (`pypde/docs/examples/ex_create_sim_and_plot.md`)
- **Interoperable Component Parameters** (`pypde/docs/examples/ex_cdf.md`)
- **Component Parameters** (`pypde/docs/examples/ex_parameters.md`)
- **Creating an Item Definition** (`pypde/docs/examples/ex_itemdef.md`)
- **Model Definition Properties** (`pypde/docs/examples/ex_model.md`)
- **Adding Instances to a Design** (`pypde/docs/examples/ex_lpf.md`)
- **Properties** (`pypde/docs/examples/ex_properties.md`)
- **Creating Custom Menus Using an Addon** (`pypde/docs/examples/ex_menu_addon.md`)
- **Padstacks and Vias** (`pypde/docs/examples/ex_padstack.md`)
- **Nested Technology** (`pypde/docs/examples/ex_nested.md`)
- **Rules** (`pypde/docs/examples/ex_rules.md`)
- **Placing Text** (`pypde/docs/examples/ex_place_text.md`)
- **Paths, Traces, and Polygons** (`pypde/docs/examples/ex_polygon.md`)
- **PySide2** (`pypde/docs/examples/ex_pyside.md`)
- **Traversing Hierarchy** (`pypde/docs/examples/ex_traversing_hierarchy.md`)
- **Working with VAR** (`pypde/docs/examples/ex_working_with_var.md`)
- **XML RPC** (`pypde/docs/examples/ex_xml_rpc.md`)
- **GDSII Import and Export** (`pypde/docs/examples/ex_translate_gds.md`)

---

<!-- === 来源: pypde/docs/examples/index.md === -->

# Examples[](#examples "Link to this heading")

The source code for the examples referenced by these help pages can be found in **$HPEESOF\_DIR/de/python**

Contents:

* [Calling Between AEL and Python](ex_calling_ael_and_python.md)
  + [Python Interface to AEL](ex_calling_ael_and_python.md#python-interface-to-ael)
* [Create Layout](ex_create_layout.md)
* [Create Schematic](ex_create_schematic.md)
* [Create Workspace](ex_workspace.md)
* [Create, Simulate, and Plot](ex_create_sim_and_plot.md)
* [Interoperable Component Parameters](ex_cdf.md)
* [Component Parameters](ex_parameters.md)
* [Creating an Item Definition](ex_itemdef.md)
* [Model Definition Properties](ex_model.md)
* [Adding Instances to a Design](ex_lpf.md)
* [Properties](ex_properties.md)
* [Creating Custom Menus Using an Addon](ex_menu_addon.md)
* [Padstacks and Vias](ex_padstack.md)
* [Nested Technology](ex_nested.md)
* [Rules](ex_rules.md)
* [Placing Text](ex_place_text.md)
* [Paths, Traces, and Polygons](ex_polygon.md)
* [PySide2](ex_pyside.md)
* [Traversing Hierarchy](ex_traversing_hierarchy.md)
* [Working with VAR](ex_working_with_var.md)
* [XML RPC](ex_xml_rpc.md)
  + [Server](ex_xml_rpc.md#server)
  + [Client](ex_xml_rpc.md#client)
* [GDSII Import and Export](ex_translate_gds.md)


---

<!-- === 来源: pypde/docs/examples/ex_calling_ael_and_python.md === -->

# Calling Between AEL and Python[](#calling-between-ael-and-python "Link to this heading")

## Python Interface to AEL[](#python-interface-to-ael "Link to this heading")

See AEL Python Examples located [here](../../../../../../../ael/python/docs/html/examples/ex_calling_ael_and_python.md).


---

<!-- === 来源: pypde/docs/examples/ex_create_layout.md === -->

# Create Layout[](#create-layout "Link to this heading")

This example creates a microstrip layout in a default technology. It adds pins to the design and prepares an RFPro simulation view. It requires that you have a workspace open with a library that does not already have a cell called “cell\_lay”.

```
def create_layout_and_add_pins_to_design_and_run_pro_view(library: de.Library) -> None:
    from keysight.ads import de
    from keysight.ads.de import db_uu

    design = db_uu.create_layout(f"{library.name}:cell_lay:layout")
    layer_id = design.create_layer_id("cond")
    design.add_rectangle(layer_id, (0.0, 0.0), (100.0, 10.0))
    design.add_rectangle(layer_id, (0.0, 20.0), (100.0, 30.0))
    dot = design.add_dot(layer_id, (0.0, 5.0))
    net = design.find_or_add_net("P1")
    term = design.add_term(net, "P1")
    design.add_pin(term, dot)
    dot = design.add_dot(layer_id, (100.0, 5.0))
    net = design.find_or_add_net("P2")
    term = design.add_term(net, "P2")
    design.add_pin(term, dot)
    dot = design.add_dot(layer_id, (0.0, 25.0))
    net = design.find_or_add_net("P3")
    term = design.add_term(net, "P3")
    design.add_pin(term, dot)
    dot = design.add_dot(layer_id, (100.0, 25.0))
    net = design.find_or_add_net("P4")
    term = design.add_term(net, "P4")
    design.add_pin(term, dot)
    design.save_design()

    # de.experimental.create_pro_view won't work in automation mode but will work while running inside ADS
    if de.is_pde_app():
        de.experimental.create_pro_view(
            db_uu.LCVName(f"{library.name}", "cell_lay", "rfpro"),
            "rfpro",
            db_uu.LCVName(f"{library.name}", "cell_lay", "layout"),
            "tech",
        )
```


---

<!-- === 来源: pypde/docs/examples/ex_create_schematic.md === -->

# Create Schematic[](#create-schematic "Link to this heading")

This example creates a schematic of an RLC filter, and adds a simulation controller. It requires that you have a workspace open with a library that does not already have a cell called “cell\_sch”.

```
def create_schematic_and_add_instances_to_design(library: de.Library) -> None:
    from keysight.ads.de import db_uu

    design = db_uu.create_schematic(f"{library.name}:cell_sch:schematic")
    design.add_instance(db_uu.LCVName("ads_simulation", "Term", "symbol"), (-2, 0), name="P1", angle=-90)
    design.add_instance(db_uu.LCVName("ads_simulation", "Term", "symbol"), (4, 0), name="P2", angle=-90)
    design.add_instance(db_uu.LCVName("ads_rflib", "GROUND", "symbol"), (-2, -1), name="", angle=-90)
    design.add_instance(db_uu.LCVName("ads_rflib", "GROUND", "symbol"), (4, -1), name="", angle=-90)

    r = design.add_instance(db_uu.LCVName("ads_rflib", "R", "symbol"), (0, 0), name="R1", angle=0)
    ind = design.add_instance(db_uu.LCVName("ads_rflib", "L", "symbol"), (2, 0), name="L1", angle=0)
    c = design.add_instance(db_uu.LCVName("ads_rflib", "C", "symbol"), (1, -1), name="C1", angle=-90)
    design.add_instance(db_uu.LCVName("ads_rflib", "GROUND", "symbol"), (1, -2), name="GND", angle=-90)
    r.parameters["R"].value = "5 ohm"
    ind.parameters["L"].value = "2 nH"
    c.parameters["C"].value = "10 pF"

    design.add_wire([(-2.0, 0.0), (0.0, 0.0)])
    design.add_wire([(3.0, 0.0), (4.0, 0.0)])

    design.add_wire([(1.0, 0.0), (1.0, -1.0)])
    design.add_wire([(1.0, 0.0), (2.0, 0.0)])

    design.add_instance(db_uu.LCVName("ads_simulation", "S_Param", "symbol"), (0, -4), name="SP1")
    design.save_design()
```


---

<!-- === 来源: pypde/docs/examples/ex_workspace.md === -->

# Create Workspace[](#create-workspace "Link to this heading")

This example creates and opens a workspace. It uses the context manager to ensure its closed when finished

```
Usage:
with create_and_open_an_empty_workspace("workspace_path") as workspace:
    # do something with the workspace
```

```
@contextmanager
def create_and_open_an_empty_workspace(workspace_path: str) -> Iterator[de.Workspace]:
    # Ensure there isn't already a workspace open
    if de.workspace_is_open():
        de.close_workspace()

    # Cannot create a workspace if the directory already exists
    workspace_directory = Path(workspace_path)
    if workspace_directory.exists():
        raise RuntimeError(f"Workspace directory already exists: {workspace_directory}")

    # Create the workspace
    workspace = de.create_workspace(workspace_directory)
    # Opening a workspace will change the current working directory
    original_working_directory = Path(os.getcwd())
    # Open the workspace
    workspace.open()
    # Return the open workspace and close when it finished
    try:
        yield workspace
    finally:
        # Assert if this workspace is no longer the active workspace
        assert de.active_workspace().path == workspace_directory
        workspace.close()
        # Change the working directory back
        os.chdir(original_working_directory)
```

This example creates a library and adds it to an open workspace

```
Usage:
with create_and_open_an_empty_workspace("workspace_path") as workspace:
    create_a_library_and_add_it_to_the_workspace(workspace)
```

```
def create_a_library_and_add_it_to_the_workspace(workspace: de.Workspace) -> None:
    assert workspace.path is not None
    # Libraries can only be added to an open workspace
    assert workspace.is_open
    # We'll create a library in the directory of the workspace
    library_name = "example_library"
    library_path = workspace.path / library_name
    # Create the library
    de.create_new_library(library_name, library_path)
    # And add it to the workspace (update lib.defs)
    workspace.add_library(library_name, library_path, de.LibraryMode.SHARED)
```


---

<!-- === 来源: pypde/docs/examples/ex_create_sim_and_plot.md === -->

# Create, Simulate, and Plot[](#create-simulate-and-plot "Link to this heading")

This example will create a new workspace in your HOME directory called “create\_simulate\_plot\_example”. In the workspace a new library and schematic are created and populate with an RC filter. Next, the circuit will be simulated and finally the response from the filter will be plotted inline in the ADS Python console.

[![../../../_images/low_pass_filter_var.png](../../../_images/low_pass_filter_var.png)](../../../_images/low_pass_filter_var.png)

```
# Copyright Keysight Technologies 2023 - 2023
import os
from pathlib import Path

import keysight.ads.de as de
from keysight.ads.de import db_uu as db

def create_workspace_and_design_then_simulate_and_plot() -> None:
    home_dir = os.environ["HOME"]
    workspace_path = os.path.join(home_dir, "create_simulate_plot_example")

    # ensure to start from a closed workspace
    if de.workspace_is_open():
        de.close_workspace()

    # create the workspace
    workspace = de.create_workspace(workspace_path)
    workspace.open()

    create_design_then_simulate_and_plot(workspace)

def create_design_then_simulate_and_plot(workspace: de.Workspace) -> None:
    from keysight.edatoolbox import util

    target_output_dir = os.path.join(workspace.path, "output")

    # create the simulation output directory
    util.safe_makedirs(target_output_dir)

    lib_dir = os.path.join(workspace.path, "low_pass_filter_lib")
    de.create_new_library("low_pass_filter_lib", lib_dir)
    workspace.add_library("low_pass_filter_lib", lib_dir, de.LibraryMode.NON_SHARED)

    # create the schematic
    design = db.create_schematic("low_pass_filter_lib:cell:schematic")

    # add components to the schematic
    design.add_instance(("ads_sources", "V_AC", "symbol"), (-2, 0), name="SRC1", angle=-90)

    r = design.add_instance(("ads_rflib", "R", "symbol"), (0, 0), name="R1", angle=0)
    r.parameters["R"].value = "3.0 kOhm"

    c = design.add_instance(("ads_rflib", "C", "symbol"), (2, 0), name="C1", angle=-90)
    c.parameters["C"].value = "1.0 uF"

    design.add_instance(("ads_rflib", "GROUND", "symbol"), (-2, -1), angle=-90)
    design.add_instance(("ads_rflib", "GROUND", "symbol"), (2, -1), angle=-90)

    design.add_wire([(-2.0, 0.0), (0.0, 0.0)])
    wire = design.add_wire([(1.0, 0.0), (2.0, 0.0)])
    wire.add_wire_label("R1_v")

    ac = design.add_instance(("ads_simulation", "AC", "symbol"), (-4, 1), name="AC1", angle=0)

    ac.parameters["Start"].value = "1.0 Hz"
    ac.parameters["Stop"].value = "1.0 MHz"
    ac.parameters["Dec"].value = "5"
    ac.parameters["Step"].value = ""

    v = design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 2), name="VAR1", angle=-90)
    assert v.is_var_instance
    v.vars["X"] = "1.0"
    v.vars["Y"] = "X/2.0"
    design.save_design()

    # data plot cannot be run in automation mode
    if de.is_pde_app():
        simulate_and_plot(design, target_output_dir)

# plot() not testable in automation mode
def simulate_and_plot(design: db.Design, output_dir: str) -> None:
    import os

    # use the dataset module to grab the output
    import keysight.ads.dataset as dataset
    from IPython.core import getipython
    from keysight.edatoolbox import ads

    ipython = getipython.get_ipython()
    if ipython is None:
        print("The remaining portion of the script must be run in an IPython environment. Exiting.")
        return

    # capture the netlist in a string
    netlist = design.generate_netlist()

    # access to the simulator object to run netlists
    simulator = ads.CircuitSimulator()

    # run the netlist, this will block output
    simulator.run_netlist(netlist, output_dir=output_dir)

    output_data = dataset.open(Path(os.path.join(output_dir, "cell.ds")))

    # switch to a dataframe representation
    # reset the index to normalize the data
    dataf = output_data["AC1.AC"].to_dataframe().reset_index()

    # plot using matplotlib/seaborn
    import matplotlib.pyplot as plt

    # plot using inline
    ipython.run_line_magic("matplotlib", "inline")  # type: ignore

    # make sure we plot the magnitude
    import numpy as np

    def dB(x) -> float:  # noqa: ANN001
        return 10.0 * np.log10(abs(x))

    _, ax = plt.subplots()
    ax.set_xscale("log")  # type: ignore
    ax.set_title("Filter response")  # type: ignore
    plt.plot(dataf["freq"], dB(dataf["R1_v"]))

    # alternatively show as dedicated window
    # plt.show()
```


---

<!-- === 来源: pypde/docs/examples/ex_cdf.md === -->

# Interoperable Component Parameters[](#interoperable-component-parameters "Link to this heading")

Example illustrating how to access and modify the value of a parameter of an interoperable component

```
def accessing_cdf_instance_parameters(design: db_uu.Design, library: de.Library) -> None:
    from keysight.ads.de import experimental as exp

    # inst_c1 is an interoperable instance placed in the design
    inst_c1 = design.instances["C1"]
    # Retrieve the cell CDF from the 'cap' cell
    cell_cdf = exp.cdf.cell_cdf(library, "cap")
    # Create the interface to the instance CDF parameters
    inst_cdf = exp.cdf.InstanceParams(inst_c1)  # CellCDF parameter is optional when passing in an Instance
    assert cell_cdf == inst_cdf.cell_cdf
    assert inst_cdf.parent_design_uu == inst_c1.parent

    # Retrieve the parameter definition for the 'c' parameter
    # Note: There are several ways to retrieve a parameter definition, as shown below
    param_def = inst_cdf.find_param_def("c")  # Returns None if not found
    assert param_def is not None
    assert param_def == inst_cdf.param_def("c")  # Throws if not found

    # The ParamDef on the instance is the same as the ParamDef on the CellCDF
    assert param_def == cell_cdf.find_param("c")  # Returns None if not found
    assert param_def == cell_cdf.param("c")  # Throws if not found

    # Note: The CDF.params property creates a collection of all the parameter definitions and while
    # that can be quite helpful for use with a debugger, it is not recommended for use cases requiring
    # high performance
    assert param_def == cell_cdf.params["c"]  # Throws if not found

    # Like ParamDef, there are multiple ways to retrieve a Parameter
    parameter = inst_cdf.find_param("c")  # Returns None if not found
    assert parameter is not None
    assert parameter == inst_cdf.param("c")  # Throws if not found

    # The parameter can also be retrieved using the ParamDef
    assert parameter == inst_cdf.param(param_def)  # Throws if not found

    # Similar to CDF.params, the Instance.params property will create a collection of Parameter
    # and may have a performance impact; consider using the param or find_param methods
    assert parameter == inst_cdf.params["c"]

    # Retrieve the value of the Parameter
    value = parameter.value
    assert value is not None

    # There are multiple ways to get and set the value of a parameter
    assert value == inst_cdf.param_value(param_def)
    # param_value_no_default will only return a value if the value is not the default value
    assert not inst_cdf.is_modified
    assert inst_cdf.param_value_no_default(param_def) is None

    # Set the value of the parameter
    parameter.value = "3p"
    assert inst_cdf.param_value(param_def) == "3p"
    # The CDF instance is now modified and param_value_no_default will return the modified value
    assert inst_cdf.is_modified
    assert inst_cdf.param_value_no_default(param_def) == "3p"

    # Set the value of the parameter using the ParamDef
    inst_cdf.set_param_value(param_def, "4p")
    assert parameter.value == "4p"

    # Set the value of the parameter using the parameter name
    inst_cdf.set_param_value("c", "5p")
    assert parameter.value == "5p"

    # Set the value of the parameter by indexing into the params collection
    inst_cdf.params["c"].value = "6p"
    assert parameter.value == "6p"

    # NOTE: Be sure to call update_instance to apply the changes or they will be lost
    inst_cdf.update_instance(inst_c1)
    inst_c1 = design.instances["C1"]
    assert inst_cdf.param("c").value == "6p"
```

Example illustrating how to add a new parameter definition to an interoperable component before placing an instance

```
def adding_a_new_parameter_definition_to_a_cell_cdf(design: db_uu.Design, library: de.Library) -> None:
    from keysight.ads.de import experimental as exp

    # Retrieve the cell CDF from the 'cap' cell
    cell_cdf = exp.cdf.cell_cdf(library, "cap")
    # Create an interface to the CDF parameters
    inst_cdf_from_design = exp.cdf.InstanceParams(design, cell_cdf)

    # Create a new ParamDef, new_param, with a display name of "New Parameter" and a default value of 10
    new_param_def = exp.cdf.ParamDef("new_param", exp.cdf.ParamType.INT)
    new_param_def.prompt = "New Parameter"
    new_param_def.default_value = 10

    # Add the new parameter to the CellCDF
    inst_cdf_from_design.cell_cdf.add_param(new_param_def)
    # Add a new instance of cap to the design
    design.add_instance((library.lib_name, "cap", "symbol"), (0, 0), name="C2")
    # Retrieve the instance just added
    inst_c2 = design.instances["C2"]

    # Create the interface to the CDF instance parameters
    inst_cdf = exp.cdf.InstanceParams(inst_c2)
    assert inst_cdf.param("new_param").value == 10

    # Update the value after placing the instance, as desired
    inst_cdf.param("new_param").value = 25

    # NOTE: Be sure to call update_instance to apply the changes or they will be lost
    inst_c2 = design.instances["C2"]
    inst_cdf = exp.cdf.InstanceParams(inst_c2)
    # Uh-oh, we forgot to call update_instance and the change was lost!
    assert inst_cdf.param("new_param").value == 10

    # So, let's try again ...
    inst_cdf.param("new_param").value = 25
    inst_cdf.update_instance(inst_c2)

    # Verify the result by re-obtaining the instance and validating the parameter value
    inst_c2 = design.instances["C2"]
    inst_cdf = exp.cdf.InstanceParams(inst_c2)
    assert inst_cdf.param("new_param").value == 25
```


---

<!-- === 来源: pypde/docs/examples/ex_parameters.md === -->

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


---

<!-- === 来源: pypde/docs/examples/ex_itemdef.md === -->

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


---

<!-- === 来源: pypde/docs/examples/ex_model.md === -->

# Model Definition Properties[](#model-definition-properties "Link to this heading")

This example shows how to create a model definition with a model name parameter that will netlist at the front of the netlist string

```
def components_with_and_without_a_model_param_parameter(library: de.Library, design: db_uu.Design) -> None:
    # Example showing how an instance is netlisted differently when ModelDef.has_model_param is set

    # This netlist callback is implemented here to show the netlist for an instance when the
    # ModelDef.has_model_param property is or is not set. If you wish to use the default
    # netlist behavior, there is no need to implement this callback.
    def netlist_callback(std_inst: de.db.StandardInstance) -> str:
        from keysight.ads.de.experimental.netlist_helper import NetlistStringBuilder

        model_def = std_inst.model_def
        assert model_def

        netlist_builder = NetlistStringBuilder(std_inst)
        netlist = netlist_builder.clear_and_get_default_netlist_str()

        if model_def.has_model_param:
            # When has_model_param is set, the value of the first parameter is treated as the Model name and will be
            # netlisted at the front in quotes. The remaining parameters will be netlisted as normal.
            assert netlist == '"MyComp":MC1  Length=5.0 mil '
        else:
            # When has_model_param is not set, the standard netlist format will be used and the first parameter,
            # along with the remaining parameters, will be netlisted as normal.
            assert netlist == "MyComponent:MC1  Model=MyComp Length=5.0 mil "

        return netlist

    # Typically create_itemdef would be a function in a module called itemdef.py in the cell for your component
    def create_itemdef(cell: de.Cell) -> de.db.ModelDef:
        assert cell.name == "MyComponent"
        # Use the standard formset from the global model lib
        standard_formset = de.db.model_lib.formsets["StdFormSet"]
        # Create a model with a couple parameters, the first one being a string parameter representing the model name
        param_model = de.db.ModelParam("Model", "Model instance name", standard_formset, de.db.ModelUnitType.STRING)
        param_model.default_value = de.db.std_string_param("MyComp")
        # The model name parameter should be set so that it is not evaluated by the expression evaluator
        param_model.is_evaluated = False

        param_length = de.db.ModelParam("Length", "Length", standard_formset, de.db.ModelUnitType.LENGTH)
        param_length.default_value = de.db.std_string_param("5.0 mil")

        my_component = de.db.ModelDef(cell.cell_name, cell.cell_name)
        my_component.inst_name_prefix = "MC"
        my_component.is_sub_design = False
        my_component.parameters = [param_model, param_length]
        my_component.callbacks = [(de.db.ModelCb(de.db.ModelCbType.ITEM_NETLIST, netlist_callback))]
        de.add_model_definition(cell.library, my_component)
        return my_component

    # Starting with a clear schematic ...
    assert design.is_schematic
    design.clear_design()

    my_comp_cell = library.create_cell("MyComponent")
    mc_def = create_itemdef(my_comp_cell)
    create_symbol(library, my_comp_cell)
    design.add_instance((f"{library.name}", "MyComponent", "symbol"), (0, 0))

    # See netlist_callback() for the effect ModelDef.has_model_param has on the netlist
    assert mc_def.has_model_param is False
    design.generate_netlist()
    mc_def.has_model_param = True
    design.generate_netlist()
```

This example shows the transmission line property on a model definition

```
def transmission_line_property(library: de.Library, design: db_uu.Design) -> None:
    assert design.is_schematic
    design.clear_design()

    # Typically create_itemdef would be a function in a module called itemdef.py in the cell for your component
    def create_itemdef(cell: de.Cell) -> de.db.ModelDef:
        assert cell.name == "MyTLine"

        # Use the standard formset from the global model lib
        standard_formset = de.db.model_lib.formsets["StdFormSet"]

        param_width = de.db.ModelParam("W", "Line Width", standard_formset, de.db.ModelUnitType.LENGTH)
        param_width.default_value = de.db.std_string_param("25.0 mil")
        param_length = de.db.ModelParam("L", "Line Length", standard_formset, de.db.ModelUnitType.LENGTH)
        param_length.default_value = de.db.std_string_param("100.0 mil")
        param_temp = de.db.ModelParam("Temp", "Temperature", standard_formset, de.db.ModelUnitType.TEMPERATURE)
        param_temp.default_value = de.db.std_string_param("")
        param_temp.is_displayed_by_default = False

        my_tline = de.db.ModelDef(cell.cell_name, cell.cell_name)
        my_tline.parameters = [param_width, param_length, param_temp]
        my_tline.inst_name_prefix = "MTLn"
        # When defining your own transmission line components, set the is_transmission_line property to True
        my_tline.is_transmission_line = True
        de.add_model_definition(cell.library, my_tline)

        return my_tline

    my_tline_cell = library.create_cell("MyTLine")
    create_itemdef(my_tline_cell)
    create_symbol(library, my_tline_cell)
    tl_inst = design.add_instance((f"{library.name}", "MyTLine", "symbol"), (0, 0))
    tl_model = tl_inst.model_def
    assert tl_model
    assert tl_model.is_transmission_line

    # Any transmission line component provided by ADS will have the ModelDefl.is_transmission_line property set to True
    mlin_inst = design.add_instance(("ads_tlines:MLIN:symbol"), (3, 0))
    mlin_model = mlin_inst.model_def
    assert mlin_model
    assert mlin_model.is_transmission_line
```

This example shows the is\_unique property on a model definition

```
def is_unique_property(library: de.Library, design: db_uu.Design) -> None:
    assert design.is_schematic
    design.clear_design()

    # Typically create_itemdef would be a function in a module called itemdef.py in the cell for your component
    def create_itemdef(cell: de.Cell) -> de.db.ModelDef:
        # Nothing special about this component other than its is_unique property
        assert cell.cell_name == "MyUniqComp"
        my_uniq_comp = de.db.ModelDef(cell.cell_name, cell.cell_name)
        my_uniq_comp.inst_name_prefix = "MUC"
        my_uniq_comp.is_unique = True
        de.add_model_definition(cell.library, my_uniq_comp)
        return my_uniq_comp

    my_uniq_cell = library.create_cell("MyUniqComp")
    create_itemdef(my_uniq_cell)
    create_symbol(library, my_uniq_cell)
    # Placing one unique component is fine
    design.add_instance((f"{library.name}", "MyUniqComp", "symbol"), (0, 0))
    try:
        # Attempting to place another results in an error
        design.add_instance((f"{library.name}", "MyUniqComp", "symbol"), (3, 0))
    except RuntimeError as e:
        assert "This item is defined to be unique. Only one instance of this type can be placed." in str(e)
```


---

<!-- === 来源: pypde/docs/examples/ex_lpf.md === -->

# Adding Instances to a Design[](#adding-instances-to-a-design "Link to this heading")

This example adds instances of components to a design and then adds that design as an instance to another design

```
# Copyright Keysight Technologies 2023 - 2023
import os

from keysight.ads import ael, de
from keysight.ads.de import ArcOrientation, GenPolyline, PointF, db_uu
from keysight.ads.de.experimental import generate_symbol as gs

def create_lpf_circuit_workspace_design_and_simulate() -> None:
    # This workspace will reside in the user's home directory under workspaces/Instances_example_wrk
    home_dir = os.environ["HOME"]
    workspace_path = os.path.join(home_dir, "workspaces/Instances_example_wrk")

    # Ensure there is no open workspace
    if de.workspace_is_open():
        de.close_workspace()
    # Create the workspace
    de.create_workspace(workspace_path)
    workspace = de.open_workspace(workspace_path)
    # Create the library
    de.create_new_library("LPF_lib", os.path.join(workspace_path, "LPF_lib"))
    # And add it to the workspace
    workspace.add_library("LPF_lib", os.path.join(workspace_path, "LPF_lib"), de.LibraryMode.SHARED)
    # Create an empty schematic
    schematic_lpf = db_uu.create_schematic("LPF_lib:LPF:schematic")
    assert schematic_lpf is not None
    # And write out the design
    # By creating and committing a transaction, we force a connectivitiy check on the design
    transaction = de.db.Transaction(schematic_lpf, "Create schematic")
    create_an_ideal_lpf_circuit(schematic_lpf)
    transaction.commit()
    schematic_lpf.save_design()

    # Generate a symbol for the design
    symbol_lpf = create_symbol_for_ideal_lpf_circuit(schematic_lpf)

    # Create a new design in a new cell
    schematic_sp = db_uu.create_schematic("LPF_lib:LPF_SP:schematic")
    assert schematic_sp is not None
    # Designs may be referenced in multiple ways, such as with a CellviewRef
    cvr = de.CellviewRef(view=symbol_lpf.view)
    assert cvr is not None
    # Write out the new design
    transaction = de.db.Transaction(schematic_sp, "Create schematic")
    add_subcircuit_to_design_and_create_lpf_circuit(schematic_sp, cvr)
    transaction.commit()
    schematic_sp.save_design()

    # qthelp://ads.2024/doc/appguide/Designing_a_Simple_Low_Pass_Filter.html
    # TODO: Specify hierarchy policy
    # TODO: Perform schematic simulation
    # TODO: Add Parameters Sweep/Values
    # TODO: Simulate

def create_an_ideal_lpf_circuit(design: db_uu.Design) -> None:
    # ensure the design is empty
    design.clear_design()
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)

    # Add an input pin to the design
    net = design.find_or_add_net("P1")
    term = design.add_term(net, "P1", db_uu.TermType.INPUT)
    dot = design.add_dot(layer_id, (0.0, 0.0))
    # Pin angle may be passed into the constructor, or
    pin = design.add_pin(term, dot, angle=0.0)
    # The pin angle may be modified after being placed
    pin.angle = 180.0
    # And when setting the pin angle this way, update the annotation position, if desired
    pin.update_pin_annotation(False)
    assert pin.term.name == "P1"

    # Add an output pin to the design
    net = design.find_or_add_net("P2")
    term = design.add_term(net, "P2", db_uu.TermType.OUTPUT)
    dot = design.add_dot(layer_id, (5.0, 0.0))
    pin = design.add_pin(term, dot)
    assert pin.term.name == "P2"

    # Add a couple instances of an inductor to the design
    # An instance may be referred by using the Library, Cell, and View name directly
    inductor = design.add_instance(de.LCVName("ads_rflib", "L", "symbol"), (0.750, 0.0), name="L1", angle=0.0)
    assert inductor is not None and inductor.name == "L1"
    # Or an instance may be referred by using a CellviewRef
    cell_view_ref = de.CellviewRef("ads_rflib", "L", "symbol")
    inductor = design.add_instance(cell_view_ref, (3.250, 0.0), name="L2", angle=0.0)
    assert inductor is not None and inductor.name == "L2"
    # Add a capacitor to the design at a -90 degree angle
    capacitor = design.add_instance(de.LCVName("ads_rflib", "C", "symbol"), (2.50, -1.25), name="C1", angle=-90.0)
    assert capacitor is not None and capacitor.name == "C1"
    # Add a ground to the design at a -90 degree angle
    ground = design.add_instance(de.LCVName("ads_rflib", "GROUND", "symbol"), (2.50, -2.25), name="GND", angle=-90.0)
    assert ground is not None and ground.name == "GND"
    # Wire them up
    # P1 to L1
    design.add_wire([(0.0, 0.0), (0.750, 0.0)])
    # L1 to L2
    design.add_wire([(1.750, 0.0), (3.250, 0.0)])
    # L2 to P2
    design.add_wire([(4.250, 0.0), (5.0, 0.0)])
    # C1 to L1 and L2
    design.add_wire([(2.50, 0.0), (2.50, -1.250)])

def create_symbol_for_ideal_lpf_circuit(schematic_lpf: db_uu.Design) -> db_uu.Design:
    symbol_lpf = db_uu.create_symbol("LPF_lib:LPF:symbol")
    # Create the symbol in LPF using SymbolGenerator
    symbol_generator = gs.SymbolGenerator(symbol_lpf, schematic_lpf, 0.25, 0.25)
    symbol_generator.is_dual_symbol_type = True
    symbol_generator.should_replace = True
    symbol_generator.pin_shape = "square"
    symbol_generator.generate_symbol()
    points_l = [(0.3, 0.2), (0.5, 0)]
    polyline_l = GenPolyline(points_l)
    polyline_l.set_segment_as_arc(0, PointF(0.375, 0), ArcOrientation.CLOCKWISE)
    symbol_layer_id = ael.call.db_get_layerid_for_symbol_body(symbol_lpf)
    symbol_lpf.add_line(symbol_layer_id, polyline_l.outline)
    points_r = [(0.7, -0.2), (0.5, 0)]
    polyline_r = GenPolyline(points_r)
    polyline_r.set_segment_as_arc(0, PointF(0.625, 0), ArcOrientation.CLOCKWISE)
    symbol_lpf.add_line(symbol_layer_id, polyline_r.outline)
    symbol_lpf.add_text(symbol_layer_id, "Input", (0.3, 0.125), "Ariel for CAE", 0.069, db_uu.TextAlignment.LOWER_LEFT)
    symbol_lpf.add_text(
        symbol_layer_id, "Output", (0.7, -0.125), "Ariel for CAE", 0.069, db_uu.TextAlignment.UPPER_RIGHT
    )
    symbol_lpf.save_design()
    return symbol_lpf

def add_subcircuit_to_design_and_create_lpf_circuit(design: db_uu.Design, sub_circuit: de.CellviewRef) -> None:
    # Add an instance of sub_circuit to design
    design.add_instance(sub_circuit, (2.50, 0.0))
    # Add some terms
    design.add_instance(de.LCVName("ads_simulation", "Term", "symbol"), (0.0, 0.0), name="Term1", angle=-90.0)
    design.add_instance(de.LCVName("ads_simulation", "Term", "symbol"), (6.0, 0.0), name="Term2", angle=-90.0)
    # Add some ground
    design.add_instance(de.LCVName("ads_rflib", "GROUND", "symbol"), (0.0, -1.0), name="GND1", angle=-90.0)
    design.add_instance(de.LCVName("ads_rflib", "GROUND", "symbol"), (6.0, -1.0), name="GND2", angle=-90.0)
    # Add an S-Param
    design.add_instance(de.LCVName("ads_simulation", "S_Param", "symbol"), (0.0, -3.0), name="S_Param", angle=0.0)
    # Wire up the terms to the sub_circuit
    design.add_wire([(0.0, 0.0), (2.50, 0.0)])
    design.add_wire([(3.50, 0.0), (6.0, 0.0)])
```


---

<!-- === 来源: pypde/docs/examples/ex_properties.md === -->

# Properties[](#properties "Link to this heading")

Example showing the different types of properties.

```
def different_types_of_properties(design: db_uu.Design) -> None:
    # Assuming the design does not have any properties

    import numpy as np  # for AppProp

    # App property (app-specific property whose value is an arbitrary array of bytes)
    app_prop_binary = de.db.AppProp.create(design, "app_prop_binary", "ILList", np.array([1, 2, 3, 4, 5, 6, 7, 8]))
    assert app_prop_binary.name == "app_prop_binary"
    assert app_prop_binary.type == de.db.PropType.APP
    assert app_prop_binary.app_type == "ILList"
    assert np.array_equal(app_prop_binary.value, np.array([1, 2, 3, 4, 5, 6, 7, 8]))

    # AppProp also supports strings
    app_prop_str = de.db.AppProp.create(design, "app_prop_str", "ILList", "Hello, World!")
    assert app_prop_str.type == de.db.PropType.APP
    assert app_prop_str.app_type == "ILList"
    # NOTE: AppProp.value_as_string doesn't verify the array of bytes is a valid string of characters
    assert app_prop_str.value_as_string() == "Hello, World!"

    # Boolean property
    bool_prop = de.db.BooleanProp.create(design, "bool_prop", True)
    assert design.props["bool_prop"] == bool_prop
    assert bool_prop.type == de.db.PropType.BOOLEAN
    assert bool_prop.value == 1
    bool_prop.value = False
    assert bool_prop.value == 0
    bool_prop.value = True
    assert bool_prop.value == 1

    # Double Property, 64-bit floating-point number
    double_prop = de.db.DoubleProp.create(design, "double_prop", 3.141592653589793)
    assert double_prop.type == de.db.PropType.DOUBLE
    assert double_prop.value == 3.141592653589793

    # Double range property, 64-bit floating-point number (min, value, max)
    double_range_prop = de.db.DoubleRangeProp.create(design, "double_range_prop", 3.1, 3.14, 3.14159)
    assert double_range_prop.name == "double_range_prop"
    assert double_range_prop.type == de.db.PropType.DOUBLE_RANGE
    assert double_range_prop.lower_bound == 3.1
    assert double_range_prop.value == 3.14
    assert double_range_prop.upper_bound == 3.14159
    # For a ranged property, valid values must be within the inclusive-lower and inclusive-upper bound
    double_range_prop.value = 3.1  # Okay
    double_range_prop.value = 3.14159  # Okay
    try:
        double_range_prop.value = 3.1416
    except RuntimeError as e:
        assert str(e) == "Value 3.1416 for property 'double_range_prop' not in specified range: [3.1 3.14159]."
    # You can change the range, if desired
    double_range_prop.set_range(2.0, 3.0, 4.0)
    assert double_range_prop.value == 3.0

    # Enum property (string value with a list of valid string values)
    enum_prop = de.db.EnumProp.create(design, "enum_prop", "red", ["red", "green", "blue"])
    assert enum_prop.name == "enum_prop"
    assert enum_prop.type == de.db.PropType.ENUM
    assert enum_prop.value == "red"
    # Enum properties must have a valid value
    try:
        enum_prop.value = "yellow"
    except RuntimeError as e:
        assert str(e) == "Value not a member of enumeration set."

    #######################################
    # FloatProp works just like DoubleProp but with a 32-bit floating-point number
    #######################################
    # FloatRangeProp works just like DoubleRangeProp but with a 32-bit floating-point numbers
    #######################################

    # Hierarchical property (no value but a property that contains other properties)
    hier_record_prop = de.db.HierProp.create(design, "hier_record_prop")
    assert hier_record_prop.name == "hier_record_prop"
    assert hier_record_prop.type == de.db.PropType.HIER
    de.db.StringProp.create(hier_record_prop, "company", "Keysight Technologies")
    de.db.IntProp.create(hier_record_prop, "year", 2024)

    # Get the properties from the HierProp
    hier_props = hier_record_prop.props
    assert len(hier_props) == 2
    assert hier_props["company"].value == "Keysight Technologies"
    assert hier_props["year"].value == 2024

    # Integer property
    int_prop = de.db.IntProp.create(design, "int_prop", 42)
    assert int_prop.name == "int_prop"
    assert int_prop.type == de.db.PropType.INT
    assert int_prop.value == 42

    # Integer range property (min, value, max)
    int_range_prop = de.db.IntRangeProp.create(design, "int_range_prop", 20, 25, 30)
    assert int_range_prop.name == "int_range_prop"
    assert int_range_prop.type == de.db.PropType.INT_RANGE
    assert int_range_prop.lower_bound == 20
    assert int_range_prop.value == 25
    assert int_range_prop.upper_bound == 30
    # For a ranged property, valid values must be within the inclusive-lower and inclusive-upper bound
    int_range_prop.value = 20  # Okay
    int_range_prop.value = 30  # Okay
    try:
        int_range_prop.value = 31
    except RuntimeError as e:
        assert str(e) == "Value 31 for property 'int_range_prop' not in specified range: [20 30]."

    # String property
    str_prop = de.db.StringProp.create(design, "str_prop", "Hello, World!")
    assert str_prop.name == "str_prop"
    assert str_prop.type == de.db.PropType.STRING
    assert str_prop.value == "Hello, World!"

    # Time property - integer representing time in seconds
    time_prop = de.db.TimeProp.create(design, "time_prop", 1717724783)
    assert time_prop.name == "time_prop"
    assert time_prop.type == de.db.PropType.TIME
    assert time_prop.value == 1717724783

    #######################################
    # Time range property operates like IntRangeProp, an integer representing time in seconds (min, value, max),
    #######################################

    # Now, let's get all the properties on the design
    assert len(design.props) == 11
    prop = design.props["app_prop_binary"]
    assert prop == app_prop_binary
    prop = design.props["app_prop_str"]
    assert prop == app_prop_str
    prop = design.props["bool_prop"]
    assert prop == bool_prop
    prop = design.props["double_prop"]
    assert prop == double_prop
    prop = design.props["double_range_prop"]
    assert prop == double_range_prop
    prop = design.props["enum_prop"]
    assert prop == enum_prop
    prop = design.props["hier_record_prop"]
    assert prop == hier_record_prop
    prop = design.props["int_prop"]
    assert prop == int_prop
    prop = design.props["int_range_prop"]
    assert prop == int_range_prop
    prop = design.props["str_prop"]
    assert prop == str_prop
    prop = design.props["time_prop"]
    assert prop == time_prop
```

Example showing the correlation between properties and deactivating an instance.

```
def accessing_deactivated_instance_properties(design: db_uu.Design) -> None:
    # Assuming design has an instance named "C1" that is activated and without any properties
    inst_c1 = design.instances["C1"]
    assert not inst_c1.is_deactivated
    properties = inst_c1.props
    assert len(properties) == 0

    # Deactivate the instance and retrieve its properties
    inst_c1.deactivate()
    assert inst_c1.is_deactivated
    properties = inst_c1.props

    # Deactivating an instance sets two properties, nlAction and lvsIgnore
    assert len(properties) == 2
    # The nlAction property is a String property and its value is "ignore" when the instance is deactivated
    nl_action = properties["nlAction"]
    assert de.db.Property.is_string(nl_action) and isinstance(nl_action, de.db.StringProp)
    assert nl_action.value == "ignore"
    # The lvsIgnore property is a Boolean property and its value is True when the instance is deactivated
    lvs_ignore = properties["lvsIgnore"]
    # OA stores Boolean properties as integers and may contain values different from 0 and 1
    assert de.db.Property.is_boolean(lvs_ignore) and isinstance(lvs_ignore, de.db.BooleanProp)
    assert lvs_ignore.value == 1

    # Reactivate and verify the properties are removed
    inst_c1.activate()
    properties = inst_c1.props
    assert len(properties) == 0

    # Deactivate and short will set a different set of properties
    inst_c1.deactivate_and_short()
    assert inst_c1.is_deactivated
    assert inst_c1.is_deactivated_and_shorted
    properties = inst_c1.props
    assert len(properties) == 2

    # The deactivateAndShort and lvsIgnore properties are set when the instance is deactivated and shorted
    deactivate_and_short = properties["deactivateAndShort"]
    assert de.db.BooleanProp.is_boolean(deactivate_and_short) and isinstance(deactivate_and_short, de.db.BooleanProp)
    assert deactivate_and_short.value == 1
    lvs_ignore = properties["lvsIgnore"]
    assert de.db.Property.is_boolean(lvs_ignore) and isinstance(lvs_ignore, de.db.BooleanProp)
    # Reactivate and verify the properties are removed
    inst_c1.activate()
    assert not inst_c1.is_deactivated
    assert not inst_c1.is_deactivated_and_shorted
    properties = inst_c1.props
    assert len(properties) == 0

    # We can go the other way now by setting the properties and verifying the instance is deactivated
    de.db.StringProp.create(inst_c1, "nlAction", "ignore")
    de.db.BooleanProp.create(inst_c1, "lvsIgnore", 1)

    properties = inst_c1.props
    assert len(properties) == 2
    assert inst_c1.is_deactivated

    # Deleting the properties will reactivate the instance
    properties["lvsIgnore"].delete_prop()
    properties["nlAction"].delete_prop()
    properties = inst_c1.props
    assert len(properties) == 0
    assert not inst_c1.is_deactivated
```

Example showing the correlation between properties and parameters for interoperable instances.

```
def properties_and_cdf_parameters(design: db_uu.Design) -> None:
    # Assume the design has an unmodified instance of analogLib:n1port named NPORT0
    inst_v1 = design.instances["NPORT0"]
    assert inst_v1.cell_name == "n1port"
    # Properties on interoperable components are also parameters.
    thermal_noise_prop = inst_v1.props["thermalnoise"]
    assert thermal_noise_prop.value == "yes"

    inst_cdf = exp.cdf.InstanceParams(inst_v1)
    thermal_noise_param = inst_cdf.params["thermalnoise"]
    assert thermal_noise_param.value == "yes"

    # Setting the value of a property will also update the value of the corresponding parameter
    assert de.db.Property.is_string(thermal_noise_prop)
    thermal_noise_prop.value = "no"
    assert thermal_noise_param.value == "no"
    # Setting the value of the parameter will also update the value of the corresponding property
    thermal_noise_param.value = "yes"
    # NOTE: Updating the value of the parameter doesn't apply to the instance until update_instance is called
    assert thermal_noise_prop.value == "no"
    inst_cdf.update_instance(inst_v1)
    # After updating the instance, the value of the parameter is applied to the property
    assert thermal_noise_prop.value == "yes"

    datafile_param = inst_cdf.params["dataFile"]
    # No value by default
    assert datafile_param.value == ""
    # No dataFile property
    assert inst_v1.props.find("dataFile") is None
    # Set the value of the parameter and update the instance
    datafile_param.value = "dataFile.txt"
    assert datafile_param.value == "dataFile.txt"
    inst_cdf.update_instance(inst_v1)
    # Property is now available
    datafile_prop = inst_v1.props["dataFile"]
    assert datafile_prop.value == "dataFile.txt"

    # Deleting a property will restore the default value of the parameter
    datafile_prop.delete_prop()
    assert inst_v1.props.find("dataFile") is None
    inst_cdf = exp.cdf.InstanceParams(inst_v1)
    datafile_param = inst_cdf.params["dataFile"]
    # Value restored to the default
    assert datafile_param.value == ""
```

Example showing how DMData is used as a container for properties associated with a library.

```
def dm_data_as_a_property_container(workspace: de.Workspace, library: de.Library) -> None:
    # NOTE: Use DMData to attach properties to a Library, Cell, or View.
    # This example just shows just the library case; Cell and View work similarly.
    # Assume the library is writable and there isn't already DMData attached to the library
    assert not library.has_dm_data
    assert library.is_writable
    # Open the DMData in write mode so that it can be saved. DMData opened with "w" mode will delete
    # existing properties.
    data = de.DMData.open(library, "w")
    assert data.owner == library
    de.db.StringProp.create(data, "company", "Keysight Technologies")
    de.db.IntProp.create(data, "year", 2024)
    # The modified property is True when DMData has been modified but not saved
    assert data.modified
    data.save()
    assert not data.modified

    # Let's close the library and reopen it to verify the properties are still there
    lib_name = library.name
    lib_path = str(library.path.resolve())
    workspace.close_library(library)
    # If you want to modify DMData and save it, you'll need to reopen the library in one of the write modes
    library = workspace.open_library(lib_name, lib_path, de.LibraryMode.NON_SHARED)
    # You can obtain DMData directly from the library, if it has been previously saved
    assert library.has_dm_data
    # You'll need to reopen the DMData in append mode if you want to modify it
    data = library.dm_data("a")
    assert data.props["company"].value == "Keysight Technologies"
    assert data.props["year"].value == 2024
    # Delete a property
    data.props["year"].delete_prop()
    assert data.props.find("year") is None
    # If you're unsure if a property exists, you can check for it. You can use find_prop and check the
    # result or catch the KeyError exception when accessing the property directly.
    prop = data.find_prop("year")
    assert prop is None
    try:
        prop = data.props["year"]
    except KeyError as e:
        assert str(e) == "'Key not found: \"year\".'"

    # Changes to DMData can be reverted to the last saved state
    data.revert()
    assert data.props["company"].value == "Keysight Technologies"
    assert data.props["year"].value == 2024

    # Save it
    data.save()
    workspace.close_library(library)
    # You cannot open DMData in write mode if the library is opened in read-only mode
    library = workspace.open_library(lib_name, lib_path, de.LibraryMode.READ_ONLY)
    try:
        data = de.DMData.open(library, "w")
    except RuntimeError as e:
        print(str)
        assert str(e) == f'Failed to get DMData for library "{lib_name}".: Library "{lib_name}" is read-only.'
        # So open it in write mode
        workspace.close_library(library)
        library = workspace.open_library(lib_name, lib_path, de.LibraryMode.NON_SHARED)

    # You can't save DMData if it's read-only, even when the library is open in one of the write modes
    data = de.DMData.open(library, "r")
    assert data.props["company"].value == "Keysight Technologies"
    assert data.props["year"].value == 2024
    data.props["year"].delete_prop()

    try:
        data.save()
    except RuntimeError as e:
        assert str(e) == "Attempt to save a read-only DMData."
        # You can make a DMData that was opened as read-only writable and save it
        data.make_writable()
        data.save()

    # And let's go ahead and delete the DMData entirely
    library.delete_dm_data()
    assert not library.has_dm_data
    workspace.close_library(library)
    library = workspace.open_library(lib_name, lib_path, de.LibraryMode.NON_SHARED)
    assert not library.has_dm_data
    workspace.close_library(library)
```


---

<!-- === 来源: pypde/docs/examples/ex_menu_addon.md === -->

# Creating Custom Menus Using an Addon[](#creating-custom-menus-using-an-addon "Link to this heading")

Addons in ADS may be implemented in Python and enabled using the App Manager in the Tools menu of ADS.

![../../../_images/addons_app_manager.png](../../../_images/addons_app_manager.png)

To select an addon that is written in Python, change the file type filter to show Python files and navigate to your addon package:

![../../../_images/addons_file_type_selector.png](../../../_images/addons_file_type_selector.png)

The following example demonstrates how to create custom menus using an addon implemented in Python.

```
# Copyright Keysight Technologies 2024 - 2024
"""Addon example that will generate menus based on window type."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from keysight.ads.de.app import Action, Addon, Window, WindowDefinition

def setup_addon(addon: "Addon") -> None:
    ...
    """This is the setup function for the Addon."""

    # Implementation of this method is optional but if you do, DO NOT invoke UI from this function!

def shutdown_addon(addon: "Addon") -> None:
    ...
    """This is the shutdown function for the Addon."""

    # Implementation of this method is optional but if you do, DO NOT invoke UI from this function!

    # Menus and Actions that are generated inside the generate_menu function do not need
    # to be explicitly removed, they will be automatically removed when the Addon is disabled
    # or unloaded (after this function returns).

    # Should you wish to remove menus yourself, you can do so using the Menu.remove_ API's.

def identify() -> None:
    print("My Menu Addon.")

def generate_menu(addon: "Addon", win_def: "WindowDefinition") -> None:
    """Menu generator for the Addon."""
    import keysight.ads.de.app as app

    win_type = win_def.window_type
    # We'll add menus to the main window, layout window, and schematic window
    if (
        win_type == app.WindowType.MAIN_WINDOW
        or win_type == app.WindowType.LAYOUT_WINDOW
        or win_type == app.WindowType.SCHEMATIC_WINDOW
    ):
        # Retrieve the window menu bar and add a new menu and actions under the Tools menu
        menu_bar = win_def.menubar
        assert menu_bar
        tools_menu = menu_bar.find_menu("Tools")
        if tools_menu:

            def add_separator_to_tools_menu() -> None:
                separator = app.Separator()
                tools_menu.add_action(separator)

            # We need to add the menu just once per WindowType we're interested in
            if win_type == app.WindowType.MAIN_WINDOW:
                my_addon_menu = tools_menu.find_menu("My Python Addon Menu")
                # Add a new menu and an action to the Tools menu on the Main Window
                if my_addon_menu is None:
                    add_separator_to_tools_menu()
                    my_addon_menu = app.Menu("My Python Addon Menu")
                    tools_menu.add_menu(my_addon_menu)
                    main_menu_action = app.Action("My Main Menu Action", my_addon_main_menu_handler, None)
                    # The shortcut for the action; functional and displays alongside the action title
                    main_menu_action.shortcut = "Ctrl+O"
                    my_addon_menu.add_action(main_menu_action)

            # For layout and schematic windows, we'll add an action directly to the Tools menu
            elif win_type == app.WindowType.LAYOUT_WINDOW:
                if tools_menu.find_action("My Layout Action") is None:
                    add_separator_to_tools_menu()
                    tools_menu.add_action(app.Action("My Layout Action", my_addon_shared_menu_handler, None))
            elif win_type == app.WindowType.SCHEMATIC_WINDOW:
                if tools_menu.find_action("My Schematic Action") is None:
                    add_separator_to_tools_menu()
                    tools_menu.add_action(app.Action("My Schematic Action", my_addon_shared_menu_handler, None))
            else:
                # not possible
                ...

def my_addon_main_menu_handler(action: "Action", window: "Window") -> None:
    from keysight.ads import ael

    # Display a message box when the menu action is triggered
    ael.call.de_info(f"Shortcut ({action.shortcut}) from {action.name} in {str(window.window_type)}")

def my_addon_shared_menu_handler(action: "Action", window: "Window") -> None:
    from keysight.ads import ael
    from keysight.ads.de import app

    if action.name == "My Layout Action":
        assert window.window_type == app.WindowType.LAYOUT_WINDOW
        ael.call.de_info("Layout window type callback handler called.")
    elif action.name == "My Schematic Action":
        assert window.window_type == app.WindowType.SCHEMATIC_WINDOW
        ael.call.de_info("Schematic window type callback handler called.")
    else:
        # not possible
        ...
```

The code above created menus listed in the Tools menu of ADS, as shown below:

![../../../_images/addons_menus.png](../../../_images/addons_menus.png)

While the entirety of your addon does not need to be implemented in \_\_init\_\_.py, its presence is necessary to define
a namespace for your module and allows for the export of symbols accessible by other Python modules.

Access to API’s in your module can be done like:

```
# This code snippet will call the identify() method defined in the menus module above
from keysight.ads.de import app
my_addon = app.import_addon_as_module("menus")
my_addon.identify()
```

![../../../_images/addons_apis_accessible.png](../../../_images/addons_apis_accessible.png)


---

<!-- === 来源: pypde/docs/examples/ex_padstack.md === -->

# Padstacks and Vias[](#padstacks-and-vias "Link to this heading")

The following example shows how to create a padstack template, add it to the technology of a library, and save it.

```
def creating_a_padstack(lib1: de.Library, lib2: de.Library) -> None:
    # A padstack is part of a library's technology and requires a substrate.
    assert lib1.has_tech
    assert lib2.has_tech
    assert lib1 != lib2
    # A padstack can be created two different ways.
    # The first way creates the padstack directly in the technology of a library
    padstack = lib1.tech.create_padstack("Example Padstack")
    # The library property is a reference to the library the padstack is a part of
    assert padstack.library == lib1

    # The second way creates a padstack that is not associated with a library and allows
    # you to add it to one or more libraries later
    padstack_no_library = tech.pads.Padstack("Another Example Padstack")

    # Adding a padstack to a library will not set the library property of the padstack
    lib1.tech.padstacks.add(padstack_no_library)
    assert padstack_no_library.library is None

    # It is not until the padstack has been retrieved from the library that the library
    # property is set.
    padstack_from_lib1 = lib1.tech.padstacks["Another Example Padstack"]
    assert padstack_from_lib1.library == lib1

    lib2.tech.padstacks.add(padstack_no_library)
    padstack_from_lib2 = lib2.tech.padstacks["Another Example Padstack"]
    assert padstack_from_lib2.library == lib2
    assert padstack_from_lib1.library == lib1

    # Save your padstack to the technology
    lib1.tech.save_padstacks()
    lib2.tech.save_padstacks()
```

The following example shows how to delete a padstack template from the technology of a library.

```
def deleting_a_padstack(library: de.Library) -> None:
    assert library.has_tech
    try:
        # If this library already has Example Padstack, retrieve it, otherwise create it
        # In addition to retrieving the padstack from the Library.tech.padstacks collection,
        # you can retrieve it by name using the Tech.get_padstack_from_lib function
        padstack = de.Tech.get_padstack_from_lib(f"{library.name}:Example Padstack")
    except RuntimeError:
        padstack = library.tech.create_padstack("Example Padstack")

    padstack = library.tech.padstacks["Example Padstack"]

    # TODO: Fix API to accept Padstack in the collection's find method?
    assert padstack in library.tech.padstacks
    # Deleting a padstack is as simple as removing it from the padstacks collection
    del library.tech.padstacks["Example Padstack"]
    assert padstack not in library.tech.padstacks

    library.tech.save_padstacks()
```

The following example shows how to build up a padstack template.

```
def building_up_a_padstack(library: de.Library) -> None:
    # A padstack is part of a library's technology and requires a substrate.
    # This example does not cover creating a substrate, but the example padstack
    # is compatible with the default settings of the Create PCB Technology
    # option when setting up the layout technology for the first time.
    assert library.has_tech
    # Create a padstack
    padstack = library.tech.create_padstack("Example Padstack")

    # Drill attributes can be set in different ways, by modifying the drill object directly
    padstack.drill.drill_type = tech.pads.DrillType.SQUARE
    padstack.drill.drill_size = "10 mil"
    padstack.drill.rotate_degrees = "45"

    # Or by initializing a new drill object and assigning it to a padstack
    drill = tech.pads.ViaPadDrill(tech.pads.DrillType.SQUARE)
    drill.drill_size = "10 mil"
    drill.rotate_degrees = "45"
    padstack.drill = drill

    # The drill_size property is a LengthValue object, which expects a string with units
    # If no units are specified, the value will be in meters
    assert padstack.drill.drill_size.value == "10 mil"
    assert padstack.drill.drill_size.mks() == 0.000254  # 10 mil in meters

    # The Padstack layer, drill, and expansion properties are references to their corresponding objects
    drill.drill_size = "25 mil"
    assert padstack.drill.drill_size.value == "25 mil"

    # Create a mask expansion -- there are string equivalents to the enum values, so
    mask_expansion = tech.pads.MaskExpansion("TopAndBottomBoard", "5 mil")
    assert mask_expansion.affects_layers.value == tech.pads.MaskExpansion.AffectsLayers.TOP_AND_BOTTOM_BOARD.value
    # is equivalent to
    mask_expansion = tech.pads.MaskExpansion(tech.pads.MaskExpansion.AffectsLayers.TOP_AND_BOTTOM_BOARD, "5 mil")
    assert mask_expansion.affects_layers.str == "TopAndBottomBoard"
    paste_expansion = tech.pads.MaskExpansion(tech.pads.MaskExpansion.AffectsLayers.NONE)  # Same as "None"
    assert paste_expansion.affects_layers.str == "None"

    padstack.mask_expansion = mask_expansion
    padstack.paste_expansion = paste_expansion
    # Like the drill, the expansion properties are references to their corresponding objects
    mask_expansion.expansion = "2.5 mil"
    assert padstack.mask_expansion.expansion.value == "2.5 mil"

    # The default layer entry holds the pad properties for all layers that are not specifically matched
    # with a LayerMatcher assigned to a PadLayerEntry in the pad_layers collection
    default_layer_entry = tech.pads.PadLayerEntry()
    default_layer_entry.pad = tech.pads.SquarePad("50 mil")
    default_layer_entry.thermal = tech.pads.Thermal("Straight")
    default_layer_entry.thermal.clearance = "5 mil"
    default_layer_entry.thermal.connection_width = "2 mil"

    padstack.default_pad_layer = default_layer_entry

    assert padstack.default_pad_layer.thermal
    assert padstack.default_pad_layer.thermal.clearance.value == "5 mil"

    # Set the default clearance to None so the clearance will use a clearance rule
    clearance = tech.pads.Antipad()
    clearance.mode = tech.pads.Antipad.Mode.NONE
    default_layer_entry.clearance = clearance

    # Create a new layer entry for the top Conductive layer. This entry will override the default layer entry
    # for this layer
    top_conductor_layer_entry = tech.pads.PadLayerEntry()
    top_conductor_layer_entry.layer_matcher = tech.pads.MatchLayerFromTopOfBoard(0, "Conductor")
    top_conductor_layer_entry.pad = tech.pads.CircularPad("75 mil")
    top_conductor_layer_entry.clearance = tech.pads.Antipad()
    top_conductor_layer_entry.clearance.mode = tech.pads.Antipad.Mode.ADD_CLEARANCE
    top_conductor_layer_entry.clearance.expansion = "15 mil"

    # The pad_layers collection consists of all the PadLayerEntry that are not the default
    assert len(padstack.pad_layers) == 0
    # Add the top conductor PadLayerEntry
    padstack.pad_layers.append(top_conductor_layer_entry)
    assert len(padstack.pad_layers) == 1

    # Create a new layer entry for the M5 layer. This entry will override the default layer entry
    # for the M5 layer, but not for any other layers
    m5_layer_entry = tech.pads.PadLayerEntry()
    m5_layer_entry.layer_matcher = tech.pads.MatchLayerByName("M5")
    m5_layer_entry.pad = tech.pads.SquarePad("50 mil")

    # The M5 entry will have clearance in the shape of an octagon
    clearance = tech.pads.Antipad()
    clearance.mode = tech.pads.Antipad.Mode.CUSTOM
    clearance.custom_antipad = tech.pads.OctagonalPad("100 mil")
    m5_layer_entry.clearance = clearance

    # Add the M5 PadLayerEntry
    padstack.pad_layers.append(m5_layer_entry)
    assert len(padstack.pad_layers) == 2

    # PadLayerEntry can accessed by index from the pad_layers collection
    assert padstack.pad_layers[1] == m5_layer_entry
    assert padstack.pad_layers[1].layer_matcher
    assert tech.pads.LayerMatcher.is_name_matcher(padstack.pad_layers[1].layer_matcher)
    assert padstack.pad_layers[1].layer_matcher.name == "M5"

    library.tech.save_padstacks()
```

The following image shows a through pad that was placed using the padstack template created in the example above.
Planes are added to show the effects of the clearance, thermal, and anti-pad settings.

![../../../_images/ex_padstack_01.png](../../../_images/ex_padstack_01.png)

The following examples show how to place pads and vias into a design.

```
def place_single_layer_pad(design: db_uu.Design, library: de.Library) -> None:
    lib_name = library.name
    # Padstack created in creating_a_padstack above
    padstack_name = "Example Padstack"
    padstack = library.tech.padstacks[padstack_name]

    # Create a pad with a single layer specified
    # The specified layer will match the relevant PadLayerEntry in the padstack
    # For example, placing a single layer pad in the M5 layer will used the M5 PadLayerEntry
    layer = library.tech.layer("M5")
    m5_pad = design.add_single_layer_pad(padstack, db_uu.LayerId(layer.number), (75, 325))
    assert m5_pad.pad_via_type.value == db_uu.PCBBase.PadViaType.SINGLE_LAYER_PAD.value
    assert m5_pad.pad_layer == layer.number

    # A pad that has been placed in a design is an Instance and can be accessed from the design by name
    assert m5_pad in design.instances and m5_pad == design.instances[m5_pad.name]
    # The padstack template name is the library name and padstack name separated by a colon
    assert m5_pad.padstack_name == f"{lib_name}:{padstack_name}"
    # The pad instance name is "Pad" followed by a number starting from 1
    assert m5_pad.name == "Pad1"
    assert m5_pad.pad_via_type == db_uu.PCBBase.PadViaType.SINGLE_LAYER_PAD
```

```
def place_pad_and_via_with_specified_layers(design: db_uu.Design, library: de.Library) -> None:
    # Padstack created in creating_a_padstack above
    padstack_name = "Example Padstack"
    padstack = library.tech.padstacks[padstack_name]

    # The pad placed in the cond layer corresponds to the PadLayerEntry with the
    # MatchLayerFromTopOfBoard(0, "Conductor") LayerMatcher
    top_layer = db_uu.LayerId(library.tech.layers["cond"].number)
    # The pad placed in the M10 layer corresponds to the default PadLayerEntry
    bottom_layer = db_uu.LayerId(library.tech.layers["M10"].number)
    cond_m10_pad = design.add_pad_with_specified_layers(padstack, top_layer, bottom_layer, (200, 325))
    assert cond_m10_pad.top_layer == top_layer.layer
    assert cond_m10_pad.bottom_layer == bottom_layer.layer
    assert cond_m10_pad.pad_via_type == db_uu.PCBBase.PadViaType.BLIND_BURIED_PAD
    assert db_uu.PCBBase.is_pcb_pad(cond_m10_pad)
    assert not db_uu.PCBBase.is_pcb_via(cond_m10_pad)

    # Placing a via with specified layers is similar to placing a pad with specified layers
    cond_m10_via = design.add_via_with_specified_layers(padstack, top_layer, bottom_layer, (200, 200))
    # The via instance name is "Via" followed by a number starting from 1
    assert cond_m10_via.name == "Via1"
    assert cond_m10_via.pad_via_type == db_uu.PCBBase.PadViaType.BLIND_BURIED_PAD
    assert db_uu.PCBBase.is_pcb_via(cond_m10_via)
    assert not db_uu.PCBBase.is_pcb_pad(cond_m10_via)
```

```
def place_pad_and_via_with_drill_layer(design: db_uu.Design, library: de.Library) -> None:
    # Padstack created in creating_a_padstack above
    padstack_name = "Example Padstack"
    padstack = library.tech.padstacks[padstack_name]

    # Create pad with the drill layer specified
    cond_m2_layer = db_uu.LayerId(library.tech.layers["cond_M2"].number)
    cond_m2_pad = design.add_pad_with_drill_layer(padstack, cond_m2_layer, (75, 200))
    assert cond_m2_pad.pad_via_type == db_uu.PCBBase.PadViaType.DRILL_LAYER
    assert cond_m2_pad.drill_layer == cond_m2_layer.layer

    # Create a via with the drill layer specified
    m4_m5_layer = db_uu.LayerId(library.tech.layers["M4_M5"].number)
    m4_m5_via = design.add_via_with_drill_layer(padstack, m4_m5_layer, (75, 75))
    assert m4_m5_via.pad_via_type == db_uu.PCBBase.PadViaType.DRILL_LAYER
    assert m4_m5_via.drill_layer == m4_m5_layer.layer
```

```
def place_through_pad_and_via(design: db_uu.Design, library: de.Library) -> None:
    # Padstack created in creating_a_padstack above
    padstack_name = "Example Padstack"
    padstack = library.tech.padstacks[padstack_name]

    # Create a through pad
    through_pad = design.add_through_pad(padstack, (325, 325))
    assert through_pad.pad_via_type == db_uu.PCBBase.PadViaType.THROUGH

    # Create a through via
    through_via = design.add_through_via(padstack, (325, 200))
    assert through_via.pad_via_type == db_uu.PCBBase.PadViaType.THROUGH
```


---

<!-- === 来源: pypde/docs/examples/ex_nested.md === -->

# Nested Technology[](#nested-technology "Link to this heading")

The following example shows how to create nested technology and layer maps from the nested library to the parent library.

```
# Copyright Keysight Technologies 2025

"""Example nested technology using the Python API."""

from keysight.ads import de

def map_nested_technology(workspace: de.Workspace) -> None:
    """Create nested technology and map layers.

    Creates RF_Board_lib and maps layers from the nested technology library smt_lib.
    """
    # create the smt_lib with technology using millimeter units
    smt_lib = create_smt_lib(workspace)
    # create the RF_Board_lib with technology using mil units and using smt_lib as nested technology
    board_lib = create_rf_board_lib(workspace, smt_lib)
    # Different ways to look up the same layer map
    layer_map1 = board_lib.tech.layer_maps[0]
    layer_map2 = board_lib.tech.layer_maps.find("smt_top")
    layer_map = de.tech.nested.find_layer_map("RF_Board_lib", "smt_top")
    assert layer_map is not None
    assert layer_map == layer_map1
    assert layer_map == layer_map2
    assert layer_map.name == "smt_top"
    assert layer_map.nested_library_name == "smt_lib"
    # The parent library is the layer_map_library
    assert layer_map.layer_map_library_name == "RF_Board_lib"
    assert layer_map.nested_mapped_layers[0] == "cond"
    # Mapped layers default to {layer_map_name}_{nested_lib_name}_{nested_layer_name}
    assert layer_map.parent_mapped_layers[0] == "smt_top_smt_lib_cond"

    # find_layer_map returns None if the named layer map is not found
    bottom_layer_map = de.tech.nested.find_layer_map("RF_Board_lib", "smt_bottom")
    if bottom_layer_map is None:
        new_layer_map = de.tech.nested.LayerMap("smt_bottom", "smt_lib", "RF_Board_lib")
        new_layer_map.is_above = False
        new_layer_map.is_flipped = True
        new_layer_map.map_nested_layer("cond")
        # new_layer_map.nested_mapped_layers.append("cond")
        # new_layer_map.parent_mapped_layers = ["smt_bottom_smt_lib_cond"]
        board_lib.tech.layer_maps.append(new_layer_map)
        board_lib.tech.save_layer_maps()
    layer_map.unmap_nested_layer("ports")

def create_smt_lib(workspace: de.Workspace) -> de.Library:
    # Create a "smt_lib" library with tech using millimeters
    smt_lib = de.create_new_library("smt_lib", workspace.path / "smt_lib")
    workspace.add_library(smt_lib.name, smt_lib.path, de.LibraryMode.SHARED)
    smt_lib.setup_schematic_tech()
    smt_lib.create_layout_tech_std_ads("millimeter", 1000)
    return smt_lib

def create_rf_board_lib(workspace: de.Workspace, smt_lib: de.Library) -> de.Library:
    # Create a "RF_Board_lib" library with tech using mils
    rf_lib = de.create_new_library("RF_Board_lib", workspace.path / "RF_Board_lib")
    workspace.add_library(rf_lib.name, rf_lib.path, de.LibraryMode.SHARED)
    rf_lib.setup_schematic_tech()
    rf_lib.create_layout_tech_std_ads("mil", 1000)

    # Create a layer map between "RF_Board_lib" and "smt_lib" for the "cond" and "ports" layers
    layer_map = de.tech.nested.LayerMap("smt_top", smt_lib, rf_lib)
    layer_map.map_nested_layer("cond")
    layer_map.map_nested_layer("ports")
    rf_lib.tech.layer_maps.append(layer_map)
    return rf_lib
```

The following image shows the nested technology settings for the RF\_Board\_lib library created in the example above.

![../../../_images/nested_technology.png](../../../_images/nested_technology.png)

The following image shows the layer mapping created for layers between RF\_Board\_lib and smt\_lib in the smt\_top layer map from the previous example.
Note that the default orientation and positioning is above pointing up.

![../../../_images/nested_mapped_layers_smt_top.png](../../../_images/nested_mapped_layers_smt_top.png)

The following image shows the layer mapping created for layers between RF\_Board\_lib and smt\_lib in the smt\_bottom layer map from the previous example.
Note that the orientation and positioning is below pointing down as set in the example using the [`is_above`](../reference/de/tech/nested/nested.md#keysight.ads.de.tech.nested.LayerMap "keysight.ads.de.tech.nested.LayerMap") and [`is_flipped`](../reference/de/tech/nested/nested.md#keysight.ads.de.tech.nested.LayerMap "keysight.ads.de.tech.nested.LayerMap") properties.

![../../../_images/nested_mapped_layers_smt_bottom.png](../../../_images/nested_mapped_layers_smt_bottom.png)


---

<!-- === 来源: pypde/docs/examples/ex_rules.md === -->

# Rules[](#rules "Link to this heading")

The following example shows to create a clearance rule, add it to the technology of a library, and save it.

```
def creating_a_clearance_rule(library: de.Library) -> None:
    # Clearance rules specify the minimum clearance between two objects

    # NOTE: You cannot create a rule that already exists
    assert not library.tech.clearance_rules.find("Example Clearance Rule")

    # Create a clearance rule with a default clearance of 10.0
    rule = tech.rule.ClearanceRule(library, "Example Clearance Rule", 10.0)

    # Set the priority of the rule, higher priority rules will take precedence over lower priority rules
    # The numerical value of the priority must be greater than or equal to zero and is relative to other
    # rule priorities; the higher the number, the higher the priority
    rule.priority = 10

    # By default, a new rule is enabled
    assert rule.enabled

    # Rules apply to a pair of objects, the first object must match the first scope and the second object,
    # the second scope.
    # By default, the both the first and second scope are set to tech.rule.ScopeType.Default
    assert rule.first_scope == rule.second_scope == tech.rule.DefaultScope()
    # The same as
    assert rule.first_scope.scope_type == rule.second_scope.scope_type == tech.rule.ScopeType.DEFAULT

    # For this example, the first scope will refer to the my_net Net
    rule.first_scope = tech.rule.NetClassScope(["my_net"])

    # The second scope will refer to any net that is not the my_net Net
    rule.second_scope = tech.rule.DifferentNetScope()

    # By default, the rule will apply to all layers, but for this example,
    # We'll specify a few different layers and show how to set different clearances for
    # different object types

    # when viewing the result inside ADS
    # Let's apply this rule to the M3, 9, and M12 layers
    rule.layers = ["M3", "M9", "M12"]

    # The rule values are a 2D matrix of the clearance values between the object types
    # The object types are:
    # Trace
    # Pad
    # Via
    # Plane
    rule.rule_values[("Plane", "Trace")] = 25.0
    rule.rule_values[("Plane", "Pad")] = 40.0
    rule.rule_values[("Plane", "Via")] = 55.0

    # The values for the object types that are not explicitly set use the default_clearance,
    # whose initial value is set when the rule is created
    assert rule.default_clearance == 10.0

    # NOTE: The order of the object types in the tuple doesn't matter
    assert rule.rule_values[("Plane", "Trace")] == rule.rule_values[("Trace", "Plane")] == 25.0

    # Add the clearance rule to the technology and save it
    library.tech.clearance_rules.add(rule)
    library.tech.save_rules()
```

The following image shows how the clearance rule created above appears inside the constraints manager of ADS.

![../../../_images/clearance_rule.png](../../../_images/clearance_rule.png)

The following example shows how to delete a clearance rule from the technology of a library.

```
def deleting_a_clearance_rule(library: de.Library) -> None:
    # Ensure the clearance rule exists before trying to delete it
    if not library.tech.clearance_rules.find("Example Clearance Rule"):
        creating_a_clearance_rule(library)

    assert library.tech.clearance_rules.find("Example Clearance Rule")

    # Deleting a clearance rule is straightforward
    del library.tech.clearance_rules["Example Clearance Rule"]
    assert not library.tech.clearance_rules.find("Example Clearance Rule")
    library.tech.save_rules()
```

The following examples shows how to create a via rule.

```
def creating_a_via_rule(library: de.Library) -> None:
    lib_name = library.name
    # Create a new via rule for cond to m2 from the Example Padstack
    # NOTE: The padstack name is in the form of "library_name:padstack_name"
    via_cond_m2_rule = tech.rule.ViaRule("via_cond_m2", f"{lib_name}:Example Padstack", "cond", "M2")

    # Set the priority of the rule, higher priority rules will take precedence over lower priority rules
    # The numerical value of the priority must be greater than or equal to zero and is relative to other
    # rule priorities; the higher the number, the higher the priority
    via_cond_m2_rule.priority = 10

    # Rules are enabled by default, but no harm in being explicit
    via_cond_m2_rule.enabled = True

    assert via_cond_m2_rule.name == "via_cond_m2"
    assert via_cond_m2_rule.padstack_name == f"{lib_name}:Example Padstack"
    assert via_cond_m2_rule.has_layer_constraints
    assert via_cond_m2_rule.top_layer == "cond"
    assert via_cond_m2_rule.bottom_layer == "M2"

    # Create another rule. You don't need to specify the layers up front if you don't want to
    via_m2_m3_rule = tech.rule.ViaRule("via_m2_m3", f"{lib_name}:Example Padstack")

    # There are no constraints set
    assert not via_m2_m3_rule.has_layer_constraints
    assert via_m2_m3_rule.top_layer == ""
    assert via_m2_m3_rule.bottom_layer == ""
    # Set them here
    via_m2_m3_rule.set_layer_constraints("M2", "M3")
    assert via_m2_m3_rule.has_layer_constraints
    assert via_m2_m3_rule.top_layer == "M2"
    assert via_m2_m3_rule.bottom_layer == "M3"

    via_m2_m3_rule.priority = 10
    via_m2_m3_rule.enabled = True

    # Add the rules to the library and save them
    library.tech.via_rules.add(via_cond_m2_rule)
    library.tech.via_rules.add(via_m2_m3_rule)
    library.tech.save_rules()
```

The following image shows how the via rule created above appears inside the constraints manager of ADS.

![../../../_images/creating_via_rules.png](../../../_images/creating_via_rules.png)

The following example shows how to create a stacked via rule.

```
def creating_a_stacked_via_rule(library: de.Library) -> None:
    libname = library.name
    # Ensure we have the via rules we need
    if library.tech.via_rules.find("via_cond_m2"):
        del library.tech.via_rules["via_cond_m2"]
    if library.tech.via_rules.find("via_m2_m3"):
        del library.tech.via_rules["via_m2_m3"]

    creating_a_via_rule(library)

    via_cond_m2_rule = library.tech.via_rules["via_cond_m2"]
    via_m2_m3_rule = library.tech.via_rules["via_m2_m3"]

    # Make the via rules stackable
    via_cond_m2_rule.is_stackable = True
    via_m2_m3_rule.is_stackable = True

    # Create a stacked via rule using the two via rules, via_cond_m2 and via_m2_m3
    # Rule names are in the form of "libname:rule_name"
    stacked_rule = tech.rule.StackedViaRule(
        "stacked_cond_m3", "cond", "M3", [f"{libname}:via_cond_m2", f"{libname}:via_m2_m3"]
    )
    stacked_rule.enabled = True
    library.tech.stacked_via_rules.add(stacked_rule)
    library.tech.save_rules()
```

The following image shows how the padstack rule created above appears inside the constraints manager of ADS.

![../../../_images/stacked_via_rule.png](../../../_images/stacked_via_rule.png)

The following example shows how to place the vias constrained by the rules defined above.

```
def placing_constrained_vias(design: db_uu.Design, library: de.Library) -> None:
    libname = library.name

    if not library.tech.padstacks.find("Example Padstack"):
        # See ex_padstack.py for the padstack template used in this example
        # NOTE: If you've copied/pasted this code into the ADS Python console,
        # you may need to execute building_up_a_padstack from ex_padstack.py
        # first to create "Example Padstack".
        from . import ex_padstack

        ex_padstack.building_up_a_padstack(library)

    if not library.tech.stacked_via_rules.find("stacked_cond_m3"):
        creating_a_stacked_via_rule(library)

    cond_layer = db_uu.LayerId.create_layer_id_from_library(library, "cond")
    m2_layer = db_uu.LayerId.create_layer_id_from_library(library, "M2")
    m3_layer = db_uu.LayerId.create_layer_id_from_library(library, "M3")

    design.add_trace(cond_layer, [(0, -200), (200, -200)], 25)
    design.add_constrained_via(f"{libname}:via_cond_m2", (200, -200))
    design.add_trace(m2_layer, [(200, -200), (200, -400)], 25)
    design.add_constrained_via(f"{libname}:via_m2_m3", (200, -400))
    design.add_trace(m3_layer, [(200, -400), (0, -400)], 25)
    design.add_stacked_via(f"{libname}:stacked_cond_m3", (0, -400))
```

The following image shows the vias placed using the rules defined above.

![../../../_images/placing_constrained_vias.png](../../../_images/placing_constrained_vias.png)


---

<!-- === 来源: pypde/docs/examples/ex_place_text.md === -->

# Placing Text[](#placing-text "Link to this heading")

This example illustrates the various ways of placing text into a design.

```
def placing_text_in_a_design(design: db_uu.Design) -> None:
    from keysight.ads.de import db_uu
    from keysight.ads.de.experimental.text_maker import TextMaker

    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)

    # There are multiple ways to place text on a design.
    # The TextMaker class pulls the text attributes from the design preferences
    text_maker = TextMaker(design)
    origin = (1.0, 0.5)
    text_maker.add_text(layer_id, "Hello Keysight 1!", origin)

    # Change text attributes as desired
    text_maker.height = 0.225
    text_maker.font_name = "Arial Italic"
    text_maker.align = db_uu.TextAlignment.LOWER_LEFT
    text_maker.orient = db_uu.Orientation.R270
    origin = (1.5, 1.0)
    text = text_maker.add_text(layer_id, "Hello Keysight 2!", origin)
    assert text.text_height == 0.225
    assert text.font_name == "Arial Italic"
    assert text.alignment == db_uu.TextAlignment.LOWER_LEFT
    assert text.orientation == db_uu.Orientation.R270

    # Alternatively, place text using the Text class directly
    origin = (1.5, 1.5)
    text = db_uu.Text(
        design,
        layer_id,
        "Hello Keysight 3!",
        origin,
        "Arial Bold",
        0.225,
        db_uu.TextAlignment.UPPER_RIGHT,
        db_uu.Orientation.R0,
    )
    assert text.text_height == 0.225
    assert text.font_name == "Arial Bold"
    assert text.alignment == db_uu.TextAlignment.UPPER_RIGHT
    assert text.orientation == db_uu.Orientation.R0

    # Or, use the add_text method on the design
    origin = (2.0, 2.0)
    text = design.add_text(
        layer_id,
        "Hello Keysight 4!",
        origin,
        "Arial",
        0.225,
        db_uu.TextAlignment.CENTER_CENTER,
        db_uu.Orientation.R180,
    )
    assert text.text_height == 0.225
    assert text.font_name == "Arial"
    assert text.alignment == db_uu.TextAlignment.CENTER_CENTER
    assert text.orientation == db_uu.Orientation.R180
```

This example uses a shape iterator (ShapeIter) to access text placed in a design.

```
def accessing_placed_text_with_a_shape_iterator(design: db_uu.Design) -> None:
    from keysight.ads.de.experimental.text_maker import TextMaker

    # For this example, ensure the design is empty
    design.clear_design()
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    # Make some text
    text_maker = TextMaker(design)
    text_maker.height = 0.225
    text_maker.font_name = "Arial Italic"
    text_maker.align = db_uu.TextAlignment.UPPER_LEFT
    text_maker.orient = db_uu.Orientation.R0
    origin = (1.0, 1.0)
    text_maker.add_text(layer_id, "Hello Keysight 1!", origin)

    # Access the text via a ShapeIter
    shape_iter = db_uu.ShapeIter(design)
    shape_iter.limit_layerid(layer_id)
    # The design was previously cleared, there will be only one shape
    for shape in shape_iter:
        assert isinstance(shape, db_uu.Text)
        assert shape.text_string == "Hello Keysight 1!"
        assert shape.text_height == 0.225
        assert shape.font_name == "Arial Italic"
        assert shape.alignment == db_uu.TextAlignment.UPPER_LEFT
        assert shape.orientation == db_uu.Orientation.R0
        # Change some attributes
        shape.text_string = "Hello Keysight 2!"
        shape.text_height = 0.16875
        shape.font_name = "Arial Bold"
        shape.orientation = db_uu.Orientation.R180

    # Recreate the ShapeIter and verify the text has been updated
    shape_iter = db_uu.ShapeIter(design)
    shape_iter.limit_layerid(layer_id)
    for shape in shape_iter:
        assert isinstance(shape, db_uu.Text)
        assert shape.text_string == "Hello Keysight 2!"
        assert shape.text_height == 0.16875
        assert shape.font_name == "Arial Bold"
        assert shape.alignment == db_uu.TextAlignment.UPPER_LEFT
        assert shape.orientation == db_uu.Orientation.R180
```

This example illustrates how to place an attribute display into a design.

```
def placing_attribute_displays(design: db_uu.Design) -> None:
    from keysight.ads import de
    from keysight.ads.de.experimental.text_maker import TextMaker

    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    # The TextMaker class pulls the text attributes from the design preferences
    text_maker = TextMaker(design)
    origin = (2.0, 3.0)
    # Change text attributes as desired
    text_maker.height = 0.16875
    text_maker.orient = db_uu.Orientation.R0
    attr_display = text_maker.add_attr_display(
        design, de.db.DesignAttrType.VIEW_NAME, layer_id, origin, de.db.TextDisplayFormat.NAME_VALUE
    )
    assert attr_display.attribute == de.db.DesignAttrType.VIEW_NAME

    origin = (2.0, 3.5)
    attr_display = text_maker.add_attr_display(
        design, de.db.DesignAttrType.LAST_SAVED_TIME, layer_id, origin, de.db.TextDisplayFormat.NAME_VALUE
    )
    assert attr_display.attribute == de.db.DesignAttrType.LAST_SAVED_TIME

    # An AttrDisplay may also be created directly from the design
    origin = (2.0, 4.0)
    attr_display = design.add_attr_display(
        design,
        de.db.DesignAttrType.LIB_NAME,
        layer_id,
        origin,
        "Arial",
        0.16875,
        de.db.TextAlignment.CENTER_CENTER,
        de.db.Orientation.R0,
        de.db.TextDisplayFormat.NAME_VALUE,
    )
    assert attr_display.attribute == de.db.DesignAttrType.LIB_NAME
```

This example places instance attribute displays into a design.

```
def adding_an_inst_attr_display(library: de.Library) -> None:
    # This example assumes the library does not have cells called cell_inst or cell_main
    layer_id = db_uu.LayerId(231)
    inst_design_lcv_name = f"{library.name}:cell_inst:schematic"
    inst_design = db_uu.create_schematic(inst_design_lcv_name)
    # Create a simple design
    with db_uu.design_saving(inst_design):
        inst_design.add_instance(("ads_sources", "V_DC", "symbol"), (0, 0.5), name="SRC1", angle=-90.0)
        inst_design.add_instance(("ads_rflib", "R", "symbol"), (3.0, 0.5), name="R1", angle=-90.0)
        inst_design.add_instance(("ads_rflib", "GROUND", "symbol"), (1.5, -0.875), angle=-90)
        inst_design.add_wire([(0.0, -0.5), (1.5, -0.875)])
        inst_design.add_wire([(1.5, -0.875), (3.0, -0.50)])
        inst_design.add_wire([(0.0, 0.5), (3.0, 0.5)])

    main_design = db_uu.create_schematic(f"{library.name}:cell_main:schematic")
    with db_uu.design_saving(main_design):
        # Insert an instance of the simple design into a new design
        instance = main_design.add_instance(inst_design_lcv_name, (0.0, 0.0), name="INST1", angle=0.0)
        # And add instance attributes displays to the design
        main_design.add_inst_attr_display(
            instance, de.db.DesignAttrType.LIB_NAME, layer_id, (0.0, 1.5), "Arial Bold", 0.16875
        )
        main_design.add_inst_attr_display(
            instance, de.db.DesignAttrType.CELL_NAME, layer_id, (0.0, 1.25), "Arial", 0.16875
        )
        main_design.add_inst_attr_display(
            instance,
            de.db.DesignAttrType.LAST_SAVED_TIME,
            layer_id,
            (0.0, 1.0),
            "Arial Italic",
            0.16875,
            display_format=de.db.TextDisplayFormat.NAME_VALUE,
        )
```


---

<!-- === 来源: pypde/docs/examples/ex_polygon.md === -->

# Paths, Traces, and Polygons[](#paths-traces-and-polygons "Link to this heading")

This examples shows different ways to add paths, traces, and polygons to your design

Adding a Path:

```
def adding_a_path(design: db_uu.Design) -> None:
    from keysight.ads import de

    # This example will add a path using the specified points directly
    points = [(100.0, 0.0), (150.0, 0.0), (150.0, 50.0), (200.0, 50.0)]
    # points_uu = [de.PointUU(point[0], point[1]) for point in points]
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    # TODO: Bend_style, cap_style, miter_radius, when supported
    # When creating a path, a width must be specified
    path = design.add_path(layer_id, points, 10.0)
    assert path is not None

    path_offset = 25.0  # Using an offset to easily adjust the placement of each path (for illustration purposes)
    points_offset = [(point[0] - path_offset, point[1] + path_offset) for point in points]
    # Paths may be added using a GenPolyline
    polyline = de.GenPolyline(points_offset, 10.0, "Square", "Square", 0.0)
    assert polyline.bend_style == de.db.BendStyle.SQUARE
    assert polyline.cap_style == de.db.CapStyle.SQUARE
    path = design.add_path(layer_id, polyline)
    assert path is not None

    path_offset = 50.0
    points_offset = [(point[0] - path_offset, point[1] + path_offset) for point in points]
    # Paths have different cap (end-points) and bend styles (corners)
    # Mitered bend styles apply a miter cutoff percentage
    polyline = de.GenPolyline(points_offset, 10.0, "Mitered", "Round", 30.0)
    assert polyline.bend_style == de.db.BendStyle.MITERED
    assert polyline.cap_style == de.db.CapStyle.ROUND
    path = design.add_path(layer_id, polyline)
    assert path is not None

    path_offset = 75.0
    points_offset = [(point[0] - path_offset, point[1] + path_offset) for point in points]
    # Curved bend styles apply a miter radius
    polyline = de.GenPolyline(points_offset, 10.0, "Curved", "Square", 45.0)
    assert polyline.bend_style == de.db.BendStyle.CURVED
    assert polyline.cap_style == de.db.CapStyle.SQUARE
    path = design.add_path(layer_id, polyline)
    assert path is not None
```

Adding a Trace:

```
def adding_a_trace(design: db_uu.Design) -> None:
    from keysight.ads import de

    transaction = de.db.Transaction(design, "Adding traces")
    # This example will add a trace using the specified points directly
    points = [(-100.0, 0.0), (-50.0, 0.0), (-50.0, 50.0), (0.0, 50.0)]
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    # TODO: Bend_style, cap_style, miter_radius, when supported
    # When creating a trace, a width must be specified
    path = design.add_trace(layer_id, points, 10.0)
    assert path is not None

    trace_offset = 25.0  # Using an offset to easily adjust the placement of each trace (for illustration purposes)
    points_offset = [(point[0] - trace_offset, point[1] + trace_offset) for point in points]
    # Traces may also be added using a GenPolyline
    polyline = de.GenPolyline(points_offset, 10.0, de.BendStyle.SQUARE, de.CapStyle.SQUARE, 0.0)
    path = design.add_trace(layer_id, polyline)
    assert path is not None

    trace_offset = 50.0
    points_offset = [(point[0] - trace_offset, point[1] + trace_offset) for point in points]
    # Traces have different cap (end-points) and bend styles (corners)
    # Mitered bend styles apply a miter cutoff percentage
    polyline = de.GenPolyline(points_offset, 10.0, de.BendStyle.MITERED, de.CapStyle.ROUND, 30.0)
    path = design.add_trace(layer_id, polyline)
    assert path is not None

    trace_offset = 75.0
    points_offset = [(point[0] - trace_offset, point[1] + trace_offset) for point in points]
    # Curved bend styles apply a miter radius
    polyline = de.GenPolyline(points_offset, 10.0, de.BendStyle.CURVED, de.CapStyle.SQUARE, 45.0)
    path = design.add_trace(layer_id, polyline)
    assert path is not None
    transaction.commit()
```

Adding a Polygon:

```
def adding_a_polygon(design: db_uu.Design) -> None:
    from keysight.ads import de

    # This example will add a polygon using the specified points directly
    points = [(15.0, -80.0), (35.0, -115.0), (75.0, -115.0), (95.0, -80.0), (75.0, -45.0), (35.0, -45.0)]
    # Using a poly_offset to easily adjust the placement of each polygon (for illustration purposes)
    poly_offset = 100.0
    points_offset = [(point[0] + poly_offset, point[1]) for point in points]
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    polygon = design.add_polygon(layer_id, points_offset)
    assert polygon is not None

    points_offset = [(point[0] - poly_offset, point[1]) for point in points]
    # Polygons may be added using a GenPolygon
    gen_polygon = de.GenPolygon(points_offset)
    polygon = design.add_polygon(layer_id, gen_polygon)
    assert polygon is not None

    # A polygon with holes may be added using a GenPolygonWithHoles
    hole_points = [(40.0, -60.0), (70.0, -60.0), (80.0, -80.0), (70.0, -100.0), (40.0, -100.0), (30.0, -80.0)]
    points_offset = [(point[0], point[1]) for point in points]

    outer_boundary = de.GenPolygon(points_offset)
    inner_boundary = de.GenPolygon(hole_points)
    gen_polygon_with_holes = de.GenPolygonWithHoles(None, outer_boundary, [inner_boundary])
    polygon = design.add_polygon(layer_id, gen_polygon_with_holes)
    assert polygon is not None
```

Iterating over Shapes in a Design:

```
def iterating_over_shapes_in_design(design: db_uu.Design) -> None:
    from keysight.ads.de.db import Transform

    # For this example, clear the design to ensure its empty
    design.clear_design()
    # ads_device:drawing for schematic, cond for layout
    layer_id = db_uu.LayerId(231 if design.is_schematic is True else 1)
    # Let's add shapes
    adding_a_path(design)
    adding_a_trace(design)
    adding_a_polygon(design)

    # Create a ShapeIter to iterate over all shapes
    shape_iter = db_uu.ShapeIter(design, layer_id)
    # New shapes will be placed on a different layer
    target_layer_id = db_uu.LayerId(229 if design.is_schematic is True else 2)
    for shape in shape_iter:
        shape_type = shape.type
        # Paths, traces, and polygons added to a design are all Polygons
        assert shape_type.is_oa_polygon
        assert isinstance(shape, db_uu.Polygon)
        # ApolloType may be used to distinguish the kind of component the Polygon represents
        # Paths and traces have a centerline; other polygons do not.
        if shape_type.is_ads_path:
            # Use a transform to move the points of the existing path
            path_line = shape.get_centerline()
            transform = Transform()
            transform.translate(dx=200.0, dy=0.0)
            path_line.transform(transform)
            # And then place the path onto a different layer
            design.add_path(target_layer_id, path_line)

        elif shape_type.is_trace:
            # Use a transform to move the points and rotate an existing trace
            trace_line = shape.get_centerline()
            transform = Transform()
            transform.rotate_degrees(45.0)
            transform.translate(dx=-100.0, dy=200.0)
            trace_line.transform(transform)
            # And then place the trace onto a different layer
            design.add_trace(target_layer_id, trace_line)

        elif shape_type.is_ads_polygon:
            # Use a transform to move the points of an existing polygon
            transform = Transform()
            transform.translate(dx=0.0, dy=-100.0)
            polygon = shape.get_gen_polygon()
            polygon.transform(transform, 0.0)
            # Convert vertices to arcs and place the new shape in another layer
            converted_polys = polygon.convert_vertices_to_arcs(15.0)
            # Only one polygon will be returned when converting vertices to arcs on a simple shape
            assert len(converted_polys) == 1
            design.add_polygon(target_layer_id, converted_polys[0])
        else:
            raise RuntimeError("Unexpected shape present in design.")
```


---

<!-- === 来源: pypde/docs/examples/ex_pyside.md === -->

# PySide2[](#pyside2 "Link to this heading")

This example uses PySide2 to build a custom GUI that can be called from a menu in ADS. PySide2 is the GUI widget toolkit that is by default shipping along with ADS.

```
# Copyright Keysight Technologies 2023 - 2023
from typing import Union

from keysight.ads import de
from keysight.ads.de import app
from PySide2 import QtCore
from PySide2.QtWidgets import QDialog, QHBoxLayout, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget

def all_lcv() -> list:
    import keysight.ads.de as de

    wrk = de.active_workspace()
    lcvs = []
    for lib_name in wrk.writable_library_names:
        lib = wrk.open_library(lib_name)
        for cell in lib.cells:
            for view in cell.views:
                lcvs.append((view, view.lcv_name))
    return lcvs

class CustomDialog(QDialog):
    def __init__(self, workspace: de.Workspace, parent: Union[QWidget, None] = None):
        super().__init__(parent)

        # Remove question mark, else have to deal with forbidden cursor
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        # Window title of the dialog
        self.setWindowTitle("All Cellviews in Workspace " + workspace.path.name)

        # Create the main vertical layout to add widgets into.
        main_vertical_layout = QVBoxLayout()

        # Text editor to display content
        # https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QPlainTextEdit.html
        editor = QPlainTextEdit()
        editor.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        editor.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        header_line = "Total number of cellviews - " + str(len(all_lcv())) + "\n"
        editor.insertPlainText(header_line)
        # Just list the view.lcv_name from (view, view.lcv_name)
        editor.appendPlainText("\n".join(lcv[1] for lcv in all_lcv()))
        editor.setReadOnly(True)
        editor.setLineWrapMode(QPlainTextEdit.NoWrap)
        # Place text editor into main layout
        main_vertical_layout.addWidget(editor)

        # create horizontal layout for button and spacer
        horizontal_layout = QHBoxLayout()
        ok_button = QPushButton("Ok")
        # this essentially dismisses the dialog when the user clicks Ok
        ok_button.clicked.connect(self.accept)  # type: ignore
        # place button in the layout and move it to the left side
        horizontal_layout.addWidget(ok_button)

        horizontal_layout.addStretch()
        # add horizontal layout to main vertical layout
        main_vertical_layout.addLayout(horizontal_layout)

        # place the layout into the body of the dialog
        self.setLayout(main_vertical_layout)

# Create and display the dialog
dlg = CustomDialog(de.active_workspace(), parent=app.window.main_pyside2_widget())
dlg.show()
```


---

<!-- === 来源: pypde/docs/examples/ex_traversing_hierarchy.md === -->

# Traversing Hierarchy[](#traversing-hierarchy "Link to this heading")

This example traverses through the design hierarchy and reports how many instances of each cell are found. The example code can be run on the shipping example of Low Pass Filter Optimization after the workspace has been loaded.

[![../../../_images/low_pass_filter_opt.png](../../../_images/low_pass_filter_opt.png)](../../../_images/low_pass_filter_opt.png)

```
# Copyright Keysight Technologies 2023 - 2023
from keysight.ads.de import CellviewRefLike, db_uu

# traverse_hierarchy("LPFoptim_lib:LPF1Hz:schematic")
def traverse_hierarchy(design_name: CellviewRefLike) -> None:
    design = db_uu.open_design(design_name)
    cell_names = {}
    for inst, _hierarchy in design.get_hierarchy_for_netlist().traverse_instances():
        cell_names[inst.cell_name] = cell_names.get(inst.cell_name, 0) + 1
    for name in sorted(cell_names.keys()):
        print(f" {name} -> {cell_names[name]} instances")
```


---

<!-- === 来源: pypde/docs/examples/ex_working_with_var.md === -->

# Working with VAR[](#working-with-var "Link to this heading")

This example shows how to update the variables inside a VAR block and evaluate an expression.

```
def var_evaluation(library: de.Library) -> None:

    def eval_expression(design: db_uu.Design, expression: str) -> str:
        expr_context = de.db.ExpressionContext()
        expr_context.setup_hierarchy_for_design(design)
        return expr_context.evaluate_expression(expression)

    design = db_uu.create_schematic(f"{library.name}:var:schematic")

    # Place an instance of VAR
    var_inst = design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR1", angle=90)
    assert var_inst.is_var_instance

    with db_uu.Transaction(design) as transaction:
        # VAR names are case-sensitive, so
        var_inst.vars["X"] = "7.5"  # X is different from
        var_inst.vars["x"] = "3.0"  # x

        assert var_inst.vars["X"] == "7.5"
        assert var_inst.vars["x"] == "3.0"

        # Values can be expressions containing other VAR names
        var_inst.vars["Y"] = "X / x"
        transaction.commit()

    # And the expressions can be evaluated like so:
    result = float(eval_expression(design, "Y"))
    assert result == 2.5  # 7.5 / 3.0

    # ADS has built-in constants like "pi" that can be used in expression evaluation.
    # See "VAR (Variables and Equations Component)" in the ADS product documentation for more information.
    with db_uu.Transaction(design) as transaction:
        var_inst.vars["r"] = "10.0"
        var_inst.vars["area"] = "pi * r ** 2"
        transaction.commit()

    result = float(eval_expression(design, "area"))
    import math

    assert math.isclose(result, 314.159265, rel_tol=1e-6)  # pi * 10.0 ^ 2

    design.save_design()
```

This example shows how to evaluate expressions containing references to VARs higher up in the design hierarchy.

```
def var_evaluation_in_design_hierarchy(library: de.Library) -> None:
    top_design = db_uu.create_schematic(f"{library.name}:top:schematic")
    middle_design = db_uu.create_schematic(f"{library.name}:middle:schematic")
    bottom_design = db_uu.create_schematic(f"{library.name}:bottom:schematic")

    # Place a VAR in bottom_design that references a VAR in middle
    var_bottom = bottom_design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR_BOTTOM", angle=90)
    var_bottom.vars["A"] = "B + 2.0"

    # Place a VAR in middle_design that references a VAR in top
    var_middle = middle_design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR_MIDDLE", angle=90)
    var_middle.vars["B"] = "C + 3.0"

    # Place a VAR in top_design
    var_top = top_design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR_TOP", angle=90)
    var_top.vars["C"] = "5.0"

    # Top has an instance of middle and middle has an instance of bottom
    bottom_inst = middle_design.add_instance(bottom_design.design_name, (0, 0), name="bottom")
    middle_inst = top_design.add_instance(middle_design.design_name, (0, 0), name="mid")

    expr_context = de.db.ExpressionContext()
    expr_context.setup_hierarchy_for_design(top_design)
    # Push down the hierarchy to the bottom design for evaluation of A
    expr_context.push_instance_for_reading(middle_inst)
    expr_context.push_instance_for_reading(bottom_inst)
    result = float(expr_context.evaluate_expression("A"))
    assert result == 10.0  # A = B + 2.0 == C + 3.0 + 2.0 == 5.0 + 3.0 + 2.0 == 10.0
    # Pop back up to the hierarchy to evaluate B
    expr_context.pop()
    result = float(expr_context.evaluate_expression("B"))
    assert result == 8.0  # B = C + 3.0 == 5.0 + 3.0 == 8.0

    top_design.save_design()
    middle_design.save_design()
    bottom_design.save_design()
```

This example shows how to evaluate an expression containing a reference to a VAR lower in the design hierarchy.

```
def var_evaluation_in_design_hierarchy_global_scope(library: de.Library) -> None:
    top_design = db_uu.create_schematic(f"{library.name}:top_global:schematic")
    bottom_design = db_uu.create_schematic(f"{library.name}:bottom_global:schematic")
    # Place an instance of VAR (Variable and Equations component)
    with db_uu.Transaction(bottom_design) as transaction:
        var_bottom = bottom_design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR1", angle=90)
        var_bottom.vars["r"] = "10.0"
        var_bottom.vars["area"] = "pi * r ** 2"
        del var_bottom.vars["X"]
        # To evaluate an expression with a reference to a VAR in a subdesign, the VAR instance must have global scope
        var_bottom.set_global_scope()
        transaction.commit()

    with db_uu.Transaction(top_design) as transaction:
        # Add an instance of bottom_design into top_design
        top_design.add_instance(bottom_design.design_name, (0, 2), name="bottom", angle=0)

        var_top = top_design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR2", angle=90)
        var_top.vars["perim"] = "2 * pi * r"
        transaction.commit()

    bottom_design.save_design()
    top_design.save_design()

    expr_context = de.db.ExpressionContext()
    expr_context.setup_hierarchy_for_design(top_design)
    result = float(expr_context.evaluate_expression("perim"))
    import math

    assert math.isclose(result, 62.831853, rel_tol=1e-6)  # 2 * pi * 10.0
```

This example shows some of the errors that can occur when working with VARs.

```
def var_evaluation_errors(library: de.Library) -> None:
    # NOTE: The error messages below are specific to the Simple Evaluator; the Full Evaluator error messages differ
    # See the Evaluation section in the Library Configuration Editor in the ADS product documentation for more information
    # on the Simple and Full Evaluators

    bottom_design = db_uu.create_schematic(f"{library.name}:cell_error_bottom:schematic")
    var_bottom = bottom_design.add_instance(("ads_datacmps", "VAR", "symbol"), (1, 0), name="VAR1", angle=90)

    # VARs are required to have at least one name/value pair and a new instance of VAR has a default "X" = "1.0"
    # It is okay to delete name/value pairs from a VAR but there must always be at least one
    try:
        del var_bottom.vars["X"]
    except RuntimeError as e:
        assert str(e) == "VAR instances need to have always at least 1 parameter"

    # When evaluating VARs, references to names must be unique within the scope of the design hierarchy
    var_bottom2 = bottom_design.add_instance(("ads_datacmps", "VAR", "symbol"), (1, 0), name="VAR2", angle=90)

    # To which X does this refer? The one in var_bottom or var_bottom2?
    var_bottom2.vars["Y"] = "X + 2"
    expr_context = de.db.ExpressionContext()
    expr_context.setup_hierarchy_for_design(bottom_design)
    try:
        # As stated previously, a VAR instance has a name/value pair that defaults to "X" = "1.0",
        # but we cannot have two different VARs in a design with the same name
        expr_context.evaluate_expression("Y")
    except RuntimeError as e:
        assert str(e) == "Schematic variable 'X' already defined at level 0"

    top = db_uu.create_schematic(f"{library.name}:cell_error_top:schematic")
    top.add_instance(bottom_design.design_name, (0, 0), name="design", angle=90)

    # To evaluate an expression with a reference to a VAR in a subdesign, the VAR instance must have global scope
    var_bottom.vars["A"] = "5.0"
    var_top = top.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 2), name="VAR2", angle=90)

    var_top.vars["B"] = "A"
    expr_context = de.db.ExpressionContext()
    expr_context.setup_hierarchy_for_design(top)
    try:
        expr_context.evaluate_expression("B")
    except RuntimeError as e:
        assert str(e) == "Error evaluating variable 'B': Error evaluating variable 'A': Variable undefined."

    # Not all expressions can be evaluated with the Simple Evaluator, which is the evaluator in automation mode
    var_top.vars["Euler"] = "e ** (pi * j)"
    if de.running_automation:
        try:
            expr_context.evaluate_expression("Euler")
        except RuntimeError as e:
            # See the Evaluation section in the Library Configuration Editor in the ADS product documentation for more information
            assert (
                str(e)
                == "Error evaluating variable 'Euler': Error evaluating variable 'j': Complex numbers are not supported by the Simple Evaluator."
            )
```


---

<!-- === 来源: pypde/docs/examples/ex_xml_rpc.md === -->

# XML RPC[](#xml-rpc "Link to this heading")

Warning

This is an advanced example and relies on so-called private functionality that may change without notice.

This is a more advanced example that shows how to control ADS through XML RPC. It uses some private functionality to ensure that any functions that are exposed are executing on the main thread again. Executing Design Environment functionality from another thread is not supported. This example is shared without warranty.

## Server[](#server "Link to this heading")

```
# Copyright Keysight Technologies 2023 - 2023
import socketserver
import threading
from xmlrpc.server import DocXMLRPCServer

class SimpleThreadedXMLRPCServer(socketserver.ThreadingMixIn, DocXMLRPCServer):
    pass

def get_all_views_wrapper() -> None:
    unused = get_all_views()
    assert unused is not None

def get_all_views() -> list[str]:
    import keysight.ads.de as de

    wrk = de.active_workspace()
    all_views = []
    for lib_name in wrk.writable_library_names:
        lib = wrk.open_library(lib_name)
        for cell in lib.cells:
            for view in cell.views:
                all_views.append(str(view.lcv_name))
    return all_views

def zoom_to_all() -> None:
    from keysight.ads import ael

    ael.call.de_view_all()

def eimt_get_all_views() -> None:
    import _pde_app

    _pde_app.ui.execute_in_main_thread(get_all_views_wrapper)

def eimt_zoom_to_all() -> None:
    import _pde_app

    _pde_app.ui.execute_in_main_thread(zoom_to_all)

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.localServer = SimpleThreadedXMLRPCServer(("0.0.0.0", 8080), logRequests=True, allow_none=True)
        self.localServer.register_function(eimt_get_all_views)
        self.localServer.register_function(eimt_zoom_to_all)

    def empty(self) -> None:
        pass

    def run(self) -> None:
        self.localServer.serve_forever()

def run_server() -> None:
    server = ServerThread()
    server.start()
```

## Client[](#client "Link to this heading")

```
# Copyright Keysight Technologies 2023 - 2023
import xmlrpc.client

def run_client() -> None:
    with xmlrpc.client.ServerProxy("http://localhost:8080/") as proxy:
        print(proxy.eimt_zoom_to_all())
```


---

<!-- === 来源: pypde/docs/examples/ex_translate_gds.md === -->

# GDSII Import and Export[](#gdsii-import-and-export "Link to this heading")

This example illustrates how to import a GDSII design with customized options.

```
def import_design(gds_file_path: str, dest_lib: de.Library, layer_map_path: str) -> None:
    # create the importer
    importer = ael.call.gds_create_importer()

    # set import options
    ael.call.gds_import_set_overwrite(importer, True)
    ael.call.gds_import_set_ignore_box(importer, True)

    # set layer map
    ael.call.gds_import_set_layermap_path(importer, layer_map_path)

    # call gds import
    ael.call.gds_import_design(importer, gds_file_path, dest_lib.name)
```

This example illustrates how to import a GDSII design with defaults.

```
def import_design_with_defaults(gds_file_path: str, dest_lib: de.Library) -> None:
    ael.call.gds_import_design(None, gds_file_path, dest_lib.name)
```

This example illustrates how to export an ADS design to a GDSII file with customized options.

```
def export_design(design: db_uu.Design, gds_file_path: str, layer_map_path: str) -> None:
    # create the exporter
    exporter = ael.call.gds_create_exporter()

    # set export options
    ael.call.gds_export_set_flatten_type(exporter, ael.decl.GDS_FLATTEN_ALL)
    ael.call.gds_export_set_rectangles_as_box(exporter, True)
    ael.call.gds_export_set_max_num_polygon_vertices(exporter, 4000)

    # set layer map
    ael.call.gds_export_set_layermap_path(exporter, layer_map_path)

    # call gds export
    ael.call.gds_export_design(exporter, design, gds_file_path)
```

This example illustrates how to export an ADS design to a GDSII file with defaults.

```
def export_design_with_defaults(design: db_uu.Design, gds_file_path: str) -> None:
    ael.call.gds_export_design(None, design, gds_file_path)
```


---

