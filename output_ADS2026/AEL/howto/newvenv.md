<!-- 来源: howto\newvenv.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [AEL Python Documentation](../index.md)
* [How-To](index.md)
* [How to Set Up a Python Virtual Environment](venv.md)
* Creating an ADS based Python virtual environment

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
  + [Using AEL Functionality in Python](../intro/usage.md)
* [Concepts](../concepts/index.md)
  + [AEL Interoperability](../concepts/ael_interoperability.md)
  + [AEL Type Conversions](../concepts/ael_type_conversions.md)
* [Reference](../reference/index.md)
  + [keysight.ads.ael](../reference/ael.md)
* [How-To](index.md)
  + [How to Set Up a Python Virtual Environment](venv.md)
    - Creating an ADS based Python virtual environment
    - [Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)
    - [ADS Python Environment Variables](pyenvvars.md)
  + [How to Use Pytest](pytest.md)
* [Examples](../examples/index.md)
  + [Calling Between AEL and Python](../examples/ex_calling_ael_and_python.md)

# Creating an ADS based Python virtual environment[](#creating-an-ads-based-python-virtual-environment "Link to this heading")

It is possible to create a Python virtual environment (venv) based on the Python shipped with ADS.
This is the recommended way to modify the ADS Python environment with external python packages.

Note

The environment variable, **HPEESOF\_DIR** points to the location of your current ADS install location.

Note

**%HOME%** is not set by default on Windows. It is recommended to set this to your user home directory, e.g. **%USERPROFILE%**.

```
set HOME=%USERPROFILE%
```

Warning

Virtual environments created in one version of ADS may not work in another version of ADS. It is recommend that you create a new virtual environment for each version of ADS you use.

1. Creating a Python virtual environment (venv).

   The venv must be created using the Python shipped with ADS

   Example for Linux:

   ```
   $HPEESOF_DIR/tools/python/bin/python3 -m venv --system-site-packages $HOME/ads_venv
   ```

   Example for Windows:

   ```
   %HPEESOF_DIR%\tools\python\python -m venv --system-site-packages %HOME%\ads_venv
   ```
2. (Optional) Modify your venv by installing additional Python packages.

   Activate the venv and install any additional packages you need.

   Example for Linux:

   ```
   source $HOME/ads_venv/bin/activate
   python3 -m pip install -r /path/to/your/requirements.txt
   ```

   Example for Windows:

   ```
   %HOME%\ads_venv\Scripts\activate
   py -m pip install -r \path\to\your\requirements.txt
   ```
3. Select the venv by setting **ADS\_PYTHONHOME**.

   This can be accomplished either as an environment variable or in de\_sim.cfg (user level or above, i.e. not supported in workspace-level cfg)

   Example for Linux:

   ```
   export ADS_PYTHONHOME=$HOME/ads_venv
   ```

   Example for Windows:

   ```
   set ADS_PYTHONHOME=%HOME%\ads_venv
   ```

   To set the venv path in de\_sim.cfg rather than an environment variable, add a line like this:

   ```
   ADS_PYTHONHOME={$HOME}/ads_venv
   ```
4. Run ADS. Python support is automatically enabled.

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