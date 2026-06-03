<!-- 来源: Examples\ex_high_pass_filter_sub_circuit.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example high pass filter sub circuit

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_high_pass_filter_sub_circuit.rst.txt)

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
  + Example high pass filter sub circuit
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
  + [Example sipro ploteye plotly](ex_sipro_ploteye_plotly.md)
  + [Example sweep inductor values](ex_sweep_inductor_values.md)
  + [Example systemvue basic](ex_systemvue_basic.md)
  + [Example voltage divider](ex_voltage_divider.md)
  + [Example vsa meas demo](ex_vsa_meas_demo.md)
* [Release Notes](../release_notes/index.md)

# Example high pass filter sub circuit[](#example-high-pass-filter-sub-circuit "Link to this heading")

This example demonstrates how to design and analyze high pass filter sub circuits.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
import math
import os

from keysight.edatoolbox import ads, circuit, dataset
from keysight.edatoolbox.util import safe_makedirs

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

    target_output_dir = args.output_dir
    safe_makedirs(target_output_dir)
    print(f"Target output dir: {target_output_dir}")

    # create a sub circuit definition of a trivial low pass filter
    high_pass_filter_def = circuit.Definition(name="Filter", pins="p n")
    R1 = high_pass_filter_def.add(circuit.R(name="R1", R="1 kOhm", p=None, n=None))
    C1 = high_pass_filter_def.add(circuit.C(name="C1", C="1 uF", p=None, n=None))
    high_pass_filter_def.connect(high_pass_filter_def.p, R1.p)
    high_pass_filter_def.connect(R1.n, C1.p)
    high_pass_filter_def.connect(C1.n, high_pass_filter_def.n)

    # create a test bench where the low pass filter will be used
    test_bench = circuit.Circuit()
    # ensure the definition of the low pass filter is available
    # before creating instances of it
    test_bench.add(high_pass_filter_def)
    HP1 = test_bench.add(circuit.Instantiation("Filter", name="HP1"))
    V = test_bench.add(
        circuit.V_Source(
            name="V",
            Freq="freq",
            Vdc="1.0 V",
            Vac="polar(1,0) V",
            Type='"V_AC"',
            SaveCurrent=1,
            p=None,
            n=None,
        )
    )
    test_bench.connect(V.n, test_bench.GND)
    test_bench.connect(V.p, HP1.n)
    test_bench.connect(HP1.p, test_bench.GND)

    ac_analysis = circuit.AC_Analysis(name="AC1")
    ac_analysis.sweep_plan.append(circuit.sweeps.LogarithmicSweep(1, 1e6, 5))
    test_bench.analyses.append(ac_analysis)
    test_bench.output_dataset = "test_bench"

    print("Running circuit simulation")
    circuit_sim = ads.CircuitSimulator()
    circuit_sim.run_netlist(test_bench.generate_netlist(), output_dir=target_output_dir)
    output_data = dataset.Dataset(os.path.join(target_output_dir, "test_bench.ds"))
    print("Response at HP1", output_data.values("AC1.AC", f"HP1.{HP1.n}"))

    try:
        import matplotlib.pyplot as plt

        response = [
            20.0 * math.log10(abs(x))
            for x in output_data.values("AC1.AC", f"HP1.{HP1.n}")
        ]
        plt.plot(response)
        plt.show(block=False)
        plt.pause(3)
        plt.close()
    except ImportError:
        pass
```

On this page

[Previous

Example empro extract resonance](ex_empro_extract_resonance.md)
[Next

Example import brd](ex_import_brd.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top