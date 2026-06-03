<!-- 来源: reference\dds\experimental\index.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../../index.md)
* [Reference](../../index.md)
* keysight.ads.dds.experimental

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
  + keysight.ads.dds.experimental
    - [DDSQtWidget](qtwidget.md)
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

# keysight.ads.dds.experimental[](#module-keysight.ads.dds.experimental "Link to this heading")

## Classes[](#classes "Link to this heading")

* [DDSQtWidget](qtwidget.md)
  + [`DDSQtWidget`](qtwidget.md#keysight.ads.dds.experimental.DDSQtWidget)

## Functions[](#functions "Link to this heading")

keysight.ads.dds.experimental.rename\_dataset\_and\_update\_expressions(*src\_dataset: str | PathLike*, *dest\_dataset: str | PathLike*) → None[](#keysight.ads.dds.experimental.rename_dataset_and_update_expressions "Link to this definition")
:   Rename the source dataset to the destination dataset and update any referenced expressions.

    This function renames the source dataset to the destination
    dataset. If the destination dataset exists it is replaced. Once
    renamed any expressions that reference the destination dataset are
    updated.

    It is recommended to use this command to rename datasets that are
    utilized by Data Display. It avoids potential crashes in Data
    Display that can occur if the dataset is renamed using other
    methods.

    When creating a dataset in the destinations ‘data’ directory it is
    recommended to prefix the dataset name with ‘\_\_dstmp’. Datasets
    that exist with this prefix are ignored by Data Display. This
    allows the source dataset to be changed without being accessed by
    Data Display.

    On Windows this function will unlock the dataset before replacing
    the destination as long as the files are being locked from the
    current ADS or Python session.

    > * Running in application mode inside ADS. This function will
    >   unlock the dataset in the current de session and will send a
    >   message to current dds session to unlock and then rename the
    >   dataset.
    > * Running in application mode inside Data Display. This
    >   function will only unlock the dataset being accessed in the
    >   current dds session.
    > * Running in automation mode inside Python. Only datasets
    >   locked by the current python session will be unlocked.
    > * This command fails if any application outside the current
    >   ADS session is accessing the dataset.

    Parameters:
    :   * **src\_dataset** (*str* *|* *os.PathLike*) – The name of the source dataset.
        * **dest\_dataset** (*str* *|* *os.PathLike*) – The name of the destination dataset. If the destination
          dataset already exists it will be replaced by the source
          dataset.

    The dataset path may be relative to or full path. Paths are
    relative to the current workspace or directory. The dataset is
    expected to have an extension of “.ds” and will be added if no
    suffix is present.

    Return type:
    :   None

    Raises:
    :   * **RuntimeError: The source dataset name is required.** –
        * **RuntimeError: The destination dataset name is required..** –
        * **RuntimeError: The source dataset has an unexpected suffix****,** **expected ".ds". Dataset = "<dataset path>".** –
        * **RuntimeError: The destination dataset has an unexpected suffix****,** **expected ".ds". Dataset = "<dataset path>".** –
        * **RuntimeError: The source dataset does not exist. Dataset = "<dataset path>".** –
        * **RuntimeError: Rename** **of** **dataset failed.** – The rename of the destination failed. This normally is
          caused by some other process having the dataset open for
          reading.

    Example

    Rename the current dataset called “default.ds” with “\_\_dstmp124.ds”.

    ```
    >>> from keysight.ads.dds.experimental import rename_dataset_and_update_expressions
    >>>
    >>> rename_dataset_and_update_expressions("data/__dstmp124.ds", "data/default.ds")
    ```

On this page

[Previous

Widget](../pywidget.md)
[Next

DDSQtWidget](qtwidget.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top