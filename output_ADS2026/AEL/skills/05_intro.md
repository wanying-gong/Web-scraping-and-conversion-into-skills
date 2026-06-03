# Intro
> **说明：** Intro 相关页面。

> **何时使用：** 当你需要查阅 Intro 相关内容时

---

## 本文件目录

- **Introduction** (`intro/index.md`)
- **Using AEL Functionality in Python** (`intro/usage.md`)

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

