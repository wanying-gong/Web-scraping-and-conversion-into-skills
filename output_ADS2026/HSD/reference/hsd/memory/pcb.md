<!-- 来源: reference\hsd\memory\pcb.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.hsd.memory](index.md)
* Memory Printed Circuit Board (PCB)

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
    - Memory Printed Circuit Board (PCB)
    - [Memory Bus T-Line](bus_tline.md)
    - [Memory Bus Designer](bus_designer.md)
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

On this page

[Previous

Memory Pre-layout](prelayout.md)
[Next

Memory Bus T-Line](bus_tline.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top