# Intro
> **说明：** Intro 相关页面。

> **何时使用：** 当你需要查阅 Intro 相关内容时

---

## 本文件目录

- **Introduction** (`intro/index.md`)
- **Licensing** (`intro/licensing.md`)
- **Using Data Display functionality in Python** (`intro/usage.md`)
- **Using Visual Studio Code** (`intro/vscode.md`)

---

<!-- === 来源: intro/index.md === -->

# Introduction[](#introduction "Link to this heading")

* [Licensing](licensing.md)
* [Using Data Display functionality in Python](usage.md)
  + [Application Mode](usage.md#application-mode)
  + [Automation Mode](usage.md#automation-mode)
* [Using Visual Studio Code](vscode.md)


---

<!-- === 来源: intro/licensing.md === -->

# Licensing[](#licensing "Link to this heading")

Importing `keysight.ads.dds` pulls a **Data Display** license. Note that the license is held for the entirety of the Python session and releases only when the Python session ends.


---

<!-- === 来源: intro/usage.md === -->

# Using Data Display functionality in Python[](#using-data-display-functionality-in-python "Link to this heading")

Data Display provides a Python API that allows for the creation and manipulation of DDS objects.
The Python API can be run in two modes: application mode or automation mode.

## Application Mode[](#application-mode "Link to this heading")

Application mode is when the Python API is used inside of Data Display (DDS).
In order to run in this mode:

> 1. Execute the DDS menu Tools->Python Console.
>    The DDS Python API will already be imported in the console.
> 2. Execute any python statement within the console.

When running in this mode, it is possible to access and modify opened DDS objects.
If the DDS objects are visible, modifications will be reflected in the windows.

Example:

Assume one DDS file is opened. In the python console, typing these statements.

```
>>>  ddsfile = dds.files[0]             # access the first opened file
>>>  page = ddsfile.pages['page 1']     # access "page 1"
>>>  ddsfile.change_page('page 1')      # cause "page 1" to be visible
>>>  page.add_text("hello", (100,100))  # add text, it will be seen in the window
>>>  ddsfile.save()                     # save the file
>>>  dds.close_dds_file(ddsfile)        # close the file (window will be closed)
```

## Automation Mode[](#automation-mode "Link to this heading")

Automation mode is when the Python API is used outside of Advanced Design System (ADS) or standalone Data Display (DDS).
In order to run in this mode, a python script is run by a python interpreter. The `keysight.ads.dds` python packages
must be imported.

Example:

```
from keysight.ads import dds

dds.version()
```

The `keysight.ads.dds` packages are not currently available as a pip-installable package.
To get access to these package, use any one of these approaches:

> 1. Use the Python interpreter in `$HPEESOF_DIR/tools/python`.
> 2. Create a virtual environment based on that interpreter. See [How to Set Up a Python Virtual Environment](../howto/venv.md).
> 3. Add `$HPEESOF_DIR/tools/python/packages` onto your Python’s `sys.path`.

Set the environment variable `HPEESOF_DIR` to point to your ADS installation prior to
using the `keysight.ads.dds` packages.

Note: If on Linux, ensure that your `LD_LIBRARY_PATH` is set, \_prior to Python being [launched\_](#id1), to have `$HPEESOF_DIR/lib/linux_x86_64` early in the list of paths. This is to make sure Python picks up the libstdc++.so from ADS. You may need to also set `QT_PLUGIN_PATH` to `$HPEESOF_DIR/bin/plugins/qt` if importing the module displays a plugin error.”

Example:

To accomplish the same thing as in the example in automation mode section, this python
script can be executed in any python environment that is set up correctly.

```
import os
os.environ['HPEESOF_DIR'] = "C:/Program Files/Keysight/ADS2025"  # use the ADS installed path

from keysight.ads import dds as dds

pathToDDSfile = "c:/workspaces/my_wrk/cell_1.dds"
ddsfile = dds.open_dds_file(pathToDDSfile)  # access the file stuff.dds
page = ddsfile.pages['page 1']              # access "page 1"
page.add_text("hello", (100,100))           # add text
ddsfile.save()                              # save the file
```

In order to see the changes, the file must be opened in the Data Display application.


---

<!-- === 来源: intro/vscode.md === -->

# Using Visual Studio Code[](#using-visual-studio-code "Link to this heading")

To invoke VS-Code from DDS:

> 1. In DDS, execute the menu "Tools->VS-Code.."
> 2. In VS-Code, execute the menu "View->Command Palette…"
> 3. Type the command "Python:Select Interpreter"
> 4. Set the python interpreter by browsing to $HPEESOF\_DIR\tools\python\python.exe (python3 for linux)

To use a python virtual environment instead of the ADS python installation:

> 1. Set up a python virtual environment. see [How to Set Up a Python Virtual Environment](../howto/venv.md)
> 2. Repeat steps 1-3 above
> 3. Set the python interpreter by browsing to the python executable in the virtual environment.


---

