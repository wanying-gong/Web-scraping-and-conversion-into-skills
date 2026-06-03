<!-- 来源: reference\dds\pyequation.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* PyEquation

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
    - PyEquation
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

# PyEquation[](#pyequation "Link to this heading")

*class* keysight.ads.dds.PyEquation[](#keysight.ads.dds.PyEquation "Link to this definition")
:   Python Equations execute python statements with dependency tracking between other equations.

    Some uses cases include defining functions, performing complex mathematical operations on data,
    importing modules, displaying widgets or windows and manipulating graphical objects.

    This class cannot be instantiated directly. See [`Page.add_py_equation()`](page.md#keysight.ads.dds.Page.add_py_equation "keysight.ads.dds.Page.add_py_equation").

    activate() → None[](#keysight.ads.dds.PyEquation.activate "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.PyEquation.bbox "Link to this definition")
    :   The bounding box associated with an object.

    calculate() → None[](#keysight.ads.dds.PyEquation.calculate "Link to this definition")

    deactivate() → None[](#keysight.ads.dds.PyEquation.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.PyEquation.delete_object "Link to this definition")

    *property* errors*: str*[](#keysight.ads.dds.PyEquation.errors "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.PyEquation.expression "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.PyEquation.fill_properties "Link to this definition")

    *property* is\_auto\_calculated*: bool*[](#keysight.ads.dds.PyEquation.is_auto_calculated "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.PyEquation.is_deactivated "Link to this definition")

    *property* is\_outlined*: bool*[](#keysight.ads.dds.PyEquation.is_outlined "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.PyEquation.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.PyEquation.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.PyEquation.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.PyEquation.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.PyEquation.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.PyEquation.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.PyEquation.name "Link to this definition")

    *property* status*: str*[](#keysight.ads.dds.PyEquation.status "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.PyEquation.string_format "Link to this definition")

    *property* text\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.PyEquation.text_properties "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.PyEquation.type "Link to this definition")

    *property* values*: dict[str, Any]*[](#keysight.ads.dds.PyEquation.values "Link to this definition")
    :   A dictionary of the expression’s variable names and evaluated values.

        Examples

        Print the value of a variable in a python equation.

        ```
        >>> exp = page.add_py_equation(
        '''\
        x = 1
        y = x*2''')
        >>> exp.values['y']
        2
        ```

On this page

[Previous

Equation](equation.md)
[Next

Text](text.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top