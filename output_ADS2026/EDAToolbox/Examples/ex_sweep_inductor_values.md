<!-- 来源: Examples\ex_sweep_inductor_values.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example sweep inductor values

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_sweep_inductor_values.rst.txt)

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
  + [Example sipro ploteye plotly](ex_sipro_ploteye_plotly.md)
  + Example sweep inductor values
  + [Example systemvue basic](ex_systemvue_basic.md)
  + [Example voltage divider](ex_voltage_divider.md)
  + [Example vsa meas demo](ex_vsa_meas_demo.md)
* [Release Notes](../release_notes/index.md)

# Example sweep inductor values[](#example-sweep-inductor-values "Link to this heading")

This example demonstrates how to use the EDA Toolbox to sweep through a series of values from an inductor.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
import os

from keysight import edatoolbox

#
# show how to modify values of a circuit, even when those values
# are part of a definition and there is no VAR predefined
from keysight.edatoolbox import ads, circuit, dataset, units
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

    netlist = r"""; Top Design: "run_schematic_SP_lib:basic_filter_flatten:schematic"
; Netlisted using Hierarchy Policy: "Standard"

Options ResourceUsage=yes UseNutmegFormat=no EnableOptim=no TopDesignName="run_schematic_SP_lib:basic_filter_flatten:schematic" DcopOutputNodeVoltages=yes DcopOutputPinCurrents=yes DcopOutputAllSweepPoints=no DcopOutputDcopType=0
; Library Name: run_schematic_SP_lib
; Cell Name: DA_LCBandpassDT_basic_filter
; View Name: schematic
define DA_LCBandpassDT_basic_filter ( P1  P2 )
parameters  Fs1=.5 GHz  Fp1=1 GHz  Fp2=2 GHz  Fs2=2.5 GHz  Ap=3 dB  As=20 dB  N=0  ResponseType=1  MinLorC=4  Rg=50 Ohm  Rl=50 Ohm  MaxRealizations=25
L:L1  P1 0 L=6.441011 nH R=1e-12 Ohm Noise=yes
C:C1  P1 0 C=1.966329 pF
L:L2  P1 N__3 L=12.869792 nH R=1e-12 Ohm Noise=yes
C:C2  N__3 N__4 C=984.098877 fF
L:L3  N__4 0 L=1.990382 nH R=1e-12 Ohm Noise=yes
C:C3  N__4 0 C=6.363175 pF
L:L4  N__4 N__7 L=12.869792 nH R=1e-12 Ohm Noise=yes
C:C4  N__7 P2 C=984.098874 fF
L:L5  P2 0 L=6.441011 nH R=1e-12 Ohm Noise=yes
C:C5  P2 0 C=1.966329 pF
end DA_LCBandpassDT_basic_filter

DA_LCBandpassDT_basic_filter:DA_LCBandpassDT1  N__3 N__2 Fs1=0.5 GHz Fp1=1 GHz Fp2=2 GHz Fs2=2.5 GHz Ap=3 dB As=20 dB N=5 ResponseType=1 MinLorC=4 Rg=50 Ohm Rl=50 Ohm MaxRealizations=25
S_Param:SP1 CalcS=yes CalcY=no CalcZ=no GroupDelayAperture=1e-4 FreqConversion=no FreqConversionPort=1 StatusLevel=2 CalcNoise=no SortNoise=0 BandwidthForNoise=1.0 Hz DevOpPtLevel=0 \
SweepVar="freq" SweepPlan="SP1_stim" OutputPlan="SP1_Output"

SweepPlan: SP1_stim Start=0 GHz Stop=3 GHz Step=0.01 GHz

OutputPlan:SP1_Output \
    Type="Output" \
    UseEquationNestLevel=yes \
    EquationNestLevel=2 \
    UseSavedEquationNestLevel=yes \
    SavedEquationNestLevel=2

#load "python","LinearCollapse"
Component Module="LinearCollapse" Type="ModelExtractor" NetworkRepresentation=2
Port:Term2  N__2 0 Num=2 Z=50 Ohm Noise=yes
Port:Term1  N__3 0 Num=1 Z=50 Ohm Noise=yes
"""

    basic_filter = circuit.Circuit(netlist)

    # verify we can access the L2 and L4 instances within the definition "DA_LCBandpassDT_basic_filter"
    print(basic_filter.DA_LCBandpassDT_basic_filter.L2)
    print(basic_filter.DA_LCBandpassDT_basic_filter.L4)

    # extract the nominal values
    nominal_L2_value = units.eval_quantity(
        basic_filter.DA_LCBandpassDT_basic_filter.L2.L
    )
    nominal_L4_value = units.eval_quantity(
        basic_filter.DA_LCBandpassDT_basic_filter.L4.L
    )

    print(f"L2 nominal value={nominal_L2_value}")
    print(f"L4 nominal value={nominal_L4_value}")

    ads_circuitsim = ads.CircuitSimulator()
    L_factors = [1.0, 2.0]
    safe_makedirs(args.output_dir)
    for L_factor in L_factors:
        print(f"Running netlist with L_factor={L_factor}")
        basic_filter.DA_LCBandpassDT_basic_filter.L2.L = nominal_L2_value / L_factor
        basic_filter.DA_LCBandpassDT_basic_filter.L4.L = nominal_L4_value / L_factor
        ads_circuitsim.run_netlist(
            basic_filter.generate_netlist(), output_dir=args.output_dir, rel_data_dir=""
        )
        print("Simulation completed")
        print("Extracting results")
        ds = dataset.Dataset(os.path.join(args.output_dir, "basic_filter_flatten.ds"))
        freqs = ds.values("SP1.SP", "freq")
        S21 = ds.values("SP1.SP", "S[2,1]")

        fs1 = 0.5e9
        fp1 = 1.0e9
        fp2 = 2.0e9
        fs2 = 2.5e9

        S21_fs1 = S21[freqs.index(fs1)]
        S21_fp1 = S21[freqs.index(fp1)]
        S21_fp2 = S21[freqs.index(fp2)]
        S21_fs2 = S21[freqs.index(fs2)]

        print(f"S21 @ [{fs1},{fp1}]=({S21_fs1},{S21_fp1})")
        print(f"S21 @ [{fs2},{fp2}]=({S21_fs2},{S21_fp2})")
```

On this page

[Previous

Example sipro ploteye plotly](ex_sipro_ploteye_plotly.md)
[Next

Example systemvue basic](ex_systemvue_basic.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top