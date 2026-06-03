<!-- 来源: Examples\ex_run_hb_simulation.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example run hb simulation

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_run_hb_simulation.rst.txt)

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
  + Example run hb simulation
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

# Example run hb simulation[](#example-run-hb-simulation "Link to this heading")

This example demonstrates how to run a Harmonic Balance simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

import os
from argparse import ArgumentParser
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from keysight.edatoolbox import ads, circuit, util
import keysight.pwdatatools as pwdt

# small helper class, used to control how the netlist is parsed
# in our case
class Bunch(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--output-dir',action="store", required=True, default=None, help='Location where the output will be created')
    args = parser.parse_args()

    target_workspace_dir = args.output_dir
    util.safe_makedirs(target_workspace_dir)
    input_workspace_file = os.path.abspath('data/Keysight_mmWave_wrk.7zads')
    target_workspace = os.path.join(target_workspace_dir, "Keysight_mmWave_wrk")

    print("Unarchiving workspace")
    # Putting the environment variable PYTHON_EDA_TOOLBOX_ADS_VISUAL to 1
    # allows to observe how the toolbox drives ADS. It is also a fallback when
    # the non-visual mode fails.
    os.environ["PYTHON_EDA_TOOLBOX_ADS_VISUAL"]="1"
    ads_application = ads.ADS()
    ads_circuitsim = ads.CircuitSimulator()
    ads_application.unarchive_workspace(input_workspace_file, target_workspace_dir)

    # The PathWave Data Tools require to have the HPEESOF_DIR to be setup
    os.environ["HPEESOF_DIR"] = os.environ.get("HPEESOF_DIR") or ads.get_ads_location()

    # -------- Helper functions --------
    def todBm(val):
        np.seterr(divide = 'ignore')
        logVal=np.abs(val.to_numpy())
        dBmval = 30+10*np.log10(logVal)
        np.nan_to_num(dBmval,nan=-100)
        return dBmval

    def computeIP1(x,y,compLevel=-1, resolution=0.01):
        from scipy import interpolate
        xi, yi=x.to_numpy(), y.to_numpy()
        # Normalize vs small signal gain
        yi -= yi[0]
        f=interpolate.interp1d(xi,yi)
        xnew=np.arange(np.amin(xi),np.amax(xi),resolution)
        ynew=f(xnew)
        idx=(np.abs(ynew-(compLevel))).argmin()
        return xnew[idx]

    # -------- Main  --------
    # ensure the circuit simulation can use the demo PDK
    data_dir = os.path.abspath(os.path.join(target_workspace, r"PDK\mmw_demo_ipdk\ads\data"))

    # Generate netlist or use the cached version on disk
    netlist = ads_application.generate_netlist(
            target_workspace, ads.LibraryCellView(
                    library="mmWave_PA_lib",
                    cell="PA_TopLevel_TestBench",
                    view="schematic_ads") )

    topCircuit=circuit.Circuit()
    topCircuit.import_netlist(netlist, Bunch(extract_analyses=False))

    # Let's run a sweep of the bias voltage
    Vd=np.arange(8,13,1)        # from 8 to 13 (not included) step by 1

    df=None
    for biasVoltage in Vd:
        curOutDir = os.path.join(target_workspace_dir,f"output/data/PA_Vd{biasVoltage}")
        util.safe_makedirs(curOutDir)

        # Update the value in the netlist
        print(f'Update existing value of Vd={topCircuit.Vd.value} to {biasVoltage} V and run simulation')
        topCircuit.Vd.value = biasVoltage

        # Run the netlist with the modified value
        ads_circuitsim.run_netlist( topCircuit.generate_netlist(),
            output_dir=curOutDir,
            rel_data_dir=data_dir)
        print(f"Simulation for Vd={biasVoltage} completed")

        # Extract the results with PW data tools
        dataStore = pwdt.read_file(os.path.join(curOutDir, "PA_TopLevel_TestBench.ds"))
        curOutput = dataStore.members[1].data

        # Massage the data to compute the output dBm value and the dependency
        curOutput['out_dBm']=todBm(curOutput['out'])
        curOutput['in_dBm']=todBm(curOutput['in'])
        curOutput['Vd']=biasVoltage
        curOutput['Gain_dB']=curOutput['out_dBm']-curOutput['in_dBm']
        curOutput['freqEng']=curOutput['freq']/1e9
        # Extracting IP1 at 28G
        opFreq=2.8e10
        Pin_28G=curOutput['Pin'].loc[curOutput['freq'] == opFreq]
        Gain_28G=curOutput['Gain_dB'].loc[curOutput['freq'] == opFreq]
        curOutput['IIP1_dBm']=computeIP1(Pin_28G,Gain_28G)

        # Concatenate the dataframes
        df=pd.concat([df,curOutput], ignore_index=True, sort=True)

    # -------- Plot  --------
    # Only selects the fundamental
    outFund=df.loc[df['freq']==opFreq]

    # Only selects one power
    outSpectrum=df.loc[df['Pin']==0]

    # Actual plot is a 2x2 grid
    fig, ax = plt.subplots(2, 2)

    # Pout vs Pin
    g1=sns.lineplot(x="Pin", y="out_dBm", hue="Vd", data=outFund, palette='Set1', ax=ax[0,0])
    g1.set(xlabel='Pin (dBm)',ylabel="Output Power at 28G (dBm)",title='Output Power at 28G vs input power and bias')

    # Gain vs Pin
    g2=sns.lineplot(x="Pin", y="Gain_dB", hue="Vd", data=outFund, palette='Set1', ax=ax[0,1])
    g2.set(xlabel='Pin (dBm)',ylabel="Gain (dB)",title='Power Gain at 28G vs input power and bias')

    # 1dB compression point vs Vd
    g3=sns.lineplot(x="Vd", y="IIP1_dBm", data=outFund, palette='Set1', ax=ax[1,0])
    g3.set(xlabel='Bias voltage (V)',ylabel="IIP1 (dBm)",title='1 dB compression point at 28G vs bias')

    # Plot a spectrum using a barplot
    g4=sns.barplot(x="freqEng", y="out_dBm", hue='Vd', data=outSpectrum, palette='Set1', ax=ax[1,1])
    g4.set(xlabel='Frequency (GHz)',ylabel="Pout (dBm)",title='Output Spectrum at Pin=0 vs bias')

    fig.suptitle('mmWave PA FOM')
    plt.show(block=False)
    plt.pause(3)
    plt.close()
```

On this page

[Previous

Example rfpro stop nets](ex_rfpro_stop_nets.md)
[Next

Example run netlist](ex_run_netlist.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top