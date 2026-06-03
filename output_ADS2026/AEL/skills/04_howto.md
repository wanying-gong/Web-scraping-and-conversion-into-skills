# Howto
> **说明：** Howto 相关页面。

> **何时使用：** 当你需要查阅 Howto 相关内容时

---

## 本文件目录

- **Installing Keysight ADS wheels into an existing Python virtual environment** (`howto/existingvenv.md`)
- **How-To** (`howto/index.md`)
- **Creating an ADS based Python virtual environment** (`howto/newvenv.md`)
- **ADS Python Environment Variables** (`howto/pyenvvars.md`)
- **How to Use Pytest** (`howto/pytest.md`)
- **How to Set Up a Python Virtual Environment** (`howto/venv.md`)

---

<!-- === 来源: howto/existingvenv.md === -->

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
   > python3 -m pip install -r venv_requirements.txt --no-index --no-cache-dir --only-binary=:all: --find-links=.
   > ```
   >
   > Example for Windows:
   >
   > ```
   > python -m pip install -r venv_requirements.txt --no-index --no-cache-dir --only-binary=:all: --find-links=.
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

<!-- === 来源: howto/index.md === -->

# How-To[](#how-to "Link to this heading")

* [How to Set Up a Python Virtual Environment](venv.md)
  + [Creating an ADS based Python virtual environment](newvenv.md)
  + [Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)
  + [ADS Python Environment Variables](pyenvvars.md)
* [How to Use Pytest](pytest.md)


---

<!-- === 来源: howto/newvenv.md === -->

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


---

<!-- === 来源: howto/pyenvvars.md === -->

# ADS Python Environment Variables[](#ads-python-environment-variables "Link to this heading")

This document describes optional environment variables used to configure the Python environment in ADS.

## ADS\_PYTHONHOME[](#ads-pythonhome "Link to this heading")

Similar to the **PYTHONHOME** environment variable, this variable specifies the path to the Python virtual environment (venv) that ADS will use.
This is useful for when you want to use a custom Python virtual environment instead of the default embedded Python in ADS.
See [Creating an ADS based Python virtual environment](newvenv.md#new-venv) for instructions on how to set up a custom virtual environment.


---

<!-- === 来源: howto/pytest.md === -->

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

<!-- === 来源: howto/venv.md === -->

# How to Set Up a Python Virtual Environment[](#how-to-set-up-a-python-virtual-environment "Link to this heading")

It is possible to use ADS modules from a Python virtual environment rather than within the embedded ADS Python.

One option is to create a new virtual environment based on the ADS Python executable.

Alternatively, an existing virtual environment can install ADS wheels through the provided pip requirements file.

* [Creating an ADS based Python virtual environment](newvenv.md)
* [Installing Keysight ADS wheels into an existing Python virtual environment](existingvenv.md)
* [ADS Python Environment Variables](pyenvvars.md)
  + [ADS\_PYTHONHOME](pyenvvars.md#ads-pythonhome)


---

