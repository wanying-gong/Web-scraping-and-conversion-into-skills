<!-- 来源: examples\ex_pages_and_windows.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* [Examples](index.md)
* Create Pages and Windows

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
  + Create Pages and Windows
  + [Create and Modify DDS file](ex_modified_file.md)
  + [Create Markers](ex_markers.md)
  + [Create Line Markers](ex_line_markers.md)
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

# Create Pages and Windows[](#create-pages-and-windows "Link to this heading")

This example creates a DDS file with two pages and windows.

```
# Copyright Keysight Technologies 2023 - 2023
import pathlib

import keysight.ads.dds as dds

examples_path = pathlib.Path(__file__).parent.resolve()
dds_file = dds.new_dds_file("amplifier.ds", examples_path)

page = dds_file.pages[0]
page2 = dds_file.new_page("page 2")
dds_file.new_window()

page2.add_equation("x", "S11")
page2.add_equation("x2", "2*S11")
page2.add_equation("dbx2", "dB(x2)")

plot1 = page.add_plot()
plot1.add_traces(["dB(S11)"])

plot2 = page.add_plot()
plot2.add_traces(["dB(S21)"])

plot3 = page.add_plot()
plot3.add_traces(["dB(S12)"])

plot4 = page.add_plot()
plot4.add_traces(["dB(S22)"])

page.align_grid([plot1, plot2, plot3, plot4], 2, 2)

plot5 = page2.add_plot()
plot5.add_trace("dbx2")

dds_file.windows[0].current_page = "page 2"
dds_file.windows[1].current_page = "page 1"

dds_file.windows[0].zoom_all()
dds_file.windows[1].zoom_all()

dds_file.save("pages_and_windows.dds")
```

On this page

[Previous

Create Shapes](ex_shapes.md)
[Next

Create and Modify DDS file](ex_modified_file.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top