<!-- 来源: reference\hsd\memory\ddr_memory.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.hsd.memory](index.md)
* Memory DRAM

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
    - [Memory Bus Designer](bus_designer.md)
    - [Memory Controller](ddr_controller.md)
    - Memory DRAM
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

On this page

[Previous

Memory Controller](ddr_controller.md)
[Next

Memory Interface Simulator](simulator.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top