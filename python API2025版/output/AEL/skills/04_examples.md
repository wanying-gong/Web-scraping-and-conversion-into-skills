# Examples
> **说明：** AEL 与 Python 互相调用的示例。

> **何时使用：** 当你需要参考可运行示例或调用模式时

---

## 本文件目录

- **Examples** (`examples/index.md`)
- **Calling Between AEL and Python** (`examples/ex_calling_ael_and_python.md`)

---

<!-- === 来源: examples/index.md === -->

# Examples[](#examples "Link to this heading")

Contents:

* [Calling Between AEL and Python](ex_calling_ael_and_python.md)
  + [Python Interface to AEL](ex_calling_ael_and_python.md#python-interface-to-ael)
  + [AEL Interface to Python](ex_calling_ael_and_python.md#ael-interface-to-python)


---

<!-- === 来源: examples/ex_calling_ael_and_python.md === -->

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

