# Reference
> **说明：** Reference 相关页面。

> **何时使用：** 当你需要查阅 Reference 相关内容时

---

## 本文件目录

- **Core** (`reference/hsd/core.md`)
- **keysight.ads.hsd** (`reference/hsd/index.md`)
- **Memory Bus Designer** (`reference/hsd/memory/bus_designer.md`)
- **Memory Bus T-Line** (`reference/hsd/memory/bus_tline.md`)
- **Memory Controller** (`reference/hsd/memory/ddr_controller.md`)
- **Memory DRAM** (`reference/hsd/memory/ddr_memory.md`)
- **Memory Termination** (`reference/hsd/memory/ddr_termination.md`)
- **keysight.ads.hsd.memory** (`reference/hsd/memory/index.md`)
- **Memory IO Component** (`reference/hsd/memory/io_component.md`)
- **Memory Printed Circuit Board (PCB)** (`reference/hsd/memory/pcb.md`)
- **Memory Pre-layout** (`reference/hsd/memory/prelayout.md`)
- **Memory Probe** (`reference/hsd/memory/probe.md`)
- **Memory Setup** (`reference/hsd/memory/setup.md`)
- **Memory Interface Simulator** (`reference/hsd/memory/simulator.md`)
- **Metadata** (`reference/hsd/metadata.md`)
- **Smart Wire** (`reference/hsd/smartwire.md`)
- **Reference** (`reference/index.md`)

---

<!-- === 来源: reference/hsd/core.md === -->

# Core[](#core "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.DesignParameters[](#keysight.ads.hsd.DesignParameters "Link to this definition")
:   Bases: `MutableMapping`[`str`, `str`]

    A dictionary-like wrapper for design parameters that supports item assignment.

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.DesignParameters.get "Link to this definition")

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.DesignParameters.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.DesignParameters.keys "Link to this definition")

    update([*E*, ]*\*\*F*) → None.  Update D from mapping/iterable E and F.[](#keysight.ads.hsd.DesignParameters.update "Link to this definition")
    :   If E present and has a .keys() method, does: for k in E.keys(): D[k] = E[k]
        If E present and lacks .keys() method, does: for (k, v) in E: D[k] = v
        In either case, this is followed by: for k, v in F.items(): D[k] = v

    values() → an object providing a view on D's values[](#keysight.ads.hsd.DesignParameters.values "Link to this definition")


---

<!-- === 来源: reference/hsd/index.md === -->

# keysight.ads.hsd[](#module-keysight.ads.hsd "Link to this heading")

ADS HSD Designer scripting.

## Classes[](#classes "Link to this heading")

* [Core](core.md)
  + [Classes](core.md#classes)
* [Metadata](metadata.md)
  + [Enumerated types](metadata.md#enumerated-types)
  + [Classes](metadata.md#classes)
* [Smart Wire](smartwire.md)
  + [Functions](smartwire.md#functions)


---

<!-- === 来源: reference/hsd/memory/bus_designer.md === -->

# Memory Bus Designer[](#memory-bus-designer "Link to this heading")

## Enumerated types[](#enumerated-types "Link to this heading")

*class* keysight.ads.hsd.memory.busdesigner.BusConfigurationType[](#keysight.ads.hsd.memory.busdesigner.BusConfigurationType "Link to this definition")
:   Bases: `EnumWrapper`

    The bus configuration type.

    CA\_CTRL\_DIMM\_BOARD *= <DdrBusConfigurationType.CA\_CTRL\_DIMM\_BOARD: 4>*[](#keysight.ads.hsd.memory.busdesigner.BusConfigurationType.CA_CTRL_DIMM_BOARD "Link to this definition")

    CA\_CTRL\_DIMM\_MOTHER\_BOARD *= <DdrBusConfigurationType.CA\_CTRL\_DIMM\_MOTHER\_BOARD: 5>*[](#keysight.ads.hsd.memory.busdesigner.BusConfigurationType.CA_CTRL_DIMM_MOTHER_BOARD "Link to this definition")

    CA\_CTRL\_EMBEDDED *= <DdrBusConfigurationType.CA\_CTRL\_EMBEDDED: 3>*[](#keysight.ads.hsd.memory.busdesigner.BusConfigurationType.CA_CTRL_EMBEDDED "Link to this definition")

    DATA\_DIMM\_BOARD *= <DdrBusConfigurationType.DATA\_DIMM\_BOARD: 1>*[](#keysight.ads.hsd.memory.busdesigner.BusConfigurationType.DATA_DIMM_BOARD "Link to this definition")

    DATA\_DIMM\_MOTHER\_BOARD *= <DdrBusConfigurationType.DATA\_DIMM\_MOTHER\_BOARD: 2>*[](#keysight.ads.hsd.memory.busdesigner.BusConfigurationType.DATA_DIMM_MOTHER_BOARD "Link to this definition")

    DATA\_EMBEDDED *= <DdrBusConfigurationType.DATA\_EMBEDDED: 0>*[](#keysight.ads.hsd.memory.busdesigner.BusConfigurationType.DATA_EMBEDDED "Link to this definition")

*class* keysight.ads.hsd.memory.busdesigner.StrobePositionType[](#keysight.ads.hsd.memory.busdesigner.StrobePositionType "Link to this definition")
:   Bases: `EnumWrapper`

    The strobe position type.

    AFTER\_DATA *= <StrobePositionType.AFTER\_DATA: 1>*[](#keysight.ads.hsd.memory.busdesigner.StrobePositionType.AFTER_DATA "Link to this definition")

    BEFORE\_DATA *= <StrobePositionType.BEFORE\_DATA: 0>*[](#keysight.ads.hsd.memory.busdesigner.StrobePositionType.BEFORE_DATA "Link to this definition")

    BETWEEN\_DATA *= <StrobePositionType.BETWEEN\_DATA: 2>*[](#keysight.ads.hsd.memory.busdesigner.StrobePositionType.BETWEEN_DATA "Link to this definition")

*class* keysight.ads.hsd.memory.busdesigner.TlineSpacingType[](#keysight.ads.hsd.memory.busdesigner.TlineSpacingType "Link to this definition")
:   Bases: `EnumWrapper`

    CENTER\_TO\_CENTER *= 'CenterLine'*[](#keysight.ads.hsd.memory.busdesigner.TlineSpacingType.CENTER_TO_CENTER "Link to this definition")

    EDGE\_TO\_EDGE *= 'EdgeToEdge'*[](#keysight.ads.hsd.memory.busdesigner.TlineSpacingType.EDGE_TO_EDGE "Link to this definition")

    *classmethod* from\_enum\_value(*enum: str*) → str[](#keysight.ads.hsd.memory.busdesigner.TlineSpacingType.from_enum_value "Link to this definition")

    *classmethod* from\_str\_value(*value: str*) → [TlineSpacingType](#keysight.ads.hsd.memory.busdesigner.TlineSpacingType "keysight.ads.hsd._common.bus_designers.TlineSpacingType")[](#keysight.ads.hsd.memory.busdesigner.TlineSpacingType.from_str_value "Link to this definition")

*class* keysight.ads.hsd.memory.busdesigner.ViaInputType[](#keysight.ads.hsd.memory.busdesigner.ViaInputType "Link to this definition")
:   Bases: `EnumWrapper`

    EM\_MODEL *= <ViaInputType.EM\_MODEL: 2>*[](#keysight.ads.hsd.memory.busdesigner.ViaInputType.EM_MODEL "Link to this definition")

    SHORT *= <ViaInputType.SHORT: 1>*[](#keysight.ads.hsd.memory.busdesigner.ViaInputType.SHORT "Link to this definition")

    SPARAMFILE *= <ViaInputType.SPARAMFILE: 0>*[](#keysight.ads.hsd.memory.busdesigner.ViaInputType.SPARAMFILE "Link to this definition")

*class* keysight.ads.hsd.memory.busdesigner.ViaPinConfigType[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType "Link to this definition")
:   Bases: `EnumWrapper`

    BREAKOUT\_COUPLED\_LEFT\_TO\_RIGHT\_END\_FEED *= <SparamPinConfigType.BREAKOUT\_COUPLED\_LEFT\_TO\_RIGHT\_END\_FEED: 4>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.BREAKOUT_COUPLED_LEFT_TO_RIGHT_END_FEED "Link to this definition")

    BREAKOUT\_COUPLED\_LEFT\_TO\_RIGHT\_MIDDLE\_FEED *= <SparamPinConfigType.BREAKOUT\_COUPLED\_LEFT\_TO\_RIGHT\_MIDDLE\_FEED: 5>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.BREAKOUT_COUPLED_LEFT_TO_RIGHT_MIDDLE_FEED "Link to this definition")

    BREAKOUT\_COUPLED\_TOP\_TO\_BOTTOM\_END\_FEED *= <SparamPinConfigType.BREAKOUT\_COUPLED\_TOP\_TO\_BOTTOM\_END\_FEED: 6>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.BREAKOUT_COUPLED_TOP_TO_BOTTOM_END_FEED "Link to this definition")

    BREAKOUT\_COUPLED\_TOP\_TO\_BOTTOM\_MIDDLE\_FEED *= <SparamPinConfigType.BREAKOUT\_COUPLED\_TOP\_TO\_BOTTOM\_MIDDLE\_FEED: 7>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.BREAKOUT_COUPLED_TOP_TO_BOTTOM_MIDDLE_FEED "Link to this definition")

    BREAKOUT\_COUPLED\_TOP\_TO\_BOTTOM\_TO\_TOP\_END\_FEED *= <SparamPinConfigType.BREAKOUT\_COUPLED\_TOP\_TO\_BOTTOM\_TO\_TOP\_END\_FEED: 8>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.BREAKOUT_COUPLED_TOP_TO_BOTTOM_TO_TOP_END_FEED "Link to this definition")

    BREAKOUT\_NON\_COUPLED\_LEFT\_TO\_RIGHT\_END\_FEED *= <SparamPinConfigType.BREAKOUT\_NON\_COUPLED\_LEFT\_TO\_RIGHT\_END\_FEED: 9>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.BREAKOUT_NON_COUPLED_LEFT_TO_RIGHT_END_FEED "Link to this definition")

    BREAKOUT\_NON\_COUPLED\_LEFT\_TO\_RIGHT\_MIDDLE\_FEED *= <SparamPinConfigType.BREAKOUT\_NON\_COUPLED\_LEFT\_TO\_RIGHT\_MIDDLE\_FEED: 10>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.BREAKOUT_NON_COUPLED_LEFT_TO_RIGHT_MIDDLE_FEED "Link to this definition")

    CLAM\_SHELL\_COUPLED\_LEFT\_TO\_RIGHT\_END\_FEED *= <SparamPinConfigType.CLAM\_SHELL\_COUPLED\_LEFT\_TO\_RIGHT\_END\_FEED: 11>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.CLAM_SHELL_COUPLED_LEFT_TO_RIGHT_END_FEED "Link to this definition")

    CLAM\_SHELL\_COUPLED\_LEFT\_TO\_RIGHT\_MIDDLE\_FEED *= <SparamPinConfigType.CLAM\_SHELL\_COUPLED\_LEFT\_TO\_RIGHT\_MIDDLE\_FEED: 12>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.CLAM_SHELL_COUPLED_LEFT_TO_RIGHT_MIDDLE_FEED "Link to this definition")

    CLAM\_SHELL\_COUPLED\_TOP\_TO\_BOTTOM\_END\_FEED *= <SparamPinConfigType.CLAM\_SHELL\_COUPLED\_TOP\_TO\_BOTTOM\_END\_FEED: 13>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.CLAM_SHELL_COUPLED_TOP_TO_BOTTOM_END_FEED "Link to this definition")

    CLAM\_SHELL\_COUPLED\_TOP\_TO\_BOTTOM\_MIDDLE\_FEED *= <SparamPinConfigType.CLAM\_SHELL\_COUPLED\_TOP\_TO\_BOTTOM\_MIDDLE\_FEED: 14>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.CLAM_SHELL_COUPLED_TOP_TO_BOTTOM_MIDDLE_FEED "Link to this definition")

    CLAM\_SHELL\_COUPLED\_TOP\_TO\_BOTTOM\_TO\_TOP\_END\_FEED *= <SparamPinConfigType.CLAM\_SHELL\_COUPLED\_TOP\_TO\_BOTTOM\_TO\_TOP\_END\_FEED: 15>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.CLAM_SHELL_COUPLED_TOP_TO_BOTTOM_TO_TOP_END_FEED "Link to this definition")

    CLAM\_SHELL\_NON\_COUPLED\_LEFT\_TO\_RIGHT\_END\_FEED *= <SparamPinConfigType.CLAM\_SHELL\_NON\_COUPLED\_LEFT\_TO\_RIGHT\_END\_FEED: 16>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.CLAM_SHELL_NON_COUPLED_LEFT_TO_RIGHT_END_FEED "Link to this definition")

    CLAM\_SHELL\_NON\_COUPLED\_LEFT\_TO\_RIGHT\_MIDDLE\_FEED *= <SparamPinConfigType.CLAM\_SHELL\_NON\_COUPLED\_LEFT\_TO\_RIGHT\_MIDDLE\_FEED: 17>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.CLAM_SHELL_NON_COUPLED_LEFT_TO_RIGHT_MIDDLE_FEED "Link to this definition")

    CUSTOM *= <SparamPinConfigType.CUSTOM: 18>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.CUSTOM "Link to this definition")

    NON\_BREAKOUT\_COUPLED\_LEFT\_TO\_RIGHT *= <SparamPinConfigType.NON\_BREAKOUT\_COUPLED\_LEFT\_TO\_RIGHT: 0>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.NON_BREAKOUT_COUPLED_LEFT_TO_RIGHT "Link to this definition")

    NON\_BREAKOUT\_COUPLED\_TOP\_TO\_BOTTOM *= <SparamPinConfigType.NON\_BREAKOUT\_COUPLED\_TOP\_TO\_BOTTOM: 1>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.NON_BREAKOUT_COUPLED_TOP_TO_BOTTOM "Link to this definition")

    NON\_BREAKOUT\_COUPLED\_TOP\_TO\_BOTTOM\_TO\_TOP *= <SparamPinConfigType.NON\_BREAKOUT\_COUPLED\_TOP\_TO\_BOTTOM\_TO\_TOP: 2>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.NON_BREAKOUT_COUPLED_TOP_TO_BOTTOM_TO_TOP "Link to this definition")

    NON\_BREAKOUT\_NON\_COUPLED\_LEFT\_TO\_RIGHT *= <SparamPinConfigType.NON\_BREAKOUT\_NON\_COUPLED\_LEFT\_TO\_RIGHT: 3>*[](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType.NON_BREAKOUT_NON_COUPLED_LEFT_TO_RIGHT "Link to this definition")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.busdesigner.TLineModel[](#keysight.ads.hsd.memory.busdesigner.TLineModel "Link to this definition")
:   Bases: `object`

    get\_clearance(*index: int*) → str[](#keysight.ads.hsd.memory.busdesigner.TLineModel.get_clearance "Link to this definition")
    :   Get the clearance of Bus Designer Tline component.

        Parameters:
        :   **index** (int) – The index of the line.

        Returns:
        :   The clearance of the line in Bus Designer Tline component.

        Return type:
        :   str

    get\_spacing(*index: int*) → str[](#keysight.ads.hsd.memory.busdesigner.TLineModel.get_spacing "Link to this definition")
    :   Get the spacing of Bus Designer Tline component.

        Returns:
        :   The spacing of Bus Designer Tline component.

        Return type:
        :   str

    get\_spacing\_type(*index: int*) → [TlineSpacingType](#keysight.ads.hsd.memory.busdesigner.TlineSpacingType "keysight.ads.hsd._common.bus_designers.TlineSpacingType")[](#keysight.ads.hsd.memory.busdesigner.TLineModel.get_spacing_type "Link to this definition")
    :   Get the spacing type of Bus Designer Tline component.

        Parameters:
        :   **index** (int) – The index of the metadata.

        Returns:
        :   The spacing type of Bus Designer Tline component.

        Return type:
        :   TlineSpacingType

    get\_width(*index: int*) → str[](#keysight.ads.hsd.memory.busdesigner.TLineModel.get_width "Link to this definition")
    :   Get the width of Bus Designer Tline component.

        Returns:
        :   The width of Bus Designer Tline component.

        Return type:
        :   str

    *property* instance\_name*: str*[](#keysight.ads.hsd.memory.busdesigner.TLineModel.instance_name "Link to this definition")
    :   Get the instance name of Bus Designer Tline component.

        Returns:
        :   The instance name of Bus Designer Tline component.

        Return type:
        :   str

    *property* length*: str*[](#keysight.ads.hsd.memory.busdesigner.TLineModel.length "Link to this definition")
    :   Get the length of Bus Designer Tline component.

        Returns:
        :   The length of Bus Designer Tline component.

        Return type:
        :   str

    *property* line\_type*: str*[](#keysight.ads.hsd.memory.busdesigner.TLineModel.line_type "Link to this definition")
    :   Get the line type of Bus Designer Tline component.

        Returns:
        :   The line type of Bus Designer Tline component.

        Return type:
        :   str

    print\_parameters() → None[](#keysight.ads.hsd.memory.busdesigner.TLineModel.print_parameters "Link to this definition")
    :   Print the properties (spacing, spacing type, width, clearance) of Bus Designer Tline component.

        Return type:
        :   None

    *property* properties*: list[dict[str, str]]*[](#keysight.ads.hsd.memory.busdesigner.TLineModel.properties "Link to this definition")
    :   Get the properties (spacing, spacing type, width, clearance) of Bus Designer Tline component.

        Returns:
        :   The properties of Bus Designer Tline component.

        Return type:
        :   list[dict[str, str]]

    set\_clearance(*index: int*, *clearance: str*) → None[](#keysight.ads.hsd.memory.busdesigner.TLineModel.set_clearance "Link to this definition")
    :   Update the clearance of Bus Designer Tline component.

        Parameters:
        :   * **index** (int) – The index of the line.
            * **clearance** (str) – The clearance of the line in Bus Designer Tline component.

        Return type:
        :   None

    set\_spacing(*index: int*, *spacing: str*) → None[](#keysight.ads.hsd.memory.busdesigner.TLineModel.set_spacing "Link to this definition")
    :   Update the spacing of Bus Designer Tline component.

        Parameters:
        :   * **index** (int) – The index of the metadata.
            * **spacing** (str) – The spacing of Bus Designer Tline component.

        Return type:
        :   None

    set\_spacing\_type(*index: int*, *spacing\_type: [TlineSpacingType](#keysight.ads.hsd.memory.busdesigner.TlineSpacingType "keysight.ads.hsd._common.bus_designers.TlineSpacingType")*) → None[](#keysight.ads.hsd.memory.busdesigner.TLineModel.set_spacing_type "Link to this definition")
    :   Update the spacing type of Bus Designer Tline component.

        Parameters:
        :   * **index** (int) – The index of the metadata.
            * **spacing\_type** (str) – The spacing type of Bus Designer Tline component.

        Return type:
        :   None

    set\_width(*index: int*, *width: str*) → None[](#keysight.ads.hsd.memory.busdesigner.TLineModel.set_width "Link to this definition")
    :   Update the width of Bus Designer Tline component.

        Parameters:
        :   **width** (str) – The width of Bus Designer Tline component.

        Return type:
        :   None

    unset\_clearance(*index: int*) → None[](#keysight.ads.hsd.memory.busdesigner.TLineModel.unset_clearance "Link to this definition")
    :   Unset the clearance of Bus Designer Tline component.

        Parameters:
        :   **index** (int) – The index of the line.

        Return type:
        :   None

*class* keysight.ads.hsd.memory.busdesigner.ViaModel[](#keysight.ads.hsd.memory.busdesigner.ViaModel "Link to this definition")
:   Bases: `object`

    *property* breakout\_feed*: str*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.breakout_feed "Link to this definition")
    :   Get the selected breakout feed of via component.

        Returns:
        :   The selected breakout feed of via component.

        Return type:
        :   str

    *property* breakout\_ref\_des\_list*: list[str]*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.breakout_ref_des_list "Link to this definition")
    :   Get the breakout ref des list string of via component.

        Returns:
        :   The breakout ref des list string of via component.

        Return type:
        :   list[str]

    *property* clamshell\_breakout\_feed*: str*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.clamshell_breakout_feed "Link to this definition")
    :   Get the clamshell breakout feed’s reference designator for the via component.

        Returns:
        :   The clamshell breakout feed’s reference designator for the via component.

        Return type:
        :   str

    *property* design\_parameters*: [DesignParameters](../core.md#keysight.ads.hsd.DesignParameters "keysight.ads.hsd._common.utils.DesignParameters")*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.design_parameters "Link to this definition")
    :   Get the design parameters associated with the via component.

        Returns:
        :   An object containing the design parameter names and their values.

        Return type:
        :   [DesignParameters](../core.md#keysight.ads.hsd.DesignParameters "keysight.ads.hsd.DesignParameters")

    *property* em\_model\_cell\_name*: str*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.em_model_cell_name "Link to this definition")
    :   Get the em model cell name of via component.

        Returns:
        :   The em model cell name of via component.

        Return type:
        :   str

    *property* has\_metadata*: bool*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.has_metadata "Link to this definition")
    :   Get the flag of via has metadata of via component.

        Returns:
        :   The via has metadata of via component.

        Return type:
        :   bool

    *property* instance\_name*: str*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.instance_name "Link to this definition")
    :   Get the instance name of via component.

        Returns:
        :   The instance name of via component.

        Return type:
        :   str

    *property* is\_coupled*: bool*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.is_coupled "Link to this definition")
    :   Get the flag of via is coupled of via component.

        Returns:
        :   The via is coupled of via component.

        Return type:
        :   bool

    *property* num\_of\_signals*: int*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.num_of_signals "Link to this definition")
    :   Get the number of signals of via component.

        Returns:
        :   The number of signals of via component.

        Return type:
        :   int

    *property* pin\_names*: list[str]*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.pin_names "Link to this definition")
    :   Get the pin names of via component.

        Returns:
        :   The pin names of via component.

        Return type:
        :   list[str]

    *property* pin\_order\_config\_type*: [ViaPinConfigType](#keysight.ads.hsd.memory.busdesigner.ViaPinConfigType "keysight.ads.hsd._common.bus_designers.ViaPinConfigType")*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.pin_order_config_type "Link to this definition")
    :   Get the sparam/em-model pin order config of via component.

        Returns:
        :   The sparam/em-model pin order config of via component.

        Return type:
        :   SparamPinConfigType

    print\_em\_model\_cell\_parameters() → None[](#keysight.ads.hsd.memory.busdesigner.ViaModel.print_em_model_cell_parameters "Link to this definition")
    :   Print the parameters of the EM model cell associated with the via component.

        Return type:
        :   None

    print\_signal\_information() → None[](#keysight.ads.hsd.memory.busdesigner.ViaModel.print_signal_information "Link to this definition")
    :   Print the signal information of the via component.

        Return type:
        :   None

    set\_em\_model\_cell\_parameter\_value(*parameter\_name: str*, *parameter\_value: str*) → None[](#keysight.ads.hsd.memory.busdesigner.ViaModel.set_em_model_cell_parameter_value "Link to this definition")
    :   Set the value of a specific parameter in the EM model cell associated with the via component.

        Parameters:
        :   * **parameter\_name** (str) – The name of the parameter to set.
            * **parameter\_value** (str) – The value to set for the specified parameter.

        Return type:
        :   None

    *property* signal\_information*: list[dict[str, str]]*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.signal_information "Link to this definition")
    :   Get the all signal information of via component.

        Returns:
        :   The all signal information of via component.

        Return type:
        :   list[dict[str, str]]

    *property* sparam\_file\_path*: str*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.sparam_file_path "Link to this definition")
    :   Get the sparam file path of via component.

        Returns:
        :   The sparam file path of via component.

        Return type:
        :   str

    *property* sparam\_file\_sweep*: bool*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.sparam_file_sweep "Link to this definition")
    :   Get the sparam file sweep status of via component.

        Returns:
        :   The sparam file sweep status of via component.

        Return type:
        :   bool

    *property* sparam\_file\_sweep\_var\_name*: str*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.sparam_file_sweep_var_name "Link to this definition")
    :   Get the sparam data file sweep variable name of via component.

        Returns:
        :   The sparam data file sweep variable name of via component.

        Return type:
        :   str

    *property* sparam\_num\_of\_ports*: int*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.sparam_num_of_ports "Link to this definition")
    :   Get the number of ports of via component.

        Returns:
        :   The number of ports of via component.

        Return type:
        :   int

    *property* uses\_breakout\_feed*: bool*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.uses_breakout_feed "Link to this definition")
    :   Get the flag of use breakout feed of via component.

        Returns:
        :   The use breakout feed of via component.

        Return type:
        :   bool

    *property* uses\_clamshell\_topology*: bool*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.uses_clamshell_topology "Link to this definition")
    :   Get the flag of use clamshell topology of via component.

        Returns:
        :   The use clamshell topology of via component.

        Return type:
        :   bool

    *property* via\_type*: [ViaInputType](#keysight.ads.hsd.memory.busdesigner.ViaInputType "keysight.ads.hsd._common.bus_designers.ViaInputType")*[](#keysight.ads.hsd.memory.busdesigner.ViaModel.via_type "Link to this definition")
    :   Get the via type of via component.

        Returns:
        :   The via type of via component.

        Return type:
        :   LayoutComponentType

*class* keysight.ads.hsd.memory.busdesigner.LayoutGroupList[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList "Link to this definition")
:   Bases: `UserList`

    append(*item*)[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.append "Link to this definition")
    :   S.append(value) – append value to the end of the sequence

    clear() → None -- remove all items from S[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.clear "Link to this definition")

    copy()[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.copy "Link to this definition")

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.count "Link to this definition")

    extend(*other*)[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.extend "Link to this definition")
    :   S.extend(iterable) – extend sequence by appending elements from the iterable

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    insert(*i*, *item*)[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.insert "Link to this definition")
    :   S.insert(index, value) – insert value before index

    insert\_line(*index: int*, *inst\_name: str = ''*) → None[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.insert_line "Link to this definition")
    :   Insert a line at the index.

        Parameters:
        :   **index** (int) – The index of the component.

        Return type:
        :   None

    insert\_via(*index: int*, *inst\_name: str = ''*) → None[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.insert_via "Link to this definition")
    :   Insert a via at the index.

        Parameters:
        :   **index** (int) – The index of the component.

        Return type:
        :   None

    move\_component(*from\_index: int*, *to\_index: int*) → None[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.move_component "Link to this definition")
    :   Move the component to a new index.

        Parameters:
        :   * **from\_index** (int) – The current index of the component.
            * **to\_index** (int) – The new index of the component.

        Return type:
        :   None

    pop([*index*]) → item -- remove and return item at index (default last).[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.pop "Link to this definition")
    :   Raise IndexError if list is empty or index is out of range.

    remove(*item*)[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.remove "Link to this definition")
    :   S.remove(value) – remove first occurrence of value.
        Raise ValueError if the value is not present.

    remove\_component(*index: int*) → None[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.remove_component "Link to this definition")
    :   Remove the component at the index.

        Parameters:
        :   **index** (int) – The index of the component.

        Return type:
        :   None

    reverse()[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.reverse "Link to this definition")
    :   S.reverse() – reverse *IN PLACE*

    sort(*\*args*, *\*\*kwds*)[](#keysight.ads.hsd.memory.busdesigner.LayoutGroupList.sort "Link to this definition")

*class* keysight.ads.hsd.memory.busdesigner.LayoutGroup[](#keysight.ads.hsd.memory.busdesigner.LayoutGroup "Link to this definition")
:   Bases: `Sequence`, `Mapping`

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.busdesigner.LayoutGroup.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.busdesigner.LayoutGroup.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.busdesigner.LayoutGroup.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.busdesigner.LayoutGroup.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.busdesigner.LayoutGroup.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.busdesigner.LayoutGroup.values "Link to this definition")

*class* keysight.ads.hsd.memory.busdesigner.BusDesigner[](#keysight.ads.hsd.memory.busdesigner.BusDesigner "Link to this definition")
:   Bases: `BusDesigner`

    The Memory Bus Designer class.

    add\_line(*group\_id: int*, *index: int*) → [TLineModel](#keysight.ads.hsd.memory.busdesigner.TLineModel "keysight.ads.hsd._common.bus_designers.TLineModel")[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.add_line "Link to this definition")
    :   Add a new line to a group in layout setup.

        Parameters:
        :   * **group\_id** (int) – The group ID of the line.
            * **index** (int) – The index of the line.

        Return type:
        :   TLineModel

    add\_via(*group\_id: int*, *index: int*) → [ViaModel](#keysight.ads.hsd.memory.busdesigner.ViaModel "keysight.ads.hsd._common.bus_designers.ViaModel")[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.add_via "Link to this definition")
    :   Add a new via to a group in layout setup.

        Parameters:
        :   * **group\_id** (int) – The group ID of the via.
            * **index** (int) – The index of the via.

        Return type:
        :   ViaModel

    *property* bus\_channel\_id*: str*[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.bus_channel_id "Link to this definition")
    :   Get the bus channel ID.

        Return type:
        :   str

    *property* bus\_configuration*: [BusConfigurationType](#keysight.ads.hsd.memory.busdesigner.BusConfigurationType "keysight.ads.hsd.memory.busdesigner.BusConfigurationType")*[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.bus_configuration "Link to this definition")
    :   Get the bus configuration.

        Return type:
        :   BusConfigurationType

    *property* controller\_ref\_des*: str*[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.controller_ref_des "Link to this definition")
    :   Get the controller reference designator.

        Return type:
        :   str

    dram\_ref\_des(*dram\_index: int*) → str[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.dram_ref_des "Link to this definition")
    :   Get the DRAM reference designator of the DRAM at the specified index in the DRAM list.

        Parameters:
        :   **dram\_index** (int) – The index of the DRAM.

        Return type:
        :   str

    *property* group*: [LayoutGroup](#keysight.ads.hsd.memory.busdesigner.LayoutGroup "keysight.ads.hsd._common.bus_designers.LayoutGroup")*[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.group "Link to this definition")

    insert\_signal(*index: int*, *ref\_des: str*, *signal\_type: str*, *signal\_index: int*, *group\_id: int*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.insert_signal "Link to this definition")
    :   Insert a new signal into signal layout grouping table, after the specified index.

        Parameters:
        :   * **index** (int) – The index of the signal layout grouping information after which new signal needs to be inserted.
            * **ref\_des** (str) – The reference designator of the signal.
            * **signal\_type** (str) – The type of the signal.
            * **signal\_index** (int) – The index of the signal.
            * **group\_id** (int) – The group ID of the signal.

        Return type:
        :   None

    line\_types\_for\_group(*group\_id: int*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.line_types_for_group "Link to this definition")
    :   Get the line types available for the group.

        Parameters:
        :   **group\_id** (int) – The group ID.

        Return type:
        :   None

    move\_component(*group\_id: int*, *from\_index: int*, *to\_index: int*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.move_component "Link to this definition")
    :   Move the component to a new index of layout setup.

        Parameters:
        :   * **group\_id** (int) – The group ID of the component.
            * **from\_index** (int) – The index of the component.
            * **to\_index** (int) – The new index of the component.

        Return type:
        :   None

    *property* number\_of\_address\_lines*: int*[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.number_of_address_lines "Link to this definition")
    :   Get the number of address lines.

        Return type:
        :   int

    number\_of\_dq\_per\_group(*dram\_index: int*) → int[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.number_of_dq_per_group "Link to this definition")
    :   Get the number of DQ per group.

        Parameters:
        :   **dram\_index** (int) – The index of the DRAM.

        Return type:
        :   int

    *property* number\_of\_drams*: int*[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.number_of_drams "Link to this definition")
    :   Get the number of DRAMs.

        Return type:
        :   int

    number\_of\_groups(*dram\_index: int*) → int[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.number_of_groups "Link to this definition")
    :   Get the number of groups.

        Parameters:
        :   **dram\_index** (int) – The index of the DRAM.

        Return type:
        :   int

    print\_dimm\_info() → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.print_dimm_info "Link to this definition")
    :   Prints the DIMM info table.

        Return type:
        :   None

    print\_dram\_info() → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.print_dram_info "Link to this definition")
    :   Prints the DRAM info table.

        Return type:
        :   None

    print\_group\_layout\_information() → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.print_group_layout_information "Link to this definition")
    :   Print the group layout info table.

        Return type:
        :   None

    print\_signal\_group\_info() → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.print_signal_group_info "Link to this definition")

    print\_signal\_group\_info(*index: int*) → None
    :   Prints the signal group info.

        Parameters:
        :   **index** (int) – The table row index.

        Return type:
        :   None

    print\_summary() → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.print_summary "Link to this definition")
    :   Print the summary of the bus designer configuration.

        Return type:
        :   None

    remove\_component(*group\_id: int*, *index: int*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.remove_component "Link to this definition")
    :   Remove the component from layout setup.

        Parameters:
        :   * **group\_id** (int) – The group ID of the component.
            * **index** (int) – The index of the component.

        Return type:
        :   None

    remove\_signal(*index: int*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.remove_signal "Link to this definition")
    :   Remove the signal from signal layout grouping table.

        Parameters:
        :   **index** (int) – The index of the signal in signal layout group information which needs to be removed.

        Return type:
        :   None

    set\_dram\_ref\_des(*dram\_index: int*, *ref\_des: str*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.set_dram_ref_des "Link to this definition")
    :   Set the DRAM reference designator of the DRAM at the specified index in the DRAM list.

        Parameters:
        :   * **dram\_index** (int) – The index of the DRAM.
            * **ref\_des** (str) – The reference designator of the DRAM.

        Return type:
        :   None

    set\_number\_of\_dq\_per\_group(*dram\_index: int*, *num\_of\_dq\_per\_group: int*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.set_number_of_dq_per_group "Link to this definition")
    :   Set the number of DQ per group.

        Parameters:
        :   * **dram\_index** (int) – The index of the DRAM.
            * **num\_of\_dq\_per\_group** (int) – The number of DQ per group.

        Return type:
        :   None

    set\_number\_of\_groups(*dram\_index: int*, *num\_of\_groups: int*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.set_number_of_groups "Link to this definition")
    :   Set the number of groups.

        Parameters:
        :   * **dram\_index** (int) – The index of the DRAM.
            * **num\_of\_groups** (int) – The number of groups.

        Return type:
        :   None

    set\_signal\_group\_id(*index: int*, *group\_id: int*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.set_signal_group_id "Link to this definition")
    :   Set the signal group ID for a signal in signal layout group information.

        Parameters:
        :   * **index** (int) – The index of the signal in signal group information.
            * **group\_id** (int) – The group ID of the signal.

        Return type:
        :   None

    set\_signal\_index(*index: int*, *signal\_index: int*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.set_signal_index "Link to this definition")
    :   Set the signal index for a signal in signal layout group information.

        Parameters:
        :   * **index** (int) – The index of the signal in signal group table.
            * **signal\_index** (int) – The index of the signal.

        Return type:
        :   None

    set\_signal\_ref\_des(*index: int*, *ref\_des: str*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.set_signal_ref_des "Link to this definition")
    :   Set the signal reference designator of a signal in signal layout group information.

        Parameters:
        :   * **index** (int) – The index of the signal in signal group information.
            * **ref\_des** (str) – The reference designator of the signal.

        Return type:
        :   None

    set\_signal\_type(*index: int*, *signal\_type: str*) → None[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.set_signal_type "Link to this definition")
    :   Set the signal type for a signal in signal layout group information.

        Parameters:
        :   * **index** (int) – The index of the signal in signal group information.
            * **signal\_type** (str) – The type of the signal.

        Return type:
        :   None

    signal\_group\_id(*index: int*) → int[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.signal_group_id "Link to this definition")
    :   Get the signal group ID for a signal in signal layout group information.

        Parameters:
        :   **index** (int) – The index of the signal in signal group information.

        Returns:
        :   The group ID of the signal.

        Return type:
        :   int

    signal\_index(*index: int*) → int[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.signal_index "Link to this definition")
    :   Get the signal index of a signal in signal layout group information.

        Parameters:
        :   **index** (int) – The index of the signal in signal group information.

        Returns:
        :   The index of the signal.

        Return type:
        :   int

    signal\_ref\_des(*index: int*) → str[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.signal_ref_des "Link to this definition")
    :   Get the signal reference designator of a signal in signal layout group information.

        Parameters:
        :   **index** (int) – The row index of the signal in signal group information.

        Returns:
        :   The reference designator of the signal.

        Return type:
        :   str

    signal\_type(*index: int*) → str[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.signal_type "Link to this definition")
    :   Get the signal type for a signal in signal layout group information.

        Parameters:
        :   **index** (int) – The index of the signal in signal group information.

        Returns:
        :   The type of the signal.

        Return type:
        :   str

    *property* strobe\_position*: [StrobePositionType](#keysight.ads.hsd.memory.busdesigner.StrobePositionType "keysight.ads.hsd.memory.busdesigner.StrobePositionType")*[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.strobe_position "Link to this definition")
    :   Get the strobe position.

        Return type:
        :   StrobePositionType

    *property* substrate\_name*: str*[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.substrate_name "Link to this definition")
    :   Get the substrate name.

        Returns:
        :   The substrate name.

        Return type:
        :   str

    *property* termination\_ref\_des*: str*[](#keysight.ads.hsd.memory.busdesigner.BusDesigner.termination_ref_des "Link to this definition")
    :   Get the termination reference designator.

        Return type:
        :   str


---

<!-- === 来源: reference/hsd/memory/bus_tline.md === -->

# Memory Bus T-Line[](#memory-bus-t-line "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.bus\_tline.DifferentialLineDelay[](#keysight.ads.hsd.memory.bus_tline.DifferentialLineDelay "Link to this definition")
:   DifferentialLineDelay(even\_line\_delay: str, odd\_line\_delay: str)

    even\_line\_delay*: str*[](#keysight.ads.hsd.memory.bus_tline.DifferentialLineDelay.even_line_delay "Link to this definition")

    odd\_line\_delay*: str*[](#keysight.ads.hsd.memory.bus_tline.DifferentialLineDelay.odd_line_delay "Link to this definition")

*class* keysight.ads.hsd.memory.bus\_tline.DifferentialLineZ0[](#keysight.ads.hsd.memory.bus_tline.DifferentialLineZ0 "Link to this definition")
:   DifferentialLineZ0(common\_z0: str, differential\_z0: str, even\_z0: str, odd\_z0: str)

    common\_z0*: str*[](#keysight.ads.hsd.memory.bus_tline.DifferentialLineZ0.common_z0 "Link to this definition")

    differential\_z0*: str*[](#keysight.ads.hsd.memory.bus_tline.DifferentialLineZ0.differential_z0 "Link to this definition")

    even\_z0*: str*[](#keysight.ads.hsd.memory.bus_tline.DifferentialLineZ0.even_z0 "Link to this definition")

    odd\_z0*: str*[](#keysight.ads.hsd.memory.bus_tline.DifferentialLineZ0.odd_z0 "Link to this definition")

*class* keysight.ads.hsd.memory.bus\_tline.LineData[](#keysight.ads.hsd.memory.bus_tline.LineData "Link to this definition")
:   LineData(channel\_id: str, ref\_des\_in: str, ref\_des\_out: str, signal\_type: keysight.ads.hsd.\_common.metadata.SignalTypeEnum | str, signal\_index: int, set\_auto\_signal\_index: bool = True, line\_width: str = ‘default’, line\_spacing: str = ‘default’, spacing\_type: str = ‘default’, add\_clearance: bool = False, line\_clearance: str = ‘default’)

    *property* add\_clearance*: bool*[](#keysight.ads.hsd.memory.bus_tline.LineData.add_clearance "Link to this definition")

    *property* channel\_id*: str*[](#keysight.ads.hsd.memory.bus_tline.LineData.channel_id "Link to this definition")

    *property* line\_clearance*: str*[](#keysight.ads.hsd.memory.bus_tline.LineData.line_clearance "Link to this definition")

    *property* line\_spacing*: str*[](#keysight.ads.hsd.memory.bus_tline.LineData.line_spacing "Link to this definition")

    *property* line\_width*: str*[](#keysight.ads.hsd.memory.bus_tline.LineData.line_width "Link to this definition")

    *property* ref\_des\_in*: str*[](#keysight.ads.hsd.memory.bus_tline.LineData.ref_des_in "Link to this definition")

    *property* ref\_des\_out*: str*[](#keysight.ads.hsd.memory.bus_tline.LineData.ref_des_out "Link to this definition")

    *property* signal\_index*: int*[](#keysight.ads.hsd.memory.bus_tline.LineData.signal_index "Link to this definition")

    *property* signal\_type*: str*[](#keysight.ads.hsd.memory.bus_tline.LineData.signal_type "Link to this definition")

    *property* spacing\_type*: str*[](#keysight.ads.hsd.memory.bus_tline.LineData.spacing_type "Link to this definition")

*class* keysight.ads.hsd.memory.bus\_tline.LinesData[](#keysight.ads.hsd.memory.bus_tline.LinesData "Link to this definition")
:   \_\_getitem\_\_(*index: int*) → [LineData](#keysight.ads.hsd.memory.bus_tline.LineData "keysight.ads.hsd.memory.bus_tline.LineData")[](#keysight.ads.hsd.memory.bus_tline.LinesData.__getitem__ "Link to this definition")

    \_\_getitem\_\_(*index: slice*) → list[[LineData](#keysight.ads.hsd.memory.bus_tline.LineData "keysight.ads.hsd.memory.bus_tline.LineData")]

    \_\_iter\_\_() → Iterator[[LineData](#keysight.ads.hsd.memory.bus_tline.LineData "keysight.ads.hsd.memory.bus_tline.LineData")][](#keysight.ads.hsd.memory.bus_tline.LinesData.__iter__ "Link to this definition")

    \_\_len\_\_() → int[](#keysight.ads.hsd.memory.bus_tline.LinesData.__len__ "Link to this definition")

    \_\_str\_\_() → str[](#keysight.ads.hsd.memory.bus_tline.LinesData.__str__ "Link to this definition")
    :   Return str(self).

*class* keysight.ads.hsd.memory.bus\_tline.BusTLine[](#keysight.ads.hsd.memory.bus_tline.BusTLine "Link to this definition")
:   *property* auto\_save*: bool*[](#keysight.ads.hsd.memory.bus_tline.BusTLine.auto_save "Link to this definition")

    *property* differential\_line\_delay*: [DifferentialLineDelay](#keysight.ads.hsd.memory.bus_tline.DifferentialLineDelay "keysight.ads.hsd.memory.bus_tline.DifferentialLineDelay")*[](#keysight.ads.hsd.memory.bus_tline.BusTLine.differential_line_delay "Link to this definition")

    *property* differential\_z0*: [DifferentialLineZ0](#keysight.ads.hsd.memory.bus_tline.DifferentialLineZ0 "keysight.ads.hsd.memory.bus_tline.DifferentialLineZ0")*[](#keysight.ads.hsd.memory.bus_tline.BusTLine.differential_z0 "Link to this definition")

    is\_line\_length\_numeric() → bool[](#keysight.ads.hsd.memory.bus_tline.BusTLine.is_line_length_numeric "Link to this definition")

    is\_line\_type\_library\_and\_substrate\_valid() → bool[](#keysight.ads.hsd.memory.bus_tline.BusTLine.is_line_type_library_and_substrate_valid "Link to this definition")

    *property* library\_substrate\_name*: str*[](#keysight.ads.hsd.memory.bus_tline.BusTLine.library_substrate_name "Link to this definition")

    *property* line\_length*: str*[](#keysight.ads.hsd.memory.bus_tline.BusTLine.line_length "Link to this definition")

    *property* line\_type\_options*: list[tuple[str, str]]*[](#keysight.ads.hsd.memory.bus_tline.BusTLine.line_type_options "Link to this definition")

    *property* line\_type\_with\_library\_name*: str*[](#keysight.ads.hsd.memory.bus_tline.BusTLine.line_type_with_library_name "Link to this definition")

    *property* lines\_table*: [LinesData](#keysight.ads.hsd.memory.bus_tline.LinesData "keysight.ads.hsd.memory.bus_tline.LinesData")*[](#keysight.ads.hsd.memory.bus_tline.BusTLine.lines_table "Link to this definition")

    *property* number\_of\_lines*: int*[](#keysight.ads.hsd.memory.bus_tline.BusTLine.number_of_lines "Link to this definition")

    save() → None[](#keysight.ads.hsd.memory.bus_tline.BusTLine.save "Link to this definition")

    *property* single\_ended\_line\_delay\_str*: str*[](#keysight.ads.hsd.memory.bus_tline.BusTLine.single_ended_line_delay_str "Link to this definition")

    *property* single\_ended\_z0\_str*: str*[](#keysight.ads.hsd.memory.bus_tline.BusTLine.single_ended_z0_str "Link to this definition")


---

<!-- === 来源: reference/hsd/memory/ddr_controller.md === -->

# Memory Controller[](#memory-controller "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.controller.IbisController[](#keysight.ads.hsd.memory.controller.IbisController "Link to this definition")
:   Bases: `Controller`

    The Controller with IBIS class.

    *property* component*: str*[](#keysight.ads.hsd.memory.controller.IbisController.component "Link to this definition")
    :   Property that retrieves the IBIS component name.

        Returns:
        :   The name of the IBIS component.

        Return type:
        :   str

    *property* component\_list*: list[str]*[](#keysight.ads.hsd.memory.controller.IbisController.component_list "Link to this definition")
    :   Property that retrieves the list of IBIS components.

        Returns:
        :   List of available IBIS components.

        Return type:
        :   list[str]

    *property* data\_mode*: str*[](#keysight.ads.hsd.memory.controller.IbisController.data_mode "Link to this definition")

    *property* dbi\_mode*: str*[](#keysight.ads.hsd.memory.controller.IbisController.dbi_mode "Link to this definition")
    :   Get the DBI mode.

        Returns:
        :   DBI mode.

        Return type:
        :   str

    *property* delay\_file*: str*[](#keysight.ads.hsd.memory.controller.IbisController.delay_file "Link to this definition")

    *property* die\_mode*: bool*[](#keysight.ads.hsd.memory.controller.IbisController.die_mode "Link to this definition")
    :   Get the die mode.

        Returns:
        :   Die mode.

        Return type:
        :   bool

    *property* enable\_dbi*: str*[](#keysight.ads.hsd.memory.controller.IbisController.enable_dbi "Link to this definition")
    :   Get the enable DBI.

        Returns:
        :   Enable DBI.

        Return type:
        :   str

    *property* file*: Path*[](#keysight.ads.hsd.memory.controller.IbisController.file "Link to this definition")
    :   Gets the IBIS file for the Controller with IBIS.

        Returns:
        :   The IBIS file.

        Return type:
        :   str

    get\_ref\_table\_ibis\_files\_exist\_error\_msg() → str[](#keysight.ads.hsd.memory.controller.IbisController.get_ref_table_ibis_files_exist_error_msg "Link to this definition")

    *property* ground*: GndCombo*[](#keysight.ads.hsd.memory.controller.IbisController.ground "Link to this definition")

    *property* group\_power\_pins*: bool*[](#keysight.ads.hsd.memory.controller.IbisController.group_power_pins "Link to this definition")

    *property* group\_vss\_pins*: bool*[](#keysight.ads.hsd.memory.controller.IbisController.group_vss_pins "Link to this definition")

    *property* ibis\_vdc*: str*[](#keysight.ads.hsd.memory.controller.IbisController.ibis_vdc "Link to this definition")
    :   Property that retrieves the IBIS VDC.

        Returns:
        :   The IBIS VDC.

        Return type:
        :   str

    include\_ref\_des(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.IbisController.include_ref_des "Link to this definition")

    *property* initialize\_ref\_des\_from*: str*[](#keysight.ads.hsd.memory.controller.IbisController.initialize_ref_des_from "Link to this definition")
    :   Get the reference designator initialization source.

        Returns:
        :   Reference designator initialization source.

        Return type:
        :   str

    is\_any\_ibis\_model() → bool[](#keysight.ads.hsd.memory.controller.IbisController.is_any_ibis_model "Link to this definition")
    :   Check if the model type is any IBIS.

        Returns:
        :   True if the model type is IBIS, False otherwise.

        Return type:
        :   bool

    *property* is\_ddr\_simulation\_mode*: bool*[](#keysight.ads.hsd.memory.controller.IbisController.is_ddr_simulation_mode "Link to this definition")

    *property* match\_channel\_id*: bool*[](#keysight.ads.hsd.memory.controller.IbisController.match_channel_id "Link to this definition")

    *property* match\_mode*: str*[](#keysight.ads.hsd.memory.controller.IbisController.match_mode "Link to this definition")

    *property* number\_of\_pins*: str*[](#keysight.ads.hsd.memory.controller.IbisController.number_of_pins "Link to this definition")

    *property* number\_of\_pins\_per\_ref\_des*: int*[](#keysight.ads.hsd.memory.controller.IbisController.number_of_pins_per_ref_des "Link to this definition")

    *property* package*: [PackageSetup](io_component.md#keysight.ads.hsd.memory.io_component.PackageSetup "keysight.ads.hsd._common.io_component.PackageSetup")*[](#keysight.ads.hsd.memory.controller.IbisController.package "Link to this definition")
    :   Property that retrieves the package setup.

        Returns:
        :   The package setup for the IBIS model.

        Return type:
        :   PackageSetup

    *abstract property* pin*: [SignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.SignalDataCollection "keysight.ads.hsd._common.io_component.SignalDataCollection")*[](#keysight.ads.hsd.memory.controller.IbisController.pin "Link to this definition")
    :   Access the signal data.

        Individual signal data can be accessed as follows:
        `` `[<ref_des>, <pin_name>]` `` where ref\_des is the reference designator and pin\_name is the pin name.
        `` `[SignalProperty]` `` where SignalProperty(channel\_id, ref\_des, signal\_type, signal\_index) is the signal info.
        `` `[<index>]` `` where index is the index of the signal.

        Returns:
        :   **SignalDataCollection**

        Return type:
        :   The signal data collection.

    *property* power*: PowerCombo*[](#keysight.ads.hsd.memory.controller.IbisController.power "Link to this definition")

    *property* power\_mode*: str*[](#keysight.ads.hsd.memory.controller.IbisController.power_mode "Link to this definition")

    *property* power\_node*: str*[](#keysight.ads.hsd.memory.controller.IbisController.power_node "Link to this definition")

    print\_ebd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.IbisController.print_ebd_ref_des_info "Link to this definition")
    :   Prints the EBD reference resignator info.

        Return type:
        :   None

    print\_emd\_pin\_data() → None[](#keysight.ads.hsd.memory.controller.IbisController.print_emd_pin_data "Link to this definition")
    :   Prints the EMD pin data.

        Return type:
        :   None

    print\_emd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.IbisController.print_emd_ref_des_info "Link to this definition")
    :   Prints the EMD reference designator info.

        Return type:
        :   None

    print\_enabled\_ebd\_node\_data() → None[](#keysight.ads.hsd.memory.controller.IbisController.print_enabled_ebd_node_data "Link to this definition")
    :   Prints the EBD pin data.

        Return type:
        :   None

    print\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.IbisController.print_ref_des_info "Link to this definition")
    :   Prints the reference designator info for the DDR Controller.

        Return type:
        :   None

    print\_signal\_data() → None[](#keysight.ads.hsd.memory.controller.IbisController.print_signal_data "Link to this definition")
    :   Prints the signal data.

        Return type:
        :   None

    *property* read\_delay\_file*: bool*[](#keysight.ads.hsd.memory.controller.IbisController.read_delay_file "Link to this definition")

    *abstract property* ref\_des*: [RefDesInfoCollection](io_component.md#keysight.ads.hsd.memory.io_component.RefDesInfoCollection "keysight.ads.hsd._common.io_component.RefDesInfoCollection")*[](#keysight.ads.hsd.memory.controller.IbisController.ref_des "Link to this definition")
    :   Access the reference designator info.

        Individual reference data can be accessed as follows:
        `` `[<ref_des>]` `` where ref\_des is the reference designator.

        Returns:
        :   **RefDesInfoCollection**

        Return type:
        :   The reference designator info collection.

    save() → None[](#keysight.ads.hsd.memory.controller.IbisController.save "Link to this definition")
    :   Save the current settings to the instance.

        Return type:
        :   None

    set\_dq\_combo\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.IbisController.set_dq_combo_index "Link to this definition")

    set\_parser(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.IbisController.set_parser "Link to this definition")

    set\_ref\_table\_clk\_offset(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.IbisController.set_ref_table_clk_offset "Link to this definition")

    set\_ref\_table\_dq\_multiplier(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.IbisController.set_ref_table_dq_multiplier "Link to this definition")

    set\_ref\_table\_dram(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.IbisController.set_ref_table_dram "Link to this definition")

    set\_signal\_channel\_id(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.IbisController.set_signal_channel_id "Link to this definition")

    set\_signal\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.IbisController.set_signal_index "Link to this definition")

    set\_signal\_sim(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.IbisController.set_signal_sim "Link to this definition")

    set\_signal\_type(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.IbisController.set_signal_type "Link to this definition")

    *property* tdqs*: bool*[](#keysight.ads.hsd.memory.controller.IbisController.tdqs "Link to this definition")

    *property* user\_defined\_ref\_des*: list[str]*[](#keysight.ads.hsd.memory.controller.IbisController.user_defined_ref_des "Link to this definition")
    :   Get the user defined reference designators.

        Returns:
        :   User defined reference designators.

        Return type:
        :   list[str]

    *property* vrm\_l*: str*[](#keysight.ads.hsd.memory.controller.IbisController.vrm_l "Link to this definition")

    *property* vrm\_r*: str*[](#keysight.ads.hsd.memory.controller.IbisController.vrm_r "Link to this definition")

    *property* vrm\_vdc*: str*[](#keysight.ads.hsd.memory.controller.IbisController.vrm_vdc "Link to this definition")

*class* keysight.ads.hsd.memory.controller.NonIbisController[](#keysight.ads.hsd.memory.controller.NonIbisController "Link to this definition")
:   Bases: `Controller`

    The Controller without IBIS class.

    *property* component*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.component "Link to this definition")
    :   Property that retrieves the IBIS component name.

        Returns:
        :   The name of the IBIS component.

        Return type:
        :   str

    *property* component\_list*: list[str]*[](#keysight.ads.hsd.memory.controller.NonIbisController.component_list "Link to this definition")
    :   Property that retrieves the list of IBIS components.

        Returns:
        :   List of available IBIS components.

        Return type:
        :   list[str]

    *property* data\_mode*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.data_mode "Link to this definition")

    *property* dbi\_mode*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.dbi_mode "Link to this definition")
    :   Get the DBI mode.

        Returns:
        :   DBI mode.

        Return type:
        :   str

    *property* delay\_file*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.delay_file "Link to this definition")

    *property* die\_mode*: bool*[](#keysight.ads.hsd.memory.controller.NonIbisController.die_mode "Link to this definition")
    :   Get the die mode.

        Returns:
        :   Die mode.

        Return type:
        :   bool

    *property* enable\_dbi*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.enable_dbi "Link to this definition")
    :   Get the enable DBI.

        Returns:
        :   Enable DBI.

        Return type:
        :   str

    get\_ref\_table\_ibis\_files\_exist\_error\_msg() → str[](#keysight.ads.hsd.memory.controller.NonIbisController.get_ref_table_ibis_files_exist_error_msg "Link to this definition")

    *property* ground*: GndCombo*[](#keysight.ads.hsd.memory.controller.NonIbisController.ground "Link to this definition")

    *property* group\_power\_pins*: bool*[](#keysight.ads.hsd.memory.controller.NonIbisController.group_power_pins "Link to this definition")

    *property* group\_vss\_pins*: bool*[](#keysight.ads.hsd.memory.controller.NonIbisController.group_vss_pins "Link to this definition")

    *property* ibis\_vdc*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.ibis_vdc "Link to this definition")
    :   Property that retrieves the IBIS VDC.

        Returns:
        :   The IBIS VDC.

        Return type:
        :   str

    include\_ref\_des(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.NonIbisController.include_ref_des "Link to this definition")

    *property* initialize\_ref\_des\_from*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.initialize_ref_des_from "Link to this definition")
    :   Get the reference designator initialization source.

        Returns:
        :   Reference designator initialization source.

        Return type:
        :   str

    is\_any\_ibis\_model() → bool[](#keysight.ads.hsd.memory.controller.NonIbisController.is_any_ibis_model "Link to this definition")
    :   Check if the model type is any IBIS.

        Returns:
        :   True if the model type is IBIS, False otherwise.

        Return type:
        :   bool

    *property* is\_ddr\_simulation\_mode*: bool*[](#keysight.ads.hsd.memory.controller.NonIbisController.is_ddr_simulation_mode "Link to this definition")

    *property* match\_channel\_id*: bool*[](#keysight.ads.hsd.memory.controller.NonIbisController.match_channel_id "Link to this definition")

    *property* match\_mode*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.match_mode "Link to this definition")

    *property* number\_of\_pins*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.number_of_pins "Link to this definition")

    *property* number\_of\_pins\_per\_ref\_des*: int*[](#keysight.ads.hsd.memory.controller.NonIbisController.number_of_pins_per_ref_des "Link to this definition")

    *property* package*: [PackageSetup](io_component.md#keysight.ads.hsd.memory.io_component.PackageSetup "keysight.ads.hsd._common.io_component.PackageSetup")*[](#keysight.ads.hsd.memory.controller.NonIbisController.package "Link to this definition")
    :   Property that retrieves the package setup.

        Returns:
        :   The package setup for the IBIS model.

        Return type:
        :   PackageSetup

    *abstract property* pin*: [SignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.SignalDataCollection "keysight.ads.hsd._common.io_component.SignalDataCollection")*[](#keysight.ads.hsd.memory.controller.NonIbisController.pin "Link to this definition")
    :   Access the signal data.

        Individual signal data can be accessed as follows:
        `` `[<ref_des>, <pin_name>]` `` where ref\_des is the reference designator and pin\_name is the pin name.
        `` `[SignalProperty]` `` where SignalProperty(channel\_id, ref\_des, signal\_type, signal\_index) is the signal info.
        `` `[<index>]` `` where index is the index of the signal.

        Returns:
        :   **SignalDataCollection**

        Return type:
        :   The signal data collection.

    *property* power*: PowerCombo*[](#keysight.ads.hsd.memory.controller.NonIbisController.power "Link to this definition")

    *property* power\_mode*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.power_mode "Link to this definition")

    *property* power\_node*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.power_node "Link to this definition")

    print\_ebd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.NonIbisController.print_ebd_ref_des_info "Link to this definition")
    :   Prints the EBD reference resignator info.

        Return type:
        :   None

    print\_emd\_pin\_data() → None[](#keysight.ads.hsd.memory.controller.NonIbisController.print_emd_pin_data "Link to this definition")
    :   Prints the EMD pin data.

        Return type:
        :   None

    print\_emd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.NonIbisController.print_emd_ref_des_info "Link to this definition")
    :   Prints the EMD reference designator info.

        Return type:
        :   None

    print\_enabled\_ebd\_node\_data() → None[](#keysight.ads.hsd.memory.controller.NonIbisController.print_enabled_ebd_node_data "Link to this definition")
    :   Prints the EBD pin data.

        Return type:
        :   None

    print\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.NonIbisController.print_ref_des_info "Link to this definition")
    :   Prints the reference designator info for the DDR Controller.

        Return type:
        :   None

    print\_signal\_data() → None[](#keysight.ads.hsd.memory.controller.NonIbisController.print_signal_data "Link to this definition")
    :   Prints the signal data.

        Return type:
        :   None

    *property* read\_delay\_file*: bool*[](#keysight.ads.hsd.memory.controller.NonIbisController.read_delay_file "Link to this definition")

    *abstract property* ref\_des*: [RefDesInfoCollection](io_component.md#keysight.ads.hsd.memory.io_component.RefDesInfoCollection "keysight.ads.hsd._common.io_component.RefDesInfoCollection")*[](#keysight.ads.hsd.memory.controller.NonIbisController.ref_des "Link to this definition")
    :   Access the reference designator info.

        Individual reference data can be accessed as follows:
        `` `[<ref_des>]` `` where ref\_des is the reference designator.

        Returns:
        :   **RefDesInfoCollection**

        Return type:
        :   The reference designator info collection.

    save() → None[](#keysight.ads.hsd.memory.controller.NonIbisController.save "Link to this definition")
    :   Save the current settings to the instance.

        Return type:
        :   None

    set\_dq\_combo\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.NonIbisController.set_dq_combo_index "Link to this definition")

    set\_parser(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.NonIbisController.set_parser "Link to this definition")

    set\_ref\_table\_clk\_offset(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.NonIbisController.set_ref_table_clk_offset "Link to this definition")

    set\_ref\_table\_dq\_multiplier(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.NonIbisController.set_ref_table_dq_multiplier "Link to this definition")

    set\_ref\_table\_dram(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.NonIbisController.set_ref_table_dram "Link to this definition")

    set\_signal\_channel\_id(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.NonIbisController.set_signal_channel_id "Link to this definition")

    set\_signal\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.NonIbisController.set_signal_index "Link to this definition")

    set\_signal\_sim(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.NonIbisController.set_signal_sim "Link to this definition")

    set\_signal\_type(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.NonIbisController.set_signal_type "Link to this definition")

    *property* tdqs*: bool*[](#keysight.ads.hsd.memory.controller.NonIbisController.tdqs "Link to this definition")

    *property* user\_defined\_ref\_des*: list[str]*[](#keysight.ads.hsd.memory.controller.NonIbisController.user_defined_ref_des "Link to this definition")
    :   Get the user defined reference designators.

        Returns:
        :   User defined reference designators.

        Return type:
        :   list[str]

    *property* vrm\_l*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.vrm_l "Link to this definition")

    *property* vrm\_r*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.vrm_r "Link to this definition")

    *property* vrm\_vdc*: str*[](#keysight.ads.hsd.memory.controller.NonIbisController.vrm_vdc "Link to this definition")

*class* keysight.ads.hsd.memory.controller.EbdController[](#keysight.ads.hsd.memory.controller.EbdController "Link to this definition")
:   Bases: `Controller`

    The EBD Controller class.

    *property* component*: str*[](#keysight.ads.hsd.memory.controller.EbdController.component "Link to this definition")
    :   Property that retrieves the IBIS component name.

        Returns:
        :   The name of the IBIS component.

        Return type:
        :   str

    *property* component\_list*: list[str]*[](#keysight.ads.hsd.memory.controller.EbdController.component_list "Link to this definition")
    :   Property that retrieves the list of IBIS components.

        Returns:
        :   List of available IBIS components.

        Return type:
        :   list[str]

    *property* data\_mode*: str*[](#keysight.ads.hsd.memory.controller.EbdController.data_mode "Link to this definition")

    *property* dbi\_mode*: str*[](#keysight.ads.hsd.memory.controller.EbdController.dbi_mode "Link to this definition")
    :   Get the DBI mode.

        Returns:
        :   DBI mode.

        Return type:
        :   str

    *property* delay\_file*: str*[](#keysight.ads.hsd.memory.controller.EbdController.delay_file "Link to this definition")

    *property* die\_mode*: bool*[](#keysight.ads.hsd.memory.controller.EbdController.die_mode "Link to this definition")
    :   Get the die mode.

        Returns:
        :   Die mode.

        Return type:
        :   bool

    *property* enable\_dbi*: str*[](#keysight.ads.hsd.memory.controller.EbdController.enable_dbi "Link to this definition")
    :   Get the enable DBI.

        Returns:
        :   Enable DBI.

        Return type:
        :   str

    *property* file*: Path*[](#keysight.ads.hsd.memory.controller.EbdController.file "Link to this definition")
    :   Gets the EBD file for the Controller with EBD.

        Returns:
        :   The EBD file.

        Return type:
        :   str

    get\_ref\_table\_ibis\_files\_exist\_error\_msg() → str[](#keysight.ads.hsd.memory.controller.EbdController.get_ref_table_ibis_files_exist_error_msg "Link to this definition")

    *property* ground*: GndCombo*[](#keysight.ads.hsd.memory.controller.EbdController.ground "Link to this definition")

    *property* group\_power\_pins*: bool*[](#keysight.ads.hsd.memory.controller.EbdController.group_power_pins "Link to this definition")

    *property* group\_vss\_pins*: bool*[](#keysight.ads.hsd.memory.controller.EbdController.group_vss_pins "Link to this definition")

    *property* ibis\_vdc*: str*[](#keysight.ads.hsd.memory.controller.EbdController.ibis_vdc "Link to this definition")
    :   Property that retrieves the IBIS VDC.

        Returns:
        :   The IBIS VDC.

        Return type:
        :   str

    include\_ref\_des(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EbdController.include_ref_des "Link to this definition")

    *property* initialize\_ref\_des\_from*: str*[](#keysight.ads.hsd.memory.controller.EbdController.initialize_ref_des_from "Link to this definition")
    :   Get the reference designator initialization source.

        Returns:
        :   Reference designator initialization source.

        Return type:
        :   str

    is\_any\_ibis\_model() → bool[](#keysight.ads.hsd.memory.controller.EbdController.is_any_ibis_model "Link to this definition")
    :   Check if the model type is any IBIS.

        Returns:
        :   True if the model type is IBIS, False otherwise.

        Return type:
        :   bool

    *property* is\_ddr\_simulation\_mode*: bool*[](#keysight.ads.hsd.memory.controller.EbdController.is_ddr_simulation_mode "Link to this definition")

    *property* match\_channel\_id*: bool*[](#keysight.ads.hsd.memory.controller.EbdController.match_channel_id "Link to this definition")

    *property* match\_mode*: str*[](#keysight.ads.hsd.memory.controller.EbdController.match_mode "Link to this definition")

    *property* number\_of\_pins*: str*[](#keysight.ads.hsd.memory.controller.EbdController.number_of_pins "Link to this definition")

    *property* number\_of\_pins\_per\_ref\_des*: int*[](#keysight.ads.hsd.memory.controller.EbdController.number_of_pins_per_ref_des "Link to this definition")

    *property* package*: [PackageSetup](io_component.md#keysight.ads.hsd.memory.io_component.PackageSetup "keysight.ads.hsd._common.io_component.PackageSetup")*[](#keysight.ads.hsd.memory.controller.EbdController.package "Link to this definition")
    :   Property that retrieves the package setup.

        Returns:
        :   The package setup for the IBIS model.

        Return type:
        :   PackageSetup

    *property* pin*: [EbdSignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection "keysight.ads.hsd._common.io_component.EbdSignalDataCollection")*[](#keysight.ads.hsd.memory.controller.EbdController.pin "Link to this definition")
    :   Gets the pin data from the EBD file.

        Returns:
        :   The pin data from the EBD file.

        Return type:
        :   [EbdSignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection "keysight.ads.hsd.memory.io_component.EbdSignalDataCollection")

    *property* power*: PowerCombo*[](#keysight.ads.hsd.memory.controller.EbdController.power "Link to this definition")

    *property* power\_mode*: str*[](#keysight.ads.hsd.memory.controller.EbdController.power_mode "Link to this definition")

    *property* power\_node*: str*[](#keysight.ads.hsd.memory.controller.EbdController.power_node "Link to this definition")

    print\_ebd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.EbdController.print_ebd_ref_des_info "Link to this definition")
    :   Prints the EBD reference resignator info.

        Return type:
        :   None

    print\_emd\_pin\_data() → None[](#keysight.ads.hsd.memory.controller.EbdController.print_emd_pin_data "Link to this definition")
    :   Prints the EMD pin data.

        Return type:
        :   None

    print\_emd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.EbdController.print_emd_ref_des_info "Link to this definition")
    :   Prints the EMD reference designator info.

        Return type:
        :   None

    print\_enabled\_ebd\_node\_data() → None[](#keysight.ads.hsd.memory.controller.EbdController.print_enabled_ebd_node_data "Link to this definition")
    :   Prints the EBD pin data.

        Return type:
        :   None

    print\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.EbdController.print_ref_des_info "Link to this definition")
    :   Prints the reference designator info for the DDR Controller.

        Return type:
        :   None

    print\_signal\_data() → None[](#keysight.ads.hsd.memory.controller.EbdController.print_signal_data "Link to this definition")
    :   Prints the signal data.

        Return type:
        :   None

    *property* read\_delay\_file*: bool*[](#keysight.ads.hsd.memory.controller.EbdController.read_delay_file "Link to this definition")

    *property* ref\_des*: [EbdRefDesInfoCollection](io_component.md#keysight.ads.hsd.memory.io_component.EbdRefDesInfoCollection "keysight.ads.hsd._common.io_component.EbdRefDesInfoCollection")*[](#keysight.ads.hsd.memory.controller.EbdController.ref_des "Link to this definition")
    :   Access the reference designator info.

        Individual reference data can be accessed as follows:
        `` `[<ref_des>]` `` where ref\_des is the reference designator.

        Returns:
        :   **RefDesInfoCollection**

        Return type:
        :   The reference designator info collection.

    save() → None[](#keysight.ads.hsd.memory.controller.EbdController.save "Link to this definition")
    :   Save the current settings to the instance.

        Return type:
        :   None

    set\_dq\_combo\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EbdController.set_dq_combo_index "Link to this definition")

    set\_parser(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EbdController.set_parser "Link to this definition")

    set\_ref\_table\_clk\_offset(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EbdController.set_ref_table_clk_offset "Link to this definition")

    set\_ref\_table\_dq\_multiplier(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EbdController.set_ref_table_dq_multiplier "Link to this definition")

    set\_ref\_table\_dram(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EbdController.set_ref_table_dram "Link to this definition")

    set\_signal\_channel\_id(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EbdController.set_signal_channel_id "Link to this definition")

    set\_signal\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EbdController.set_signal_index "Link to this definition")

    set\_signal\_sim(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EbdController.set_signal_sim "Link to this definition")

    set\_signal\_type(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EbdController.set_signal_type "Link to this definition")

    *property* tdqs*: bool*[](#keysight.ads.hsd.memory.controller.EbdController.tdqs "Link to this definition")

    *property* user\_defined\_ref\_des*: list[str]*[](#keysight.ads.hsd.memory.controller.EbdController.user_defined_ref_des "Link to this definition")
    :   Get the user defined reference designators.

        Returns:
        :   User defined reference designators.

        Return type:
        :   list[str]

    *property* vrm\_l*: str*[](#keysight.ads.hsd.memory.controller.EbdController.vrm_l "Link to this definition")

    *property* vrm\_r*: str*[](#keysight.ads.hsd.memory.controller.EbdController.vrm_r "Link to this definition")

    *property* vrm\_vdc*: str*[](#keysight.ads.hsd.memory.controller.EbdController.vrm_vdc "Link to this definition")

*class* keysight.ads.hsd.memory.controller.EmdController[](#keysight.ads.hsd.memory.controller.EmdController "Link to this definition")
:   Bases: `Controller`

    The EMD Controller class.

    *property* component*: str*[](#keysight.ads.hsd.memory.controller.EmdController.component "Link to this definition")
    :   Property that retrieves the IBIS component name.

        Returns:
        :   The name of the IBIS component.

        Return type:
        :   str

    *property* component\_list*: list[str]*[](#keysight.ads.hsd.memory.controller.EmdController.component_list "Link to this definition")
    :   Property that retrieves the list of IBIS components.

        Returns:
        :   List of available IBIS components.

        Return type:
        :   list[str]

    *property* data\_mode*: str*[](#keysight.ads.hsd.memory.controller.EmdController.data_mode "Link to this definition")

    *property* dbi\_mode*: str*[](#keysight.ads.hsd.memory.controller.EmdController.dbi_mode "Link to this definition")
    :   Get the DBI mode.

        Returns:
        :   DBI mode.

        Return type:
        :   str

    *property* delay\_file*: str*[](#keysight.ads.hsd.memory.controller.EmdController.delay_file "Link to this definition")

    *property* die\_mode*: bool*[](#keysight.ads.hsd.memory.controller.EmdController.die_mode "Link to this definition")
    :   Get the die mode.

        Returns:
        :   Die mode.

        Return type:
        :   bool

    *property* enable\_dbi*: str*[](#keysight.ads.hsd.memory.controller.EmdController.enable_dbi "Link to this definition")
    :   Get the enable DBI.

        Returns:
        :   Enable DBI.

        Return type:
        :   str

    *property* file*: Path*[](#keysight.ads.hsd.memory.controller.EmdController.file "Link to this definition")
    :   Gets the EMD file for the Controller with EMD.

        Returns:
        :   The EMD file.

        Return type:
        :   str

    get\_ref\_table\_ibis\_files\_exist\_error\_msg() → str[](#keysight.ads.hsd.memory.controller.EmdController.get_ref_table_ibis_files_exist_error_msg "Link to this definition")

    *property* ground*: GndCombo*[](#keysight.ads.hsd.memory.controller.EmdController.ground "Link to this definition")

    *property* group\_power\_pins*: bool*[](#keysight.ads.hsd.memory.controller.EmdController.group_power_pins "Link to this definition")

    *property* group\_vss\_pins*: bool*[](#keysight.ads.hsd.memory.controller.EmdController.group_vss_pins "Link to this definition")

    *property* ibis\_vdc*: str*[](#keysight.ads.hsd.memory.controller.EmdController.ibis_vdc "Link to this definition")
    :   Property that retrieves the IBIS VDC.

        Returns:
        :   The IBIS VDC.

        Return type:
        :   str

    include\_ref\_des(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EmdController.include_ref_des "Link to this definition")

    *property* initialize\_ref\_des\_from*: str*[](#keysight.ads.hsd.memory.controller.EmdController.initialize_ref_des_from "Link to this definition")
    :   Get the reference designator initialization source.

        Returns:
        :   Reference designator initialization source.

        Return type:
        :   str

    is\_any\_ibis\_model() → bool[](#keysight.ads.hsd.memory.controller.EmdController.is_any_ibis_model "Link to this definition")
    :   Check if the model type is any IBIS.

        Returns:
        :   True if the model type is IBIS, False otherwise.

        Return type:
        :   bool

    *property* is\_ddr\_simulation\_mode*: bool*[](#keysight.ads.hsd.memory.controller.EmdController.is_ddr_simulation_mode "Link to this definition")

    *property* match\_channel\_id*: bool*[](#keysight.ads.hsd.memory.controller.EmdController.match_channel_id "Link to this definition")

    *property* match\_mode*: str*[](#keysight.ads.hsd.memory.controller.EmdController.match_mode "Link to this definition")

    *property* number\_of\_pins*: str*[](#keysight.ads.hsd.memory.controller.EmdController.number_of_pins "Link to this definition")

    *property* number\_of\_pins\_per\_ref\_des*: int*[](#keysight.ads.hsd.memory.controller.EmdController.number_of_pins_per_ref_des "Link to this definition")

    *property* package*: [PackageSetup](io_component.md#keysight.ads.hsd.memory.io_component.PackageSetup "keysight.ads.hsd._common.io_component.PackageSetup")*[](#keysight.ads.hsd.memory.controller.EmdController.package "Link to this definition")
    :   Property that retrieves the package setup.

        Returns:
        :   The package setup for the IBIS model.

        Return type:
        :   PackageSetup

    *property* pin*: [EmdSignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection "keysight.ads.hsd._common.io_component.EmdSignalDataCollection")*[](#keysight.ads.hsd.memory.controller.EmdController.pin "Link to this definition")
    :   Gets the pin data from the EMD file.

        Returns:
        :   The pin data from the EMD file.

        Return type:
        :   [EmdSignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection "keysight.ads.hsd.memory.io_component.EmdSignalDataCollection")

    *property* power*: PowerCombo*[](#keysight.ads.hsd.memory.controller.EmdController.power "Link to this definition")

    *property* power\_mode*: str*[](#keysight.ads.hsd.memory.controller.EmdController.power_mode "Link to this definition")

    *property* power\_node*: str*[](#keysight.ads.hsd.memory.controller.EmdController.power_node "Link to this definition")

    print\_ebd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.EmdController.print_ebd_ref_des_info "Link to this definition")
    :   Prints the EBD reference resignator info.

        Return type:
        :   None

    print\_emd\_pin\_data() → None[](#keysight.ads.hsd.memory.controller.EmdController.print_emd_pin_data "Link to this definition")
    :   Prints the EMD pin data.

        Return type:
        :   None

    print\_emd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.EmdController.print_emd_ref_des_info "Link to this definition")
    :   Prints the EMD reference designator info.

        Return type:
        :   None

    print\_enabled\_ebd\_node\_data() → None[](#keysight.ads.hsd.memory.controller.EmdController.print_enabled_ebd_node_data "Link to this definition")
    :   Prints the EBD pin data.

        Return type:
        :   None

    print\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.controller.EmdController.print_ref_des_info "Link to this definition")
    :   Prints the reference designator info for the DDR Controller.

        Return type:
        :   None

    print\_signal\_data() → None[](#keysight.ads.hsd.memory.controller.EmdController.print_signal_data "Link to this definition")
    :   Prints the signal data.

        Return type:
        :   None

    *property* read\_delay\_file*: bool*[](#keysight.ads.hsd.memory.controller.EmdController.read_delay_file "Link to this definition")

    *property* ref\_des*: [EmdRefDesInfoCollection](io_component.md#keysight.ads.hsd.memory.io_component.EmdRefDesInfoCollection "keysight.ads.hsd._common.io_component.EmdRefDesInfoCollection")*[](#keysight.ads.hsd.memory.controller.EmdController.ref_des "Link to this definition")
    :   Access the reference designator info.

        Individual reference data can be accessed as follows:
        `` `[<ref_des>]` `` where ref\_des is the reference designator.

        Returns:
        :   **RefDesInfoCollection**

        Return type:
        :   The reference designator info collection.

    save() → None[](#keysight.ads.hsd.memory.controller.EmdController.save "Link to this definition")
    :   Save the current settings to the instance.

        Return type:
        :   None

    set\_dq\_combo\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EmdController.set_dq_combo_index "Link to this definition")

    set\_parser(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EmdController.set_parser "Link to this definition")

    set\_ref\_table\_clk\_offset(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EmdController.set_ref_table_clk_offset "Link to this definition")

    set\_ref\_table\_dq\_multiplier(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EmdController.set_ref_table_dq_multiplier "Link to this definition")

    set\_ref\_table\_dram(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EmdController.set_ref_table_dram "Link to this definition")

    set\_signal\_channel\_id(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EmdController.set_signal_channel_id "Link to this definition")

    set\_signal\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EmdController.set_signal_index "Link to this definition")

    set\_signal\_sim(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EmdController.set_signal_sim "Link to this definition")

    set\_signal\_type(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.controller.EmdController.set_signal_type "Link to this definition")

    *property* tdqs*: bool*[](#keysight.ads.hsd.memory.controller.EmdController.tdqs "Link to this definition")

    *property* user\_defined\_ref\_des*: list[str]*[](#keysight.ads.hsd.memory.controller.EmdController.user_defined_ref_des "Link to this definition")
    :   Get the user defined reference designators.

        Returns:
        :   User defined reference designators.

        Return type:
        :   list[str]

    *property* vrm\_l*: str*[](#keysight.ads.hsd.memory.controller.EmdController.vrm_l "Link to this definition")

    *property* vrm\_r*: str*[](#keysight.ads.hsd.memory.controller.EmdController.vrm_r "Link to this definition")

    *property* vrm\_vdc*: str*[](#keysight.ads.hsd.memory.controller.EmdController.vrm_vdc "Link to this definition")


---

<!-- === 来源: reference/hsd/memory/ddr_memory.md === -->

# Memory DRAM[](#memory-dram "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.memory.IbisMemory[](#keysight.ads.hsd.memory.memory.IbisMemory "Link to this definition")
:   Bases: `Memory`

    The Memory with IBIS class.

    *property* component*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.component "Link to this definition")
    :   Property that retrieves the IBIS component name.

        Returns:
        :   The name of the IBIS component.

        Return type:
        :   str

    *property* component\_list*: list[str]*[](#keysight.ads.hsd.memory.memory.IbisMemory.component_list "Link to this definition")
    :   Property that retrieves the list of IBIS components.

        Returns:
        :   List of available IBIS components.

        Return type:
        :   list[str]

    *property* data\_mode*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.data_mode "Link to this definition")

    *property* dbi\_mode*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.dbi_mode "Link to this definition")
    :   Get the DBI mode.

        Returns:
        :   DBI mode.

        Return type:
        :   str

    *property* delay\_file*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.delay_file "Link to this definition")

    *property* die\_mode*: bool*[](#keysight.ads.hsd.memory.memory.IbisMemory.die_mode "Link to this definition")
    :   Get the die mode.

        Returns:
        :   Die mode.

        Return type:
        :   bool

    *property* enable\_dbi*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.enable_dbi "Link to this definition")
    :   Get the enable DBI.

        Returns:
        :   Enable DBI.

        Return type:
        :   str

    *property* file*: Path*[](#keysight.ads.hsd.memory.memory.IbisMemory.file "Link to this definition")
    :   Gets the IBIS file for the Memory with IBIS.

        Returns:
        :   The IBIS file.

        Return type:
        :   str

    get\_ref\_table\_ibis\_files\_exist\_error\_msg() → str[](#keysight.ads.hsd.memory.memory.IbisMemory.get_ref_table_ibis_files_exist_error_msg "Link to this definition")

    *property* ground*: GndCombo*[](#keysight.ads.hsd.memory.memory.IbisMemory.ground "Link to this definition")

    *property* group\_power\_pins*: bool*[](#keysight.ads.hsd.memory.memory.IbisMemory.group_power_pins "Link to this definition")

    *property* group\_vss\_pins*: bool*[](#keysight.ads.hsd.memory.memory.IbisMemory.group_vss_pins "Link to this definition")

    *property* ibis\_vdc*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.ibis_vdc "Link to this definition")
    :   Property that retrieves the IBIS VDC.

        Returns:
        :   The IBIS VDC.

        Return type:
        :   str

    include\_ref\_des(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.IbisMemory.include_ref_des "Link to this definition")

    *property* initialize\_ref\_des\_from*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.initialize_ref_des_from "Link to this definition")
    :   Get the reference designator initialization source.

        Returns:
        :   Reference designator initialization source.

        Return type:
        :   str

    is\_any\_ibis\_model() → bool[](#keysight.ads.hsd.memory.memory.IbisMemory.is_any_ibis_model "Link to this definition")
    :   Check if the model type is any IBIS.

        Returns:
        :   True if the model type is IBIS, False otherwise.

        Return type:
        :   bool

    *property* is\_ddr\_simulation\_mode*: bool*[](#keysight.ads.hsd.memory.memory.IbisMemory.is_ddr_simulation_mode "Link to this definition")

    *property* match\_channel\_id*: bool*[](#keysight.ads.hsd.memory.memory.IbisMemory.match_channel_id "Link to this definition")

    *property* match\_mode*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.match_mode "Link to this definition")

    *property* number\_of\_pins*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.number_of_pins "Link to this definition")

    *property* number\_of\_pins\_per\_ref\_des*: int*[](#keysight.ads.hsd.memory.memory.IbisMemory.number_of_pins_per_ref_des "Link to this definition")

    *property* package*: [PackageSetup](io_component.md#keysight.ads.hsd.memory.io_component.PackageSetup "keysight.ads.hsd._common.io_component.PackageSetup")*[](#keysight.ads.hsd.memory.memory.IbisMemory.package "Link to this definition")
    :   Property that retrieves the package setup.

        Returns:
        :   The package setup for the IBIS model.

        Return type:
        :   PackageSetup

    *abstract property* pin*: [SignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.SignalDataCollection "keysight.ads.hsd._common.io_component.SignalDataCollection")*[](#keysight.ads.hsd.memory.memory.IbisMemory.pin "Link to this definition")
    :   Access the signal data.

        Individual signal data can be accessed as follows:
        `` `[<ref_des>, <pin_name>]` `` where ref\_des is the reference designator and pin\_name is the pin name.
        `` `[SignalProperty]` `` where SignalProperty(channel\_id, ref\_des, signal\_type, signal\_index) is the signal info.
        `` `[<index>]` `` where index is the index of the signal.

        Returns:
        :   **SignalDataCollection**

        Return type:
        :   The signal data collection.

    *property* power*: PowerCombo*[](#keysight.ads.hsd.memory.memory.IbisMemory.power "Link to this definition")

    *property* power\_mode*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.power_mode "Link to this definition")

    *property* power\_node*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.power_node "Link to this definition")

    print\_ebd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.IbisMemory.print_ebd_ref_des_info "Link to this definition")
    :   Prints the EBD reference resignator info.

        Return type:
        :   None

    print\_emd\_pin\_data() → None[](#keysight.ads.hsd.memory.memory.IbisMemory.print_emd_pin_data "Link to this definition")
    :   Prints the EMD pin data.

        Return type:
        :   None

    print\_emd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.IbisMemory.print_emd_ref_des_info "Link to this definition")
    :   Prints the EMD reference designator info.

        Return type:
        :   None

    print\_enabled\_ebd\_node\_data() → None[](#keysight.ads.hsd.memory.memory.IbisMemory.print_enabled_ebd_node_data "Link to this definition")
    :   Prints the EBD pin data.

        Return type:
        :   None

    print\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.IbisMemory.print_ref_des_info "Link to this definition")
    :   Prints the reference designator info for the DDR Memory.

        Return type:
        :   None

    print\_signal\_data() → None[](#keysight.ads.hsd.memory.memory.IbisMemory.print_signal_data "Link to this definition")
    :   Prints the signal data.

        Return type:
        :   None

    *property* read\_delay\_file*: bool*[](#keysight.ads.hsd.memory.memory.IbisMemory.read_delay_file "Link to this definition")

    *abstract property* ref\_des*: [RefDesInfoCollection](io_component.md#keysight.ads.hsd.memory.io_component.RefDesInfoCollection "keysight.ads.hsd._common.io_component.RefDesInfoCollection")*[](#keysight.ads.hsd.memory.memory.IbisMemory.ref_des "Link to this definition")
    :   Access the reference designator info.

        Individual reference data can be accessed as follows:
        `` `[<ref_des>]` `` where ref\_des is the reference designator.

        Returns:
        :   **RefDesInfoCollection**

        Return type:
        :   The reference designator info collection.

    save() → None[](#keysight.ads.hsd.memory.memory.IbisMemory.save "Link to this definition")
    :   Save the current settings to the instance.

        Return type:
        :   None

    set\_dq\_combo\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.IbisMemory.set_dq_combo_index "Link to this definition")

    set\_parser(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.IbisMemory.set_parser "Link to this definition")

    set\_ref\_table\_clk\_offset(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.IbisMemory.set_ref_table_clk_offset "Link to this definition")

    set\_ref\_table\_dq\_multiplier(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.IbisMemory.set_ref_table_dq_multiplier "Link to this definition")

    set\_ref\_table\_dram(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.IbisMemory.set_ref_table_dram "Link to this definition")

    set\_signal\_channel\_id(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.IbisMemory.set_signal_channel_id "Link to this definition")

    set\_signal\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.IbisMemory.set_signal_index "Link to this definition")

    set\_signal\_sim(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.IbisMemory.set_signal_sim "Link to this definition")

    set\_signal\_type(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.IbisMemory.set_signal_type "Link to this definition")

    *property* tdqs*: bool*[](#keysight.ads.hsd.memory.memory.IbisMemory.tdqs "Link to this definition")

    *property* user\_defined\_ref\_des*: list[str]*[](#keysight.ads.hsd.memory.memory.IbisMemory.user_defined_ref_des "Link to this definition")
    :   Get the user defined reference designators.

        Returns:
        :   User defined reference designators.

        Return type:
        :   list[str]

    *property* vrm\_l*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.vrm_l "Link to this definition")

    *property* vrm\_r*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.vrm_r "Link to this definition")

    *property* vrm\_vdc*: str*[](#keysight.ads.hsd.memory.memory.IbisMemory.vrm_vdc "Link to this definition")

*class* keysight.ads.hsd.memory.memory.NonIbisMemory[](#keysight.ads.hsd.memory.memory.NonIbisMemory "Link to this definition")
:   Bases: `Memory`

    The Non-IBIS Memory class.

    *property* component*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.component "Link to this definition")
    :   Property that retrieves the IBIS component name.

        Returns:
        :   The name of the IBIS component.

        Return type:
        :   str

    *property* component\_list*: list[str]*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.component_list "Link to this definition")
    :   Property that retrieves the list of IBIS components.

        Returns:
        :   List of available IBIS components.

        Return type:
        :   list[str]

    *property* data\_mode*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.data_mode "Link to this definition")

    *property* dbi\_mode*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.dbi_mode "Link to this definition")
    :   Get the DBI mode.

        Returns:
        :   DBI mode.

        Return type:
        :   str

    *property* delay\_file*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.delay_file "Link to this definition")

    *property* die\_mode*: bool*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.die_mode "Link to this definition")
    :   Get the die mode.

        Returns:
        :   Die mode.

        Return type:
        :   bool

    *property* enable\_dbi*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.enable_dbi "Link to this definition")
    :   Get the enable DBI.

        Returns:
        :   Enable DBI.

        Return type:
        :   str

    get\_ref\_table\_ibis\_files\_exist\_error\_msg() → str[](#keysight.ads.hsd.memory.memory.NonIbisMemory.get_ref_table_ibis_files_exist_error_msg "Link to this definition")

    *property* ground*: GndCombo*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.ground "Link to this definition")

    *property* group\_power\_pins*: bool*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.group_power_pins "Link to this definition")

    *property* group\_vss\_pins*: bool*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.group_vss_pins "Link to this definition")

    *property* ibis\_vdc*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.ibis_vdc "Link to this definition")
    :   Property that retrieves the IBIS VDC.

        Returns:
        :   The IBIS VDC.

        Return type:
        :   str

    include\_ref\_des(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.include_ref_des "Link to this definition")

    *property* initialize\_ref\_des\_from*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.initialize_ref_des_from "Link to this definition")
    :   Get the reference designator initialization source.

        Returns:
        :   Reference designator initialization source.

        Return type:
        :   str

    is\_any\_ibis\_model() → bool[](#keysight.ads.hsd.memory.memory.NonIbisMemory.is_any_ibis_model "Link to this definition")
    :   Check if the model type is any IBIS.

        Returns:
        :   True if the model type is IBIS, False otherwise.

        Return type:
        :   bool

    *property* is\_ddr\_simulation\_mode*: bool*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.is_ddr_simulation_mode "Link to this definition")

    *property* match\_channel\_id*: bool*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.match_channel_id "Link to this definition")

    *property* match\_mode*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.match_mode "Link to this definition")

    *property* number\_of\_pins*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.number_of_pins "Link to this definition")

    *property* number\_of\_pins\_per\_ref\_des*: int*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.number_of_pins_per_ref_des "Link to this definition")

    *property* package*: [PackageSetup](io_component.md#keysight.ads.hsd.memory.io_component.PackageSetup "keysight.ads.hsd._common.io_component.PackageSetup")*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.package "Link to this definition")
    :   Property that retrieves the package setup.

        Returns:
        :   The package setup for the IBIS model.

        Return type:
        :   PackageSetup

    *abstract property* pin*: [SignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.SignalDataCollection "keysight.ads.hsd._common.io_component.SignalDataCollection")*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.pin "Link to this definition")
    :   Access the signal data.

        Individual signal data can be accessed as follows:
        `` `[<ref_des>, <pin_name>]` `` where ref\_des is the reference designator and pin\_name is the pin name.
        `` `[SignalProperty]` `` where SignalProperty(channel\_id, ref\_des, signal\_type, signal\_index) is the signal info.
        `` `[<index>]` `` where index is the index of the signal.

        Returns:
        :   **SignalDataCollection**

        Return type:
        :   The signal data collection.

    *property* power*: PowerCombo*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.power "Link to this definition")

    *property* power\_mode*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.power_mode "Link to this definition")

    *property* power\_node*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.power_node "Link to this definition")

    print\_ebd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.print_ebd_ref_des_info "Link to this definition")
    :   Prints the EBD reference resignator info.

        Return type:
        :   None

    print\_emd\_pin\_data() → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.print_emd_pin_data "Link to this definition")
    :   Prints the EMD pin data.

        Return type:
        :   None

    print\_emd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.print_emd_ref_des_info "Link to this definition")
    :   Prints the EMD reference designator info.

        Return type:
        :   None

    print\_enabled\_ebd\_node\_data() → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.print_enabled_ebd_node_data "Link to this definition")
    :   Prints the EBD pin data.

        Return type:
        :   None

    print\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.print_ref_des_info "Link to this definition")
    :   Prints the reference designator info for the DDR Memory.

        Return type:
        :   None

    print\_signal\_data() → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.print_signal_data "Link to this definition")
    :   Prints the signal data.

        Return type:
        :   None

    *property* read\_delay\_file*: bool*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.read_delay_file "Link to this definition")

    *abstract property* ref\_des*: [RefDesInfoCollection](io_component.md#keysight.ads.hsd.memory.io_component.RefDesInfoCollection "keysight.ads.hsd._common.io_component.RefDesInfoCollection")*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.ref_des "Link to this definition")
    :   Access the reference designator info.

        Individual reference data can be accessed as follows:
        `` `[<ref_des>]` `` where ref\_des is the reference designator.

        Returns:
        :   **RefDesInfoCollection**

        Return type:
        :   The reference designator info collection.

    save() → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.save "Link to this definition")
    :   Save the current settings to the instance.

        Return type:
        :   None

    set\_dq\_combo\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.set_dq_combo_index "Link to this definition")

    set\_parser(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.set_parser "Link to this definition")

    set\_ref\_table\_clk\_offset(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.set_ref_table_clk_offset "Link to this definition")

    set\_ref\_table\_dq\_multiplier(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.set_ref_table_dq_multiplier "Link to this definition")

    set\_ref\_table\_dram(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.set_ref_table_dram "Link to this definition")

    set\_signal\_channel\_id(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.set_signal_channel_id "Link to this definition")

    set\_signal\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.set_signal_index "Link to this definition")

    set\_signal\_sim(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.set_signal_sim "Link to this definition")

    set\_signal\_type(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.NonIbisMemory.set_signal_type "Link to this definition")

    *property* tdqs*: bool*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.tdqs "Link to this definition")

    *property* user\_defined\_ref\_des*: list[str]*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.user_defined_ref_des "Link to this definition")
    :   Get the user defined reference designators.

        Returns:
        :   User defined reference designators.

        Return type:
        :   list[str]

    *property* vrm\_l*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.vrm_l "Link to this definition")

    *property* vrm\_r*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.vrm_r "Link to this definition")

    *property* vrm\_vdc*: str*[](#keysight.ads.hsd.memory.memory.NonIbisMemory.vrm_vdc "Link to this definition")

*class* keysight.ads.hsd.memory.memory.EbdMemory[](#keysight.ads.hsd.memory.memory.EbdMemory "Link to this definition")
:   Bases: `Memory`

    The EBD Memory class.

    *property* component*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.component "Link to this definition")
    :   Property that retrieves the IBIS component name.

        Returns:
        :   The name of the IBIS component.

        Return type:
        :   str

    *property* component\_list*: list[str]*[](#keysight.ads.hsd.memory.memory.EbdMemory.component_list "Link to this definition")
    :   Property that retrieves the list of IBIS components.

        Returns:
        :   List of available IBIS components.

        Return type:
        :   list[str]

    *property* data\_mode*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.data_mode "Link to this definition")

    *property* dbi\_mode*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.dbi_mode "Link to this definition")
    :   Get the DBI mode.

        Returns:
        :   DBI mode.

        Return type:
        :   str

    *property* delay\_file*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.delay_file "Link to this definition")

    *property* die\_mode*: bool*[](#keysight.ads.hsd.memory.memory.EbdMemory.die_mode "Link to this definition")
    :   Get the die mode.

        Returns:
        :   Die mode.

        Return type:
        :   bool

    *property* enable\_dbi*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.enable_dbi "Link to this definition")
    :   Get the enable DBI.

        Returns:
        :   Enable DBI.

        Return type:
        :   str

    *property* file*: Path*[](#keysight.ads.hsd.memory.memory.EbdMemory.file "Link to this definition")
    :   Gets the EBD file for the Memory with EBD.

        Returns:
        :   The EBD file.

        Return type:
        :   str

    get\_ref\_table\_ibis\_files\_exist\_error\_msg() → str[](#keysight.ads.hsd.memory.memory.EbdMemory.get_ref_table_ibis_files_exist_error_msg "Link to this definition")

    *property* ground*: GndCombo*[](#keysight.ads.hsd.memory.memory.EbdMemory.ground "Link to this definition")

    *property* group\_power\_pins*: bool*[](#keysight.ads.hsd.memory.memory.EbdMemory.group_power_pins "Link to this definition")

    *property* group\_vss\_pins*: bool*[](#keysight.ads.hsd.memory.memory.EbdMemory.group_vss_pins "Link to this definition")

    *property* ibis\_vdc*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.ibis_vdc "Link to this definition")
    :   Property that retrieves the IBIS VDC.

        Returns:
        :   The IBIS VDC.

        Return type:
        :   str

    include\_ref\_des(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EbdMemory.include_ref_des "Link to this definition")

    *property* initialize\_ref\_des\_from*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.initialize_ref_des_from "Link to this definition")
    :   Get the reference designator initialization source.

        Returns:
        :   Reference designator initialization source.

        Return type:
        :   str

    is\_any\_ibis\_model() → bool[](#keysight.ads.hsd.memory.memory.EbdMemory.is_any_ibis_model "Link to this definition")
    :   Check if the model type is any IBIS.

        Returns:
        :   True if the model type is IBIS, False otherwise.

        Return type:
        :   bool

    *property* is\_ddr\_simulation\_mode*: bool*[](#keysight.ads.hsd.memory.memory.EbdMemory.is_ddr_simulation_mode "Link to this definition")

    *property* match\_channel\_id*: bool*[](#keysight.ads.hsd.memory.memory.EbdMemory.match_channel_id "Link to this definition")

    *property* match\_mode*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.match_mode "Link to this definition")

    *property* number\_of\_pins*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.number_of_pins "Link to this definition")

    *property* number\_of\_pins\_per\_ref\_des*: int*[](#keysight.ads.hsd.memory.memory.EbdMemory.number_of_pins_per_ref_des "Link to this definition")

    *property* package*: [PackageSetup](io_component.md#keysight.ads.hsd.memory.io_component.PackageSetup "keysight.ads.hsd._common.io_component.PackageSetup")*[](#keysight.ads.hsd.memory.memory.EbdMemory.package "Link to this definition")
    :   Property that retrieves the package setup.

        Returns:
        :   The package setup for the IBIS model.

        Return type:
        :   PackageSetup

    *property* pin*: [EbdSignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection "keysight.ads.hsd._common.io_component.EbdSignalDataCollection")*[](#keysight.ads.hsd.memory.memory.EbdMemory.pin "Link to this definition")
    :   Gets the pin data from the EBD file.

        Returns:
        :   The pin data from the EBD file.

        Return type:
        :   [EbdSignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection "keysight.ads.hsd.memory.io_component.EbdSignalDataCollection")

    *property* power*: PowerCombo*[](#keysight.ads.hsd.memory.memory.EbdMemory.power "Link to this definition")

    *property* power\_mode*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.power_mode "Link to this definition")

    *property* power\_node*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.power_node "Link to this definition")

    print\_ebd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.EbdMemory.print_ebd_ref_des_info "Link to this definition")
    :   Prints the EBD reference resignator info.

        Return type:
        :   None

    print\_emd\_pin\_data() → None[](#keysight.ads.hsd.memory.memory.EbdMemory.print_emd_pin_data "Link to this definition")
    :   Prints the EMD pin data.

        Return type:
        :   None

    print\_emd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.EbdMemory.print_emd_ref_des_info "Link to this definition")
    :   Prints the EMD reference designator info.

        Return type:
        :   None

    print\_enabled\_ebd\_node\_data() → None[](#keysight.ads.hsd.memory.memory.EbdMemory.print_enabled_ebd_node_data "Link to this definition")
    :   Prints the EBD pin data.

        Return type:
        :   None

    print\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.EbdMemory.print_ref_des_info "Link to this definition")
    :   Prints the reference designator info for the DDR Memory.

        Return type:
        :   None

    print\_signal\_data() → None[](#keysight.ads.hsd.memory.memory.EbdMemory.print_signal_data "Link to this definition")
    :   Prints the signal data.

        Return type:
        :   None

    *property* read\_delay\_file*: bool*[](#keysight.ads.hsd.memory.memory.EbdMemory.read_delay_file "Link to this definition")

    *property* ref\_des*: [EbdRefDesInfoCollection](io_component.md#keysight.ads.hsd.memory.io_component.EbdRefDesInfoCollection "keysight.ads.hsd._common.io_component.EbdRefDesInfoCollection")*[](#keysight.ads.hsd.memory.memory.EbdMemory.ref_des "Link to this definition")
    :   Access the reference designator info.

        Individual reference data can be accessed as follows:
        `` `[<ref_des>]` `` where ref\_des is the reference designator.

        Returns:
        :   **RefDesInfoCollection**

        Return type:
        :   The reference designator info collection.

    save() → None[](#keysight.ads.hsd.memory.memory.EbdMemory.save "Link to this definition")
    :   Save the current settings to the instance.

        Return type:
        :   None

    set\_dq\_combo\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EbdMemory.set_dq_combo_index "Link to this definition")

    set\_parser(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EbdMemory.set_parser "Link to this definition")

    set\_ref\_table\_clk\_offset(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EbdMemory.set_ref_table_clk_offset "Link to this definition")

    set\_ref\_table\_dq\_multiplier(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EbdMemory.set_ref_table_dq_multiplier "Link to this definition")

    set\_ref\_table\_dram(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EbdMemory.set_ref_table_dram "Link to this definition")

    set\_signal\_channel\_id(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EbdMemory.set_signal_channel_id "Link to this definition")

    set\_signal\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EbdMemory.set_signal_index "Link to this definition")

    set\_signal\_sim(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EbdMemory.set_signal_sim "Link to this definition")

    set\_signal\_type(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EbdMemory.set_signal_type "Link to this definition")

    *property* tdqs*: bool*[](#keysight.ads.hsd.memory.memory.EbdMemory.tdqs "Link to this definition")

    *property* user\_defined\_ref\_des*: list[str]*[](#keysight.ads.hsd.memory.memory.EbdMemory.user_defined_ref_des "Link to this definition")
    :   Get the user defined reference designators.

        Returns:
        :   User defined reference designators.

        Return type:
        :   list[str]

    *property* vrm\_l*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.vrm_l "Link to this definition")

    *property* vrm\_r*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.vrm_r "Link to this definition")

    *property* vrm\_vdc*: str*[](#keysight.ads.hsd.memory.memory.EbdMemory.vrm_vdc "Link to this definition")

*class* keysight.ads.hsd.memory.memory.EmdMemory[](#keysight.ads.hsd.memory.memory.EmdMemory "Link to this definition")
:   Bases: `Memory`

    The EMD Memory class.

    *property* component*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.component "Link to this definition")
    :   Property that retrieves the IBIS component name.

        Returns:
        :   The name of the IBIS component.

        Return type:
        :   str

    *property* component\_list*: list[str]*[](#keysight.ads.hsd.memory.memory.EmdMemory.component_list "Link to this definition")
    :   Property that retrieves the list of IBIS components.

        Returns:
        :   List of available IBIS components.

        Return type:
        :   list[str]

    *property* data\_mode*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.data_mode "Link to this definition")

    *property* dbi\_mode*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.dbi_mode "Link to this definition")
    :   Get the DBI mode.

        Returns:
        :   DBI mode.

        Return type:
        :   str

    *property* delay\_file*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.delay_file "Link to this definition")

    *property* die\_mode*: bool*[](#keysight.ads.hsd.memory.memory.EmdMemory.die_mode "Link to this definition")
    :   Get the die mode.

        Returns:
        :   Die mode.

        Return type:
        :   bool

    *property* enable\_dbi*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.enable_dbi "Link to this definition")
    :   Get the enable DBI.

        Returns:
        :   Enable DBI.

        Return type:
        :   str

    *property* file*: Path*[](#keysight.ads.hsd.memory.memory.EmdMemory.file "Link to this definition")
    :   Gets the EMD file for the Memory with EMD.

        Returns:
        :   The EMD file.

        Return type:
        :   str

    get\_ref\_table\_ibis\_files\_exist\_error\_msg() → str[](#keysight.ads.hsd.memory.memory.EmdMemory.get_ref_table_ibis_files_exist_error_msg "Link to this definition")

    *property* ground*: GndCombo*[](#keysight.ads.hsd.memory.memory.EmdMemory.ground "Link to this definition")

    *property* group\_power\_pins*: bool*[](#keysight.ads.hsd.memory.memory.EmdMemory.group_power_pins "Link to this definition")

    *property* group\_vss\_pins*: bool*[](#keysight.ads.hsd.memory.memory.EmdMemory.group_vss_pins "Link to this definition")

    *property* ibis\_vdc*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.ibis_vdc "Link to this definition")
    :   Property that retrieves the IBIS VDC.

        Returns:
        :   The IBIS VDC.

        Return type:
        :   str

    include\_ref\_des(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EmdMemory.include_ref_des "Link to this definition")

    *property* initialize\_ref\_des\_from*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.initialize_ref_des_from "Link to this definition")
    :   Get the reference designator initialization source.

        Returns:
        :   Reference designator initialization source.

        Return type:
        :   str

    is\_any\_ibis\_model() → bool[](#keysight.ads.hsd.memory.memory.EmdMemory.is_any_ibis_model "Link to this definition")
    :   Check if the model type is any IBIS.

        Returns:
        :   True if the model type is IBIS, False otherwise.

        Return type:
        :   bool

    *property* is\_ddr\_simulation\_mode*: bool*[](#keysight.ads.hsd.memory.memory.EmdMemory.is_ddr_simulation_mode "Link to this definition")

    *property* match\_channel\_id*: bool*[](#keysight.ads.hsd.memory.memory.EmdMemory.match_channel_id "Link to this definition")

    *property* match\_mode*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.match_mode "Link to this definition")

    *property* number\_of\_pins*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.number_of_pins "Link to this definition")

    *property* number\_of\_pins\_per\_ref\_des*: int*[](#keysight.ads.hsd.memory.memory.EmdMemory.number_of_pins_per_ref_des "Link to this definition")

    *property* package*: [PackageSetup](io_component.md#keysight.ads.hsd.memory.io_component.PackageSetup "keysight.ads.hsd._common.io_component.PackageSetup")*[](#keysight.ads.hsd.memory.memory.EmdMemory.package "Link to this definition")
    :   Property that retrieves the package setup.

        Returns:
        :   The package setup for the IBIS model.

        Return type:
        :   PackageSetup

    *property* pin*: [EmdSignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection "keysight.ads.hsd._common.io_component.EmdSignalDataCollection")*[](#keysight.ads.hsd.memory.memory.EmdMemory.pin "Link to this definition")
    :   Gets the pin data from the EMD file.

        Returns:
        :   The pin data from the EMD file.

        Return type:
        :   [EmdSignalDataCollection](io_component.md#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection "keysight.ads.hsd.memory.io_component.EmdSignalDataCollection")

    *property* power*: PowerCombo*[](#keysight.ads.hsd.memory.memory.EmdMemory.power "Link to this definition")

    *property* power\_mode*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.power_mode "Link to this definition")

    *property* power\_node*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.power_node "Link to this definition")

    print\_ebd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.EmdMemory.print_ebd_ref_des_info "Link to this definition")
    :   Prints the EBD reference resignator info.

        Return type:
        :   None

    print\_emd\_pin\_data() → None[](#keysight.ads.hsd.memory.memory.EmdMemory.print_emd_pin_data "Link to this definition")
    :   Prints the EMD pin data.

        Return type:
        :   None

    print\_emd\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.EmdMemory.print_emd_ref_des_info "Link to this definition")
    :   Prints the EMD reference designator info.

        Return type:
        :   None

    print\_enabled\_ebd\_node\_data() → None[](#keysight.ads.hsd.memory.memory.EmdMemory.print_enabled_ebd_node_data "Link to this definition")
    :   Prints the EBD pin data.

        Return type:
        :   None

    print\_ref\_des\_info() → None[](#keysight.ads.hsd.memory.memory.EmdMemory.print_ref_des_info "Link to this definition")
    :   Prints the reference designator info for the DDR Memory.

        Return type:
        :   None

    print\_signal\_data() → None[](#keysight.ads.hsd.memory.memory.EmdMemory.print_signal_data "Link to this definition")
    :   Prints the signal data.

        Return type:
        :   None

    *property* read\_delay\_file*: bool*[](#keysight.ads.hsd.memory.memory.EmdMemory.read_delay_file "Link to this definition")

    *property* ref\_des*: [EmdRefDesInfoCollection](io_component.md#keysight.ads.hsd.memory.io_component.EmdRefDesInfoCollection "keysight.ads.hsd._common.io_component.EmdRefDesInfoCollection")*[](#keysight.ads.hsd.memory.memory.EmdMemory.ref_des "Link to this definition")
    :   Access the reference designator info.

        Individual reference data can be accessed as follows:
        `` `[<ref_des>]` `` where ref\_des is the reference designator.

        Returns:
        :   **RefDesInfoCollection**

        Return type:
        :   The reference designator info collection.

    save() → None[](#keysight.ads.hsd.memory.memory.EmdMemory.save "Link to this definition")
    :   Save the current settings to the instance.

        Return type:
        :   None

    set\_dq\_combo\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EmdMemory.set_dq_combo_index "Link to this definition")

    set\_parser(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EmdMemory.set_parser "Link to this definition")

    set\_ref\_table\_clk\_offset(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EmdMemory.set_ref_table_clk_offset "Link to this definition")

    set\_ref\_table\_dq\_multiplier(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EmdMemory.set_ref_table_dq_multiplier "Link to this definition")

    set\_ref\_table\_dram(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EmdMemory.set_ref_table_dram "Link to this definition")

    set\_signal\_channel\_id(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EmdMemory.set_signal_channel_id "Link to this definition")

    set\_signal\_index(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EmdMemory.set_signal_index "Link to this definition")

    set\_signal\_sim(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EmdMemory.set_signal_sim "Link to this definition")

    set\_signal\_type(*\*args: Any*, *\*\*kwargs: Any*) → None[](#keysight.ads.hsd.memory.memory.EmdMemory.set_signal_type "Link to this definition")

    *property* tdqs*: bool*[](#keysight.ads.hsd.memory.memory.EmdMemory.tdqs "Link to this definition")

    *property* user\_defined\_ref\_des*: list[str]*[](#keysight.ads.hsd.memory.memory.EmdMemory.user_defined_ref_des "Link to this definition")
    :   Get the user defined reference designators.

        Returns:
        :   User defined reference designators.

        Return type:
        :   list[str]

    *property* vrm\_l*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.vrm_l "Link to this definition")

    *property* vrm\_r*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.vrm_r "Link to this definition")

    *property* vrm\_vdc*: str*[](#keysight.ads.hsd.memory.memory.EmdMemory.vrm_vdc "Link to this definition")


---

<!-- === 来源: reference/hsd/memory/ddr_termination.md === -->

# Memory Termination[](#memory-termination "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.termination.TerminationSetting[](#keysight.ads.hsd.memory.termination.TerminationSetting "Link to this definition")
:   Bases: `object`

    ca\_ctrl\_voltage[](#keysight.ads.hsd.memory.termination.TerminationSetting.ca_ctrl_voltage "Link to this definition")

    ca\_resistance[](#keysight.ads.hsd.memory.termination.TerminationSetting.ca_resistance "Link to this definition")

    ck\_capacitance[](#keysight.ads.hsd.memory.termination.TerminationSetting.ck_capacitance "Link to this definition")

    ck\_resistance[](#keysight.ads.hsd.memory.termination.TerminationSetting.ck_resistance "Link to this definition")

    ck\_voltage[](#keysight.ads.hsd.memory.termination.TerminationSetting.ck_voltage "Link to this definition")

    ctrl\_resistance[](#keysight.ads.hsd.memory.termination.TerminationSetting.ctrl_resistance "Link to this definition")

    save\_cb*: Callable[[], None] | None*[](#keysight.ads.hsd.memory.termination.TerminationSetting.save_cb "Link to this definition")

    set\_ck\_termination(*resistance: str | float*) → None[](#keysight.ads.hsd.memory.termination.TerminationSetting.set_ck_termination "Link to this definition")

    set\_ck\_termination(*resistance: str | float*, *voltage: str | float*) → None

    set\_ck\_termination(*resistance: str | float*, *voltage: str | float*, *capacitance: str | float*) → None

*class* keysight.ads.hsd.memory.termination.TerminationPortEnableModel[](#keysight.ads.hsd.memory.termination.TerminationPortEnableModel "Link to this definition")
:   Bases: `object`

    *property* metadata*: str*[](#keysight.ads.hsd.memory.termination.TerminationPortEnableModel.metadata "Link to this definition")

    *property* port\_name\_enable\_status*: ProxyDict*[](#keysight.ads.hsd.memory.termination.TerminationPortEnableModel.port_name_enable_status "Link to this definition")

    *property* ref\_des\_enable\_status*: ProxyDict*[](#keysight.ads.hsd.memory.termination.TerminationPortEnableModel.ref_des_enable_status "Link to this definition")

    save\_cb*: Callable[[], None]*[](#keysight.ads.hsd.memory.termination.TerminationPortEnableModel.save_cb "Link to this definition")

*class* keysight.ads.hsd.memory.termination.Termination[](#keysight.ads.hsd.memory.termination.Termination "Link to this definition")
:   Bases: `object`

    *property* available\_pcb\_or\_prelayout\_insts*: dict[str, str]*[](#keysight.ads.hsd.memory.termination.Termination.available_pcb_or_prelayout_insts "Link to this definition")

    linked\_instance\_name[](#keysight.ads.hsd.memory.termination.Termination.linked_instance_name "Link to this definition")

    *property* ports*: [TerminationPortEnableModel](#keysight.ads.hsd.memory.termination.TerminationPortEnableModel "keysight.ads.hsd.memory.termination.TerminationPortEnableModel")*[](#keysight.ads.hsd.memory.termination.Termination.ports "Link to this definition")

    save() → None[](#keysight.ads.hsd.memory.termination.Termination.save "Link to this definition")

    save\_cb*: Callable[[], None]*[](#keysight.ads.hsd.memory.termination.Termination.save_cb "Link to this definition")

    *property* settings*: [TerminationSetting](#keysight.ads.hsd.memory.termination.TerminationSetting "keysight.ads.hsd.memory.termination.TerminationSetting")*[](#keysight.ads.hsd.memory.termination.Termination.settings "Link to this definition")

## Functions[](#functions "Link to this heading")

keysight.ads.hsd.memory.termination.termination(*design: Design*, *term\_inst\_name: str = ''*) → [Termination](#keysight.ads.hsd.memory.termination.Termination "keysight.ads.hsd.memory.termination.Termination")[](#keysight.ads.hsd.memory.termination.termination "Link to this definition")


---

<!-- === 来源: reference/hsd/memory/index.md === -->

# keysight.ads.hsd.memory[](#module-keysight.ads.hsd.memory "Link to this heading")

ADS Memory Designer API.

* [Memory Setup](setup.md)
  + [Enumerated types](setup.md#enumerated-types)
  + [Classes](setup.md#classes)
* [Memory Pre-layout](prelayout.md)
  + [Enumerated types](prelayout.md#enumerated-types)
  + [Classes](prelayout.md#classes)
* [Memory Printed Circuit Board (PCB)](pcb.md)
  + [Enumerated types](pcb.md#enumerated-types)
  + [Classes](pcb.md#classes)
* [Memory Bus T-Line](bus_tline.md)
  + [Classes](bus_tline.md#classes)
* [Memory Bus Designer](bus_designer.md)
  + [Enumerated types](bus_designer.md#enumerated-types)
  + [Classes](bus_designer.md#classes)
* [Memory Controller](ddr_controller.md)
  + [Classes](ddr_controller.md#classes)
* [Memory DRAM](ddr_memory.md)
  + [Classes](ddr_memory.md#classes)
* [Memory Interface Simulator](simulator.md)
  + [`SimulationMode`](simulator.md#keysight.ads.hsd.memory.simulator.SimulationMode)
  + [`PassivityMode`](simulator.md#keysight.ads.hsd.memory.simulator.PassivityMode)
  + [`ToleranceMode`](simulator.md#keysight.ads.hsd.memory.simulator.ToleranceMode)
  + [`TimeStepControlMethod`](simulator.md#keysight.ads.hsd.memory.simulator.TimeStepControlMethod)
  + [`IntegrationMethod`](simulator.md#keysight.ads.hsd.memory.simulator.IntegrationMethod)
  + [`CrosstalkAnalysisBitPattern`](simulator.md#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern)
  + [`CrosstalkAnalysisVictimMode`](simulator.md#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisVictimMode)
  + [`SparamSweepType`](simulator.md#keysight.ads.hsd.memory.simulator.SparamSweepType)
  + [`SparamSweepMode`](simulator.md#keysight.ads.hsd.memory.simulator.SparamSweepMode)
  + [`SparamTermPlacement`](simulator.md#keysight.ads.hsd.memory.simulator.SparamTermPlacement)
  + [Classes](simulator.md#classes)
* [Memory Probe](probe.md)
  + [Enumerated types](probe.md#enumerated-types)
  + [Classes](probe.md#classes)
* [Memory Termination](ddr_termination.md)
  + [Classes](ddr_termination.md#classes)
  + [Functions](ddr_termination.md#functions)
* [Memory IO Component](io_component.md)
  + [Enumerated types](io_component.md#enumerated-types)
  + [Classes](io_component.md#classes)


---

<!-- === 来源: reference/hsd/memory/io_component.md === -->

# Memory IO Component[](#memory-io-component "Link to this heading")

## Enumerated types[](#enumerated-types "Link to this heading")

*class* keysight.ads.hsd.memory.io\_component.AMIParameterType[](#keysight.ads.hsd.memory.io_component.AMIParameterType "Link to this definition")
:   Bases: `EnumWrapper`

    AMI parameter type.

    MODEL\_SPECIFIC *= <AmiParameterType.MODEL\_SPECIFIC: 1>*[](#keysight.ads.hsd.memory.io_component.AMIParameterType.MODEL_SPECIFIC "Link to this definition")

    RESERVED *= <AmiParameterType.RESERVED: 0>*[](#keysight.ads.hsd.memory.io_component.AMIParameterType.RESERVED "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.PackageType[](#keysight.ads.hsd.memory.io_component.PackageType "Link to this definition")
:   Bases: `Enum`

    Enum for package types.

    EXTERNAL\_S\_PARAMETER\_PACKAGE *= <PkgType.EXTERNAL\_PACKAGE: 4>*[](#keysight.ads.hsd.memory.io_component.PackageType.EXTERNAL_S_PARAMETER_PACKAGE "Link to this definition")

    IBIS\_INTERCONNECT\_MODEL *= <PkgType.ISS: 3>*[](#keysight.ads.hsd.memory.io_component.PackageType.IBIS_INTERCONNECT_MODEL "Link to this definition")

    IBIS\_PACKAGE\_MODEL *= <PkgType.DEFINE\_PACKAGE\_MODEL: 2>*[](#keysight.ads.hsd.memory.io_component.PackageType.IBIS_PACKAGE_MODEL "Link to this definition")

    IBIS\_RLC\_PACKAGE *= <PkgType.RLC: 1>*[](#keysight.ads.hsd.memory.io_component.PackageType.IBIS_RLC_PACKAGE "Link to this definition")

    NONE *= <PkgType.NONE: 0>*[](#keysight.ads.hsd.memory.io_component.PackageType.NONE "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.IbisPackageModelType[](#keysight.ads.hsd.memory.io_component.IbisPackageModelType "Link to this definition")
:   Bases: `Enum`

    Enum for IBIS package model types.

    LUMPED\_MATRIX\_MODEL *= 5*[](#keysight.ads.hsd.memory.io_component.IbisPackageModelType.LUMPED_MATRIX_MODEL "Link to this definition")

    W\_ELEMENT *= 2*[](#keysight.ads.hsd.memory.io_component.IbisPackageModelType.W_ELEMENT "Link to this definition")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.io\_component.RefDesInfo[](#keysight.ads.hsd.memory.io_component.RefDesInfo "Link to this definition")
:   Bases: `object`

    *property* clk\_offset*: int*[](#keysight.ads.hsd.memory.io_component.RefDesInfo.clk_offset "Link to this definition")

    *property* dq\_multiplier*: int*[](#keysight.ads.hsd.memory.io_component.RefDesInfo.dq_multiplier "Link to this definition")

    *property* dram\_type*: str*[](#keysight.ads.hsd.memory.io_component.RefDesInfo.dram_type "Link to this definition")

    *property* include*: bool*[](#keysight.ads.hsd.memory.io_component.RefDesInfo.include "Link to this definition")

    *abstract property* pin*: [RefDesSignalDataCollection](#keysight.ads.hsd.memory.io_component.RefDesSignalDataCollection "keysight.ads.hsd._common.io_component.RefDesSignalDataCollection")*[](#keysight.ads.hsd.memory.io_component.RefDesInfo.pin "Link to this definition")
    :   Access the signal data for the reference designator.

        Individual signal data can be accessed as follows:
        `` `[<pin_name>]` `` where pin\_name is the pin name.

        Returns:
        :   **RefDesSignalDataCollection**

        Return type:
        :   The reference designator signal data collection.

    *property* ref\_des*: str*[](#keysight.ads.hsd.memory.io_component.RefDesInfo.ref_des "Link to this definition")

    *property* ref\_dqm\_en*: bool*[](#keysight.ads.hsd.memory.io_component.RefDesInfo.ref_dqm_en "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.RefDesInfoKeysView[](#keysight.ads.hsd.memory.io_component.RefDesInfoKeysView "Link to this definition")
:   Bases: `KeysView`

    isdisjoint(*other*)[](#keysight.ads.hsd.memory.io_component.RefDesInfoKeysView.isdisjoint "Link to this definition")
    :   Return True if two sets have a null intersection.

*class* keysight.ads.hsd.memory.io\_component.RefDesInfoCollection[](#keysight.ads.hsd.memory.io_component.RefDesInfoCollection "Link to this definition")
:   Bases: `Sequence`, `Mapping`

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.RefDesInfoCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.RefDesInfoCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.RefDesInfoCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.RefDesInfoCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.RefDesInfoCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.RefDesInfoCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.AmiParameterEntry[](#keysight.ads.hsd.memory.io_component.AmiParameterEntry "Link to this definition")
:   Bases: `object`

    AMI parameter entry.

    *property* description*: str*[](#keysight.ads.hsd.memory.io_component.AmiParameterEntry.description "Link to this definition")

    *property* index*: int*[](#keysight.ads.hsd.memory.io_component.AmiParameterEntry.index "Link to this definition")

    *property* prefix*: str*[](#keysight.ads.hsd.memory.io_component.AmiParameterEntry.prefix "Link to this definition")

    *property* sub\_param\_name*: str*[](#keysight.ads.hsd.memory.io_component.AmiParameterEntry.sub_param_name "Link to this definition")

    *property* valid\_values\_with\_tips*: list[tuple[str, str]]*[](#keysight.ads.hsd.memory.io_component.AmiParameterEntry.valid_values_with_tips "Link to this definition")

    *property* value*: str*[](#keysight.ads.hsd.memory.io_component.AmiParameterEntry.value "Link to this definition")

    *property* variable*: str | None*[](#keysight.ads.hsd.memory.io_component.AmiParameterEntry.variable "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.AmiParameter[](#keysight.ads.hsd.memory.io_component.AmiParameter "Link to this definition")
:   Bases: `object`

    AMI parameter info.

    *property* description*: str*[](#keysight.ads.hsd.memory.io_component.AmiParameter.description "Link to this definition")

    *property* has\_sub\_parameters*: bool*[](#keysight.ads.hsd.memory.io_component.AmiParameter.has_sub_parameters "Link to this definition")

    *property* index*: int*[](#keysight.ads.hsd.memory.io_component.AmiParameter.index "Link to this definition")

    *property* name*: str*[](#keysight.ads.hsd.memory.io_component.AmiParameter.name "Link to this definition")

    *property* prefix*: str*[](#keysight.ads.hsd.memory.io_component.AmiParameter.prefix "Link to this definition")

    *property* size*: int*[](#keysight.ads.hsd.memory.io_component.AmiParameter.size "Link to this definition")

    *property* type*: [AMIParameterType](#keysight.ads.hsd.memory.io_component.AMIParameterType "keysight.ads.hsd._common.io_component.AMIParameterType")*[](#keysight.ads.hsd.memory.io_component.AmiParameter.type "Link to this definition")

    *property* valid\_values\_with\_tips*: list[tuple[str, str]]*[](#keysight.ads.hsd.memory.io_component.AmiParameter.valid_values_with_tips "Link to this definition")

    *property* value*: str*[](#keysight.ads.hsd.memory.io_component.AmiParameter.value "Link to this definition")

    *property* variable*: str | None*[](#keysight.ads.hsd.memory.io_component.AmiParameter.variable "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.AmiParameterCollection[](#keysight.ads.hsd.memory.io_component.AmiParameterCollection "Link to this definition")
:   Bases: `Sequence`, `Mapping`

    Collection of AMI parameters.

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.AmiParameterCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.AmiParameterCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.AmiParameterCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.AmiParameterCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.AmiParameterCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.AmiParameterCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.AmiParameters[](#keysight.ads.hsd.memory.io_component.AmiParameters "Link to this definition")
:   Bases: `object`

    AMI parameters.

    *property* parameters*: [AmiParameterCollection](#keysight.ads.hsd.memory.io_component.AmiParameterCollection "keysight.ads.hsd._common.io_component.AmiParameterCollection")*[](#keysight.ads.hsd.memory.io_component.AmiParameters.parameters "Link to this definition")
    :   Get the list of AMI parameters.

*class* keysight.ads.hsd.memory.io\_component.SingleValueParameter[](#keysight.ads.hsd.memory.io_component.SingleValueParameter "Link to this definition")
:   Bases: `object`

    Single value parameter.

    *property* unit*: str*[](#keysight.ads.hsd.memory.io_component.SingleValueParameter.unit "Link to this definition")

    *property* units*: list[str]*[](#keysight.ads.hsd.memory.io_component.SingleValueParameter.units "Link to this definition")

    *property* value*: str*[](#keysight.ads.hsd.memory.io_component.SingleValueParameter.value "Link to this definition")

    *property* var\_name*: str*[](#keysight.ads.hsd.memory.io_component.SingleValueParameter.var_name "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.SelectValueParameter[](#keysight.ads.hsd.memory.io_component.SelectValueParameter "Link to this definition")
:   Bases: `object`

    Select value parameter.

    *property* value*: str*[](#keysight.ads.hsd.memory.io_component.SelectValueParameter.value "Link to this definition")

    *property* values*: list[str]*[](#keysight.ads.hsd.memory.io_component.SelectValueParameter.values "Link to this definition")

    *property* var\_name*: str*[](#keysight.ads.hsd.memory.io_component.SelectValueParameter.var_name "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.PrbsParameters[](#keysight.ads.hsd.memory.io_component.PrbsParameters "Link to this definition")
:   Bases: `object`

    Prbs Parameters.

    *property* bit\_file*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.PrbsParameters.bit_file "Link to this definition")

    *property* bit\_sequence*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.PrbsParameters.bit_sequence "Link to this definition")

    *property* mode*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.PrbsParameters.mode "Link to this definition")

    *property* pam\_symbol\_file*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.PrbsParameters.pam_symbol_file "Link to this definition")

    *property* pam\_symbol\_sequence*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.PrbsParameters.pam_symbol_sequence "Link to this definition")

    *property* pj\_amplitude*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.PrbsParameters.pj_amplitude "Link to this definition")

    *property* pj\_frequency*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.PrbsParameters.pj_frequency "Link to this definition")

    *property* register\_length*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.PrbsParameters.register_length "Link to this definition")

    *property* rj\_rms*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.PrbsParameters.rj_rms "Link to this definition")

    *property* seed*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.PrbsParameters.seed "Link to this definition")

    *property* taps*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.PrbsParameters.taps "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.JitterParameters[](#keysight.ads.hsd.memory.io_component.JitterParameters "Link to this definition")
:   Bases: `object`

    Access the jitter Parameters.

    *property* amplitude\_noise*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.amplitude_noise "Link to this definition")

    *property* clock\_dcd*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.clock_dcd "Link to this definition")

    *property* dcd*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.dcd "Link to this definition")

    *property* enable\_jitter\_pdf*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.enable_jitter_pdf "Link to this definition")

    *property* jitter\_pdf\_max*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.jitter_pdf_max "Link to this definition")

    *property* jitter\_pdf\_mean1*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.jitter_pdf_mean1 "Link to this definition")

    *property* jitter\_pdf\_mean2*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.jitter_pdf_mean2 "Link to this definition")

    *property* jitter\_pdf\_min*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.jitter_pdf_min "Link to this definition")

    *property* jitter\_pdf\_sigma*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.jitter_pdf_sigma "Link to this definition")

    *property* jitter\_pdf\_type*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.jitter_pdf_type "Link to this definition")

    *property* pj\_amplitude*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.pj_amplitude "Link to this definition")

    *property* pj\_frequency*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.pj_frequency "Link to this definition")

    *property* sj\_amplitude*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.JitterParameters.sj_amplitude "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.TxEqualizationParameters[](#keysight.ads.hsd.memory.io_component.TxEqualizationParameters "Link to this definition")
:   Bases: `object`

    Tx Equalization parameters.

    *property* de\_emphasis*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.TxEqualizationParameters.de_emphasis "Link to this definition")

    *property* equalization\_method*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.TxEqualizationParameters.equalization_method "Link to this definition")

    *property* fir\_taps*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.TxEqualizationParameters.fir_taps "Link to this definition")

    *property* tap\_interval*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.TxEqualizationParameters.tap_interval "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.CtleParameters[](#keysight.ads.hsd.memory.io_component.CtleParameters "Link to this definition")
:   Bases: `object`

    CTLE (Continuous Time Linear Equalization) Parameters.

    *property* ctle\_file*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.CtleParameters.ctle_file "Link to this definition")

    *property* ctle\_mode*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.CtleParameters.ctle_mode "Link to this definition")

    *property* enable*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.CtleParameters.enable "Link to this definition")

    *property* poles*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.CtleParameters.poles "Link to this definition")

    *property* prefactor*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.CtleParameters.prefactor "Link to this definition")

    *property* zeros*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.CtleParameters.zeros "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.DfeParameters[](#keysight.ads.hsd.memory.io_component.DfeParameters "Link to this definition")
:   Bases: `object`

    DFE (Decision Feedback Equalizer) Parameters.

    *property* enable*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.DfeParameters.enable "Link to this definition")

    *property* mode*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.DfeParameters.mode "Link to this definition")

    *property* number\_of\_taps\_for\_optimized\_mode*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.DfeParameters.number_of_taps_for_optimized_mode "Link to this definition")

    *property* slicer\_output*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.DfeParameters.slicer_output "Link to this definition")

    *property* taps\_for\_manual\_mode*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.DfeParameters.taps_for_manual_mode "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.FfeParameters[](#keysight.ads.hsd.memory.io_component.FfeParameters "Link to this definition")
:   Bases: `object`

    FFE (Feed Forward Equalizer) Parameters.

    *property* enable*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.FfeParameters.enable "Link to this definition")

    *property* mode*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.FfeParameters.mode "Link to this definition")

    *property* number\_of\_postcursor\_taps\_for\_optimized\_mode*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.FfeParameters.number_of_postcursor_taps_for_optimized_mode "Link to this definition")

    *property* number\_of\_precursor\_taps\_for\_optimized\_mode*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.FfeParameters.number_of_precursor_taps_for_optimized_mode "Link to this definition")

    *property* postcursor\_taps\_for\_manual\_mode*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.FfeParameters.postcursor_taps_for_manual_mode "Link to this definition")

    *property* precursor\_taps\_for\_manual\_mode*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.FfeParameters.precursor_taps_for_manual_mode "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.TapFileParameters[](#keysight.ads.hsd.memory.io_component.TapFileParameters "Link to this definition")
:   Bases: `object`

    FFE/DFE Tap file parameters.

    *property* input\_file*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.TapFileParameters.input_file "Link to this definition")

    *property* output\_file*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.TapFileParameters.output_file "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.ElectricalParameters[](#keysight.ads.hsd.memory.io_component.ElectricalParameters "Link to this definition")
:   Bases: `object`

    Electrical parameters.

    *property* add\_rlc\_parasitics*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ElectricalParameters.add_rlc_parasitics "Link to this definition")
    :   Access the add RLC parasitics parameter.

    *property* c\_parasitic*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ElectricalParameters.c_parasitic "Link to this definition")
    :   Access the C\_parasitic parameter.

    *property* l\_parasitic*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ElectricalParameters.l_parasitic "Link to this definition")
    :   Access the L\_parasitic parameter.

    *property* r\_in*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ElectricalParameters.r_in "Link to this definition")
    :   Access the R\_in parameter.

    *property* r\_out*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ElectricalParameters.r_out "Link to this definition")
    :   Access the R\_out parameter.

    *property* r\_out\_non\_target*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ElectricalParameters.r_out_non_target "Link to this definition")
    :   Access the R\_out\_non\_target parameter.

    *property* r\_parasitic*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ElectricalParameters.r_parasitic "Link to this definition")
    :   Access the R\_parasitic parameter.

    *property* v\_term*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ElectricalParameters.v_term "Link to this definition")
    :   Access the V\_term parameter.

*class* keysight.ads.hsd.memory.io\_component.WaveformParameters[](#keysight.ads.hsd.memory.io_component.WaveformParameters "Link to this definition")
:   Bases: `object`

    Waveform parameters.

    *property* fall\_time*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.WaveformParameters.fall_time "Link to this definition")
    :   Access the fall time parameter.

    *property* rise\_time*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.WaveformParameters.rise_time "Link to this definition")
    :   Access the rise time parameter.

    *property* v\_high*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.WaveformParameters.v_high "Link to this definition")
    :   Access the V\_high parameter.

    *property* v\_low*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.WaveformParameters.v_low "Link to this definition")
    :   Access the V\_low parameter.

*class* keysight.ads.hsd.memory.io\_component.AdditionalJitterParameters[](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters "Link to this definition")
:   Bases: `object`

    Additional jitter parameters.

    *property* rx\_dcd*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters.rx_dcd "Link to this definition")
    :   Access the Rx duty cycle distortion parameter.

    *property* rx\_dj*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters.rx_dj "Link to this definition")
    :   Access the Rx deterministic jitter parameter.

    *property* rx\_noise*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters.rx_noise "Link to this definition")
    :   Access the Rx\_Noise parameter.

    *property* rx\_rj*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters.rx_rj "Link to this definition")
    :   Access the Rx random jitter parameter.

    *property* rx\_sj*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters.rx_sj "Link to this definition")
    :   Access the Rx sinusoidal jitter parameter.

    *property* tx\_dcd*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters.tx_dcd "Link to this definition")
    :   Access the Tx duty cycle distortion parameter.

    *property* tx\_dj*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters.tx_dj "Link to this definition")
    :   Access the Tx deterministic jitter parameter.

    *property* tx\_rj*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters.tx_rj "Link to this definition")
    :   Access the Tx random jitter parameter.

    *property* tx\_sj*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters.tx_sj "Link to this definition")
    :   Access the Tx sinusoidal jitter parameter.

    *property* tx\_sj\_frequency*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters.tx_sj_frequency "Link to this definition")
    :   Access the Tx sinusoidal jitter frequency parameter.

*class* keysight.ads.hsd.memory.io\_component.ModelParameters[](#keysight.ads.hsd.memory.io_component.ModelParameters "Link to this definition")
:   Bases: `object`

    Model parameters.

    *property* add\_dc\_offset\_to\_output*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.add_dc_offset_to_output "Link to this definition")
    :   Access the add DC offset to output parameter.

    *property* ami*: [AmiParameters](#keysight.ads.hsd.memory.io_component.AmiParameters "keysight.ads.hsd._common.io_component.AmiParameters")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.ami "Link to this definition")
    :   Access the AMI parameters.

    *property* ami\_additional\_jitter*: [AdditionalJitterParameters](#keysight.ads.hsd.memory.io_component.AdditionalJitterParameters "keysight.ads.hsd._common.io_component.AdditionalJitterParameters")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.ami_additional_jitter "Link to this definition")
    :   Access the AMI additional jitter parameters.

    *property* clock\_mode*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.clock_mode "Link to this definition")
    :   Access the clock mode parameter.

    *property* ctle*: [CtleParameters](#keysight.ads.hsd.memory.io_component.CtleParameters "keysight.ads.hsd._common.io_component.CtleParameters")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.ctle "Link to this definition")
    :   Access the CTLE parameters.

    *property* delay*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.delay "Link to this definition")
    :   Access the delay parameter.

    *property* dfe*: [DfeParameters](#keysight.ads.hsd.memory.io_component.DfeParameters "keysight.ads.hsd._common.io_component.DfeParameters")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.dfe "Link to this definition")
    :   Access the DFE parameters.

    *property* electrical*: [ElectricalParameters](#keysight.ads.hsd.memory.io_component.ElectricalParameters "keysight.ads.hsd._common.io_component.ElectricalParameters")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.electrical "Link to this definition")
    :   Access the electrical parameters.

    *property* ffe*: [FfeParameters](#keysight.ads.hsd.memory.io_component.FfeParameters "keysight.ads.hsd._common.io_component.FfeParameters")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.ffe "Link to this definition")
    :   Access the FFE parameters.

    *property* flavor*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.flavor "Link to this definition")
    :   Access the flavor parameter.

    *property* ibis\_corner\_type*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.ibis_corner_type "Link to this definition")
    :   Access the IBIS corner type parameter.

    *property* ibis\_rx\_model\_selector*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.ibis_rx_model_selector "Link to this definition")
    :   Access the IBIS model selector RX parameter.

    *property* ibis\_tx\_model\_selector*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.ibis_tx_model_selector "Link to this definition")
    :   Access the IBIS model selector TX parameter.

    *property* interpolation\_mode*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.interpolation_mode "Link to this definition")
    :   Access the interpolation mode parameter.

    *property* jitter*: [JitterParameters](#keysight.ads.hsd.memory.io_component.JitterParameters "keysight.ads.hsd._common.io_component.JitterParameters")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.jitter "Link to this definition")
    :   Access the jitter parameters.

    *property* modulation*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.modulation "Link to this definition")
    :   Access the modulation parameter.

    *property* pair\_differential\_pins*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.pair_differential_pins "Link to this definition")
    :   Access the pair differential pins parameter.

    *property* prbs*: [PrbsParameters](#keysight.ads.hsd.memory.io_component.PrbsParameters "keysight.ads.hsd._common.io_component.PrbsParameters")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.prbs "Link to this definition")
    :   Access the VT PRBS parameters.

    *property* rx\_custom\_number\_of\_time\_points\_per\_ui*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.rx_custom_number_of_time_points_per_ui "Link to this definition")
    :   Access the RX custom time points parameter.

    *property* rx\_number\_of\_time\_points\_per\_ui*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.rx_number_of_time_points_per_ui "Link to this definition")
    :   Access the RX number of time points per UI parameter.

    *property* rx\_save\_out\_inout\_parameters*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.rx_save_out_inout_parameters "Link to this definition")
    :   Access the Save Out / In Out parameters (RX) parameter.

    *property* save\_impulse\_response*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.save_impulse_response "Link to this definition")
    :   Access the save impulse response parameter.

    *property* tap*: [TapFileParameters](#keysight.ads.hsd.memory.io_component.TapFileParameters "keysight.ads.hsd._common.io_component.TapFileParameters")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.tap "Link to this definition")
    :   Access the tap file parameters.

    *property* target*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.target "Link to this definition")
    :   Access the target parameter.

    *property* tx\_custom\_number\_of\_time\_points\_per\_ui*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.tx_custom_number_of_time_points_per_ui "Link to this definition")
    :   Access the TX custom time points parameter.

    *property* tx\_eq*: [TxEqualizationParameters](#keysight.ads.hsd.memory.io_component.TxEqualizationParameters "keysight.ads.hsd._common.io_component.TxEqualizationParameters")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.tx_eq "Link to this definition")
    :   Access the equalization parameters.

    *property* tx\_number\_of\_time\_points\_per\_ui*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.tx_number_of_time_points_per_ui "Link to this definition")
    :   Access the TX number of time points per UI parameter.

    *property* tx\_save\_output\_and\_inout\_parameters*: [SelectValueParameter](#keysight.ads.hsd.memory.io_component.SelectValueParameter "keysight.ads.hsd._common.io_component.SelectValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.tx_save_output_and_inout_parameters "Link to this definition")
    :   Access the Save Output and In-Out parameters (TX) parameter.

    *property* user\_defined\_pam\_mapping*: [SingleValueParameter](#keysight.ads.hsd.memory.io_component.SingleValueParameter "keysight.ads.hsd._common.io_component.SingleValueParameter")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.user_defined_pam_mapping "Link to this definition")
    :   Access the user defined PAM mapping parameter.

    *property* waveform*: [WaveformParameters](#keysight.ads.hsd.memory.io_component.WaveformParameters "keysight.ads.hsd._common.io_component.WaveformParameters")*[](#keysight.ads.hsd.memory.io_component.ModelParameters.waveform "Link to this definition")
    :   Access the waveform parameters.

*class* keysight.ads.hsd.memory.io\_component.SignalData[](#keysight.ads.hsd.memory.io_component.SignalData "Link to this definition")
:   Bases: `object`

    *property* channel\_id*: str*[](#keysight.ads.hsd.memory.io_component.SignalData.channel_id "Link to this definition")

    *property* cloned\_pin*: bool*[](#keysight.ads.hsd.memory.io_component.SignalData.cloned_pin "Link to this definition")

    *property* model*: str*[](#keysight.ads.hsd.memory.io_component.SignalData.model "Link to this definition")

    *property* parameter*: [ModelParameters](#keysight.ads.hsd.memory.io_component.ModelParameters "keysight.ads.hsd._common.io_component.ModelParameters")*[](#keysight.ads.hsd.memory.io_component.SignalData.parameter "Link to this definition")
    :   Access the model setup parameters for the signal data.

    *property* pin\_name*: str*[](#keysight.ads.hsd.memory.io_component.SignalData.pin_name "Link to this definition")

    *property* ref\_des*: str*[](#keysight.ads.hsd.memory.io_component.SignalData.ref_des "Link to this definition")

    *property* signal\_index*: int*[](#keysight.ads.hsd.memory.io_component.SignalData.signal_index "Link to this definition")

    *property* signal\_info*: [SignalProperty](#keysight.ads.hsd.memory.io_component.SignalProperty "keysight.ads.hsd._common.io_component.SignalProperty")*[](#keysight.ads.hsd.memory.io_component.SignalData.signal_info "Link to this definition")

    *property* signal\_name*: str*[](#keysight.ads.hsd.memory.io_component.SignalData.signal_name "Link to this definition")

    *property* signal\_type*: [SignalTypeEnum](../metadata.md#keysight.ads.hsd.metadata.SignalTypeEnum "keysight.ads.hsd._common.metadata.SignalTypeEnum")*[](#keysight.ads.hsd.memory.io_component.SignalData.signal_type "Link to this definition")

    *property* simulate*: bool*[](#keysight.ads.hsd.memory.io_component.SignalData.simulate "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.EbdNodeData[](#keysight.ads.hsd.memory.io_component.EbdNodeData "Link to this definition")
:   Bases: [`SignalData`](#keysight.ads.hsd.memory.io_component.SignalData "keysight.ads.hsd._common.io_component.SignalData")

    Class representing EBD node data.

    *property* channel\_id*: str*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.channel_id "Link to this definition")
    :   Get the signal name for the EBD node.

    *property* cloned\_pin*: bool*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.cloned_pin "Link to this definition")
    :   EBD does not support cloned pin property.

    *property* model*: str*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.model "Link to this definition")
    :   EBD does not support model property.

    *property* node\_name*: str*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.node_name "Link to this definition")

    *property* parameter*: [ModelParameters](#keysight.ads.hsd.memory.io_component.ModelParameters "keysight.ads.hsd._common.io_component.ModelParameters")*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.parameter "Link to this definition")
    :   Access the model setup parameters for the node.

    *property* pin\_name*: str*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.pin_name "Link to this definition")

    *property* ref\_des*: str*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.ref_des "Link to this definition")
    :   Get the reference designator for the EBD node.

    *property* signal\_index*: int*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.signal_index "Link to this definition")
    :   Get the signal index for the EBD node.

    *property* signal\_info*: [SignalProperty](#keysight.ads.hsd.memory.io_component.SignalProperty "keysight.ads.hsd._common.io_component.SignalProperty")*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.signal_info "Link to this definition")

    *property* signal\_name*: str*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.signal_name "Link to this definition")
    :   EBD does not support signal name property.

    *property* signal\_type*: [SignalTypeEnum](../metadata.md#keysight.ads.hsd.metadata.SignalTypeEnum "keysight.ads.hsd._common.metadata.SignalTypeEnum")*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.signal_type "Link to this definition")
    :   Get the signal type for the EBD node.

    *property* simulate*: bool*[](#keysight.ads.hsd.memory.io_component.EbdNodeData.simulate "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.EbdSignalData[](#keysight.ads.hsd.memory.io_component.EbdSignalData "Link to this definition")
:   Bases: [`SignalData`](#keysight.ads.hsd.memory.io_component.SignalData "keysight.ads.hsd._common.io_component.SignalData")

    Class representing EBD signal data.

    *property* channel\_id*: str*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.channel_id "Link to this definition")

    *property* cloned\_pin*: bool*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.cloned_pin "Link to this definition")

    *property* model*: str*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.model "Link to this definition")

    *property* node*: [EbdNodeDataCollection](#keysight.ads.hsd.memory.io_component.EbdNodeDataCollection "keysight.ads.hsd._common.io_component.EbdNodeDataCollection")*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.node "Link to this definition")
    :   Access the EBD node data.

        Individual EBD node data can be accessed as follows:
        `` `[<node_name>]` `` where node\_name is the node name.

        Returns:
        :   **EbdNodeDataCollection**

        Return type:
        :   The EBD node data collection.

    *property* parameter*: [ModelParameters](#keysight.ads.hsd.memory.io_component.ModelParameters "keysight.ads.hsd._common.io_component.ModelParameters")*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.parameter "Link to this definition")
    :   Access the model setup parameters for the signal data.

    *property* pin\_name*: str*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.pin_name "Link to this definition")

    *property* ref\_des*: str*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.ref_des "Link to this definition")

    *property* signal\_index*: int*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.signal_index "Link to this definition")

    *property* signal\_info*: [SignalProperty](#keysight.ads.hsd.memory.io_component.SignalProperty "keysight.ads.hsd._common.io_component.SignalProperty")*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.signal_info "Link to this definition")

    *property* signal\_name*: str*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.signal_name "Link to this definition")

    *property* signal\_type*: [SignalTypeEnum](../metadata.md#keysight.ads.hsd.metadata.SignalTypeEnum "keysight.ads.hsd._common.metadata.SignalTypeEnum")*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.signal_type "Link to this definition")

    *property* simulate*: bool*[](#keysight.ads.hsd.memory.io_component.EbdSignalData.simulate "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.EmdNodeData[](#keysight.ads.hsd.memory.io_component.EmdNodeData "Link to this definition")
:   Bases: [`SignalData`](#keysight.ads.hsd.memory.io_component.SignalData "keysight.ads.hsd._common.io_component.SignalData")

    Class representing EMD node data.

    *property* channel\_id*: str*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.channel_id "Link to this definition")
    :   Get the signal name for the EMD node.

    *property* cloned\_pin*: bool*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.cloned_pin "Link to this definition")

    *property* model*: str*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.model "Link to this definition")

    *property* node\_name*: str*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.node_name "Link to this definition")

    *property* parameter*: [ModelParameters](#keysight.ads.hsd.memory.io_component.ModelParameters "keysight.ads.hsd._common.io_component.ModelParameters")*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.parameter "Link to this definition")
    :   Access the model setup parameters for the node.

    *property* pin\_name*: str*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.pin_name "Link to this definition")

    *property* ref\_des*: str*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.ref_des "Link to this definition")

    *property* signal\_index*: int*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.signal_index "Link to this definition")
    :   Get the signal index for the EMD node.

    *property* signal\_info*: [SignalProperty](#keysight.ads.hsd.memory.io_component.SignalProperty "keysight.ads.hsd._common.io_component.SignalProperty")*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.signal_info "Link to this definition")

    *property* signal\_name*: str*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.signal_name "Link to this definition")
    :   Get the signal name for the EMD node.

    *property* signal\_type*: [SignalTypeEnum](../metadata.md#keysight.ads.hsd.metadata.SignalTypeEnum "keysight.ads.hsd._common.metadata.SignalTypeEnum")*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.signal_type "Link to this definition")
    :   Get the signal type for the EMD node.

    *property* simulate*: bool*[](#keysight.ads.hsd.memory.io_component.EmdNodeData.simulate "Link to this definition")
    :   Get whether the EMD node is included for simulation.

*class* keysight.ads.hsd.memory.io\_component.EmdSignalData[](#keysight.ads.hsd.memory.io_component.EmdSignalData "Link to this definition")
:   Bases: [`SignalData`](#keysight.ads.hsd.memory.io_component.SignalData "keysight.ads.hsd._common.io_component.SignalData")

    Class representing EMD signal data.

    *property* channel\_id*: str*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.channel_id "Link to this definition")

    *property* cloned\_pin*: bool*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.cloned_pin "Link to this definition")

    *property* model*: str*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.model "Link to this definition")

    *property* node*: [EmdNodeDataCollection](#keysight.ads.hsd.memory.io_component.EmdNodeDataCollection "keysight.ads.hsd._common.io_component.EmdNodeDataCollection")*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.node "Link to this definition")
    :   Access the EMD node data.

        Individual EMD node data can be accessed as follows:
        `` `[<node_name>]` `` where node\_name is the node name.

        Returns:
        :   **EmdNodeDataCollection**

        Return type:
        :   The EMD node data collection.

    *property* parameter*: [ModelParameters](#keysight.ads.hsd.memory.io_component.ModelParameters "keysight.ads.hsd._common.io_component.ModelParameters")*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.parameter "Link to this definition")
    :   Access the model setup parameters for the signal data.

    *property* pin\_name*: str*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.pin_name "Link to this definition")

    *property* ref\_des*: str*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.ref_des "Link to this definition")

    *property* signal\_index*: int*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.signal_index "Link to this definition")

    *property* signal\_info*: [SignalProperty](#keysight.ads.hsd.memory.io_component.SignalProperty "keysight.ads.hsd._common.io_component.SignalProperty")*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.signal_info "Link to this definition")

    *property* signal\_name*: str*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.signal_name "Link to this definition")

    *property* signal\_type*: [SignalTypeEnum](../metadata.md#keysight.ads.hsd.metadata.SignalTypeEnum "keysight.ads.hsd._common.metadata.SignalTypeEnum")*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.signal_type "Link to this definition")

    *property* simulate*: bool*[](#keysight.ads.hsd.memory.io_component.EmdSignalData.simulate "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.SignalProperty[](#keysight.ads.hsd.memory.io_component.SignalProperty "Link to this definition")
:   Bases: `object`

    *property* channel\_id*: str*[](#keysight.ads.hsd.memory.io_component.SignalProperty.channel_id "Link to this definition")

    *property* ref\_des*: str*[](#keysight.ads.hsd.memory.io_component.SignalProperty.ref_des "Link to this definition")

    *property* signal\_index*: int*[](#keysight.ads.hsd.memory.io_component.SignalProperty.signal_index "Link to this definition")

    *property* signal\_type*: [SignalTypeEnum](../metadata.md#keysight.ads.hsd.metadata.SignalTypeEnum "keysight.ads.hsd._common.metadata.SignalTypeEnum")*[](#keysight.ads.hsd.memory.io_component.SignalProperty.signal_type "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.SignalDataKeysView[](#keysight.ads.hsd.memory.io_component.SignalDataKeysView "Link to this definition")
:   Bases: `KeysView`

    isdisjoint(*other*)[](#keysight.ads.hsd.memory.io_component.SignalDataKeysView.isdisjoint "Link to this definition")
    :   Return True if two sets have a null intersection.

*class* keysight.ads.hsd.memory.io\_component.SignalDataCollection[](#keysight.ads.hsd.memory.io_component.SignalDataCollection "Link to this definition")
:   Bases: `Sequence`, `Mapping`

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.SignalDataCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.SignalDataCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.SignalDataCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.SignalDataCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.SignalDataCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.SignalDataCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.EbdNodeDataCollection[](#keysight.ads.hsd.memory.io_component.EbdNodeDataCollection "Link to this definition")
:   Bases: `Sequence`, `Mapping`

    Collection of EBD node data.

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.EbdNodeDataCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.EbdNodeDataCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.EbdNodeDataCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.EbdNodeDataCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.EbdNodeDataCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.EbdNodeDataCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.EbdSignalDataCollection[](#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection "Link to this definition")
:   Bases: [`SignalDataCollection`](#keysight.ads.hsd.memory.io_component.SignalDataCollection "keysight.ads.hsd._common.io_component.SignalDataCollection")

    Collection of EBD signal data.

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.EmdNodeDataCollection[](#keysight.ads.hsd.memory.io_component.EmdNodeDataCollection "Link to this definition")
:   Bases: `Sequence`, `Mapping`

    Collection of EMD node data.

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.EmdNodeDataCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.EmdNodeDataCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.EmdNodeDataCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.EmdNodeDataCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.EmdNodeDataCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.EmdNodeDataCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.EmdSignalDataCollection[](#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection "Link to this definition")
:   Bases: [`SignalDataCollection`](#keysight.ads.hsd.memory.io_component.SignalDataCollection "keysight.ads.hsd._common.io_component.SignalDataCollection")

    Collection of EMD signal data.

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.RefDesSignalDataCollection[](#keysight.ads.hsd.memory.io_component.RefDesSignalDataCollection "Link to this definition")
:   Bases: [`SignalDataCollection`](#keysight.ads.hsd.memory.io_component.SignalDataCollection "keysight.ads.hsd._common.io_component.SignalDataCollection")

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.RefDesSignalDataCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.RefDesSignalDataCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.RefDesSignalDataCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.RefDesSignalDataCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.RefDesSignalDataCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.RefDesSignalDataCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.RefDesEbdSignalDataCollection[](#keysight.ads.hsd.memory.io_component.RefDesEbdSignalDataCollection "Link to this definition")
:   Bases: [`EbdSignalDataCollection`](#keysight.ads.hsd.memory.io_component.EbdSignalDataCollection "keysight.ads.hsd._common.io_component.EbdSignalDataCollection")

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.RefDesEbdSignalDataCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.RefDesEbdSignalDataCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.RefDesEbdSignalDataCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.RefDesEbdSignalDataCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.RefDesEbdSignalDataCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.RefDesEbdSignalDataCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.RefDesEmdSignalDataCollection[](#keysight.ads.hsd.memory.io_component.RefDesEmdSignalDataCollection "Link to this definition")
:   Bases: [`EmdSignalDataCollection`](#keysight.ads.hsd.memory.io_component.EmdSignalDataCollection "keysight.ads.hsd._common.io_component.EmdSignalDataCollection")

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.RefDesEmdSignalDataCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.RefDesEmdSignalDataCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.RefDesEmdSignalDataCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.RefDesEmdSignalDataCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.RefDesEmdSignalDataCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.RefDesEmdSignalDataCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.EbdRefDesInfo[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfo "Link to this definition")
:   Bases: [`RefDesInfo`](#keysight.ads.hsd.memory.io_component.RefDesInfo "keysight.ads.hsd._common.io_component.RefDesInfo")

    Class representing EBD reference designator info.

    *property* clk\_offset*: int*[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfo.clk_offset "Link to this definition")

    *property* dq\_multiplier*: int*[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfo.dq_multiplier "Link to this definition")

    *property* dram\_type*: str*[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfo.dram_type "Link to this definition")

    *property* include*: bool*[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfo.include "Link to this definition")

    *property* pin*: [RefDesEbdSignalDataCollection](#keysight.ads.hsd.memory.io_component.RefDesEbdSignalDataCollection "keysight.ads.hsd._common.io_component.RefDesEbdSignalDataCollection")*[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfo.pin "Link to this definition")
    :   Access the signal data for the reference designator.

        Individual signal data can be accessed as follows:
        `` `[<pin_name>]` `` where pin\_name is the pin name.

        Returns:
        :   **RefDesSignalDataCollection**

        Return type:
        :   The reference designator signal data collection.

    *property* ref\_des*: str*[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfo.ref_des "Link to this definition")

    *property* ref\_dqm\_en*: bool*[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfo.ref_dqm_en "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.EbdRefDesInfoCollection[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfoCollection "Link to this definition")
:   Bases: [`RefDesInfoCollection`](#keysight.ads.hsd.memory.io_component.RefDesInfoCollection "keysight.ads.hsd._common.io_component.RefDesInfoCollection")

    Collection of EBD reference designator info.

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfoCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfoCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfoCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfoCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfoCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.EbdRefDesInfoCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.EmdRefDesInfo[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfo "Link to this definition")
:   Bases: [`RefDesInfo`](#keysight.ads.hsd.memory.io_component.RefDesInfo "keysight.ads.hsd._common.io_component.RefDesInfo")

    Class representing EMD reference designator info.

    *property* clk\_offset*: int*[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfo.clk_offset "Link to this definition")

    *property* dq\_multiplier*: int*[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfo.dq_multiplier "Link to this definition")

    *property* dram\_type*: str*[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfo.dram_type "Link to this definition")

    *property* include*: bool*[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfo.include "Link to this definition")

    *property* pin*: [RefDesEmdSignalDataCollection](#keysight.ads.hsd.memory.io_component.RefDesEmdSignalDataCollection "keysight.ads.hsd._common.io_component.RefDesEmdSignalDataCollection")*[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfo.pin "Link to this definition")
    :   Access the signal data for the reference designator.

        Individual signal data can be accessed as follows:
        `` `[<pin_name>]` `` where pin\_name is the pin name.

        Returns:
        :   **RefDesSignalDataCollection**

        Return type:
        :   The reference designator signal data collection.

    *property* ref\_des*: str*[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfo.ref_des "Link to this definition")

    *property* ref\_dqm\_en*: bool*[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfo.ref_dqm_en "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.EmdRefDesInfoCollection[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfoCollection "Link to this definition")
:   Bases: [`RefDesInfoCollection`](#keysight.ads.hsd.memory.io_component.RefDesInfoCollection "keysight.ads.hsd._common.io_component.RefDesInfoCollection")

    Collection of EMD reference designator info.

    count(*value*) → integer -- return number of occurrences of value[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfoCollection.count "Link to this definition")

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfoCollection.get "Link to this definition")

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfoCollection.index "Link to this definition")
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    items() → a set-like object providing a view on D's items[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfoCollection.items "Link to this definition")

    keys() → a set-like object providing a view on D's keys[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfoCollection.keys "Link to this definition")

    values() → an object providing a view on D's values[](#keysight.ads.hsd.memory.io_component.EmdRefDesInfoCollection.values "Link to this definition")

*class* keysight.ads.hsd.memory.io\_component.DefinedPackage[](#keysight.ads.hsd.memory.io_component.DefinedPackage "Link to this definition")
:   Bases: `object`

    Class representing a defined package.

    *property* name*: str*[](#keysight.ads.hsd.memory.io_component.DefinedPackage.name "Link to this definition")
    :   Get the defined package name.

        Returns:
        :   Defined package name.

        Return type:
        :   str

    *property* type*: [IbisPackageModelType](#keysight.ads.hsd.memory.io_component.IbisPackageModelType "keysight.ads.hsd._common.io_component.IbisPackageModelType")*[](#keysight.ads.hsd.memory.io_component.DefinedPackage.type "Link to this definition")
    :   Get the defined package model type.

        Returns:
        :   Defined package model type.

        Return type:
        :   IbisPackageModelType

*class* keysight.ads.hsd.memory.io\_component.InterconnectModel[](#keysight.ads.hsd.memory.io_component.InterconnectModel "Link to this definition")
:   Bases: `object`

    Class representing an interconnect model.

    *property* group*: str*[](#keysight.ads.hsd.memory.io_component.InterconnectModel.group "Link to this definition")
    :   Get the ISS group name.

        Returns:
        :   ISS group name.

        Return type:
        :   str

    *property* pin\_pad\_buffer\_model*: str*[](#keysight.ads.hsd.memory.io_component.InterconnectModel.pin_pad_buffer_model "Link to this definition")
    :   Get the ISS pin pad buffer model.

        Returns:
        :   ISS pin pad buffer model.

        Return type:
        :   str

    *property* pin\_pad\_model*: str*[](#keysight.ads.hsd.memory.io_component.InterconnectModel.pin_pad_model "Link to this definition")
    :   Get the ISS pin pad model.

        Returns:
        :   ISS pin pad model.

        Return type:
        :   str

    *property* terminate\_unused\_ports*: bool*[](#keysight.ads.hsd.memory.io_component.InterconnectModel.terminate_unused_ports "Link to this definition")
    :   Get whether unused ports are terminated.

        Returns:
        :   True if unused ports are terminated, False otherwise.

        Return type:
        :   bool

    *property* termination\_value*: str*[](#keysight.ads.hsd.memory.io_component.InterconnectModel.termination_value "Link to this definition")
    :   Get the termination value for unused ports.

        Returns:
        :   Termination value for unused ports.

        Return type:
        :   str

*class* keysight.ads.hsd.memory.io\_component.ExternalSParamPackage[](#keysight.ads.hsd.memory.io_component.ExternalSParamPackage "Link to this definition")
:   Bases: `object`

    Class representing an external S-parameter package.

    *property* file*: Path*[](#keysight.ads.hsd.memory.io_component.ExternalSParamPackage.file "Link to this definition")
    :   Get the S-parameter file.

        Returns:
        :   S-parameter file.

        Return type:
        :   str

    *property* file\_type*: SParameterFileType*[](#keysight.ads.hsd.memory.io_component.ExternalSParamPackage.file_type "Link to this definition")
    :   Get the S-parameter file type.

        Returns:
        :   S-parameter file type.

        Return type:
        :   SParameterFileType

*class* keysight.ads.hsd.memory.io\_component.PackageSetup[](#keysight.ads.hsd.memory.io_component.PackageSetup "Link to this definition")
:   Bases: `object`

    *property* defined\_package*: [DefinedPackage](#keysight.ads.hsd.memory.io_component.DefinedPackage "keysight.ads.hsd._common.io_component.DefinedPackage")*[](#keysight.ads.hsd.memory.io_component.PackageSetup.defined_package "Link to this definition")
    :   Get the defined package name.

        Returns:
        :   Defined package name.

        Return type:
        :   str

    *property* emd*: str*[](#keysight.ads.hsd.memory.io_component.PackageSetup.emd "Link to this definition")
    :   Get the external EMD package name.

        Returns:
        :   EMD package name.

        Return type:
        :   str

    *property* external\_s\_parameter\_package*: [ExternalSParamPackage](#keysight.ads.hsd.memory.io_component.ExternalSParamPackage "keysight.ads.hsd._common.io_component.ExternalSParamPackage")*[](#keysight.ads.hsd.memory.io_component.PackageSetup.external_s_parameter_package "Link to this definition")
    :   Get the external S-parameter package.

        Returns:
        :   External S-parameter package.

        Return type:
        :   ExternalSParamPackage

    *property* interconnect\_model*: [InterconnectModel](#keysight.ads.hsd.memory.io_component.InterconnectModel "keysight.ads.hsd._common.io_component.InterconnectModel")*[](#keysight.ads.hsd.memory.io_component.PackageSetup.interconnect_model "Link to this definition")
    :   Get the interconnect model.

        Returns:
        :   Interconnect model.

        Return type:
        :   InterconnectModel

    *property* type*: [PackageType](#keysight.ads.hsd.memory.io_component.PackageType "keysight.ads.hsd._common.io_component.PackageType")*[](#keysight.ads.hsd.memory.io_component.PackageSetup.type "Link to this definition")
    :   Get the package type.

        Returns:
        :   Package type.

        Return type:
        :   str


---

<!-- === 来源: reference/hsd/memory/pcb.md === -->

# Memory Printed Circuit Board (PCB)[](#memory-printed-circuit-board-pcb "Link to this heading")

## Enumerated types[](#enumerated-types "Link to this heading")

*class* keysight.ads.hsd.memory.pcb.SetupMode[](#keysight.ads.hsd.memory.pcb.SetupMode "Link to this definition")
:   Bases: `Enum`

    DATA\_FILE *= <PCBRadioSelectionEnum.DataFile: 1>*[](#keysight.ads.hsd.memory.pcb.SetupMode.DATA_FILE "Link to this definition")

    SIPRO\_CELL *= <PCBRadioSelectionEnum.SIProCell: 0>*[](#keysight.ads.hsd.memory.pcb.SetupMode.SIPRO_CELL "Link to this definition")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.pcb.PCBModel[](#keysight.ads.hsd.memory.pcb.PCBModel "Link to this definition")
:   Bases: `object`

    *property* datafile\_name*: str | None*[](#keysight.ads.hsd.memory.pcb.PCBModel.datafile_name "Link to this definition")

    *property* datafile\_type*: str | None*[](#keysight.ads.hsd.memory.pcb.PCBModel.datafile_type "Link to this definition")

    *property* has\_metadata*: bool*[](#keysight.ads.hsd.memory.pcb.PCBModel.has_metadata "Link to this definition")

    *property* is\_setup*: bool*[](#keysight.ads.hsd.memory.pcb.PCBModel.is_setup "Link to this definition")

    *property* metadata*: [MetaData](../metadata.md#keysight.ads.hsd.metadata.MetaData "keysight.ads.hsd._common.metadata.MetaData") | None*[](#keysight.ads.hsd.memory.pcb.PCBModel.metadata "Link to this definition")

    *property* pcb\_instance\_name*: str*[](#keysight.ads.hsd.memory.pcb.PCBModel.pcb_instance_name "Link to this definition")

    *property* setup\_mode*: [SetupMode](#keysight.ads.hsd.memory.pcb.SetupMode "keysight.ads.hsd.memory.pcb.SetupMode") | None*[](#keysight.ads.hsd.memory.pcb.PCBModel.setup_mode "Link to this definition")

    *property* sipro\_file\_name*: str | None*[](#keysight.ads.hsd.memory.pcb.PCBModel.sipro_file_name "Link to this definition")

    *property* sipro\_lcv\_name*: str | None*[](#keysight.ads.hsd.memory.pcb.PCBModel.sipro_lcv_name "Link to this definition")

*class* keysight.ads.hsd.memory.pcb.PCBEditor[](#keysight.ads.hsd.memory.pcb.PCBEditor "Link to this definition")
:   Bases: `object`

    Setup of DDR\_PCB Instance.

    *property* pcb\_instance*: Instance*[](#keysight.ads.hsd.memory.pcb.PCBEditor.pcb_instance "Link to this definition")

    *property* pcb\_model*: [PCBModel](#keysight.ads.hsd.memory.pcb.PCBModel "keysight.ads.hsd.memory.pcb.PCBModel")*[](#keysight.ads.hsd.memory.pcb.PCBEditor.pcb_model "Link to this definition")

    port\_info(*key: str*) → [PortInfo](../metadata.md#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd.metadata.PortInfo")[](#keysight.ads.hsd.memory.pcb.PCBEditor.port_info "Link to this definition")

    port\_info(*key: int*) → [PortInfo](../metadata.md#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd.metadata.PortInfo")
    :   Get PortInfo object from the metadata of the PCB instance of this edit session with the given port name.

        Parameters:
        :   **port\_name** – Port name to be used for getting the metadata

        Returns:
        :   PortInfo object containing the metadata

        Return type:
        :   PortInfo

    read\_metadata\_from\_csv\_file(*csv\_file\_path: Path | str = ''*) → None[](#keysight.ads.hsd.memory.pcb.PCBEditor.read_metadata_from_csv_file "Link to this definition")
    :   Set the CSV File path of the PCB Instance of this edit session to the given csv file path and read DDRMetaData from it.

        .csv file format to be used for DIMM\_Connector and PCB:

        <ReferenceDesignator>,<PinName>,<SignalType>,<SignalIndex>,<PortName>,<ChannelID>,<Terminated>,<TerminationOhms>,<AltSignalType>,<AltSignalIndex>

        where,

        <ReferenceDesignator>, <PinName>, <SignalType>, <PortName>, <AltSignalType> - are strings

        <SignalIndex>, <ChannelID>, <Terminated>, <AltSignalIndex> - are integers

        <TerminationOhms> - is a double

        Parameters:
        :   **csv\_file\_path** – File system path of the given csv file, can be pathlib.Path or str.
            If not given, the csv file to be read will be the csv\_file\_path associated with the current PCBModel.

        Return type:
        :   None

    save\_change() → None[](#keysight.ads.hsd.memory.pcb.PCBEditor.save_change "Link to this definition")

    save\_metadata\_to\_csv\_file(*csv\_file\_path: Path | str*) → None[](#keysight.ads.hsd.memory.pcb.PCBEditor.save_metadata_to_csv_file "Link to this definition")
    :   Save MetaData of the PCB instance of this edit session to the given csv\_file.

        Parameters:
        :   **csv\_file\_path** – The path of the csv file for the MetaData to be saved to

        Return type:
        :   None

    setup\_with\_datafile(*data\_file\_path: Path | str*) → bool[](#keysight.ads.hsd.memory.pcb.PCBEditor.setup_with_datafile "Link to this definition")
    :   Set up an Instance of ads\_simulation:DDR\_PCB with a Data file(Touchstone, SmatrixIO, Dataset, CITI).

        Parameters:
        :   **data\_file\_path** – Path of the data file to be used for setting up, could be absolute or relative, delimiter could be / or

        Returns:
        :   True of the DDR\_PCB Instance is correctly setup, otherwise False

        Return type:
        :   bool

    setup\_with\_sipro\_cell(*sipro\_cell\_lcv: LCVName | tuple[str, str, str]*) → bool[](#keysight.ads.hsd.memory.pcb.PCBEditor.setup_with_sipro_cell "Link to this definition")
    :   Set up an Instance of ads\_simulation:DDR\_PCB with a SIPro cell with a valid SnP Instance (contains a SmatrixIO file).

        Parameters:
        :   **sipro\_cell\_lcv** – Lib-cell-view name of the SIPro cell, must be in the same workspace with the design of the current PCB instance

        Returns:
        :   True of the DDR\_PCB Instance is correctly setup, otherwise False

        Return type:
        :   bool

    update\_metadata\_with\_port\_name(*port\_name: str*, *port\_info: [PortInfo](../metadata.md#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo")*) → None[](#keysight.ads.hsd.memory.pcb.PCBEditor.update_metadata_with_port_name "Link to this definition")
    :   Update metadata of the PCB instance of this edit session with the given port name.

        Parameters:
        :   * **port\_name** – Port name to be used for updating the metadata
            * **port\_info** – Updated PortInfo object containing the metadata to be updated

        Return type:
        :   None


---

<!-- === 来源: reference/hsd/memory/prelayout.md === -->

# Memory Pre-layout[](#memory-pre-layout "Link to this heading")

## Enumerated types[](#enumerated-types "Link to this heading")

*class* keysight.ads.hsd.memory.prelayout.SetupMode[](#keysight.ads.hsd.memory.prelayout.SetupMode "Link to this definition")
:   Bases: `Enum`

    ADS\_CELL *= <PrelayoutFlowSelectionType.UseExistingCell: 0>*[](#keysight.ads.hsd.memory.prelayout.SetupMode.ADS_CELL "Link to this definition")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.prelayout.PrelayoutModel[](#keysight.ads.hsd.memory.prelayout.PrelayoutModel "Link to this definition")
:   Bases: `object`

    *property* design\_name*: str*[](#keysight.ads.hsd.memory.prelayout.PrelayoutModel.design_name "Link to this definition")
    :   Returns the name of the subcircuit design.

        Returns:
        :   The name of the subcircuit design associated with this instance.

        Return type:
        :   str

    *property* design\_parameters*: [DesignParameters](../core.md#keysight.ads.hsd.DesignParameters "keysight.ads.hsd._common.utils.DesignParameters")*[](#keysight.ads.hsd.memory.prelayout.PrelayoutModel.design_parameters "Link to this definition")
    :   Returns a dictionary-like object for accessing design parameters.

        Returns:
        :   A dictionary-like object that allows getting and setting design parameters
            using bracket notation:

            > model.design\_parameters[<param\_name>] = <param\_value>

        Return type:
        :   [DesignParameters](../core.md#keysight.ads.hsd.DesignParameters "keysight.ads.hsd.DesignParameters")

    *property* has\_metadata*: bool*[](#keysight.ads.hsd.memory.prelayout.PrelayoutModel.has_metadata "Link to this definition")

    *property* is\_setup*: bool*[](#keysight.ads.hsd.memory.prelayout.PrelayoutModel.is_setup "Link to this definition")
    :   Determines whether the pre-layout instance is initialized.

        Returns:
        :   True if the subcircuit design name is set and metadata is available, indicating the instance is properly set up; False otherwise.

        Return type:
        :   bool

    *property* metadata*: [MetaData](../metadata.md#keysight.ads.hsd.metadata.MetaData "keysight.ads.hsd._common.metadata.MetaData") | None*[](#keysight.ads.hsd.memory.prelayout.PrelayoutModel.metadata "Link to this definition")
    :   Returns the metadata associated with this pre-layout instance.

        The metadata provides detailed signal information for the pre-layout sub-circuit,
        such as signal names, types, and other relevant properties. If metadata is not
        available for this instance, returns None.

        Returns:
        :   The signal information or metadata for the pre-layout sub-circuit, or None if no metadata is present.

        Return type:
        :   [MetaData](../metadata.md#keysight.ads.hsd.metadata.MetaData "keysight.ads.hsd.metadata.MetaData") | None

    *property* setup\_mode*: [SetupMode](#keysight.ads.hsd.memory.prelayout.SetupMode "keysight.ads.hsd.memory.prelayout.SetupMode") | None*[](#keysight.ads.hsd.memory.prelayout.PrelayoutModel.setup_mode "Link to this definition")
    :   Returns the current setup mode if the object correctly initialized.

        Returns:
        :   An instance of SetupMode if the object is in setup mode; otherwise, None.

        Return type:
        :   [SetupMode](#keysight.ads.hsd.memory.prelayout.SetupMode "keysight.ads.hsd.memory.prelayout.SetupMode") | None

*class* keysight.ads.hsd.memory.prelayout.PrelayoutEditor[](#keysight.ads.hsd.memory.prelayout.PrelayoutEditor "Link to this definition")
:   Bases: `object`

    Set up DDR\_PreLayout Instance.

    apply\_metadata\_to\_subcircuit\_schematic\_pin\_names() → None[](#keysight.ads.hsd.memory.prelayout.PrelayoutEditor.apply_metadata_to_subcircuit_schematic_pin_names "Link to this definition")
    :   Apply the signal information to the pin names of the sub-circuit schematic.

        It will generate a new sub-circuit schematic called MemDesDDR\_schematic with updated pin names.
        If a new pre-layout instance is set up with that sub-circuit schematic, it will parse the pin names
        to retrieve signal information i.e. metadata.

        Return type:
        :   None

    port\_info(*key: str | int*) → [PortInfo](../metadata.md#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo")[](#keysight.ads.hsd.memory.prelayout.PrelayoutEditor.port_info "Link to this definition")

    port\_info(*key: str*) → [PortInfo](../metadata.md#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo")

    port\_info(*key: int*) → [PortInfo](../metadata.md#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo")
    :   Get PortInfo object from the metadata of the Pre-layout instance of this edit session with the given port name or index.

        Parameters:
        :   **key** (*str* *|* *int*) – Port name or index to be used for getting the metadata

        Returns:
        :   PortInfo object containing the metadata

        Return type:
        :   PortInfo

        Raises:
        :   * **TypeError** – If the key type is not str or int.
            * **IndexError** – If the int key as port index is out of range.
            * **KeyError** – If the str key as port name is not found.

    *property* prelayout\_instance*: Instance*[](#keysight.ads.hsd.memory.prelayout.PrelayoutEditor.prelayout_instance "Link to this definition")

    *property* prelayout\_model*: [PrelayoutModel](#keysight.ads.hsd.memory.prelayout.PrelayoutModel "keysight.ads.hsd.memory.prelayout.PrelayoutModel")*[](#keysight.ads.hsd.memory.prelayout.PrelayoutEditor.prelayout_model "Link to this definition")

    read\_metadata\_from\_csv\_file(*csv\_file\_path: Path | str = ''*) → None[](#keysight.ads.hsd.memory.prelayout.PrelayoutEditor.read_metadata_from_csv_file "Link to this definition")
    :   Set the CSV File path of the Pre-layout Instance of this edit session to the given csv file path and read metadata from it.

        .csv file format to be used for Pre-layout:

        <ReferenceDesignator>,<PinName>,<SignalType>,<SignalIndex>,<PortName>,<ChannelID>,<Terminated>,<TerminationOhms>,<AltSignalType>,<AltSignalIndex>

        where,

        <ReferenceDesignator>, <PinName>, <SignalType>, <PortName>, <AltSignalType> - are strings

        <SignalIndex>, <ChannelID>, <Terminated>, <AltSignalIndex> - are integers

        <TerminationOhms> - is a double

        Parameters:
        :   **csv\_file\_path** (*Path* *|* *str*) – File system path of the given csv file, can be pathlib.Path or str.
            If not given, the csv file to be read will be the csv\_file\_path associated with the current PrelayoutModel.

        Return type:
        :   None

    save() → None[](#keysight.ads.hsd.memory.prelayout.PrelayoutEditor.save "Link to this definition")
    :   Saves the parameters and metadata to the pre-layout instance.

    save\_metadata\_to\_csv\_file(*csv\_file\_path: Path | str*) → None[](#keysight.ads.hsd.memory.prelayout.PrelayoutEditor.save_metadata_to_csv_file "Link to this definition")
    :   Save MetaData of the Pre-layout instance of this edit session to the given csv\_file.

        Parameters:
        :   **csv\_file\_path** (*Path* *|* *str*) – The path of the csv file for the MetaData to be saved to

        Return type:
        :   None

    select\_sub\_ckt(*lcv\_name: str | tuple[str, str, str] | LCVName*) → None[](#keysight.ads.hsd.memory.prelayout.PrelayoutEditor.select_sub_ckt "Link to this definition")

    select\_sub\_ckt(*lcv\_name: str*) → None

    select\_sub\_ckt(*lcv\_name: tuple[str, str, str]*) → None

    select\_sub\_ckt(*lcv\_name: LCVName*) → None
    :   Select a sub-circuit that defines a pre-layout design.

        Parameters:
        :   **lcv\_name** (*str* *|* *tuple**[**str**,* *str**,* *str**]* *|* *de.LCVName*) – The name of the library cell view to select.
            If a string is provided, it is the full name of the cell in the form “{library name}:{cell name}:{view name}”.
            If a tuple is provided, it is the cell name, library name, and view name in that order.
            Alternatively, a de.LCVName object can be provided.

        Raises:
        :   **TypeError** – If the lcv\_name type is not str | tuple[str, str, str] | de.LCVName.

    update\_metadata\_with\_port\_name(*port\_name: str*, *port\_info: [PortInfo](../metadata.md#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo")*) → None[](#keysight.ads.hsd.memory.prelayout.PrelayoutEditor.update_metadata_with_port_name "Link to this definition")
    :   Update metadata of the Pre-layout instance of this edit session with the given port name.

        Parameters:
        :   * **port\_name** (*str*) – Port name to be used for updating the metadata
            * **port\_info** ([*PortInfo*](../metadata.md#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd.metadata.PortInfo")) – Updated PortInfo object containing the metadata to be updated

        Return type:
        :   None


---

<!-- === 来源: reference/hsd/memory/probe.md === -->

# Memory Probe[](#memory-probe "Link to this heading")

## Enumerated types[](#enumerated-types "Link to this heading")

*class* keysight.ads.hsd.memory.probe.ProbeFlowType[](#keysight.ads.hsd.memory.probe.ProbeFlowType "Link to this definition")
:   Bases: `Enum`

    CROSSTALK\_ANALYSIS *= <MemoryProbeFlowType.CROSSTALK\_ANALYSIS: 2>*[](#keysight.ads.hsd.memory.probe.ProbeFlowType.CROSSTALK_ANALYSIS "Link to this definition")

    MEASUREMENT *= <MemoryProbeFlowType.MEASUREMENT: 0>*[](#keysight.ads.hsd.memory.probe.ProbeFlowType.MEASUREMENT "Link to this definition")

    WRITE\_LEVELING *= <MemoryProbeFlowType.WRITE\_LEVELING: 1>*[](#keysight.ads.hsd.memory.probe.ProbeFlowType.WRITE_LEVELING "Link to this definition")

*class* keysight.ads.hsd.memory.probe.Measurement[](#keysight.ads.hsd.memory.probe.Measurement "Link to this definition")
:   Bases: `Enum`

    Bathtub *= 'Bathtub'*[](#keysight.ads.hsd.memory.probe.Measurement.Bathtub "Link to this definition")

    BathtubQPlots *= 'Bathtub QPlots'*[](#keysight.ads.hsd.memory.probe.Measurement.BathtubQPlots "Link to this definition")

    BerContour *= 'BER Contour'*[](#keysight.ads.hsd.memory.probe.Measurement.BerContour "Link to this definition")

    BerContourHeightAndWidth *= 'Height and Width at Targeted BER'*[](#keysight.ads.hsd.memory.probe.Measurement.BerContourHeightAndWidth "Link to this definition")

    ClockSignal *= 'Clock Signal'*[](#keysight.ads.hsd.memory.probe.Measurement.ClockSignal "Link to this definition")

    CustomizedMask *= 'Customized Mask'*[](#keysight.ads.hsd.memory.probe.Measurement.CustomizedMask "Link to this definition")

    Ddr5Mask *= 'DDR5 Mask'*[](#keysight.ads.hsd.memory.probe.Measurement.Ddr5Mask "Link to this definition")

    Eye *= 'Eye'*[](#keysight.ads.hsd.memory.probe.Measurement.Eye "Link to this definition")

    EyeHeightAndWidth *= 'Eye Height and Width'*[](#keysight.ads.hsd.memory.probe.Measurement.EyeHeightAndWidth "Link to this definition")

    EyeLevelInfo *= 'Eye Level Info'*[](#keysight.ads.hsd.memory.probe.Measurement.EyeLevelInfo "Link to this definition")

    MaskMargin *= 'Mask Margin'*[](#keysight.ads.hsd.memory.probe.Measurement.MaskMargin "Link to this definition")

    Skew *= 'Skew'*[](#keysight.ads.hsd.memory.probe.Measurement.Skew "Link to this definition")

    SlewRate *= 'Slew Rate'*[](#keysight.ads.hsd.memory.probe.Measurement.SlewRate "Link to this definition")

    StrobedEye *= 'Strobed Eye'*[](#keysight.ads.hsd.memory.probe.Measurement.StrobedEye "Link to this definition")

    VSRPAM4 *= 'VSR PAM4 Parameters'*[](#keysight.ads.hsd.memory.probe.Measurement.VSRPAM4 "Link to this definition")

    VSRPAMn *= 'VSR PAMN Parameters'*[](#keysight.ads.hsd.memory.probe.Measurement.VSRPAMn "Link to this definition")

    Waveform *= 'Waveform'*[](#keysight.ads.hsd.memory.probe.Measurement.Waveform "Link to this definition")

    tDIVW1Margin *= 'tDIVW1 Margin'*[](#keysight.ads.hsd.memory.probe.Measurement.tDIVW1Margin "Link to this definition")

    tDIVW2Margin *= 'tDIVW2 Margin'*[](#keysight.ads.hsd.memory.probe.Measurement.tDIVW2Margin "Link to this definition")

    vDIVWMargin *= 'vDIVW Margin'*[](#keysight.ads.hsd.memory.probe.Measurement.vDIVWMargin "Link to this definition")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.probe.SignalData[](#keysight.ads.hsd.memory.probe.SignalData "Link to this definition")
:   Bases: `object`

*class* keysight.ads.hsd.memory.probe.SignalPortType[](#keysight.ads.hsd.memory.probe.SignalPortType "Link to this definition")
:   Bases: `object`

*class* keysight.ads.hsd.memory.probe.ProbeMeasurementSettings[](#keysight.ads.hsd.memory.probe.ProbeMeasurementSettings "Link to this definition")
:   Bases: `object`

    *property* ber\_list*: str*[](#keysight.ads.hsd.memory.probe.ProbeMeasurementSettings.ber_list "Link to this definition")

    *property* enable\_ber\_list*: bool*[](#keysight.ads.hsd.memory.probe.ProbeMeasurementSettings.enable_ber_list "Link to this definition")

    *property* enable\_waveform\_segment*: bool*[](#keysight.ads.hsd.memory.probe.ProbeMeasurementSettings.enable_waveform_segment "Link to this definition")

    *property* extrapolate\_ber*: bool*[](#keysight.ads.hsd.memory.probe.ProbeMeasurementSettings.extrapolate_ber "Link to this definition")

    *property* target\_ber*: float*[](#keysight.ads.hsd.memory.probe.ProbeMeasurementSettings.target_ber "Link to this definition")

    *property* timing\_bath\_tub*: str*[](#keysight.ads.hsd.memory.probe.ProbeMeasurementSettings.timing_bath_tub "Link to this definition")

    *property* use\_old\_measurement\_name*: bool*[](#keysight.ads.hsd.memory.probe.ProbeMeasurementSettings.use_old_measurement_name "Link to this definition")

    *property* voltage\_bath\_tub*: float*[](#keysight.ads.hsd.memory.probe.ProbeMeasurementSettings.voltage_bath_tub "Link to this definition")

    *property* waveform\_collection\_segment*: str*[](#keysight.ads.hsd.memory.probe.ProbeMeasurementSettings.waveform_collection_segment "Link to this definition")

*class* keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings "Link to this definition")
:   Bases: `object`

    *property* align\_dq\_mask\_with\_eye*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.align_dq_mask_with_eye "Link to this definition")

    *property* dq\_eye\_mask\_file\_path*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.dq_eye_mask_file_path "Link to this definition")

    *property* enable\_dq\_eye\_mask\_file*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.enable_dq_eye_mask_file "Link to this definition")

    *property* group\_probe\_dq\_box*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.group_probe_dq_box "Link to this definition")

    *property* probe\_vih\_dq\_ac*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.probe_vih_dq_ac "Link to this definition")

    *property* probe\_vih\_dq\_dc*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.probe_vih_dq_dc "Link to this definition")

    *property* probe\_vil\_dq\_ac*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.probe_vil_dq_ac "Link to this definition")

    *property* probe\_vil\_dq\_dc*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.probe_vil_dq_dc "Link to this definition")

    *property* probe\_vref\_dq*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.probe_vref_dq "Link to this definition")

    *property* tdivw2\_dq*: float*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.tdivw2_dq "Link to this definition")

    *property* tdivw\_dq*: float*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.tdivw_dq "Link to this definition")

    *property* use\_custom\_mask\_dq*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.use_custom_mask_dq "Link to this definition")

    *property* use\_internal\_probe\_vref\_dq*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings.use_internal_probe_vref_dq "Link to this definition")

*class* keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings "Link to this definition")
:   Bases: `object`

    *property* align\_ca\_mask\_with\_eye*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.align_ca_mask_with_eye "Link to this definition")

    *property* ca\_eye\_mask\_file\_path*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.ca_eye_mask_file_path "Link to this definition")

    *property* enable\_ca\_eye\_mask\_file*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.enable_ca_eye_mask_file "Link to this definition")

    *property* group\_probe\_ca\_box*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.group_probe_ca_box "Link to this definition")

    *property* probe\_vih\_ca\_ac*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.probe_vih_ca_ac "Link to this definition")

    *property* probe\_vih\_ca\_dc*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.probe_vih_ca_dc "Link to this definition")

    *property* probe\_vil\_ca\_ac*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.probe_vil_ca_ac "Link to this definition")

    *property* probe\_vil\_ca\_dc*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.probe_vil_ca_dc "Link to this definition")

    *property* probe\_vref\_ca*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.probe_vref_ca "Link to this definition")

    *property* tcivw2\_ca*: float*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.tcivw2_ca "Link to this definition")

    *property* tcivw\_ca*: float*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.tcivw_ca "Link to this definition")

    *property* use\_custom\_mask\_ca*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.use_custom_mask_ca "Link to this definition")

    *property* use\_internal\_probe\_vref\_ca*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings.use_internal_probe_vref_ca "Link to this definition")

*class* keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings "Link to this definition")
:   Bases: `object`

    *property* align\_cs\_mask\_with\_eye*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.align_cs_mask_with_eye "Link to this definition")

    *property* cs\_eye\_mask\_file\_path*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.cs_eye_mask_file_path "Link to this definition")

    *property* enable\_cs\_eye\_mask\_file*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.enable_cs_eye_mask_file "Link to this definition")

    *property* group\_probe\_cs\_box*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.group_probe_cs_box "Link to this definition")

    *property* probe\_vih\_cs\_ac*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.probe_vih_cs_ac "Link to this definition")

    *property* probe\_vih\_cs\_dc*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.probe_vih_cs_dc "Link to this definition")

    *property* probe\_vil\_cs\_ac*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.probe_vil_cs_ac "Link to this definition")

    *property* probe\_vil\_cs\_dc*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.probe_vil_cs_dc "Link to this definition")

    *property* probe\_vref\_cs*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.probe_vref_cs "Link to this definition")

    *property* tcsivw*: float*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.tcsivw "Link to this definition")

    *property* tcsivw2*: float*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.tcsivw2 "Link to this definition")

    *property* use\_custom\_mask\_cs*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.use_custom_mask_cs "Link to this definition")

    *property* use\_internal\_probe\_vref\_cs*: bool*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings.use_internal_probe_vref_cs "Link to this definition")

*class* keysight.ads.hsd.memory.probe.ProbeSingleEndedCkStrobeInputVoltageSettings[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCkStrobeInputVoltageSettings "Link to this definition")
:   Bases: `object`

    *property* probe\_vih\_se\_ck*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCkStrobeInputVoltageSettings.probe_vih_se_ck "Link to this definition")

    *property* probe\_vih\_se\_dqs*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCkStrobeInputVoltageSettings.probe_vih_se_dqs "Link to this definition")

    *property* probe\_vil\_se\_ck*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCkStrobeInputVoltageSettings.probe_vil_se_ck "Link to this definition")

    *property* probe\_vil\_se\_dqs*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCkStrobeInputVoltageSettings.probe_vil_se_dqs "Link to this definition")

    *property* probe\_vref\_ck*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCkStrobeInputVoltageSettings.probe_vref_ck "Link to this definition")

    *property* probe\_vref\_dqs*: str*[](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCkStrobeInputVoltageSettings.probe_vref_dqs "Link to this definition")

*class* keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings[](#keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings "Link to this definition")
:   Bases: `object`

    *property* probe\_vih\_diff\_ck*: str*[](#keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings.probe_vih_diff_ck "Link to this definition")

    *property* probe\_vih\_diff\_ck\_ac*: str*[](#keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings.probe_vih_diff_ck_ac "Link to this definition")

    *property* probe\_vih\_diff\_dqs*: str*[](#keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings.probe_vih_diff_dqs "Link to this definition")

    *property* probe\_vih\_diff\_dqs\_ac*: str*[](#keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings.probe_vih_diff_dqs_ac "Link to this definition")

    *property* probe\_vil\_diff\_ck*: str*[](#keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings.probe_vil_diff_ck "Link to this definition")

    *property* probe\_vil\_diff\_ck\_ac*: str*[](#keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings.probe_vil_diff_ck_ac "Link to this definition")

    *property* probe\_vil\_diff\_dqs*: str*[](#keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings.probe_vil_diff_dqs "Link to this definition")

    *property* probe\_vil\_diff\_dqs\_ac*: str*[](#keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings.probe_vil_diff_dqs_ac "Link to this definition")

*class* keysight.ads.hsd.memory.probe.ProbeAdvancedSettings[](#keysight.ads.hsd.memory.probe.ProbeAdvancedSettings "Link to this definition")
:   Bases: `object`

    *property* amplitude\_resolution*: str*[](#keysight.ads.hsd.memory.probe.ProbeAdvancedSettings.amplitude_resolution "Link to this definition")

    *property* center\_eye\_for\_transient\_and\_statistical\_mode*: bool*[](#keysight.ads.hsd.memory.probe.ProbeAdvancedSettings.center_eye_for_transient_and_statistical_mode "Link to this definition")

    *property* enable\_transient\_block\_sizing*: bool*[](#keysight.ads.hsd.memory.probe.ProbeAdvancedSettings.enable_transient_block_sizing "Link to this definition")

    *property* lower\_eye\_boundary\_percentage*: float*[](#keysight.ads.hsd.memory.probe.ProbeAdvancedSettings.lower_eye_boundary_percentage "Link to this definition")

    *property* time\_resolution*: int*[](#keysight.ads.hsd.memory.probe.ProbeAdvancedSettings.time_resolution "Link to this definition")

    *property* time\_to\_skip\_for\_stable\_waveform*: float*[](#keysight.ads.hsd.memory.probe.ProbeAdvancedSettings.time_to_skip_for_stable_waveform "Link to this definition")

    *property* transient\_block\_size*: float*[](#keysight.ads.hsd.memory.probe.ProbeAdvancedSettings.transient_block_size "Link to this definition")

    *property* upper\_eye\_boundary\_percentage*: float*[](#keysight.ads.hsd.memory.probe.ProbeAdvancedSettings.upper_eye_boundary_percentage "Link to this definition")

*class* keysight.ads.hsd.memory.probe.WriteLevelingSettings[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings "Link to this definition")
:   Bases: `object`

    *property* enable\_transient\_block\_sizing*: bool*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.enable_transient_block_sizing "Link to this definition")

    *property* transient\_block\_size*: float*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.transient_block_size "Link to this definition")

    *property* write\_leveling\_lower\_burst\_threshold\_dqs*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_lower_burst_threshold_dqs "Link to this definition")

    *property* write\_leveling\_lower\_single\_ended\_threshold\_ck*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_lower_single_ended_threshold_ck "Link to this definition")

    *property* write\_leveling\_lower\_single\_ended\_threshold\_dqs*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_lower_single_ended_threshold_dqs "Link to this definition")

    *property* write\_leveling\_lower\_threshold\_ca*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_lower_threshold_ca "Link to this definition")

    *property* write\_leveling\_lower\_threshold\_ck*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_lower_threshold_ck "Link to this definition")

    *property* write\_leveling\_lower\_threshold\_dq*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_lower_threshold_dq "Link to this definition")

    *property* write\_leveling\_upper\_burst\_threshold\_dqs*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_upper_burst_threshold_dqs "Link to this definition")

    *property* write\_leveling\_upper\_single\_ended\_threshold\_ck*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_upper_single_ended_threshold_ck "Link to this definition")

    *property* write\_leveling\_upper\_single\_ended\_threshold\_dqs*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_upper_single_ended_threshold_dqs "Link to this definition")

    *property* write\_leveling\_upper\_threshold\_ca*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_upper_threshold_ca "Link to this definition")

    *property* write\_leveling\_upper\_threshold\_ck*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_upper_threshold_ck "Link to this definition")

    *property* write\_leveling\_upper\_threshold\_dq*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_upper_threshold_dq "Link to this definition")

    *property* write\_leveling\_use\_internal\_vref\_ca*: bool*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_use_internal_vref_ca "Link to this definition")

    *property* write\_leveling\_use\_internal\_vref\_dq*: bool*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_use_internal_vref_dq "Link to this definition")

    *property* write\_leveling\_vref\_ca*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_vref_ca "Link to this definition")

    *property* write\_leveling\_vref\_ck*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_vref_ck "Link to this definition")

    *property* write\_leveling\_vref\_dq*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_vref_dq "Link to this definition")

    *property* write\_leveling\_vref\_dqs*: str*[](#keysight.ads.hsd.memory.probe.WriteLevelingSettings.write_leveling_vref_dqs "Link to this definition")

*class* keysight.ads.hsd.memory.probe.ProbeConfiguration[](#keysight.ads.hsd.memory.probe.ProbeConfiguration "Link to this definition")
:   Bases: `object`

    *property* advanced\_settings*: [ProbeAdvancedSettings](#keysight.ads.hsd.memory.probe.ProbeAdvancedSettings "keysight.ads.hsd.memory.probe.ProbeAdvancedSettings")*[](#keysight.ads.hsd.memory.probe.ProbeConfiguration.advanced_settings "Link to this definition")

    *property* differential\_ck\_strobe\_input\_voltage\_settings*: [ProbeDifferentialCkStrobeInputVoltageSettings](#keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings "keysight.ads.hsd.memory.probe.ProbeDifferentialCkStrobeInputVoltageSettings")*[](#keysight.ads.hsd.memory.probe.ProbeConfiguration.differential_ck_strobe_input_voltage_settings "Link to this definition")

    *property* measurement\_settings*: [ProbeMeasurementSettings](#keysight.ads.hsd.memory.probe.ProbeMeasurementSettings "keysight.ads.hsd.memory.probe.ProbeMeasurementSettings")*[](#keysight.ads.hsd.memory.probe.ProbeConfiguration.measurement_settings "Link to this definition")

    *property* single\_ended\_ca\_ctrl\_input\_voltage\_settings*: [ProbeSingleEndedCaCtrlInputVoltageSettings](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings "keysight.ads.hsd.memory.probe.ProbeSingleEndedCaCtrlInputVoltageSettings")*[](#keysight.ads.hsd.memory.probe.ProbeConfiguration.single_ended_ca_ctrl_input_voltage_settings "Link to this definition")

    *property* single\_ended\_ck\_strobe\_input\_voltage\_settings*: [ProbeSingleEndedCkStrobeInputVoltageSettings](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCkStrobeInputVoltageSettings "keysight.ads.hsd.memory.probe.ProbeSingleEndedCkStrobeInputVoltageSettings")*[](#keysight.ads.hsd.memory.probe.ProbeConfiguration.single_ended_ck_strobe_input_voltage_settings "Link to this definition")

    *property* single\_ended\_cs\_input\_voltage\_settings*: [ProbeSingleEndedCsInputVoltageSettings](#keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings "keysight.ads.hsd.memory.probe.ProbeSingleEndedCsInputVoltageSettings")*[](#keysight.ads.hsd.memory.probe.ProbeConfiguration.single_ended_cs_input_voltage_settings "Link to this definition")

    *property* single\_ended\_data\_input\_voltage\_settings*: [ProbeSingleEndedDataInputVoltageSettings](#keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings "keysight.ads.hsd.memory.probe.ProbeSingleEndedDataInputVoltageSettings")*[](#keysight.ads.hsd.memory.probe.ProbeConfiguration.single_ended_data_input_voltage_settings "Link to this definition")

    *property* write\_leveling\_settings*: [WriteLevelingSettings](#keysight.ads.hsd.memory.probe.WriteLevelingSettings "keysight.ads.hsd.memory.probe.WriteLevelingSettings")*[](#keysight.ads.hsd.memory.probe.ProbeConfiguration.write_leveling_settings "Link to this definition")

*class* keysight.ads.hsd.memory.probe.DesignExplorationSettings[](#keysight.ads.hsd.memory.probe.DesignExplorationSettings "Link to this definition")
:   Bases: `object`

    *property* design\_exploration\_limit\_path*: str*[](#keysight.ads.hsd.memory.probe.DesignExplorationSettings.design_exploration_limit_path "Link to this definition")

    *property* design\_exploration\_path*: str*[](#keysight.ads.hsd.memory.probe.DesignExplorationSettings.design_exploration_path "Link to this definition")

    *property* enable\_csv\_report*: bool*[](#keysight.ads.hsd.memory.probe.DesignExplorationSettings.enable_csv_report "Link to this definition")

    *property* enable\_design\_exploration*: bool*[](#keysight.ads.hsd.memory.probe.DesignExplorationSettings.enable_design_exploration "Link to this definition")

    *property* enable\_dynamic\_report*: bool*[](#keysight.ads.hsd.memory.probe.DesignExplorationSettings.enable_dynamic_report "Link to this definition")

    *property* enable\_html\_report*: bool*[](#keysight.ads.hsd.memory.probe.DesignExplorationSettings.enable_html_report "Link to this definition")

    *property* export\_multiple\_report*: bool*[](#keysight.ads.hsd.memory.probe.DesignExplorationSettings.export_multiple_report "Link to this definition")

    *property* sort\_report\_table\_data\_selection*: str*[](#keysight.ads.hsd.memory.probe.DesignExplorationSettings.sort_report_table_data_selection "Link to this definition")

*class* keysight.ads.hsd.memory.probe.Probe[](#keysight.ads.hsd.memory.probe.Probe "Link to this definition")
:   Bases: `object`

    MemoryProbe class.

    add\_aggressor\_signals(*signal\_keys: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.add_aggressor_signals "Link to this definition")
    :   Add aggressor signals to selected aggressor signal list.

        Aggressor signals will be added if valid available aggressor signal keys are provided.
        Flow: Crosstalk analysis

        Parameters:
        :   **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) to add.

        Return type:
        :   None

    add\_all\_aggressor\_signals() → None[](#keysight.ads.hsd.memory.probe.Probe.add_all_aggressor_signals "Link to this definition")
    :   Add all the available aggressor signals.

        All the available aggressor signals will be added.
        Flow: CrossTalk analysis

        Return type:
        :   None

    add\_all\_signals() → None[](#keysight.ads.hsd.memory.probe.Probe.add_all_signals "Link to this definition")
    :   Select all the available signals.

        All the available signals will be added.
        Flow: Measurement, WriteLeveling

        Return type:
        :   None

    add\_measurements(*signal\_keys: str | list[str]*, *measurements: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.add_measurements "Link to this definition")

    add\_measurements(*signal\_keys: str | list[str]*, *measurements: [Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") | list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")]*) → None
    :   Add measurements for signals.

        Measurements will be added for the selected signals if valid selected signal keys and available measurements are provided.
        Flow: Measurement

        Parameters:
        :   * **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the measurements are to be added.
            * **measurements** ([*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") *|* *list* *[*[*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")*]* *|* *str* *|* *list**[**str**]*) – The measurement(s) to be added.

        Return type:
        :   None

    add\_measurements\_for\_design\_exploration(*signal\_keys: str | list[str]*, *measurements: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.add_measurements_for_design_exploration "Link to this definition")

    add\_measurements\_for\_design\_exploration(*signal\_keys: str | list[str]*, *measurements: [Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") | list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")]*) → None
    :   Add measurements for design exploration for signals.

        Measurements will be added for design exploration if valid selected signal keys and available measurements are provided.
        Flow: Measurement

        Parameters:
        :   * **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the measurements are to be added.
            * **measurements** ([*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") *|* *list**[*[*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")*]* *|* *str* *|* *list**[**str**]*) – The measurement(s) to be added.

        Return type:
        :   None

    add\_reference\_signals(*signal\_keys: str | list[str]*, *measurements: str | list[str]*, *reference\_signal\_keys: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.add_reference_signals "Link to this definition")

    add\_reference\_signals(*signal\_keys: str | list[str]*, *measurements: [Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") | list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")]*, *reference\_signal\_keys: str | list[str]*) → None
    :   Add reference signals for specified measurements for specified signals.

        Reference signals will be added if valid selected signal keys, measurements, and available reference signal keys are provided.
        Flow: Measurement

        Parameters:
        :   * **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the reference signals are to be added.
            * **measurements** ([*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") *|* *list**[*[*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")*]* *|* *str* *|* *list**[**str**]*) – The measurement(s) for which the reference signals are to be added.
            * **reference\_signal\_keys** (*str* *|* *list**[**str**]*) – The reference signal key(s) to be added.

        Return type:
        :   None

    add\_signals(*signal\_keys: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.add_signals "Link to this definition")
    :   Add signals to the selected signal list.

        Signals will be added if valid available signal keys are provided.
        Flow: Measurement, WriteLeveling

        Parameters:
        :   **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) to add.

        Return type:
        :   None

    add\_test\_points(*signal\_keys: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.add_test_points "Link to this definition")
    :   Add test points to selected test point list.

        Test points will be added if valid available test point signal keys are provided.
        Flow: Crosstalk analysis

        Parameters:
        :   **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) to select.

        Return type:
        :   None

    *property* all\_aggressor\_signals*: list[str]*[](#keysight.ads.hsd.memory.probe.Probe.all_aggressor_signals "Link to this definition")
    :   Retrieve all the aggressor signals.

        Returns all the aggressor signals (available and selected).
        Flow: CrossTalk analysis

        Returns:
        :   **list[str]**

        Return type:
        :   All the aggressor signals.

    *property* all\_signals*: list[str]*[](#keysight.ads.hsd.memory.probe.Probe.all_signals "Link to this definition")
    :   Retrieve all the signals.

        Returns all the signals in the design (available and selected).
        Flow: Measurement, WriteLeveling

        Returns:
        :   **list[str]**

        Return type:
        :   All the signals.

    *property* available\_aggressor\_signals*: list[str]*[](#keysight.ads.hsd.memory.probe.Probe.available_aggressor_signals "Link to this definition")
    :   Retrieve the available aggressor signals.

        Returns the available aggressor signals, not yet selected.
        Flow: Crosstalk analysis

        Returns:
        :   **list[str]**

        Return type:
        :   The available aggressor signals.

    available\_measurements(*signal\_keys: str | list[str]*) → list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")][](#keysight.ads.hsd.memory.probe.Probe.available_measurements "Link to this definition")
    :   Retrieve the available measurements.

        Returns the available measurements if valid selected signal keys are provided.
        Flow: Measurement

        Parameters:
        :   **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the available measurements are to be retrieved.

        Returns:
        :   **list[str]**

        Return type:
        :   The available measurements.

    available\_measurements\_for\_design\_exploration(*signal\_keys: str | list[str]*) → list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")][](#keysight.ads.hsd.memory.probe.Probe.available_measurements_for_design_exploration "Link to this definition")
    :   Retrieve the available measurements for design exploration.

        Returns the available measurements for design exploration if valid selected signal keys are provided.
        Flow: Measurement, Crosstalk analysis

        Parameters:
        :   **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the available measurements are to be retrieved.

        Returns:
        :   **list[str]**

        Return type:
        :   The available measurements for design exploration.

    available\_reference\_signals(*signal\_keys: str | list[str]*, *measurements: str | list[str]*) → list[str][](#keysight.ads.hsd.memory.probe.Probe.available_reference_signals "Link to this definition")

    available\_reference\_signals(*signal\_keys: str | list[str]*, *measurements: [Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") | list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")]*) → list[str]
    :   Retrieve the available reference signals.

        Returns the available reference signals if valid selected signal keys and measurements are provided.
        Flow: Measurement

        Parameters:
        :   * **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the available reference signals are to be retrieved.
            * **measurements** ([*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") *|* *list* *[*[*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")*]* *|* *str* *|* *list**[**str**]*) – The measurement(s) for which the available reference signals are to be retrieved.

        Returns:
        :   **list[str]**

        Return type:
        :   The available reference signals.

    *property* available\_signals*: list[str]*[](#keysight.ads.hsd.memory.probe.Probe.available_signals "Link to this definition")
    :   Retrieve the available signals.

        Returns the available signals, not yet selected.
        Flow: Measurement, WriteLeveling

        Returns:
        :   **list[str]**

        Return type:
        :   The available signals.

    *property* available\_test\_points*: list[str]*[](#keysight.ads.hsd.memory.probe.Probe.available_test_points "Link to this definition")
    :   Retrieve the available test points.

        Returns the available test points.
        Flow: Crosstalk analysis

        Returns:
        :   **list[str]**

        Return type:
        :   The available test points.

    design\_exploration\_limits(*signal\_keys: str | list[str]*, *measurement: str*) → str[](#keysight.ads.hsd.memory.probe.Probe.design_exploration_limits "Link to this definition")

    design\_exploration\_limits(*signal\_keys: str | list[str]*, *measurement: [Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")*) → str
    :   Retrieve the design exploration limits.

        Returns the design exploration limits if valid selected signal keys and selected measurement are provided.
        Flow: Measurement

        Parameters:
        :   * **signal\_keys** (*str* *|* *list**[**str**]*) – The signal keys for which the design exploration limits are to be retrieved.
            * **measurement** ([*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") *|* *str*) – The measurement name for which the design exploration limits are to be retrieved.

        Returns:
        :   **str**

        Return type:
        :   The design exploration limits.

    *property* design\_exploration\_settings*: [DesignExplorationSettings](#keysight.ads.hsd.memory.probe.DesignExplorationSettings "keysight.ads.hsd.memory.probe.DesignExplorationSettings")*[](#keysight.ads.hsd.memory.probe.Probe.design_exploration_settings "Link to this definition")
    :   Retrieve the design exploration settings.

        Returns the design exploration settings.

        Returns:
        :   **DesignExplorationSettings**

        Return type:
        :   The design exploration settings.

    *property* enable\_design\_exploration*: bool*[](#keysight.ads.hsd.memory.probe.Probe.enable_design_exploration "Link to this definition")
    :   Check if design exploration is enabled.

        Returns whether design exploration is enabled.

        Returns:
        :   **bool**

        Return type:
        :   True if design exploration is enabled, False otherwise.

    *property* flow\_type*: [ProbeFlowType](#keysight.ads.hsd.memory.probe.ProbeFlowType "keysight.ads.hsd.memory.probe.ProbeFlowType")*[](#keysight.ads.hsd.memory.probe.Probe.flow_type "Link to this definition")
    :   Retrieve the flow type of the memory probe.

        Returns:
        :   **MemoryProbeFlowType**

        Return type:
        :   The flow type of the memory probe.

    *property* probe\_configuration*: [ProbeConfiguration](#keysight.ads.hsd.memory.probe.ProbeConfiguration "keysight.ads.hsd.memory.probe.ProbeConfiguration")*[](#keysight.ads.hsd.memory.probe.Probe.probe_configuration "Link to this definition")
    :   Retrieve the probe configuration.

        Returns the probe configuration.

        Returns:
        :   **MemoryProbeConfiguration**

        Return type:
        :   The probe configuration.

    remove\_aggressor\_signals(*signal\_keys: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.remove_aggressor_signals "Link to this definition")
    :   Remove aggressor signals from select aggressor signal list.

        Aggressor signals will be removed if valid selected aggressor signal keys are provided.
        Flow: Crosstalk analysis

        Parameters:
        :   **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) to remove.

        Return type:
        :   None

    remove\_all\_aggressor\_signals() → None[](#keysight.ads.hsd.memory.probe.Probe.remove_all_aggressor_signals "Link to this definition")
    :   Remove all the selected aggressor signals.

        All the selected aggressor signals will be removed.
        Flow: Crosstalk analysis

        Return type:
        :   None

    remove\_all\_signals() → None[](#keysight.ads.hsd.memory.probe.Probe.remove_all_signals "Link to this definition")
    :   Remove all the selected signals.

        All the selected signals will be removed.
        Flow: Measurement, WriteLeveling

        Return type:
        :   None

    remove\_measurements(*signal\_keys: str | list[str]*, *measurements: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.remove_measurements "Link to this definition")

    remove\_measurements(*signal\_keys: str | list[str]*, *measurements: [Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") | list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")]*) → None
    :   Remove measurements for signals.

        Measurements will be removed from the selected signals if valid selected signal keys and selected measurements are provided.
        Flow: Measurement

        Parameters:
        :   * **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the measurements are to be removed.
            * **measurements** ([*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") *|* *list* *[*[*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")*]* *|* *str* *|* *list**[**str**]*) – The measurement(s) to be removed.

        Return type:
        :   None

    remove\_measurements\_for\_design\_exploration(*signal\_keys: str | list[str]*, *measurements: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.remove_measurements_for_design_exploration "Link to this definition")

    remove\_measurements\_for\_design\_exploration(*signal\_keys: str | list[str]*, *measurements: [Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") | list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")]*) → None
    :   Remove measurements for design exploration for signals.

        Measurements will be removed for design exploration if valid selected signal keys and selected measurements are provided.
        Flow: Measurement

        Parameters:
        :   * **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the measurements are to be removed.
            * **measurements** ([*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") *|* *list**[*[*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")*]* *|* *str* *|* *list**[**str**]*) – The measurement(s) to be removed.

        Return type:
        :   None

    remove\_reference\_signals(*signal\_keys: str | list[str]*, *measurements: str | list[str]*, *reference\_signal\_keys: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.remove_reference_signals "Link to this definition")

    remove\_reference\_signals(*signal\_keys: str | list[str]*, *measurements: [Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") | list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")]*, *reference\_signal\_keys: str | list[str]*) → None
    :   Remove reference signals for specified measurements for specified signals.

        Reference signals will be removed if valid selected signal keys, measurements, and selected reference signal keys are provided.
        Flow: Measurement

        Parameters:
        :   * **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the reference signals are to be removed.
            * **measurements** ([*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") *|* *list**[*[*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")*]* *|* *str* *|* *list**[**str**]*) – The measurement(s) for which the reference signals are to be removed.
            * **reference\_signal\_keys** (*str* *|* *list**[**str**]*) – The reference signal key(s) to be removed.

        Return type:
        :   None

    remove\_signals(*signal\_keys: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.remove_signals "Link to this definition")
    :   Remove signals from the selected signal list.

        Signals will be removed if valid selected signal keys are provided.
        Flow: Measurement, WriteLeveling

        Parameters:
        :   **signal\_keys** (*str* *|* *list**[**str**]*) – The signal keys to remove.

        Return type:
        :   None

    remove\_test\_points(*signal\_keys: str | list[str]*) → None[](#keysight.ads.hsd.memory.probe.Probe.remove_test_points "Link to this definition")
    :   Remove test points from selected test point list.

        Test points will be removed if valid selected test point signal keys are provided.
        Flow: Crosstalk analysis

        Parameters:
        :   **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) to remove.

        Return type:
        :   None

    save() → None[](#keysight.ads.hsd.memory.probe.Probe.save "Link to this definition")
    :   Save the current settings to the instance.

        Return type:
        :   None

    *property* selected\_aggressor\_signals*: list[str]*[](#keysight.ads.hsd.memory.probe.Probe.selected_aggressor_signals "Link to this definition")
    :   Retrieve the selected aggressor signals.

        Returns the selected aggressor signals.
        Flow: Crosstalk analysis

        Returns:
        :   **list[str]**

        Return type:
        :   The selected aggressor signals.

    selected\_measurements(*signal\_keys: str | list[str]*) → list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")][](#keysight.ads.hsd.memory.probe.Probe.selected_measurements "Link to this definition")
    :   Retrieve the selected measurements.

        Returns the selected measurements if valid selected signal keys are provided.
        Flow: Measurement

        Parameters:
        :   **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the selected measurements are to be retrieved.

        Returns:
        :   **list[str]**

        Return type:
        :   The selected measurements.

    selected\_measurements\_for\_design\_exploration(*signal\_keys: str | list[str]*) → list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")][](#keysight.ads.hsd.memory.probe.Probe.selected_measurements_for_design_exploration "Link to this definition")
    :   Retrieve the selected measurements for design exploration.

        Returns the selected measurements for design exploration if valid selected signal keys are provided.
        Flow: Measurement, Crosstalk analysis

        Parameters:
        :   **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the selected measurements are to be retrieved.

        Returns:
        :   **list[str]**

        Return type:
        :   The selected measurements for design exploration.

    selected\_reference\_signals(*signal\_keys: str | list[str]*, *measurements: str | list[str]*) → list[str][](#keysight.ads.hsd.memory.probe.Probe.selected_reference_signals "Link to this definition")

    selected\_reference\_signals(*signal\_keys: str | list[str]*, *measurements: [Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") | list[[Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")]*) → list[str]
    :   Retrieve the selected reference signals.

        Returns the selected reference signals if valid selected signals and measurements are provided.
        Flow: Measurement

        Parameters:
        :   * **signal\_keys** (*str* *|* *list**[**str**]*) – The signal key(s) for which the selected reference signals are to be retrieved.
            * **measurements** ([*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") *|* *list* *[*[*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")*]* *|* *str* *|* *list**[**str**]*) – The measurement(s) for which the selected reference signals are to be retrieved.

        Returns:
        :   **list[str]**

        Return type:
        :   The selected reference signals.

    *property* selected\_signals*: list[str]*[](#keysight.ads.hsd.memory.probe.Probe.selected_signals "Link to this definition")
    :   Retrieve the selected signals.

        Returns current selected signals.
        Flow: Measurement, WriteLeveling

        Returns:
        :   **list[str]**

        Return type:
        :   The selected signals.

    *property* selected\_test\_points*: list[str]*[](#keysight.ads.hsd.memory.probe.Probe.selected_test_points "Link to this definition")
    :   Retrieve the selected test points.

        Returns the selected test points.
        Flow: Crosstalk analysis

        Returns:
        :   **list[str]**

        Return type:
        :   The selected test points.

    set\_design\_exploration\_limits(*signal\_keys: str | list[str]*, *measurement: str*, *limits: str*) → None[](#keysight.ads.hsd.memory.probe.Probe.set_design_exploration_limits "Link to this definition")

    set\_design\_exploration\_limits(*signal\_keys: str | list[str]*, *measurement: [Measurement](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement")*, *limits: str*) → None
    :   Set the design exploration limits.

        Design exploration limits will be set if valid selected signal keys, selected measurement and limits are provided.
        Flow: Measurement

        Parameters:
        :   * **signal\_keys** (*str* *|* *list**[**str**]*) – The signal keys for which the design exploration limits are to be set.
            * **measurement** ([*Measurement*](#keysight.ads.hsd.memory.probe.Measurement "keysight.ads.hsd.memory.probe.Measurement") *|* *str*) – The measurement name for which the design exploration limits are to be set.
            * **limits** (*str*) – The limits to be set.

        Return type:
        :   None

    *property* write\_leveling\_file\_name*: str*[](#keysight.ads.hsd.memory.probe.Probe.write_leveling_file_name "Link to this definition")
    :   Retrieve the write leveling file name.

        Returns the write leveling file name.
        Flow: WriteLeveling

        Returns:
        :   **str**

        Return type:
        :   The write leveling file name.

    *property* write\_leveling\_signal\_specifier*: str*[](#keysight.ads.hsd.memory.probe.Probe.write_leveling_signal_specifier "Link to this definition")
    :   Retrieve the write leveling signal specifier.

        Returns the write leveling signal specifier.
        Flow: WriteLeveling

        Returns:
        :   **str**

        Return type:
        :   The write leveling signal specifier.


---

<!-- === 来源: reference/hsd/memory/setup.md === -->

# Memory Setup[](#memory-setup "Link to this heading")

## Enumerated types[](#enumerated-types "Link to this heading")

*class* keysight.ads.hsd.memory.setup.DramType[](#keysight.ads.hsd.memory.setup.DramType "Link to this definition")
:   Bases: `EnumWrapper`

    DDR4 *= <DramType.DDR4: 0>*[](#keysight.ads.hsd.memory.setup.DramType.DDR4 "Link to this definition")

    DDR5 *= <DramType.DDR5: 3>*[](#keysight.ads.hsd.memory.setup.DramType.DDR5 "Link to this definition")

    DDR\_X *= <DramType.DDR\_X: 16>*[](#keysight.ads.hsd.memory.setup.DramType.DDR_X "Link to this definition")

    GDDR6 *= <DramType.GDDR6: 5>*[](#keysight.ads.hsd.memory.setup.DramType.GDDR6 "Link to this definition")

    GDDR6X *= <DramType.GDDR6X: 6>*[](#keysight.ads.hsd.memory.setup.DramType.GDDR6X "Link to this definition")

    GDDR7 *= <DramType.GDDR7: 7>*[](#keysight.ads.hsd.memory.setup.DramType.GDDR7 "Link to this definition")

    GDDR\_X *= <DramType.GDDR\_X: 18>*[](#keysight.ads.hsd.memory.setup.DramType.GDDR_X "Link to this definition")

    HBM2 *= <DramType.HBM2: 8>*[](#keysight.ads.hsd.memory.setup.DramType.HBM2 "Link to this definition")

    HBM3 *= <DramType.HBM3: 12>*[](#keysight.ads.hsd.memory.setup.DramType.HBM3 "Link to this definition")

    HBM4 *= <DramType.HBM4: 15>*[](#keysight.ads.hsd.memory.setup.DramType.HBM4 "Link to this definition")

    HBM\_X *= <DramType.HBM\_X: 19>*[](#keysight.ads.hsd.memory.setup.DramType.HBM_X "Link to this definition")

    LPDDR4 *= <DramType.LPDDR4: 1>*[](#keysight.ads.hsd.memory.setup.DramType.LPDDR4 "Link to this definition")

    LPDDR4X *= <DramType.LPDDR4X: 2>*[](#keysight.ads.hsd.memory.setup.DramType.LPDDR4X "Link to this definition")

    LPDDR5 *= <DramType.LPDDR5: 4>*[](#keysight.ads.hsd.memory.setup.DramType.LPDDR5 "Link to this definition")

    LPDDR5X *= <DramType.LPDDR5X: 13>*[](#keysight.ads.hsd.memory.setup.DramType.LPDDR5X "Link to this definition")

    LPDDR6 *= <DramType.LPDDR6: 14>*[](#keysight.ads.hsd.memory.setup.DramType.LPDDR6 "Link to this definition")

    LPDDR\_X *= <DramType.LPDDR\_X: 17>*[](#keysight.ads.hsd.memory.setup.DramType.LPDDR_X "Link to this definition")

    NAND\_X *= <DramType.NAND\_X: 20>*[](#keysight.ads.hsd.memory.setup.DramType.NAND_X "Link to this definition")

    NVDDR *= <DramType.NVDDR: 9>*[](#keysight.ads.hsd.memory.setup.DramType.NVDDR "Link to this definition")

    NVDDR23 *= <DramType.NVDDR23: 10>*[](#keysight.ads.hsd.memory.setup.DramType.NVDDR23 "Link to this definition")

    NVLPDDR4 *= <DramType.NVLPDDR4: 11>*[](#keysight.ads.hsd.memory.setup.DramType.NVLPDDR4 "Link to this definition")

*class* keysight.ads.hsd.memory.setup.DataCycleType[](#keysight.ads.hsd.memory.setup.DataCycleType "Link to this definition")
:   Bases: `EnumWrapper`

    READ *= 'Read'*[](#keysight.ads.hsd.memory.setup.DataCycleType.READ "Link to this definition")

    WRITE *= 'Write'*[](#keysight.ads.hsd.memory.setup.DataCycleType.WRITE "Link to this definition")

*class* keysight.ads.hsd.memory.setup.SignalPortType[](#keysight.ads.hsd.memory.setup.SignalPortType "Link to this definition")
:   Bases: `EnumWrapper`

    DIFFERENTIAL *= 'Differential'*[](#keysight.ads.hsd.memory.setup.SignalPortType.DIFFERENTIAL "Link to this definition")

    SINGLE\_ENDED *= 'SingleEnded'*[](#keysight.ads.hsd.memory.setup.SignalPortType.SINGLE_ENDED "Link to this definition")

*class* keysight.ads.hsd.memory.setup.DataCycleMode[](#keysight.ads.hsd.memory.setup.DataCycleMode "Link to this definition")
:   Bases: `EnumWrapper`

    BURST *= 'Burst'*[](#keysight.ads.hsd.memory.setup.DataCycleMode.BURST "Link to this definition")

    CONTINUOUS *= 'Continuous'*[](#keysight.ads.hsd.memory.setup.DataCycleMode.CONTINUOUS "Link to this definition")

*class* keysight.ads.hsd.memory.setup.BurstMode[](#keysight.ads.hsd.memory.setup.BurstMode "Link to this definition")
:   Bases: `EnumWrapper`

    AUTO *= 'Auto'*[](#keysight.ads.hsd.memory.setup.BurstMode.AUTO "Link to this definition")

    DDR5\_0p5tCK *= 'DDR5\_0.5tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.DDR5_0p5tCK "Link to this definition")

    DDR5\_1p5tCK *= 'DDR5\_1.5tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.DDR5_1p5tCK "Link to this definition")

    DDR5\_1tCK *= 'DDR5\_1tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.DDR5_1tCK "Link to this definition")

    DDR5\_2tCK *= 'DDR5\_2tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.DDR5_2tCK "Link to this definition")

    DDR5\_2tCK\_0010 *= 'DDR5\_2tCK\_0010'*[](#keysight.ads.hsd.memory.setup.BurstMode.DDR5_2tCK_0010 "Link to this definition")

    DDR5\_2tCK\_1110 *= 'DDR5\_2tCK\_1110'*[](#keysight.ads.hsd.memory.setup.BurstMode.DDR5_2tCK_1110 "Link to this definition")

    DDR5\_3tCK *= 'DDR5\_3tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.DDR5_3tCK "Link to this definition")

    DDR5\_4tCK *= 'DDR5\_4tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.DDR5_4tCK "Link to this definition")

    LPDDR\_2p5tWCK *= '2.5 tWCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_2p5tWCK "Link to this definition")

    LPDDR\_Static\_0p5tWCK *= 'Static\_0.5tWCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_0p5tWCK "Link to this definition")

    LPDDR\_Static\_10tCK\_HalfToggle\_2tCK\_FullToggle\_4tCK *= 'Static\_10tCK\_HalfToggle\_2tCK\_FullToggle\_4tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_10tCK_HalfToggle_2tCK_FullToggle_4tCK "Link to this definition")

    LPDDR\_Static\_2p5tWCK *= 'Static\_2.5tWCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_2p5tWCK "Link to this definition")

    LPDDR\_Static\_2tCK\_HalfToggle\_0tCK\_FullToggle\_2tCK *= 'Static\_2tCK\_HalfToggle\_0tCK\_FullToggle\_2tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_2tCK_HalfToggle_0tCK_FullToggle_2tCK "Link to this definition")

    LPDDR\_Static\_2tWCK\_Toggle\_2tWCK *= 'Static\_2tWCK\_Toggle\_2tWCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_2tWCK_Toggle_2tWCK "Link to this definition")

    LPDDR\_Static\_2tWCK\_Toggle\_6tWCK *= 'Static\_2tWCK\_Toggle\_6tWCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_2tWCK_Toggle_6tWCK "Link to this definition")

    LPDDR\_Static\_3tCK\_HalfToggle\_0tCK\_FullToggle\_3tCK *= 'Static\_3tCK\_HalfToggle\_0tCK\_FullToggle\_3tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_3tCK_HalfToggle_0tCK_FullToggle_3tCK "Link to this definition")

    LPDDR\_Static\_4p5tWCK *= 'Static\_4.5tWCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_4p5tWCK "Link to this definition")

    LPDDR\_Static\_4tCK\_HalfToggle\_0tCK\_FullToggle\_3tCK *= 'Static\_4tCK\_HalfToggle\_0tCK\_FullToggle\_3tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_4tCK_HalfToggle_0tCK_FullToggle_3tCK "Link to this definition")

    LPDDR\_Static\_4tWCK\_Toggle\_0tWCK *= 'Static\_4tWCK\_Toggle\_0tWCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_4tWCK_Toggle_0tWCK "Link to this definition")

    LPDDR\_Static\_4tWCK\_Toggle\_4tWCK *= 'Static\_4tWCK\_Toggle\_4tWCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_4tWCK_Toggle_4tWCK "Link to this definition")

    LPDDR\_Static\_5tCK\_HalfToggle\_0tCK\_FullToggle\_3tCK *= 'Static\_5tCK\_HalfToggle\_0tCK\_FullToggle\_3tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_5tCK_HalfToggle_0tCK_FullToggle_3tCK "Link to this definition")

    LPDDR\_Static\_6tCK\_HalfToggle\_0tCK\_FullToggle\_3tCK *= 'Static\_6tCK\_HalfToggle\_0tCK\_FullToggle\_3tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_6tCK_HalfToggle_0tCK_FullToggle_3tCK "Link to this definition")

    LPDDR\_Static\_6tCK\_HalfToggle\_2tCK\_FullToggle\_3tCK *= 'Static\_6tCK\_HalfToggle\_2tCK\_FullToggle\_3tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_6tCK_HalfToggle_2tCK_FullToggle_3tCK "Link to this definition")

    LPDDR\_Static\_7tCK\_HalfToggle\_2tCK\_FullToggle\_4tCK *= 'Static\_7tCK\_HalfToggle\_2tCK\_FullToggle\_4tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_7tCK_HalfToggle_2tCK_FullToggle_4tCK "Link to this definition")

    LPDDR\_Static\_8tCK\_HalfToggle\_2tCK\_FullToggle\_4tCK *= 'Static\_8tCK\_HalfToggle\_2tCK\_FullToggle\_4tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_8tCK_HalfToggle_2tCK_FullToggle_4tCK "Link to this definition")

    LPDDR\_Static\_9tCK\_HalfToggle\_2tCK\_FullToggle\_4tCK *= 'Static\_9tCK\_HalfToggle\_2tCK\_FullToggle\_4tCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Static_9tCK_HalfToggle_2tCK_FullToggle_4tCK "Link to this definition")

    LPDDR\_Toggle\_2p5tWCK *= 'Toggle\_2.5tWCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Toggle_2p5tWCK "Link to this definition")

    LPDDR\_Toggle\_4p5tWCK *= 'Toggle\_4.5tWCK'*[](#keysight.ads.hsd.memory.setup.BurstMode.LPDDR_Toggle_4p5tWCK "Link to this definition")

*class* keysight.ads.hsd.memory.setup.DqSignalPatternType[](#keysight.ads.hsd.memory.setup.DqSignalPatternType "Link to this definition")
:   Bases: `EnumWrapper`

    CONTINUOUS\_1010 *= 'Continuous1010'*[](#keysight.ads.hsd.memory.setup.DqSignalPatternType.CONTINUOUS_1010 "Link to this definition")

    CONTINUOUS\_DATA *= 'ContinuousData'*[](#keysight.ads.hsd.memory.setup.DqSignalPatternType.CONTINUOUS_DATA "Link to this definition")

*class* keysight.ads.hsd.memory.setup.StrobeState[](#keysight.ads.hsd.memory.setup.StrobeState "Link to this definition")
:   Bases: `EnumWrapper`

    DIFFERENTIAL *= <SignalPortTypeEnum.Differential: 0>*[](#keysight.ads.hsd.memory.setup.StrobeState.DIFFERENTIAL "Link to this definition")

    NEGATIVE *= <SignalPortTypeEnum.Negative: 3>*[](#keysight.ads.hsd.memory.setup.StrobeState.NEGATIVE "Link to this definition")

    POSITIVE *= <SignalPortTypeEnum.Positive: 2>*[](#keysight.ads.hsd.memory.setup.StrobeState.POSITIVE "Link to this definition")

    SINGLE\_ENDED *= <SignalPortTypeEnum.SingleEnded: 1>*[](#keysight.ads.hsd.memory.setup.StrobeState.SINGLE_ENDED "Link to this definition")

*class* keysight.ads.hsd.memory.setup.CkState[](#keysight.ads.hsd.memory.setup.CkState "Link to this definition")
:   Bases: `EnumWrapper`

    DIFFERENTIAL *= <SignalPortTypeEnum.Differential: 0>*[](#keysight.ads.hsd.memory.setup.CkState.DIFFERENTIAL "Link to this definition")

    NEGATIVE *= <SignalPortTypeEnum.Negative: 3>*[](#keysight.ads.hsd.memory.setup.CkState.NEGATIVE "Link to this definition")

    POSITIVE *= <SignalPortTypeEnum.Positive: 2>*[](#keysight.ads.hsd.memory.setup.CkState.POSITIVE "Link to this definition")

    SINGLE\_ENDED *= <SignalPortTypeEnum.SingleEnded: 1>*[](#keysight.ads.hsd.memory.setup.CkState.SINGLE_ENDED "Link to this definition")

*class* keysight.ads.hsd.memory.setup.CkDqsSourceSignalMode[](#keysight.ads.hsd.memory.setup.CkDqsSourceSignalMode "Link to this definition")
:   Bases: `EnumWrapper`

    DIFFERENTIAL *= 'Differential'*[](#keysight.ads.hsd.memory.setup.CkDqsSourceSignalMode.DIFFERENTIAL "Link to this definition")

    SINGLE\_ENDED *= 'SingleEnded'*[](#keysight.ads.hsd.memory.setup.CkDqsSourceSignalMode.SINGLE_ENDED "Link to this definition")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.setup.Setup[](#keysight.ads.hsd.memory.setup.Setup "Link to this definition")
:   Bases: `object`

    *property* burst\_length*: NumericStr*[](#keysight.ads.hsd.memory.setup.Setup.burst_length "Link to this definition")

    *property* ca\_to\_ck\_timing*: NumericStr*[](#keysight.ads.hsd.memory.setup.Setup.ca_to_ck_timing "Link to this definition")

    *property* ck\_state*: [CkState](#keysight.ads.hsd.memory.setup.CkState "keysight.ads.hsd.memory.setup.CkState")*[](#keysight.ads.hsd.memory.setup.Setup.ck_state "Link to this definition")

    *property* clock\_strobe\_src\_data\_mode*: [CkDqsSourceSignalMode](#keysight.ads.hsd.memory.setup.CkDqsSourceSignalMode "keysight.ads.hsd.memory.setup.CkDqsSourceSignalMode")*[](#keysight.ads.hsd.memory.setup.Setup.clock_strobe_src_data_mode "Link to this definition")

    *property* cs\_to\_ck\_timing*: NumericStr*[](#keysight.ads.hsd.memory.setup.Setup.cs_to_ck_timing "Link to this definition")

    *property* ctrl\_to\_ck\_timing*: NumericStr*[](#keysight.ads.hsd.memory.setup.Setup.ctrl_to_ck_timing "Link to this definition")

    *property* data\_cycle*: [DataCycleType](#keysight.ads.hsd.memory.setup.DataCycleType "keysight.ads.hsd.memory.setup.DataCycleType")*[](#keysight.ads.hsd.memory.setup.Setup.data_cycle "Link to this definition")

    *property* data\_cycle\_mode*: [DataCycleMode](#keysight.ads.hsd.memory.setup.DataCycleMode "keysight.ads.hsd.memory.setup.DataCycleMode")*[](#keysight.ads.hsd.memory.setup.Setup.data_cycle_mode "Link to this definition")

    *property* data\_signal\_per\_strobe*: NumericStr*[](#keysight.ads.hsd.memory.setup.Setup.data_signal_per_strobe "Link to this definition")

    *property* dq\_signal\_pattern*: [DqSignalPatternType](#keysight.ads.hsd.memory.setup.DqSignalPatternType "keysight.ads.hsd.memory.setup.DqSignalPatternType")*[](#keysight.ads.hsd.memory.setup.Setup.dq_signal_pattern "Link to this definition")

    *property* dram\_type*: [DramType](#keysight.ads.hsd.memory.setup.DramType "keysight.ads.hsd.memory.setup.DramType")*[](#keysight.ads.hsd.memory.setup.Setup.dram_type "Link to this definition")

    *property* modulation\_flavor*: NumericStr*[](#keysight.ads.hsd.memory.setup.Setup.modulation_flavor "Link to this definition")

    *property* modulation\_type*: NumericStr*[](#keysight.ads.hsd.memory.setup.Setup.modulation_type "Link to this definition")

    *property* pathfinding\_mode*: bool*[](#keysight.ads.hsd.memory.setup.Setup.pathfinding_mode "Link to this definition")

    *property* postamble\_mode*: [BurstMode](#keysight.ads.hsd.memory.setup.BurstMode "keysight.ads.hsd.memory.setup.BurstMode")*[](#keysight.ads.hsd.memory.setup.Setup.postamble_mode "Link to this definition")

    *property* preamble\_mode*: [BurstMode](#keysight.ads.hsd.memory.setup.BurstMode "keysight.ads.hsd.memory.setup.BurstMode")*[](#keysight.ads.hsd.memory.setup.Setup.preamble_mode "Link to this definition")

    *property* re\_state*: [CkState](#keysight.ads.hsd.memory.setup.CkState "keysight.ads.hsd.memory.setup.CkState")*[](#keysight.ads.hsd.memory.setup.Setup.re_state "Link to this definition")

    save() → None[](#keysight.ads.hsd.memory.setup.Setup.save "Link to this definition")
    :   Save the current settings to the instance.

        Return type:
        :   None

    *property* speed\_grade*: NumericStr*[](#keysight.ads.hsd.memory.setup.Setup.speed_grade "Link to this definition")

    *property* strobe\_state*: [StrobeState](#keysight.ads.hsd.memory.setup.StrobeState "keysight.ads.hsd.memory.setup.StrobeState")*[](#keysight.ads.hsd.memory.setup.Setup.strobe_state "Link to this definition")

    *property* strobe\_to\_ck\_timing*: NumericStr*[](#keysight.ads.hsd.memory.setup.Setup.strobe_to_ck_timing "Link to this definition")


---

<!-- === 来源: reference/hsd/memory/simulator.md === -->

# Memory Interface Simulator[](#memory-interface-simulator "Link to this heading")

*class* keysight.ads.hsd.memory.simulator.SimulationMode[](#keysight.ads.hsd.memory.simulator.SimulationMode "Link to this definition")
:   Bases: `EnumWrapper`

    BIT\_BY\_BIT *= <SimulationMode.BITBYBIT: 0>*[](#keysight.ads.hsd.memory.simulator.SimulationMode.BIT_BY_BIT "Link to this definition")

    STATISTICAL *= <SimulationMode.STATISTICAL: 1>*[](#keysight.ads.hsd.memory.simulator.SimulationMode.STATISTICAL "Link to this definition")

    S\_PARAMETER *= <SimulationMode.SPARAMETER: 4>*[](#keysight.ads.hsd.memory.simulator.SimulationMode.S_PARAMETER "Link to this definition")

    TRANSIENT *= <SimulationMode.TRANSIENT: 5>*[](#keysight.ads.hsd.memory.simulator.SimulationMode.TRANSIENT "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.PassivityMode[](#keysight.ads.hsd.memory.simulator.PassivityMode "Link to this definition")
:   Bases: `EnumWrapper`

    NONE *= <PassivityMode.NONE: 0>*[](#keysight.ads.hsd.memory.simulator.PassivityMode.NONE "Link to this definition")

    NORMAL *= <PassivityMode.NORMAL: 1>*[](#keysight.ads.hsd.memory.simulator.PassivityMode.NORMAL "Link to this definition")

    STRICT *= <PassivityMode.STRICT: 2>*[](#keysight.ads.hsd.memory.simulator.PassivityMode.STRICT "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.ToleranceMode[](#keysight.ads.hsd.memory.simulator.ToleranceMode "Link to this definition")
:   Bases: `EnumWrapper`

    AUTO *= <ToleranceMode.AUTO: 1>*[](#keysight.ads.hsd.memory.simulator.ToleranceMode.AUTO "Link to this definition")

    RELAX *= <ToleranceMode.RELAX: 0>*[](#keysight.ads.hsd.memory.simulator.ToleranceMode.RELAX "Link to this definition")

    STRICT *= <ToleranceMode.STRICT: 2>*[](#keysight.ads.hsd.memory.simulator.ToleranceMode.STRICT "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.TimeStepControlMethod[](#keysight.ads.hsd.memory.simulator.TimeStepControlMethod "Link to this definition")
:   Bases: `EnumWrapper`

    FIXED *= <TimeStepControlMethod.FIXED: 0>*[](#keysight.ads.hsd.memory.simulator.TimeStepControlMethod.FIXED "Link to this definition")

    ITERATION\_COUNT *= <TimeStepControlMethod.ITERATION\_COUNT: 1>*[](#keysight.ads.hsd.memory.simulator.TimeStepControlMethod.ITERATION_COUNT "Link to this definition")

    TRUNC\_ERROR *= <TimeStepControlMethod.TRUNC\_ERROR: 2>*[](#keysight.ads.hsd.memory.simulator.TimeStepControlMethod.TRUNC_ERROR "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.IntegrationMethod[](#keysight.ads.hsd.memory.simulator.IntegrationMethod "Link to this definition")
:   Bases: `EnumWrapper`

    GEAR *= <IntegrationMethod.GEAR: 1>*[](#keysight.ads.hsd.memory.simulator.IntegrationMethod.GEAR "Link to this definition")

    TRAPEZOIDAL *= <IntegrationMethod.TRAPEZOIDAL: 0>*[](#keysight.ads.hsd.memory.simulator.IntegrationMethod.TRAPEZOIDAL "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern "Link to this definition")
:   Bases: `EnumWrapper`

    CONTINUOUS\_BITS *= <XtlkAnalysisBitPattern.CONTINUOUS\_BITS: 0>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern.CONTINUOUS_BITS "Link to this definition")

    SINGLE\_BIT *= <XtlkAnalysisBitPattern.SINGLE\_BIT: 1>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern.SINGLE_BIT "Link to this definition")

    STEP\_FALL *= <XtlkAnalysisBitPattern.STEP\_FALL: 3>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern.STEP_FALL "Link to this definition")

    STEP\_RISE *= <XtlkAnalysisBitPattern.STEP\_RISE: 2>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern.STEP_RISE "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.CrosstalkAnalysisVictimMode[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisVictimMode "Link to this definition")
:   Bases: `EnumWrapper`

    HIGHSTATE *= <XtlkAnalysisVictimMode.HIGHSTATE: 0>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisVictimMode.HIGHSTATE "Link to this definition")

    LOWSTATE *= <XtlkAnalysisVictimMode.LOWSTATE: 1>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisVictimMode.LOWSTATE "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.SparamSweepType[](#keysight.ads.hsd.memory.simulator.SparamSweepType "Link to this definition")
:   Bases: `EnumWrapper`

    LINEAR *= <SweepType.LINEAR: 1>*[](#keysight.ads.hsd.memory.simulator.SparamSweepType.LINEAR "Link to this definition")

    LOG *= <SweepType.LOG: 2>*[](#keysight.ads.hsd.memory.simulator.SparamSweepType.LOG "Link to this definition")

    SINGLE\_POINT *= <SweepType.SINGLE\_POINT: 0>*[](#keysight.ads.hsd.memory.simulator.SparamSweepType.SINGLE_POINT "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.SparamSweepMode[](#keysight.ads.hsd.memory.simulator.SparamSweepMode "Link to this definition")
:   Bases: `EnumWrapper`

    CENTER\_SPAN *= <SweepMode.CENTER\_SPAN: 1>*[](#keysight.ads.hsd.memory.simulator.SparamSweepMode.CENTER_SPAN "Link to this definition")

    START\_STOP *= <SweepMode.START\_STOP: 0>*[](#keysight.ads.hsd.memory.simulator.SparamSweepMode.START_STOP "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.SparamTermPlacement[](#keysight.ads.hsd.memory.simulator.SparamTermPlacement "Link to this definition")
:   Bases: `EnumWrapper`

    CONTROLLER\_DIE\_TO\_MEMORY\_DIE *= <TermPlacementOption.CONTROLLER\_DIE\_TO\_MEMORY\_DIE: 2>*[](#keysight.ads.hsd.memory.simulator.SparamTermPlacement.CONTROLLER_DIE_TO_MEMORY_DIE "Link to this definition")

    CONTROLLER\_DIE\_TO\_MEMORY\_PACKAGE *= <TermPlacementOption.CONTROLLER\_DIE\_TO\_MEMORY\_PACKAGE: 3>*[](#keysight.ads.hsd.memory.simulator.SparamTermPlacement.CONTROLLER_DIE_TO_MEMORY_PACKAGE "Link to this definition")

    CONTROLLER\_PACKAGE\_TO\_MEMORY\_DIE *= <TermPlacementOption.CONTROLLER\_PACKAGE\_TO\_MEMORY\_DIE: 4>*[](#keysight.ads.hsd.memory.simulator.SparamTermPlacement.CONTROLLER_PACKAGE_TO_MEMORY_DIE "Link to this definition")

    CONTROLLER\_PACKAGE\_TO\_MEMORY\_PACKAGE *= <TermPlacementOption.CONTROLLER\_PACKAGE\_TO\_MEMORY\_PACKAGE: 5>*[](#keysight.ads.hsd.memory.simulator.SparamTermPlacement.CONTROLLER_PACKAGE_TO_MEMORY_PACKAGE "Link to this definition")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting "Link to this definition")
:   Bases: `CommonConvolutionSettings`

    *property* anti\_aliasing\_window\_size*: int*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.anti_aliasing_window_size "Link to this definition")

    *property* max\_impulse\_response\_frequency*: float | None*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.max_impulse_response_frequency "Link to this definition")

    *property* max\_impulse\_response\_length*: int*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.max_impulse_response_length "Link to this definition")

    *property* number\_of\_time\_points\_per\_UI*: int*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.number_of_time_points_per_UI "Link to this definition")

    *property* passivity\_mode*: [PassivityMode](#keysight.ads.hsd.memory.simulator.PassivityMode "keysight.ads.hsd._common.simulators.PassivityMode")*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.passivity_mode "Link to this definition")

    *property* reuse\_cached\_impulse\_response*: bool*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.reuse_cached_impulse_response "Link to this definition")

    *property* save\_characterization\_result*: bool*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.save_characterization_result "Link to this definition")

    *property* size\_of\_processing\_block*: int*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.size_of_processing_block "Link to this definition")

    *property* tolerance\_mode*: [ToleranceMode](#keysight.ads.hsd.memory.simulator.ToleranceMode "keysight.ads.hsd._common.simulators.ToleranceMode")*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.tolerance_mode "Link to this definition")

    *property* use\_transient\_low\_freq\_extrapolation*: bool*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.use_transient_low_freq_extrapolation "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.TransientConvolutionSetting[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting "Link to this definition")
:   Bases: `CommonConvolutionSettings`

    *property* absolute\_impulse\_response\_truncation*: float*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.absolute_impulse_response_truncation "Link to this definition")

    *property* number\_of\_passes\_for\_impulse\_calculation*: int | None*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.number_of_passes_for_impulse_calculation "Link to this definition")

    *property* passivity\_mode*: [PassivityMode](#keysight.ads.hsd.memory.simulator.PassivityMode "keysight.ads.hsd._common.simulators.PassivityMode")*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.passivity_mode "Link to this definition")

    *property* relative\_impulse\_response\_truncation\_factor*: float*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.relative_impulse_response_truncation_factor "Link to this definition")

    *property* save\_impulse\_spectrum*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.save_impulse_spectrum "Link to this definition")

    *property* short\_tline\_delay*: str*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.short_tline_delay "Link to this definition")

    *property* tolerance\_mode*: [ToleranceMode](#keysight.ads.hsd.memory.simulator.ToleranceMode "keysight.ads.hsd._common.simulators.ToleranceMode")*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.tolerance_mode "Link to this definition")

    *property* transient\_delta\_impulse\_frequency*: str*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.transient_delta_impulse_frequency "Link to this definition")

    *property* transient\_max\_impulse\_frequency*: str*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.transient_max_impulse_frequency "Link to this definition")

    *property* use\_approximate\_models*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.use_approximate_models "Link to this definition")

    *property* use\_transient\_low\_freq\_extrapolation*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.use_transient_low_freq_extrapolation "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.TransientConvergenceSettings[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings "Link to this definition")
:   Bases: `object`

    *property* check\_only\_delta\_voltage*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.check_only_delta_voltage "Link to this definition")

    *property* check\_strange\_behavior\_at\_every\_timestep*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.check_strange_behavior_at_every_timestep "Link to this definition")

    *property* connect\_all\_nodes\_to\_ground*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.connect_all_nodes_to_ground "Link to this definition")

    *property* iv\_relative\_tolerance*: float | None*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.iv_relative_tolerance "Link to this definition")

    *property* max\_iteration\_per\_time\_step*: int*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.max_iteration_per_time_step "Link to this definition")

    *property* max\_iterations\_at\_initial\_dc*: int*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.max_iterations_at_initial_dc "Link to this definition")

    *property* perform\_kcl\_check*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.perform_kcl_check "Link to this definition")

    *property* skip\_device\_evaluation*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.skip_device_evaluation "Link to this definition")

    *property* use\_custom\_initial\_condition*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.use_custom_initial_condition "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.TransientIntegrationSettings[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings "Link to this definition")
:   Bases: `object`

    *property* charge\_accuracy*: float*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.charge_accuracy "Link to this definition")

    *property* integration\_coefficient\_mu*: float | None*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.integration_coefficient_mu "Link to this definition")

    *property* integration\_method*: [IntegrationMethod](#keysight.ads.hsd.memory.simulator.IntegrationMethod "keysight.ads.hsd._common.simulators.IntegrationMethod")*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.integration_method "Link to this definition")

    *property* max\_gear\_order*: int*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.max_gear_order "Link to this definition")

    *property* time\_step\_control\_method*: [TimeStepControlMethod](#keysight.ads.hsd.memory.simulator.TimeStepControlMethod "keysight.ads.hsd._common.simulators.TimeStepControlMethod")*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.time_step_control_method "Link to this definition")

    *property* truncation\_error\_factor*: float*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.truncation_error_factor "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings "Link to this definition")
:   Bases: `object`

    *property* bit\_pattern*: [CrosstalkAnalysisBitPattern](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern "keysight.ads.hsd._common.simulators.CrosstalkAnalysisBitPattern")*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings.bit_pattern "Link to this definition")

    *property* enabled*: bool*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings.enabled "Link to this definition")

    *property* victim\_mode*: [CrosstalkAnalysisVictimMode](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisVictimMode "keysight.ads.hsd._common.simulators.CrosstalkAnalysisVictimMode")*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings.victim_mode "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings[](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings "Link to this definition")
:   Bases: `object`

    *property* enabled*: bool*[](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings.enabled "Link to this definition")

    *property* limit\_in\_db*: int*[](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings.limit_in_db "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.SParamSweepSettings[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings "Link to this definition")
:   Bases: `object`

    *property* center*: str*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.center "Link to this definition")

    *property* is\_using\_number\_of\_points*: bool*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.is_using_number_of_points "Link to this definition")

    *property* number\_of\_points*: int*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.number_of_points "Link to this definition")

    *property* points\_per\_decade*: int*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.points_per_decade "Link to this definition")

    *property* span*: str*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.span "Link to this definition")

    *property* start*: str*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.start "Link to this definition")

    *property* step\_size*: str*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.step_size "Link to this definition")

    *property* stop*: str*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.stop "Link to this definition")

    *property* sweep\_mode*: [SparamSweepMode](#keysight.ads.hsd.memory.simulator.SparamSweepMode "keysight.ads.hsd._common.simulators.SparamSweepMode")*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.sweep_mode "Link to this definition")

    *property* sweep\_type*: [SparamSweepType](#keysight.ads.hsd.memory.simulator.SparamSweepType "keysight.ads.hsd._common.simulators.SparamSweepType")*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.sweep_type "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.BitByBitSimulation[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation "Link to this definition")
:   Bases: `CommonSimulator`

    *property* convolution\_settings*: [ChannelSimConvolutionSetting](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting "keysight.ads.hsd._common.simulators.ChannelSimConvolutionSetting")*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.convolution_settings "Link to this definition")

    *property* crosstalk\_analysis\_settings*: [CrosstalkAnalysisSettings](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings "keysight.ads.hsd._common.simulators.CrosstalkAnalysisSettings")*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.crosstalk_analysis_settings "Link to this definition")

    *property* crosstalk\_limiter\_settings*: [CrosstalkLimiterSettings](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings "keysight.ads.hsd._common.simulators.CrosstalkLimiterSettings")*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.crosstalk_limiter_settings "Link to this definition")

    *property* enable\_low\_BER\_floor*: bool*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.enable_low_BER_floor "Link to this definition")

    *property* number\_of\_bits*: int*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.number_of_bits "Link to this definition")

    *property* simulation\_mode*: [SimulationMode](#keysight.ads.hsd.memory.simulator.SimulationMode "keysight.ads.hsd._common.simulators.SimulationMode")*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.simulation_mode "Link to this definition")

    *property* status\_level*: str*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.status_level "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.StatisticalSimulation[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation "Link to this definition")
:   Bases: `CommonSimulator`

    *property* convolution\_settings*: [ChannelSimConvolutionSetting](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting "keysight.ads.hsd._common.simulators.ChannelSimConvolutionSetting")*[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation.convolution_settings "Link to this definition")

    *property* crosstalk\_limiter\_settings*: [CrosstalkLimiterSettings](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings "keysight.ads.hsd._common.simulators.CrosstalkLimiterSettings")*[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation.crosstalk_limiter_settings "Link to this definition")

    *property* enable\_low\_BER\_floor*: bool*[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation.enable_low_BER_floor "Link to this definition")

    *property* simulation\_mode*: [SimulationMode](#keysight.ads.hsd.memory.simulator.SimulationMode "keysight.ads.hsd._common.simulators.SimulationMode")*[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation.simulation_mode "Link to this definition")

    *property* status\_level*: str*[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation.status_level "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.TransientSimulation[](#keysight.ads.hsd.memory.simulator.TransientSimulation "Link to this definition")
:   Bases: `CommonSimulator`

    *property* convergence\_settings*: [TransientConvergenceSettings](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings "keysight.ads.hsd._common.simulators.TransientConvergenceSettings")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.convergence_settings "Link to this definition")

    *property* convolution\_settings*: [TransientConvolutionSetting](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting "keysight.ads.hsd._common.simulators.TransientConvolutionSetting")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.convolution_settings "Link to this definition")

    *property* crosstalk\_analysis\_settings*: [CrosstalkAnalysisSettings](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings "keysight.ads.hsd._common.simulators.CrosstalkAnalysisSettings")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.crosstalk_analysis_settings "Link to this definition")

    *property* crosstalk\_limiter\_settings*: [CrosstalkLimiterSettings](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings "keysight.ads.hsd._common.simulators.CrosstalkLimiterSettings")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.crosstalk_limiter_settings "Link to this definition")

    *property* enable\_low\_BER\_floor*: bool*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.enable_low_BER_floor "Link to this definition")

    *property* integration\_settings*: [TransientIntegrationSettings](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings "keysight.ads.hsd._common.simulators.TransientIntegrationSettings")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.integration_settings "Link to this definition")

    *property* limit\_time\_step\_for\_tline*: bool*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.limit_time_step_for_tline "Link to this definition")

    *property* max\_time\_step*: str*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.max_time_step "Link to this definition")

    *property* min\_time\_step*: str*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.min_time_step "Link to this definition")

    *property* simulation\_mode*: [SimulationMode](#keysight.ads.hsd.memory.simulator.SimulationMode "keysight.ads.hsd._common.simulators.SimulationMode")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.simulation_mode "Link to this definition")

    *property* start\_time*: str*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.start_time "Link to this definition")

    *property* status\_level*: str*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.status_level "Link to this definition")

    *property* stop\_time*: str*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.stop_time "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.SParameterSimulation[](#keysight.ads.hsd.memory.simulator.SParameterSimulation "Link to this definition")
:   Bases: `CommonSimulator`

    *property* enable\_low\_BER\_floor*: bool*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.enable_low_BER_floor "Link to this definition")

    *property* open\_sparam\_toolkit*: bool*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.open_sparam_toolkit "Link to this definition")

    *property* reference\_impedance*: float*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.reference_impedance "Link to this definition")

    *property* simulation\_mode*: [SimulationMode](#keysight.ads.hsd.memory.simulator.SimulationMode "keysight.ads.hsd._common.simulators.SimulationMode")*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.simulation_mode "Link to this definition")

    *property* sparam\_sweep*: [SParamSweepSettings](#keysight.ads.hsd.memory.simulator.SParamSweepSettings "keysight.ads.hsd._common.simulators.SParamSweepSettings")*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.sparam_sweep "Link to this definition")

    *property* status\_level*: str*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.status_level "Link to this definition")

    *property* termination\_placement*: [SparamTermPlacement](#keysight.ads.hsd.memory.simulator.SparamTermPlacement "keysight.ads.hsd._common.simulators.SparamTermPlacement")*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.termination_placement "Link to this definition")


---

<!-- === 来源: reference/hsd/metadata.md === -->

# Metadata[](#metadata "Link to this heading")

## Enumerated types[](#enumerated-types "Link to this heading")

*class* keysight.ads.hsd.metadata.SignalTypeEnum[](#keysight.ads.hsd.metadata.SignalTypeEnum "Link to this definition")
:   Bases: `EnumWrapper`

    A *= <SignalTypeEnum.A: 16>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.A "Link to this definition")

    ACT\_n *= <SignalTypeEnum.ACT\_n: 31>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.ACT_n "Link to this definition")

    AERR *= <SignalTypeEnum.AERR: 38>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.AERR "Link to this definition")

    ALERT\_n *= <SignalTypeEnum.ALERT\_n: 32>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.ALERT_n "Link to this definition")

    APAR *= <SignalTypeEnum.APAR: 44>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.APAR "Link to this definition")

    BA *= <SignalTypeEnum.BA: 27>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.BA "Link to this definition")

    BG *= <SignalTypeEnum.BG: 28>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.BG "Link to this definition")

    BWD\_N *= <SignalTypeEnum.BWD\_N: 80>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.BWD_N "Link to this definition")

    BWD\_P *= <SignalTypeEnum.BWD\_P: 79>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.BWD_P "Link to this definition")

    C *= <SignalTypeEnum.C: 18>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.C "Link to this definition")

    CABI\_n *= <SignalTypeEnum.CABI\_n: 36>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CABI_n "Link to this definition")

    CAS\_n *= <SignalTypeEnum.CAS\_n: 25>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CAS_n "Link to this definition")

    CKE *= <SignalTypeEnum.CKE: 23>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CKE "Link to this definition")

    CK\_c *= <SignalTypeEnum.CK\_c: 15>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CK_c "Link to this definition")

    CK\_t *= <SignalTypeEnum.CK\_t: 14>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CK_t "Link to this definition")

    CS\_n *= <SignalTypeEnum.CS\_n: 22>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CS_n "Link to this definition")

    DBI\_n *= <SignalTypeEnum.DBI\_n: 30>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DBI_n "Link to this definition")

    DERR *= <SignalTypeEnum.DERR: 37>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DERR "Link to this definition")

    DM\_n *= <SignalTypeEnum.DM\_n: 29>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DM_n "Link to this definition")

    DPAR *= <SignalTypeEnum.DPAR: 43>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DPAR "Link to this definition")

    DQ *= <SignalTypeEnum.DQ: 0>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DQ "Link to this definition")

    DQS\_c *= <SignalTypeEnum.DQS\_c: 5>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DQS_c "Link to this definition")

    DQS\_t *= <SignalTypeEnum.DQS\_t: 4>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DQS_t "Link to this definition")

    DQX *= <SignalTypeEnum.DQX: 1>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DQX "Link to this definition")

    ECC *= <SignalTypeEnum.ECC: 41>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.ECC "Link to this definition")

    EDC *= <SignalTypeEnum.EDC: 35>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.EDC "Link to this definition")

    FWD\_N *= <SignalTypeEnum.FWD\_N: 78>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.FWD_N "Link to this definition")

    FWD\_P *= <SignalTypeEnum.FWD\_P: 77>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.FWD_P "Link to this definition")

    ODT *= <SignalTypeEnum.ODT: 21>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.ODT "Link to this definition")

    PAR *= <SignalTypeEnum.PAR: 33>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.PAR "Link to this definition")

    PARITY *= <SignalTypeEnum.PARITY: 34>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.PARITY "Link to this definition")

    R *= <SignalTypeEnum.R: 17>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.R "Link to this definition")

    RAS\_n *= <SignalTypeEnum.RAS\_n: 24>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RAS_n "Link to this definition")

    RDQS\_c *= <SignalTypeEnum.RDQS\_c: 7>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RDQS_c "Link to this definition")

    RDQS\_t *= <SignalTypeEnum.RDQS\_t: 6>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RDQS_t "Link to this definition")

    RE\_c *= <SignalTypeEnum.RE\_c: 40>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RE_c "Link to this definition")

    RE\_t *= <SignalTypeEnum.RE\_t: 39>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RE_t "Link to this definition")

    RXCKN *= <SignalTypeEnum.RXCKN: 76>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXCKN "Link to this definition")

    RXCKP *= <SignalTypeEnum.RXCKP: 75>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXCKP "Link to this definition")

    RXCKRD *= <SignalTypeEnum.RXCKRD: 59>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXCKRD "Link to this definition")

    RXCKSB *= <SignalTypeEnum.RXCKSB: 62>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXCKSB "Link to this definition")

    RXCKSBRD *= <SignalTypeEnum.RXCKSBRD: 64>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXCKSBRD "Link to this definition")

    RXDATA *= <SignalTypeEnum.RXDATA: 74>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXDATA "Link to this definition")

    RXDATARD *= <SignalTypeEnum.RXDATARD: 57>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXDATARD "Link to this definition")

    RXDATASB *= <SignalTypeEnum.RXDATASB: 61>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXDATASB "Link to this definition")

    RXDATASBRD *= <SignalTypeEnum.RXDATASBRD: 63>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXDATASBRD "Link to this definition")

    RXTRK *= <SignalTypeEnum.RXTRK: 56>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXTRK "Link to this definition")

    RXTRKRD *= <SignalTypeEnum.RXTRKRD: 60>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXTRKRD "Link to this definition")

    RXVLD *= <SignalTypeEnum.RXVLD: 55>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXVLD "Link to this definition")

    RXVLDRD *= <SignalTypeEnum.RXVLDRD: 58>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXVLDRD "Link to this definition")

    SEV *= <SignalTypeEnum.SEV: 42>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.SEV "Link to this definition")

    TXCKN *= <SignalTypeEnum.TXCKN: 73>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXCKN "Link to this definition")

    TXCKP *= <SignalTypeEnum.TXCKP: 72>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXCKP "Link to this definition")

    TXCKRD *= <SignalTypeEnum.TXCKRD: 49>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXCKRD "Link to this definition")

    TXCKSB *= <SignalTypeEnum.TXCKSB: 52>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXCKSB "Link to this definition")

    TXCKSBRD *= <SignalTypeEnum.TXCKSBRD: 54>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXCKSBRD "Link to this definition")

    TXDATA *= <SignalTypeEnum.TXDATA: 71>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXDATA "Link to this definition")

    TXDATARD *= <SignalTypeEnum.TXDATARD: 47>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXDATARD "Link to this definition")

    TXDATASB *= <SignalTypeEnum.TXDATASB: 51>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXDATASB "Link to this definition")

    TXDATASBRD *= <SignalTypeEnum.TXDATASBRD: 53>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXDATASBRD "Link to this definition")

    TXTRK *= <SignalTypeEnum.TXTRK: 46>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXTRK "Link to this definition")

    TXTRKRD *= <SignalTypeEnum.TXTRKRD: 50>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXTRKRD "Link to this definition")

    TXVLD *= <SignalTypeEnum.TXVLD: 45>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXVLD "Link to this definition")

    TXVLDRD *= <SignalTypeEnum.TXVLDRD: 48>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXVLDRD "Link to this definition")

    UNKNOWN *= <SignalTypeEnum.UNKNOWN: 86>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.UNKNOWN "Link to this definition")

    VCCAON *= <SignalTypeEnum.VCCAON: 66>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.VCCAON "Link to this definition")

    VCCIO *= <SignalTypeEnum.VCCIO: 65>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.VCCIO "Link to this definition")

    VDD *= <SignalTypeEnum.VDD: 19>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.VDD "Link to this definition")

    VPP *= <SignalTypeEnum.VPP: 20>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.VPP "Link to this definition")

    VSS *= <SignalTypeEnum.VSS: 85>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.VSS "Link to this definition")

    WCK\_c *= <SignalTypeEnum.WCK\_c: 13>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.WCK_c "Link to this definition")

    WCK\_t *= <SignalTypeEnum.WCK\_t: 12>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.WCK_t "Link to this definition")

    WDQS\_c *= <SignalTypeEnum.WDQS\_c: 9>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.WDQS_c "Link to this definition")

    WDQS\_t *= <SignalTypeEnum.WDQS\_t: 8>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.WDQS_t "Link to this definition")

    WE\_n *= <SignalTypeEnum.WE\_n: 26>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.WE_n "Link to this definition")

*class* keysight.ads.hsd.metadata.SignalNodeType[](#keysight.ads.hsd.metadata.SignalNodeType "Link to this definition")
:   NEGATIVE *= <SignalNodeType.Negative: 2>*[](#keysight.ads.hsd.metadata.SignalNodeType.NEGATIVE "Link to this definition")

    POSITIVE *= <SignalNodeType.Positive: 1>*[](#keysight.ads.hsd.metadata.SignalNodeType.POSITIVE "Link to this definition")

    SINGLE\_ENDED *= <SignalNodeType.SingleEnded: 0>*[](#keysight.ads.hsd.metadata.SignalNodeType.SINGLE_ENDED "Link to this definition")

*class* keysight.ads.hsd.metadata.SignalPortTypeEnum[](#keysight.ads.hsd.metadata.SignalPortTypeEnum "Link to this definition")
:   DIFFERENTIAL *= <SignalPortTypeEnum.Differential: 0>*[](#keysight.ads.hsd.metadata.SignalPortTypeEnum.DIFFERENTIAL "Link to this definition")

    NEGATIVE *= <SignalPortTypeEnum.Negative: 3>*[](#keysight.ads.hsd.metadata.SignalPortTypeEnum.NEGATIVE "Link to this definition")

    POSITIVE *= <SignalPortTypeEnum.Positive: 2>*[](#keysight.ads.hsd.metadata.SignalPortTypeEnum.POSITIVE "Link to this definition")

    SINGLE\_ENDED *= <SignalPortTypeEnum.SingleEnded: 1>*[](#keysight.ads.hsd.metadata.SignalPortTypeEnum.SINGLE_ENDED "Link to this definition")

*class* keysight.ads.hsd.metadata.PortInfoSimilarity[](#keysight.ads.hsd.metadata.PortInfoSimilarity "Link to this definition")
:   HAS\_ALT\_SIGNAL\_ID\_SAME\_AS\_SIGNAL\_ID *= <PortInfoSimilarity.HasAltSignalIdSameAsSignalId: 5>*[](#keysight.ads.hsd.metadata.PortInfoSimilarity.HAS_ALT_SIGNAL_ID_SAME_AS_SIGNAL_ID "Link to this definition")

    HAS\_SAME\_ALT\_SIGNAL\_IDS *= <PortInfoSimilarity.HasSameAltSignalIds: 2>*[](#keysight.ads.hsd.metadata.PortInfoSimilarity.HAS_SAME_ALT_SIGNAL_IDS "Link to this definition")

    HAS\_SAME\_SIGNAL\_IDS *= <PortInfoSimilarity.HasSameSignalIds: 1>*[](#keysight.ads.hsd.metadata.PortInfoSimilarity.HAS_SAME_SIGNAL_IDS "Link to this definition")

    HAS\_SAME\_SIGNAL\_ID\_AND\_ALT\_SIGNAL\_ID *= <PortInfoSimilarity.HasSameSignalIdAndAltSignalId: 3>*[](#keysight.ads.hsd.metadata.PortInfoSimilarity.HAS_SAME_SIGNAL_ID_AND_ALT_SIGNAL_ID "Link to this definition")

    HAS\_SIGNAL\_ID\_SAME\_AS\_ALT\_SIGNAL\_ID *= <PortInfoSimilarity.HasSignalIdSameAsAltSignalId: 4>*[](#keysight.ads.hsd.metadata.PortInfoSimilarity.HAS_SIGNAL_ID_SAME_AS_ALT_SIGNAL_ID "Link to this definition")

*class* keysight.ads.hsd.metadata.PortConnectivityCollisionType[](#keysight.ads.hsd.metadata.PortConnectivityCollisionType "Link to this definition")
:   ALT\_SIGNAL\_ID\_COLLIDING *= <PortConnectivityCollisionType.AltSignalIdColliding: 2>*[](#keysight.ads.hsd.metadata.PortConnectivityCollisionType.ALT_SIGNAL_ID_COLLIDING "Link to this definition")

    NO\_COLLISION *= <PortConnectivityCollisionType.NoCollision: 0>*[](#keysight.ads.hsd.metadata.PortConnectivityCollisionType.NO_COLLISION "Link to this definition")

    SIGNAL\_ID\_AND\_ALT\_SIGNAL\_ID\_COLLIDING *= <PortConnectivityCollisionType.SignalIdAndAltSignalIdColliding: 3>*[](#keysight.ads.hsd.metadata.PortConnectivityCollisionType.SIGNAL_ID_AND_ALT_SIGNAL_ID_COLLIDING "Link to this definition")

    SIGNAL\_ID\_COLLIDING *= <PortConnectivityCollisionType.SignalIdColliding: 1>*[](#keysight.ads.hsd.metadata.PortConnectivityCollisionType.SIGNAL_ID_COLLIDING "Link to this definition")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.metadata.SignalType[](#keysight.ads.hsd.metadata.SignalType "Link to this definition")
:   *property* is\_differential\_type*: bool*[](#keysight.ads.hsd.metadata.SignalType.is_differential_type "Link to this definition")

    *property* is\_power\_type*: bool*[](#keysight.ads.hsd.metadata.SignalType.is_power_type "Link to this definition")

    *property* name*: str*[](#keysight.ads.hsd.metadata.SignalType.name "Link to this definition")

    *property* name\_without\_polarity*: str*[](#keysight.ads.hsd.metadata.SignalType.name_without_polarity "Link to this definition")

    *property* pair*: [SignalType](#keysight.ads.hsd.metadata.SignalType "keysight.ads.hsd._common.metadata.SignalType")*[](#keysight.ads.hsd.metadata.SignalType.pair "Link to this definition")

    *property* signal\_node\_type*: [SignalNodeType](#keysight.ads.hsd.metadata.SignalNodeType "keysight.ads.hsd._common.metadata.SignalNodeType")*[](#keysight.ads.hsd.metadata.SignalType.signal_node_type "Link to this definition")

    *property* type*: [SignalTypeEnum](#keysight.ads.hsd.metadata.SignalTypeEnum "keysight.ads.hsd._common.metadata.SignalTypeEnum")*[](#keysight.ads.hsd.metadata.SignalType.type "Link to this definition")

*class* keysight.ads.hsd.metadata.SignalId[](#keysight.ads.hsd.metadata.SignalId "Link to this definition")
:   *property* index*: int*[](#keysight.ads.hsd.metadata.SignalId.index "Link to this definition")

    *property* is\_power\_type*: bool*[](#keysight.ads.hsd.metadata.SignalId.is_power_type "Link to this definition")

    *property* is\_signal\_type\_unknown*: bool*[](#keysight.ads.hsd.metadata.SignalId.is_signal_type_unknown "Link to this definition")

    is\_valid\_and\_same\_as(*other: [SignalId](#keysight.ads.hsd.metadata.SignalId "keysight.ads.hsd._common.metadata.SignalId")*) → bool[](#keysight.ads.hsd.metadata.SignalId.is_valid_and_same_as "Link to this definition")

    *property* type*: [SignalType](#keysight.ads.hsd.metadata.SignalType "keysight.ads.hsd._common.metadata.SignalType")*[](#keysight.ads.hsd.metadata.SignalId.type "Link to this definition")

    *property* type\_name*: str*[](#keysight.ads.hsd.metadata.SignalId.type_name "Link to this definition")

*class* keysight.ads.hsd.metadata.PortInfo[](#keysight.ads.hsd.metadata.PortInfo "Link to this definition")
:   *property* alt\_signal\_index*: int | None*[](#keysight.ads.hsd.metadata.PortInfo.alt_signal_index "Link to this definition")

    *property* alt\_signal\_type*: [SignalType](#keysight.ads.hsd.metadata.SignalType "keysight.ads.hsd._common.metadata.SignalType") | None*[](#keysight.ads.hsd.metadata.PortInfo.alt_signal_type "Link to this definition")

    *property* channel\_id*: str*[](#keysight.ads.hsd.metadata.PortInfo.channel_id "Link to this definition")

    *property* connected\_pin\_list*: list[str]*[](#keysight.ads.hsd.metadata.PortInfo.connected_pin_list "Link to this definition")

    copy\_with\_new\_port\_name(*new\_port\_name: str*) → [PortInfo](#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo")[](#keysight.ads.hsd.metadata.PortInfo.copy_with_new_port_name "Link to this definition")
    :   Returns a deep copy of this port info object with the new port name.

        Since port\_name cannot be changed directly, this method is used to create a new port info object with the new port name.

        Parameters:
        :   **(****str****)** (*new\_port\_name*)

    *property* has\_alt\_signal\_id*: bool*[](#keysight.ads.hsd.metadata.PortInfo.has_alt_signal_id "Link to this definition")

    *property* is\_terminated*: bool*[](#keysight.ads.hsd.metadata.PortInfo.is_terminated "Link to this definition")

    *property* port\_name*: str*[](#keysight.ads.hsd.metadata.PortInfo.port_name "Link to this definition")

    *property* ref\_des*: str*[](#keysight.ads.hsd.metadata.PortInfo.ref_des "Link to this definition")

    *property* signal\_id*: [SignalId](#keysight.ads.hsd.metadata.SignalId "keysight.ads.hsd._common.metadata.SignalId")*[](#keysight.ads.hsd.metadata.PortInfo.signal_id "Link to this definition")

    *property* signal\_index*: int*[](#keysight.ads.hsd.metadata.PortInfo.signal_index "Link to this definition")

    *property* signal\_type*: [SignalType](#keysight.ads.hsd.metadata.SignalType "keysight.ads.hsd._common.metadata.SignalType")*[](#keysight.ads.hsd.metadata.PortInfo.signal_type "Link to this definition")

    *property* termination\_value*: float*[](#keysight.ads.hsd.metadata.PortInfo.termination_value "Link to this definition")

*class* keysight.ads.hsd.metadata.MetaData[](#keysight.ads.hsd.metadata.MetaData "Link to this definition")
:   \_\_bool\_\_() → bool[](#keysight.ads.hsd.metadata.MetaData.__bool__ "Link to this definition")

    \_\_contains\_\_(*port\_info: [PortInfo](#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo") | str*) → bool[](#keysight.ads.hsd.metadata.MetaData.__contains__ "Link to this definition")

    \_\_getitem\_\_(*key: str | int*) → [PortInfo](#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo")[](#keysight.ads.hsd.metadata.MetaData.__getitem__ "Link to this definition")

    \_\_iter\_\_() → Iterator[[PortInfo](#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo")][](#keysight.ads.hsd.metadata.MetaData.__iter__ "Link to this definition")

    \_\_len\_\_() → int[](#keysight.ads.hsd.metadata.MetaData.__len__ "Link to this definition")

    \_\_str\_\_() → str[](#keysight.ads.hsd.metadata.MetaData.__str__ "Link to this definition")
    :   Return str(self).

    apply(*other\_metadata: [MetaData](#keysight.ads.hsd.metadata.MetaData "keysight.ads.hsd._common.metadata.MetaData")*) → None[](#keysight.ads.hsd.metadata.MetaData.apply "Link to this definition")
    :   Applies the port info(s) with the same port name(s) from the other metadata to this metadata.


---

<!-- === 来源: reference/hsd/smartwire.md === -->

# Smart Wire[](#smart-wire "Link to this heading")

## Functions[](#functions "Link to this heading")

keysight.ads.hsd.smart\_wire.auto\_connect(*from\_instance: Instance | Term*, *to\_instance: Instance | Term*) → bool[](#keysight.ads.hsd.smart_wire.auto_connect "Link to this definition")
:   Auto connect a smart component or term to a smart component or term.

    Two terms will raise an exception.

keysight.ads.hsd.smart\_wire.custom\_connect(*from\_instance: Instance | Term*, *to\_instance: Instance | Term*, *from\_port\_names: list[str]*, *to\_port\_names: list[str]*) → bool[](#keysight.ads.hsd.smart_wire.custom_connect "Link to this definition")
:   Custom connect a smart component or term to a smart component or term with the port name lists that should be connected.

    Port name list can be empty if it is associated with a term. Otherwise, the port name lists must be the same length.
    If the port name lists are not the same length, InvalidCustomConnectPortNamesError with be raised.
    Two terms will raise an exception.


---

<!-- === 来源: reference/index.md === -->

# Reference[](#reference "Link to this heading")

* [keysight.ads.hsd](hsd/index.md)
* [keysight.ads.hsd.memory](hsd/memory/index.md)

**Indices**

* [Index](../genindex.md)
* [Module Index](../py-modindex.md)


---

