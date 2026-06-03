<!-- 来源: examples\rfpro\ex_convert_emsetup_to_rfpro_view.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [EM Tools Python Documentation](../../index.md)
* [Examples](../index.md)
* [RFPro Examples](index.md)
* Convert EM Setup to RFPro View

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
* [Reference](../../reference/index.md)
  + [keysight.ads.emtools](../../reference/emtools.md)
* [Examples](../index.md)
  + [RFPro Examples](index.md)
    - [Create RFPro View](ex_create_rfpro_view.md)
    - [Get the Substrate from an EM Setup View](ex_get_emsetup_substrate_info.md)
    - Convert EM Setup to RFPro View
  + [PEPro Examples](../pepro/index.md)
    - [Creates a new pepro View](../pepro/ex_create_pepro_view.md)
    - [Run existing PEPro analysis persent in workspace.](../pepro/ex_run_pepro_sim.md)
    - [Creates a new selected nets type analysis in pepro View and run the simulation.](../pepro/ex_create_and_run_selected_nets_analysis.md)
    - [Creates a new pe thermal analysis in pepro View and run the simulation.](../pepro/ex_create_and_run_thermal_analysis.md)

# Convert EM Setup to RFPro View[](#convert-em-setup-to-rfpro-view "Link to this heading")

This example shows how to create an RFPro view with an analysis created from an existing EM Setup view.

1. An RFPro view is created, if needed, in the python context of ADS.
2. An RFPro analysis is created from the EM Setup view in the python context of RFPro.

```
# Copyright Keysight Technologies 2025

def ads_find_emsetup_view_and_create_rfpro_view(example_dir : str, workspace_name : str, libray_name : str, cell_name : str) -> tuple [str:str]:
    from tempfile import gettempdir
    import os
    import shutil
    from pathlib import Path
    import keysight.ads.de as de
    import keysight.ads.emtools as em

    tempdir = gettempdir()
    workspace_dir = Path(os.path.join(tempdir, workspace_name))
    if workspace_dir.exists():
        shutil.rmtree(workspace_dir)

    archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
    de.unarchive_file(archive_file, tempdir)
    workspace = de.open_workspace(workspace_dir)

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

On this page

[Previous

Get the Substrate from an EM Setup View](ex_get_emsetup_substrate_info.md)
[Next

PEPro Examples](../pepro/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top