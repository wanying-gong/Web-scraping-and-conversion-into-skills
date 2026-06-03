# Appexamples
> **说明：** Appexamples 相关页面。

> **何时使用：** 当你需要查阅 Appexamples 相关内容时

---

## 本文件目录

- **Add an Addon to Data Display** (`appExamples/ex_addon.md`)
- **Add Menu to Data Display Menubar** (`appExamples/ex_custom_menu.md`)
- **Add Matplotlib Plot to Data Display Window** (`appExamples/ex_matplotlib_widget.md`)
- **Add Widgets to Data Display Page** (`appExamples/ex_page_widget.md`)
- **App Examples** (`appExamples/index.md`)

---

<!-- === 来源: appExamples/ex_addon.md === -->

# Add an Addon to Data Display[](#add-an-addon-to-data-display "Link to this heading")

This is an example of how python can be used to add an addon to Data Display.
This must be run in application mode.

```
# Copyright Keysight Technologies 2024 - 2024
from pathlib import Path

import keysight.ads.dds.app as app

examples_path = Path(__file__).parent.resolve()

addon = app.find_addon("MyAddon")
if addon is None:
    addon_path = examples_path / "ex_addon" / "__init__.py"
    addon = app.Addon("MyAddon", addon_path, enabled=True)
    app.add_user_addon(addon)
```


---

<!-- === 来源: appExamples/ex_custom_menu.md === -->

# Add Menu to Data Display Menubar[](#add-menu-to-data-display-menubar "Link to this heading")

This is an example of how to add menus to the Data Display menubar.
This must be run in application mode.

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

<!-- === 来源: appExamples/ex_matplotlib_widget.md === -->

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


---

<!-- === 来源: appExamples/ex_page_widget.md === -->

# Add Widgets to Data Display Page[](#add-widgets-to-data-display-page "Link to this heading")

This is an example of how to add PySide2 Qt widgets to a Data Display page.
This example adds 3 different buttons that behave differently.
This must be run in application mode.

```
import keysight.ads.dds as dds
import keysight.ads.dds.app as app
from PySide6.QtWidgets import QPushButton

def myclick() -> None:
    ddo = dds.get_dds_files()[0]
    for obj in ddo.selected_objects:
        if obj.is_deactivated:
            obj.activate()
        else:
            obj.deactivate()

cur_file = dds.get_dds_files()[0]
page = cur_file.pages[0]
mainwindow = app.get_pyside_main_window(cur_file.windows[0])
view = mainwindow.centralWidget()

locked_button = QPushButton(parent=view, text="Toggle Activate 1")
locked_button.clicked.connect(myclick)
locked_button.move(view.width() - locked_button.width() - 100, 0)
locked_button.show()

panning_button = QPushButton(parent=view, text="Toggle Activate 2")
panning_button.clicked.connect(myclick)
panning_button.show()
page.add_widget(panning_button, dds.Point(3000, 3000))

resizing_button = QPushButton(parent=mainwindow.centralWidget(), text="Toggle Activate 3")
resizing_button.clicked.connect(myclick)
resizing_button.show()
page.add_widget(resizing_button, dds.Rect(top_left=(100, 100), bottom_right=(1100, 600)))
```


---

<!-- === 来源: appExamples/index.md === -->

# App Examples[](#app-examples "Link to this heading")

* [Add Menu to Data Display Menubar](ex_custom_menu.md)
* [Add Widgets to Data Display Page](ex_page_widget.md)
* [Add Matplotlib Plot to Data Display Window](ex_matplotlib_widget.md)
* [Add an Addon to Data Display](ex_addon.md)


---

