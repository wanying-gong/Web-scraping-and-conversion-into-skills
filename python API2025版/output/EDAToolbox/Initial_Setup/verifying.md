<!-- 来源: Initial_Setup\verifying.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Initial Setup](index.md)
* Verifying Installation

1.2.4

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Initial_Setup/verifying.rst.txt)

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

* [API Reference](../API_Reference/index.md)
  + [ADS](../API_Reference/ads/index.md)
    - [Functions](../API_Reference/ads/functions/index.md)
    - [Classes](../API_Reference/ads/classes/index.md)
      * [ADS](../API_Reference/ads/classes/ads.md)
      * [CircuitSimulator](../API_Reference/ads/classes/circuit_simulator.md)
  + [Circuit API](../API_Reference/circuit/index.md)
    - [Functions](../API_Reference/circuit/functions/index.md)
    - [Classes](../API_Reference/circuit/classes/index.md)
      * [Circuit](../API_Reference/circuit/classes/circuit.md)
      * [Definition](../API_Reference/circuit/classes/definition.md)
      * [Instance](../API_Reference/circuit/classes/instance.md)
      * [Node](../API_Reference/circuit/classes/node.md)
      * [OptimizationRange](../API_Reference/circuit/classes/optimization_range.md)
      * [TuningRange](../API_Reference/circuit/classes/tuning_range.md)
      * [Value](../API_Reference/circuit/classes/value.md)
  + [Dataset](../API_Reference/dataset/index.md)
  + [External API](../API_Reference/extra/index.md)
    - [empro.analysis](../API_Reference/extra/empro/index.md)
  + [Multi Python API](../API_Reference/multi_python/index.md)
    - [Functions](../API_Reference/multi_python/functions/index.md)
  + [xxPro](../API_Reference/xxpro/index.md)
* [Initial Setup](index.md)
  + [Installation](installation.md)
  + [Prerequisites](prerequisites.md)
  + Verifying Installation
  + [SSH](ssh.md)
* [Examples](../Examples/index.md)
* [How-To](../How-To/index.md)
  + [Create a Circuit](../How-To/circuit.md)
  + [Run a Circuit Simulation](../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../How-To/sipro.md)
* [Release Notes](../release_notes/index.md)

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

On this page

[Previous

Prerequisites](prerequisites.md)
[Next

SSH](ssh.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top