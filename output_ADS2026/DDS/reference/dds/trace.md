<!-- 来源: reference\dds\trace.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Trace

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

# Trace[](#trace "Link to this heading")

*class* keysight.ads.dds.Trace[](#keysight.ads.dds.Trace "Link to this definition")
:   Traces are used to display data on a plot.

    This class cannot be instantiated directly.
    An instance(s) is created by the methods add\_trace() and add\_traces() in a plot.

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.Trace.__init__ "Link to this definition")

    add\_marker(*name: str*, *indep\_value\_or\_expr: float | str*, *type: [MarkerType](marker.md#keysight.ads.dds.MarkerType "keysight.ads.dds.core.ddplot.MarkerType") | str = MarkerType.NORMAL*) → [TraceMarker](marker.md#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker")[](#keysight.ads.dds.Trace.add_marker "Link to this definition")

    *property* autosequence\_settings*: [AutoSequenceSettings](#keysight.ads.dds.AutoSequenceSettings "keysight.ads.dds.core.ddplot.AutoSequenceSettings")*[](#keysight.ads.dds.Trace.autosequence_settings "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Trace.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* bus\_always\_display\_transition*: bool*[](#keysight.ads.dds.Trace.bus_always_display_transition "Link to this definition")

    *property* bus\_text\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.Trace.bus_text_color "Link to this definition")

    *property* color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.Trace.color "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.Trace.delete_object "Link to this definition")

    *property* density\_num\_colors*: int*[](#keysight.ads.dds.Trace.density_num_colors "Link to this definition")

    *property* density\_start\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.Trace.density_start_color "Link to this definition")

    *property* density\_symbol\_type*: [DensitySymbolType](#keysight.ads.dds.DensitySymbolType "keysight.ads.dds.core.ddbase.DensitySymbolType")*[](#keysight.ads.dds.Trace.density_symbol_type "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.Trace.dep_axis "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.Trace.expression "Link to this definition")

    *property* font*: str*[](#keysight.ads.dds.Trace.font "Link to this definition")

    *property* histogram\_enable\_fill*: bool*[](#keysight.ads.dds.Trace.histogram_enable_fill "Link to this definition")

    *property* histogram\_fill\_pattern*: str*[](#keysight.ads.dds.Trace.histogram_fill_pattern "Link to this definition")

    *property* history\_count*: int*[](#keysight.ads.dds.Trace.history_count "Link to this definition")
    :   The number of history subtraces currently maintained for this trace.

        Return type:
        :   int

    *property* history\_labels*: list[str]*[](#keysight.ads.dds.Trace.history_labels "Link to this definition")
    :   The label for each history subtrace ordered from newest to oldest. The default labels are generated based on the event that caused the history to be generated.

    *property* indep\_axis*: str*[](#keysight.ads.dds.Trace.indep_axis "Link to this definition")

    *property* label\_properties*: [TraceLabelProperties](#keysight.ads.dds.TraceLabelProperties "keysight.ads.dds.core.ddplot.TraceLabelProperties")*[](#keysight.ads.dds.Trace.label_properties "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Trace.line_properties "Link to this definition")

    *property* line\_type*: [LineType](basic.md#keysight.ads.dds.LineType "keysight.ads.dds.core.ddbase.LineType")*[](#keysight.ads.dds.Trace.line_type "Link to this definition")

    *property* linear\_symbol\_spacing*: [SymbolSpacing](#keysight.ads.dds.SymbolSpacing "keysight.ads.dds.core.ddplot.SymbolSpacing")*[](#keysight.ads.dds.Trace.linear_symbol_spacing "Link to this definition")

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

    start\_history(*depth: int | None = None*) → None[](#keysight.ads.dds.Trace.start_history "Link to this definition")
    :   Enable history mode for this trace.

        Parameters:
        :   **depth** (*int* *[**optional**,* *default=None**]*) – The number of history subtraces to maintain for this trace. If not specified,
            the default depth is used.

        Return type:
        :   None

    stop\_history() → None[](#keysight.ads.dds.Trace.stop_history "Link to this definition")
    :   Disable history mode for this trace.

        Return type:
        :   None

    *property* string\_format\_option*: [StringFormatOption](basic.md#keysight.ads.dds.StringFormatOption "keysight.ads.dds.core.ddbase.StringFormatOption")*[](#keysight.ads.dds.Trace.string_format_option "Link to this definition")

    *property* subtrace\_settings*: dict[str, SubtraceSettings]*[](#keysight.ads.dds.Trace.subtrace_settings "Link to this definition")
    :   Get the subtrace settings for this trace.

    *property* symbol\_type*: [SymbolType](#keysight.ads.dds.SymbolType "keysight.ads.dds.core.ddbase.SymbolType")*[](#keysight.ads.dds.Trace.symbol_type "Link to this definition")

    *property* trace\_type*: [TraceType](#keysight.ads.dds.TraceType "keysight.ads.dds.core.ddplot.TraceType")*[](#keysight.ads.dds.Trace.trace_type "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Trace.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.Trace.uid "Link to this definition")

    *property* variable*: bool | int | float | complex | str | VariableBlock | None*[](#keysight.ads.dds.Trace.variable "Link to this definition")

    *property* width*: float*[](#keysight.ads.dds.Trace.width "Link to this definition")

*class* keysight.ads.dds.TextTrace[](#keysight.ads.dds.TextTrace "Link to this definition")
:   \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.TextTrace.__init__ "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.TextTrace.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* complex\_format*: [ComplexStringFormatOption](basic.md#keysight.ads.dds.ComplexStringFormatOption "keysight.ads.dds.core.ddbase.ComplexStringFormatOption")*[](#keysight.ads.dds.TextTrace.complex_format "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.TextTrace.delete_object "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.TextTrace.expression "Link to this definition")

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

    *property* type*: ObjectType*[](#keysight.ads.dds.TextTrace.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.TextTrace.uid "Link to this definition")

    *property* variable*: bool | int | float | complex | str | VariableBlock | None*[](#keysight.ads.dds.TextTrace.variable "Link to this definition")

*class* keysight.ads.dds.AutoSequenceSettings[](#keysight.ads.dds.AutoSequenceSettings "Link to this definition")
:   Class that contains properties for autosequencing in linear traces.

    \_\_init\_\_(*sweep\_var: str | None = None*, *enable\_symbol\_type: bool | None = None*, *symbol\_type\_seq\_num: int | None = None*, *enable\_line\_type: bool | None = None*, *line\_type\_seq\_num: int | None = None*, *enable\_line\_color: bool | None = None*, *line\_color\_seq\_num: int | None = None*, *enable\_line\_color\_family: bool | None = None*, *line\_color\_family\_seq\_num: int | None = None*)[](#keysight.ads.dds.AutoSequenceSettings.__init__ "Link to this definition")
    :   Create an instance of AutoSequenceSettings.

        Only the parameters that are set will be applied to the trace.
        When setting Trace.autosequence\_settings, only properties that are not None will be applied.

        Parameters:
        :   * **sweep\_var** (*str* *[**optional**,* *default=None**]*) – The sweep parameter that will be used for autosequencing.
              If the “\*” is passed, all sweep variables are selected.
              If no sweep parameter is specified, the default value is None, which will have no effect the trace being applied to.
            * **enable\_symbol\_type** (*bool* *[**optional**,* *default=None**]*) – If True, the symbol type will be included in autosequencing, and vice versa if False.
              The default value is None.
            * **symbol\_type\_seq\_num** (*int* *[**optional**,* *default=None**]*) – The sequence number for symbol type in autosequence. If no sequence number is specified, the default value is None.
            * **enable\_line\_type** (*bool* *[**optional**,* *default=None**]*) – If True, the line type will be included in autosequencing, and vice versa if False.
              The default value is None.
            * **line\_type\_seq\_num** (*int* *[**optional**,* *default=None**]*) – The sequence number for line type in autosequence. If no sequence number is specified, the default value is None.
            * **enable\_line\_color** (*bool* *[**optional**,* *default=None**]*) – If True, the line color will be included in autosequencing, and vice versa if False.
              The default value is None.
            * **line\_color\_seq\_num** (*int* *[**optional**,* *default=None**]*) – The sequence number for line color in autosequence. If no sequence number is specified, the default value is None.

        Example

        Only enable symbol type and line color in autosequencing, and explicitly set the symbol type sequence number to 2.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("amplifier.dds")
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot("My Plot")
        >>> trace = plot.add_trace("dB(S12)")
        >>> trace.autosequence_settings = dds.AutoSequenceSettings(sweep_var="*", enable_symbol_type=True, symbol_type_seq_num=2, enable_line_color=True)
        >>> trace.autosequence_settings
            <AutoSequenceSettings sweep_var="*">
        ```

    *property* enable\_line\_color*: bool*[](#keysight.ads.dds.AutoSequenceSettings.enable_line_color "Link to this definition")

    *property* enable\_line\_color\_family*: bool*[](#keysight.ads.dds.AutoSequenceSettings.enable_line_color_family "Link to this definition")

    *property* enable\_line\_type*: bool*[](#keysight.ads.dds.AutoSequenceSettings.enable_line_type "Link to this definition")

    *property* enable\_symbol\_type*: bool*[](#keysight.ads.dds.AutoSequenceSettings.enable_symbol_type "Link to this definition")

    *property* line\_color\_family\_seq\_num*: int*[](#keysight.ads.dds.AutoSequenceSettings.line_color_family_seq_num "Link to this definition")

    *property* line\_color\_seq\_num*: int*[](#keysight.ads.dds.AutoSequenceSettings.line_color_seq_num "Link to this definition")

    *property* line\_type\_seq\_num*: int*[](#keysight.ads.dds.AutoSequenceSettings.line_type_seq_num "Link to this definition")

    *property* sweep\_var*: str | None*[](#keysight.ads.dds.AutoSequenceSettings.sweep_var "Link to this definition")

    *property* symbol\_type\_seq\_num*: int*[](#keysight.ads.dds.AutoSequenceSettings.symbol_type_seq_num "Link to this definition")

*class* keysight.ads.dds.DensitySymbolType[](#keysight.ads.dds.DensitySymbolType "Link to this definition")
:   CROSS *= <DensitySymbolType.CROSS: 8>*[](#keysight.ads.dds.DensitySymbolType.CROSS "Link to this definition")

    DOT *= <DensitySymbolType.DOT: 0>*[](#keysight.ads.dds.DensitySymbolType.DOT "Link to this definition")

    FILLED\_CIRCLE *= <DensitySymbolType.FILLED\_CIRCLE: 10>*[](#keysight.ads.dds.DensitySymbolType.FILLED_CIRCLE "Link to this definition")

    FILLED\_DIAMOND *= <DensitySymbolType.FILLED\_DIAMOND: 13>*[](#keysight.ads.dds.DensitySymbolType.FILLED_DIAMOND "Link to this definition")

    FILLED\_REVERSE\_TRIANGLE *= <DensitySymbolType.FILLED\_REVERSE\_TRIANGLE: 12>*[](#keysight.ads.dds.DensitySymbolType.FILLED_REVERSE_TRIANGLE "Link to this definition")

    FILLED\_SQUARE *= <DensitySymbolType.FILLED\_SQUARE: 9>*[](#keysight.ads.dds.DensitySymbolType.FILLED_SQUARE "Link to this definition")

    FILLED\_TRIANGLE *= <DensitySymbolType.FILLED\_TRIANGLE: 11>*[](#keysight.ads.dds.DensitySymbolType.FILLED_TRIANGLE "Link to this definition")

    STAR *= <DensitySymbolType.STAR: 6>*[](#keysight.ads.dds.DensitySymbolType.STAR "Link to this definition")

    X *= <DensitySymbolType.X: 7>*[](#keysight.ads.dds.DensitySymbolType.X "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.DensitySymbolType.str "Link to this definition")

*class* keysight.ads.dds.TraceLabelProperties[](#keysight.ads.dds.TraceLabelProperties "Link to this definition")
:   Class that contains properties for trace labels.

    \_\_init\_\_(*display\_label: bool | None = None*, *string\_format: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat") | None = None*, *offset: float | None = None*, *font: str | None = None*, *font\_size: int | None = None*, *show\_units: bool | None = None*, *show\_parameter\_names: bool | None = None*) → None[](#keysight.ads.dds.TraceLabelProperties.__init__ "Link to this definition")
    :   Create an instance of TraceLabelProperties.

        Parameters:
        :   * **display\_label** (*bool* *[**optional**,* *default=None**]*) – If True, trace labels will be displayed in linear and digital traces, and vice versa if False.
              If no value is passed, it will not be affected in the trace.
            * **string\_format** ([*StringFormat*](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.StringFormat") *[**optional**,* *default=None**]*) – The format option and significant digits that will be used for the label.
              If no format is specified, it will not be affected in the trace.
            * **offset** (*float* *[**optional**,* *default=None**]*) – If no value is passed, the label offset will not be affected in the trace.
            * **font** (*str* *[**optional**,* *default=None**]*) – If no value is passed, the label font will not be affected in the trace.
            * **font\_size** (*int* *[**optional**,* *default=None**]*) – If no value is passed, the label font size will not be affected in the trace.
            * **show\_units** (*bool* *[**optional**,* *default=None**]*) – If True, the units will be shown, and vice versa if False.
              If no value is passed, it will not be affected in the trace.
            * **show\_parameter\_names** (*bool* *[**optional**,* *default=None**]*) – If True, the parameter names will be shown, and vice versa if False.
              If no value is passed, it will not be affected in the trace.

        Raises:
        :   **RuntimeError: Font name "<font>" not found on system.** – The “font” parameter is not found in the list of fonts.

    *property* display\_label*: bool*[](#keysight.ads.dds.TraceLabelProperties.display_label "Link to this definition")

    *property* font*: str*[](#keysight.ads.dds.TraceLabelProperties.font "Link to this definition")

    *property* font\_size*: int*[](#keysight.ads.dds.TraceLabelProperties.font_size "Link to this definition")

    *property* offset*: float*[](#keysight.ads.dds.TraceLabelProperties.offset "Link to this definition")

    *property* show\_parameter\_names*: bool*[](#keysight.ads.dds.TraceLabelProperties.show_parameter_names "Link to this definition")

    *property* show\_units*: bool*[](#keysight.ads.dds.TraceLabelProperties.show_units "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.TraceLabelProperties.string_format "Link to this definition")

*class* keysight.ads.dds.SymbolSpacing[](#keysight.ads.dds.SymbolSpacing "Link to this definition")
:   ALL\_DATA\_POINTS *= <SymbolSpacing.ALL\_DATA\_POINTS: 1>*[](#keysight.ads.dds.SymbolSpacing.ALL_DATA_POINTS "Link to this definition")

    AUTO\_SPACED *= <SymbolSpacing.AUTO\_SPACED: 0>*[](#keysight.ads.dds.SymbolSpacing.AUTO_SPACED "Link to this definition")

    NONE *= <SymbolSpacing.NO\_SYMBOLS: 2>*[](#keysight.ads.dds.SymbolSpacing.NONE "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.SymbolSpacing.str "Link to this definition")

*class* keysight.ads.dds.SymbolType[](#keysight.ads.dds.SymbolType "Link to this definition")
:   CIRCLE *= <SymbolType.CIRCLE: 2>*[](#keysight.ads.dds.SymbolType.CIRCLE "Link to this definition")

    CROSS *= <SymbolType.CROSS: 8>*[](#keysight.ads.dds.SymbolType.CROSS "Link to this definition")

    DIAMOND *= <SymbolType.DIAMOND: 5>*[](#keysight.ads.dds.SymbolType.DIAMOND "Link to this definition")

    DOT *= <SymbolType.DOT: 0>*[](#keysight.ads.dds.SymbolType.DOT "Link to this definition")

    REVERSE\_TRIANGLE *= <SymbolType.REVERSE\_TRIANGLE: 4>*[](#keysight.ads.dds.SymbolType.REVERSE_TRIANGLE "Link to this definition")

    SQUARE *= <SymbolType.SQUARE: 1>*[](#keysight.ads.dds.SymbolType.SQUARE "Link to this definition")

    STAR *= <SymbolType.STAR: 6>*[](#keysight.ads.dds.SymbolType.STAR "Link to this definition")

    TRIANGLE *= <SymbolType.TRIANGLE: 3>*[](#keysight.ads.dds.SymbolType.TRIANGLE "Link to this definition")

    X *= <SymbolType.X: 7>*[](#keysight.ads.dds.SymbolType.X "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.SymbolType.str "Link to this definition")

*class* keysight.ads.dds.TraceType[](#keysight.ads.dds.TraceType "Link to this definition")
:   AUTOMATIC *= <TraceTypeC.AutomaticTrace: 0>*[](#keysight.ads.dds.TraceType.AUTOMATIC "Link to this definition")

    BUS *= <TraceTypeC.BusTrace: 6>*[](#keysight.ads.dds.TraceType.BUS "Link to this definition")

    DENSITY *= <TraceTypeC.DensityTrace: 8>*[](#keysight.ads.dds.TraceType.DENSITY "Link to this definition")

    DIGITAL *= <TraceTypeC.DigitalTrace: 5>*[](#keysight.ads.dds.TraceType.DIGITAL "Link to this definition")

    HISTOGRAM *= <TraceTypeC.HistogramTrace: 3>*[](#keysight.ads.dds.TraceType.HISTOGRAM "Link to this definition")

    LINEAR *= <TraceTypeC.LinearTrace: 1>*[](#keysight.ads.dds.TraceType.LINEAR "Link to this definition")

    SAMPLED *= <TraceTypeC.SampledTrace: 7>*[](#keysight.ads.dds.TraceType.SAMPLED "Link to this definition")

    SCATTER *= <TraceTypeC.ScatterTrace: 4>*[](#keysight.ads.dds.TraceType.SCATTER "Link to this definition")

    SPECTRAL *= <TraceTypeC.SpectralTrace: 2>*[](#keysight.ads.dds.TraceType.SPECTRAL "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.TraceType.str "Link to this definition")

On this page

[Previous

Legend](legend.md)
[Next

Markers](marker.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top