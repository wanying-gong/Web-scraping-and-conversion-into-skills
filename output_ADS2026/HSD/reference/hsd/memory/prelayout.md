<!-- 来源: reference\hsd\memory\prelayout.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.hsd.memory](index.md)
* Memory Pre-layout

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
    - Memory Pre-layout
    - [Memory Printed Circuit Board (PCB)](pcb.md)
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

On this page

[Previous

Memory Setup](setup.md)
[Next

Memory Printed Circuit Board (PCB)](pcb.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top