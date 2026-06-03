<!-- 来源: reference\ael.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [AEL Python Documentation](../index.md)
* [Reference](index.md)
* keysight.ads.ael

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

* [Introduction](../intro/index.md)
  + [Using AEL Functionality in Python](../intro/usage.md)
* [Concepts](../concepts/index.md)
  + [AEL Interoperability](../concepts/ael_interoperability.md)
  + [AEL Type Conversions](../concepts/ael_type_conversions.md)
* [Reference](index.md)
  + keysight.ads.ael
* [Examples](../examples/index.md)
  + [Calling Between AEL and Python](../examples/ex_calling_ael_and_python.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
  + [How to Use Pytest](../howto/pytest.md)

# keysight.ads.ael[](#keysight-ads-ael "Link to this heading")

## AEL Bridge[](#ael-bridge "Link to this heading")

keysight.ads.ael.call[](#keysight.ads.ael.call "Link to this definition")

The `ael.call` object is a bridge to make AEL objects accessible to Python scripts.
For example:

```
# Call the AEL function "strcat" with arguments 1 and "a".
assert ael.call.strcat(1, "a") == "1a"

# Get the AEL value "TRUE". This is an integer-typed value.
assert ael.call.TRUE == 1
```

keysight.ads.ael.decl[](#keysight.ads.ael.decl "Link to this definition")

The `ael.decl` object is also a bridge but intended to be used similarly to an AEL decl statement.
For example:

```
# Set the AEL variable named "xyz".
ael.decl.xyz = "set from Python"
```

*class* keysight.ads.ael.AELValue[](#keysight.ads.ael.AELValue "Link to this definition")
:   \_\_init\_\_(*value: Any*, *\**, *convert: bool | None = None*) → None[](#keysight.ads.ael.AELValue.__init__ "Link to this definition")

    ael\_type\_name() → str[](#keysight.ads.ael.AELValue.ael_type_name "Link to this definition")

    as\_python\_value(*convert: bool | None = None*) → Any[](#keysight.ads.ael.AELValue.as_python_value "Link to this definition")

    is\_null() → bool[](#keysight.ads.ael.AELValue.is_null "Link to this definition")

On this page

[Previous

Reference](index.md)
[Next

Examples](../examples/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top