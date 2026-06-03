<!-- 来源: reference\hsd\memory\bus_designer.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.hsd.memory](index.md)
* Memory Bus Designer

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

* [Introduction](../../../intro/index.md)
  + [Using Visual Studio Code](../../../intro/vscode.md)
* [Reference](../../index.md)
  + [keysight.ads.hsd](../index.md)
    - [Core](../core.md)
    - [Metadata](../metadata.md)
    - [Smart Wire](../smartwire.md)
  + [keysight.ads.hsd.memory](index.md)
    - [Memory Setup](setup.md)
    - [Memory Pre-layout](prelayout.md)
    - [Memory Printed Circuit Board (PCB)](pcb.md)
    - [Memory Bus T-Line](bus_tline.md)
    - Memory Bus Designer
    - [Memory Controller](ddr_controller.md)
    - [Memory DRAM](ddr_memory.md)
    - [Memory Interface Simulator](simulator.md)
    - [Memory Probe](probe.md)
    - [Memory Termination](ddr_termination.md)
    - [Memory IO Component](io_component.md)
* [How-To](../../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../howto/existingvenv.md)
  + [How to Use Pytest](../../../howto/pytest.md)
* [Examples](../../../examples/index.md)
  + [Setup a Printed Circuit Board (PCB)](../../../examples/pcb_setup.md)
  + [Setup a design for Memory Designer](../../../examples/sample_design.md)

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

On this page

[Previous

Memory Bus T-Line](bus_tline.md)
[Next

Memory Controller](ddr_controller.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top