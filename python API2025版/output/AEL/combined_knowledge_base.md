# AEL Python Documentation Knowledge Base
> 本文件由 MarkItDown 自动转换，BFS 遍历自 Keysight ADS2025 Update 2 AEL Python 文档。
> 共 13 个页面。

---

## 目录 (Table of Contents)

1. [index.md](#index)
2. [intro\index.md](#intro--index)
3. [intro\usage.md](#intro--usage)
4. [concepts\index.md](#concepts--index)
5. [concepts\ael_interoperability.md](#concepts--ael_interoperability)
6. [concepts\ael_type_conversions.md](#concepts--ael_type_conversions)
7. [reference\index.md](#reference--index)
8. [reference\ael.md](#reference--ael)
9. [examples\index.md](#examples--index)
10. [examples\ex_calling_ael_and_python.md](#examples--ex_calling_ael_and_python)
11. [howto\index.md](#howto--index)
12. [howto\venv.md](#howto--venv)
13. [howto\pytest.md](#howto--pytest)

---



---

## 1. index.md {#index}

# AEL Python documentation[](#ael-python-documentation "Link to this heading")

Contents:

* [Introduction](intro/index.md)
  + [Using AEL Functionality in Python](intro/usage.md)
* [Concepts](concepts/index.md)
  + [AEL Interoperability](concepts/ael_interoperability.md)
  + [AEL Type Conversions](concepts/ael_type_conversions.md)
* [Reference](reference/index.md)
  + [keysight.ads.ael](reference/ael.md)
* [Examples](examples/index.md)
  + [Calling Between AEL and Python](examples/ex_calling_ael_and_python.md)
* [How-To](howto/index.md)
  + [How to Set Up a Python Virtual Environment](howto/venv.md)
  + [How to Use Pytest](howto/pytest.md)


---

## 2. intro\index.md {#intro--index}

# Introduction[](#introduction "Link to this heading")

* [Using AEL Functionality in Python](usage.md)


---

## 3. intro\usage.md {#intro--usage}

# Using AEL Functionality in Python[](#using-ael-functionality-in-python "Link to this heading")

A Python script running inside of ADS can access functionality of AEL.

```
from keysight.ads import ael
```

The `keysight.ads.ael` package is not currently available as a pip-installable package.
To get access to this package, use any one of these approaches:

> 1. Use the Python interpreter in `$HPEESOF_DIR/tools/python`.
> 2. Create a virtual environment based on that interpreter. See [How to Set Up a Python Virtual Environment](../howto/venv.md).
> 3. Add `$HPEESOF_DIR/tools/python/packages` onto your Python’s `sys.path`.

Set the environment variable `HPEESOF_DIR` to point to your ADS installation prior to
using the `keysight.ads.ael` package.


---

## 4. concepts\index.md {#concepts--index}

# Concepts[](#concepts "Link to this heading")

* [AEL Interoperability](ael_interoperability.md)
  + [Calling AEL From Python](ael_interoperability.md#calling-ael-from-python)
  + [Calling Python From AEL](ael_interoperability.md#calling-python-from-ael)
* [AEL Type Conversions](ael_type_conversions.md)


---

## 5. concepts\ael_interoperability.md {#concepts--ael_interoperability}

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

## 6. concepts\ael_type_conversions.md {#concepts--ael_type_conversions}

# AEL Type Conversions[](#ael-type-conversions "Link to this heading")

| Python Type | AEL Type | Notes |
| --- | --- | --- |
| `bool` | `ee_bool` | AEL `TRUE` and `FALSE` are integer-typed values. |
| `int` | `int` |  |
| `float` | `double` |  |

Todo

Fill out the table of AEL type conversions


---

## 7. reference\index.md {#reference--index}

# Reference[](#reference "Link to this heading")

* [keysight.ads.ael](ael.md)
  + [AEL Bridge](ael.md#ael-bridge)
    - [`call`](ael.md#keysight.ads.ael.call)
    - [`decl`](ael.md#keysight.ads.ael.decl)
    - [`AELValue`](ael.md#keysight.ads.ael.AELValue)


---

## 8. reference\ael.md {#reference--ael}

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


---

## 9. examples\index.md {#examples--index}

# Examples[](#examples "Link to this heading")

Contents:

* [Calling Between AEL and Python](ex_calling_ael_and_python.md)
  + [Python Interface to AEL](ex_calling_ael_and_python.md#python-interface-to-ael)
  + [AEL Interface to Python](ex_calling_ael_and_python.md#ael-interface-to-python)


---

## 10. examples\ex_calling_ael_and_python.md {#examples--ex_calling_ael_and_python}

# Calling Between AEL and Python[](#calling-between-ael-and-python "Link to this heading")

## Python Interface to AEL[](#python-interface-to-ael "Link to this heading")

This python example demonstrates how to load an AEL file and execute a function defined inside.

```
# Copyright Keysight Technologies 2024 - 2024
# The methods in this example are separated into two sections:
# The first section demonstrates calling into AEL from Python.
# The second section contains functions that are called by AEL.
# See ex_calling_ael_and_python.ael for the AEL equivalent.

def loading_an_ael_file_and_calling_a_function() -> None:
    from keysight.ads import ael

    # Load the corresponding AEL file
    ael_filename = ael.hpeesof_path() + "/ael/python/examples/ex_calling_ael_and_python"
    # You can check if a function is defined using the AEL function is_function_defined()
    is_defined = ael.call.is_function_defined("concatenate_strings")
    assert not is_defined
    # Load the file
    ael.call.load(ael_filename)
    is_defined = ael.call.is_function_defined("concatenate_strings")
    assert is_defined
    # And call a function in the AEL file just loaded
    result = ael.call.concatenate_strings("Hello from ", "Keysight!")
    print(result)
    assert result == "Hello from Keysight!"
    # AEL functions can be loaded into specific vocabularies and accessed in Python by specifying the vocabulary
    # For example, if we decide to load the AEL file into the vocabulary of a loaded library, we can do:
    # ael.call.load(ael_filename, "my_library")
    # ael.call(vocab="my_library").concatenate_strings("Hello from ", "Keysight!")

# Called by AEL example
def function_called_by_ael_example(arg: int) -> int:
    return arg * 2

def function_called_when_this_file_is_loaded() -> None:
    print("Hello from Keysight!")

# Loaded by AEL example
function_called_when_this_file_is_loaded()
```

## AEL Interface to Python[](#ael-interface-to-python "Link to this heading")

This ael example demonstrates how to execute statements in Python from AEL.

```
// Copyright Keysight Technologies 2024 - 2024
// The methods in this example are separated into two sections:
// The first section demonstrates calling into Python from AEL.
// The second section contains functions that are called by Python.
// See ex_calling_ael_and_python.py for the Python equivalent.

defun python_exec_example()
{
    // The below AEL string is formatted to look like:
    //
    // def hello(name: str) -> str:
    //     from keysight.ads import ael
    //
    //     greeting = ael.call.strcat("hello ", name)
    //
    //     return greeting
    //
    // print(hello("Mr. Smith""))

    decl statement = strcat("def hello(name: str) -> str:\n",
                           "\tfrom keysight.ads import ael\n",
                           "\tgreeting = ael.call.strcat(\"hello \",name)\n",
                           "\treturn greeting\n\n",
                           "print(hello(\"Mr. Smith\"))\n");

    python_exec(statement);
}
// end python_exec_example()

defun python_exec_file_example()
{
    // Python statements in a file can be executed by calling python_exec_file
    decl example_path = strcat(getsysenv("HPEESOF_DIR"), "/ael/python/examples/");
    decl file = strcat(example_path, "ex_calling_ael_and_python.py");
    python_exec_file(file); // outputs `Hello from Keysight!`
}
// end python_exec_file_example()

defun importing_a_python_module_and_executing_a_function()
 {
    // Update the Python system path, if necessary, to load your module
    decl example_path = strcat(getsysenv("HPEESOF_DIR"), "/ael/python/examples/");
    decl path_append = strcat("import sys; sys.path.append(\"", example_path, "\");");
    python_exec(path_append);

    // You can import the module, call a function, and retrieve the result
    decl example_module = python_import_module("ex_calling_ael_and_python");
    decl example_function = python_get_attr(example_module, "function_called_by_ael_example");
    decl result = python_call(example_function, list(25));
    decl str_result = strcat("Result is ", result);
    return str_result;
}
// end importing_a_python_module_and_executing_a_function()

// Called by Python example
defun concatenate_strings(str1, str2)
{
    return strcat(str1, str2);
}
```


---

## 11. howto\index.md {#howto--index}

# How-To[](#how-to "Link to this heading")

* [How to Set Up a Python Virtual Environment](venv.md)
* [How to Use Pytest](pytest.md)


---

## 12. howto\venv.md {#howto--venv}

# How to Set Up a Python Virtual Environment[](#how-to-set-up-a-python-virtual-environment "Link to this heading")

It is possible to access AEL python functionality in a python virtual environment rather than the embedded ADS Python installation.

The venv must be created using the Python shipped with ADS, using the **--system-site-packages** flag so that the venv has access to the **keysight.ads.ael** Python API.

> For linux:
>
> ```
> $HPEESOF_DIR/tools/python/bin/python3 -m venv --system-site-packages $HOME/ads_venv
> ```
>
> For windows:
>
> ```
> %HPEESOF_DIR%\tools\python\python -m venv --system-site-packages %HOME%\ads_venv
> ```


---

## 13. howto\pytest.md {#howto--pytest}

# How to Use Pytest[](#how-to-use-pytest "Link to this heading")

Pytest is a mature full-featured testing tool for Python. It is useful when developing Python scripts.
Pytest is not installed in the ADS Python installation.

The recommended steps to use Pytest are:

> 1. Create a Python virtual environment. See [How to Set Up a Python Virtual Environment](venv.md).
> 2. Activate the Python virtual environment.
> 3. Install pytest into the virtual environment.
>
>    > ```
>    > pip install pytest
>    > ```
> 4. Run pytest on your test scripts.
>
>    > ```
>    > cd path/to/tests
>    > pytest
>    > ```
