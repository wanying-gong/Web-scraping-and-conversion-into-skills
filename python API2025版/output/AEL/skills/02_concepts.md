# Concepts
> **说明：** AEL 与 Python 互操作、类型转换等核心概念。

> **何时使用：** 当你需要理解 AEL/Python 互操作机制或类型转换规则时

---

## 本文件目录

- **Concepts** (`concepts/index.md`)
- **AEL Interoperability** (`concepts/ael_interoperability.md`)
- **AEL Type Conversions** (`concepts/ael_type_conversions.md`)

---

<!-- === 来源: concepts/index.md === -->

# Concepts[](#concepts "Link to this heading")

* [AEL Interoperability](ael_interoperability.md)
  + [Calling AEL From Python](ael_interoperability.md#calling-ael-from-python)
  + [Calling Python From AEL](ael_interoperability.md#calling-python-from-ael)
* [AEL Type Conversions](ael_type_conversions.md)


---

<!-- === 来源: concepts/ael_interoperability.md === -->

# AEL Interoperability[](#ael-interoperability "Link to this heading")

ADS provides a bridge between AEL and Python, allowing you to call AEL functions from Python, and Python functions from AEL.

## Calling AEL From Python[](#calling-ael-from-python "Link to this heading")

AEL functions may be called from Python using the `ael` package, which provides the interface to any loaded AEL function.

Many types are automatically converted between Python objects and AEL types, as described in [Converting Values](#converting-values-label)

```
from keysight.ads import ael
from keysight.ads.de.experimental_uu import db as db_uu

design = db_uu.open_design("my_lib:my_cell:layout")
# The AEL function `db_get_cell_name(DesignContext)` is callable via the `ael` package
# Automatic type conversion of both the Design object and return string
cell_name = ael.call.db_get_cell_name(design)
assert design.cell_name == cell_name
```

### Specifying the Vocabulary[](#specifying-the-vocabulary "Link to this heading")

AEL names are divided into namespaces called *vocabularies*. Each vocabulary has a set of
names that it contains, plus an optional link to a parent vocabulary. Searching for an
identifier in a vocabulary will first look in that vocabulary’s names, and if not found,
will recursively look in the parent vocabulary.

The default vocabulary is often a fine choice.

To specify a different vocabulary, use this form:

```
# Calls the "other_function" function in the "Other" vocabulary.
ael.call(vocab="Other").other_function()

# Gets the AEL variable named "xyz" in the "Other" vocabulary.
ael.decl(vocab="Other").xyz
```

Not all the AEL functions available in ADS are available when running in automation mode.
While not a comprehensive rule, API’s that access application features, such as the GUI, are not available in automation mode.

Attempts to call a function that isn’t available will raise an exception.

To control the behavior of your scripts when running in automation mode, you can
call either running\_automation or is\_pde\_app or call the AEL function is\_function\_defined() to check if
a particular function is callable.

```
from keysight.ads import ael
from keysight.ads import de
# If you already know a function isn't available unless ADS is running, use is_pde_app
if de.is_pde_app():
    ael.call.de_save_all_designs()

# Alternatively, check if the function is defined
if ael.call.is_function_defined("de_save_all_designs"):
    ael.call.de_save_all_designs()
```

See [AEL Bridge](../reference/ael.md#ael-bridge-label) for more information.

## Calling Python From AEL[](#calling-python-from-ael "Link to this heading")

The following is a list of AEL functions that can be used for executing Python code.

### python\_call()[](#python-call "Link to this heading")

Calls the specified Python function with an optional argument list.

```
result = python_call(callable [,args] [,convert]);

callable: any callable, such as a function or object with the __call__() attribute.
args: an optional AEL list of arguments, list("arg1", "arg2"), defaults to an empty list
convert: optional Boolean, one of:
    TRUE: Convert the result to an AEL type or raise an error on conversion failure
    NULL: Convert the result to an AEL type or return it as a PythonObject on conversion failure
    FALSE: Always return the result as a PythonObject
    defaults to NULL

Example:
    os_module = python_import_module("os")
    getenv_func = python_get_attr(os_module, "getenv")
    result = python_call(getenv_func, list("HPEESOF_DIR"))
```

### python\_eval()[](#python-eval "Link to this heading")

Evaluates the specified string as a Python expression.

```
result = python_eval(expression [,convert]);

expression: a string containing a Python expression
convert: optional Boolean, one of:
    TRUE: Convert the result to an AEL type or raise an error on conversion failure
    NULL: Convert the result to an AEL type or return it as a PythonObject on conversion failure
    FALSE: Always return the result as a PythonObject
    defaults to NULL

Example:
    result = python_eval("10 / 4");  // returns 2.5
```

### python\_exec()[](#python-exec "Link to this heading")

Executes the statements in the specified string as a Python script.

This function does not return a value.

```
python_exec(statements);

script: a string containing Python statements

Example:
    python_exec("print('Hello, world!')");

Example:
    decl statements = strcat("def my_function(x):");
    statements = strcat(statements, "\tprint(f'Hello World! {x}')\n");
    statements = strcat(statements, "my_function(10)\n");
    python_exec(statements);
```

### python\_exec\_file()[](#python-exec-file "Link to this heading")

Executes the statements contained in the specified file as a Python script.
This function operates similarly to python\_exec but reads the statements from a file.

This function does not return a value.

```
python_exec_file(filename);

filename: The file containing python statements

Example:
    python_exec_file("my_script.py");
```

### python\_get\_attr()[](#python-get-attr "Link to this heading")

Returns the attribute object from the specified object.

```
result = python_get_attr(object, attributeName [,convert]);

object: a PythonObject (class, module, etc.)
attributeName: the name of the attribute
convert: optional Boolean, one of:
    TRUE: Convert the result to an AEL type or raise an error on conversion failure
    NULL: Convert the result to an AEL type or return it as a PythonObject on conversion failure
    FALSE: Always return the result as a PythonObject
    defaults to NULL

Example:
    osModule = python_import_module("os")
    getenvFunc = python_get_attr(osModule, "getenv")
    result = python_call(getenvFunc, list("HPEESOF_DIR"))
```

### python\_import\_module()[](#python-import-module "Link to this heading")

Imports the specified module.

```
result = python_import_module(modulePath);

modulePath: The path to the module ("os", "keysight.ads.de", etc.)

Example:
    osModule = python_import_module("os");

Example:
    deModule = python_import_module("keysight.ads.de");
```

### python\_to\_ael()[](#python-to-ael "Link to this heading")

Converts the PythonObject to an AEL type.

```
result = python_to_ael(pythonObject, [convert]);

pythonObject: An instance of PythonObject
convert: optional Boolean, one of:
    TRUE: Convert the result to an AEL type or raise an error on conversion failure
    NULL: Convert the result to an AEL type or return it as a PythonObject on conversion failure
    FALSE: Always return the result as a PythonObject
    defaults to NULL
```

### ael\_to\_python()[](#ael-to-python "Link to this heading")

Converts the AEL value to a PythonObject.

```
result = ael_to_python(aelValue, [convert])

aelValue: Any AEL object
convert: option Boolean, one of:
    TRUE: Convert the result to an AEL type, or raise an error on conversion failure
    NULL: Convert the result to an AEL type, or return it as a PythonObject on conversion failure
    FALSE: Always return the result as a PythonObject

    result: An object of the AEL type "PythonObject".
    The underlying `py::object` is the result of the conversion to Python.
    If no conversion is defined, then the underlying `py::object` is of type `ael.AELValue`
```

### Converting Values[](#converting-values "Link to this heading")

Many values will be automatically converted from Python types to AEL types, or vice versa.
For example, in this call:

```
ael.call.strcat(1, "a")
```

there are several automatic conversions.

> 1. The Python integer value `1` is converted to an AEL integer value `1`.
> 2. The Python string value `"a"` is converted to an AEL string value `"a"`.
> 3. After the call, the AEL string value `"1a"` is converted to the Python string value `"1a"`.

Many application-specific types are converted too. See [AEL Type Conversions](ael_type_conversions.md) for more.

If a Python value cannot be converted to an AEL type, it is instead wrapped in an AEL type
`PythonObject`. This allows a Python object to be passed to AEL, and passed back to Python,
even if there is no AEL equivalent for the type.

Similarly, if an AEL value cannot be converted to a Python type, it is instead wrapped in a
Python object [`AELValue`](../reference/ael.md#keysight.ads.ael.AELValue "keysight.ads.ael.AELValue"). This allows an AEL value to be passed to Python, and passed
back to AEL, even if there is no Python equivalent for the type.

To have more control over conversions, use the keyword argument `convert`.

* `convert=None` (default): Convert the value if possible, otherwise wrap it in a `PythonObject`
  or [`AELValue`](../reference/ael.md#keysight.ads.ael.AELValue "keysight.ads.ael.AELValue").
* `convert=True`: Require conversion to succeed. Raise an exception if conversion fails.
* `convert=False`: Do not convert. Always wrap the value in a `PythonObject` or
  [`AELValue`](../reference/ael.md#keysight.ads.ael.AELValue "keysight.ads.ael.AELValue").

Examples:

```
ael.decl.MyTuple = ael.AELValue((1, 2, 3), convert=False)
```

Also see [AEL Type Conversions](ael_type_conversions.md).

See [Calling Between AEL and Python](../examples/ex_calling_ael_and_python.md) for more examples.

Todo

Describe getting var values from AEL


---

<!-- === 来源: concepts/ael_type_conversions.md === -->

# AEL Type Conversions[](#ael-type-conversions "Link to this heading")

| Python Type | AEL Type | Notes |
| --- | --- | --- |
| `bool` | `ee_bool` | AEL `TRUE` and `FALSE` are integer-typed values. |
| `int` | `int` |  |
| `float` | `double` |  |

Todo

Fill out the table of AEL type conversions


---

