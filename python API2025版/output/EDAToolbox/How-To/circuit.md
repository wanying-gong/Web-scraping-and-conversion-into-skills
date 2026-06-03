<!-- 来源: How-To\circuit.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [How-To](index.md)
* Create a Circuit

1.2.4

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/How-To/circuit.rst.txt)

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
  + Create a Circuit
  + [Run a Circuit Simulation](circuit_sim.md)
  + [Create SIPro View and Run Simulation](sipro.md)
* [Release Notes](../release_notes/index.md)

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

On this page

[Previous

How-To](index.md)
[Next

Run a Circuit Simulation](circuit_sim.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top