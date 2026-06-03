# Intro
> **说明：** Intro 相关页面。

> **何时使用：** 当你需要查阅 Intro 相关内容时

---

## 本文件目录

- **Introduction** (`intro/index.md`)
- **Using Visual Studio Code** (`intro/vscode.md`)

---

<!-- === 来源: intro/index.md === -->

# Introduction[](#introduction "Link to this heading")

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

