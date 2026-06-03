<!-- 来源: How-To\circuit_sim.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [How-To](index.md)
* Run a Circuit Simulation

1.2.4

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/How-To/circuit_sim.rst.txt)

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

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
* [Initial Setup](../Initial_Setup/index.md)
  + [Installation](../Initial_Setup/installation.md)
  + [Prerequisites](../Initial_Setup/prerequisites.md)
  + [Verifying Installation](../Initial_Setup/verifying.md)
  + [SSH](../Initial_Setup/ssh.md)
* [Examples](../Examples/index.md)
* [How-To](index.md)
  + [Create a Circuit](circuit.md)
  + Run a Circuit Simulation
  + [Create SIPro View and Run Simulation](sipro.md)
* [Release Notes](../release_notes/index.md)

# Run a Circuit Simulation[](#run-a-circuit-simulation "Link to this heading")

This section will go through an example of how to run a circuit simulation on a schematic.

## Step 0: Get the example workspaces[](#step-0-get-the-example-workspaces "Link to this heading")

Download the example workspaces, or if you are familiar with the git revision control system, directly clone the whole directory to a working location.

The examples can be found on the [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

[![../_images/screenshot_download_examples.png](../_images/screenshot_download_examples.png)](../_images/screenshot_download_examples.png)

Assume you have put these files in your “f:/temp/edatoolbox” directory.

## Step 1: Creating the ADS application object[](#step-1-creating-the-ads-application-object "Link to this heading")

First, let’s make an ADS application object that gives access to a workspace and its contents. But even before that, import the `edatoolbox`

```
>>> from keysight.edatoolbox import ads, circuit, dataset
>>> from keysight.edatoolbox.util import safe_makedirs
>>> ads_application = ads.ADS()
```

## Step 2: Unarchiving[](#step-2-unarchiving "Link to this heading")

Next, we use the ads module to unarchive the workspace. Alternatively you can use this manually with tools like 7-zip.

```
>>> target_workspace_dir = r"f:\temp\edatoolbox\examples\scratch"
>>> ads_application.unarchive_workspace(r"f:\temp\edatoolbox\examples\data\run_schematic_wrk.7zads", target_workspace_dir)
```

## Step 3: Generating the netlist[](#step-3-generating-the-netlist "Link to this heading")

The EDA Toolbox makes a distinction between the circuit simulator application, the ADS platform and the netlists as concepts. The circuit simulator will accept a netlist and perform a simulation. The ADS platform is responsible for generating the netlist. If we want to work with the netlist we can turn it into a Circuit object and manipulate it, but that is optional. In our example will be take the circuit and modify one of the resistor values.

We will feed the circuit simulator with a netlist, so the first step is to generate the netlist.

```
>>> target_workspace = os.path.join(target_workspace_dir, 'run_schematic_wrk')
>>> netlist = ads_application.generate_netlist( target_workspace,
                    ads.LibraryCellView(library="run_schematic_lib",
                                        cell="voltage_divider",
                                        view="schematic") )
```

## Step 4: Working the circuit[](#step-4-working-the-circuit "Link to this heading")

Instead of just passing the netlist directly to the circuit simulator we investigate it and also change some of the values of the resistor.

```
>>> voltage_divider = circuit.Circuit(netlist)
>>> print(f'Existing value of R2.R={voltage_divider.R2.R}')
```

Let us also change the value of the resistor.

```
>>> voltage_divider.R2.R = '10 Ohm'
```

## Step 5: Run the simulation[](#step-5-run-the-simulation "Link to this heading")

At this point we are ready to run the circuit simulator by giving it the circuit we just modified. The circuit object called “voltage\_divider” and we need to generate the netlist for it.

```
>>> new_netlist = voltage_divider.generate_netlist()
```

In order to run the netlist we first create a circuit simulator object very similar to how we create the ADS application object.

```
>>> ads_circuitsim = ads.CircuitSimulator()
>>> safe_makedirs(r"f:\temp\edatoolbox\examples\scratch\output")
>>> ads_circuitsim.run_netlist(new_netlist, output_dir=r"f:\temp\edatoolbox\examples\scratch\output")
```

The Python command will complete when the circuit simulator is done.

## Step 6: Extract the results[](#step-6-extract-the-results "Link to this heading")

The final thing left to do is extract the results. For this we use the built-in dataset module of the edatoolbox. The API of keysight.edatoolbox.dataset matches that of the pydataset and pwdatatools. When the pydataset built-in to ADS is available the keysight.edatoolbox will internally use it for speeding up all access to the data. The advantage of the keysight.edatoolbox.dataset is that is available independently of the Python version you are using, as it is a pure Python module. For that it does give us some performance.

```
>>> output_data = dataset.Dataset(os.path.join(r'f:\temp\edatoolbox\examples\scratch\output','voltage_divider.ds'))
>>> print(f"Voltage at node 'in' {output_data.values('DC1.DC', 'in')[0]}V")
>>> print(f"Voltage at node 'out' {output_data.values('DC1.DC', 'out')[0]}V")
```

On this page

[Previous

Create a Circuit](circuit.md)
[Next

Create SIPro View and Run Simulation](sipro.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top