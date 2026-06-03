<!-- 来源: pydocs\howto\exporter.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../index.md)
* [How-To](index.md)
* Export Workspace and Design Objects to Python

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
  + [Use Python in the ADS Application](embedded.md)
  + [Set Up a Python Virtual Environment](venv.md)
  + [Set Up Visual Studio Code for Development](vscode.md)
  + [Use Pytest](pytest.md)
  + [Enable Python Support For Your Library](python_integration.md)
  + [Execute Python Scripts in Different Contexts](execution.md)
  + Export Workspace and Design Objects to Python
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

# Export Workspace and Design Objects to Python[](#export-workspace-and-design-objects-to-python "Link to this heading")

The **Python Exporter** is a tool that allows you to export your workspace objects (including, but not limited to: libraries, substrates, cells, and designs) to Python scripts.

The resulting script (or scripts) use the ADS Python API to recreate the exported objects. It is an invaluable tool for learning how to use the ADS Python API
to create designs and other workspace objects programmatically.

The **Python Exporter** consists of two components:

> * The exporter itself, which are Python scripts that iterate over your workspace objects to generate the code necessary to recreate them. Executing the generated code recreates the original workspace object, or set of objects, using the ADS Python API.
> * An ADS Addon that allows you to easily run the exporter from within ADS by providing context menu options for exporting your workspace objects to Python.

The exporter source code is located at `%HPEESOF_DIR%\tools\python\packages\keysight\ads\de\experimental\python_exporter`. The exporter source provides some customizable
options for how the code is generated; these options may be toggled in the source code directly. In addition to being the tool that generates the Python code, it illustrates
how to iterate over the various types of ADS workspace and design objects to obtain all the information necessary for recreation.

It is recommended to review the source code and to also trace through the code in a debugger to understand how it works, as it serves as an extremely useful reference for learning how to use the ADS Python API.
See [Configure the Run/Debug environment](vscode.md#configure-the-rundebug-environment) for information on how to set up VS Code to debug ADS Python scripts.

The Addon can be enabled by going to **Tools -> App Manager** and selecting the **Python Exporter** from the list of Addons in the ADS Application Features section.

![../../_images/PythonExporterAddon.png](../../_images/PythonExporterAddon.png)

The Addon implementation is located at `%HPEESOF_DIR%\addons\python\python_exporter`.

Enabling the **Python Exporter** adds the context menu item, **Export Python**, to certain context menus in ADS that appear when right-clicking. The option appears in the context menu when
right-clicking on various elements in the Folder and Library views of the main window, as well as when right-clicking on a design in a design window. For example, when selecting Export Python from
the context menu of a design window, the exporter will generate the necessary Python code for recreating the design and save it to the clipboard. The generated design will be located
in a new cell, having the same name as the original cell but with a `_script` suffix appended. The rules for cell names can be modified as desired in the exporter source code.

**Note:** The animation below showing **Copy Python Recipe Script** is from an older version of ADS and has been replaced with **Export Python**.

![../../_images/PythonExporter.gif](../../_images/PythonExporter.gif)

In addition to exporting single designs, context menu options have been added when right-clicking on the workspace, library, cell, or view from Folder and Library views that allow
you to export your workspace, library, cells, and views to Python. When using these options, a `de_exported_python` folder will be created in the workspace and will contain all
the scripts necessary for recreation. Executing the `generate_all.py` script will run all the generated scripts for recreating your workspace, library, cells, and/or views.
When using these options, only one script (the top-level script, which varies depending on which export option you selected) will save to the clipboard; the other scripts will
need to be accessed from the `de_exported_python` folder in the workspace.

![../../_images/PythonExporterAddon-2.png](../../_images/PythonExporterAddon-2.png)

On this page

[Previous

Execute Python Scripts in Different Contexts](execution.md)
[Next

Record Actions in ADS as Python Code](recorder.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top