<!-- 来源: Examples\ex_vsa_meas_demo.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example vsa meas demo

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_vsa_meas_demo.rst.txt)

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
  + [Example sweep inductor values](ex_sweep_inductor_values.md)
  + [Example systemvue basic](ex_systemvue_basic.md)
  + [Example voltage divider](ex_voltage_divider.md)
  + Example vsa meas demo
* [Release Notes](../release_notes/index.md)

# Example vsa meas demo[](#example-vsa-meas-demo "Link to this heading")

This example demonstrates how to use the EDA Toolbox to use VSA from a Python script.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc , Keysight Confidential
#

# This example is a translation into Python of the shipping example with VSA called "Measurement Demo"
# originally written in C#

import sys
import os
import time
from keysight.edatoolbox import vsa

try:
    import clr
except ImportError:
    print('This example requires the Python.NET module called "clr".  Install it through "pip install pythonnet"')
    # depending on the version of Python there is more drama involved than expected
    # * for Python 3.8.x: it suffices to do "py -3.8 -m pip install pythonnet"
    # * for Python 3.10.x (and supposedly 3.9.x): the install of pythonnet is broken through pip.  There
    #   are multiple failure modes, some suggest to first install the module 'wheel' but that doesn't resolve
    #   it either.  The fix for the issue has not been propagated through the pip module, but a way to work around
    #   the issue is to use "py -3.10 -m pip install --pre pythonnet": see https://github.com/pythonnet/pythonnet/issues/1600
    raise

if __name__=="__main__":
    print(f"VSA found at {vsa.get_vsa_location()}")

    # make sure the CLR has path visibility for the DLLs
    # we use the edatoolbox.vsa.get_vsa_location() to find the latest installed VSA
    sys.path.append(os.path.join(vsa.get_vsa_location(), r'Interfaces'))
    clr.AddReference("Agilent.SA.Vsa.Interfaces")

    # at this point we are good to go and can import the CLR API of VSA
    import Agilent.SA.Vsa as vsa_clr

    # connect to an existing VSA session or launch a new one in case there is none
    new_session_started = False
    app = vsa_clr.ApplicationFactory.Create()       # try to connect to an existing session

    if not app:     # if that is not available, create a new session
        print(f"No existing VSA session found, starting a new session")
        app = vsa_clr.ApplicationFactory.Create(True, None, None, -1)
        new_session_started = True
        print(f"Connected to the new VSA session")
    else:
        print(f"Connected to an existing VSA session")

    app.IsVisible = True
    app.Title = "Measurement Demo"

    meas = app.Measurements.SelectedItem
    disp = app.Display

    disp.Preset()
    meas.Preset()
    meas.Reset()

    meas.Frequency.Center = 1e9
    meas.Frequency.Span = 5e6

    meas.Input.Analog.Channels[0].Range = 1.0
    disp.Traces[0].Format = vsa_clr.TraceFormatType.LinearMagnitude

    meas.IsContinuous = False
    meas.Restart()

    meas_is_done = False
    for i in range(50):
        time.sleep(0.1)
        meas_is_done = meas.Status.Value & vsa_clr.StatusBits.MeasurementDone
        if meas_is_done:
            break

    if not meas_is_done:
        print("Measurement failed to complete")

    disp.Traces[0].YScaleAuto()
    disp.Traces[1].YScaleAuto()

    yData = disp.Traces[0].DoubleData(vsa_clr.TraceDataSelect.Y, False)
    xData = disp.Traces[0].DoubleData(vsa_clr.TraceDataSelect.X, False)

    print("Showing first 10 data points of measurements")
    for i in range(min(len(xData), 10)):
        print(f"{i}: X={xData[i]}, Y={yData[i]}")

    input("Press enter to exit the demo")
    app.Title = ""

    if new_session_started:
        app.Quit()
```

On this page

[Previous

Example voltage divider](ex_voltage_divider.md)
[Next

Release Notes](../release_notes/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top