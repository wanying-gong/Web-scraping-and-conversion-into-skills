<!-- 来源: reference\dds\objects.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Object

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

* [Introduction](../../intro/index.md)
  + [Licensing](../../intro/licensing.md)
  + [Using Data Display functionality in Python](../../intro/usage.md)
  + [Using Visual Studio Code](../../intro/vscode.md)
* [Concepts](../../concepts/index.md)
  + [Python Script Execution](../../concepts/execution.md)
* [Reference](../index.md)
  + [keysight.ads.dds](index.md)
    - [DDSFile](file.md)
    - [Page](page.md)
    - [Point](point.md)
    - [Rect](rect.md)
    - [Grid](grid.md)
    - [Plots](plots.md)
    - [Axes](axes.md)
    - [Legend](legend.md)
    - [Trace](trace.md)
    - [Markers](marker.md)
    - [Line Markers](linemarker.md)
    - [Limit Lines](limitlines.md)
    - [Masks](masks.md)
    - [Specification](specifications.md)
    - [Equation](equation.md)
    - [PyEquation](pyequation.md)
    - [Text](text.md)
    - [Picture](picture.md)
    - [Shapes](shapes.md)
    - [Group](group.md)
    - [Common Properties](basic.md)
    - [Print](print.md)
    - Object
    - [Window](windows.md)
    - [Widget](pywidget.md)
  + [keysight.ads.dds.experimental](experimental/index.md)
    - [DDSQtWidget](experimental/qtwidget.md)
  + [keysight.ads.dds.app](app/index.md)
    - [Addon](app/addon.md)
    - [Callbacks](app/callbacks.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating an ADS based Python virtual environment](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
    - [ADS Python Environment Variables](../../howto/pyenvvars.md)
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
  + [Experimental Examples](../../examples/experimental/index.md)
    - [DDS Qt Widget displayed in a Qt QDialog](../../examples/experimental/ex_dds_qt_widget.md)
    - [DDS Qt Widget printed using a Qt QPrinter](../../examples/experimental/ex_dds_qt_widget.md#dds-qt-widget-printed-using-a-qt-qprinter)
    - [DDS Qt Widget output to a Qt QPixmap](../../examples/experimental/ex_dds_qt_widget.md#dds-qt-widget-output-to-a-qt-qpixmap)
    - [DDS rename dataset and update expressions](../../examples/experimental/ex_rename_dataset.md)
* [App Examples](../../appExamples/index.md)
  + [Add Menu to Data Display Menubar](../../appExamples/ex_custom_menu.md)
  + [Add Widgets to Data Display Page](../../appExamples/ex_page_widget.md)
  + [Add Matplotlib Plot to Data Display Window](../../appExamples/ex_matplotlib_widget.md)
  + [Add an Addon to Data Display](../../appExamples/ex_addon.md)
* [Addon Examples](../../addonExamples/index.md)
  + [Addon to Generate Menus](../../addonExamples/ex_addon/init.md)
  + [3D Plot Addon](../../addonExamples/ex_addon_3d_plot/index.md)
    - [Menu for 3D Plot Addon](../../addonExamples/ex_addon_3d_plot/init.md)
    - [Plot for 3D Plot Addon](../../addonExamples/ex_addon_3d_plot/ex_addon_3d_plot.md)

# Object[](#object "Link to this heading")

*class* keysight.ads.dds.ObjectType[](#keysight.ads.dds.ObjectType "Link to this definition")
:   This class provides functions that can determine what type of object is passed.

    *static* is\_antenna\_plot(*obj: BaseObject*) → TypeGuard[[AntennaPlot](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.AntennaPlot")][](#keysight.ads.dds.ObjectType.is_antenna_plot "Link to this definition")

    *static* is\_box(*obj: BaseObject*) → TypeGuard[[Box](shapes.md#keysight.ads.dds.Box "keysight.ads.dds.Box")][](#keysight.ads.dds.ObjectType.is_box "Link to this definition")

    *static* is\_circle(*obj: BaseObject*) → TypeGuard[[Circle](shapes.md#keysight.ads.dds.Circle "keysight.ads.dds.Circle")][](#keysight.ads.dds.ObjectType.is_circle "Link to this definition")

    *static* is\_equation(*obj: BaseObject*) → TypeGuard[[Equation](equation.md#keysight.ads.dds.Equation "keysight.ads.dds.Equation")][](#keysight.ads.dds.ObjectType.is_equation "Link to this definition")

    *static* is\_exportable(*obj: BaseObject*) → bool[](#keysight.ads.dds.ObjectType.is_exportable "Link to this definition")

    *static* is\_group(*obj: BaseObject*) → TypeGuard[[Group](group.md#keysight.ads.dds.Group "keysight.ads.dds.Group")][](#keysight.ads.dds.ObjectType.is_group "Link to this definition")

    *static* is\_legend(*obj: BaseObject*) → TypeGuard[[Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.Legend")][](#keysight.ads.dds.ObjectType.is_legend "Link to this definition")

    *static* is\_limit\_line(*obj: BaseObject*) → TypeGuard[[LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.LimitLine")][](#keysight.ads.dds.ObjectType.is_limit_line "Link to this definition")

    *static* is\_line(*obj: BaseObject*) → TypeGuard[[Line](shapes.md#keysight.ads.dds.Line "keysight.ads.dds.Line")][](#keysight.ads.dds.ObjectType.is_line "Link to this definition")

    *static* is\_listing(*obj: BaseObject*) → TypeGuard[[Listing](plots.md#keysight.ads.dds.Listing "keysight.ads.dds.Listing")][](#keysight.ads.dds.ObjectType.is_listing "Link to this definition")

    *static* is\_mask(*obj: BaseObject*) → TypeGuard[Mask][](#keysight.ads.dds.ObjectType.is_mask "Link to this definition")

    *static* is\_picture(*obj: BaseObject*) → TypeGuard[[Picture](picture.md#keysight.ads.dds.Picture "keysight.ads.dds.Picture")][](#keysight.ads.dds.ObjectType.is_picture "Link to this definition")

    *static* is\_plot(*obj: BaseObject*) → TypeGuard[Plot][](#keysight.ads.dds.ObjectType.is_plot "Link to this definition")

    *static* is\_polar\_plot(*obj: BaseObject*) → TypeGuard[[PolarPlot](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.PolarPlot")][](#keysight.ads.dds.ObjectType.is_polar_plot "Link to this definition")

    *static* is\_polygon(*obj: BaseObject*) → TypeGuard[[Polygon](shapes.md#keysight.ads.dds.Polygon "keysight.ads.dds.Polygon")][](#keysight.ads.dds.ObjectType.is_polygon "Link to this definition")

    *static* is\_polyline(*obj: BaseObject*) → TypeGuard[[Polyline](shapes.md#keysight.ads.dds.Polyline "keysight.ads.dds.Polyline")][](#keysight.ads.dds.ObjectType.is_polyline "Link to this definition")

    *static* is\_py\_equation(*obj: BaseObject*) → TypeGuard[[PyEquation](pyequation.md#keysight.ads.dds.PyEquation "keysight.ads.dds.PyEquation")][](#keysight.ads.dds.ObjectType.is_py_equation "Link to this definition")

    *static* is\_rect\_plot(*obj: BaseObject*) → TypeGuard[[RectPlot](plots.md#keysight.ads.dds.RectPlot "keysight.ads.dds.RectPlot")][](#keysight.ads.dds.ObjectType.is_rect_plot "Link to this definition")

    *static* is\_slider(*obj: BaseObject*) → TypeGuard[[Slider](plots.md#keysight.ads.dds.Slider "keysight.ads.dds.Slider")][](#keysight.ads.dds.ObjectType.is_slider "Link to this definition")

    *static* is\_smith\_chart(*obj: BaseObject*) → TypeGuard[[SmithChart](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart")][](#keysight.ads.dds.ObjectType.is_smith_chart "Link to this definition")

    *static* is\_specification(*obj: BaseObject*) → TypeGuard[[Specification](specifications.md#keysight.ads.dds.Specification "keysight.ads.dds.Specification")][](#keysight.ads.dds.ObjectType.is_specification "Link to this definition")

    *static* is\_stacked\_plot(*obj: BaseObject*) → TypeGuard[[StackedPlot](plots.md#keysight.ads.dds.StackedPlot "keysight.ads.dds.StackedPlot")][](#keysight.ads.dds.ObjectType.is_stacked_plot "Link to this definition")

    *static* is\_text(*obj: BaseObject*) → TypeGuard[[Text](text.md#keysight.ads.dds.Text "keysight.ads.dds.Text")][](#keysight.ads.dds.ObjectType.is_text "Link to this definition")

    *static* is\_trace(*obj: BaseObject*) → TypeGuard[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.Trace")][](#keysight.ads.dds.ObjectType.is_trace "Link to this definition")

    *static* is\_widget(*obj: BaseObject*) → TypeGuard[[Widget](pywidget.md#keysight.ads.dds.Widget "keysight.ads.dds.Widget")][](#keysight.ads.dds.ObjectType.is_widget "Link to this definition")

On this page

[Previous

Print](print.md)
[Next

Window](windows.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top