# Pydocs
> **说明：** Pydocs 相关页面。

> **何时使用：** 当你需要查阅 Pydocs 相关内容时

---

## 本文件目录

- **Connectivity Objects** (`pydocs/concepts/connectivity.md`)
- **ADS Concepts** (`pydocs/concepts/index.md`)
- **Workspace Elements** (`pydocs/concepts/workspace_elements.md`)
- **Use Python in the ADS Application** (`pydocs/howto/embedded.md`)
- **Execute Python Scripts in Different Contexts** (`pydocs/howto/execution.md`)
- **Export Workspace and Design Objects to Python** (`pydocs/howto/exporter.md`)
- **How-To** (`pydocs/howto/index.md`)
- **Develop a Python Pcell in ADS** (`pydocs/howto/pcell.md`)
- **Use Pytest** (`pydocs/howto/pytest.md`)
- **Enable Python Support For Your Library** (`pydocs/howto/python_integration.md`)
- **Record Actions in ADS as Python Code** (`pydocs/howto/recorder.md`)
- **Set Up a Python Virtual Environment** (`pydocs/howto/venv.md`)
- **Set Up Visual Studio Code for Development** (`pydocs/howto/vscode.md`)
- **Introduction** (`pydocs/intro/index.md`)
- **Deprecated APIs** (`pydocs/py/_generated/deprecations.md`)

---

<!-- === 来源: pydocs/concepts/connectivity.md === -->

# Connectivity Objects[](#connectivity-objects "Link to this heading")

Connectivity objects in ADS Python represent the logical and physical connections between components.
They include Nets, Terms, Pins, InstTerms, and InstPins.

To learn more about connectivity objects available within an ADS design, see [Connectivity Objects](..%5C..%5C..%5C..%5C..%5Cads%5CContent%5Cads2026update2%5Cael%5CConnectivity_Objects.md).

## Net[](#net "Link to this heading")

A [`Net`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.Net.md#keysight.ads.de.db_uu.Net "keysight.ads.de.db_uu.Net") represents the logical connectivity within a design, the
electrical path in a circuit. A collection of wires or interconnects that carry the same signal is
considered to be on the same net. Nets connect to Terms and InstTerms.

ADS Python supports multiple types of Nets:

[`ScalarNet`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.ScalarNet.md#keysight.ads.de.db_uu.ScalarNet "keysight.ads.de.db_uu.ScalarNet"): A single-bit net that is not part of a BusNet and
does not use bus-name syntax. Generally speaking, ScalarNet is the most common type of Net.

[`BusNet`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.BusNet.md#keysight.ads.de.db_uu.BusNet "keysight.ads.de.db_uu.BusNet"): A multi-bit Net that shares a common base name and uses
bus-name syntax (e.g. “A<0:7>”). A BusNet can be viewed as a collection of single-bit logical connections.

[`BusNetBit`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.BusNetBit.md#keysight.ads.de.db_uu.BusNetBit "keysight.ads.de.db_uu.BusNetBit"): A single-bit of a BusNet and uses bus-name syntax
(e.g. “A<0>”).

[`BundleNet`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.BundleNet.md#keysight.ads.de.db_uu.BundleNet "keysight.ads.de.db_uu.BundleNet"). A multi-bit Net that does not share a common base
name, but instead uses comma separated names for each bit (e.g., “A, B, C”)

The following image shows a schematic with the net, Net1. The three wires and the InstTerms they are
connected to are all on Net1.

![../../_images/net.png](../../_images/net.png)

## Term[](#term "Link to this heading")

A [`Term`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.Term.md#keysight.ads.de.db_uu.Term "keysight.ads.de.db_uu.Term") (terminal) represents a logical connection point for a design.
Nets associated with the terminals are logically made available to the next higher level in a design hierarchy.
Pins associated with a Term represent the physical connection point for the design.

## Pin[](#pin "Link to this heading")

A [`Pin`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.Pin.md#keysight.ads.de.db_uu.Pin "keysight.ads.de.db_uu.Pin") represents a physical connection point of terminals to
nets. A term can have multiple pins, where multiple physical connections can correspond to a
single logical connection. A pin is associated with one or more physical figures and holds information
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

An [`InstTerm`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.InstTerm.md#keysight.ads.de.db_uu.InstTerm "keysight.ads.de.db_uu.InstTerm") represents a logical connection point between
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

An [`InstPin`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.InstPin.md#keysight.ads.de.db_uu.InstPin "keysight.ads.de.db_uu.InstPin") represents a pin in the master design of an instance
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

<!-- === 来源: pydocs/concepts/index.md === -->

# ADS Concepts[](#ads-concepts "Link to this heading")

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

An ADS [`Workspace`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.Workspace.md#keysight.ads.de.Workspace "keysight.ads.de.Workspace") is a directory on disk, where all design work must be done.

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
by calling [`keysight.ads.de.active_workspace()`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.active_workspace.md#keysight.ads.de.active_workspace "keysight.ads.de.active_workspace").

```
from keysight.ads import de
# Check if there is an open workspace and retrieve it
if de.workspace_is_open():
    workspace: de.Workspace = de.active_workspace()
```

A workspace defines a **library mapping** of OpenAccess libraries. Each entry in
the mapping associates a library name, like `mylib`, with a library directory,
like `./mylib`, as well as its access mode, such as `LibraryMode.READ_ONLY`.
The library mapping is contained in a file, typically named `lib.defs`,
in the workspace directory.

## Library[](#library "Link to this heading")

An ADS [`Library`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.Library.md#keysight.ads.de.Library "keysight.ads.de.Library") is a directory, formatted as an OpenAccess library.
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
library to the definition file, use the [`Workspace.add_library()`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.Workspace.md#keysight.ads.de.Workspace.add_library "keysight.ads.de.Workspace.add_library") method.

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

A [`Cell`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.Cell.md#keysight.ads.de.Cell "keysight.ads.de.Cell") is an object that contains cellviews (such as schematic views, layout views,
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

A [`View`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.View.md#keysight.ads.de.View "keysight.ads.de.View") represents a specific aspect or representation of a cell. For example, a view can be a
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

A [`Design`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.Design.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design") in ADS is an instance of a design view.
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

An [`Instance`](../../pypde/docs/reference/de/db_uu/_autosummary/keysight.ads.de.db_uu.Instance.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance") represents an instance of a design that is included as
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

<!-- === 来源: pydocs/howto/embedded.md === -->

# Use Python in the ADS Application[](#use-python-in-the-ads-application "Link to this heading")

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

Creating user interfaces, like dialog windows, can be done using PySide.

```
# Copyright Keysight Technologies 2023 - 2023
from typing import Union

from PySide6.QtWidgets import QDialog, QPlainTextEdit, QVBoxLayout, QWidget

class Form(QDialog):
    def __init__(self, parent: Union[QWidget, None] = None) -> None:
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

PySide6 is installed and available when using Python inside ADS.

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

See [Creating Custom Menus Using an Addon](../../pypde/docs/examples/ui/ex_menu_addon.md) for a working example of a Python addon.


---

<!-- === 来源: pydocs/howto/execution.md === -->

# Execute Python Scripts in Different Contexts[](#execute-python-scripts-in-different-contexts "Link to this heading")

When developing Python scripts for ADS (or DDS\*), it is important to consider the execution context the script runs in,
as the set of available functionality differs depending on whether or not the script executes within the context
of the application.

When executing scripts from within the ADS application, whether from the Python console, an addon, or menu action, etc.,
application level functionality is available, you can display a message box or access a window, for example.
Scripts executing outside the application context do not have access to ADS application functionality, such as user interface
and interprocess communication. This includes, but is not limited to, the [`keysight.ads.de.app`](../../pypde/docs/reference/de/app/index.md#module-keysight.ads.de.app "keysight.ads.de.app") package and AEL application
functions that interact with the user interface or access the simulator in some manner. Simulation in automation mode can make
use of the `keysight.edatoolbox` package, which is beyond the scope of this document.

To determine if the executing context is the ADS application, the script can check [`keysight.ads.de.is_pde_app()`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.is_pde_app.md#keysight.ads.de.is_pde_app "keysight.ads.de.is_pde_app").

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
`is_app` function, for ADS, this is [`keysight.ads.de.is_pde_app()`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.is_pde_app.md#keysight.ads.de.is_pde_app "keysight.ads.de.is_pde_app"), and for DDS, this is `keysight.ads.dds.is_dds_app()`.

*Note: The* [`keysight.ads.de.running_automation()`](../../pypde/docs/reference/de/_autosummary/keysight.ads.de.running_automation.md#keysight.ads.de.running_automation "keysight.ads.de.running_automation") *and* `keysight.ads.dds.running_automation()` *functions are misnamed and
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

<!-- === 来源: pydocs/howto/exporter.md === -->

# Export Workspace and Design Objects to Python[](#export-workspace-and-design-objects-to-python "Link to this heading")

The **Python Exporter** is a tool that allows you to export your workspace objects (including, but not limited to: libraries, substrates, cells, and designs) to Python scripts.

The resulting script (or scripts) use the ADS Python API to recreate the exported objects. It is an invaluable tool for learning how to use the ADS Python API
to create designs and other workspace objects programmatically.

The **Python Exporter** consists of two components:

> * The exporter itself, which are Python scripts that iterate over your workspace objects to generate the code necessary to recreate them. Executing the generated code recreates the original workspace object, or set of objects, using the ADS Python API.
> * An ADS Addon that allows you to easily run the exporter from within ADS by providing context menu options for exporting your workspace objects to Python.

The exporter source code is located at `%HPEESOF_DIR%\tools\python\packages\keysight\ads\de\experimental\python_exporter`. The exporter source provides some customizable
options for how the code is generated; these options may be toggled in the source code directly. In addition to being the tool that generates the Python code, it illustrates
how to iterate over the various types of ADS workspace and design objects to obtain all the information necessary for recreation.

It is recommended to review the source code and to also trace through the code in a debugger to understand how it works, as it serves as an extremely useful reference for learning how to use the ADS Python API.
See [Configure the Run/Debug environment](vscode.md#configure-the-rundebug-environment) for information on how to set up VS Code to debug ADS Python scripts.

The Addon can be enabled by going to **Tools -> App Manager** and selecting the **Python Exporter** from the list of Addons in the ADS Application Features section.

![../../_images/PythonExporterAddon.png](../../_images/PythonExporterAddon.png)

The Addon implementation is located at `%HPEESOF_DIR%\addons\python\python_exporter`.

Enabling the **Python Exporter** adds the context menu item, **Export Python**, to certain context menus in ADS that appear when right-clicking. The option appears in the context menu when
right-clicking on various elements in the Folder and Library views of the main window, as well as when right-clicking on a design in a design window. For example, when selecting Export Python from
the context menu of a design window, the exporter will generate the necessary Python code for recreating the design and save it to the clipboard. The generated design will be located
in a new cell, having the same name as the original cell but with a `_script` suffix appended. The rules for cell names can be modified as desired in the exporter source code.

**Note:** The animation below showing **Copy Python Recipe Script** is from an older version of ADS and has been replaced with **Export Python**.

![../../_images/PythonExporter.gif](../../_images/PythonExporter.gif)

In addition to exporting single designs, context menu options have been added when right-clicking on the workspace, library, cell, or view from Folder and Library views that allow
you to export your workspace, library, cells, and views to Python. When using these options, a `de_exported_python` folder will be created in the workspace and will contain all
the scripts necessary for recreation. Executing the `generate_all.py` script will run all the generated scripts for recreating your workspace, library, cells, and/or views.
When using these options, only one script (the top-level script, which varies depending on which export option you selected) will save to the clipboard; the other scripts will
need to be accessed from the `de_exported_python` folder in the workspace.

![../../_images/PythonExporterAddon-2.png](../../_images/PythonExporterAddon-2.png)


---

<!-- === 来源: pydocs/howto/index.md === -->

# How-To[](#how-to "Link to this heading")

* [Use Python in the ADS Application](embedded.md)
  + [Jupyter Console](embedded.md#jupyter-console)
  + [Customizing the ADS UI](embedded.md#customizing-the-ads-ui)
* [Set Up a Python Virtual Environment](venv.md)
  + [Creating an ADS based Python virtual environment](venv.md#creating-an-ads-based-python-virtual-environment)
  + [Install Keysight ADS Wheels into an Existing Python Virtual Environment](venv.md#install-keysight-ads-wheels-into-an-existing-python-virtual-environment)
  + [ADS Python Environment Variables](venv.md#ads-python-environment-variables)
* [Set Up Visual Studio Code for Development](vscode.md)
* [Use Pytest](pytest.md)
* [Enable Python Support For Your Library](python_integration.md)
  + [Library Initialization](python_integration.md#library-initialization)
  + [Cell Initialization](python_integration.md#cell-initialization)
  + [View Initialization](python_integration.md#view-initialization)
* [Execute Python Scripts in Different Contexts](execution.md)
  + [Automation](execution.md#automation)
* [Export Workspace and Design Objects to Python](exporter.md)
* [Record Actions in ADS as Python Code](recorder.md)
* [Develop a Python Pcell in ADS](pcell.md)


---

<!-- === 来源: pydocs/howto/pcell.md === -->

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


---

<!-- === 来源: pydocs/howto/pytest.md === -->

# Use Pytest[](#use-pytest "Link to this heading")

Pytest is a popular testing framework for Python and quite useful when developing Python scripts.
Pytest is not installed in the ADS Python installation, and there are multiple ways to obtain it.

**QUICK REFERENCE (More detailed instructions below):**

* [Using Pytest inside VSCode](#using-pytest-inside-vscode)
* [Using Pytest outside VSCode](#using-pytest-outside-vscode)

**Using Pytest inside VSCode**

Pytest integrates well with VS Code and has built-in support for running and debugging tests.

See [Set Up Visual Studio Code for Development](vscode.md#setup-vscode) for instructions on how to set up VS Code.

Click on the Testing icon in the Activity Bar on the side of the window to bring up the testing tab. Click on the **Configure Python Tests** button to configure the test framework.

In the dropdown that appears at the top of the window, select the root directory you wish to configure tests for.

Select the **pytest** option from the list of available test frameworks.

Pytest has rules for discovering your tests. By default, Pytest will look for files that start with `test_` or end with `_test.py` under the selected directory and subdirectories.
In those files, it will look for functions that start with `test_`. If you want to change the rules for discovering your tests, you can do so by creating a `pytest.ini` file in the root directory of your local code.

[pytest.org](https://docs.pytest.org/en/stable/index.html) has a wealth of information on how to configure and write tests using Pytest.

Select `. Root directory` (or any subdirectory you like). You can change this option later if you want to.

![../../_images/VSCode_configure_pytest.gif](../../_images/VSCode_configure_pytest.gif)

**NOTE:** In order to discover your tests, Pytest will import your test file(s), executing global code in the process. This may result in an error. If this happens, some or all of your tests may not appear in the Tests Results panel.
The Python Output window shows the log of the test discovery process. Errors encountered will be shown in the log.

Below is a screenshot of the Python Output window showing successful Pytest discovery.

![../../_images/VSCode_pytest_discovery.png](../../_images/VSCode_pytest_discovery.png)

Tests can be run individually or all at once. Click one of the Debug (or Run) icons to run your tests.
Tests that have not run yet are shown as a gray circle, while successful tests are shown as a green circle with a check and failed tests are shown as a red circle with an x.

![../../_images/VSCode_run_pytest_1.gif](../../_images/VSCode_run_pytest_1.gif)

Existing results can be cleared by selecting the **Clear All Results** option from the Testing actions dropdown menu.

![../../_images/VSCode_run_pytest_2.gif](../../_images/VSCode_run_pytest_2.gif)

**Using Pytest outside VSCode**

Should you prefer to run Pytest outside of VS Code, you can do so from the command line.
The recommended steps to use Pytest are:

> 1. Create a Python virtual environment. See [Set Up a Python Virtual Environment](venv.md).
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

Pytest will, by default, search for and execute any test functions under the current working directory and subdirectories using the following rules:

> 1. Pytest will search for tests in any files prefixed `test_*.py` or postfixed `*_test.py`. This can be
>    configured with the [python\_files](https://docs.pytest.org/en/stable/reference/reference.html#confval-python_files) option.
> 2. Any files considered by the above rules will be searched for any functions prefixed with `test*`, this can be
>    configured with the
>    [python\_functions](https://docs.pytest.org/en/stable/reference/reference.html#confval-python_functions) option.

Additionally you may limit the scope of which tests are run by providing a directory, file, or test name on the command
line as follows:

> 1. For directories: `pytest path/to/test/directory`
> 2. For test files: `pytest path/to/test_file.py`
> 3. For specific tests: `pytest path/to/test_file.py::test_function_name`

For complete documentation reference the [pytest docs](https://docs.pytest.org/en/stable/how-to/index.html).


---

<!-- === 来源: pydocs/howto/python_integration.md === -->

# Enable Python Support For Your Library[](#enable-python-support-for-your-library "Link to this heading")

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

<!-- === 来源: pydocs/howto/recorder.md === -->

# Record Actions in ADS as Python Code[](#record-actions-in-ads-as-python-code "Link to this heading")

The **Python Recorder** is a feature in ADS that allows you to record your actions in the ADS Design Environment as Python code.

This can be useful for automating repetitive tasks, creating scripts for design modification, or learning how to use the ADS Python API.

To enable the Python Recorder, choose the **Start Recording Python** option from the **Tools** menu:

![../../_images/PythonRecorder.png](../../_images/PythonRecorder.png)

Once recording is started, actions performed in the ADS Design Environment will be recorded as Python code and will appear in the Python console.
You can stop the recording at any time by selecting the **Stop Recording Python** option from the **Tools** menu.

Note

Not every action is ADS is recorded and some actions may be recorded as AEL calls rather than Python API calls. The recorder is an evolving feature and will be improved over time.


---

<!-- === 来源: pydocs/howto/venv.md === -->

# Set Up a Python Virtual Environment[](#set-up-a-python-virtual-environment "Link to this heading")

It is possible to use ADS modules from a Python virtual environment rather than within the embedded ADS Python.

One option is to create a new virtual environment based on the ADS Python executable.

Alternatively, an existing virtual environment can install ADS wheels through the provided pip requirements file.

## Creating an ADS based Python virtual environment[](#creating-an-ads-based-python-virtual-environment "Link to this heading")

It is possible to create a Python virtual environment (venv) based on the Python shipped with ADS.
This is the recommended way to modify the ADS Python environment with external python packages.

Note

The environment variable, **HPEESOF\_DIR** points to the location of your current ADS install location.

Note

**%HOME%** is not set by default on Windows. It is recommended to set this to your user home directory, e.g. **%USERPROFILE%**.

```
set HOME=%USERPROFILE%
```

Warning

Virtual environments created in one version of ADS may not work in another version of ADS. It is recommend that you create a new virtual environment for each version of ADS you use.

1. Creating a Python virtual environment (venv).

   The venv must be created using the Python shipped with ADS

   Example for Linux:

   ```
   $HPEESOF_DIR/tools/python/bin/python3 -m venv --system-site-packages $HOME/ads_venv
   ```

   Example for Windows:

   ```
   %HPEESOF_DIR%\tools\python\python -m venv --system-site-packages %HOME%\ads_venv
   ```
2. (Optional) Modify your venv by installing additional Python packages.

   Activate the venv and install any additional packages you need.

   Example for Linux:

   ```
   source $HOME/ads_venv/bin/activate
   python3 -m pip install -r /path/to/your/requirements.txt
   ```

   Example for Windows:

   ```
   %HOME%\ads_venv\Scripts\activate
   py -m pip install -r \path\to\your\requirements.txt
   ```
3. Select the venv by setting **ADS\_PYTHONHOME**.

   This can be accomplished either as an environment variable or in de\_sim.cfg (user level or above, i.e. not supported in workspace-level cfg)

   Example for Linux:

   ```
   export ADS_PYTHONHOME=$HOME/ads_venv
   ```

   Example for Windows:

   ```
   set ADS_PYTHONHOME=%HOME%\ads_venv
   ```

   To set the venv path in de\_sim.cfg rather than an environment variable, add a line like this:

   ```
   ADS_PYTHONHOME={$HOME}/ads_venv
   ```
4. Run ADS. Python support is automatically enabled.

   ```
   ads
   ```

   To verify the venv is being used, execute menu **Python->Python Console…**, and type the following in the console:

   ```
   import sys
   print(sys.executable)
   ```

   The path to the Python executable will be displayed, and it should be prefixed by the venv path.

## Install Keysight ADS Wheels into an Existing Python Virtual Environment[](#install-keysight-ads-wheels-into-an-existing-python-virtual-environment "Link to this heading")

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
   > python3 -m pip install -r venv_requirements.txt --no-index --no-cache-dir --only-binary=:all: --find-links=.
   > ```
   >
   > Example for Windows:
   >
   > ```
   > python -m pip install -r venv_requirements.txt --no-index --no-cache-dir --only-binary=:all: --find-links=.
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

## ADS Python Environment Variables[](#ads-python-environment-variables "Link to this heading")

This document describes optional environment variables used to configure the Python environment in ADS.

### ADS\_PYTHONHOME[](#ads-pythonhome "Link to this heading")

Similar to the **PYTHONHOME** environment variable, this variable specifies the path to the Python virtual environment (venv) that ADS will use.
This is useful for when you want to use a custom Python virtual environment instead of the default embedded Python in ADS.


---

<!-- === 来源: pydocs/howto/vscode.md === -->

# Set Up Visual Studio Code for Development[](#set-up-visual-studio-code-for-development "Link to this heading")

Although other IDEs are available, Keysight recommends using Visual Studio Code (VSCode) for Python development with ADS.

**NOTE:** The term `workspace` used throughout these instructions refer to a VSCode workspace, not an ADS workspace.
These instructions are tailored towards Windows, but apply for Linux as well, with minor differences.

**QUICK REFERENCE (More detailed instructions below):**

* [Install VSCode and the recommended extensions](#install-vscode-and-recommended-extensions)
* [Add ADS Python source code to the workspace](#add-ads-python-source-code-to-the-workspace)
* [Add your local Python code to the workspace](#add-your-local-python-code-to-the-workspace)
* [Select the Python interpreter to use](#select-the-python-interpreter-to-use)
* [Configure the Run/Debug environment](#configure-the-rundebug-environment)

**1. Install VSCode and Recommended Extensions**

VSCode can be downloaded from <https://code.visualstudio.com/>. The latest available version is recommended.

If you already have VSCode installed, ensure that you have the latest version by selecting **Help** > **Check for Updates…** from the menu bar.
You are free to use any extensions you like to aid with your development, but Keysight recommends the following extensions:

* **Python** - This extension provides support for Python development.
* **Python Debugger** - This extension provides support for debugging Python code in VSCode. This is typically included with the Python extension.
* **Pylance** - This extension is built on top of Pyright and provides support for static type checking and IntelliSense in Python code.
* **Black Formatter** - This extension provides support for formatting Python code using the Black code formatter; increasing readability and consistency.
* **Ruff** - This extension provides support for linting Python code using the Ruff linter, enforcing quality and style standards.

To install these extensions, open VSCode and select the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
Then search for each extension by name and click the Install button.

**Recommended Extensions**

![../../_images/VSCode_extensions.png](../../_images/VSCode_extensions.png)

**NOTE:** ADS relies on the `HPEESOF_DIR` environment variable and to run in [automation mode](execution.md#automation-mode), this variable must be set to
the ADS installation directory of the version you are working with.

**2. Add ADS Python Source Code to the Workspace**

A VSCode workspace is a collection of one or more directories, each called a root directory. Each root directory can be configured with its own settings, as desired.
It is recommended you add the ADS Python source code to the workspace for easy navigation and debugging.

Do this by selecting **File** > **Add Folder to Workspace…** from the menu bar and choosing the `%HPEESOF_DIR%\tools\python\packages` directory.

![../../_images/VSCode_add_folder_to_workspace.gif](../../_images/VSCode_add_folder_to_workspace.gif)

Alternatively, if there is no workspace open, you can click the **Open Folder** button from the Explorer panel. If no workspace has been created, adding a folder will create a new workspace with the selected folder as a root directory.
Additional directories can be added in this manner. You can save your workspace by selecting **File** > **Save Workspace As…** from the menu bar.
This will create a file with the extension `.code-workspace` that contains the workspace configuration.

**NOTE:** If you wish to add the Python example scripts to your workspace as well, they are located in `%HPEESOF_DIR%\doc\python\de\examples`.

**3. Add Your Local Python Code to the Workspace**

Add any local code you are developing in the same manner as above.

Below shows an example workspace.

![../../_images/VSCode_example_workspace.png](../../_images/VSCode_example_workspace.png)

**4. Select the Python Interpreter to Use**

By default, VSCode will use the Python interpreter that is in your system path. You will need to select the interpreter provided by ADS.
If you wish to create your own Python virtual environment and use the interpreter from there, see [Set Up a Python Virtual Environment](venv.md#setup-venv) for more information.

Open up the **Command Palette** by pressing `F1` (or `Ctrl+Shift+P`, or **View -> Command Palette…** from the menu bar) and type `Python: Select Interpreter`.

While each root directory in the workspace may have its own interpreter, you should use the one provided by ADS.
Choosing “Select at Workspace level” will set the interpreter for all root directories in the workspace.

**NOTE:** In the interpreter selection box, the interpreter listed as **Recommended** or **Global** may not be the interpreter you want to use.
If necessary, choose the “Enter interpreter path…” option and navigate to the Python interpreter provided by ADS.
It is located at `%HPEESOF_DIR%\tools\python\python.exe` (or `$HPEESOF_DIR/tools/python/bin/python3` on Linux).

![../../_images/VSCode_select_interpreter.gif](../../_images/VSCode_select_interpreter.gif)

**5. Configure the Run/Debug Environment**

To run or debug your code, you will need to configure the Run/Debug environment. This is done by creating a `launch.json` file in the `.vscode` directory of your workspace.

* Select the Run and Debug icon in the Activity Bar on the side of the window and choose the **create a launch.json file** option.
* Choose the root directory corresponding to your local code.
* Choose the “Python Debugger” option from the list of available debuggers.
* Choose the “Python File” option from the list of available configurations. This will create a `.vscode` directory in the root directory with a `launch.json` file inside.

This will create a `launch.json` file with contents shown below:

**NOTE:**: When debugging, you may want to step into the ADS Python source code.
To do so, you must add the “justMyCode”: false option to the configuration. You can do this by manually editing the configuration, and is shown below.

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode" : false
        }
    ]
}
```

![../../_images/VSCode_debug_settings.gif](../../_images/VSCode_debug_settings.gif)

**NOTE:** Each section in the `configurations` array is a separate run configuration that appears in the dropdown menu of the Run and Debug view.

A configuration can also be set up to pass command line arguments to the script being run.
To do this, add the `args` field to the configuration and set it to an array of strings. For example:

```
{
    "name": "Python Debugger: My Custom Script",
    "type": "debugpy",
    "request": "launch",
    "program": "/path/to/my_script.py",
    "console": "integratedTerminal",
    "justMyCode" : false,
    "args": [
        "arg1",
        "arg2"
    ]
}
```

**Verifying the Run/Debug Settings**

Now that you have a `launch.json` file, you can verify that the settings are correct.

Copy the following code into a new file called `test_example.py` in the root directory for your local code (it is also located in `%HPEESOF_DIR%\doc\python\de\examples\vscode_example`).

**NOTE:** Name the file `test_example.py`, as it will be used later on in these instructions to verify the Pytest configuration.

```
def test_import_keysight_ads_de_example() -> None:
    try:
        from keysight.ads import de
    except ImportError as e:
        raise ImportError("Failed to import keysight.ads.de. Verify your environment has been configured properly.") from e

    version = de.version()

    assert version >= 630, "Version of keysight.ads.de is not as expected."
    print(f"Import of keysight.ads.de successful in ADS version {de.version()}.")

# Run the test if this file is executed directly
if __name__ == "__main__":
    test_import_keysight_ads_de_example()
```

Open the file `test_example.py` and set a breakpoint on the line `from keysight.ads import de` by clicking in the left margin of the editor window.
Set another breakpoint on the line `version = de.version()`.
Now click the green triangle button to start debugging. The debugger will stop at the breakpoint, allowing you to step through your source code.

There are different ways to debug the active file in VSCode, but by choosing the **Python Debugger: Current File** option and clicking the green triangle button,
you will be able to step into the ADS Python source code.

While stopped on the first breakpoint, click the `Step Over (F10)` button (or press `F10`) to step over the line `from keysight.ads import de`.

**NOTE:** The debugger toolbar may not appear in the same location as shown below.
If successful, the debugger will proceed to the next statement and be located at the second breakpoint.

Now step into the ADS Python source code by clicking the `Step Into (F11)` button (or pressing `F11`).

**NOTE:** If the `justMyCode` option is set to `false`, as described above, the debugger will step into the ADS Python source code.
When not set, you may see a small popup window from VSCode indicating that it skipped stepping into code that is not located in your workspace.

The `VARIABLES` portion of the Run and Debug view is where you can view or modify the values of your variables.

![../../_images/VSCode_debugging.gif](../../_images/VSCode_debugging.gif)

**Attach to Process**

You can attach to ADS using the `debugpy` library. This allows you to run your code in ADS and debug it in VSCode. To do this, first create a launch configuration in your `launch.json` file for attaching to a process.

Set the `host` to `localhost` and `port` to an available port; this example uses `8765`.

Below is an updated `launch.json` file with the attach configuration added.

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": false
        },
        {
            "name": "Python Attach: Port 8765",
            "type": "debugpy",
            "request": "attach",
            "justMyCode": false,
            "connect": {
                "host": "localhost",
                "port": 8765
            }
        }
    ]
}
```

**NOTE:** A copy of this file is located in `%HPEESOF_DIR%\doc\python\de\examples\vscode_example`.

**Verifying the Attach to Process Settings**

To verify the process attach settings, launch ADS and open up the Python console. You can do so by selecting **Tools** > **Python Console…** from the menu bar.

From the Python console, run the following code to listen to localhost and the port specified above.

```
import debugpy
debugpy.listen(("localhost", 8765))
```

![../../_images/VSCode_debugpy_1.gif](../../_images/VSCode_debugpy_1.gif)

In VSCode, select the Run and Debug icon in the Activity Bar and choose the **Python Attach: Port 8765** option from the dropdown menu.
Then click the green triangle button to attach the debugger to ADS.

You will know you are connected when the `CALL STACK` portion of the Run and Debug becomes populated.

Navigate to the `de.version()` API located in `%HPEESOF_DIR%\packages\keysight\ads\de\__init__.py` and set a breakpoint on the line `return _pde.version()`.

**NOTE:** You can press `F12` on the API in `test_example.py` to quickly go to the definition.

Now that you have connected to ADS, from the Python console in ADS, type `de.version()` and press Enter.
This will call the `de.version()` API and the debugger in VSCode will stop on the breakpoint you set.

To return control back to ADS, you can click the `Continue (F5)` button (or press `F5`) in the debugger toolbar.

![../../_images/VSCode_debugpy_2.gif](../../_images/VSCode_debugpy_2.gif)


---

<!-- === 来源: pydocs/intro/index.md === -->

# Introduction[](#introduction "Link to this heading")

ADS provides a Python environment that is tightly integrated with the ADS Design Environment. This allows you to create and modify designs and technology, automate tasks, create custom user interfaces, and extend the functionality of ADS using Python.

Note

This documentation assumes you have a working knowledge of Python programming. If you are new to Python, consider reviewing introductory Python tutorials and resources available online.

## Using ADS Design Environment Functionality in Python[](#using-ads-design-environment-functionality-in-python "Link to this heading")

To develop with the ADS Python API, you can either use the embedded Python interpreter within ADS or set up an external Python environment that can access ADS Design Environment functionality.

These two approaches are referred to as “application (or app) mode” and “automation mode,” respectively.
For more information on these modes, and their importance, see [Execute Python Scripts in Different Contexts](../howto/execution.md#python-script-execution).

Warning

Importing `keysight.ads.de` pulls **Schematic** and **Layout** licenses. Note that the licenses are held for the entirety of the Python session and release when the Python session ends.

## Automation[](#automation "Link to this heading")

A Python script running outside ADS can access functionality of the ADS Design Environment.

```
from keysight.ads import de

de.open_workspace(...)
```

To access `keysight.ads.de` functionality, use any one of these approaches:

> 1. Use the Python interpreter in `$HPEESOF_DIR/tools/python`.
> 2. Use a virtual environment. See [Set Up a Python Virtual Environment](../howto/venv.md).
> 3. Add `$HPEESOF_DIR/tools/python/packages` onto your Python’s `sys.path`.

Set the environment variable `HPEESOF_DIR` to point to your ADS installation prior to
using the `keysight.ads.de` package.

## Embedded Python in ADS[](#embedded-python-in-ads "Link to this heading")

A Python interpreter is embedded within the ADS Design Environment application and is accessible from a number of different ways throughout the ADS application.

Note

See [Use Python in the ADS Application](../howto/embedded.md#embedded-python) for more information on using the embedded Python interpreter in ADS.

Note

See [Enable Python Support For Your Library](../howto/python_integration.md#enabling-python-support) for information on enabling Python support for your libraries.

## Design Creation and Modification Using Python[](#design-creation-and-modification-using-python "Link to this heading")

To facilitate design creation and modification using Python, ADS provides a couple of features within the application to help you get started.

The **Python Exporter** is a tool that allows you to export your workspace objects (including, but not limited to: libraries, substrates, cells, and designs) to Python scripts.
You can use this tool to generate the Python code necessary to recreate your designs, providing you with the code needed to create designs programmatically.
These scripts may be studied and modified as needed to suit your requirements.

See [Export Workspace and Design Objects to Python](../howto/exporter.md#python-exporter) for more information on using the **Python Exporter**.

In addition to design creation, ADS provides a feature to record your actions in the ADS Design Environment as Python code.

See [Record Actions in ADS as Python Code](../howto/recorder.md#python-recorder) for more information on using the **Python Recorder**.

Note

If you find yourself asking, “How do I do X in Python?”, consider using the **Python Exporter** and/or the **Python Recorder** to help you get started.


---

<!-- === 来源: pydocs/py/_generated/deprecations.md === -->

# Deprecated APIs[](#deprecated-apis "Link to this heading")

The following API’s are deprecated and scheduled for removal in a future release. A deprecated API will be removed in a major release and is given an entire release cycle’s notice before removal. For example, an API initially marked as deprecated in ADS 2025 Update 1 or ADS 2026 will be scheduled for removal in ADS 2027. Removal primarily occurs only in major releases and not in update or patch releases.

## Deprecated APIs to be removed in ADS 2027[](#deprecated-apis-to-be-removed-in-ads-2027 "Link to this heading")

| API | Message |
| --- | --- |
| `keysight.ads.de._list_like._IndexedMutableCollection._append_sequence()` | Use extend(values). |
| `keysight.ads.de._list_like._IndexedMutableCollection._extend_single()` | Use extend([value]). |
| `keysight.ads.de._list_like._IndexedMutableCollection._insert_sequence()` | Use a loop and insert(value) or assign to a slice. |
| [`keysight.ads.de.app.window.main_pyside2_widget()`](../../../pypde/docs/reference/de/app/_autosummary/keysight.ads.de.app.window.main_pyside2_widget.md#keysight.ads.de.app.window.main_pyside2_widget "keysight.ads.de.app.window.main_pyside2_widget") | Use main\_pyside\_widget instead. |
| `keysight.ads.de.db._genpolyline.GenPolyline.teardrop_info()` | Use teardrops or teardrop\_touches. |
| `keysight.ads.de.db._genpolyline.GenPolyline.teardrop_info()` | Use teardrops or teardrop\_touches. |
| `keysight.ads.de.db._parameters.Param.evaluate_no_expr()` | Use evaluate\_without\_expr instead. |
| `keysight.ads.de.db._parameters.ParamBase.evaluate_no_expr()` | Use evaluate\_without\_expr instead. |
| `keysight.ads.de.db._parameters.ParamCompound.evaluate_no_expr()` | Use evaluate\_without\_expr instead. |
| `keysight.ads.de.db._parameters.ParamItem.form_name()` | Replace the ParamItem instead. |
| `keysight.ads.de.db._parameters.ParamNonRepeated.evaluate_no_expr()` | Use evaluate\_without\_expr instead. |
| `keysight.ads.de.db._parameters.ParamRepeated.append_repeat()` | Use: repeat = repeats.clone(value); repeat.value = value. |
| `keysight.ads.de.db._parameters.ParamRepeated.evaluate_no_expr()` | Use evaluate\_without\_expr instead. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.__init__()` | Use GenPolyline.teardrops or GenPolyline.teardrop\_touches. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.definition()` | Use GenPolyline.teardrops. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.has_teardrops()` | Use GenPolyline.teardrop\_touches. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.set_definition()` | Use GenPolyline.teardrops. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.set_touching()` | Use GenPolyline.teardrop\_touches. |
| `keysight.ads.de.db._teardrop.TeardropLineInfo.touch()` | Use GenPolyline.teardrop\_touches. |
| `keysight.ads.de.db_dbu._db_x.InstPin.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_dbu._db_x.InstTerm.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_dbu._db_x.Pin.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_dbu._line_type_info.LineTypeInfo.teardrop_definition_back()` | Use teardrop\_back |
| `keysight.ads.de.db_dbu._line_type_info.LineTypeInfo.teardrop_definition_back()` | Use teardrop\_back |
| `keysight.ads.de.db_dbu._line_type_info.LineTypeInfo.teardrop_definition_front()` | Use teardrop\_front |
| `keysight.ads.de.db_dbu._line_type_info.LineTypeInfo.teardrop_definition_front()` | Use teardrop\_front |
| `keysight.ads.de.db_uu._db_x.InstPin.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_uu._db_x.InstTerm.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_uu._db_x.Pin.find_first_wire_label()` | Use net\_label instead. |
| `keysight.ads.de.db_uu._line_type_info.LineTypeInfo.teardrop_definition_back()` | Use teardrop\_back |
| `keysight.ads.de.db_uu._line_type_info.LineTypeInfo.teardrop_definition_back()` | Use teardrop\_back |
| `keysight.ads.de.db_uu._line_type_info.LineTypeInfo.teardrop_definition_front()` | Use teardrop\_front |
| `keysight.ads.de.db_uu._line_type_info.LineTypeInfo.teardrop_definition_front()` | Use teardrop\_front |
| `keysight.ads.de.experimental.preferences._Design_get_preference()` | Use the preferences property instead. |
| `keysight.ads.de.experimental.preferences._Design_set_preference()` | Use the preferences property instead. |
| `keysight.ads.de.experimental.preferences._Library_get_layout_preference()` | Use the layout\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Library_get_schematic_preference()` | Use the schematic\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Library_set_layout_preference()` | Use the layout\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Library_set_schematic_preference()` | Use the schematic\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Workspace_get_layout_preference()` | Use the layout\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Workspace_get_schematic_preference()` | Use the schematic\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Workspace_set_layout_preference()` | Use the layout\_preferences property instead. |
| `keysight.ads.de.experimental.preferences._Workspace_set_schematic_preference()` | Use the schematic\_preferences property instead. |
| [`keysight.ads.de.tech._tech.LineBeginEndTypes`](../../../pypde/docs/reference/de/tech/_autosummary/keysight.ads.de.tech.LineBeginEndTypes.md#keysight.ads.de.tech.LineBeginEndTypes "keysight.ads.de.tech._tech.LineBeginEndTypes") | Use LineEndType |
| [`keysight.ads.de.tech._tech.LineCornerTypes`](../../../pypde/docs/reference/de/tech/_autosummary/keysight.ads.de.tech.LineCornerTypes.md#keysight.ads.de.tech.LineCornerTypes "keysight.ads.de.tech._tech.LineCornerTypes") | Use LineCornerType |
| [`keysight.ads.de.tech._tech.LineStripSpacingTypes`](../../../pypde/docs/reference/de/tech/_autosummary/keysight.ads.de.tech.LineStripSpacingTypes.md#keysight.ads.de.tech.LineStripSpacingTypes "keysight.ads.de.tech._tech.LineStripSpacingTypes") | Use LineStripSpacingType |

## Deprecated APIs to be removed in ADS 2028[](#deprecated-apis-to-be-removed-in-ads-2028 "Link to this heading")

| API | Message |
| --- | --- |
| `keysight.ads.de.db._layer_id.LayerId.create_layer_id_from_library()` | Use ‘from\_name’ instead. |
| `keysight.ads.de.db._layer_id.LayerId.create_layer_id_from_library_name()` | Use ‘from\_name’ instead. |
| `keysight.ads.de.db_dbu._db_x.ApolloObject.is_part_of_composite_object()` | Use is\_child\_of\_composite\_object. |
| `keysight.ads.de.db_dbu._design.PCellInfo.function()` | Use ael\_function or python\_function. |
| `keysight.ads.de.db_dbu._design.PCellInfo.function()` | Use ael\_function or python\_function. |
| `keysight.ads.de.db_uu._db_x.ApolloObject.is_part_of_composite_object()` | Use is\_child\_of\_composite\_object. |
| `keysight.ads.de.db_uu._design.PCellInfo.function()` | Use ael\_function or python\_function. |
| `keysight.ads.de.db_uu._design.PCellInfo.function()` | Use ael\_function or python\_function. |


---

