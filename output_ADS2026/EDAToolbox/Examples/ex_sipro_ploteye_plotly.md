<!-- 来源: Examples\ex_sipro_ploteye_plotly.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example sipro ploteye plotly

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_sipro_ploteye_plotly.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* [Initial Setup](../Initial_Setup/index.md)
  + [Installation](../Initial_Setup/installation.md)
  + [Prerequisites](../Initial_Setup/prerequisites.md)
  + [Verifying Installation](../Initial_Setup/verifying.md)
  + [SSH](../Initial_Setup/ssh.md)
* [How-To](../How-To/index.md)
  + [Create a Circuit](../How-To/circuit.md)
  + [Run a Circuit Simulation](../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../How-To/sipro.md)
* [API Reference](../API_Reference/index.md)
  + [ADS](../API_Reference/ads/index.md)
    - [Functions](../API_Reference/ads/functions/index.md)
    - [Classes](../API_Reference/ads/classes/index.md)
      * [ADS](../API_Reference/ads/classes/ads.md)
      * [CircuitSimulator](../API_Reference/ads/classes/circuit_simulator.md)
  + [Circuit API](../API_Reference/circuit/index.md)
    - [Functions](../API_Reference/circuit/functions/index.md)
    - [Classes](../API_Reference/circuit/classes/index.md)
      * [Circuit](../API_Reference/circuit/classes/circuit.md)
      * [Definition](../API_Reference/circuit/classes/definition.md)
      * [Instance](../API_Reference/circuit/classes/instance.md)
      * [Node](../API_Reference/circuit/classes/node.md)
      * [OptimizationRange](../API_Reference/circuit/classes/optimization_range.md)
      * [TuningRange](../API_Reference/circuit/classes/tuning_range.md)
      * [Value](../API_Reference/circuit/classes/value.md)
  + [Dataset](../API_Reference/dataset/index.md)
  + [External API](../API_Reference/extra/index.md)
    - [empro.analysis](../API_Reference/extra/empro/index.md)
  + [Multi Python API](../API_Reference/multi_python/index.md)
    - [Functions](../API_Reference/multi_python/functions/index.md)
  + [xxPro](../API_Reference/xxpro/index.md)
* [Examples](index.md)
  + [Running EDA Toolbox Examples](Running%20Examples.md)
  + [Example baluns](ex_baluns.md)
  + [Example co optimize matching network](ex_co_optimize_matching_network.md)
  + [Example create 3d empro serpentines](ex_create_3d_empro_serpentines.md)
  + [Example dump workspace netlists](ex_dump_workspace_netlists.md)
  + [Example empro extract resonance](ex_empro_extract_resonance.md)
  + [Example high pass filter sub circuit](ex_high_pass_filter_sub_circuit.md)
  + [Example import brd](ex_import_brd.md)
  + [Example import ipc2581](ex_import_ipc2581.md)
  + [Example import odb](ex_import_odb.md)
  + [Example low pass filter](ex_low_pass_filter.md)
  + [Example multi python](ex_multi_python.md)
  + [Example odbpp simulate pipro ac reuse sio](ex_odbpp_simulate_pipro_ac_reuse_sio.md)
  + [Example odbpp simulate pipro dc](ex_odbpp_simulate_pipro_dc.md)
  + [Example odbpp simulate rfpro](ex_odbpp_simulate_rfpro.md)
  + [Example optimize matching network](ex_optimize_matching_network.md)
  + [Example pipro ac](ex_pipro_example_ac.md)
  + [Example pipro dc](ex_pipro_example_dc.md)
  + [Example quantumpro one qubit epr](ex_quantumpro_one_qubit_epr.md)
  + [Example quantumpro one qubit freq](ex_quantumpro_one_qubit_freq.md)
  + [Example rfpro stop nets](ex_rfpro_stop_nets.md)
  + [Example run hb simulation](ex_run_hb_simulation.md)
  + [Example run netlist](ex_run_netlist.md)
  + [Example run netlist from disk](ex_run_netlist_from_disk.md)
  + [Example run schematic](ex_run_schematic.md)
  + [Example sipro automation](ex_sipro_automation.md)
  + [Example sipro channelsim flow](ex_sipro_channelsim_flow.md)
  + [Example sipro SI](ex_sipro_example_si.md)
  + [Example sipro extract tdr](ex_sipro_extract_tdr.md)
  + [Example sipro eye diagram](ex_sipro_eye_diagram.md)
  + Example sipro ploteye plotly
  + [Example sweep inductor values](ex_sweep_inductor_values.md)
  + [Example systemvue basic](ex_systemvue_basic.md)
  + [Example voltage divider](ex_voltage_divider.md)
  + [Example vsa meas demo](ex_vsa_meas_demo.md)
* [Release Notes](../release_notes/index.md)

# Example sipro ploteye plotly[](#example-sipro-ploteye-plotly "Link to this heading")

This example demonstrates how to run an SI simulation and extract the Eye diagram and plot it using Plotly.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#
from argparse import ArgumentParser
from dataclasses import dataclass
import os

import keysight.pwdatatools as pwdt
import plotly.express as px

from keysight.edatoolbox import ads, circuit, momentum, util, xxpro

@dataclass
class CircuitImportOptions:
    extract_analyses: bool

try:
    import empro
    import empro.toolkit
    import empro.toolkit.analysis
except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using the Python from EMPro.  Use it by launching emproenv.bat/.sh"
    )
    raise

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--output-dir",
        action="store",
        required=True,
        default=None,
        help="Location where the output will be created",
    )
    parser.add_argument(
        "--ploteye",
        action="store",
        required=False,
        default="True",
        help="Set to True to view eye diagram plot , otherwise set False , defaulted to True",
    )
    args = parser.parse_args()

    target_workspace_dir = args.output_dir
    util.safe_makedirs(target_workspace_dir)
    input_workspace_file = os.path.abspath("data/DQLines_wrk.7zads")
    target_workspace = os.path.join(target_workspace_dir, "DQLines_wrk")

    assert target_workspace_dir is not None
    assert input_workspace_file is not None
    assert os.path.exists(target_workspace_dir)
    assert os.path.exists(input_workspace_file)
    assert not os.path.exists(
        target_workspace
    ), f"Target workspace {target_workspace} already exists!"

    print(f"Input workspace file: {input_workspace_file}")
    print(f"Target output dir: {target_workspace_dir}")

    ads_application = ads.ADS()
    print("ADS application created")
    os.environ["HPEESOF_DIR"] = ads.get_ads_location()
    print("Unarchiving workspace")
    ads_application.unarchive_workspace(input_workspace_file, target_workspace_dir)

    pro_lcv = ads.LibraryCellView(library="DQLines_lib", cell="DQLines", view="sipi")

    # for SI analyses and Momentum analyses we need to pass on to xxPro the location of the Momentum binaries
    momentum_dir = momentum.get_momentum_location()
    empro.toolkit.analysis.setMomentumDir(momentum_dir)

    with util.remember_cwd():
        xxpro.use_workspace(target_workspace)
        xxpro.load_pro_view(pro_lcv)
        empro.activeProject.saveActiveProject()

        # take the latest analysis
        active_analysis = empro.activeProject.analyses[-1]

        print("Running and waiting for simulation...")
        empro.toolkit.analysis.runAnalysis(
            active_analysis, waitForConfirmation=False, saveProject=True
        )
        empro.activeProject.simulations.isQueueHeld = False
        active_simulation = empro.activeProject.simulations[-1]
        empro.toolkit.simulation.wait(active_simulation)
        empro.activeProject.saveActiveProject()

    # now also run the channel analysis, plot eye diagram with plotly library and save the eyeplot
    netlist = ads_application.generate_netlist(
        target_workspace,
        ads.LibraryCellView(
            library="DQLines_lib", cell="channel_sim", view="schematic"
        ),
    )
    ads_circuitsim = ads.CircuitSimulator()
    ckt = circuit.Circuit(
        netlist, import_options=CircuitImportOptions(extract_analyses=False)
    )
    print(f"Existing File={ckt.definitions[ckt.X1.instance_type].DQ0.File}")
    new_sio_location = os.path.join(
        active_simulation.simulationPath(), "emds_dsn", "design", "design.sio"
    )
    print(f"New File={new_sio_location}")
    ckt.definitions[ckt.X1.instance_type].DQ0.File = f'"{new_sio_location}"'
    ads_circuitsim.run_netlist(ckt.generate_netlist(), output_dir=args.output_dir)

    print("====Measurement Results====")
    filepath = os.path.join(target_workspace_dir, "channel_sim.ds")
    results = pwdt.read_file(filepath)

    eyemeassummary = results.members[2].to_pandas_dataframe()

    print(eyemeassummary.to_string(index=False))

    if not args.ploteye.lower() == "false":
        eyevoutdata = results.members[0].to_pandas_dataframe()
        config = dict({"scrollZoom": True})

        if not "index" in eyevoutdata.columns:
            # creating dummy index column for plotly to color the points.
            # TODO : Remove if once pwdatatools stops discarding the index column containing the eye diagram density values.
            eyevoutdata["index"] = eyevoutdata["Density"] / max(eyevoutdata["Density"]) * 100

        fig = px.scatter(
            eyevoutdata, y="Density", x="time", color="index", title="Eye Diagram"
        )
        fig.show(config=config)
        imagefile = os.path.join(target_workspace_dir, "eyeplot.jpeg")
        # install if write image fails : pip install kaleido==0.1.0post1
        fig.write_image(imagefile)
```

On this page

[Previous

Example sipro eye diagram](ex_sipro_eye_diagram.md)
[Next

Example sweep inductor values](ex_sweep_inductor_values.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top