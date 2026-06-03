<!-- 来源: addonExamples\ex_addon_3d_plot\init.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Addon Examples](../index.md)
* [3D Plot Addon](index.md)
* Menu for 3D Plot Addon

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

* [Introduction](../../intro/index.md)
  + [Licensing](../../intro/licensing.md)
  + [Using Data Display functionality in Python](../../intro/usage.md)
  + [Using Visual Studio Code](../../intro/vscode.md)
* [Concepts](../../concepts/index.md)
  + [Python Script Execution](../../concepts/execution.md)
* [Reference](../../reference/index.md)
  + [keysight.ads.dds](../../reference/dds/index.md)
    - [DDSFile](../../reference/dds/file.md)
    - [Page](../../reference/dds/page.md)
    - [Point](../../reference/dds/point.md)
    - [Rect](../../reference/dds/rect.md)
    - [Grid](../../reference/dds/grid.md)
    - [Plots](../../reference/dds/plots.md)
    - [Axes](../../reference/dds/axes.md)
    - [Legend](../../reference/dds/legend.md)
    - [Trace](../../reference/dds/trace.md)
    - [Markers](../../reference/dds/marker.md)
    - [Line Markers](../../reference/dds/linemarker.md)
    - [Limit Lines](../../reference/dds/limitlines.md)
    - [Masks](../../reference/dds/masks.md)
    - [Specification](../../reference/dds/specifications.md)
    - [Equation](../../reference/dds/equation.md)
    - [PyEquation](../../reference/dds/pyequation.md)
    - [Text](../../reference/dds/text.md)
    - [Picture](../../reference/dds/picture.md)
    - [Shapes](../../reference/dds/shapes.md)
    - [Group](../../reference/dds/group.md)
    - [Common Properties](../../reference/dds/basic.md)
    - [Print](../../reference/dds/print.md)
    - [Object](../../reference/dds/objects.md)
    - [Window](../../reference/dds/windows.md)
    - [Widget](../../reference/dds/pywidget.md)
  + [keysight.ads.dds.experimental](../../reference/dds/experimental/index.md)
  + [keysight.ads.dds.app](../../reference/dds/app/index.md)
    - [Addon](../../reference/dds/app/addon.md)
    - [Callbacks](../../reference/dds/app/callbacks.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
  + [How to Use Pytest](../../howto/pytest.md)
* [Examples](../../examples/index.md)
  + [Create Shapes](../../examples/ex_shapes.md)
  + [Create Pages and Windows](../../examples/ex_pages_and_windows.md)
  + [Create and Modify DDS file](../../examples/ex_modified_file.md)
  + [Create Markers](../../examples/ex_markers.md)
  + [Create Line Markers](../../examples/ex_line_markers.md)
  + [Create equations using dataset variables](../../examples/ex_expressions_and_dataframes.md)
  + [Plot Simulation Output](../../examples/ex_simple.md)
  + [Plot Amplifier Simulation Data](../../examples/ex_optimized_amp.md)
  + [Create Pages and Windows](../../examples/ex_python_equations.md)
  + [Add Specifications to a Plot](../../examples/ex_specifications.md)
  + [Plot a Time-Domain Output Voltage Waveform](../../examples/ex_trantest.md)
  + [Plot Parameter Extraction of Simulation Data](../../examples/ex_crq_extraction.md)
  + [Add custom menu to Data-Display file](../../examples/ex_custom_menu.md)
  + [Print PDF file](../../examples/ex_print.md)
* [App Examples](../../appExamples/index.md)
  + [Add Menu to Data Display Menubar](../../appExamples/ex_custom_menu.md)
  + [Add Widgets to Data Display Page](../../appExamples/ex_page_widget.md)
  + [Add Matplotlib Plot to Data Display Window](../../appExamples/ex_matplotlib_widget.md)
  + [Add an Addon to Data Display](../../appExamples/ex_addon.md)
* [Addon Examples](../index.md)
  + [Addon to Generate Menus](../ex_addon/init.md)
  + [3D Plot Addon](index.md)
    - Menu for 3D Plot Addon
    - [Plot for 3D Plot Addon](ex_addon_3d_plot.md)

# Menu for 3D Plot Addon[](#menu-for-3d-plot-addon "Link to this heading")

This adds the menu for a 3D Plot. The callback is in a seperate python file.

```
# Copyright Keysight Technologies 2024 - 2024
"""Addon example that will generate menus based on window type."""

import keysight.ads.dds as dds
import keysight.ads.dds.app as app
from PySide2.QtWidgets import QMenu

from .ex_matplotlib_3d import add_3d_plot

def popup_callback(menu: QMenu, file: dds.DDSFile, window: dds.Window, pos: dds.Point) -> None:
    page_name = window.current_page.name

    if len(file.selected_objects) == 0:
        action = menu.addAction("Insert 3D Plot")
        action.triggered.connect(lambda: add_3d_plot(file, window, page_name, pos))

def setup_addon(addon: app.Addon) -> None:
    # Implementation of this method is optional but if you do, DO NOT invoke UI from this function!
    app.register_popup_callback(popup_callback)

def shutdown_addon(addon: app.Addon) -> None:
    # Implementation of this method is optional but if you do, DO NOT invoke UI from this function!
    ...

def identify() -> None:
    print("3D Addon Example")
```

On this page

[Previous

3D Plot Addon](index.md)
[Next

Plot for 3D Plot Addon](ex_addon_3d_plot.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top