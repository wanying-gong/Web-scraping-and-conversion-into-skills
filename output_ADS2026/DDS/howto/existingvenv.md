<!-- 来源: howto\existingvenv.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../index.md)
* [How-To](index.md)
* [How to Set Up a Python Virtual Environment](venv.md)
* Installing Keysight ADS wheels into an existing Python virtual environment

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

* [Introduction](../intro/index.md)
  + [Licensing](../intro/licensing.md)
  + [Using Data Display functionality in Python](../intro/usage.md)
  + [Using Visual Studio Code](../intro/vscode.md)
* [Concepts](../concepts/index.md)
  + [Python Script Execution](../concepts/execution.md)
* [Reference](../reference/index.md)
  + [keysight.ads.dds](../reference/dds/index.md)
    - [DDSFile](../reference/dds/file.md)
    - [Page](../reference/dds/page.md)
    - [Point](../reference/dds/point.md)
    - [Rect](../reference/dds/rect.md)
    - [Grid](../reference/dds/grid.md)
    - [Plots](../reference/dds/plots.md)
    - [Axes](../reference/dds/axes.md)
    - [Legend](../reference/dds/legend.md)
    - [Trace](../reference/dds/trace.md)
    - [Markers](../reference/dds/marker.md)
    - [Line Markers](../reference/dds/linemarker.md)
    - [Limit Lines](../reference/dds/limitlines.md)
    - [Masks](../reference/dds/masks.md)
    - [Specification](../reference/dds/specifications.md)
    - [Equation](../reference/dds/equation.md)
    - [PyEquation](../reference/dds/pyequation.md)
    - [Text](../reference/dds/text.md)
    - [Picture](../reference/dds/picture.md)
    - [Shapes](../reference/dds/shapes.md)
    - [Group](../reference/dds/group.md)
    - [Common Properties](../reference/dds/basic.md)
    - [Print](../reference/dds/print.md)
    - [Object](../reference/dds/objects.md)
    - [Window](../reference/dds/windows.md)
    - [Widget](../reference/dds/pywidget.md)
  + [keysight.ads.dds.experimental](../reference/dds/experimental/index.md)
    - [DDSQtWidget](../reference/dds/experimental/qtwidget.md)
  + [keysight.ads.dds.app](../reference/dds/app/index.md)
    - [Addon](../reference/dds/app/addon.md)
    - [Callbacks](../reference/dds/app/callbacks.md)
* [How-To](index.md)
  + [How to Set Up a Python Virtual Environment](venv.md)
    - [Creating an ADS based Python virtual environment](newvenv.md)
    - Installing Keysight ADS wheels into an existing Python virtual environment
    - [ADS Python Environment Variables](pyenvvars.md)
  + [How to Use Pytest](pytest.md)
* [Examples](../examples/index.md)
  + [Create Shapes](../examples/ex_shapes.md)
  + [Create Pages and Windows](../examples/ex_pages_and_windows.md)
  + [Create and Modify DDS file](../examples/ex_modified_file.md)
  + [Create Markers](../examples/ex_markers.md)
  + [Create Line Markers](../examples/ex_line_markers.md)
  + [Create equations using dataset variables](../examples/ex_expressions_and_dataframes.md)
  + [Plot Simulation Output](../examples/ex_simple.md)
  + [Plot Amplifier Simulation Data](../examples/ex_optimized_amp.md)
  + [Create Pages and Windows](../examples/ex_python_equations.md)
  + [Add Specifications to a Plot](../examples/ex_specifications.md)
  + [Plot a Time-Domain Output Voltage Waveform](../examples/ex_trantest.md)
  + [Plot Parameter Extraction of Simulation Data](../examples/ex_crq_extraction.md)
  + [Add custom menu to Data-Display file](../examples/ex_custom_menu.md)
  + [Print PDF file](../examples/ex_print.md)
  + [Experimental Examples](../examples/experimental/index.md)
    - [DDS Qt Widget displayed in a Qt QDialog](../examples/experimental/ex_dds_qt_widget.md)
    - [DDS Qt Widget printed using a Qt QPrinter](../examples/experimental/ex_dds_qt_widget.md#dds-qt-widget-printed-using-a-qt-qprinter)
    - [DDS Qt Widget output to a Qt QPixmap](../examples/experimental/ex_dds_qt_widget.md#dds-qt-widget-output-to-a-qt-qpixmap)
    - [DDS rename dataset and update expressions](../examples/experimental/ex_rename_dataset.md)
* [App Examples](../appExamples/index.md)
  + [Add Menu to Data Display Menubar](../appExamples/ex_custom_menu.md)
  + [Add Widgets to Data Display Page](../appExamples/ex_page_widget.md)
  + [Add Matplotlib Plot to Data Display Window](../appExamples/ex_matplotlib_widget.md)
  + [Add an Addon to Data Display](../appExamples/ex_addon.md)
* [Addon Examples](../addonExamples/index.md)
  + [Addon to Generate Menus](../addonExamples/ex_addon/init.md)
  + [3D Plot Addon](../addonExamples/ex_addon_3d_plot/index.md)
    - [Menu for 3D Plot Addon](../addonExamples/ex_addon_3d_plot/init.md)
    - [Plot for 3D Plot Addon](../addonExamples/ex_addon_3d_plot/ex_addon_3d_plot.md)

# Installing Keysight ADS wheels into an existing Python virtual environment[](#installing-keysight-ads-wheels-into-an-existing-python-virtual-environment "Link to this heading")

1. Open a console window and load an existing virtual environment

   > The existing venv must have been created from a Python installation with the same major and minor Python version as ADS.
2. Navigate to the ADS wheelhouse directory

   > Example for Linux:
   >
   > ```
   > cd $HPEESOF_DIR/tools/python/wheelhouse
   > ```
   >
   > Example for Windows:
   >
   > ```
   > cd %HPEESOF_DIR%\tools\python\wheelhouse
   > ```
3. Install packages with pip requirements file

   > Example for Linux:
   >
   > ```
   > python3 -m pip install -r venv_requirements.txt --no-index --no-cache-dir --only-binary=:all: --find-links=.
   > ```
   >
   > Example for Windows:
   >
   > ```
   > python -m pip install -r venv_requirements.txt --no-index --no-cache-dir --only-binary=:all: --find-links=.
   > ```
4. To verify packages have been installed
   :   Example for Linux:

       ```
       python3 -m pip list
       ```

       Example for Windows:

       ```
       python -m pip list
       ```

       You should see various keysight-ads-\* wheels listed

On this page

[Previous

Creating an ADS based Python virtual environment](newvenv.md)
[Next

ADS Python Environment Variables](pyenvvars.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top