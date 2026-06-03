<!-- 来源: pypde\docs\reference\de\tech\rule\rule.html -->

[![Logo](../../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../../index.md)
* [Design](../../../../index.md)
* [Reference](../../../index.md)
* [keysight.ads.de.tech](../index.md)
* Via Rules

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

* [Introduction](../../../../../../pydocs/intro/index.md)
  + [Licensing](../../../../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../../../../pydocs/intro/extension.md)
* [Concepts](../../../../../../pydocs/concepts/index.md)
  + [Terminology](../../../../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../../../../pydocs/concepts/execution.md)
* [How-To](../../../../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../../../../pydocs/howto/pytest.md)

* [Design](../../../../index.md)
  + [Reference](../../../index.md)
    - [keysight.ads.de](../../index.md)
      * [Workspace](../../workspace.md)
      * [Library](../../library.md)
      * [Cell](../../cell.md)
      * [View](../../view.md)
      * [CellviewRef](../../cellviewref.md)
      * [DesignHierarchy](../../design_hierarchy.md)
      * [DMData](../../dmdata.md)
      * [ItemInfo](../../item_info.md)
      * [Points](../../points.md)
      * [Collections](../../collections.md)
    - [keysight.ads.de.ael](../../ael.md)
    - [keysight.ads.de.app](../../app/index.md)
      * [Actions and Menus](../../app/action.md)
      * [Addons](../../app/addon.md)
      * [Callbacks](../../app/callbacks.md)
      * [Windows and Widgets](../../app/window.md)
    - [keysight.ads.de.db](../../db/index.md)
      * [Callbacks](../../db/callbacks.md)
      * [Enumerated Types](../../db/enums.md)
      * [Parameter Forms](../../db/forms.md)
      * [GenPolyline](../../db/genpolyline.md)
      * [Model Definition](../../db/model_def.md)
      * [Parameters](../../db/parameters.md)
      * [Properties](../../db/properties.md)
      * [Transaction](../../db/transaction.md)
    - [keysight.ads.de.db\_dbu](../../db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../../db_uu/index.md)
      * [Design Elements](../../db_uu/db_uu.md)
      * [LayerId](../../db_uu/layer_id.md)
      * [LineTypeInfo](../../db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../../experimental/index.md)
      * [CDF](../../experimental/cdf/index.md)
      * [Commands](../../experimental/commands.md)
      * [Handles](../../experimental/handles.md)
      * [Netlist Utilities](../../experimental/netlist_helper.md)
      * [Polygon Utilities](../../experimental/polygon_utils.md)
      * [Preferences](../../experimental/preferences.md)
      * [xxPro View](../../experimental/pro_view.md)
      * [Symbol Generator](../../experimental/symbol.md)
      * [Text Maker](../../experimental/text_maker.md)
    - [keysight.ads.de.tech](../index.md)
      * [Tech](../tech.md)
      * [Padstacks](../pads/pads.md)
      * Via Rules
      * [Nested Technology](../nested/nested.md)
    - [keysight.ads.de.app.dds](../../app/dds.md)
  + [Examples](../../../../examples/index.md)
    - [Calling Between AEL and Python](../../../../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../../../examples/ex_create_layout.md)
    - [Create Schematic](../../../../examples/ex_create_schematic.md)
    - [Create Workspace](../../../../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../../../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../../../examples/ex_cdf.md)
    - [Component Parameters](../../../../examples/ex_parameters.md)
    - [Creating an Item Definition](../../../../examples/ex_itemdef.md)
    - [Model Definition Properties](../../../../examples/ex_model.md)
    - [Adding Instances to a Design](../../../../examples/ex_lpf.md)
    - [Properties](../../../../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../../../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../../../examples/ex_padstack.md)
    - [Nested Technology](../../../../examples/ex_nested.md)
    - [Rules](../../../../examples/ex_rules.md)
    - [Placing Text](../../../../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../../../examples/ex_polygon.md)
    - [PySide2](../../../../examples/ex_pyside.md)
    - [Traversing Hierarchy](../../../../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../../../examples/ex_working_with_var.md)
    - [XML RPC](../../../../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../../../examples/ex_translate_gds.md)
* [Technology](../../../../../../pysubst/docs/index.md)
  + [Reference](../../../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Via Rules[](#via-rules "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.tech.rule.ClearanceRule[](#keysight.ads.de.tech.rule.ClearanceRule "Link to this definition")
:   Defines rules used to create clearances.

    \_\_init\_\_(*lib: [Library](../../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *name: str*, *value: float*) → None[](#keysight.ads.de.tech.rule.ClearanceRule.__init__ "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.tech.rule.ClearanceRule.name "Link to this definition")

    *property* enabled*: bool*[](#keysight.ads.de.tech.rule.ClearanceRule.enabled "Link to this definition")

    *property* priority*: int*[](#keysight.ads.de.tech.rule.ClearanceRule.priority "Link to this definition")

    *property* layers*: list[str]*[](#keysight.ads.de.tech.rule.ClearanceRule.layers "Link to this definition")

    *property* default\_clearance*: float*[](#keysight.ads.de.tech.rule.ClearanceRule.default_clearance "Link to this definition")

    *property* max\_rule\_value*: float*[](#keysight.ads.de.tech.rule.ClearanceRule.max_rule_value "Link to this definition")

    *property* rule\_values*: \_TechClearanceRuleValuesAdapter*[](#keysight.ads.de.tech.rule.ClearanceRule.rule_values "Link to this definition")
    :   A collection of clearance values by object type.

    *property* first\_scope*: [RuleScope](#keysight.ads.de.tech.rule.RuleScope "keysight.ads.de.tech.rule.RuleScope")*[](#keysight.ads.de.tech.rule.ClearanceRule.first_scope "Link to this definition")

    *property* second\_scope*: [RuleScope](#keysight.ads.de.tech.rule.RuleScope "keysight.ads.de.tech.rule.RuleScope")*[](#keysight.ads.de.tech.rule.ClearanceRule.second_scope "Link to this definition")

*class* keysight.ads.de.tech.rule.DefaultScope[](#keysight.ads.de.tech.rule.DefaultScope "Link to this definition")
:   Rule applies in all cases.

    \_\_init\_\_() → None[](#keysight.ads.de.tech.rule.DefaultScope.__init__ "Link to this definition")

*class* keysight.ads.de.tech.rule.DifferentNetScope[](#keysight.ads.de.tech.rule.DifferentNetScope "Link to this definition")
:   Rule applies to pairs of objects on the different nets.

    \_\_init\_\_() → None[](#keysight.ads.de.tech.rule.DifferentNetScope.__init__ "Link to this definition")

*class* keysight.ads.de.tech.rule.LineTypeScope[](#keysight.ads.de.tech.rule.LineTypeScope "Link to this definition")
:   Rule applies to the specified line types.

    \_\_init\_\_(*line\_types: Sequence[str]*) → None[](#keysight.ads.de.tech.rule.LineTypeScope.__init__ "Link to this definition")

    *property* line\_types*: list[str]*[](#keysight.ads.de.tech.rule.LineTypeScope.line_types "Link to this definition")

*class* keysight.ads.de.tech.rule.NetClassScope[](#keysight.ads.de.tech.rule.NetClassScope "Link to this definition")
:   Rule applies to objects on the specified nets.

    \_\_init\_\_(*net\_names: Sequence[str]*) → None[](#keysight.ads.de.tech.rule.NetClassScope.__init__ "Link to this definition")

    *property* net\_names*: list[str]*[](#keysight.ads.de.tech.rule.NetClassScope.net_names "Link to this definition")

*class* keysight.ads.de.tech.rule.NetScope[](#keysight.ads.de.tech.rule.NetScope "Link to this definition")
:   Rule applies to objects on the specified net.

    \_\_init\_\_(*net\_name: str*) → None[](#keysight.ads.de.tech.rule.NetScope.__init__ "Link to this definition")

    *property* net\_name*: str*[](#keysight.ads.de.tech.rule.NetScope.net_name "Link to this definition")

*class* keysight.ads.de.tech.rule.RuleScope[](#keysight.ads.de.tech.rule.RuleScope "Link to this definition")
:   Base class for rule scopes.

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.tech.rule.RuleScope.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* scope\_type*: ScopeType*[](#keysight.ads.de.tech.rule.RuleScope.scope_type "Link to this definition")

*class* keysight.ads.de.tech.rule.SameNetScope[](#keysight.ads.de.tech.rule.SameNetScope "Link to this definition")
:   Rule applies to pairs of objects on the same net.

    \_\_init\_\_() → None[](#keysight.ads.de.tech.rule.SameNetScope.__init__ "Link to this definition")

*class* keysight.ads.de.tech.rule.StackedViaRule[](#keysight.ads.de.tech.rule.StackedViaRule "Link to this definition")
:   Defines rules used to create Stacked PCB Vias.

    \_\_init\_\_(*name: str*, *top\_layer: str*, *bottom\_layer: str*, *rules: Sequence[str]*) → None[](#keysight.ads.de.tech.rule.StackedViaRule.__init__ "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.tech.rule.StackedViaRule.name "Link to this definition")

    *property* top\_layer*: str*[](#keysight.ads.de.tech.rule.StackedViaRule.top_layer "Link to this definition")

    *property* bottom\_layer*: str*[](#keysight.ads.de.tech.rule.StackedViaRule.bottom_layer "Link to this definition")

    *property* enabled*: bool*[](#keysight.ads.de.tech.rule.StackedViaRule.enabled "Link to this definition")

    *property* priority*: int*[](#keysight.ads.de.tech.rule.StackedViaRule.priority "Link to this definition")

    *property* via\_rules*: ListRefAbc[str]*[](#keysight.ads.de.tech.rule.StackedViaRule.via_rules "Link to this definition")
    :   Return the collection of via rules in this stacked via rule.

*class* keysight.ads.de.tech.rule.TeardropRule[](#keysight.ads.de.tech.rule.TeardropRule "Link to this definition")
:   Defines rules used to create Teardrop definitions.

    \_\_init\_\_(*name: str*, *definition: [TeardropDefinition](../../db/genpolyline.md#keysight.ads.de.db.TeardropDefinition "keysight.ads.de.db.TeardropDefinition")*, *layers: Sequence[str] = []*) → None[](#keysight.ads.de.tech.rule.TeardropRule.__init__ "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.tech.rule.TeardropRule.name "Link to this definition")

    *property* definition*: [TeardropDefinition](../../db/genpolyline.md#keysight.ads.de.db.TeardropDefinition "keysight.ads.de.db.TeardropDefinition")*[](#keysight.ads.de.tech.rule.TeardropRule.definition "Link to this definition")

    *property* enabled*: bool*[](#keysight.ads.de.tech.rule.TeardropRule.enabled "Link to this definition")

    *property* priority*: int*[](#keysight.ads.de.tech.rule.TeardropRule.priority "Link to this definition")

    *property* layers*: list[str]*[](#keysight.ads.de.tech.rule.TeardropRule.layers "Link to this definition")

*class* keysight.ads.de.tech.rule.ViaRule[](#keysight.ads.de.tech.rule.ViaRule "Link to this definition")
:   Defines rules used to create PCB Vias.

    \_\_init\_\_(*name: str*, *padstack\_name: str*) → None[](#keysight.ads.de.tech.rule.ViaRule.__init__ "Link to this definition")

    \_\_init\_\_(*name: str*, *padstack\_name: str*, *top\_layer: str*, *bottom\_layer: str*) → None

    *property* name*: str*[](#keysight.ads.de.tech.rule.ViaRule.name "Link to this definition")

    *property* padstack\_name*: str*[](#keysight.ads.de.tech.rule.ViaRule.padstack_name "Link to this definition")

    *property* enabled*: bool*[](#keysight.ads.de.tech.rule.ViaRule.enabled "Link to this definition")

    *property* is\_stackable*: bool*[](#keysight.ads.de.tech.rule.ViaRule.is_stackable "Link to this definition")

    *property* has\_layer\_constraints*: bool*[](#keysight.ads.de.tech.rule.ViaRule.has_layer_constraints "Link to this definition")

    set\_unconstrained() → None[](#keysight.ads.de.tech.rule.ViaRule.set_unconstrained "Link to this definition")
    :   Clear the layer constraints. See set\_layer\_constraints.

    set\_layer\_constraints(*top\_layer: str*, *bottom\_layer: str*) → None[](#keysight.ads.de.tech.rule.ViaRule.set_layer_constraints "Link to this definition")
    :   Set layer constraints. See set\_unconstrained.

    *property* top\_layer*: str*[](#keysight.ads.de.tech.rule.ViaRule.top_layer "Link to this definition")

    *property* bottom\_layer*: str*[](#keysight.ads.de.tech.rule.ViaRule.bottom_layer "Link to this definition")

    *property* priority*: int*[](#keysight.ads.de.tech.rule.ViaRule.priority "Link to this definition")

On this page

[Previous

Padstacks](../pads/pads.md)
[Next

Nested Technology](../nested/nested.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top