<!-- 来源: reference\emtools.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [EM Tools Python Documentation](../index.md)
* [Reference](index.md)
* keysight.ads.emtools

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
* [Reference](index.md)
  + keysight.ads.emtools
* [Examples](../examples/index.md)
  + [RFPro Examples](../examples/rfpro/index.md)
    - [Create RFPro View](../examples/rfpro/ex_create_rfpro_view.md)
    - [Get the Substrate from an EM Setup View](../examples/rfpro/ex_get_emsetup_substrate_info.md)
    - [Convert EM Setup to RFPro View](../examples/rfpro/ex_convert_emsetup_to_rfpro_view.md)
  + [PEPro Examples](../examples/pepro/index.md)
    - [Creates a new pepro View](../examples/pepro/ex_create_pepro_view.md)
    - [Run existing PEPro analysis persent in workspace.](../examples/pepro/ex_run_pepro_sim.md)
    - [Creates a new selected nets type analysis in pepro View and run the simulation.](../examples/pepro/ex_create_and_run_selected_nets_analysis.md)
    - [Creates a new pe thermal analysis in pepro View and run the simulation.](../examples/pepro/ex_create_and_run_thermal_analysis.md)

# keysight.ads.emtools[](#module-keysight.ads.emtools "Link to this heading")

EM Tools Module.

The `keysight.ads.emtools` module provides ADS functionality to facilitate working with the EM tools. This module is typically
imported as:

```
from keysight.ads import emtools
```

## Classes[](#classes "Link to this heading")

*class* keysight.ads.emtools.EmproSetup[](#keysight.ads.emtools.EmproSetup "Link to this definition")
:   Class to work on the EM view setup.

    \_\_init\_\_(*filepath\_\_or\_\_empro\_lcv\_tuple: str | tuple | None = None*) → [EmproSetup](#keysight.ads.emtools.EmproSetup "keysight.ads.emtools.EmproSetup")[](#keysight.ads.emtools.EmproSetup.__init__ "Link to this definition")
    :   Initialize with 3 strings – library name, cell name and view name – or provide the view’s setup filepath.

    default\_filename() → str[](#keysight.ads.emtools.EmproSetup.default_filename "Link to this definition")
    :   Returns the default EM view setup file name.

    *property* design\_refs*: Dict*[](#keysight.ads.emtools.EmproSetup.design_refs "Link to this definition")
    :   The design references – layout and substrate – of the EM view setup.

        Getter:
        :   Returns this setup’s design references.

        Setter:
        :   Sets this setup’s design references.

    *property* tool*: str*[](#keysight.ads.emtools.EmproSetup.tool "Link to this definition")
    :   The tool for this EM view setup.

        Getter:
        :   Returns this setup’s tool.

        Setter:
        :   Sets this setup’s tool.

    write(*filepath\_or\_lcv: str | tuple*) → None[](#keysight.ads.emtools.EmproSetup.write "Link to this definition")
    :   Writes the EM view setup data.

        Parameters:
        :   **filepath\_or\_lcv** – Either provide a tuple of strings – library name, cell name and view name – or provide the view’s setup filepath.

## Functions[](#functions "Link to this heading")

### xxPro[](#xxpro "Link to this heading")

keysight.ads.emtools.create\_empro\_view(*empro\_lcv: tuple[str, str, str]*, *tool: str*, *layout\_lcv: tuple[str, str, str]*, *substrate\_ls: tuple[str, str]*) → None[](#keysight.ads.emtools.create_empro_view "Link to this definition")
:   Create a view, saved on disk, that can be opened in the specified EM tool.

    Parameters:
    :   * **empro\_lcv** – Tuple containing the library name, cell name and the EM view name to be created.
        * **tool** – EM tool name, eihter ‘pipro’, ‘sipro’, ‘rfpro’, ‘pepro’, ‘quantumpro’, etc.
        * **layout\_lcv** – Tuple containing the library name, cell name and the layout view name.
        * **substrate\_ls** – Tuple containing the library name and substrate name.

    Raises:
    :   **RuntimeError** – If the view cannot be created.

keysight.ads.emtools.update\_empro\_view(*empro\_lcv: tuple[str, str, str]*) → None[](#keysight.ads.emtools.update_empro_view "Link to this definition")
:   Update the EM view after a layout or substrate change.

    Updates the auxiliary files associated with the EM view: .adsPcells cache, adsMultiTechData.json, proj.ltd,…

    Parameters:
    :   **empro\_lcv** – Tuple containing the library name, cell name and the EM view name to be updated.

    Raises:
    :   **RuntimeError** – If the view cannot be updated.

### EM Setup[](#em-setup "Link to this heading")

keysight.ads.emtools.find\_emsetup\_view\_name(*layout\_lcv: tuple[str, str, str]*) → str[](#keysight.ads.emtools.find_emsetup_view_name "Link to this definition")
:   Find the active EM Setup view name from the Layout view.

    Parameters:
    :   **layout\_lcv** – Tuple containing the library name, cell name and the layout view name.

    Return type:
    :   The EM Setup view name

    Raises:
    :   **RuntimeError** – If no EM Setup view can be found.

keysight.ads.emtools.get\_substrate\_info(*emsetup\_lcv: tuple[str, str, str]*) → tuple[str, str][](#keysight.ads.emtools.get_substrate_info "Link to this definition")
:   Get the substrate info of the EM Setup view.

    Parameters:
    :   **emsetup\_lcv** – Tuple containing the library name, cell name and the EM Setup view name.

    Return type:
    :   Tuple containing the substrate library name and the substrate file name with extension.

### General[](#general "Link to this heading")

keysight.ads.emtools.version() → str[](#keysight.ads.emtools.version "Link to this definition")
:   Returns the version of the emtools package.

On this page

[Previous

Reference](index.md)
[Next

Examples](../examples/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top