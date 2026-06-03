<!-- 来源: reference\dds\basic.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Common Properties

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
    - [Masks](masks.md)
    - [Specification](specifications.md)
    - [Equation](equation.md)
    - [PyEquation](pyequation.md)
    - [Text](text.md)
    - [Picture](picture.md)
    - [Shapes](shapes.md)
    - [Group](group.md)
    - Common Properties
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

# Common Properties[](#common-properties "Link to this heading")

*class* keysight.ads.dds.Color[](#keysight.ads.dds.Color "Link to this definition")
:   Class that contains color information.

    Available colors specified in the configuration file hpeecolor.cfg, which by default resides in
    $HPEESOF\_DIR/config (where $HPEESOF\_DIR represents the complete installation path).
    See documentation for customizing the ADS environment found in the ADS installation manual for details.
    The available colors can be obtained by the method [`colors()`](#keysight.ads.dds.Color.colors "keysight.ads.dds.Color.colors").
    Individual colors can be obtained either by index or by rgb values.

    Parameters:
    :   **index\_or\_rgb** (*int* *|* *tuple**[**int**,* *int**,* *int**]*) – If an integer is passed, the color returned is nth element in the list of available colors.
        If a tuple is passed, the color returned is the element in the list of available colors that matches the rgb value to the tuple.

    Raises:
    :   * **RuntimeError: Invalid color index "<int>" specified. Color index must be between "0" and "<int>".** – The integer parameter is out of bounds of the available colors.
        * **RuntimeError: Unable to find color r={<int>}****,** **g={<int>}****,** **b={<int>}.** – The tuple parameter does not match any available colors.

    Example

    Obtain the 2nd color in the list of colors

    ```
    >>> from keysight.ads import dds as dds
    >>> yellow = dds.Color(2)
    >>> print(yellow.rgb)
        (255, 255, 0)
    ```

    Create yellow. The rgb values of yellow is (255, 255, 0).

    ```
    >>> from keysight.ads import dds as dds
    >>> yellow = dds.Color((255, 255, 0))
    >>> print(yellow.index)
        2
    ```

    *static* color\_index(*color: tuple[int, int, int]*) → int[](#keysight.ads.dds.Color.color_index "Link to this definition")
    :   Return the index into the available list of colors that matches the rgb parameter.

        The list is obtained by the method [`colors()`](#keysight.ads.dds.Color.colors "keysight.ads.dds.Color.colors").

        Parameters:
        :   **color** (*tuple**[**int**,* *int**,* *int**]**)*) – The rgb values to match.

        Returns:
        :   Index into the list of available colors that matches the tuple. If a match is not found, an exception is thrown.

        Return type:
        :   int

        Raises:
        :   **RuntimeError: Unable to find color r=<int>****,** **g=<int>****,** **b=<int>.** – This occurs when the rgb value is not found in the list of available colors,
            which is obtained by the method [`colors()`](#keysight.ads.dds.Color.colors "keysight.ads.dds.Color.colors").

        Example

        Get the index of a particular rgb value.

        ```
        >>> from keysight.ads import dds as dds
        >>> yellow_index = dds.Color.color_index((255, 255, 0))
        >>> print(dds.Color.colors()[yellow_index])
            (255, 255, 0)
        ```

    *static* colors() → list[tuple[int, int, int]][](#keysight.ads.dds.Color.colors "Link to this definition")
    :   Return a list of colors.

        Returns:
        :   A list of available colors. These are defined in the config file "$HPEESOF\_DIR/config/hpeecolor.cfg".
            Each color in the list is stored as a tuple of 3 integers representing the rgb value of the color.
            Specific colors may be obtained by specifying an index into this list. Matching an element to an
            rgb value can be done by using the method [`color_index()`](#keysight.ads.dds.Color.color_index "keysight.ads.dds.Color.color_index").

        Return type:
        :   list[tuple[int, int, int]]

        Raises:
        :   **RuntimeError: Color map is empty** **or** **missing. Please verify that "$HPEESOF\_DIR/config/hpeecolor.cfg" exists and is correctly configured.** – The config file hpeecolor.cfg is not found. There is no list.

        Example

        Obtain a list of available colors.

        ```
        >>> from keysight.ads import dds as dds
        >>> colors = dds.Color.colors()
        ```

    *property* index*: int*[](#keysight.ads.dds.Color.index "Link to this definition")
    :   The index into the list of available colors.

    *property* rgb*: tuple[int, int, int]*[](#keysight.ads.dds.Color.rgb "Link to this definition")
    :   The rgb value of the color.

*class* keysight.ads.dds.DensitySymbolProperties[](#keysight.ads.dds.DensitySymbolProperties "Link to this definition")

*class* keysight.ads.dds.FillProperties[](#keysight.ads.dds.FillProperties "Link to this definition")
:   Class that contains properties for fill patterns.

    Available fill patterns are specified in the configuration file hpeefill.cfg, which by default resides in
    $HPEESOF\_DIR/config (where $HPEESOF\_DIR represents the complete installation path).
    See documentation for customizing the ADS environment found in the ADS installation manual for details.
    The available fill patterns can be obtained by the method [`fill_patterns()`](#keysight.ads.dds.FillProperties.fill_patterns "keysight.ads.dds.FillProperties.fill_patterns").
    Individual fill patterns can be obtained by indexing into the fill patterns list with a string.

    Parameters:
    :   * **pattern** (*str* *[**optional**,* *default=None**]*) – If a string is passed, the fill pattern used is the element in the list of available fill patterns that matches the string.
          If the patterns is not found, an exception is thrown.
        * **color** ([*Color*](#keysight.ads.dds.Color "keysight.ads.dds.Color") *[**optional**,* *default=None**]*) – If a valid Color is passed, the fill pattern will be drawn in the specified color. If no color is specified (value == None), then
          the fill pattern will be drawn in black. If an invalid color is specified, an exception is thrown.

    Raises:
    :   * **RuntimeError: Unable to find pattern <pattern>** – The “pattern”” parameter is not found in the list of fill patterns.
        * **RuntimeError: Invalid color index "<int>" specified. Color index must be between "0" and "<int>".** – The integer parameter is out of bounds of the available colors.
        * **RuntimeError: Unable to find color r={<int>}****,** **g={<int>}****,** **b={<int>}.** – The tuple parameter does not match any available colors.

    Example

    Set fill to yellow dots in a circle.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> page = dds_file.pages[0]
    >>> center = dds.Point(500, 500)
    >>> obj = page.add_circle(center, 100)
    >>> obj.fill_properties = dds.FillProperties('dots_1', dds.Color(2))
    >>> print(obj.fill_properties)
        <FillProperties pattern="dots_1" color=<Color "2">>
    ```

    *property* color*: [Color](#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.FillProperties.color "Link to this definition")

    *static* fill\_patterns() → list[str][](#keysight.ads.dds.FillProperties.fill_patterns "Link to this definition")
    :   Return a list of patterns.

        Returns:
        :   A list of available patterns. These are defined in the config file "$HPEESOF\_DIR/config/hpeefill.cfg".
            Each pattern in the list is stored as a string.

        Return type:
        :   list[str]

        Example

        Obtain a list of available patterns.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds.FillPatterns.fill_patterns()
        ```

    *property* pattern*: str*[](#keysight.ads.dds.FillProperties.pattern "Link to this definition")

*class* keysight.ads.dds.LineProperties[](#keysight.ads.dds.LineProperties "Link to this definition")
:   Class that contains properties for lines.

    Available types are defined by the class [`LineType`](#keysight.ads.dds.LineType "keysight.ads.dds.LineType").

    Parameters:
    :   * **type** ([*LineType*](#keysight.ads.dds.LineType "keysight.ads.dds.LineType") *[**optional**,* *default=None**]*) – Any value other than a value from class:LineType will throw an exception.
        * **color** ([*Color*](#keysight.ads.dds.Color "keysight.ads.dds.Color") *[**optional**,* *default=None**]*) – If a valid Color is passed, the fill pattern will be drawn in the specified color. If no color is specified (value == None), then
          the fill pattern will be drawn in black. If an invalid color is specified, an exception is thrown.
        * **width** (*float* *[**optional**,* *default=None**]*) – The width is truncated to the nearest tenth. If width is not passed, the width is 0.5. If a negative width is passed, it is simply ignored.

    Raises:
    :   * **RuntimeError: Invalid color index "<int>" specified. Color index must be between "0" and "<int>".** – The integer parameter is out of bounds of the available colors.
        * **RuntimeError: Unable to find color r={<int>}****,** **g={<int>}****,** **b={<int>}.** – The tuple parameter does not match any available colors.

    Example

    Set line type to green long dashes in a circle.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> page = dds_file.pages[0]
    >>> center = dds.Point(500, 500)
    >>> obj = page.add_circle(center, 100)
    >>> obj.line_properties = dds.FillProperties(dds.LineType.LONG_DASH, dds.Color(3), 2.7)
    >>> print(obj.line_properties)
        <LineProperties type=LineType.LONG_DASH color=<Color "3"> width=-2.7>
    ```

    *property* color*: [Color](#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.LineProperties.color "Link to this definition")

    *property* type*: [LineType](#keysight.ads.dds.LineType "keysight.ads.dds.core.ddbase.LineType") | None*[](#keysight.ads.dds.LineProperties.type "Link to this definition")

    *property* width*: float*[](#keysight.ads.dds.LineProperties.width "Link to this definition")

*class* keysight.ads.dds.LineType[](#keysight.ads.dds.LineType "Link to this definition")
:   DOT *= <DDlineTypeC.DOT: 1>*[](#keysight.ads.dds.LineType.DOT "Link to this definition")

    DOT\_DOT *= <DDlineTypeC.DOT\_DOT: 2>*[](#keysight.ads.dds.LineType.DOT_DOT "Link to this definition")

    LONG\_DASH *= <DDlineTypeC.LONG\_DASH: 5>*[](#keysight.ads.dds.LineType.LONG_DASH "Link to this definition")

    LONG\_DOT\_DASH *= <DDlineTypeC.LONG\_DOT\_DASH: 6>*[](#keysight.ads.dds.LineType.LONG_DOT_DASH "Link to this definition")

    SHORT\_DASH *= <DDlineTypeC.SHORT\_DASH: 3>*[](#keysight.ads.dds.LineType.SHORT_DASH "Link to this definition")

    SHORT\_DOT\_DASH *= <DDlineTypeC.SHORT\_DOT\_DASH: 4>*[](#keysight.ads.dds.LineType.SHORT_DOT_DASH "Link to this definition")

    SOLID *= <DDlineTypeC.SOLID\_LINE: 0>*[](#keysight.ads.dds.LineType.SOLID "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.LineType.str "Link to this definition")

*class* keysight.ads.dds.SymbolProperties[](#keysight.ads.dds.SymbolProperties "Link to this definition")

*class* keysight.ads.dds.TextProperties[](#keysight.ads.dds.TextProperties "Link to this definition")
:   Class that contains properties for text.

    The available fonts can be obtained by the method `get_fonts()`.
    The Data Display default font can be obtained by the mothod :meth:’get\_default\_font’.
    Individual fonts can be obtained by indexing into the fonts list with a string.

    Parameters:
    :   * **font** (*str* *[**optional**,* *default=None**]*) – If a string is passed, the font used is the element in the list of available fonts that matches the string.
          If no font is specified, the default font is used.
          If the font is not found, an exception is thrown.
        * **color** ([*Color*](#keysight.ads.dds.Color "keysight.ads.dds.Color") *[**optional**,* *default=None**]*) – If a valid Color is passed, the text will be drawn in the specified color. If no color is specified (value == None), then
          the text will be drawn in black. If an invalid color is specified, an exception is thrown.
        * **size** (*int* *[**optional**,* *default=None**]*) – If an integer is passed, it specifies the size of the font.
          If size is not passed or is negative, the default size is used.

    Raises:
    :   * **RuntimeError: Font name "<font>" not found on system.** – The “font” parameter is not found in the list of fonts.
        * **RuntimeError: Invalid color index "<int>" specified. Color index must be between "0" and "<int>".** – The integer parameter is out of bounds of the available colors.

    Example

    Set text properties on a text on a page.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> page = dds_file.pages[0]
    >>> obj = page.add_text("Hello World"dds.Point(500,500))
    >>> obj.text_properties = dds.TextProperties('Roman', dds.Color(2), 24)
    >>> print(obj.text_properties)
        <TextProperties font="Roman" color=<Color "2"> size=23>
    ```

    *property* color*: [Color](#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.TextProperties.color "Link to this definition")

    *static* default\_font() → str[](#keysight.ads.dds.TextProperties.default_font "Link to this definition")

    *property* font*: str*[](#keysight.ads.dds.TextProperties.font "Link to this definition")

    *static* font\_exists(*font: str*) → bool[](#keysight.ads.dds.TextProperties.font_exists "Link to this definition")

    *static* fonts() → list[str][](#keysight.ads.dds.TextProperties.fonts "Link to this definition")
    :   Return a list of fonts.

        Returns:
        :   A list of available fonts. Each font in the list is stored as a string.

        Return type:
        :   list[str]

        Example

        Obtain a list of available fonts.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds.TextProperties.fonts()
        ```

    *property* size*: int*[](#keysight.ads.dds.TextProperties.size "Link to this definition")

    text\_size(*text: str*) → tuple[int, int][](#keysight.ads.dds.TextProperties.text_size "Link to this definition")

*class* keysight.ads.dds.StringFormat[](#keysight.ads.dds.StringFormat "Link to this definition")
:   *property* complex\_format*: ComplexStringFormatOption*[](#keysight.ads.dds.StringFormat.complex_format "Link to this definition")

    *property* format*: StringFormatOption*[](#keysight.ads.dds.StringFormat.format "Link to this definition")

    *property* signficant\_digits*: int*[](#keysight.ads.dds.StringFormat.signficant_digits "Link to this definition")

    *property* units\_format*: UnitsStringOption*[](#keysight.ads.dds.StringFormat.units_format "Link to this definition")

On this page

[Previous

Group](group.md)
[Next

Print](print.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top