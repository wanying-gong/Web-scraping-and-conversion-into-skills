<!-- 来源: appExamples\ex_addon.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* [App Examples](index.md)
* Add an Addon to Data Display

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../intro/index.md)
  + [Licensing](../intro/licensing.md)
  + [Using Data Display functionality in Python](../intro/usage.md)
  + [Using Visual Studio Code](../intro/vscode.md)
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
    - [DDSQtWidget](../reference/dds/experimental/qtwidget.md)
  + [keysight.ads.dds.app](../reference/dds/app/index.md)
    - [Addon](../reference/dds/app/addon.md)
    - [Callbacks](../reference/dds/app/callbacks.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating an ADS based Python virtual environment](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
    - [ADS Python Environment Variables](../howto/pyenvvars.md)
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
  + [Experimental Examples](../examples/experimental/index.md)
    - [DDS Qt Widget displayed in a Qt QDialog](../examples/experimental/ex_dds_qt_widget.md)
    - [DDS Qt Widget printed using a Qt QPrinter](../examples/experimental/ex_dds_qt_widget.md#dds-qt-widget-printed-using-a-qt-qprinter)
    - [DDS Qt Widget output to a Qt QPixmap](../examples/experimental/ex_dds_qt_widget.md#dds-qt-widget-output-to-a-qt-qpixmap)
    - [DDS rename dataset and update expressions](../examples/experimental/ex_rename_dataset.md)
* [App Examples](index.md)
  + [Add Menu to Data Display Menubar](ex_custom_menu.md)
  + [Add Widgets to Data Display Page](ex_page_widget.md)
  + [Add Matplotlib Plot to Data Display Window](ex_matplotlib_widget.md)
  + Add an Addon to Data Display
* [Addon Examples](../addonExamples/index.md)
  + [Addon to Generate Menus](../addonExamples/ex_addon/init.md)
  + [3D Plot Addon](../addonExamples/ex_addon_3d_plot/index.md)
    - [Menu for 3D Plot Addon](../addonExamples/ex_addon_3d_plot/init.md)
    - [Plot for 3D Plot Addon](../addonExamples/ex_addon_3d_plot/ex_addon_3d_plot.md)

# Add an Addon to Data Display[](#add-an-addon-to-data-display "Link to this heading")

This is an example of how python can be used to add an addon to Data Display.
This must be run in application mode.

```
# Copyright Keysight Technologies 2024 - 2024
from pathlib import Path

import keysight.ads.dds.app as app

examples_path = Path(__file__).parent.resolve()

addon = app.find_addon("MyAddon")
if addon is None:
    addon_path = examples_path / "ex_addon" / "__init__.py"
    addon = app.Addon("MyAddon", addon_path, enabled=True)
    app.add_user_addon(addon)
```

On this page

[Previous

Add Matplotlib Plot to Data Display Window](ex_matplotlib_widget.md)
[Next

Addon Examples](../addonExamples/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top