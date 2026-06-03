<!-- 来源: reference\dds\file.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* DDSFile

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
    - DDSFile
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

# DDSFile[](#ddsfile "Link to this heading")

*class* keysight.ads.dds.DDSFile[](#keysight.ads.dds.DDSFile "Link to this definition")
:   The top of the graphical object structure associated with a Data Display file.

    This class cannot be instantiated directly, but instead
    is created and returned when a Data Display file is created or opened.

    See also

    [`new_dds_file()`](index.md#keysight.ads.dds.new_dds_file "keysight.ads.dds.new_dds_file")
    :   Create a new Data Display file.

    [`open_dds_file()`](index.md#keysight.ads.dds.open_dds_file "keysight.ads.dds.open_dds_file")
    :   Open an existing Data Display file.

    \_\_init\_\_(*\*args*, *\*\*kwargs*) → None[](#keysight.ads.dds.DDSFile.__init__ "Link to this definition")

    add\_dataset\_alias(*name: str*, *path: str*) → None[](#keysight.ads.dds.DDSFile.add_dataset_alias "Link to this definition")
    :   Add a dataset alias to the [`dataset_aliases`](#keysight.ads.dds.DDSFile.dataset_aliases "keysight.ads.dds.DDSFile.dataset_aliases") properties.

        A dataset alias is a short name mapped to a full path of a dataset.

        Parameters:
        :   * **name** (*str*) – A short name for the dataset alias to add.
            * **path** (*str*) – The path to the dataset. It may be an absolute path or a relative path, and it may include environment variables.

        Return type:
        :   None

    add\_external\_dataset\_path(*path: str | PathLike*) → None[](#keysight.ads.dds.DDSFile.add_external_dataset_path "Link to this definition")
    :   Add a dataset path to the [`external_dataset_paths`](#keysight.ads.dds.DDSFile.external_dataset_paths "keysight.ads.dds.DDSFile.external_dataset_paths") property.

        Parameters:
        :   **name** (*str* *|* *os.PathLike*) – The path to the dataset. It may be an absolute or relative path.

        Return type:
        :   None

    change\_page(*name: str*, *win: [Window](windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window") | None = None*) → None[](#keysight.ads.dds.DDSFile.change_page "Link to this definition")
    :   Change which [`Page`](page.md#keysight.ads.dds.Page "keysight.ads.dds.Page") will be displayed when the DDSFile is opened in Data Display.

        If running in automation mode and the DDSFile is saved after the change\_page(), the next time the DDSFile is
        opened in the Data Display application, it will open to the page specified.
        If running in application mode and the DDSFile is currently opened, the specified page will be displayed immediately.

        Parameters:
        :   * **name** (*str*) – The name of the page to be displayed.
            * **win** ([*Window*](windows.md#keysight.ads.dds.Window "keysight.ads.dds.Window") *[**optional**]*) – The window which will display the changed page. If this parameter is omitted, the change page will only
              occur on the default page, which is the page that was created when the DDSFile was initially created.

        Return type:
        :   None

        Raises:
        :   **RuntimeError: Unable to find page {"<page name>"}.** – This exception occurs if the specified Page name is not found in DDSfile.

        Examples

        Change pages so that next time the DDSFile is opened in the Data Display application, it displays the first page
        on the first window, and displays the last page in the 2nd window.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.new_dds_file()
        >>> lastIndx = len(dds_file.pages)
        >>> dds_file.new_window()
        >>> dds_file.change_page(dds_file.pages[0], dds_file.windows[0])
        >>> dds_file.change_page(dds_file.pages[lastIndx - 1].name, dds_file.windows[1])
        >>> dds_file.save()
        ```

        Change the page on the default window of DDSFile. Note that when a new page is created in DDSFile, it becomes
        the page that will be displayed in the default window.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds_file = dds.new_dds_file()
        >>> ddsfile.new_page("page 2")
        >>> print(ddsfile.windows[0].current_page)
            page 2
        >>> ddsfile.change_page("page 1")
        >>> print(ddsfile.windows[0].current_page)
            page 1
        >>> ddsfile.save()
        ```

    close(*force: bool | None = None*) → None[](#keysight.ads.dds.DDSFile.close "Link to this definition")
    :   Close the DDSfile.

        Parameters:
        :   **force** (*bool* *[**optional**,* *default=False**]*) – A boolean parameter to control how a modified DDSFile is
            closed. When True any modification will be discarded and
            the DDSFile will be closed. When False (default value)
            attempting to close a modified DDSFile will raise an
            error leaving the DDSFile open.

        Return type:
        :   None

        Raises:
        :   **RuntimeError: Unable to close the modified object.** – Raised when attempting to close a modified DDSFile object and force is not True.

        Examples

        Close a file that was saved

        ```
        >>> from keysight.ads import dds
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot()
        >>> dds_file.save("test.dds")
        >>> dds_file.close()
        >>> print(dds.get_dds_files())
        ()
        ```

        Close a modified file with the force option

        ```
        >>> from keysight.ads import dds
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot()
        >>> dds_file.close(True)
        >>> print(dds.get_dds_files())
        ()
        ```

        See also

        [`close_dds_file()`](index.md#keysight.ads.dds.close_dds_file "keysight.ads.dds.close_dds_file")
        :   Close a Data Display file.

        [`save()`](#keysight.ads.dds.DDSFile.save "keysight.ads.dds.DDSFile.save")
        :   Save a modified Data Display file.

    close\_window(*win: [Window](windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window")*) → None[](#keysight.ads.dds.DDSFile.close_window "Link to this definition")
    :   Close a window viewing the DDSFile.

        There must always be one window available.

        Parameters:
        :   **win** ([*Window*](windows.md#keysight.ads.dds.Window "keysight.ads.dds.Window")) – The window to delete.

        Return type:
        :   None

    *property* data\_path*: str*[](#keysight.ads.dds.DDSFile.data_path "Link to this definition")
    :   The relative path to a subfolder or a full path that specifies the directory in which the dataset file is located.

        Default value is “./data”. It is reset in [`new_dds_file()`](index.md#keysight.ads.dds.new_dds_file "keysight.ads.dds.new_dds_file") or [`open_dds_file()`](index.md#keysight.ads.dds.open_dds_file "keysight.ads.dds.open_dds_file").

    *property* dataset\_aliases*: dict[str, str]*[](#keysight.ads.dds.DDSFile.dataset_aliases "Link to this definition")
    :   A dictionary that contains the dataset aliases.

        The key-value pairs are [<alias name>, <path>].

        See also

        [`add_dataset_alias()`](#keysight.ads.dds.DDSFile.add_dataset_alias "keysight.ads.dds.DDSFile.add_dataset_alias")
        :   Add a dataset alias to this property.

        [`remove_dataset_alias()`](#keysight.ads.dds.DDSFile.remove_dataset_alias "keysight.ads.dds.DDSFile.remove_dataset_alias")
        :   Remove a dataset alias to this property.

    *property* default\_dataset*: str*[](#keysight.ads.dds.DDSFile.default_dataset "Link to this definition")
    :   The name of the default dataset file.

        The file name may or may not include the extension “.ds”. If it is specified
        as a file name or relative path, the dataset file lives in the directory pointed to by the [`data_path`](#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path") property. It
        may also be specified with an absolute path.

        If the file is not found, the default\_dataset is set to the first dataset file found in the [`data_path`](#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path") property. If no
        default dataset file can be found, then the default\_dataset is set to “dataset”. If default\_dataset cannot be set
        to the specified value, a message is printed to the output.

        Example

        Set the default dataset and ensure that it was found

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file('c:/tmp/MyWorkspace_wrk/myDDSfile.dds')
        >>> dds_file.default_dataset = "myDataset"
        >>> if dds_file.default_dataset != "myDataset":
        >>>     exit()
        ```

    delete\_page(*name: str*) → None[](#keysight.ads.dds.DDSFile.delete_page "Link to this definition")
    :   Delete a page from the DDSFile.

        Each DDSFile is required to have at least one page.
        Any windows viewing that page will have the page changed to the next page or the
        first page if the last page is deleted.
        A list of pages in a DDSFile can be obtained from the [`pages`](#keysight.ads.dds.DDSFile.pages "keysight.ads.dds.DDSFile.pages") property.

        Parameters:
        :   **name** (*str*) – The name of the Page to be renamed.

        Return type:
        :   None

        Raises:
        :   * **RuntimeError: Unable to find page {"<page name>"}.** – This exception occurs if the specified Page name to rename is not found in the DDSFile.
            * **RuntimeError: You cannot delete the last page in a DDS window. The page delete operation has been cancelled.** – This exception occurs if the DDSFile has only 1 page.
            * **RuntimeError: Error deleting current page.** – This exception occurs if for an unknown reason, the page cannot be deleted.

        Example

        Delete a page in the DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.new_dds_file()
        >>> dds_file.new_window()
        >>> dds_file.new_page("readme")
        >>> print(dds_file.pages)
            (<Page "page 1">, <Page "readme">)
        >>> dds_file.delete("page 1")
        >>> print(dds_file.pages)
            (<Page "readme">,)
        >>> dds_file.save()
        ```

    *property* dot\_grid\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.DDSFile.dot_grid_color "Link to this definition")
    :   The color of the dot grid for pages in the DDSFile.

    *property* external\_dataset\_paths*: list[str]*[](#keysight.ads.dds.DDSFile.external_dataset_paths "Link to this definition")
    :   A list of paths to datasets that can be accessed in the DDSFile.

        See also

        [`add_external_dataset_path()`](#keysight.ads.dds.DDSFile.add_external_dataset_path "keysight.ads.dds.DDSFile.add_external_dataset_path")
        :   Add a dataset path to this property.

        [`remove_external_dataset_path()`](#keysight.ads.dds.DDSFile.remove_external_dataset_path "keysight.ads.dds.DDSFile.remove_external_dataset_path")
        :   Remove a dataset path to this property.

    get\_closest\_grid\_point(*value: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")[](#keysight.ads.dds.DDSFile.get_closest_grid_point "Link to this definition")
    :   Return the closest grid point to the specified Point or tuple.

        Parameters:
        :   **value** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – Point or tuple that represents a point on the a page of the DDSFile.

        Return type:
        :   [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point")

        Example

        Insert a plot at a specific point on the page.

        ```
        >>> from keysight.ads import dds as dds
        >>> tmp_workspace_path = 'c:/tmp/MyWorkspace_wrk'
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> snapPt = dds_file.get_closest_grid_point(dds.Point(100,100))
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot(snapPt)
        >>> dds_file.save("test.dds")
        ```

    *property* grid\_on*: bool*[](#keysight.ads.dds.DDSFile.grid_on "Link to this definition")
    :   Indicates if the grid is on for pages in the DDSFile.

    *property* grid\_type*: [GridType](grid.md#keysight.ads.dds.GridType "keysight.ads.dds.core.ddobj.GridType")*[](#keysight.ads.dds.DDSFile.grid_type "Link to this definition")
    :   The grid type for pages in the DDSFile.

    insert\_template(*path: str | PathLike*) → None[](#keysight.ads.dds.DDSFile.insert_template "Link to this definition")
    :   Insert a Data Display Template into the DDSFile.

        Parameters:
        :   **name** (*str* *|* *os.PathLike*) – The path to the template. It may be an absolute or relative path.
            It may or may not include the “.ddt” extension. However, the actual file must have the extension “.ddt”.

        Return type:
        :   None

        Example

        Insert the Data Display Template “myPlot” into a DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> dds_file.insert_template("c:/tmp/myPlot")
        ```

        See also

        [`save_as_template()`](#keysight.ads.dds.DDSFile.save_as_template "keysight.ads.dds.DDSFile.save_as_template")
        :   Save a DDSFile to a Data Display template file.

    *property* is\_history\_paused*: bool*[](#keysight.ads.dds.DDSFile.is_history_paused "Link to this definition")
    :   Indicates whether or not history mode is paused on all plots.

        Return type:
        :   bool

    *property* is\_modified*: bool*[](#keysight.ads.dds.DDSFile.is_modified "Link to this definition")
    :   The modified status of the Data Display file.

    *property* line\_grid\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.DDSFile.line_grid_color "Link to this definition")
    :   The color of the line grid for pages in the DDSFile.

    *property* name*: str*[](#keysight.ads.dds.DDSFile.name "Link to this definition")

    *property* named\_views*: dict[str, [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")]*[](#keysight.ads.dds.DDSFile.named_views "Link to this definition")

    new\_page(*name: str*) → [Page](page.md#keysight.ads.dds.Page "keysight.ads.dds.core.ddpage.Page")[](#keysight.ads.dds.DDSFile.new_page "Link to this definition")
    :   Return a new Page.

        When a new page is created, it becomes the page being viewed in the default window.
        A list of pages in a DDSFile can be obtained from the [`pages`](#keysight.ads.dds.DDSFile.pages "keysight.ads.dds.DDSFile.pages") property.

        Parameters:
        :   **name** (*str*) – The name of the new Page

        Returns:
        :   If a page with the “name” parameter already exists, a unique page name will be determined by adding
            a space followed by a unique number to the end of “name”.

        Return type:
        :   [Page](page.md#keysight.ads.dds.Page "keysight.ads.dds.Page")

        Raises:
        :   * **RuntimeError: Page name is too long.** – Page names cannot exceed 1023 characters.
            * **RuntimeError: Unable to get new page object.** – This exception occurs if the new page was not created.
            * **RuntimeError: Page not created because "<name>" is an existing page.** – Pages must have a unique name.
            * **RuntimeError: Page not created because "<name>" has leading** **or** **trailing whitespace.** – Page names cannot have any leading or trailing whitespace.

        Example

        Create two new pages.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.new_dds_file()
        >>> page1 = dds_file.new_page("myNewPage")
        >>> print(page1.name)
            myNewPage
        >>> page2 = dds_file.new_page("myNewPage")
        >>> print(page2.name)
            myNewPage 1
        >>> print(dds_file.pages)
            (<Page "page 1">, <Page "myNewPage">, <Page "myNewPage 1">)
        >>> print(dds_file.window[0].current_page)
            myNewPage 1
        >>> print(dds_file.window[1].current_page)
            page 1
        ```

    new\_window() → [Window](windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window")[](#keysight.ads.dds.DDSFile.new_window "Link to this definition")
    :   Create an additional window viewing the contents of a page in the DDSFile.

        Each DDSFile can have multiple windows. Multiple windows can view the same or
        different pages and can be scaled to display different views of the page.
        A list of windows in a DDSFile can be obtained from the [`windows`](#keysight.ads.dds.DDSFile.windows "keysight.ads.dds.DDSFile.windows") property.

        Returns:
        :   The new window.

        Return type:
        :   [Window](windows.md#keysight.ads.dds.Window "keysight.ads.dds.Window")

        Example

        Create a new window for DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.new_dds_file()
        >>> win = ddsfile.new_window()
        >>> ddsfile.windows
            [<Window "">, <Window "">]
        ```

    *property* pages*: NamedItemCollectionAbc[[Page](page.md#keysight.ads.dds.Page "keysight.ads.dds.core.ddpage.Page")]*[](#keysight.ads.dds.DDSFile.pages "Link to this definition")
    :   A collection of pages contained in the DDSFile.

        The collection reflects the order in which the pages were created.
        This property is Read-only. Use class methods to modify the collection.

        Examples

        Check if a page exists.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.new_dds_file()
        >>> exists = "page 1" in dds_file.pages
        ```

        Access a page by name.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.new_dds_file()
        >>> if 'page 1' in dds_file.pages:
        >>>     page = dds_file.pages['page 1']
        ```

        Access a page by index.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.new_dds_file()
        >>> page = ddsfile.pages[0]
        ```

        See also

        [`new_page()`](#keysight.ads.dds.DDSFile.new_page "keysight.ads.dds.DDSFile.new_page")
        :   Create a new Page.

        [`rename_page()`](#keysight.ads.dds.DDSFile.rename_page "keysight.ads.dds.DDSFile.rename_page")
        :   Rename a Page.

        [`delete_page()`](#keysight.ads.dds.DDSFile.delete_page "keysight.ads.dds.DDSFile.delete_page")
        :   Delete a Page.

        [`change_page()`](#keysight.ads.dds.DDSFile.change_page "keysight.ads.dds.DDSFile.change_page")
        :   Change page being viewed.

        [`Window.page_name_order`](windows.md#keysight.ads.dds.Window.page_name_order "keysight.ads.dds.Window.page_name_order")
        :   Change the display order of the pages.

    print\_all\_pages(*file: str | PathLike*, *orientation: [PrinterOrientation](print.md#keysight.ads.dds.PrinterOrientation "keysight.ads.dds.core.ddobj.PrinterOrientation") | str = PrinterOrientation.LANDSCAPE*, *size: [PaperSize](print.md#keysight.ads.dds.PaperSize "keysight.ads.dds.core.ddobj.PaperSize") | str = PaperSize.LETTER*, *fit\_to\_page: bool = True*) → None[](#keysight.ads.dds.DDSFile.print_all_pages "Link to this definition")
    :   Print all pages of DDSFile to a file.

        Parameters:
        :   * **file** (*str* *|* *os.PathLike*) – The path to the new file. This may be an absolute or relative path.
              The extension determines the output file (e.g., “.pdf” for PDF files or “.png” for PNG files).
              Note: Images may be saved as multiple files.
            * **orientation** ([*PrinterOrientation*](print.md#keysight.ads.dds.PrinterOrientation "keysight.ads.dds.PrinterOrientation") *|* *str* *[**optional**,* *default=PrinterOrientation.LANDSCAPE**]*) – The orientation of the file. :class: dds.PrinterOrientation
            * **size** ([*PaperSize*](print.md#keysight.ads.dds.PaperSize "keysight.ads.dds.PaperSize") *|* *str* *[**optional**,* *default=PaperSize.LETTER**]*) – The paper size to use in the file. :class: dds.PaperSize
            * **fit\_to\_page** (*bool* *[**optional**,* *default=True**]*) – If True, the pages in DDSFile may be scaled to fit on a printed page. Otherwise, the pages in the DDSFile are not scaled.

        Return type:
        :   None

        Raises:
        :   * **RuntimeError: Invalid data display object.** – This exception occurs if the DDSFile is invalid.
            * **RuntimeError: Unable to open the gplot printer.** – Unable to access printer.
            * **RuntimeError: PrinterOrientation has no value** – <str>.: The string passed to the orientation parameter does not correspond to a valid PrinterOrientation value.
            * **RuntimeError: PaperSize has no value** – <str>.: The string passed to the size parameter does not correspond to a valid PaperSize value.

        Example

        Print all pages of a DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> ddsfile.print_all_pages("x.pdf", dds.PrinterOrientation.PORTRAIT, dds.PaperSize.A0, False)
        ```

        See also

        [`print_pages_by_name()`](#keysight.ads.dds.DDSFile.print_pages_by_name "keysight.ads.dds.DDSFile.print_pages_by_name")
        :   Print specific pages to a file.

    print\_all\_pages\_to\_pdf(*pdf: str | PathLike*, *orientation: [PrinterOrientation](print.md#keysight.ads.dds.PrinterOrientation "keysight.ads.dds.core.ddobj.PrinterOrientation") | str = PrinterOrientation.LANDSCAPE*, *size: [PaperSize](print.md#keysight.ads.dds.PaperSize "keysight.ads.dds.core.ddobj.PaperSize") | str = PaperSize.LETTER*, *fit\_to\_page: bool = True*) → None[](#keysight.ads.dds.DDSFile.print_all_pages_to_pdf "Link to this definition")
    :   Print all pages of DDSFile to a pdf file.

        print\_all\_pages\_to\_pdf is deprecated, and will be removed in the 2027 release. Use: print\_all\_pages

    print\_pages\_by\_name(*file: str | PathLike*, *pages: list[str]*, *orientation: [PrinterOrientation](print.md#keysight.ads.dds.PrinterOrientation "keysight.ads.dds.core.ddobj.PrinterOrientation") | str = PrinterOrientation.LANDSCAPE*, *size: [PaperSize](print.md#keysight.ads.dds.PaperSize "keysight.ads.dds.core.ddobj.PaperSize") | str = PaperSize.LETTER*, *fit\_to\_page: bool = True*) → None[](#keysight.ads.dds.DDSFile.print_pages_by_name "Link to this definition")
    :   Print specific pages of DDSFile to a file.

        Parameters:
        :   * **file** (*str* *|* *os.PathLike*) – The path to the new file. This may be an absolute or relative path. The extension determines the output file (e.g., “.pdf” for PDF files or “.png” for PNG files).
            * **pages** (*list**[**str**]*) – A list of pages specified by strings. Each page will be printed to the file.
            * **orientation** ([*PrinterOrientation*](print.md#keysight.ads.dds.PrinterOrientation "keysight.ads.dds.PrinterOrientation") *|* *str* *[**optional**,* *default=PrinterOrientation.LANDSCAPE**]*) – The orientation of the file. :class: dds.PrinterOrientation
            * **size** ([*PaperSize*](print.md#keysight.ads.dds.PaperSize "keysight.ads.dds.PaperSize") *|* *str* *[**optional**,* *default=PaperSize.LETTER**]*) – The paper size to use in the printed file. :class: dds.PaperSize
            * **fit\_to\_page** (*bool* *[**optional**,* *default=True**]*) – If True, the pages in DDSFile may be scaled to fit on a printed page. Otherwise, the pages in the DDSFile are not scaled.

        Return type:
        :   None

        Raises:
        :   * **RuntimeError: Invalid data display object.** – This exception occurs if the DDSFile is invalid.
            * **RuntimeError: Unable to open the gplot printer.** – Unable to access printer.
            * **RuntimeError: PrinterOrientation has no value** – <str>.: The string passed to the orientation parameter does not correspond to a valid PrinterOrientation value.
            * **RuntimeError: PaperSize has no value** – <str>.: The string passed to the size parameter does not correspond to a valid PaperSize value.

        Example

        Print all pages of a DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> ddsfile.print_pages_by_name("x.pdf", ["page 1"])
        ```

        See also

        [`print_all_pages()`](#keysight.ads.dds.DDSFile.print_all_pages "keysight.ads.dds.DDSFile.print_all_pages")
        :   Print all pages to a file.

    print\_pages\_by\_name\_to\_pdf(*pdf: str | PathLike*, *pages: list[str]*, *orientation: [PrinterOrientation](print.md#keysight.ads.dds.PrinterOrientation "keysight.ads.dds.core.ddobj.PrinterOrientation") | str = PrinterOrientation.LANDSCAPE*, *size: [PaperSize](print.md#keysight.ads.dds.PaperSize "keysight.ads.dds.core.ddobj.PaperSize") | str = PaperSize.LETTER*, *fit\_to\_page: bool = True*) → None[](#keysight.ads.dds.DDSFile.print_pages_by_name_to_pdf "Link to this definition")
    :   Print named pages of DDSFile to a pdf file.

        print\_pages\_by\_name\_to\_pdf is deprecated, and will be removed in the 2027 release. Use: print\_pages\_by\_name

    recalculate\_equations() → None[](#keysight.ads.dds.DDSFile.recalculate_equations "Link to this definition")
    :   Recalculate all expressions in the DDSFile.

        This method forces all expressions to be recalculated for expressions that may depend on external objects and files.

    reload\_default\_dataset() → None[](#keysight.ads.dds.DDSFile.reload_default_dataset "Link to this definition")
    :   Reload default dataset and recalculate dependent equations.

    remove\_dataset\_alias(*name: str*) → None[](#keysight.ads.dds.DDSFile.remove_dataset_alias "Link to this definition")
    :   Remove a dataset alias from the [`dataset_aliases`](#keysight.ads.dds.DDSFile.dataset_aliases "keysight.ads.dds.DDSFile.dataset_aliases") property.

        A dataset alias is a short name mapped to a full path of a dataset.

        Parameters:
        :   **name** (*str*) – Name of the dataset alias to remove.

        Return type:
        :   None

    remove\_external\_dataset\_path(*path: str | PathLike*) → None[](#keysight.ads.dds.DDSFile.remove_external_dataset_path "Link to this definition")
    :   Remove a dataset path from the [`external_dataset_paths`](#keysight.ads.dds.DDSFile.external_dataset_paths "keysight.ads.dds.DDSFile.external_dataset_paths") property.

        Parameters:
        :   **name** (*str* *|* *os.PathLike*) – The path to the dataset. It may be an absolute or relative path.

        Return type:
        :   None

    rename\_page(*name: str*, *new\_name: str*) → None[](#keysight.ads.dds.DDSFile.rename_page "Link to this definition")
    :   Rename a page.

        The rename is effective in all windows in the DDSFile.

        Parameters:
        :   * **name** (*str*) – The name of the page to be renamed.
            * **new\_name** (*str*) – The new name of the page.

        Return type:
        :   None

        Raises:
        :   **RuntimeError: Unable to find page {"<page name>"}** – This exception occurs if the specified page to rename is not found in the DDSFile.

        Example

        Rename a page in the DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.new_dds_file()
        >>> dds_file.new_window()
        >>> print(dds_file.pages)
            (<Page "page 1">)
        >>> dds_file.rename_page("page 1", "readme")
        >>> print(dds_file.pages)
            (<Page "readme">)
        >>> print(dds_file.windows[0].current_page)
            readme
        >>> print(dds_file.windows[1].current_page)
            readme
        >>> dds_file.save()
        ```

    save(*name: str | None = None*, *path: str | PathLike | None = None*) → None[](#keysight.ads.dds.DDSFile.save "Link to this definition")
    :   Save the DDSFile.

        Parameters:
        :   * **name** (*str* *[**optional**,* *default=None**]*) – Specifies the file name where the DDSFile will be saved. This may include an absolute path or relative path.
              The extension “.dds” may or may not be included. However, when saved, it will ensure the file has a “.dds” extension.
              If it is an absolute path, the “path” parameter will be ignored.
              If its a relative path, it is joined with the “path” parameter.
              If the DDSFile has been saved before, the current file name will be used UNLESS “name” is passed.
              If DDSFile is a new file that has never been saved before, this parameter MUST be passed or an exception will occur.
            * **path** (*str* *[**optional**,* *default=None**]*) – Specifies the directory where the DDSFile will be saved.
              If the DDSFile has been saved before, the current directory will be used UNLESS “path” is passed.
              If DDSFile is a new file that has never been saved before, this parameter MUST be passed or an exception will occur.

        Return type:
        :   None

        Raises:
        :   * **RuntimeError: No filename specified to save object.** – This exception occurs if the DDSFile is a new file that has never been saved and the “name” parameter is not passed or empty.
            * **RuntimeError: No path specified to save object.** – This exception occurs if the DDSFile is a new file that has never been saved and the “path” parameter is not passed or empty.
            * **RuntimeError: Writing dds file failed\** – {<path>}.: This exception occurs when the file write failed.

        Examples

        Open an existing file and save it

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> dds_file.save()  #Overwrites test.dds
        >>> dds_file = dds.open_dds_file("c:/tmp/external.dds")
        >>> dds_file.save()  #Overwrites "c:/tmp/external.dds"
        ```

        Open an existing file save it to a different file in the same directory.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> dds_file.save("newTest.dds")         #Writes new file "newTest.dds" in the current directory
        >>> dds_file = dds.open_dds_file("c:/tmp/external.dds")
        >>> dds_file.save("newExternal.dds")    #Writes new file "c:/tmp/newExternal.dds"
        ```

        Open new file and save it

        ```
        >>> dds_file = dds.new_dds_file("cell_1.ds", "c:/tmp")
            Opens a new DDSFile with path set to "c:/tmp"
        >>> dds_file.save("newFile.dds")
            Writes new file "c:/tmp/newFile.dds"
        ```

        See also

        [`close()`](#keysight.ads.dds.DDSFile.close "keysight.ads.dds.DDSFile.close")
        :   Close the Data Display file.

        [`new_dds_file()`](index.md#keysight.ads.dds.new_dds_file "keysight.ads.dds.new_dds_file")
        :   Create a new Data Display file.

        [`open_dds_file()`](index.md#keysight.ads.dds.open_dds_file "keysight.ads.dds.open_dds_file")
        :   Open an existing Data Display file.

    save\_as\_template(*path: str | PathLike*) → None[](#keysight.ads.dds.DDSFile.save_as_template "Link to this definition")
    :   Save the DDSFile as a Data Display Template.

        Parameters:
        :   **name** (*str* *|* *os.PathLike*) – The path to the template. It may be an absolute or relative path.
            It may or may not include the “.ddt” extension.

        Return type:
        :   None

        Example

        Create a template from a DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.new_dds_file("xxx.ds", "c:/tmp")
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot()
        >>> trace = plot.add_trace("SimpleVar")
        >>> dds_file.save_as_template("c:/tmp/myPlot")
        ```

        See also

        [`insert_template()`](#keysight.ads.dds.DDSFile.insert_template "keysight.ads.dds.DDSFile.insert_template")
        :   Insert a Data Display template into the DDSFile.

    *property* selected\_objects*: list[GraphicalObject]*[](#keysight.ads.dds.DDSFile.selected_objects "Link to this definition")
    :   A list of selected objects.

        Example

        Select a plot on the DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> page = dds_file.pages[0]
        >>> sel_objs = dds_file.selected_objects
        >>> print(sel_objs)
            []
        >>> plot = page.objects[0]
        >>> dds_file.selected_objects = [plot]
        >>> sel_objs = dds_file.selected_objects
        >>> print(sel_objs)
            [<RectPlot "">]
        ```

    *property* snap\_auto\_set\_xy*: bool*[](#keysight.ads.dds.DDSFile.snap_auto_set_xy "Link to this definition")
    :   Indicate whether or not to automatically set Y=X when any X value in snap grid property is modified.

        In this mode, the Y value can still be modified independently.

    *property* snap\_distance\_x*: float*[](#keysight.ads.dds.DDSFile.snap_distance_x "Link to this definition")
    :   The snap grid distance (in inches) for the X-coordinate for pages in the DDSFile.

    *property* snap\_distance\_y*: float*[](#keysight.ads.dds.DDSFile.snap_distance_y "Link to this definition")
    :   The snap grid distance (in inches) for the Y-coordinate for pages in the DDSFile.

    *property* snap\_enabled*: bool*[](#keysight.ads.dds.DDSFile.snap_enabled "Link to this definition")
    :   Indicate whether or not the snap grid is enabled for pages in the DDSFile.

        When enabled, plots, lists, and other graphical objects snap to the grid when
        they are moved or resized. This makes it easier to move the objects into
        exact alignment on the display, or to space them evenly.

    *property* snap\_grid\_per\_display\_grid\_x*: int*[](#keysight.ads.dds.DDSFile.snap_grid_per_display_grid_x "Link to this definition")
    :   The snap grid per display grid for the X-coordinate for pages in the DDSFile.

    *property* snap\_grid\_per\_display\_grid\_y*: int*[](#keysight.ads.dds.DDSFile.snap_grid_per_display_grid_y "Link to this definition")
    :   The snap grid per display grid for the Y-coordinate for pages in the DDSFile.

    start\_history(*depth: int | None = None*) → None[](#keysight.ads.dds.DDSFile.start_history "Link to this definition")
    :   Enable history mode on all plots that support it.

        Parameters:
        :   **depth** (*int* *[**optional**,* *default=None**]*) – The number of history subtraces to maintain for each plot. If not specified,
            the default depth is used.

        Return type:
        :   None

    stop\_history() → None[](#keysight.ads.dds.DDSFile.stop_history "Link to this definition")
    :   Disable history mode on all plots.

        Return type:
        :   None

    *property* type*: ObjectType*[](#keysight.ads.dds.DDSFile.type "Link to this definition")

    *property* uid*: int*[](#keysight.ads.dds.DDSFile.uid "Link to this definition")

    var(*name: str*) → Any[](#keysight.ads.dds.DDSFile.var "Link to this definition")
    :   Return a variable by name. The variable could be from an equation, markers, or other source.

    *property* windows*: list[[Window](windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window")]*[](#keysight.ads.dds.DDSFile.windows "Link to this definition")
    :   A list of Windows viewing the contents of the DDSFile.

        See also

        [`new_window()`](#keysight.ads.dds.DDSFile.new_window "keysight.ads.dds.DDSFile.new_window")
        :   Create a new window in the DDSFile.

On this page

[Previous

keysight.ads.dds](index.md)
[Next

Page](page.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top