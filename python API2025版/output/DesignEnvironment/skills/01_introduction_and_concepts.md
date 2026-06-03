# Introduction, Concepts & How-To
> **说明：** ADS Python 入门介绍、许可证说明、嵌入式 Python 用法、核心概念（术语/工作区元素/连接对象/OpenAccess/脚本执行）、以及 How-To 指南（虚拟环境设置、Pytest 使用）。

> **何时使用：** 当你需要了解 ADS Python 基础、概念术语、或配置开发环境时

---

## 本文件目录

- **Introduction** (`pydocs/intro/index.md`)
- **Licensing** (`pydocs/intro/licensing.md`)
- **Using Python in ADS Design Environment** (`pydocs/intro/embedded.md`)
- **Using ADS Design Environment Functionality in Python** (`pydocs/intro/extension.md`)
- **Concepts** (`pydocs/concepts/index.md`)
- **Terminology** (`pydocs/concepts/terminology.md`)
- **Workspace Elements** (`pydocs/concepts/workspace_elements.md`)
- **Connectivity Objects** (`pydocs/concepts/connectivity.md`)
- **OpenAccess Integration** (`pydocs/concepts/openaccess_integration.md`)
- **Python Script Execution** (`pydocs/concepts/execution.md`)
- **How-To** (`pydocs/howto/index.md`)
- **How to Set Up a Python Virtual Environment** (`pydocs/howto/venv.md`)
- **Creating a new Python virtual environment based on ADS Python** (`pydocs/howto/newvenv.md`)
- **Installing Keysight ADS wheels into an existing Python virtual environment** (`pydocs/howto/existingvenv.md`)
- **How to Use Pytest** (`pydocs/howto/pytest.md`)

---

<!-- === 来源: pydocs/intro/index.md === -->

# Introduction[](#introduction "Link to this heading")

* [Licensing](licensing.md)
* [Using Python in ADS Design Environment](embedded.md)
  + [Jupyter Console](embedded.md#jupyter-console)
  + [Customizing the ADS UI](embedded.md#customizing-the-ads-ui)
* [Using ADS Design Environment Functionality in Python](extension.md)


---

<!-- === 来源: pydocs/intro/licensing.md === -->

# Licensing[](#licensing "Link to this heading")

Importing `keysight.ads.de` pulls **Schematic** and **Layout** licenses. Note that the licenses are held for the entirety of the Python session and release when the Python session ends.


---

<!-- === 来源: pydocs/intro/embedded.md === -->

# Using Python in ADS Design Environment[](#using-python-in-ads-design-environment "Link to this heading")

The ADS Design Environment includes an embedded Python interpreter and can be accessed from the **Tools > Python Console…** top-level menu
or by using the **Ctrl-Shift-P** keyboard shortcut. If the interpreter window is already displayed, the shortcut will bring the window to the foreground.

## Jupyter Console[](#jupyter-console "Link to this heading")

[![../../_images/jupyter_console.png](../../_images/jupyter_console.png)](../../_images/jupyter_console.png)

The Jupyter console has both tooltips and tab-completion.

Note

Completion assistance does not pop up automatically. Invoke it by pressing the TAB key.

The Jupyter console supports IPython’s magic commands for IPython. For example:

> * `%clear`: clear the current window
> * `%alias`: create shortcut commands
> * `%matplotlib inline`: render matplotlib plots in the console window
> * `%matplotlib auto`: reset the handling of matplotlib plots

Full reference: [IPython Magic Commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html).

## Customizing the ADS UI[](#customizing-the-ads-ui "Link to this heading")

Customization of ADS, like adding menus, can be done using the [`keysight.ads.de.app`](../../pypde/docs/reference/de/app/index.md#module-keysight.ads.de.app "keysight.ads.de.app") module.

Creating user interfaces, like dialog windows, can be done using PySide2.

```
# Copyright Keysight Technologies 2023 - 2023
from typing import Union

from PySide2.QtWidgets import QDialog, QPlainTextEdit, QVBoxLayout, QWidget

class Form(QDialog):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self.setWindowTitle("My Customization Example")
        layout = QVBoxLayout()
        editor = QPlainTextEdit()
        editor.setPlainText("Text")
        layout.addWidget(editor)
        self.setLayout(layout)

form = Form()
form.show()
```

Note

PySide2 is installed and available when using Python inside ADS.

### Add-ons[](#add-ons "Link to this heading")

Python-implemented addons are supported by ADS using a similar mechanism as AEL-implemented addons and
can be implemented as a package where \_\_init\_\_.py contains three optional, well-known, functions.

\_\_init\_\_.py[](#id1 "Link to this code")

```
# Optionally defined setup function for the addon (Do not invoke UI elements here).
def setup_addon(addon: "Addon") -> None: ...
# Optionally defined shutdown function for the addon (Do not invoke UI elements here).
def shutdown_addon(addon: "Addon") -> None: ...
# Optionally defined function for generating custom menus
def generate_menu(addon: "Addon", win_def: "WindowDefinition") -> None: ...
```

See [Creating Custom Menus Using an Addon](../../pypde/docs/examples/ex_menu_addon.md) for a working example of a Python addon.


---

<!-- === 来源: pydocs/intro/extension.md === -->

# Using ADS Design Environment Functionality in Python[](#using-ads-design-environment-functionality-in-python "Link to this heading")

A Python script running outside ADS can access functionality of the ADS Design Environment.

```
from keysight.ads import de

de.open_workspace(...)
```

To access `keysight.ads.de` functionality, use any one of these approaches:

> 1. Use the Python interpreter in `$HPEESOF_DIR/tools/python`.
> 2. Use a virtual environment. See [How to Set Up a Python Virtual Environment](../howto/venv.md).
> 3. Add `$HPEESOF_DIR/tools/python/packages` onto your Python’s `sys.path`.

Set the environment variable `HPEESOF_DIR` to point to your ADS installation prior to
using the `keysight.ads.de` package.


---

<!-- === 来源: pydocs/concepts/index.md === -->

# Concepts[](#concepts "Link to this heading")

* [Terminology](terminology.md)
  + [Workspace Elements](workspace_elements.md)
  + [Connectivity Objects](connectivity.md)
* [OpenAccess Integration](openaccess_integration.md)
  + [Enabling Python Support For Your Library](openaccess_integration.md#enabling-python-support-for-your-library)
  + [Library Initialization](openaccess_integration.md#library-initialization)
  + [Cell Initialization](openaccess_integration.md#cell-initialization)
  + [View Initialization](openaccess_integration.md#view-initialization)
* [Python Script Execution](execution.md)
  + [Automation](execution.md#automation)


---

<!-- === 来源: pydocs/concepts/terminology.md === -->

# Terminology[](#terminology "Link to this heading")

* [Workspace Elements](workspace_elements.md)
  + [Workspace](workspace_elements.md#workspace)
  + [Library](workspace_elements.md#library)
  + [Cell](workspace_elements.md#cell)
  + [View](workspace_elements.md#view)
  + [Design](workspace_elements.md#design)
  + [Instance](workspace_elements.md#instance)
* [Connectivity Objects](connectivity.md)
  + [Net](connectivity.md#net)
  + [Term](connectivity.md#term)
  + [Pin](connectivity.md#pin)
  + [InstTerm](connectivity.md#instterm)
  + [InstPin](connectivity.md#instpin)


---

<!-- === 来源: pydocs/concepts/workspace_elements.md === -->

# Workspace Elements[](#workspace-elements "Link to this heading")

## Workspace[](#workspace "Link to this heading")

An ADS [`Workspace`](../../pypde/docs/reference/de/workspace.md#keysight.ads.de.Workspace "keysight.ads.de.Workspace") is a directory on disk, where all design work must be done.

It is used to store and organize the design work in a **Library:Cell:View** hierarchical
structure. Additionally, it contains simulation results, data display files, and other
data files.

```
# import the design environment package
from keysight.ads import de
# Creating a new workspace
workspace: de.Workspace = de.create_workspace('path_to_workspace')
# A newly created workspace is not open by default, and be can opened by:
workspace.open()
# Or, for an existing workspace:
workspace: de.Workspace = de.open_workspace('path_to_workspace')
```

Only one workspace may be open at a time. You can obtain the currently opened workspace
by calling `get_active_workspace()`.

```
from keysight.ads import de
# Check if there is an open workspace and retrieve it
if de.workspace_is_open():
    workspace: de.Workspace = de.get_active_workspace()
```

A workspace defines a **library mapping** of OpenAccess libraries. Each entry in
the mapping associates a library name, like `mylib`, with a library directory,
like `./mylib`, as well as its access mode, such as `LibraryMode.READ_ONLY`.
The library mapping is contained in a file, typically named `lib.defs`,
in the workspace directory.

## Library[](#library "Link to this heading")

An ADS [`Library`](../../pypde/docs/reference/de/library.md#keysight.ads.de.Library "keysight.ads.de.Library") is a directory, formatted as an OpenAccess library.
A library contains a set of cells plus some configuration shared across the cells.
All types of designs are contained in a library. A library does not have
to physically reside in the workspace directory.
It is common to have one or more library directories inside the workspace directory.
However, a workspace can also refer to libraries in other locations.

Libraries have a unique name and path and help prevent name collisions with
PDKs and other system libraries; they help to organize designs that share
a common technology.

Creating a library using ADS Python is straightforward:

```
from keysight.ads import de
# Create a new library named "mylib"
# Often, "path_to_library" is a path contained in a workspace directory
# and carries the same name as the library
library: de.Library = de.create_new_library("mylib", "path_to_library")
```

When a library definition file is loaded, each of the libraries defined in the file
are opened and every referenced library definition file is loaded. While workspaces
cannot be added to other workspaces, libraries from other workspaces can. To add a
library to the definition file, use the `add_library()` method.

```
from keysight.ads import de
# Given a workspace, add "library_name", located at "path_to_library"
# as a read-only library to the workspace
workspace.add_library("library_name", "path_to_library", de.LibraryMode.READ_ONLY)
```

Libraries can be opened in one of three different modes:

* SHARED: The library is opened for reading and writing, using lock files
  :   to prevent multiple users from modifying a given design in the library
      at the same time. An error is thrown if a user attempts to open a design that
      is already open by another user or process.
* NON\_SHARED: The library is opened for reading and writing without using lock files.
  :   In this mode, no error is given if two users or processes open a particular design
      at the same time.
* READ\_ONLY: The library is opened for reading only. Design modifications cannot be saved
  :   in this mode.

By default, libraries are opened as READ\_ONLY.

All designs stored in a library inherit the technology of the library and will need to
be created or attached to the library.

```
from keysight.ads import de
# Setup a basic technology for schematic and layout views of the library
# Typically you'll want to specify the substrate interfaces, layers, materials, etc.
# yourself, or copy them from another library
library.setup_schematic_tech()
library.create_layout_tech_std_ads("mil", 1000, True)
```

## Cell[](#cell "Link to this heading")

A `` Cell` `` is an object that contains cellviews (such as schematic views, layout views,
and symbol views) and other files relevant to the design (such as itemdef.py, which specifies
the model for your component). Cells are contained within libraries and are represented
as directories on disk under the library.

A cell will be automatically created the first time you create a design in a library
for a cell that does not already exist. For example, if you wish to create a new
schematic in a new cell, called “mycell”, in the library “mylib”, you can do so as follows:

```
from keysight.ads import de
# Create a new schematic design in a view called "schematic", in a cell called "mycell",
# in a library called "mylib"
design: de.db_uu.Design = de.db_uu.create_schematic("myLib:mycell:schematic")
assert design.cell.cell_name == "mycell"

# Cells can also be created directly without an initial design by passing
# in the library and cell name
# Create a new cell called "mycell1" in a library called "mylib"
cell: de.Cell = de.Cell.create(myLib, "mycell1")
assert cell.cell_name == "mycell1"
```

## View[](#view "Link to this heading")

A [`View`](../../pypde/docs/reference/de/view.md#keysight.ads.de.View "keysight.ads.de.View") represents a specific aspect or representation of a cell. For example, a view can be a
schematic view, a layout view, a symbol view, etc. Views are contained within cells and are
represented as directories on disk underneath the cell directory. Not all views are design
views; such as a Verilog view.

Similar to cells, views will be automatically created the first time you create a design in a
cell for a view that does not already exist. For example, if you wish to create a schematic
view, you can do so as follows:

```
from keysight.ads import de
# Create a new schematic design in a view called "schematic", in a cell called "mycell",
# in a library called "mylib"
design: de.db_uu.Design = de.db_uu.create_schematic("myLib:mycell:schematic")
assert design.cell.cell_name == "mycell"

# Alternatively, you can create a view directly from a cell
cell: de.Cell = de.Cell.create(myLib, "mycell1")
# Create a view of the schematic type named my_schematic
view: de.View = cell.create_view("my_schematic", "schematic")

assert view.view_name == "my_schematic"
# Not all views are design views, but a schematic view is
assert view.is_design_view and view.is_schematic_view
# Given a design view, you can obtain the associated design by using the design initializer
# and setting the named parameter view to the view object
design: de.db_uu.Design = de.db_uu.Design(view=view)
```

Iterating through all the cells and views in a library can be done as follows:

```
from keysight.ads import de
# Assumes the library "myLib" is already open
library: de.Library = de.get_open_library("myLib")
for cell in library.cells:
    print(f"cell name: {cell.cell_name}")
    for view in cell.views:
        print(f"view name: {view.view_name}")
```

## Design[](#design "Link to this heading")

A [`Design`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design") in ADS is an instance of a design view.
The ADS Python API separates designs and associated design objects into two major categories,
differentiated by the unit specification of the design, user units (db\_uu) and database units (dbu).

Every design will be one of the two types and the other type can be easily
obtained by calling either in\_user\_units or in\_database\_units on an instance
of a design. Any object or element contained in a design will be of the same unit type
as the design.

User units are the unit type that the user sees while interacting with GUI and are floating
point values. Database units are the unit type when storing the design in the database and
are integer values. You can determine the factor between the two units by calling
uu\_to\_dbu\_factor or dbu\_to\_uu\_factor on an instance of a design. Additionally, Any
point can be converted between the two units by calling uu\_to\_dbu or dbu\_to\_uu.

Schematic and symbol designs have a uu\_to\_dbu\_factor of 160 (dbu\_to\_uu\_factor of 0.00625)
and cannot be modified. Layout designs have a resolution that is determined by the technology
of the library.

Typically, when working with designs, the user unit type is used.

```
from keysight.ads import de
# Create a design
design: de.db_uu.Design = de.db_uu.create_layout("myLib:mycell:layout")
# The dbu_to_uu_factor of this layout design is determined by the setting in the technology
# in the library. If, for example, you have configured the technology to have 1000 dbu per uu,
# then the dbu_to_uu_factor will be 0.001
assert design.dbu_to_uu_factor == 0.001
# The uu_to_dbu_factor will be 1000
assert design.uu_to_dbu_factor == 1000

# Regardless of the technology settings, schematic and symbol designs have a fixed factor
# of 160 dbu per uu and cannot be modified.
design: de.db_uu.Design = de.db_uu.create_schematic("myLib:mycell:schematic")
assert design.dbu_to_uu_factor == 0.00625
assert design.uu_to_dbu_factor == 160
```

## Instance[](#instance "Link to this heading")

An [`Instance`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance") represents an instance of a design that is included as
part of another design. The design containing the instance is referred to as the parent design; the design
being instantiated is referred to as the master design. Instances can be used to create hierarchical
designs, where the master design of an instance can contain instances of other master designs, continuing
for as many levels of hierarchy as needed to complete the overall design.

Adding instances to a design can be done by calling the add\_instance method on a design object and are
specified by the library, cell, and view.

```
from keysight.ads import de

design: de.db_uu.Design = de.db_uu.create_schematic("myLib:mycell:schematic")

# Create an instance of a resistor symbol and place it in the schematic at (0, 0)
cellview: de.CellviewRef = de.CellviewRef("ads_rflib", "R", "symbol")
instance: de.db_uu.Instance = design.add_instance(cellview, (0, 0), name="R1")

# Iterating over the parameters of an instance
for param in instance.parameters:
    # The __repr__ of the parameter will return the name and value
    print(param)

# When modifying the value of a parameter, put the modification under a transaction
# and invoke the parameter changed callback
with de.db.Transaction(design) as transaction:
    instance.parameters["R"].value = "100 Ohm"
    # Some components, custom ones or ones provided by ADS, may have a callback that
    # responds to parameter changes.
    # You can invoke this callback by calling invoke_item_parameter_changed_callback
    instance.invoke_item_parameter_changed_callback("R")
    transaction.commit()

# You can obtain the model definition (also known as an item or component definition)
# of the instance
model_del: de.db.ModelDef = instance.model_def
# The model definition
```


---

<!-- === 来源: pydocs/concepts/connectivity.md === -->

# Connectivity Objects[](#connectivity-objects "Link to this heading")

Connectivity objects in ADS Python represent the logical and physical connections between components.
They include Nets, Terms, Pins, InstTerms, and InstPins.

## Net[](#net "Link to this heading")

A [`Net`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu.Net") represents the logical connectivity within a design, the
electrical path in a circuit. A collection of wires or interconnects that carry the same signal is
considered to be on the same net. Nets connect to Terms and InstTerms.

ADS Python supports multiple types of Nets:

[`ScalarNet`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.ScalarNet "keysight.ads.de.db_uu.ScalarNet"): A single-bit net that is not part of a BusNet and
does not use bus-name syntax. Generally speaking, ScalarNet is the most common type of Net.

[`BusNet`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.BusNet "keysight.ads.de.db_uu.BusNet"): A multi-bit Net that shares a common base name and uses
bus-name syntax (e.g. “A<0:7>”). A BusNet can be viewed as a collection of single-bit logical connections.

[`BusNetBit`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.BusNetBit "keysight.ads.de.db_uu.BusNetBit"): A single-bit of a BusNet and uses bus-name syntax
(e.g. “A<0>”).

[`BundleNet`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.BundleNet "keysight.ads.de.db_uu.BundleNet"). A multi-bit Net that does not share a common base
name, but instead uses comma separated names for each bit (e.g., “A, B, C”)

The following image shows a schematic with the net, Net1. The three wires and the InstTerms they are
connected to are all on Net1.

![../../_images/net.png](../../_images/net.png)

## Term[](#term "Link to this heading")

A [`Term`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term") (terminal) represents a logical connection point for a design.
Nets associated with the terminals are logically made available to the next higher level in a design hierarchy.
Pins associated with a Term represent the physical connection point for the design.

## Pin[](#pin "Link to this heading")

A [`Pin`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.Pin "keysight.ads.de.db_uu.Pin") represents a physical connection point of terminals to
nets. A term can have multiple pins, where multiple physical connections can correspond to a
single logical connection. A pin is associated with one or more phsyical figures and holds information
on the term it represents and physical properties, such as its location and angle.

```
def adding_a_pin_to_a_design(design: db_uu.Design) -> None:
    with de.db.Transaction(design) as transaction:
        net = design.find_or_add_net("P1")
        term = design.add_term(net, "P1")
        layer_id = design.create_layer_id("cond")
        dot = design.add_dot(layer_id, (0.0, 0.0))
        # Pins are associated with a term and a pinfig, often just a dot
        design.add_pin(term, dot)
        transaction.commit()
```

## InstTerm[](#instterm "Link to this heading")

An [`InstTerm`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.InstTerm "keysight.ads.de.db_uu.InstTerm") represents a logical connection point between
a net and a term in the master of an instance. An InstTerm with a corresponding Term in the master
design is considered bound to the term, and is bound by either number or by name. All bound InstTerms
of an instance must be bound the same way (either all by number or all by name). An InstTerm that does
not have a corresponding Term in the master design (if, for example, the master design was modified
and the term removed after an instance of the master was placed into a parent design) is said to be
unbound.

```
def checking_inst_term_properties(design: db_uu.Design) -> None:
    for instance in design.instances:
        for inst_term in instance.inst_terms:
            if inst_term.is_bound:
                # Obtain either the number or name from the bound InstTerm
                if inst_term.is_numbered:
                    print(f"Term is numbered: {inst_term.term_number}")
                else:
                    print(f"Term is named: {inst_term.term_name}")

            # More than one InstPin may be associated with an InstTerm:
            for inst_pin in inst_term.inst_pins:
                print(inst_pin)

            # Obtain the net from the InstTerm, which may be None
            net = inst_term.net
            print(net)
```

## InstPin[](#instpin "Link to this heading")

An [`InstPin`](../../pypde/docs/reference/de/db_uu/db_uu.md#keysight.ads.de.db_uu.InstPin "keysight.ads.de.db_uu.InstPin") represents a pin in the master design of an instance
mapped into the parent design. When a wire is connected to an InstPin, the net associated with the
wire connects to the InstTerm associated with the InstPin.

```
def connecting_a_wire_to_an_inst_term(design: db_uu.Design) -> None:
    # Create an instance of a resistor symbol and place it in the schematic at (0, 0)
    cellview_ref: de.CellviewRef = de.CellviewRef("ads_rflib", "R", "symbol")
    r1: db_uu.Instance = design.add_instance(cellview_ref, (0, 0), name="R1")
    r2: db_uu.Instance = design.add_instance(cellview_ref, (3, 0), name="R2")

    # Anytime connectivity is modified, it should be done within a transaction. Committing a transaction
    # will check, and potentially repair, the design for connectivity errors.
    with de.db.Transaction(design) as transaction:
        # Note: You can use the snap_point property for making connections
        r1_snap_point = r1.inst_pins[1].snap_point
        r2_snap_point = r2.inst_pins[0].snap_point
        assert r1_snap_point is not None and r2_snap_point is not None
        # Connecting a wire to an InstPin will propagate the Net to the InstPin
        wire = design.add_wire([r1_snap_point, r2_snap_point])
        # Setting the wire label will also set its net, which will propagate to the InstPin
        wire.add_wire_label("N1")
        assert r1.inst_pins[1].net is not None and r1.inst_pins[1].net.name == "N1"
        assert r2.inst_pins[0].net is not None and r2.inst_pins[0].net.name == "N1"

        transaction.commit()
```

In the following image, we have a schematic with two pins, each of them connecting to a component on
a net. The P1 Term is connected to the P1 Net and the P2 Term is connected to the P2 Net.

![../../_images/pin_term_net.png](../../_images/pin_term_net.png)

In this image, the symbol View of the above design was placed into a parent design as an Instance.
Connections to the pins in the master design are made through the corresponding InstTerms in the
parent design.

The P1 InstTerm is the connection point between the Net on the parent design and the Term on the master
design of the instance.

![../../_images/inst_term.png](../../_images/inst_term.png)


---

<!-- === 来源: pydocs/concepts/openaccess_integration.md === -->

# OpenAccess Integration[](#openaccess-integration "Link to this heading")

## Enabling Python Support For Your Library[](#enabling-python-support-for-your-library "Link to this heading")

In order to access Python functionality in your library, you need to notify ADS.
This is done by setting **PYTHON\_ENABLED=TRUE** in your libary’s `eesof_lib.cfg` file.
With **PYTHON\_ENABLED=TRUE**, ADS will attempt to initialize your library when it is
first opened.

## Library Initialization[](#library-initialization "Link to this heading")

Your **PYTHON\_ENABLED** library may contain an optional `__init__.py` designating the library
as a Python module. Within `__init__`, ADS will attempt to execute an initialization routine
when the library is loaded. Subsequently, it will attempt to execute a shutdown routine when
the library is unloaded.

ADS will attempt to call the well-known functions from your library’s `__init__.py`:

```
# Optionally defined initialization routine for your library, called when your library is loaded
def setup_library(library: de.Library) -> None:
    # perform any setup needed here
    ...

# Optionally defined shutdown routine for your library, called when your library is unloaded
def shutdown_library(library: de.Library) -> None:
    # perform any cleanup here
    ...
```

## Cell Initialization[](#cell-initialization "Link to this heading")

Your **PYTHON\_ENABLED** library may contain cells that require custom initialization. This can be
done by providing an optional `__init__.py` in your cell’s directory. ADS will attempt
to execute an initialization routine when your cell is first accessed.

ADS will attempt to call the well-known function from your cell’s `__init__.py`:

```
# Optionally defined initialization routine for your cell, called when your cell is first accessed
def setup_cell(cell: de.Cell) -> None:
    # perform any setup needed here
    ...
```

ADS will attempt to create an item definition for your cell, if it exists. In order to do so,
you must define your item definition within your cell using the well-known file name `itemdef.py`.
Inside `itemdef.py`, you must define the well-known method `create_itemdef`. Upon accessing
your cell, ADS will attempt to create the item definition.

For **PYTHON\_ENABLED** libraries, ADS will first attempt to create the item definition executing
`create_itemdef` in the cell’s `itemdef.py`. If that method is not available, ADS will attempt
to create the item definition by loading an AEL implementation in `itemdef.ael`.

## View Initialization[](#view-initialization "Link to this heading")

Your **PYTHON\_ENABLED** library may contain views, such as a PCell, that require custom
initialization. This can be done by providing an optional `__init__.py` in your view’s directory.
ADS will attempt to execute an initialization routine when your view is first accessed.

ADS will attempt to call the well-known function from your view’s `__init__.py`:

```
def setup_view(view: de.View) -> None:
    # perform any setup needed here
    ...
```


---

<!-- === 来源: pydocs/concepts/execution.md === -->

# Python Script Execution[](#python-script-execution "Link to this heading")

When developing Python scripts for ADS (or DDS\*), it is important to consider the execution context the script runs in,
as the set of available functionality differs depending on whether or not the script executes within the context
of the application.

When executing scripts from within the ADS application, whether from the Python console, an addon, or menu action, etc.,
application level functionality is available, you can display a message box or access a window, for example.
Scripts executing outside the application context do not have access to ADS application functionality, such as user interface
and interprocess communication. This includes, but is not limited to, the [`keysight.ads.de.app`](../../pypde/docs/reference/de/app/index.md#module-keysight.ads.de.app "keysight.ads.de.app") package and AEL application
functions that interact with the user interface or access the simulator in some manner. Simulation in automation mode can make
use of the `keysight.edatoolbox` package, which is beyond the scope of this document.

To determine if the executing context is the ADS application, the script can check [`keysight.ads.de.is_pde_app()`](../../pypde/docs/reference/de/index.md#keysight.ads.de.is_pde_app "keysight.ads.de.is_pde_app").

*\*Note: DDS is the Data Display application, which is a separate application that can be launched from the command line or
from within ADS. Both ADS and DDS have their own embedded Python interpreter and are separate execution contexts.*

## Automation[](#automation "Link to this heading")

‘Automation’ is a term used to describe when the execution context of an extension module is not the owning application.
Importing the [`keysight.ads.de`](../../pypde/docs/reference/de/index.md#module-keysight.ads.de "keysight.ads.de") or `keysight.ads.dds` packages directly into a Python process is considered
ADS or DDS automation, respectively. Additionally, importing the `keysight.ads.dds` package from within the
ADS application is considered DDS automation, just as importing [`keysight.ads.de`](../../pypde/docs/reference/de/index.md#module-keysight.ads.de "keysight.ads.de") from within the DDS application
is considered ADS automation.

When running in an automation mode (ADS, DDS, or both), scripts are not able to access the associated application’s user
interface. For example, when running scripts inside ADS, the DDS user interface APIs are not available, and vice versa.
Examples of UI functionality include, but are not limited to: windows, message boxes, palettes, menus, and toolbars.

To determine if a particular execution context is automation, the script can check the return value of the appropriate
`is_app` function, for ADS, this is [`keysight.ads.de.is_pde_app()`](../../pypde/docs/reference/de/index.md#keysight.ads.de.is_pde_app "keysight.ads.de.is_pde_app"), and for DDS, this is `keysight.ads.dds.is_dds_app()`.

*Note: The* [`keysight.ads.de.running_automation()`](../../pypde/docs/reference/de/index.md#keysight.ads.de.running_automation "keysight.ads.de.running_automation") *and* `keysight.ads.dds.running_automation()` *functions are misnamed and
those names will be deprecated in a future release. Both functions mean the same thing, that the script is not executing in
either the ADS or DDS application context, but a Python application context.*

The following examples demonstrate the different results of the `is_pde_app`, `is_dds_app`, and `running_automation`
functions when executed from different contexts:

From within the ADS application:

![../../_images/ADS_app_automation_modes.png](../../_images/ADS_app_automation_modes.png)

From within the DDS application:

![../../_images/DDS_app_automation_modes.png](../../_images/DDS_app_automation_modes.png)

From the command line:

![../../_images/Automation_mode.png](../../_images/Automation_mode.png)


---

<!-- === 来源: pydocs/howto/index.md === -->

# How-To[](#how-to "Link to this heading")

* [How to Set Up a Python Virtual Environment](venv.md)
  + [Creating a new Python virtual environment based on ADS Python](newvenv.md)
  + [Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)
* [How to Use Pytest](pytest.md)


---

<!-- === 来源: pydocs/howto/venv.md === -->

# How to Set Up a Python Virtual Environment[](#how-to-set-up-a-python-virtual-environment "Link to this heading")

It is possible to use ADS modules from a Python virtual environment rather than within the embedded ADS Python.

One option is to create a new virtual environment based on the ADS Python executable.

Alternatively, an existing virtual environment can install ADS wheels through the provided pip requirements file.

* [Creating a new Python virtual environment based on ADS Python](newvenv.md)
* [Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)


---

<!-- === 来源: pydocs/howto/newvenv.md === -->

# Creating a new Python virtual environment based on ADS Python[](#creating-a-new-python-virtual-environment-based-on-ads-python "Link to this heading")

1. Create a Python virtual environment (venv).

   The venv must be created using the Python shipped with ADS, or with another Python installation with the same major and minor version.

   Example for Linux:

   ```
   $HPEESOF_DIR/tools/python/bin/python3 -m venv --system-site-packages $HOME/ads_venv
   ```

   Example for Windows:

   ```
   %HPEESOF_DIR%\tools\python\python -m venv --system-site-packages %USERPROFILE%\ads_venv
   ```
2. Select the venv by setting **ADS\_PYTHONHOME**.

   This can be accomplished either as an environment variable or in de\_sim.cfg (user level or above, i.e. not supported in workspace-level cfg)

   Example for Linux:

   ```
   export ADS_PYTHONHOME=$HOME/ads_venv
   ```

   Example for Windows:

   ```
   set ADS_PYTHONHOME=%USERPROFILE%\ads_venv
   ```

   To set the venv path in de\_sim.cfg rather than an environment variable, add a line like this:

   ```
   ADS_PYTHONHOME={$HOME}/ads_venv
   ```
3. Run ADS. Python support is automatically enabled.

   ```
   ads
   ```

   To verify the venv is being used, execute menu **Python->Python Console…**, and type the following in the console:

   ```
   import sys
   print(sys.executable)
   ```

   The path to the Python executable will be displayed, and it should be prefixed by the venv path.


---

<!-- === 来源: pydocs/howto/existingvenv.md === -->

# Installing Keysight ADS wheels into an existing Python virtual environment[](#installing-keysight-ads-wheels-into-an-existing-python-virtual-environment "Link to this heading")

1. Open a console window and load an existing virtual environment

   > The existing venv must have been created from a Python installation with the same major and minor Python version as ADS.
2. Navigate to the ADS wheelhouse directory

   > Example for Linux:
   >
   > ```
   > cd $HPEESOF_DIR/tools/python/wheelhouse
   > ```
   >
   > Example for Windows:
   >
   > ```
   > cd %HPEESOF_DIR%\tools\python\wheelhouse
   > ```
3. Install packages with pip requirements file

   > Example for Linux:
   >
   > ```
   > python3 -m pip install -r venv_requirements.txt --find-links .
   > ```
   >
   > Example for Windows:
   >
   > ```
   > python -m pip install -r venv_requirements.txt --find-links .
   > ```
4. To verify packages have been installed
   :   Example for Linux:

       ```
       python3 -m pip list
       ```

       Example for Windows:

       ```
       python -m pip list
       ```

       You should see various keysight-ads-\* wheels listed


---

<!-- === 来源: pydocs/howto/pytest.md === -->

# How to Use Pytest[](#how-to-use-pytest "Link to this heading")

Pytest is a mature full-featured testing tool for Python. It is useful when developing Python scripts.
Pytest is not installed in the ADS Python installation.

The recommended steps to use Pytest are:

> 1. Create a Python virtual environment. See [How to Set Up a Python Virtual Environment](venv.md).
> 2. Activate the Python virtual environment.
> 3. Install pytest into the virtual environment.
>
>    > ```
>    > pip install pytest
>    > ```
> 4. Run pytest on your test scripts.
>
>    > ```
>    > cd path/to/tests
>    > pytest
>    > ```


---

