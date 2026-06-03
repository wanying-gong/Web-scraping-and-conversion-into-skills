<!-- 来源: reference\dds\axes.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Axes

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
    - Axes
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
    - [Object](objects.md)
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

# Axes[](#axes "Link to this heading")

*class* keysight.ads.dds.AntennaIndepAxis[](#keysight.ads.dds.AntennaIndepAxis "Link to this definition")
:   The independent axis of [`AntennaPlot`](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.AntennaPlot").

    This class cannot be instantiated directly. It is automatically instantiated when an [`AntennaPlot`](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.AntennaPlot") is created.
    It is accessed by the property [`AntennaPlot.indep_axis`](plots.md#keysight.ads.dds.AntennaPlot.indep_axis "keysight.ads.dds.AntennaPlot.indep_axis").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.AntennaIndepAxis.grid_properties "Link to this definition")

    *property* is\_all\_indep\_data\_displayed*: bool*[](#keysight.ads.dds.AntennaIndepAxis.is_all_indep_data_displayed "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.AntennaIndepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.AntennaIndepAxis.label "Link to this definition")

    *property* label\_properties*: [AxisTextProperties](#keysight.ads.dds.AxisTextProperties "keysight.ads.dds.core.ddbase.AxisTextProperties")*[](#keysight.ads.dds.AntennaIndepAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.AntennaIndepAxis.name "Link to this definition")

    *property* orientation*: [AxisOrientation](#keysight.ads.dds.AxisOrientation "keysight.ads.dds.core.ddplot.AxisOrientation")*[](#keysight.ads.dds.AntennaIndepAxis.orientation "Link to this definition")

    *property* show\_label*: bool*[](#keysight.ads.dds.AntennaIndepAxis.show_label "Link to this definition")

    *property* show\_tick\_values*: bool*[](#keysight.ads.dds.AntennaIndepAxis.show_tick_values "Link to this definition")

    *property* show\_ticks*: bool*[](#keysight.ads.dds.AntennaIndepAxis.show_ticks "Link to this definition")

    *property* start*: float*[](#keysight.ads.dds.AntennaIndepAxis.start "Link to this definition")

    *property* stop*: float*[](#keysight.ads.dds.AntennaIndepAxis.stop "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.AntennaIndepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.AntennaDepAxis[](#keysight.ads.dds.AntennaDepAxis "Link to this definition")
:   The dependent axis of [`AntennaPlot`](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.AntennaPlot").

    This class cannot be instantiated directly. It is automatically instantiated when an [`AntennaPlot`](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.AntennaPlot") is created.
    It is accessed by the property [`AntennaPlot.dep_axis`](plots.md#keysight.ads.dds.AntennaPlot.dep_axis "keysight.ads.dds.AntennaPlot.dep_axis").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.AntennaDepAxis.grid_properties "Link to this definition")

    *property* is\_autoscaled*: bool*[](#keysight.ads.dds.AntennaDepAxis.is_autoscaled "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.AntennaDepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.AntennaDepAxis.label "Link to this definition")

    *property* label\_properties*: [AxisTextProperties](#keysight.ads.dds.AxisTextProperties "keysight.ads.dds.core.ddbase.AxisTextProperties")*[](#keysight.ads.dds.AntennaDepAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.AntennaDepAxis.max "Link to this definition")

    *property* min*: float*[](#keysight.ads.dds.AntennaDepAxis.min "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.AntennaDepAxis.name "Link to this definition")

    *property* orientation*: [AxisOrientation](#keysight.ads.dds.AxisOrientation "keysight.ads.dds.core.ddplot.AxisOrientation")*[](#keysight.ads.dds.AntennaDepAxis.orientation "Link to this definition")

    *property* show\_label*: bool*[](#keysight.ads.dds.AntennaDepAxis.show_label "Link to this definition")

    *property* show\_tick\_values*: bool*[](#keysight.ads.dds.AntennaDepAxis.show_tick_values "Link to this definition")

    *property* show\_ticks*: bool*[](#keysight.ads.dds.AntennaDepAxis.show_ticks "Link to this definition")

    *property* step*: float*[](#keysight.ads.dds.AntennaDepAxis.step "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.AntennaDepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.PolarIndepAxis[](#keysight.ads.dds.PolarIndepAxis "Link to this definition")
:   The independent axis of [`PolarPlot`](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.PolarPlot").

    This class cannot be instantiated directly. It is automatically instantiated when a [`PolarPlot`](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.PolarPlot") is created.
    It is accessed by the property [`PolarPlot.indep_axis`](plots.md#keysight.ads.dds.PolarPlot.indep_axis "keysight.ads.dds.PolarPlot.indep_axis").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.PolarIndepAxis.grid_properties "Link to this definition")

    *property* is\_all\_indep\_data\_displayed*: bool*[](#keysight.ads.dds.PolarIndepAxis.is_all_indep_data_displayed "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.PolarIndepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.PolarIndepAxis.label "Link to this definition")

    *property* label\_properties*: [AxisTextProperties](#keysight.ads.dds.AxisTextProperties "keysight.ads.dds.core.ddbase.AxisTextProperties")*[](#keysight.ads.dds.PolarIndepAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.PolarIndepAxis.name "Link to this definition")

    *property* orientation*: [AxisOrientation](#keysight.ads.dds.AxisOrientation "keysight.ads.dds.core.ddplot.AxisOrientation")*[](#keysight.ads.dds.PolarIndepAxis.orientation "Link to this definition")

    *property* show\_label*: bool*[](#keysight.ads.dds.PolarIndepAxis.show_label "Link to this definition")

    *property* show\_tick\_values*: bool*[](#keysight.ads.dds.PolarIndepAxis.show_tick_values "Link to this definition")

    *property* show\_ticks*: bool*[](#keysight.ads.dds.PolarIndepAxis.show_ticks "Link to this definition")

    *property* start*: float*[](#keysight.ads.dds.PolarIndepAxis.start "Link to this definition")

    *property* stop*: float*[](#keysight.ads.dds.PolarIndepAxis.stop "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.PolarIndepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.PolarDepAxis[](#keysight.ads.dds.PolarDepAxis "Link to this definition")
:   The dependent axis of [`PolarPlot`](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.PolarPlot").

    This class cannot be instantiated directly. It is automatically instantiated when a [`PolarPlot`](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.PolarPlot") is created.
    It is accessed by the property [`PolarPlot.dep_axis`](plots.md#keysight.ads.dds.PolarPlot.dep_axis "keysight.ads.dds.PolarPlot.dep_axis").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.PolarDepAxis.grid_properties "Link to this definition")

    *property* is\_autoscaled*: bool*[](#keysight.ads.dds.PolarDepAxis.is_autoscaled "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.PolarDepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.PolarDepAxis.label "Link to this definition")

    *property* label\_properties*: [AxisTextProperties](#keysight.ads.dds.AxisTextProperties "keysight.ads.dds.core.ddbase.AxisTextProperties")*[](#keysight.ads.dds.PolarDepAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.PolarDepAxis.max "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.PolarDepAxis.name "Link to this definition")

    *property* orientation*: [AxisOrientation](#keysight.ads.dds.AxisOrientation "keysight.ads.dds.core.ddplot.AxisOrientation")*[](#keysight.ads.dds.PolarDepAxis.orientation "Link to this definition")

    *property* show\_label*: bool*[](#keysight.ads.dds.PolarDepAxis.show_label "Link to this definition")

    *property* show\_tick\_values*: bool*[](#keysight.ads.dds.PolarDepAxis.show_tick_values "Link to this definition")

    *property* show\_ticks*: bool*[](#keysight.ads.dds.PolarDepAxis.show_ticks "Link to this definition")

    *property* step*: float*[](#keysight.ads.dds.PolarDepAxis.step "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.PolarDepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.RectAxis[](#keysight.ads.dds.RectAxis "Link to this definition")
:   The axes of [`RectPlot`](plots.md#keysight.ads.dds.RectPlot "keysight.ads.dds.RectPlot") and [`StackedPlot`](plots.md#keysight.ads.dds.StackedPlot "keysight.ads.dds.StackedPlot").

    This class cannot be instantiated directly. It is automatically instantiated when a [`RectPlot`](plots.md#keysight.ads.dds.RectPlot "keysight.ads.dds.RectPlot") or [`StackedPlot`](plots.md#keysight.ads.dds.StackedPlot "keysight.ads.dds.StackedPlot")
    is created. It is accessed by the properties [`RectPlot.axes`](plots.md#keysight.ads.dds.RectPlot.axes "keysight.ads.dds.RectPlot.axes") and [`StackedPlot.axes`](plots.md#keysight.ads.dds.StackedPlot.axes "keysight.ads.dds.StackedPlot.axes").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.RectAxis.grid_properties "Link to this definition")

    *property* is\_autoscaled*: bool*[](#keysight.ads.dds.RectAxis.is_autoscaled "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.RectAxis.is_grid_on "Link to this definition")

    *property* is\_logarithmic*: bool*[](#keysight.ads.dds.RectAxis.is_logarithmic "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.RectAxis.label "Link to this definition")

    *property* label\_properties*: [AxisTextProperties](#keysight.ads.dds.AxisTextProperties "keysight.ads.dds.core.ddbase.AxisTextProperties")*[](#keysight.ads.dds.RectAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.RectAxis.max "Link to this definition")

    *property* min*: float*[](#keysight.ads.dds.RectAxis.min "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.RectAxis.name "Link to this definition")

    *property* orientation*: [AxisOrientation](#keysight.ads.dds.AxisOrientation "keysight.ads.dds.core.ddplot.AxisOrientation")*[](#keysight.ads.dds.RectAxis.orientation "Link to this definition")

    set\_range(*min: float*, *max: float*, *step: float | None = None*) → None[](#keysight.ads.dds.RectAxis.set_range "Link to this definition")

    *property* show\_label*: bool*[](#keysight.ads.dds.RectAxis.show_label "Link to this definition")

    *property* show\_tick\_values*: bool*[](#keysight.ads.dds.RectAxis.show_tick_values "Link to this definition")

    *property* show\_ticks*: bool*[](#keysight.ads.dds.RectAxis.show_ticks "Link to this definition")

    *property* step*: float*[](#keysight.ads.dds.RectAxis.step "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.RectAxis.string_format "Link to this definition")

*class* keysight.ads.dds.SmithChartIndepAxis[](#keysight.ads.dds.SmithChartIndepAxis "Link to this definition")
:   The independent axis of [`SmithChart`](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart").

    This class cannot be instantiated directly. It is automatically instantiated when a [`SmithChart`](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart") is created.
    It is accessed by the property [`SmithChart.indep_axis`](plots.md#keysight.ads.dds.SmithChart.indep_axis "keysight.ads.dds.SmithChart.indep_axis").

    *property* admittance\_grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.SmithChartIndepAxis.admittance_grid_properties "Link to this definition")

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.SmithChartIndepAxis.grid_properties "Link to this definition")

    *property* impedance\_grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.SmithChartIndepAxis.impedance_grid_properties "Link to this definition")

    *property* is\_all\_indep\_data\_displayed*: bool*[](#keysight.ads.dds.SmithChartIndepAxis.is_all_indep_data_displayed "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.SmithChartIndepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.SmithChartIndepAxis.label "Link to this definition")

    *property* label\_properties*: [AxisTextProperties](#keysight.ads.dds.AxisTextProperties "keysight.ads.dds.core.ddbase.AxisTextProperties")*[](#keysight.ads.dds.SmithChartIndepAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.SmithChartIndepAxis.name "Link to this definition")

    *property* orientation*: [AxisOrientation](#keysight.ads.dds.AxisOrientation "keysight.ads.dds.core.ddplot.AxisOrientation")*[](#keysight.ads.dds.SmithChartIndepAxis.orientation "Link to this definition")

    *property* show\_label*: bool*[](#keysight.ads.dds.SmithChartIndepAxis.show_label "Link to this definition")

    *property* show\_tick\_values*: bool*[](#keysight.ads.dds.SmithChartIndepAxis.show_tick_values "Link to this definition")

    *property* show\_ticks*: bool*[](#keysight.ads.dds.SmithChartIndepAxis.show_ticks "Link to this definition")

    *property* start*: float*[](#keysight.ads.dds.SmithChartIndepAxis.start "Link to this definition")

    *property* stop*: float*[](#keysight.ads.dds.SmithChartIndepAxis.stop "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.SmithChartIndepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.SmithChartDepAxis[](#keysight.ads.dds.SmithChartDepAxis "Link to this definition")
:   The dependent axis of [`SmithChart`](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart").

    This class cannot be instantiated directly. It is automatically instantiated when a [`SmithChart`](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart") is created.
    It is accessed by the property [`SmithChart.dep_axis`](plots.md#keysight.ads.dds.SmithChart.dep_axis "keysight.ads.dds.SmithChart.dep_axis").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.SmithChartDepAxis.grid_properties "Link to this definition")

    *property* is\_autoscaled*: bool*[](#keysight.ads.dds.SmithChartDepAxis.is_autoscaled "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.SmithChartDepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.SmithChartDepAxis.label "Link to this definition")

    *property* label\_properties*: [AxisTextProperties](#keysight.ads.dds.AxisTextProperties "keysight.ads.dds.core.ddbase.AxisTextProperties")*[](#keysight.ads.dds.SmithChartDepAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.SmithChartDepAxis.max "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.SmithChartDepAxis.name "Link to this definition")

    *property* orientation*: [AxisOrientation](#keysight.ads.dds.AxisOrientation "keysight.ads.dds.core.ddplot.AxisOrientation")*[](#keysight.ads.dds.SmithChartDepAxis.orientation "Link to this definition")

    *property* show\_label*: bool*[](#keysight.ads.dds.SmithChartDepAxis.show_label "Link to this definition")

    *property* show\_tick\_values*: bool*[](#keysight.ads.dds.SmithChartDepAxis.show_tick_values "Link to this definition")

    *property* show\_ticks*: bool*[](#keysight.ads.dds.SmithChartDepAxis.show_ticks "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.SmithChartDepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.TextAxis[](#keysight.ads.dds.TextAxis "Link to this definition")
:   *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.TextAxis.grid_properties "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.TextAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.TextAxis.label "Link to this definition")

    *property* label\_properties*: [AxisTextProperties](#keysight.ads.dds.AxisTextProperties "keysight.ads.dds.core.ddbase.AxisTextProperties")*[](#keysight.ads.dds.TextAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.TextAxis.name "Link to this definition")

    *property* orientation*: [AxisOrientation](#keysight.ads.dds.AxisOrientation "keysight.ads.dds.core.ddplot.AxisOrientation")*[](#keysight.ads.dds.TextAxis.orientation "Link to this definition")

    *property* show\_label*: bool*[](#keysight.ads.dds.TextAxis.show_label "Link to this definition")

    *property* show\_tick\_values*: bool*[](#keysight.ads.dds.TextAxis.show_tick_values "Link to this definition")

    *property* show\_ticks*: bool*[](#keysight.ads.dds.TextAxis.show_ticks "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.TextAxis.string_format "Link to this definition")

*class* keysight.ads.dds.AxisOrientation[](#keysight.ads.dds.AxisOrientation "Link to this definition")
:   RIGHT\_Y\_DIRECTION *= <AxisOrientation.RIGHT\_Y\_DIRECTION: 4>*[](#keysight.ads.dds.AxisOrientation.RIGHT_Y_DIRECTION "Link to this definition")

    X\_DIRECTION *= <AxisOrientation.X\_DIRECTION: 1>*[](#keysight.ads.dds.AxisOrientation.X_DIRECTION "Link to this definition")

    Y\_DIRECTION *= <AxisOrientation.Y\_DIRECTION: 2>*[](#keysight.ads.dds.AxisOrientation.Y_DIRECTION "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.AxisOrientation.str "Link to this definition")

*class* keysight.ads.dds.AxisTextProperties[](#keysight.ads.dds.AxisTextProperties "Link to this definition")
:   \_\_init\_\_(*font: str | None = None*, *color: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color") | None = None*, *label\_font\_size: int | None = None*, *tick\_font\_size: int | None = None*) → None[](#keysight.ads.dds.AxisTextProperties.__init__ "Link to this definition")
    :   Create an instance of AxisTextProperties.

        Parameters:
        :   * **font** (*str* *[**optional**,* *default=None**]*) – If a string is passed, the font used is the element in the
              list of available fonts that matches the string. If no
              font is specified, the default axis font is used. If the
              font is not found, an exception is thrown.
            * **color** ([*Color*](basic.md#keysight.ads.dds.Color "keysight.ads.dds.Color") *[**optional**,* *default=None**]*) – If a valid Color is passed, the axis label text and tick
              text will be drawn in the specified color. If no color is
              specified (value == None), then the text will be drawn in
              default axis color. If an invalid color is specified, an
              exception is thrown.
            * **label\_font\_size** (*int* *[**optional**,* *default=None**]*) – If an integer is passed, it specifies the point size of the axis label font.
              If label\_font\_size is not passed or is negative, the default axis label font size is used.
            * **tick\_font\_size** (*int* *[**optional**,* *default=None**]*) – If an integer is passed, it specifies the point size of the axis tick font.
              If tick\_font\_size is not passed or is negative, the default axis tick font size is used.

        Raises:
        :   * **RuntimeError: Font name "<font>" not found on system.** – The “font” parameter is not found in the list of fonts.
            * **RuntimeError: Invalid color index "<int>" specified. Color index must be between "0" and "<int>".** – The integer parameter is out of bounds of the available colors.

        Example

        Set axis label and tick text label font size on the X Axis of the plot.

        ```
        >>> from keysight.ads import dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot()
        >>>
        >>> props = dds.AxisTextProperties(label_font_size=22, tick_font_size=10)
        >>> plot.axes["X Axis"].label_properties = props
        >>>
        >>> props = plot.axes["X Axis"].label_properties
        >>> assert props.label_font_size == 22
        >>> assert props.tick_font_size == 10
        ```

    *property* color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.AxisTextProperties.color "Link to this definition")

    *static* default\_font() → str[](#keysight.ads.dds.AxisTextProperties.default_font "Link to this definition")

    *property* font*: str*[](#keysight.ads.dds.AxisTextProperties.font "Link to this definition")

    *static* font\_exists(*font: str*) → bool[](#keysight.ads.dds.AxisTextProperties.font_exists "Link to this definition")

    *static* fonts() → list[str][](#keysight.ads.dds.AxisTextProperties.fonts "Link to this definition")
    :   Return a list of fonts.

        Returns:
        :   A list of available fonts. Each font in the list is stored as a string.

        Return type:
        :   list[str]

        Example

        Obtain a list of available fonts.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds.TextProperties.fonts()
        ```

    *property* label\_font\_size*: int*[](#keysight.ads.dds.AxisTextProperties.label_font_size "Link to this definition")

    *property* size*: int*[](#keysight.ads.dds.AxisTextProperties.size "Link to this definition")

    text\_size(*text: str*) → tuple[int, int][](#keysight.ads.dds.AxisTextProperties.text_size "Link to this definition")

    *property* tick\_font\_size*: int*[](#keysight.ads.dds.AxisTextProperties.tick_font_size "Link to this definition")

On this page

[Previous

Plots](plots.md)
[Next

Legend](legend.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top