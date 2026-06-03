# Addonexamples
> **说明：** Addonexamples 相关页面。

> **何时使用：** 当你需要查阅 Addonexamples 相关内容时

---

## 本文件目录

- **Addon to Generate Menus** (`addonExamples/ex_addon/init.md`)
- **Plot for 3D Plot Addon** (`addonExamples/ex_addon_3d_plot/ex_addon_3d_plot.md`)
- **3D Plot Addon** (`addonExamples/ex_addon_3d_plot/index.md`)
- **Menu for 3D Plot Addon** (`addonExamples/ex_addon_3d_plot/init.md`)
- **Addon Examples** (`addonExamples/index.md`)

---

<!-- === 来源: addonExamples/ex_addon/init.md === -->

# Addon to Generate Menus[](#addon-to-generate-menus "Link to this heading")

This is an example of a python file that can be used to initialize an Addon in the
Data Display App Manager.

```
# Copyright Keysight Technologies 2024 - 2024
"""Addon example that will generate menus based on window type."""

import keysight.ads.ael as ael
import keysight.ads.dds as dds
import keysight.ads.dds.app as app
from PySide2.QtWidgets import QMenu

def insert_activate(file: dds.DDSFile, win: dds.Window) -> None:
    mw = app.get_pyside2_main_window(win)
    mb = mw.menuBar()
    menu = mb.addMenu("Python Addon")
    action = menu.addAction("Toggle Activate")

    def toggle_activate() -> None:
        for obj in file.selected_objects:
            if obj.is_deactivated:
                obj.activate()
            else:
                obj.deactivate()

    action.triggered.connect(toggle_activate)

def window_callback(file: dds.DDSFile, win: dds.Window, cb_type: app.WindowChange) -> None:
    if cb_type is app.WindowChange.OPENED:
        insert_activate(file, win)

def file_modified_callback(file: dds.DDSFile) -> None:
    ael.call.info_message("File Modified!")

def outline_equation(eq: dds.Equation) -> None:
    eq.is_outlined = True

def copy_text(text: dds.Text, page: dds.Page) -> None:
    page.add_text(text.string, text.bbox.bottom_left())

def popup_callback(menu: QMenu, file: dds.DDSFile, window: dds.Window, pos: dds.Point) -> None:
    action = menu.addAction("Insert a text box")
    action.triggered.connect(lambda: window.current_page.add_text("Hello, World!", pos))

    if len(file.selected_objects) == 0:
        return
    obj = file.selected_objects[0]
    if dds.ObjectType.is_equation(obj):
        action = menu.addAction("Outline Equation Action")
        action.triggered.connect(lambda: outline_equation(obj))
    elif dds.ObjectType.is_text(obj):
        action = menu.addAction("Copy Text Action")
        action.triggered.connect(lambda: copy_text(obj, window.current_page))

def setup_addon(addon: app.Addon) -> None:
    # Implementation of this method is optional but if you do, DO NOT invoke UI from this function!
    app.register_window_callback(window_callback)
    app.register_file_modified_callback(file_modified_callback)
    app.register_popup_callback(popup_callback)

def shutdown_addon(addon: app.Addon) -> None:
    # Implementation of this method is optional but if you do, DO NOT invoke UI from this function!
    ...

def identify() -> None:
    print("Addon Example")
```


---

<!-- === 来源: addonExamples/ex_addon_3d_plot/ex_addon_3d_plot.md === -->

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


---

<!-- === 来源: addonExamples/ex_addon_3d_plot/index.md === -->

# 3D Plot Addon[](#d-plot-addon "Link to this heading")

* [Menu for 3D Plot Addon](init.md)
* [Plot for 3D Plot Addon](ex_addon_3d_plot.md)


---

<!-- === 来源: addonExamples/ex_addon_3d_plot/init.md === -->

# Menu for 3D Plot Addon[](#menu-for-3d-plot-addon "Link to this heading")

This adds the menu for a 3D Plot. The callback is in a seperate python file.

```
# Copyright Keysight Technologies 2024 - 2024
"""Addon example that will generate menus based on window type."""

import keysight.ads.dds as dds
import keysight.ads.dds.app as app
from PySide2.QtWidgets import QMenu

from .ex_matplotlib_3d import add_3d_plot

def popup_callback(menu: QMenu, file: dds.DDSFile, window: dds.Window, pos: dds.Point) -> None:
    page_name = window.current_page.name

    if len(file.selected_objects) == 0:
        action = menu.addAction("Insert 3D Plot")
        action.triggered.connect(lambda: add_3d_plot(file, window, page_name, pos))

def setup_addon(addon: app.Addon) -> None:
    # Implementation of this method is optional but if you do, DO NOT invoke UI from this function!
    app.register_popup_callback(popup_callback)

def shutdown_addon(addon: app.Addon) -> None:
    # Implementation of this method is optional but if you do, DO NOT invoke UI from this function!
    ...

def identify() -> None:
    print("3D Addon Example")
```


---

<!-- === 来源: addonExamples/index.md === -->

# Addon Examples[](#addon-examples "Link to this heading")

* [Addon to Generate Menus](ex_addon/init.md)
* [3D Plot Addon](ex_addon_3d_plot/index.md)
  + [Menu for 3D Plot Addon](ex_addon_3d_plot/init.md)
  + [Plot for 3D Plot Addon](ex_addon_3d_plot/ex_addon_3d_plot.md)


---

