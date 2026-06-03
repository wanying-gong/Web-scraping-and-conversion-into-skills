<!-- 来源: pydocs\howto\pytest.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../index.md)
* [How-To](index.md)
* Use Pytest

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
  + Use Pytest
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

# Use Pytest[](#use-pytest "Link to this heading")

Pytest is a popular testing framework for Python and quite useful when developing Python scripts.
Pytest is not installed in the ADS Python installation, and there are multiple ways to obtain it.

**QUICK REFERENCE (More detailed instructions below):**

* [Using Pytest inside VSCode](#using-pytest-inside-vscode)
* [Using Pytest outside VSCode](#using-pytest-outside-vscode)

**Using Pytest inside VSCode**

Pytest integrates well with VS Code and has built-in support for running and debugging tests.

See [Set Up Visual Studio Code for Development](vscode.md#setup-vscode) for instructions on how to set up VS Code.

Click on the Testing icon in the Activity Bar on the side of the window to bring up the testing tab. Click on the **Configure Python Tests** button to configure the test framework.

In the dropdown that appears at the top of the window, select the root directory you wish to configure tests for.

Select the **pytest** option from the list of available test frameworks.

Pytest has rules for discovering your tests. By default, Pytest will look for files that start with `test_` or end with `_test.py` under the selected directory and subdirectories.
In those files, it will look for functions that start with `test_`. If you want to change the rules for discovering your tests, you can do so by creating a `pytest.ini` file in the root directory of your local code.

[pytest.org](https://docs.pytest.org/en/stable/index.html) has a wealth of information on how to configure and write tests using Pytest.

Select `. Root directory` (or any subdirectory you like). You can change this option later if you want to.

![../../_images/VSCode_configure_pytest.gif](../../_images/VSCode_configure_pytest.gif)

**NOTE:** In order to discover your tests, Pytest will import your test file(s), executing global code in the process. This may result in an error. If this happens, some or all of your tests may not appear in the Tests Results panel.
The Python Output window shows the log of the test discovery process. Errors encountered will be shown in the log.

Below is a screenshot of the Python Output window showing successful Pytest discovery.

![../../_images/VSCode_pytest_discovery.png](../../_images/VSCode_pytest_discovery.png)

Tests can be run individually or all at once. Click one of the Debug (or Run) icons to run your tests.
Tests that have not run yet are shown as a gray circle, while successful tests are shown as a green circle with a check and failed tests are shown as a red circle with an x.

![../../_images/VSCode_run_pytest_1.gif](../../_images/VSCode_run_pytest_1.gif)

Existing results can be cleared by selecting the **Clear All Results** option from the Testing actions dropdown menu.

![../../_images/VSCode_run_pytest_2.gif](../../_images/VSCode_run_pytest_2.gif)

**Using Pytest outside VSCode**

Should you prefer to run Pytest outside of VS Code, you can do so from the command line.
The recommended steps to use Pytest are:

> 1. Create a Python virtual environment. See [Set Up a Python Virtual Environment](venv.md).
> 2. Activate the Python virtual environment.
> 3. Install pytest into the virtual environment.
>
>    > ```
>    > pip install pytest
>    > ```
> 4. Run pytest on your test scripts.
>
>    > ```
>    > cd path/to/tests
>    > pytest
>    > ```

Pytest will, by default, search for and execute any test functions under the current working directory and subdirectories using the following rules:

> 1. Pytest will search for tests in any files prefixed `test_*.py` or postfixed `*_test.py`. This can be
>    configured with the [python\_files](https://docs.pytest.org/en/stable/reference/reference.html#confval-python_files) option.
> 2. Any files considered by the above rules will be searched for any functions prefixed with `test*`, this can be
>    configured with the
>    [python\_functions](https://docs.pytest.org/en/stable/reference/reference.html#confval-python_functions) option.

Additionally you may limit the scope of which tests are run by providing a directory, file, or test name on the command
line as follows:

> 1. For directories: `pytest path/to/test/directory`
> 2. For test files: `pytest path/to/test_file.py`
> 3. For specific tests: `pytest path/to/test_file.py::test_function_name`

For complete documentation reference the [pytest docs](https://docs.pytest.org/en/stable/how-to/index.html).

On this page

[Previous

Set Up Visual Studio Code for Development](vscode.md)
[Next

Enable Python Support For Your Library](python_integration.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top