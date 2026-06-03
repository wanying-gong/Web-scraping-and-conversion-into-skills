<!-- 来源: pypde\docs\examples\parameters\ex_cdf.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Examples](../../../../examples.md)
* [Design Environment](../index.md)
* [Parameters](index.md)
* Interoperable Component Parameters

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
    - [Design Creation](../design_creation/index.md)
      * [Create Layout](../design_creation/ex_create_layout.md)
      * [Create Schematic](../design_creation/ex_create_schematic.md)
      * [Create, Simulate, and Plot](../design_creation/ex_create_sim_and_plot.md)
    - [Design Elements](../design_elements/index.md)
      * [Placing Text](../design_elements/ex_place_text.md)
      * [Moving Objects](../design_elements/ex_move.md)
      * [Paths, Traces, and Polygons](../design_elements/ex_polygon.md)
      * [Adding Instances to a Design](../design_elements/ex_lpf.md)
      * [Traversing Hierarchy](../design_elements/ex_traversing_hierarchy.md)
      * [Plane Editing](../design_elements/ex_plane_editing.md)
    - [Parameters](index.md)
      * Interoperable Component Parameters
      * [Working with VAR](ex_working_with_var.md)
      * [Component Parameters](ex_parameters.md)
      * [Creating an Item Definition](ex_itemdef.md)
      * [Model Definition Properties](ex_model.md)
      * [Creating a Text Form](ex_text_form.md)
      * [Properties](ex_properties.md)
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

# Interoperable Component Parameters[](#interoperable-component-parameters "Link to this heading")

Example illustrating how to access and modify the value of a parameter of an interoperable component

```
def accessing_cdf_instance_parameters(design: db_uu.Design, library: de.Library) -> None:
    from keysight.ads.de import experimental as exp

    # inst_c1 is an interoperable instance placed in the design
    inst_c1 = design.instances["C1"]
    # Retrieve the cell CDF from the 'cap' cell
    cell_cdf = exp.cdf.cell_cdf(library, "cap")
    # Create the interface to the instance CDF parameters
    inst_cdf = exp.cdf.InstanceParams(inst_c1)  # CellCDF parameter is optional when passing in an Instance
    assert cell_cdf == inst_cdf.cell_cdf
    assert inst_cdf.parent_design_uu == inst_c1.parent

    # Retrieve the parameter definition for the 'c' parameter
    # Note: There are several ways to retrieve a parameter definition, as shown below
    param_def = inst_cdf.find_param_def("c")  # Returns None if not found
    assert param_def is not None
    assert param_def == inst_cdf.param_def("c")  # Throws if not found

    # The ParamDef on the instance is the same as the ParamDef on the CellCDF
    assert param_def == cell_cdf.find_param("c")  # Returns None if not found
    assert param_def == cell_cdf.param("c")  # Throws if not found

    # Note: The CDF.params property creates a collection of all the parameter definitions and while
    # that can be quite helpful for use with a debugger, it is not recommended for use cases requiring
    # high performance
    assert param_def == cell_cdf.params["c"]  # Throws if not found

    # Like ParamDef, there are multiple ways to retrieve a Parameter
    parameter = inst_cdf.find_param("c")  # Returns None if not found
    assert parameter is not None
    assert parameter == inst_cdf.param("c")  # Throws if not found

    # The parameter can also be retrieved using the ParamDef
    assert parameter == inst_cdf.param(param_def)  # Throws if not found

    # Similar to CDF.params, the Instance.params property will create a collection of Parameter
    # and may have a performance impact; consider using the param or find_param methods
    assert parameter == inst_cdf.params["c"]

    # Retrieve the value of the Parameter
    value = parameter.value
    assert value is not None

    # There are multiple ways to get and set the value of a parameter
    assert value == inst_cdf.param_value(param_def)
    # param_value_no_default will only return a value if the value is not the default value
    assert not inst_cdf.is_modified
    assert inst_cdf.param_value_no_default(param_def) is None

    # Set the value of the parameter
    parameter.value = "3p"
    assert inst_cdf.param_value(param_def) == "3p"
    # The CDF instance is now modified and param_value_no_default will return the modified value
    assert inst_cdf.is_modified
    assert inst_cdf.param_value_no_default(param_def) == "3p"

    # Set the value of the parameter using the ParamDef
    inst_cdf.set_param_value(param_def, "4p")
    assert parameter.value == "4p"

    # Set the value of the parameter using the parameter name
    inst_cdf.set_param_value("c", "5p")
    assert parameter.value == "5p"

    # Set the value of the parameter by indexing into the params collection
    inst_cdf.params["c"].value = "6p"
    assert parameter.value == "6p"

    # NOTE: Be sure to call update_instance to apply the changes or they will be lost
    inst_cdf.update_instance(inst_c1)
    inst_c1 = design.instances["C1"]
    assert inst_cdf.param("c").value == "6p"
```

Example illustrating how to add a new parameter definition to an interoperable component before placing an instance

```
def adding_a_new_parameter_definition_to_a_cell_cdf(design: db_uu.Design, library: de.Library) -> None:
    from keysight.ads.de import experimental as exp

    # Retrieve the cell CDF from the 'cap' cell
    cell_cdf = exp.cdf.cell_cdf(library, "cap")
    # Create an interface to the CDF parameters
    inst_cdf_from_design = exp.cdf.InstanceParams(design, cell_cdf)

    # Create a new ParamDef, new_param, with a display name of "New Parameter" and a default value of 10
    new_param_def = exp.cdf.ParamDef("new_param", exp.cdf.ParamType.INT)
    new_param_def.prompt = "New Parameter"
    new_param_def.default_value = 10

    # Add the new parameter to the CellCDF
    inst_cdf_from_design.cell_cdf.add_param(new_param_def)
    # Add a new instance of cap to the design
    design.add_instance((library.lib_name, "cap", "symbol"), (0, 0), name="C2")
    # Retrieve the instance just added
    inst_c2 = design.instances["C2"]

    # Create the interface to the CDF instance parameters
    inst_cdf = exp.cdf.InstanceParams(inst_c2)
    assert inst_cdf.param("new_param").value == 10

    # Update the value after placing the instance, as desired
    inst_cdf.param("new_param").value = 25

    # NOTE: Be sure to call update_instance to apply the changes or they will be lost
    inst_c2 = design.instances["C2"]
    inst_cdf = exp.cdf.InstanceParams(inst_c2)
    # Uh-oh, we forgot to call update_instance and the change was lost!
    assert inst_cdf.param("new_param").value == 10

    # So, let's try again ...
    inst_cdf.param("new_param").value = 25
    inst_cdf.update_instance(inst_c2)

    # Verify the result by re-obtaining the instance and validating the parameter value
    inst_c2 = design.instances["C2"]
    inst_cdf = exp.cdf.InstanceParams(inst_c2)
    assert inst_cdf.param("new_param").value == 25
```

On this page

[Previous

Parameters](index.md)
[Next

Working with VAR](ex_working_with_var.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top