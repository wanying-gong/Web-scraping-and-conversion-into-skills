<!-- 来源: reference\dds\index.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* keysight.ads.dds

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
  + keysight.ads.dds
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

# keysight.ads.dds[](#module-keysight.ads.dds "Link to this heading")

ADS Data Display scripting.

Automate the Data Display Environment using the `keysight.ads.dds` package. This is typically
imported as:

```
from keysight.ads import dds
```

## Classes[](#classes "Link to this heading")

* [DDSFile](file.md)
  + [`DDSFile`](file.md#keysight.ads.dds.DDSFile)
* [Page](page.md)
  + [`Page`](page.md#keysight.ads.dds.Page)
* [Point](point.md)
  + [`Point`](point.md#keysight.ads.dds.Point)
* [Rect](rect.md)
  + [`Rect`](rect.md#keysight.ads.dds.Rect)
* [Grid](grid.md)
  + [`GridType`](grid.md#keysight.ads.dds.GridType)
* [Plots](plots.md)
  + [`AntennaPlot`](plots.md#keysight.ads.dds.AntennaPlot)
  + [`Listing`](plots.md#keysight.ads.dds.Listing)
  + [`PolarPlot`](plots.md#keysight.ads.dds.PolarPlot)
  + [`RectPlot`](plots.md#keysight.ads.dds.RectPlot)
  + [`Slider`](plots.md#keysight.ads.dds.Slider)
  + [`SmithChart`](plots.md#keysight.ads.dds.SmithChart)
  + [`StackedPlot`](plots.md#keysight.ads.dds.StackedPlot)
* [Axes](axes.md)
  + [`AntennaIndepAxis`](axes.md#keysight.ads.dds.AntennaIndepAxis)
  + [`AntennaDepAxis`](axes.md#keysight.ads.dds.AntennaDepAxis)
  + [`PolarIndepAxis`](axes.md#keysight.ads.dds.PolarIndepAxis)
  + [`PolarDepAxis`](axes.md#keysight.ads.dds.PolarDepAxis)
  + [`RectAxis`](axes.md#keysight.ads.dds.RectAxis)
  + [`SmithChartIndepAxis`](axes.md#keysight.ads.dds.SmithChartIndepAxis)
  + [`SmithChartDepAxis`](axes.md#keysight.ads.dds.SmithChartDepAxis)
  + [`TextAxis`](axes.md#keysight.ads.dds.TextAxis)
* [Legend](legend.md)
  + [`Legend`](legend.md#keysight.ads.dds.Legend)
* [Trace](trace.md)
  + [`Trace`](trace.md#keysight.ads.dds.Trace)
  + [`TextTrace`](trace.md#keysight.ads.dds.TextTrace)
* [Markers](marker.md)
  + [`TraceMarker`](marker.md#keysight.ads.dds.TraceMarker)
  + [`MarkerType`](marker.md#keysight.ads.dds.MarkerType)
  + [`MarkerMode`](marker.md#keysight.ads.dds.MarkerMode)
  + [`MarkerReadoutContentProperties`](marker.md#keysight.ads.dds.MarkerReadoutContentProperties)
  + [`TraceMarkerSymbol`](marker.md#keysight.ads.dds.TraceMarkerSymbol)
  + [`TraceMarkerSymbolProperties`](marker.md#keysight.ads.dds.TraceMarkerSymbolProperties)
* [Line Markers](linemarker.md)
  + [`LineMarker`](linemarker.md#keysight.ads.dds.LineMarker)
  + [`LineMarkerSymbolProperties`](linemarker.md#keysight.ads.dds.LineMarkerSymbolProperties)
* [Limit Lines](limitlines.md)
  + [`LimitLine`](limitlines.md#keysight.ads.dds.LimitLine)
  + [`LimitLineType`](limitlines.md#keysight.ads.dds.LimitLineType)
* [Masks](masks.md)
  + [`LineMask`](masks.md#keysight.ads.dds.LineMask)
  + [`PolygonMask`](masks.md#keysight.ads.dds.PolygonMask)
  + [`PolylineMask`](masks.md#keysight.ads.dds.PolylineMask)
  + [`RectMask`](masks.md#keysight.ads.dds.RectMask)
* [Specification](specifications.md)
  + [`Specification`](specifications.md#keysight.ads.dds.Specification)
* [Equation](equation.md)
  + [`Equation`](equation.md#keysight.ads.dds.Equation)
* [PyEquation](pyequation.md)
  + [`PyEquation`](pyequation.md#keysight.ads.dds.PyEquation)
* [Text](text.md)
  + [`Text`](text.md#keysight.ads.dds.Text)
* [Picture](picture.md)
  + [`Picture`](picture.md#keysight.ads.dds.Picture)
* [Shapes](shapes.md)
  + [`Box`](shapes.md#keysight.ads.dds.Box)
  + [`Circle`](shapes.md#keysight.ads.dds.Circle)
  + [`Line`](shapes.md#keysight.ads.dds.Line)
  + [`Polyline`](shapes.md#keysight.ads.dds.Polyline)
  + [`Polygon`](shapes.md#keysight.ads.dds.Polygon)
* [Group](group.md)
  + [`Group`](group.md#keysight.ads.dds.Group)
* [Common Properties](basic.md)
  + [`Color`](basic.md#keysight.ads.dds.Color)
  + [`DensitySymbolProperties`](basic.md#keysight.ads.dds.DensitySymbolProperties)
  + [`FillProperties`](basic.md#keysight.ads.dds.FillProperties)
  + [`LineProperties`](basic.md#keysight.ads.dds.LineProperties)
  + [`LineType`](basic.md#keysight.ads.dds.LineType)
  + [`SymbolProperties`](basic.md#keysight.ads.dds.SymbolProperties)
  + [`TextProperties`](basic.md#keysight.ads.dds.TextProperties)
  + [`StringFormat`](basic.md#keysight.ads.dds.StringFormat)
* [Print](print.md)
  + [`PaperSize`](print.md#keysight.ads.dds.PaperSize)
  + [`PrinterOrientation`](print.md#keysight.ads.dds.PrinterOrientation)
* [Object](objects.md)
  + [`ObjectType`](objects.md#keysight.ads.dds.ObjectType)
* [Window](windows.md)
  + [`Window`](windows.md#keysight.ads.dds.Window)
* [Widget](pywidget.md)
  + [`Widget`](pywidget.md#keysight.ads.dds.Widget)

## Functions[](#functions "Link to this heading")

keysight.ads.dds.get\_dds\_path() → str[](#keysight.ads.dds.get_dds_path "Link to this definition")
:   Return the path of the current working directory.

    Returns:
    :   Path of the current working directory.
        In application mode, if running in ADS (Advanced Design System), it is set by default to the path of the opened workspace.
        In application mode, if running in standalone DDS (Data Display), it is set by default to the path from which DDS was invoked.
        In automation mode, it is set by default to the path from which python was invoked.
        This path may be set by [`init_dds_path()`](#keysight.ads.dds.init_dds_path "keysight.ads.dds.init_dds_path").

    Return type:
    :   string

    Examples

    ```
    >>> from keysight.ads import dds
    >>> dds_path = dds.dds.get_dds_path()
    ```

keysight.ads.dds.init\_dds\_path(*path: str | PathLike*) → None[](#keysight.ads.dds.init_dds_path "Link to this definition")
:   Initialize the dds path.

    The dds path is the path used as a default path in the functions [`new_dds_file()`](#keysight.ads.dds.new_dds_file "keysight.ads.dds.new_dds_file"), [`open_dds_file()`](#keysight.ads.dds.open_dds_file "keysight.ads.dds.open_dds_file") and
    [`save()`](file.md#keysight.ads.dds.DDSFile.save "keysight.ads.dds.DDSFile.save").
    It is typically set once per python script.
    In application mode, if running in ADS (Advanced Design System), it is set by default to the path of the opened workspace.
    In application mode, if running in standalone DDS (Data Display), it is set by default to the path from which DDS was invoked.
    In automation mode, it is set by default to the path from which python was invoked.
    This path may be retrieved by [`get_dds_path()`](#keysight.ads.dds.get_dds_path "keysight.ads.dds.get_dds_path").

    Parameters:
    :   **path** (*str* *|* *os.PathLike*) – The path may be a relative path or an absolute path.

    Return type:
    :   None

    Example

    ```
    >>> from keysight.ads import dds
    >>> dds.init_dds_path("c:/tmp")
    ```

keysight.ads.dds.running\_automation() → bool[](#keysight.ads.dds.running_automation "Link to this definition")
:   Return True if running in Data Display automation mode.

    Return type:
    :   bool

keysight.ads.dds.version() → int[](#keysight.ads.dds.version "Link to this definition")
:   Return the product version.

    Returns:
    :   Example: 615

    Return type:
    :   int

keysight.ads.dds.product\_version() → str[](#keysight.ads.dds.product_version "Link to this definition")
:   Return a string with the product name, build version and date of build.

    Returns:
    :   Example: ‘Data Display Server (\*) 615.gDevelop Jul 25 2024 (64-bit)’

    Return type:
    :   str

keysight.ads.dds.close\_dds\_file(*file: [DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile")*) → None[](#keysight.ads.dds.close_dds_file "Link to this definition")
:   Close a DDSFile.

    If the DDSFile has modifications, the modifications will be lost.
    If running in application mode and the DDSFile is currently opened, the Data Display window will be closed.

    Parameters:
    :   **file** ([*DDSFile*](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile")) –

    Return type:
    :   None

    Raises:
    :   **RuntimeError: Error: Attempting to access a deleted object.** – This can occur in application mode when the window associated with DDSFile is closed interactively. In automation mode,
        this can occur if the DDSFile was previously closed.

keysight.ads.dds.get\_dds\_files() → NamedItemCollectionAbc[[DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile")][](#keysight.ads.dds.get_dds_files "Link to this definition")
:   Return a mutable list of opened DDSFiles.

    Return type:
    :   NamedItemCollectionAbc[[DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile")]

    Example

    Obtain a DDSFile named “test.dds” that is currently opened.

    ```
    >>> from keysight.ads import dds as dds
    >>> dds_file = None
    >>> if 'test' in dds.get_dds_files():
    >>>     dds_file = dds.get_dds_files()['test']
    ```

keysight.ads.dds.new\_dds\_file(*dataset: str | ~os.PathLike | None = None*, *path: str | ~os.PathLike | ~collections.abc.Callable[[]*, *str] | None = <function dds\_path>*) → [DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile")[](#keysight.ads.dds.new_dds_file "Link to this definition")
:   Create a new DDSFile and sets the [`data_path`](file.md#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path") and the [`default_dataset`](file.md#keysight.ads.dds.DDSFile.default_dataset "keysight.ads.dds.DDSFile.default_dataset").

    The DDSFile is only in memory until [`save()`](file.md#keysight.ads.dds.DDSFile.save "keysight.ads.dds.DDSFile.save") is called.
    If running in application mode, the new Data Display window will open and be visible.

    Parameters:
    :   * **dataset** (*str* *|* *os.PathLike* *[**optional**]*) – The name of the default dataset. It may be an absolute or relative path.
          It may or may not include the “.ds” extension.
          If the path is relative or omitted or not found, then the default dataset is set to the first
          dataset found in the dataset path (See 2nd parameter for details about the dataset path).
          If no default dataset can be found in the dataset path, it is
          set to whatever was passed, or if no parameter was passed, then it is set to “dataset”.
          The default dataset can be obtained from the property [`default_dataset`](file.md#keysight.ads.dds.DDSFile.default_dataset "keysight.ads.dds.DDSFile.default_dataset").
        * **path** (*str* *|* *os.PathLike* *|* *Callable**[**[**]**,* *str**]* *[**default = get\_dds\_path**(**)**]*) – It may be an absolute path, a relative path, or
          the name of a function that takes no parameters and returns a str that will be interpreted as a path.
          If the path is relative, it is joined to the path obtained from the function [`get_dds_path()`](#keysight.ads.dds.get_dds_path "keysight.ads.dds.get_dds_path").
          If it is omitted, the path is obtained from the function [`get_dds_path()`](#keysight.ads.dds.get_dds_path "keysight.ads.dds.get_dds_path").
          This path will also be used when the DDSFile is saved. See [`save()`](file.md#keysight.ads.dds.DDSFile.save "keysight.ads.dds.DDSFile.save").
          The path will be joined with the property [`data_path`](file.md#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path") and then reset that property
          to reflect the newly joined path. The dataset path is used to search for dataset files and can be
          obtained from the property [`data_path`](file.md#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path").

    Returns:
    :   When a new DDSFile is created, its dataset path and default dataset will be set.
        In addition, a [`Window`](windows.md#keysight.ads.dds.Window "keysight.ads.dds.Window") and the first [`Page`](page.md#keysight.ads.dds.Page "keysight.ads.dds.Page") will be created.

    Return type:
    :   [DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile")

    Examples

    Create a new DDSFile in the current directory indicated by the function get\_dds\_path() that will use
    the first dataset found in property data\_path. Assume the datasets in data\_path are: amplifier.ds, swept\_s\_param.ds.

    ```
    >>> from keysight.ads import dds as dds
    >>> print(get_dds_path())
        c:\\workspaces\\my_wrk
    >>> dds_file = dds.new_dds_file()
    >>> print(dds_file.data_path)
        c:\\workspaces\\my_wrk\\data
    >>> print(dds_file.default_dataset)
    >>> amplifier
    ```

    Create a new DDSFile in a specific ADS workspace and that will use the first dataset found in the property data\_path.
    Assume the datasets in data\_path are: amplifier.ds, swept\_s\_param.ds.

    ```
    >>> from keysight.ads import dds as dds
    >>> dds_file = dds.new_dds_file(None, "c:/tmp/my_wrk")
    >>> print(dds_file.data_path)
        c:\\tmp\\my_wrk\\data
    >>> print(dds_file.default_dataset)
    >>> amplifier
    ```

    Create a new DDSFile in a specific ADS workspace and that will use a specific dataset found in the property data\_path.
    Assume the datasets in data\_path are: amplifier.ds, swept\_s\_param.ds.

    ```
    >>> from keysight.ads import dds as dds
    >>> dds_file = dds.new_dds_file("swept_s_param", "c:/tmp/my_wrk")
    >>> print(dds_file.data_path)
        c:\\tmp\\my_wrk\\data
    >>> print(dds_file.default_dataset)
        swept_s_param
    ```

    Create a new DDSFile and set the dataset to a dataset not found in the data\_path.
    Assume the datasets in data\_path are: amplifier.ds, swept\_s\_param.ds.

    ```
    >>> from keysight.ads import dds as dds
    >>> dds_file = dds.new_dds_file("c:/datasets/sim1.ds", "c:/my_data")
    >>> print(dds_file.data_path)
        c:\\my_data\\data
    >>> print(dds_file.default_dataset)
        c:\\datasets\\sim1.ds
    ```

    See also

    [`default_dataset`](file.md#keysight.ads.dds.DDSFile.default_dataset "keysight.ads.dds.DDSFile.default_dataset")
    :   The default dataset being used by the DDSFile.

    [`data_path`](file.md#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path")
    :   The default dataset being used by the DDSFile.

keysight.ads.dds.open\_dds\_file(*path: str | PathLike*) → [DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile")[](#keysight.ads.dds.open_dds_file "Link to this definition")
:   Open a DDSFile.

    If running in application mode, a new Data Display window will open and show contents of the DDSFile.

    Parameters:
    :   **path** (*str* *|* *os.PathLike*) – The name of the DDSFile to open. It may be an absolute or relative path.
        The file must include the “.dds” extension.
        If the path is relative, it is joined to the path obtained from the function [`get_dds_path()`](#keysight.ads.dds.get_dds_path "keysight.ads.dds.get_dds_path").

    Return type:
    :   [DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile")

    Raises:
    :   * **RuntimeError: The file path is empty.** –
        * **RuntimeError: The file does not exist: <path>** –

    Example

    Modify a DDSFile.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> ddsfile.new_page("newPage")
    >>> ddsfile.save()
    ```

On this page

[Previous

Reference](../index.md)
[Next

DDSFile](file.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top