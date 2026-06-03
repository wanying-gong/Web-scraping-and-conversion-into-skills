<!-- 来源: pypde\docs\examples\ex_create_sim_and_plot.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* [Examples](index.md)
* Create, Simulate, and Plot

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
    - Create, Simulate, and Plot
    - [Interoperable Component Parameters](ex_cdf.md)
    - [Component Parameters](ex_parameters.md)
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

On this page

[Previous

Create Workspace](ex_workspace.md)
[Next

Interoperable Component Parameters](ex_cdf.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top