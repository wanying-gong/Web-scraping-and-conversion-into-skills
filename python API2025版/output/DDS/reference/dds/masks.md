<!-- 来源: reference\dds\masks.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Masks

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
    - [Trace](trace.md)
    - [Markers](marker.md)
    - [Line Markers](linemarker.md)
    - [Limit Lines](limitlines.md)
    - Masks
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

# Masks[](#masks "Link to this heading")

*class* keysight.ads.dds.LineMask[](#keysight.ads.dds.LineMask "Link to this definition")
:   Line mask on a plot.

    This class cannot be instantiated directly.
    An instance is created by [`RectPlot.add_line_mask()`](plots.md#keysight.ads.dds.RectPlot.add_line_mask "keysight.ads.dds.RectPlot.add_line_mask").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.LineMask.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* data\_points*: list[tuple[float | str, float | str]]*[](#keysight.ads.dds.LineMask.data_points "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.LineMask.delete_object "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.LineMask.dep_axis "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.LineMask.indep_axis "Link to this definition")

    *property* is\_locked*: bool*[](#keysight.ads.dds.LineMask.is_locked "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.LineMask.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.LineMask.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.LineMask.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.LineMask.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.LineMask.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.LineMask.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.LineMask.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.LineMask.type "Link to this definition")

*class* keysight.ads.dds.PolygonMask[](#keysight.ads.dds.PolygonMask "Link to this definition")
:   Polygon mask on a plot.

    This class cannot be instantiated directly.
    An instance is created by [`RectPlot.add_polygon_mask()`](plots.md#keysight.ads.dds.RectPlot.add_polygon_mask "keysight.ads.dds.RectPlot.add_polygon_mask").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.PolygonMask.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* data\_points*: list[tuple[float | str, float | str]]*[](#keysight.ads.dds.PolygonMask.data_points "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.PolygonMask.delete_object "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.PolygonMask.dep_axis "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.PolygonMask.fill_properties "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.PolygonMask.indep_axis "Link to this definition")

    *property* is\_locked*: bool*[](#keysight.ads.dds.PolygonMask.is_locked "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.PolygonMask.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.PolygonMask.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.PolygonMask.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.PolygonMask.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.PolygonMask.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.PolygonMask.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.PolygonMask.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.PolygonMask.type "Link to this definition")

*class* keysight.ads.dds.PolylineMask[](#keysight.ads.dds.PolylineMask "Link to this definition")
:   Polyline mask on a plot.

    This class cannot be instantiated directly.
    An instance is created by [`RectPlot.add_polyline_mask()`](plots.md#keysight.ads.dds.RectPlot.add_polyline_mask "keysight.ads.dds.RectPlot.add_polyline_mask").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.PolylineMask.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* data\_points*: list[tuple[float | str, float | str]]*[](#keysight.ads.dds.PolylineMask.data_points "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.PolylineMask.delete_object "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.PolylineMask.dep_axis "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.PolylineMask.indep_axis "Link to this definition")

    *property* is\_locked*: bool*[](#keysight.ads.dds.PolylineMask.is_locked "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.PolylineMask.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.PolylineMask.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.PolylineMask.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.PolylineMask.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.PolylineMask.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.PolylineMask.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.PolylineMask.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.PolylineMask.type "Link to this definition")

*class* keysight.ads.dds.RectMask[](#keysight.ads.dds.RectMask "Link to this definition")
:   Rectangle mask on a plot.

    This class cannot be instantiated directly.
    An instance is created by [`RectPlot.add_rectangle_mask()`](plots.md#keysight.ads.dds.RectPlot.add_rectangle_mask "keysight.ads.dds.RectPlot.add_rectangle_mask").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.RectMask.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* data\_points*: list[tuple[float | str, float | str]]*[](#keysight.ads.dds.RectMask.data_points "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.RectMask.delete_object "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.RectMask.dep_axis "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.RectMask.fill_properties "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.RectMask.indep_axis "Link to this definition")

    *property* is\_locked*: bool*[](#keysight.ads.dds.RectMask.is_locked "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.RectMask.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.RectMask.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.RectMask.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.RectMask.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.RectMask.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.RectMask.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.RectMask.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.RectMask.type "Link to this definition")

On this page

[Previous

Limit Lines](limitlines.md)
[Next

Specification](specifications.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top