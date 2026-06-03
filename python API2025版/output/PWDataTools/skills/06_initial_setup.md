# Initial Setup
> **说明：** Initial Setup 相关页面。

> **何时使用：** 当你需要查阅 Initial Setup 相关内容时

---

## 本文件目录

- **Dependencies** (`initial_setup/dependencies.md`)
- **Initial Setup** (`initial_setup/index.md`)
- **Installation** (`initial_setup/installation.md`)

---

<!-- === 来源: initial_setup/dependencies.md === -->

# Dependencies[](#dependencies "Link to this heading")

## Python libraries[](#python-libraries "Link to this heading")

Below are the Python and library dependencies for `pwdatatools`.

* Python: 3.9 and higher
* pandas: 1.3 and higher
* numpy: 1.18 and higher

If you use pip to install `pwdatatools`, the dependencies are installed automatically (if missing from your Python environment). If you have an older version of a dependency already installed, pip has various options for controlling what happens. If you are using Anaconda, see the Anaconda documentation for instructions on how to install a Python wheel file without breaking existing packages.

In addition to the above depedencies, pwdatatools has soft dependencies on the `scipy` library. This means that `scipy` is not installed automatically by pip (by default). This is because `scipy` is only used for a small subset of the functionality within `pwdatatools`. `pwdatatools` can also make use of two Keysight-provided Python libraries that are not available on PyPI.org. This means they are not automatically installed when you pip install Data Tools. You can find these libraries in the ADS installation directory, or just ask your Keysight field or support contact.

* The `keysight-ads-dataset` library: not strictly required for reading and writing ADS datasets, but is recommended since it speeds up file processing (located in the ADS installation directory in the “tools/python/wheelhouse” subdirectory)
* The `keysight-systemvue` library: required for reading and writing SystemVue datasets (located in the SystemVue installation directory in the “Python” subdirectory)

Note

The term ‘and higher’ above includes new minor and maintenance versions, but *not* any new major versions.

PathWave Data Tools also includes a `viz` module for data visualization. This module requires the following additional dependencies:

* `matplotlib`
* `seaborn`

However, if you are not using the `viz` module, you do not need to install these dependencies.

## Keysight software[](#keysight-software "Link to this heading")

In order to work with certain types of datafiles, ADS or SystemVue installations may be required. Below are the minimum recommended versions.

* PathWave Advanced Design System (ADS) 2021 or later
* PathWave System Design (SystemVue) 2023 or later

## Licensing[](#licensing "Link to this heading")

Most of the functionality of `pwdatatools` does not require a license. However, an ADS Data Display license is required to read measured load pull datafile formats (Maury, Focus, and Keysight formats). Addtionally, if you are on Windows OS, you must download and install EEsof Licensing Tools from here: [https://edadocs.software.keysight.com/display/downloads/Licensing+Software+Downloads](https://edadocs.software.keysight.com/display/downloads/Licensing%2BSoftware%2BDownloads). The required licensing bits are included in the ADS installation for Linux.


---

<!-- === 来源: initial_setup/index.md === -->

# Initial Setup[](#initial-setup "Link to this heading")

* [Installation](installation.md)
* [Dependencies](dependencies.md)
  + [Python libraries](dependencies.md#python-libraries)
  + [Keysight software](dependencies.md#keysight-software)
  + [Licensing](dependencies.md#licensing)


---

<!-- === 来源: initial_setup/installation.md === -->

# Installation[](#installation "Link to this heading")

These instructions describe how to use `pip` to install Data Tools. Note that `pip` will also install or update the Python libraries listed in [Dependencies](dependencies.md#dependencies). The first set of instructions are for users; instructions for developers follow in the next section.

Warning

These instructions assume you are using a standard Python distribution from [python.org](https://www.python.org), and are not appropriate for Anaconda. If you are using Anaconda, refer to [their website](https://www.anaconda.com/) for instructions on how to properly install a Python wheel into your Anaconda environment without breaking packages.

Note

You can ignore these installation instructions if you are using the Python environment that is included in ADS because `pwdatatools` and all its dependencies are already installed.

You won’t find `pwdatatools` on PyPI.org, so unless you’re a Keysight employee, you won’t be able to pip install `pwdatatools` from the web like most Python libraries you are using. You will have to obtain a wheel file from our Knowledge Center or from a product that includes it (for example ADS). You can obtain the wheel file from the Knowledge Center here: <https://edadocs.software.keysight.com/pages/viewpage.action?pageId=748497656>.

See also

If you are new to installing Python packages, refer to the [Python Packaging User Guide](https://packaging.python.org/tutorials/installing-packages/).

Below shows how to pip install a `pwdatatools` wheel file on Windows. It assumes you have already downloaded the wheel file to some local folder on your computer.

```
> pip install keysight_pwdatatools-0.11.0-cp312-cp312-win_amd64.whl
```

Note

There are several wheel files created for each release of `pwdatatools`. Each wheel is targeted to one version of Python and one operating system (Windows or Linux). Verify that the wheel file that you have matches your version of Python and the operating system that you are using. Also, when you install it, be sure you are invoking the correct version of pip that is asssociated with your desired Python environment. The aforementioned tutorial on installing packages covers this, as well as how to create and activate a Python “virtual environment” (a good practice).

Some capabilities in `pwdatatools` rely on having ADS or SystemVue installed. See [Keysight software](dependencies.md#keysight-software) for more details.

Important

An ADS Data Display license is required to read measured load pull datafile formats. Additionally, if you are on Windows OS, you must download and install EEsof Licensing Tools from here: [https://edadocs.software.keysight.com/display/downloads/Licensing+Software+Downloads](https://edadocs.software.keysight.com/display/downloads/Licensing%2BSoftware%2BDownloads).


---

