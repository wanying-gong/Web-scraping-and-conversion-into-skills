<!-- 来源: reference\dds\page.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Page

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
    - Page
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

# Page[](#page "Link to this heading")

*class* keysight.ads.dds.Page[](#keysight.ads.dds.Page "Link to this definition")
:   A page is an area to organize Data Display objects that can be viewed in windows.

    This class cannot be instantiated directly. When a Data Display file is created, a page is
    automatically created. Additional pages can be created with [`DDSFile.new_page()`](file.md#keysight.ads.dds.DDSFile.new_page "keysight.ads.dds.DDSFile.new_page").
    Pages can be access by the property [`DDSFile.pages`](file.md#keysight.ads.dds.DDSFile.pages "keysight.ads.dds.DDSFile.pages")

    Data Display objects that can be inserted into a page include plots, equations, shapes,
    pictures, text, widgets, and groups.

    Example

    Access default page of a DDSFile.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> default_page = ddsfile.pages[0]
    ```

    Create a new page in a DDSFile.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> myPage = ddsfile.new_page("myPage")
    >>> print(ddsfile.pages)
        (<Page "myPage">, <Page "page 1">)
    >>> ddfile.save()
    ```

    add\_antenna\_plot(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [AntennaPlot](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.core.ddplot.AntennaPlot")[](#keysight.ads.dds.Page.add_antenna_plot "Link to this definition")
    :   Add an antenna plot to the page,.

        It is the same as [`add_plot()`](#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot") except that it returns an antenna plot.

    add\_box(*rect: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → [Box](shapes.md#keysight.ads.dds.Box "keysight.ads.dds.core.ddshape.Box")[](#keysight.ads.dds.Page.add_box "Link to this definition")
    :   Add a box to the page.

        Parameters:
        :   **rect** ([*Rect*](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – Coordinates of the box.

        Returns:
        :   Returns the box placed on the page.

        Return type:
        :   [Box](shapes.md#keysight.ads.dds.Box "keysight.ads.dds.Box")

        Example

        Insert a box.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> tl = dds.Point(500, 500)
        >>> br = dds.Point(1500, 1500)
        >>> obj = page.add_box(dds.Rect(top_left=tl, bottom_right=br))
        ```

    add\_circle(*center: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*, *radius: int*) → [Circle](shapes.md#keysight.ads.dds.Circle "keysight.ads.dds.core.ddshape.Circle")[](#keysight.ads.dds.Page.add_circle "Link to this definition")
    :   Add a circle to the page.

        Parameters:
        :   * **center** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]*) – Coordinates of the center of the circle.
            * **radius** (*int*) – Specifies the radius of the circle.

        Returns:
        :   Returns the circle placed on the page.

        Return type:
        :   [Circle](shapes.md#keysight.ads.dds.Circle "keysight.ads.dds.Circle")

        Example

        Insert a circle.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> center = dds.Point(500, 500)
        >>> obj = page.add_circle(center, 100)
        ```

    add\_equation(*name: str*, *value: str*, */*, *location: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*) → [Equation](equation.md#keysight.ads.dds.Equation "keysight.ads.dds.core.ddshape.Equation")[](#keysight.ads.dds.Page.add_equation "Link to this definition")

    add\_equation(*expression: str*, *location: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, */*) → [Equation](equation.md#keysight.ads.dds.Equation "keysight.ads.dds.core.ddshape.Equation")
    :   Add an equation to the page.

        Parameters:
        :   * **expression\_or\_name** (*name - str**,* *value -str* *|* *expressions : str*) – An expression can be specified by two strings, e.g. “x” and “S11”, or by one string, e.g. “x = S11”
            * **Location** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]* *[**optional**,* *default = None**]*) – Coordinates of where to place the equation on the page.
              If a Point or tuple[int,int] is passed, the top\_left corner of the equation will be placed at that location.
              If omitted, the equation is placed in an empty spot on the page.
              The location of the equation may be moved to a different location with the method [`Equation.move()`](equation.md#keysight.ads.dds.Equation.move "keysight.ads.dds.Equation.move").

        Returns:
        :   Returns the equation placed on the page.

        Return type:
        :   [Equation](equation.md#keysight.ads.dds.Equation "keysight.ads.dds.Equation")

        Raises:
        :   **RuntimeError: The equation must contain a name and value separated by an = sign.** – This occurs when only 1 string parameter is passed that does not contain a full expression.

        Example

        Insert equations.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> page = dds_file.pages[0]
        >>> equ1 = page.add_equation("x", "S11")
        >>> print(equ1)
            <UserExpression "x=S11">
        >>> equ2 = page.add_equation("y = S12",(100,100))
        >>> print(equ2)
            <UserExpression "y=S12">
        >>> dds_file.save()
        ```

    add\_group(*objs: list[GraphicalObject]*) → [Group](group.md#keysight.ads.dds.Group "keysight.ads.dds.core.ddshape.Group")[](#keysight.ads.dds.Page.add_group "Link to this definition")
    :   Add a group to the page.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Returns:
        :   Returns the group that contains the specified objects.

        Return type:
        :   [Group](group.md#keysight.ads.dds.Group "keysight.ads.dds.Group")

        Example

        Insert a group.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> eq = page.add_equation("x", "10")
        >>> text = page.add_text("text", (0, 0))
        >>> group = page.add_group([eq, text])
        ```

    add\_line(*start: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*, *end: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → [Line](shapes.md#keysight.ads.dds.Line "keysight.ads.dds.core.ddshape.Line")[](#keysight.ads.dds.Page.add_line "Link to this definition")
    :   Add a line to the page.

        Parameters:
        :   * **start** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]*) – Coordinates of where to start the line.
            * **end** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]*) – Coordinates of where to end the line.

        Returns:
        :   Returns the line placed on the page.

        Return type:
        :   [Line](shapes.md#keysight.ads.dds.Line "keysight.ads.dds.Line")

        Example

        Insert a line.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> start = dds.Point(500, 500)
        >>> end = dds.Point(1500, 1500)
        >>> obj = page.add_line(start, end)
        ```

    add\_list(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [Listing](plots.md#keysight.ads.dds.Listing "keysight.ads.dds.core.ddplot.Listing")[](#keysight.ads.dds.Page.add_list "Link to this definition")
    :   Add a list plot to the page.

        It is the same as [`add_plot()`](#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot") except that it returns a list plot.

    add\_picture(*path: str*, *rect: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → [Picture](picture.md#keysight.ads.dds.Picture "keysight.ads.dds.core.ddshape.Picture")[](#keysight.ads.dds.Page.add_picture "Link to this definition")
    :   Add a picture to the page.

        Parameters:
        :   * **path** (*str*) – The path of the file that contains the picture. This path may be either a relative or absolute path.
            * **rect** ([*Rect*](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – Coordinates of the rectangle that will contain the picture.

        Returns:
        :   Returns the picture placed on the page.

        Return type:
        :   [Picture](picture.md#keysight.ads.dds.Picture "keysight.ads.dds.Picture")

        Example

        Insert a picture.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> rect = dds.Rect(top=0, left=0, bottom=100, right=100)
        >>> obj = page.add_picture("some_path", rect)
        ```

    add\_plot(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [RectPlot](plots.md#keysight.ads.dds.RectPlot "keysight.ads.dds.core.ddplot.RectPlot")[](#keysight.ads.dds.Page.add_plot "Link to this definition")
    :   Add a rectangle plot to the page.

        Parameters:
        :   * **Location** ([*Rect*](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.Rect") *|* [*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]* *[**optional**,* *default = None**]*) – Coordinates of where to place the plot on the page.
              If a Rect is passed, the plot will be placed at that location, and it will have the dimensions of the Rect.
              If a Point or tuple[int,int] is passed, the top\_left corner of the plot will be placed at that location,
              and it will be a default size.
              If omitted, the plot is placed in an empty spot on the page, and it will be a default size.
              The location of the plot may be moved to a different location with the method [`RectPlot.move()`](plots.md#keysight.ads.dds.RectPlot.move "keysight.ads.dds.RectPlot.move").
              The location and size of the plot may be modified with the property [`RectPlot.bbox`](plots.md#keysight.ads.dds.RectPlot.bbox "keysight.ads.dds.RectPlot.bbox").
            * **traces** (*str* *|* *list**[**str**]* *[**optional**,* *default = None**]*) – A single trace or a list of trace specified by name that will be placed on the plot.
              A trace may be a variable from a dataset or it may be an equation in the DDSFile.
              See [`Trace`](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.Trace") for details.
              If omitted, an empty plot will be created.
              Traces may be added with the methods [`RectPlot.add_trace()`](plots.md#keysight.ads.dds.RectPlot.add_trace "keysight.ads.dds.RectPlot.add_trace") and [`RectPlot.add_traces()`](plots.md#keysight.ads.dds.RectPlot.add_traces "keysight.ads.dds.RectPlot.add_traces").
            * **title** (*str* *[**optional**,* *default = None**]*) – The string to be used as the title of the plot.
              If omitted, the plot will not have a title.
              The title may be added by modifying the property [`RectPlot.title`](plots.md#keysight.ads.dds.RectPlot.title "keysight.ads.dds.RectPlot.title").

        Returns:
        :   Returns the rectangle plot placed on the page.

        Return type:
        :   [RectPlot](plots.md#keysight.ads.dds.RectPlot "keysight.ads.dds.RectPlot")

        Example

        Insert two rectangle plots side by side onto the default page.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot(dds.Rect(top=0,left=0,bottom=4000,right=4000), ["dB(S11)", "eqn1"], "Rectangle Plot 1")
        >>> empty_plot = page.add_plot()
        >>> empty_plot.add_traces(["dB(S12)","eqn1"])
        >>> empty_plot.move((6000,-4500))
        >>> empty_plot.title = "Rectangle Plot 2"
        >>> dds_file.save()
        ```

    add\_polar\_plot(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [PolarPlot](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.core.ddplot.PolarPlot")[](#keysight.ads.dds.Page.add_polar_plot "Link to this definition")
    :   Add a polar plot to the page.

        It is the same as [`add_plot()`](#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot") except that it returns a polar plot.

    add\_polygon(*pts: list[[Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]]*) → [Polygon](shapes.md#keysight.ads.dds.Polygon "keysight.ads.dds.core.ddshape.Polygon")[](#keysight.ads.dds.Page.add_polygon "Link to this definition")
    :   Add a polygon to the page.

        Parameters:
        :   **pts** (*list**[*[*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]**]*) – Coordinates of vertices of the polygon.

        Returns:
        :   Returns the polygon placed on the page.

        Return type:
        :   [Polygon](shapes.md#keysight.ads.dds.Polygon "keysight.ads.dds.Polygon")

        Example

        Insert a polygon.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> points = [
        >>>     dds.Point(2000, 2000),
        >>>     dds.Point(3000, 3000),
        >>>     dds.Point(4000, 4000),
        >>> ]
        >>> obj = page.add_polygon(points)
        ```

    add\_polyline(*pts: list[[Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]]*) → [Polyline](shapes.md#keysight.ads.dds.Polyline "keysight.ads.dds.core.ddshape.Polyline")[](#keysight.ads.dds.Page.add_polyline "Link to this definition")
    :   Add a polyline to the page.

        Parameters:
        :   **pts** (*list**[*[*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]**]*) – Coordinates of vertices of the polyline.

        Returns:
        :   Returns the polyline placed on the page.

        Return type:
        :   PolyLine

        Example

        Insert a polyline.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> points = [
        >>>     dds.Point(2000, 2000),
        >>>     dds.Point(3000, 3000),
        >>>     dds.Point(4000, 4000),
        >>> ]
        >>> obj = page.add_polyline(points)
        ```

    add\_py\_equation(*expression: str*, *location: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*) → [PyEquation](pyequation.md#keysight.ads.dds.PyEquation "keysight.ads.dds.core.ddshape.PyEquation")[](#keysight.ads.dds.Page.add_py_equation "Link to this definition")
    :   Add a python code to the page as a graphical object.

        Parameters:
        :   * **expression** (*str*) – An expression can be one or multiple lines of python code.
            * **Location** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]* *[**optional**,* *default = None**]*) – Coordinates of where to place the equation on the page.
              If a Point or tuple[int,int] is passed, the top\_left corner of the equation will be placed at that location.
              If omitted, the equation is placed in an empty spot on the page.

        Returns:
        :   Returns the python object placed on the page.

        Return type:
        :   [PyEquation](pyequation.md#keysight.ads.dds.PyEquation "keysight.ads.dds.PyEquation")

        Examples

        Add a python equation that calculates a numerical value

        ```
        >>> exp = page.add_py_equation('''
        from math import sqrt
        y = sqrt(4)''')
        >>> print(exp.values['y'])
        2
        ```

    add\_slider(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [Slider](plots.md#keysight.ads.dds.Slider "keysight.ads.dds.core.ddplot.Slider")[](#keysight.ads.dds.Page.add_slider "Link to this definition")
    :   Add a slider to the page.

        A slider will typically have one trace with a marker for an independent variable.

        Example

        For a swept simulation with Independent Variables ‘R1’ and ‘R2’ and Dependent Variable ‘V’, the trace
        would be “V[::,0]” for sweeping with ‘R1’ data.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> page = dds_file.pages[0]
        >>> plot = page.add_slider(traces="swept_simulation..V[::,0]")
        >>> dds_file.save()
        ```

    add\_smith\_chart(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [SmithChart](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.core.ddplot.SmithChart")[](#keysight.ads.dds.Page.add_smith_chart "Link to this definition")
    :   Add a smith chart to the page.

        It is the same as [`add_plot()`](#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot") except that it returns a smith chart.

    add\_stacked\_plot(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [StackedPlot](plots.md#keysight.ads.dds.StackedPlot "keysight.ads.dds.core.ddplot.StackedPlot")[](#keysight.ads.dds.Page.add_stacked_plot "Link to this definition")
    :   Add a stacked plot to the page.

        It is the same as [`add_plot()`](#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot") except that it returns a stacked plot.

    add\_text(*text: str*, *location: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → [Text](text.md#keysight.ads.dds.Text "keysight.ads.dds.core.ddshape.Text")[](#keysight.ads.dds.Page.add_text "Link to this definition")
    :   Add a text to the page.

        Parameters:
        :   * **text** (*str*) – Contents of the text.
            * **location** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]*) – Coordinates of the location of the text.

        Returns:
        :   Returns the text placed on the page.

        Return type:
        :   [Text](text.md#keysight.ads.dds.Text "keysight.ads.dds.Text")

        Example

        Insert a text.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> obj = page.add_text("text", (0, 0))
        ```

    add\_widget(*widget: QWidget*, *location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*) → [Widget](pywidget.md#keysight.ads.dds.Widget "keysight.ads.dds.core.ddshape.Widget")[](#keysight.ads.dds.Page.add_widget "Link to this definition")

    align\_bottom(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_bottom "Link to this definition")
    :   Align a list of graphical objects along the bottom coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the bottom.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_bottom([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(50,0), bottom_right=(150,100)">
        ```

    align\_center\_horizontal(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_center_horizontal "Link to this definition")
    :   Align a list of graphical objects along the center horizontal coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the center horizontal.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_center_horizontal([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(50,0), bottom_right=(150,100)">
        ```

    align\_center\_vertical(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_center_vertical "Link to this definition")
    :   Align a list of graphical objects along the center vertical coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the center vertical.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_center_vertical([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(0,50), bottom_right=(100,150)">
        ```

    align\_grid(*objs: list[GraphicalObject]*, *rows: int*, *columns: int*) → None[](#keysight.ads.dds.Page.align_grid "Link to this definition")
    :   Align a list of graphical objects into specified rows and columns, based on the location of the first object in the list.

        Parameters:
        :   * **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.
            * **rows** (*int*) – The number of rows in the layout of the objects.
            * **columns** (*int*) – The number of columns in the layout of the objects.

        Return type:
        :   None

        Raises:
        :   **RuntimeError: Not enough rows and columns specified for objects.** – Too many objects to fit in the specified row/column layout.

        Example

        Align objects on the grid in 2 rows, 1 column.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_grid([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(0,200), bottom_right=(100,300)">
        ```

    align\_left(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_left "Link to this definition")
    :   Align a list of graphical objects along the left coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the left.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_left([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(0,50), bottom_right=(100,150)">
        ```

    align\_right(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_right "Link to this definition")
    :   Align a list of graphical objects along the right coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the right.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_right([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(0,50), bottom_right=(100,150)">
        ```

    align\_top(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_top "Link to this definition")
    :   Align a list of graphical objects along the top coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the top.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_top([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(50,0), bottom_right=(150,100)">
        ```

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Page.bbox "Link to this definition")
    :   The calculation of adding the bounding boxes of all the objects on the page.

        This property is Read-only.

        Raises:
        :   **RuntimeError: Invalid bounding box calculated for page.** – This occurs when there are no objects on the page.

        Example

        Find an empty space on a page to place a new plot.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds"")
        >>> page = dds_file.pages[0]
        >>> locForNewPlot = (0,0)
        >>> if len(page.objects) > 0:
        >>>     locForNewPlot = page.bbox.bottom_right + (1000,0)
        >>> plot = page.new_plot(locForNewPlot)
        ```

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.change_object_order "Link to this definition")
    :   Change the order that the objects are referenced and displayed.

        Change the order that the objects are referenced and displayed.
        Objects that exist on the page but are not included in
        the list of objects to be reorderd will be place before the
        objects being reordered. Objects that are not referenced
        in the page are ignored.

        Example

        Build three objects and change order to display the box under the
        plot and list.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>> list = page.add_list();
        >>> box = page.add_box(dds.Rect(top=1000, left=1000, bottom=5000, right=5000));
        >>>
        >>> page.objects
        [<RectPlot "">, <TextPlot "">, <Box "">]
        >>>
        >>> page.change_object_order([list, plot])
        >>>
        >>> page.objects
        [<Box "">, <TextPlot "">, <RectPlot "">]
        ```

    *property* name*: str*[](#keysight.ads.dds.Page.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.Page.objects "Link to this definition")
    :   A list of objects on a page.

        This property is Read-only.
        It is may be modified by adding/deleting objects on the page.

        Example

        Obtain a list of objects in the default page that has a plot and an equation.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds"")
        >>> page = dds_file.pages[0]
        >>> objs == page.objects
        >>> print(objs)
            [<AntennaPlot "">, <UserExpression  "a = S11">]
        >>> textObj = page.add_text("hello", (100,100))
        >>> print(page.objects)
            [<Text "hello", <AntennaPlot "">, <UserExpression  "a = S11">]
        >>> textObj.delete_object()
        >>> print(page.objects)
            [<AntennaPlot "">, <UserExpression  "a = S11">]
        ```

    remove\_group(*group: [Group](group.md#keysight.ads.dds.Group "keysight.ads.dds.core.ddshape.Group")*) → None[](#keysight.ads.dds.Page.remove_group "Link to this definition")
    :   Remove a group to the page.

        Parameters:
        :   **group** ([*Group*](group.md#keysight.ads.dds.Group "keysight.ads.dds.Group")) – The group to remove from the page.

        Return type:
        :   None

        Example

        Insert a group.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> eq = page.add_equation("x", "10")
        >>> text = page.add_text("text", (0, 0))
        >>> group = page.add_group([eq, text])
        >>> page.remove(group)
        ```

    *property* selected\_objects*: list[GraphicalObject]*[](#keysight.ads.dds.Page.selected_objects "Link to this definition")
    :   A list of selected objects on a page.

        This property may be modified.

        Example

        Select the plots on the default page of a DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds"")
        >>> page = dds_file.pages[0]
        >>> selObjs == page.selected_objects
        >>> print(selObjs)
            []
        >>> objs = page.objects
        >>> print(objs)
            [<AntennaPlot "">, <RectPlot "">, <UserExpression  "a = S11">]
        >>> objsToSelect = []
        >>> for obj in objs:
        >>>     if dds.ObjectType.is_plot(obj):
        >>>         objsToSelect.append(obj)
        >>> page.selected_objects = objsToSelect
        >>> selObjs = page.selected_objects
        >>> print(selObjs)
            [<AntennaPlot "">, <RectPlot "">]
        ```

    *property* type*: ObjectType*[](#keysight.ads.dds.Page.type "Link to this definition")

On this page

[Previous

DDSFile](file.md)
[Next

Point](point.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top