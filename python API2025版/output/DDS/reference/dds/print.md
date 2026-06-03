<!-- 来源: reference\dds\print.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.dds](index.md)
* Print

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
    - [Common Properties](basic.md)
    - Print
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

# Print[](#print "Link to this heading")

*class* keysight.ads.dds.PaperSize[](#keysight.ads.dds.PaperSize "Link to this definition")
:   An enumerated type to describe printer paper sizes.

    Printing is provided in class [`DDSFile`](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile").

    A0 *= <PaperSize.A0: 5>*[](#keysight.ads.dds.PaperSize.A0 "Link to this definition")

    A1 *= <PaperSize.A1: 6>*[](#keysight.ads.dds.PaperSize.A1 "Link to this definition")

    A2 *= <PaperSize.A2: 7>*[](#keysight.ads.dds.PaperSize.A2 "Link to this definition")

    A3 *= <PaperSize.A3: 8>*[](#keysight.ads.dds.PaperSize.A3 "Link to this definition")

    A4 *= <PaperSize.A4: 0>*[](#keysight.ads.dds.PaperSize.A4 "Link to this definition")

    A5 *= <PaperSize.A5: 9>*[](#keysight.ads.dds.PaperSize.A5 "Link to this definition")

    A6 *= <PaperSize.A6: 10>*[](#keysight.ads.dds.PaperSize.A6 "Link to this definition")

    A7 *= <PaperSize.A7: 11>*[](#keysight.ads.dds.PaperSize.A7 "Link to this definition")

    A8 *= <PaperSize.A8: 12>*[](#keysight.ads.dds.PaperSize.A8 "Link to this definition")

    A9 *= <PaperSize.A9: 13>*[](#keysight.ads.dds.PaperSize.A9 "Link to this definition")

    B0 *= <PaperSize.B0: 14>*[](#keysight.ads.dds.PaperSize.B0 "Link to this definition")

    B1 *= <PaperSize.B1: 15>*[](#keysight.ads.dds.PaperSize.B1 "Link to this definition")

    B10 *= <PaperSize.B10: 16>*[](#keysight.ads.dds.PaperSize.B10 "Link to this definition")

    B2 *= <PaperSize.B2: 17>*[](#keysight.ads.dds.PaperSize.B2 "Link to this definition")

    B3 *= <PaperSize.B3: 18>*[](#keysight.ads.dds.PaperSize.B3 "Link to this definition")

    B4 *= <PaperSize.B4: 19>*[](#keysight.ads.dds.PaperSize.B4 "Link to this definition")

    B5 *= <PaperSize.B5: 1>*[](#keysight.ads.dds.PaperSize.B5 "Link to this definition")

    B6 *= <PaperSize.B6: 20>*[](#keysight.ads.dds.PaperSize.B6 "Link to this definition")

    B7 *= <PaperSize.B7: 21>*[](#keysight.ads.dds.PaperSize.B7 "Link to this definition")

    B8 *= <PaperSize.B8: 22>*[](#keysight.ads.dds.PaperSize.B8 "Link to this definition")

    B9 *= <PaperSize.B9: 23>*[](#keysight.ads.dds.PaperSize.B9 "Link to this definition")

    C5E *= <PaperSize.C5E: 24>*[](#keysight.ads.dds.PaperSize.C5E "Link to this definition")

    COMM10E *= <PaperSize.Comm10E: 25>*[](#keysight.ads.dds.PaperSize.COMM10E "Link to this definition")

    DLE *= <PaperSize.DLE: 26>*[](#keysight.ads.dds.PaperSize.DLE "Link to this definition")

    EXECUTIVE *= <PaperSize.Executive: 4>*[](#keysight.ads.dds.PaperSize.EXECUTIVE "Link to this definition")

    FOLIO *= <PaperSize.Folio: 27>*[](#keysight.ads.dds.PaperSize.FOLIO "Link to this definition")

    LEDGER *= <PaperSize.Ledger: 28>*[](#keysight.ads.dds.PaperSize.LEDGER "Link to this definition")

    LEGAL *= <PaperSize.Legal: 3>*[](#keysight.ads.dds.PaperSize.LEGAL "Link to this definition")

    LETTER *= <PaperSize.Letter: 2>*[](#keysight.ads.dds.PaperSize.LETTER "Link to this definition")

    TABLOID *= <PaperSize.Tabloid: 29>*[](#keysight.ads.dds.PaperSize.TABLOID "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.PaperSize.str "Link to this definition")

*class* keysight.ads.dds.PrinterOrientation[](#keysight.ads.dds.PrinterOrientation "Link to this definition")
:   An enumerated type to describe printer orientation.

    Printing is provided in class [`DDSFile`](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile").

    LANDSCAPE *= <PrinterOrientation.Landscape: 1>*[](#keysight.ads.dds.PrinterOrientation.LANDSCAPE "Link to this definition")
    :   This value will print image horizontally on paper.

    PORTRAIT *= <PrinterOrientation.Portrait: 0>*[](#keysight.ads.dds.PrinterOrientation.PORTRAIT "Link to this definition")
    :   This value will print image vertically on paper.

    *property* str*: str*[](#keysight.ads.dds.PrinterOrientation.str "Link to this definition")

On this page

[Previous

Common Properties](basic.md)
[Next

Object](objects.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top