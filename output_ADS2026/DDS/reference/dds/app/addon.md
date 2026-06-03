<!-- 来源: reference\dds\app\addon.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [DDS Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.dds.app](index.md)
* Addon

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
  + [keysight.ads.dds.experimental](../experimental/index.md)
    - [DDSQtWidget](../experimental/qtwidget.md)
  + [keysight.ads.dds.app](index.md)
    - Addon
    - [Callbacks](callbacks.md)
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

# Addon[](#addon "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.dds.app.Addon[](#keysight.ads.dds.app.Addon "Link to this definition")
:   Bases: `object`

    Used to extend the functionality of ADS by adding code that is loaded at startup.

    \_\_init\_\_(*name: str*, *path: str*, *enabled: bool = True*, *location: [AddonLocale](#keysight.ads.dds.app.AddonLocale "keysight.ads.dds.app.addon.AddonLocale") = AddonLocale.USER*) → None[](#keysight.ads.dds.app.Addon.__init__ "Link to this definition")

    *property* enabled*: bool*[](#keysight.ads.dds.app.Addon.enabled "Link to this definition")

    *property* location*: [AddonLocale](#keysight.ads.dds.app.AddonLocale "keysight.ads.dds.app.addon.AddonLocale")*[](#keysight.ads.dds.app.Addon.location "Link to this definition")
    :   Specifies the location of the xml configuration file that references this Addon.

    module\_name() → str[](#keysight.ads.dds.app.Addon.module_name "Link to this definition")
    :   Return the full name of the Python module for this Addon.

        Will raise an exception if this Addon does not have a Python module.

    *property* name*: str*[](#keysight.ads.dds.app.Addon.name "Link to this definition")

    *property* raw\_startup\_file*: str*[](#keysight.ads.dds.app.Addon.raw_startup_file "Link to this definition")
    :   The startup file for this Addon - possibly including environment variables.

    *property* root\_directory*: str*[](#keysight.ads.dds.app.Addon.root_directory "Link to this definition")
    :   The directory containing the startup file.

    *property* startup\_file*: str*[](#keysight.ads.dds.app.Addon.startup_file "Link to this definition")
    :   The startup file for this Addon.

    *property* sync\_location*: str*[](#keysight.ads.dds.app.Addon.sync_location "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.dds.app.AddonLocale[](#keysight.ads.dds.app.AddonLocale "Link to this definition")
:   Bases: `Enum`

    Specifies the location of the xml configuration file.

    MEMORY *= <AddonLocale.MEMORY: 0>*[](#keysight.ads.dds.app.AddonLocale.MEMORY "Link to this definition")
    :   The Addon is not stored in any file.

    USER *= <AddonLocale.USER: 1>*[](#keysight.ads.dds.app.AddonLocale.USER "Link to this definition")
    :   The Addon location in the HOME directory for Addon’s installed by the user.

    SITE *= <AddonLocale.SITE: 2>*[](#keysight.ads.dds.app.AddonLocale.SITE "Link to this definition")
    :   The Addon location for custom Addon’s installed at the user’s site.

    INSTALLATION *= <AddonLocale.INSTALLATION: 3>*[](#keysight.ads.dds.app.AddonLocale.INSTALLATION "Link to this definition")
    :   The Addon location in the product directory for Addon’s installed by ADS.

## Functions[](#functions "Link to this heading")

> keysight.ads.dds.app.add\_memory\_addon(*addon: [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")*) → None[](#keysight.ads.dds.app.add_memory_addon "Link to this definition")
> :   Add addon to the set of memory Addons (load if enabled).
>
> keysight.ads.dds.app.add\_user\_addon(*addon: [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")*) → None[](#keysight.ads.dds.app.add_user_addon "Link to this definition")
> :   Add addon to the list of user Addons (load if enabled).
>
> keysight.ads.dds.app.addon(*addon\_name: str*) → [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")[](#keysight.ads.dds.app.addon "Link to this definition")
> :   Search all the locations for an Addon with the given name.
>
>     Raises an exception if no enabled Addon was found.
>
> keysight.ads.dds.app.enable\_addon(*addon: [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")*, *enable: bool*) → [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")[](#keysight.ads.dds.app.enable_addon "Link to this definition")
> :   Enable or disable the addon.
>
>     If this is overriding the state of an installation or site
>     addon, this will return a different Addon (either a new override
>     or the original whose override we just removed).
>
> keysight.ads.dds.app.find\_addon(*addon\_name: str*) → [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon") | None[](#keysight.ads.dds.app.find_addon "Link to this definition")
> :   Search all the locations for an Addon with the given name.
>
>     Returns None if no Addon was found.
>
> keysight.ads.dds.app.import\_addon\_as\_module(*addon\_name: str*) → ModuleType[](#keysight.ads.dds.app.import_addon_as_module "Link to this definition")
> :   Import the Python module for an ADS Addon.
>
> keysight.ads.dds.app.remove\_memory\_addon(*addon: [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")*) → None[](#keysight.ads.dds.app.remove_memory_addon "Link to this definition")
> :   Remove addon from the set of memory Addons (unload if enabled).
>
> keysight.ads.dds.app.remove\_user\_addon(*addon: [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")*) → None[](#keysight.ads.dds.app.remove_user_addon "Link to this definition")
> :   Remove addon from the list of user Addons (unload if enabled).

On this page

[Previous

keysight.ads.dds.app](index.md)
[Next

Callbacks](callbacks.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top