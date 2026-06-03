<!-- 来源: Examples\ex_create_3d_empro_serpentines.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Examples](index.md)
* Example create 3d empro serpentines

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Examples/ex_create_3d_empro_serpentines.rst.txt)

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
  + Example create 3d empro serpentines
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

On this page

[Previous

Example co optimize matching network](ex_co_optimize_matching_network.md)
[Next

Example dump workspace netlists](ex_dump_workspace_netlists.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top