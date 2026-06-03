<!-- 来源: reference\ann\annsetup.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ANN Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.ann](index.md)
* AnnSetup

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

* [Introduction](../../intro/index.md)
  + [Licensing](../../intro/licensing.md)
  + [Using ANN Functionality in Python](../../intro/usage.md)
  + [Using Visual Studio Code](../../intro/vscode.md)
* [Reference](../index.md)
  + [keysight.ads.ann](index.md)
    - AnnSetup
    - [NeuronActivationFunctionType](neuronactivationfunctiontype.md)
    - [OutputActivationFunctionType](outputactivationfunctiontype.md)
    - [NetworkTrainingType](networktrainingtype.md)
    - [NetworkInitializationMethod](networkinitializationmethod.md)
    - [OutputFormat](outputformat.md)
    - [ModelerOptimizer](modeleroptimizer.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
  + [How to Use Pytest](../../howto/pytest.md)
* [Examples](../../examples/index.md)
  + [Basic Extraction and Simulation](../../examples/ex_basic.md)
  + [In-memory Extraction](../../examples/ex_inmemory_extraction.md)
  + [Training with Error Weighting](../../examples/ex_training_error_weighting.md)

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

On this page

[Previous

keysight.ads.ann](index.md)
[Next

NeuronActivationFunctionType](neuronactivationfunctiontype.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top