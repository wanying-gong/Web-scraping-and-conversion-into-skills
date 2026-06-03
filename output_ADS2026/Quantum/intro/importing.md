<!-- 来源: intro\importing.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Quantum Python Documentation](../index.md)
* [Introduction](index.md)
* Importing Modules

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

* [Introduction](index.md)
  + Importing Modules
  + [Using Visual Studio Code](vscode.md)
* [Reference](../reference/index.md)
  + [Quantum Addon](../reference/quantum/index.md)
    - [Hamiltonian Analysis](../reference/quantum/hamiltonian_analysis.md)
    - [Parameter Extraction](../reference/quantum/parameter_extraction.md)
    - [SQUID Extrema Analysis](../reference/quantum/squid_extrema_analysis.md)
    - [Dilution Fridge Input Line Designer](../reference/quantum/dilution_fridge_input_line_designer.md)
    - [Time Dynamics Analysis](../reference/quantum/time_dynamics_analysis.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
  + [How to Use Pytest](../howto/pytest.md)

# Importing Modules[](#importing-modules "Link to this heading")

Importing modules for the quantum tool suite is similar but slightly different to the typical import process for addons.
For instance, to import the ‘Transmon’ class from the ‘hamiltonian\_analysis’ module you would:

```
from keysight.ads.de import app
quantum_addon = app.import_addon_as_module("Quantum Tools")
quantum_analysis_module = quantum_addon.src.keysight.ads.quantum_analysis
transmon = quantum_analysis_module.python.hamiltonian_analysis.Transmon
```

On this page

[Previous

Introduction](index.md)
[Next

Using Visual Studio Code](vscode.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top