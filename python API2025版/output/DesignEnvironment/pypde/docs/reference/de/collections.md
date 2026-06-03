<!-- 来源: pypde\docs\reference\de\collections.html -->

[![Logo](../../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [ADS](../../../../index.md)
* [Design](../../index.md)
* [Reference](../index.md)
* [keysight.ads.de](index.md)
* Collections

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
      * [DesignHierarchy](design_hierarchy.md)
      * [DMData](dmdata.md)
      * [ItemInfo](item_info.md)
      * [Points](points.md)
      * Collections
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

# Collections[](#collections "Link to this heading")

Collection classes are not intended to be instantiated directly and are used as accessors to the individual elements of a collection returned in various classes.

*class* keysight.ads.de.\_list\_like.IndexedMutableCollectionAbc[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc "Link to this definition")
:   An abstract base class (ABC) for a list-like collection of elements.

    This is used to support cases where the elements are controlled
    by the owner.
    Assigning elements will assign the new objects to the owner.
    Inserting or appending new elements will add the new objects to the owner.
    Deleting an element from the collection will remove it from the owner.

    *abstract* \_\_delitem\_\_(*index: int*) → None[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__delitem__ "Link to this definition")

    *abstract* \_\_getitem\_\_(*index*)[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__getitem__ "Link to this definition")

    *abstract* \_\_iadd\_\_(*values: T | Sequence[T]*) → [IndexedMutableCollectionAbc](#keysight.ads.de._list_like.IndexedMutableCollectionAbc "keysight.ads.de._list_like.IndexedMutableCollectionAbc")[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__iadd__ "Link to this definition")

    \_\_iter\_\_()[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__iter__ "Link to this definition")

    *abstract* \_\_len\_\_()[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__len__ "Link to this definition")

    *abstract* \_\_setitem\_\_(*index: int*, *value: T*) → None[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.__setitem__ "Link to this definition")

    *abstract* \_\_setitem\_\_(*index: slice*, *value: Sequence[T]*) → None

    *abstract* append(*values: T | Sequence[T]*) → None[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.append "Link to this definition")

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.count "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    *abstract* insert(*index: int*, *values: T | Sequence[T]*) → None[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.insert "Link to this definition")

    *abstract* pop(*index: int = -1*) → T[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.pop "Link to this definition")

    *abstract* remove(*index: int*) → None[](#keysight.ads.de._list_like.IndexedMutableCollectionAbc.remove "Link to this definition")

*class* keysight.ads.de.\_list\_like.NamedMutableCollectionAbc[](#keysight.ads.de._list_like.NamedMutableCollectionAbc "Link to this definition")
:   An abstract base class (ABC) for a mutable collection of named wrapper objects.

    This is used to support cases where the elements are controlled
    by the owner.

    *abstract* \_\_delitem\_\_(*key: str*) → None[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.__delitem__ "Link to this definition")

    *abstract* \_\_getitem\_\_(*key: str*) → T[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.__getitem__ "Link to this definition")

    \_\_init\_\_(*\*args*, *\*\*kwargs*)[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.__init__ "Link to this definition")

    *abstract* \_\_iter\_\_() → Iterator[T][](#keysight.ads.de._list_like.NamedMutableCollectionAbc.__iter__ "Link to this definition")

    *abstract* \_\_len\_\_() → int[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.__len__ "Link to this definition")

    *abstract* add(*value: T*) → None[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.add "Link to this definition")

    *abstract* find(*key: str*) → T | None[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.find "Link to this definition")
    :   Find an item by name. Returns None if not found.

    *abstract* get(*key: str*) → T | None[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.get "Link to this definition")
    :   Find an item by name. Returns None if not found.

    *abstract* names() → list[str][](#keysight.ads.de._list_like.NamedMutableCollectionAbc.names "Link to this definition")
    :   Return the names in this collection.

    *abstract* remove(*value: T*) → None[](#keysight.ads.de._list_like.NamedMutableCollectionAbc.remove "Link to this definition")

On this page

[Previous

Points](points.md)
[Next

keysight.ads.de.ael](ael.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top