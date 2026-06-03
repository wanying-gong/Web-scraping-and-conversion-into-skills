<!-- 来源: reference\hsd\memory\setup.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.hsd.memory](index.md)
* Memory Setup

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
    - Memory Setup
    - [Memory Pre-layout](prelayout.md)
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

On this page

[Previous

keysight.ads.hsd.memory](index.md)
[Next

Memory Pre-layout](prelayout.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top