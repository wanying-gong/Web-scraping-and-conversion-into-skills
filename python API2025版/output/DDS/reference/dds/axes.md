<!-- 来源: reference\dds\axes.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Axes

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
  + [keysight.ads.dds.app](app/index.md)
    - [Addon](app/addon.md)
    - [Callbacks](app/callbacks.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
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

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.AntennaIndepAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.AntennaIndepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.AntennaIndepAxis.orientation "Link to this definition")

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

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.AntennaDepAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.AntennaDepAxis.max "Link to this definition")

    *property* min*: float*[](#keysight.ads.dds.AntennaDepAxis.min "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.AntennaDepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.AntennaDepAxis.orientation "Link to this definition")

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

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.PolarIndepAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.PolarIndepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.PolarIndepAxis.orientation "Link to this definition")

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

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.PolarDepAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.PolarDepAxis.max "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.PolarDepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.PolarDepAxis.orientation "Link to this definition")

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

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.RectAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.RectAxis.max "Link to this definition")

    *property* min*: float*[](#keysight.ads.dds.RectAxis.min "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.RectAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.RectAxis.orientation "Link to this definition")

    set\_range(*min: float*, *max: float*, *step: float | None = None*) → None[](#keysight.ads.dds.RectAxis.set_range "Link to this definition")

    *property* step*: float*[](#keysight.ads.dds.RectAxis.step "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.RectAxis.string_format "Link to this definition")

*class* keysight.ads.dds.SmithChartIndepAxis[](#keysight.ads.dds.SmithChartIndepAxis "Link to this definition")
:   The independent axis of [`SmithChart`](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart").

    This class cannot be instantiated directly. It is automatically instantiated when a [`SmithChart`](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart") is created.
    It is accessed by the property [`SmithChart.indep_axis`](plots.md#keysight.ads.dds.SmithChart.indep_axis "keysight.ads.dds.SmithChart.indep_axis").

    *property* admittance\_grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.SmithChartIndepAxis.admittance_grid_properties "Link to this definition")

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.SmithChartIndepAxis.grid_properties "Link to this definition")

    *property* is\_all\_indep\_data\_displayed*: bool*[](#keysight.ads.dds.SmithChartIndepAxis.is_all_indep_data_displayed "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.SmithChartIndepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.SmithChartIndepAxis.label "Link to this definition")

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.SmithChartIndepAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.SmithChartIndepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.SmithChartIndepAxis.orientation "Link to this definition")

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

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.SmithChartDepAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.SmithChartDepAxis.max "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.SmithChartDepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.SmithChartDepAxis.orientation "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.SmithChartDepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.TextAxis[](#keysight.ads.dds.TextAxis "Link to this definition")
:   *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.TextAxis.grid_properties "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.TextAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.TextAxis.label "Link to this definition")

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.TextAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.TextAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.TextAxis.orientation "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.TextAxis.string_format "Link to this definition")

On this page

[Previous

Plots](plots.md)
[Next

Legend](legend.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top