<!-- 来源: examples\ex_expressions_and_dataframes.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* [Examples](index.md)
* Create equations using dataset variables

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
  + Create equations using dataset variables
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

# Create equations using dataset variables[](#create-equations-using-dataset-variables "Link to this heading")

This example accesses data from a dataset or from a dds equation to create new data and save the new data into a new dataset. New DDS equations are created with both the default dataset and the new dataset.

```
# Copyright Keysight Technologies 2024 - 2024
from pathlib import Path

import keysight.ads.dds as dds  # isort:skip
import keysight.ads.dataset as dataset  # isort:skip
import pandas as pd

examples_path = Path(__file__).parent.resolve()
dds_file = dds.new_dds_file("amplifier.ds", examples_path)

df = pd.DataFrame()
with dataset.open_dataset_for_reading(examples_path / "data/amplifier.ds") as ds:
    df = ds.varblocks["SP1.SP"].to_dataframe()

page = dds_file.pages[0]
eq = page.add_equation("dbS21 = dB(S21)")
eq_df = eq.variable.to_dataframe()

times2_df = 2 * eq_df
times2_df.columns = ["dbS21x2"]

with dataset.create_dataset(examples_path / "data/python_meas.ds") as ds:
    ds.create_varblock_from_dataframe("SP1.SP.python", times2_df)

page.add_equation("dbS21x2 = python_meas..dbS21x2")
page.add_plot(traces=["dbS21", "dbS21x2"])
dds_file.save("expressions_and_dataframes.dds")
```

On this page

[Previous

Create Line Markers](ex_line_markers.md)
[Next

Plot Simulation Output](ex_simple.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top