# Intro
> **说明：** Intro 相关页面。

> **何时使用：** 当你需要查阅 Intro 相关内容时

---

## 本文件目录

- **Introduction** (`intro/index.md`)
- **Using Design Cloud Functionality in Python** (`intro/usage.md`)
- **Using Visual Studio Code** (`intro/vscode.md`)

---

<!-- === 来源: intro/index.md === -->

# Introduction[](#introduction "Link to this heading")

* [Using Design Cloud Functionality in Python](usage.md)
* [Using Visual Studio Code](vscode.md)


---

<!-- === 来源: intro/usage.md === -->

# Using Design Cloud Functionality in Python[](#using-design-cloud-functionality-in-python "Link to this heading")

Design Cloud provides Python APIs that allow a user to run circuit simulations
on the design cloud server, Local Queue or Site Cluster Queue

A Python script running outside ADS can access the functionality of Design Cloud.

```
from keysight.ads.experimental_simulation import hpc
```

The `keysight.ads.experimental_simulation` package is not currently available as a pip-installable package.
To get access to this package, use any one of these approaches:

> 1. Use the Python interpreter in `$HPEESOF_DIR/tools/python`.
> 2. Create a virtual environment based on that interpreter. See [How to Set Up a Python Virtual Environment](../howto/venv.md).

Set the environment variable `HPEESOF_DIR` to point to your ADS installation prior to
using the `keysight.ads.experimental_simulation` package.


---

<!-- === 来源: intro/vscode.md === -->

# Using Visual Studio Code[](#using-visual-studio-code "Link to this heading")

To invoke ADS Python from VS-Code:

> 1. In VS-Code, execute the menu "View->Command Palette…"
> 2. Type the command "Python:Select Interpreter"
> 3. Set the python interpreter by browsing to $HPEESOF\_DIR\tools\python\python.exe (python3 for linux)

To use a python virtual environment instead of the ADS python installation:

> 1. Set up a python virtual environment. see [How to Set Up a Python Virtual Environment](../howto/venv.md)
> 2. Repeat steps 1-3 above
> 3. Set the python interpreter by browsing to the python executable in the virtual environment.


---

