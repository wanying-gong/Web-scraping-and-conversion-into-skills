<!-- 来源: pypde\docs\examples\ex_rules.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* [Examples](index.md)
* Rules

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
    - [Model Definition Properties](ex_model.md)
    - [Adding Instances to a Design](ex_lpf.md)
    - [Properties](ex_properties.md)
    - [Creating Custom Menus Using an Addon](ex_menu_addon.md)
    - [Padstacks and Vias](ex_padstack.md)
    - [Nested Technology](ex_nested.md)
    - Rules
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

# Rules[](#rules "Link to this heading")

The following example shows to create a clearance rule, add it to the technology of a library, and save it.

```
def creating_a_clearance_rule(library: de.Library) -> None:
    # Clearance rules specify the minimum clearance between two objects

    # NOTE: You cannot create a rule that already exists
    assert not library.tech.clearance_rules.find("Example Clearance Rule")

    # Create a clearance rule with a default clearance of 10.0
    rule = tech.rule.ClearanceRule(library, "Example Clearance Rule", 10.0)

    # Set the priority of the rule, higher priority rules will take precedence over lower priority rules
    # The numerical value of the priority must be greater than or equal to zero and is relative to other
    # rule priorities; the higher the number, the higher the priority
    rule.priority = 10

    # By default, a new rule is enabled
    assert rule.enabled

    # Rules apply to a pair of objects, the first object must match the first scope and the second object,
    # the second scope.
    # By default, the both the first and second scope are set to tech.rule.ScopeType.Default
    assert rule.first_scope == rule.second_scope == tech.rule.DefaultScope()
    # The same as
    assert rule.first_scope.scope_type == rule.second_scope.scope_type == tech.rule.ScopeType.DEFAULT

    # For this example, the first scope will refer to the my_net Net
    rule.first_scope = tech.rule.NetClassScope(["my_net"])

    # The second scope will refer to any net that is not the my_net Net
    rule.second_scope = tech.rule.DifferentNetScope()

    # By default, the rule will apply to all layers, but for this example,
    # We'll specify a few different layers and show how to set different clearances for
    # different object types

    # when viewing the result inside ADS
    # Let's apply this rule to the M3, 9, and M12 layers
    rule.layers = ["M3", "M9", "M12"]

    # The rule values are a 2D matrix of the clearance values between the object types
    # The object types are:
    # Trace
    # Pad
    # Via
    # Plane
    rule.rule_values[("Plane", "Trace")] = 25.0
    rule.rule_values[("Plane", "Pad")] = 40.0
    rule.rule_values[("Plane", "Via")] = 55.0

    # The values for the object types that are not explicitly set use the default_clearance,
    # whose initial value is set when the rule is created
    assert rule.default_clearance == 10.0

    # NOTE: The order of the object types in the tuple doesn't matter
    assert rule.rule_values[("Plane", "Trace")] == rule.rule_values[("Trace", "Plane")] == 25.0

    # Add the clearance rule to the technology and save it
    library.tech.clearance_rules.add(rule)
    library.tech.save_rules()
```

The following image shows how the clearance rule created above appears inside the constraints manager of ADS.

![../../../_images/clearance_rule.png](../../../_images/clearance_rule.png)

The following example shows how to delete a clearance rule from the technology of a library.

```
def deleting_a_clearance_rule(library: de.Library) -> None:
    # Ensure the clearance rule exists before trying to delete it
    if not library.tech.clearance_rules.find("Example Clearance Rule"):
        creating_a_clearance_rule(library)

    assert library.tech.clearance_rules.find("Example Clearance Rule")

    # Deleting a clearance rule is straightforward
    del library.tech.clearance_rules["Example Clearance Rule"]
    assert not library.tech.clearance_rules.find("Example Clearance Rule")
    library.tech.save_rules()
```

The following examples shows how to create a via rule.

```
def creating_a_via_rule(library: de.Library) -> None:
    lib_name = library.name
    # Create a new via rule for cond to m2 from the Example Padstack
    # NOTE: The padstack name is in the form of "library_name:padstack_name"
    via_cond_m2_rule = tech.rule.ViaRule("via_cond_m2", f"{lib_name}:Example Padstack", "cond", "M2")

    # Set the priority of the rule, higher priority rules will take precedence over lower priority rules
    # The numerical value of the priority must be greater than or equal to zero and is relative to other
    # rule priorities; the higher the number, the higher the priority
    via_cond_m2_rule.priority = 10

    # Rules are enabled by default, but no harm in being explicit
    via_cond_m2_rule.enabled = True

    assert via_cond_m2_rule.name == "via_cond_m2"
    assert via_cond_m2_rule.padstack_name == f"{lib_name}:Example Padstack"
    assert via_cond_m2_rule.has_layer_constraints
    assert via_cond_m2_rule.top_layer == "cond"
    assert via_cond_m2_rule.bottom_layer == "M2"

    # Create another rule. You don't need to specify the layers up front if you don't want to
    via_m2_m3_rule = tech.rule.ViaRule("via_m2_m3", f"{lib_name}:Example Padstack")

    # There are no constraints set
    assert not via_m2_m3_rule.has_layer_constraints
    assert via_m2_m3_rule.top_layer == ""
    assert via_m2_m3_rule.bottom_layer == ""
    # Set them here
    via_m2_m3_rule.set_layer_constraints("M2", "M3")
    assert via_m2_m3_rule.has_layer_constraints
    assert via_m2_m3_rule.top_layer == "M2"
    assert via_m2_m3_rule.bottom_layer == "M3"

    via_m2_m3_rule.priority = 10
    via_m2_m3_rule.enabled = True

    # Add the rules to the library and save them
    library.tech.via_rules.add(via_cond_m2_rule)
    library.tech.via_rules.add(via_m2_m3_rule)
    library.tech.save_rules()
```

The following image shows how the via rule created above appears inside the constraints manager of ADS.

![../../../_images/creating_via_rules.png](../../../_images/creating_via_rules.png)

The following example shows how to create a stacked via rule.

```
def creating_a_stacked_via_rule(library: de.Library) -> None:
    libname = library.name
    # Ensure we have the via rules we need
    if library.tech.via_rules.find("via_cond_m2"):
        del library.tech.via_rules["via_cond_m2"]
    if library.tech.via_rules.find("via_m2_m3"):
        del library.tech.via_rules["via_m2_m3"]

    creating_a_via_rule(library)

    via_cond_m2_rule = library.tech.via_rules["via_cond_m2"]
    via_m2_m3_rule = library.tech.via_rules["via_m2_m3"]

    # Make the via rules stackable
    via_cond_m2_rule.is_stackable = True
    via_m2_m3_rule.is_stackable = True

    # Create a stacked via rule using the two via rules, via_cond_m2 and via_m2_m3
    # Rule names are in the form of "libname:rule_name"
    stacked_rule = tech.rule.StackedViaRule(
        "stacked_cond_m3", "cond", "M3", [f"{libname}:via_cond_m2", f"{libname}:via_m2_m3"]
    )
    stacked_rule.enabled = True
    library.tech.stacked_via_rules.add(stacked_rule)
    library.tech.save_rules()
```

The following image shows how the padstack rule created above appears inside the constraints manager of ADS.

![../../../_images/stacked_via_rule.png](../../../_images/stacked_via_rule.png)

The following example shows how to place the vias constrained by the rules defined above.

```
def placing_constrained_vias(design: db_uu.Design, library: de.Library) -> None:
    libname = library.name

    if not library.tech.padstacks.find("Example Padstack"):
        # See ex_padstack.py for the padstack template used in this example
        # NOTE: If you've copied/pasted this code into the ADS Python console,
        # you may need to execute building_up_a_padstack from ex_padstack.py
        # first to create "Example Padstack".
        from . import ex_padstack

        ex_padstack.building_up_a_padstack(library)

    if not library.tech.stacked_via_rules.find("stacked_cond_m3"):
        creating_a_stacked_via_rule(library)

    cond_layer = db_uu.LayerId.create_layer_id_from_library(library, "cond")
    m2_layer = db_uu.LayerId.create_layer_id_from_library(library, "M2")
    m3_layer = db_uu.LayerId.create_layer_id_from_library(library, "M3")

    design.add_trace(cond_layer, [(0, -200), (200, -200)], 25)
    design.add_constrained_via(f"{libname}:via_cond_m2", (200, -200))
    design.add_trace(m2_layer, [(200, -200), (200, -400)], 25)
    design.add_constrained_via(f"{libname}:via_m2_m3", (200, -400))
    design.add_trace(m3_layer, [(200, -400), (0, -400)], 25)
    design.add_stacked_via(f"{libname}:stacked_cond_m3", (0, -400))
```

The following image shows the vias placed using the rules defined above.

![../../../_images/placing_constrained_vias.png](../../../_images/placing_constrained_vias.png)

On this page

[Previous

Nested Technology](ex_nested.md)
[Next

Placing Text](ex_place_text.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top