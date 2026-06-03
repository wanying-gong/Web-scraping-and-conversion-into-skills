<!-- 来源: pydocs\intro\embedded.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../index.md)
* [Introduction](index.md)
* Using Python in ADS Design Environment

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

* [Introduction](index.md)
  + [Licensing](licensing.md)
  + Using Python in ADS Design Environment
  + [Using ADS Design Environment Functionality in Python](extension.md)
* [Concepts](../concepts/index.md)
  + [Terminology](../concepts/terminology.md)
    - [Workspace Elements](../concepts/workspace_elements.md)
    - [Connectivity Objects](../concepts/connectivity.md)
  + [OpenAccess Integration](../concepts/openaccess_integration.md)
  + [Python Script Execution](../concepts/execution.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
  + [How to Use Pytest](../howto/pytest.md)

* [Design](../../pypde/docs/index.md)
  + [Reference](../../pypde/docs/reference/index.md)
    - [keysight.ads.de](../../pypde/docs/reference/de/index.md)
      * [Workspace](../../pypde/docs/reference/de/workspace.md)
      * [Library](../../pypde/docs/reference/de/library.md)
      * [Cell](../../pypde/docs/reference/de/cell.md)
      * [View](../../pypde/docs/reference/de/view.md)
      * [CellviewRef](../../pypde/docs/reference/de/cellviewref.md)
      * [DesignHierarchy](../../pypde/docs/reference/de/design_hierarchy.md)
      * [DMData](../../pypde/docs/reference/de/dmdata.md)
      * [ItemInfo](../../pypde/docs/reference/de/item_info.md)
      * [Points](../../pypde/docs/reference/de/points.md)
      * [Collections](../../pypde/docs/reference/de/collections.md)
    - [keysight.ads.de.ael](../../pypde/docs/reference/de/ael.md)
    - [keysight.ads.de.app](../../pypde/docs/reference/de/app/index.md)
      * [Actions and Menus](../../pypde/docs/reference/de/app/action.md)
      * [Addons](../../pypde/docs/reference/de/app/addon.md)
      * [Callbacks](../../pypde/docs/reference/de/app/callbacks.md)
      * [Windows and Widgets](../../pypde/docs/reference/de/app/window.md)
    - [keysight.ads.de.db](../../pypde/docs/reference/de/db/index.md)
      * [Callbacks](../../pypde/docs/reference/de/db/callbacks.md)
      * [Enumerated Types](../../pypde/docs/reference/de/db/enums.md)
      * [Parameter Forms](../../pypde/docs/reference/de/db/forms.md)
      * [GenPolyline](../../pypde/docs/reference/de/db/genpolyline.md)
      * [Model Definition](../../pypde/docs/reference/de/db/model_def.md)
      * [Parameters](../../pypde/docs/reference/de/db/parameters.md)
      * [Properties](../../pypde/docs/reference/de/db/properties.md)
      * [Transaction](../../pypde/docs/reference/de/db/transaction.md)
    - [keysight.ads.de.db\_dbu](../../pypde/docs/reference/de/db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../../pypde/docs/reference/de/db_uu/index.md)
      * [Design Elements](../../pypde/docs/reference/de/db_uu/db_uu.md)
      * [LayerId](../../pypde/docs/reference/de/db_uu/layer_id.md)
      * [LineTypeInfo](../../pypde/docs/reference/de/db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../../pypde/docs/reference/de/experimental/index.md)
      * [CDF](../../pypde/docs/reference/de/experimental/cdf/index.md)
      * [Commands](../../pypde/docs/reference/de/experimental/commands.md)
      * [Handles](../../pypde/docs/reference/de/experimental/handles.md)
      * [Netlist Utilities](../../pypde/docs/reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../pypde/docs/reference/de/experimental/polygon_utils.md)
      * [Preferences](../../pypde/docs/reference/de/experimental/preferences.md)
      * [xxPro View](../../pypde/docs/reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../pypde/docs/reference/de/experimental/symbol.md)
      * [Text Maker](../../pypde/docs/reference/de/experimental/text_maker.md)
    - [keysight.ads.de.tech](../../pypde/docs/reference/de/tech/index.md)
      * [Tech](../../pypde/docs/reference/de/tech/tech.md)
      * [Padstacks](../../pypde/docs/reference/de/tech/pads/pads.md)
      * [Via Rules](../../pypde/docs/reference/de/tech/rule/rule.md)
      * [Nested Technology](../../pypde/docs/reference/de/tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../../pypde/docs/reference/de/app/dds.md)
  + [Examples](../../pypde/docs/examples/index.md)
    - [Calling Between AEL and Python](../../pypde/docs/examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../pypde/docs/examples/ex_create_layout.md)
    - [Create Schematic](../../pypde/docs/examples/ex_create_schematic.md)
    - [Create Workspace](../../pypde/docs/examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../pypde/docs/examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../pypde/docs/examples/ex_cdf.md)
    - [Component Parameters](../../pypde/docs/examples/ex_parameters.md)
    - [Creating an Item Definition](../../pypde/docs/examples/ex_itemdef.md)
    - [Model Definition Properties](../../pypde/docs/examples/ex_model.md)
    - [Adding Instances to a Design](../../pypde/docs/examples/ex_lpf.md)
    - [Properties](../../pypde/docs/examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../pypde/docs/examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../pypde/docs/examples/ex_padstack.md)
    - [Nested Technology](../../pypde/docs/examples/ex_nested.md)
    - [Rules](../../pypde/docs/examples/ex_rules.md)
    - [Placing Text](../../pypde/docs/examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../pypde/docs/examples/ex_polygon.md)
    - [PySide2](../../pypde/docs/examples/ex_pyside.md)
    - [Traversing Hierarchy](../../pypde/docs/examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../pypde/docs/examples/ex_working_with_var.md)
    - [XML RPC](../../pypde/docs/examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../pypde/docs/examples/ex_translate_gds.md)
* [Technology](../../pysubst/docs/index.md)
  + [Reference](../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Using Python in ADS Design Environment[](#using-python-in-ads-design-environment "Link to this heading")

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

Creating user interfaces, like dialog windows, can be done using PySide2.

```
# Copyright Keysight Technologies 2023 - 2023
from typing import Union

from PySide2.QtWidgets import QDialog, QPlainTextEdit, QVBoxLayout, QWidget

class Form(QDialog):
    def __init__(self, parent: Union[QWidget, None] = None):
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

PySide2 is installed and available when using Python inside ADS.

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

See [Creating Custom Menus Using an Addon](../../pypde/docs/examples/ex_menu_addon.md) for a working example of a Python addon.

On this page

[Previous

Licensing](licensing.md)
[Next

Using ADS Design Environment Functionality in Python](extension.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top