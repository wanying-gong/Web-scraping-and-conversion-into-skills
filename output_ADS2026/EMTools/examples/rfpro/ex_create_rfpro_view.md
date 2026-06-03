<!-- 来源: examples\rfpro\ex_create_rfpro_view.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [EM Tools Python Documentation](../../index.md)
* [Examples](../index.md)
* [RFPro Examples](index.md)
* Create RFPro View

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
    - Create RFPro View
    - [Get the Substrate from an EM Setup View](ex_get_emsetup_substrate_info.md)
    - [Convert EM Setup to RFPro View](ex_convert_emsetup_to_rfpro_view.md)
  + [PEPro Examples](../pepro/index.md)
    - [Creates a new pepro View](../pepro/ex_create_pepro_view.md)
    - [Run existing PEPro analysis persent in workspace.](../pepro/ex_run_pepro_sim.md)
    - [Creates a new selected nets type analysis in pepro View and run the simulation.](../pepro/ex_create_and_run_selected_nets_analysis.md)
    - [Creates a new pe thermal analysis in pepro View and run the simulation.](../pepro/ex_create_and_run_thermal_analysis.md)

# Create RFPro View[](#create-rfpro-view "Link to this heading")

This example shows how to create an RFPro view.

```
# Copyright Keysight Technologies 2025

def create_rfpro_view(example_dir : str, workspace_name : str, libray_name : str, cell_name : str):
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

On this page

[Previous

RFPro Examples](index.md)
[Next

Get the Substrate from an EM Setup View](ex_get_emsetup_substrate_info.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top