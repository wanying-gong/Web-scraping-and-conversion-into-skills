# Examples
> **说明：** Examples 相关页面。

> **何时使用：** 当你需要查阅 Examples 相关内容时

---

## 本文件目录

- **Basic Extraction and Simulation** (`examples/ex_basic.md`)
- **In-memory Extraction** (`examples/ex_inmemory_extraction.md`)
- **Training with Error Weighting** (`examples/ex_training_error_weighting.md`)
- **Examples** (`examples/index.md`)

---

<!-- === 来源: examples/ex_basic.md === -->

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


---

<!-- === 来源: examples/ex_inmemory_extraction.md === -->

# In-memory Extraction[](#in-memory-extraction "Link to this heading")

This example demonstrates simulating a model with in-memory pandas dataframes.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
# Copyright Keysight Technologies 2024
import numpy as np
import pandas as pd
import keysight.ads.ann as ann

# Create training dataset
sine_wave_freq = 1e6
sampling_freq = 10 * sine_wave_freq
signal_duration = 10/sine_wave_freq
sample_period = 1.0/sampling_freq
num_of_samples = signal_duration/sample_period
time = np.arange(0, num_of_samples) * sample_period
x = np.sin(2 * np.pi * sine_wave_freq * time)
data = np.column_stack((time, x))

# Create training dataframe
training_df = pd.DataFrame(data)
print("The training data looks like\n", training_df.head())

# Configure the ANN
num_inputs = 1
num_outputs = 1 # i.e. prediction values
setup = ann.AnnSetup(num_inputs, num_outputs)

setup.num_hidden_layers = 2 # Generally 2 layers is enough for EDA curve fittings
setup.num_neurons_per_layer = 20 # Increase this number to increase model complexity
setup.neuron_activation_function_type = ann.NeuronActivationFunctionType.HYPERBOLIC_TANGENT
setup.network_training_type = ann.NetworkTrainingType.STANDARD # Please refer to the documentation for the (ADJOINT) cases
setup.modeler_optimizer = ann.ModelerOptimizer.QUASI_NEWTON # Chose BAYESIAN_REGULARIZATION at a cost of training speed for improved overfitting handelings
setup.max_training_iterations = 500 # Increase this number to increase training epochs
setup.training_stop_tolerance = 0 # RMSE loss to trigger early stopping

# Use 'ALL' to get all available ANN outputs (Verilog-A, C module, equation, struct, and scale)
setup.output_format = ann.OutputFormat.ALL

ann.configure_setup(setup)

# Train the model
output_df = ann.auxiliary_functions.extract_inmemory(
    input_data=training_df,
    input_columns=[0], # The indices of input columns (or you can use labels, e.g. ["col1", "col2"])
    output_columns = [1], # Optional: The indices of output columns. If you don't specify the output_columns, all non-input_columns will be treated as outputs
    ann_saving_names = "mytest", # Optional: name for ANN Output files
)

# Examine training outputs
print("The output dataframe looks like\n", output_df.head())

# ANN also offers convinent continuous training/simulation options based on trained ANN networks.abs

# For example, by running the scripts above, we should have files named "mytest.struc" and "mytest.scale" stored in our training directory
# Since we configured the setup.output_format to "ALL", you will see more ANN model files such as
# "mytest.c" (for C-consumptions), "mytest.equation" (a txt equation file),
# "mytest.inc" (for VA-consumptions), "mytest.scale" (for internal usages), and "mytest.struc" (for internal usages).
# To pick-up a trained ANN model using this ANN Python module, we will use the "mytest.scale" and "mytest.struc" files

# Create a fresh ANN setup object
fresh_setup = ann.AnnSetup(5, 5) # The values num_inputs and num_outputs do not matter, they will be overriden when we do "ann.configure_setup(fresh_setup)"
fresh_setup.existing_file = "mytest.struc" # ANN will automatically handle the .scale file
ann.configure_setup(fresh_setup) # Configure the ANN with the fresh setup

# Now this fresh_setup will have every configurations automatically loaded. We simply need to call
# the simulate_inmemory function for a simulation, or extract_inmemory for continious trainings (of course we need to give a training dataframe for extractions)

# Let's do a simulation:
input_df = df = pd.DataFrame([[1e-7], [2e-7]]) # One column only, since the previously trained ANN only accepts 1 input
print("The simulation input df looks like\n", input_df.head())

simulated_df = ann.auxiliary_functions.simulate_inmemory(
    input_df,
    input_columns = None, # If we don't specify the "input_columns", ANN will treat the entire input_df as the inputs (num_inputs = number of columns)
)

print("The simulation output looks like\n", simulated_df.head())
```

## Import Modules[](#import-modules "Link to this heading")

To setup the environment, you need to import the following modules:

```
import numpy as np
import pandas as pd
import keysight.ads.ann as ann
```

## Create ANN Dataset for Training[](#create-ann-dataset-for-training "Link to this heading")

The ANN can be trained on any given number of inputs and one output. As such, it’s possible to create datasets for the training with different numbers of inputs.
The following snippet creates the ANN dataset for training.

```
# Create training dataset
sine_wave_freq = 1e6
sampling_freq = 10 * sine_wave_freq
signal_duration = 10/sine_wave_freq
sample_period = 1.0/sampling_freq
num_of_samples = signal_duration/sample_period
time = np.arange(0, num_of_samples) * sample_period
x = np.sin(2 * np.pi * sine_wave_freq * time)
data = np.column_stack((time, x))
```

## Create Training Dataframe[](#create-training-dataframe "Link to this heading")

Training a Dataframe involves using a dataframe to teach the neural network to recognize patterns and make predictions.

```
# Create training dataframe
training_df = pd.DataFrame(data)
print("The training data looks like\n", training_df.head())
```

## Configure ANN for Training[](#configure-ann-for-training "Link to this heading")

The following snippet configures ANN for training.

```
num_inputs = 1
num_outputs = 1 # i.e. prediction values
setup = ann.AnnSetup(num_inputs, num_outputs)
setup.num_hidden_layers = 2 # Generally 2 layers is enough for EDA curve fittings
setup.num_neurons_per_layer = 20 # Increase this number to increase model complexity
setup.neuron_activation_function_type = ann.NeuronActivationFunctionType.HYPERBOLIC_TANGENT
setup.network_training_type = ann.NetworkTrainingType.STANDARD # Please refer to the documentation for the (ADJOINT) cases
setup.modeler_optimizer = ann.ModelerOptimizer.QUASI_NEWTON # Chose BAYESIAN_REGULARIZATION at a cost of training speed for improved overfitting handelings
setup.max_training_iterations = 500 # Increase this number to increase training epochs
setup.training_stop_tolerance = 0 # RMSE loss to trigger early stopping
setup.output_format = ann.OutputFormat.ALL
ann.configure_setup(setup)
```

## Train ANN Model[](#train-ann-model "Link to this heading")

The following snippet trains ANN model.

```
output_df = ann.auxiliary_functions.extract_inmemory(
    input_data=training_df,
    input_columns=[0], # The indices of input columns (or you can use labels, e.g. ["col1", "col2"])
    output_columns = [1], # Optional: The indices of output columns. If you don't specify the output_columns, all non-input_columns will be treated as outputs
    ann_saving_names = "mytest", # Optional: name for ANN Output files
)
print("The output dataframe looks like\n", output_df.head())
```

By running the above code, we should have files named *mytest.struc* and *mytest.scale* stored in our training directory.
Since we configured the setup.output\_format to “ALL”, you will see more ANN model files such as *mytest.c* (for C-consumptions), *mytest.equation* (a txt equation file),
*mytest.inc* (for VA-consumptions), *mytest.scale* (for internal usages), and *mytest.struc* (for internal usages). To pick-up a trained ANN model using this ANN Python module, we will use the *mytest.scale* and *mytest.struc* files.

## Configure the ANN with a Fresh Setup[](#configure-the-ann-with-a-fresh-setup "Link to this heading")

The following snippet creates a fresh ANN Setup object.

```
fresh_setup = ann.AnnSetup(5, 5) # The values num_inputs and num_outputs do not matter, they will be overriden when we do "ann.configure_setup(fresh_setup)"
fresh_setup.existing_file = "mytest.struc" # ANN will automatically handle the .scale file
ann.configure_setup(fresh_setup) # Configure the ANN with the fresh setup
```

The above code configures the ANN with the fresh setup. Now, the fresh setup will automatically load every configuration.

## Run a Simulation[](#run-a-simulation "Link to this heading")

Use the below snippet to simulate a fresh ANN setup.

```
input_df = df = pd.DataFrame([[1e-7], [2e-7]]) # One column only, since the previously trained ANN only accepts 1 input
print("The simulation input df looks like\n", input_df.head())
simulated_df = ann.auxiliary_functions.simulate_inmemory(
    input_df,
    input_columns = None, # If we don't specify the "input_columns", ANN will treat the entire input_df as the inputs (num_inputs = number of columns)
)
print("The simulation output looks like\n", simulated_df.head())
```


---

<!-- === 来源: examples/ex_training_error_weighting.md === -->

# Training with Error Weighting[](#training-with-error-weighting "Link to this heading")

This example demonstrates training a model with error weighting.

## Example Code[](#example-code "Link to this heading")

The complete example code is given below:

```
 1# Copyright Keysight Technologies 2024
 2import keysight.ads.ann as ann
 3
 4import numpy as np
 5import pandas as pd
 6
 7# Training error weighting file is an interesting topic and it is useful when you want to assign
 8# more weights to specific data points
 9
10# Let's create an simple example. We will first create a basic ANN setup and
11# train it with only 2 iterations, so the accuracy is low
12
13num_inputs = 1
14num_outputs = 1 # i.e. prediction values
15setup = ann.AnnSetup(num_inputs, num_outputs)
16setup.max_training_iterations = 2
17setup.seed = 1234
18setup.num_neurons_per_layer = 10
19setup.neuron_activation_function_type = ann.NeuronActivationFunctionType.SIGMOID
20ann.configure_setup(setup)
21
22# Then we create a basic training data. Basically we are fitting for y=x^2
23training_df = pd.DataFrame(
24    {
25        "Input": range(1, 5),
26        "Output": [i**2 for i in range(1, 5)],
27    }
28)
29print("The training data looks like\n", training_df.head())
30
31output_df = ann.auxiliary_functions.extract_inmemory(
32    input_data=training_df,
33    input_columns=[0],
34)
35
36# Since we only trained for 2 iterations, the fitting result won't be good
37print("The output dataframe looks like\n", output_df.head())
38
39# Now let's write a training error weighting file. It should have the same rows as our inputs,
40# and same columns as our num_inputs. We will simply make a point-wise multiplication between
41# the training error weighting file and the input data to assign weights.abs
42
43# For example, let's set all other training error weights to 1 and the weight for the last data point to 100.
44weighting_df = pd.DataFrame(
45    [1, 1, 1, 100]
46)
47
48# Then we save it as a space-deliminited txt file:
49name = r"training_error_weighting_example.txt"
50np.savetxt(name, weighting_df.values, fmt="%d")
51
52# Now lets use the same setup, but with the training error weighting file configured:
53setup.training_error_weighting_file = name
54ann.configure_setup(setup)
55
56# This time, we should observe that the fitting for the last data point (x=54, y=16) gets better
57new_output_df = ann.auxiliary_functions.extract_inmemory(
58    input_data=training_df,
59    input_columns=[0],
60)
61print("The output dataframe with 'training_error_weighting_file' configured looks like \n", new_output_df.head())
```

## Import Modules[](#import-modules "Link to this heading")

To setup the environment, you need to import the following modules:

```
import keysight.ads.ann as ann
import numpy as np
import pandas as pd
```

## Create an ANN setup[](#create-an-ann-setup "Link to this heading")

Below snippet creates a basic ANN setup which is trained with only 2 iterations, so the accuracy is low.

```
num_inputs = 1
num_outputs = 1 # i.e. prediction values
setup = ann.AnnSetup(num_inputs, num_outputs)
setup.max_training_iterations = 2
setup.seed = 1234
setup.num_neurons_per_layer = 10
setup.neuron_activation_function_type = ann.NeuronActivationFunctionType.SIGMOID
ann.configure_setup(setup)
```

## Create a Training Data[](#create-a-training-data "Link to this heading")

Below snippet creates a basic training data.

```
training_df = pd.DataFrame(
    {
        "Input": range(1, 5),
        "Output": [i**2 for i in range(1, 5)],
    }
)
print("The training data looks like\n", training_df.head())
output_df = ann.auxiliary_functions.extract_inmemory(
    input_data=training_df,
    input_columns=[0],
)
print("The output dataframe looks like\n", output_df.head())
```

## Create a Training Weighting File[](#create-a-training-weighting-file "Link to this heading")

Below snippet creates a training weighting file.

```
weighting_df = pd.DataFrame(
    [1, 1, 1, 100]
)
name = r"training_error_weighting_example.txt"
np.savetxt(name, weighting_df.values, fmt="%d")
```

## Configure ANN with the Training Error Weighted File[](#configure-ann-with-the-training-error-weighted-file "Link to this heading")

Below snippet configures ANN with the training error weighting file.

```
setup.training_error_weighting_file = name
ann.configure_setup(setup)
```

## Generate the Output[](#generate-the-output "Link to this heading")

Below snippet generates the output with a training error weighting file.

```
new_output_df = ann.auxiliary_functions.extract_inmemory(
    input_data=training_df,
    input_columns=[0],
)
print("The output dataframe with 'training_error_weighting_file' configured looks like \n", new_output_df.head())
```


---

<!-- === 来源: examples/index.md === -->

# Examples[](#examples "Link to this heading")

Contents:

* [Basic Extraction and Simulation](ex_basic.md)
  + [Example Code](ex_basic.md#example-code)
  + [Import Modules](ex_basic.md#import-modules)
  + [Generate the Input Data File](ex_basic.md#generate-the-input-data-file)
  + [Get the Output File](ex_basic.md#get-the-output-file)
  + [Configure ANN For Training](ex_basic.md#configure-ann-for-training)
  + [Generate the Output](ex_basic.md#generate-the-output)
* [In-memory Extraction](ex_inmemory_extraction.md)
  + [Example Code](ex_inmemory_extraction.md#example-code)
  + [Import Modules](ex_inmemory_extraction.md#import-modules)
  + [Create ANN Dataset for Training](ex_inmemory_extraction.md#create-ann-dataset-for-training)
  + [Create Training Dataframe](ex_inmemory_extraction.md#create-training-dataframe)
  + [Configure ANN for Training](ex_inmemory_extraction.md#configure-ann-for-training)
  + [Train ANN Model](ex_inmemory_extraction.md#train-ann-model)
  + [Configure the ANN with a Fresh Setup](ex_inmemory_extraction.md#configure-the-ann-with-a-fresh-setup)
  + [Run a Simulation](ex_inmemory_extraction.md#run-a-simulation)
* [Training with Error Weighting](ex_training_error_weighting.md)
  + [Example Code](ex_training_error_weighting.md#example-code)
  + [Import Modules](ex_training_error_weighting.md#import-modules)
  + [Create an ANN setup](ex_training_error_weighting.md#create-an-ann-setup)
  + [Create a Training Data](ex_training_error_weighting.md#create-a-training-data)
  + [Create a Training Weighting File](ex_training_error_weighting.md#create-a-training-weighting-file)
  + [Configure ANN with the Training Error Weighted File](ex_training_error_weighting.md#configure-ann-with-the-training-error-weighted-file)
  + [Generate the Output](ex_training_error_weighting.md#generate-the-output)


---

