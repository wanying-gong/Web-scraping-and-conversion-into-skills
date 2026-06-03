# EM Tools Python Documentation Knowledge Base
> 本文件由 MarkItDown 自动转换，BFS 遍历自 Keysight ADS2025 Update 2 EM Tools Python Documentation HTML 文档。
> 共 8 个页面。

---

## 目录 (Table of Contents)

1. [index.md](#index)
2. [intro\index.md](#intro--index)
3. [reference\index.md](#reference--index)
4. [reference\emtools.md](#reference--emtools)
5. [examples\index.md](#examples--index)
6. [examples\ex_create_rfpro_view.md](#examples--ex_create_rfpro_view)
7. [examples\ex_get_emsetup_substrate_info.md](#examples--ex_get_emsetup_substrate_info)
8. [examples\ex_convert_emsetup_to_rfpro_view.md](#examples--ex_convert_emsetup_to_rfpro_view)

---



---

## 1. index.md {#index}

# EM Tools Python Documentation[](#em-tools-python-documentation "Link to this heading")

Contents:

* [Introduction](intro/index.md)
* [Reference](reference/index.md)
  + [keysight.ads.emtools](reference/emtools.md)
* [Examples](examples/index.md)
  + [Create RFPro View](examples/ex_create_rfpro_view.md)
  + [Get the Substrate from an EM Setup View](examples/ex_get_emsetup_substrate_info.md)
  + [Convert EM Setup to RFPro View](examples/ex_convert_emsetup_to_rfpro_view.md)


---

## 2. intro\index.md {#intro--index}

# Introduction[](#introduction "Link to this heading")

A Python script can access functionality needed to work with the EM tools in ADS.

```
from keysight.ads import emtools
```

The `keysight.ads.emtools` package is not currently available as a pip-installable package.
To get access to this package, use any one of these approaches:

> 1. Use the Python interpreter in `$HPEESOF_DIR/tools/python`.
> 2. Create a virtual environment based on that interpreter.
> 3. Add `$HPEESOF_DIR/tools/python/packages` onto your Python’s `sys.path`.

Set the environment variable `HPEESOF_DIR` to point to your ADS installation prior to
using the `keysight.ads.emtools` package.


---

## 3. reference\index.md {#reference--index}

# Reference[](#reference "Link to this heading")

* [keysight.ads.emtools](emtools.md)
  + [Classes](emtools.md#classes)
    - [`EmproSetup`](emtools.md#keysight.ads.emtools.EmproSetup)
  + [Functions](emtools.md#functions)
    - [xxPro](emtools.md#xxpro)
    - [EM Setup](emtools.md#em-setup)
    - [General](emtools.md#general)


---

## 4. reference\emtools.md {#reference--emtools}

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

## 5. examples\index.md {#examples--index}

# Examples[](#examples "Link to this heading")

The source code for the examples referenced by these help pages can be found in **$HPEESOF\_DIR/em/python/examples**

Contents:

* [Create RFPro View](ex_create_rfpro_view.md)
* [Get the Substrate from an EM Setup View](ex_get_emsetup_substrate_info.md)
* [Convert EM Setup to RFPro View](ex_convert_emsetup_to_rfpro_view.md)


---

## 6. examples\ex_create_rfpro_view.md {#examples--ex_create_rfpro_view}

# Create RFPro View[](#create-rfpro-view "Link to this heading")

This example shows how to create an RFPro view.

```
# Copyright Keysight Technologies 2025

def create_rfpro_view(example_dir : str, workspace_name : str, libray_name : str, cell_name : str):
    import os
    import shutil
    from pathlib import Path
    import keysight.ads.de as de
    import keysight.ads.emtools as em

    workspace_dir = Path(workspace_name)
    if workspace_dir.exists():
        shutil.rmtree(workspace_dir)

    archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
    de.unarchive_file(archive_file, ".")
    workspace = de.open_workspace(workspace_name)

    library = de.Library.get(libray_name)
    cell = library.cell(cell_name)
    if not cell.view_exists("rfpro"):
        print("creating rfpro view")
        em.create_empro_view(
            (library.name, cell.name, "rfpro"), # rfpro LCV
            "rfpro", # tool
            (library.name, cell.name, "layout"), # layout LCV
            (library.name, "tech.subst") # substrate
            )
    else:
        print("rfpro view already exists")

    workspace.close()

if __name__ == "__main__":

    create_rfpro_view("examples/EM/Antenna", "Single_patch_wrk", "Single_patch_lib", "Single_patch")
    print("Done!")
```


---

## 7. examples\ex_get_emsetup_substrate_info.md {#examples--ex_get_emsetup_substrate_info}

# Get the Substrate from an EM Setup View[](#get-the-substrate-from-an-em-setup-view "Link to this heading")

This example shows how to retrieve the substrate information from an existing EM Setup view.

1. First, the name if the active EM Setup view is retrieved from the Layout view.
2. Then, the substrate information, library name, substrate name and extension is retrieved from the EM Setup view.

```
# Copyright Keysight Technologies 2025

def get_emsetup_substrate_info(example_dir : str, workspace_name : str, libray_name : str, cell_name : str):
    import os
    import shutil
    from pathlib import Path
    import keysight.ads.de as de
    import keysight.ads.emtools as em

    workspace_dir = Path(workspace_name)
    if workspace_dir.exists():
        shutil.rmtree(workspace_dir)

    archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
    de.unarchive_file(archive_file, ".")
    workspace = de.open_workspace(workspace_name)

    emsetup_view_name = em.find_emsetup_view_name((libray_name, cell_name, "layout"))
    print(f"EM Setup view name={emsetup_view_name}")

    library = de.Library.get(libray_name)
    cell = library.cell(cell_name)
    if cell.view_exists(emsetup_view_name):
        (substrateLibraryName, substrateFileName) = em.get_substrate_info((libray_name, cell_name, emsetup_view_name))
        print(f"Substrate library={substrateLibraryName}, name={substrateFileName}");
    else:
        print(f"EM Setup view does not exist.")

    workspace.close()

if __name__ == "__main__":

    get_emsetup_substrate_info("examples/EM/Antenna", "Single_patch_wrk", "Single_patch_lib", "Single_patch")
    print("Done!")
```


---

## 8. examples\ex_convert_emsetup_to_rfpro_view.md {#examples--ex_convert_emsetup_to_rfpro_view}

# Convert EM Setup to RFPro View[](#convert-em-setup-to-rfpro-view "Link to this heading")

This example shows how to create an RFPro view with an analysis created from an existing EM Setup view.

1. An RFPro view is created, if needed, in the python context of ADS.
2. An RFPro analysis is created from the EM Setup view in the python context of RFPro.

```
# Copyright Keysight Technologies 2025

def ads_find_emsetup_view_and_create_rfpro_view(example_dir : str, workspace_name : str, libray_name : str, cell_name : str) -> tuple [str:str]:
    import os
    import shutil
    from pathlib import Path
    import keysight.ads.de as de
    import keysight.ads.emtools as em

    workspace_dir = Path(workspace_name)
    if workspace_dir.exists():
        shutil.rmtree(workspace_dir)

    archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
    de.unarchive_file(archive_file, ".")
    workspace = de.open_workspace(workspace_name)

    library = de.Library.get(libray_name)
    cell = library.cell(cell_name)

    layout_view_name = "layout"
    emsetup_view_name = em.find_emsetup_view_name((libray_name, cell_name, layout_view_name))
    if not cell.view_exists(emsetup_view_name):
        raise RuntimeError(f"\"{library.name}:{cell.name}\" has no EM Setup view")
    (substrateLibraryName, substrateName) = em.get_substrate_info((libray_name, cell_name, emsetup_view_name))

    rfpro_view_name = "rfpro"
    if not cell.view_exists(rfpro_view_name):
        print("Creating the rfpro view")
        em.create_empro_view(
            (library.name, cell.name, rfpro_view_name), # rfpro LCV
            "rfpro", # tool
            (library.name, cell.name, layout_view_name), # layout LCV
            (substrateLibraryName, substrateName) # substrate LS
            )
    else:
        print("The rfpro view exists")
    workspace.close()

    return (emsetup_view_name, rfpro_view_name)

def rfpro_create_analysis_from_emsetup_view(workspace_name : str, libray_name : str, cell_name : str, rfpro_view_name : str, emsetup_view_name : str):
    import empro
    import empro.toolkit
    import keysight.edatoolbox.xxpro as xxpro
    import keysight.edatoolbox.ads as ads

    print("Opening the rfpro view...")
    xxpro.use_workspace(workspace_name)
    pro_lcv = ads.LibraryCellView(library=libray_name, cell=cell_name, view=rfpro_view_name)
    xxpro.load_pro_view(pro_lcv)
    with empro.activeProject as project:
        print("Creating an analysis from an EM Setup view...")
        analysis = empro.analysis.Analysis.fromEmSetup(emsetup_view_name)
        empro.activeProject.analyses.clear()
        empro.activeProject.analyses.append(analysis)
        project.saveActiveProject()

if __name__ == "__main__":

    EXAMPLE_DIR = "examples/EM/Antenna"
    WORKSPACE_NAME = "Single_patch_wrk"
    LIBRARY_NAME = "Single_patch_lib"
    CELL_NAME = "Single_patch"

    import keysight.edatoolbox.multi_python as multi_python

    with multi_python.ads_context() as ads_ctx:
        (emsetup_view_name, rfpro_view_name) = ads_ctx.call(ads_find_emsetup_view_and_create_rfpro_view, args=[EXAMPLE_DIR, WORKSPACE_NAME, LIBRARY_NAME, CELL_NAME])

    with multi_python.xxpro_context() as empro_ctx:
        empro_ctx.call(rfpro_create_analysis_from_emsetup_view, args=[WORKSPACE_NAME, LIBRARY_NAME, CELL_NAME, rfpro_view_name, emsetup_view_name])

    print("Done!")
```
