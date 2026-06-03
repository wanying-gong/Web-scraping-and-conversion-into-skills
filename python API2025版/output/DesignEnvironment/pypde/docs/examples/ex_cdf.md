<!-- 来源: pypde\docs\examples\ex_cdf.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* [Examples](index.md)
* Interoperable Component Parameters

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../../../pydocs/intro/index.md)
  + [Licensing](../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../pydocs/intro/extension.md)
* [Concepts](../../../pydocs/concepts/index.md)
  + [Terminology](../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../pydocs/concepts/execution.md)
* [How-To](../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../pydocs/howto/pytest.md)

* [Design](../index.md)
  + [Reference](../reference/index.md)
    - [keysight.ads.de](../reference/de/index.md)
      * [Workspace](../reference/de/workspace.md)
      * [Library](../reference/de/library.md)
      * [Cell](../reference/de/cell.md)
      * [View](../reference/de/view.md)
      * [CellviewRef](../reference/de/cellviewref.md)
      * [DesignHierarchy](../reference/de/design_hierarchy.md)
      * [DMData](../reference/de/dmdata.md)
      * [ItemInfo](../reference/de/item_info.md)
      * [Points](../reference/de/points.md)
      * [Collections](../reference/de/collections.md)
    - [keysight.ads.de.ael](../reference/de/ael.md)
    - [keysight.ads.de.app](../reference/de/app/index.md)
      * [Actions and Menus](../reference/de/app/action.md)
      * [Addons](../reference/de/app/addon.md)
      * [Callbacks](../reference/de/app/callbacks.md)
      * [Windows and Widgets](../reference/de/app/window.md)
    - [keysight.ads.de.db](../reference/de/db/index.md)
      * [Callbacks](../reference/de/db/callbacks.md)
      * [Enumerated Types](../reference/de/db/enums.md)
      * [Parameter Forms](../reference/de/db/forms.md)
      * [GenPolyline](../reference/de/db/genpolyline.md)
      * [Model Definition](../reference/de/db/model_def.md)
      * [Parameters](../reference/de/db/parameters.md)
      * [Properties](../reference/de/db/properties.md)
      * [Transaction](../reference/de/db/transaction.md)
    - [keysight.ads.de.db\_dbu](../reference/de/db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../reference/de/db_uu/index.md)
      * [Design Elements](../reference/de/db_uu/db_uu.md)
      * [LayerId](../reference/de/db_uu/layer_id.md)
      * [LineTypeInfo](../reference/de/db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../reference/de/experimental/index.md)
      * [CDF](../reference/de/experimental/cdf/index.md)
      * [Commands](../reference/de/experimental/commands.md)
      * [Handles](../reference/de/experimental/handles.md)
      * [Netlist Utilities](../reference/de/experimental/netlist_helper.md)
      * [Polygon Utilities](../reference/de/experimental/polygon_utils.md)
      * [Preferences](../reference/de/experimental/preferences.md)
      * [xxPro View](../reference/de/experimental/pro_view.md)
      * [Symbol Generator](../reference/de/experimental/symbol.md)
      * [Text Maker](../reference/de/experimental/text_maker.md)
    - [keysight.ads.de.tech](../reference/de/tech/index.md)
      * [Tech](../reference/de/tech/tech.md)
      * [Padstacks](../reference/de/tech/pads/pads.md)
      * [Via Rules](../reference/de/tech/rule/rule.md)
      * [Nested Technology](../reference/de/tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../reference/de/app/dds.md)
  + [Examples](index.md)
    - [Calling Between AEL and Python](ex_calling_ael_and_python.md)
    - [Create Layout](ex_create_layout.md)
    - [Create Schematic](ex_create_schematic.md)
    - [Create Workspace](ex_workspace.md)
    - [Create, Simulate, and Plot](ex_create_sim_and_plot.md)
    - Interoperable Component Parameters
    - [Component Parameters](ex_parameters.md)
    - [Creating an Item Definition](ex_itemdef.md)
    - [Model Definition Properties](ex_model.md)
    - [Adding Instances to a Design](ex_lpf.md)
    - [Properties](ex_properties.md)
    - [Creating Custom Menus Using an Addon](ex_menu_addon.md)
    - [Padstacks and Vias](ex_padstack.md)
    - [Nested Technology](ex_nested.md)
    - [Rules](ex_rules.md)
    - [Placing Text](ex_place_text.md)
    - [Paths, Traces, and Polygons](ex_polygon.md)
    - [PySide2](ex_pyside.md)
    - [Traversing Hierarchy](ex_traversing_hierarchy.md)
    - [Working with VAR](ex_working_with_var.md)
    - [XML RPC](ex_xml_rpc.md)
    - [GDSII Import and Export](ex_translate_gds.md)
* [Technology](../../../pysubst/docs/index.md)
  + [Reference](../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../pysubst/docs/examples/ex_substrate_with_layout.md)

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

Create, Simulate, and Plot](ex_create_sim_and_plot.md)
[Next

Component Parameters](ex_parameters.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top