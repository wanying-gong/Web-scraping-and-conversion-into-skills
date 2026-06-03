<!-- 来源: addonExamples\ex_addon_3d_plot\ex_addon_3d_plot.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Addon Examples](../index.md)
* [3D Plot Addon](index.md)
* Plot for 3D Plot Addon

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

* [Introduction](../../intro/index.md)
  + [Licensing](../../intro/licensing.md)
  + [Using Data Display functionality in Python](../../intro/usage.md)
  + [Using Visual Studio Code](../../intro/vscode.md)
* [Concepts](../../concepts/index.md)
  + [Python Script Execution](../../concepts/execution.md)
* [Reference](../../reference/index.md)
  + [keysight.ads.dds](../../reference/dds/index.md)
    - [DDSFile](../../reference/dds/file.md)
    - [Page](../../reference/dds/page.md)
    - [Point](../../reference/dds/point.md)
    - [Rect](../../reference/dds/rect.md)
    - [Grid](../../reference/dds/grid.md)
    - [Plots](../../reference/dds/plots.md)
    - [Axes](../../reference/dds/axes.md)
    - [Legend](../../reference/dds/legend.md)
    - [Trace](../../reference/dds/trace.md)
    - [Markers](../../reference/dds/marker.md)
    - [Line Markers](../../reference/dds/linemarker.md)
    - [Limit Lines](../../reference/dds/limitlines.md)
    - [Masks](../../reference/dds/masks.md)
    - [Specification](../../reference/dds/specifications.md)
    - [Equation](../../reference/dds/equation.md)
    - [PyEquation](../../reference/dds/pyequation.md)
    - [Text](../../reference/dds/text.md)
    - [Picture](../../reference/dds/picture.md)
    - [Shapes](../../reference/dds/shapes.md)
    - [Group](../../reference/dds/group.md)
    - [Common Properties](../../reference/dds/basic.md)
    - [Print](../../reference/dds/print.md)
    - [Object](../../reference/dds/objects.md)
    - [Window](../../reference/dds/windows.md)
    - [Widget](../../reference/dds/pywidget.md)
  + [keysight.ads.dds.experimental](../../reference/dds/experimental/index.md)
  + [keysight.ads.dds.app](../../reference/dds/app/index.md)
    - [Addon](../../reference/dds/app/addon.md)
    - [Callbacks](../../reference/dds/app/callbacks.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
  + [How to Use Pytest](../../howto/pytest.md)
* [Examples](../../examples/index.md)
  + [Create Shapes](../../examples/ex_shapes.md)
  + [Create Pages and Windows](../../examples/ex_pages_and_windows.md)
  + [Create and Modify DDS file](../../examples/ex_modified_file.md)
  + [Create Markers](../../examples/ex_markers.md)
  + [Create Line Markers](../../examples/ex_line_markers.md)
  + [Create equations using dataset variables](../../examples/ex_expressions_and_dataframes.md)
  + [Plot Simulation Output](../../examples/ex_simple.md)
  + [Plot Amplifier Simulation Data](../../examples/ex_optimized_amp.md)
  + [Create Pages and Windows](../../examples/ex_python_equations.md)
  + [Add Specifications to a Plot](../../examples/ex_specifications.md)
  + [Plot a Time-Domain Output Voltage Waveform](../../examples/ex_trantest.md)
  + [Plot Parameter Extraction of Simulation Data](../../examples/ex_crq_extraction.md)
  + [Add custom menu to Data-Display file](../../examples/ex_custom_menu.md)
  + [Print PDF file](../../examples/ex_print.md)
* [App Examples](../../appExamples/index.md)
  + [Add Menu to Data Display Menubar](../../appExamples/ex_custom_menu.md)
  + [Add Widgets to Data Display Page](../../appExamples/ex_page_widget.md)
  + [Add Matplotlib Plot to Data Display Window](../../appExamples/ex_matplotlib_widget.md)
  + [Add an Addon to Data Display](../../appExamples/ex_addon.md)
* [Addon Examples](../index.md)
  + [Addon to Generate Menus](../ex_addon/init.md)
  + [3D Plot Addon](index.md)
    - [Menu for 3D Plot Addon](init.md)
    - Plot for 3D Plot Addon

# Plot for 3D Plot Addon[](#plot-for-3d-plot-addon "Link to this heading")

This contains the code that is called during a callback that creates a 3d plot.

```
from typing import Union

import keysight.ads.dds as dds
import keysight.ads.dds.app as app
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from PySide2.QtWidgets import (
    QVBoxLayout,
    QWidget,
)

class PlotWidget(QWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        #  create widgets
        self.view = FigureCanvas(Figure(figsize=(5, 3)))
        ax = self.view.figure.add_subplot(projection="3d")

        # Plot a sin curve using the x and y axes.
        x = np.linspace(0, 1, 100)
        y = np.sin(x * 2 * np.pi) / 2 + 0.5
        ax.plot(x, y, zs=0, zdir="z")

        # Plot scatterplot data (20 2D points per colour) on the x and z axes.
        colors = ("r", "g", "b", "k")

        # Fixing random state for reproducibility
        np.random.seed(19680801)

        x = np.random.sample(20 * len(colors))
        y = np.random.sample(20 * len(colors))
        c_list = []
        for c in colors:
            c_list.extend([c] * 20)
        # By using zdir='y', the y value of these points is fixed to the zs value 0
        # and the (x, y) points are plotted on the x and z axes.
        ax.scatter(x, y, zs=0, zdir="y", c=c_list)

        # Make legend, set axes limits and labels
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_zlim(0, 1)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        # Customize the view angle so it's easier to see that the scatter points lie
        # on the plane y=0
        ax.view_init(elev=20.0, azim=-35)

        #  Create layout
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.view)
        self.setLayout(vlayout)

def add_3d_plot(
    file: dds.DDSFile, win: dds.Window, page_name: str, location: Union[dds.Point | dds.Rect]
) -> dds.Widget:
    page = file.pages[page_name]
    mw = app.get_pyside2_main_window(win)
    plot = PlotWidget()
    plot.setParent(mw.centralWidget())
    plot.show()

    rect = location if isinstance(location, dds.Rect) else dds.Rect(top_left=location, width=3000, height=3000)
    widget = page.add_widget(plot, rect)
    return widget
```

On this page

[Previous

Menu for 3D Plot Addon](init.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top