<!-- 来源: reference\hsd\memory\io_component.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.hsd.memory](index.md)
* Memory IO Component

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
    - [Memory Termination](ddr_termination.md)
    - Memory IO Component
* [How-To](../../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../../howto/existingvenv.md)
  + [How to Use Pytest](../../../howto/pytest.md)
* [Examples](../../../examples/index.md)
  + [Setup a Printed Circuit Board (PCB)](../../../examples/pcb_setup.md)
  + [Setup a design for Memory Designer](../../../examples/sample_design.md)

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

On this page

[Previous

Memory Termination](ddr_termination.md)
[Next

How-To](../../../howto/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top