<!-- 来源: reference\dds\app\callbacks.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.dds.app](index.md)
* Callbacks

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

* [Introduction](../../../intro/index.md)
  + [Licensing](../../../intro/licensing.md)
  + [Using Data Display functionality in Python](../../../intro/usage.md)
  + [Using Visual Studio Code](../../../intro/vscode.md)
* [Concepts](../../../concepts/index.md)
  + [Python Script Execution](../../../concepts/execution.md)
* [Reference](../../index.md)
  + [keysight.ads.dds](../index.md)
    - [DDSFile](../file.md)
    - [Page](../page.md)
    - [Point](../point.md)
    - [Rect](../rect.md)
    - [Grid](../grid.md)
    - [Plots](../plots.md)
    - [Axes](../axes.md)
    - [Legend](../legend.md)
    - [Trace](../trace.md)
    - [Markers](../marker.md)
    - [Line Markers](../linemarker.md)
    - [Limit Lines](../limitlines.md)
    - [Masks](../masks.md)
    - [Specification](../specifications.md)
    - [Equation](../equation.md)
    - [PyEquation](../pyequation.md)
    - [Text](../text.md)
    - [Picture](../picture.md)
    - [Shapes](../shapes.md)
    - [Group](../group.md)
    - [Common Properties](../basic.md)
    - [Print](../print.md)
    - [Object](../objects.md)
    - [Window](../windows.md)
    - [Widget](../pywidget.md)
  + [keysight.ads.dds.experimental](../experimental/index.md)
  + [keysight.ads.dds.app](index.md)
    - [Addon](addon.md)
    - Callbacks
* [How-To](../../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../howto/existingvenv.md)
  + [How to Use Pytest](../../../howto/pytest.md)
* [Examples](../../../examples/index.md)
  + [Create Shapes](../../../examples/ex_shapes.md)
  + [Create Pages and Windows](../../../examples/ex_pages_and_windows.md)
  + [Create and Modify DDS file](../../../examples/ex_modified_file.md)
  + [Create Markers](../../../examples/ex_markers.md)
  + [Create Line Markers](../../../examples/ex_line_markers.md)
  + [Create equations using dataset variables](../../../examples/ex_expressions_and_dataframes.md)
  + [Plot Simulation Output](../../../examples/ex_simple.md)
  + [Plot Amplifier Simulation Data](../../../examples/ex_optimized_amp.md)
  + [Create Pages and Windows](../../../examples/ex_python_equations.md)
  + [Add Specifications to a Plot](../../../examples/ex_specifications.md)
  + [Plot a Time-Domain Output Voltage Waveform](../../../examples/ex_trantest.md)
  + [Plot Parameter Extraction of Simulation Data](../../../examples/ex_crq_extraction.md)
  + [Add custom menu to Data-Display file](../../../examples/ex_custom_menu.md)
  + [Print PDF file](../../../examples/ex_print.md)
* [App Examples](../../../appExamples/index.md)
  + [Add Menu to Data Display Menubar](../../../appExamples/ex_custom_menu.md)
  + [Add Widgets to Data Display Page](../../../appExamples/ex_page_widget.md)
  + [Add Matplotlib Plot to Data Display Window](../../../appExamples/ex_matplotlib_widget.md)
  + [Add an Addon to Data Display](../../../appExamples/ex_addon.md)
* [Addon Examples](../../../addonExamples/index.md)
  + [Addon to Generate Menus](../../../addonExamples/ex_addon/init.md)
  + [3D Plot Addon](../../../addonExamples/ex_addon_3d_plot/index.md)
    - [Menu for 3D Plot Addon](../../../addonExamples/ex_addon_3d_plot/init.md)
    - [Plot for 3D Plot Addon](../../../addonExamples/ex_addon_3d_plot/ex_addon_3d_plot.md)

# Callbacks[](#callbacks "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.dds.app.FileModifiedCallback[](#keysight.ads.dds.app.FileModifiedCallback "Link to this definition")
:   Holds a callback function to be called when a file in a window is modified.

*class* keysight.ads.dds.app.PopupCallback[](#keysight.ads.dds.app.PopupCallback "Link to this definition")

*class* keysight.ads.dds.app.WindowCallback[](#keysight.ads.dds.app.WindowCallback "Link to this definition")
:   Holds a callback function to be called when a file is opened in a window.

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.dds.app.WindowChange[](#keysight.ads.dds.app.WindowChange "Link to this definition")
:   OPENED *= <WindowChange.OPENED: 0>*[](#keysight.ads.dds.app.WindowChange.OPENED "Link to this definition")

    CLOSED *= <WindowChange.CLOSED: 1>*[](#keysight.ads.dds.app.WindowChange.CLOSED "Link to this definition")

    SAVED\_AS *= <WindowChange.SAVED\_AS: 2>*[](#keysight.ads.dds.app.WindowChange.SAVED_AS "Link to this definition")

## Functions[](#functions "Link to this heading")

> keysight.ads.dds.app.register\_file\_modified\_callback(*cb: Callable[[[DDSFile](../file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile")], None]*) → [FileModifiedCallback](#keysight.ads.dds.app.FileModifiedCallback "keysight.ads.dds.app.callbacks.FileModifiedCallback")[](#keysight.ads.dds.app.register_file_modified_callback "Link to this definition")
>
> keysight.ads.dds.app.register\_popup\_callback(*callback: Callable[[QMenu, [DDSFile](../file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile"), [Window](../windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window"), [Point](../point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")], None]*) → [PopupCallback](#keysight.ads.dds.app.PopupCallback "keysight.ads.dds.app.callbacks.PopupCallback")[](#keysight.ads.dds.app.register_popup_callback "Link to this definition")
>
> keysight.ads.dds.app.register\_window\_callback(*cb: Callable[[[DDSFile](../file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile"), [Window](../windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window"), [WindowChange](#keysight.ads.dds.app.WindowChange "keysight.ads.dds.app.callbacks.WindowChange")], None]*) → [WindowCallback](#keysight.ads.dds.app.WindowCallback "keysight.ads.dds.app.callbacks.WindowCallback")[](#keysight.ads.dds.app.register_window_callback "Link to this definition")
>
> keysight.ads.dds.app.unregister\_file\_modified\_callback(*callback: [FileModifiedCallback](#keysight.ads.dds.app.FileModifiedCallback "keysight.ads.dds.app.callbacks.FileModifiedCallback")*) → None[](#keysight.ads.dds.app.unregister_file_modified_callback "Link to this definition")
> :   Unregister a registered file modified callback.
>
>     callback: Should be the object returned by register\_file\_modified\_callback.
>
> keysight.ads.dds.app.unregister\_popup\_callback(*callback: [PopupCallback](#keysight.ads.dds.app.PopupCallback "keysight.ads.dds.app.callbacks.PopupCallback")*) → None[](#keysight.ads.dds.app.unregister_popup_callback "Link to this definition")
>
> keysight.ads.dds.app.unregister\_window\_callback(*callback: [WindowCallback](#keysight.ads.dds.app.WindowCallback "keysight.ads.dds.app.callbacks.WindowCallback")*) → None[](#keysight.ads.dds.app.unregister_window_callback "Link to this definition")
> :   Unregister a registered file opened callback.
>
>     callback: Should be the object returned by register\_window\_callback.

On this page

[Previous

Addon](addon.md)
[Next

How-To](../../../howto/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top