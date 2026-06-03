<!-- 来源: reference\dds\trace.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Trace

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
    - [Axes](axes.md)
    - [Legend](legend.md)
    - Trace
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

# Trace[](#trace "Link to this heading")

*class* keysight.ads.dds.Trace[](#keysight.ads.dds.Trace "Link to this definition")
:   Traces are used to display data on a plot.

    This class cannot be instantiated directly.
    An instance(s) is created by the methods add\_trace() and add\_traces() in a plot.

    add\_marker(*name: str*, *indep\_value\_or\_expr: float | str*, *type: [MarkerType](marker.md#keysight.ads.dds.MarkerType "keysight.ads.dds.core.ddplot.MarkerType") | str = MarkerType.NORMAL*) → [TraceMarker](marker.md#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker")[](#keysight.ads.dds.Trace.add_marker "Link to this definition")

    *property* autosequence\_settings*: AutoSequenceSettings*[](#keysight.ads.dds.Trace.autosequence_settings "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Trace.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* bus\_always\_display\_transition*: bool*[](#keysight.ads.dds.Trace.bus_always_display_transition "Link to this definition")

    *property* bus\_text\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.Trace.bus_text_color "Link to this definition")

    *property* color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.Trace.color "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.Trace.delete_object "Link to this definition")

    *property* density\_num\_colors*: int*[](#keysight.ads.dds.Trace.density_num_colors "Link to this definition")

    *property* density\_start\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.Trace.density_start_color "Link to this definition")

    *property* density\_symbol\_type*: DensitySymbolType*[](#keysight.ads.dds.Trace.density_symbol_type "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.Trace.dep_axis "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.Trace.expression "Link to this definition")

    *property* font*: str*[](#keysight.ads.dds.Trace.font "Link to this definition")

    *property* histogram\_enable\_fill*: bool*[](#keysight.ads.dds.Trace.histogram_enable_fill "Link to this definition")

    *property* histogram\_fill\_pattern*: str*[](#keysight.ads.dds.Trace.histogram_fill_pattern "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.Trace.indep_axis "Link to this definition")

    *property* label\_properties*: TraceLabelProperties*[](#keysight.ads.dds.Trace.label_properties "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Trace.line_properties "Link to this definition")

    *property* line\_type*: [LineType](basic.md#keysight.ads.dds.LineType "keysight.ads.dds.core.ddbase.LineType")*[](#keysight.ads.dds.Trace.line_type "Link to this definition")

    *property* linear\_symbol\_spacing*: SymbolSpacing*[](#keysight.ads.dds.Trace.linear_symbol_spacing "Link to this definition")

    *property* markers*: NamedItemCollectionAbc[[TraceMarker](marker.md#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker")]*[](#keysight.ads.dds.Trace.markers "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Trace.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Trace.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Trace.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Trace.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Trace.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Trace.name "Link to this definition")

    *property* spectral\_display\_arrowheads*: bool*[](#keysight.ads.dds.Trace.spectral_display_arrowheads "Link to this definition")

    *property* string\_format\_option*: StringFormatOption*[](#keysight.ads.dds.Trace.string_format_option "Link to this definition")

    *property* symbol\_type*: SymbolType*[](#keysight.ads.dds.Trace.symbol_type "Link to this definition")

    *property* trace\_type*: TraceType*[](#keysight.ads.dds.Trace.trace_type "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Trace.type "Link to this definition")

    *property* variable*: bool | int | float | complex | str | VariableBlock | None*[](#keysight.ads.dds.Trace.variable "Link to this definition")

    *property* width*: float*[](#keysight.ads.dds.Trace.width "Link to this definition")

*class* keysight.ads.dds.TextTrace[](#keysight.ads.dds.TextTrace "Link to this definition")
:   add\_marker(*name: str*, *indep\_value\_or\_expr: float | str*, *type: [MarkerType](marker.md#keysight.ads.dds.MarkerType "keysight.ads.dds.core.ddplot.MarkerType") | str = MarkerType.NORMAL*) → [TraceMarker](marker.md#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker")[](#keysight.ads.dds.TextTrace.add_marker "Link to this definition")

    *property* autosequence\_settings*: AutoSequenceSettings*[](#keysight.ads.dds.TextTrace.autosequence_settings "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.TextTrace.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* bus\_always\_display\_transition*: bool*[](#keysight.ads.dds.TextTrace.bus_always_display_transition "Link to this definition")

    *property* bus\_text\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.TextTrace.bus_text_color "Link to this definition")

    *property* color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.TextTrace.color "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.TextTrace.delete_object "Link to this definition")

    *property* density\_num\_colors*: int*[](#keysight.ads.dds.TextTrace.density_num_colors "Link to this definition")

    *property* density\_start\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.TextTrace.density_start_color "Link to this definition")

    *property* density\_symbol\_type*: DensitySymbolType*[](#keysight.ads.dds.TextTrace.density_symbol_type "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.TextTrace.dep_axis "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.TextTrace.expression "Link to this definition")

    *property* font*: str*[](#keysight.ads.dds.TextTrace.font "Link to this definition")

    *property* histogram\_enable\_fill*: bool*[](#keysight.ads.dds.TextTrace.histogram_enable_fill "Link to this definition")

    *property* histogram\_fill\_pattern*: str*[](#keysight.ads.dds.TextTrace.histogram_fill_pattern "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.TextTrace.indep_axis "Link to this definition")

    *property* label\_properties*: TraceLabelProperties*[](#keysight.ads.dds.TextTrace.label_properties "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.TextTrace.line_properties "Link to this definition")

    *property* line\_type*: [LineType](basic.md#keysight.ads.dds.LineType "keysight.ads.dds.core.ddbase.LineType")*[](#keysight.ads.dds.TextTrace.line_type "Link to this definition")

    *property* linear\_symbol\_spacing*: SymbolSpacing*[](#keysight.ads.dds.TextTrace.linear_symbol_spacing "Link to this definition")

    *property* markers*: NamedItemCollectionAbc[[TraceMarker](marker.md#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker")]*[](#keysight.ads.dds.TextTrace.markers "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.TextTrace.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.TextTrace.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.TextTrace.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.TextTrace.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.TextTrace.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.TextTrace.name "Link to this definition")

    *property* spectral\_display\_arrowheads*: bool*[](#keysight.ads.dds.TextTrace.spectral_display_arrowheads "Link to this definition")

    *property* string\_format\_option*: StringFormatOption*[](#keysight.ads.dds.TextTrace.string_format_option "Link to this definition")

    *property* symbol\_type*: SymbolType*[](#keysight.ads.dds.TextTrace.symbol_type "Link to this definition")

    *property* trace\_type*: TraceType*[](#keysight.ads.dds.TextTrace.trace_type "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.TextTrace.type "Link to this definition")

    *property* variable*: bool | int | float | complex | str | VariableBlock | None*[](#keysight.ads.dds.TextTrace.variable "Link to this definition")

    *property* width*: float*[](#keysight.ads.dds.TextTrace.width "Link to this definition")

On this page

[Previous

Legend](legend.md)
[Next

Markers](marker.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top