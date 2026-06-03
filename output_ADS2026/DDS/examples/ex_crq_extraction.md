<!-- 来源: examples\ex_crq_extraction.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* [Examples](index.md)
* Plot Parameter Extraction of Simulation Data

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
  + [Create and Modify DDS file](ex_modified_file.md)
  + [Create Markers](ex_markers.md)
  + [Create Line Markers](ex_line_markers.md)
  + [Create equations using dataset variables](ex_expressions_and_dataframes.md)
  + [Plot Simulation Output](ex_simple.md)
  + [Plot Amplifier Simulation Data](ex_optimized_amp.md)
  + [Create Pages and Windows](ex_python_equations.md)
  + [Add Specifications to a Plot](ex_specifications.md)
  + [Plot a Time-Domain Output Voltage Waveform](ex_trantest.md)
  + Plot Parameter Extraction of Simulation Data
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

# Plot Parameter Extraction of Simulation Data[](#plot-parameter-extraction-of-simulation-data "Link to this heading")

This example opens a dataset of S-Param simulation and creates a DDS file that contains a smith chart plot with traces representing the capacitance, resistance, and quality factor. It also creates several parameter extraction equations on a second page.

```
# Copyright Keysight Technologies 2023 - 2023
import pathlib

import keysight.ads.dds as dds
import keysight.ads.dataset as ds

examples_path = pathlib.Path(__file__).parent.resolve()
amp_ds = ds.open_dataset_for_reading(examples_path / "data" / "amplifier.ds")
if "SP1.SP" not in amp_ds.varblock_names:
    raise RuntimeError("Dataset does not have S-Param simulation.")

dds_file = dds.new_dds_file("amplifier.ds", examples_path)

page1 = dds_file.pages[0]
page1.name = "plots"
cap = page1.add_plot()
cap.title = "Effective Capacitance"
cap.add_traces(["C11", "C12", "C22"])

res = page1.add_plot()
res.title = "Effective Resistance"
res.add_traces(["R11", "R12", "R22"])

qual = page1.add_plot()
qual.title = "Quality Factor"
qual.add_traces(["Q11", "Q12", "Q22"])

smith = page1.add_smith_chart()
smith.add_legend()
smith.add_trace("S")

page1.align_grid([cap, res, qual, smith], 2, 2)

page2 = dds_file.new_page("equations")
page2.add_equation("omega = 2*pi*SP.freq")
page2.add_equation("YM_2p=stoy(S)")
page2.add_equation("ZM_2p=stoz(S)")
page2.add_equation("C11=-1/imag(1/YM_2p(1,1))/omega")
page2.add_equation("C12=-1/imag(ZM_2p(1,1)-2*ZM_2p(1,2)+ZM_2p(2,2))/omega")
page2.add_equation("C22=-1/imag(1/YM_2p(2,2))/omega")
page2.add_equation("R11=real(1/YM_2p(1,1))")
page2.add_equation("R12=real(ZM_2p(1,1)-2*ZM_2p(1,2)+ZM_2p(2,2))")
page2.add_equation("R22=real(1/YM_2p(2,2))")
page2.add_equation("Q11=1/(omega*C11*R11)")
page2.add_equation("Q12=1/(omega*C12*R12)")
page2.add_equation("Q22=1/(omega*C22*R22)")

bbox = page2.bbox
bbox.expand(page2.objects[11].bbox)
bbox.adjust(left=-10, right=10, top=-10, bottom=10)
page2.add_box(bbox)

text = page2.add_text("Parameter Extraction Equations", (0, 0))
text.text_properties = dds.TextProperties(size=24)
text.move((bbox.left, bbox.top - text.bbox.height))

dds_file.save("CRQ_extraction.dds")
```

On this page

[Previous

Plot a Time-Domain Output Voltage Waveform](ex_trantest.md)
[Next

Add custom menu to Data-Display file](ex_custom_menu.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top