<!-- 来源: howto\newvenv.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Quantum Python Documentation](../index.md)
* [How-To](index.md)
* [How to Set Up a Python Virtual Environment](venv.md)
* Creating a new Python virtual environment based on ADS Python

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
  + [Importing Modules](../intro/importing.md)
  + [Using Visual Studio Code](../intro/vscode.md)
* [Reference](../reference/index.md)
  + [Quantum Addon](../reference/quantum/index.md)
    - [Hamiltonian Analysis](../reference/quantum/hamiltonian_analysis.md)
    - [Parameter Extraction](../reference/quantum/parameter_extraction.md)
    - [SQUID Extrema Analysis](../reference/quantum/squid_extrema_analysis.md)
    - [Dilution Fridge Input Line Designer](../reference/quantum/dilution_fridge_input_line_designer.md)
    - [Time Dynamics Analysis](../reference/quantum/time_dynamics_analysis.md)
* [How-To](index.md)
  + [How to Set Up a Python Virtual Environment](venv.md)
    - Creating a new Python virtual environment based on ADS Python
    - [Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)
  + [How to Use Pytest](pytest.md)

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

On this page

[Previous

How to Set Up a Python Virtual Environment](venv.md)
[Next

Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top