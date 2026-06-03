<!-- 来源: reference\ael.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [AEL Python Documentation](../index.md)
* [Reference](index.md)
* keysight.ads.ael

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

* [Introduction](../intro/index.md)
  + [Using AEL Functionality in Python](../intro/usage.md)
* [Concepts](../concepts/index.md)
  + [AEL Interoperability](../concepts/ael_interoperability.md)
  + [AEL Type Conversions](../concepts/ael_type_conversions.md)
* [Reference](index.md)
  + keysight.ads.ael
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating an ADS based Python virtual environment](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
    - [ADS Python Environment Variables](../howto/pyenvvars.md)
  + [How to Use Pytest](../howto/pytest.md)
* [Examples](../examples/index.md)
  + [Calling Between AEL and Python](../examples/ex_calling_ael_and_python.md)

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
:   AELValue is an opaque type that may be returned from or passed into AEL functions.

    In most cases, you will not need to use this type directly as the underlying object represented
    by AELValue will be converted to/from either a native Python type or an ADS Python type automatically.

    Not all AEL functions will return an AELValue convertible to a Python type, however those AELValues
    may be passed to other AEL functions expecting the same underlying type.

    \_\_init\_\_(*value: Any*, *\**, *convert: bool | None = None*) → None[](#keysight.ads.ael.AELValue.__init__ "Link to this definition")

    ael\_type\_name() → str[](#keysight.ads.ael.AELValue.ael_type_name "Link to this definition")
    :   Underlying type name of the AEL value.

    as\_python\_value(*convert: bool | None = None*) → Any[](#keysight.ads.ael.AELValue.as_python_value "Link to this definition")
    :   Convert the AELValue into a Python value.

        Parameters:
        :   **convert** (*Optional**[**bool**,* *default = None**]*) –

            * If True, convert the AELValue into a Python value, or raise an exception if conversion is not possible.
            * If None, convert the AELValue into a Python value, or return the AELValue object if conversion is not possible.
            * If False, do not convert. Return the AELValue object.

    is\_null() → bool[](#keysight.ads.ael.AELValue.is_null "Link to this definition")
    :   Whether the underlying AEL value is null.

On this page

[Previous

Reference](index.md)
[Next

How-To](../howto/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top