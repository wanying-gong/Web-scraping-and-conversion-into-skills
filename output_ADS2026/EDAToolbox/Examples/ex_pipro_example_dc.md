<!-- 来源: Examples\ex_pipro_example_dc.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example pipro dc

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_pipro_example_dc.rst.txt)

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
  + Example pipro dc
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
  + [Example sipro ploteye plotly](ex_sipro_ploteye_plotly.md)
  + [Example sweep inductor values](ex_sweep_inductor_values.md)
  + [Example systemvue basic](ex_systemvue_basic.md)
  + [Example voltage divider](ex_voltage_divider.md)
  + [Example vsa meas demo](ex_vsa_meas_demo.md)
* [Release Notes](../release_notes/index.md)

# Example pipro dc[](#example-pipro-dc "Link to this heading")

This example demonstrates how load an SIPro view and setup and run an PIPro DC simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
import os
import re
from keysight.edatoolbox import ads, util, xxpro

try:
    import empro
    import empro.toolkit
    import empro.toolkit.analysis
    from empro.toolkit.analysis.dc import output
    from empro.toolkit.analysis.dc.results import DCResult
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
    args = parser.parse_args()

    target_workspace_dir = args.output_dir
    util.safe_makedirs(target_workspace_dir)
    input_workspace_file = os.path.abspath("data/SIPro_PIPro_DDR4_wrk.7zads")
    target_workspace = os.path.join(target_workspace_dir, "SIPro_PIPro_DDR4_wrk")

    assert target_workspace_dir != None
    assert input_workspace_file != None
    assert os.path.exists(target_workspace_dir)
    assert os.path.exists(input_workspace_file)
    assert not os.path.exists(
        target_workspace
    ), f"Target workspace {target_workspace} already exists!"

    print(f"Input workspace file: {input_workspace_file}")
    print(f"Target output dir: {target_workspace_dir}")

    ads_application = ads.ADS()
    print("ADS application created")

    print("Unarchiving workspace")
    ads_application.unarchive_workspace(input_workspace_file, target_workspace_dir)

    print("Creating xxPro simulation view")
    input_lcv = ads.LibraryCellView(
        library="PC4-RDIMM_V090_RC_F0_20131106_lib",
        cell="PC4-RDIMM_V090_RC_F0_20131106",
        view="layout",
    )
    pro_lcv = ads.LibraryCellView(
        library="PC4-RDIMM_V090_RC_F0_20131106_lib",
        cell="PC4-RDIMM_V090_RC_F0_20131106",
        view="sipro",
    )
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate="PC4-RDIMM_V090_RC_F0_20131106",
        pro_lcv=pro_lcv,
        tool="sipi",
    )

    print("xxPro simulation view created")

    with util.remember_cwd():
        os.environ[
            "HPEESOF_DIR"
        ] = (
            ads.get_ads_location()
        )  # ensure the referenced env vars in lib.defs can be found
        xxpro.use_workspace(target_workspace)

        # at this stage the view is still completely empty
        # we still need to load the requested layouts in it
        xxpro.load_pro_view(pro_lcv)
        empro.activeProject.saveActiveProject()

        with empro.activeProject:
            # create an analysis
            analysis = empro.analysis.Analysis(
                empro.analysis.Analysis.DCAnalysisType, "Test"
            )
            ground_nets = ["GND"]
            power_nets = ["VDD"]
            vrm_definitions = [("J1", "1.2 V")]
            sink_definitions = [(f"U{index}", "0.1 A") for index in range(1, 20)]

            net_list = analysis.nets
            for net_name in ground_nets + power_nets:
                net_list.append(empro.activeProject.layout.nets[net_name])

            vrm_list = analysis.vrms
            for vrm_name, vrm_voltage in vrm_definitions:
                instance = empro.activeProject.layout.instances[vrm_name]
                plus_pins = [
                    pin for pin in instance.pins() if pin.netName in power_nets
                ]
                minus_pins = [
                    pin for pin in instance.pins() if pin.netName in ground_nets
                ]
                vrm = empro.analysis.Vrm(plus_pins, minus_pins, vrm_name)
                vrm.voltage = vrm_voltage
                vrm.sourceType = "PackagedVrm"
                vrm_list.append(vrm)

            sink_list = analysis.sinks
            for sink_name, sink_current in sink_definitions:
                instance = empro.activeProject.layout.instances[sink_name]
                plus_pins = [
                    pin for pin in instance.pins() if pin.netName in power_nets
                ]
                minus_pins = [
                    pin for pin in instance.pins() if pin.netName in ground_nets
                ]
                sink = empro.analysis.Sink(plus_pins, minus_pins, sink_name)
                sink.current = sink_current
                sink_list.append(sink)

            empro.activeProject.analyses.append(analysis)

        print("Running and waiting for simulation...")
        active_analysis = empro.activeProject.analyses[-1]
        empro.toolkit.analysis.runAnalysis(
            active_analysis, waitForConfirmation=False, saveProject=True
        )
        empro.activeProject.simulations.isQueueHeld = False
        active_simulation = empro.activeProject.simulations[-1]
        empro.toolkit.simulation.wait(active_simulation)
        empro.activeProject.saveActiveProject()

        print("Simulation complete, IR drop per sink:")
        dc_result = DCResult(active_analysis)

        for sink in dc_result.sinks:
            irDrop = sink.vrmOutputVoltage - sink.inputVoltage
            print(f"{sink.name}: {irDrop*1000:2.2f} mV")

        ads_path = ads.get_ads_location()
        ads_ver = -1
        if re.search(r"\d{4}", ads_path):
            ads_ver = int(re.search(r"\d{4}", ads_path).group())

        if(ads_ver >= 2024):
            print("DC report generation in progress...")
            # HTML Report
            output.exportDCResultstoHtml(
                dc_result,
                directory=target_workspace,
                report_name="DCReport",
                open_report=True,
            )
            # Docx Report
            output.exportDCResultstoDocx(
                dc_result,
                directory=target_workspace,
                report_name="DCReport",
                open_report=True,
            )
            print("DC report generated")
```

On this page

[Previous

Example pipro ac](ex_pipro_example_ac.md)
[Next

Example quantumpro one qubit epr](ex_quantumpro_one_qubit_epr.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top