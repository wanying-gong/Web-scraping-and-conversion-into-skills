<!-- 来源: examples\ex_get_emsetup_substrate_info.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [EM Tools Python Documentation](../index.md)
* [Examples](index.md)
* Get the Substrate from an EM Setup View

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
  + [Create RFPro View](ex_create_rfpro_view.md)
  + Get the Substrate from an EM Setup View
  + [Convert EM Setup to RFPro View](ex_convert_emsetup_to_rfpro_view.md)

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

On this page

[Previous

Create RFPro View](ex_create_rfpro_view.md)
[Next

Convert EM Setup to RFPro View](ex_convert_emsetup_to_rfpro_view.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top