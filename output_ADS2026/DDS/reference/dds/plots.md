<!-- 来源: reference\dds\plots.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Plots

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
    - Plots
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

# Plots[](#plots "Link to this heading")

*class* keysight.ads.dds.AntennaPlot[](#keysight.ads.dds.AntennaPlot "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_antenna_plot()`](page.md#keysight.ads.dds.Page.add_antenna_plot "keysight.ads.dds.Page.add_antenna_plot").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.AntennaPlot.__init__ "Link to this definition")

    activate() → None[](#keysight.ads.dds.AntennaPlot.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.AntennaPlot.add_legend "Link to this definition")

    add\_py\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.AntennaPlot.add_py_trace "Link to this definition")

    add\_py\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.AntennaPlot.add_py_traces "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.AntennaPlot.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.AntennaPlot.add_traces "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.AntennaPlot.bbox "Link to this definition")
    :   The bounding box of the grid of a plot. It does not include markers, axes labels, ticks, or title.

        To obtain the bounding box of plot and all of its associated objects, use [`children_bbox`](#keysight.ads.dds.AntennaPlot.children_bbox "keysight.ads.dds.AntennaPlot.children_bbox").

        Example

        Add two plots the exact same size, side by side.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My First Plot")
        >>> top = plot.bbox.top
        >>> bottom = plot.bbox.bottom
        >>> margin = plot.bbox.left - plot.children_bbox.left
        >>> left = plot.children_bbox.right + margin + 200
        >>> grid_width = plot.bbox.right - plot.bbox.left
        >>> right = left + grid_width
        >>> new_location = dds.Rect(top_left = (left, top),bottom_right = (right, bottom))
        >>> page.add_plot( new_location, ["[0::10]","[10::20]"], "My Second Plot")
        ```

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.AntennaPlot.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.AntennaPlot.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.AntennaPlot.children_bbox "Link to this definition")
    :   The bounding box of a plot that includes grid, markers, axes labels, ticks and title.

        To obtain the bounding box of only the grid, use [`bbox`](#keysight.ads.dds.AntennaPlot.bbox "keysight.ads.dds.AntennaPlot.bbox").

        Examples

        Add a plot and add a frame around that plot.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My Simple Plot")
        >>> page.add_box(plot.children_bbox)
        ```

        Add two plots and ensure they do not overlap. The end result is a smith chart and rect plot side by side, no overlapping.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file("amplifier.ds")
        >>> page = dds_file.pages[0]
        >>> smith_chart = page.add_smith_chart((500,500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>> rect_plot= page.add_plot(smith_chart.children_bbox.adjusted(right = 500, left = 500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>>if rect_plot.children_bbox.left <= smith_chart.children_bbox.right:
        >>>    left = smith_chart.children_bbox.left
        >>>    spacing = 500
        >>>    width_to_move = smith_chart.children_bbox.right - smith_chart.children_bbox.left + spacing
        >>>    new_start_point = dds.Point(rect_plot.bbox.left + width_to_move, 0)
        >>>    rect_plot.move(new_start_point)
        >>> dds_file.save()
        ```

    deactivate() → None[](#keysight.ads.dds.AntennaPlot.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.AntennaPlot.delete_object "Link to this definition")

    *property* dep\_axis*: [AntennaDepAxis](axes.md#keysight.ads.dds.AntennaDepAxis "keysight.ads.dds.core.ddplot.AntennaDepAxis")*[](#keysight.ads.dds.AntennaPlot.dep_axis "Link to this definition")

    *property* indep\_axis*: [AntennaIndepAxis](axes.md#keysight.ads.dds.AntennaIndepAxis "keysight.ads.dds.core.ddplot.AntennaIndepAxis")*[](#keysight.ads.dds.AntennaPlot.indep_axis "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.AntennaPlot.is_deactivated "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.AntennaPlot.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.AntennaPlot.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.AntennaPlot.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.AntennaPlot.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.AntennaPlot.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.AntennaPlot.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.AntennaPlot.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    start\_history(*depth: int | None = None*) → None[](#keysight.ads.dds.AntennaPlot.start_history "Link to this definition")
    :   Enable history mode this plot.

        Parameters:
        :   **depth** (*int* *[**optional**,* *default=None**]*) – The number of history subtraces to maintain for this plot. If not specified,
            the default depth is used.

        Return type:
        :   None

    stop\_history() → None[](#keysight.ads.dds.AntennaPlot.stop_history "Link to this definition")
    :   Disable history mode for this plot.

        Return type:
        :   None

    *property* title*: str | None*[](#keysight.ads.dds.AntennaPlot.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.AntennaPlot.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.AntennaPlot.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.AntennaPlot.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.AntennaPlot.uid "Link to this definition")

*class* keysight.ads.dds.Listing[](#keysight.ads.dds.Listing "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_list()`](page.md#keysight.ads.dds.Page.add_list "keysight.ads.dds.Page.add_list").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.Listing.__init__ "Link to this definition")

    activate() → None[](#keysight.ads.dds.Listing.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.Listing.add_legend "Link to this definition")

    add\_py\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.Listing.add_py_trace "Link to this definition")

    add\_py\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.Listing.add_py_traces "Link to this definition")

    add\_trace(*expression: str*) → [TextTrace](trace.md#keysight.ads.dds.TextTrace "keysight.ads.dds.core.ddplot.TextTrace")[](#keysight.ads.dds.Listing.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[TextTrace](trace.md#keysight.ads.dds.TextTrace "keysight.ads.dds.core.ddplot.TextTrace")][](#keysight.ads.dds.Listing.add_traces "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Listing.bbox "Link to this definition")
    :   The bounding box of the grid of a plot. It does not include markers, axes labels, ticks, or title.

        To obtain the bounding box of plot and all of its associated objects, use [`children_bbox`](#keysight.ads.dds.Listing.children_bbox "keysight.ads.dds.Listing.children_bbox").

        Example

        Add two plots the exact same size, side by side.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My First Plot")
        >>> top = plot.bbox.top
        >>> bottom = plot.bbox.bottom
        >>> margin = plot.bbox.left - plot.children_bbox.left
        >>> left = plot.children_bbox.right + margin + 200
        >>> grid_width = plot.bbox.right - plot.bbox.left
        >>> right = left + grid_width
        >>> new_location = dds.Rect(top_left = (left, top),bottom_right = (right, bottom))
        >>> page.add_plot( new_location, ["[0::10]","[10::20]"], "My Second Plot")
        ```

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Listing.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.Listing.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Listing.children_bbox "Link to this definition")
    :   The bounding box of a plot that includes grid, markers, axes labels, ticks and title.

        To obtain the bounding box of only the grid, use [`bbox`](#keysight.ads.dds.Listing.bbox "keysight.ads.dds.Listing.bbox").

        Examples

        Add a plot and add a frame around that plot.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My Simple Plot")
        >>> page.add_box(plot.children_bbox)
        ```

        Add two plots and ensure they do not overlap. The end result is a smith chart and rect plot side by side, no overlapping.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file("amplifier.ds")
        >>> page = dds_file.pages[0]
        >>> smith_chart = page.add_smith_chart((500,500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>> rect_plot= page.add_plot(smith_chart.children_bbox.adjusted(right = 500, left = 500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>>if rect_plot.children_bbox.left <= smith_chart.children_bbox.right:
        >>>    left = smith_chart.children_bbox.left
        >>>    spacing = 500
        >>>    width_to_move = smith_chart.children_bbox.right - smith_chart.children_bbox.left + spacing
        >>>    new_start_point = dds.Point(rect_plot.bbox.left + width_to_move, 0)
        >>>    rect_plot.move(new_start_point)
        >>> dds_file.save()
        ```

    deactivate() → None[](#keysight.ads.dds.Listing.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.Listing.delete_object "Link to this definition")

    *property* is\_autosized*: bool*[](#keysight.ads.dds.Listing.is_autosized "Link to this definition")

    *property* is\_column\_headings\_displayed*: bool*[](#keysight.ads.dds.Listing.is_column_headings_displayed "Link to this definition")

    *property* is\_data\_transposed*: bool*[](#keysight.ads.dds.Listing.is_data_transposed "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.Listing.is_deactivated "Link to this definition")

    *property* is\_indep\_data\_displayed*: bool*[](#keysight.ads.dds.Listing.is_indep_data_displayed "Link to this definition")

    *property* is\_outlined*: bool*[](#keysight.ads.dds.Listing.is_outlined "Link to this definition")

    *property* is\_table\_format\_suppressed*: bool*[](#keysight.ads.dds.Listing.is_table_format_suppressed "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Listing.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Listing.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Listing.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Listing.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Listing.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Listing.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Listing.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.Listing.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.Listing.string_format "Link to this definition")

    *property* text\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.Listing.text_properties "Link to this definition")

    *property* title*: str | None*[](#keysight.ads.dds.Listing.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.Listing.title_properties "Link to this definition")

    *property* traces*: list[[TextTrace](trace.md#keysight.ads.dds.TextTrace "keysight.ads.dds.core.ddplot.TextTrace")]*[](#keysight.ads.dds.Listing.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Listing.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.Listing.uid "Link to this definition")

*class* keysight.ads.dds.PolarPlot[](#keysight.ads.dds.PolarPlot "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_polar_plot()`](page.md#keysight.ads.dds.Page.add_polar_plot "keysight.ads.dds.Page.add_polar_plot").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.PolarPlot.__init__ "Link to this definition")

    activate() → None[](#keysight.ads.dds.PolarPlot.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.PolarPlot.add_legend "Link to this definition")

    add\_py\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.PolarPlot.add_py_trace "Link to this definition")

    add\_py\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.PolarPlot.add_py_traces "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.PolarPlot.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.PolarPlot.add_traces "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.PolarPlot.bbox "Link to this definition")
    :   The bounding box of the grid of a plot. It does not include markers, axes labels, ticks, or title.

        To obtain the bounding box of plot and all of its associated objects, use [`children_bbox`](#keysight.ads.dds.PolarPlot.children_bbox "keysight.ads.dds.PolarPlot.children_bbox").

        Example

        Add two plots the exact same size, side by side.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My First Plot")
        >>> top = plot.bbox.top
        >>> bottom = plot.bbox.bottom
        >>> margin = plot.bbox.left - plot.children_bbox.left
        >>> left = plot.children_bbox.right + margin + 200
        >>> grid_width = plot.bbox.right - plot.bbox.left
        >>> right = left + grid_width
        >>> new_location = dds.Rect(top_left = (left, top),bottom_right = (right, bottom))
        >>> page.add_plot( new_location, ["[0::10]","[10::20]"], "My Second Plot")
        ```

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.PolarPlot.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.PolarPlot.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.PolarPlot.children_bbox "Link to this definition")
    :   The bounding box of a plot that includes grid, markers, axes labels, ticks and title.

        To obtain the bounding box of only the grid, use [`bbox`](#keysight.ads.dds.PolarPlot.bbox "keysight.ads.dds.PolarPlot.bbox").

        Examples

        Add a plot and add a frame around that plot.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My Simple Plot")
        >>> page.add_box(plot.children_bbox)
        ```

        Add two plots and ensure they do not overlap. The end result is a smith chart and rect plot side by side, no overlapping.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file("amplifier.ds")
        >>> page = dds_file.pages[0]
        >>> smith_chart = page.add_smith_chart((500,500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>> rect_plot= page.add_plot(smith_chart.children_bbox.adjusted(right = 500, left = 500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>>if rect_plot.children_bbox.left <= smith_chart.children_bbox.right:
        >>>    left = smith_chart.children_bbox.left
        >>>    spacing = 500
        >>>    width_to_move = smith_chart.children_bbox.right - smith_chart.children_bbox.left + spacing
        >>>    new_start_point = dds.Point(rect_plot.bbox.left + width_to_move, 0)
        >>>    rect_plot.move(new_start_point)
        >>> dds_file.save()
        ```

    deactivate() → None[](#keysight.ads.dds.PolarPlot.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.PolarPlot.delete_object "Link to this definition")

    *property* dep\_axis*: [PolarDepAxis](axes.md#keysight.ads.dds.PolarDepAxis "keysight.ads.dds.core.ddplot.PolarDepAxis")*[](#keysight.ads.dds.PolarPlot.dep_axis "Link to this definition")

    *property* indep\_axis*: [PolarIndepAxis](axes.md#keysight.ads.dds.PolarIndepAxis "keysight.ads.dds.core.ddplot.PolarIndepAxis")*[](#keysight.ads.dds.PolarPlot.indep_axis "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.PolarPlot.is_deactivated "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.PolarPlot.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.PolarPlot.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.PolarPlot.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.PolarPlot.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.PolarPlot.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.PolarPlot.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.PolarPlot.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    start\_history(*depth: int | None = None*) → None[](#keysight.ads.dds.PolarPlot.start_history "Link to this definition")
    :   Enable history mode this plot.

        Parameters:
        :   **depth** (*int* *[**optional**,* *default=None**]*) – The number of history subtraces to maintain for this plot. If not specified,
            the default depth is used.

        Return type:
        :   None

    stop\_history() → None[](#keysight.ads.dds.PolarPlot.stop_history "Link to this definition")
    :   Disable history mode for this plot.

        Return type:
        :   None

    *property* title*: str | None*[](#keysight.ads.dds.PolarPlot.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.PolarPlot.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.PolarPlot.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.PolarPlot.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.PolarPlot.uid "Link to this definition")

*class* keysight.ads.dds.RectPlot[](#keysight.ads.dds.RectPlot "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_plot()`](page.md#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.RectPlot.__init__ "Link to this definition")

    activate() → None[](#keysight.ads.dds.RectPlot.activate "Link to this definition")

    add\_axis(*name: str*, *orientation: [AxisOrientation](axes.md#keysight.ads.dds.AxisOrientation "keysight.ads.dds.core.ddplot.AxisOrientation")*) → [RectAxis](axes.md#keysight.ads.dds.RectAxis "keysight.ads.dds.core.ddplot.RectAxis")[](#keysight.ads.dds.RectPlot.add_axis "Link to this definition")

    add\_greater\_than\_limit\_line(*name: str*, *x1: float | str*, *x2: float | str*, *y: float | str*) → [LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.core.ddplot.LimitLine")[](#keysight.ads.dds.RectPlot.add_greater_than_limit_line "Link to this definition")

    add\_inside\_limit\_line(*name: str*, *x1: float | str | None = None*, *y1: float | str | None = None*, *x2: float | str | None = None*, *y2: float | str | None = None*, *pt1: tuple[float | str, float | str] | None = None*, *pt2: tuple[float | str, float | str] | None = None*) → [LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.core.ddplot.LimitLine")[](#keysight.ads.dds.RectPlot.add_inside_limit_line "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.RectPlot.add_legend "Link to this definition")

    add\_less\_than\_limit\_line(*name: str*, *x1: float | str*, *x2: float | str*, *y: float | str*) → [LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.core.ddplot.LimitLine")[](#keysight.ads.dds.RectPlot.add_less_than_limit_line "Link to this definition")

    add\_line\_marker(*name: str*, *independent\_value: str | float*) → [LineMarker](linemarker.md#keysight.ads.dds.LineMarker "keysight.ads.dds.core.ddplot.LineMarker")[](#keysight.ads.dds.RectPlot.add_line_marker "Link to this definition")

    add\_line\_mask(*name: str*, *pt1: tuple[float | str, float | str]*, *pt2: tuple[float | str, float | str]*) → [LineMask](masks.md#keysight.ads.dds.LineMask "keysight.ads.dds.core.ddplot.LineMask")[](#keysight.ads.dds.RectPlot.add_line_mask "Link to this definition")

    add\_outside\_limit\_line(*name: str*, *x1: float | str | None = None*, *y1: float | str | None = None*, *x2: float | str | None = None*, *y2: float | str | None = None*, *pt1: tuple[float | str, float | str] | None = None*, *pt2: tuple[float | str, float | str] | None = None*) → [LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.core.ddplot.LimitLine")[](#keysight.ads.dds.RectPlot.add_outside_limit_line "Link to this definition")

    add\_polygon\_mask(*name: str*, *points: list[tuple[float | str, float | str]]*) → [PolygonMask](masks.md#keysight.ads.dds.PolygonMask "keysight.ads.dds.core.ddplot.PolygonMask")[](#keysight.ads.dds.RectPlot.add_polygon_mask "Link to this definition")

    add\_polyline\_mask(*name: str*, *points: list[tuple[float | str, float | str]]*) → [PolylineMask](masks.md#keysight.ads.dds.PolylineMask "keysight.ads.dds.core.ddplot.PolylineMask")[](#keysight.ads.dds.RectPlot.add_polyline_mask "Link to this definition")

    add\_py\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.RectPlot.add_py_trace "Link to this definition")

    add\_py\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.RectPlot.add_py_traces "Link to this definition")

    add\_rectangle\_mask(*name: str*, *x1: float | str | None = None*, *y1: float | str | None = None*, *x2: float | str | None = None*, *y2: float | str | None = None*, *pt1: tuple[float | str, float | str] | None = None*, *pt2: tuple[float | str, float | str] | None = None*) → [RectMask](masks.md#keysight.ads.dds.RectMask "keysight.ads.dds.core.ddplot.RectMask")[](#keysight.ads.dds.RectPlot.add_rectangle_mask "Link to this definition")

    add\_specification(*name: str*, *objs: list[PlotGraphicalObject]*) → [Specification](specifications.md#keysight.ads.dds.Specification "keysight.ads.dds.core.ddplot.Specification")[](#keysight.ads.dds.RectPlot.add_specification "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.RectPlot.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.RectPlot.add_traces "Link to this definition")

    *property* axes*: NamedItemCollectionAbc[[RectAxis](axes.md#keysight.ads.dds.RectAxis "keysight.ads.dds.core.ddplot.RectAxis")]*[](#keysight.ads.dds.RectPlot.axes "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.RectPlot.bbox "Link to this definition")
    :   The bounding box of the grid of a plot. It does not include markers, axes labels, ticks, or title.

        To obtain the bounding box of plot and all of its associated objects, use [`children_bbox`](#keysight.ads.dds.RectPlot.children_bbox "keysight.ads.dds.RectPlot.children_bbox").

        Example

        Add two plots the exact same size, side by side.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My First Plot")
        >>> top = plot.bbox.top
        >>> bottom = plot.bbox.bottom
        >>> margin = plot.bbox.left - plot.children_bbox.left
        >>> left = plot.children_bbox.right + margin + 200
        >>> grid_width = plot.bbox.right - plot.bbox.left
        >>> right = left + grid_width
        >>> new_location = dds.Rect(top_left = (left, top),bottom_right = (right, bottom))
        >>> page.add_plot( new_location, ["[0::10]","[10::20]"], "My Second Plot")
        ```

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.RectPlot.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.RectPlot.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.RectPlot.children_bbox "Link to this definition")
    :   The bounding box of a plot that includes grid, markers, axes labels, ticks and title.

        To obtain the bounding box of only the grid, use [`bbox`](#keysight.ads.dds.RectPlot.bbox "keysight.ads.dds.RectPlot.bbox").

        Examples

        Add a plot and add a frame around that plot.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My Simple Plot")
        >>> page.add_box(plot.children_bbox)
        ```

        Add two plots and ensure they do not overlap. The end result is a smith chart and rect plot side by side, no overlapping.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file("amplifier.ds")
        >>> page = dds_file.pages[0]
        >>> smith_chart = page.add_smith_chart((500,500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>> rect_plot= page.add_plot(smith_chart.children_bbox.adjusted(right = 500, left = 500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>>if rect_plot.children_bbox.left <= smith_chart.children_bbox.right:
        >>>    left = smith_chart.children_bbox.left
        >>>    spacing = 500
        >>>    width_to_move = smith_chart.children_bbox.right - smith_chart.children_bbox.left + spacing
        >>>    new_start_point = dds.Point(rect_plot.bbox.left + width_to_move, 0)
        >>>    rect_plot.move(new_start_point)
        >>> dds_file.save()
        ```

    deactivate() → None[](#keysight.ads.dds.RectPlot.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.RectPlot.delete_object "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.RectPlot.is_deactivated "Link to this definition")

    *property* limit\_lines*: list[[LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.core.ddplot.LimitLine")]*[](#keysight.ads.dds.RectPlot.limit_lines "Link to this definition")

    *property* line\_markers*: NamedItemCollectionAbc[[LineMarker](linemarker.md#keysight.ads.dds.LineMarker "keysight.ads.dds.core.ddplot.LineMarker")]*[](#keysight.ads.dds.RectPlot.line_markers "Link to this definition")

    *property* masks*: list[Mask]*[](#keysight.ads.dds.RectPlot.masks "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.RectPlot.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.RectPlot.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.RectPlot.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.RectPlot.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.RectPlot.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.RectPlot.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.RectPlot.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    remove\_specification(*spec: [Specification](specifications.md#keysight.ads.dds.Specification "keysight.ads.dds.core.ddplot.Specification")*) → None[](#keysight.ads.dds.RectPlot.remove_specification "Link to this definition")

    *property* specifications*: NamedItemCollectionAbc[[Specification](specifications.md#keysight.ads.dds.Specification "keysight.ads.dds.core.ddplot.Specification")]*[](#keysight.ads.dds.RectPlot.specifications "Link to this definition")

    start\_history(*depth: int | None = None*) → None[](#keysight.ads.dds.RectPlot.start_history "Link to this definition")
    :   Enable history mode this plot.

        Parameters:
        :   **depth** (*int* *[**optional**,* *default=None**]*) – The number of history subtraces to maintain for this plot. If not specified,
            the default depth is used.

        Return type:
        :   None

    stop\_history() → None[](#keysight.ads.dds.RectPlot.stop_history "Link to this definition")
    :   Disable history mode for this plot.

        Return type:
        :   None

    *property* title*: str | None*[](#keysight.ads.dds.RectPlot.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.RectPlot.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.RectPlot.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.RectPlot.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.RectPlot.uid "Link to this definition")

*class* keysight.ads.dds.Slider[](#keysight.ads.dds.Slider "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_slider()`](page.md#keysight.ads.dds.Page.add_slider "keysight.ads.dds.Page.add_slider").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.Slider.__init__ "Link to this definition")

    activate() → None[](#keysight.ads.dds.Slider.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.Slider.add_legend "Link to this definition")

    add\_py\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.Slider.add_py_trace "Link to this definition")

    add\_py\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.Slider.add_py_traces "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.Slider.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.Slider.add_traces "Link to this definition")

    *property* axes*: NamedItemCollectionAbc[[RectAxis](axes.md#keysight.ads.dds.RectAxis "keysight.ads.dds.core.ddplot.RectAxis")]*[](#keysight.ads.dds.Slider.axes "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Slider.bbox "Link to this definition")
    :   The bounding box of the grid of a plot. It does not include markers, axes labels, ticks, or title.

        To obtain the bounding box of plot and all of its associated objects, use [`children_bbox`](#keysight.ads.dds.Slider.children_bbox "keysight.ads.dds.Slider.children_bbox").

        Example

        Add two plots the exact same size, side by side.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My First Plot")
        >>> top = plot.bbox.top
        >>> bottom = plot.bbox.bottom
        >>> margin = plot.bbox.left - plot.children_bbox.left
        >>> left = plot.children_bbox.right + margin + 200
        >>> grid_width = plot.bbox.right - plot.bbox.left
        >>> right = left + grid_width
        >>> new_location = dds.Rect(top_left = (left, top),bottom_right = (right, bottom))
        >>> page.add_plot( new_location, ["[0::10]","[10::20]"], "My Second Plot")
        ```

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Slider.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.Slider.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Slider.children_bbox "Link to this definition")
    :   The bounding box of a plot that includes grid, markers, axes labels, ticks and title.

        To obtain the bounding box of only the grid, use [`bbox`](#keysight.ads.dds.Slider.bbox "keysight.ads.dds.Slider.bbox").

        Examples

        Add a plot and add a frame around that plot.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My Simple Plot")
        >>> page.add_box(plot.children_bbox)
        ```

        Add two plots and ensure they do not overlap. The end result is a smith chart and rect plot side by side, no overlapping.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file("amplifier.ds")
        >>> page = dds_file.pages[0]
        >>> smith_chart = page.add_smith_chart((500,500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>> rect_plot= page.add_plot(smith_chart.children_bbox.adjusted(right = 500, left = 500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>>if rect_plot.children_bbox.left <= smith_chart.children_bbox.right:
        >>>    left = smith_chart.children_bbox.left
        >>>    spacing = 500
        >>>    width_to_move = smith_chart.children_bbox.right - smith_chart.children_bbox.left + spacing
        >>>    new_start_point = dds.Point(rect_plot.bbox.left + width_to_move, 0)
        >>>    rect_plot.move(new_start_point)
        >>> dds_file.save()
        ```

    deactivate() → None[](#keysight.ads.dds.Slider.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.Slider.delete_object "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.Slider.is_deactivated "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Slider.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Slider.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Slider.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Slider.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Slider.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Slider.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.Slider.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    *property* title*: str | None*[](#keysight.ads.dds.Slider.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.Slider.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.Slider.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Slider.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.Slider.uid "Link to this definition")

*class* keysight.ads.dds.SmithChart[](#keysight.ads.dds.SmithChart "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_smith_chart()`](page.md#keysight.ads.dds.Page.add_smith_chart "keysight.ads.dds.Page.add_smith_chart").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.SmithChart.__init__ "Link to this definition")

    activate() → None[](#keysight.ads.dds.SmithChart.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.SmithChart.add_legend "Link to this definition")

    add\_py\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.SmithChart.add_py_trace "Link to this definition")

    add\_py\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.SmithChart.add_py_traces "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.SmithChart.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.SmithChart.add_traces "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.SmithChart.bbox "Link to this definition")
    :   The bounding box of the grid of a plot. It does not include markers, axes labels, ticks, or title.

        To obtain the bounding box of plot and all of its associated objects, use [`children_bbox`](#keysight.ads.dds.SmithChart.children_bbox "keysight.ads.dds.SmithChart.children_bbox").

        Example

        Add two plots the exact same size, side by side.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My First Plot")
        >>> top = plot.bbox.top
        >>> bottom = plot.bbox.bottom
        >>> margin = plot.bbox.left - plot.children_bbox.left
        >>> left = plot.children_bbox.right + margin + 200
        >>> grid_width = plot.bbox.right - plot.bbox.left
        >>> right = left + grid_width
        >>> new_location = dds.Rect(top_left = (left, top),bottom_right = (right, bottom))
        >>> page.add_plot( new_location, ["[0::10]","[10::20]"], "My Second Plot")
        ```

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.SmithChart.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.SmithChart.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.SmithChart.children_bbox "Link to this definition")
    :   The bounding box of a plot that includes grid, markers, axes labels, ticks and title.

        To obtain the bounding box of only the grid, use [`bbox`](#keysight.ads.dds.SmithChart.bbox "keysight.ads.dds.SmithChart.bbox").

        Examples

        Add a plot and add a frame around that plot.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My Simple Plot")
        >>> page.add_box(plot.children_bbox)
        ```

        Add two plots and ensure they do not overlap. The end result is a smith chart and rect plot side by side, no overlapping.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file("amplifier.ds")
        >>> page = dds_file.pages[0]
        >>> smith_chart = page.add_smith_chart((500,500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>> rect_plot= page.add_plot(smith_chart.children_bbox.adjusted(right = 500, left = 500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>>if rect_plot.children_bbox.left <= smith_chart.children_bbox.right:
        >>>    left = smith_chart.children_bbox.left
        >>>    spacing = 500
        >>>    width_to_move = smith_chart.children_bbox.right - smith_chart.children_bbox.left + spacing
        >>>    new_start_point = dds.Point(rect_plot.bbox.left + width_to_move, 0)
        >>>    rect_plot.move(new_start_point)
        >>> dds_file.save()
        ```

    deactivate() → None[](#keysight.ads.dds.SmithChart.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.SmithChart.delete_object "Link to this definition")

    *property* dep\_axis*: [SmithChartDepAxis](axes.md#keysight.ads.dds.SmithChartDepAxis "keysight.ads.dds.core.ddplot.SmithChartDepAxis")*[](#keysight.ads.dds.SmithChart.dep_axis "Link to this definition")

    *property* indep\_axis*: [SmithChartIndepAxis](axes.md#keysight.ads.dds.SmithChartIndepAxis "keysight.ads.dds.core.ddplot.SmithChartIndepAxis")*[](#keysight.ads.dds.SmithChart.indep_axis "Link to this definition")

    *property* is\_admittance\_displayed*: bool*[](#keysight.ads.dds.SmithChart.is_admittance_displayed "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.SmithChart.is_deactivated "Link to this definition")

    *property* is\_impedance\_displayed*: bool*[](#keysight.ads.dds.SmithChart.is_impedance_displayed "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.SmithChart.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.SmithChart.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.SmithChart.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.SmithChart.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.SmithChart.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.SmithChart.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.SmithChart.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    start\_history(*depth: int | None = None*) → None[](#keysight.ads.dds.SmithChart.start_history "Link to this definition")
    :   Enable history mode this plot.

        Parameters:
        :   **depth** (*int* *[**optional**,* *default=None**]*) – The number of history subtraces to maintain for this plot. If not specified,
            the default depth is used.

        Return type:
        :   None

    stop\_history() → None[](#keysight.ads.dds.SmithChart.stop_history "Link to this definition")
    :   Disable history mode for this plot.

        Return type:
        :   None

    *property* title*: str | None*[](#keysight.ads.dds.SmithChart.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.SmithChart.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.SmithChart.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.SmithChart.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.SmithChart.uid "Link to this definition")

*class* keysight.ads.dds.StackedPlot[](#keysight.ads.dds.StackedPlot "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_stacked_plot()`](page.md#keysight.ads.dds.Page.add_stacked_plot "keysight.ads.dds.Page.add_stacked_plot").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.StackedPlot.__init__ "Link to this definition")

    activate() → None[](#keysight.ads.dds.StackedPlot.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.StackedPlot.add_legend "Link to this definition")

    add\_line\_marker(*name: str*, *independent\_value: str*) → [LineMarker](linemarker.md#keysight.ads.dds.LineMarker "keysight.ads.dds.core.ddplot.LineMarker")[](#keysight.ads.dds.StackedPlot.add_line_marker "Link to this definition")

    add\_py\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.StackedPlot.add_py_trace "Link to this definition")

    add\_py\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.StackedPlot.add_py_traces "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.StackedPlot.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.StackedPlot.add_traces "Link to this definition")

    *property* axes*: list[[RectAxis](axes.md#keysight.ads.dds.RectAxis "keysight.ads.dds.core.ddplot.RectAxis")]*[](#keysight.ads.dds.StackedPlot.axes "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.StackedPlot.bbox "Link to this definition")
    :   The bounding box of the grid of a plot. It does not include markers, axes labels, ticks, or title.

        To obtain the bounding box of plot and all of its associated objects, use [`children_bbox`](#keysight.ads.dds.StackedPlot.children_bbox "keysight.ads.dds.StackedPlot.children_bbox").

        Example

        Add two plots the exact same size, side by side.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My First Plot")
        >>> top = plot.bbox.top
        >>> bottom = plot.bbox.bottom
        >>> margin = plot.bbox.left - plot.children_bbox.left
        >>> left = plot.children_bbox.right + margin + 200
        >>> grid_width = plot.bbox.right - plot.bbox.left
        >>> right = left + grid_width
        >>> new_location = dds.Rect(top_left = (left, top),bottom_right = (right, bottom))
        >>> page.add_plot( new_location, ["[0::10]","[10::20]"], "My Second Plot")
        ```

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.StackedPlot.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.StackedPlot.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.StackedPlot.children_bbox "Link to this definition")
    :   The bounding box of a plot that includes grid, markers, axes labels, ticks and title.

        To obtain the bounding box of only the grid, use [`bbox`](#keysight.ads.dds.StackedPlot.bbox "keysight.ads.dds.StackedPlot.bbox").

        Examples

        Add a plot and add a frame around that plot.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot((500, 500), ["[0::10]","[10::20]"], "My Simple Plot")
        >>> page.add_box(plot.children_bbox)
        ```

        Add two plots and ensure they do not overlap. The end result is a smith chart and rect plot side by side, no overlapping.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file("amplifier.ds")
        >>> page = dds_file.pages[0]
        >>> smith_chart = page.add_smith_chart((500,500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>> rect_plot= page.add_plot(smith_chart.children_bbox.adjusted(right = 500, left = 500), ["dB(S11)", "dB(S12)","dB(S21)", "dB(S12)"])
        >>>if rect_plot.children_bbox.left <= smith_chart.children_bbox.right:
        >>>    left = smith_chart.children_bbox.left
        >>>    spacing = 500
        >>>    width_to_move = smith_chart.children_bbox.right - smith_chart.children_bbox.left + spacing
        >>>    new_start_point = dds.Point(rect_plot.bbox.left + width_to_move, 0)
        >>>    rect_plot.move(new_start_point)
        >>> dds_file.save()
        ```

    deactivate() → None[](#keysight.ads.dds.StackedPlot.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.StackedPlot.delete_object "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.StackedPlot.is_deactivated "Link to this definition")

    *property* line\_markers*: NamedItemCollectionAbc[[LineMarker](linemarker.md#keysight.ads.dds.LineMarker "keysight.ads.dds.core.ddplot.LineMarker")]*[](#keysight.ads.dds.StackedPlot.line_markers "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.StackedPlot.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.StackedPlot.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.StackedPlot.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.StackedPlot.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.StackedPlot.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.StackedPlot.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.StackedPlot.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    start\_history(*depth: int | None = None*) → None[](#keysight.ads.dds.StackedPlot.start_history "Link to this definition")
    :   Enable history mode this plot.

        Parameters:
        :   **depth** (*int* *[**optional**,* *default=None**]*) – The number of history subtraces to maintain for this plot. If not specified,
            the default depth is used.

        Return type:
        :   None

    stop\_history() → None[](#keysight.ads.dds.StackedPlot.stop_history "Link to this definition")
    :   Disable history mode for this plot.

        Return type:
        :   None

    *property* title*: str | None*[](#keysight.ads.dds.StackedPlot.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.StackedPlot.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.StackedPlot.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.StackedPlot.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.StackedPlot.uid "Link to this definition")

On this page

[Previous

Grid](grid.md)
[Next

Axes](axes.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top