# Examples
> **说明：** Examples 相关页面。

> **何时使用：** 当你需要查阅 Examples 相关内容时

---

## 本文件目录

- **Plot Parameter Extraction of Simulation Data** (`examples/ex_crq_extraction.md`)
- **Add custom menu to Data-Display file** (`examples/ex_custom_menu.md`)
- **Create equations using dataset variables** (`examples/ex_expressions_and_dataframes.md`)
- **Create Line Markers** (`examples/ex_line_markers.md`)
- **Create Markers** (`examples/ex_markers.md`)
- **Create and Modify DDS file** (`examples/ex_modified_file.md`)
- **Plot Amplifier Simulation Data** (`examples/ex_optimized_amp.md`)
- **Create Pages and Windows** (`examples/ex_pages_and_windows.md`)
- **Print PDF file** (`examples/ex_print.md`)
- **Create Pages and Windows** (`examples/ex_python_equations.md`)
- **Create Shapes** (`examples/ex_shapes.md`)
- **Plot Simulation Output** (`examples/ex_simple.md`)
- **Add Specifications to a Plot** (`examples/ex_specifications.md`)
- **Plot a Time-Domain Output Voltage Waveform** (`examples/ex_trantest.md`)
- **DDS Qt Widget displayed in a Qt QDialog** (`examples/experimental/ex_dds_qt_widget.md`)
- **DDS rename dataset and update expressions** (`examples/experimental/ex_rename_dataset.md`)
- **Experimental Examples** (`examples/experimental/index.md`)
- **Examples** (`examples/index.md`)

---

<!-- === 来源: examples/ex_crq_extraction.md === -->

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


---

<!-- === 来源: examples/ex_custom_menu.md === -->

# Add custom menu to Data-Display file[](#add-custom-menu-to-data-display-file "Link to this heading")

This example creates a DDS file and adds a custom menu to the main menubar.

```
# Copyright Keysight Technologies 2024 - 2024
from pathlib import Path

import keysight.ads.dds as dds
import keysight.ads.dds.app as app

examples_path = Path(__file__).parent.resolve()

dds_file = dds.new_dds_file("amplifier.ds", examples_path)

mw = app.get_pyside_main_window(dds_file.windows[0])
mb = mw.menuBar()
menu = mb.addMenu("Custom Menu")
action = menu.addAction("Toggle Activate")

def toggle_activate() -> None:
    for obj in dds_file.selected_objects:
        if obj.is_deactivated:
            obj.activate()
        else:
            obj.deactivate()

action.triggered.connect(toggle_activate)
```


---

<!-- === 来源: examples/ex_expressions_and_dataframes.md === -->

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


---

<!-- === 来源: examples/ex_line_markers.md === -->

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


---

<!-- === 来源: examples/ex_markers.md === -->

# Create Markers[](#create-markers "Link to this heading")

This example creates a DDS file that contains plots, traces and markers.

```
# Copyright Keysight Technologies 2023 - 2023
from pathlib import Path

import keysight.ads.dds as dds

examples_path = Path(__file__).parent.resolve()
dds_file = dds.new_dds_file("amplifier.ds", examples_path)
page = dds_file.pages[0]

plot1 = page.add_plot()
traces = plot1.add_traces(["dB(S11)", "dB(S21)"])

marker1 = traces[0].add_marker("m1", "0.5 GHz")
marker2 = traces[0].add_marker("m2", "0.2 GHz")
marker3 = traces[1].add_marker("m3", "0.3 GHz")

marker2.set_delta(marker1)
marker3.set_delta(marker2)

marker3.reset_mode()

symbol_type = dds.TraceMarkerSymbol.CIRCLE
color = dds.Color(5)
size = 30
properties = dds.TraceMarkerSymbolProperties(symbol_type, color, size)
marker3.symbol_properties = properties

plot2 = page.add_plot()
traces = plot2.add_traces(["[1::10]"])

marker4 = traces[0].add_marker("m4", "5")
marker5 = traces[0].add_marker("m5", "1")
marker6 = traces[0].add_marker("m6", "1")

marker5.set_offset(marker4, "-2")
marker6.set_offset(marker4, "2")

marker6.reset_mode()

page.align_grid([plot1, plot2], 1, 2)

dds_file.save("markers.dds")
```


---

<!-- === 来源: examples/ex_modified_file.md === -->

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


---

<!-- === 来源: examples/ex_optimized_amp.md === -->

# Plot Amplifier Simulation Data[](#plot-amplifier-simulation-data "Link to this heading")

This example creates a DDS file that contains a rectangular plot, a smith chart, several traces and markers to illustrate amplifier simulation data.

```
# Copyright Keysight Technologies 2023 - 2023
import pathlib

import keysight.ads.dds as dds

examples_path = pathlib.Path(__file__).parent.resolve()
dds_file = dds.new_dds_file("amplifier.ds", examples_path)
page = dds_file.pages[0]

rect_plot = page.add_plot()
traces = rect_plot.add_traces(["dB(S21)", "dB(S12)"])
traces[0].add_marker("m1", 455000000)

smith_plot = page.add_smith_chart((rect_plot.bbox.right, 0))
smith_plot.add_traces(["S22", "S11"])

s_list = page.add_list((smith_plot.bbox.right, 0))
s_list.add_traces(["S11"])

probe_list = page.add_list((0, rect_plot.bbox.bottom))
probe_list.add_traces(["DC1.DC.VBE", "DC1.DC.Probe1.i"])

dds_file.save("optimized_amp.dds")
```


---

<!-- === 来源: examples/ex_pages_and_windows.md === -->

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


---

<!-- === 来源: examples/ex_print.md === -->

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
dds_file.print_all_pages(all_pages_pdf)

# print specific pages
page_2_pdf = examples_path / "plots.pdf"
dds_file.print_pages_by_name(page_2_pdf, ["page 1", "page 3"])
```


---

<!-- === 来源: examples/ex_python_equations.md === -->

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
    plot = page.add_plot()
    plot.add_py_trace("df")

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


---

<!-- === 来源: examples/ex_shapes.md === -->

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


---

<!-- === 来源: examples/ex_simple.md === -->

# Plot Simulation Output[](#plot-simulation-output "Link to this heading")

This example creates a DDS file that contains several rectangular plots with one trace on each plot.

```
# Copyright Keysight Technologies 2023 - 2023
import pathlib

import keysight.ads.dds as dds

examples_path = pathlib.Path(__file__).parent.resolve()
dds_file = dds.new_dds_file("amplifier.ds", examples_path)
page = dds_file.pages[0]

plot1 = page.add_plot()
plot1.add_traces(["dB(S11)"])

plot2 = page.add_plot()
plot2.add_traces(["dB(S21)"])

plot3 = page.add_plot(traces="dB(S12)")
plot4 = page.add_plot(traces=["dB(S12)"])

page.align_grid([plot1, plot2, plot3, plot4], 2, 2)

dds_file.save("simple.dds")
```


---

<!-- === 来源: examples/ex_specifications.md === -->

# Add Specifications to a Plot[](#add-specifications-to-a-plot "Link to this heading")

This example creates a DDS file with specifications on a plot.

```
# Copyright Keysight Technologies 2023 - 2023
import pathlib

import keysight.ads.dds as dds

examples_path = pathlib.Path(__file__).parent.resolve()
dds_file = dds.new_dds_file("amplifier.ds", examples_path)
page = dds_file.pages[0]

plot = page.add_plot()
plot.add_traces(["[0::20]"])

inside = plot.add_inside_limit_line("inside", 0, 20, 10, 10)
outside = plot.add_outside_limit_line("outside", 15, 0, 20, 5)
greater = plot.add_greater_than_limit_line("greater", 10, 20, 0)
less = plot.add_less_than_limit_line("lesser", 0, 10, 20)

rect = plot.add_rectangle_mask("rect", 10, 15, 15, 10)
line = plot.add_line_mask("line", (0, 20), (20, 0))
polygon = plot.add_polygon_mask("polygon", [(0, 0), (5, 5), (5, 0)])
polyline = plot.add_polyline_mask("polyline", [(0, 5), (5, 0), (10, 5)])

polygon.line_properties = dds.LineProperties(dds.LineType.SHORT_DOT_DASH)
polygon.fill_properties = dds.FillProperties("circles_small", dds.Color(5))

plot.add_specification("spec1", [inside, outside])
plot.add_specification("spec2", [polygon, rect])

dds_file.save("specifications.dds")
```


---

<!-- === 来源: examples/ex_trantest.md === -->

# Plot a Time-Domain Output Voltage Waveform[](#plot-a-time-domain-output-voltage-waveform "Link to this heading")

This example creates a DDS file that contains a plot that charts a time-domain output voltage waveform.

```
# Copyright Keysight Technologies 2023 - 2023
import pathlib

import keysight.ads.dds as dds

def center_rect_above_rect(rect: dds.Rect, above_rect: dds.Rect) -> dds.Rect:
    spacing = 750
    top = above_rect.top - rect.height - spacing
    left = int((above_rect.width - rect.width) / 2) + above_rect.left
    bot = above_rect.top - spacing
    right = left + rect.width
    return dds.Rect(top=top, left=left, bottom=bot, right=right)

examples_path = pathlib.Path(__file__).parent.resolve()
dds_file = dds.new_dds_file("Trantest.ds", examples_path)
page = dds_file.pages[0]

v_plot = page.add_plot((0, 0))
v_plot.title = "Time-Domain Output Voltage Waveform"
v_plot.add_trace("Vout")

spacing = 750
i_plot = page.add_plot((spacing + v_plot.bbox.right, 0))
i_plot.title = "input and Output Current Waveforms"
i_plot.add_traces(["Vout/50", "-InputSource.i"])

plots_bbox = v_plot.bbox.expanded(i_plot.bbox)

text = page.add_text("The amplifier has current gain, but not voltage gain.", (0, 0))
text.bbox = center_rect_above_rect(text.bbox, plots_bbox)

page.add_equation("Pdel_dBm", "10*log(mean(Vout**2/50))+30")
listing = page.add_list()
listing.add_trace("Pdel_dBm")

dds_file.save("Trantest.dds")
```


---

<!-- === 来源: examples/experimental/ex_dds_qt_widget.md === -->

# DDS Qt Widget displayed in a Qt QDialog[](#dds-qt-widget-displayed-in-a-qt-qdialog "Link to this heading")

This example uses a DDS Qt Widget object to view a DDSFile in a Qt Dialog.

```
# Copyright Keysight Technologies 2025 - 2025
from keysight.ads.dds import Rect, new_dds_file
from keysight.ads.dds.experimental import DDSQtWidget
from PySide6.QtWidgets import QDialog, QVBoxLayout

# Creat the Qt Dialog to display the DDSFile
dialog = QDialog()
layout = QVBoxLayout(dialog)

# Create a DDSFile object that contains a shape
dds_file = new_dds_file()
page = dds_file.pages[0]
box = Rect(top=0, left=0, bottom=100, right=200)
page.add_box(box)

# Create the DDSQtWidget object using the DDSFile
ddswidget = DDSQtWidget(parent=dialog, ddsfile=dds_file)
layout.addWidget(ddswidget)

dialog.resize(400, 400)
dialog.show()
dialog.exec()
```

# DDS Qt Widget printed using a Qt QPrinter[](#dds-qt-widget-printed-using-a-qt-qprinter "Link to this heading")

This example uses a DDS Qt Widget object to print DDSFile using a Qt Printer.

```
# Copyright Keysight Technologies 2025 - 2025
from keysight.ads.dds import Rect, new_dds_file
from keysight.ads.dds.experimental import DDSQtWidget
from PySide6.QtGui import QPainter
from PySide6.QtPrintSupport import QPrintDialog, QPrinter

# Create a DDSFile object that contains a shape
dds_file = new_dds_file()
page = dds_file.pages[0]
box = Rect(top=0, left=0, bottom=100, right=200)
page.add_box(box)

# Create the DDSQtWidget object using the DDSFile
ddswidget = DDSQtWidget(ddsfile=dds_file)

# Create a Qt Printer printer and a QPrintDialog
# to choose the printer to print the DDSFile out to.
printer = QPrinter(QPrinter.HighResolution)
print_dialog = QPrintDialog(printer, ddswidget)
if print_dialog.exec() == QPrintDialog.Accepted:
    painter = QPainter(printer)
    ddswidget.render_dds_widget(painter)
    painter.end()
```

# DDS Qt Widget output to a Qt QPixmap[](#dds-qt-widget-output-to-a-qt-qpixmap "Link to this heading")

This example uses a DDS Qt Widget object to create a PNG file from a DDSFile using a QPixmap.

```
# Copyright Keysight Technologies 2025 - 2025
from keysight.ads.dds import Rect, new_dds_file
from keysight.ads.dds.experimental import DDSQtWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPixmap

# Create a DDSFile object that contains a shape
dds_file = new_dds_file()
page = dds_file.pages[0]
box = Rect(top=0, left=0, bottom=100, right=200)
page.add_box(box)

# Create the DDSQtWidget object using the DDSFile
ddswidget = DDSQtWidget(ddsfile=dds_file)

# Create a Qt QPixmap of the DDSFile
pixmap = QPixmap(1024, 1024)
pixmap.fill(Qt.white)
painter = QPainter(pixmap)

ddswidget.render_dds_widget(painter)

painter.end()
pixmap.save("example.png")
```


---

<!-- === 来源: examples/experimental/ex_rename_dataset.md === -->

# DDS rename dataset and update expressions[](#dds-rename-dataset-and-update-expressions "Link to this heading")

This example uses the DDS rename\_dataset\_and\_update\_expressions() function
to update the dataset that is being accessed by a ddsfile.

```
# Copyright Keysight Technologies 2025 - 2025
from pathlib import Path

import pandas

from keysight.ads.dds import new_dds_file  # isort:skip
from keysight.ads.dds.experimental import rename_dataset_and_update_expressions  # isort:skip
from keysight.ads import dataset  # isort:skip

# A simple function that creates a dataset with a
# single list of data.
def create_dataset(dspath: Path, data: list) -> None:
    with dataset.open(dspath, "w") as ds:
        df = pandas.DataFrame(data, columns=["Numbers"])
        ds.create_varblock_from_dataframe("SimpleVar", df)

# Make sure the "data" directory exists
data_path = Path("data").resolve()
if not data_path.exists():
    data_path.mkdir()

# Create an initial dataset with some data.
test_dataset = data_path / "replace_dataset_example.ds"
data = [1, 5, 8, 20, 50]
create_dataset(test_dataset, data)

# Create a DDSFile object using the dataset.
dds_file = new_dds_file(test_dataset)
page = dds_file.pages[0]

# Add an equation using the data from the dataset.
equ = page.add_equation("data", "Numbers")

# Verify the initial data.
assert equ.status == "Valid"
df = equ.variable.to_dataframe()
assert df.values.tolist() == [[1], [5], [8], [20], [50]]

# Create temp dataset to update the dataset with.
temp_dataset = data_path / "__dstmp1212.ds"
data = [10, 50, 200, 400, 900]
create_dataset(temp_dataset, data)

# Now replace the dataset with the temp dataset and update
# the expressions in the ddsfile.
rename_dataset_and_update_expressions(temp_dataset, test_dataset)

# Verify that the data updated as expected.
assert equ.status == "Valid"
df = equ.variable.to_dataframe()
assert df.values.tolist() == [[10], [50], [200], [400], [900]]
```


---

<!-- === 来源: examples/experimental/index.md === -->

# Experimental Examples[](#experimental-examples "Link to this heading")

Contents:

* [DDS Qt Widget displayed in a Qt QDialog](ex_dds_qt_widget.md)
* [DDS Qt Widget printed using a Qt QPrinter](ex_dds_qt_widget.md#dds-qt-widget-printed-using-a-qt-qprinter)
* [DDS Qt Widget output to a Qt QPixmap](ex_dds_qt_widget.md#dds-qt-widget-output-to-a-qt-qpixmap)
* [DDS rename dataset and update expressions](ex_rename_dataset.md)


---

<!-- === 来源: examples/index.md === -->

# Examples[](#examples "Link to this heading")

Contents:

* [Create Shapes](ex_shapes.md)
* [Create Pages and Windows](ex_pages_and_windows.md)
* [Create and Modify DDS file](ex_modified_file.md)
* [Create Markers](ex_markers.md)
* [Create Line Markers](ex_line_markers.md)
* [Create equations using dataset variables](ex_expressions_and_dataframes.md)
* [Plot Simulation Output](ex_simple.md)
* [Plot Amplifier Simulation Data](ex_optimized_amp.md)
* [Create Pages and Windows](ex_python_equations.md)
* [Add Specifications to a Plot](ex_specifications.md)
* [Plot a Time-Domain Output Voltage Waveform](ex_trantest.md)
* [Plot Parameter Extraction of Simulation Data](ex_crq_extraction.md)
* [Add custom menu to Data-Display file](ex_custom_menu.md)
* [Print PDF file](ex_print.md)
* [Experimental Examples](experimental/index.md)
  + [DDS Qt Widget displayed in a Qt QDialog](experimental/ex_dds_qt_widget.md)
  + [DDS Qt Widget printed using a Qt QPrinter](experimental/ex_dds_qt_widget.md#dds-qt-widget-printed-using-a-qt-qprinter)
  + [DDS Qt Widget output to a Qt QPixmap](experimental/ex_dds_qt_widget.md#dds-qt-widget-output-to-a-qt-qpixmap)
  + [DDS rename dataset and update expressions](experimental/ex_rename_dataset.md)


---

