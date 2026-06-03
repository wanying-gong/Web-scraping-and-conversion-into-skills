<!-- 来源: pypde\docs\examples\ex_working_with_var.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../index.md)
* [Design](../index.md)
* [Examples](index.md)
* Working with VAR

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
    - [Rules](ex_rules.md)
    - [Placing Text](ex_place_text.md)
    - [Paths, Traces, and Polygons](ex_polygon.md)
    - [PySide2](ex_pyside.md)
    - [Traversing Hierarchy](ex_traversing_hierarchy.md)
    - Working with VAR
    - [XML RPC](ex_xml_rpc.md)
    - [GDSII Import and Export](ex_translate_gds.md)
* [Technology](../../../pysubst/docs/index.md)
  + [Reference](../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# Working with VAR[](#working-with-var "Link to this heading")

This example shows how to update the variables inside a VAR block and evaluate an expression.

```
def var_evaluation(library: de.Library) -> None:

    def eval_expression(design: db_uu.Design, expression: str) -> str:
        expr_context = de.db.ExpressionContext()
        expr_context.setup_hierarchy_for_design(design)
        return expr_context.evaluate_expression(expression)

    design = db_uu.create_schematic(f"{library.name}:var:schematic")

    # Place an instance of VAR
    var_inst = design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR1", angle=90)
    assert var_inst.is_var_instance

    with db_uu.Transaction(design) as transaction:
        # VAR names are case-sensitive, so
        var_inst.vars["X"] = "7.5"  # X is different from
        var_inst.vars["x"] = "3.0"  # x

        assert var_inst.vars["X"] == "7.5"
        assert var_inst.vars["x"] == "3.0"

        # Values can be expressions containing other VAR names
        var_inst.vars["Y"] = "X / x"
        transaction.commit()

    # And the expressions can be evaluated like so:
    result = float(eval_expression(design, "Y"))
    assert result == 2.5  # 7.5 / 3.0

    # ADS has built-in constants like "pi" that can be used in expression evaluation.
    # See "VAR (Variables and Equations Component)" in the ADS product documentation for more information.
    with db_uu.Transaction(design) as transaction:
        var_inst.vars["r"] = "10.0"
        var_inst.vars["area"] = "pi * r ** 2"
        transaction.commit()

    result = float(eval_expression(design, "area"))
    import math

    assert math.isclose(result, 314.159265, rel_tol=1e-6)  # pi * 10.0 ^ 2

    design.save_design()
```

This example shows how to evaluate expressions containing references to VARs higher up in the design hierarchy.

```
def var_evaluation_in_design_hierarchy(library: de.Library) -> None:
    top_design = db_uu.create_schematic(f"{library.name}:top:schematic")
    middle_design = db_uu.create_schematic(f"{library.name}:middle:schematic")
    bottom_design = db_uu.create_schematic(f"{library.name}:bottom:schematic")

    # Place a VAR in bottom_design that references a VAR in middle
    var_bottom = bottom_design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR_BOTTOM", angle=90)
    var_bottom.vars["A"] = "B + 2.0"

    # Place a VAR in middle_design that references a VAR in top
    var_middle = middle_design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR_MIDDLE", angle=90)
    var_middle.vars["B"] = "C + 3.0"

    # Place a VAR in top_design
    var_top = top_design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR_TOP", angle=90)
    var_top.vars["C"] = "5.0"

    # Top has an instance of middle and middle has an instance of bottom
    bottom_inst = middle_design.add_instance(bottom_design.design_name, (0, 0), name="bottom")
    middle_inst = top_design.add_instance(middle_design.design_name, (0, 0), name="mid")

    expr_context = de.db.ExpressionContext()
    expr_context.setup_hierarchy_for_design(top_design)
    # Push down the hierarchy to the bottom design for evaluation of A
    expr_context.push_instance_for_reading(middle_inst)
    expr_context.push_instance_for_reading(bottom_inst)
    result = float(expr_context.evaluate_expression("A"))
    assert result == 10.0  # A = B + 2.0 == C + 3.0 + 2.0 == 5.0 + 3.0 + 2.0 == 10.0
    # Pop back up to the hierarchy to evaluate B
    expr_context.pop()
    result = float(expr_context.evaluate_expression("B"))
    assert result == 8.0  # B = C + 3.0 == 5.0 + 3.0 == 8.0

    top_design.save_design()
    middle_design.save_design()
    bottom_design.save_design()
```

This example shows how to evaluate an expression containing a reference to a VAR lower in the design hierarchy.

```
def var_evaluation_in_design_hierarchy_global_scope(library: de.Library) -> None:
    top_design = db_uu.create_schematic(f"{library.name}:top_global:schematic")
    bottom_design = db_uu.create_schematic(f"{library.name}:bottom_global:schematic")
    # Place an instance of VAR (Variable and Equations component)
    with db_uu.Transaction(bottom_design) as transaction:
        var_bottom = bottom_design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR1", angle=90)
        var_bottom.vars["r"] = "10.0"
        var_bottom.vars["area"] = "pi * r ** 2"
        del var_bottom.vars["X"]
        # To evaluate an expression with a reference to a VAR in a subdesign, the VAR instance must have global scope
        var_bottom.set_global_scope()
        transaction.commit()

    with db_uu.Transaction(top_design) as transaction:
        # Add an instance of bottom_design into top_design
        top_design.add_instance(bottom_design.design_name, (0, 2), name="bottom", angle=0)

        var_top = top_design.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 0), name="VAR2", angle=90)
        var_top.vars["perim"] = "2 * pi * r"
        transaction.commit()

    bottom_design.save_design()
    top_design.save_design()

    expr_context = de.db.ExpressionContext()
    expr_context.setup_hierarchy_for_design(top_design)
    result = float(expr_context.evaluate_expression("perim"))
    import math

    assert math.isclose(result, 62.831853, rel_tol=1e-6)  # 2 * pi * 10.0
```

This example shows some of the errors that can occur when working with VARs.

```
def var_evaluation_errors(library: de.Library) -> None:
    # NOTE: The error messages below are specific to the Simple Evaluator; the Full Evaluator error messages differ
    # See the Evaluation section in the Library Configuration Editor in the ADS product documentation for more information
    # on the Simple and Full Evaluators

    bottom_design = db_uu.create_schematic(f"{library.name}:cell_error_bottom:schematic")
    var_bottom = bottom_design.add_instance(("ads_datacmps", "VAR", "symbol"), (1, 0), name="VAR1", angle=90)

    # VARs are required to have at least one name/value pair and a new instance of VAR has a default "X" = "1.0"
    # It is okay to delete name/value pairs from a VAR but there must always be at least one
    try:
        del var_bottom.vars["X"]
    except RuntimeError as e:
        assert str(e) == "VAR instances need to have always at least 1 parameter"

    # When evaluating VARs, references to names must be unique within the scope of the design hierarchy
    var_bottom2 = bottom_design.add_instance(("ads_datacmps", "VAR", "symbol"), (1, 0), name="VAR2", angle=90)

    # To which X does this refer? The one in var_bottom or var_bottom2?
    var_bottom2.vars["Y"] = "X + 2"
    expr_context = de.db.ExpressionContext()
    expr_context.setup_hierarchy_for_design(bottom_design)
    try:
        # As stated previously, a VAR instance has a name/value pair that defaults to "X" = "1.0",
        # but we cannot have two different VARs in a design with the same name
        expr_context.evaluate_expression("Y")
    except RuntimeError as e:
        assert str(e) == "Schematic variable 'X' already defined at level 0"

    top = db_uu.create_schematic(f"{library.name}:cell_error_top:schematic")
    top.add_instance(bottom_design.design_name, (0, 0), name="design", angle=90)

    # To evaluate an expression with a reference to a VAR in a subdesign, the VAR instance must have global scope
    var_bottom.vars["A"] = "5.0"
    var_top = top.add_instance(("ads_datacmps", "VAR", "symbol"), (0, 2), name="VAR2", angle=90)

    var_top.vars["B"] = "A"
    expr_context = de.db.ExpressionContext()
    expr_context.setup_hierarchy_for_design(top)
    try:
        expr_context.evaluate_expression("B")
    except RuntimeError as e:
        assert str(e) == "Error evaluating variable 'B': Error evaluating variable 'A': Variable undefined."

    # Not all expressions can be evaluated with the Simple Evaluator, which is the evaluator in automation mode
    var_top.vars["Euler"] = "e ** (pi * j)"
    if de.running_automation:
        try:
            expr_context.evaluate_expression("Euler")
        except RuntimeError as e:
            # See the Evaluation section in the Library Configuration Editor in the ADS product documentation for more information
            assert (
                str(e)
                == "Error evaluating variable 'Euler': Error evaluating variable 'j': Complex numbers are not supported by the Simple Evaluator."
            )
```

On this page

[Previous

Traversing Hierarchy](ex_traversing_hierarchy.md)
[Next

XML RPC](ex_xml_rpc.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top