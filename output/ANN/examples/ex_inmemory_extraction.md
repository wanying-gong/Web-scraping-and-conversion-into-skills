<!-- 来源: examples\ex_inmemory_extraction.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ANN Python Documentation](../index.md)
* [Examples](index.md)
* In-memory Extraction

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
  + [Basic Extraction and Simulation](ex_basic.md)
  + In-memory Extraction
  + [Training with Error Weighting](ex_training_error_weighting.md)

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

On this page

[Previous

Basic Extraction and Simulation](ex_basic.md)
[Next

Training with Error Weighting](ex_training_error_weighting.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top