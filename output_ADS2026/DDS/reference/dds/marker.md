<!-- 来源: reference\dds\marker.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Markers

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
    - Markers
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

# Markers[](#markers "Link to this heading")

*class* keysight.ads.dds.TraceMarker[](#keysight.ads.dds.TraceMarker "Link to this definition")
:   Markers return the independent and dependent values of the data.

    This class cannot be instantiated directly.
    An instance is created by the [`Trace.add_marker()`](trace.md#keysight.ads.dds.Trace.add_marker "keysight.ads.dds.Trace.add_marker").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.TraceMarker.__init__ "Link to this definition")

    *property* aperture\_height*: int*[](#keysight.ads.dds.TraceMarker.aperture_height "Link to this definition")

    *property* aperture\_width*: int*[](#keysight.ads.dds.TraceMarker.aperture_width "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.TraceMarker.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* complex\_format*: [ComplexStringFormatOption](basic.md#keysight.ads.dds.ComplexStringFormatOption "keysight.ads.dds.core.ddbase.ComplexStringFormatOption")*[](#keysight.ads.dds.TraceMarker.complex_format "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.TraceMarker.delete_object "Link to this definition")

    *property* delta\_dep\_value*: str | None*[](#keysight.ads.dds.TraceMarker.delta_dep_value "Link to this definition")

    *property* delta\_indep\_value*: str | None*[](#keysight.ads.dds.TraceMarker.delta_indep_value "Link to this definition")

    *property* delta\_reference*: [TraceMarker](#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker") | None*[](#keysight.ads.dds.TraceMarker.delta_reference "Link to this definition")
    :   The marker used as a reference for the delta.

    *property* dep\_value*: str*[](#keysight.ads.dds.TraceMarker.dep_value "Link to this definition")

    *property* indep\_value*: str*[](#keysight.ads.dds.TraceMarker.indep_value "Link to this definition")

    *property* index*: int*[](#keysight.ads.dds.TraceMarker.index "Link to this definition")

    *property* is\_name\_displayed*: bool*[](#keysight.ads.dds.TraceMarker.is_name_displayed "Link to this definition")

    *property* is\_readout\_displayed*: bool*[](#keysight.ads.dds.TraceMarker.is_readout_displayed "Link to this definition")

    *property* is\_symbol\_displayed*: bool*[](#keysight.ads.dds.TraceMarker.is_symbol_displayed "Link to this definition")

    *property* label\_text\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.TraceMarker.label_text_properties "Link to this definition")

    *property* marker\_type*: [MarkerType](#keysight.ads.dds.MarkerType "keysight.ads.dds.core.ddplot.MarkerType")*[](#keysight.ads.dds.TraceMarker.marker_type "Link to this definition")

    *property* mode*: [MarkerMode](#keysight.ads.dds.MarkerMode "keysight.ads.dds.core.ddplot.MarkerMode")*[](#keysight.ads.dds.TraceMarker.mode "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.TraceMarker.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.TraceMarker.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.TraceMarker.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.TraceMarker.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.TraceMarker.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.TraceMarker.name "Link to this definition")

    *property* offset*: float | None*[](#keysight.ads.dds.TraceMarker.offset "Link to this definition")

    *property* offset\_dep\_value*: str | None*[](#keysight.ads.dds.TraceMarker.offset_dep_value "Link to this definition")

    *property* offset\_indep\_value*: str | None*[](#keysight.ads.dds.TraceMarker.offset_indep_value "Link to this definition")

    *property* offset\_reference*: [TraceMarker](#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker") | None*[](#keysight.ads.dds.TraceMarker.offset_reference "Link to this definition")
    :   The marker used as a reference for the offset.

    *property* readout\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.TraceMarker.readout_bbox "Link to this definition")

    *property* readout\_content\_properties*: [MarkerReadoutContentProperties](#keysight.ads.dds.MarkerReadoutContentProperties "keysight.ads.dds.core.ddbase.MarkerReadoutContentProperties")*[](#keysight.ads.dds.TraceMarker.readout_content_properties "Link to this definition")

    *property* readout\_fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.TraceMarker.readout_fill_properties "Link to this definition")

    readout\_move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.TraceMarker.readout_move "Link to this definition")

    *property* readout\_outline\_on*: bool*[](#keysight.ads.dds.TraceMarker.readout_outline_on "Link to this definition")

    *property* readout\_text\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.TraceMarker.readout_text_properties "Link to this definition")

    reset\_mode() → None[](#keysight.ads.dds.TraceMarker.reset_mode "Link to this definition")

    set\_delta(*reference\_marker: [TraceMarker](#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker") | str*) → None[](#keysight.ads.dds.TraceMarker.set_delta "Link to this definition")

    set\_offset(*reference\_marker: [TraceMarker](#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker") | str*, *offset\_expr: float | str*) → None[](#keysight.ads.dds.TraceMarker.set_offset "Link to this definition")

    *property* smith\_chart\_format*: MarkerSmithChartFormat*[](#keysight.ads.dds.TraceMarker.smith_chart_format "Link to this definition")

    *property* sweep\_index\_equations\_enabled*: bool*[](#keysight.ads.dds.TraceMarker.sweep_index_equations_enabled "Link to this definition")

    *property* symbol\_properties*: [TraceMarkerSymbolProperties](#keysight.ads.dds.TraceMarkerSymbolProperties "keysight.ads.dds.core.ddplot.TraceMarkerSymbolProperties")*[](#keysight.ads.dds.TraceMarker.symbol_properties "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.TraceMarker.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.TraceMarker.uid "Link to this definition")

    *property* variable*: VariableBlock | None*[](#keysight.ads.dds.TraceMarker.variable "Link to this definition")

*class* keysight.ads.dds.MarkerType[](#keysight.ads.dds.MarkerType "Link to this definition")
:   MAX *= <MarkerType.MAX: 8>*[](#keysight.ads.dds.MarkerType.MAX "Link to this definition")

    MIN *= <MarkerType.MIN: 16>*[](#keysight.ads.dds.MarkerType.MIN "Link to this definition")

    NORMAL *= <MarkerType.NORMAL: 1>*[](#keysight.ads.dds.MarkerType.NORMAL "Link to this definition")

    PEAK *= <MarkerType.PEAK: 2>*[](#keysight.ads.dds.MarkerType.PEAK "Link to this definition")

    VALLEY *= <MarkerType.VALLEY: 4>*[](#keysight.ads.dds.MarkerType.VALLEY "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.MarkerType.str "Link to this definition")

*class* keysight.ads.dds.MarkerMode[](#keysight.ads.dds.MarkerMode "Link to this definition")
:   DELTA *= <MarkerMode.DELTA: 1>*[](#keysight.ads.dds.MarkerMode.DELTA "Link to this definition")

    NORMAL *= <MarkerMode.NORMAL: 0>*[](#keysight.ads.dds.MarkerMode.NORMAL "Link to this definition")

    OFFSET *= <MarkerMode.OFFSET: 2>*[](#keysight.ads.dds.MarkerMode.OFFSET "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.MarkerMode.str "Link to this definition")

*class* keysight.ads.dds.MarkerReadoutContentProperties[](#keysight.ads.dds.MarkerReadoutContentProperties "Link to this definition")
:   \_\_init\_\_(*show\_name: bool | None = None*, *show\_dependent\_value: bool | None = None*, *show\_independent\_value: bool | None = None*, *show\_type: bool | None = None*, *show\_smith\_chart\_value: bool | None = None*, *show\_sweep\_value: bool | None = None*, *move\_with\_plot: bool | None = None*) → None[](#keysight.ads.dds.MarkerReadoutContentProperties.__init__ "Link to this definition")
    :   Create an instance of MarkerReadoutContentProperties.

        Parameters:
        :   * **show\_name** (*bool* *[**optional**,* *default=None**]*) – If True, marker name will be shown.
            * **show\_dependent\_value** (*bool* *[**optional**,* *default=None**]*) – If True, dependent value will be shown.
            * **show\_independent\_value** (*bool* *[**optional**,* *default=None**]*) – If True, independent value will be shown.
            * **show\_type** (*bool* *[**optional**,* *default=None**]*) – If True, marker type will be shown.
            * **show\_smith\_chart\_value** (*bool* *[**optional**,* *default=None**]*) – If True, smith chart value will be shown.
            * **show\_sweep\_value** (*bool* *[**optional**,* *default=None**]*) – If True, sweep value will be shown.
            * **move\_with\_plot** (*bool* *[**optional**,* *default=None**]*) – If True, readout box moves with plot.

    *property* move\_with\_plot*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.move_with_plot "Link to this definition")

    *property* show\_dependent\_value*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_dependent_value "Link to this definition")

    *property* show\_independent\_value*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_independent_value "Link to this definition")

    *property* show\_name*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_name "Link to this definition")

    *property* show\_smith\_chart\_value*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_smith_chart_value "Link to this definition")

    *property* show\_sweep\_value*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_sweep_value "Link to this definition")

    *property* show\_type*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_type "Link to this definition")

*class* keysight.ads.dds.TraceMarkerSymbol[](#keysight.ads.dds.TraceMarkerSymbol "Link to this definition")
:   CIRCLE *= <TraceMarkerSymbol.CIRCLE: 2>*[](#keysight.ads.dds.TraceMarkerSymbol.CIRCLE "Link to this definition")

    TRIANGLE\_EMPTY *= <TraceMarkerSymbol.TRIANGLE\_EMPTY: 1>*[](#keysight.ads.dds.TraceMarkerSymbol.TRIANGLE_EMPTY "Link to this definition")

    TRIANGLE\_FILLED *= <TraceMarkerSymbol.TRIANGLE\_FILLED: 0>*[](#keysight.ads.dds.TraceMarkerSymbol.TRIANGLE_FILLED "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.TraceMarkerSymbol.str "Link to this definition")

*class* keysight.ads.dds.TraceMarkerSymbolProperties[](#keysight.ads.dds.TraceMarkerSymbolProperties "Link to this definition")
:   \_\_init\_\_(*type: [TraceMarkerSymbol](#keysight.ads.dds.TraceMarkerSymbol "keysight.ads.dds.core.ddplot.TraceMarkerSymbol") | str | None = None*, *color: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color") | None = None*, *size: int | None = None*) → None[](#keysight.ads.dds.TraceMarkerSymbolProperties.__init__ "Link to this definition")

    *property* color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.TraceMarkerSymbolProperties.color "Link to this definition")

    *property* size*: int*[](#keysight.ads.dds.TraceMarkerSymbolProperties.size "Link to this definition")

    *property* type*: [TraceMarkerSymbol](#keysight.ads.dds.TraceMarkerSymbol "keysight.ads.dds.core.ddplot.TraceMarkerSymbol") | None*[](#keysight.ads.dds.TraceMarkerSymbolProperties.type "Link to this definition")

On this page

[Previous

Trace](trace.md)
[Next

Line Markers](linemarker.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top