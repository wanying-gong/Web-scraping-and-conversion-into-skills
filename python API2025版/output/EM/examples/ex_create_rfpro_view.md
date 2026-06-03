<!-- 来源: examples\ex_create_rfpro_view.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [EM Tools Python Documentation](../index.md)
* [Examples](index.md)
* Create RFPro View

ADS 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../intro/index.md)
* [Reference](../reference/index.md)
  + [keysight.ads.emtools](../reference/emtools.md)
* [Examples](index.md)
  + Create RFPro View
  + [Get the Substrate from an EM Setup View](ex_get_emsetup_substrate_info.md)
  + [Convert EM Setup to RFPro View](ex_convert_emsetup_to_rfpro_view.md)

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

On this page

[Previous

Examples](index.md)
[Next

Get the Substrate from an EM Setup View](ex_get_emsetup_substrate_info.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top