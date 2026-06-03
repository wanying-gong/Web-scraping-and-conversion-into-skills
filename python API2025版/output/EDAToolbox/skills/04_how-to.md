# How To
> **说明：** How To 相关页面。

> **何时使用：** 当你需要查阅 How To 相关内容时

---

## 本文件目录

- **Create a Circuit** (`How-To/circuit.md`)
- **Run a Circuit Simulation** (`How-To/circuit_sim.md`)
- **How-To** (`How-To/index.md`)
- **Create SIPro View and Run Simulation** (`How-To/sipro.md`)

---

<!-- === 来源: How-To/circuit.md === -->

# Create a Circuit[](#create-a-circuit "Link to this heading")

This section will go through an example of how to create a circuit from scratch and run a simulation on it and extract the results from it. In this example we will create a very simple RC low pass filter. If you have the matplotlib module available, then we will also show how to generate a plot of the response of the filter.

## Step 0: Getting ready[](#step-0-getting-ready "Link to this heading")

Import the module that we are going to use. At this point we only need the circuit module giving us access to a Circuit class and start building the actual circuit within Python.

```
>>> from keysight.edatoolbox import circuit
>>> low_pass_filter = circuit.Circuit()
```

## Step 1: Adding the components[](#step-1-adding-the-components "Link to this heading")

Next up is adding the components. There is a wide variety of components that can be added. We will just add 3 types here, a resistor, a component and finally also a voltage source. First up are the R and C components.

```
>>> R1 = low_pass_filter.add(circuit.R(name='R1', R="1 kOhm", p=None, n=None))
>>> C1 = low_pass_filter.add(circuit.C(name='C1', C="1 uF", p=None, n=None))
```

We add the components, given them a name, respectively ‘R1’ and ‘C1’. From the start we give them also a value of ‘1 kOhm’ and ‘1 uF’. Further we need to specify how the components will connect. However we don’t necessarily have to do it at this point, and we can’t. So for that reason we mark the ‘p’ and ‘n’ pin to remain unconnected, we do that by assigning ‘None’ to them. Later on we will connect the components to each other.

Finally we add a voltage source. We intend to do an AC analysis, so we add an AC voltage source:

```
>>> V = low_pass_filter.add(circuit.V_Source(name='V', Freq='freq', Vac='polar(1,0) V', Type='"V_AC"', p=None, n=None))
```

This one requires to use some of the more specifics of a voltage source in ADS netlist language. Critical is to mark the voltage source as an AC source by providing Type=‘“V\_AC”’, note that there is double quoting required!

## Step 2: Connecting the instances[](#step-2-connecting-the-instances "Link to this heading")

What is left is to connect all the instances together, essentially wiring all the instances to each other properly. Note that we will make use of the special .GND node part of any circuit we create.

The first line is will connect the negative pin of the voltage source V to the GND of the circuit.

```
>>> low_pass_filter.connect(V.n, low_pass_filter.GND)
```

Next up is connecting the positive pin of the voltage source V to the positive pin of resistor R1.

```
>>> low_pass_filter.connect(V.p, R1.p)
```

Finally we will connect the negative pin of the resistor R1 to the positive pin of the capacitor of C1. In the same way we finally connect the negative pin of C1 back to the GND node of the circuit.

```
>>> low_pass_filter.connect(R1.n, C1.p)
>>> low_pass_filter.connect(C1.n, low_pass_filter.GND)
```

## Step 3: Analysis?[](#step-3-analysis "Link to this heading")

A circuit has a list of instances, one of those instances could be a simulation controller and while the API does support that way of organizing the circuit, there is also another, more recommended way. To the circuit we can now add an analysis and configure it. It removes the need to go through all the specifics of adding sweep plan instance, option instances, etc.

Setting up an AC analysis is done by creating an AC analysis object, and configuring the desired frequency plan.

```
>>> ac_analysis = circuit.AC_Analysis(name='AC1')
>>> ac_analysis.sweep_plan.append(circuit.sweeps.LogarithmicSweep(1, 1e6, 5))
```

Finally we add the ac\_analysis object to the circuit, and selecting how the circuit simulator should call the resulting dataset. If we leave this blank the circuit simulator will pick a name, making it difficult later on to grab the dataset for reading it.

```
>>> low_pass_filter.analyses.append(ac_analysis)
>>> low_pass_filter.output_dataset = "low_pass_filter"
```

## Step 4: Run the simulation[](#step-4-run-the-simulation "Link to this heading")

Before we can run the simulation we need to import the remaining modules from the edatoolbox. In single script one would typically organize all the imports at the top, but in our example here we import piecemeal.

```
>>> from keysight.edatoolbox import ads
>>> from keysight.edatoolbox.util import safe_makedirs
```

Create now the circuit simulator application object to use to run a netlist. Our netlist comes from the Circuit object.

```
>>> circuit_sim = ads.CircuitSimulator()
>>> safe_makedirs('output')
>>> circuit_sim.run_netlist(low_pass_filter.generate_netlist(), output_dir='output')
```

## Step 5: Extracting and plotting results[](#step-5-extracting-and-plotting-results "Link to this heading")

When the simulation is done we need to extract the data and we are also going to plot it using the matplotlib module.

First step is to import modules we needed for this:

```
>>> import os
>>> import math
>>> from keysight.edatoolbox import dataset
>>> import matplotlib.pyplot as plt
```

Next up we read the dataset and bring it into Python and start with printing the values we find at the positive node of the C1 capacitor.

```
>>> output_data = dataset.Dataset(os.path.join('output','low_pass_filter.ds'))
>>> print('Response at C1', output_data.values('AC1.AC',str(C1.p)))
```

Optionally we also plot the results.

```
>>> import matplotlib.pyplot as plt
>>> response = [20.0*math.log10(abs(x)) for x in output_data.values('AC1.AC',str(C1.p))]
>>> plt.plot(response)
>>> plt.show()
```

Note, you may not have matplotlib available, so you can install it by using pip. For users on Windows, matplotlib can sometimes be problematic to install, especially on Python 3.10. There are several options in case you want to use matplotlib:

* install a pre-release package: py -m pip –pre matplotlib, this is the recommend way
* install a pre-release package: py -m pip matplotlib=3.5.0rc1 has been reported to work
* install seaborn and use seaborn, note that matplotlib is a dependency of seaborn so you may face similar issues
* use a Python distribution shipped with EMPro, IC-CAP or ADS. All of those have matplotlib pre-installed, ready to use!


---

<!-- === 来源: How-To/circuit_sim.md === -->

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


---

<!-- === 来源: How-To/index.md === -->

# How-To[](#how-to "Link to this heading")

* [Create a Circuit](circuit.md)
  + [Step 0: Getting ready](circuit.md#step-0-getting-ready)
  + [Step 1: Adding the components](circuit.md#step-1-adding-the-components)
  + [Step 2: Connecting the instances](circuit.md#step-2-connecting-the-instances)
  + [Step 3: Analysis?](circuit.md#step-3-analysis)
  + [Step 4: Run the simulation](circuit.md#step-4-run-the-simulation)
  + [Step 5: Extracting and plotting results](circuit.md#step-5-extracting-and-plotting-results)
* [Run a Circuit Simulation](circuit_sim.md)
  + [Step 0: Get the example workspaces](circuit_sim.md#step-0-get-the-example-workspaces)
  + [Step 1: Creating the ADS application object](circuit_sim.md#step-1-creating-the-ads-application-object)
  + [Step 2: Unarchiving](circuit_sim.md#step-2-unarchiving)
  + [Step 3: Generating the netlist](circuit_sim.md#step-3-generating-the-netlist)
  + [Step 4: Working the circuit](circuit_sim.md#step-4-working-the-circuit)
  + [Step 5: Run the simulation](circuit_sim.md#step-5-run-the-simulation)
  + [Step 6: Extract the results](circuit_sim.md#step-6-extract-the-results)
* [Create SIPro View and Run Simulation](sipro.md)
  + [Step 0: Get the example workspaces](sipro.md#step-0-get-the-example-workspaces)
  + [Step 1: Creating the ADS application object](sipro.md#step-1-creating-the-ads-application-object)
  + [Step 2: Unarchiving](sipro.md#step-2-unarchiving)
  + [Step 3: Creating the SIPro view](sipro.md#step-3-creating-the-sipro-view)
  + [Step 4: Loading the SIPro view into the SIPro tool](sipro.md#step-4-loading-the-sipro-view-into-the-sipro-tool)
  + [Step 5: Creating an Analysis](sipro.md#step-5-creating-an-analysis)
  + [Step 6: Running an Analysis](sipro.md#step-6-running-an-analysis)
  + [Step 7: Extracting some results](sipro.md#step-7-extracting-some-results)


---

<!-- === 来源: How-To/sipro.md === -->

# Create SIPro View and Run Simulation[](#create-sipro-view-and-run-simulation "Link to this heading")

This section will go through an example of how to run a SIPro simulation, starting from a zipped workspace.

## Step 0: Get the example workspaces[](#step-0-get-the-example-workspaces "Link to this heading")

Download the example workspaces, or if you are familiar with the git revision control system, directly clone the whole directory to a working location.

The examples can be found on the [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

Assume you have put these files in your “f:/temp/edatoolbox” directory.

## Step 1: Creating the ADS application object[](#step-1-creating-the-ads-application-object "Link to this heading")

First, let’s make an ADS application object that gives access to a workspace and its contents. But even before that, import the `edatoolbox`

```
>>> from keysight.edatoolbox import ads, momentum, xxpro
>>> ads_application = ads.ADS()
```

## Step 2: Unarchiving[](#step-2-unarchiving "Link to this heading")

Next, we use the ads module to unarchive the workspace. Alternatively you can use this manually with tools like 7-zip.

```
>>> target_workspace_dir = r"f:\temp\edatoolbox\examples\scratch"
>>> ads_application.unarchive_workspace(r"f:\temp\edatoolbox\examples\data\SIPro_PIPro_DDR4_wrk.7zads", target_workspace_dir)
```

## Step 3: Creating the SIPro view[](#step-3-creating-the-sipro-view "Link to this heading")

Now that we have unarchived the workspace, we want to create the SIPro view. To achieve this we define our input LibraryCellView and SIPro LibraryCellView.

```
>>> input_lcv = ads.LibraryCellView( library = "PC4-RDIMM_V090_RC_F0_20131106_lib",
...                                  cell = "PC4-RDIMM_V090_RC_F0_20131106",
...                                  view = "layout")
>>> sipro_lcv = ads.LibraryCellView( library = "PC4-RDIMM_V090_RC_F0_20131106_lib",
...                                  cell = "PC4-RDIMM_V090_RC_F0_20131106",
...                                  view = "sipro")
```

And we use our ads\_application to create the SIPro view.

```
>>> import os
>>> target_workspace = os.path.join(target_workspace_dir, "SIPro_PIPro_DDR4_wrk")
>>> ads_application.create_pro_view( target_workspace,
...                                  input_lcv = input_lcv,
...                                  substrate = "PC4-RDIMM_V090_RC_F0_20131106",
...                                  pro_lcv = sipro_lcv,
...                                  tool = "sipi")
```

## Step 4: Loading the SIPro view into the SIPro tool[](#step-4-loading-the-sipro-view-into-the-sipro-tool "Link to this heading")

In this step, we will start using SIPro’s built-in python API, so we will need to import `empro`

```
>>> import empro
>>> import empro.toolkit
>>> import empro.toolkit.analysis
```

At this point, we have created the SIPro view, but in order to start using SIPro we still need to properly configure it.

First, we will first tell SIPro what momentum to use, using the `edatoolbox`

```
>>> momentum_dir = momentum.get_momentum_location()
>>> empro.toolkit.analysis.setMomentumDir(momentum_dir)
```

Next, we tell SIPro what workspace we are currently using.

```
>>> os.environ['HPEESOF_DIR'] = ads.get_ads_location()  # ensure the referenced env vars in lib.defs can be found
>>> xxpro.use_workspace(target_workspace)
```

Finally, we can load the SIPro view into the SIPro tool and save the SIPro project.

```
>>> xxpro.load_pro_view(sipro_lcv)
>>> empro.activeProject.saveActiveProject()
```

## Step 5: Creating an Analysis[](#step-5-creating-an-analysis "Link to this heading")

Now we are ready to create an Analysis, we will name it “Test”. Use the `empro.analysis.Analysis.PASIAnalysisType` as a first argument, to make sure it will be a Power-Aware-SI Analysis.

```
>>> analysis = empro.analysis.Analysis(empro.analysis.Analysis.PASIAnalysisType, "Test")
```

Let’s define all the ports using the convention: `(port_name, list_of_plus_pin_names, list_of_min_pin_names)`.

```
>>> port_definitions = [ ('DQ00_J1', ['J1.P_5'], ['J1.P_6']),
...                      ('DQ00R_U19', ['U19.P_D3'], ['U19.P_D1']),
...                      ('DQ01_J1',['J1.P_150'],['J1.P_149']),
...                      ('DQ01R_U19',['U19.P_C2'],['U19.P_D1']),
...                      ('DQ02_J1',['J1.P_12'],['J1.P_11']),
...                      ('DQ02R_U19',['U19.P_D7'],['U19.P_C8']),
...                      ('DQ03_J1',['J1.P_157'],['J1.P_156']),
...                      ('DQ03R_U19',['U19.P_B7'],['U19.P_C8'])]
```

To aid us, we will define a helper function to get the `empro.geometry.Pin` object from the `layout`.

```
>>> def pin_from_name(layout, name):
...     try:
...         inst_name, pin_name = name.split(".")
...         return layout.instances[inst_name].instPin(pin_name)
...     except ValueError:
...         return layout.topLevelPins[name]
```

Now we can add the ports to the Analysis.

```
>>> layout = empro.activeProject.layout
>>> for port_def in port_definitions:
...     name, plus_pins, minus_pins = port_def
...     plus_pins = [pin_from_name(layout, name) for name in plus_pins]
...     minus_pins = [pin_from_name(layout, name) for name in minus_pins]
...     port = empro.analysis.Port(plus_pins,minus_pins, name)
...     analysis.ports.append(port)
```

Next, we add the components and set a model for the components to use.

```
>>> component_model_group = empro.analysis.ComponentModelGroup(layout.components['PC4-RDIMM_V090_RC_F0_20131106_lib:rn_2pos_respack_2x0201-510-501140a_15'])
>>> component_model_group.arrayedComponent = True
>>> component_model_group.pinPortMap().update( [('P_1', 1), ('P_2', 2), ('P_3', -2), ('P_4', -1)] )
>>> for instance_name in ['RN95', 'RN97']:
...     component_model_group.appendInstance(empro.analysis.ComponentInstance(layout.instances[instance_name]))

>>> component_model = empro.analysis.ComponentModel(empro.components.RLCSpecification('lumped','15 Ohm',0,0,'Series') )
>>> component_model_group.appendModel(component_model)
>>> analysis.componentModelGroups.append(component_model_group)
```

Finally, we add all the required nets to the Analysis.

```
>>> for net in analysis.requiredNets():
...     analysis.nets.append(net)
```

Now that the Analysis is complete, don’t forget to add it to the activeProject.

```
>>> empro.activeProject.analyses.append(analysis)
```

## Step 6: Running an Analysis[](#step-6-running-an-analysis "Link to this heading")

The previous step actually adds a clone of `analysis` to the activeProject’s analyses list. If we want to be able to view the results afterwards using the SIPro GUI, we need to make sure we run the Analysis that was actually added to the analyses list.

```
>>> active_analysis = empro.activeProject.analyses[-1]
```

Next, we run, wait for completion, and save `active_analysis`.

```
>>> empro.toolkit.analysis.runAnalysis(active_analysis, waitForConfirmation=False, saveProject=True)
>>> empro.activeProject.simulations.isQueueHeld = False
>>> active_simulation = empro.activeProject.simulations[-1]
>>> empro.toolkit.simulation.wait(active_simulation)
>>> empro.activeProject.saveActiveProject()
```

These commands might take some time, depending on the machine you are using.

## Step 7: Extracting some results[](#step-7-extracting-some-results "Link to this heading")

In this final step, we will extract the S21 data and write it to a csv-file. First we grab the datasets.

```
>>> res = empro.analysis.CircuitResults(active_analysis)
>>> freqs = list(res.frequencies())
>>> S21_mag = res.Src(1,0,"ComplexMagnitude")
>>> S21_phase = res.Src(1,0,"Phase")
```

The dataset in `Src` (S-row-column) are 0 indexed, so S21 is accessed as row 1, column 0.

Now we can open a csv file and write the S parameter data to it.

```
>>> output_file = os.path.join(target_workspace_dir, "sparams.csv")
>>> with open(output_file,"w") as file:
...     line = ",".join(["Frequency", "S21 (mag)", "S21 (phase)"])
...     file.write(line + "\n")
...     for i in range(len(freqs)):
...         line = f"{freqs[i]},{S21_mag[i]},{S21_phase[i]}"
...         file.write(line + "\n")
```


---

