<!-- 来源: Examples\ex_co_optimize_matching_network.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example co optimize matching network

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_co_optimize_matching_network.rst.txt)

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
  + Example co optimize matching network
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
  + [Example vsa meas demo](ex_vsa_meas_demo.md)
* [Release Notes](../release_notes/index.md)

# Example co optimize matching network[](#example-co-optimize-matching-network "Link to this heading")

This example demonstrates how to use the EDA Toolbox to co-optimize between an EMPro antenna and the ADS Circuit load circuit.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2022 Keysight Technologies, Inc , Keysight Confidential

from argparse import ArgumentParser
import math
import os

import numpy as np
from scipy import optimize

# import the automation tools for Python for ADS and CircuitSimulation
from keysight.edatoolbox import ads, circuit, dataset, util

try:
    import empro
    import empro.toolkit
    import empro.toolkit.zap

    # ariane requires empro
    import ariane  # isort:skip
except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using "
        "the Python from EMPro. Use it by launching emproenv.bat/.sh"
    )
    raise

# Global counter to track output directories, convenient for debugging
optimization_iteration = 0

class Bunch(object):
    """A convenience class to organize properties of objects."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def lc_resonance(
    l_value,
    c_value,
    t_cond,
    t_subst,
    matching_network,
    workdir_path,
    workspace_path,
    iterate_output_dirs,
):
    """Estimate resonance frequency of an LC circuit.

    Parameters
    ----------
    l_value : float
        Inductance in H.
    c_value : float
        Capacitance in F.
    t_cond : float
        Conductor thickness in meters.
    t_subst : float
        Substrate thickness in meters.
    matching_network : Circuit
        A circuit schematic.
    workdir_path : str
        Directory to save simulation data.
    workspace_path : str
        Path to an ADS workspace containing the LC circuit schematic.
    iterate_output_dirs : bool
        If True dump simulation data to a new directory, otherwise overwrite
        previous data.

    Returns
    -------
    Tuple[float, float]
        A tuple containing S11 magnitude and resonance frequency.
    """
    print(
        "Optimization iteration, applying parameters: "
        f"[{l_value}, {c_value}, {t_cond}, {t_subst}]"
    )
    # set the parameters on the circuit netlist
    matching_network.L.value = f"{l_value * 1e9} nH"
    matching_network.C.value = f"{c_value * 1e12} pF"

    # set the parameters on the EMPro EM simulation
    with empro.activeProject as project:
        project.parameters.setFormula("conductor_thickness", t_cond)
        project.parameters.setFormula("substrate_thickness", t_subst)

    print("Running and waiting for EMPro-FEM simulation...")
    simulation = empro.activeProject.createSimulation(True)
    empro.activeProject.simulations.isQueueHeld = False
    empro.toolkit.simulation.wait(simulation)

    print("EMPro-FEM simulation finished...")
    sio_file_path = os.path.join(
        simulation.simulationPath(), "emds_dsn", "design", "design.sio"
    )
    sio_file_path = sio_file_path.replace("/", "\\")
    matching_network.SNP1.File = f'"{sio_file_path}"'
    print(f"S Parameter file of matching network: {matching_network.SNP1.File}")

    global optimization_iteration
    optimization_iteration += 1
    if iterate_output_dirs:
        output_dir_name = f"output_{optimization_iteration}"
    else:
        output_dir_name = "output"

    output_dir = os.path.join(workdir_path, output_dir_name)
    util.safe_makedirs(output_dir)

    print("Running and waiting for circuit simulation...")
    ads_circuitsim.run_netlist(
        matching_network.generate_netlist(),
        output_dir=output_dir,
        rel_data_dir=workspace_path,
    )
    print("Circuit simulation finished...")
    ds = dataset.Dataset(os.path.join(output_dir, "matching_s_param.ds"))
    freqs = ds.values("SP1.SP", "freq")
    s11 = [abs(x) for x in ds.values("SP1.SP", "S[1,1]")]
    mag_s11, frequency = min(zip(s11, freqs))
    print(
        f"Applying parameters: [{l_value}, {c_value}, {t_cond}, {t_subst}]"
        f" --> resonant frequency={frequency}"
    )
    return mag_s11, frequency

if __name__ == "__main__":
    # allow to incrementally generate output dirs,
    # otherwise 1 output directory is recycled
    iterate_output_dirs = True

    parser = ArgumentParser()
    parser.add_argument(
        "--output-dir",
        action="store",
        required=True,
        default=None,
        help="Location where the output will be created",
    )
    args = parser.parse_args()

    # use the provided example ADS workspace and extract it and specify the path below
    print("Unarchiving ADS workspace")
    target_workspace_dir = args.output_dir
    util.safe_makedirs(args.output_dir)
    input_workspace_file = os.path.abspath(
        os.path.join("data", "simple_matching_wrk.7zads")
    )
    target_workspace = os.path.join(args.output_dir, "simple_matching_wrk")

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
    ads_application.unarchive_workspace(input_workspace_file, args.output_dir)

    # use the provided EMPro workspace and extract it and specify the path below
    library_dir = os.path.join(args.output_dir, "empro_workdir", "antenna_lib")
    util.safe_makedirs(library_dir)
    ariane.Library.create(library_dir, os.path.basename(library_dir))
    empro.toolkit.zap.unzep(
        os.path.join("data", "test_antenna_inverted_f.zep"), "all", library_dir
    )

    # Load the empro project
    print("Loading EMPro project")
    empro_proj = empro.activeProject.loadActiveProjectFrom(
        os.path.join(library_dir, "test_antenna_inverted_f")
    )

    print("Creating ADS Circuit Simulation connection")
    ads_circuitsim = ads.CircuitSimulator()

    # Extract the netlist from ADS
    print("Generating netlist")
    netlist = ads_application.generate_netlist(
        target_workspace,
        ads.LibraryCellView(
            library="simple_matching_lib", cell="matching_s_param", view="schematic"
        ),
    )

    print("Loading netlist in Circuit")
    matching_network = circuit.Circuit(
        netlist, import_options=Bunch(extract_analyses=False)
    )

    def optimization_goal(x):
        """Optimize the reflection to be minimal at 2.4 GHz."""
        _, resonance = lc_resonance(
            l_value=x[0],
            c_value=x[1],
            t_cond=x[2],
            t_subst=x[3],
            matching_network=matching_network,
            workdir_path=target_workspace_dir,
            workspace_path=target_workspace,
            iterate_output_dirs=iterate_output_dirs,
        )
        value = (resonance - 2.4e9) ** 2
        return value

    print("Optimizing circuit...")
    result = optimize.minimize(
        optimization_goal,
        x0=np.array(
            [
                2e-9,  # L
                0.6e-12,  # C
                0.000034,  # conductor_thickness
                0.0015,  # substrate_thickness
            ]
        ),
        bounds=optimize.Bounds(
            [2e-10, 0.6e-13, 0.000034 * 0.25, 0.0015 * 0.25],
            [2e-8, 0.6e-11, 0.000034 * 4.0, 0.0015 * 4.0],
        ),
        method="nelder-mead",
        options={"disp": False},
    )

    print("Optimization converged")
    print(
        f"L = {result.x[0] * 1e9} nH, C = {result.x[1] * 1e12} pF, "
        f"conductor_thickness = {result.x[2] * 1e3} mm, "
        f"substrate_thickness = {result.x[3] * 1e3} mm"
    )

    mag_s11, resonance = lc_resonance(
        l_value=result.x[0],
        c_value=result.x[1],
        t_cond=result.x[2],
        t_subst=result.x[3],
        matching_network=matching_network,
        workdir_path=target_workspace_dir,
        workspace_path=target_workspace,
        iterate_output_dirs=iterate_output_dirs,
    )

    print(f"Resonance={resonance * 1e-9} GHz, value={20.0 * math.log10(mag_s11)} dB")
    print("Optimization completed")
```

On this page

[Previous

Example baluns](ex_baluns.md)
[Next

Example create 3d empro serpentines](ex_create_3d_empro_serpentines.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top