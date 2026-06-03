<!-- 来源: examples\ex_python_equations.html -->

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
  + [Create Pages and Windows](ex_pages_and_windows.md)
  + [Create and Modify DDS file](ex_modified_file.md)
  + [Create Markers](ex_markers.md)
  + [Create Line Markers](ex_line_markers.md)
  + [Create equations using dataset variables](ex_expressions_and_dataframes.md)
  + [Plot Simulation Output](ex_simple.md)
  + [Plot Amplifier Simulation Data](ex_optimized_amp.md)
  + Create Pages and Windows
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

This example creates a DDS file with various examples on how to use python statements on a page.

```
# Copyright Keysight Technologies 2025 - 2025
from pathlib import Path

import keysight.ads.dds as dds

def add_equations_using_dataset_variables(page: dds.Page) -> None:
    py1 = page.add_py_equation("""S11 = datasets['amplifier']['SP1.SP'].to_dataframe()""")
    assert py1.values["S11"].shape[0] == 200

    py2 = page.add_py_equation("""VBE = var('VBE')""")
    assert py2.values["VBE"].to_dataframe().loc[0, "VBE"] == 0.7641268128928568

def add_simple_python_equations(page: dds.Page) -> None:
    x = page.add_py_equation("x = 1")
    y = page.add_py_equation("y = 2")
    z = page.add_py_equation(
        """\
z = x + y
z1 = y - x"""
    )
    assert x.values["x"] == 1
    assert y.values["y"] == 2
    assert z.values["z"] == 3
    assert z.values["z1"] == 1

def add_python_measurement(page: dds.Page) -> None:
    page.add_py_equation(
        """\
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact"""
    )
    py = page.add_py_equation("fact = factorial(5)")
    assert py.values["fact"] == 120

def import_python_measurements(page: dds.Page) -> None:
    page.add_py_equation("from math import sqrt")
    math = page.add_py_equation("sqrt1 = sqrt(4)")
    assert math.values["sqrt1"] == 2

    page.add_py_equation("import math")
    math = page.add_py_equation("sqrt2 = math.sqrt(4)")
    assert math.values["sqrt2"] == 2

    page.add_py_equation(
        """\
import sys
import os
sys.path.append(os.getcwd())
import my_module"""
    )

def plot_python_equations(page: dds.Page) -> None:
    page.add_py_equation(
        """\
list_data = [100, 200, 300, 40, 10, 700]
df = pd.DataFrame(list_data, columns=["Numbers"])"""
    )
    page.add_plot(traces=['py_var("df")'])

def add_python_using_ael_equations(page: dds.Page) -> None:
    page.add_equation("aeleq = 2")
    py = page.add_py_equation("""using_aeleq = ael_var('aeleq') + 3""")
    assert py.values["using_aeleq"] == 5

def add_ael_equation_using_python_equations(page: dds.Page) -> None:
    page.add_py_equation("pyvar = 2")
    eq = page.add_equation('using_pyvar = py_var("pyvar") + 3')
    assert eq.values["using_pyvar"] == 5

def call_ael_measurements_using_python_equations(page: dds.Page) -> None:
    # AEL based measurement functions only support Indexed Variable Blocks.
    page.add_py_equation("a = pd.DataFrame([100, 200, 300, 400], columns=['a'])")
    mean = page.add_py_equation(
        """\
a_vb = dds.get_expr_dataset().create_varblock_from_dataframe("a", a)
a_ivb = dds.IndexedVariableBlock(a_vb, 0)
mean_a = ael.call.mean(a_ivb)"""
    )
    assert mean.values["mean_a"] == 250

examples_path = Path(__file__).parent.resolve()
dds_file = dds.new_dds_file("amplifier.ds", examples_path)
page = dds_file.pages[0]

add_equations_using_dataset_variables(page)
add_simple_python_equations(page)
add_python_measurement(page)
import_python_measurements(page)
plot_python_equations(page)
add_python_using_ael_equations(page)
call_ael_measurements_using_python_equations(page)

dds_file.save("python_equations.dds")
```

On this page

[Previous

Plot Amplifier Simulation Data](ex_optimized_amp.md)
[Next

Add Specifications to a Plot](ex_specifications.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top