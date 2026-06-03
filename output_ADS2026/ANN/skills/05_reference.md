# Reference
> **说明：** Reference 相关页面。

> **何时使用：** 当你需要查阅 Reference 相关内容时

---

## 本文件目录

- **AnnSetup** (`reference/ann/annsetup.md`)
- **keysight.ads.ann** (`reference/ann/index.md`)
- **ModelerOptimizer** (`reference/ann/modeleroptimizer.md`)
- **NetworkInitializationMethod** (`reference/ann/networkinitializationmethod.md`)
- **NetworkTrainingType** (`reference/ann/networktrainingtype.md`)
- **NeuronActivationFunctionType** (`reference/ann/neuronactivationfunctiontype.md`)
- **OutputActivationFunctionType** (`reference/ann/outputactivationfunctiontype.md`)
- **OutputFormat** (`reference/ann/outputformat.md`)
- **Reference** (`reference/index.md`)

---

<!-- === 来源: reference/ann/annsetup.md === -->

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

<!-- === 来源: reference/ann/index.md === -->

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

<!-- === 来源: reference/ann/modeleroptimizer.md === -->

# ModelerOptimizer[](#modeleroptimizer "Link to this heading")

*class* keysight.ads.ann.ModelerOptimizer[](#keysight.ads.ann.ModelerOptimizer "Link to this definition")
:   BAYESIAN\_REGULARIZATION *= <ModelerOptimizer.BAYESIAN\_REGULARIZATION: 2>*[](#keysight.ads.ann.ModelerOptimizer.BAYESIAN_REGULARIZATION "Link to this definition")

    QUASI\_NEWTON *= <ModelerOptimizer.QUASI\_NEWTON: 1>*[](#keysight.ads.ann.ModelerOptimizer.QUASI_NEWTON "Link to this definition")


---

<!-- === 来源: reference/ann/networkinitializationmethod.md === -->

# NetworkInitializationMethod[](#networkinitializationmethod "Link to this heading")

*class* keysight.ads.ann.NetworkInitializationMethod[](#keysight.ads.ann.NetworkInitializationMethod "Link to this definition")
:   NGUYEN\_WIDROW\_LAYER *= <NetworkInitializationMethod.NGUYEN\_WIDROW\_LAYER: 2>*[](#keysight.ads.ann.NetworkInitializationMethod.NGUYEN_WIDROW_LAYER "Link to this definition")

    RANDOM\_NUMBER *= <NetworkInitializationMethod.RANDOM\_NUMBER: 1>*[](#keysight.ads.ann.NetworkInitializationMethod.RANDOM_NUMBER "Link to this definition")


---

<!-- === 来源: reference/ann/networktrainingtype.md === -->

# NetworkTrainingType[](#networktrainingtype "Link to this heading")

*class* keysight.ads.ann.NetworkTrainingType[](#keysight.ads.ann.NetworkTrainingType "Link to this definition")
:   ADJOINT *= <NetworkTrainingType.ADJOINT: 2>*[](#keysight.ads.ann.NetworkTrainingType.ADJOINT "Link to this definition")

    PATTERN\_RECOGNITION\_AND\_CLASSIFICATION *= <NetworkTrainingType.PATTERN\_RECOGNITION\_AND\_CLASSIFICATION: 3>*[](#keysight.ads.ann.NetworkTrainingType.PATTERN_RECOGNITION_AND_CLASSIFICATION "Link to this definition")

    STANDARD *= <NetworkTrainingType.STANDARD: 1>*[](#keysight.ads.ann.NetworkTrainingType.STANDARD "Link to this definition")


---

<!-- === 来源: reference/ann/neuronactivationfunctiontype.md === -->

# NeuronActivationFunctionType[](#neuronactivationfunctiontype "Link to this heading")

*class* keysight.ads.ann.NeuronActivationFunctionType[](#keysight.ads.ann.NeuronActivationFunctionType "Link to this definition")
:   HYPERBOLIC\_TANGENT *= <NeuronActivationFunctionType.HYPERBOLIC\_TANGENT: 2>*[](#keysight.ads.ann.NeuronActivationFunctionType.HYPERBOLIC_TANGENT "Link to this definition")

    RELU *= <NeuronActivationFunctionType.RELU: 3>*[](#keysight.ads.ann.NeuronActivationFunctionType.RELU "Link to this definition")

    SIGMOID *= <NeuronActivationFunctionType.SIGMOID: 1>*[](#keysight.ads.ann.NeuronActivationFunctionType.SIGMOID "Link to this definition")


---

<!-- === 来源: reference/ann/outputactivationfunctiontype.md === -->

# OutputActivationFunctionType[](#outputactivationfunctiontype "Link to this heading")

*class* keysight.ads.ann.OutputActivationFunctionType[](#keysight.ads.ann.OutputActivationFunctionType "Link to this definition")
:   HYPERBOLIC\_TANGENT *= <OutputActivationFunctionType.HYPERBOLIC\_TANGENT: 2>*[](#keysight.ads.ann.OutputActivationFunctionType.HYPERBOLIC_TANGENT "Link to this definition")

    LINEAR *= <OutputActivationFunctionType.LINEAR: 0>*[](#keysight.ads.ann.OutputActivationFunctionType.LINEAR "Link to this definition")

    RELU *= <OutputActivationFunctionType.RELU: 3>*[](#keysight.ads.ann.OutputActivationFunctionType.RELU "Link to this definition")

    SATLINS *= <OutputActivationFunctionType.SATLINS: 4>*[](#keysight.ads.ann.OutputActivationFunctionType.SATLINS "Link to this definition")

    SIGMOID *= <OutputActivationFunctionType.SIGMOID: 1>*[](#keysight.ads.ann.OutputActivationFunctionType.SIGMOID "Link to this definition")


---

<!-- === 来源: reference/ann/outputformat.md === -->

# OutputFormat[](#outputformat "Link to this heading")

*class* keysight.ads.ann.OutputFormat[](#keysight.ads.ann.OutputFormat "Link to this definition")
:   ALL *= <OutputFormat.ALL: 5>*[](#keysight.ads.ann.OutputFormat.ALL "Link to this definition")

    C\_CODE *= <OutputFormat.C\_CODE: 4>*[](#keysight.ads.ann.OutputFormat.C_CODE "Link to this definition")

    STRUC\_AND\_SCALE *= <OutputFormat.STRUC\_AND\_SCALE: 3>*[](#keysight.ads.ann.OutputFormat.STRUC_AND_SCALE "Link to this definition")

    TEXT\_FORMULA *= <OutputFormat.TEXT\_FORMULA: 1>*[](#keysight.ads.ann.OutputFormat.TEXT_FORMULA "Link to this definition")

    VERILOG\_A\_FORMAT *= <OutputFormat.VERILOG\_A\_FORMAT: 2>*[](#keysight.ads.ann.OutputFormat.VERILOG_A_FORMAT "Link to this definition")


---

<!-- === 来源: reference/index.md === -->

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

