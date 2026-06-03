<!-- 来源: examples\ex_basic.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ANN Python Documentation](../index.md)
* [Examples](index.md)
* Basic Extraction and Simulation

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../intro/index.md)
  + [Licensing](../intro/licensing.md)
  + [Using ANN Functionality in Python](../intro/usage.md)
  + [Using Visual Studio Code](../intro/vscode.md)
* [Reference](../reference/index.md)
  + [keysight.ads.ann](../reference/ann/index.md)
    - [AnnSetup](../reference/ann/annsetup.md)
    - [NeuronActivationFunctionType](../reference/ann/neuronactivationfunctiontype.md)
    - [OutputActivationFunctionType](../reference/ann/outputactivationfunctiontype.md)
    - [NetworkTrainingType](../reference/ann/networktrainingtype.md)
    - [NetworkInitializationMethod](../reference/ann/networkinitializationmethod.md)
    - [OutputFormat](../reference/ann/outputformat.md)
    - [ModelerOptimizer](../reference/ann/modeleroptimizer.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
  + [How to Use Pytest](../howto/pytest.md)
* [Examples](index.md)
  + Basic Extraction and Simulation
  + [In-memory Extraction](ex_inmemory_extraction.md)
  + [Training with Error Weighting](ex_training_error_weighting.md)

# Basic Extraction and Simulation[](#basic-extraction-and-simulation "Link to this heading")

This example demonstrates basic setup followed by extraction and simulation utilizing the ANN interface.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright Keysight Technologies 2024

import keysight.ads.ann as ann

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_input_datafile() -> str:
    d = {"x": [1, 2, 3, 4, 5], "y": [1, 4, 9, 16, 25]}
    df = pd.DataFrame(data=d)
    name = r"in.txt"
    np.savetxt(name, df.values, fmt="%d")
    return name

def generate_simulation_datafile() -> str:
    d = {"x": [2.5, 3.5, 6]}
    df = pd.DataFrame(data=d)
    name = r"sim.txt"
    np.savetxt(name, df.values, fmt="%d")
    return name

def get_file_data(file_name: str) -> list[float]:
    ret = []
    with open(file_name) as output_file:
        while line := output_file.readline():
            ret.append([float(elem) for elem in line.split()])
    return ret

# in this example, the input file are manually created
input_file = generate_input_datafile()
simulation_file = generate_simulation_datafile()

# Configure the ANN for training
num_inputs = 1
num_outputs = 1 # i.e. prediction values
setup = ann.AnnSetup(num_inputs, num_outputs)
# for reproducibility
setup.seed = 1234
setup.num_neurons_per_layer = 10
setup.neuron_activation_function_type = ann.NeuronActivationFunctionType.SIGMOID

ann.configure_setup(setup)
ann.extract_model(input_file, r"model.txt")
ann.simulate_model(r"out.txt", simulation_file)

data = get_file_data("out.txt")

print(data)
#plt.plot(data)
#plt.show()
```

## Import Modules[](#import-modules "Link to this heading")

To setup the environment, you need to import the following modules:

```
import keysight.ads.ann as ann
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

## Generate the Input Data File[](#generate-the-input-data-file "Link to this heading")

In this example, input files are manually created. Use the following snippet to create the input files.

```
input_file = generate_input_datafile()
simulation_file = generate_simulation_datafile()
```

The generate\_input\_datafile() generates the input datafile. The following snippet is the defintition of the generate\_input\_datafile().

```
def generate_input_datafile() -> str:
    d = {"x": [1, 2, 3, 4, 5], "y": [1, 4, 9, 16, 25]}
    df = pd.DataFrame(data=d)
    name = r"in.txt"
    np.savetxt(name, df.values, fmt="%d")
    return name
```

The generate\_simulation\_datafile() generates the simulation datafile. The following snippet is the defintition of the generate\_simulation\_datafile().

```
def generate_simulation_datafile() -> str:
    d = {"x": [2.5, 3.5, 6]}
    df = pd.DataFrame(data=d)
    name = r"sim.txt"
    np.savetxt(name, df.values, fmt="%d")
    return name
```

## Get the Output File[](#get-the-output-file "Link to this heading")

The following snippet is used to get the output file.

```
def get_file_data(file_name: str) -> list[float]:
    ret = []
    with open(file_name) as output_file:
        while line := output_file.readline():
            ret.append([float(elem) for elem in line.split()])
    return ret
```

## Configure ANN For Training[](#configure-ann-for-training "Link to this heading")

The following snippet is used to configure ANN for training.

```
num_inputs = 1
num_outputs = 1 # i.e. prediction values
setup = ann.AnnSetup(num_inputs, num_outputs)
# for reproducibility
setup.seed = 1234
setup.num_neurons_per_layer = 10
setup.neuron_activation_function_type = ann.NeuronActivationFunctionType.SIGMOID
ann.configure_setup(setup)
```

## Generate the Output[](#generate-the-output "Link to this heading")

The following snippet is used to generate the output of ANN training.

```
ann.extract_model(input_file, r"model.txt")
ann.simulate_model(r"out.txt", simulation_file)
data = get_file_data("out.txt")
print(data)
```

On this page

[Previous

Examples](index.md)
[Next

In-memory Extraction](ex_inmemory_extraction.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top