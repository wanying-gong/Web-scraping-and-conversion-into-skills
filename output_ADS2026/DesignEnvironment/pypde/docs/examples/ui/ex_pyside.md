<!-- 来源: pypde\docs\examples\ui\ex_pyside.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Examples](../../../../examples.md)
* [Design Environment](../index.md)
* [UI](index.md)
* PySide

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

* [Introduction](../../../../pydocs/intro/index.md)
* [How-To](../../../../pydocs/howto/index.md)
  + [Use Python in the ADS Application](../../../../pydocs/howto/embedded.md)
  + [Set Up a Python Virtual Environment](../../../../pydocs/howto/venv.md)
  + [Set Up Visual Studio Code for Development](../../../../pydocs/howto/vscode.md)
  + [Use Pytest](../../../../pydocs/howto/pytest.md)
  + [Enable Python Support For Your Library](../../../../pydocs/howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../../../../pydocs/howto/execution.md)
  + [Export Workspace and Design Objects to Python](../../../../pydocs/howto/exporter.md)
  + [Record Actions in ADS as Python Code](../../../../pydocs/howto/recorder.md)
  + [Develop a Python Pcell in ADS](../../../../pydocs/howto/pcell.md)
* [ADS Concepts](../../../../pydocs/concepts/index.md)
  + [Workspace Elements](../../../../pydocs/concepts/workspace_elements.md)
  + [Connectivity Objects](../../../../pydocs/concepts/connectivity.md)
* [Reference](../../../../reference.md)
  + [Deprecated APIs](../../../../pydocs/py/_generated/deprecations.md)
  + [Design Environment](../../reference/index.md)
    - [keysight.ads.de](../../reference/de/index.md)
      * [ADS Application Environment](../../reference/de/ads_environment.md)
      * [ADS Workspace Components](../../reference/de/workspace_components.md)
      * [Design Hierarchy](../../reference/de/design_hierarchy.md)
      * [Smart Package](../../reference/de/package.md)
      * [Geometry](../../reference/de/geometry.md)
      * [Collections](../../reference/de/collections.md)
      * [Printer](../../reference/de/printer.md)
    - [keysight.ads.de.ael](../../reference/de/ael.md)
    - [keysight.ads.de.app](../../reference/de/app/index.md)
      * [Application](../../reference/de/app/application.md)
      * [Actions and Menus](../../reference/de/app/action.md)
      * [Addons](../../reference/de/app/addon.md)
      * [Window and Design Callbacks](../../reference/de/app/callbacks.md)
      * [Windows and Widgets](../../reference/de/app/window.md)
      * [Experimental](../../reference/de/app/experimental.md)
    - [keysight.ads.de.app.dds](../../reference/de/app/dds.md)
      * [exec\_python](../../reference/de/app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../reference/de/db/index.md)
      * [Models, Parameters, and Forms](../../reference/de/db/parameters.md)
      * [Properties](../../reference/de/db/properties.md)
      * [Preferences](../../reference/de/db/preferences.md)
      * [Transaction](../../reference/de/db/transaction.md)
      * [Smart Mount](../../reference/de/db/smart_mount.md)
      * [Geometry](../../reference/de/db/geometry.md)
      * [Teardrops](../../reference/de/db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../reference/de/db_dbu/index.md)
      * [DbBox](../../reference/de/db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../reference/de/db_uu/index.md)
      * [Database Objects](../../reference/de/db_uu/database_objects.md)
      * [Iterators](../../reference/de/db_uu/iterators.md)
      * [Designs](../../reference/de/db_uu/design.md)
      * [Teardrops](../../reference/de/db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../../reference/de/experimental/index.md)
      * [CDF](../../reference/de/experimental/cdf.md)
      * [Design Commands](../../reference/de/experimental/commands.md)
      * [Component Handles](../../reference/de/experimental/handles.md)
      * [Netlist Utilities](../../reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../reference/de/experimental/polygon_utils.md)
      * [xxPro View](../../reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../reference/de/experimental/symbol.md)
      * [Text Maker](../../reference/de/experimental/text_maker.md)
      * [Notebook](../../reference/de/experimental/notebook.md)
      * [Layer/Purpose Pairs](../../reference/de/experimental/lpp.md)
    - [keysight.ads.de.tech](../../reference/de/tech/index.md)
      * [Technology](../../reference/de/tech/tech.md)
      * [Layers](../../reference/de/tech/layers.md)
      * [Line Items](../../reference/de/tech/line_items.md)
      * [Padstacks](../../reference/de/tech/pads.md)
      * [Rules](../../reference/de/tech/rule.md)
  + [Substrate](../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../../../examples.md)
  + [Design Environment](../index.md)
    - [Workspace Creation](../workspace/ex_workspace.md)
    - [Design Creation](../design_creation/index.md)
      * [Create Layout](../design_creation/ex_create_layout.md)
      * [Create Schematic](../design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../design_elements/index.md)
      * [Placing Text](../design_elements/ex_place_text.md)
      * [Moving Objects](../design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../design_elements/ex_plane_editing.md)
    - [Parameters](../parameters/index.md)
      * [Interoperable Component Parameters](../parameters/ex_cdf.md)
      * [Working with VAR](../parameters/ex_working_with_var.md)
      * [Component Parameters](../parameters/ex_parameters.md)
      * [Creating an Item Definition](../parameters/ex_itemdef.md)
      * [Model Definition Properties](../parameters/ex_model.md)
      * [Creating a Text Form](../parameters/ex_text_form.md)
      * [Properties](../parameters/ex_properties.md)
    - [Technology](../technology/index.md)
      * [Padstacks and Vias](../technology/ex_padstack.md)
      * [Nested Technology](../technology/ex_nested.md)
      * [Rules](../technology/ex_rules.md)
    - [Translators](../translators/index.md)
      * [DXF Import and Export](../translators/ex_translate_dxf.md)
      * [Gerber Export](../translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../translators/ex_translate_gds.md)
    - [UI](index.md)
      * [Creating Custom Menus Using an Addon](ex_menu_addon.md)
      * PySide
    - [Utility](../utility/index.md)
      * [Calling Between AEL and Python](../utility/ex_calling_ael_and_python.md)
      * [Smart Package](../utility/ex_smart_pkg.md)
      * [XML RPC](../utility/ex_xml_rpc.md)
  + [Substrate](../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../../../genindex.md)

# PySide[](#pyside "Link to this heading")

This example uses PySide to build a custom GUI that can be called from a menu in ADS. PySide is the GUI widget toolkit that is by default shipping along with ADS.

```
# Copyright Keysight Technologies 2023 - 2023
from typing import Union

from keysight.ads import de
from keysight.ads.de import app
from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QHBoxLayout, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget

def all_lcv() -> list:
    import keysight.ads.de as de

    wrk = de.active_workspace()
    lcvs = []
    for lib_name in wrk.writable_library_names:
        lib = wrk.open_library(lib_name)
        for cell in lib.cells:
            for view in cell.views:
                lcvs.append((view, view.lcv_name))
    return lcvs

class CustomDialog(QDialog):
    def __init__(self, workspace: de.Workspace, parent: Union[QWidget, None] = None):
        super().__init__(parent)

        # Remove question mark, else have to deal with forbidden cursor
        self.setWindowFlag(QtCore.Qt.WindowType.WindowContextHelpButtonHint, False)

        # Window title of the dialog
        self.setWindowTitle("All Cellviews in Workspace " + workspace.path.name)

        # Create the main vertical layout to add widgets into.
        main_vertical_layout = QVBoxLayout()

        # Text editor to display content
        # https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPlainTextEdit.html
        editor = QPlainTextEdit()
        editor.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        editor.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        header_line = "Total number of cellviews - " + str(len(all_lcv())) + "\n"
        editor.insertPlainText(header_line)
        # Just list the view.lcv_name from (view, view.lcv_name)
        editor.appendPlainText("\n".join(lcv[1] for lcv in all_lcv()))
        editor.setReadOnly(True)
        editor.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        # Place text editor into main layout
        main_vertical_layout.addWidget(editor)

        # create horizontal layout for button and spacer
        horizontal_layout = QHBoxLayout()
        ok_button = QPushButton("Ok")
        # this essentially dismisses the dialog when the user clicks Ok
        ok_button.clicked.connect(self.accept)  # type: ignore
        # place button in the layout and move it to the left side
        horizontal_layout.addWidget(ok_button)

        horizontal_layout.addStretch()
        # add horizontal layout to main vertical layout
        main_vertical_layout.addLayout(horizontal_layout)

        # place the layout into the body of the dialog
        self.setLayout(main_vertical_layout)

# Create and display the dialog
dlg = CustomDialog(de.active_workspace(), parent=app.window.main_pyside_widget())
dlg.show()
```

On this page

[Previous

Creating Custom Menus Using an Addon](ex_menu_addon.md)
[Next

Utility](../utility/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top