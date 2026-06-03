<!-- 来源: concepts\ael_type_conversions.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [AEL Python Documentation](../index.md)
* [Concepts](index.md)
* AEL Type Conversions

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
* [Concepts](index.md)
  + [AEL Interoperability](ael_interoperability.md)
  + AEL Type Conversions
* [Reference](../reference/index.md)
  + [keysight.ads.ael](../reference/ael.md)
* [How-To](../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../howto/venv.md)
    - [Creating an ADS based Python virtual environment](../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../howto/existingvenv.md)
    - [ADS Python Environment Variables](../howto/pyenvvars.md)
  + [How to Use Pytest](../howto/pytest.md)
* [Examples](../examples/index.md)
  + [Calling Between AEL and Python](../examples/ex_calling_ael_and_python.md)

# AEL Type Conversions[](#ael-type-conversions "Link to this heading")

This table is not an exhaustive list of all AEL type conversions. Consider using the `type` function for any values returned by AEL functions to see their Python type.

AEL types that do not have a corresponding Python type may still be used opaquely and passed to other AEL functions.

| Python Type | AEL Type | Notes |
| --- | --- | --- |
| `bool` | `ee_bool` | AEL `TRUE` and `FALSE` are integer-typed values. |
| `int` | `int` |  |
| `float` | `double` |  |
| `complex` | `complex()` | Python `4 + 2j` is the equivalent to AEL `complex(4, 2)` |
| `str` | `string` | AEL `string` is a sequence of characters, similar to Python’s string type. |
| `Design` | `DesignContext` | An AEL `DesignContext` is equivalent to a Python `Design` object. |
| `ApolloObject` | `Corresponding component type Object` | AEL objects are converted to their corresponding Python `ApolloObject` type. For example, an AEL `Instance` is converted to a Python `Instance` object. |

On this page

[Previous

AEL Interoperability](ael_interoperability.md)
[Next

Reference](../reference/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top