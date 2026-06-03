<!-- 来源: examples\ex_training_error_weighting.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ANN Python Documentation](../index.md)
* [Examples](index.md)
* Training with Error Weighting

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
  + [In-memory Extraction](ex_inmemory_extraction.md)
  + Training with Error Weighting

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

On this page

[Previous

In-memory Extraction](ex_inmemory_extraction.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top