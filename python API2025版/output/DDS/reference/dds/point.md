<!-- 来源: reference\dds\point.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Point

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
    - Point
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

# Point[](#point "Link to this heading")

*class* keysight.ads.dds.Point[](#keysight.ads.dds.Point "Link to this definition")
:   An (x,y) coordinate grid point.

    Parameters:
    :   * **x** (*int*) – X-coordinate
        * **y** (*int*) – Y-coordinate

    Example

    Create a Point.

    ```
    >>> from keysight.ads import dds
    >>> snap_pt == dds.Point(100, 50)
    >>> print(snap_pt)
        Point(x=100, y=50)
    ```

    astuple() → tuple[int, int][](#keysight.ads.dds.Point.astuple "Link to this definition")
    :   Convert a Point to a tuple.

        Returns:
        :   returns a tuple containing the x,y values of Point

        Return type:
        :   tuple[int, int]

        Example

        Convert a Point to a tuple.

        ```
        >>> from keysight.ads import dds
        >>> snap_pt == dds.Point(100, 50)
        >>> print(snap_pt)
            Point(x=100, y=50)
        >>> print(snap_pt.astuple())
            (100,50)
        ```

    x*: int* *= 0*[](#keysight.ads.dds.Point.x "Link to this definition")
    :   The x-coordinate.

        Example

        Modify a Point.

        ```
        >>> from keysight.ads import dds
        >>> snap_pt == dds.Point(100, 50)
        >>> print(snap_pt)
            Point(x=100, y=50)
        >>> snap_pt.x = 200
        >>> print(snap_pt)
            Point(x=200, y=50)
        ```

    y*: int* *= 0*[](#keysight.ads.dds.Point.y "Link to this definition")
    :   The y-coordinate.

        Example

        Modify a Point.

        ```
        >>> from keysight.ads import dds
        >>> snap_pt == dds.Point(100, 50)
        >>> print(snap_pt)
            Point(x=100, y=50)
        >>> snap_pt.y = 200
        >>> print(snap_pt)
            Point(x=200, y=200)
        ```

On this page

[Previous

Page](page.md)
[Next

Rect](rect.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top