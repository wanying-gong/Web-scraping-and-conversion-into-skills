<!-- 来源: examples\ex_modified_file.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* [Examples](index.md)
* Create and Modify DDS file

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
  + [Create Shapes](ex_shapes.md)
  + [Create Pages and Windows](ex_pages_and_windows.md)
  + Create and Modify DDS file
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

# Create and Modify DDS file[](#create-and-modify-dds-file "Link to this heading")

This example creates a DDS file and then modifies it.

```
# Copyright Keysight Technologies 2023 - 2023
import os
from pathlib import Path

import keysight.ads.dds as dds

def create_example() -> str:
    examples_path = Path(__file__).parent.resolve()
    dds_file = dds.new_dds_file("amplifier.ds", examples_path)
    page = dds_file.pages[0]
    plot1 = page.add_plot()
    plot1.add_traces(["dB(S11)"])

    plot2 = page.add_plot()
    plot2.add_traces(["dB(S21)"])

    plot3 = page.add_plot()
    plot3.add_traces(["dB(S12)"])

    plot4 = page.add_plot()
    plot4.add_traces(["dB(S22)"])

    page.align_grid([plot1, plot2, plot3, plot4], 2, 2)

    inside = plot1.add_inside_limit_line(
        "inside",
        "0.0 GHz",
        0.2,
        "0.5 GHz",
        0.1,
    )
    polygon = plot1.add_polygon_mask("polygon", [(0, 0), (".2 GHz", -0.2), (".4 GHz", 0)])
    plot1.add_rectangle_mask("rect", ".6 GHz", 0, ".7 GHz", -0.1)

    plot1.add_specification("spec1", [inside, polygon])

    bbox = dds_file.pages["page 1"].bbox
    page.add_text("test", bbox.bottom_left)
    page.add_equation("x", "S11")

    dds_file.save("file.dds")
    dds.close_dds_file(dds_file)
    return examples_path / "file.dds"

def modify_example(example: str) -> None:
    dds_file = dds.open_dds_file(example)

    for page in dds_file.pages:
        for obj in page.objects:
            if dds.ObjectType.is_plot(obj):
                if dds.ObjectType.is_rect_plot(obj):
                    for spec in obj.specifications:
                        spec.name = f"changed_{spec.name}"
                        spec.pass_fail_expression_name = f"changed_{spec.pass_fail_expression_name}"
                        for trace in spec:
                            trace.name = f"changed_{trace.name}"
                    for line in obj.limit_lines:
                        line.name = f"changed_{line.name}"
                        line.pass_fail_expression_name = f"changed_{line.pass_fail_expression_name}"
                    for mask in obj.masks:
                        mask.name = f"changed_{mask.name}"

                for trace in obj.traces:
                    trace.expression = f"2 * {trace.expression}"
                    for marker in trace.markers:
                        marker.name = f"changed_{marker.name}"

            elif dds.ObjectType.is_polygon(obj):
                obj.move((10, 10))
            elif dds.ObjectType.is_text(obj):
                obj.string = f"changed_{obj.string}"
                print(f"text - {obj.string}")
            elif dds.ObjectType.is_equation(obj):
                obj.expression = f"{obj.expression}*2"
                print(f"equation - {obj.expression}")

    dds_file.save("modified_file.dds")

example = create_example()
modify_example(example)
os.remove(example)
```

On this page

[Previous

Create Pages and Windows](ex_pages_and_windows.md)
[Next

Create Markers](ex_markers.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top