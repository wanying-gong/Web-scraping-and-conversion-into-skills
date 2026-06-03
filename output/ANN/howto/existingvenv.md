<!-- 来源: howto\existingvenv.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ANN Python Documentation](../index.md)
* [How-To](index.md)
* [How to Set Up a Python Virtual Environment](venv.md)
* Installing Keysight ADS wheels into an existing Python virtual environment

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
* [How-To](index.md)
  + [How to Set Up a Python Virtual Environment](venv.md)
    - [Creating a new Python virtual environment based on ADS Python](newvenv.md)
    - Installing Keysight ADS wheels into an existing Python virtual environment
  + [How to Use Pytest](pytest.md)
* [Examples](../examples/index.md)
  + [Basic Extraction and Simulation](../examples/ex_basic.md)
  + [In-memory Extraction](../examples/ex_inmemory_extraction.md)
  + [Training with Error Weighting](../examples/ex_training_error_weighting.md)

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

On this page

[Previous

Creating a new Python virtual environment based on ADS Python](newvenv.md)
[Next

How to Use Pytest](pytest.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top