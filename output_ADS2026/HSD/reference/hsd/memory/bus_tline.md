<!-- 来源: reference\hsd\memory\bus_tline.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.hsd.memory](index.md)
* Memory Bus T-Line

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
    - Memory Bus T-Line
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

On this page

[Previous

Memory Printed Circuit Board (PCB)](pcb.md)
[Next

Memory Bus Designer](bus_designer.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top