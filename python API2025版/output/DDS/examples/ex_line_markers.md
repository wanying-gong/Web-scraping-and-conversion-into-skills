<!-- 来源: examples\ex_line_markers.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* [Examples](index.md)
* Create Line Markers

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
  + [keysight.ads.dds.app](../reference/dds/app/index.md)
    - [Addon](../reference/dds/app/addon.md)
    - [Callbacks](../reference/dds/app/callbacks.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
  + [How to Use Pytest](../howto/pytest.md)
* [Examples](index.md)
  + [Create Shapes](ex_shapes.md)
  + [Create Pages and Windows](ex_pages_and_windows.md)
  + [Create and Modify DDS file](ex_modified_file.md)
  + [Create Markers](ex_markers.md)
  + Create Line Markers
  + [Create equations using dataset variables](ex_expressions_and_dataframes.md)
  + [Plot Simulation Output](ex_simple.md)
  + [Plot Amplifier Simulation Data](ex_optimized_amp.md)
  + [Create Pages and Windows](ex_python_equations.md)
  + [Add Specifications to a Plot](ex_specifications.md)
  + [Plot a Time-Domain Output Voltage Waveform](ex_trantest.md)
  + [Plot Parameter Extraction of Simulation Data](ex_crq_extraction.md)
  + [Add custom menu to Data-Display file](ex_custom_menu.md)
  + [Print PDF file](ex_print.md)
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

# Create Line Markers[](#create-line-markers "Link to this heading")

This example creates a DDS file that contains a plot, trace and line marker.

```
# Copyright Keysight Technologies 2023 - 2023
from pathlib import Path

import keysight.ads.dds as dds

examples_path = Path(__file__).parent.resolve()
dds_file = dds.new_dds_file("amplifier.ds", examples_path)
page = dds_file.pages[0]

plot = page.add_plot()
plot.add_traces(["dB(S11)", "dB(S21)"])

line_marker = plot.add_line_marker("m1", "0.5 GHz")

line_marker.indep_value = "0.3 GHz"

plot.add_line_marker("m2", "0.8 GHz")

markers = plot.line_markers

dds_file.save("line_markers.dds")
```

On this page

[Previous

Create Markers](ex_markers.md)
[Next

Create equations using dataset variables](ex_expressions_and_dataframes.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top