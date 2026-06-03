<!-- 来源: reference\dds\rect.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Rect

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
    - Rect
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

# Rect[](#rect "Link to this heading")

*class* keysight.ads.dds.Rect[](#keysight.ads.dds.Rect "Link to this definition")
:   A simple rectangle defined by top, left, bottom, right values.

    The (top,left) values are always less than the (bottom,right) values.
    If they are specified otherwise, they will automatically be swapped. However, the
    dimensions of the rectangle will remain as specified.

    Parameters:
    :   * **top** (*int* *[**optional**,* *default=None**]*) – An integer that represents the y-coordinate of the top edge of the rectangle.
        * **left** (*int* *[**optional**,* *default=None**]*) – An integer that represents the x-coordinate of the left edge the rectangle
        * **bottom** (*int* *[**optional**,* *default=None**]*) – An integer that represents the y-coordinate of the bottom edge of the rectangle.
        * **right** (*int* *[**optional**,* *default=None**]*) – An integer that represents the x-coordinate of the right edge of the rectangle.
        * **top\_left** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]* *[**optional**,* *default=None**]*) – A Point or tuple[int,int] that contains x,y coordinates that represent the top-left corner of the rectangle.
        * **bottom\_right** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]* *[**optional**,* *default=None**]*) – A Point or tuple[int,int] that contains x,y coordinates that represent the bottom-right corner of the rectangle.
        * **width** (*int* *[**optional**,* *default=None**]*) – An integer that represents the width of the rectangle.
        * **height** (*int* *[**optional**,* *default=None**]*) – An integer that represents the height of the rectangle.

    Example

    Valid combinations of parameters to create a Rect.

    ```
    >>> from keysight.ads import dds
    >>> a = dds.Rect()
    >>> print(a)
        <Rect "top_left=(0,0), bottom_right=(0,0)">
    >>> b = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
    >>> print(b)
        <Rect "top_left=(0,0), bottom_right=(100,100)">
    >>> c = dds.Rect(top_left=dds.Point(50, 100), bottom_right=dds.Point(150, 200))
    >>> print(c)
        <Rect "top_left=(50,100), bottom_right=(150,200)">
    >>> d = dds.Rect(top_left=dds.Point(50,100), width = 500, height = 200)
    >>> print(d)
        <Rect "top_left=(50,100), bottom_right=(550,300)">
    >>> e = dds.Rect(top = 100, left = 50, width = 500, height = 200)
    >>> print(e)
            <Rect "top_left=(50,100), bottom_right=(550,300)">
    ```

    adjust(*\**, *left: int | None = None*, *top: int | None = None*, *right: int | None = None*, *bottom: int | None = None*) → None[](#keysight.ads.dds.Rect.adjust "Link to this definition")
    :   Modify the rectangle by adding parameters to the corresponding edge.

        Parameters:
        :   * **left** (*int* *[**optional**,* *default=None**]*) – An integer to add to “left” property
            * **top** (*int* *[**optional**,* *default=None**]*) – An integer to add to “top” property
            * **right** (*int* *[**optional**,* *default=None**]*) – An integer to add to “right” property
            * **bottom** (*int* *[**optional**,* *default=None**]*) – An integer to add to “bottom” property

        Return type:
        :   None

        Example

        Modify the rectangle to be narrower and taller.

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> r.adjust(right =-50, bottom = 100)
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(50,200)">
        ```

    adjusted(*\**, *left: int | None = None*, *top: int | None = None*, *right: int | None = None*, *bottom: int | None = None*) → [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")[](#keysight.ads.dds.Rect.adjusted "Link to this definition")
    :   Return a new Rect with coordinates determined by adding parameter(s) to the rectangle.

        The original Rect is not modified.

        Parameters:
        :   * **left** (*int* *[**optional**,* *default=None**]*) – An integer to add to “left” property
            * **top** (*int* *[**optional**,* *default=None**]*) – An integer to add to “top” property
            * **right** (*int* *[**optional**,* *default=None**]*) – An integer to add to “right” property
            * **bottom** (*int* *[**optional**,* *default=None**]*) – An integer to add to “bottom” property

        Returns:
        :   Create a new Rect with coordinates determined by adding the parameter(s) to the corresponding edge of the rectangle.

        Return type:
        :   [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")

        Example

        Create a new rect that is narrower and taller than self(Rect).

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> newRect = r.adjusted(right =-50, bottom = 100)
        >>> print(newRect)
            <Rect "top_left=(0,0), bottom_right=(50,200)">
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        ```

    *property* bottom*: int*[](#keysight.ads.dds.Rect.bottom "Link to this definition")
    :   An integer that represents the y-coordinate of the bottom edge of the rectangle.

    *property* bottom\_left*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Rect.bottom_left "Link to this definition")
    :   A Point that contains x,y coordinates that represent the bottom-left corner of the rectangle.

    *property* bottom\_right*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Rect.bottom_right "Link to this definition")
    :   A Point that contains x,y coordinates that represent the bottom-right corner of the rectangle.

    center() → [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")[](#keysight.ads.dds.Rect.center "Link to this definition")
    :   Return the center point of the rectangle.

        Returns:
        :   The center Point of the rectangle.

        Return type:
        :   [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point")

        Example

        Get the center point of the rectangle.

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> c = r.center()
        >>> print(c)
            Point(x=50, y=50)
        ```

    contains(*shape: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → bool[](#keysight.ads.dds.Rect.contains "Link to this definition")
    :   Return True if a shape is contained inside the rectangle.

        Parameters:
        :   **shape** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]* *|* [*Rect*](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – The shape to check is a point, tuple[int,int] or a rectangle.

        Returns:
        :   True if “shape” is completely contained inside the rectangle.
            Otherwise, returns False.

        Return type:
        :   bool

        Example

        Check if a Rect or a Point is contained in the rectangle.

        ```
        >>> from keysight.ads import dds
        >>> first = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> second = dds.Rect(top = 0, left = 0, bottom = 90, right = 90)
        >>> inside = first.contains(second)
        >>> print(inside)
            True
        >>> inside = first.contains(dds.Point(100, 200))
        >>> print(inside)
            False
        ```

    expand(*shape: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → None[](#keysight.ads.dds.Rect.expand "Link to this definition")
    :   Modify the rectangle by possibly expanding it to include a shape.

        Parameters:
        :   **shape** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]* *|* [*Rect*](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – The shape to include in the rectangle is a point, tuple[int,int] or another rectangle.

        Return type:
        :   None

        Example

        Expand the rectangle to include a Point and a Rect

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> r.expand(dds.Point(-50, 80))
        >>> print(r)
            <Rect "top_left=(-50,0), bottom_right=(100,100)">
        >>> r.expand(dds.Rect(top = -50, left = -40, bottom = 200, right = 150))
        >>> print(r)
            <Rect "top_left=(-50,-50), bottom_right=(150,200)">
        ```

    expanded(*shape: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")[](#keysight.ads.dds.Rect.expanded "Link to this definition")
    :   Return a new Rect with coordinates determined by expanding the rectangle to include a shape.

        The original Rect is not modified.

        Parameters:
        :   **shape** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]* *|* [*Rect*](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – The shape to include in the rectangle is a point, tuple[int,int] or another rectangle.

        Returns:
        :   Create a new Rect with coordinates determined by expanding the rectangle to include “shape”.

        Return type:
        :   [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")

        Example

        Create a new Rect by expanding the rectangle to include a Point and a Rect.

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> one = r.expanded(dds.Point(-50, 80))
        >>> print(one)
            <Rect "top_left=(-50,0), bottom_right=(100,100)">
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> two = r.expand(dds.Rect(top = -50, left = -40, bottom = 200, right = 150))
        >>> print(two)
            <Rect "top_left=(-50,-50), bottom_right=(150,200)">
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        ```

    *property* height*: int*[](#keysight.ads.dds.Rect.height "Link to this definition")
    :   An integer that represents the height of the rectangle.

    intersected(*rect: [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")[](#keysight.ads.dds.Rect.intersected "Link to this definition")
    :   Return a new rectangle that represents the intersection between 2 rectangles.

        The original Rect is not modified.

        Parameters:
        :   **rect** ([*Rect*](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – A rectangle used to calculate the intersection.

        Returns:
        :   Calculates the intersection between “rect” and the rectangle and creates a new Rect to represent the intersection.
            There are 10 cases of intersection: any of the 4 corners of “rect” are contained in the rectangle,
            any of the 4 sides of “rect” are contained in the rectangle, “rect” is totally contained in the rectangle,
            or “rect” equals the rectangle.

        Return type:
        :   [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")

        Example

        Get the intersection between 2 rectangles.

        ```
        >>> from keysight.ads import dds
        >>> first = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> second = dds.Rect(top = 10, left = 10, bottom = 110, right = 110)
        >>> intersection = first.intersects(second)
        >>> print(intersection)
            <Rect "top_left=(10,10), bottom_right=(100,100)">
        ```

    intersects(*rect: [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → bool[](#keysight.ads.dds.Rect.intersects "Link to this definition")
    :   Return True if 2 rectangles intersect.

        Parameters:
        :   **rect** ([*Rect*](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – A rectangle used to check for intersection.

        Returns:
        :   True if any point of “rect” is contained in the rectangle.
            Otherwise, returns False.

        Return type:
        :   bool

        Example

        Check if 2 rectangles intersect.

        ```
        >>> from keysight.ads import dds
        >>> first = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> second = dds.Rect(top = 10, left = 10, bottom = 110, right = 110)
        >>> inside = first.intersects(second)
        >>> print(inside)
            True
        ```

    *property* left*: int*[](#keysight.ads.dds.Rect.left "Link to this definition")
    :   An integer that represents the x-coordinate of the left edge of the rectangle.

    *property* right*: int*[](#keysight.ads.dds.Rect.right "Link to this definition")
    :   An integer that represents the y-coordinate of the right edge of the rectangle.

    *property* top*: int*[](#keysight.ads.dds.Rect.top "Link to this definition")
    :   An integer that represents the y-coordinate of the top edge of the rectangle.

    *property* top\_left*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Rect.top_left "Link to this definition")
    :   A Point that contains x,y coordinates that represent the top-left corner of the rectangle.

    *property* top\_right*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Rect.top_right "Link to this definition")
    :   A Point that contains x,y coordinates that represent the top-right corner of the rectangle.

    translate(*x\_offset: int*, *y\_offset: int*) → None[](#keysight.ads.dds.Rect.translate "Link to this definition")
    :   Modify the rectangle by adding offsets to its coordinates.

        Parameters:
        :   * **x\_offset** (*int*) – An integer to add to the x-coordinates
            * **y\_offset** (*int*) – An integer to add to the y-coordinates

        Return type:
        :   None

        Example

        Modify a rectangle to be wider and shorter.

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> r.translate(x_offset = 50, y_offset = -50)
        >>> print(r)
            <Rect "top_left=(50,-50), bottom_right=(150,50)">
        ```

    translated(*x\_offset: int*, *y\_offset: int*) → [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")[](#keysight.ads.dds.Rect.translated "Link to this definition")
    :   Return a new Rect with coordinates determined by adding offsets to the rectangle.

        The original Rect is not modified.

        Parameters:
        :   * **x\_offset** (*int*) – An integer to add to the x-coordinates
            * **y\_offset** (*int*) – An integer to add to the y-coordinates

        Returns:
        :   Creates a new Rect with coordinates determined by adding “x\_offset” and “y\_offset” to the x,y coordinates of the rectangle.

        Return type:
        :   [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")

        Example

        Create a new Rect that is wider and shorter than the rectangle.

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> newRect = r.translated(x_offset = 50, y_offset = -50)
        >>> print(newRect)
            <Rect "top_left=(50,-50), bottom_right=(150,50)">
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        ```

    *property* width*: int*[](#keysight.ads.dds.Rect.width "Link to this definition")
    :   An integer that represents the width of the rectangle.

On this page

[Previous

Point](point.md)
[Next

Grid](grid.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top