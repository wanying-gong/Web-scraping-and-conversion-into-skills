<!-- 来源: reference\hsd\memory\probe.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.hsd.memory](index.md)
* Memory Probe

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
    - Memory Probe
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

On this page

[Previous

Memory Interface Simulator](simulator.md)
[Next

Memory Termination](ddr_termination.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top