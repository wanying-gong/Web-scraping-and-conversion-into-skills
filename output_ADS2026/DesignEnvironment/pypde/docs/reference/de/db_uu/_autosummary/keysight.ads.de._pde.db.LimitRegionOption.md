<!-- 来源: pypde\docs\reference\de\db_uu\_autosummary\keysight.ads.de._pde.db.LimitRegionOption.html -->

[![Logo](../../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../../index.md)
* [Reference](../../../../../../reference.md)
* [Design Environment](../../../index.md)
* [keysight.ads.de.db\_uu](../index.md)
* [Iterators](../iterators.md)
* LimitRegionOption

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

* [Introduction](../../../../../../pydocs/intro/index.md)
* [How-To](../../../../../../pydocs/howto/index.md)
  + [Use Python in the ADS Application](../../../../../../pydocs/howto/embedded.md)
  + [Set Up a Python Virtual Environment](../../../../../../pydocs/howto/venv.md)
  + [Set Up Visual Studio Code for Development](../../../../../../pydocs/howto/vscode.md)
  + [Use Pytest](../../../../../../pydocs/howto/pytest.md)
  + [Enable Python Support For Your Library](../../../../../../pydocs/howto/python_integration.md)
  + [Execute Python Scripts in Different Contexts](../../../../../../pydocs/howto/execution.md)
  + [Export Workspace and Design Objects to Python](../../../../../../pydocs/howto/exporter.md)
  + [Record Actions in ADS as Python Code](../../../../../../pydocs/howto/recorder.md)
  + [Develop a Python Pcell in ADS](../../../../../../pydocs/howto/pcell.md)
* [ADS Concepts](../../../../../../pydocs/concepts/index.md)
  + [Workspace Elements](../../../../../../pydocs/concepts/workspace_elements.md)
  + [Connectivity Objects](../../../../../../pydocs/concepts/connectivity.md)
* [Reference](../../../../../../reference.md)
  + [Deprecated APIs](../../../../../../pydocs/py/_generated/deprecations.md)
  + [Design Environment](../../../index.md)
    - [keysight.ads.de](../../index.md)
      * [ADS Application Environment](../../ads_environment.md)
      * [ADS Workspace Components](../../workspace_components.md)
      * [Design Hierarchy](../../design_hierarchy.md)
      * [Smart Package](../../package.md)
      * [Geometry](../../geometry.md)
      * [Collections](../../collections.md)
      * [Printer](../../printer.md)
    - [keysight.ads.de.ael](../../ael.md)
    - [keysight.ads.de.app](../../app/index.md)
      * [Application](../../app/application.md)
      * [Actions and Menus](../../app/action.md)
      * [Addons](../../app/addon.md)
      * [Window and Design Callbacks](../../app/callbacks.md)
      * [Windows and Widgets](../../app/window.md)
      * [Experimental](../../app/experimental.md)
    - [keysight.ads.de.app.dds](../../app/dds.md)
      * [exec\_python](../../app/_autosummary/keysight.ads.de.app.dds.exec_python.md)
    - [keysight.ads.de.db](../../db/index.md)
      * [Models, Parameters, and Forms](../../db/parameters.md)
      * [Properties](../../db/properties.md)
      * [Preferences](../../db/preferences.md)
      * [Transaction](../../db/transaction.md)
      * [Smart Mount](../../db/smart_mount.md)
      * [Geometry](../../db/geometry.md)
      * [Teardrops](../../db/teardrops.md)
    - [keysight.ads.de.db\_dbu](../../db_dbu/index.md)
      * [DbBox](../../db_dbu/_autosummary/keysight.ads.de.db_dbu.DbBox.md)
    - [keysight.ads.de.db\_uu](../index.md)
      * [Database Objects](../database_objects.md)
      * [Iterators](../iterators.md)
      * [Designs](../design.md)
      * [Teardrops](../teardrop.md)
    - [keysight.ads.de.experimental](../../experimental/index.md)
      * [CDF](../../experimental/cdf.md)
      * [Design Commands](../../experimental/commands.md)
      * [Component Handles](../../experimental/handles.md)
      * [Netlist Utilities](../../experimental/netlist_helper.md)
      * [Polygon Utilities](../../experimental/polygon_utils.md)
      * [xxPro View](../../experimental/pro_view.md)
      * [Symbol Generator](../../experimental/symbol.md)
      * [Text Maker](../../experimental/text_maker.md)
      * [Notebook](../../experimental/notebook.md)
      * [Layer/Purpose Pairs](../../experimental/lpp.md)
    - [keysight.ads.de.tech](../../tech/index.md)
      * [Technology](../../tech/tech.md)
      * [Layers](../../tech/layers.md)
      * [Line Items](../../tech/line_items.md)
      * [Padstacks](../../tech/pads.md)
      * [Rules](../../tech/rule.md)
  + [Substrate](../../../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../../../pysubst/docs/reference/subst/index.md)
      * [Substrate and Materials](../../../../../../pysubst/docs/reference/subst/subst.md)
* [Examples](../../../../../../examples.md)
  + [Design Environment](../../../../examples/index.md)
    - [Workspace Creation](../../../../examples/workspace/ex_workspace.md)
    - [Design Creation](../../../../examples/design_creation/index.md)
      * [Create Layout](../../../../examples/design_creation/ex_create_layout.md)
      * [Create Schematic](../../../../examples/design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../../../../examples/design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../../../../examples/design_elements/index.md)
      * [Placing Text](../../../../examples/design_elements/ex_place_text.md)
      * [Moving Objects](../../../../examples/design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../../../../examples/design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../../../../examples/design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../../../../examples/design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../../../../examples/design_elements/ex_plane_editing.md)
    - [Parameters](../../../../examples/parameters/index.md)
      * [Interoperable Component Parameters](../../../../examples/parameters/ex_cdf.md)
      * [Working with VAR](../../../../examples/parameters/ex_working_with_var.md)
      * [Component Parameters](../../../../examples/parameters/ex_parameters.md)
      * [Creating an Item Definition](../../../../examples/parameters/ex_itemdef.md)
      * [Model Definition Properties](../../../../examples/parameters/ex_model.md)
      * [Creating a Text Form](../../../../examples/parameters/ex_text_form.md)
      * [Properties](../../../../examples/parameters/ex_properties.md)
    - [Technology](../../../../examples/technology/index.md)
      * [Padstacks and Vias](../../../../examples/technology/ex_padstack.md)
      * [Nested Technology](../../../../examples/technology/ex_nested.md)
      * [Rules](../../../../examples/technology/ex_rules.md)
    - [Translators](../../../../examples/translators/index.md)
      * [DXF Import and Export](../../../../examples/translators/ex_translate_dxf.md)
      * [Gerber Export](../../../../examples/translators/ex_translate_gbr.md)
      * [GDSII Import and Export](../../../../examples/translators/ex_translate_gds.md)
    - [UI](../../../../examples/ui/index.md)
      * [Creating Custom Menus Using an Addon](../../../../examples/ui/ex_menu_addon.md)
      * [PySide](../../../../examples/ui/ex_pyside.md)
    - [Utility](../../../../examples/utility/index.md)
      * [Calling Between AEL and Python](../../../../examples/utility/ex_calling_ael_and_python.md)
      * [Smart Package](../../../../examples/utility/ex_smart_pkg.md)
      * [XML RPC](../../../../examples/utility/ex_xml_rpc.md)
  + [Substrate](../../../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../../../pysubst/docs/examples/ex_substrate_with_layout.md)
    - [Z-Height of a Strip Conductor in a Substrate](../../../../../../pysubst/docs/examples/ex_substrate_strip_height.md)
* [Index](../../../../../../genindex.md)

# LimitRegionOption[](#limitregionoption "Link to this heading")

*class* LimitRegionOption[](#keysight.ads.de._pde.db.LimitRegionOption "Link to this definition")
:   Bases: `Enum`

    Attributes

    |  |  |
    | --- | --- |
    | [`REGION_MUST_CONTAIN_OBJECT`](#keysight.ads.de._pde.db.LimitRegionOption.REGION_MUST_CONTAIN_OBJECT "keysight.ads.de._pde.db.LimitRegionOption.REGION_MUST_CONTAIN_OBJECT") |  |
    | [`REGION_MUST_TOUCH_ACTUAL_OBJECT`](#keysight.ads.de._pde.db.LimitRegionOption.REGION_MUST_TOUCH_ACTUAL_OBJECT "keysight.ads.de._pde.db.LimitRegionOption.REGION_MUST_TOUCH_ACTUAL_OBJECT") |  |
    | [`REGION_MUST_TOUCH_OBJECT_EDGE`](#keysight.ads.de._pde.db.LimitRegionOption.REGION_MUST_TOUCH_OBJECT_EDGE "keysight.ads.de._pde.db.LimitRegionOption.REGION_MUST_TOUCH_OBJECT_EDGE") |  |
    | [`REGION_MAY_TOUCH_ONLY_BOUNDING_BOX`](#keysight.ads.de._pde.db.LimitRegionOption.REGION_MAY_TOUCH_ONLY_BOUNDING_BOX "keysight.ads.de._pde.db.LimitRegionOption.REGION_MAY_TOUCH_ONLY_BOUNDING_BOX") |  |

    REGION\_MUST\_CONTAIN\_OBJECT *= 0*[](#keysight.ads.de._pde.db.LimitRegionOption.REGION_MUST_CONTAIN_OBJECT "Link to this definition")

    REGION\_MUST\_TOUCH\_ACTUAL\_OBJECT *= 1*[](#keysight.ads.de._pde.db.LimitRegionOption.REGION_MUST_TOUCH_ACTUAL_OBJECT "Link to this definition")

    REGION\_MUST\_TOUCH\_OBJECT\_EDGE *= 2*[](#keysight.ads.de._pde.db.LimitRegionOption.REGION_MUST_TOUCH_OBJECT_EDGE "Link to this definition")

    REGION\_MAY\_TOUCH\_ONLY\_BOUNDING\_BOX *= 3*[](#keysight.ads.de._pde.db.LimitRegionOption.REGION_MAY_TOUCH_ONLY_BOUNDING_BOX "Link to this definition")

On this page

[Previous

ViaIter](keysight.ads.de.db_uu.ViaIter.md)
[Next

ShapeIterNetOption](keysight.ads.de._pde.db.ShapeIterNetOption.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top