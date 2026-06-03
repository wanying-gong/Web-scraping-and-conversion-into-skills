# Reference
> **说明：** Reference 相关页面。

> **何时使用：** 当你需要查阅 Reference 相关内容时

---

## 本文件目录

- **keysight.ads.emtools** (`reference/emtools.md`)
- **Reference** (`reference/index.md`)

---

<!-- === 来源: reference/emtools.md === -->

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


---

<!-- === 来源: reference/index.md === -->

# Reference[](#reference "Link to this heading")

* [keysight.ads.emtools](emtools.md)
  + [Classes](emtools.md#classes)
    - [`EmproSetup`](emtools.md#keysight.ads.emtools.EmproSetup)
  + [Functions](emtools.md#functions)
    - [xxPro](emtools.md#xxpro)
    - [EM Setup](emtools.md#em-setup)
    - [General](emtools.md#general)


---

