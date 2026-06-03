# ANN Python Documentation Knowledge Base
> 本文件由 MarkItDown 自动转换，BFS 遍历自 Keysight ADS2025 Update 2 ANN Python Documentation HTML 文档。
> 共 23 个页面。

---

## 目录 (Table of Contents)

1. [index.md](#index)
2. [intro\index.md](#intro--index)
3. [intro\licensing.md](#intro--licensing)
4. [intro\usage.md](#intro--usage)
5. [intro\vscode.md](#intro--vscode)
6. [reference\index.md](#reference--index)
7. [reference\ann\index.md](#reference--ann--index)
8. [reference\ann\annsetup.md](#reference--ann--annsetup)
9. [reference\ann\neuronactivationfunctiontype.md](#reference--ann--neuronactivationfunctiontype)
10. [reference\ann\outputactivationfunctiontype.md](#reference--ann--outputactivationfunctiontype)
11. [reference\ann\networktrainingtype.md](#reference--ann--networktrainingtype)
12. [reference\ann\networkinitializationmethod.md](#reference--ann--networkinitializationmethod)
13. [reference\ann\outputformat.md](#reference--ann--outputformat)
14. [reference\ann\modeleroptimizer.md](#reference--ann--modeleroptimizer)
15. [howto\index.md](#howto--index)
16. [howto\venv.md](#howto--venv)
17. [howto\newvenv.md](#howto--newvenv)
18. [howto\existingvenv.md](#howto--existingvenv)
19. [howto\pytest.md](#howto--pytest)
20. [examples\index.md](#examples--index)
21. [examples\ex_basic.md](#examples--ex_basic)
22. [examples\ex_inmemory_extraction.md](#examples--ex_inmemory_extraction)
23. [examples\ex_training_error_weighting.md](#examples--ex_training_error_weighting)

---



---

## 1. index.md {#index}

# ANN Python documentation[](#ann-python-documentation "Link to this heading")

Contents:

* [Introduction](intro/index.md)
  + [Licensing](intro/licensing.md)
  + [Using ANN Functionality in Python](intro/usage.md)
  + [Using Visual Studio Code](intro/vscode.md)
* [Reference](reference/index.md)
  + [keysight.ads.ann](reference/ann/index.md)
* [How-To](howto/index.md)
  + [How to Set Up a Python Virtual Environment](howto/venv.md)
  + [How to Use Pytest](howto/pytest.md)
* [Examples](examples/index.md)
  + [Basic Extraction and Simulation](examples/ex_basic.md)
  + [In-memory Extraction](examples/ex_inmemory_extraction.md)
  + [Training with Error Weighting](examples/ex_training_error_weighting.md)


---

## 2. intro\index.md {#intro--index}

# Introduction[](#introduction "Link to this heading")

* [Licensing](licensing.md)
* [Using ANN Functionality in Python](usage.md)
* [Using Visual Studio Code](vscode.md)


---

## 3. intro\licensing.md {#intro--licensing}

# Licensing[](#licensing "Link to this heading")

Importing `keysight.ads.ann` pulls a **Harmonic Balance** license. Note that the license is held for the entirety of the Python session and only releases when the Python session ends.

To release the license without closing the current Python session, call `ann.release_module()`. This will release the **Harmonic Balance** license. However, any calls to extract, simulate, or train the module will throw until a license is reacquired. To reacquire the license, call `ann.init_module()`.


---

## 4. intro\usage.md {#intro--usage}

# Using ANN Functionality in Python[](#using-ann-functionality-in-python "Link to this heading")

A Python script running outside ADS can access functionality of ANN.

```
from keysight.ads import ann

ann.version()
```

The `keysight.ads.ann` package is not currently available as a pip-installable package.
To get access to this package, use any one of these approaches:

> 1. Use the Python interpreter in `$HPEESOF_DIR/tools/python`.
> 2. Create a virtual environment based on that interpreter. See [How to Set Up a Python Virtual Environment](../howto/venv.md).
> 3. Add `$HPEESOF_DIR/tools/python/packages` onto your Python’s `sys.path`.

Set the environment variable `HPEESOF_DIR` to point to your ADS installation prior to
using the `keysight.ads.ann` package.


---

## 5. intro\vscode.md {#intro--vscode}

# Using Visual Studio Code[](#using-visual-studio-code "Link to this heading")

To invoke ADS Python ANN from VS-Code:

> 1. In VS-Code, execute the menu "View->Command Palette…"
> 2. Type the command "Python:Select Interpreter"
> 3. Set the python interpreter by browsing to $HPEESOF\_DIR\tools\python\python.exe (python3 for linux)

To use a python virtual environment instead of the ADS python installation:

> 1. Set up a python virtual environment. see [How to Set Up a Python Virtual Environment](../howto/venv.md)
> 2. Repeat steps 1-3 above
> 3. Set the python interpreter by browsing to the python executable in the virtual environment.


---

## 6. reference\index.md {#reference--index}

# Reference[](#reference "Link to this heading")

* [keysight.ads.ann](ann/index.md)
  + [Classes](ann/index.md#classes)
    - [AnnSetup](ann/annsetup.md)
    - [NeuronActivationFunctionType](ann/neuronactivationfunctiontype.md)
    - [OutputActivationFunctionType](ann/outputactivationfunctiontype.md)
    - [NetworkTrainingType](ann/networktrainingtype.md)
    - [NetworkInitializationMethod](ann/networkinitializationmethod.md)
    - [OutputFormat](ann/outputformat.md)
    - [ModelerOptimizer](ann/modeleroptimizer.md)
  + [Functions](ann/index.md#functions)
    - [`version()`](ann/index.md#keysight.ads.ann.version)
    - [`version_number()`](ann/index.md#keysight.ads.ann.version_number)
    - [`set_verbose()`](ann/index.md#keysight.ads.ann.set_verbose)
    - [`reset()`](ann/index.md#keysight.ads.ann.reset)
    - [`configure()`](ann/index.md#keysight.ads.ann.configure)
    - [`configure_setup()`](ann/index.md#keysight.ads.ann.configure_setup)
    - [`extract_model()`](ann/index.md#keysight.ads.ann.extract_model)
    - [`simulate_model()`](ann/index.md#keysight.ads.ann.simulate_model)
    - [`read_setup_file()`](ann/index.md#keysight.ads.ann.read_setup_file)
    - [`execute_with_setup_file()`](ann/index.md#keysight.ads.ann.execute_with_setup_file)
    - [`init_module()`](ann/index.md#keysight.ads.ann.init_module)
    - [`release_module()`](ann/index.md#keysight.ads.ann.release_module)

**Indices**

* [Index](../genindex.md)
* [Module Index](../py-modindex.md)


---

## 7. reference\ann\index.md {#reference--ann--index}

# keysight.ads.ann[](#module-keysight.ads.ann "Link to this heading")

ADS ANN python interface.

Typically imported as:

```
from keysight.ads import ann
```

## Classes[](#classes "Link to this heading")

* [AnnSetup](annsetup.md)
  + [`AnnSetup`](annsetup.md#keysight.ads.ann.AnnSetup)
* [NeuronActivationFunctionType](neuronactivationfunctiontype.md)
  + [`NeuronActivationFunctionType`](neuronactivationfunctiontype.md#keysight.ads.ann.NeuronActivationFunctionType)
* [OutputActivationFunctionType](outputactivationfunctiontype.md)
  + [`OutputActivationFunctionType`](outputactivationfunctiontype.md#keysight.ads.ann.OutputActivationFunctionType)
* [NetworkTrainingType](networktrainingtype.md)
  + [`NetworkTrainingType`](networktrainingtype.md#keysight.ads.ann.NetworkTrainingType)
* [NetworkInitializationMethod](networkinitializationmethod.md)
  + [`NetworkInitializationMethod`](networkinitializationmethod.md#keysight.ads.ann.NetworkInitializationMethod)
* [OutputFormat](outputformat.md)
  + [`OutputFormat`](outputformat.md#keysight.ads.ann.OutputFormat)
* [ModelerOptimizer](modeleroptimizer.md)
  + [`ModelerOptimizer`](modeleroptimizer.md#keysight.ads.ann.ModelerOptimizer)

## Functions[](#functions "Link to this heading")

keysight.ads.ann.version() → str[](#keysight.ads.ann.version "Link to this definition")

keysight.ads.ann.version\_number() → int[](#keysight.ads.ann.version_number "Link to this definition")

keysight.ads.ann.set\_verbose(*enable: bool*) → None[](#keysight.ads.ann.set_verbose "Link to this definition")

keysight.ads.ann.reset() → None[](#keysight.ads.ann.reset "Link to this definition")

keysight.ads.ann.configure(*num\_inputs: int*, *num\_outputs: int*) → None[](#keysight.ads.ann.configure "Link to this definition")

keysight.ads.ann.configure\_setup(*setup: [AnnSetup](annsetup.md#keysight.ads.ann.AnnSetup "keysight.ads.ann.AnnSetup")*) → None[](#keysight.ads.ann.configure_setup "Link to this definition")

keysight.ads.ann.extract\_model(*input\_file: str*, *output\_file: str*, *validation\_file: str | None = None*) → None[](#keysight.ads.ann.extract_model "Link to this definition")

keysight.ads.ann.simulate\_model(*sim\_file: str*, *input\_file: str*) → None[](#keysight.ads.ann.simulate_model "Link to this definition")

keysight.ads.ann.read\_setup\_file(*file: str*) → None[](#keysight.ads.ann.read_setup_file "Link to this definition")

keysight.ads.ann.execute\_with\_setup\_file(*file: str*) → None[](#keysight.ads.ann.execute_with_setup_file "Link to this definition")

keysight.ads.ann.init\_module() → None[](#keysight.ads.ann.init_module "Link to this definition")

keysight.ads.ann.release\_module() → None[](#keysight.ads.ann.release_module "Link to this definition")


---

## 8. reference\ann\annsetup.md {#reference--ann--annsetup}

# AnnSetup[](#annsetup "Link to this heading")

*class* keysight.ads.ann.AnnSetup[](#keysight.ads.ann.AnnSetup "Link to this definition")
:   \_\_init\_\_(*num\_inputs: int*, *num\_outputs: int*) → None[](#keysight.ads.ann.AnnSetup.__init__ "Link to this definition")

    *property* existing\_file*: str*[](#keysight.ads.ann.AnnSetup.existing_file "Link to this definition")

    *property* iterations\_per\_validation*: int*[](#keysight.ads.ann.AnnSetup.iterations_per_validation "Link to this definition")

    *property* max\_training\_iterations*: int*[](#keysight.ads.ann.AnnSetup.max_training_iterations "Link to this definition")

    *property* modeler\_optimizer*: [ModelerOptimizer](modeleroptimizer.md#keysight.ads.ann.ModelerOptimizer "keysight.ads.ann.ModelerOptimizer")*[](#keysight.ads.ann.AnnSetup.modeler_optimizer "Link to this definition")

    *property* network\_initialization\_method*: [NetworkInitializationMethod](networkinitializationmethod.md#keysight.ads.ann.NetworkInitializationMethod "keysight.ads.ann.NetworkInitializationMethod")*[](#keysight.ads.ann.AnnSetup.network_initialization_method "Link to this definition")

    *property* network\_training\_type*: [NetworkTrainingType](networktrainingtype.md#keysight.ads.ann.NetworkTrainingType "keysight.ads.ann.NetworkTrainingType")*[](#keysight.ads.ann.AnnSetup.network_training_type "Link to this definition")

    *property* neuron\_activation\_function\_type*: [NeuronActivationFunctionType](neuronactivationfunctiontype.md#keysight.ads.ann.NeuronActivationFunctionType "keysight.ads.ann.NeuronActivationFunctionType")*[](#keysight.ads.ann.AnnSetup.neuron_activation_function_type "Link to this definition")

    *property* num\_hidden\_layers*: int*[](#keysight.ads.ann.AnnSetup.num_hidden_layers "Link to this definition")

    *property* num\_inputs*: int*[](#keysight.ads.ann.AnnSetup.num_inputs "Link to this definition")

    *property* num\_neurons\_per\_layer*: int*[](#keysight.ads.ann.AnnSetup.num_neurons_per_layer "Link to this definition")

    *property* num\_outputs*: int*[](#keysight.ads.ann.AnnSetup.num_outputs "Link to this definition")

    *property* output\_activation\_function\_type*: [OutputActivationFunctionType](outputactivationfunctiontype.md#keysight.ads.ann.OutputActivationFunctionType "keysight.ads.ann.OutputActivationFunctionType")*[](#keysight.ads.ann.AnnSetup.output_activation_function_type "Link to this definition")

    *property* output\_file*: str*[](#keysight.ads.ann.AnnSetup.output_file "Link to this definition")

    *property* output\_format*: [OutputFormat](outputformat.md#keysight.ads.ann.OutputFormat "keysight.ads.ann.OutputFormat")*[](#keysight.ads.ann.AnnSetup.output_format "Link to this definition")

    *property* seed*: int*[](#keysight.ads.ann.AnnSetup.seed "Link to this definition")

    *property* training\_error\_weighting\_file*: str*[](#keysight.ads.ann.AnnSetup.training_error_weighting_file "Link to this definition")

    *property* training\_file*: str*[](#keysight.ads.ann.AnnSetup.training_file "Link to this definition")

    *property* training\_stop\_tolerance*: float*[](#keysight.ads.ann.AnnSetup.training_stop_tolerance "Link to this definition")


---

## 9. reference\ann\neuronactivationfunctiontype.md {#reference--ann--neuronactivationfunctiontype}

# NeuronActivationFunctionType[](#neuronactivationfunctiontype "Link to this heading")

*class* keysight.ads.ann.NeuronActivationFunctionType[](#keysight.ads.ann.NeuronActivationFunctionType "Link to this definition")
:   HYPERBOLIC\_TANGENT *= <NeuronActivationFunctionType.HYPERBOLIC\_TANGENT: 2>*[](#keysight.ads.ann.NeuronActivationFunctionType.HYPERBOLIC_TANGENT "Link to this definition")

    RELU *= <NeuronActivationFunctionType.RELU: 3>*[](#keysight.ads.ann.NeuronActivationFunctionType.RELU "Link to this definition")

    SIGMOID *= <NeuronActivationFunctionType.SIGMOID: 1>*[](#keysight.ads.ann.NeuronActivationFunctionType.SIGMOID "Link to this definition")


---

## 10. reference\ann\outputactivationfunctiontype.md {#reference--ann--outputactivationfunctiontype}

# OutputActivationFunctionType[](#outputactivationfunctiontype "Link to this heading")

*class* keysight.ads.ann.OutputActivationFunctionType[](#keysight.ads.ann.OutputActivationFunctionType "Link to this definition")
:   HYPERBOLIC\_TANGENT *= <OutputActivationFunctionType.HYPERBOLIC\_TANGENT: 2>*[](#keysight.ads.ann.OutputActivationFunctionType.HYPERBOLIC_TANGENT "Link to this definition")

    LINEAR *= <OutputActivationFunctionType.LINEAR: 0>*[](#keysight.ads.ann.OutputActivationFunctionType.LINEAR "Link to this definition")

    RELU *= <OutputActivationFunctionType.RELU: 3>*[](#keysight.ads.ann.OutputActivationFunctionType.RELU "Link to this definition")

    SATLINS *= <OutputActivationFunctionType.SATLINS: 4>*[](#keysight.ads.ann.OutputActivationFunctionType.SATLINS "Link to this definition")

    SIGMOID *= <OutputActivationFunctionType.SIGMOID: 1>*[](#keysight.ads.ann.OutputActivationFunctionType.SIGMOID "Link to this definition")


---

## 11. reference\ann\networktrainingtype.md {#reference--ann--networktrainingtype}

# NetworkTrainingType[](#networktrainingtype "Link to this heading")

*class* keysight.ads.ann.NetworkTrainingType[](#keysight.ads.ann.NetworkTrainingType "Link to this definition")
:   ADJOINT *= <NetworkTrainingType.ADJOINT: 2>*[](#keysight.ads.ann.NetworkTrainingType.ADJOINT "Link to this definition")

    PATTERN\_RECOGNITION\_AND\_CLASSIFICATION *= <NetworkTrainingType.PATTERN\_RECOGNITION\_AND\_CLASSIFICATION: 3>*[](#keysight.ads.ann.NetworkTrainingType.PATTERN_RECOGNITION_AND_CLASSIFICATION "Link to this definition")

    STANDARD *= <NetworkTrainingType.STANDARD: 1>*[](#keysight.ads.ann.NetworkTrainingType.STANDARD "Link to this definition")


---

## 12. reference\ann\networkinitializationmethod.md {#reference--ann--networkinitializationmethod}

# NetworkInitializationMethod[](#networkinitializationmethod "Link to this heading")

*class* keysight.ads.ann.NetworkInitializationMethod[](#keysight.ads.ann.NetworkInitializationMethod "Link to this definition")
:   NGUYEN\_WIDROW\_LAYER *= <NetworkInitializationMethod.NGUYEN\_WIDROW\_LAYER: 2>*[](#keysight.ads.ann.NetworkInitializationMethod.NGUYEN_WIDROW_LAYER "Link to this definition")

    RANDOM\_NUMBER *= <NetworkInitializationMethod.RANDOM\_NUMBER: 1>*[](#keysight.ads.ann.NetworkInitializationMethod.RANDOM_NUMBER "Link to this definition")


---

## 13. reference\ann\outputformat.md {#reference--ann--outputformat}

# OutputFormat[](#outputformat "Link to this heading")

*class* keysight.ads.ann.OutputFormat[](#keysight.ads.ann.OutputFormat "Link to this definition")
:   ALL *= <OutputFormat.ALL: 5>*[](#keysight.ads.ann.OutputFormat.ALL "Link to this definition")

    C\_CODE *= <OutputFormat.C\_CODE: 4>*[](#keysight.ads.ann.OutputFormat.C_CODE "Link to this definition")

    STRUC\_AND\_SCALE *= <OutputFormat.STRUC\_AND\_SCALE: 3>*[](#keysight.ads.ann.OutputFormat.STRUC_AND_SCALE "Link to this definition")

    TEXT\_FORMULA *= <OutputFormat.TEXT\_FORMULA: 1>*[](#keysight.ads.ann.OutputFormat.TEXT_FORMULA "Link to this definition")

    VERILOG\_A\_FORMAT *= <OutputFormat.VERILOG\_A\_FORMAT: 2>*[](#keysight.ads.ann.OutputFormat.VERILOG_A_FORMAT "Link to this definition")


---

## 14. reference\ann\modeleroptimizer.md {#reference--ann--modeleroptimizer}

# ModelerOptimizer[](#modeleroptimizer "Link to this heading")

*class* keysight.ads.ann.ModelerOptimizer[](#keysight.ads.ann.ModelerOptimizer "Link to this definition")
:   BAYESIAN\_REGULARIZATION *= <ModelerOptimizer.BAYESIAN\_REGULARIZATION: 2>*[](#keysight.ads.ann.ModelerOptimizer.BAYESIAN_REGULARIZATION "Link to this definition")

    QUASI\_NEWTON *= <ModelerOptimizer.QUASI\_NEWTON: 1>*[](#keysight.ads.ann.ModelerOptimizer.QUASI_NEWTON "Link to this definition")


---

## 15. howto\index.md {#howto--index}

# How-To[](#how-to "Link to this heading")

* [How to Set Up a Python Virtual Environment](venv.md)
  + [Creating a new Python virtual environment based on ADS Python](newvenv.md)
  + [Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)
* [How to Use Pytest](pytest.md)


---

## 16. howto\venv.md {#howto--venv}

# How to Set Up a Python Virtual Environment[](#how-to-set-up-a-python-virtual-environment "Link to this heading")

It is possible to use ADS modules from a Python virtual environment rather than within the embedded ADS Python.

One option is to create a new virtual environment based on the ADS Python executable.

Alternatively, an existing virtual environment can install ADS wheels through the provided pip requirements file.

* [Creating a new Python virtual environment based on ADS Python](newvenv.md)
* [Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)


---

## 17. howto\newvenv.md {#howto--newvenv}

# Creating a new Python virtual environment based on ADS Python[](#creating-a-new-python-virtual-environment-based-on-ads-python "Link to this heading")

1. Create a Python virtual environment (venv).

   The venv must be created using the Python shipped with ADS, or with another Python installation with the same major and minor version.

   Example for Linux:

   ```
   $HPEESOF_DIR/tools/python/bin/python3 -m venv --system-site-packages $HOME/ads_venv
   ```

   Example for Windows:

   ```
   %HPEESOF_DIR%\tools\python\python -m venv --system-site-packages %USERPROFILE%\ads_venv
   ```
2. Select the venv by setting **ADS\_PYTHONHOME**.

   This can be accomplished either as an environment variable or in de\_sim.cfg (user level or above, i.e. not supported in workspace-level cfg)

   Example for Linux:

   ```
   export ADS_PYTHONHOME=$HOME/ads_venv
   ```

   Example for Windows:

   ```
   set ADS_PYTHONHOME=%USERPROFILE%\ads_venv
   ```

   To set the venv path in de\_sim.cfg rather than an environment variable, add a line like this:

   ```
   ADS_PYTHONHOME={$HOME}/ads_venv
   ```
3. Run ADS. Python support is automatically enabled.

   ```
   ads
   ```

   To verify the venv is being used, execute menu **Python->Python Console…**, and type the following in the console:

   ```
   import sys
   print(sys.executable)
   ```

   The path to the Python executable will be displayed, and it should be prefixed by the venv path.


---

## 18. howto\existingvenv.md {#howto--existingvenv}

# Installing Keysight ADS wheels into an existing Python virtual environment[](#installing-keysight-ads-wheels-into-an-existing-python-virtual-environment "Link to this heading")

1. Open a console window and load an existing virtual environment

   > The existing venv must have been created from a Python installation with the same major and minor Python version as ADS.
2. Navigate to the ADS wheelhouse directory

   > Example for Linux:
   >
   > ```
   > cd $HPEESOF_DIR/tools/python/wheelhouse
   > ```
   >
   > Example for Windows:
   >
   > ```
   > cd %HPEESOF_DIR%\tools\python\wheelhouse
   > ```
3. Install packages with pip requirements file

   > Example for Linux:
   >
   > ```
   > python3 -m pip install -r venv_requirements.txt --find-links .
   > ```
   >
   > Example for Windows:
   >
   > ```
   > python -m pip install -r venv_requirements.txt --find-links .
   > ```
4. To verify packages have been installed
   :   Example for Linux:

       ```
       python3 -m pip list
       ```

       Example for Windows:

       ```
       python -m pip list
       ```

       You should see various keysight-ads-\* wheels listed


---

## 19. howto\pytest.md {#howto--pytest}

# How to Use Pytest[](#how-to-use-pytest "Link to this heading")

Pytest is a mature full-featured testing tool for Python. It is useful when developing Python scripts.
Pytest is not installed in the ADS Python installation.

The recommended steps to use Pytest are:

> 1. Create a Python virtual environment. See [How to Set Up a Python Virtual Environment](venv.md).
> 2. Activate the Python virtual environment.
> 3. Install pytest into the virtual environment.
>
>    > ```
>    > pip install pytest
>    > ```
> 4. Run pytest on your test scripts.
>
>    > ```
>    > cd path/to/tests
>    > pytest
>    > ```


---

## 20. examples\index.md {#examples--index}

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

## 21. examples\ex_basic.md {#examples--ex_basic}

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

## 22. examples\ex_inmemory_extraction.md {#examples--ex_inmemory_extraction}

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

## 23. examples\ex_training_error_weighting.md {#examples--ex_training_error_weighting}

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
