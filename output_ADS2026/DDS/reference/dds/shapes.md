<!-- 来源: reference\dds\shapes.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Shapes

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
    - Shapes
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

# Shapes[](#shapes "Link to this heading")

*class* keysight.ads.dds.Box[](#keysight.ads.dds.Box "Link to this definition")
:   A simple box on a page.

    This class cannot be instantiated directly. See [`Page.add_box()`](page.md#keysight.ads.dds.Page.add_box "keysight.ads.dds.Page.add_box").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.Box.__init__ "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Box.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Box.delete_object "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.Box.fill_properties "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Box.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Box.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Box.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Box.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Box.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Box.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Box.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Box.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.Box.uid "Link to this definition")

*class* keysight.ads.dds.Circle[](#keysight.ads.dds.Circle "Link to this definition")
:   A simple circle on a page.

    This class cannot be instantiated directly. See [`Page.add_circle()`](page.md#keysight.ads.dds.Page.add_circle "keysight.ads.dds.Page.add_circle").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.Circle.__init__ "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Circle.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* center*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Circle.center "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.Circle.delete_object "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.Circle.fill_properties "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Circle.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Circle.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Circle.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Circle.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Circle.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Circle.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Circle.name "Link to this definition")

    *property* radius*: int*[](#keysight.ads.dds.Circle.radius "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Circle.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.Circle.uid "Link to this definition")

*class* keysight.ads.dds.Line[](#keysight.ads.dds.Line "Link to this definition")
:   A simple line on a page.

    This class cannot be instantiated directly. See [`Page.add_line()`](page.md#keysight.ads.dds.Page.add_line "keysight.ads.dds.Page.add_line").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.Line.__init__ "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Line.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Line.delete_object "Link to this definition")

    *property* end*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Line.end "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Line.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Line.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Line.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Line.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Line.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Line.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Line.name "Link to this definition")

    *property* start*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Line.start "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Line.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.Line.uid "Link to this definition")

*class* keysight.ads.dds.Polyline[](#keysight.ads.dds.Polyline "Link to this definition")
:   A simple polyline on a page.

    This class cannot be instantiated directly. See [`Page.add_polyline()`](page.md#keysight.ads.dds.Page.add_polyline "keysight.ads.dds.Page.add_polyline").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.Polyline.__init__ "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Polyline.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Polyline.delete_object "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Polyline.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Polyline.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Polyline.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Polyline.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Polyline.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Polyline.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Polyline.name "Link to this definition")

    *property* points*: list[[Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")]*[](#keysight.ads.dds.Polyline.points "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Polyline.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.Polyline.uid "Link to this definition")

*class* keysight.ads.dds.Polygon[](#keysight.ads.dds.Polygon "Link to this definition")
:   A simple polygon on a page.

    This class cannot be instantiated directly. See [`Page.add_polygon()`](page.md#keysight.ads.dds.Page.add_polygon "keysight.ads.dds.Page.add_polygon").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.Polygon.__init__ "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Polygon.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Polygon.delete_object "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.Polygon.fill_properties "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Polygon.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Polygon.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Polygon.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Polygon.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Polygon.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Polygon.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Polygon.name "Link to this definition")

    *property* points*: list[[Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")]*[](#keysight.ads.dds.Polygon.points "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Polygon.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.Polygon.uid "Link to this definition")

On this page

[Previous

Picture](picture.md)
[Next

Group](group.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top