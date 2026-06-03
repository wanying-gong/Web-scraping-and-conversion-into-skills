<!-- 来源: appExamples\ex_matplotlib_widget.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* [App Examples](index.md)
* Add Matplotlib Plot to Data Display Window

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
  + Add Matplotlib Plot to Data Display Window
  + [Add an Addon to Data Display](ex_addon.md)
* [Addon Examples](../addonExamples/index.md)
  + [Addon to Generate Menus](../addonExamples/ex_addon/init.md)
  + [3D Plot Addon](../addonExamples/ex_addon_3d_plot/index.md)
    - [Menu for 3D Plot Addon](../addonExamples/ex_addon_3d_plot/init.md)
    - [Plot for 3D Plot Addon](../addonExamples/ex_addon_3d_plot/ex_addon_3d_plot.md)

# Add Matplotlib Plot to Data Display Window[](#add-matplotlib-plot-to-data-display-window "Link to this heading")

This is an example of how to place a Matplotlib plot on a Data Display window.
This must be run in application mode.

```
import keysight.ads.dds as dds
import keysight.ads.dds.app as app
from matplotlib.backends.backend_qtagg import FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QDoubleSpinBox,
    QHBoxLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

class PlotWidget(QWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        #  create widgets
        self.view = FigureCanvas(Figure(figsize=(5, 3)))
        self.axes = self.view.figure.subplots()
        self.toolbar = NavigationToolbar2QT(self.view, self)
        self.input = QLineEdit()
        self.std_input = QDoubleSpinBox()
        self.std_input.setValue(1)

        #  Create layout
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input)
        input_layout.addWidget(self.std_input)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.toolbar)
        vlayout.addWidget(self.view)
        vlayout.addLayout(input_layout)
        self.setLayout(vlayout)

        # connect inputs with on_change method
        self.input.editingFinished.connect(self.on_change)
        self.std_input.valueChanged.connect(self.on_change)
        self.on_change()

    def on_change(self) -> None:
        text = self.input.text()
        std = self.std_input.value()

        page = dds.get_dds_files()[0].pages[0]
        eq = [x for x in page.objects if dds.ObjectType.is_equation(x) and x.expression.split("=")[0].strip() == text]
        if len(eq) == 0:
            self.axes.clear()
            self.view.draw()
            return

        df = eq[0].variable.to_dataframe()
        times_df = std * df
        self.axes.clear()
        self.axes.plot(times_df)
        self.view.draw()

file = dds.get_dds_files()[0]
page = file.pages[0]
mw = app.get_pyside_main_window(file.windows[0])
plot = PlotWidget()
plot.setParent(mw.centralWidget())
page.add_widget(plot, dds.Rect(top_left=(0, 0), bottom_right=(3000, 3000)))
plot.show()
```

On this page

[Previous

Add Widgets to Data Display Page](ex_page_widget.md)
[Next

Add an Addon to Data Display](ex_addon.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top