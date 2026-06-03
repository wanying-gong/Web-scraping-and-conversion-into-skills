# Reference
> **说明：** keysight.ads.ael API 参考。

> **何时使用：** 当你需要查询 keysight.ads.ael 模块 API 时

---

## 本文件目录

- **Reference** (`reference/index.md`)
- **keysight.ads.ael** (`reference/ael.md`)

---

<!-- === 来源: reference/index.md === -->

# Reference[](#reference "Link to this heading")

* [keysight.ads.ael](ael.md)
  + [AEL Bridge](ael.md#ael-bridge)
    - [`call`](ael.md#keysight.ads.ael.call)
    - [`decl`](ael.md#keysight.ads.ael.decl)
    - [`AELValue`](ael.md#keysight.ads.ael.AELValue)


---

<!-- === 来源: reference/ael.md === -->

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

