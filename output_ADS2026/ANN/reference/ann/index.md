<!-- 来源: reference\ann\index.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ANN Python Documentation](../../index.md)
* [Reference](../index.md)
* keysight.ads.ann

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

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
  + keysight.ads.ann
    - [AnnSetup](annsetup.md)
    - [NeuronActivationFunctionType](neuronactivationfunctiontype.md)
    - [OutputActivationFunctionType](outputactivationfunctiontype.md)
    - [NetworkTrainingType](networktrainingtype.md)
    - [NetworkInitializationMethod](networkinitializationmethod.md)
    - [OutputFormat](outputformat.md)
    - [ModelerOptimizer](modeleroptimizer.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating an ADS based Python virtual environment](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
    - [ADS Python Environment Variables](../../howto/pyenvvars.md)
  + [How to Use Pytest](../../howto/pytest.md)
* [Examples](../../examples/index.md)
  + [Basic Extraction and Simulation](../../examples/ex_basic.md)
  + [In-memory Extraction](../../examples/ex_inmemory_extraction.md)
  + [Training with Error Weighting](../../examples/ex_training_error_weighting.md)

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

On this page

[Previous

Reference](../index.md)
[Next

AnnSetup](annsetup.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top