# Intro
> **说明：** Intro 相关页面。

> **何时使用：** 当你需要查阅 Intro 相关内容时

---

## 本文件目录

- **Importing Modules** (`intro/importing.md`)
- **Introduction** (`intro/index.md`)
- **Using Visual Studio Code** (`intro/vscode.md`)

---

<!-- === 来源: intro/importing.md === -->

# Importing Modules[](#importing-modules "Link to this heading")

Importing modules for the quantum tool suite is similar but slightly different to the typical import process for addons.
For instance, to import the ‘Transmon’ class from the ‘hamiltonian\_analysis’ module you would:

```
from keysight.ads.de import app
quantum_addon = app.import_addon_as_module("Quantum Tools")
quantum_analysis_module = quantum_addon.src.keysight.ads.quantum_analysis
transmon = quantum_analysis_module.python.hamiltonian_analysis.Transmon
```


---

<!-- === 来源: intro/index.md === -->

# Introduction[](#introduction "Link to this heading")

* [Importing Modules](importing.md)
* [Using Visual Studio Code](vscode.md)


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

