<!-- 来源: examples\pepro\ex_create_pepro_view.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [EM Tools Python Documentation](../../index.md)
* [Examples](../index.md)
* [PEPro Examples](index.md)
* Creates a new pepro View

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
  + [RFPro Examples](../rfpro/index.md)
    - [Create RFPro View](../rfpro/ex_create_rfpro_view.md)
    - [Get the Substrate from an EM Setup View](../rfpro/ex_get_emsetup_substrate_info.md)
    - [Convert EM Setup to RFPro View](../rfpro/ex_convert_emsetup_to_rfpro_view.md)
  + [PEPro Examples](index.md)
    - Creates a new pepro View
    - [Run existing PEPro analysis persent in workspace.](ex_run_pepro_sim.md)
    - [Creates a new selected nets type analysis in pepro View and run the simulation.](ex_create_and_run_selected_nets_analysis.md)
    - [Creates a new pe thermal analysis in pepro View and run the simulation.](ex_create_and_run_thermal_analysis.md)

# Creates a new pepro View[](#creates-a-new-pepro-view "Link to this heading")

This example shows how to creates a new pepro(pepro1) view.

1. Creates pepro view in workspace.

```
# Copyright Keysight Technologies 2025
"""
This example demonstrates how to create a new pepro view.
"""
from tempfile import gettempdir
import os
import shutil
from pathlib import Path
import keysight.ads.de as de
import keysight.ads.emtools as em

def create_pepro_view(example_dir : str, workspace_name : str, libray_name : str, cell_name : str):

    tempdir = gettempdir()
    print(f"Using temporary directory: {tempdir}")
    workspace_dir = Path(os.path.join(tempdir, workspace_name))
    if workspace_dir.exists():
        shutil.rmtree(workspace_dir)

    archive_file = os.path.join(de.hpeesof_path(), example_dir, workspace_name + ".7zads")
    de.unarchive_file(archive_file, tempdir)
    workspace = de.open_workspace(workspace_dir)

    library = de.Library.get(libray_name)
    cell = library.cell(cell_name)
    if not cell.view_exists("pepro1"):
        print("creating pepro view")
        em.create_empro_view(
            (library.name, cell.name, "pepro1"), # pepro LCV
            "pepro", # tool
            (library.name, cell.name, "layout"), # layout LCV
            (library.name, "tech.subst") # substrate
            )
    else:
        print("pepro view already exists")

    workspace.close()

if __name__ == "__main__":

    create_pepro_view("examples/PE", "Power_module_wrk", "Power_module_lib", "SiC_intelligent_power_module")
    print("Done!")

```

On this page

[Previous

PEPro Examples](index.md)
[Next

Run existing PEPro analysis persent in workspace.](ex_run_pepro_sim.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top