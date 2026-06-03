<!-- 来源: examples\ex_shapes.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* [Examples](index.md)
* Create Shapes

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
* [Examples](index.md)
  + Create Shapes
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
  + [Print PDF file](ex_print.md)
  + [Experimental Examples](experimental/index.md)
    - [DDS Qt Widget displayed in a Qt QDialog](experimental/ex_dds_qt_widget.md)
    - [DDS Qt Widget printed using a Qt QPrinter](experimental/ex_dds_qt_widget.md#dds-qt-widget-printed-using-a-qt-qprinter)
    - [DDS Qt Widget output to a Qt QPixmap](experimental/ex_dds_qt_widget.md#dds-qt-widget-output-to-a-qt-qpixmap)
    - [DDS rename dataset and update expressions](experimental/ex_rename_dataset.md)
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

# Create Shapes[](#create-shapes "Link to this heading")

This example creates a DDS file that contains a box, circle, polygon, and text.

```
# Copyright Keysight Technologies 2023 - 2023
import pathlib

import keysight.ads.dds as dds

examples_path = pathlib.Path(__file__).parent.resolve()
dds_file = dds.new_dds_file("amplifier.ds", examples_path)

# changing appearance of objects
page = dds_file.pages[0]

dashed = dds.LineProperties(dds.LineType.SHORT_DASH, dds.Color(5), 7)
thick = dds.LineProperties(dds.LineType.SOLID, dds.Color(5), 10)

text = page.add_text("Outlined Text", (0, 0))
text.is_outlined = True
text.line_properties = dds.LineProperties(dds.LineType.SHORT_DASH, dds.Color(5), 10)

box = page.add_box(dds.Rect(top_left=text.bbox.bottom_left, bottom_right=text.bbox.bottom_left + (500, 500)))
box.line_properties = thick

circle = page.add_circle(text.bbox.bottom_right, 300)
circle.line_properties = dds.LineProperties(dds.LineType.LONG_DOT_DASH, dds.Color((255, 0, 0)))

polygon = page.add_polygon([box.bbox.top_right, box.bbox.top_right + (500, 500), box.bbox.top_right + (500, 0)])
polygon.fill_properties = dds.FillProperties("solid")

plot = page.add_plot()
trace = plot.add_trace("[10::100]")
trace.line_properties = thick

# plots arranged on a page using points
page2 = dds_file.new_page("plot placement")
plot = page2.add_plot()
plot.add_trace("[10::100]")

under_plot_with_title = page2.add_plot(plot.bbox.bottom_left)
under_plot_with_title.add_trace("[10::100]")
under_plot_with_title.title = "Has a title"
text_height = under_plot_with_title.title_properties.text_size("test")[1]
under_plot_with_title.move((0, text_height))

under_plot = page2.add_plot(under_plot_with_title.bbox.bottom_left)
under_plot.add_trace("[10::100]")

next_to_plot = page2.add_plot(plot.bbox.top_right)
next_to_plot.add_trace("[10::100]")

# plots arranged on a page using rects
buffer = 750
page3 = dds_file.new_page("plot rects")
plot = page3.add_plot(dds.Rect(top_left=(0, 0), width=3000, height=3000))
plot.add_traces(["dB(S11)"])

plot = page3.add_polar_plot(dds.Rect(top_left=(3000 + buffer, 0), width=3000, height=3000))
plot.add_traces(["dB(S21)"])

plot = page3.add_smith_chart(dds.Rect(top_left=(0, 3000 + buffer), width=3000, height=3000))
plot.add_traces(["dB(S12)"])

plot = page3.add_antenna_plot(dds.Rect(top_left=(0, 6000 + 2 * buffer), width=3000, height=3000))
plot.add_traces(["dB(S22)"])

plot = page3.add_list(dds.Rect(top_left=(3000 + buffer, 3000 + buffer), width=3000, height=3000))
plot.add_traces(["dB(S22)"])

dds_file.save("shapes.dds")
```

On this page

[Previous

Examples](index.md)
[Next

Create Pages and Windows](ex_pages_and_windows.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top