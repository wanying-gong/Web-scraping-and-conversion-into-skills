<!-- 来源: examples\ex_print.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* [Examples](index.md)
* Print PDF file

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
  + [Create Line Markers](ex_line_markers.md)
  + [Create equations using dataset variables](ex_expressions_and_dataframes.md)
  + [Plot Simulation Output](ex_simple.md)
  + [Plot Amplifier Simulation Data](ex_optimized_amp.md)
  + [Create Pages and Windows](ex_python_equations.md)
  + [Add Specifications to a Plot](ex_specifications.md)
  + [Plot a Time-Domain Output Voltage Waveform](ex_trantest.md)
  + [Plot Parameter Extraction of Simulation Data](ex_crq_extraction.md)
  + [Add custom menu to Data-Display file](ex_custom_menu.md)
  + Print PDF file
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

# Print PDF file[](#print-pdf-file "Link to this heading")

This example prints all pages or a page of a dds file.

```
# Copyright Keysight Technologies 2023 - 2024
import pathlib

import keysight.ads.dds as dds

examples_path = pathlib.Path(__file__).parent.resolve()
dds_file = dds.new_dds_file("amplifier.ds", examples_path)

# Page 1 - plot with traces and markers
page1 = dds_file.pages[0]

plot = page1.add_plot()
traces = plot.add_traces(["dB(S11)", "dB(S21)"])

marker = traces[0].add_marker("m1", "0.5 GHz")
plot.add_line_marker("m2", "0.2 GHz")

# Page 2 - text and polygon
page2 = dds_file.new_page("page 2")

text = page2.add_text("Page 2", (0, 0))

box = page2.add_box(dds.Rect(top_left=text.bbox.bottom_left, bottom_right=text.bbox.bottom_left + (500, 500)))
box.line_properties = dds.LineProperties(dds.LineType.SOLID, dds.Color(5), 10)

polygon = page2.add_polygon([box.bbox.top_right, box.bbox.top_right + (500, 500), box.bbox.top_right + (500, 0)])
polygon.fill_properties = dds.FillProperties("solid")

# Page 3 - smith chart
page3 = dds_file.new_page("page 3")

smith = page3.add_smith_chart()
smith.add_legend()
smith.add_trace("S")

# save the file
dds_file.save("print_to_pdf.dds")

# print all pages
all_pages_pdf = examples_path / "all_dds_pages.pdf"
dds_file.print_all_pages_to_pdf(all_pages_pdf)

# print specific pages
page_2_pdf = examples_path / "plots.pdf"
dds_file.print_pages_by_name_to_pdf(page_2_pdf, ["page 1", "page 3"])
```

On this page

[Previous

Add custom menu to Data-Display file](ex_custom_menu.md)
[Next

App Examples](../appExamples/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top