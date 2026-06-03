<!-- 来源: pypde\docs\examples\design_creation\ex_create_schematic.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Examples](../../../../examples.md)
* [Design Environment](../index.md)
* [Design Creation](index.md)
* Create Schematic

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

* [Introduction](../../../../pydocs/intro/index.md)
* [How-To](../../../../pydocs/howto/index.md)
  + [Use Python in the ADS Application](../../../../pydocs/howto/embedded.md)
  + [Set Up a Python Virtual Environment](../../../../pydocs/howto/venv.md)
  + [Set Up Visual Studio Code for Development](../../../../pydocs/howto/vscode.md)
  + [Use Pytest](../../../../pydocs/howto/pytest.md)
  + [Enable Python Support For Your Library](../../../../pydocs/howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../../../../pydocs/howto/execution.md)
  + [Export Workspace and Design Objects to Python](../../../../pydocs/howto/exporter.md)
  + [Record Actions in ADS as Python Code](../../../../pydocs/howto/recorder.md)
  + [Develop a Python Pcell in ADS](../../../../pydocs/howto/pcell.md)
* [ADS Concepts](../../../../pydocs/concepts/index.md)
  + [Workspace Elements](../../../../pydocs/concepts/workspace_elements.md)
  + [Connectivity Objects](../../../../pydocs/concepts/connectivity.md)
* [Reference](../../../../reference.md)
  + [Deprecated APIs](../../../../pydocs/py/_generated/deprecations.md)
  + [Design Environment](../../reference/index.md)
    - [keysight.ads.de](../../reference/de/index.md)
      * [ADS Application Environment](../../reference/de/ads_environment.md)
      * [ADS Workspace Components](../../reference/de/workspace_components.md)
      * [Design Hierarchy](../../reference/de/design_hierarchy.md)
      * [Smart Package](../../reference/de/package.md)
      * [Geometry](../../reference/de/geometry.md)
      * [Collections](../../reference/de/collections.md)
      * [Printer](../../reference/de/printer.md)
    - [keysight.ads.de.ael](../../reference/de/ael.md)
    - [keysight.ads.de.app](../../reference/de/app/index.md)
      * [Application](../../reference/de/app/application.md)
      * [Actions and Menus](../../reference/de/app/action.md)
      * [Addons](../../reference/de/app/addon.md)
      * [Window and Design Callbacks](../../reference/de/app/callbacks.md)
      * [Windows and Widgets](../../reference/de/app/window.md)
      * [Experimental](../../reference/de/app/experimental.md)
    - [keysight.ads.de.app.dds](../../reference/de/app/dds.md)
      * [exec\_python](../../reference/de/app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../reference/de/db/index.md)
      * [Models, Parameters, and Forms](../../reference/de/db/parameters.md)
      * [Properties](../../reference/de/db/properties.md)
      * [Preferences](../../reference/de/db/preferences.md)
      * [Transaction](../../reference/de/db/transaction.md)
      * [Smart Mount](../../reference/de/db/smart_mount.md)
      * [Geometry](../../reference/de/db/geometry.md)
      * [Teardrops](../../reference/de/db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../reference/de/db_dbu/index.md)
      * [DbBox](../../reference/de/db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../../reference/de/db_uu/index.md)
      * [Database Objects](../../reference/de/db_uu/database_objects.md)
      * [Iterators](../../reference/de/db_uu/iterators.md)
      * [Designs](../../reference/de/db_uu/design.md)
      * [Teardrops](../../reference/de/db_uu/teardrop.md)
    - [keysight.ads.de.experimental](../../reference/de/experimental/index.md)
      * [CDF](../../reference/de/experimental/cdf.md)
      * [Design Commands](../../reference/de/experimental/commands.md)
      * [Component Handles](../../reference/de/experimental/handles.md)
      * [Netlist Utilities](../../reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../../reference/de/experimental/polygon_utils.md)
      * [xxPro View](../../reference/de/experimental/pro_view.md)
      * [Symbol Generator](../../reference/de/experimental/symbol.md)
      * [Text Maker](../../reference/de/experimental/text_maker.md)
      * [Notebook](../../reference/de/experimental/notebook.md)
      * [Layer/Purpose Pairs](../../reference/de/experimental/lpp.md)
    - [keysight.ads.de.tech](../../reference/de/tech/index.md)
      * [Technology](../../reference/de/tech/tech.md)
      * [Layers](../../reference/de/tech/layers.md)
      * [Line Items](../../reference/de/tech/line_items.md)
      * [Padstacks](../../reference/de/tech/pads.md)
      * [Rules](../../reference/de/tech/rule.md)
  + [Substrate](../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../../../examples.md)
  + [Design Environment](../index.md)
    - [Workspace Creation](../workspace/ex_workspace.md)
    - [Design Creation](index.md)
      * [Create Layout](ex_create_layout.md)
      * Create Schematic
      * [Create, Simulate, and Plot](ex_create_sim_and_plot.md)
    - [Design Elements](../design_elements/index.md)
      * [Placing Text](../design_elements/ex_place_text.md)
      * [Moving Objects](../design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../design_elements/ex_plane_editing.md)
    - [Parameters](../parameters/index.md)
      * [Interoperable Component Parameters](../parameters/ex_cdf.md)
      * [Working with VAR](../parameters/ex_working_with_var.md)
      * [Component Parameters](../parameters/ex_parameters.md)
      * [Creating an Item Definition](../parameters/ex_itemdef.md)
      * [Model Definition Properties](../parameters/ex_model.md)
      * [Creating a Text Form](../parameters/ex_text_form.md)
      * [Properties](../parameters/ex_properties.md)
    - [Technology](../technology/index.md)
      * [Padstacks and Vias](../technology/ex_padstack.md)
      * [Nested Technology](../technology/ex_nested.md)
      * [Rules](../technology/ex_rules.md)
    - [Translators](../translators/index.md)
      * [DXF Import and Export](../translators/ex_translate_dxf.md)
      * [Gerber Export](../translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../translators/ex_translate_gds.md)
    - [UI](../ui/index.md)
      * [Creating Custom Menus Using an Addon](../ui/ex_menu_addon.md)
      * [PySide](../ui/ex_pyside.md)
    - [Utility](../utility/index.md)
      * [Calling Between AEL and Python](../utility/ex_calling_ael_and_python.md)
      * [Smart Package](../utility/ex_smart_pkg.md)
      * [XML RPC](../utility/ex_xml_rpc.md)
  + [Substrate](../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../../../genindex.md)

# Create Schematic[](#create-schematic "Link to this heading")

This example creates a schematic of an RLC filter, and adds a simulation controller. It requires that you have a workspace open with a library that does not already have a cell called “cell\_sch”.

```
def create_schematic_and_add_instances_to_design(library: de.Library) -> None:
    from keysight.ads.de import db_uu

    design = db_uu.create_schematic(f"{library.name}:cell_sch:schematic")
    # Explicit names ─ ADS keeps them exactly.
    design.add_instance(db_uu.LCVName("ads_simulation", "Term", "symbol"), (-2, 0), name="P1", angle=-90)
    design.add_instance(db_uu.LCVName("ads_simulation", "Term", "symbol"), (4, 0), name="P2", angle=-90)
    design.add_instance(db_uu.LCVName("ads_rflib", "GROUND", "symbol"), (-2, -1), name="G1", angle=-90)
    design.add_instance(db_uu.LCVName("ads_rflib", "GROUND", "symbol"), (4, -1), name="G5", angle=-90)

    r = design.add_instance(db_uu.LCVName("ads_rflib", "R", "symbol"), (0, 0), name="R1", angle=0)
    ind = design.add_instance(db_uu.LCVName("ads_rflib", "L", "symbol"), (2, 0), name="L1", angle=0)
    c = design.add_instance(db_uu.LCVName("ads_rflib", "C", "symbol"), (1, -1), name="C1", angle=-90)
    # Note:
    # No name given ─ ADS auto‑adds the next “G#”.
    design.add_instance(db_uu.LCVName("ads_rflib", "GROUND", "symbol"), (1, -2), name="", angle=-90)
    r.parameters["R"].value = "5 ohm"
    ind.parameters["L"].value = "2 nH"
    c.parameters["C"].value = "10 pF"

    design.add_wire([(-2.0, 0.0), (0.0, 0.0)])
    design.add_wire([(3.0, 0.0), (4.0, 0.0)])

    design.add_wire([(1.0, 0.0), (1.0, -1.0)])
    design.add_wire([(1.0, 0.0), (2.0, 0.0)])

    design.add_instance(db_uu.LCVName("ads_simulation", "S_Param", "symbol"), (0, -4), name="SP1")
    design.save_design()
```

On this page

[Previous

Create Layout](ex_create_layout.md)
[Next

Create, Simulate, and Plot](ex_create_sim_and_plot.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top