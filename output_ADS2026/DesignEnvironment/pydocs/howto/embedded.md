<!-- 来源: pydocs\howto\embedded.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../index.md)
* [How-To](index.md)
* Use Python in the ADS Application

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
* [How-To](index.md)
  + Use Python in the ADS Application
  + [Set Up a Python Virtual Environment](venv.md)
  + [Set Up Visual Studio Code for Development](vscode.md)
  + [Use Pytest](pytest.md)
  + [Enable Python Support For Your Library](python_integration.md)
  + [Execute Python Scripts in Different Contexts](execution.md)
  + [Export Workspace and Design Objects to Python](exporter.md)
  + [Record Actions in ADS as Python Code](recorder.md)
  + [Develop a Python Pcell in ADS](pcell.md)
* [ADS Concepts](../concepts/index.md)
  + [Workspace Elements](../concepts/workspace_elements.md)
  + [Connectivity Objects](../concepts/connectivity.md)
* [Reference](../../reference.md)
  + [Deprecated APIs](../py/_generated/deprecations.md)
  + [Design Environment](../../pypde/docs/reference/index.md)
    - [keysight.ads.de](../../pypde/docs/reference/de/index.md)
      * [ADS Application Environment](../../pypde/docs/reference/de/ads_environment.md)
      * [ADS Workspace Components](../../pypde/docs/reference/de/workspace_components.md)
      * [Design Hierarchy](../../pypde/docs/reference/de/design_hierarchy.md)
      * [Smart Package](../../pypde/docs/reference/de/package.md)
      * [Geometry](../../pypde/docs/reference/de/geometry.md)
      * [Collections](../../pypde/docs/reference/de/collections.md)
      * [Printer](../../pypde/docs/reference/de/printer.md)
    - [keysight.ads.de.ael](../../pypde/docs/reference/de/ael.md)
    - [keysight.ads.de.app](../../pypde/docs/reference/de/app/index.md)
      * [Application](../../pypde/docs/reference/de/app/application.md)
      * [Actions and Menus](../../pypde/docs/reference/de/app/action.md)
      * [Addons](../../pypde/docs/reference/de/app/addon.md)
      * [Window and Design Callbacks](../../pypde/docs/reference/de/app/callbacks.md)
      * [Windows and Widgets](../../pypde/docs/reference/de/app/window.md)
      * [Experimental](../../pypde/docs/reference/de/app/experimental.md)
    - [keysight.ads.de.app.dds](../../pypde/docs/reference/de/app/dds.md)
      * [exec\_python](../../pypde/docs/reference/de/app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../pypde/docs/reference/de/db/index.md)
      * [Models, Parameters, and Forms](../../pypde/docs/reference/de/db/parameters.md)
      * [Properties](../../pypde/docs/reference/de/db/properties.md)
      * [Preferences](../../pypde/docs/reference/de/db/preferences.md)
      * [Transaction](../../pypde/docs/reference/de/db/transaction.md)
      * [Smart Mount](../../pypde/docs/reference/de/db/smart_mount.md)
      * [Geometry](../../pypde/docs/reference/de/db/geometry.md)
      * [Teardrops](../../pypde/docs/reference/de/db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../pypde/docs/reference/de/db_dbu/index.md)
      * [DbBox](../../pypde/docs/reference/de/db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../pypde/docs/reference/de/db_uu/index.md)
      * [Database Objects](../../pypde/docs/reference/de/db_uu/database_objects.md)
      * [Iterators](../../pypde/docs/reference/de/db_uu/iterators.md)
      * [Designs](../../pypde/docs/reference/de/db_uu/design.md)
      * [Teardrops](../../pypde/docs/reference/de/db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../../pypde/docs/reference/de/experimental/index.md)
      * [CDF](../../pypde/docs/reference/de/experimental/cdf.md)
      * [Design Commands](../../pypde/docs/reference/de/experimental/commands.md)
      * [Component Handles](../../pypde/docs/reference/de/experimental/handles.md)
      * [Netlist Utilities](../../pypde/docs/reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../pypde/docs/reference/de/experimental/polygon_utils.md)
      * [xxPro View](../../pypde/docs/reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../pypde/docs/reference/de/experimental/symbol.md)
      * [Text Maker](../../pypde/docs/reference/de/experimental/text_maker.md)
      * [Notebook](../../pypde/docs/reference/de/experimental/notebook.md)
      * [Layer/Purpose Pairs](../../pypde/docs/reference/de/experimental/lpp.md)
    - [keysight.ads.de.tech](../../pypde/docs/reference/de/tech/index.md)
      * [Technology](../../pypde/docs/reference/de/tech/tech.md)
      * [Layers](../../pypde/docs/reference/de/tech/layers.md)
      * [Line Items](../../pypde/docs/reference/de/tech/line_items.md)
      * [Padstacks](../../pypde/docs/reference/de/tech/pads.md)
      * [Rules](../../pypde/docs/reference/de/tech/rule.md)
  + [Substrate](../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../examples.md)
  + [Design Environment](../../pypde/docs/examples/index.md)
    - [Workspace Creation](../../pypde/docs/examples/workspace/ex_workspace.md)
    - [Design Creation](../../pypde/docs/examples/design_creation/index.md)
      * [Create Layout](../../pypde/docs/examples/design_creation/ex_create_layout.md)
      * [Create Schematic](../../pypde/docs/examples/design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../../pypde/docs/examples/design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../../pypde/docs/examples/design_elements/index.md)
      * [Placing Text](../../pypde/docs/examples/design_elements/ex_place_text.md)
      * [Moving Objects](../../pypde/docs/examples/design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../../pypde/docs/examples/design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../../pypde/docs/examples/design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../../pypde/docs/examples/design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../../pypde/docs/examples/design_elements/ex_plane_editing.md)
    - [Parameters](../../pypde/docs/examples/parameters/index.md)
      * [Interoperable Component Parameters](../../pypde/docs/examples/parameters/ex_cdf.md)
      * [Working with VAR](../../pypde/docs/examples/parameters/ex_working_with_var.md)
      * [Component Parameters](../../pypde/docs/examples/parameters/ex_parameters.md)
      * [Creating an Item Definition](../../pypde/docs/examples/parameters/ex_itemdef.md)
      * [Model Definition Properties](../../pypde/docs/examples/parameters/ex_model.md)
      * [Creating a Text Form](../../pypde/docs/examples/parameters/ex_text_form.md)
      * [Properties](../../pypde/docs/examples/parameters/ex_properties.md)
    - [Technology](../../pypde/docs/examples/technology/index.md)
      * [Padstacks and Vias](../../pypde/docs/examples/technology/ex_padstack.md)
      * [Nested Technology](../../pypde/docs/examples/technology/ex_nested.md)
      * [Rules](../../pypde/docs/examples/technology/ex_rules.md)
    - [Translators](../../pypde/docs/examples/translators/index.md)
      * [DXF Import and Export](../../pypde/docs/examples/translators/ex_translate_dxf.md)
      * [Gerber Export](../../pypde/docs/examples/translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../../pypde/docs/examples/translators/ex_translate_gds.md)
    - [UI](../../pypde/docs/examples/ui/index.md)
      * [Creating Custom Menus Using an Addon](../../pypde/docs/examples/ui/ex_menu_addon.md)
      * [PySide](../../pypde/docs/examples/ui/ex_pyside.md)
    - [Utility](../../pypde/docs/examples/utility/index.md)
      * [Calling Between AEL and Python](../../pypde/docs/examples/utility/ex_calling_ael_and_python.md)
      * [Smart Package](../../pypde/docs/examples/utility/ex_smart_pkg.md)
      * [XML RPC](../../pypde/docs/examples/utility/ex_xml_rpc.md)
  + [Substrate](../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../genindex.md)

# Use Python in the ADS Application[](#use-python-in-the-ads-application "Link to this heading")

The ADS Design Environment includes an embedded Python interpreter and can be accessed from the **Tools > Python Console…** top-level menu
or by using the **Ctrl-Shift-P** keyboard shortcut. If the interpreter window is already displayed, the shortcut will bring the window to the foreground.

## Jupyter Console[](#jupyter-console "Link to this heading")

[![../../_images/jupyter_console.png](../../_images/jupyter_console.png)](../../_images/jupyter_console.png)

The Jupyter console has both tooltips and tab-completion.

Note

Completion assistance does not pop up automatically. Invoke it by pressing the TAB key.

The Jupyter console supports IPython’s magic commands for IPython. For example:

> * `%clear`: clear the current window
> * `%alias`: create shortcut commands
> * `%matplotlib inline`: render matplotlib plots in the console window
> * `%matplotlib auto`: reset the handling of matplotlib plots

Full reference: [IPython Magic Commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html).

## Customizing the ADS UI[](#customizing-the-ads-ui "Link to this heading")

Customization of ADS, like adding menus, can be done using the [`keysight.ads.de.app`](../../pypde/docs/reference/de/app/index.md#module-keysight.ads.de.app "keysight.ads.de.app") module.

Creating user interfaces, like dialog windows, can be done using PySide.

```
# Copyright Keysight Technologies 2023 - 2023
from typing import Union

from PySide6.QtWidgets import QDialog, QPlainTextEdit, QVBoxLayout, QWidget

class Form(QDialog):
    def __init__(self, parent: Union[QWidget, None] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("My Customization Example")
        layout = QVBoxLayout()
        editor = QPlainTextEdit()
        editor.setPlainText("Text")
        layout.addWidget(editor)
        self.setLayout(layout)

form = Form()
form.show()
```

Note

PySide6 is installed and available when using Python inside ADS.

### Add-ons[](#add-ons "Link to this heading")

Python-implemented addons are supported by ADS using a similar mechanism as AEL-implemented addons and
can be implemented as a package where \_\_init\_\_.py contains three optional, well-known, functions.

\_\_init\_\_.py[](#id1 "Link to this code")

```
# Optionally defined setup function for the addon (Do not invoke UI elements here).
def setup_addon(addon: "Addon") -> None: ...
# Optionally defined shutdown function for the addon (Do not invoke UI elements here).
def shutdown_addon(addon: "Addon") -> None: ...
# Optionally defined function for generating custom menus
def generate_menu(addon: "Addon", win_def: "WindowDefinition") -> None: ...
```

See [Creating Custom Menus Using an Addon](../../pypde/docs/examples/ui/ex_menu_addon.md) for a working example of a Python addon.

On this page

[Previous

How-To](index.md)
[Next

Set Up a Python Virtual Environment](venv.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top