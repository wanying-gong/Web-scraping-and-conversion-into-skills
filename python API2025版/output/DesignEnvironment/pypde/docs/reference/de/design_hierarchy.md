<!-- 来源: pypde\docs\reference\de\design_hierarchy.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Design](../../index.md)
* [Reference](../index.md)
* [keysight.ads.de](index.md)
* DesignHierarchy

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

* [Introduction](../../../../pydocs/intro/index.md)
  + [Licensing](../../../../pydocs/intro/licensing.md)
  + [Using Python in ADS Design Environment](../../../../pydocs/intro/embedded.md)
  + [Using ADS Design Environment Functionality in Python](../../../../pydocs/intro/extension.md)
* [Concepts](../../../../pydocs/concepts/index.md)
  + [Terminology](../../../../pydocs/concepts/terminology.md)
    - [Workspace Elements](../../../../pydocs/concepts/workspace_elements.md)
    - [Connectivity Objects](../../../../pydocs/concepts/connectivity.md)
  + [OpenAccess Integration](../../../../pydocs/concepts/openaccess_integration.md)
  + [Python Script Execution](../../../../pydocs/concepts/execution.md)
* [How-To](../../../../pydocs/howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../../pydocs/howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../../pydocs/howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../../pydocs/howto/existingvenv.md)
  + [How to Use Pytest](../../../../pydocs/howto/pytest.md)

* [Design](../../index.md)
  + [Reference](../index.md)
    - [keysight.ads.de](index.md)
      * [Workspace](workspace.md)
      * [Library](library.md)
      * [Cell](cell.md)
      * [View](view.md)
      * [CellviewRef](cellviewref.md)
      * DesignHierarchy
      * [DMData](dmdata.md)
      * [ItemInfo](item_info.md)
      * [Points](points.md)
      * [Collections](collections.md)
    - [keysight.ads.de.ael](ael.md)
    - [keysight.ads.de.app](app/index.md)
      * [Actions and Menus](app/action.md)
      * [Addons](app/addon.md)
      * [Callbacks](app/callbacks.md)
      * [Windows and Widgets](app/window.md)
    - [keysight.ads.de.db](db/index.md)
      * [Callbacks](db/callbacks.md)
      * [Enumerated Types](db/enums.md)
      * [Parameter Forms](db/forms.md)
      * [GenPolyline](db/genpolyline.md)
      * [Model Definition](db/model_def.md)
      * [Parameters](db/parameters.md)
      * [Properties](db/properties.md)
      * [Transaction](db/transaction.md)
    - [keysight.ads.de.db\_dbu](db_dbu/index.md)
    - [keysight.ads.de.db\_uu](db_uu/index.md)
      * [Design Elements](db_uu/db_uu.md)
      * [LayerId](db_uu/layer_id.md)
      * [LineTypeInfo](db_uu/line_type_info.md)
    - [keysight.ads.de.experimental](experimental/index.md)
      * [CDF](experimental/cdf/index.md)
      * [Commands](experimental/commands.md)
      * [Handles](experimental/handles.md)
      * [Netlist Utilities](experimental/netlist_helper.md)
      * [Polygon Utilities](experimental/polygon_utils.md)
      * [Preferences](experimental/preferences.md)
      * [xxPro View](experimental/pro_view.md)
      * [Symbol Generator](experimental/symbol.md)
      * [Text Maker](experimental/text_maker.md)
    - [keysight.ads.de.tech](tech/index.md)
      * [Tech](tech/tech.md)
      * [Padstacks](tech/pads/pads.md)
      * [Via Rules](tech/rule/rule.md)
      * [Nested Technology](tech/nested/nested.md)
    - [keysight.ads.de.app.dds](app/dds.md)
  + [Examples](../../examples/index.md)
    - [Calling Between AEL and Python](../../examples/ex_calling_ael_and_python.md)
    - [Create Layout](../../examples/ex_create_layout.md)
    - [Create Schematic](../../examples/ex_create_schematic.md)
    - [Create Workspace](../../examples/ex_workspace.md)
    - [Create, Simulate, and Plot](../../examples/ex_create_sim_and_plot.md)
    - [Interoperable Component Parameters](../../examples/ex_cdf.md)
    - [Component Parameters](../../examples/ex_parameters.md)
    - [Creating an Item Definition](../../examples/ex_itemdef.md)
    - [Model Definition Properties](../../examples/ex_model.md)
    - [Adding Instances to a Design](../../examples/ex_lpf.md)
    - [Properties](../../examples/ex_properties.md)
    - [Creating Custom Menus Using an Addon](../../examples/ex_menu_addon.md)
    - [Padstacks and Vias](../../examples/ex_padstack.md)
    - [Nested Technology](../../examples/ex_nested.md)
    - [Rules](../../examples/ex_rules.md)
    - [Placing Text](../../examples/ex_place_text.md)
    - [Paths, Traces, and Polygons](../../examples/ex_polygon.md)
    - [PySide2](../../examples/ex_pyside.md)
    - [Traversing Hierarchy](../../examples/ex_traversing_hierarchy.md)
    - [Working with VAR](../../examples/ex_working_with_var.md)
    - [XML RPC](../../examples/ex_xml_rpc.md)
    - [GDSII Import and Export](../../examples/ex_translate_gds.md)
* [Technology](../../../../pysubst/docs/index.md)
  + [Reference](../../../../pysubst/docs/reference/index.md)
    - [keysight.ads.subst](../../../../pysubst/docs/reference/subst/index.md)
  + [Examples](../../../../pysubst/docs/examples/index.md)
    - [Create Substrate](../../../../pysubst/docs/examples/ex_make_substrate.md)
    - [Substrate with Layout](../../../../pysubst/docs/examples/ex_substrate_with_layout.md)

# DesignHierarchy[](#designhierarchy "Link to this heading")

*class* keysight.ads.de.DesignHierarchy[](#keysight.ads.de.DesignHierarchy "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.DesignHierarchy.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* depth*: int*[](#keysight.ads.de.DesignHierarchy.depth "Link to this definition")

    *property* design*: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*[](#keysight.ads.de.DesignHierarchy.design "Link to this definition")

    *property* is\_at\_root*: bool*[](#keysight.ads.de.DesignHierarchy.is_at_root "Link to this definition")

    is\_primitive\_instance(*inst: [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*) → bool[](#keysight.ads.de.DesignHierarchy.is_primitive_instance "Link to this definition")

    parent\_designs() → Iterable[[Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")][](#keysight.ads.de.DesignHierarchy.parent_designs "Link to this definition")

    parent\_instance\_names() → Iterable[str][](#keysight.ads.de.DesignHierarchy.parent_instance_names "Link to this definition")

    pop() → [DesignHierarchy](#keysight.ads.de.DesignHierarchy "keysight.ads.de._core.design_hierarchy.DesignHierarchy")[](#keysight.ads.de.DesignHierarchy.pop "Link to this definition")

    push\_instance\_for\_reading(*inst: [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*) → [DesignHierarchy](#keysight.ads.de.DesignHierarchy "keysight.ads.de.DesignHierarchy")[](#keysight.ads.de.DesignHierarchy.push_instance_for_reading "Link to this definition")
    :   Push into the instance in read-only mode.

        Modifications of a read-only design may only be saved to a new cellview.

    push\_instance\_for\_writing(*inst: [Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*) → [DesignHierarchy](#keysight.ads.de.DesignHierarchy "keysight.ads.de.DesignHierarchy")[](#keysight.ads.de.DesignHierarchy.push_instance_for_writing "Link to this definition")
    :   Push into the instance in edit mode.

    *property* root\_design*: [Design](db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*[](#keysight.ads.de.DesignHierarchy.root_design "Link to this definition")

    traverse\_instances(*include\_implicit: bool = False*, *include\_pin\_insts: bool = True*, *limit\_box: [BoxF](points.md#keysight.ads.de.BoxF "keysight.ads.de.BoxF") | None = None*, *allow\_box\_intersect: bool = True*) → Iterable[tuple[[Instance](db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance"), [DesignHierarchy](#keysight.ads.de.DesignHierarchy "keysight.ads.de.DesignHierarchy")]][](#keysight.ads.de.DesignHierarchy.traverse_instances "Link to this definition")
    :   Iterate through design hierarchically.

        Parameters:
        :   * **include\_implicit** (*bool*) – Defaults to false and will include implicit shapes individually when set. For example
              bus nets will show up as one when set to false, but will be enumerated individually
              when set to True.
            * **include\_pin\_insts** (*bool*) – Defaults to True and will include PinInst objects during the traversal.
            * **limit\_box** ([*BoxF*](points.md#keysight.ads.de.BoxF "keysight.ads.de.BoxF")) – Default to None and when set will limit the traversal to the specified region in user units.
            * **allow\_box\_intersect** (*bool*) – Defaults to True and when set includes instances that intersect the specified box to be part
              of the traversal, otherwise only instances wholly inside the box are returned.

        Example

        ```
        >>> for x, _ in topdsn.get_hierarchy_for_netlist().traverse_instances(include_implicit = True):
        ...     print(f"Inst = {x}")
        ```

On this page

[Previous

CellviewRef](cellviewref.md)
[Next

DMData](dmdata.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top