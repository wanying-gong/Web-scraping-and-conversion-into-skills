<!-- 来源: pypde\docs\examples\parameters\ex_working_with_var.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Examples](../../../../examples.md)
* [Design Environment](../index.md)
* [Parameters](index.md)
* Working with VAR

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
      * [Interoperable Component Parameters](ex_cdf.md)
      * Working with VAR
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

# Working with VAR[](#working-with-var "Link to this heading")

Detailed information on the VAR (Variables and Equations) component can be found in [VAR Component Reference](..%5C..%5C..%5C..%5C..%5C..%5C..%5Cads%5CContent%5Cads2026update2%5Cccsim%5CVAR_%28Variables_and_Equations_Component%29.md).

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

Interoperable Component Parameters](ex_cdf.md)
[Next

Component Parameters](ex_parameters.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top