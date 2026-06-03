<!-- 来源: reference\hsd\memory\ddr_controller.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.hsd.memory](index.md)
* Memory Controller

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
    - Memory Controller
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

On this page

[Previous

Memory Bus Designer](bus_designer.md)
[Next

Memory DRAM](ddr_memory.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top