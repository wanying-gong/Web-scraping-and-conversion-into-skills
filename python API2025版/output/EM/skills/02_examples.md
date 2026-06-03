# Examples
> **说明：** Examples 相关页面。

> **何时使用：** 当你需要查阅 Examples 相关内容时

---

## 本文件目录

- **Convert EM Setup to RFPro View** (`examples/ex_convert_emsetup_to_rfpro_view.md`)
- **Create RFPro View** (`examples/ex_create_rfpro_view.md`)
- **Get the Substrate from an EM Setup View** (`examples/ex_get_emsetup_substrate_info.md`)
- **Examples** (`examples/index.md`)

---

<!-- === 来源: examples/ex_convert_emsetup_to_rfpro_view.md === -->

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


---

<!-- === 来源: examples/ex_create_rfpro_view.md === -->

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

<!-- === 来源: examples/ex_get_emsetup_substrate_info.md === -->

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

<!-- === 来源: examples/index.md === -->

# Examples[](#examples "Link to this heading")

The source code for the examples referenced by these help pages can be found in **$HPEESOF\_DIR/em/python/examples**

Contents:

* [Create RFPro View](ex_create_rfpro_view.md)
* [Get the Substrate from an EM Setup View](ex_get_emsetup_substrate_info.md)
* [Convert EM Setup to RFPro View](ex_convert_emsetup_to_rfpro_view.md)


---

