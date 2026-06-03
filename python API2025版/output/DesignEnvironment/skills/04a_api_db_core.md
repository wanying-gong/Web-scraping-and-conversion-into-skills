# Database Core API: keysight.ads.de.db / db_dbu
> **说明：** 数据库核心 API：Parameter Forms（参数表单）、Parameters（参数）、Properties（属性）、Enums（枚举类型）、Transaction（事务）、GenPolyline（折线）、Model Definition（模型定义）、Callbacks（数据库回调）、DBU 单位系统概览。

> **何时使用：** 当你需要读写设计数据库元素、处理参数/属性/枚举/几何图形时

---

## 本文件目录

- **keysight.ads.de.db** (`pypde/docs/reference/de/db/index.md`)
- **Callbacks** (`pypde/docs/reference/de/db/callbacks.md`)
- **Enumerated Types** (`pypde/docs/reference/de/db/enums.md`)
- **Parameter Forms** (`pypde/docs/reference/de/db/forms.md`)
- **GenPolyline** (`pypde/docs/reference/de/db/genpolyline.md`)
- **Model Definition** (`pypde/docs/reference/de/db/model_def.md`)
- **Parameters** (`pypde/docs/reference/de/db/parameters.md`)
- **Properties** (`pypde/docs/reference/de/db/properties.md`)
- **Transaction** (`pypde/docs/reference/de/db/transaction.md`)
- **keysight.ads.de.db\_dbu** (`pypde/docs/reference/de/db_dbu/index.md`)

---

<!-- === 来源: pypde/docs/reference/de/db/index.md === -->

# keysight.ads.de.db[](#module-keysight.ads.de.db "Link to this heading")

Database module.

Contains classes that are independent of database units.
See also ..db\_uu and ..db\_dbu.

## Classes[](#classes "Link to this heading")

* [Callbacks](callbacks.md)
  + [Classes](callbacks.md#classes)
  + [Enumerated Types](callbacks.md#enumerated-types)
  + [Functions](callbacks.md#functions)
* [Enumerated Types](enums.md)
  + [`AttrType`](enums.md#keysight.ads.de.db.AttrType)
  + [`DesignAttrType`](enums.md#keysight.ads.de.db.DesignAttrType)
  + [`DesignMode`](enums.md#keysight.ads.de.db.DesignMode)
  + [`InstAttrType`](enums.md#keysight.ads.de.db.InstAttrType)
  + [`InstTermAttrType`](enums.md#keysight.ads.de.db.InstTermAttrType)
  + [`NetAttrType`](enums.md#keysight.ads.de.db.NetAttrType)
  + [`Orientation`](enums.md#keysight.ads.de.db.Orientation)
  + [`SignalType`](enums.md#keysight.ads.de.db.SignalType)
  + [`TermAttrType`](enums.md#keysight.ads.de.db.TermAttrType)
  + [`TermType`](enums.md#keysight.ads.de.db.TermType)
  + [`TextAlignment`](enums.md#keysight.ads.de.db.TextAlignment)
  + [`TextDisplayFormat`](enums.md#keysight.ads.de.db.TextDisplayFormat)
* [Parameter Forms](forms.md)
  + [Classes](forms.md#classes)
  + [Functions](forms.md#functions)
* [GenPolyline](genpolyline.md)
  + [Classes](genpolyline.md#classes)
  + [Enumerated Types](genpolyline.md#enumerated-types)
* [Model Definition](model_def.md)
  + [Classes](model_def.md#classes)
* [Parameters](parameters.md)
  + [Classes](parameters.md#classes)
  + [Enumerated Types](parameters.md#enumerated-types)
  + [Functions](parameters.md#functions)
* [Properties](properties.md)
  + [Classes](properties.md#classes)
  + [Enumerated Types](properties.md#enumerated-types)
* [Transaction](transaction.md)
  + [Classes](transaction.md#classes)
  + [Enumerated Types](transaction.md#enumerated-types)


---

<!-- === 来源: pypde/docs/reference/de/db/callbacks.md === -->

# Callbacks[](#callbacks "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.ModelCb[](#keysight.ads.de.db.ModelCb "Link to this definition")
:   Bases: [`ModelCbBase`](#keysight.ads.de.db.ModelCbBase "keysight.ads.de.db._callbacks.ModelCbBase")

    A model callback that is implemented in Python.

    \_\_init\_\_(*callback\_type: Literal[ModelCbType.PARAMETER\_DEFAULT\_VALUE]*, *callback: Callable[['ModelParam', 'ModelDefBase', 'Design'], 'ParamItem']*) → None[](#keysight.ads.de.db.ModelCb.__init__ "Link to this definition")

    \_\_init\_\_(*callback\_type: Literal[ModelCbType.PARAMETER\_MODIFIED]*, *callback: Callable[['ItemInfo'], bool]*) → None

    \_\_init\_\_(*callback\_type: Literal[ModelCbType.ITEM\_NETLIST]*, *callback: Callable[[[StandardInstance](#keysight.ads.de.db.StandardInstance "keysight.ads.de.db._callbacks.StandardInstance")], str]*) → None

    \_\_init\_\_(*callback\_type: Literal[ModelCbType.ITEM\_MODIFIED]*, *callback: Callable[['Instance'], None]*) → None
    :   Initialize a callback.

        callback\_typeModelCbType
        :   **ModelCbType.PARAMETER\_DEFAULT\_VALUE** :
            Override the default value set in [`ModelParam.default_value`](model_def.md#keysight.ads.de.db.ModelParam.default_value "keysight.ads.de.db.ModelParam.default_value").
            Return a [`ParamItem`](parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem")

            **ModelCbType.PARAMETER\_MODIFIED** :
            Called when a parameter has been modified.
            Return True if dependent parameter data had been modified.

            **ModelCbType.ITEM\_NETLIST** :
            Called when generating a netlist.
            Return the netlist string

            **ModelCbType.ITEM\_MODIFIED** :
            Called when this item has been modified.
            Return None

        callback : The user-supplied function to call

*class* keysight.ads.de.db.ModelCbAEL[](#keysight.ads.de.db.ModelCbAEL "Link to this definition")
:   Bases: [`ModelCbBase`](#keysight.ads.de.db.ModelCbBase "keysight.ads.de.db._callbacks.ModelCbBase")

    A model callback that is implemented in AEL.

    \_\_init\_\_(*callback\_type: [ModelCbType](#keysight.ads.de.db.ModelCbType "keysight.ads.de.db._callbacks.ModelCbType")*, *vocabulary: str*, *function: str*, *client\_data: object*, *enabled: bool = True*) → None[](#keysight.ads.de.db.ModelCbAEL.__init__ "Link to this definition")

    *property* function\_name*: str*[](#keysight.ads.de.db.ModelCbAEL.function_name "Link to this definition")

    get\_client\_data\_string(*format\_strings: bool*) → str[](#keysight.ads.de.db.ModelCbAEL.get_client_data_string "Link to this definition")

    *property* vocabulary*: str*[](#keysight.ads.de.db.ModelCbAEL.vocabulary "Link to this definition")

*class* keysight.ads.de.db.ModelCbBase[](#keysight.ads.de.db.ModelCbBase "Link to this definition")
:   Base class for callbacks used by model definitions and model parameters.

    See `de.db.ModelParam` and `de.db.ModelDef`.
    Each callback function can be implemented in Python or AEL.

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.ModelCbBase.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* enabled*: bool*[](#keysight.ads.de.db.ModelCbBase.enabled "Link to this definition")

    *property* type*: [ModelCbType](#keysight.ads.de.db.ModelCbType "keysight.ads.de.db._callbacks.ModelCbType")*[](#keysight.ads.de.db.ModelCbBase.type "Link to this definition")

*class* keysight.ads.de.db.NetlistInstance[](#keysight.ads.de.db.NetlistInstance "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.NetlistInstance.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* instance\_name*: str*[](#keysight.ads.de.db.NetlistInstance.instance_name "Link to this definition")

    *property* instance\_name\_for\_netlist*: str*[](#keysight.ads.de.db.NetlistInstance.instance_name_for_netlist "Link to this definition")

    *property* netlisted\_master\_name*: str*[](#keysight.ads.de.db.NetlistInstance.netlisted_master_name "Link to this definition")

    *property* nodes*: list[[NetlistNode](#keysight.ads.de.db.NetlistNode "keysight.ads.de.db._callbacks.NetlistNode")]*[](#keysight.ads.de.db.NetlistInstance.nodes "Link to this definition")

    *property* parent\_design*: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design") | None*[](#keysight.ads.de.db.NetlistInstance.parent_design "Link to this definition")

    *property* parent\_design\_name*: str*[](#keysight.ads.de.db.NetlistInstance.parent_design_name "Link to this definition")

*class* keysight.ads.de.db.NetlistNode[](#keysight.ads.de.db.NetlistNode "Link to this definition")
:   \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.NetlistNode.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* is\_grounded*: bool*[](#keysight.ads.de.db.NetlistNode.is_grounded "Link to this definition")

    *property* node\_name*: str*[](#keysight.ads.de.db.NetlistNode.node_name "Link to this definition")

    *property* pin\_name*: str*[](#keysight.ads.de.db.NetlistNode.pin_name "Link to this definition")

    *property* pin\_number*: int*[](#keysight.ads.de.db.NetlistNode.pin_number "Link to this definition")

*class* keysight.ads.de.db.StandardInstance[](#keysight.ads.de.db.StandardInstance "Link to this definition")
:   Bases: [`NetlistInstance`](#keysight.ads.de.db.NetlistInstance "keysight.ads.de.db._callbacks.NetlistInstance")

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.StandardInstance.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* instance*: [Instance](../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*[](#keysight.ads.de.db.StandardInstance.instance "Link to this definition")

    *property* model\_def*: [ModelDefBase](model_def.md#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db.ModelDefBase") | None*[](#keysight.ads.de.db.StandardInstance.model_def "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.db.ModelCbType[](#keysight.ads.de.db.ModelCbType "Link to this definition")
:   An enumeration specifying the purpose of a parameter callback.

    PARAMETER\_DEFAULT\_VALUE *= <ModelCbType.PARM\_DEFAULT\_VALUE\_CB: 0>*[](#keysight.ads.de.db.ModelCbType.PARAMETER_DEFAULT_VALUE "Link to this definition")
    :   This type of callback returns a design specific default parameter value.

    PARAMETER\_MODIFIED *= <ModelCbType.PARM\_MODIFIED\_CB: 1>*[](#keysight.ads.de.db.ModelCbType.PARAMETER_MODIFIED "Link to this definition")
    :   This type of callback is called whenever a specific parameter is modified.

    ITEM\_NETLIST *= <ModelCbType.ITEM\_NETLIST\_CB: 3>*[](#keysight.ads.de.db.ModelCbType.ITEM_NETLIST "Link to this definition")
    :   This type of callback returns a custom netlist string.

    ITEM\_MODIFIED *= <ModelCbType.ITEM\_MODIFIED\_CB: 8>*[](#keysight.ads.de.db.ModelCbType.ITEM_MODIFIED "Link to this definition")
    :   This type of callback is called whenever a specific item is modified.

## Functions[](#functions "Link to this heading")

keysight.ads.de.db.invoke\_parameter\_changed\_callback(*instance: [Instance](../db_uu/db_uu.md#keysight.ads.de.db_uu.Instance "keysight.ads.de.db_uu.Instance")*, *parameter\_names: Sequence[str]*) → None[](#keysight.ads.de.db.invoke_parameter_changed_callback "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/db/enums.md === -->

# Enumerated Types[](#enumerated-types "Link to this heading")

keysight.ads.de.db.AttrType[](#keysight.ads.de.db.AttrType "Link to this definition")
:   alias of `Union`[[`DesignAttrType`](#keysight.ads.de.db.DesignAttrType "keysight.ads.de.db._db_types.DesignAttrType"), [`InstAttrType`](#keysight.ads.de.db.InstAttrType "keysight.ads.de.db._db_types.InstAttrType"), [`InstTermAttrType`](#keysight.ads.de.db.InstTermAttrType "keysight.ads.de.db._db_types.InstTermAttrType"), [`NetAttrType`](#keysight.ads.de.db.NetAttrType "keysight.ads.de.db._db_types.NetAttrType"), [`TermAttrType`](#keysight.ads.de.db.TermAttrType "keysight.ads.de.db._db_types.TermAttrType")]

*class* keysight.ads.de.db.DesignAttrType[](#keysight.ads.de.db.DesignAttrType "Link to this definition")
:   LIB\_NAME *= <DesignAttrType.LIB\_NAME: 0>*[](#keysight.ads.de.db.DesignAttrType.LIB_NAME "Link to this definition")

    CELL\_NAME *= <DesignAttrType.CELL\_NAME: 1>*[](#keysight.ads.de.db.DesignAttrType.CELL_NAME "Link to this definition")

    VIEW\_NAME *= <DesignAttrType.VIEW\_NAME: 2>*[](#keysight.ads.de.db.DesignAttrType.VIEW_NAME "Link to this definition")

    CELL\_TYPE *= <DesignAttrType.CELL\_TYPE: 3>*[](#keysight.ads.de.db.DesignAttrType.CELL_TYPE "Link to this definition")

    LAST\_SAVED\_TIME *= <DesignAttrType.LAST\_SAVED\_TIME: 4>*[](#keysight.ads.de.db.DesignAttrType.LAST_SAVED_TIME "Link to this definition")

*class* keysight.ads.de.db.DesignMode[](#keysight.ads.de.db.DesignMode "Link to this definition")
:   READ\_ONLY *= <DesignMode.READ\_ONLY: 0>*[](#keysight.ads.de.db.DesignMode.READ_ONLY "Link to this definition")

    WRITE *= <DesignMode.WRITE: 1>*[](#keysight.ads.de.db.DesignMode.WRITE "Link to this definition")

    APPEND *= <DesignMode.APPEND: 2>*[](#keysight.ads.de.db.DesignMode.APPEND "Link to this definition")

*class* keysight.ads.de.db.InstAttrType[](#keysight.ads.de.db.InstAttrType "Link to this definition")
:   LIB\_NAME *= <InstAttrType.LIB\_NAME: 0>*[](#keysight.ads.de.db.InstAttrType.LIB_NAME "Link to this definition")

    CELL\_NAME *= <InstAttrType.CELL\_NAME: 1>*[](#keysight.ads.de.db.InstAttrType.CELL_NAME "Link to this definition")

    VIEW\_NAME *= <InstAttrType.VIEW\_NAME: 2>*[](#keysight.ads.de.db.InstAttrType.VIEW_NAME "Link to this definition")

    NAME *= <InstAttrType.NAME: 3>*[](#keysight.ads.de.db.InstAttrType.NAME "Link to this definition")

    NUM\_BITS *= <InstAttrType.NUM\_BITS: 4>*[](#keysight.ads.de.db.InstAttrType.NUM_BITS "Link to this definition")

    IS\_BOUND *= <InstAttrType.IS\_BOUND: 5>*[](#keysight.ads.de.db.InstAttrType.IS_BOUND "Link to this definition")

*class* keysight.ads.de.db.InstTermAttrType[](#keysight.ads.de.db.InstTermAttrType "Link to this definition")
:   NAME *= <InstTermAttrType.NAME: 0>*[](#keysight.ads.de.db.InstTermAttrType.NAME "Link to this definition")

*class* keysight.ads.de.db.NetAttrType[](#keysight.ads.de.db.NetAttrType "Link to this definition")
:   NAME *= <NetAttrType.NAME: 0>*[](#keysight.ads.de.db.NetAttrType.NAME "Link to this definition")

    SIG\_TYPE *= <NetAttrType.SIG\_TYPE: 1>*[](#keysight.ads.de.db.NetAttrType.SIG_TYPE "Link to this definition")

    IS\_GLOBAL *= <NetAttrType.IS\_GLOBAL: 2>*[](#keysight.ads.de.db.NetAttrType.IS_GLOBAL "Link to this definition")

    IS\_IMPLICIT *= <NetAttrType.IS\_IMPLICIT: 3>*[](#keysight.ads.de.db.NetAttrType.IS_IMPLICIT "Link to this definition")

    IS\_EMPTY *= <NetAttrType.IS\_EMPTY: 4>*[](#keysight.ads.de.db.NetAttrType.IS_EMPTY "Link to this definition")

    NUM\_BITS *= <NetAttrType.NUM\_BITS: 5>*[](#keysight.ads.de.db.NetAttrType.NUM_BITS "Link to this definition")

*class* keysight.ads.de.db.Orientation[](#keysight.ads.de.db.Orientation "Link to this definition")
:   R0 *= <OrientEnum.R0: 0>*[](#keysight.ads.de.db.Orientation.R0 "Link to this definition")

    R90 *= <OrientEnum.R90: 1>*[](#keysight.ads.de.db.Orientation.R90 "Link to this definition")

    R180 *= <OrientEnum.R180: 2>*[](#keysight.ads.de.db.Orientation.R180 "Link to this definition")

    R270 *= <OrientEnum.R270: 3>*[](#keysight.ads.de.db.Orientation.R270 "Link to this definition")

    MY *= <OrientEnum.MY: 4>*[](#keysight.ads.de.db.Orientation.MY "Link to this definition")

    MYR90 *= <OrientEnum.MYR90: 5>*[](#keysight.ads.de.db.Orientation.MYR90 "Link to this definition")

    MX *= <OrientEnum.MX: 6>*[](#keysight.ads.de.db.Orientation.MX "Link to this definition")

    MXR90 *= <OrientEnum.MXR90: 7>*[](#keysight.ads.de.db.Orientation.MXR90 "Link to this definition")

    *static* concat\_orientations(*first: [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*, *second: [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*) → [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")[](#keysight.ads.de.db.Orientation.concat_orientations "Link to this definition")

    *static* get\_relative\_orientation(*first: [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*, *second: [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")*) → [Orientation](#keysight.ads.de.db.Orientation "keysight.ads.de.db._db_types.Orientation")[](#keysight.ads.de.db.Orientation.get_relative_orientation "Link to this definition")

*class* keysight.ads.de.db.SignalType[](#keysight.ads.de.db.SignalType "Link to this definition")
:   SIGNAL *= <SignalType.SIGNAL: 0>*[](#keysight.ads.de.db.SignalType.SIGNAL "Link to this definition")

    POWER *= <SignalType.POWER: 1>*[](#keysight.ads.de.db.SignalType.POWER "Link to this definition")

    GROUND *= <SignalType.GROUND: 2>*[](#keysight.ads.de.db.SignalType.GROUND "Link to this definition")

    CLOCK *= <SignalType.CLOCK: 3>*[](#keysight.ads.de.db.SignalType.CLOCK "Link to this definition")

    TIE\_OFF *= <SignalType.TIE\_OFF: 4>*[](#keysight.ads.de.db.SignalType.TIE_OFF "Link to this definition")

    TIE\_HI *= <SignalType.TIE\_HI: 5>*[](#keysight.ads.de.db.SignalType.TIE_HI "Link to this definition")

    TIE\_LO *= <SignalType.TIE\_LO: 6>*[](#keysight.ads.de.db.SignalType.TIE_LO "Link to this definition")

    ANALOG *= <SignalType.ANALOG: 7>*[](#keysight.ads.de.db.SignalType.ANALOG "Link to this definition")

    SCAN *= <SignalType.SCAN: 8>*[](#keysight.ads.de.db.SignalType.SCAN "Link to this definition")

    RESET *= <SignalType.RESET: 9>*[](#keysight.ads.de.db.SignalType.RESET "Link to this definition")

*class* keysight.ads.de.db.TermAttrType[](#keysight.ads.de.db.TermAttrType "Link to this definition")
:   NAME *= <TermAttrType.NAME: 0>*[](#keysight.ads.de.db.TermAttrType.NAME "Link to this definition")

    HAS\_PINS *= <TermAttrType.HAS\_PINS: 1>*[](#keysight.ads.de.db.TermAttrType.HAS_PINS "Link to this definition")

    NUM\_BITS *= <TermAttrType.NUM\_BITS: 2>*[](#keysight.ads.de.db.TermAttrType.NUM_BITS "Link to this definition")

*class* keysight.ads.de.db.TermType[](#keysight.ads.de.db.TermType "Link to this definition")
:   INPUT *= <TermType.INPUT: 0>*[](#keysight.ads.de.db.TermType.INPUT "Link to this definition")

    OUTPUT *= <TermType.OUTPUT: 1>*[](#keysight.ads.de.db.TermType.OUTPUT "Link to this definition")

    INPUT\_OUTPUT *= <TermType.INPUT\_OUTPUT: 2>*[](#keysight.ads.de.db.TermType.INPUT_OUTPUT "Link to this definition")

    SWITCH *= <TermType.SWITCH: 3>*[](#keysight.ads.de.db.TermType.SWITCH "Link to this definition")

    JUMPER *= <TermType.JUMPER: 4>*[](#keysight.ads.de.db.TermType.JUMPER "Link to this definition")

    UNUSED *= <TermType.UNUSED: 5>*[](#keysight.ads.de.db.TermType.UNUSED "Link to this definition")

    TRISTATE *= <TermType.TRISTATE: 6>*[](#keysight.ads.de.db.TermType.TRISTATE "Link to this definition")

*class* keysight.ads.de.db.TextAlignment[](#keysight.ads.de.db.TextAlignment "Link to this definition")
:   UPPER\_LEFT *= <TextAlignment.UPPER\_LEFT: 0>*[](#keysight.ads.de.db.TextAlignment.UPPER_LEFT "Link to this definition")

    CENTER\_LEFT *= <TextAlignment.CENTER\_LEFT: 1>*[](#keysight.ads.de.db.TextAlignment.CENTER_LEFT "Link to this definition")

    LOWER\_LEFT *= <TextAlignment.LOWER\_LEFT: 2>*[](#keysight.ads.de.db.TextAlignment.LOWER_LEFT "Link to this definition")

    UPPER\_CENTER *= <TextAlignment.UPPER\_CENTER: 3>*[](#keysight.ads.de.db.TextAlignment.UPPER_CENTER "Link to this definition")

    CENTER\_CENTER *= <TextAlignment.CENTER\_CENTER: 4>*[](#keysight.ads.de.db.TextAlignment.CENTER_CENTER "Link to this definition")

    LOWER\_CENTER *= <TextAlignment.LOWER\_CENTER: 5>*[](#keysight.ads.de.db.TextAlignment.LOWER_CENTER "Link to this definition")

    UPPER\_RIGHT *= <TextAlignment.UPPER\_RIGHT: 6>*[](#keysight.ads.de.db.TextAlignment.UPPER_RIGHT "Link to this definition")

    CENTER\_RIGHT *= <TextAlignment.CENTER\_RIGHT: 7>*[](#keysight.ads.de.db.TextAlignment.CENTER_RIGHT "Link to this definition")

    LOWER\_RIGHT *= <TextAlignment.LOWER\_RIGHT: 8>*[](#keysight.ads.de.db.TextAlignment.LOWER_RIGHT "Link to this definition")

*class* keysight.ads.de.db.TextDisplayFormat[](#keysight.ads.de.db.TextDisplayFormat "Link to this definition")
:   NAME *= <TextDisplayFormat.NAME: 0>*[](#keysight.ads.de.db.TextDisplayFormat.NAME "Link to this definition")

    VALUE *= <TextDisplayFormat.VALUE: 1>*[](#keysight.ads.de.db.TextDisplayFormat.VALUE "Link to this definition")

    NAME\_VALUE *= <TextDisplayFormat.NAME\_VALUE: 2>*[](#keysight.ads.de.db.TextDisplayFormat.NAME_VALUE "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/db/forms.md === -->

# Parameter Forms[](#parameter-forms "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.CompoundForm[](#keysight.ads.de.db.CompoundForm "Link to this definition")
:   Bases: [`Form`](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")

    CompoundForm is a type of Form for a parameter that contains one or more sub-parameters.

    The CompoundForm describes how the parameter is netlisted and displayed.
    The Form for each sub-parameter describes how that portion of the parameter is netlisted and displayed.
    The number of sub-parameters is fixed by the parameter definition.

    \_\_init\_\_(*name: str*, *label: str = ''*, *params: Sequence[[ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")] = []*, *net\_format: str = ''*, *display\_format: str = ''*, *dialog\_data: str = ''*) → None[](#keysight.ads.de.db.CompoundForm.__init__ "Link to this definition")

    add\_parameter(*parameter: [ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")*) → None[](#keysight.ads.de.db.CompoundForm.add_parameter "Link to this definition")

    *property* parameters*: NamedListRefAbc[[ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")]*[](#keysight.ads.de.db.CompoundForm.parameters "Link to this definition")

*class* keysight.ads.de.db.ConstForm[](#keysight.ads.de.db.ConstForm "Link to this definition")
:   Bases: [`Form`](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")

    A Form representing a fixed value, such as “Yes” or 1.

    \_\_init\_\_(*name: str*, *label: str | None = None*, *net\_format: str | None = None*, *display\_format: str | None = None*, *dialog\_data: str = ''*) → None[](#keysight.ads.de.db.ConstForm.__init__ "Link to this definition")

*class* keysight.ads.de.db.Form[](#keysight.ads.de.db.Form "Link to this definition")
:   All parameter values are described by a Form that defines how the parameter is netlisted and displayed.

    A Form must appear in the Formset of a parameter definition in order to be usable by that parameter.
    See [`Formset`](#keysight.ads.de.db.Formset "keysight.ads.de.db.Formset") and class de.db.ModelParam.

    *property* dialog\_data*: str*[](#keysight.ads.de.db.Form.dialog_data "Link to this definition")
    :   A string used by edit dialogs for this form.

        If this string is empty, the name of the form will be used by default.

    *property* discrete*: bool*[](#keysight.ads.de.db.Form.discrete "Link to this definition")

    *property* display\_format*: str*[](#keysight.ads.de.db.Form.display_format "Link to this definition")
    :   The display format string for values using this form.

    *static* is\_compound\_form(*form: [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → TypeGuard[[CompoundForm](#keysight.ads.de.db.CompoundForm "keysight.ads.de.db._forms.CompoundForm")][](#keysight.ads.de.db.Form.is_compound_form "Link to this definition")

    *static* is\_constant\_form(*form: [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → TypeGuard[[ConstForm](#keysight.ads.de.db.ConstForm "keysight.ads.de.db._forms.ConstForm")][](#keysight.ads.de.db.Form.is_constant_form "Link to this definition")

    *static* is\_null\_form(*form: [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → TypeGuard[[NullForm](#keysight.ads.de.db.NullForm "keysight.ads.de.db._forms.NullForm")][](#keysight.ads.de.db.Form.is_null_form "Link to this definition")

    *static* is\_string\_form(*form: [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → TypeGuard[[StringForm](#keysight.ads.de.db.StringForm "keysight.ads.de.db._forms.StringForm")][](#keysight.ads.de.db.Form.is_string_form "Link to this definition")

    *property* label*: str*[](#keysight.ads.de.db.Form.label "Link to this definition")
    :   Short descriptive label of the Form.

    *property* name*: str*[](#keysight.ads.de.db.Form.name "Link to this definition")
    :   Unique name of the Form.

    *property* net\_format*: str*[](#keysight.ads.de.db.Form.net_format "Link to this definition")
    :   The netlist format string for values using this form.

*class* keysight.ads.de.db.Formset[](#keysight.ads.de.db.Formset "Link to this definition")
:   A Formset holds one or more Forms that define how a parameter is netlisted and displayed.

    \_\_init\_\_(*name: str*, *forms: Sequence[[Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")]*) → None[](#keysight.ads.de.db.Formset.__init__ "Link to this definition")

    contains(*name: str*) → bool[](#keysight.ads.de.db.Formset.contains "Link to this definition")
    :   contains is deprecated, and will be removed in the 2025 Update 2 release. Use Formset.forms.find(name) is not None.

    find\_constant\_form\_by\_label\_or\_display(*label\_or\_display: str*) → [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form") | None[](#keysight.ads.de.db.Formset.find_constant_form_by_label_or_display "Link to this definition")

    find\_form\_by\_label(*label: str*) → [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form") | None[](#keysight.ads.de.db.Formset.find_form_by_label "Link to this definition")

    find\_form\_by\_name(*name: str*) → [Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form") | None[](#keysight.ads.de.db.Formset.find_form_by_name "Link to this definition")

    *property* forms*: NamedListRefAbc[[Form](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")]*[](#keysight.ads.de.db.Formset.forms "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.Formset.name "Link to this definition")

*class* keysight.ads.de.db.NullForm[](#keysight.ads.de.db.NullForm "Link to this definition")
:   Bases: [`Form`](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")

    A Form representing a parameter with no value.

*class* keysight.ads.de.db.RepeatedForm[](#keysight.ads.de.db.RepeatedForm "Link to this definition")
:   Bases: [`Form`](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")

    RepeatedForm is the form used for a parameter that is repeatable.

    All repeatable parameters share the same RepeatedForm.

*class* keysight.ads.de.db.StringForm[](#keysight.ads.de.db.StringForm "Link to this definition")
:   Bases: [`Form`](#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")

    A Form representing a value stored in a string.

    \_\_init\_\_(*name: str*, *label: str | None = None*, *net\_format: str = '%v'*, *display\_format: str = '%v'*, *dialog\_data: str = ''*) → None[](#keysight.ads.de.db.StringForm.__init__ "Link to this definition")

*class* keysight.ads.de.db.StringFormWithAELCallbacks[](#keysight.ads.de.db.StringFormWithAELCallbacks "Link to this definition")
:   Bases: [`StringForm`](#keysight.ads.de.db.StringForm "keysight.ads.de.db._forms.StringForm")

*class* keysight.ads.de.db.StringFormWithCallbacks[](#keysight.ads.de.db.StringFormWithCallbacks "Link to this definition")
:   Bases: [`StringForm`](#keysight.ads.de.db.StringForm "keysight.ads.de.db._forms.StringForm")

    \_\_init\_\_(*name: str*, *label: str | None = None*, *net\_format: str = '%v'*, *display\_format: str = '%v'*, *dialog\_data: str = ''*, *option\_cb: Callable[[[Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")], list[str]] | None = None*, *valid\_cb: Callable[[str], bool] | None = None*, *data\_cb: Callable[[[ParamItem](parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem"), [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")], list[str]] | None = None*) → None[](#keysight.ads.de.db.StringFormWithCallbacks.__init__ "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.de.db.global\_model\_lib() → ModelLib[](#keysight.ads.de.db.global_model_lib "Link to this definition")

db.model\_lib *A collection of global forms and formsets.*[](#keysight.ads.de.db.model_lib "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/db/genpolyline.md === -->

# GenPolyline[](#genpolyline "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.CurveInfo[](#keysight.ads.de.db.CurveInfo "Link to this definition")
:   *property* start\_pt*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db.CurveInfo.start_pt "Link to this definition")

    *property* end\_pt*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db.CurveInfo.end_pt "Link to this definition")

    *property* center\_pt*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db.CurveInfo.center_pt "Link to this definition")

    *property* bulge*: float*[](#keysight.ads.de.db.CurveInfo.bulge "Link to this definition")

    *property* angle\_radians*: float*[](#keysight.ads.de.db.CurveInfo.angle_radians "Link to this definition")

    *property* start\_angle\_radians*: float*[](#keysight.ads.de.db.CurveInfo.start_angle_radians "Link to this definition")

    *property* angle\_degrees*: float*[](#keysight.ads.de.db.CurveInfo.angle_degrees "Link to this definition")

    *property* start\_angle\_degrees*: float*[](#keysight.ads.de.db.CurveInfo.start_angle_degrees "Link to this definition")

    *property* radius*: float*[](#keysight.ads.de.db.CurveInfo.radius "Link to this definition")

    *property* arc\_orientation*: [ArcOrientation](#keysight.ads.de.db.ArcOrientation "keysight.ads.de._pde.ArcOrientation")*[](#keysight.ads.de.db.CurveInfo.arc_orientation "Link to this definition")

    *property* is\_clockwise*: bool*[](#keysight.ads.de.db.CurveInfo.is_clockwise "Link to this definition")

    *property* is\_counter\_clockwise*: bool*[](#keysight.ads.de.db.CurveInfo.is_counter_clockwise "Link to this definition")

    *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db.CurveInfo.bbox "Link to this definition")

*class* keysight.ads.de.db.Edge[](#keysight.ads.de.db.Edge "Link to this definition")
:   A temporary object that represents the edge of an Outline.

    This edge should only be used as a temporary object. Any modifications
    to the Outline will invalidate the Edge object.

    *property* start\_pt*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db.Edge.start_pt "Link to this definition")

    *property* end\_pt*: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*[](#keysight.ads.de.db.Edge.end_pt "Link to this definition")

    *property* is\_arc*: bool*[](#keysight.ads.de.db.Edge.is_arc "Link to this definition")

    *property* curve\_info*: [CurveInfo](#keysight.ads.de.db.CurveInfo "keysight.ads.de.db._genpolyline.CurveInfo") | None*[](#keysight.ads.de.db.Edge.curve_info "Link to this definition")

*class* keysight.ads.de.db.GenPolygon[](#keysight.ads.de.db.GenPolygon "Link to this definition")
:   TPoint[](#keysight.ads.de.db.GenPolygon.TPoint "Link to this definition")
    :   alias of `Union`[[`PointF`](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF"), `tuple`[`float`, `float`], [`PointDBU`](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU"), `tuple`[`int`, `int`]]

    \_\_init\_\_(*points: Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float] | [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU") | tuple[int, int]] | None = None*, *outline: [Outline](#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline") | None = None*) → None[](#keysight.ads.de.db.GenPolygon.__init__ "Link to this definition")

    *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db.GenPolygon.bbox "Link to this definition")

    *property* empty*: bool*[](#keysight.ads.de.db.GenPolygon.empty "Link to this definition")

    *property* has\_arcs*: bool*[](#keysight.ads.de.db.GenPolygon.has_arcs "Link to this definition")

    *property* points*: list[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")]*[](#keysight.ads.de.db.GenPolygon.points "Link to this definition")

    *property* outline*: [Outline](#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline")*[](#keysight.ads.de.db.GenPolygon.outline "Link to this definition")

    box\_intersects\_or\_contains\_edge(*box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → bool[](#keysight.ads.de.db.GenPolygon.box_intersects_or_contains_edge "Link to this definition")

    overlaps(*box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → bool[](#keysight.ads.de.db.GenPolygon.overlaps "Link to this definition")

    contains(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → bool[](#keysight.ads.de.db.GenPolygon.contains "Link to this definition")

    add\_point(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → None[](#keysight.ads.de.db.GenPolygon.add_point "Link to this definition")

    set\_segment\_as\_arc(*index: int*, *point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*, *arc\_orientation: [ArcOrientation](#keysight.ads.de.db.ArcOrientation "keysight.ads.de._pde.ArcOrientation") | str*) → None[](#keysight.ads.de.db.GenPolygon.set_segment_as_arc "Link to this definition")

    set\_segment\_as\_arc\_bulge(*index: int*, *bulge: float*) → None[](#keysight.ads.de.db.GenPolygon.set_segment_as_arc_bulge "Link to this definition")

    remove\_arcs(*arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.GenPolygon.remove_arcs "Link to this definition")

    transform(*transformation: [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")*, *arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.GenPolygon.transform "Link to this definition")

*class* keysight.ads.de.db.GenPolygonWithHoles[](#keysight.ads.de.db.GenPolygonWithHoles "Link to this definition")
:   TPoint[](#keysight.ads.de.db.GenPolygonWithHoles.TPoint "Link to this definition")
    :   alias of `Union`[[`PointF`](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF"), `tuple`[`float`, `float`], [`PointDBU`](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU"), `tuple`[`int`, `int`]]

    \_\_init\_\_(*points: Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float] | [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU") | tuple[int, int]] | None = None*, *outer\_boundary: [GenPolygon](#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon") | None = None*, *inner\_boundaries: Sequence[[GenPolygon](#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon")] | None = None*) → None[](#keysight.ads.de.db.GenPolygonWithHoles.__init__ "Link to this definition")

    *property* outer\_boundary*: [GenPolygon](#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon")*[](#keysight.ads.de.db.GenPolygonWithHoles.outer_boundary "Link to this definition")

    *property* inner\_boundaries*: list[[GenPolygon](#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon")]*[](#keysight.ads.de.db.GenPolygonWithHoles.inner_boundaries "Link to this definition")
    :   A copy of the collection of holes in this polygon.

        inner\_boundaries is deprecated, and will be removed in the 2026 release. Use: GenPolygonWithHoles.holes.

    *property* holes*: ReadableListRefAbc[[GenPolygon](#keysight.ads.de.db.GenPolygon "keysight.ads.de.db._genpolyline.GenPolygon")]*[](#keysight.ads.de.db.GenPolygonWithHoles.holes "Link to this definition")
    :   The collection of holes in this polygon.

    *property* num\_holes*: int*[](#keysight.ads.de.db.GenPolygonWithHoles.num_holes "Link to this definition")

    *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db.GenPolygonWithHoles.bbox "Link to this definition")

    *property* empty*: bool*[](#keysight.ads.de.db.GenPolygonWithHoles.empty "Link to this definition")

    *property* has\_arcs*: bool*[](#keysight.ads.de.db.GenPolygonWithHoles.has_arcs "Link to this definition")

    contains(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → bool[](#keysight.ads.de.db.GenPolygonWithHoles.contains "Link to this definition")

    box\_intersects\_or\_contains\_edge(*box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → bool[](#keysight.ads.de.db.GenPolygonWithHoles.box_intersects_or_contains_edge "Link to this definition")

    overlaps\_box(*box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*) → bool[](#keysight.ads.de.db.GenPolygonWithHoles.overlaps_box "Link to this definition")

    overlaps\_polygon(*is\_closed: bool*, *other: [GenPolygonWithHoles](#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")*, *other\_is\_closed: bool*) → bool[](#keysight.ads.de.db.GenPolygonWithHoles.overlaps_polygon "Link to this definition")

    self\_intersects(*arc\_resolution\_degrees: float*) → bool[](#keysight.ads.de.db.GenPolygonWithHoles.self_intersects "Link to this definition")

    remove\_arcs(*arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.GenPolygonWithHoles.remove_arcs "Link to this definition")

    transform(*transformation: [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")*, *arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.GenPolygonWithHoles.transform "Link to this definition")

    convert\_vertices\_to\_arcs(*radius: float*, *arc\_resolution\_degrees: float = 5.0*, *minimum\_vertex\_distance: float = 0.0*) → list[[GenPolygonWithHoles](#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")][](#keysight.ads.de.db.GenPolygonWithHoles.convert_vertices_to_arcs "Link to this definition")

    oversize(*oversize\_amount: float*, *miter\_angle\_degrees: float = 0.0*, *minimum\_vertex\_distance: float = 0.0*) → list[[GenPolygonWithHoles](#keysight.ads.de.db.GenPolygonWithHoles "keysight.ads.de.db._genpolyline.GenPolygonWithHoles")][](#keysight.ads.de.db.GenPolygonWithHoles.oversize "Link to this definition")

*class* keysight.ads.de.db.GenPolyline[](#keysight.ads.de.db.GenPolyline "Link to this definition")
:   TPoint[](#keysight.ads.de.db.GenPolyline.TPoint "Link to this definition")
    :   alias of `Union`[[`PointF`](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF"), `tuple`[`float`, `float`], [`PointDBU`](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU"), `tuple`[`int`, `int`]]

    \_\_init\_\_(*points: ~collections.abc.Sequence[~keysight.ads.de.\_points.PointF | tuple[float*, *float] | ~keysight.ads.de.\_points.PointDBU | tuple[int*, *int]] | None = None*, *width: float = 0.0*, *bend\_style: ~keysight.ads.de.\_pde.BendStyle | str = <BendStyle.SQUARE: 0>*, *cap\_style: ~keysight.ads.de.\_pde.CapStyle | str = <CapStyle.ROUND: 1>*, *miter\_radius: float = 0.0*) → None[](#keysight.ads.de.db.GenPolyline.__init__ "Link to this definition")

    copy() → [GenPolyline](#keysight.ads.de.db.GenPolyline "keysight.ads.de.db._genpolyline.GenPolyline")[](#keysight.ads.de.db.GenPolyline.copy "Link to this definition")
    :   Return a copy of this object.

    *property* points*: list[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")]*[](#keysight.ads.de.db.GenPolyline.points "Link to this definition")

    *property* outline*: [Outline](#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline")*[](#keysight.ads.de.db.GenPolyline.outline "Link to this definition")

    *property* width*: float*[](#keysight.ads.de.db.GenPolyline.width "Link to this definition")

    *property* bend\_style*: [BendStyle](#keysight.ads.de.db.BendStyle "keysight.ads.de._pde.BendStyle")*[](#keysight.ads.de.db.GenPolyline.bend_style "Link to this definition")

    *property* cap\_style*: [CapStyle](#keysight.ads.de.db.CapStyle "keysight.ads.de._pde.CapStyle")*[](#keysight.ads.de.db.GenPolyline.cap_style "Link to this definition")

    *property* miter\_radius*: float*[](#keysight.ads.de.db.GenPolyline.miter_radius "Link to this definition")

    *property* teardrop\_info*: [TeardropLineInfo](#keysight.ads.de.db.TeardropLineInfo "keysight.ads.de.db._teardrop.TeardropLineInfo")*[](#keysight.ads.de.db.GenPolyline.teardrop_info "Link to this definition")

    *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db.GenPolyline.bbox "Link to this definition")

    *property* empty*: bool*[](#keysight.ads.de.db.GenPolyline.empty "Link to this definition")

    *property* has\_arcs*: bool*[](#keysight.ads.de.db.GenPolyline.has_arcs "Link to this definition")

    add\_point(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → None[](#keysight.ads.de.db.GenPolyline.add_point "Link to this definition")

    set\_segment\_as\_arc(*index: int*, *point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*, *arc\_orientation: [ArcOrientation](#keysight.ads.de.db.ArcOrientation "keysight.ads.de._pde.ArcOrientation") | str*) → None[](#keysight.ads.de.db.GenPolyline.set_segment_as_arc "Link to this definition")

    set\_segment\_as\_arc\_bulge(*index: int*, *bulge: float*) → None[](#keysight.ads.de.db.GenPolyline.set_segment_as_arc_bulge "Link to this definition")

    transform(*transformation: [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")*) → None[](#keysight.ads.de.db.GenPolyline.transform "Link to this definition")

*class* keysight.ads.de.db.MatrixForTransform[](#keysight.ads.de.db.MatrixForTransform "Link to this definition")
:   \_\_init\_\_() → None[](#keysight.ads.de.db.MatrixForTransform.__init__ "Link to this definition")

    translate(*dx: float*, *dy: float*) → None[](#keysight.ads.de.db.MatrixForTransform.translate "Link to this definition")

    rotate\_degrees(*degrees: float*) → None[](#keysight.ads.de.db.MatrixForTransform.rotate_degrees "Link to this definition")

    scale(*dx: float*, *dy: float*) → None[](#keysight.ads.de.db.MatrixForTransform.scale "Link to this definition")

    invert() → None[](#keysight.ads.de.db.MatrixForTransform.invert "Link to this definition")

    *property* dx*: float*[](#keysight.ads.de.db.MatrixForTransform.dx "Link to this definition")

    *property* dy*: float*[](#keysight.ads.de.db.MatrixForTransform.dy "Link to this definition")

    *property* m11*: float*[](#keysight.ads.de.db.MatrixForTransform.m11 "Link to this definition")

    *property* m12*: float*[](#keysight.ads.de.db.MatrixForTransform.m12 "Link to this definition")

    *property* m21*: float*[](#keysight.ads.de.db.MatrixForTransform.m21 "Link to this definition")

    *property* m22*: float*[](#keysight.ads.de.db.MatrixForTransform.m22 "Link to this definition")

*class* keysight.ads.de.db.Outline[](#keysight.ads.de.db.Outline "Link to this definition")
:   Represents a polyline composed of line and/or arc segments.

    It may represent either an open or closed shape.
    GenPolyline uses an Outline to represent an open shape.
    GenPolygonF and GenPolygonF\_with\_holes use an Outline to represent a closed shape.
    The points (vertices) and bulges control the shape of the outline.
    The edges are temporary objects that get invalidated whenever the Outline is modified.

    TPoint[](#keysight.ads.de.db.Outline.TPoint "Link to this definition")
    :   alias of `Union`[[`PointF`](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF"), `tuple`[`float`, `float`], [`PointDBU`](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU"), `tuple`[`int`, `int`]]

    \_\_init\_\_(*points: Sequence[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | tuple[float, float] | [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU") | tuple[int, int]] | None = None*, *bulges: Sequence[float] | None = None*) → None[](#keysight.ads.de.db.Outline.__init__ "Link to this definition")

    *property* points*: [IndexedMutableCollectionAbc](../collections.md#keysight.ads.de._list_like.IndexedMutableCollectionAbc "keysight.ads.de._list_like.IndexedMutableCollectionAbc")[[PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")]*[](#keysight.ads.de.db.Outline.points "Link to this definition")
    :   The collection of vertices for this outline.

    *property* edges*: IndexedReadableCollectionAbc[[Edge](#keysight.ads.de.db.Edge "keysight.ads.de.db._genpolyline.Edge")]*[](#keysight.ads.de.db.Outline.edges "Link to this definition")
    :   The collection of edges for this outline. The edges are only for short term use.

    *property* bbox*: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*[](#keysight.ads.de.db.Outline.bbox "Link to this definition")

    *property* empty*: bool*[](#keysight.ads.de.db.Outline.empty "Link to this definition")
    :   True if the outline has no points.

    *property* has\_arcs*: bool*[](#keysight.ads.de.db.Outline.has_arcs "Link to this definition")
    :   True if none of the edges are arcs.

    box\_intersects\_or\_contains\_edge(*box: [BoxF](../points.md#keysight.ads.de.BoxF "keysight.ads.de._points.BoxF")*, *is\_closed: bool*) → bool[](#keysight.ads.de.db.Outline.box_intersects_or_contains_edge "Link to this definition")

    edges\_intersect(*is\_closed: bool*, *other: [Outline](#keysight.ads.de.db.Outline "keysight.ads.de.db._genpolyline.Outline")*, *other\_is\_closed: bool*) → bool[](#keysight.ads.de.db.Outline.edges_intersect "Link to this definition")

    contains(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → bool[](#keysight.ads.de.db.Outline.contains "Link to this definition")

    contains\_and\_not\_on\_edge(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → bool[](#keysight.ads.de.db.Outline.contains_and_not_on_edge "Link to this definition")

    add\_point(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → None[](#keysight.ads.de.db.Outline.add_point "Link to this definition")

    insert\_point(*index: int*, *point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → None[](#keysight.ads.de.db.Outline.insert_point "Link to this definition")

    delete\_point(*index: int*) → None[](#keysight.ads.de.db.Outline.delete_point "Link to this definition")

    set\_point(*index: int*, *point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → None[](#keysight.ads.de.db.Outline.set_point "Link to this definition")

    set\_segment\_as\_arc(*index: int*, *point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*, *arc\_orientation: [ArcOrientation](#keysight.ads.de.db.ArcOrientation "keysight.ads.de._pde.ArcOrientation") | str*) → None[](#keysight.ads.de.db.Outline.set_segment_as_arc "Link to this definition")

    set\_segment\_as\_arc\_bulge(*index: int*, *bulge: float*) → None[](#keysight.ads.de.db.Outline.set_segment_as_arc_bulge "Link to this definition")

    remove\_arcs(*arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.Outline.remove_arcs "Link to this definition")

    transform(*transform: [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")*, *arc\_resolution\_degrees: float*) → None[](#keysight.ads.de.db.Outline.transform "Link to this definition")

    curve\_info(*index: int*) → [CurveInfo](#keysight.ads.de.db.CurveInfo "keysight.ads.de.db._genpolyline.CurveInfo") | None[](#keysight.ads.de.db.Outline.curve_info "Link to this definition")

*class* keysight.ads.de.db.TeardropDefinition[](#keysight.ads.de.db.TeardropDefinition "Link to this definition")
:   \_\_init\_\_(*width: [TeardropDefinitionWidth](#keysight.ads.de.db.TeardropDefinitionWidth "keysight.ads.de.db._teardrop.TeardropDefinitionWidth") | None = None*, *\**, *height: [TeardropDefinitionHeight](#keysight.ads.de.db.TeardropDefinitionHeight "keysight.ads.de.db._teardrop.TeardropDefinitionHeight") | None = None*, *angle: [TeardropDefinitionAngle](#keysight.ads.de.db.TeardropDefinitionAngle "keysight.ads.de.db._teardrop.TeardropDefinitionAngle") | None = None*) → None[](#keysight.ads.de.db.TeardropDefinition.__init__ "Link to this definition")

    *property* style*: [TeardropDefinitionStyle](#keysight.ads.de.db.TeardropDefinitionStyle "keysight.ads.de._pde.TeardropDefinitionStyle")*[](#keysight.ads.de.db.TeardropDefinition.style "Link to this definition")

    *property* width*: [TeardropDefinitionWidth](#keysight.ads.de.db.TeardropDefinitionWidth "keysight.ads.de.db._teardrop.TeardropDefinitionWidth") | None*[](#keysight.ads.de.db.TeardropDefinition.width "Link to this definition")

    *property* height*: [TeardropDefinitionHeight](#keysight.ads.de.db.TeardropDefinitionHeight "keysight.ads.de.db._teardrop.TeardropDefinitionHeight") | None*[](#keysight.ads.de.db.TeardropDefinition.height "Link to this definition")

    *property* angle*: [TeardropDefinitionAngle](#keysight.ads.de.db.TeardropDefinitionAngle "keysight.ads.de.db._teardrop.TeardropDefinitionAngle") | None*[](#keysight.ads.de.db.TeardropDefinition.angle "Link to this definition")

*class* keysight.ads.de.db.TeardropDefinitionAngle[](#keysight.ads.de.db.TeardropDefinitionAngle "Link to this definition")
:   Bases: `object`

*class* keysight.ads.de.db.TeardropDefinitionHeight[](#keysight.ads.de.db.TeardropDefinitionHeight "Link to this definition")
:   Bases: `object`

*class* keysight.ads.de.db.TeardropDefinitionWidth[](#keysight.ads.de.db.TeardropDefinitionWidth "Link to this definition")
:   Bases: `object`

*class* keysight.ads.de.db.TeardropLineInfo[](#keysight.ads.de.db.TeardropLineInfo "Link to this definition")
:   Bases: `object`

*class* keysight.ads.de.db.TeardropTouching[](#keysight.ads.de.db.TeardropTouching "Link to this definition")
:   Bases: `object`

    *property* was\_set\_manually*: bool*[](#keysight.ads.de.db.TeardropTouching.was_set_manually "Link to this definition")
    :   For testing.

    copy() → [TeardropTouching](#keysight.ads.de.db.TeardropTouching "keysight.ads.de.db._teardrop.TeardropTouching")[](#keysight.ads.de.db.TeardropTouching.copy "Link to this definition")
    :   Return a copy of this object.

*class* keysight.ads.de.db.Transform[](#keysight.ads.de.db.Transform "Link to this definition")
:   \_\_init\_\_() → None[](#keysight.ads.de.db.Transform.__init__ "Link to this definition")

    *property* matrix*: [MatrixForTransform](#keysight.ads.de.db.MatrixForTransform "keysight.ads.de.db._genpolyline.MatrixForTransform")*[](#keysight.ads.de.db.Transform.matrix "Link to this definition")

    *property* preserves\_aspect\_ratio*: bool*[](#keysight.ads.de.db.Transform.preserves_aspect_ratio "Link to this definition")

    *property* preserves\_mirroring*: bool*[](#keysight.ads.de.db.Transform.preserves_mirroring "Link to this definition")

    *property* is\_orthogonal*: bool*[](#keysight.ads.de.db.Transform.is_orthogonal "Link to this definition")

    *property* mirrored\_in\_x*: bool*[](#keysight.ads.de.db.Transform.mirrored_in_x "Link to this definition")

    *property* mirrored\_in\_y*: bool*[](#keysight.ads.de.db.Transform.mirrored_in_y "Link to this definition")

    scale(*dx: float*, *dy: float*) → None[](#keysight.ads.de.db.Transform.scale "Link to this definition")

    mirror\_x(*mirror: bool = True*) → None[](#keysight.ads.de.db.Transform.mirror_x "Link to this definition")

    mirror\_y(*mirror: bool = True*) → None[](#keysight.ads.de.db.Transform.mirror_y "Link to this definition")

    clear() → None[](#keysight.ads.de.db.Transform.clear "Link to this definition")

    translate(*point: tuple[float, float] | [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF") | None = None*, *\**, *dx: float | None = None*, *dy: float | None = None*) → None[](#keysight.ads.de.db.Transform.translate "Link to this definition")

    rotate\_radians(*radians: float*) → None[](#keysight.ads.de.db.Transform.rotate_radians "Link to this definition")

    rotate\_degrees(*degrees: float*) → None[](#keysight.ads.de.db.Transform.rotate_degrees "Link to this definition")

    reverse() → None[](#keysight.ads.de.db.Transform.reverse "Link to this definition")

    multiply\_transform(*other: [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")*) → [Transform](#keysight.ads.de.db.Transform "keysight.ads.de.db._genpolyline.Transform")[](#keysight.ads.de.db.Transform.multiply_transform "Link to this definition")

    transform\_user\_point(*point: [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")*) → [PointF](../points.md#keysight.ads.de.PointF "keysight.ads.de._points.PointF")[](#keysight.ads.de.db.Transform.transform_user_point "Link to this definition")

    transform\_point(*point: tuple[float, float]*) → tuple[float, float][](#keysight.ads.de.db.Transform.transform_point "Link to this definition")

    transform\_distance(*distance: float*) → float[](#keysight.ads.de.db.Transform.transform_distance "Link to this definition")

    transform\_angle\_radians(*radians: float*) → float[](#keysight.ads.de.db.Transform.transform_angle_radians "Link to this definition")

    transform\_angle\_degrees(*degrees: float*) → float[](#keysight.ads.de.db.Transform.transform_angle_degrees "Link to this definition")

    get\_transform\_angle() → int[](#keysight.ads.de.db.Transform.get_transform_angle "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.db.ArcOrientation[](#keysight.ads.de.db.ArcOrientation "Link to this definition")
:   Defines the orientation of an arc or sequence of points.

    Members:

    > CLOCKWISE : ‘Clockwise’: The orientation is clockwise.
    >
    > ZERO : ‘Zero’: The orientation is unspecified or we don’t care.
    >
    > COUNTER\_CLOCKWISE : ‘CounterClockwise’: The orientation is counter-clockwise.

    CLOCKWISE *= <ArcOrientation.CLOCKWISE: -1>*[](#keysight.ads.de.db.ArcOrientation.CLOCKWISE "Link to this definition")

    COUNTER\_CLOCKWISE *= <ArcOrientation.COUNTER\_CLOCKWISE: 1>*[](#keysight.ads.de.db.ArcOrientation.COUNTER_CLOCKWISE "Link to this definition")

    ZERO *= <ArcOrientation.ZERO: 0>*[](#keysight.ads.de.db.ArcOrientation.ZERO "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.ArcOrientation](#keysight.ads.de.db.ArcOrientation "keysight.ads.de._pde.ArcOrientation")*, *value: int*) → None[](#keysight.ads.de.db.ArcOrientation.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.ArcOrientation.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.ArcOrientation.name "Link to this definition")

    *property* str[](#keysight.ads.de.db.ArcOrientation.str "Link to this definition")
    :   Return the string representation of the orientation.

    *property* value[](#keysight.ads.de.db.ArcOrientation.value "Link to this definition")

*class* keysight.ads.de.db.BendStyle[](#keysight.ads.de.db.BendStyle "Link to this definition")
:   Defines the style of a bend in a polyline or polygon.

    Members:

    > SQUARE : ‘Square’: The bend has square corners.
    >
    > CURVED : ‘Curved’: The bend has curved corners with a specified radius.
    >
    > MITERED : ‘Mitered’: The bend has mitered corners - prefer AdaptiveMitered.
    >
    > NEW\_MITERED : ‘AdaptiveMitered’: Deprecated alias for ADAPTIVE\_MITERED.
    >
    > ADAPTIVE\_MITERED : ‘AdaptiveMitered’: The bend has mitered corners with consistent cut length.
    >
    > ROUNDED : ‘Rounded’: The bend has rounded corners.
    >
    > EXACT\_MITERED : ‘ExactMitered’: The bend has miter specified exactly - for internal use only.

    ADAPTIVE\_MITERED *= <BendStyle.NEW\_MITERED: 3>*[](#keysight.ads.de.db.BendStyle.ADAPTIVE_MITERED "Link to this definition")

    CURVED *= <BendStyle.CURVED: 1>*[](#keysight.ads.de.db.BendStyle.CURVED "Link to this definition")

    EXACT\_MITERED *= <BendStyle.EXACT\_MITERED: 5>*[](#keysight.ads.de.db.BendStyle.EXACT_MITERED "Link to this definition")

    MITERED *= <BendStyle.MITERED: 2>*[](#keysight.ads.de.db.BendStyle.MITERED "Link to this definition")

    NEW\_MITERED *= <BendStyle.NEW\_MITERED: 3>*[](#keysight.ads.de.db.BendStyle.NEW_MITERED "Link to this definition")

    ROUNDED *= <BendStyle.ROUNDED: 4>*[](#keysight.ads.de.db.BendStyle.ROUNDED "Link to this definition")

    SQUARE *= <BendStyle.SQUARE: 0>*[](#keysight.ads.de.db.BendStyle.SQUARE "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.BendStyle](#keysight.ads.de.db.BendStyle "keysight.ads.de._pde.BendStyle")*, *value: int*) → None[](#keysight.ads.de.db.BendStyle.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.BendStyle.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.BendStyle.name "Link to this definition")

    *property* str[](#keysight.ads.de.db.BendStyle.str "Link to this definition")
    :   Return the string representation of the bend style.

    *property* value[](#keysight.ads.de.db.BendStyle.value "Link to this definition")

*class* keysight.ads.de.db.CapStyle[](#keysight.ads.de.db.CapStyle "Link to this definition")
:   Defines the style of polyline end caps.

    Members:

    > SQUARE : ‘Square’: The end cap is square.
    >
    > ROUND : ‘Round’: The end cap is round.
    >
    > SQUARE\_EXTENDED : ‘SquareExtended’: The end cap is square and extended by half the width.
    >
    > CHAMFER : ‘Chamfer’: The end cap is chamfered.

    CHAMFER *= <CapStyle.CHAMFER: 3>*[](#keysight.ads.de.db.CapStyle.CHAMFER "Link to this definition")

    ROUND *= <CapStyle.ROUND: 1>*[](#keysight.ads.de.db.CapStyle.ROUND "Link to this definition")

    SQUARE *= <CapStyle.SQUARE: 0>*[](#keysight.ads.de.db.CapStyle.SQUARE "Link to this definition")

    SQUARE\_EXTENDED *= <CapStyle.SQUARE\_EXTENDED: 2>*[](#keysight.ads.de.db.CapStyle.SQUARE_EXTENDED "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.CapStyle](#keysight.ads.de.db.CapStyle "keysight.ads.de._pde.CapStyle")*, *value: int*) → None[](#keysight.ads.de.db.CapStyle.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.CapStyle.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.CapStyle.name "Link to this definition")

    *property* str[](#keysight.ads.de.db.CapStyle.str "Link to this definition")
    :   Return the string representation of the end cap style.

    *property* value[](#keysight.ads.de.db.CapStyle.value "Link to this definition")

keysight.ads.de.db.LineInfoEnd[](#keysight.ads.de.db.LineInfoEnd "Link to this definition")
:   alias of `End`

*class* keysight.ads.de.db.TeardropDefinitionStyle[](#keysight.ads.de.db.TeardropDefinitionStyle "Link to this definition")
:   Bases: `pybind11_object`

    Members:

    NONE

    WIDTH\_AND\_HEIGHT

    WIDTH\_TANGENT

    TEARDROP\_ANGLE

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.TeardropDefinitionStyle](#keysight.ads.de.db.TeardropDefinitionStyle "keysight.ads.de._pde.TeardropDefinitionStyle")*, *value: int*) → None[](#keysight.ads.de.db.TeardropDefinitionStyle.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.TeardropDefinitionStyle.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.TeardropDefinitionStyle.name "Link to this definition")

*class* keysight.ads.de.db.TeardropValueUnits[](#keysight.ads.de.db.TeardropValueUnits "Link to this definition")
:   Bases: `pybind11_object`

    Determines how a teardrop value is specified (ratio or absolute value).

    Members:

    > VALUE : ‘Value’: The value is specified as an absolute value.
    >
    > DB\_UNITS : ‘Value’: Deprecated alias for VALUE.
    >
    > RATIO : ‘Ratio’: The value is specified as a ratio.

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.TeardropValueUnits](#keysight.ads.de.db.TeardropValueUnits "keysight.ads.de._pde.TeardropValueUnits")*, *value: int*) → None[](#keysight.ads.de.db.TeardropValueUnits.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.TeardropValueUnits.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.TeardropValueUnits.name "Link to this definition")

    *property* str[](#keysight.ads.de.db.TeardropValueUnits.str "Link to this definition")
    :   Return the string representation of the TeardropValueUnits.

*class* keysight.ads.de.db.TouchType[](#keysight.ads.de.db.TouchType "Link to this definition")
:   Members:

    NONE

    CIRCLE

    CIRCLE *= <TouchType.CIRCLE: 1>*[](#keysight.ads.de.db.TouchType.CIRCLE "Link to this definition")

    NONE *= <TouchType.NONE: 0>*[](#keysight.ads.de.db.TouchType.NONE "Link to this definition")

    \_\_init\_\_(*self: [keysight.ads.de.\_pde.TouchType](#keysight.ads.de.db.TouchType "keysight.ads.de._pde.TouchType")*, *value: int*) → None[](#keysight.ads.de.db.TouchType.__init__ "Link to this definition")

    \_\_new\_\_(*\*\*kwargs*)[](#keysight.ads.de.db.TouchType.__new__ "Link to this definition")

    *property* name[](#keysight.ads.de.db.TouchType.name "Link to this definition")

    *property* value[](#keysight.ads.de.db.TouchType.value "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/db/model_def.md === -->

# Model Definition[](#model-definition "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.ModelDef[](#keysight.ads.de.db.ModelDef "Link to this definition")
:   A model definition implemented in Python.

    \_\_init\_\_(*name: str*, *label: str*) → None[](#keysight.ads.de.db.ModelDef.__init__ "Link to this definition")
    :   Construct a ModelDef.

        Parameters:
        :   * **name** (*str*) – The name of the item, for a cell definition, this is the cell name
            * **label** (*str*) – Display label, e.g. “Resistor”

*class* keysight.ads.de.db.ModelDefAEL[](#keysight.ads.de.db.ModelDefAEL "Link to this definition")
:   A model definition implemented in AEL.

*class* keysight.ads.de.db.ModelDefBase[](#keysight.ads.de.db.ModelDefBase "Link to this definition")
:   A model definition, sometimes referred to as an item definition or component definition, contains the parameter definitions for a particular component or design.

    append\_parameter(*parameter: [ModelParam](#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")*) → None[](#keysight.ads.de.db.ModelDefBase.append_parameter "Link to this definition")
    :   append\_parameter is deprecated, and will be removed in the 2025 Update 2 release. Use: parameters.append(name)

    *property* callbacks*: ListRefAbc[[ModelCbBase](callbacks.md#keysight.ads.de.db.ModelCbBase "keysight.ads.de.db._callbacks.ModelCbBase")]*[](#keysight.ads.de.db.ModelDefBase.callbacks "Link to this definition")
    :   Return the collection of callbacks in this model definition.

    *property* component\_name*: str*[](#keysight.ads.de.db.ModelDefBase.component_name "Link to this definition")

    delete\_parameter(*index: int*) → None[](#keysight.ads.de.db.ModelDefBase.delete_parameter "Link to this definition")
    :   delete\_parameter is deprecated, and will be removed in the 2025 Update 2 release. Use: del(parameters[index])

    *static* find\_model\_def(*libOrCell: [Library](../library.md#keysight.ads.de.Library "keysight.ads.de._core.library.Library")*, *cellName: str*) → [ModelDefBase](#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db._model_def.ModelDefBase") | None[](#keysight.ads.de.db.ModelDefBase.find_model_def "Link to this definition")

    *static* find\_model\_def(*libOrCell: [Cell](../cell.md#keysight.ads.de.Cell "keysight.ads.de._core.cell.Cell")*) → [ModelDefBase](#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db._model_def.ModelDefBase") | None

    *property* has\_model\_param*: bool*[](#keysight.ads.de.db.ModelDefBase.has_model_param "Link to this definition")
    :   A model definition with has\_model\_param set to True will netlist the first parameter as the model name.

        See the [Model Definition Properties](../../../examples/ex_model.md#model-definition-properties) section in the ADS Python Design Environment documentation.

    insert\_parameter(*parameter: [ModelParam](#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")*, *index: int*) → None[](#keysight.ads.de.db.ModelDefBase.insert_parameter "Link to this definition")
    :   insert\_parameter is deprecated, and will be removed in the 2025 Update 2 release. Use: parameters.insert(index, parameter)

    *property* inst\_name\_prefix*: str*[](#keysight.ads.de.db.ModelDefBase.inst_name_prefix "Link to this definition")

    *property* is\_bom\_item*: bool*[](#keysight.ads.de.db.ModelDefBase.is_bom_item "Link to this definition")

    *property* is\_custom\_variable*: bool*[](#keysight.ads.de.db.ModelDefBase.is_custom_variable "Link to this definition")

    *property* is\_ground*: bool*[](#keysight.ads.de.db.ModelDefBase.is_ground "Link to this definition")

    *property* is\_smart\_component*: bool*[](#keysight.ads.de.db.ModelDefBase.is_smart_component "Link to this definition")

    *property* is\_sub\_design*: bool*[](#keysight.ads.de.db.ModelDefBase.is_sub_design "Link to this definition")

    *property* is\_transmission\_line*: bool*[](#keysight.ads.de.db.ModelDefBase.is_transmission_line "Link to this definition")

    *property* is\_unique*: bool*[](#keysight.ads.de.db.ModelDefBase.is_unique "Link to this definition")
    :   Only one instance of this model is allowed in a design.

    *property* is\_variable*: bool*[](#keysight.ads.de.db.ModelDefBase.is_variable "Link to this definition")

    *property* label*: str*[](#keysight.ads.de.db.ModelDefBase.label "Link to this definition")

    *property* legacy\_dialog\_data*: str*[](#keysight.ads.de.db.ModelDefBase.legacy_dialog_data "Link to this definition")

    *property* legacy\_dialog\_name*: str*[](#keysight.ads.de.db.ModelDefBase.legacy_dialog_name "Link to this definition")

    *property* library\_name*: str*[](#keysight.ads.de.db.ModelDefBase.library_name "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.ModelDefBase.name "Link to this definition")

    *property* parameters*: NamedListRefAbc[[ModelParam](#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")]*[](#keysight.ads.de.db.ModelDefBase.parameters "Link to this definition")
    :   Return the collection of parameter definitions in this model definition.

        A parameter definition may be accessed by using the [] operator.
        Use parameters.find to find a parameter by name.

*class* keysight.ads.de.db.ModelParam[](#keysight.ads.de.db.ModelParam "Link to this definition")
:   ModelParam is a parameter definition that is a part of a model definition (see `de.db.ModelDef`).

    Parameter values have associated forms (see `de.db.Form`).
    The allowed forms for a given parameter are listed in its formset (see `de.db.Formset`)

    \_\_init\_\_(*name: str*, *label: str*, *formset: [Formset](forms.md#keysight.ads.de.db.Formset "keysight.ads.de.db.Formset") | None = None*, *unit\_type: [ModelUnitType](parameters.md#keysight.ads.de.db.ModelUnitType "keysight.ads.de.db.ModelUnitType") | str | None = None*, *param\_type: [ModelParamType](parameters.md#keysight.ads.de.db.ModelParamType "keysight.ads.de.db.ModelParamType") | str | None = None*) → None[](#keysight.ads.de.db.ModelParam.__init__ "Link to this definition")
    :   Initialize a ModelParam.

        Parameters:
        :   * **name** (*str*) – Name of the parameter
            * **label** (*str*) – Descriptive label for the parameter
            * **formset** ([*Formset*](forms.md#keysight.ads.de.db.Formset "keysight.ads.de.db.Formset")) – A Formset is a list of one or more [`Form`](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db.Form") that describe how the parameter
              is stored, how it is netlisted and how it is displayed on a schematic
              If not specified, the global StdFormSet will be used.
            * **unit\_type** (*Optional**[*[*ModelUnitType*](parameters.md#keysight.ads.de.db.ModelUnitType "keysight.ads.de.db.ModelUnitType")*]*) – The units of the parameter, defaults to NO\_UNIT (plain numbers)
            * **param\_type** (*Optional**[*[*ModelParamType*](parameters.md#keysight.ads.de.db.ModelParamType "keysight.ads.de.db.ModelParamType")*]*) – The datatype of the parameter value, defaults to REAL

    *property* callbacks*: ListRefAbc[[ModelCbBase](callbacks.md#keysight.ads.de.db.ModelCbBase "keysight.ads.de.db._callbacks.ModelCbBase")]*[](#keysight.ads.de.db.ModelParam.callbacks "Link to this definition")
    :   Return the collection of callbacks in this parameter definition.

    *property* default\_value*: [ParamItem](parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem") | None*[](#keysight.ads.de.db.ModelParam.default_value "Link to this definition")

    find\_parameter\_form(*param: [ParamItem](parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem")*) → [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db.Form") | None[](#keysight.ads.de.db.ModelParam.find_parameter_form "Link to this definition")
    :   find\_parameter\_form is deprecated, and will be removed in the 2025 Update 2 release. Use: formset.forms.find(param.form\_name)

    find\_parameter\_form\_by\_name(*name: str*) → [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db.Form") | None[](#keysight.ads.de.db.ModelParam.find_parameter_form_by_name "Link to this definition")
    :   find\_parameter\_form\_by\_name is deprecated, and will be removed in the 2025 Update 2 release. Use: formset.forms.find(name)

    *property* forms*: Sequence[[Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db.Form")]*[](#keysight.ads.de.db.ModelParam.forms "Link to this definition")
    :   formset.forms

        Type:
        :   forms is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* formset*: [Formset](forms.md#keysight.ads.de.db.Formset "keysight.ads.de.db.Formset")*[](#keysight.ads.de.db.ModelParam.formset "Link to this definition")

    get\_default\_value\_copy(*design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design")*, *model\_definition: [ModelDefBase](#keysight.ads.de.db.ModelDefBase "keysight.ads.de.db.ModelDefBase")*) → [ParamItem](parameters.md#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem")[](#keysight.ads.de.db.ModelParam.get_default_value_copy "Link to this definition")
    :   Get a copy of the default value, invoking the callback if one exists.

    *property* is\_constant*: bool*[](#keysight.ads.de.db.ModelParam.is_constant "Link to this definition")

    *property* is\_design\_name*: bool*[](#keysight.ads.de.db.ModelParam.is_design_name "Link to this definition")

    *property* is\_discrete\_value*: bool*[](#keysight.ads.de.db.ModelParam.is_discrete_value "Link to this definition")

    *property* is\_displayed\_by\_default*: bool*[](#keysight.ads.de.db.ModelParam.is_displayed_by_default "Link to this definition")

    *property* is\_doe*: bool*[](#keysight.ads.de.db.ModelParam.is_doe "Link to this definition")

    *property* is\_editable*: bool*[](#keysight.ads.de.db.ModelParam.is_editable "Link to this definition")

    *property* is\_evaluated*: bool*[](#keysight.ads.de.db.ModelParam.is_evaluated "Link to this definition")

    *property* is\_ignored\_by\_pcell*: bool*[](#keysight.ads.de.db.ModelParam.is_ignored_by_pcell "Link to this definition")

    *property* is\_netlist\_rhs\_only*: bool*[](#keysight.ads.de.db.ModelParam.is_netlist_rhs_only "Link to this definition")

    *property* is\_netlistable*: bool*[](#keysight.ads.de.db.ModelParam.is_netlistable "Link to this definition")

    *property* is\_not\_netlisted\_at\_definition*: bool*[](#keysight.ads.de.db.ModelParam.is_not_netlisted_at_definition "Link to this definition")

    *property* is\_on\_screen\_editable*: bool*[](#keysight.ads.de.db.ModelParam.is_on_screen_editable "Link to this definition")

    *property* is\_optimizable*: bool*[](#keysight.ads.de.db.ModelParam.is_optimizable "Link to this definition")

    *property* is\_repeated*: bool*[](#keysight.ads.de.db.ModelParam.is_repeated "Link to this definition")

    *property* is\_statistical*: bool*[](#keysight.ads.de.db.ModelParam.is_statistical "Link to this definition")

    *property* label*: str*[](#keysight.ads.de.db.ModelParam.label "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.ModelParam.name "Link to this definition")

    *property* param\_type*: [ModelParamType](parameters.md#keysight.ads.de.db.ModelParamType "keysight.ads.de.db.ModelParamType")*[](#keysight.ads.de.db.ModelParam.param_type "Link to this definition")

    *property* unit\_type*: [ModelUnitType](parameters.md#keysight.ads.de.db.ModelUnitType "keysight.ads.de.db.ModelUnitType")*[](#keysight.ads.de.db.ModelParam.unit_type "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/db/parameters.md === -->

# Parameters[](#parameters "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.AppParam[](#keysight.ads.de.db.AppParam "Link to this definition")
:   Bases: `object`

    Holds the value for an application defined OAParam.

    \_\_init\_\_(*app\_type: str*, *value: str | ndarray*) → None[](#keysight.ads.de.db.AppParam.__init__ "Link to this definition")

    *property* app\_type*: str*[](#keysight.ads.de.db.AppParam.app_type "Link to this definition")

    set\_value\_from\_string(*value: str*) → None[](#keysight.ads.de.db.AppParam.set_value_from_string "Link to this definition")

    *property* value*: ndarray*[](#keysight.ads.de.db.AppParam.value "Link to this definition")

    value\_as\_string() → str[](#keysight.ads.de.db.AppParam.value_as_string "Link to this definition")

*class* keysight.ads.de.db.ExpressionContext[](#keysight.ads.de.db.ExpressionContext "Link to this definition")
:   Used for expression evaluation.

    \_\_init\_\_()[](#keysight.ads.de.db.ExpressionContext.__init__ "Link to this definition")

    clear\_design\_caches() → None[](#keysight.ads.de.db.ExpressionContext.clear_design_caches "Link to this definition")
    :   Clear all the caches for this design.

    evaluate\_expression(*expr: str*, *\**, *clear\_caches: bool = False*) → str[](#keysight.ads.de.db.ExpressionContext.evaluate_expression "Link to this definition")
    :   Evaluate the expression in this expression context and return the result.

        If clear\_caches is True, clear all the caches for this design before evaluating.

    *property* hierarchy\_context*: [DesignHierarchy](../design_hierarchy.md#keysight.ads.de.DesignHierarchy "keysight.ads.de._core.design_hierarchy.DesignHierarchy")*[](#keysight.ads.de.db.ExpressionContext.hierarchy_context "Link to this definition")

    *property* is\_valid*: bool*[](#keysight.ads.de.db.ExpressionContext.is_valid "Link to this definition")
    :   Returns True if the HierarchyContext is valid.

    pop() → None[](#keysight.ads.de.db.ExpressionContext.pop "Link to this definition")

    push\_instance\_for\_reading(*inst: InstanceDbu | InstanceUu*) → None[](#keysight.ads.de.db.ExpressionContext.push_instance_for_reading "Link to this definition")

    setup\_hierarchy\_for\_design(*design: DesignDbu | DesignUu*) → None[](#keysight.ads.de.db.ExpressionContext.setup_hierarchy_for_design "Link to this definition")

    setup\_hierarchy\_for\_layout\_only(*design: DesignDbu | DesignUu*) → None[](#keysight.ads.de.db.ExpressionContext.setup_hierarchy_for_layout_only "Link to this definition")

*class* keysight.ads.de.db.OAParam[](#keysight.ads.de.db.OAParam "Link to this definition")
:   OAParams are accessed by your artwork function when generating artwork for your Pcell.

    They are also used to store properties and CDF parameters.
    See `Design.pcell_parameters()`

    \_\_init\_\_(*name: str*, *param\_type: [OAParamType](#keysight.ads.de.db.OAParamType "keysight.ads.de.db._pcell_parameters.OAParamType")*, *val: int | float | str | [TimeParam](#keysight.ads.de.db.TimeParam "keysight.ads.de.db._pcell_parameters.TimeParam") | [AppParam](#keysight.ads.de.db.AppParam "keysight.ads.de.db._pcell_parameters.AppParam")*) → None[](#keysight.ads.de.db.OAParam.__init__ "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.OAParam.name "Link to this definition")

    string\_value\_from\_app\_type(*app\_type: str*) → str[](#keysight.ads.de.db.OAParam.string_value_from_app_type "Link to this definition")

    *property* type*: [OAParamType](#keysight.ads.de.db.OAParamType "keysight.ads.de.db._pcell_parameters.OAParamType")*[](#keysight.ads.de.db.OAParam.type "Link to this definition")

    *property* value*: int | float | str | [TimeParam](#keysight.ads.de.db.TimeParam "keysight.ads.de.db._pcell_parameters.TimeParam") | [AppParam](#keysight.ads.de.db.AppParam "keysight.ads.de.db._pcell_parameters.AppParam")*[](#keysight.ads.de.db.OAParam.value "Link to this definition")

    value\_from\_list\_app\_type() → list[](#keysight.ads.de.db.OAParam.value_from_list_app_type "Link to this definition")

*class* keysight.ads.de.db.Param[](#keysight.ads.de.db.Param "Link to this definition")
:   Bases: [`ParamNonRepeated`](#keysight.ads.de.db.ParamNonRepeated "keysight.ads.de.db._parameters.ParamNonRepeated")

    A single-valued parameter with a value, netlist value, and display value.

    *property* display\_value*: str*[](#keysight.ads.de.db.Param.display_value "Link to this definition")

    evaluate(*expr\_context: [ExpressionContext](#keysight.ads.de.db.ExpressionContext "keysight.ads.de.db._parameters.ExpressionContext")*) → bool | int | float | str[](#keysight.ads.de.db.Param.evaluate "Link to this definition")
    :   Evaluate this parameter value.

    evaluate\_no\_expr() → str[](#keysight.ads.de.db.Param.evaluate_no_expr "Link to this definition")
    :   Prepare this parameter value for use by removing quotes and evaluating units.

        Does not support expressions.
        Will raise an exception if the value has an arithmetic expression
        or references other parameters or variables.

    *property* netlist\_value*: str*[](#keysight.ads.de.db.Param.netlist_value "Link to this definition")

    *property* value*: str*[](#keysight.ads.de.db.Param.value "Link to this definition")

*class* keysight.ads.de.db.ParamBase[](#keysight.ads.de.db.ParamBase "Link to this definition")
:   Base class that holds both a parameter item and its definition.

    See [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db.ParamItem") and `de.db.ModelParam`.

    *property* definition*: [ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam") | None*[](#keysight.ads.de.db.ParamBase.definition "Link to this definition")

    *property* display\_value*: str | list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamBase.display_value "Link to this definition")

    evaluate(*expr\_context: [ExpressionContext](#keysight.ads.de.db.ExpressionContext "keysight.ads.de.db._parameters.ExpressionContext")*) → bool | int | float | str | list[bool | int | float | str] | list[list[bool | int | float | str]][](#keysight.ads.de.db.ParamBase.evaluate "Link to this definition")
    :   Evaluate this parameter value.

    evaluate\_no\_expr() → str | list[str] | list[list[str]][](#keysight.ads.de.db.ParamBase.evaluate_no_expr "Link to this definition")
    :   Prepare this parameter value for use by removing quotes and evaluating units.

        Does not support expressions.
        Will raise an exception if the value has an arithmetic expression
        or references other parameters or variables.

    *property* form\_name*: str*[](#keysight.ads.de.db.ParamBase.form_name "Link to this definition")

    *static* is\_compound(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[ParamCompound](#keysight.ads.de.db.ParamCompound "keysight.ads.de.db._parameters.ParamCompound")][](#keysight.ads.de.db.ParamBase.is_compound "Link to this definition")

    *static* is\_const(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")][](#keysight.ads.de.db.ParamBase.is_const "Link to this definition")

    *static* is\_null(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")][](#keysight.ads.de.db.ParamBase.is_null "Link to this definition")

    *static* is\_repeated(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[ParamRepeated](#keysight.ads.de.db.ParamRepeated "keysight.ads.de.db._parameters.ParamRepeated")][](#keysight.ads.de.db.ParamBase.is_repeated "Link to this definition")

    *static* is\_single\_valued(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")][](#keysight.ads.de.db.ParamBase.is_single_valued "Link to this definition")

    *static* is\_string(*p: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*) → TypeGuard[[Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")][](#keysight.ads.de.db.ParamBase.is_string "Link to this definition")

    *property* item*: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*[](#keysight.ads.de.db.ParamBase.item "Link to this definition")

    *static* make\_param(*item: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*, *model\_param: [ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam") | None*) → [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")[](#keysight.ads.de.db.ParamBase.make_param "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.ParamBase.name "Link to this definition")

    *property* netlist\_value*: str | list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamBase.netlist_value "Link to this definition")

    *property* no\_plot*: bool*[](#keysight.ads.de.db.ParamBase.no_plot "Link to this definition")
    :   When True, this parameter will not be displayed in schematic view.

    *property* value*: str | list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamBase.value "Link to this definition")

*class* keysight.ads.de.db.ParamCompound[](#keysight.ads.de.db.ParamCompound "Link to this definition")
:   Bases: [`ParamNonRepeated`](#keysight.ads.de.db.ParamNonRepeated "keysight.ads.de.db._parameters.ParamNonRepeated")

    A parameter that consists of one or more sub-parameters.

    The sub-parameters may be accessed via sub\_params.

    *property* display\_value*: list[str]*[](#keysight.ads.de.db.ParamCompound.display_value "Link to this definition")

    evaluate(*expr\_context: [ExpressionContext](#keysight.ads.de.db.ExpressionContext "keysight.ads.de.db._parameters.ExpressionContext")*) → list[bool | int | float | str][](#keysight.ads.de.db.ParamCompound.evaluate "Link to this definition")
    :   Evaluate this compound parameter value.

    evaluate\_no\_expr() → list[str][](#keysight.ads.de.db.ParamCompound.evaluate_no_expr "Link to this definition")
    :   Prepare this compound parameter value for use by removing quotes and evaluating units.

        Does not support expressions.
        Will raise an exception if the value has an arithmetic expression
        or references other parameters or variables.

    *property* fields*: list[[Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")]*[](#keysight.ads.de.db.ParamCompound.fields "Link to this definition")
    :   list(sub\_params)

        Type:
        :   fields is deprecated, and will be removed in the 2025 Update 2 release. Use

    get\_field(*index: int*) → [Param](#keysight.ads.de.db.Param "keysight.ads.de.db._parameters.Param")[](#keysight.ads.de.db.ParamCompound.get_field "Link to this definition")
    :   Return the sub-parameter at the specified index.

        get\_field is deprecated, and will be removed in the 2025 Update 2 release. Use: sub\_params[index]

    *property* netlist\_value*: list[str]*[](#keysight.ads.de.db.ParamCompound.netlist_value "Link to this definition")

    *property* num\_fields*: int*[](#keysight.ads.de.db.ParamCompound.num_fields "Link to this definition")
    :   len(sub\_params)

        Type:
        :   num\_fields is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* sub\_params*: \_SubParamCollection*[](#keysight.ads.de.db.ParamCompound.sub_params "Link to this definition")

    *property* value*: list[str]*[](#keysight.ads.de.db.ParamCompound.value "Link to this definition")

*class* keysight.ads.de.db.ParamItem[](#keysight.ads.de.db.ParamItem "Link to this definition")
:   Base class for parameter items.

    See also `de.db.ModelParam` which is the parameter definition.
    The classes derived from ParamItem are used for default values in ModelParam
    and to hold instance and terminal parameter values.

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.ParamItem.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    clone() → [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")[](#keysight.ads.de.db.ParamItem.clone "Link to this definition")

    *property* form\_name*: str*[](#keysight.ads.de.db.ParamItem.form_name "Link to this definition")

    *static* is\_compound(*p: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → TypeGuard[[ParamItemCompound](#keysight.ads.de.db.ParamItemCompound "keysight.ads.de.db._parameters.ParamItemCompound")][](#keysight.ads.de.db.ParamItem.is_compound "Link to this definition")

    *static* is\_const(*p: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → TypeGuard[[ParamItemConst](#keysight.ads.de.db.ParamItemConst "keysight.ads.de.db._parameters.ParamItemConst")][](#keysight.ads.de.db.ParamItem.is_const "Link to this definition")

    *static* is\_null(*p: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → TypeGuard[[ParamItemNull](#keysight.ads.de.db.ParamItemNull "keysight.ads.de.db._parameters.ParamItemNull")][](#keysight.ads.de.db.ParamItem.is_null "Link to this definition")

    *static* is\_repeated(*p: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → TypeGuard[[ParamItemRepeated](#keysight.ads.de.db.ParamItemRepeated "keysight.ads.de.db._parameters.ParamItemRepeated")][](#keysight.ads.de.db.ParamItem.is_repeated "Link to this definition")

    *static* is\_string(*p: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → TypeGuard[[ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString")][](#keysight.ads.de.db.ParamItem.is_string "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.ParamItem.name "Link to this definition")

    *property* no\_plot*: bool*[](#keysight.ads.de.db.ParamItem.no_plot "Link to this definition")
    :   When True, this parameter will not be displayed in schematic view.

*class* keysight.ads.de.db.ParamItemCompound[](#keysight.ads.de.db.ParamItemCompound "Link to this definition")
:   Bases: [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")

    A parameter item that consists one or more sub-parameters.

    The number of sub-parameters must match the number of sub-parameters on the
    compound form that is used to create the parameter definition.

    \_\_init\_\_(*param\_name: str*, *form\_name: str*, *subparams: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → None[](#keysight.ads.de.db.ParamItemCompound.__init__ "Link to this definition")

    get\_sub\_parameter(*index: int*) → [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")[](#keysight.ads.de.db.ParamItemCompound.get_sub_parameter "Link to this definition")
    :   get\_sub\_parameter is deprecated, and will be removed in the 2025 Update 2 release. Use sub\_params[index]

    get\_sub\_parameters() → Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")][](#keysight.ads.de.db.ParamItemCompound.get_sub_parameters "Link to this definition")
    :   get\_sub\_parameters is deprecated, and will be removed in the 2025 Update 2 release. Use: list(sub\_params)

    *property* has\_sub\_parameters*: bool*[](#keysight.ads.de.db.ParamItemCompound.has_sub_parameters "Link to this definition")
    :   len(sub\_params) > 0

        Type:
        :   has\_sub\_parameters is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* number\_of\_sub\_parameters*: int*[](#keysight.ads.de.db.ParamItemCompound.number_of_sub_parameters "Link to this definition")
    :   len(sub\_params)

        Type:
        :   number\_of\_sub\_parameters is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* sub\_params*: IndexedSettableCollectionAbc[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*[](#keysight.ads.de.db.ParamItemCompound.sub_params "Link to this definition")

    *property* value*: list[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*[](#keysight.ads.de.db.ParamItemCompound.value "Link to this definition")
    :   sub\_params

        Type:
        :   value is deprecated, and will be removed in the 2025 Update 2 release. Use

*class* keysight.ads.de.db.ParamItemConst[](#keysight.ads.de.db.ParamItemConst "Link to this definition")
:   Bases: [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")

    A parameter item whose value is determined by its form - (see `de.db.ConstForm`).

    \_\_init\_\_(*param\_name: str*) → None[](#keysight.ads.de.db.ParamItemConst.__init__ "Link to this definition")

    \_\_init\_\_(*param\_name: str*, *form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → None

*class* keysight.ads.de.db.ParamItemNull[](#keysight.ads.de.db.ParamItemNull "Link to this definition")
:   Bases: [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")

    A parameter item with no value.

    \_\_init\_\_(*param\_name: str*) → None[](#keysight.ads.de.db.ParamItemNull.__init__ "Link to this definition")

    *property* value*: None*[](#keysight.ads.de.db.ParamItemNull.value "Link to this definition")

*class* keysight.ads.de.db.ParamItemRepeated[](#keysight.ads.de.db.ParamItemRepeated "Link to this definition")
:   Bases: [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")

    A parameter item that holds a list of one or more repeats.

    The parameter definition’s formset dictates the forms that can be used for each repeat.
    A repeat cannot also be repeated but may use compound forms, having their own sub-parameters.

    \_\_init\_\_(*param\_name: str*, *repeats: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → None[](#keysight.ads.de.db.ParamItemRepeated.__init__ "Link to this definition")

    append\_repeat(*param: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → None[](#keysight.ads.de.db.ParamItemRepeated.append_repeat "Link to this definition")
    :   append\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.append(param)

    append\_repeats(*params: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → None[](#keysight.ads.de.db.ParamItemRepeated.append_repeats "Link to this definition")
    :   append\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.append(params)

    clear\_and\_set\_repeats(*parameters: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → None[](#keysight.ads.de.db.ParamItemRepeated.clear_and_set_repeats "Link to this definition")
    :   clear\_and\_set\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats = parameters

    clear\_and\_set\_single\_repeat(*parameter: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → None[](#keysight.ads.de.db.ParamItemRepeated.clear_and_set_single_repeat "Link to this definition")
    :   clear\_and\_set\_single\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats = parameter

    extract\_repeat(*index: int*) → [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")[](#keysight.ads.de.db.ParamItemRepeated.extract_repeat "Link to this definition")
    :   extract\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.pop(index)

    get\_repeat(*index: int*) → [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")[](#keysight.ads.de.db.ParamItemRepeated.get_repeat "Link to this definition")
    :   get\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats[index]

    get\_repeats() → Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")][](#keysight.ads.de.db.ParamItemRepeated.get_repeats "Link to this definition")
    :   get\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use: list(repeats)

    *property* has\_repeats*: bool*[](#keysight.ads.de.db.ParamItemRepeated.has_repeats "Link to this definition")
    :   len(repeats) > 0

        Type:
        :   has\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use

    insert\_repeat(*index: int*, *param: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*) → None[](#keysight.ads.de.db.ParamItemRepeated.insert_repeat "Link to this definition")
    :   insert\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.insert(index, param)

    *property* number\_of\_repeats*: int*[](#keysight.ads.de.db.ParamItemRepeated.number_of_repeats "Link to this definition")
    :   len(repeats)

        Type:
        :   number\_of\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* repeats*: \_RepeatParamItemCollection*[](#keysight.ads.de.db.ParamItemRepeated.repeats "Link to this definition")

    *property* value*: list[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*[](#keysight.ads.de.db.ParamItemRepeated.value "Link to this definition")
    :   list(repeats)

        Type:
        :   value is deprecated, and will be removed in the 2025 Update 2 release. Use

*class* keysight.ads.de.db.ParamItemString[](#keysight.ads.de.db.ParamItemString "Link to this definition")
:   Bases: [`ParamItem`](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")

    A string-valued parameter item.

    \_\_init\_\_(*param\_name: str*) → None[](#keysight.ads.de.db.ParamItemString.__init__ "Link to this definition")

    \_\_init\_\_(*param\_name: str*, *form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*, *param\_value: str*) → None

    *property* value*: str*[](#keysight.ads.de.db.ParamItemString.value "Link to this definition")

*class* keysight.ads.de.db.ParamIter[](#keysight.ads.de.db.ParamIter "Link to this definition")
:   An iterator that can be used to visit parameters of an instance or terminal.

    \_\_init\_\_(*owner: InstanceDbu | InstanceUu*) → None[](#keysight.ads.de.db.ParamIter.__init__ "Link to this definition")

    \_\_init\_\_(*owner: TermBaseDbu | TermBaseUu*) → None

    *property* definition*: [ModelParam](model_def.md#keysight.ads.de.db.ModelParam "keysight.ads.de.db._model_def.ModelParam")*[](#keysight.ads.de.db.ParamIter.definition "Link to this definition")

    *property* is\_valid*: bool*[](#keysight.ads.de.db.ParamIter.is_valid "Link to this definition")

    *property* item*: [ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")*[](#keysight.ads.de.db.ParamIter.item "Link to this definition")

    *property* value*: [ParamBase](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")*[](#keysight.ads.de.db.ParamIter.value "Link to this definition")

*class* keysight.ads.de.db.ParamNonRepeated[](#keysight.ads.de.db.ParamNonRepeated "Link to this definition")
:   Bases: [`ParamBase`](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")

    Non-repeated parameters are either Param or ParamCompound.

    \_\_init\_\_(*unused: InvalidCall*, *\*args*, *\*\*kwargs*) → None[](#keysight.ads.de.db.ParamNonRepeated.__init__ "Link to this definition")
    :   Return an error about attempts to initialize objects that don’t support initialization.

    *property* display\_value*: str | list[str]*[](#keysight.ads.de.db.ParamNonRepeated.display_value "Link to this definition")

    evaluate(*expr\_context: [ExpressionContext](#keysight.ads.de.db.ExpressionContext "keysight.ads.de.db._parameters.ExpressionContext")*) → bool | int | float | str | list[bool | int | float | str][](#keysight.ads.de.db.ParamNonRepeated.evaluate "Link to this definition")
    :   Evaluate this parameter value.

    evaluate\_no\_expr() → str | list[str][](#keysight.ads.de.db.ParamNonRepeated.evaluate_no_expr "Link to this definition")
    :   Prepare this parameter value for use by removing quotes and evaluating units.

        Does not support expressions.
        Will raise an exception if the value has an arithmetic expression
        or references other parameters or variables.

    *property* netlist\_value*: str | list[str]*[](#keysight.ads.de.db.ParamNonRepeated.netlist_value "Link to this definition")

    *property* value*: str | list[str]*[](#keysight.ads.de.db.ParamNonRepeated.value "Link to this definition")

*class* keysight.ads.de.db.ParamRepeated[](#keysight.ads.de.db.ParamRepeated "Link to this definition")
:   Bases: [`ParamBase`](#keysight.ads.de.db.ParamBase "keysight.ads.de.db._parameters.ParamBase")

    A parameter that is essentially a vector of parameters of the same definition.

    The repeats of a repeated parameter must be non-repeating.
    There must always be at least one repeat.

    append\_repeat(*value: str | Sequence[str]*) → None[](#keysight.ads.de.db.ParamRepeated.append_repeat "Link to this definition")
    :   append\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.append(value)

    delete\_repeat(*index: int*) → None[](#keysight.ads.de.db.ParamRepeated.delete_repeat "Link to this definition")
    :   delete\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.remove(index)

    *property* display\_value*: list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamRepeated.display_value "Link to this definition")

    evaluate(*expr\_context: [ExpressionContext](#keysight.ads.de.db.ExpressionContext "keysight.ads.de.db._parameters.ExpressionContext")*) → list[bool | int | float | str] | list[list[bool | int | float | str]][](#keysight.ads.de.db.ParamRepeated.evaluate "Link to this definition")
    :   Evaluate this repeated parameter value.

    evaluate\_no\_expr() → str | list[str] | list[list[str]][](#keysight.ads.de.db.ParamRepeated.evaluate_no_expr "Link to this definition")
    :   Prepare this repeated parameter value for use by removing quotes and evaluating units.

        Does not support expressions.
        Will raise an exception if the value has an arithmetic expression
        or references other parameters or variables.

    get\_repeat(*index: int*) → [ParamNonRepeated](#keysight.ads.de.db.ParamNonRepeated "keysight.ads.de.db._parameters.ParamNonRepeated")[](#keysight.ads.de.db.ParamRepeated.get_repeat "Link to this definition")
    :   get\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats[index]

    insert\_repeat(*index: int*, *value: str | Sequence[str]*) → None[](#keysight.ads.de.db.ParamRepeated.insert_repeat "Link to this definition")
    :   insert\_repeat is deprecated, and will be removed in the 2025 Update 2 release. Use: repeats.insert(index, value)

    *property* netlist\_value*: list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamRepeated.netlist_value "Link to this definition")

    *property* num\_repeats*: int*[](#keysight.ads.de.db.ParamRepeated.num_repeats "Link to this definition")
    :   len(repeats)

        Type:
        :   num\_repeats is deprecated, and will be removed in the 2025 Update 2 release. Use

    *property* repeats*: \_RepeatParamCollection*[](#keysight.ads.de.db.ParamRepeated.repeats "Link to this definition")

    *property* value*: list[str] | list[list[str]]*[](#keysight.ads.de.db.ParamRepeated.value "Link to this definition")

*class* keysight.ads.de.db.TimeParam[](#keysight.ads.de.db.TimeParam "Link to this definition")
:   \_\_init\_\_(*time: int*) → None[](#keysight.ads.de.db.TimeParam.__init__ "Link to this definition")

    *property* time*: int*[](#keysight.ads.de.db.TimeParam.time "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.db.ModelParamType[](#keysight.ads.de.db.ModelParamType "Link to this definition")
:   REAL *= 'real'*[](#keysight.ads.de.db.ModelParamType.REAL "Link to this definition")

    STRING *= 'string'*[](#keysight.ads.de.db.ModelParamType.STRING "Link to this definition")

    INT *= 'int'*[](#keysight.ads.de.db.ModelParamType.INT "Link to this definition")

    COMPLEX *= 'complex'*[](#keysight.ads.de.db.ModelParamType.COMPLEX "Link to this definition")

    REAL\_ARRAY *= 'realArray'*[](#keysight.ads.de.db.ModelParamType.REAL_ARRAY "Link to this definition")

    INT\_ARRAY *= 'intArray'*[](#keysight.ads.de.db.ModelParamType.INT_ARRAY "Link to this definition")

    STRING\_ARRAY *= 'stringArray'*[](#keysight.ads.de.db.ModelParamType.STRING_ARRAY "Link to this definition")

    COMPLEX\_ARRAY *= 'complexArray'*[](#keysight.ads.de.db.ModelParamType.COMPLEX_ARRAY "Link to this definition")

    FIXED\_POINT *= 'fixed'*[](#keysight.ads.de.db.ModelParamType.FIXED_POINT "Link to this definition")

    FIXED\_POINT\_ARRAY *= 'fixedArray'*[](#keysight.ads.de.db.ModelParamType.FIXED_POINT_ARRAY "Link to this definition")

    PRECISION\_STRING *= 'precision'*[](#keysight.ads.de.db.ModelParamType.PRECISION_STRING "Link to this definition")

    UNSPECIFIED *= 'unspecified'*[](#keysight.ads.de.db.ModelParamType.UNSPECIFIED "Link to this definition")

*class* keysight.ads.de.db.ModelUnitType[](#keysight.ads.de.db.ModelUnitType "Link to this definition")
:   STRING *= 'string'*[](#keysight.ads.de.db.ModelUnitType.STRING "Link to this definition")

    NO\_UNIT *= 'num'*[](#keysight.ads.de.db.ModelUnitType.NO_UNIT "Link to this definition")

    FREQUENCY *= 'freq'*[](#keysight.ads.de.db.ModelUnitType.FREQUENCY "Link to this definition")

    RESISTANCE *= 'res'*[](#keysight.ads.de.db.ModelUnitType.RESISTANCE "Link to this definition")

    CONDUCTANCE *= 'cond'*[](#keysight.ads.de.db.ModelUnitType.CONDUCTANCE "Link to this definition")

    INDUCTANCE *= 'ind'*[](#keysight.ads.de.db.ModelUnitType.INDUCTANCE "Link to this definition")

    CAPACITANCE *= 'cap'*[](#keysight.ads.de.db.ModelUnitType.CAPACITANCE "Link to this definition")

    LENGTH *= 'lng'*[](#keysight.ads.de.db.ModelUnitType.LENGTH "Link to this definition")

    TIME *= 'time'*[](#keysight.ads.de.db.ModelUnitType.TIME "Link to this definition")

    ANGLE *= 'ang'*[](#keysight.ads.de.db.ModelUnitType.ANGLE "Link to this definition")

    POWER *= 'power'*[](#keysight.ads.de.db.ModelUnitType.POWER "Link to this definition")

    VOLTAGE *= 'volt'*[](#keysight.ads.de.db.ModelUnitType.VOLTAGE "Link to this definition")

    CURRENT *= 'cur'*[](#keysight.ads.de.db.ModelUnitType.CURRENT "Link to this definition")

    DISTANCE *= 'dist'*[](#keysight.ads.de.db.ModelUnitType.DISTANCE "Link to this definition")

    TEMPERATURE *= 'temp'*[](#keysight.ads.de.db.ModelUnitType.TEMPERATURE "Link to this definition")

    DB\_GAIN *= 'dbg'*[](#keysight.ads.de.db.ModelUnitType.DB_GAIN "Link to this definition")

    DATARATE *= 'datarate'*[](#keysight.ads.de.db.ModelUnitType.DATARATE "Link to this definition")

    PERCENT *= 'pct'*[](#keysight.ads.de.db.ModelUnitType.PERCENT "Link to this definition")

*class* keysight.ads.de.db.OAParamType[](#keysight.ads.de.db.OAParamType "Link to this definition")
:   The type of an OAParam.

    INT *= <OAParamType.INT: 0>*[](#keysight.ads.de.db.OAParamType.INT "Link to this definition")

    FLOAT *= <OAParamType.FLOAT: 1>*[](#keysight.ads.de.db.OAParamType.FLOAT "Link to this definition")

    STRING *= <OAParamType.STRING: 2>*[](#keysight.ads.de.db.OAParamType.STRING "Link to this definition")

    APP\_PARAM *= <OAParamType.APP\_PARAM: 3>*[](#keysight.ads.de.db.OAParamType.APP_PARAM "Link to this definition")
    :   Application defined parameter holding typed data.

    DOUBLE *= <OAParamType.DOUBLE: 4>*[](#keysight.ads.de.db.OAParamType.DOUBLE "Link to this definition")

    BOOLEAN *= <OAParamType.BOOLEAN: 5>*[](#keysight.ads.de.db.OAParamType.BOOLEAN "Link to this definition")

    TIME *= <OAParamType.TIME: 6>*[](#keysight.ads.de.db.OAParamType.TIME "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.de.db.add\_variable\_to\_var\_instance(*instance: InstanceDbu | InstanceUu*, *name: str*, *value: str*) → None[](#keysight.ads.de.db.add_variable_to_var_instance "Link to this definition")

keysight.ads.de.db.compound\_param(*form\_name: str*, *sub\_params: Sequence[[ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString") | [ParamItemConst](#keysight.ads.de.db.ParamItemConst "keysight.ads.de.db._parameters.ParamItemConst")]*) → [ParamItemCompound](#keysight.ads.de.db.ParamItemCompound "keysight.ads.de.db._parameters.ParamItemCompound")[](#keysight.ads.de.db.compound_param "Link to this definition")

keysight.ads.de.db.const\_param(*form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → [ParamItemConst](#keysight.ads.de.db.ParamItemConst "keysight.ads.de.db._parameters.ParamItemConst")[](#keysight.ads.de.db.const_param "Link to this definition")

keysight.ads.de.db.get\_ui\_indexed\_parameter\_ui\_string(*instance: InstanceDbu | InstanceUu*, *index: int*) → str[](#keysight.ads.de.db.get_ui_indexed_parameter_ui_string "Link to this definition")

keysight.ads.de.db.make\_compound\_param(*form\_name: str*, *sub\_params: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → [ParamItemCompound](#keysight.ads.de.db.ParamItemCompound "keysight.ads.de.db._parameters.ParamItemCompound")[](#keysight.ads.de.db.make_compound_param "Link to this definition")
:   make\_compound\_param is deprecated, and will be removed in the 2025 Update 2 release. Use: compound\_param

keysight.ads.de.db.make\_const\_param(*form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*) → [ParamItemConst](#keysight.ads.de.db.ParamItemConst "keysight.ads.de.db._parameters.ParamItemConst")[](#keysight.ads.de.db.make_const_param "Link to this definition")
:   make\_const\_param is deprecated, and will be removed in the 2025 Update 2 release. Use: const\_param

keysight.ads.de.db.make\_repeated\_param(*repeats: Sequence[[ParamItem](#keysight.ads.de.db.ParamItem "keysight.ads.de.db._parameters.ParamItem")]*) → [ParamItemRepeated](#keysight.ads.de.db.ParamItemRepeated "keysight.ads.de.db._parameters.ParamItemRepeated")[](#keysight.ads.de.db.make_repeated_param "Link to this definition")
:   make\_repeated\_param is deprecated, and will be removed in the 2025 Update 2 release. Use: repeated\_param

keysight.ads.de.db.make\_string\_param(*form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*, *value: str*) → [ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString")[](#keysight.ads.de.db.make_string_param "Link to this definition")
:   make\_string\_param is deprecated, and will be removed in the 2025 Update 2 release. Use: string\_param or std\_string\_param

keysight.ads.de.db.repeated\_param(*repeats: Sequence[[ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString") | [ParamItemConst](#keysight.ads.de.db.ParamItemConst "keysight.ads.de.db._parameters.ParamItemConst") | [ParamItemCompound](#keysight.ads.de.db.ParamItemCompound "keysight.ads.de.db._parameters.ParamItemCompound")]*) → [ParamItemRepeated](#keysight.ads.de.db.ParamItemRepeated "keysight.ads.de.db._parameters.ParamItemRepeated")[](#keysight.ads.de.db.repeated_param "Link to this definition")

keysight.ads.de.db.std\_string\_param(*value: str*) → [ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString")[](#keysight.ads.de.db.std_string_param "Link to this definition")
:   Make a ParamItemString using the StdForm.

keysight.ads.de.db.string\_param(*form: str | [Form](forms.md#keysight.ads.de.db.Form "keysight.ads.de.db._forms.Form")*, *value: str*) → [ParamItemString](#keysight.ads.de.db.ParamItemString "keysight.ads.de.db._parameters.ParamItemString")[](#keysight.ads.de.db.string_param "Link to this definition")

keysight.ads.de.db.update\_pcell\_params\_and\_maybe\_relocate\_in\_layout(*instance: InstanceDbu | InstanceUu*, *hierarchy\_context: [DesignHierarchy](../design_hierarchy.md#keysight.ads.de.DesignHierarchy "keysight.ads.de._core.design_hierarchy.DesignHierarchy")*) → None[](#keysight.ads.de.db.update_pcell_params_and_maybe_relocate_in_layout "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/db/properties.md === -->

# Properties[](#properties "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.AppProp[](#keysight.ads.de.db.AppProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    An application specific property.

    These properties have an app\_type and then arbitrary data.
    The data can be anything, including a string.

    *property* app\_type*: str*[](#keysight.ads.de.db.AppProp.app_type "Link to this definition")

    *static* create(*owner: OwnerT*, *name: str*, *app\_type: str*, *value: ndarray | str*) → [AppProp](#keysight.ads.de.db.AppProp "keysight.ads.de.db.AppProp")[](#keysight.ads.de.db.AppProp.create "Link to this definition")

    set\_value\_from\_string(*value: str*) → None[](#keysight.ads.de.db.AppProp.set_value_from_string "Link to this definition")

    *property* value*: ndarray*[](#keysight.ads.de.db.AppProp.value "Link to this definition")

    value\_as\_string() → str[](#keysight.ads.de.db.AppProp.value_as_string "Link to this definition")
    :   Return the value as a string (assumes it is a string).

*class* keysight.ads.de.db.BooleanProp[](#keysight.ads.de.db.BooleanProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: int*) → [BooleanProp](#keysight.ads.de.db.BooleanProp "keysight.ads.de.db.BooleanProp")[](#keysight.ads.de.db.BooleanProp.create "Link to this definition")

    *property* value*: int*[](#keysight.ads.de.db.BooleanProp.value "Link to this definition")

*class* keysight.ads.de.db.DoubleProp[](#keysight.ads.de.db.DoubleProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: float*) → [DoubleProp](#keysight.ads.de.db.DoubleProp "keysight.ads.de.db.DoubleProp")[](#keysight.ads.de.db.DoubleProp.create "Link to this definition")

    *property* value*: float*[](#keysight.ads.de.db.DoubleProp.value "Link to this definition")

*class* keysight.ads.de.db.DoubleRangeProp[](#keysight.ads.de.db.DoubleRangeProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *lower\_bound: float*, *value: float*, *upper\_bound: float*) → [DoubleRangeProp](#keysight.ads.de.db.DoubleRangeProp "keysight.ads.de.db.DoubleRangeProp")[](#keysight.ads.de.db.DoubleRangeProp.create "Link to this definition")

    *property* lower\_bound*: float*[](#keysight.ads.de.db.DoubleRangeProp.lower_bound "Link to this definition")

    set\_range(*lower\_bound: float*, *value: float*, *upper\_bound: float*) → None[](#keysight.ads.de.db.DoubleRangeProp.set_range "Link to this definition")

    *property* upper\_bound*: float*[](#keysight.ads.de.db.DoubleRangeProp.upper_bound "Link to this definition")

    *property* value*: float*[](#keysight.ads.de.db.DoubleRangeProp.value "Link to this definition")

*class* keysight.ads.de.db.EnumProp[](#keysight.ads.de.db.EnumProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    An Enum property - holds a string chosen from a list of strings.

    *static* create(*owner: OwnerT*, *name: str*, *value: str*, *enums: Sequence[str]*) → [EnumProp](#keysight.ads.de.db.EnumProp "keysight.ads.de.db.EnumProp")[](#keysight.ads.de.db.EnumProp.create "Link to this definition")

    *property* enums*: list[str]*[](#keysight.ads.de.db.EnumProp.enums "Link to this definition")

    *property* value*: str*[](#keysight.ads.de.db.EnumProp.value "Link to this definition")

*class* keysight.ads.de.db.FloatProp[](#keysight.ads.de.db.FloatProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: float*) → [FloatProp](#keysight.ads.de.db.FloatProp "keysight.ads.de.db.FloatProp")[](#keysight.ads.de.db.FloatProp.create "Link to this definition")

    *property* value*: float*[](#keysight.ads.de.db.FloatProp.value "Link to this definition")

*class* keysight.ads.de.db.FloatRangeProp[](#keysight.ads.de.db.FloatRangeProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *lower\_bound: float*, *value: float*, *upper\_bound: float*) → [FloatRangeProp](#keysight.ads.de.db.FloatRangeProp "keysight.ads.de.db.FloatRangeProp")[](#keysight.ads.de.db.FloatRangeProp.create "Link to this definition")

    *property* lower\_bound*: float*[](#keysight.ads.de.db.FloatRangeProp.lower_bound "Link to this definition")

    set\_range(*lower\_bound: float*, *value: float*, *upper\_bound: float*) → None[](#keysight.ads.de.db.FloatRangeProp.set_range "Link to this definition")

    *property* upper\_bound*: float*[](#keysight.ads.de.db.FloatRangeProp.upper_bound "Link to this definition")

    *property* value*: float*[](#keysight.ads.de.db.FloatRangeProp.value "Link to this definition")

*class* keysight.ads.de.db.HierProp[](#keysight.ads.de.db.HierProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    An hierarchical property - intended to have properties.

    *static* create(*owner: OwnerT*, *name: str*) → [HierProp](#keysight.ads.de.db.HierProp "keysight.ads.de.db.HierProp")[](#keysight.ads.de.db.HierProp.create "Link to this definition")

*class* keysight.ads.de.db.IntProp[](#keysight.ads.de.db.IntProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: int*) → [IntProp](#keysight.ads.de.db.IntProp "keysight.ads.de.db.IntProp")[](#keysight.ads.de.db.IntProp.create "Link to this definition")

    *property* value*: int*[](#keysight.ads.de.db.IntProp.value "Link to this definition")

*class* keysight.ads.de.db.IntRangeProp[](#keysight.ads.de.db.IntRangeProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *lower\_bound: int*, *value: int*, *upper\_bound: int*) → [IntRangeProp](#keysight.ads.de.db.IntRangeProp "keysight.ads.de.db.IntRangeProp")[](#keysight.ads.de.db.IntRangeProp.create "Link to this definition")

    *property* lower\_bound*: int*[](#keysight.ads.de.db.IntRangeProp.lower_bound "Link to this definition")

    set\_range(*lower\_bound: int*, *value: int*, *upper\_bound: int*) → None[](#keysight.ads.de.db.IntRangeProp.set_range "Link to this definition")

    *property* upper\_bound*: int*[](#keysight.ads.de.db.IntRangeProp.upper_bound "Link to this definition")

    *property* value*: int*[](#keysight.ads.de.db.IntRangeProp.value "Link to this definition")

*class* keysight.ads.de.db.Property[](#keysight.ads.de.db.Property "Link to this definition")
:   Bases: `object`

    The base class for all properties.

    These properties live in a database, typically a design, but can also
    live in DM data files for Library, Cell, and View.

    To add a property to an object, you first choose the class for the Property,
    then initialize an object on the desired property owner.
    For example:
    de.db.StringProp(inst, “name”, “value”)

    To delete a property use delete\_prop.

    delete\_prop() → None[](#keysight.ads.de.db.Property.delete_prop "Link to this definition")

    find\_prop(*name: str*) → [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property") | None[](#keysight.ads.de.db.Property.find_prop "Link to this definition")

    *static* is\_app(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[AppProp](#keysight.ads.de.db.AppProp "keysight.ads.de.db._prop.AppProp")][](#keysight.ads.de.db.Property.is_app "Link to this definition")

    *static* is\_boolean(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[BooleanProp](#keysight.ads.de.db.BooleanProp "keysight.ads.de.db._prop.BooleanProp")][](#keysight.ads.de.db.Property.is_boolean "Link to this definition")

    *static* is\_double(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[DoubleProp](#keysight.ads.de.db.DoubleProp "keysight.ads.de.db._prop.DoubleProp")][](#keysight.ads.de.db.Property.is_double "Link to this definition")

    *static* is\_double\_range(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[DoubleRangeProp](#keysight.ads.de.db.DoubleRangeProp "keysight.ads.de.db._prop.DoubleRangeProp")][](#keysight.ads.de.db.Property.is_double_range "Link to this definition")

    *static* is\_enum(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[EnumProp](#keysight.ads.de.db.EnumProp "keysight.ads.de.db._prop.EnumProp")][](#keysight.ads.de.db.Property.is_enum "Link to this definition")

    *static* is\_float(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[FloatProp](#keysight.ads.de.db.FloatProp "keysight.ads.de.db._prop.FloatProp")][](#keysight.ads.de.db.Property.is_float "Link to this definition")

    *static* is\_float\_range(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[FloatRangeProp](#keysight.ads.de.db.FloatRangeProp "keysight.ads.de.db._prop.FloatRangeProp")][](#keysight.ads.de.db.Property.is_float_range "Link to this definition")

    *static* is\_hier(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[HierProp](#keysight.ads.de.db.HierProp "keysight.ads.de.db._prop.HierProp")][](#keysight.ads.de.db.Property.is_hier "Link to this definition")

    *static* is\_int(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[IntProp](#keysight.ads.de.db.IntProp "keysight.ads.de.db._prop.IntProp")][](#keysight.ads.de.db.Property.is_int "Link to this definition")

    *static* is\_int\_range(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[IntRangeProp](#keysight.ads.de.db.IntRangeProp "keysight.ads.de.db._prop.IntRangeProp")][](#keysight.ads.de.db.Property.is_int_range "Link to this definition")

    *static* is\_string(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[StringProp](#keysight.ads.de.db.StringProp "keysight.ads.de.db._prop.StringProp")][](#keysight.ads.de.db.Property.is_string "Link to this definition")

    *static* is\_time(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[TimeProp](#keysight.ads.de.db.TimeProp "keysight.ads.de.db._prop.TimeProp")][](#keysight.ads.de.db.Property.is_time "Link to this definition")

    *static* is\_time\_range(*p: [Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")*) → TypeGuard[[TimeRangeProp](#keysight.ads.de.db.TimeRangeProp "keysight.ads.de.db._prop.TimeRangeProp")][](#keysight.ads.de.db.Property.is_time_range "Link to this definition")

    *property* name*: str*[](#keysight.ads.de.db.Property.name "Link to this definition")

    *property* owner*: OwnerT*[](#keysight.ads.de.db.Property.owner "Link to this definition")

    *property* props*: NamedReadableCollectionAbc[[Property](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")]*[](#keysight.ads.de.db.Property.props "Link to this definition")

    *property* type*: [PropType](#keysight.ads.de.db.PropType "keysight.ads.de.db._prop.PropType")*[](#keysight.ads.de.db.Property.type "Link to this definition")

    *property* value*: str*[](#keysight.ads.de.db.Property.value "Link to this definition")

*class* keysight.ads.de.db.PropIter[](#keysight.ads.de.db.PropIter "Link to this definition")
:   Bases: `object`

    \_\_init\_\_(*owner: OwnerT*) → None[](#keysight.ads.de.db.PropIter.__init__ "Link to this definition")

*class* keysight.ads.de.db.StringProp[](#keysight.ads.de.db.StringProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: str*) → [StringProp](#keysight.ads.de.db.StringProp "keysight.ads.de.db.StringProp")[](#keysight.ads.de.db.StringProp.create "Link to this definition")

    *property* value*: str*[](#keysight.ads.de.db.StringProp.value "Link to this definition")

*class* keysight.ads.de.db.TimeProp[](#keysight.ads.de.db.TimeProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *value: int*) → [TimeProp](#keysight.ads.de.db.TimeProp "keysight.ads.de.db.TimeProp")[](#keysight.ads.de.db.TimeProp.create "Link to this definition")

    *property* value*: int*[](#keysight.ads.de.db.TimeProp.value "Link to this definition")

*class* keysight.ads.de.db.TimeRangeProp[](#keysight.ads.de.db.TimeRangeProp "Link to this definition")
:   Bases: [`Property`](#keysight.ads.de.db.Property "keysight.ads.de.db._prop.Property")

    *static* create(*owner: OwnerT*, *name: str*, *lower\_bound: int*, *value: int*, *upper\_bound: int*) → [TimeRangeProp](#keysight.ads.de.db.TimeRangeProp "keysight.ads.de.db.TimeRangeProp")[](#keysight.ads.de.db.TimeRangeProp.create "Link to this definition")

    *property* lower\_bound*: int*[](#keysight.ads.de.db.TimeRangeProp.lower_bound "Link to this definition")

    set\_range(*lower\_bound: int*, *value: int*, *upper\_bound: int*) → None[](#keysight.ads.de.db.TimeRangeProp.set_range "Link to this definition")

    *property* upper\_bound*: int*[](#keysight.ads.de.db.TimeRangeProp.upper_bound "Link to this definition")

    *property* value*: int*[](#keysight.ads.de.db.TimeRangeProp.value "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.db.PropType[](#keysight.ads.de.db.PropType "Link to this definition")
:   The type of a Property.

    INT *= <PropType.INT: 166>*[](#keysight.ads.de.db.PropType.INT "Link to this definition")

    INT\_RANGE *= <PropType.INT\_RANGE: 167>*[](#keysight.ads.de.db.PropType.INT_RANGE "Link to this definition")

    FLOAT *= <PropType.FLOAT: 168>*[](#keysight.ads.de.db.PropType.FLOAT "Link to this definition")

    FLOAT\_RANGE *= <PropType.FLOAT\_RANGE: 169>*[](#keysight.ads.de.db.PropType.FLOAT_RANGE "Link to this definition")

    STRING *= <PropType.STRING: 170>*[](#keysight.ads.de.db.PropType.STRING "Link to this definition")

    APP *= <PropType.APP: 171>*[](#keysight.ads.de.db.PropType.APP "Link to this definition")

    DOUBLE *= <PropType.DOUBLE: 172>*[](#keysight.ads.de.db.PropType.DOUBLE "Link to this definition")

    DOUBLE\_RANGE *= <PropType.DOUBLE\_RANGE: 173>*[](#keysight.ads.de.db.PropType.DOUBLE_RANGE "Link to this definition")

    BOOLEAN *= <PropType.BOOLEAN: 174>*[](#keysight.ads.de.db.PropType.BOOLEAN "Link to this definition")

    HIER *= <PropType.HIER: 175>*[](#keysight.ads.de.db.PropType.HIER "Link to this definition")

    TIME *= <PropType.TIME: 176>*[](#keysight.ads.de.db.PropType.TIME "Link to this definition")

    TIME\_RANGE *= <PropType.TIME\_RANGE: 177>*[](#keysight.ads.de.db.PropType.TIME_RANGE "Link to this definition")

    ENUM *= <PropType.ENUM: 178>*[](#keysight.ads.de.db.PropType.ENUM "Link to this definition")


---

<!-- === 来源: pypde/docs/reference/de/db/transaction.md === -->

# Transaction[](#transaction "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.de.db.Transaction[](#keysight.ads.de.db.Transaction "Link to this definition")
:   Operations performed between when the Transaction is created and when it is committed may be undone.

    This provides the ability to group multiple operations together and undo them with a call to rollback.

    \_\_init\_\_(*design: [Design](../db_uu/db_uu.md#keysight.ads.de.db_uu.Design "keysight.ads.de.db_uu.Design") | DesignDb*, *command: str = 'Edit'*) → None[](#keysight.ads.de.db.Transaction.__init__ "Link to this definition")

    commit() → None[](#keysight.ads.de.db.Transaction.commit "Link to this definition")

    is\_empty() → bool[](#keysight.ads.de.db.Transaction.is_empty "Link to this definition")

    rollback() → None[](#keysight.ads.de.db.Transaction.rollback "Link to this definition")

    *property* state*: [TransactionState](#keysight.ads.de.db.TransactionState "keysight.ads.de.db._transaction.TransactionState")*[](#keysight.ads.de.db.Transaction.state "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.de.db.TransactionState[](#keysight.ads.de.db.TransactionState "Link to this definition")
:   An enumeration specifying the state of a design transaction.

    IN\_PROGRESS *= <TransactionState.IN\_PROGRESS: 0>*[](#keysight.ads.de.db.TransactionState.IN_PROGRESS "Link to this definition")
    :   The transaction is in progress.

    COMMITTED *= <TransactionState.COMMITTED: 1>*[](#keysight.ads.de.db.TransactionState.COMMITTED "Link to this definition")
    :   The transaction has been committed.

    ROLLED\_BACK *= <TransactionState.ROLLED\_BACK: 2>*[](#keysight.ads.de.db.TransactionState.ROLLED_BACK "Link to this definition")
    :   The transaction has been rolled back.


---

<!-- === 来源: pypde/docs/reference/de/db_dbu/index.md === -->

# keysight.ads.de.db\_dbu[](#keysight-ads-de-db-dbu "Link to this heading")

The classes and functions defined in the [keysight.ads.de.db\_uu](../db_uu/index.md) and keysight.ads.de.db\_dbu packages are largely identical but are differentiated by units; user units (uu) and database units (dbu).

See the [keysight.ads.de.db\_uu](../db_uu/index.md) package for the API definition that is available in both the keysight.ads.de.db\_uu and keysight.ads.de.db\_dbu packages.

Database module using integer database units without conversion.

## Classes[](#classes "Link to this heading")

> *class* keysight.ads.de.db\_dbu.DbBox[](#keysight.ads.de.db_dbu.DbBox "Link to this definition")
> :   Bases: `object`
>
>     \_\_init\_\_(*x1: int | None = None*, *y1: int | None = None*, *x2: int | None = None*, *y2: int | None = None*, *lower\_left: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU") | None = None*, *upper\_right: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU") | None = None*) → None[](#keysight.ads.de.db_dbu.DbBox.__init__ "Link to this definition")
>
>     contains\_box(*box: [DbBox](#keysight.ads.de.db_dbu.DbBox "keysight.ads.de.db_dbu._db_box.DbBox")*) → bool[](#keysight.ads.de.db_dbu.DbBox.contains_box "Link to this definition")
>
>     contains\_coordinates(*x: int*, *y: int*) → bool[](#keysight.ads.de.db_dbu.DbBox.contains_coordinates "Link to this definition")
>
>     contains\_point(*point: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*) → bool[](#keysight.ads.de.db_dbu.DbBox.contains_point "Link to this definition")
>
>     *property* has\_zero\_area*: bool*[](#keysight.ads.de.db_dbu.DbBox.has_zero_area "Link to this definition")
>
>     *property* is\_degenerate*: bool*[](#keysight.ads.de.db_dbu.DbBox.is_degenerate "Link to this definition")
>
>     *property* lower\_left*: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*[](#keysight.ads.de.db_dbu.DbBox.lower_left "Link to this definition")
>
>     *property* lower\_right*: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*[](#keysight.ads.de.db_dbu.DbBox.lower_right "Link to this definition")
>
>     overlaps(*box: [DbBox](#keysight.ads.de.db_dbu.DbBox "keysight.ads.de.db_dbu._db_box.DbBox")*) → bool[](#keysight.ads.de.db_dbu.DbBox.overlaps "Link to this definition")
>
>     *property* upper\_left*: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*[](#keysight.ads.de.db_dbu.DbBox.upper_left "Link to this definition")
>
>     *property* upper\_right*: [PointDBU](../points.md#keysight.ads.de.PointDBU "keysight.ads.de._points.PointDBU")*[](#keysight.ads.de.db_dbu.DbBox.upper_right "Link to this definition")
>
>     *property* x1*: int*[](#keysight.ads.de.db_dbu.DbBox.x1 "Link to this definition")
>
>     *property* x2*: int*[](#keysight.ads.de.db_dbu.DbBox.x2 "Link to this definition")
>
>     *property* y1*: int*[](#keysight.ads.de.db_dbu.DbBox.y1 "Link to this definition")
>
>     *property* y2*: int*[](#keysight.ads.de.db_dbu.DbBox.y2 "Link to this definition")


---

