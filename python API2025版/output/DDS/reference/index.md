<!-- 来源: reference\index.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* Reference

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

* [Introduction](../intro/index.md)
  + [Licensing](../intro/licensing.md)
  + [Using Data Display functionality in Python](../intro/usage.md)
  + [Using Visual Studio Code](../intro/vscode.md)
* [Concepts](../concepts/index.md)
  + [Python Script Execution](../concepts/execution.md)
* Reference
  + [keysight.ads.dds](dds/index.md)
    - [DDSFile](dds/file.md)
    - [Page](dds/page.md)
    - [Point](dds/point.md)
    - [Rect](dds/rect.md)
    - [Grid](dds/grid.md)
    - [Plots](dds/plots.md)
    - [Axes](dds/axes.md)
    - [Legend](dds/legend.md)
    - [Trace](dds/trace.md)
    - [Markers](dds/marker.md)
    - [Line Markers](dds/linemarker.md)
    - [Limit Lines](dds/limitlines.md)
    - [Masks](dds/masks.md)
    - [Specification](dds/specifications.md)
    - [Equation](dds/equation.md)
    - [PyEquation](dds/pyequation.md)
    - [Text](dds/text.md)
    - [Picture](dds/picture.md)
    - [Shapes](dds/shapes.md)
    - [Group](dds/group.md)
    - [Common Properties](dds/basic.md)
    - [Print](dds/print.md)
    - [Object](dds/objects.md)
    - [Window](dds/windows.md)
    - [Widget](dds/pywidget.md)
  + [keysight.ads.dds.experimental](dds/experimental/index.md)
  + [keysight.ads.dds.app](dds/app/index.md)
    - [Addon](dds/app/addon.md)
    - [Callbacks](dds/app/callbacks.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
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
* [App Examples](../appExamples/index.md)
  + [Add Menu to Data Display Menubar](../appExamples/ex_custom_menu.md)
  + [Add Widgets to Data Display Page](../appExamples/ex_page_widget.md)
  + [Add Matplotlib Plot to Data Display Window](../appExamples/ex_matplotlib_widget.md)
  + [Add an Addon to Data Display](../appExamples/ex_addon.md)
* [Addon Examples](../addonExamples/index.md)
  + [Addon to Generate Menus](../addonExamples/ex_addon/init.md)
  + [3D Plot Addon](../addonExamples/ex_addon_3d_plot/index.md)
    - [Menu for 3D Plot Addon](../addonExamples/ex_addon_3d_plot/init.md)
    - [Plot for 3D Plot Addon](../addonExamples/ex_addon_3d_plot/ex_addon_3d_plot.md)

# Reference[](#reference "Link to this heading")

* [keysight.ads.dds](dds/index.md)
  + [Classes](dds/index.md#classes)
    - [DDSFile](dds/file.md)
    - [Page](dds/page.md)
    - [Point](dds/point.md)
    - [Rect](dds/rect.md)
    - [Grid](dds/grid.md)
    - [Plots](dds/plots.md)
    - [Axes](dds/axes.md)
    - [Legend](dds/legend.md)
    - [Trace](dds/trace.md)
    - [Markers](dds/marker.md)
    - [Line Markers](dds/linemarker.md)
    - [Limit Lines](dds/limitlines.md)
    - [Masks](dds/masks.md)
    - [Specification](dds/specifications.md)
    - [Equation](dds/equation.md)
    - [PyEquation](dds/pyequation.md)
    - [Text](dds/text.md)
    - [Picture](dds/picture.md)
    - [Shapes](dds/shapes.md)
    - [Group](dds/group.md)
    - [Common Properties](dds/basic.md)
    - [Print](dds/print.md)
    - [Object](dds/objects.md)
    - [Window](dds/windows.md)
    - [Widget](dds/pywidget.md)
  + [Functions](dds/index.md#functions)
    - [`get_dds_path()`](dds/index.md#keysight.ads.dds.get_dds_path)
    - [`init_dds_path()`](dds/index.md#keysight.ads.dds.init_dds_path)
    - [`running_automation()`](dds/index.md#keysight.ads.dds.running_automation)
    - [`version()`](dds/index.md#keysight.ads.dds.version)
    - [`product_version()`](dds/index.md#keysight.ads.dds.product_version)
    - [`close_dds_file()`](dds/index.md#keysight.ads.dds.close_dds_file)
    - [`get_dds_files()`](dds/index.md#keysight.ads.dds.get_dds_files)
    - [`new_dds_file()`](dds/index.md#keysight.ads.dds.new_dds_file)
    - [`open_dds_file()`](dds/index.md#keysight.ads.dds.open_dds_file)
* [keysight.ads.dds.experimental](dds/experimental/index.md)
  + [Classes](dds/experimental/index.md#classes)
  + [Functions](dds/experimental/index.md#functions)
* [keysight.ads.dds.app](dds/app/index.md)
  + [Classes](dds/app/index.md#classes)
    - [Addon](dds/app/addon.md)
    - [Callbacks](dds/app/callbacks.md)
  + [Functions](dds/app/index.md#functions)
    - [`get_pyside2_main_window()`](dds/app/index.md#keysight.ads.dds.app.get_pyside2_main_window)
    - [`is_alt_pressed()`](dds/app/index.md#keysight.ads.dds.app.is_alt_pressed)
    - [`is_control_pressed()`](dds/app/index.md#keysight.ads.dds.app.is_control_pressed)
    - [`is_shift_pressed()`](dds/app/index.md#keysight.ads.dds.app.is_shift_pressed)

**Indices**

* [Index](../genindex.md)
* [Module Index](../py-modindex.md)

On this page

[Previous

Python Script Execution](../concepts/execution.md)
[Next

keysight.ads.dds](dds/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top