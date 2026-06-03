<!-- 来源: pypde\docs\examples\design_creation\ex_create_sim_and_plot.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Examples](../../../../examples.md)
* [Design Environment](../index.md)
* [Design Creation](index.md)
* Create, Simulate, and Plot

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

* [Introduction](../../../../pydocs/intro/index.md)
* [How-To](../../../../pydocs/howto/index.md)
  + [Use Python in the ADS Application](../../../../pydocs/howto/embedded.md)
  + [Set Up a Python Virtual Environment](../../../../pydocs/howto/venv.md)
  + [Set Up Visual Studio Code for Development](../../../../pydocs/howto/vscode.md)
  + [Use Pytest](../../../../pydocs/howto/pytest.md)
  + [Enable Python Support For Your Library](../../../../pydocs/howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../../../../pydocs/howto/execution.md)
  + [Export Workspace and Design Objects to Python](../../../../pydocs/howto/exporter.md)
  + [Record Actions in ADS as Python Code](../../../../pydocs/howto/recorder.md)
  + [Develop a Python Pcell in ADS](../../../../pydocs/howto/pcell.md)
* [ADS Concepts](../../../../pydocs/concepts/index.md)
  + [Workspace Elements](../../../../pydocs/concepts/workspace_elements.md)
  + [Connectivity Objects](../../../../pydocs/concepts/connectivity.md)
* [Reference](../../../../reference.md)
  + [Deprecated APIs](../../../../pydocs/py/_generated/deprecations.md)
  + [Design Environment](../../reference/index.md)
    - [keysight.ads.de](../../reference/de/index.md)
      * [ADS Application Environment](../../reference/de/ads_environment.md)
      * [ADS Workspace Components](../../reference/de/workspace_components.md)
      * [Design Hierarchy](../../reference/de/design_hierarchy.md)
      * [Smart Package](../../reference/de/package.md)
      * [Geometry](../../reference/de/geometry.md)
      * [Collections](../../reference/de/collections.md)
      * [Printer](../../reference/de/printer.md)
    - [keysight.ads.de.ael](../../reference/de/ael.md)
    - [keysight.ads.de.app](../../reference/de/app/index.md)
      * [Application](../../reference/de/app/application.md)
      * [Actions and Menus](../../reference/de/app/action.md)
      * [Addons](../../reference/de/app/addon.md)
      * [Window and Design Callbacks](../../reference/de/app/callbacks.md)
      * [Windows and Widgets](../../reference/de/app/window.md)
      * [Experimental](../../reference/de/app/experimental.md)
    - [keysight.ads.de.app.dds](../../reference/de/app/dds.md)
      * [exec\_python](../../reference/de/app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../reference/de/db/index.md)
      * [Models, Parameters, and Forms](../../reference/de/db/parameters.md)
      * [Properties](../../reference/de/db/properties.md)
      * [Preferences](../../reference/de/db/preferences.md)
      * [Transaction](../../reference/de/db/transaction.md)
      * [Smart Mount](../../reference/de/db/smart_mount.md)
      * [Geometry](../../reference/de/db/geometry.md)
      * [Teardrops](../../reference/de/db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../reference/de/db_dbu/index.md)
      * [DbBox](../../reference/de/db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../reference/de/db_uu/index.md)
      * [Database Objects](../../reference/de/db_uu/database_objects.md)
      * [Iterators](../../reference/de/db_uu/iterators.md)
      * [Designs](../../reference/de/db_uu/design.md)
      * [Teardrops](../../reference/de/db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../../reference/de/experimental/index.md)
      * [CDF](../../reference/de/experimental/cdf.md)
      * [Design Commands](../../reference/de/experimental/commands.md)
      * [Component Handles](../../reference/de/experimental/handles.md)
      * [Netlist Utilities](../../reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../reference/de/experimental/polygon_utils.md)
      * [xxPro View](../../reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../reference/de/experimental/symbol.md)
      * [Text Maker](../../reference/de/experimental/text_maker.md)
      * [Notebook](../../reference/de/experimental/notebook.md)
      * [Layer/Purpose Pairs](../../reference/de/experimental/lpp.md)
    - [keysight.ads.de.tech](../../reference/de/tech/index.md)
      * [Technology](../../reference/de/tech/tech.md)
      * [Layers](../../reference/de/tech/layers.md)
      * [Line Items](../../reference/de/tech/line_items.md)
      * [Padstacks](../../reference/de/tech/pads.md)
      * [Rules](../../reference/de/tech/rule.md)
  + [Substrate](../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../../../examples.md)
  + [Design Environment](../index.md)
    - [Workspace Creation](../workspace/ex_workspace.md)
    - [Design Creation](index.md)
      * [Create Layout](ex_create_layout.md)
      * [Create Schematic](ex_create_schematic.md)
      * Create, Simulate, and Plot
    - [Design Elements](../design_elements/index.md)
      * [Placing Text](../design_elements/ex_place_text.md)
      * [Moving Objects](../design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../design_elements/ex_plane_editing.md)
    - [Parameters](../parameters/index.md)
      * [Interoperable Component Parameters](../parameters/ex_cdf.md)
      * [Working with VAR](../parameters/ex_working_with_var.md)
      * [Component Parameters](../parameters/ex_parameters.md)
      * [Creating an Item Definition](../parameters/ex_itemdef.md)
      * [Model Definition Properties](../parameters/ex_model.md)
      * [Creating a Text Form](../parameters/ex_text_form.md)
      * [Properties](../parameters/ex_properties.md)
    - [Technology](../technology/index.md)
      * [Padstacks and Vias](../technology/ex_padstack.md)
      * [Nested Technology](../technology/ex_nested.md)
      * [Rules](../technology/ex_rules.md)
    - [Translators](../translators/index.md)
      * [DXF Import and Export](../translators/ex_translate_dxf.md)
      * [Gerber Export](../translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../translators/ex_translate_gds.md)
    - [UI](../ui/index.md)
      * [Creating Custom Menus Using an Addon](../ui/ex_menu_addon.md)
      * [PySide](../ui/ex_pyside.md)
    - [Utility](../utility/index.md)
      * [Calling Between AEL and Python](../utility/ex_calling_ael_and_python.md)
      * [Smart Package](../utility/ex_smart_pkg.md)
      * [XML RPC](../utility/ex_xml_rpc.md)
  + [Substrate](../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../../../genindex.md)

# Create, Simulate, and Plot[](#create-simulate-and-plot "Link to this heading")

This example will create a new workspace in your HOME directory called “create\_simulate\_plot\_example”. In the workspace a new library and schematic are created and populate with an RC filter. Next, the circuit will be simulated and finally the response from the filter will be plotted inline in the ADS Python console.

[![../../../../_images/low_pass_filter_var.png](../../../../_images/low_pass_filter_var.png)](../../../../_images/low_pass_filter_var.png)

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

On this page

[Previous

Create Schematic](ex_create_schematic.md)
[Next

Design Elements](../design_elements/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top