<!-- 来源: reference\dds\windows.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Window

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
    - [Shapes](shapes.md)
    - [Group](group.md)
    - [Common Properties](basic.md)
    - [Print](print.md)
    - [Object](objects.md)
    - Window
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

# Window[](#window "Link to this heading")

*class* keysight.ads.dds.Window[](#keysight.ads.dds.Window "Link to this definition")
:   A Window is a view of a Page.

    This class cannot be instantiated directly. When a Data Display file is created, a page and
    a window are automatically created. Additional windows can be created with [`DDSFile.new_window()`](file.md#keysight.ads.dds.DDSFile.new_window "keysight.ads.dds.DDSFile.new_window").
    Pages can be access by the property [`DDSFile.windows`](file.md#keysight.ads.dds.DDSFile.windows "keysight.ads.dds.DDSFile.windows").

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.Window.__init__ "Link to this definition")

    *property* current\_page*: [Page](page.md#keysight.ads.dds.Page "keysight.ads.dds.core.ddpage.Page")*[](#keysight.ads.dds.Window.current_page "Link to this definition")

    *static* from\_qwidget(*widget: QMainWindow*) → [Window](#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window")[](#keysight.ads.dds.Window.from_qwidget "Link to this definition")
    :   Get the DDS Window if it is associated with a given QMainWindow widget.

    *property* name*: str*[](#keysight.ads.dds.Window.name "Link to this definition")

    *property* page\_name\_order*: list[str]*[](#keysight.ads.dds.Window.page_name_order "Link to this definition")
    :   The list of page names in display order.

        This property holds the list of page names as they are
        displayed to the user. It allows you to change the order
        of page names in the window page tabs and to update the
        order of pages in the windows toolbar page menu.

        The windows tabs are ordered from left to right with the first
        name in the list being the left most tab in the window and the
        last page name in the list is the right most tab.

        To change the page tab order simply reorder the page names in
        the new desired order and update the property.

        When updating the property, any page name with a corresponding
        page object, that doesn’t exist in the list will be appended
        to the end of the list. Any duplicate page names found in the
        list are ignored. Any page name that doesn’t have a object is
        ignored.

        Example

        This example we change the page name order of three pages and
        then we make a mistake in the name which causes the actual
        page name to be appended to the end of the list of page names.

        ```
        >>> from keysight.ads import dds
        >>> dds_file = dds.new_dds_file()
        >>> dds_file.new_page("page 2")
        <Page name="page 2">
        >>> dds_file.new_page("page 3")
        <Page name="page 3">
        >>> window = dds_file.windows[0]
        >>>
        >>> print( window.page_name_order )
        ['page 1', 'page 2', 'page 3']
        >>>
        >>> window.page_name_order = ['page 2', 'page 3', 'page 1']
        >>> print( window.page_name_order )
        ['page 2', 'page 3', 'page 1']
        >>>
        >>> # Make a mistake in the page name.  Notice that 'page 33'
        >>> # doesn't exist and 'page 3', which now isn't in the list,
        >>> # is appended to the end of the list.
        >>> window.page_name_order = ['page 2', 'page 33', 'page 1']
        >>> print( window.page_name_order )
        ['page 2', 'page 1', 'page 3']
        ```

    *property* qwidget*: QMainWindow*[](#keysight.ads.dds.Window.qwidget "Link to this definition")
    :   Get the QMainWindow object associated with the window. The QMainWindow can be used to modify the user interface.

    *property* type*: ObjectType*[](#keysight.ads.dds.Window.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.Window.uid "Link to this definition")

    *property* view\_rect*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Window.view_rect "Link to this definition")

    zoom\_all() → None[](#keysight.ads.dds.Window.zoom_all "Link to this definition")

On this page

[Previous

Object](objects.md)
[Next

Widget](pywidget.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top