<!-- 来源: reference\dds\experimental\qtwidget.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.dds.experimental](index.md)
* DDSQtWidget

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

* [Introduction](../../../intro/index.md)
  + [Licensing](../../../intro/licensing.md)
  + [Using Data Display functionality in Python](../../../intro/usage.md)
  + [Using Visual Studio Code](../../../intro/vscode.md)
* [Concepts](../../../concepts/index.md)
  + [Python Script Execution](../../../concepts/execution.md)
* [Reference](../../index.md)
  + [keysight.ads.dds](../index.md)
    - [DDSFile](../file.md)
    - [Page](../page.md)
    - [Point](../point.md)
    - [Rect](../rect.md)
    - [Grid](../grid.md)
    - [Plots](../plots.md)
    - [Axes](../axes.md)
    - [Legend](../legend.md)
    - [Trace](../trace.md)
    - [Markers](../marker.md)
    - [Line Markers](../linemarker.md)
    - [Limit Lines](../limitlines.md)
    - [Masks](../masks.md)
    - [Specification](../specifications.md)
    - [Equation](../equation.md)
    - [PyEquation](../pyequation.md)
    - [Text](../text.md)
    - [Picture](../picture.md)
    - [Shapes](../shapes.md)
    - [Group](../group.md)
    - [Common Properties](../basic.md)
    - [Print](../print.md)
    - [Object](../objects.md)
    - [Window](../windows.md)
    - [Widget](../pywidget.md)
  + [keysight.ads.dds.experimental](index.md)
    - DDSQtWidget
  + [keysight.ads.dds.app](../app/index.md)
    - [Addon](../app/addon.md)
    - [Callbacks](../app/callbacks.md)
* [How-To](../../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../howto/venv.md)
    - [Creating an ADS based Python virtual environment](../../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../howto/existingvenv.md)
    - [ADS Python Environment Variables](../../../howto/pyenvvars.md)
  + [How to Use Pytest](../../../howto/pytest.md)
* [Examples](../../../examples/index.md)
  + [Create Shapes](../../../examples/ex_shapes.md)
  + [Create Pages and Windows](../../../examples/ex_pages_and_windows.md)
  + [Create and Modify DDS file](../../../examples/ex_modified_file.md)
  + [Create Markers](../../../examples/ex_markers.md)
  + [Create Line Markers](../../../examples/ex_line_markers.md)
  + [Create equations using dataset variables](../../../examples/ex_expressions_and_dataframes.md)
  + [Plot Simulation Output](../../../examples/ex_simple.md)
  + [Plot Amplifier Simulation Data](../../../examples/ex_optimized_amp.md)
  + [Create Pages and Windows](../../../examples/ex_python_equations.md)
  + [Add Specifications to a Plot](../../../examples/ex_specifications.md)
  + [Plot a Time-Domain Output Voltage Waveform](../../../examples/ex_trantest.md)
  + [Plot Parameter Extraction of Simulation Data](../../../examples/ex_crq_extraction.md)
  + [Add custom menu to Data-Display file](../../../examples/ex_custom_menu.md)
  + [Print PDF file](../../../examples/ex_print.md)
  + [Experimental Examples](../../../examples/experimental/index.md)
    - [DDS Qt Widget displayed in a Qt QDialog](../../../examples/experimental/ex_dds_qt_widget.md)
    - [DDS Qt Widget printed using a Qt QPrinter](../../../examples/experimental/ex_dds_qt_widget.md#dds-qt-widget-printed-using-a-qt-qprinter)
    - [DDS Qt Widget output to a Qt QPixmap](../../../examples/experimental/ex_dds_qt_widget.md#dds-qt-widget-output-to-a-qt-qpixmap)
    - [DDS rename dataset and update expressions](../../../examples/experimental/ex_rename_dataset.md)
* [App Examples](../../../appExamples/index.md)
  + [Add Menu to Data Display Menubar](../../../appExamples/ex_custom_menu.md)
  + [Add Widgets to Data Display Page](../../../appExamples/ex_page_widget.md)
  + [Add Matplotlib Plot to Data Display Window](../../../appExamples/ex_matplotlib_widget.md)
  + [Add an Addon to Data Display](../../../appExamples/ex_addon.md)
* [Addon Examples](../../../addonExamples/index.md)
  + [Addon to Generate Menus](../../../addonExamples/ex_addon/init.md)
  + [3D Plot Addon](../../../addonExamples/ex_addon_3d_plot/index.md)
    - [Menu for 3D Plot Addon](../../../addonExamples/ex_addon_3d_plot/init.md)
    - [Plot for 3D Plot Addon](../../../addonExamples/ex_addon_3d_plot/ex_addon_3d_plot.md)

# DDSQtWidget[](#ddsqtwidget "Link to this heading")

*class* keysight.ads.dds.experimental.DDSQtWidget[](#keysight.ads.dds.experimental.DDSQtWidget "Link to this definition")
:   A Qt Widget that utilizes the specified DDSFile objects.

    This class defines a Qt Widget that can be utilized in Qt Dialogs,
    Qt Images and printed with QPrinter.

    By default this widget will view the first page found in the
    associated with the DDSFile.

    Initially when the widget is displayed it will view all the
    objects that are available on the page being viewed by the widget.
    This view may be updated by calling the zoom methods provided by
    this widget. Also, the mouse wheel and click and drag zoom box are
    enabled to allow interactive changs of the current view.

    Parameters:
    :   * **parent** (*QWidget* *[**optional**,* *default=None**]*) – The QWidget that owns the widget.
        * **ddsfile** ([*DDSFile*](../file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile") *[**optional**,* *default=None**]*) – The DDSFile object utilized by the widget.

    Example

    Create a dialog to display the DDSFile object.

    ```
    >>> from PySide6.QtWidgets import QDialog, QVBoxLayout
    >>> from keysight.ads.dds import Rect, new_dds_file
    >>> from keysight.ads.dds.experimental import DDSQtWidget
    >>>
    >>> dds_file = new_dds_file()
    >>> page = dds_file.pages[0]
    >>> box = Rect(top=0,left=0,bottom=100,right=200)
    >>> page.add_box(box)
    >>>
    >>> dialog = QDialog()
    >>> layout = QVBoxLayout(dialog)
    >>>
    >>> ddswidget = DDSQtWidget(parent=dialog, ddsfile=dds_file)
    >>> layout.addWidget(ddswidget)
    >>>
    >>> dialog.resize(400,400)
    >>> dialog.show()
    >>> dialog.exec()
    ```

    See also

    [QWidget - Qt for Python](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html)
    :   The class documentation for the inherited QWidget class.

    \_\_init\_\_(*parent: QWidget | None = None*, *ddsfile: [DDSFile](../file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile") | None = None*)[](#keysight.ads.dds.experimental.DDSQtWidget.__init__ "Link to this definition")

    get\_dds\_file() → [DDSFile](../file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile") | None[](#keysight.ads.dds.experimental.DDSQtWidget.get_dds_file "Link to this definition")
    :   Return the `DDSFile` that is utilized by widget.

    get\_zoom\_rectangle() → [Rect](../rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")[](#keysight.ads.dds.experimental.DDSQtWidget.get_zoom_rectangle "Link to this definition")
    :   Get the current zoom rectangle (in dds database units).

    render\_dds\_widget(*painter: QPainter*) → None[](#keysight.ads.dds.experimental.DDSQtWidget.render_dds_widget "Link to this definition")
    :   Render the Data Display Qt Widget with the passed in QPainter.

        Immediately render the Data Display Qt Widget using the passed
        in painter. It scales the widget to fit the painter device
        dimensions. It’s useful to create a image files with QPixmap or
        printing using QPrinter.

        Parameters:
        :   **painter** (*QPainter object*) – The painter utilized to render the Data Display File.

        Examples

        Render the Data Display Qt Widget into a PNG file.

        ```
        >>> from PySide6.QtGui import QPainter, QPixmap
        >>> from PySide6.QtCore import Qt
        >>> from keysight.ads.dds import Rect, new_dds_file
        >>> from keysight.ads.dds.experimental import DDSQtWidget
        >>>
        >>> dds_file = new_dds_file()
        >>> page = dds_file.pages[0]
        >>> box = Rect(top=0,left=0,bottom=100,right=200)
        >>> page.add_box(box)
        >>>
        >>> ddswidget = DDSQtWidget(ddsfile=dds_file)
        >>>
        >>> pixmap = QPixmap(1024, 1024)
        >>> pixmap.fill(Qt.white)
        >>> painter = QPainter(pixmap)
        >>>
        >>> ddswidget.render_dds_widget(painter)
        >>>
        >>> painter.end()
        >>> pixmap.save("example.png")
        ```

        Render the Data Display Qt Widget to a printer using QPrinter.

        ```
        >>> from PySide6.QtPrintSupport import QPrinter, QPrintDialog
        >>> from PySide6.QtGui import QPainter
        >>> from keysight.ads.dds import Rect, new_dds_file
        >>> from keysight.ads.dds.experimental import DDSQtWidget
        >>>
        >>> ddsfile = new_dds_file()
        >>> page = ddsfile.pages[0]
        >>> box = Rect(top=0,left=0,bottom=100,right=200)
        >>> page.add_box(box)
        >>>
        >>> ddswidget = DDSQtWidget()
        >>> ddswidget.set_dds_file(ddsfile)
        >>>
        >>> printer = QPrinter(QPrinter.HighResolution)
        >>> print_dialog = QPrintDialog(printer, ddswidget)
        >>> if print_dialog.exec() == QPrintDialog.Accepted:
        ...     painter = QPainter(printer)
        ...     ddswidget.render_dds_widget(painter)
        ...     painter.end()
        ```

    set\_dds\_file(*ddsfile: [DDSFile](../file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile")*) → None[](#keysight.ads.dds.experimental.DDSQtWidget.set_dds_file "Link to this definition")
    :   Set the `DDSFile` to be utilized by this widget.

        Set the DDSFile object utilized by the Data Display Qt Widget.
        If the DDSFile has been assigned previously the current Data
        Display Window and associated Page will be set to default values.

        Parameters:
        :   **ddsfile** ([*DDSFile*](../file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile")) – The DDSFile object utilized by the widget.

    set\_page(*page: [Page](../page.md#keysight.ads.dds.Page "keysight.ads.dds.core.ddpage.Page")*) → None[](#keysight.ads.dds.experimental.DDSQtWidget.set_page "Link to this definition")
    :   Set the `Page` to be viewed by this widget.

        Set the page that is to be viewed by the widget. By
        default the page will be the first page in the DDSFile.

        Parameters:
        :   **page** (*Data Display Page*) – The page to be viewed by the widget.

    set\_zoom\_rectangle(*zoomRect: [Rect](../rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → None[](#keysight.ads.dds.experimental.DDSQtWidget.set_zoom_rectangle "Link to this definition")
    :   Set the current zoom rectangle (in dds database units).

    staticMetaObject *= PySide6.QtCore.QMetaObject("DDSQtWidget" inherits "QWidget": )*[](#keysight.ads.dds.experimental.DDSQtWidget.staticMetaObject "Link to this definition")

    use\_dds\_background\_color(*enable: bool*) → None[](#keysight.ads.dds.experimental.DDSQtWidget.use_dds_background_color "Link to this definition")

    zoom\_all() → None[](#keysight.ads.dds.experimental.DDSQtWidget.zoom_all "Link to this definition")
    :   Set the current view to display all the object in the window.

    zoom\_in\_by\_2() → None[](#keysight.ads.dds.experimental.DDSQtWidget.zoom_in_by_2 "Link to this definition")
    :   Zoom the current view in by a factor of 2.

    zoom\_out\_by\_2() → None[](#keysight.ads.dds.experimental.DDSQtWidget.zoom_out_by_2 "Link to this definition")
    :   Zoom the current view out by a factor of 2.

On this page

[Previous

keysight.ads.dds.experimental](index.md)
[Next

keysight.ads.dds.app](../app/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top