<!-- 来源: reference\hsd\memory\ddr_termination.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.hsd.memory](index.md)
* Memory Termination

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
    - [Memory DRAM](ddr_memory.md)
    - [Memory Interface Simulator](simulator.md)
    - [Memory Probe](probe.md)
    - Memory Termination
    - [Memory IO Component](io_component.md)
* [How-To](../../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../howto/existingvenv.md)
  + [How to Use Pytest](../../../howto/pytest.md)
* [Examples](../../../examples/index.md)
  + [Setup a Printed Circuit Board (PCB)](../../../examples/pcb_setup.md)
  + [Setup a design for Memory Designer](../../../examples/sample_design.md)

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

On this page

[Previous

Memory Probe](probe.md)
[Next

Memory IO Component](io_component.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top