<!-- 来源: pypde\docs\reference\de\db\forms.html -->

[![Logo](../../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../../index.md)
* [Design](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.de.db](index.md)
* Parameter Forms

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

* [Introduction](../../../../../pydocs/intro/index.md)
  + [Licensing](../../../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../../../pydocs/intro/extension.md)
* [Concepts](../../../../../pydocs/concepts/index.md)
  + [Terminology](../../../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../../../pydocs/concepts/execution.md)
* [How-To](../../../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../../../pydocs/howto/pytest.md)

* [Design](../../../index.md)
  + [Reference](../../index.md)
    - [keysight.ads.de](../index.md)
      * [Workspace](../workspace.md)
      * [Library](../library.md)
      * [Cell](../cell.md)
      * [View](../view.md)
      * [CellviewRef](../cellviewref.md)
      * [DesignHierarchy](../design_hierarchy.md)
      * [DMData](../dmdata.md)
      * [ItemInfo](../item_info.md)
      * [Points](../points.md)
      * [Collections](../collections.md)
    - [keysight.ads.de.ael](../ael.md)
    - [keysight.ads.de.app](../app/index.md)
      * [Actions and Menus](../app/action.md)
      * [Addons](../app/addon.md)
      * [Callbacks](../app/callbacks.md)
      * [Windows and Widgets](../app/window.md)
    - [keysight.ads.de.db](index.md)
      * [Callbacks](callbacks.md)
      * [Enumerated Types](enums.md)
      * Parameter Forms
      * [GenPolyline](genpolyline.md)
      * [Model Definition](model_def.md)
      * [Parameters](parameters.md)
      * [Properties](properties.md)
      * [Transaction](transaction.md)
    - [keysight.ads.de.db\_dbu](../db_dbu/index.md)
    - [keysight.ads.de.db\_uu](../db_uu/index.md)
      * [Design Elements](../db_uu/db_uu.md)
      * [LayerId](../db_uu/layer_id.md)
      * [LineTypeInfo](../db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](../experimental/index.md)
      * [CDF](../experimental/cdf/index.md)
      * [Commands](../experimental/commands.md)
      * [Handles](../experimental/handles.md)
      * [Netlist Utilities](../experimental/netlist_helper.md)
      * [Polygon Utilities](../experimental/polygon_utils.md)
      * [Preferences](../experimental/preferences.md)
      * [xxPro View](../experimental/pro_view.md)
      * [Symbol Generator](../experimental/symbol.md)
      * [Text Maker](../experimental/text_maker.md)
    - [keysight.ads.de.tech](../tech/index.md)
      * [Tech](../tech/tech.md)
      * [Padstacks](../tech/pads/pads.md)
      * [Via Rules](../tech/rule/rule.md)
      * [Nested Technology](../tech/nested/nested.md)
    - [keysight.ads.de.app.dds](../app/dds.md)
  + [Examples](../../../examples/index.md)
    - [Calling Between AEL and Python](../../../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../../examples/ex_create_layout.md)
    - [Create Schematic](../../../examples/ex_create_schematic.md)
    - [Create Workspace](../../../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../../examples/ex_cdf.md)
    - [Component Parameters](../../../examples/ex_parameters.md)
    - [Creating an Item Definition](../../../examples/ex_itemdef.md)
    - [Model Definition Properties](../../../examples/ex_model.md)
    - [Adding Instances to a Design](../../../examples/ex_lpf.md)
    - [Properties](../../../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../../examples/ex_padstack.md)
    - [Nested Technology](../../../examples/ex_nested.md)
    - [Rules](../../../examples/ex_rules.md)
    - [Placing Text](../../../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../../examples/ex_polygon.md)
    - [PySide2](../../../examples/ex_pyside.md)
    - [Traversing Hierarchy](../../../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../../examples/ex_working_with_var.md)
    - [XML RPC](../../../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../../examples/ex_translate_gds.md)
* [Technology](../../../../../pysubst/docs/index.md)
  + [Reference](../../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Parameter Forms[](#parameter-forms "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.CompoundForm[](#keysight.ads.de.db.CompoundForm "Link to this definition")
:   Bases: [`Form`](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")

    CompoundForm is a type of Form for a parameter that contains one or more sub-parameters.

    The CompoundForm describes how the parameter is netlisted and displayed.
    The Form for each sub-parameter describes how that portion of the parameter is netlisted and displayed.
    The number of sub-parameters is fixed by the parameter definition.

    \_\_init\_\_(*name: str*, *label: str = ''*, *params: Sequence[[ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")] = []*, *net\_format: str = ''*, *display\_format: str = ''*, *dialog\_data: str = ''*) → None[](#keysight.ads.de.db.CompoundForm.__init__ "Link to this definition")

    add\_parameter(*parameter: [ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")*) → None[](#keysight.ads.de.db.CompoundForm.add_parameter "Link to this definition")

    *property* parameters*: NamedListRefAbc[[ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")]*[](#keysight.ads.de.db.CompoundForm.parameters "Link to this definition")

*class* keysight.ads.de.db.ConstForm[](#keysight.ads.de.db.ConstForm "Link to this definition")
:   Bases: [`Form`](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")

    A Form representing a fixed value, such as “Yes” or 1.

    \_\_init\_\_(*name: str*, *label: str | None = None*, *net\_format: str | None = None*, *display\_format: str | None = None*, *dialog\_data: str = ''*) → None[](#keysight.ads.de.db.ConstForm.__init__ "Link to this definition")

*class* keysight.ads.de.db.Form[](#keysight.ads.de.db.Form "Link to this definition")
:   All parameter values are described by a Form that defines how the parameter is netlisted and displayed.

    A Form must appear in the Formset of a parameter definition in order to be usable by that parameter.
    See [`Formset`](#keysight.ads.de.db.Formset "keysight.ads.de.db.Formset") and class de.db.ModelParam.

    *property* dialog\_data*: str*[](#keysight.ads.de.db.Form.dialog_data "Link to this definition")
    :   A string used by edit dialogs for this form.

        If this string is empty, the name of the form will be used by default.

    *property* discrete*: bool*[](#keysight.ads.de.db.Form.discrete "Link to this definition")

    *property* display\_format*: str*[](#keysight.ads.de.db.Form.display_format "Link to this definition")
    :   The display format string for values using this form.

    *static* is\_compound\_form(*form: [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → TypeGuard[[CompoundForm](#keysight.ads.de.db.CompoundForm "keysight.ads.de.db._forms.CompoundForm")][](#keysight.ads.de.db.Form.is_compound_form "Link to this definition")

    *static* is\_constant\_form(*form: [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → TypeGuard[[ConstForm](#keysight.ads.de.db.ConstForm "keysight.ads.de.db._forms.ConstForm")][](#keysight.ads.de.db.Form.is_constant_form "Link to this definition")

    *static* is\_null\_form(*form: [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → TypeGuard[[NullForm](#keysight.ads.de.db.NullForm "keysight.ads.de.db._forms.NullForm")][](#keysight.ads.de.db.Form.is_null_form "Link to this definition")

    *static* is\_string\_form(*form: [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → TypeGuard[[StringForm](#keysight.ads.de.db.StringForm "keysight.ads.de.db._forms.StringForm")][](#keysight.ads.de.db.Form.is_string_form "Link to this definition")

    *property* label*: str*[](#keysight.ads.de.db.Form.label "Link to this definition")
    :   Short descriptive label of the Form.

    *property* name*: str*[](#keysight.ads.de.db.Form.name "Link to this definition")
    :   Unique name of the Form.

    *property* net\_format*: str*[](#keysight.ads.de.db.Form.net_format "Link to this definition")
    :   The netlist format string for values using this form.

*class* keysight.ads.de.db.Formset[](#keysight.ads.de.db.Formset "Link to this definition")
:   A Formset holds one or more Forms that define how a parameter is netlisted and displayed.

    \_\_init\_\_(*name: str*, *forms: Sequence[[Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")]*) → None[](#keysight.ads.de.db.Formset.__init__ "Link to this definition")

    contains(*name: str*) → bool[](#keysight.ads.de.db.Formset.contains "Link to this definition")
    :   contains is deprecated, and will be removed in the 2025 Update 2 release. Use Formset.forms.find(name) is not None.

    find\_constant\_form\_by\_label\_or\_display(*label\_or\_display: str*) → [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form") | None[](#keysight.ads.de.db.Formset.find_constant_form_by_label_or_display "Link to this definition")

    find\_form\_by\_label(*label: str*) → [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form") | None[](#keysight.ads.de.db.Formset.find_form_by_label "Link to this definition")

    find\_form\_by\_name(*name: str*) → [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form") | None[](#keysight.ads.de.db.Formset.find_form_by_name "Link to this definition")

    *property* forms*: NamedListRefAbc[[Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")]*[](#keysight.ads.de.db.Formset.forms "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.Formset.name "Link to this definition")

*class* keysight.ads.de.db.NullForm[](#keysight.ads.de.db.NullForm "Link to this definition")
:   Bases: [`Form`](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")

    A Form representing a parameter with no value.

*class* keysight.ads.de.db.RepeatedForm[](#keysight.ads.de.db.RepeatedForm "Link to this definition")
:   Bases: [`Form`](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")

    RepeatedForm is the form used for a parameter that is repeatable.

    All repeatable parameters share the same RepeatedForm.

*class* keysight.ads.de.db.StringForm[](#keysight.ads.de.db.StringForm "Link to this definition")
:   Bases: [`Form`](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")

    A Form representing a value stored in a string.

    \_\_init\_\_(*name: str*, *label: str | None = None*, *net\_format: str = '%v'*, *display\_format: str = '%v'*, *dialog\_data: str = ''*) → None[](#keysight.ads.de.db.StringForm.__init__ "Link to this definition")

*class* keysight.ads.de.db.StringFormWithAELCallbacks[](#keysight.ads.de.db.StringFormWithAELCallbacks "Link to this definition")
:   Bases: [`StringForm`](#keysight.ads.de.db.StringForm "keysight.ads.de.db._forms.StringForm")

*class* keysight.ads.de.db.StringFormWithCallbacks[](#keysight.ads.de.db.StringFormWithCallbacks "Link to this definition")
:   Bases: [`StringForm`](#keysight.ads.de.db.StringForm "keysight.ads.de.db._forms.StringForm")

    \_\_init\_\_(*name: str*, *label: str | None = None*, *net\_format: str = '%v'*, *display\_format: str = '%v'*, *dialog\_data: str = ''*, *option\_cb: Callable[[[Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")], list[str]] | None = None*, *valid\_cb: Callable[[str], bool] | None = None*, *data\_cb: Callable[[[ParamItem](parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem"), [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")], list[str]] | None = None*) → None[](#keysight.ads.de.db.StringFormWithCallbacks.__init__ "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.de.db.global\_model\_lib() → ModelLib[](#keysight.ads.de.db.global_model_lib "Link to this definition")

db.model\_lib *A collection of global forms and formsets.*[](#keysight.ads.de.db.model_lib "Link to this definition")

On this page

[Previous

Enumerated Types](enums.md)
[Next

GenPolyline](genpolyline.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top