<!-- 来源: pypde\docs\examples\ex_model.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* [Examples](index.md)
* Model Definition Properties

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
    - [Interoperable Component Parameters](ex_cdf.md)
    - [Component Parameters](ex_parameters.md)
    - [Creating an Item Definition](ex_itemdef.md)
    - Model Definition Properties
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

# Model Definition Properties[](#model-definition-properties "Link to this heading")

This example shows how to create a model definition with a model name parameter that will netlist at the front of the netlist string

```
def components_with_and_without_a_model_param_parameter(library: de.Library, design: db_uu.Design) -> None:
    # Example showing how an instance is netlisted differently when ModelDef.has_model_param is set

    # This netlist callback is implemented here to show the netlist for an instance when the
    # ModelDef.has_model_param property is or is not set. If you wish to use the default
    # netlist behavior, there is no need to implement this callback.
    def netlist_callback(std_inst: de.db.StandardInstance) -> str:
        from keysight.ads.de.experimental.netlist_helper import NetlistStringBuilder

        model_def = std_inst.model_def
        assert model_def

        netlist_builder = NetlistStringBuilder(std_inst)
        netlist = netlist_builder.clear_and_get_default_netlist_str()

        if model_def.has_model_param:
            # When has_model_param is set, the value of the first parameter is treated as the Model name and will be
            # netlisted at the front in quotes. The remaining parameters will be netlisted as normal.
            assert netlist == '"MyComp":MC1  Length=5.0 mil '
        else:
            # When has_model_param is not set, the standard netlist format will be used and the first parameter,
            # along with the remaining parameters, will be netlisted as normal.
            assert netlist == "MyComponent:MC1  Model=MyComp Length=5.0 mil "

        return netlist

    # Typically create_itemdef would be a function in a module called itemdef.py in the cell for your component
    def create_itemdef(cell: de.Cell) -> de.db.ModelDef:
        assert cell.name == "MyComponent"
        # Use the standard formset from the global model lib
        standard_formset = de.db.model_lib.formsets["StdFormSet"]
        # Create a model with a couple parameters, the first one being a string parameter representing the model name
        param_model = de.db.ModelParam("Model", "Model instance name", standard_formset, de.db.ModelUnitType.STRING)
        param_model.default_value = de.db.std_string_param("MyComp")
        # The model name parameter should be set so that it is not evaluated by the expression evaluator
        param_model.is_evaluated = False

        param_length = de.db.ModelParam("Length", "Length", standard_formset, de.db.ModelUnitType.LENGTH)
        param_length.default_value = de.db.std_string_param("5.0 mil")

        my_component = de.db.ModelDef(cell.cell_name, cell.cell_name)
        my_component.inst_name_prefix = "MC"
        my_component.is_sub_design = False
        my_component.parameters = [param_model, param_length]
        my_component.callbacks = [(de.db.ModelCb(de.db.ModelCbType.ITEM_NETLIST, netlist_callback))]
        de.add_model_definition(cell.library, my_component)
        return my_component

    # Starting with a clear schematic ...
    assert design.is_schematic
    design.clear_design()

    my_comp_cell = library.create_cell("MyComponent")
    mc_def = create_itemdef(my_comp_cell)
    create_symbol(library, my_comp_cell)
    design.add_instance((f"{library.name}", "MyComponent", "symbol"), (0, 0))

    # See netlist_callback() for the effect ModelDef.has_model_param has on the netlist
    assert mc_def.has_model_param is False
    design.generate_netlist()
    mc_def.has_model_param = True
    design.generate_netlist()
```

This example shows the transmission line property on a model definition

```
def transmission_line_property(library: de.Library, design: db_uu.Design) -> None:
    assert design.is_schematic
    design.clear_design()

    # Typically create_itemdef would be a function in a module called itemdef.py in the cell for your component
    def create_itemdef(cell: de.Cell) -> de.db.ModelDef:
        assert cell.name == "MyTLine"

        # Use the standard formset from the global model lib
        standard_formset = de.db.model_lib.formsets["StdFormSet"]

        param_width = de.db.ModelParam("W", "Line Width", standard_formset, de.db.ModelUnitType.LENGTH)
        param_width.default_value = de.db.std_string_param("25.0 mil")
        param_length = de.db.ModelParam("L", "Line Length", standard_formset, de.db.ModelUnitType.LENGTH)
        param_length.default_value = de.db.std_string_param("100.0 mil")
        param_temp = de.db.ModelParam("Temp", "Temperature", standard_formset, de.db.ModelUnitType.TEMPERATURE)
        param_temp.default_value = de.db.std_string_param("")
        param_temp.is_displayed_by_default = False

        my_tline = de.db.ModelDef(cell.cell_name, cell.cell_name)
        my_tline.parameters = [param_width, param_length, param_temp]
        my_tline.inst_name_prefix = "MTLn"
        # When defining your own transmission line components, set the is_transmission_line property to True
        my_tline.is_transmission_line = True
        de.add_model_definition(cell.library, my_tline)

        return my_tline

    my_tline_cell = library.create_cell("MyTLine")
    create_itemdef(my_tline_cell)
    create_symbol(library, my_tline_cell)
    tl_inst = design.add_instance((f"{library.name}", "MyTLine", "symbol"), (0, 0))
    tl_model = tl_inst.model_def
    assert tl_model
    assert tl_model.is_transmission_line

    # Any transmission line component provided by ADS will have the ModelDefl.is_transmission_line property set to True
    mlin_inst = design.add_instance(("ads_tlines:MLIN:symbol"), (3, 0))
    mlin_model = mlin_inst.model_def
    assert mlin_model
    assert mlin_model.is_transmission_line
```

This example shows the is\_unique property on a model definition

```
def is_unique_property(library: de.Library, design: db_uu.Design) -> None:
    assert design.is_schematic
    design.clear_design()

    # Typically create_itemdef would be a function in a module called itemdef.py in the cell for your component
    def create_itemdef(cell: de.Cell) -> de.db.ModelDef:
        # Nothing special about this component other than its is_unique property
        assert cell.cell_name == "MyUniqComp"
        my_uniq_comp = de.db.ModelDef(cell.cell_name, cell.cell_name)
        my_uniq_comp.inst_name_prefix = "MUC"
        my_uniq_comp.is_unique = True
        de.add_model_definition(cell.library, my_uniq_comp)
        return my_uniq_comp

    my_uniq_cell = library.create_cell("MyUniqComp")
    create_itemdef(my_uniq_cell)
    create_symbol(library, my_uniq_cell)
    # Placing one unique component is fine
    design.add_instance((f"{library.name}", "MyUniqComp", "symbol"), (0, 0))
    try:
        # Attempting to place another results in an error
        design.add_instance((f"{library.name}", "MyUniqComp", "symbol"), (3, 0))
    except RuntimeError as e:
        assert "This item is defined to be unique. Only one instance of this type can be placed." in str(e)
```

On this page

[Previous

Creating an Item Definition](ex_itemdef.md)
[Next

Adding Instances to a Design](ex_lpf.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top