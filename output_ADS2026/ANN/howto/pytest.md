<!-- 来源: howto\pytest.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ANN Python Documentation](../index.md)
* [How-To](index.md)
* How to Use Pytest

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
* [How-To](index.md)
  + [How to Set Up a Python Virtual Environment](venv.md)
    - [Creating an ADS based Python virtual environment](newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)
    - [ADS Python Environment Variables](pyenvvars.md)
  + How to Use Pytest
* [Examples](../examples/index.md)
  + [Basic Extraction and Simulation](../examples/ex_basic.md)
  + [In-memory Extraction](../examples/ex_inmemory_extraction.md)
  + [Training with Error Weighting](../examples/ex_training_error_weighting.md)

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

On this page

[Previous

ADS Python Environment Variables](pyenvvars.md)
[Next

Examples](../examples/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top