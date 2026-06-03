# Examples
> **说明：** Examples 相关页面。

> **何时使用：** 当你需要查阅 Examples 相关内容时

---

## 本文件目录

- **Example baluns** (`Examples/ex_baluns.md`)
- **Example co optimize matching network** (`Examples/ex_co_optimize_matching_network.md`)
- **Example create 3d empro serpentines** (`Examples/ex_create_3d_empro_serpentines.md`)
- **Example dump workspace netlists** (`Examples/ex_dump_workspace_netlists.md`)
- **Example empro extract resonance** (`Examples/ex_empro_extract_resonance.md`)
- **Example high pass filter sub circuit** (`Examples/ex_high_pass_filter_sub_circuit.md`)
- **Example import brd** (`Examples/ex_import_brd.md`)
- **Example import ipc2581** (`Examples/ex_import_ipc2581.md`)
- **Example import odb** (`Examples/ex_import_odb.md`)
- **Example low pass filter** (`Examples/ex_low_pass_filter.md`)
- **Example multi python** (`Examples/ex_multi_python.md`)
- **Example odbpp simulate pipro ac reuse sio** (`Examples/ex_odbpp_simulate_pipro_ac_reuse_sio.md`)
- **Example odbpp simulate pipro dc** (`Examples/ex_odbpp_simulate_pipro_dc.md`)
- **Example odbpp simulate rfpro** (`Examples/ex_odbpp_simulate_rfpro.md`)
- **Example optimize matching network** (`Examples/ex_optimize_matching_network.md`)
- **Example pipro ac** (`Examples/ex_pipro_example_ac.md`)
- **Example pipro dc** (`Examples/ex_pipro_example_dc.md`)
- **Example quantumpro one qubit epr** (`Examples/ex_quantumpro_one_qubit_epr.md`)
- **Example quantumpro one qubit freq** (`Examples/ex_quantumpro_one_qubit_freq.md`)
- **Example rfpro stop nets** (`Examples/ex_rfpro_stop_nets.md`)
- **Example run hb simulation** (`Examples/ex_run_hb_simulation.md`)
- **Example run netlist** (`Examples/ex_run_netlist.md`)
- **Example run netlist from disk** (`Examples/ex_run_netlist_from_disk.md`)
- **Example run schematic** (`Examples/ex_run_schematic.md`)
- **Example sipro automation** (`Examples/ex_sipro_automation.md`)
- **Example sipro channelsim flow** (`Examples/ex_sipro_channelsim_flow.md`)
- **Example sipro SI** (`Examples/ex_sipro_example_si.md`)
- **Example sipro extract tdr** (`Examples/ex_sipro_extract_tdr.md`)
- **Example sipro eye diagram** (`Examples/ex_sipro_eye_diagram.md`)
- **Example sipro ploteye plotly** (`Examples/ex_sipro_ploteye_plotly.md`)
- **Example sweep inductor values** (`Examples/ex_sweep_inductor_values.md`)
- **Example systemvue basic** (`Examples/ex_systemvue_basic.md`)
- **Example voltage divider** (`Examples/ex_voltage_divider.md`)
- **Example vsa meas demo** (`Examples/ex_vsa_meas_demo.md`)
- **Examples** (`Examples/index.md`)

---

<!-- === 来源: Examples/ex_baluns.md === -->

# Example baluns[](#example-baluns "Link to this heading")

This example demonstrates how to create and analyze balun circuit using the EDA Toolbox.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2023 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
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
    balun_circuit = circuit.Circuit()

    SnP1 = balun_circuit.add(
        circuit.SnP(
            name="SnP1", n1=None, n2=None, n3=None, n4=None, NumPorts=4, File='"T.s4p"'
        )
    )
    Balun1 = balun_circuit.add(
        circuit.Balun4Port(
            name="balun1", c="cbalun1", d="dbalun1", p="pbalun1", n="nbalun1"
        )
    )
    Balun2 = balun_circuit.add(
        circuit.Balun4Port(
            name="balun2", c="cbalun2", d="dbalun2", p="pbalun2", n="nbalun2"
        )
    )

    TermG1 = balun_circuit.add(circuit.Port(name="Term1", Num=1, Z=100, p=None, n=None))
    TermG2 = balun_circuit.add(circuit.Port(name="Term2", Num=3, Z=10, p=None, n=None))
    TermG3 = balun_circuit.add(
        circuit.Port(name="Term3", Num=2, Z=1000, p=None, n=None)
    )
    TermG4 = balun_circuit.add(circuit.Port(name="Term4", Num=4, Z=25, p=None, n=None))

    for port in [TermG1, TermG2, TermG3, TermG4]:
        balun_circuit.connect(port.n, balun_circuit.GND)

    balun_circuit.connect(TermG1.p, Balun1.d)
    balun_circuit.connect(TermG2.p, Balun1.c)
    balun_circuit.connect(Balun1.p, SnP1.n1)
    balun_circuit.connect(Balun1.n, SnP1.n3)

    balun_circuit.connect(SnP1.n2, Balun2.p)
    balun_circuit.connect(SnP1.n4, Balun2.n)

    balun_circuit.connect(Balun2.d, TermG3.p)
    balun_circuit.connect(Balun2.c, TermG4.p)

    analysis = circuit.SP_Analysis(name="SP1")
    analysis.frequency_plan = [
        circuit.sweeps.LinearSweep(start=0.0, stop=20e9, step=0.01e9)
    ]
    balun_circuit.analyses.append(analysis)
    balun_circuit.output_dataset = "common_diff"

    print("Running circuit simulation")
    circuit_sim = ads.CircuitSimulator()
    print(balun_circuit.generate_netlist())
    circuit_sim.run_netlist(
        balun_circuit.generate_netlist(), output_dir=target_output_dir
    )
    output_data = dataset.Dataset(os.path.join(target_output_dir, "common_diff.ds"))
```


---

<!-- === 来源: Examples/ex_co_optimize_matching_network.md === -->

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


---

<!-- === 来源: Examples/ex_create_3d_empro_serpentines.md === -->

# Example create 3d empro serpentines[](#example-create-3d-empro-serpentines "Link to this heading")

This example demonstrates how to create and model serpentines in EMPro.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2022 Keysight Technologies, Inc , Keysight Confidential
# ruff: noqa: D103
"""Example on how to create a 3D serpentine in EMPro and simulate it."""

from argparse import ArgumentParser
import os

from keysight.edatoolbox import util

try:
    import empro
    from empro.geometry import Boolean, Box, Cover, Line, Model, Sketch, Trace
    import empro.toolkit
except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using "
        "the Python from EMPro. Use it by launching emproenv.bat/.sh"
    )
    raise

# convenience functions to simplify creating serpentines
def addPolyLine(sketch, vertices):
    for tail, head in zip(vertices[:-1], vertices[1:], strict=False):
        sketch.add(Line(tail, head))

def addPolygon(sketch, vertices):
    addPolyLine(sketch, vertices + vertices[:1])

def sheetBody(sketch):
    model = Model()
    model.recipe.append(Cover(sketch))
    return model

def makeSheetBody(listOfPolygonsByVertices):
    sketch = Sketch()
    for polygonVertices in listOfPolygonsByVertices:
        addPolygon(sketch, polygonVertices)
    return sheetBody(sketch)

# Example function on how to union multiple models into one model
def unionModels(models):
    assert len(models) > 1
    return Boolean.uniteMulti(models[0], models[1:])

# create trace based parts, that optionally have fillets and thickness
def makeTraceParts(listOfPolylinesByVertices, width, thickness=0.0):
    parts = []
    for polygonVertices in listOfPolylinesByVertices:
        sketch = Sketch()
        vertices = [(vertex[0], vertex[1], 0.0) for vertex in polygonVertices]
        addPolyLine(sketch, vertices)
        for idx, polygonVertex in enumerate(polygonVertices):
            if len(polygonVertex) > 2:  # the vertex contains a fillet radius
                sketch.filletVertex(f"vertex{idx}", polygonVertex[2])
        trace = Trace(sketch)
        trace.width = width
        model = Model()
        model.recipe.append(trace)
        if float(empro.core.Expression(thickness)) > 0.0:
            model.recipe.append(empro.geometry.ThickenSheet(thickness))
        parts.append(model)
    return parts

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

    output_dir = args.output_dir
    util.safe_makedirs(output_dir)
    empro_proj_path = os.path.join(output_dir, "testserpentines")

    assert output_dir is not None
    assert empro_proj_path is not None
    assert os.path.exists(output_dir)
    assert not os.path.exists(empro_proj_path), (
        "EMPro project 'testserpentines' already exists!"
    )

    print(f"Target output dir: {output_dir}")
    print(f"EMPro output project: {empro_proj_path}")

    with empro.activeProject as project:
        traces = [
            [
                (0.0, 0.0),
                (0.001, 0.0, 0.00025),
                (0.001, 0.001, 0.00025),
                (0.002, 0.001, 0.00025),
                (0.002, 0.0, 0.00025),
                (0.003, 0.0),
            ]
        ]
        serpentines = makeTraceParts(traces, "0.1 mm", "0.025 mm")
        for serpentine in serpentines:
            project.geometry.append(serpentine)

        empro.activeProject.materials.append(empro.toolkit.defaultMaterial("Cu"))
        for part in project.geometry.flatList(False):
            part.material = project.materials[-1]

        substrate = empro.geometry.Model()
        substrate.recipe.append(Box(0.005, 0.0001, 0.003))
        substrate.coordinateSystem.anchorPoint = (0.0015, 0.0005, -0.0001)
        project.geometry.append(substrate)
        project.materials.append(empro.toolkit.defaultMaterial("FR-4"))
        project.geometry[1].material = project.materials[-1]

        empro.activeProject.saveActiveProjectTo(empro_proj_path)
        empro.activeProject.loadActiveProjectFrom(empro_proj_path)
```


---

<!-- === 来源: Examples/ex_dump_workspace_netlists.md === -->

# Example dump workspace netlists[](#example-dump-workspace-netlists "Link to this heading")

This example demonstrates how to create a netlist for each circuit in a workspace.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
import os
import re

from keysight.edatoolbox import ads, circuit, util

try:
    import empro
    import ariane
except ImportError:
    print("ariane module is not found, run this example using the Python from xxPro")
    raise

def query(lib_defs):
    def map_libraries(lib_defs):
        if not os.path.isfile(lib_defs):
            raise ValueError("{lib_defs} does not exist".format(lib_defs=lib_defs))
        return {name: path for (path, name) in ariane.getFlattenedLibraryList(lib_defs)}

    libraries = map_libraries(lib_defs)
    for library in libraries:
        try:
            lib_path = libraries[library]
        except KeyError:
            raise ValueError(
                "{library} is not a library in {lib_defs}".format(
                    lib_defs=lib_defs, library=library
                )
            )

        lib = ariane.Library.open(lib_path)
        schematics = [
            ads.LibraryCellView(library, cell, view)
            for cell, view, type_ in lib.getCellViewNamesAndTypes()
            if type_ == "schematic"
        ]
        return schematics

if __name__ == "__main__":
    circuit_sim_built_in_vars = set(["NonLinearDemoKit_thermal"])

    parser = ArgumentParser()
    parser.add_argument(
        "--output-dir",
        action="store",
        default=None,
        help="Location of the workspace to query",
    )
    args = parser.parse_args()

    target_workspace_dir = args.output_dir
    util.safe_makedirs(target_workspace_dir)
    input_workspace_file = os.path.abspath("data/simple_matching_wrk.7zads")
    target_workspace = os.path.join(target_workspace_dir, "simple_matching_wrk")

    ads_application = ads.ADS()
    print("ADS application created")

    print("Unarchiving workspace")
    ads_application.unarchive_workspace(input_workspace_file, target_workspace_dir)

    lib_defs = os.path.join(target_workspace, "lib.defs")
    schematics = query(lib_defs)

    ads_application = ads.ADS()
    netlists = ads_application.generate_netlist(target_workspace, schematics)

    for index, netlist in enumerate(netlists):
        with open(f"{target_workspace}/netlist_{index}.ckt", "w") as nlf:
            nlf.write(netlist)
        ckt = circuit.Circuit(netlist)
        print(schematics[index])
        if ckt.instances:
            print(" Instances:")
            for inst_name, inst in ckt.instances.items():
                if isinstance(inst, circuit.Var):
                    # Var's are instances themselves but we do not enlist them here
                    # as they have a dedicated section
                    continue
                if hasattr(inst, "instance_parameters"):
                    # This part is a workaround to handle instance parameters
                    # with index "[x-x]"; will be replaced as an API
                    instanceParameters = ""
                    for p in inst.instance_parameters.keys():
                        numIndex = re.search(r"\[(.*?)\]", p)
                        if numIndex:
                            baseParameterName = p.split("[")[0]
                            startIndex = int(numIndex.group(1).split("-")[0])
                            endIndex = int(numIndex.group(1).split("-")[1])
                            for x in range(startIndex, endIndex + 1):
                                currentParameter = f'{baseParameterName}[{x}]'
                                if getattr(inst, baseParameterName):
                                    instanceParameters = ",".join(
                                        [instanceParameters, currentParameter]
                                    )
                        else:
                            if getattr(inst, p):
                                instanceParameters = ",".join([instanceParameters, p])
                    print("  ", inst_name, "->", instanceParameters)
                else:
                    print("  ", inst_name, "-> no instance parameters available")
        if ckt.variables:
            print(" Variables:")
            var_names = [
                var
                for var in ckt.variables.keys()
                if var not in circuit_sim_built_in_vars
            ]
            print("  ", ",".join(var_names))
            for var_name in var_names:
                var = ckt.instances[var_name]
                print(
                    f'   {var_name}={var.value} {var.optimization or "No optimization info"}, {var.tuning or "No tuning info"}'
                )
        else:
            print(" No variables found")
```


---

<!-- === 来源: Examples/ex_empro_extract_resonance.md === -->

# Example empro extract resonance[](#example-empro-extract-resonance "Link to this heading")

This example demonstrates how to extract the resonant frequency of a patch antenna.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2025 Keysight Technologies, Keysight Confidential
# ruff: noqa: D100

from argparse import ArgumentParser
import json
import math
import os

import ariane
import empro
import empro.toolkit.portparam
import empro.toolkit.simulation
import empro.toolkit.zap

from keysight.edatoolbox import util

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

    assert not os.path.exists(args.output_dir), (
        f"Target workspace {args.output_dir} already exists!"
    )

    util.safe_makedirs(args.output_dir)

    parameters = None
    parameter_filepath = os.path.abspath("data/parameters.json")
    with open(parameter_filepath, "r") as parameter_file:
        data = parameter_file.read()
        parameters = json.loads(data)
        print("Loaded parameters: {parameters}", parameters)

    # assume it is an OA version, create the hosting library
    libraryDir = args.output_dir
    ariane.Library.create(libraryDir, os.path.basename(libraryDir))
    # unzep in the library
    proj_path = os.path.abspath("data/test_antenna_inverted_f.zep")
    empro.toolkit.zap.unzep(proj_path, "all", libraryDir)
    proj = empro.activeProject.loadActiveProjectFrom(
        os.path.join(libraryDir, "test_antenna_inverted_f")
    )

    with empro.activeProject as project:
        project.parameters.setFormula(
            "conductor_thickness", parameters["conductor_thickness"]
        )
        project.parameters.setFormula(
            "substrate_thickness", parameters["substrate_thickness"]
        )

    simulation = empro.activeProject.createSimulation(True)
    print("Running and waiting for simulation...")
    empro.activeProject.simulations.isQueueHeld = False
    empro.toolkit.simulation.wait(simulation)

    s = empro.toolkit.portparam.getSMatrix(sim=simulation.id())
    s11 = s[1, 1]
    resonant_value, resonant_frequency = min(
        zip(abs(s11), s11.dimension(0), strict=False)
    )
    resonant_value = 20.0 * math.log(resonant_value) / math.log(10.0)

    print("Resonance frequency: {}".format(resonant_frequency))
    print("Resonance value: {}".format(resonant_value))
    output_file = os.path.join(libraryDir, "output.txt")
    with open(output_file, "w") as output_file:
        output_file.write("Resonance frequency: {}\n".format(resonant_frequency))
        output_file.write("Resonance value: {}".format(resonant_value))
```


---

<!-- === 来源: Examples/ex_high_pass_filter_sub_circuit.md === -->

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


---

<!-- === 来源: Examples/ex_import_brd.md === -->

# Example import brd[](#example-import-brd "Link to this heading")

This example demonstrates how to import a .BRD file into ADS.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2025 Keysight Technologies, Inc, Keysight Confidential
#
from argparse import ArgumentParser
import os
import subprocess

from keysight.edatoolbox import ads, util

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
        "--cds-root",
        action="store",
        required=False,
        default=None,
        help="Location of Cadence Allegro PCB Designer",
    )
    parser.add_argument(
        "board",
        action="store",
        nargs="?",
        default="data/PC4_RDIMM_V090_RC_J0_20130725.brd",
        help="The .brd file to import",
    )
    args = parser.parse_args()
    cds_root = args.cds_root

    if cds_root is not None:
        os.environ["CDS_ROOT"] = cds_root
    elif os.environ.get("CDS_ROOT") is not None:
        cds_root = os.environ["CDS_ROOT"]
    else:
        raise ValueError(
            "BRD file importer requires Extracta utility from Allegro PCB Designer"
        )

    target_workspace_dir = args.output_dir
    if not os.path.isabs(target_workspace_dir):
        target_workspace_dir = os.path.abspath(target_workspace_dir)

    util.safe_makedirs(target_workspace_dir)
    workspace_name = "brd_import_wrk"
    target_workspace = os.path.join(target_workspace_dir, workspace_name)

    assert target_workspace_dir is not None
    assert os.path.exists(target_workspace_dir)
    assert not os.path.exists(target_workspace), (
        f"Target workspace {target_workspace} already exists!"
    )

    print(f"Target output dir: {target_workspace_dir}")

    ads_application = ads.ADS()
    ads_application.create_workspace(target_workspace_dir, workspace_name)
    print("ADS workspace created")

    brd_file = os.path.split(args.board)[-1]
    src_brd_file = os.path.abspath(args.board)
    dest_brd_file = os.path.join(target_workspace_dir, brd_file)

    print("Prepare board for import with current Allegro version by running dbdoctor")

    try:
        cmd = [
            os.path.join(cds_root, "tools", "bin", "dbdoctor"),
            "-outfile",
            dest_brd_file,
            src_brd_file,
        ]
        res = subprocess.run(
            cmd,
            cwd=target_workspace_dir,
            capture_output=True,
            text=True,
        )
        # return codes 1, 2, 3 seen for successful updates depending
        # on the fixes/changes that dbdoctor needed to perform.
        assert res.returncode <= 3, (
            f"Cannot process {brd_file} with extracta\n\n{res.stderr}"
        )
        print(res.stdout)
    except Exception:
        print(f"Command failed: {' '.join(cmd)}")
        raise

    print("Import .brd")
    ads_application.import_brd(target_workspace, dest_brd_file)
```


---

<!-- === 来源: Examples/ex_import_ipc2581.md === -->

# Example import ipc2581[](#example-import-ipc2581 "Link to this heading")

This example demonstrates how to import an IPC2581 file into ADS.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2024 Keysight Technologies, Inc, Keysight Confidential
#
from argparse import ArgumentParser
import os

from keysight.edatoolbox import ads, util

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
    workspace_name = "ipc2581_import_wrk"
    target_workspace = os.path.join(target_workspace_dir, workspace_name)

    assert target_workspace_dir is not None
    assert os.path.exists(target_workspace_dir)
    assert not os.path.exists(
        target_workspace
    ), f"Target workspace {target_workspace} already exists!"

    print(f"Target output dir: {target_workspace_dir}")

    ads_application = ads.ADS()
    ads_application.create_workspace(target_workspace_dir, workspace_name)
    print("ADS workspace created")

    print("Import IPC-2581")
    ipc_file = os.path.abspath("data/test-3_r2.xml")
    ads_application.import_ipc2581(
        target_workspace, ipc_file, library="test", cell="test"
    )
```


---

<!-- === 来源: Examples/ex_import_odb.md === -->

# Example import odb[](#example-import-odb "Link to this heading")

This example demonstrates how to import an ODB++ file into ADS.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#
from argparse import ArgumentParser
import os

from keysight.edatoolbox import ads, util

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
    workspace_name = "odb_import_wrk"
    target_workspace = os.path.join(target_workspace_dir, workspace_name)

    assert target_workspace_dir is not None
    assert os.path.exists(target_workspace_dir)
    assert not os.path.exists(
        target_workspace
    ), f"Target workspace {target_workspace} already exists!"

    print(f"Target output dir: {target_workspace_dir}")

    ads_application = ads.ADS()
    ads_application.create_workspace(target_workspace_dir, workspace_name)
    print("ADS workspace created")

    print("Import ODB++")
    odb_file = os.path.abspath("data/Minipc/minipc_pm_v0_pm.zip")
    ads_application.import_odbpp(
        target_workspace, odb_file, library="minipc_lib", use_legacy_importer=False
    )
```


---

<!-- === 来源: Examples/ex_low_pass_filter.md === -->

# Example low pass filter[](#example-low-pass-filter "Link to this heading")

This example demonstrates how to design and analyze low pass filter circuits.

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

    low_pass_filter = circuit.Circuit()

    R1 = low_pass_filter.add(circuit.R(name="R1", R="1 kOhm", p=None, n=None))
    C1 = low_pass_filter.add(circuit.C(name="C1", C="1 uF", p=None, n=None))
    V = low_pass_filter.add(
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

    low_pass_filter.connect(V.n, low_pass_filter.GND)
    low_pass_filter.connect(V.p, R1.p)
    low_pass_filter.connect(R1.n, C1.p)
    low_pass_filter.connect(C1.n, low_pass_filter.GND)

    ac_analysis = circuit.AC_Analysis(name="AC1")
    ac_analysis.sweep_plan.append(circuit.sweeps.LogarithmicSweep(1, 1e6, 5))
    low_pass_filter.analyses.append(ac_analysis)
    low_pass_filter.output_dataset = "low_pass_filter"

    print("Running circuit simulation")
    circuit_sim = ads.CircuitSimulator()
    circuit_sim.run_netlist(
        low_pass_filter.generate_netlist(), output_dir=target_output_dir
    )
    output_data = dataset.Dataset(os.path.join(target_output_dir, "low_pass_filter.ds"))
    print("Response at C1", output_data.values("AC1.AC", str(C1.p)))

    try:
        import matplotlib.pyplot as plt

        response = [
            20.0 * math.log10(abs(x)) for x in output_data.values("AC1.AC", str(C1.p))
        ]
        plt.plot(response)
        plt.show(block=False)
        plt.pause(3)
        plt.close()
    except ImportError:
        pass
```


---

<!-- === 来源: Examples/ex_multi_python.md === -->

# Example multi python[](#example-multi-python "Link to this heading")

This example demonstrates how to work with multiple Python versions from a single script.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2024 Keysight Technologies, Inc, Keysight Confidential
#

from keysight.edatoolbox import multi_python

def xxpro_scoped_function():
    import empro

    return empro.core.ApplicationInfo.applicationName()

def ads_scoped_function():
    print("ads_scoped_function")
    from keysight.ads import de

    return de.version()

if __name__ == "__main__":
    with multi_python.ads_context() as ads_ctx:
        for i in range(10):
            ads_ctx.call(ads_scoped_function)

    with multi_python.xxpro_context() as empro_ctx:
        for i in range(10):
            assert "EMPro" in empro_ctx.call(xxpro_scoped_function)

    with multi_python.xxpro_context(
        r"C:\kd\empro\prod\opt\empro\prod\win32_64\bin\tools\win32\python"
    ) as empro_ctx:
        for i in range(10):
            assert "EMPro" in empro_ctx.call(xxpro_scoped_function)
```


---

<!-- === 来源: Examples/ex_odbpp_simulate_pipro_ac_reuse_sio.md === -->

# Example odbpp simulate pipro ac reuse sio[](#example-odbpp-simulate-pipro-ac-reuse-sio "Link to this heading")

This example demonstrates how to import an ODB++ file and setup a PIPro AC simulation and reuse an existing .sio file.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2025 Keysight Technologies, Keysight Confidential
# ruff: noqa: D100
from argparse import ArgumentParser
import glob
import os
from pathlib import Path

import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots

from keysight.edatoolbox import ads, circuit, momentum, util, xxpro
import keysight.pwdatatools as pwdt

try:
    import empro
    import empro.toolkit
    import empro.toolkit.analysis
except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using the Python"
        " from EMPro. Use it by launching emproenv.bat/.sh"
    )
    raise

class Bunch(object):
    """Convert input kwargs to object attributes."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

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
        "--reuse-sio",
        action="store_true",
        help="Reuse the sio file",
    )
    args = parser.parse_args()
    output_dir = Path(args.output_dir).absolute()
    reuse_sio = args.reuse_sio
    util.safe_makedirs(args.output_dir)

    # Path to odbfile
    data_path = Path(__file__).parent / "data"
    odb_file = data_path / "Minipc" / "minipc_pm_v0_pm.zip"
    cell_name = "minipc"
    library_name = f"{cell_name}_lib"
    target_workspace_name = f"{cell_name}_wrk"
    target_workspace_path = output_dir / target_workspace_name
    target_workspace = str(target_workspace_path)
    netlist_directory = data_path / "PIProACAnalysis" / "Netlist"
    sio_file = data_path / "PIProACAnalysis" / "siofile" / "design.sio"

    assert odb_file.exists(), f"Input ODB++ file {odb_file} does not exist!"
    assert output_dir.exists(), f"Output directory {output_dir} does not exist!"
    assert netlist_directory.exists(), (
        f"Netlist directory {netlist_directory} does not exist!"
    )
    assert sio_file.exists(), f"SIO file {sio_file} does not exist!"
    assert not target_workspace_path.exists(), (
        f"Target workspace {target_workspace} already exists!"
    )

    print(f"Input ODB++: {odb_file}")

    print(f"Target workspace: {target_workspace}")

    if not reuse_sio:
        # Step 1: Creating the ADS application object
        ads_application = ads.ADS()
        print("ADS application created")
        print("Creating workspace")
        if not os.path.exists(target_workspace):
            ads_application.create_workspace(output_dir, target_workspace_name)

        # Step 2: Import odb++ file

        print("Importing ODB++")

        odbpp_import_options = ads.OdbImportOptions()
        odbpp_import_options.separate_component_lib = False
        odbpp_import_options.separate_tech_lib = False

        ads_application.import_odbpp(
            target_workspace,
            odb_file,
            library=library_name,
            cell=cell_name,
            use_legacy_importer=False,
            import_options=odbpp_import_options,
        )
        print("ODB++ imported")

        # update the material database
        matdb_path = str(target_workspace_path / library_name / "materials.matdb")
        matdb = ads.MaterialDatabase(matdb_path)
        for diel in matdb.dielectrics:
            eps_r = float(diel.er_real)
            if eps_r <= 0.0:
                diel.er_real = 4.0
        matdb.write(matdb_path)

        # update the thickness of metal layers
        subst_path = str(target_workspace_path / library_name / "tech.subst")
        substrate_info = ads.SubstrateModel(subst_path)
        for layer in substrate_info.layers:
            if layer.layer == 1033:
                layer.thick = -1.761411  # negative thickness : below interface
            if layer.index == 8:
                layer.thick = 0.6654142

        # update the thickness of dielectric layers
        for material in substrate_info.materials:
            if material.index == 1:
                material.thick = 3.01

        substrate_info.write(subst_path)
        input_lcv = ads.LibraryCellView(
            library=library_name, cell=cell_name, view="layout"
        )
        pro_lcv = ads.LibraryCellView(
            library=library_name, cell=cell_name, view="sipi1"
        )

        # Step 3: Creating the SIPro view
        print("Creating PIPro simulation view")
        ads_application.create_pro_view(
            target_workspace,
            input_lcv=input_lcv,
            substrate=cell_name,
            pro_lcv=pro_lcv,
            tool="sipi",
        )
        print("PIPro simulation view created")

        momentum_dir = momentum.get_momentum_location()
        empro.toolkit.analysis.setMomentumDir(momentum_dir)
        with util.remember_cwd():
            os.environ["HPEESOF_DIR"] = (
                ads.get_ads_location()
            )  # ensure the referenced env vars in lib.defs can be found

            # Step 4: Loading the SIPro view into the SIPro tool
            xxpro.use_workspace(target_workspace)
            xxpro.load_pro_view(pro_lcv)
            empro.activeProject.saveActiveProject()

            # Step 5 : ==== Script generated by ADS Window starts here =====
            # Create an Analysis
            analysis = empro.analysis.Analysis()
            analysis.name = "AC by Script"
            analysis.analysisType = empro.analysis.Analysis.ACAnalysisType

            # Set VRM List
            vrmList = analysis.vrms

            plusPins = ["Q4.1", "Q4.2", "Q4.3"]
            minusPins = ["C3.1", "Q6.2"]
            vrm = empro.toolkit.analysis.createVrmFromPins(plusPins, minusPins)
            vrm.name = "PLL_1V8_Q4"
            vrm.resistance = empro.core.Expression("0 Ohm")
            vrm.tolerance = empro.core.Expression("0.01")
            vrm.outputVoltagePositiveVariation = empro.core.Expression("0.00")
            vrm.outputVoltageNegativeVariation = empro.core.Expression("0.00")
            vrm.inductance = empro.core.Expression("0 mH")
            vrm.voltage = empro.core.Expression("1.5 V")
            vrm.sourceType = "PackagedVrm"
            vrm.hasSenseLine = False
            vrmList.append(vrm)

            # Set Sink List
            sinkList = analysis.sinks

            plusPins = [
                "U1.AB14",
                "U1.AC14",
                "U1.AC16",
                "U1.AC17",
                "U1.AC19",
                "U1.AC21",
                "U1.AD27",
                "U1.AE18",
                "U1.AH27",
                "U1.AM27",
                "U1.D27",
                "U1.H27",
                "U1.M27",
                "U1.T27",
                "U1.U15",
                "U1.U16",
                "U1.U17",
                "U1.U20",
                "U1.U21",
                "U1.U22",
                "U1.W19",
                "U1.Y27",
            ]
            minusPins = [
                "U1.A6",
                "U1.A11",
                "U1.A16",
                "U1.A21",
                "U1.A27",
                "U1.A29",
                "U1.A30",
                "U1.A31",
                "U1.A34",
                "U1.A35",
                "U1.A38",
                "U1.AA1",
                "U1.AA11",
                "U1.AA17",
                "U1.AA21",
                "U1.AA26",
                "U1.AA27",
                "U1.AA28",
                "U1.AA29",
                "U1.AA30",
                "U1.AA31",
                "U1.AA34",
                "U1.AA35",
                "U1.AA38",
                "U1.AA39",
                "U1.AB3",
                "U1.AB8",
                "U1.AB13",
                "U1.AB18",
                "U1.AB23",
                "U1.AB26",
                "U1.AB27",
                "U1.AB32",
                "U1.AB33",
                "U1.AB36",
                "U1.AB37",
                "U1.AC10",
                "U1.AC15",
                "U1.AC20",
                "U1.AC22",
                "U1.AC25",
                "U1.AC27",
                "U1.AC28",
                "U1.AC29",
                "U1.AC30",
                "U1.AC31",
                "U1.AC34",
                "U1.AC35",
                "U1.AC38",
                "U1.AC39",
                "U1.AD2",
                "U1.AD12",
                "U1.AD26",
                "U1.AD32",
                "U1.AD33",
                "U1.AD36",
                "U1.AD37",
                "U1.AE4",
                "U1.AE9",
                "U1.AE19",
                "U1.AE24",
                "U1.AE26",
                "U1.AE27",
                "U1.AE30",
                "U1.AE31",
                "U1.AE34",
                "U1.AE35",
                "U1.AE38",
                "U1.AE39",
                "U1.AF1",
                "U1.AF6",
                "U1.AF11",
                "U1.AF16",
                "U1.AF26",
                "U1.AF27",
                "U1.AF30",
                "U1.AF31",
                "U1.AF32",
                "U1.AF33",
                "U1.AF34",
                "U1.AF35",
                "U1.AF36",
                "U1.AF37",
                "U1.AG3",
                "U1.AG13",
                "U1.AG18",
                "U1.AG23",
                "U1.AG26",
                "U1.AG27",
                "U1.AG30",
                "U1.AG31",
                "U1.AG34",
                "U1.AG35",
                "U1.AG38",
                "U1.AG39",
                "U1.AH10",
                "U1.AH15",
                "U1.AH20",
                "U1.AH26",
                "U1.AH32",
                "U1.AH33",
                "U1.AH36",
                "U1.AH37",
                "U1.AJ2",
                "U1.AJ7",
                "U1.AJ12",
                "U1.AJ17",
                "U1.AJ22",
                "U1.AJ27",
                "U1.AJ28",
                "U1.AJ29",
                "U1.AJ30",
                "U1.AJ31",
                "U1.AJ34",
                "U1.AJ35",
                "U1.AJ38",
                "U1.AJ39",
                "U1.AK4",
                "U1.AK27",
                "U1.AK32",
                "U1.AK33",
                "U1.AK36",
                "U1.AK37",
                "U1.AL1",
                "U1.AL16",
                "U1.AL27",
                "U1.AL30",
                "U1.AL31",
                "U1.AL34",
                "U1.AL35",
                "U1.AL38",
                "U1.AL39",
                "U1.AM3",
                "U1.AM15",
                "U1.AM23",
                "U1.AM26",
                "U1.AM32",
                "U1.AM33",
                "U1.AM36",
                "U1.AM37",
                "U1.AN5",
                "U1.AN10",
                "U1.AN15",
                "U1.AN20",
                "U1.AN27",
                "U1.AN30",
                "U1.AN31",
                "U1.AN34",
                "U1.AN35",
                "U1.AN38",
                "U1.AN39",
                "U1.AP2",
                "U1.AP7",
                "U1.AP12",
                "U1.AP14",
                "U1.AP27",
                "U1.AP32",
                "U1.AP33",
                "U1.AP36",
                "U1.AP37",
                "U1.AR4",
                "U1.AR9",
                "U1.AR14",
                "U1.AR15",
                "U1.AR19",
                "U1.AR27",
                "U1.AR30",
                "U1.AR31",
                "U1.AR34",
                "U1.AR35",
                "U1.AR38",
                "U1.AR39",
                "U1.AT1",
                "U1.AT6",
                "U1.AT11",
                "U1.AT16",
                "U1.AT27",
                "U1.AT28",
                "U1.AT29",
                "U1.AT32",
                "U1.AT33",
                "U1.AT36",
                "U1.AT37",
                "U1.AU3",
                "U1.AU8",
                "U1.AU13",
                "U1.AU18",
                "U1.AU23",
                "U1.AU29",
                "U1.AU30",
                "U1.AU31",
                "U1.AU34",
                "U1.AU35",
                "U1.AU38",
                "U1.AU39",
                "U1.AV5",
                "U1.AV10",
                "U1.AV15",
                "U1.AV20",
                "U1.AV25",
                "U1.AV31",
                "U1.AV32",
                "U1.AV33",
                "U1.AV36",
                "U1.AV37",
                "U1.AW7",
                "U1.AW12",
                "U1.AW17",
                "U1.AW22",
                "U1.AW27",
                "U1.AW29",
                "U1.AW31",
                "U1.AW34",
                "U1.AW35",
                "U1.AW38",
                "U1.B2",
                "U1.B3",
                "U1.B8",
                "U1.B13",
                "U1.B17",
                "U1.B18",
                "U1.B23",
                "U1.B25",
                "U1.B27",
                "U1.B28",
                "U1.B29",
                "U1.B32",
                "U1.B33",
                "U1.B36",
                "U1.B37",
                "U1.C5",
                "U1.C10",
                "U1.C15",
                "U1.C20",
                "U1.C27",
                "U1.C28",
                "U1.C29",
                "U1.C30",
                "U1.C31",
                "U1.C34",
                "U1.C35",
                "U1.C38",
                "U1.C39",
                "U1.D2",
                "U1.D7",
                "U1.D12",
                "U1.D15",
                "U1.D17",
                "U1.D22",
                "U1.D26",
                "U1.D30",
                "U1.D31",
                "U1.D32",
                "U1.D33",
                "U1.D36",
                "U1.D37",
                "U1.E4",
                "U1.E9",
                "U1.E14",
                "U1.E19",
                "U1.E27",
                "U1.E30",
                "U1.E31",
                "U1.E32",
                "U1.E33",
                "U1.E34",
                "U1.E35",
                "U1.E38",
                "U1.E39",
                "U1.F1",
                "U1.F6",
                "U1.F11",
                "U1.F16",
                "U1.F21",
                "U1.F27",
                "U1.F30",
                "U1.F31",
                "U1.F32",
                "U1.F33",
                "U1.F36",
                "U1.F37",
                "U1.G3",
                "U1.G18",
                "U1.G23",
                "U1.G27",
                "U1.G30",
                "U1.G31",
                "U1.G32",
                "U1.G33",
                "U1.G34",
                "U1.G35",
                "U1.G38",
                "U1.G39",
                "U1.H5",
                "U1.H10",
                "U1.H15",
                "U1.H26",
                "U1.H30",
                "U1.H31",
                "U1.H32",
                "U1.H33",
                "U1.H36",
                "U1.H37",
                "U1.J2",
                "U1.J7",
                "U1.J17",
                "U1.J27",
                "U1.J30",
                "U1.J31",
                "U1.J32",
                "U1.J33",
                "U1.J34",
                "U1.J35",
                "U1.J38",
                "U1.J39",
                "U1.K27",
                "U1.K32",
                "U1.K33",
                "U1.K36",
                "U1.K37",
                "U1.L1",
                "U1.L16",
                "U1.L21",
                "U1.L27",
                "U1.L30",
                "U1.L31",
                "U1.L34",
                "U1.L35",
                "U1.L38",
                "U1.L39",
                "U1.M3",
                "U1.M13",
                "U1.M18",
                "U1.M23",
                "U1.M26",
                "U1.M32",
                "U1.M33",
                "U1.M36",
                "U1.M37",
                "U1.N5",
                "U1.N10",
                "U1.N15",
                "U1.N21",
                "U1.N26",
                "U1.N27",
                "U1.N30",
                "U1.N31",
                "U1.N34",
                "U1.N35",
                "U1.N38",
                "U1.N39",
                "U1.P2",
                "U1.P7",
                "U1.P12",
                "U1.P17",
                "U1.P26",
                "U1.P27",
                "U1.P32",
                "U1.P33",
                "U1.P36",
                "U1.P37",
                "U1.R9",
                "U1.R19",
                "U1.R24",
                "U1.R26",
                "U1.R27",
                "U1.R30",
                "U1.R31",
                "U1.R34",
                "U1.R35",
                "U1.R38",
                "U1.R39",
                "U1.T1",
                "U1.T11",
                "U1.T16",
                "U1.T21",
                "U1.T26",
                "U1.T32",
                "U1.T33",
                "U1.T36",
                "U1.T37",
                "U1.U3",
                "U1.U8",
                "U1.U13",
                "U1.U18",
                "U1.U23",
                "U1.U27",
                "U1.U30",
                "U1.U31",
                "U1.U34",
                "U1.U35",
                "U1.U38",
                "U1.U39",
                "U1.V10",
                "U1.V15",
                "U1.V20",
                "U1.V25",
                "U1.V26",
                "U1.V27",
                "U1.V32",
                "U1.V33",
                "U1.V36",
                "U1.V37",
                "U1.W2",
                "U1.W7",
                "U1.W12",
                "U1.W17",
                "U1.W22",
                "U1.W26",
                "U1.W27",
                "U1.W30",
                "U1.W31",
                "U1.W34",
                "U1.W35",
                "U1.W38",
                "U1.W39",
                "U1.Y9",
                "U1.Y15",
                "U1.Y19",
                "U1.Y24",
                "U1.Y26",
                "U1.Y32",
                "U1.Y33",
                "U1.Y36",
                "U1.Y37",
            ]
            sink = empro.toolkit.analysis.createSinkFromPins(plusPins, minusPins)
            sink.name = "PLL_1V8_U1"
            sink.resistance = empro.core.Expression("1 MOhm")
            sink.positiveTolerance = empro.core.Expression("0.05")
            sink.negativeTolerance = empro.core.Expression("0.05")
            sink.current = empro.core.Expression("3 A")
            sink.pinCurrentModel = "EqualVoltage"

            sink.packageModel = None
            sinkList.append(sink)

            # Set Netlist
            netList = analysis.nets

            net = empro.analysis.Net("GND", empro.activeProject.geometry[0])
            netList.append(net)

            net = empro.analysis.Net("PLL_1V8", empro.activeProject.geometry[0])
            netList.append(net)

            # Set Component Model Group List
            componentModelGroupList = analysis.componentModelGroups

            # Create Component Model Group
            componentModelGroup = empro.analysis.ComponentModelGroup(
                f"{library_name}:grm033r60j104ke19d_capc0603x33x15ll03t05",
                empro.activeProject.geometry[0],
            )
            componentModelGroup.name = "grm033r60j104ke19d_capc0603x33x15ll03t05"
            componentModelGroup.arrayedComponent = False
            componentModelGroup.updateableAfterSimulation = True
            pinNamePortNumberPairs = (("1", -1), ("2", 1))
            pinPortMap = componentModelGroup.pinPortMap()
            pinPortMap.update(pinNamePortNumberPairs)
            instances = [
                "C424",
                "C425",
                "C426",
                "C427",
                "C428",
                "C429",
                "C430",
                "C431",
                "C432",
                "C433",
                "C434",
                "C435",
                "C436",
                "C437",
                "C438",
                "C439",
                "C440",
                "C441",
                "C442",
                "C443",
                "C444",
            ]
            for instance in instances:
                componentModelGroup.appendInstance(
                    empro.toolkit.analysis.createComponentInstanceFromInstance(instance)
                )

            # Create Component Model
            componentModel = empro.analysis.ComponentModel(
                1, ""
            )  # LumpedType = 1, ModelDBType = 2, SnPType = 3, LibCell = 4
            componentModel.name = "model"
            componentModel.getPassiveLoad().impedance.resistance = (
                empro.core.Expression("0 Ohm")
            )
            componentModel.getPassiveLoad().impedance.capacitance = (
                empro.core.Expression("0.1 uF")
            )
            componentModel.getPassiveLoad().impedance.inductance = (
                empro.core.Expression("0 H")
            )
            componentModel.getPassiveLoad().impedance.elementArrangement = "Series"
            componentModelGroup.appendModel(componentModel)
            componentModelGroupList.append(componentModelGroup)

            # Create Component Model Group
            componentModelGroup = empro.analysis.ComponentModelGroup(
                f"{library_name}:grm31cr60j107me39l_capc3216x190x55ml30t25",
                empro.activeProject.geometry[0],
            )
            componentModelGroup.name = "grm31cr60j107me39l_capc3216x190x55ml30t25"
            componentModelGroup.arrayedComponent = False
            componentModelGroup.updateableAfterSimulation = True
            pinNamePortNumberPairs = (("1", -1), ("2", 1))
            pinPortMap = componentModelGroup.pinPortMap()
            pinPortMap.update(pinNamePortNumberPairs)
            instances = ["C423"]
            for instance in instances:
                componentModelGroup.appendInstance(
                    empro.toolkit.analysis.createComponentInstanceFromInstance(instance)
                )

            # Create Component Model
            componentModel = empro.analysis.ComponentModel(
                1, ""
            )  # LumpedType = 1, ModelDBType = 2, SnPType = 3, LibCell = 4
            componentModel.name = "model"
            componentModel.getPassiveLoad().impedance.resistance = (
                empro.core.Expression("0 Ohm")
            )
            componentModel.getPassiveLoad().impedance.capacitance = (
                empro.core.Expression("100 uF")
            )
            componentModel.getPassiveLoad().impedance.inductance = (
                empro.core.Expression("0 H")
            )
            componentModel.getPassiveLoad().impedance.elementArrangement = "Series"
            componentModelGroup.appendModel(componentModel)
            componentModelGroupList.append(componentModelGroup)

            # Set Analysis Options
            options = analysis.simulationSettings

            # Set Ambient Conditions
            options.ambientConditions.backgroundTemperature = empro.core.Expression(
                298.15
            )

            # Set Frequency Plans

            # Set Frequency Plan List
            frequencyPlanList = options.femFrequencyPlanList()
            frequencyPlanList.clear()

            plan = empro.simulation.FrequencyPlan()
            plan.type = "Adaptive"
            plan.startFrequency = empro.core.Expression("10 kHz")
            plan.stopFrequency = empro.core.Expression("300 MHz")
            plan.numberOfFrequencyPoints = 300
            plan.samplePointsLimit = 300
            plan.pointsPerDecade = 5
            plan.enabled = True
            frequencyPlanList.append(plan)

            # Set Field Storage
            options.saveFieldsFor = "NoFrequencies"
            options.farFieldEnabled = False
            options.farFieldAngularResolution = empro.core.Expression("5 deg")

            # Set Simulator

            # Set Preset Simulator Setup By Name
            options.preset = None

            # Set User-Defined Advanced Simulator Setup

            # Set FEM Options

            # Set FEM Matrix Solver
            options.femMatrixSolver.solverType = "MatrixSolverAuto"

            # Set FEM Mesh Settings
            femMeshSettings = options.femMeshSettings
            femMeshSettings.includeResistiveLossesInGround = False
            femMeshSettings.orderOfBasisFunctions = 1
            femMeshSettings.useTargetMeshSize = False
            femMeshSettings.autoTargetMeshSize = False
            femMeshSettings.targetMeshSize = empro.core.Expression("2 mm")
            femMeshSettings.useMeshDomainOptimization = False
            femMeshSettings.minimumNumberOfPasses = 1
            femMeshSettings.maximumNumberOfPasses = 1
            femMeshSettings.refineAtSpecificFrequency = False
            femMeshSettings.refinementFrequency = empro.core.Expression("10 GHz")

            # Set Resources Settings
            resourceSettings = empro.simulation.LocalResourceSettings()
            resourceSettings.numberOfWorkers = 1
            resourceSettings.numberOfThreads = 0
            options.resourceSettings = resourceSettings

            # Set ParameterSweep
            options.parameterSweepEnabled = False
            options.parameterSequences.clear()

            # Add the Analysis to the list of Analyses
            empro.activeProject.analyses.append(analysis)

            # ===== Script generated by ADS Window Ends here ======
            # take the latest analysis
            active_analysis = empro.activeProject.analyses[-1]

            # Step 6: Run Analysis for the nets added in SIPro
            print("Running and waiting for simulation...")
            empro.toolkit.analysis.runAnalysis(
                active_analysis, waitForConfirmation=False, saveProject=True
            )
            empro.activeProject.simulations.isQueueHeld = False
            active_simulation = empro.activeProject.simulations[-1]
            empro.toolkit.simulation.wait(active_simulation)
            new_sio_location = os.path.join(
                active_simulation.simulationPath(), "emds_dsn", "design", "design.sio"
            )
            empro.activeProject.saveActiveProject()
    else:
        new_sio_location = sio_file
        os.environ["HPEESOF_DIR"] = ads.get_ads_location()
        util.safe_makedirs(target_workspace)

    netlists = glob.glob(os.path.join(netlist_directory, "*.log"))

    for netlist in netlists:
        netlist_data = ""
        with open(netlist, "r") as file:
            netlist_data = file.read()
        # Step 8:
        # Run Channel simulation using circuit simulator module with updated netlist
        print(f"Running Channel simulation for {netlist}...")
        dataset_name = Path(netlist).stem
        ads_circuitsim = ads.CircuitSimulator()
        ckt = circuit.Circuit(
            netlist_data, import_options=Bunch(extract_analyses=False)
        )
        ckt.AC.File = f'"{new_sio_location}"'
        ckt.output_dataset = f"{dataset_name}"
        ads_circuitsim.run_netlist(ckt.generate_netlist(), output_dir=target_workspace)

    # Step 9 : Plot measurement results
    print("====Plot Results====")
    file_path = os.path.join(target_workspace, "minipc_pm_ac_PI-AC_AC_decapoff.ds")
    results = pwdt.read_file(file_path)

    data = results.members[0].to_pandas_dataframe()
    config = dict({"scrollZoom": True})
    fig1 = px.line(data, x=data["freq"], y=data["Z[1,1]"].apply(np.abs))

    file_path = os.path.join(target_workspace, "minipc_pm_ac_PI-AC_AC_decapon.ds")
    results = pwdt.read_file(file_path)

    data = results.members[0].to_pandas_dataframe()
    config = dict({"scrollZoom": True})
    fig2 = px.line(data, x=data["freq"], y=data["Z[1,1]"].apply(np.abs))

    fig = make_subplots(
        rows=2,
        cols=1,
        subplot_titles=(
            "Magnitude of Z[1,1] versus Frequency for netliminipc_pm_ac_PI-AC_AC_decapoff",  # noqa: E501
            "Magnitude of Z[1,1] versus Frequency for netliminipc_pm_ac_PI-AC_AC_decapon",  # noqa: E501
        ),
    )
    fig.add_traces(fig1.data, rows=1, cols=1)
    fig.update_xaxes(
        title_text="Freq (Hz)",
        minor=dict(ticks="inside", ticklen=6, showgrid=True),
        type="log",
        row=1,
        col=1,
    )
    fig.update_yaxes(title_text="mag(Z)  [Ohm]", type="log", row=1, col=1)
    fig.add_traces(fig2.data, rows=2, cols=1)
    fig.update_xaxes(
        title_text="Freq (Hz)",
        minor=dict(ticks="inside", ticklen=6, showgrid=True),
        type="log",
        row=2,
        col=1,
    )
    fig.update_yaxes(title_text="mag(Z)  [Ohm]", type="log", row=2, col=1)
    fig.show(config=config)
    print("====Analysis Successfully Completed====")
```


---

<!-- === 来源: Examples/ex_odbpp_simulate_pipro_dc.md === -->

# Example odbpp simulate pipro dc[](#example-odbpp-simulate-pipro-dc "Link to this heading")

This example demonstrates how to import an ODB++ file and setup a PIPro DC simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2025 Keysight Technologies, Keysight Confidential
from argparse import ArgumentParser
import os
from pathlib import Path

from keysight.edatoolbox import ads, momentum, util, xxpro

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
    output_dir = Path(args.output_dir).absolute()
    util.safe_makedirs(args.output_dir)

    # Path to the ODB++ file
    odb_file = Path(__file__).parent / "data" / "Minipc" / "minipc_pm_v0_pm.zip"
    cell_name = "minipc_pm"
    lib_name = f"{cell_name}_lib"
    tech_lib_name = f"{cell_name}_tech_lib"
    component_lib_name = f"{cell_name}_component_lib"
    target_workspace_name = f"{cell_name}_wrk"
    target_workspace_path = output_dir / target_workspace_name
    target_workspace = str(target_workspace_path)

    assert odb_file.exists(), f"ODB++ file {odb_file} does not exist!"
    assert output_dir.exists(), f"Output directory {output_dir} does not exist!"
    assert not target_workspace_path.exists(), (
        f"Target workspace {target_workspace} already exists!"
    )

    print(f"Input ODB++: {odb_file}")
    print(f"Target workspace: {target_workspace}")

    # Step 1: Creating the ADS application object
    ads_application = ads.ADS()
    print("ADS application created")
    print("Creating workspace")
    if not target_workspace_path.exists():
        ads_application.create_workspace(output_dir, target_workspace_name)

    # Step 2: Import odb++ file

    print("Importing ODB++")
    ads_application.import_odbpp(
        target_workspace,
        odb_file,
        library=lib_name,
        cell=cell_name,
        use_legacy_importer=False,
    )
    print("ODB++ imported")

    # update the material database
    matdb_path = str(target_workspace_path / tech_lib_name / "materials.matdb")
    matdb = ads.MaterialDatabase(matdb_path)
    for diel in matdb.dielectrics:
        eps_r = float(diel.er_real)
        if eps_r <= 0.0:
            diel.er_real = 4.0
    matdb.write(matdb_path)

    # update the thickness of metal layers
    subst_path = str(target_workspace_path / tech_lib_name / f"{cell_name}.subst")
    substrate_info = ads.SubstrateModel(subst_path)
    for layer in substrate_info.layers:
        if layer.layer == 1033:
            layer.thick = -1.761411  # negative thickness : below interface
        if layer.index == 8:
            layer.thick = 0.6654142

    # update the thickness of dielectric layers
    for material in substrate_info.materials:
        if material.index == 1:
            material.thick = 3.01

    substrate_info.write(subst_path)

    input_lcv = ads.LibraryCellView(library=lib_name, cell=cell_name, view="layout")
    pro_lcv = ads.LibraryCellView(library=lib_name, cell=cell_name, view="sipi1")

    # Step 3: Creating the SIPro view
    print("Creating PIPro simulation view")
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate=cell_name,
        pro_lcv=pro_lcv,
        tool="sipi",
        substrate_library=tech_lib_name,
    )
    print("PIPro simulation view created")

    momentum_dir = momentum.get_momentum_location()
    empro.toolkit.analysis.setMomentumDir(momentum_dir)
    with util.remember_cwd():
        os.environ["HPEESOF_DIR"] = (
            ads.get_ads_location()
        )  # ensure the referenced env vars in lib.defs can be found

        # Step 4: Loading the SIPro view into the SIPro tool
        xxpro.use_workspace(target_workspace)
        xxpro.load_pro_view(pro_lcv)
        empro.activeProject.saveActiveProject()

        # Step 5 : ==== Script generated by ADS Window starts here =====
        # Create an Analysis
        analysis = empro.analysis.Analysis()
        analysis.name = "DC by Script"
        analysis.analysisType = empro.analysis.Analysis.DCAnalysisType

        # Set VRM List
        vrmList = analysis.vrms

        plusPins = ["Q4.1", "Q4.2", "Q4.3"]
        minusPins = ["C3.1", "Q6.2"]
        vrm = empro.toolkit.analysis.createVrmFromPins(plusPins, minusPins)
        vrm.name = "PLL_1V8_Q4"
        vrm.resistance = empro.core.Expression("0 Ohm")
        vrm.tolerance = empro.core.Expression("0.01")
        vrm.outputVoltagePositiveVariation = empro.core.Expression("0.00")
        vrm.outputVoltageNegativeVariation = empro.core.Expression("0.00")
        vrm.inductance = empro.core.Expression("0 mH")
        vrm.voltage = empro.core.Expression("1.5 V")
        vrm.sourceType = "PackagedVrm"
        vrm.hasSenseLine = False
        vrmList.append(vrm)

        # Set Sink List
        sinkList = analysis.sinks

        plusPins = [
            "U1.AB14",
            "U1.AC14",
            "U1.AC16",
            "U1.AC17",
            "U1.AC19",
            "U1.AC21",
            "U1.AD27",
            "U1.AE18",
            "U1.AH27",
            "U1.AM27",
            "U1.D27",
            "U1.H27",
            "U1.M27",
            "U1.T27",
            "U1.U15",
            "U1.U16",
            "U1.U17",
            "U1.U20",
            "U1.U21",
            "U1.U22",
            "U1.W19",
            "U1.Y27",
        ]
        minusPins = [
            "U1.A6",
            "U1.A11",
            "U1.A16",
            "U1.A21",
            "U1.A27",
            "U1.A29",
            "U1.A30",
            "U1.A31",
            "U1.A34",
            "U1.A35",
            "U1.A38",
            "U1.AA1",
            "U1.AA11",
            "U1.AA17",
            "U1.AA21",
            "U1.AA26",
            "U1.AA27",
            "U1.AA28",
            "U1.AA29",
            "U1.AA30",
            "U1.AA31",
            "U1.AA34",
            "U1.AA35",
            "U1.AA38",
            "U1.AA39",
            "U1.AB3",
            "U1.AB8",
            "U1.AB13",
            "U1.AB18",
            "U1.AB23",
            "U1.AB26",
            "U1.AB27",
            "U1.AB32",
            "U1.AB33",
            "U1.AB36",
            "U1.AB37",
            "U1.AC10",
            "U1.AC15",
            "U1.AC20",
            "U1.AC22",
            "U1.AC25",
            "U1.AC27",
            "U1.AC28",
            "U1.AC29",
            "U1.AC30",
            "U1.AC31",
            "U1.AC34",
            "U1.AC35",
            "U1.AC38",
            "U1.AC39",
            "U1.AD2",
            "U1.AD12",
            "U1.AD26",
            "U1.AD32",
            "U1.AD33",
            "U1.AD36",
            "U1.AD37",
            "U1.AE4",
            "U1.AE9",
            "U1.AE19",
            "U1.AE24",
            "U1.AE26",
            "U1.AE27",
            "U1.AE30",
            "U1.AE31",
            "U1.AE34",
            "U1.AE35",
            "U1.AE38",
            "U1.AE39",
            "U1.AF1",
            "U1.AF6",
            "U1.AF11",
            "U1.AF16",
            "U1.AF26",
            "U1.AF27",
            "U1.AF30",
            "U1.AF31",
            "U1.AF32",
            "U1.AF33",
            "U1.AF34",
            "U1.AF35",
            "U1.AF36",
            "U1.AF37",
            "U1.AG3",
            "U1.AG13",
            "U1.AG18",
            "U1.AG23",
            "U1.AG26",
            "U1.AG27",
            "U1.AG30",
            "U1.AG31",
            "U1.AG34",
            "U1.AG35",
            "U1.AG38",
            "U1.AG39",
            "U1.AH10",
            "U1.AH15",
            "U1.AH20",
            "U1.AH26",
            "U1.AH32",
            "U1.AH33",
            "U1.AH36",
            "U1.AH37",
            "U1.AJ2",
            "U1.AJ7",
            "U1.AJ12",
            "U1.AJ17",
            "U1.AJ22",
            "U1.AJ27",
            "U1.AJ28",
            "U1.AJ29",
            "U1.AJ30",
            "U1.AJ31",
            "U1.AJ34",
            "U1.AJ35",
            "U1.AJ38",
            "U1.AJ39",
            "U1.AK4",
            "U1.AK27",
            "U1.AK32",
            "U1.AK33",
            "U1.AK36",
            "U1.AK37",
            "U1.AL1",
            "U1.AL16",
            "U1.AL27",
            "U1.AL30",
            "U1.AL31",
            "U1.AL34",
            "U1.AL35",
            "U1.AL38",
            "U1.AL39",
            "U1.AM3",
            "U1.AM15",
            "U1.AM23",
            "U1.AM26",
            "U1.AM32",
            "U1.AM33",
            "U1.AM36",
            "U1.AM37",
            "U1.AN5",
            "U1.AN10",
            "U1.AN15",
            "U1.AN20",
            "U1.AN27",
            "U1.AN30",
            "U1.AN31",
            "U1.AN34",
            "U1.AN35",
            "U1.AN38",
            "U1.AN39",
            "U1.AP2",
            "U1.AP7",
            "U1.AP12",
            "U1.AP14",
            "U1.AP27",
            "U1.AP32",
            "U1.AP33",
            "U1.AP36",
            "U1.AP37",
            "U1.AR4",
            "U1.AR9",
            "U1.AR14",
            "U1.AR15",
            "U1.AR19",
            "U1.AR27",
            "U1.AR30",
            "U1.AR31",
            "U1.AR34",
            "U1.AR35",
            "U1.AR38",
            "U1.AR39",
            "U1.AT1",
            "U1.AT6",
            "U1.AT11",
            "U1.AT16",
            "U1.AT27",
            "U1.AT28",
            "U1.AT29",
            "U1.AT32",
            "U1.AT33",
            "U1.AT36",
            "U1.AT37",
            "U1.AU3",
            "U1.AU8",
            "U1.AU13",
            "U1.AU18",
            "U1.AU23",
            "U1.AU29",
            "U1.AU30",
            "U1.AU31",
            "U1.AU34",
            "U1.AU35",
            "U1.AU38",
            "U1.AU39",
            "U1.AV5",
            "U1.AV10",
            "U1.AV15",
            "U1.AV20",
            "U1.AV25",
            "U1.AV31",
            "U1.AV32",
            "U1.AV33",
            "U1.AV36",
            "U1.AV37",
            "U1.AW7",
            "U1.AW12",
            "U1.AW17",
            "U1.AW22",
            "U1.AW27",
            "U1.AW29",
            "U1.AW31",
            "U1.AW34",
            "U1.AW35",
            "U1.AW38",
            "U1.B2",
            "U1.B3",
            "U1.B8",
            "U1.B13",
            "U1.B17",
            "U1.B18",
            "U1.B23",
            "U1.B25",
            "U1.B27",
            "U1.B28",
            "U1.B29",
            "U1.B32",
            "U1.B33",
            "U1.B36",
            "U1.B37",
            "U1.C5",
            "U1.C10",
            "U1.C15",
            "U1.C20",
            "U1.C27",
            "U1.C28",
            "U1.C29",
            "U1.C30",
            "U1.C31",
            "U1.C34",
            "U1.C35",
            "U1.C38",
            "U1.C39",
            "U1.D2",
            "U1.D7",
            "U1.D12",
            "U1.D15",
            "U1.D17",
            "U1.D22",
            "U1.D26",
            "U1.D30",
            "U1.D31",
            "U1.D32",
            "U1.D33",
            "U1.D36",
            "U1.D37",
            "U1.E4",
            "U1.E9",
            "U1.E14",
            "U1.E19",
            "U1.E27",
            "U1.E30",
            "U1.E31",
            "U1.E32",
            "U1.E33",
            "U1.E34",
            "U1.E35",
            "U1.E38",
            "U1.E39",
            "U1.F1",
            "U1.F6",
            "U1.F11",
            "U1.F16",
            "U1.F21",
            "U1.F27",
            "U1.F30",
            "U1.F31",
            "U1.F32",
            "U1.F33",
            "U1.F36",
            "U1.F37",
            "U1.G3",
            "U1.G18",
            "U1.G23",
            "U1.G27",
            "U1.G30",
            "U1.G31",
            "U1.G32",
            "U1.G33",
            "U1.G34",
            "U1.G35",
            "U1.G38",
            "U1.G39",
            "U1.H5",
            "U1.H10",
            "U1.H15",
            "U1.H26",
            "U1.H30",
            "U1.H31",
            "U1.H32",
            "U1.H33",
            "U1.H36",
            "U1.H37",
            "U1.J2",
            "U1.J7",
            "U1.J17",
            "U1.J27",
            "U1.J30",
            "U1.J31",
            "U1.J32",
            "U1.J33",
            "U1.J34",
            "U1.J35",
            "U1.J38",
            "U1.J39",
            "U1.K27",
            "U1.K32",
            "U1.K33",
            "U1.K36",
            "U1.K37",
            "U1.L1",
            "U1.L16",
            "U1.L21",
            "U1.L27",
            "U1.L30",
            "U1.L31",
            "U1.L34",
            "U1.L35",
            "U1.L38",
            "U1.L39",
            "U1.M3",
            "U1.M13",
            "U1.M18",
            "U1.M23",
            "U1.M26",
            "U1.M32",
            "U1.M33",
            "U1.M36",
            "U1.M37",
            "U1.N5",
            "U1.N10",
            "U1.N15",
            "U1.N21",
            "U1.N26",
            "U1.N27",
            "U1.N30",
            "U1.N31",
            "U1.N34",
            "U1.N35",
            "U1.N38",
            "U1.N39",
            "U1.P2",
            "U1.P7",
            "U1.P12",
            "U1.P17",
            "U1.P26",
            "U1.P27",
            "U1.P32",
            "U1.P33",
            "U1.P36",
            "U1.P37",
            "U1.R9",
            "U1.R19",
            "U1.R24",
            "U1.R26",
            "U1.R27",
            "U1.R30",
            "U1.R31",
            "U1.R34",
            "U1.R35",
            "U1.R38",
            "U1.R39",
            "U1.T1",
            "U1.T11",
            "U1.T16",
            "U1.T21",
            "U1.T26",
            "U1.T32",
            "U1.T33",
            "U1.T36",
            "U1.T37",
            "U1.U3",
            "U1.U8",
            "U1.U13",
            "U1.U18",
            "U1.U23",
            "U1.U27",
            "U1.U30",
            "U1.U31",
            "U1.U34",
            "U1.U35",
            "U1.U38",
            "U1.U39",
            "U1.V10",
            "U1.V15",
            "U1.V20",
            "U1.V25",
            "U1.V26",
            "U1.V27",
            "U1.V32",
            "U1.V33",
            "U1.V36",
            "U1.V37",
            "U1.W2",
            "U1.W7",
            "U1.W12",
            "U1.W17",
            "U1.W22",
            "U1.W26",
            "U1.W27",
            "U1.W30",
            "U1.W31",
            "U1.W34",
            "U1.W35",
            "U1.W38",
            "U1.W39",
            "U1.Y9",
            "U1.Y15",
            "U1.Y19",
            "U1.Y24",
            "U1.Y26",
            "U1.Y32",
            "U1.Y33",
            "U1.Y36",
            "U1.Y37",
        ]
        sink = empro.toolkit.analysis.createSinkFromPins(plusPins, minusPins)
        sink.name = "PLL_1V8_U1"
        sink.resistance = empro.core.Expression("1 MOhm")
        sink.positiveTolerance = empro.core.Expression("0.05")
        sink.negativeTolerance = empro.core.Expression("0.05")
        sink.current = empro.core.Expression("3 A")
        sink.pinCurrentModel = "EqualVoltage"

        sink.packageModel = None
        sinkList.append(sink)

        # Set Netlist
        netList = analysis.nets

        net = empro.analysis.Net("GND", empro.activeProject.geometry[0])
        netList.append(net)

        net = empro.analysis.Net("PLL_1V8", empro.activeProject.geometry[0])
        netList.append(net)

        # Set Component Model Group List
        componentModelGroupList = analysis.componentModelGroups

        # Create Component Model Group
        componentModelGroup = empro.analysis.ComponentModelGroup(
            f"{component_lib_name}:grm033r60j104ke19d_capc0603x33x15ll03t05",
            empro.activeProject.geometry[0],
        )
        componentModelGroup.name = "grm033r60j104ke19d_capc0603x33x15ll03t05"
        componentModelGroup.arrayedComponent = False
        componentModelGroup.updateableAfterSimulation = True
        pinNamePortNumberPairs = (("1", -1), ("2", 1))
        pinPortMap = componentModelGroup.pinPortMap()
        pinPortMap.update(pinNamePortNumberPairs)
        instances = [
            "C424",
            "C425",
            "C426",
            "C427",
            "C428",
            "C429",
            "C430",
            "C431",
            "C432",
            "C433",
            "C434",
            "C435",
            "C436",
            "C437",
            "C438",
            "C439",
            "C440",
            "C441",
            "C442",
            "C443",
            "C444",
        ]
        for instance in instances:
            componentModelGroup.appendInstance(
                empro.toolkit.analysis.createComponentInstanceFromInstance(instance)
            )

        # Create Component Model
        componentModel = empro.analysis.ComponentModel(
            1, ""
        )  # LumpedType = 1, ModelDBType = 2, SnPType = 3, LibCell = 4
        componentModel.name = "model"
        componentModel.getPassiveLoad().impedance.resistance = empro.core.Expression(
            "0 Ohm"
        )
        componentModel.getPassiveLoad().impedance.capacitance = empro.core.Expression(
            "0.1 uF"
        )
        componentModel.getPassiveLoad().impedance.inductance = empro.core.Expression(
            "0 H"
        )
        componentModel.getPassiveLoad().impedance.elementArrangement = "Series"
        componentModelGroup.appendModel(componentModel)
        componentModelGroupList.append(componentModelGroup)

        # Create Component Model Group
        componentModelGroup = empro.analysis.ComponentModelGroup(
            f"{component_lib_name}:grm31cr60j107me39l_capc3216x190x55ml30t25",
            empro.activeProject.geometry[0],
        )
        componentModelGroup.name = "grm31cr60j107me39l_capc3216x190x55ml30t25"
        componentModelGroup.arrayedComponent = False
        componentModelGroup.updateableAfterSimulation = True
        pinNamePortNumberPairs = (("1", -1), ("2", 1))
        pinPortMap = componentModelGroup.pinPortMap()
        pinPortMap.update(pinNamePortNumberPairs)
        instances = ["C423"]
        for instance in instances:
            componentModelGroup.appendInstance(
                empro.toolkit.analysis.createComponentInstanceFromInstance(instance)
            )

        # Create Component Model
        componentModel = empro.analysis.ComponentModel(
            1, ""
        )  # LumpedType = 1, ModelDBType = 2, SnPType = 3, LibCell = 4
        componentModel.name = "model"
        componentModel.getPassiveLoad().impedance.resistance = empro.core.Expression(
            "0 Ohm"
        )
        componentModel.getPassiveLoad().impedance.capacitance = empro.core.Expression(
            "100 uF"
        )
        componentModel.getPassiveLoad().impedance.inductance = empro.core.Expression(
            "0 H"
        )
        componentModel.getPassiveLoad().impedance.elementArrangement = "Series"
        componentModelGroup.appendModel(componentModel)
        componentModelGroupList.append(componentModelGroup)

        # Set Analysis Options
        options = analysis.simulationSettings

        # Set Ambient Conditions
        options.ambientConditions.backgroundTemperature = empro.core.Expression(298.15)

        # Set Frequency Plans

        # Set Frequency Plan List
        frequencyPlanList = options.femFrequencyPlanList()
        frequencyPlanList.clear()

        plan = empro.simulation.FrequencyPlan()
        plan.type = "Adaptive"
        plan.startFrequency = empro.core.Expression("10 kHz")
        plan.stopFrequency = empro.core.Expression("300 MHz")
        plan.numberOfFrequencyPoints = 300
        plan.samplePointsLimit = 300
        plan.pointsPerDecade = 5
        plan.enabled = True
        frequencyPlanList.append(plan)

        # Set Field Storage
        options.saveFieldsFor = "NoFrequencies"
        options.farFieldEnabled = False
        options.farFieldAngularResolution = empro.core.Expression("5 deg")

        # Set Simulator

        # Set Preset Simulator Setup By Name
        options.preset = None

        # Set User-Defined Advanced Simulator Setup

        # Set FEM Options

        # Set FEM Matrix Solver
        options.femMatrixSolver.solverType = "MatrixSolverAuto"

        # Set FEM Mesh Settings
        femMeshSettings = options.femMeshSettings
        femMeshSettings.includeResistiveLossesInGround = False
        femMeshSettings.orderOfBasisFunctions = 1
        femMeshSettings.useTargetMeshSize = False
        femMeshSettings.autoTargetMeshSize = False
        femMeshSettings.targetMeshSize = empro.core.Expression("2 mm")
        femMeshSettings.useMeshDomainOptimization = False
        femMeshSettings.minimumNumberOfPasses = 1
        femMeshSettings.maximumNumberOfPasses = 1
        femMeshSettings.refineAtSpecificFrequency = False
        femMeshSettings.refinementFrequency = empro.core.Expression("10 GHz")

        # Set Resources Settings
        resourceSettings = empro.simulation.LocalResourceSettings()
        resourceSettings.numberOfWorkers = 1
        resourceSettings.numberOfThreads = 0
        options.resourceSettings = resourceSettings

        # Set ParameterSweep
        options.parameterSweepEnabled = False
        options.parameterSequences.clear()

        # Add the Analysis to the list of Analyses
        empro.activeProject.analyses.append(analysis)

        # ===== Script generated by ADS Window Ends here ======
        # take the latest analysis
        active_analysis = empro.activeProject.analyses[-1]

        # Step 6: Run Analysis for the nets added in SIPro
        print("Running and waiting for simulation...")
        empro.toolkit.analysis.runAnalysis(
            active_analysis, waitForConfirmation=False, saveProject=True
        )
        empro.activeProject.simulations.isQueueHeld = False
        active_simulation = empro.activeProject.simulations[-1]
        empro.toolkit.simulation.wait(active_simulation)
        new_sio_location = os.path.join(
            active_simulation.simulationPath(), "emds_dsn", "design", "design.sio"
        )
        empro.activeProject.saveActiveProject()

        print("Simulation complete, IR drop per sink:")
        dc_result = DCResult(active_analysis)

        for sink in dc_result.sinks:
            irDrop = sink.vrmOutputVoltage - sink.inputVoltage
            print(f"{sink.name}: {irDrop * 1000:2.2f} mV")

        if ads_application.version >= 591:  # >= ADS 2024
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
    print("====Analysis Successfully Completed====")
```


---

<!-- === 来源: Examples/ex_odbpp_simulate_rfpro.md === -->

# Example odbpp simulate rfpro[](#example-odbpp-simulate-rfpro "Link to this heading")

This example demonstrates how to how to import an ODB++ file and setup and run an RFPro simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2025 Keysight Technologies, Keysight Confidential
# ruff: noqa: D100
from argparse import ArgumentParser
import os
from pathlib import Path

from keysight.edatoolbox import ads, util, xxpro

try:
    import empro
    from empro.geometry import Vector3d
    import empro.toolkit
    import empro.toolkit.analysis
except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using the Python"
        " from EMPro. Use it by launching emproenv.bat/.sh"
    )
    raise

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--output-dir",
        action="store",
        default=None,
        help="Location where the workspace will be created",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir).absolute()
    util.safe_makedirs(args.output_dir)
    tgz_file = Path(__file__).parent / "data" / "line_via_stub.tgz"
    target_workspace_name = "line_via_stub_wrk"
    target_workspace_path = output_dir / target_workspace_name
    target_workspace = str(target_workspace_path)

    cell_name = "line_via_stub"
    library_name = f"{cell_name}_lib"

    assert output_dir.exists(), f"Output directory {output_dir} does not exist!"
    assert tgz_file.exists(), f"Input ODB++ file {tgz_file} does not exist!"
    assert not target_workspace_path.exists(), (
        f"Target workspace {target_workspace} already exists!"
    )

    print(f"Input ODB++: {tgz_file}")
    print(f"Target workspace: {target_workspace}")

    ads_application = ads.ADS()
    print("ADS application created")

    print("Creating workspace")
    if not os.path.exists(target_workspace):
        ads_application.create_workspace(output_dir, target_workspace_name)

    print("Importing ODB++")

    odbpp_import_options = ads.OdbImportOptions()
    odbpp_import_options.separate_component_lib = False
    odbpp_import_options.separate_tech_lib = False

    ads_application.import_odbpp(
        target_workspace,
        tgz_file,
        library=library_name,
        cell=cell_name,
        use_legacy_importer=False,
        import_options=odbpp_import_options,
    )

    print("ODB++ imported")

    # update the material database
    matdb_path = str(target_workspace_path / library_name / "materials.matdb")
    matdb = ads.MaterialDatabase(matdb_path)
    for diel in matdb.dielectrics:
        if diel.er_real <= 0.0:
            diel.er_real = 4.0
    matdb.write(matdb_path)

    # update the thickness of metal layers
    subst_path = str(target_workspace_path / library_name / "tech.subst")
    substrate_info = ads.SubstrateModel(subst_path)
    for layer in substrate_info.layers:
        if layer.layer == 1023:
            layer.thick = -1.39188  # negative thickness : below interface
        if layer.index == 6:
            layer.thick = 1.371

    # update the thickness of dielectric layers
    for material in substrate_info.materials:
        if material.index == 1:
            material.thick = 12.051

    substrate_info.write(subst_path)
    input_lcv = ads.LibraryCellView(library=library_name, cell=cell_name, view="layout")
    pro_lcv = ads.LibraryCellView(
        library=library_name, cell=cell_name, view="rfproSetup"
    )

    print("Creating xxPro simulation view")
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate="tech",
        pro_lcv=pro_lcv,
        tool="rfpro",
    )
    print("xxPro simulation view created")

    with util.remember_cwd():
        os.environ["HPEESOF_DIR"] = (
            ads.get_ads_location()
        )  # ensure the referenced env vars in lib.defs can be found
        xxpro.use_workspace(target_workspace)

        # To load existing project instead of creating a new one
        # res = empro.activeProject.loadActiveProjectFrom(library_name, cell_name,
        #   "rfproSetup")

        # at this stage the view is still completely empty
        # we still need to load the requested layouts in it
        xxpro.load_pro_view(pro_lcv)

        # create an analysis
        with empro.activeProject as project:
            # Change the roles of the components once the view is loaded
            for component in empro.activeProject.layout.components:
                component.cellRole = empro.geometry.Component.CIRCUIT
            empro.activeProject.layout.reExtractNets()
            empro.activeProject.saveActiveProject()

            layout = empro.activeProject.layout
            component_side = layout.layers["component_side (1004)"]
            gnd_layer = layout.layers["ground_plane (1005)"]

            # add a reference pin on the ground layer
            ref_gnd_pin = layout.addReferencePin("ref_gnd_pin", gnd_layer)

            # locate the positive pins and add pins
            vpin1 = layout.addVirtualPin(
                "vpin1",
                Vector3d("2377.51 mil", "3038.88 mil", 0),
                component_side,
                layout.ZPositionOnLayer.TOP,
            )
            vpin2 = layout.addVirtualPin(
                "vpin2",
                Vector3d("3120.36 mil", "3040.82 mil", 0),
                component_side,
                layout.ZPositionOnLayer.TOP,
            )

            # setup the analysis given the pins, use the user-defined analysis
            # although it will give the entire design to simulate
            analysis = empro.analysis.Analysis(
                empro.analysis.Analysis.EMUDAnalysisType, "Analysis"
            )

            # Set PortList
            portDefinitions = [
                (vpin1, ref_gnd_pin),
                (vpin2, ref_gnd_pin),
            ]

            for portIdx, portDef in enumerate(portDefinitions):
                plusPin, minusPin = portDef
                analysis.ports.append(
                    empro.analysis.Port([plusPin], [minusPin], f"port{portIdx + 1}")
                )

            analysis.nets.append(layout.nets["DRV_N"])
            analysis.nets.append(layout.nets["GND"])

            options = analysis.simulationSettings
            frequencyPlanList = options.femFrequencyPlanList()
            frequencyPlanList.clear()

            plan = empro.simulation.FrequencyPlan()
            plan.type = "Linear"
            plan.startFrequency = "0 Hz"
            plan.stopFrequency = "1 GHz"
            plan.numberOfFrequencyPoints = 11
            frequencyPlanList.append(plan)

            # Set Field Storage
            options.saveFieldsFor = "NoFrequencies"
            options.farFieldEnabled = False
            options.setPresetByName("FEM")

            femMeshSettings = options.femMeshSettings
            femMeshSettings.generation = "Generation2"
            femMeshSettings.autoConductorMeshing = True
            femMeshSettings.maximumNumberOfPasses = 1
            empro.activeProject.analyses.append(analysis)

        empro.activeProject.saveActiveProject()
        active_analysis = empro.activeProject.analyses[-1]

        empro.toolkit.analysis.runAnalysis(
            active_analysis, waitForConfirmation=False, saveProject=True
        )
        print("Running and waiting for simulation...")
        empro.activeProject.simulations.isQueueHeld = False
        sim_from_list = empro.activeProject.simulations[-1]
        empro.toolkit.simulation.wait(sim_from_list)

        print("Extracting results")
        result = empro.analysis.CircuitResults(active_analysis)
        delay12 = result.delay(0, 1)

        nr_results = len(delay12)
        freq_dimension = delay12.dimension(0)
        frequencies = [freq_dimension.at(idx) for idx in range(nr_results)]
        delay_values = [delay12.at(idx) for idx in range(nr_results)]
        delays = list(zip(frequencies, delay_values, strict=False))
        frequency, delay_at_1GHz = delays[-1]
        print(f"Delay at 1 GHz={delay_at_1GHz}")
```


---

<!-- === 来源: Examples/ex_optimize_matching_network.md === -->

# Example optimize matching network[](#example-optimize-matching-network "Link to this heading")

This example demonstrates how to optimize a matching network by varying the L and C parameters of the matching circuit.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc , Keysight Confidential
#
from argparse import ArgumentParser
import math
import os

# SciPy and NumPy should be installed separately
import numpy as np
from scipy import optimize

from keysight.edatoolbox import ads, circuit, dataset, util

# Global counter to track output directories, convenient for debugging
optimization_iteration = 0

def lc_resonance(
    l_value,
    c_value,
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
    matching_network.L.value = f"{l_value * 1e9} nH"
    matching_network.C.value = f"{c_value * 1e12} pF"

    global optimization_iteration
    optimization_iteration += 1
    if iterate_output_dirs:
        output_dir_name = f"output_{optimization_iteration}"
    else:
        output_dir_name = "output"

    output_dir = os.path.join(workdir_path, output_dir_name)
    util.safe_makedirs(output_dir)

    ads_circuitsim.run_netlist(
        matching_network.generate_netlist(),
        output_dir=output_dir,
        rel_data_dir=workspace_path,
    )
    ds_dump = ads.DSDump()
    ds_dump.dump_ds(os.path.join(output_dir, "matching.ds"))
    ds = dataset.Dataset(os.path.join(output_dir, "matching.ds"))
    freqs = ds.values("SP1.SP", "freq")
    s11 = [abs(x[1]) for x in ds.values("SP1.SP", "S[1,1]")]
    mag_s11, frequency = min(zip(s11, freqs))

    return mag_s11, frequency

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
    input_workspace_file = os.path.abspath("data/simple_matching_wrk.7zads")
    target_workspace = os.path.join(target_workspace_dir, "simple_matching_wrk")

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
    ads_circuitsim = ads.CircuitSimulator()
    ads_application.unarchive_workspace(input_workspace_file, target_workspace_dir)
    print("ADS workspace created")

    # Allow to incrementally generate output dirs,
    # otherwise the  1st output directory is recycled
    iterate_output_dirs = True
    netlist = ads_application.generate_netlist(
        target_workspace,
        ads.LibraryCellView(
            library="simple_matching_lib", cell="matching", view="schematic"
        ),
    )
    print("Netlist extracted")

    matching_network = circuit.Circuit(netlist)

    def optimization_goal(x):
        """Optimize the reflection to be minimal at 2.4 GHz."""
        l_value = x[0]
        c_value = x[1]
        _, resonance = lc_resonance(
            l_value,
            c_value,
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
        x0=np.array([2e-9, 0.6e-12]),
        bounds=optimize.Bounds([2e-10, 0.6e-13], [2e-8, 0.6e-11]),
        method="nelder-mead",
        options={"disp": False},
    )

    l_value = result.x[0]
    c_value = result.x[1]

    print("Optimization converged")
    print(f"L = {l_value * 1e9} nH, C = {c_value * 1e12} pF")

    mag_s11, resonance = lc_resonance(
        l_value,
        c_value,
        matching_network=matching_network,
        workdir_path=target_workspace_dir,
        workspace_path=target_workspace,
        iterate_output_dirs=iterate_output_dirs,
    )

    print(f"Resonance={resonance * 1e-9} GHz, value={20.0 * math.log10(mag_s11)} dB")
    print("Optimization completed")
```


---

<!-- === 来源: Examples/ex_pipro_example_ac.md === -->

# Example pipro ac[](#example-pipro-ac "Link to this heading")

This example demonstrates how load an SIPro view and setup and run an PIPro AC simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
import os

from keysight.edatoolbox import ads, util, xxpro

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
            layout = empro.activeProject.layout

            # create an analysis
            analysis = empro.analysis.Analysis(
                empro.analysis.Analysis.ACAnalysisType, "Test"
            )

            ground_nets = ["GND"]
            power_nets = ["VDD"]
            vrm_definitions = [("J1", "1.2 V")]
            sink_definitions = [(f"U{index}", "0.1 A") for index in range(1, 20)]

            net_list = analysis.nets
            for net_name in ground_nets + power_nets:
                net_list.append(layout.nets[net_name])

            vrm_list = analysis.vrms
            for vrm_name, vrm_voltage in vrm_definitions:
                instance = layout.instances[vrm_name]
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
                instance = layout.instances[sink_name]
                plus_pins = [
                    pin for pin in instance.pins() if pin.netName in power_nets
                ]
                minus_pins = [
                    pin for pin in instance.pins() if pin.netName in ground_nets
                ]
                sink = empro.analysis.Sink(plus_pins, minus_pins, sink_name)
                sink.current = sink_current
                sink_list.append(sink)

            component_model_group_list = analysis.componentModelGroups
            component_model_group = empro.analysis.ComponentModelGroup(
                layout.components[
                    "PC4-RDIMM_V090_RC_F0_20131106_lib:c_capacitors_0603-511-500044_4.7a_4.7uf"
                ]
            )
            instances = ["C106", "C14", "C16", "C28", "C74", "C79"]
            for instance_name in instances:
                component_model_group.appendInstance(
                    empro.analysis.ComponentInstance(layout.instances[instance_name])
                )
            component_model_group.appendModel(
                empro.analysis.ComponentModel(
                    empro.components.RLCSpecification(
                        "lumped", 0, 0, "4.7 uF", "Series"
                    )
                )
            )
            component_model_group_list.append(component_model_group)

            component_model_group = empro.analysis.ComponentModelGroup(
                layout.components[
                    "PC4-RDIMM_V090_RC_F0_20131106_lib:c_capacitors_0402-511-500201_4.7a_4.7uf"
                ]
            )
            instances = ["C116", "C117", "C118", "C119", "C120", "C121", "C122", "C123"]
            for instance_name in instances:
                component_model_group.appendInstance(
                    empro.analysis.ComponentInstance(layout.instances[instance_name])
                )
            component_model_group.appendModel(
                empro.analysis.ComponentModel(
                    empro.components.RLCSpecification(
                        "lumped", 0, 0, "4.7 uF", "Series"
                    )
                )
            )
            component_model_group_list.append(component_model_group)

            component_model_group = empro.analysis.ComponentModelGroup(
                layout.components[
                    "PC4-RDIMM_V090_RC_F0_20131106_lib:c_capacitors_0402-511-500048_1.0a_1.0uf"
                ]
            )
            instances = [
                "C100",
                "C102",
                "C104",
                "C105",
                "C107",
                "C108",
                "C109",
                "C110",
                "C111",
                "C24",
                "C31",
                "C33",
                "C35",
                "C37",
                "C42",
                "C44",
                "C46",
                "C54",
                "C60",
                "C63",
                "C66",
                "C68",
                "C70",
                "C75",
                "C76",
                "C77",
                "C78",
                "C81",
                "C83",
                "C85",
                "C87",
                "C91",
                "C95",
                "C96",
                "C97",
            ]
            for instance_name in instances:
                component_model_group.appendInstance(
                    empro.analysis.ComponentInstance(layout.instances[instance_name])
                )
            component_model_group.appendModel(
                empro.analysis.ComponentModel(
                    empro.components.RLCSpecification(
                        "lumped", 0, 0, "1.0 uF", "Series"
                    )
                )
            )
            component_model_group_list.append(component_model_group)

            frequency_plan_list = analysis.simulationSettings.femFrequencyPlanList()
            frequency_plan_list.clear()
            plan = empro.simulation.FrequencyPlan()
            plan.type = "Logarithmic"
            plan.startFrequency = empro.core.Expression("1 MHz")
            plan.stopFrequency = empro.core.Expression("100 MHz")
            plan.pointsPerDecade = 5
            plan.enabled = True
            frequency_plan_list.append(plan)

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

        res = empro.analysis.CircuitResults(active_analysis)
        freqs = list(res.frequencies())
        for i, sink in enumerate(active_analysis.sinks):
            impedance = res.Zrc(i + 1, i + 1, "ComplexMagnitude")
            min_impedance = min(list(impedance))
            freq = freqs[list(impedance).index(min_impedance)]
            print(
                f"{impedance.name} minimum impedance: {min_impedance} ohm, found at f: {freq} Hz"
            )
```


---

<!-- === 来源: Examples/ex_pipro_example_dc.md === -->

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


---

<!-- === 来源: Examples/ex_quantumpro_one_qubit_epr.md === -->

# Example quantumpro one qubit epr[](#example-quantumpro-one-qubit-epr "Link to this heading")

This example demonstrates how to load a QuantumPro view and setup and run an extraction of the Qubit parameters, like anharmonicity and quality factor.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2023 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
import os

from keysight.edatoolbox import ads, util, xxpro

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
    args = parser.parse_args()

    target_workspace_dir = args.output_dir
    util.safe_makedirs(target_workspace_dir)
    input_workspace_file = os.path.abspath("data/QuantumPro_Single_Qubit_wrk.7zads")
    target_workspace = os.path.join(target_workspace_dir, "Single_Qubit_Chip_wrk")

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
        library="Single_Qubit_Chip_lib",
        cell="Single_Qubit",
        view="layout",
    )
    pro_lcv = ads.LibraryCellView(
        library="Single_Qubit_Chip_lib",
        cell="Single_Qubit",
        view="quantumpro-setup",
    )
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate="tech",
        pro_lcv=pro_lcv,
        tool="quantumpro",
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

        analysisName = 'Energy Participation Analysis by Script'
        with empro.activeProject: # Create an Analysis
            for component in empro.activeProject.geometry[0]._componentList():
                if "Q_InductorAbstract" in component.cellName or "R_Space" in component.cellName:
                    component.cellRole = empro.geometry.Component.CIRCUIT
                else:
                    component.cellRole = empro.geometry.Component.SUBDESIGN
            empro.activeProject.layout.reExtractNets()
            empro.activeProject.saveActiveProject()

            # Create an Analysis
            analysis = empro.analysis.Analysis()
            analysis.name = analysisName
            analysis.analysisType = empro.analysis.Analysis.QEPAnalysisType

            # Set Netlist
            netList = analysis.nets

            net = empro.analysis.Net('P5', empro.activeProject.geometry[0])
            netList.append(net)

            net = empro.analysis.Net('P6', empro.activeProject.geometry[0])
            netList.append(net)

            # Set Component Model Group List
            componentModelGroupList = analysis.componentModelGroups

            # Create Component Model Group
            componentModelGroup = empro.analysis.ComponentModelGroup('ads_quantum:Q_InductorAbstract', empro.activeProject.geometry[0])
            componentModelGroup.name = 'Q_InductorAbstract'
            componentModelGroup.arrayedComponent = False
            componentModelGroup.updateableAfterSimulation = True
            pinNamePortNumberPairs = (('P1', 1), ('P2', -1))
            pinPortMap = componentModelGroup.pinPortMap()
            pinPortMap.update(pinNamePortNumberPairs)
            instances = ['L1']
            for instance in instances:
                componentModelGroup.appendInstance(empro.toolkit.analysis.createComponentInstanceFromInstance(instance))

            # Create Component Model
            componentModel = empro.analysis.ComponentModel(1, "") # LumpedType = 1, ModelDBType = 2, SnPType = 3, LibCell = 4
            componentModel.name = 'model'
            componentModel.getPassiveLoad().impedance.resistance=empro.core.Expression('0 Ohm')
            componentModel.getPassiveLoad().impedance.capacitance=empro.core.Expression('0 F')
            componentModel.getPassiveLoad().impedance.inductance=empro.core.Expression('11 nH')
            componentModel.getPassiveLoad().impedance.elementArrangement='Parallel'
            componentModelGroup.appendModel(componentModel)
            componentModelGroupList.append(componentModelGroup)

            # Set Analysis Options
            options = analysis.simulationSettings

            # Set Ambient Conditions
            options.ambientConditions.backgroundTemperature = empro.core.Expression(298.15)

            # Set Frequency Plans

            # Set Frequency Plan List
            frequencyPlanList = options.femFrequencyPlanList()
            frequencyPlanList.clear()

            # Set Field Storage
            options.saveFieldsFor = 'AllFrequencies'
            options.farFieldEnabled = False
            options.farFieldAngularResolution = empro.core.Expression('5 deg')

            # Set Simulator

            # Set Preset Simulator Setup By Name
            options.preset = None

            # Set User-Defined Advanced Simulator Setup

            # Set FEM Options

            # Set FEM Matrix Solver
            options.femMatrixSolver.solverType = 'MatrixSolverAuto'

            # Set FEM Eigen Solver Settings
            femEigenSolverSettings = options.femEigenSolverSettings
            femEigenSolverSettings.lowFreqLimit = empro.core.Expression('1 GHz')
            femEigenSolverSettings.highFreqLimit = empro.core.Expression('10 GHz')

            # Set FEM Mesh Settings
            femMeshSettings = options.femMeshSettings
            femMeshSettings.generation = 'Generation2'
            femMeshSettings.includeResistiveLossesInGround = True
            femMeshSettings.orderOfBasisFunctions = 2
            femMeshSettings.useTargetMeshSize = True
            femMeshSettings.autoTargetMeshSize = True
            femMeshSettings.targetMeshSize = empro.core.Expression('wavelength(maxFreq)/3.0')
            femMeshSettings.useMeshDomainOptimization = False
            femMeshSettings.generation = 'Generation2'
            femMeshSettings.minimumNumberOfPasses = 1
            femMeshSettings.maximumNumberOfPasses = 15
            femMeshSettings.refineAtSpecificFrequency = False
            femMeshSettings.refinementFrequency = empro.core.Expression('10 GHz')

            # Set FEM Per Layer Overrides
            femPerPartOverrides = options.femPerLayerOverrides

            override = femPerPartOverrides.add('cond (1)', 1)
            override.targetMeshSize = empro.core.Expression('5 um')

            # Set Resources Settings
            resourceSettings = empro.simulation.LocalResourceSettings()
            resourceSettings.numberOfWorkers = 1
            resourceSettings.numberOfThreads = 0
            options.resourceSettings = resourceSettings

            # Set ParameterSweep
            options.parameterSweepEnabled = False
            options.parameterSequences.clear()

            # Add the Analysis to the list of Analyses
            empro.activeProject.analyses.append(analysis)

        empro.activeProject.saveActiveProject()
        print("Running and waiting for simulation...")
        active_analysis = empro.activeProject.analyses[-1]
        empro.toolkit.analysis.runAnalysis(
            active_analysis, waitForConfirmation=False, saveProject=True
        )
        empro.activeProject.simulations.isQueueHeld = False
        active_simulation = empro.activeProject.simulations[-1]
        empro.toolkit.simulation.wait(active_simulation)
        empro.activeProject.saveActiveProject()

        #Extract parameters
        analysis = empro.activeProject.analyses[analysisName]
        params = empro.analysis.QubitParameters(analysis)

        print("Results:")
        results = params.getResults()
        chi = results.chiMatrix
        rabi = results.rabiMatrix

        for qubit in results.qubits:
            print(qubit.name)
            print(f"Frequency: {qubit.frequency}")
            print(f"Inductance: {qubit.inductance}")
            print(f"Anharmonicity: {qubit.anharmonicity}")
            print(f"Quality Factor: {qubit.qualityFactor}")
            print(f"T1: {qubit.t1}")
            print()

        for resonator in results.resonators:
            print(resonator.name)
            print(f"Frequency: {resonator.frequency}")
            print(f"Anharmonicity: {resonator.anharmonicity}")
            print(f"Quality Factor: {resonator.qualityFactor}")
            print(f"T1: {resonator.t1}")
            print()

        print("Chi Matrix:")
        print(chi.values)
        print()
```


---

<!-- === 来源: Examples/ex_quantumpro_one_qubit_freq.md === -->

# Example quantumpro one qubit freq[](#example-quantumpro-one-qubit-freq "Link to this heading")

This example demonstrates how load an QuantumPro view and setup and run an extraction of the Qubit parameters, like anharmonicity and quality factor per frequency.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2023 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
import os

from keysight.edatoolbox import ads, util, xxpro

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
    args = parser.parse_args()

    target_workspace_dir = args.output_dir
    util.safe_makedirs(target_workspace_dir)
    input_workspace_file = os.path.abspath("data/QuantumPro_Single_Qubit_wrk.7zads")
    target_workspace = os.path.join(target_workspace_dir, "Single_Qubit_Chip_wrk")

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
        library="Single_Qubit_Chip_lib",
        cell="Single_Qubit",
        view="layout",
    )
    pro_lcv = ads.LibraryCellView(
        library="Single_Qubit_Chip_lib",
        cell="Single_Qubit",
        view="quantumpro-setup",
    )
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate="tech",
        pro_lcv=pro_lcv,
        tool="quantumpro",
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

        analysisName = 'Full EM Analysis by Script'
        with empro.activeProject: # Create an Analysis
            for component in empro.activeProject.geometry[0]._componentList():
                if "Q_InductorAbstract" in component.cellName or "R_Space" in component.cellName:
                    component.cellRole = empro.geometry.Component.CIRCUIT
                else:
                    component.cellRole = empro.geometry.Component.SUBDESIGN
            empro.activeProject.layout.reExtractNets()
            empro.activeProject.saveActiveProject()

            # Create an Analysis
            analysis = empro.analysis.Analysis()
            analysis.name = analysisName
            analysis.analysisType = empro.analysis.Analysis.EMFUAnalysisType

            # Set PortList
            portList = analysis.ports

            plusPins = ['P2']
            minusPins = ['GND']
            port = empro.toolkit.analysis.createPortFromPins(plusPins,minusPins)
            port.name = 'P2'
            port.referenceImpedance = empro.core.Expression(50.0)
            port.feedType = 'Auto'
            portList.append(port)

            plusPins = ['P4']
            minusPins = ['P3']
            port = empro.toolkit.analysis.createPortFromPins(plusPins,minusPins)
            port.name = 'P4'
            port.referenceImpedance = empro.core.Expression(50.0)
            port.feedType = 'Auto'
            portList.append(port)

            # Set Netlist
            netList = analysis.nets

            net = empro.analysis.Net('GND', empro.activeProject.geometry[0])
            netList.append(net)

            net = empro.analysis.Net('P2', empro.activeProject.geometry[0])
            netList.append(net)

            net = empro.analysis.Net('P4', empro.activeProject.geometry[0])
            netList.append(net)

            net = empro.analysis.Net('P5', empro.activeProject.geometry[0])
            netList.append(net)

            net = empro.analysis.Net('P6', empro.activeProject.geometry[0])
            netList.append(net)

            # Set Component Model Group List
            componentModelGroupList = analysis.componentModelGroups

            # Create Component Model Group
            componentModelGroup = empro.analysis.ComponentModelGroup('ads_quantum:Q_InductorAbstract', empro.activeProject.geometry[0])
            componentModelGroup.name = 'Q_InductorAbstract'
            componentModelGroup.arrayedComponent = False
            componentModelGroup.updateableAfterSimulation = True
            pinNamePortNumberPairs = (('P1', 1), ('P2', -1))
            pinPortMap = componentModelGroup.pinPortMap()
            pinPortMap.update(pinNamePortNumberPairs)
            instances = ['L1']
            for instance in instances:
                componentModelGroup.appendInstance(empro.toolkit.analysis.createComponentInstanceFromInstance(instance))

            # Create Component Model
            componentModel = empro.analysis.ComponentModel(1, "") # LumpedType = 1, ModelDBType = 2, SnPType = 3, LibCell = 4
            componentModel.name = 'model'
            componentModel.getPassiveLoad().impedance.resistance=empro.core.Expression('0 Ohm')
            componentModel.getPassiveLoad().impedance.capacitance=empro.core.Expression('0 F')
            componentModel.getPassiveLoad().impedance.inductance=empro.core.Expression('11 nH')
            componentModel.getPassiveLoad().impedance.elementArrangement='Parallel'
            componentModelGroup.appendModel(componentModel)
            componentModelGroupList.append(componentModelGroup)

            # Set Analysis Options
            options = analysis.simulationSettings

            # Set Ambient Conditions
            options.ambientConditions.backgroundTemperature = empro.core.Expression(298.15)

            # Set Frequency Plans

            # Set Frequency Plan List
            frequencyPlanList = options.femFrequencyPlanList()
            frequencyPlanList.clear()
            try:
                frequencyPlanList._frequencyPlanType = 'Interpolating_AllFields'
            except:
                print("New frequencyplan features are not available prior to 2023.20")
                pass

            plan = empro.simulation.FrequencyPlan()
            try:
                plan.computeType = 'Simulated'
                plan.sweepType = 'Adaptive'
                plan.nearFieldType = 'AllNearFields'
                plan.farFieldType = 'NoFarFields'
            except:
                plan.type = 'Adaptive'
                plan.enabled = True
            plan.startFrequency = empro.core.Expression('1 GHz')
            plan.stopFrequency = empro.core.Expression('10 GHz')
            plan.numberOfFrequencyPoints = 901
            plan.samplePointsLimit = 300
            plan.pointsPerDecade = 5
            frequencyPlanList.append(plan)

            # Set frequency plan global settings
            options.saveFieldsFor = 'AsDefinedByFrequencyPlans'
            options.farFieldEnabled = False
            options.farFieldAngularResolution = empro.core.Expression('5 deg')
            options.adaptiveFpMaxSamples = 300
            options.adaptiveFpSaveFieldsFor = 'UserDefinedFrequencies'

            # Set Simulator

            # Set Preset Simulator Setup By Name
            options.setPresetByName('Momentum Microwave')

            # Set User-Defined Advanced Simulator Setup

            # Set MoM Options

            # Set MoM Mesh Settings
            momMeshSettings = options.momMeshSettings
            momMeshSettings.meshGranularity = empro.core.Expression('200 cpw')
            momMeshSettings.edgeMesh = 'Automatic'

            # Set MoM Per Net Overrides
            momPerPartoverrides = options.momPerNetOverrides
            override = momPerPartoverrides.add('P5', 0)
            override.meshGranularity = empro.core.Expression('2000 cpw')
            override = momPerPartoverrides.add('P6', 0)
            override.meshGranularity = empro.core.Expression('2000 cpw')

            # Set FEM Options

            # Set FEM Mesh Settings
            femMeshSettings = options.femMeshSettings
            femMeshSettings.includeResistiveLossesInGround = True

            # Set Resources Settings
            resourceSettings = empro.simulation.LocalResourceSettings()
            resourceSettings.numberOfWorkers = 1
            resourceSettings.numberOfThreads = 0
            options.resourceSettings = resourceSettings

            # Set ParameterSweep
            options.parameterSweepEnabled = False
            options.parameterSequences.clear()

            # Add the Analysis to the list of Analyses
            empro.activeProject.analyses.append(analysis)

        empro.activeProject.saveActiveProject()
        print("Running and waiting for simulation...")
        active_analysis = empro.activeProject.analyses[-1]
        empro.toolkit.analysis.runAnalysis(
            active_analysis, waitForConfirmation=False, saveProject=True
        )
        empro.activeProject.simulations.isQueueHeld = False
        active_simulation = empro.activeProject.simulations[-1]
        empro.toolkit.simulation.wait(active_simulation)
        empro.activeProject.saveActiveProject()

        #Extract parameters
        analysis = empro.activeProject.analyses[analysisName]
        params = empro.analysis.QubitParameters(analysis)

        print("Results:")
        results = params.getResults()
        chi = results.chiMatrix
        rabi = results.rabiMatrix

        for qubit in results.qubits:
            print(qubit.name)
            print(f"Frequency: {qubit.frequency}")
            print(f"Inductance: {qubit.inductance}")
            print(f"Anharmonicity: {qubit.anharmonicity}")
            print()

        for resonator in results.resonators:
            print(resonator.name)
            print(f"Frequency {resonator.frequency}")
            print(f"Anharmonicity: {resonator.anharmonicity}")
            print()

        print("Chi Matrix:")
        print(chi.values)
        print()
        print("Rabi Matrix:")
        print(rabi.values)
        print()
```


---

<!-- === 来源: Examples/ex_rfpro_stop_nets.md === -->

# Example rfpro stop nets[](#example-rfpro-stop-nets "Link to this heading")

This example demonstrates how to setup an RFPro simulation using the concept of stop nets.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

# This example can be run from within a running RFPro session opened on the
# ADS Example "RFPro Two Stage RF Board Amplifier"

# It will generate an analysis with all nets and components found between
# Q1.P1 and Q2.P2, stop at GND-typed nets

from argparse import ArgumentParser
from collections import defaultdict
import os

import empro

from keysight.edatoolbox import ads, util, xxpro

stop_pins = ["R4.P1"]
stop_nets = ["Gnd", "C5.P1"]
io_pins = ["Q1.P1", "Q2.P2"]

def populate_analysis_from_io_pins_stop_nets(analysis, io_pins, stop_pins, stop_nets):
    # take an existing analysis and based on io_pins, stop_pins and stop_nets
    # fill the analysis
    layout = empro.activeProject.layout
    pins = layout.topLevelPins

    pin_to_nets = {}
    pin_to_shorted_pins = (
        {}
    )  # tracks which pins are shorted across a component instance
    instance_to_connected_nets = {}
    pin_name_to_pin = {}
    net_to_pins = defaultdict(list)
    for pin in pins:
        pin_to_nets[pin.name] = pin.netName
    for instance in layout.instances:
        pins_on_instance = []
        nets_on_instance = []
        for pin in instance.pins():
            pin_name = f"{instance.name}.{pin.name}"
            pin_name_to_pin[pin_name] = pin
            pin_to_nets[pin_name] = pin.netName
            net_to_pins[pin.netName] = net_to_pins.get(pin.netName, []) + [
                pin_name,
            ]
            pins_on_instance.append(pin_name)
            nets_on_instance.append(pin.netName)
        for pin in pins_on_instance:
            pin_to_shorted_pins[pin] = pins_on_instance
        instance_to_connected_nets[instance.name] = nets_on_instance

    nets_to_analyse = []
    for startPin in io_pins:
        nets_to_consider = [pin_to_nets[startPin]]
        nets_visited = set()  # to avoid loops

        iteration = 0
        while nets_to_consider:
            active_net = nets_to_consider.pop(0)
            if active_net in nets_visited:
                continue

            nets_visited.add(active_net)
            nets_to_analyse.append(active_net)

            pins_range = stop_pins + io_pins
            # what is connected to this net?
            all_pins_connected_to_net = [
                pin for pin in net_to_pins[active_net] if pin not in pins_range
            ]
            # for each of the pins part of the net, collect what nets they are connected to
            # this should be only the active_net
            nets_connected = set(
                [pin_to_nets[pin] for pin in all_pins_connected_to_net]
            )
            assert len(nets_connected) == 1
            # for all pins request which components they optionally belong to and assume
            # there is a short on that component and travel over that component
            shorted_pins = []
            for pin in all_pins_connected_to_net:
                shorted_pins += pin_to_shorted_pins.get(pin, [])

            shorted_pins = [pin for pin in shorted_pins if pin not in pins_range]

            # collected the nets of these pins
            nets_connected = [pin_to_nets[pin] for pin in shorted_pins]
            nets_connected = [
                net for net in set(nets_connected) if net not in stop_nets
            ]

            nets_to_consider += nets_connected
            iteration += 1
            # avoid getting stuck in large loops due to mistakes in algorithm
            if iteration == 1000:
                raise RuntimeError("Iteration limit encountered")

    # add also the stop nets
    nets_to_analyse += stop_nets
    # add all the required nets to the analysis
    for net in nets_to_analyse:
        analysis.nets.append(layout.nets[net])

    # find all instances that have at least two nets part of the nets_to_analyse
    instances_to_analyse = []
    for instance in layout.instances:
        nets_at_instance = set(instance_to_connected_nets[instance.name])
        nets_at_instance = nets_at_instance.intersection(set(nets_to_analyse))
        if len(nets_at_instance) >= 2:
            # check if none of the io_pins are at the instance, as we can't add those instances
            # as it will generate an error
            pin_names_from_instance = set(
                [f"{instance.name}.{pin.name}" for pin in instance.pins()]
            )
            if len(pin_names_from_instance.intersection(io_pins)) == 0:
                instances_to_analyse.append(instance)

    for instance in instances_to_analyse:
        component_model_group = empro.analysis.ComponentModelGroup(
            layout.components[f"{instance.libraryName}:{instance.cellName}"]
        )
        component_model_group.name = instance.name
        component_model_group.appendInstance(
            empro.analysis.ComponentInstance(layout.instances[instance.name])
        )

        print(instance.name, instance.libraryName)
        if instance.cellName == "HBFP-0420":
            model = empro.analysis.ComponentModel(
                4, f"{instance.libraryName}:{instance.cellName}"
            )
            model.viewName = "symbol"
        else:
            model = empro.analysis.ComponentModel(
                empro.components.RLCSpecification("lumped", "15 Ohm", 0, 0, "Series")
            )
        component_model_group.appendModel(model)
        component_model_group.pinPortMap().update([("P1", 1), ("P2", -1)])
        analysis.componentModelGroups.append(component_model_group)

    gnd_layer = layout.layers["ground_bottom (6)"]
    if "Reference Pin on ground_bottom (6)" not in [
        x.name for x in layout.topLevelPins
    ]:
        ref_gnd_pin = layout.addReferencePin(
            "Reference Pin on ground_bottom (6)", gnd_layer
        )
    else:
        ref_gnd_pin = layout.topLevelPins["Reference Pin on ground_bottom (6)"]
    for pin in io_pins:
        port = empro.analysis.Port([pin_name_to_pin[pin]], [ref_gnd_pin], f"{pin}")
        analysis.ports.append(port)

    for net in analysis.requiredNets():
        analysis.nets.append(net)

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
    input_workspace_file = os.path.abspath("data/RFPro_2Stage_RF_Board_Amp_wrk.7zads")
    target_workspace = os.path.join(
        target_workspace_dir, "RFPro_2Stage_RF_Board_Amp_wrk"
    )

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

    print("Unarchiving workspace")
    ads_application.unarchive_workspace(input_workspace_file, target_workspace_dir)

    print("Creating xxPro simulation view")
    input_lcv = ads.LibraryCellView(
        library="RF_Board_lib", cell="Two_Stage_Amp", view="layout"
    )
    pro_lcv = ads.LibraryCellView(
        library="RF_Board_lib", cell="Two_Stage_Amp", view="rfpro"
    )
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate="tech",
        pro_lcv=pro_lcv,
        tool="rfpro",
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
        with empro.activeProject as project:
            # Change the roles of the components once the view is loaded
            for component in empro.activeProject.layout.components:
                if component.cellRole != empro.geometry.Component.CIRCUIT:
                    component.cellRole = empro.geometry.Component.CIRCUIT
            empro.activeProject.layout.reExtractNets()

            empro.activeProject.saveActiveProject()

        with empro.activeProject:
            analysis = empro.analysis.Analysis(
                empro.analysis.Analysis.EMUDAnalysisType, "ScriptedAnalysis"
            )
            populate_analysis_from_io_pins_stop_nets(
                analysis, io_pins, stop_pins, stop_nets
            )
            empro.activeProject.analyses.append(analysis)

        empro.activeProject.saveActiveProject()
```


---

<!-- === 来源: Examples/ex_run_hb_simulation.md === -->

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


---

<!-- === 来源: Examples/ex_run_netlist.md === -->

# Example run netlist[](#example-run-netlist "Link to this heading")

This example demonstrates how to run a simulation by specifying a netlist from a string.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc , Keysight Confidential
#

from argparse import ArgumentParser
from keysight.edatoolbox import ads, util

if __name__=="__main__":

    parser = ArgumentParser()
    parser.add_argument('--output-dir',action="store", required=True, default=None, help='Location where the output will be created')
    args = parser.parse_args()

    target_output_dir = args.output_dir
    util.safe_makedirs(target_output_dir)

    netlist = r"""; Top Design: "run_schematic_lib:voltage_divider:schematic"
    ; Netlisted using Hierarchy Policy: "Standard_ic"

    Options ResourceUsage=yes UseNutmegFormat=no EnableOptim=no TopDesignName="run_schematic_lib:voltage_divider:schematic" DcopOutputNodeVoltages=yes DcopOutputPinCurrents=yes DcopOutputAllSweepPoints=no DcopOutputDcopType=0
    R:R1  in out R=50 Ohm Noise=yes
    R:R2  out 0 R=10 Ohm Noise=yes
    V_Source:SRC1  in 0 Type="V_DC" Vdc=1.0 V SaveCurrent=1
    DC:DC1 StatusLevel=2 DevOpPtLevel=0 UseFiniteDiff=no PrintOpPoint=no Restart=1 \
    OutputPlan="DC1_Output"

    OutputPlan:DC1_Output \
        Type="Output" \
        UseNodeNestLevel=yes \
        NodeNestLevel=2 \
        UseEquationNestLevel=yes \
        EquationNestLevel=2 \
        UseSavedEquationNestLevel=yes \
        SavedEquationNestLevel=2 \
        UseDeviceCurrentNestLevel=no \
        DeviceCurrentNestLevel=0 \
        DeviceCurrentDeviceType="All" \
        DeviceCurrentSymSyntax=yes \
        UseCurrentNestLevel=yes \
        CurrentNestLevel=999 \
        UseDeviceVoltageNestLevel=no \
        DeviceVoltageNestLevel=0 \
        DeviceVoltageDeviceType="All"
    """

    print("Running netlist")
    print(f"Target output dir: {target_output_dir}")
    ads_circuitsim = ads.CircuitSimulator()
    ads_circuitsim.run_netlist(netlist, output_dir=target_output_dir)
    print("Simulation completed")
```


---

<!-- === 来源: Examples/ex_run_netlist_from_disk.md === -->

# Example run netlist from disk[](#example-run-netlist-from-disk "Link to this heading")

This example demonstrates how to run a simulation by specifying a netlist from disk.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# import the automation tools for Python for ADS and CircuitSimulation
# load the edatoolbox

import os
from argparse import ArgumentParser
from keysight.edatoolbox import ads, util

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--output-dir',action="store", required=True, default=None, help='Location where the output will be created')
    args = parser.parse_args()

    target_output_dir = args.output_dir
    util.safe_makedirs(target_output_dir)

    netlist_location = os.path.join(r"data","netlist.ckt")
    with open(netlist_location,'r') as netlistF:
        netlist = netlistF.read()

    ads_circuitsim = ads.CircuitSimulator()
    workspace_dir = None    # for this example there is no need to specify the workspace as it will
                            # not reference data
    ads_circuitsim.run_netlist(netlist, output_dir=target_output_dir, rel_data_dir=workspace_dir)
    print("Simulation completed")
```


---

<!-- === 来源: Examples/ex_run_schematic.md === -->

# Example run schematic[](#example-run-schematic "Link to this heading")

This example demonstrates how to run a simulation by specifying the schematic from a workspace.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc , Keysight Confidential
#

import os
from argparse import ArgumentParser

# import the automation tools for Python for ADS and CircuitSimulation
# load the edatoolbox
from keysight.edatoolbox import ads, circuit, dataset
from keysight.edatoolbox.util import safe_makedirs

class Bunch(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

if __name__=="__main__":
    parser = ArgumentParser()
    parser.add_argument('--output-dir',action="store", required=True, default=None, help='Location where the output will be created')
    args = parser.parse_args()

    ads_application = ads.ADS()

    target_output_dir = args.output_dir
    safe_makedirs(target_output_dir)
    target_workspace = os.path.join(target_output_dir, 'run_schematic_wrk')
    input_workspace_file = os.path.abspath('data/run_schematic_wrk.7zads')

    assert(target_output_dir!=None)
    assert(input_workspace_file!=None)
    assert(os.path.exists(target_output_dir))
    assert(os.path.exists(input_workspace_file))
    assert not os.path.exists(target_workspace), f"Target workspace {target_workspace} already exists!"

    print("Unarchiving workspace")
    ads_application.unarchive_workspace(input_workspace_file, target_output_dir)

    print(f"Input workspace file: {input_workspace_file}")
    print(f"Target output dir: {target_output_dir}")

    print("Generating netlist")
    netlist = ads_application.generate_netlist( target_workspace,
                                                ads.LibraryCellView( library="run_schematic_lib",
                                                                    cell="voltage_divider",
                                                                    view="schematic") )

    voltage_divider = circuit.Circuit(netlist, import_options=Bunch(extract_analyses=False))
    print(f'Existing value of R2.R={voltage_divider.R2.R}')
    voltage_divider.R2.R = '10 ohm'

    print("Running netlist")
    ads_circuitsim = ads.CircuitSimulator()
    ads_circuitsim.run_netlist(voltage_divider.generate_netlist(), output_dir=target_output_dir, rel_data_dir=target_output_dir)

    output_data = dataset.Dataset(os.path.join(target_output_dir,'voltage_divider.ds'))
    print(f"Voltage at node 'in' {output_data.values('DC1.DC', 'in')[0]}V")
    print(f"Voltage at node 'out' {output_data.values('DC1.DC', 'out')[0]}V")

    print("Simulation completed")
```


---

<!-- === 来源: Examples/ex_sipro_automation.md === -->

# Example sipro automation[](#example-sipro-automation "Link to this heading")

This example demonstartes how to run an SIPro SI simulation starting from an ODB++.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2025 Keysight Technologies, Keysight Confidential
#
"""Create and execute SIPro analyses based on an input .csv file."""

from argparse import ArgumentParser
from collections import defaultdict
import json
import os
from pathlib import Path
import re

from keysight.edatoolbox import ads, momentum, util, xxpro

SIGNAL_INDEX = 0
SIGNAL_POLARITY = 1

try:
    # import empro stuff for this specific sipro simulation
    import empro
    import empro.toolkit
    import empro.toolkit.analysis

except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using the Python"
        " from EMPro.  Use it by launching emproenv.bat/.sh"
    )
    raise

def get_inst_pins_on_net(project, netName):
    """Get all pins of instances connected to a net."""
    instPinsOnNet = []
    for inst in project.layout.instances:
        for pin in inst.pins():
            if pin.netName == netName:
                instPinsOnNet.append((inst, pin))
    return instPinsOnNet

def pin_to_pin_distance(pinPos1, pinPos2, precision=8):
    """Calculate the distance between two pins."""
    import math

    return round(
        math.sqrt(
            (pinPos1.x - pinPos2.x) ** 2
            + (pinPos1.y - pinPos2.y) ** 2
            + (pinPos1.z - pinPos2.z) ** 2
        ),
        precision,
    )

def get_closest_ref_pin_on_ground(instAndInstPinPair, sameInstanceOnly, project):
    """Get the closest reference pin on ground."""
    groundNetNames = {
        net.name for net in project.layout.nets if net.type == empro.geometry.Net.GROUND
    }
    inst = instAndInstPinPair[0]
    instPin = instAndInstPinPair[1]
    distDictionary = defaultdict(list)
    if sameInstanceOnly:
        for pin in inst.pins():
            if pin.netName in groundNetNames:
                dist = pin_to_pin_distance(instPin.dotPosition, pin.dotPosition)
                distDictionary[dist].append((inst, pin))
    else:
        for inst in project.layout.instances:
            for pin in inst.pins():
                if pin.netName in groundNetNames:
                    dist = pin_to_pin_distance(instPin.dotPosition, pin.dotPosition)
                    distDictionary[dist].append((inst, pin))

    if len(distDictionary) > 0:
        distDictionary = sorted(distDictionary.items(), key=lambda x: x[0])
        return distDictionary[0]
    return []

def start_find_reference(project, targetNetName):
    """Find the reference pins on the target net."""
    allPins = []
    instPins = get_inst_pins_on_net(project, targetNetName)

    findInSameInstanceOnly = False
    for instAndInstPinPair in instPins:
        plusPins = []
        minusPins = []
        dist, instAndInstPinPairGnds = get_closest_ref_pin_on_ground(
            instAndInstPinPair, findInSameInstanceOnly, project
        )
        plusPins.append(instAndInstPinPair[0].name + "." + instAndInstPinPair[1].name)

        if len(instAndInstPinPairGnds) > 0:
            for instAndInstPinPairGnd in instAndInstPinPairGnds:
                minusPins.append(
                    instAndInstPinPairGnd[0].name + "." + instAndInstPinPairGnd[1].name
                )
            allPins.append(plusPins)
            allPins.append(minusPins)

    return allPins

def load_layout_in_project(project, lcv):
    """Create the SIPro layout."""
    projectLocation = empro.libCellViewProjectLocation(lcv.library, lcv.cell, lcv.view)
    defaultSimDir = empro.simulation.directoryForSimulations(projectLocation, False)
    oaDesignRefMap = empro.geometry._processViewSetupAndGetDesignRefMap(
        lcv.library, lcv.cell, lcv.view
    )

    # loads a lib/cell/view into a project
    # usually view=layout and there is only 1 layout,
    # but this can be extended to load multiple layouts at the same time

    project.location = projectLocation
    for key, oaDesignRef in oaDesignRefMap.items():
        # we need to use this special routine to allow the LTD file
        # to be picked up so the simulators can perform
        # simulations using it, important for encrypted workflows but also for Momentum
        layout = empro.geometry.OaLayout.readLayoutEx(
            oaDesignRef, key, os.path.join(defaultSimDir, "extra")
        )
        empro.activeProject.geometry.append(layout)

def create_workspace(
    workspace_path: str | Path,
    odbpp_file: str | Path,
    cell_name: str,
    library_name: str,
):
    """Create a workspace and import an ODB++ file into it."""
    workspace_path = Path(workspace_path).absolute()
    workspace_str = str(workspace_path)
    odbpp_file = Path(odbpp_file).absolute()

    # start running ADS and create workspace and import ODB++ file
    ads_application = ads.ADS()
    print("ADS application created ")

    # is not existing, create new workspace
    if not workspace_path.exists():
        ads_application.create_workspace(workspace_path.parent, workspace_path.stem)
        print(f"Created workspace {workspace_path}")

        print(f"Importing ODB++ {odbpp_file}")

        odbpp_import_options = ads.OdbImportOptions()
        odbpp_import_options.separate_component_lib = False
        odbpp_import_options.separate_tech_lib = False

        ads_application.import_odbpp(
            workspace_str,
            odbpp_file,
            library=library_name,
            cell=cell_name,
            use_legacy_importer=False,
            import_options=odbpp_import_options,
        )
        print("ODB++ imported ")

        # update the material database
        matdb_path = str(workspace_path / library_name / "materials.matdb")
        matdb = ads.MaterialDatabase(matdb_path)
        for diel in matdb.dielectrics:
            if diel.er_real <= 0.0:
                diel.er_real = 4.0
        matdb.write(matdb_path)

        # update the thickness of metal layers
        subst_path = str(workspace_path / library_name / "tech.subst")
        substrate_info = ads.SubstrateModel(subst_path)
        for layer in substrate_info.layers:
            if layer.layer == 1036:
                layer.thick = -1.761411  # negative thickness : below interface
            if layer.index == 8:
                layer.thick = 0.6654142

        # update the thickness of dielectric layers
        for material in substrate_info.materials:
            if material.index == 1:
                material.thick = 3.9371

        substrate_info.write(subst_path)

        print("Creating xxPro simulation view... ")
        input_lcv = ads.LibraryCellView(library_name, cell_name, "layout")

        pro_lcv = ads.LibraryCellView(library_name, cell_name, "sipro")

        ads_application.create_pro_view(
            workspace_str,
            input_lcv=input_lcv,
            substrate=cell_name,
            pro_lcv=pro_lcv,
            tool="sipi",
        )
        print("xxPro simulation view created!")

        # load library
        xxpro.use_workspace(workspace_str)

        with util.remember_cwd():
            # at this stage the view is still completely empty
            # we still need to load the requested layouts in it
            with empro.activeProject as project:
                load_layout_in_project(project, pro_lcv)

        momentum_dir = momentum.get_momentum_location()
        empro.toolkit.analysis.setMomentumDir(momentum_dir)
        print("Workspace created!")
    # if already existing workspace, open it
    else:
        xxpro.use_workspace(workspace_str)

        print(f"Workspace {workspace_path} already exists.")
        # Load the project
        empro.activeProject.loadActiveProjectFrom(library_name, cell_name, "sipro")
        momentum_dir = momentum.get_momentum_location()
        empro.toolkit.analysis.setMomentumDir(momentum_dir)
        print("Workspace loaded! ")
    empro.activeProject.saveActiveProject()

def create_analysis(
    net_definitions, start_freq, stop_freq, freq_pts, num_of_Sim, freq_type
):
    """Create an SIPro analysis."""
    with util.remember_cwd():
        layout = empro.activeProject.layout
        assert layout is not None
        analysis = empro.analysis.Analysis()
        analysis.name = f"Analysis {str(num_of_Sim)} by Script"
        analysis.analysisType = empro.analysis.Analysis.PASIAnalysisType
        print(f"{analysis.name} is now running")
        portList = analysis.ports
        netNames = ["GND"]

        for net_i in net_definitions:
            net_list = net_i.split(",")

            # given a range of nets
            if len(net_list) >= 3:
                net = net_list[0]
                print("Analyzing a range of nets")
                start_range = net_list[1]
                end_range = net_list[2]
                for i in range(int(start_range), int(end_range) + 1):
                    # find plus and minus pins
                    print(f"Creating ports for {net}{i}")
                    allPins = start_find_reference(empro.activeProject, net + str(i))
                    plusPins = [
                        allPins[index]
                        for index in filter(lambda x: x % 2 == 0, range(len(allPins)))
                    ]
                    minusPins = [
                        allPins[index]
                        for index in filter(lambda x: x % 2 == 1, range(len(allPins)))
                    ]

                    # create ports
                    for j in range(len(plusPins)):
                        port = empro.toolkit.analysis.createPortFromPins(
                            plusPins[j], minusPins[j]
                        )
                        for k in plusPins[j]:
                            ref, _ = k.split(".")
                            port.name = f"{net}{i}_{ref}"
                            portList.append(port)

                    # add net name into netNames array
                    netNames.append(f"{net}{i}")

            # given single nets in a line
            else:
                net = net_list[0]
                print(f"Creating ports for {net}")
                netNames.append(net)
                allPins = start_find_reference(empro.activeProject, net)
                plusPins = [
                    allPins[index]
                    for index in filter(lambda x: x % 2 == 0, range(len(allPins)))
                ]
                minusPins = [
                    allPins[index]
                    for index in filter(lambda x: x % 2 == 1, range(len(allPins)))
                ]

                for j in range(len(plusPins)):
                    port = empro.toolkit.analysis.createPortFromPins(
                        plusPins[j], minusPins[j]
                    )

                    for k in plusPins[j]:
                        ref, _ = k.split(".")
                        port.name = f"{net}_{ref}"
                        portList.append(port)

        # Build nets, add them to the analysis
        layout = empro.activeProject.geometry[0]
        net_list = analysis.nets
        for netName in netNames:
            net = empro.analysis.Net(netName, layout)
            net_list.append(net)

        # Create new frequency plan
        options = analysis.simulationSettings
        frequencyPlanList = options.femFrequencyPlanList()
        frequencyPlanList.clear()
        plan = empro.simulation.FrequencyPlan()
        plan.type = freq_type
        plan.startFrequency = start_freq
        plan.stopFrequency = stop_freq
        plan.numberOfFrequencyPoints = freq_pts
        plan.samplePointsLimit = freq_pts
        plan.enabled = True
        frequencyPlanList.append(plan)

        return analysis

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--output-dir",
        action="store",
        default=None,
        help="Location where the workspace will be created",
    )
    args = parser.parse_args()
    data_path = Path(__file__).parent / "data"
    input_file_location = data_path / "sample.txt"
    output_dir = Path(args.output_dir).absolute()
    util.safe_makedirs(args.output_dir)
    tgz_file = data_path / "sipro_sample_odb.tgz"
    cell_name = "sipro_sample_odb"
    library_name = f"{cell_name}_lib"
    target_workspace_name = f"{cell_name}_wrk"
    target_workspace_path = output_dir / target_workspace_name

    assert input_file_location.exists(), f"{input_file_location} does not exist"
    assert tgz_file.exists(), f"{tgz_file} does not exist"
    assert output_dir.exists(), f"{output_dir} does not exist"
    assert not target_workspace_path.exists(), f"{target_workspace_path} already exists"

    os.environ["HPEESOF_DIR"] = (
        ads.get_ads_location()
    )  # ensure the referenced env vars in lib.defs can be found

    # create workspace information
    create_workspace(
        target_workspace_path,
        odbpp_file=tgz_file,
        cell_name=cell_name,
        library_name=library_name,
    )

    # collect all information
    simSessionsList = []
    with open(input_file_location) as myfile:
        for jsonObj in myfile:
            tempData = json.loads(jsonObj)
            simSessionsList.append(tempData)

        for simData in simSessionsList:
            testId = simData["id"]
            net_definitions = []
            for signal_net in simData["signal_net"]:
                signal_name = signal_net["name"]
                signal_index = re.findall(r"\[(\w+:\w)\]", signal_name)
                filtered_name = re.sub(r"\[(\w+:\w)\]", "", signal_name)
                polarity_list = ["N", "P"]
                if 2 == len(signal_index):
                    start_index = int(signal_index[SIGNAL_INDEX].split(":")[0])
                    end_index = int(signal_index[SIGNAL_INDEX].split(":")[1]) + 1
                    net_definitions = [
                        "{}{}_{}".format(filtered_name, i, j)
                        for i in range(start_index, end_index)
                        for j in polarity_list
                    ]
                elif 1 == len(signal_index):
                    temp = signal_index[SIGNAL_INDEX].split(":")[0]
                    if temp.isdigit():
                        start_index = int(signal_index[SIGNAL_INDEX].split(":")[0])
                        end_index = int(signal_index[SIGNAL_INDEX].split(":")[1]) + 1
                        net_definitions = [
                            f"{filtered_name}{i}" for i in range(start_index, end_index)
                        ]
                    else:
                        net_definitions = [
                            f"{filtered_name}_{i}" for i in polarity_list
                        ]
                else:
                    net_definitions = filtered_name
            start_freq = float(simData["start_frequency"])
            stop_freq = float(simData["stop_frequency"])
            freq_pts = int(simData["frequency_points"])
            freq_type = simData["type"]
            num_of_Sim = len(empro.activeProject.analyses) + 1
            # create analysis
            analysis = create_analysis(
                net_definitions, start_freq, stop_freq, freq_pts, num_of_Sim, freq_type
            )

            # add analysis to project
            analyses = empro.activeProject.analyses
            analyses.append(analysis)
            analysis = analyses[-1]

            # run the analysis
            print(analysis.name, " running")
            empro.toolkit.analysis.runAnalysis(analysis, waitForConfirmation=False)
            print("Waiting on Simulation...")
            my_simulation = empro.toolkit.analysis.getSimulation(analysis)
            empro.toolkit.simulation.wait(my_simulation)
            empro.activeProject.saveActiveProject()

            # Possible simulation status: "Initialized", "Error", "Queued",
            # "Completed", "Killed", "Solving", "Unarchiving", "Unarchived",
            # "Killing", "Solved"
            # Will be added into an enum inside EDA Toolbox
            print("Simulation Done, Status: ", my_simulation.status)
            if my_simulation.status == "Completed":
                results = empro.analysis.CircuitResults(analysis)
                results.samplingConfig = empro.enparams.SamplingConfig(
                    freq_type, freq_pts
                )

                numPorts = results.numberOfPorts()
                freqs = results.frequencies()
                for p in range(numPorts):
                    for q in range(numPorts):
                        print(
                            [
                                results.Src(p, q, "ComplexMagnitude").at(freq_idx)
                                for freq_idx in range(len(freqs))
                            ]
                        )
            elif my_simulation.status == "Error":
                print("Simulation invalid because: ", my_simulation.reasonWhyInvalid())
            else:
                print("Done with Error!")

    print("Total number of simulations ", num_of_Sim)
```


---

<!-- === 来源: Examples/ex_sipro_channelsim_flow.md === -->

# Example sipro channelsim flow[](#example-sipro-channelsim-flow "Link to this heading")

This example demonstrates how to run a channel simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2025 Keysight Technologies, Keysight Confidential
# ruff: noqa: D100
from argparse import ArgumentParser
import os
from pathlib import Path
import re

import plotly.express as px
from plotly.subplots import make_subplots

from keysight.edatoolbox import ads, circuit, momentum, util, xxpro
import keysight.pwdatatools as pwdt

def update_sio_path_in_subckt(new_sio_file_location: str, subckt_file: str):
    """Update the file location of an SIO file in a subcircuit netlist.

    Parameters
    ----------
    new_sio_file_location : str
        New location of the SIO file.
    subckt_file : str
        Path to the subcircuit file.
    """
    new_sio_file_location = str(new_sio_file_location).replace("\\", "\\\\")
    with open(subckt_file, "r") as file:
        data = file.read()
    data = re.sub(r'File="[^"]*"', 'File="' + new_sio_file_location + '"', data)
    with open(subckt_file, "w") as file:
        file.write(data)
    print("New Sio file location updated")

def update_subckt_path_in_netlist(new_subckt_file_location: str, netlist_file: str):
    """Update the file location of a subcircuit netlist in a netlist file.

    Parameters
    ----------
    new_subckt_file_location : str
        New location of subcircuit netlist.
    netlist_file : str
        Path for netlist file.
    """
    new_subckt_file_location = str(new_subckt_file_location).replace("\\", "\\\\")
    with open(netlist_file, "r") as file:
        data = file.read()
    data = re.sub(
        r'#include "[^"]*"', '#include "' + new_subckt_file_location + '"', data
    )
    with open(netlist_file, "w") as file:
        file.write(data)
    print("New subckt file location updated")

def read_netlist(netlist_file_location: str):
    """Return the content of the netlist file.

    Parameters
    ----------
    netlist_file_location : str
        Path for netlist.log file.

    Returns
    -------
    str
        Content of the netlist file.
    """
    netlist = ""
    with open(netlist_file_location, "r") as file:
        netlist = file.read()
    return netlist

try:
    import empro
    import empro.toolkit
    import empro.toolkit.analysis
except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using the Python"
        " from EMPro.  Use it by launching emproenv.bat/.sh"
    )
    raise

class Bunch(object):
    """Convert kwargs to object attributes."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

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
    output_dir = Path(args.output_dir).absolute()
    util.safe_makedirs(args.output_dir)

    data_path = Path(__file__).parent / "data"
    odb_file = data_path / "Minipc" / "minipc_pm_v0_pm.zip"
    cell_name = "minipc_pm"
    library_name = f"{cell_name}_lib"
    target_workspace_name = f"{cell_name}_wrk"
    target_workspace_path = output_dir / target_workspace_name
    target_workspace = str(target_workspace_path)
    netlist_file = data_path / "Minipc" / "Netlist" / "netlist.log"
    subckt_file = (
        data_path
        / "Minipc"
        / "Netlist"
        / "minipc_pm_lib_minipc_pm_DDR_Ckt_DQ0_DDR_PCB1_subCktNetlist.log"
    )

    assert odb_file.exists(), f"ODB++ file {odb_file} does not exist"
    assert netlist_file.exists(), f"Netlist file {netlist_file} does not exist"
    assert subckt_file.exists(), f"Subcircuit file {subckt_file} does not exist"
    assert output_dir.exists(), f"Output directory {output_dir} does not exist"
    assert not target_workspace_path.exists(), (
        f"Target workspace {target_workspace} already exists!"
    )

    print(f"Input ODB++: {odb_file}")

    print(f"Target workspace: {target_workspace}")

    # Step 1: Creating the ADS application object
    ads_application = ads.ADS()
    print("ADS application created")
    print("Creating workspace")
    if not os.path.exists(target_workspace):
        ads_application.create_workspace(output_dir, target_workspace_name)

    # Step 2: Import odb++ file

    print("Importing ODB++")

    odbpp_import_options = ads.OdbImportOptions()
    odbpp_import_options.separate_component_lib = False
    odbpp_import_options.separate_tech_lib = False

    ads_application.import_odbpp(
        target_workspace,
        odb_file,
        library=library_name,
        cell=cell_name,
        use_legacy_importer=False,
        import_options=odbpp_import_options,
    )
    print("ODB++ imported")

    # update the material database
    matdb_path = str(target_workspace_path / library_name / "materials.matdb")
    matdb = ads.MaterialDatabase(matdb_path)
    for diel in matdb.dielectrics:
        if diel.er_real <= 0.0:
            diel.er_real = 4.0
    matdb.write(matdb_path)

    # update the thickness of metal layers
    subst_path = str(target_workspace_path / library_name / f"{cell_name}.subst")
    substrate_info = ads.SubstrateModel(subst_path)
    for layer in substrate_info.layers:
        if layer.layer == 1033:
            layer.thick = -1.761411  # negative thickness : below interface
        if layer.index == 8:
            layer.thick = 0.6654142

    # update the thickness of dielectric layers
    for material in substrate_info.materials:
        if material.index == 1:
            material.thick = 3.01

    substrate_info.write(subst_path)

    input_lcv = ads.LibraryCellView(library=library_name, cell=cell_name, view="layout")
    pro_lcv = ads.LibraryCellView(library=library_name, cell=cell_name, view="sipi1")

    # Step 3: Creating the SIPro view
    print("Creating SIPro simulation view")
    ads_application.create_pro_view(
        target_workspace,
        input_lcv=input_lcv,
        substrate=cell_name,
        pro_lcv=pro_lcv,
        tool="sipi",
    )
    print("xxPro simulation view created")

    momentum_dir = momentum.get_momentum_location()
    empro.toolkit.analysis.setMomentumDir(momentum_dir)
    with util.remember_cwd():
        os.environ["HPEESOF_DIR"] = (
            ads.get_ads_location()
        )  # ensure the referenced env vars in lib.defs can be found

        # Step 4: Loading the SIPro view into the SIPro tool
        xxpro.use_workspace(target_workspace)
        xxpro.load_pro_view(pro_lcv)
        empro.activeProject.saveActiveProject()

        # Step 5 : ==== Script generated by ADS Window starts here =====
        # Create an Analysis
        analysis = empro.analysis.Analysis()
        analysis.name = "DQ0 by Script"
        analysis.analysisType = empro.analysis.Analysis.PASIAnalysisType

        # Set PortList
        portList = analysis.ports

        plusPins = ["U1.AV26"]
        minusPins = ["U1.AV25"]
        port = empro.toolkit.analysis.createPortFromPins(plusPins, minusPins)
        port.name = "DDR4_DQ0_U1"
        port.referenceImpedance = empro.core.Expression("50")
        port.feedType = "Auto"
        portList.append(port)

        plusPins = ["U15.G2"]
        minusPins = ["U15.H1"]
        port = empro.toolkit.analysis.createPortFromPins(plusPins, minusPins)
        port.name = "DDR4_DQ0_U15"
        port.referenceImpedance = empro.core.Expression("50")
        port.feedType = "Auto"
        portList.append(port)

        # Set Netlist
        netList = analysis.nets

        net = empro.analysis.Net("GND", empro.activeProject.geometry[0])
        netList.append(net)

        net = empro.analysis.Net("DDR4_DQ0", empro.activeProject.geometry[0])
        netList.append(net)

        # Set Analysis Options
        options = analysis.simulationSettings

        # Set Ambient Conditions
        options.ambientConditions.backgroundTemperature = empro.core.Expression(298.15)

        # Set Frequency Plans

        # Set Frequency Plan List
        frequencyPlanList = options.femFrequencyPlanList()
        frequencyPlanList.clear()

        plan = empro.simulation.FrequencyPlan()
        plan.type = "Linear"
        plan.startFrequency = empro.core.Expression("20 kHz")
        plan.stopFrequency = empro.core.Expression("20.416667 GHz")
        plan.numberOfFrequencyPoints = 66
        plan.samplePointsLimit = 300
        plan.pointsPerDecade = 20
        plan.enabled = True
        frequencyPlanList.append(plan)

        # Set Field Storage
        options.saveFieldsFor = "NoFrequencies"
        options.farFieldEnabled = False
        options.farFieldAngularResolution = empro.core.Expression("5 deg")

        # Set Simulator

        # Set Preset Simulator Setup By Name
        options.preset = None

        # Set User-Defined Advanced Simulator Setup

        # Set FEM Options

        # Set FEM Matrix Solver
        options.femMatrixSolver.solverType = "MatrixSolverAuto"

        # Set FEM Mesh Settings
        femMeshSettings = options.femMeshSettings
        femMeshSettings.includeResistiveLossesInGround = False
        femMeshSettings.orderOfBasisFunctions = 1
        femMeshSettings.useTargetMeshSize = False
        femMeshSettings.autoTargetMeshSize = False
        femMeshSettings.targetMeshSize = empro.core.Expression("2 mm")
        femMeshSettings.useMeshDomainOptimization = True
        femMeshSettings.minimumNumberOfPasses = 1
        femMeshSettings.maximumNumberOfPasses = 1
        femMeshSettings.refineAtSpecificFrequency = False
        femMeshSettings.refinementFrequency = empro.core.Expression("1 GHz")

        # Set Resources Settings
        # Set Resources Settings
        resourceSettings = empro.simulation.LocalResourceSettings()
        resourceSettings.numberOfWorkers = 1
        resourceSettings.numberOfThreads = 0
        options.resourceSettings = resourceSettings

        # Set ParameterSweep
        options.parameterSweepEnabled = False
        options.parameterSequences.clear()

        # Add the Analysis to the list of Analyses
        empro.activeProject.analyses.append(analysis)
        # ===== Script generated by ADS Window Ends here ======
        # take the latest analysis
        active_analysis = empro.activeProject.analyses[-1]

        # Step 6: Run Analysis for the nets added in SIPro
        print("Running and waiting for simulation...")
        empro.toolkit.analysis.runAnalysis(
            active_analysis, waitForConfirmation=False, saveProject=True
        )
        empro.activeProject.simulations.isQueueHeld = False
        active_simulation = empro.activeProject.simulations[-1]
        empro.toolkit.simulation.wait(active_simulation)
        new_sio_location = os.path.join(
            active_simulation.simulationPath(), "emds_dsn", "design", "design.sio"
        )
        empro.activeProject.saveActiveProject()

    # replace new sio in the subckt netlist
    # Step 7 : update netlist for Memory designer Schematic with new sio file
    update_sio_path_in_subckt(new_sio_location, subckt_file)

    # replace new subckt in the netlist file
    update_subckt_path_in_netlist(subckt_file, netlist_file)

    netlist = read_netlist(netlist_file)
    # Step 8:
    # Run Channel simulation using circuit simulator module using updated netlist

    ads_circuitsim = ads.CircuitSimulator()
    ckt = circuit.Circuit(netlist, import_options=Bunch(extract_analyses=False))
    ads_circuitsim.run_netlist(ckt.generate_netlist(), output_dir=target_workspace)

    # Step 9 : Plot measurement results
    print("====Measurement Results====")
    ds_file = os.path.join(target_workspace, "md.ds")
    results = pwdt.read_file(ds_file)

    eye_meas_summary = results.get_member_as_block(
        "Tran1.TDM.Memory_Probe.Ch0_U15_DQ0.EyeHeight"
    ).to_pandas_dataframe()

    print(eye_meas_summary.to_string(index=False))

    eyevout_data1 = results.get_member_as_block(
        "Tran1.TDM.Memory_Probe.Ch0_U15_DQ0.Eye"
    ).to_pandas_dataframe()
    eyevout_data2 = results.get_member_as_block(
        "Tran1.TDM.Memory_Probe.Ch0_U1_DQ0.Eye"
    ).to_pandas_dataframe()
    config = dict({"scrollZoom": True})

    if "index" not in eyevout_data1.columns:
        # creating dummy index column for plotly to color the points.
        # TODO : Remove if once pwdatatools stops discarding the index
        # column containing the eye diagram density values.
        eyevout_data1["index"] = (
            eyevout_data1["Density"] / max(eyevout_data1["Density"]) * 100
        )

    if "index" not in eyevout_data2.columns:
        # creating dummy index column for plotly to color the points.
        # TODO : Remove if once pwdatatools stops discarding the index
        # column containing the eye diagram density values.
        eyevout_data2["index"] = (
            eyevout_data2["Density"] / max(eyevout_data2["Density"]) * 100
        )

    fig1 = px.scatter(eyevout_data1, y="Density", x="time", color="index")
    fig2 = px.scatter(eyevout_data2, y="Density", x="time", color="index")
    fig = make_subplots(
        rows=2,
        cols=1,
        subplot_titles=(
            "Ch0_U15_DQ0.Eye.Density Vs Time",
            "Ch0_U1_DQ0.Eye.Density Vs Time",
        ),
        shared_xaxes=True,
        shared_yaxes=True,
        x_title="Time (psec)",
        y_title="Density",
    )
    fig.add_traces(fig1.data, rows=1, cols=1)
    fig.add_traces(fig2.data, rows=2, cols=1)
    fig.update_layout(title_text=f"Eye Diagram plots for : {odb_file}")
    fig.show(config=config)
    # imagefile = os.path.join(target_workspace, "eyeplot.jpeg")
    # fig.write_image(imagefile)
    print("====Analysis Successfully Completed====")
```


---

<!-- === 来源: Examples/ex_sipro_example_si.md === -->

# Example sipro SI[](#example-sipro-si "Link to this heading")

This example demonstrates how to run an SI simulation.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

from argparse import ArgumentParser
import os

from keysight.edatoolbox import ads, momentum, util, xxpro

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

    # for SI analyses and Momentum analyses we need to pass on to xxPro the location of the Momentum binaries
    momentum_dir = momentum.get_momentum_location()
    empro.toolkit.analysis.setMomentumDir(momentum_dir)

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
            layout = empro.activeProject.layout
            # create an analysis
            analysis = empro.analysis.Analysis(
                empro.analysis.Analysis.PASIAnalysisType, "Test"
            )

            portList = analysis.ports
            port_definitions = [
                ("DQ00_J1", ["J1.P_5"], ["J1.P_6"]),
                ("DQ00R_U19", ["U19.P_D3"], ["U19.P_D1"]),
                ("DQ01_J1", ["J1.P_150"], ["J1.P_149"]),
                ("DQ01R_U19", ["U19.P_C2"], ["U19.P_D1"]),
                ("DQ02_J1", ["J1.P_12"], ["J1.P_11"]),
                ("DQ02R_U19", ["U19.P_D7"], ["U19.P_C8"]),
                ("DQ03_J1", ["J1.P_157"], ["J1.P_156"]),
                ("DQ03R_U19", ["U19.P_B7"], ["U19.P_C8"]),
            ]

            def pin_from_name(layout, name: str):
                """Return a pin object from a hierachical pin name.

                Parameters
                ----------
                layout : empro.layout_wrapper.LayoutWrapper
                    Layout of an active xxPro project.
                name : str
                    Pin name.

                Returns
                -------
                empro.geometry.Pin
                    A pin object corresponding to the pin name.
                """
                try:
                    inst_name, pin_name = name.split(".")
                    return layout.instances[inst_name].instPin(pin_name)
                except ValueError:
                    return layout.topLevelPins[name]

            for port_def in port_definitions:
                name, plus_pins, minus_pins = port_def
                plus_pins = [pin_from_name(layout, name) for name in plus_pins]
                minus_pins = [pin_from_name(layout, name) for name in minus_pins]
                port = empro.analysis.Port(plus_pins, minus_pins, name)
                portList.append(port)

            component_model_group_list = analysis.componentModelGroups
            component_model_group = empro.analysis.ComponentModelGroup(
                layout.components[
                    "PC4-RDIMM_V090_RC_F0_20131106_lib:rn_2pos_respack_2x0201-510-501140a_15"
                ]
            )
            component_model_group.arrayedComponent = True
            component_model_group.pinPortMap().update(
                [("P_1", 1), ("P_2", 2), ("P_3", -2), ("P_4", -1)]
            )
            for instance_name in ["RN95", "RN97"]:
                component_model_group.appendInstance(
                    empro.analysis.ComponentInstance(layout.instances[instance_name])
                )

            component_model = empro.analysis.ComponentModel(
                empro.components.RLCSpecification("lumped", "15 Ohm", 0, 0, "Series")
            )
            component_model_group.appendModel(component_model)
            component_model_group_list.append(component_model_group)

            net_list = analysis.nets
            for net in analysis.requiredNets():
                net_list.append(net)

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

        res = empro.analysis.CircuitResults(active_analysis)
        freqs = list(res.frequencies())
        S21_mag = res.Src(1, 0, "ComplexMagnitude")
        S21_phase = res.Src(1, 0, "Phase")
        S43_mag = res.Src(3, 2, "ComplexMagnitude")
        S43_phase = res.Src(3, 2, "Phase")
        S65_mag = res.Src(5, 4, "ComplexMagnitude")
        S65_phase = res.Src(5, 4, "Phase")
        S87_mag = res.Src(7, 6, "ComplexMagnitude")
        S87_phase = res.Src(7, 6, "Phase")

        output_file = os.path.join(target_workspace_dir, "sparams.csv")
        print(f"Writing S parameter data to {output_file}")
        with open(output_file, "w") as file:
            line = ",".join(
                [
                    "Frequency",
                    "S21 (mag)",
                    "S21 (phase)",
                    "S43 (mag)",
                    "S43 (phase)",
                    "S65 (mag)",
                    "S65 (phase)",
                    "S87 (mag)",
                    "S87 (phase)",
                ]
            )
            file.write(line + "\n")
            for i in range(len(freqs)):
                line = f"{freqs[i]},{S21_mag[i]},{S21_phase[i]},{S43_mag[i]},{S43_phase[i]},{S65_mag[i]},{S65_phase[i]},{S87_mag[i]},{S87_phase[i]}"
                file.write(line + "\n")
```


---

<!-- === 来源: Examples/ex_sipro_extract_tdr.md === -->

# Example sipro extract tdr[](#example-sipro-extract-tdr "Link to this heading")

This example demonstrates how to run an SI simulation and extract the TDR results.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#
from argparse import ArgumentParser
import os

import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

from keysight.edatoolbox import ads, momentum, util, xxpro

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

    print("Unarchiving workspace")
    ads_application.unarchive_workspace(input_workspace_file, target_workspace_dir)

    pro_lcv = ads.LibraryCellView(library="DQLines_lib", cell="DQLines", view="sipi")

    # for SI analyses and Momentum analyses we need to pass on to xxPro the location of the Momentum binaries
    momentum_dir = momentum.get_momentum_location()
    empro.toolkit.analysis.setMomentumDir(momentum_dir)

    with util.remember_cwd():
        os.environ[
            "HPEESOF_DIR"
        ] = (
            ads.get_ads_location()
        )  # ensure the referenced env vars in lib.defs can be found
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

        # Configure an Impedance TDR plot
        result = empro.analysis.CircuitResults(active_analysis)
        tdr_config = empro.datasource.TDRConfig()
        tdr_config.resultType = "Impedance"
        tdr_config.nbTimeSamples = 301
        tdr_config.startTime = 0.0
        tdr_config.delay = 1e-9
        tdr_config.stopTime = 5.0e-9
        tdr_config.responseType = "StepResponse"
        tdr_config.windowType = "Kaiser"
        result.tdrConfig = tdr_config

        # extract TDR Results
        tdr11 = result.Trc(0, 0)
        tdr12 = result.Trc(0, 1)
        tdr21 = result.Trc(1, 0)
        tdr22 = result.Trc(1, 1)

        # Subplots for tdr11 and tdr22
        nr_results = len(tdr11)
        time_dimension = tdr11.dimension(0)
        time_values = [time_dimension.at(idx) for idx in range(nr_results)]
        tdr11_values = [tdr11.at(idx) for idx in range(nr_results)]
        tdr22_values = [tdr22.at(idx) for idx in range(nr_results)]

        fig = make_subplots(rows=2, cols=1)
        config = dict({"scrollZoom": True})
        fig = make_subplots(
            rows=2,
            cols=1,
            x_title="Time(ns)",
            y_title="Impedance(ohm)",
            subplot_titles=(f"{tdr11.name}", f"{tdr22.name}"),
        )
        fig1 = px.line(y=tdr11_values, x=time_values)
        fig2 = px.line(y=tdr22_values, x=time_values)
        fig.add_trace(fig1.data[0], row=1, col=1)
        fig.add_trace(fig2.data[0], row=2, col=1)

        fig.show(config=config)

        # write results into csv
        outputfile = os.path.join(target_workspace_dir, "DQLines_wrk_TDR.csv")
        data = pd.DataFrame(
            data=zip(time_values, tdr11_values, tdr22_values),
            columns=["Time(ns)", "TDR11_Impedance", "TDR22_Impedance"],
        )
        data.to_csv(outputfile, index=False)
        print("Execution Successful")
```


---

<!-- === 来源: Examples/ex_sipro_eye_diagram.md === -->

# Example sipro eye diagram[](#example-sipro-eye-diagram "Link to this heading")

This example demonstrates how to run an SI simulation and extract the Eye diagram.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
# ruff: noqa: D100
from argparse import ArgumentParser
import os

from keysight.edatoolbox import ads, circuit, momentum, util, xxpro

class Bunch(object):
    """Convert input kwargs to object attributes."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

try:
    import empro
    import empro.toolkit
    import empro.toolkit.analysis
except ImportError:
    print(
        "Cannot import empro module - this usually means you are not using "
        "the Python from EMPro. Use it by launching emproenv.bat/.sh"
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
    input_workspace_file = os.path.abspath("data/DQLines_wrk.7zads")
    target_workspace = os.path.join(target_workspace_dir, "DQLines_wrk")

    assert target_workspace_dir is not None
    assert input_workspace_file is not None
    assert os.path.exists(target_workspace_dir)
    assert os.path.exists(input_workspace_file)
    assert not os.path.exists(target_workspace), (
        f"Target workspace {target_workspace} already exists!"
    )

    print(f"Input workspace file: {input_workspace_file}")
    print(f"Target output dir: {target_workspace_dir}")

    ads_application = ads.ADS()
    print("ADS application created")

    print("Unarchiving workspace")
    ads_application.unarchive_workspace(input_workspace_file, target_workspace_dir)

    pro_lcv = ads.LibraryCellView(library="DQLines_lib", cell="DQLines", view="sipi")

    # for SI analyses and Momentum analyses we need to pass on to xxPro
    # the location of the Momentum binaries
    momentum_dir = momentum.get_momentum_location()
    empro.toolkit.analysis.setMomentumDir(momentum_dir)

    with util.remember_cwd():
        os.environ["HPEESOF_DIR"] = (
            ads.get_ads_location()
        )  # ensure the referenced env vars in lib.defs can be found
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

    # now also run the channel analysis and bring up the DDS with the eye diagram
    netlist = ads_application.generate_netlist(
        target_workspace,
        ads.LibraryCellView(
            library="DQLines_lib", cell="channel_sim", view="schematic"
        ),
    )

    ads_circuitsim = ads.CircuitSimulator()
    ckt = circuit.Circuit(netlist, import_options=Bunch(extract_analyses=False))
    print(f"Existing File={ckt.definitions[ckt.X1.instance_type].DQ0.File}")
    new_sio_location = os.path.join(
        active_simulation.simulationPath(), "emds_dsn", "design", "design.sio"
    )
    print(f"New File={new_sio_location}")
    ckt.definitions[ckt.X1.instance_type].DQ0.File = f'"{new_sio_location}"'
    ads_circuitsim.run_netlist(ckt.generate_netlist(), output_dir=args.output_dir)
    # Uncommnet the following line to run data display, disabled for now as it blocks CI
    # ads_dds = ads.DataDisplay()
    # ads_dds.run_dds(
    #     args.output_dir,
    #     datadisplay_file=os.path.join(target_workspace, "channel_sim.dds"),
    # )
```


---

<!-- === 来源: Examples/ex_sipro_ploteye_plotly.md === -->

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


---

<!-- === 来源: Examples/ex_sweep_inductor_values.md === -->

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


---

<!-- === 来源: Examples/ex_systemvue_basic.md === -->

# Example systemvue basic[](#example-systemvue-basic "Link to this heading")

This example demonstrates how to how to use the EDA Toolbox to perform basic SystemVue commands.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

import os

from keysight.edatoolbox import multi_python, systemvue

# example using the Python SV API, even when you are running this
# script from a version that doesn't have the SV Python API

def function_in_current_context(an_arg):
    import sys

    print(f"Current context sys.executable={sys.executable}")
    try:
        import svepythonapi
    except ImportError:
        print("failed to import svepythonapi module")

def function_in_systemvue_context(an_arg):
    import svepythonapi

    sv_py_major, sv_py_minor = systemvue.python_version_for_systemvue(
        systemvue.get_systemvue_location()
    )
    print(f"Required Python version SystemVue={sv_py_major}, {sv_py_minor}")
    sv_installation_dir = systemvue.get_systemvue_location()
    ws = svepythonapi.Application().open_workspace(
        os.path.join(sv_installation_dir, "Template", "RF PhasedArray TX.wsv")
    )
    print("Successfully imported svepythonapi module")
    print(f"Workspace path: {ws.workspace_path}")
    print(f"Analyses: {ws.analyses}")
    print(f"Datasets: {ws.datasets}")

if __name__ == "__main__":
    function_in_current_context(42)
    multi_python.py_systemvue_multiprocess_execute(function_in_systemvue_context, 10)
```


---

<!-- === 来源: Examples/ex_voltage_divider.md === -->

# Example voltage divider[](#example-voltage-divider "Link to this heading")

This example demonstrates how to design and analyze voltage divider circuits.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
#
# Copyright 1983-2022 Keysight Technologies, Inc, Keysight Confidential
#

import os
from argparse import ArgumentParser
from keysight.edatoolbox import ads, circuit, dataset
from keysight.edatoolbox.util import safe_makedirs

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--output-dir',action="store", required=True, default=None, help='Location where the output will be created')
    args = parser.parse_args()

    target_output_dir = args.output_dir
    safe_makedirs(target_output_dir)
    print(f"Target output dir: {target_output_dir}")

    voltage_divider = circuit.Circuit()

    R1 = voltage_divider.add(circuit.R(name='R1', R="50 Ohm", p=None, n=None))
    R2 = voltage_divider.add(circuit.R(name='R2', R="50 Ohm", p=None, n=None))
    V = voltage_divider.add(circuit.V_Source(name='V', Vdc="1.0 V", Type='"V_DC"', SaveCurrent=1, p=None, n=None))

    voltage_divider.connect(V.n, voltage_divider.GND)
    voltage_divider.connect(V.p, R1.p)
    voltage_divider.connect(R1.n, R2.p)
    voltage_divider.connect(R2.n, voltage_divider.GND)
    voltage_divider.analyses.append(circuit.DC_Analysis(name='DC1'))
    voltage_divider.output_dataset = 'voltage_divider'

    print('Running circuit simulation')
    circuit_sim = ads.CircuitSimulator()
    circuit_sim.run_netlist(voltage_divider.generate_netlist(), output_dir=target_output_dir)
    output_data = dataset.Dataset(os.path.join(target_output_dir,'voltage_divider.ds'))
    print('Voltage at R1', output_data.values('DC1.DC',str(R1.p)))
    print('Voltage at R2', output_data.values('DC1.DC',str(R2.p)))
```


---

<!-- === 来源: Examples/ex_vsa_meas_demo.md === -->

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


---

<!-- === 来源: Examples/index.md === -->

# Examples[](#examples "Link to this heading")

* [Running EDA Toolbox Examples](Running%20Examples.md)
* [Example baluns](ex_baluns.md)
* [Example co optimize matching network](ex_co_optimize_matching_network.md)
* [Example create 3d empro serpentines](ex_create_3d_empro_serpentines.md)
* [Example dump workspace netlists](ex_dump_workspace_netlists.md)
* [Example empro extract resonance](ex_empro_extract_resonance.md)
* [Example high pass filter sub circuit](ex_high_pass_filter_sub_circuit.md)
* [Example import brd](ex_import_brd.md)
* [Example import ipc2581](ex_import_ipc2581.md)
* [Example import odb](ex_import_odb.md)
* [Example low pass filter](ex_low_pass_filter.md)
* [Example multi python](ex_multi_python.md)
* [Example odbpp simulate pipro ac reuse sio](ex_odbpp_simulate_pipro_ac_reuse_sio.md)
* [Example odbpp simulate pipro dc](ex_odbpp_simulate_pipro_dc.md)
* [Example odbpp simulate rfpro](ex_odbpp_simulate_rfpro.md)
* [Example optimize matching network](ex_optimize_matching_network.md)
* [Example pipro ac](ex_pipro_example_ac.md)
* [Example pipro dc](ex_pipro_example_dc.md)
* [Example quantumpro one qubit epr](ex_quantumpro_one_qubit_epr.md)
* [Example quantumpro one qubit freq](ex_quantumpro_one_qubit_freq.md)
* [Example rfpro stop nets](ex_rfpro_stop_nets.md)
* [Example run hb simulation](ex_run_hb_simulation.md)
* [Example run netlist](ex_run_netlist.md)
* [Example run netlist from disk](ex_run_netlist_from_disk.md)
* [Example run schematic](ex_run_schematic.md)
* [Example sipro automation](ex_sipro_automation.md)
* [Example sipro channelsim flow](ex_sipro_channelsim_flow.md)
* [Example sipro SI](ex_sipro_example_si.md)
* [Example sipro extract tdr](ex_sipro_extract_tdr.md)
* [Example sipro eye diagram](ex_sipro_eye_diagram.md)
* [Example sipro ploteye plotly](ex_sipro_ploteye_plotly.md)
* [Example sweep inductor values](ex_sweep_inductor_values.md)
* [Example systemvue basic](ex_systemvue_basic.md)
* [Example voltage divider](ex_voltage_divider.md)
* [Example vsa meas demo](ex_vsa_meas_demo.md)


---

