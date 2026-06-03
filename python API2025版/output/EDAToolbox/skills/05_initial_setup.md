# Initial Setup
> **说明：** Initial Setup 相关页面。

> **何时使用：** 当你需要查阅 Initial Setup 相关内容时

---

## 本文件目录

- **Initial Setup** (`Initial_Setup/index.md`)
- **Installation** (`Initial_Setup/installation.md`)
- **Prerequisites** (`Initial_Setup/prerequisites.md`)
- **SSH** (`Initial_Setup/ssh.md`)
- **Verifying Installation** (`Initial_Setup/verifying.md`)

---

<!-- === 来源: Initial_Setup/index.md === -->

# Initial Setup[](#initial-setup "Link to this heading")

* [Installation](installation.md)
  + [Installing in xxPro distribution](installation.md#installing-in-xxpro-distribution)
    - [Examples](installation.md#examples)
* [Prerequisites](prerequisites.md)
  + [EDA Toolbox + Circuit simulation](prerequisites.md#eda-toolbox-circuit-simulation)
  + [EDA Toolbox + xxPro simulation](prerequisites.md#eda-toolbox-xxpro-simulation)
  + [EDA Toolbox + other](prerequisites.md#eda-toolbox-other)
* [Verifying Installation](verifying.md)
  + [Base installation](verifying.md#base-installation)
  + [Modules used in examples](verifying.md#modules-used-in-examples)
    - [Matplotlib, Numpy, Pandas, Scipy](verifying.md#matplotlib-numpy-pandas-scipy)
    - [Seaborn](verifying.md#seaborn)
    - [PathWave Datatools](verifying.md#pathwave-datatools)
* [SSH](ssh.md)


---

<!-- === 来源: Initial_Setup/installation.md === -->

# Installation[](#installation "Link to this heading")

These instructions describe how to use `pip` to install the EDA Toolbox.

Warning

These instructions assume you are using a standard Python distribution from [python.org](https://www.python.org). Python 3.10.x is the recommended installation to use.

On Linux:

```
pip install /path/to/wheelfile/keysight.edatoolbox-1.2.1-py3-none-any.whl
```

On Windows, Python is often installed through `py` allowing to select a particular version and acts as jump station to the various Python installation available on the system.

```
py -m pip install c:\path\to\wheelfile\keysight.edatoolbox-1.2.s1-py3-none-any.whl
```

The wheel files can be downloaded here: [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

## Installing in xxPro distribution[](#installing-in-xxpro-distribution "Link to this heading")

The EDA Toolbox can be installed in any generic Python distribution, but also be inside the Python distribution of EMPro or SIPro for that matter. That may be necessary if you
want to combine the capabilities of both. Some example scripts show how to do that and in those cases it is recommended to install the Toolbox into the distribution of xxPro.

Installing into the xxPro distribution starts with making sure you are using the Python of the xxPro distribution.

If you have ADS 2023 or more recent, open a terminal/command prompt and:

```
C:\Program Files\Keysight\ADS2025\fem\2025.00\win32_64\bin\emproenv.bat
```

On Linux start a bash shell under the xxPro environment:

```
/path/to/emproenv.sh bash
```

After you have done that, you can again use the pip installation procedure. Note that on Windows andyou will need to use python instead of py, on Linux use python:

```
python -m pip install c:\path\to\wheelfile\keysight.edatoolbox-1.2.1-py3-none-any.whl
```

```
python -m pip install /path/to/wheelfile/keysight.edatoolbox-1.2.1-py3-none-any.whl
```

### Examples[](#examples "Link to this heading")

The examples can be found on the [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).


---

<!-- === 来源: Initial_Setup/prerequisites.md === -->

# Prerequisites[](#prerequisites "Link to this heading")

## EDA Toolbox + Circuit simulation[](#eda-toolbox-circuit-simulation "Link to this heading")

To use the EDA Toolbox with circuit simulation, including the building and manipulating of circuits, it is sufficient to have a working Python 3.8+ installation and an ADS 2022 U1 or more recent installation.
For the Python EDA Toolbox version 3.10.x is recommended though and that can be found on [python.org](https://www.python.org)

## EDA Toolbox + xxPro simulation[](#eda-toolbox-xxpro-simulation "Link to this heading")

To use the EDA Toolbox with EMPro/SIPro simulation, including the building and manipulating of circuits, it is recommended to use an ADS 2023 or more recent installation. That installation already
comes with Python 3.10 and it is recommend to use the Python installation then that comes with it to fully enjoy the capabilities of the combination. Refer to the installation manual on how
to install the EDA Toolbox into the Python of xxPro or ADS.

## EDA Toolbox + other[](#eda-toolbox-other "Link to this heading")

To use the EDA Toolbox with other functionality it is typically sufficient to have a working Python 3.8+ installation and the respective product like VSA or SystemVue installed.
For the Python EDA Toolbox version 3.10.x is recommended though and that can be found on [python.org](https://www.python.org)


---

<!-- === 来源: Initial_Setup/ssh.md === -->

# SSH[](#ssh "Link to this heading")

When you are using SSH to run Python code on a remote machine in combination with the EDA Toolbox you need to make sure that the SSH session is able to open a graphical window on the remote machine. This is necessary for some operations executed by the EDA Toolbox, even if it does not display a GUI at first sight. In some cases there is no
display available on the remote machine, so you need to use X11 forwarding to display the GUI on your local machine. To enable X11 forwarding, you need to add the -X option to the SSH command.

Alternatively you can use a virtual display, which is a display that is not connected to a physical display device. This is useful when you are running the EDA Toolbox on a remote machine that does not have a display. To use a virtual display, you need to install the xvfb package and run the following command before starting the EDA Toolbox:

`
xvfb-run -a -s “-screen 0 1400x900x24” python3 my\_script.py
`


---

<!-- === 来源: Initial_Setup/verifying.md === -->

# Verifying Installation[](#verifying-installation "Link to this heading")

After the installation you may want to verify if everything is set up properly.

Warning

These instructions assume you are using a standard Python distribution from [python.org](https://www.python.org). Python 3.10.x is the recommended installation to use.
If you have multiple Python distributions installed on Windows you will need to specify to ‘py’ which version you use. In our case this will be: py -3.10, so
equivalent pip instructions below become py -3.10 -m pip instead of just py -m pip.

If you are using the ADS/xxPro installation all these commands will use python instead of py.

## Base installation[](#base-installation "Link to this heading")

In the same command prompt you did the install, now execute below command and it should print out “Keysight EDA Toolbox succesfully installed”, if there is a Python stacktrace with a module import error, then the installation has failed.

```
py -c"import keysight.edatoolbox;print('Keysight EDA Toolbox succesfully installed')"
```

On Linux:

```
python3 -c"import keysight.edatoolbox;print('Keysight EDA Toolbox succesfully installed')"
```

## Modules used in examples[](#modules-used-in-examples "Link to this heading")

The examples also use other modules beyond the keysight.edatoolbox, such as plotting libraries Matplotlib and Seaborn or the PathWave datatools.
You can verify in similar way if the modules are properly installed.

### Matplotlib, Numpy, Pandas, Scipy[](#matplotlib-numpy-pandas-scipy "Link to this heading")

```
py -c"import numpy;print('Numpy succesfully installed')"
py -c"import matplotlib;print('Matplotlib succesfully installed')"
py -c"import pandas;print('Pandas succesfully installed')"
py -c"import scipy;print('Scipy succesfully installed')"
py -c"import plotly ;print('plotly succesfully installed')"
```

If it fails, below instructions can be used to install Matplotlib, the recipe is the same for numpy, maptlotlib, pandas, scipy and plotly.

```
py -m pip install matplotlib
```

Or all at once:

```
py -m pip install numpy matplotlib pandas scipy plotly
```

Matplotlib can require building of additional modules and requiring the availability of a compiler on your system. If that is the case, you can also use some of the pre-built wheels.
Those can be downloaded here: [Pre-built wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib) In that case use the whl file to install it, download the correct wheel for your Python version,
the recommended version is Python 3.10, so the packages will look in signature as follows:

```
py -m pip install SciPy-1.8.1-cp310-cp310-win_amd64.whl
```

### Seaborn[](#seaborn "Link to this heading")

```
py -c"import seaborn;print('Seaborn succesfully installed')"
```

If it fails, below instructions can be used to install Seaborn:

```
py -m pip install seaborn
```

### PathWave Datatools[](#pathwave-datatools "Link to this heading")

```
py -c"import keysight.pwdatatools;print('PathWave datatools succesfully installed')"
```

[PathWave Datatools user installation guide](https://docs.keysight.com/pwdt0x9x0/initial-setup/installation)

Alternatively you can grab the 0.5.0 wheel here: [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202). and install using pip

```
py -m pip install kkeysight_pwdatatools-0.5.0-cp310-cp310-win_amd64.whl
```

There is a possibilty that saving image files can throw error using plotly (for certain versions), in that case , try to install specific version of kaleido

```
py -m pip install kaleido==0.1.0post1
```


---

