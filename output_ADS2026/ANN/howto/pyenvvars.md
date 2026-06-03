<!-- 来源: howto\pyenvvars.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ANN Python Documentation](../index.md)
* [How-To](index.md)
* [How to Set Up a Python Virtual Environment](venv.md)
* ADS Python Environment Variables

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
    - ADS Python Environment Variables
  + [How to Use Pytest](pytest.md)
* [Examples](../examples/index.md)
  + [Basic Extraction and Simulation](../examples/ex_basic.md)
  + [In-memory Extraction](../examples/ex_inmemory_extraction.md)
  + [Training with Error Weighting](../examples/ex_training_error_weighting.md)

# ADS Python Environment Variables[](#ads-python-environment-variables "Link to this heading")

This document describes optional environment variables used to configure the Python environment in ADS.

## ADS\_PYTHONHOME[](#ads-pythonhome "Link to this heading")

Similar to the **PYTHONHOME** environment variable, this variable specifies the path to the Python virtual environment (venv) that ADS will use.
This is useful for when you want to use a custom Python virtual environment instead of the default embedded Python in ADS.
See [Creating an ADS based Python virtual environment](newvenv.md#new-venv) for instructions on how to set up a custom virtual environment.

On this page

[Previous

Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)
[Next

How to Use Pytest](pytest.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top