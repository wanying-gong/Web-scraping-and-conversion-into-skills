# How-To
> **说明：** 虚拟环境和 Pytest 等开发流程说明。

> **何时使用：** 当你需要配置 AEL Python 开发环境或测试流程时

---

## 本文件目录

- **How-To** (`howto/index.md`)
- **How to Set Up a Python Virtual Environment** (`howto/venv.md`)
- **How to Use Pytest** (`howto/pytest.md`)

---

<!-- === 来源: howto/index.md === -->

# How-To[](#how-to "Link to this heading")

* [How to Set Up a Python Virtual Environment](venv.md)
* [How to Use Pytest](pytest.md)


---

<!-- === 来源: howto/venv.md === -->

# How to Set Up a Python Virtual Environment[](#how-to-set-up-a-python-virtual-environment "Link to this heading")

It is possible to access AEL python functionality in a python virtual environment rather than the embedded ADS Python installation.

The venv must be created using the Python shipped with ADS, using the **--system-site-packages** flag so that the venv has access to the **keysight.ads.ael** Python API.

> For linux:
>
> ```
> $HPEESOF_DIR/tools/python/bin/python3 -m venv --system-site-packages $HOME/ads_venv
> ```
>
> For windows:
>
> ```
> %HPEESOF_DIR%\tools\python\python -m venv --system-site-packages %HOME%\ads_venv
> ```


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

