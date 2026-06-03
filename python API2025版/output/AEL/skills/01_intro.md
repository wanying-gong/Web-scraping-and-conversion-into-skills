# Introduction
> **说明：** AEL Python 文档入口、概览和 Python 中使用 AEL 功能的说明。

> **何时使用：** 当你需要了解 AEL Python 文档结构或基础使用方式时

---

## 本文件目录

- **AEL Python documentation** (`index.md`)
- **Introduction** (`intro/index.md`)
- **Using AEL Functionality in Python** (`intro/usage.md`)

---

<!-- === 来源: index.md === -->

# AEL Python documentation[](#ael-python-documentation "Link to this heading")

Contents:

* [Introduction](intro/index.md)
  + [Using AEL Functionality in Python](intro/usage.md)
* [Concepts](concepts/index.md)
  + [AEL Interoperability](concepts/ael_interoperability.md)
  + [AEL Type Conversions](concepts/ael_type_conversions.md)
* [Reference](reference/index.md)
  + [keysight.ads.ael](reference/ael.md)
* [Examples](examples/index.md)
  + [Calling Between AEL and Python](examples/ex_calling_ael_and_python.md)
* [How-To](howto/index.md)
  + [How to Set Up a Python Virtual Environment](howto/venv.md)
  + [How to Use Pytest](howto/pytest.md)


---

<!-- === 来源: intro/index.md === -->

# Introduction[](#introduction "Link to this heading")

* [Using AEL Functionality in Python](usage.md)


---

<!-- === 来源: intro/usage.md === -->

# Using AEL Functionality in Python[](#using-ael-functionality-in-python "Link to this heading")

A Python script running inside of ADS can access functionality of AEL.

```
from keysight.ads import ael
```

The `keysight.ads.ael` package is not currently available as a pip-installable package.
To get access to this package, use any one of these approaches:

> 1. Use the Python interpreter in `$HPEESOF_DIR/tools/python`.
> 2. Create a virtual environment based on that interpreter. See [How to Set Up a Python Virtual Environment](../howto/venv.md).
> 3. Add `$HPEESOF_DIR/tools/python/packages` onto your Python’s `sys.path`.

Set the environment variable `HPEESOF_DIR` to point to your ADS installation prior to
using the `keysight.ads.ael` package.


---

