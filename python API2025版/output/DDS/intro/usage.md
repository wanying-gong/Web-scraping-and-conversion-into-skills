<!-- 来源: intro\usage.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* [Introduction](index.md)
* Using Data Display functionality in Python

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](index.md)
  + [Licensing](licensing.md)
  + Using Data Display functionality in Python
  + [Using Visual Studio Code](vscode.md)
* [Concepts](../concepts/index.md)
  + [Python Script Execution](../concepts/execution.md)
* [Reference](../reference/index.md)
  + [keysight.ads.dds](../reference/dds/index.md)
    - [DDSFile](../reference/dds/file.md)
    - [Page](../reference/dds/page.md)
    - [Point](../reference/dds/point.md)
    - [Rect](../reference/dds/rect.md)
    - [Grid](../reference/dds/grid.md)
    - [Plots](../reference/dds/plots.md)
    - [Axes](../reference/dds/axes.md)
    - [Legend](../reference/dds/legend.md)
    - [Trace](../reference/dds/trace.md)
    - [Markers](../reference/dds/marker.md)
    - [Line Markers](../reference/dds/linemarker.md)
    - [Limit Lines](../reference/dds/limitlines.md)
    - [Masks](../reference/dds/masks.md)
    - [Specification](../reference/dds/specifications.md)
    - [Equation](../reference/dds/equation.md)
    - [PyEquation](../reference/dds/pyequation.md)
    - [Text](../reference/dds/text.md)
    - [Picture](../reference/dds/picture.md)
    - [Shapes](../reference/dds/shapes.md)
    - [Group](../reference/dds/group.md)
    - [Common Properties](../reference/dds/basic.md)
    - [Print](../reference/dds/print.md)
    - [Object](../reference/dds/objects.md)
    - [Window](../reference/dds/windows.md)
    - [Widget](../reference/dds/pywidget.md)
  + [keysight.ads.dds.experimental](../reference/dds/experimental/index.md)
  + [keysight.ads.dds.app](../reference/dds/app/index.md)
    - [Addon](../reference/dds/app/addon.md)
    - [Callbacks](../reference/dds/app/callbacks.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
  + [How to Use Pytest](../howto/pytest.md)
* [Examples](../examples/index.md)
  + [Create Shapes](../examples/ex_shapes.md)
  + [Create Pages and Windows](../examples/ex_pages_and_windows.md)
  + [Create and Modify DDS file](../examples/ex_modified_file.md)
  + [Create Markers](../examples/ex_markers.md)
  + [Create Line Markers](../examples/ex_line_markers.md)
  + [Create equations using dataset variables](../examples/ex_expressions_and_dataframes.md)
  + [Plot Simulation Output](../examples/ex_simple.md)
  + [Plot Amplifier Simulation Data](../examples/ex_optimized_amp.md)
  + [Create Pages and Windows](../examples/ex_python_equations.md)
  + [Add Specifications to a Plot](../examples/ex_specifications.md)
  + [Plot a Time-Domain Output Voltage Waveform](../examples/ex_trantest.md)
  + [Plot Parameter Extraction of Simulation Data](../examples/ex_crq_extraction.md)
  + [Add custom menu to Data-Display file](../examples/ex_custom_menu.md)
  + [Print PDF file](../examples/ex_print.md)
* [App Examples](../appExamples/index.md)
  + [Add Menu to Data Display Menubar](../appExamples/ex_custom_menu.md)
  + [Add Widgets to Data Display Page](../appExamples/ex_page_widget.md)
  + [Add Matplotlib Plot to Data Display Window](../appExamples/ex_matplotlib_widget.md)
  + [Add an Addon to Data Display](../appExamples/ex_addon.md)
* [Addon Examples](../addonExamples/index.md)
  + [Addon to Generate Menus](../addonExamples/ex_addon/init.md)
  + [3D Plot Addon](../addonExamples/ex_addon_3d_plot/index.md)
    - [Menu for 3D Plot Addon](../addonExamples/ex_addon_3d_plot/init.md)
    - [Plot for 3D Plot Addon](../addonExamples/ex_addon_3d_plot/ex_addon_3d_plot.md)

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

On this page

[Previous

Licensing](licensing.md)
[Next

Using Visual Studio Code](vscode.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top