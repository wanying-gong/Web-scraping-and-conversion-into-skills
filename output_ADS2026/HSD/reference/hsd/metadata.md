<!-- 来源: reference\hsd\metadata.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../index.md)
* [Reference](../index.md)
* [keysight.ads.hsd](index.md)
* Metadata

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

* [Introduction](../../intro/index.md)
  + [Using Visual Studio Code](../../intro/vscode.md)
* [Reference](../index.md)
  + [keysight.ads.hsd](index.md)
    - [Core](core.md)
    - Metadata
    - [Smart Wire](smartwire.md)
  + [keysight.ads.hsd.memory](memory/index.md)
    - [Memory Setup](memory/setup.md)
    - [Memory Pre-layout](memory/prelayout.md)
    - [Memory Printed Circuit Board (PCB)](memory/pcb.md)
    - [Memory Bus T-Line](memory/bus_tline.md)
    - [Memory Bus Designer](memory/bus_designer.md)
    - [Memory Controller](memory/ddr_controller.md)
    - [Memory DRAM](memory/ddr_memory.md)
    - [Memory Interface Simulator](memory/simulator.md)
    - [Memory Probe](memory/probe.md)
    - [Memory Termination](memory/ddr_termination.md)
    - [Memory IO Component](memory/io_component.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
  + [How to Use Pytest](../../howto/pytest.md)
* [Examples](../../examples/index.md)
  + [Setup a Printed Circuit Board (PCB)](../../examples/pcb_setup.md)
  + [Setup a design for Memory Designer](../../examples/sample_design.md)

# Metadata[](#metadata "Link to this heading")

## Enumerated types[](#enumerated-types "Link to this heading")

*class* keysight.ads.hsd.metadata.SignalTypeEnum[](#keysight.ads.hsd.metadata.SignalTypeEnum "Link to this definition")
:   Bases: `EnumWrapper`

    A *= <SignalTypeEnum.A: 16>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.A "Link to this definition")

    ACT\_n *= <SignalTypeEnum.ACT\_n: 31>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.ACT_n "Link to this definition")

    AERR *= <SignalTypeEnum.AERR: 38>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.AERR "Link to this definition")

    ALERT\_n *= <SignalTypeEnum.ALERT\_n: 32>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.ALERT_n "Link to this definition")

    APAR *= <SignalTypeEnum.APAR: 44>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.APAR "Link to this definition")

    BA *= <SignalTypeEnum.BA: 27>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.BA "Link to this definition")

    BG *= <SignalTypeEnum.BG: 28>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.BG "Link to this definition")

    BWD\_N *= <SignalTypeEnum.BWD\_N: 80>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.BWD_N "Link to this definition")

    BWD\_P *= <SignalTypeEnum.BWD\_P: 79>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.BWD_P "Link to this definition")

    C *= <SignalTypeEnum.C: 18>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.C "Link to this definition")

    CABI\_n *= <SignalTypeEnum.CABI\_n: 36>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CABI_n "Link to this definition")

    CAS\_n *= <SignalTypeEnum.CAS\_n: 25>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CAS_n "Link to this definition")

    CKE *= <SignalTypeEnum.CKE: 23>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CKE "Link to this definition")

    CK\_c *= <SignalTypeEnum.CK\_c: 15>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CK_c "Link to this definition")

    CK\_t *= <SignalTypeEnum.CK\_t: 14>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CK_t "Link to this definition")

    CS\_n *= <SignalTypeEnum.CS\_n: 22>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.CS_n "Link to this definition")

    DBI\_n *= <SignalTypeEnum.DBI\_n: 30>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DBI_n "Link to this definition")

    DERR *= <SignalTypeEnum.DERR: 37>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DERR "Link to this definition")

    DM\_n *= <SignalTypeEnum.DM\_n: 29>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DM_n "Link to this definition")

    DPAR *= <SignalTypeEnum.DPAR: 43>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DPAR "Link to this definition")

    DQ *= <SignalTypeEnum.DQ: 0>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DQ "Link to this definition")

    DQS\_c *= <SignalTypeEnum.DQS\_c: 5>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DQS_c "Link to this definition")

    DQS\_t *= <SignalTypeEnum.DQS\_t: 4>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DQS_t "Link to this definition")

    DQX *= <SignalTypeEnum.DQX: 1>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.DQX "Link to this definition")

    ECC *= <SignalTypeEnum.ECC: 41>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.ECC "Link to this definition")

    EDC *= <SignalTypeEnum.EDC: 35>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.EDC "Link to this definition")

    FWD\_N *= <SignalTypeEnum.FWD\_N: 78>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.FWD_N "Link to this definition")

    FWD\_P *= <SignalTypeEnum.FWD\_P: 77>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.FWD_P "Link to this definition")

    ODT *= <SignalTypeEnum.ODT: 21>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.ODT "Link to this definition")

    PAR *= <SignalTypeEnum.PAR: 33>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.PAR "Link to this definition")

    PARITY *= <SignalTypeEnum.PARITY: 34>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.PARITY "Link to this definition")

    R *= <SignalTypeEnum.R: 17>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.R "Link to this definition")

    RAS\_n *= <SignalTypeEnum.RAS\_n: 24>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RAS_n "Link to this definition")

    RDQS\_c *= <SignalTypeEnum.RDQS\_c: 7>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RDQS_c "Link to this definition")

    RDQS\_t *= <SignalTypeEnum.RDQS\_t: 6>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RDQS_t "Link to this definition")

    RE\_c *= <SignalTypeEnum.RE\_c: 40>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RE_c "Link to this definition")

    RE\_t *= <SignalTypeEnum.RE\_t: 39>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RE_t "Link to this definition")

    RXCKN *= <SignalTypeEnum.RXCKN: 76>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXCKN "Link to this definition")

    RXCKP *= <SignalTypeEnum.RXCKP: 75>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXCKP "Link to this definition")

    RXCKRD *= <SignalTypeEnum.RXCKRD: 59>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXCKRD "Link to this definition")

    RXCKSB *= <SignalTypeEnum.RXCKSB: 62>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXCKSB "Link to this definition")

    RXCKSBRD *= <SignalTypeEnum.RXCKSBRD: 64>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXCKSBRD "Link to this definition")

    RXDATA *= <SignalTypeEnum.RXDATA: 74>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXDATA "Link to this definition")

    RXDATARD *= <SignalTypeEnum.RXDATARD: 57>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXDATARD "Link to this definition")

    RXDATASB *= <SignalTypeEnum.RXDATASB: 61>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXDATASB "Link to this definition")

    RXDATASBRD *= <SignalTypeEnum.RXDATASBRD: 63>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXDATASBRD "Link to this definition")

    RXTRK *= <SignalTypeEnum.RXTRK: 56>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXTRK "Link to this definition")

    RXTRKRD *= <SignalTypeEnum.RXTRKRD: 60>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXTRKRD "Link to this definition")

    RXVLD *= <SignalTypeEnum.RXVLD: 55>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXVLD "Link to this definition")

    RXVLDRD *= <SignalTypeEnum.RXVLDRD: 58>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.RXVLDRD "Link to this definition")

    SEV *= <SignalTypeEnum.SEV: 42>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.SEV "Link to this definition")

    TXCKN *= <SignalTypeEnum.TXCKN: 73>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXCKN "Link to this definition")

    TXCKP *= <SignalTypeEnum.TXCKP: 72>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXCKP "Link to this definition")

    TXCKRD *= <SignalTypeEnum.TXCKRD: 49>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXCKRD "Link to this definition")

    TXCKSB *= <SignalTypeEnum.TXCKSB: 52>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXCKSB "Link to this definition")

    TXCKSBRD *= <SignalTypeEnum.TXCKSBRD: 54>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXCKSBRD "Link to this definition")

    TXDATA *= <SignalTypeEnum.TXDATA: 71>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXDATA "Link to this definition")

    TXDATARD *= <SignalTypeEnum.TXDATARD: 47>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXDATARD "Link to this definition")

    TXDATASB *= <SignalTypeEnum.TXDATASB: 51>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXDATASB "Link to this definition")

    TXDATASBRD *= <SignalTypeEnum.TXDATASBRD: 53>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXDATASBRD "Link to this definition")

    TXTRK *= <SignalTypeEnum.TXTRK: 46>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXTRK "Link to this definition")

    TXTRKRD *= <SignalTypeEnum.TXTRKRD: 50>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXTRKRD "Link to this definition")

    TXVLD *= <SignalTypeEnum.TXVLD: 45>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXVLD "Link to this definition")

    TXVLDRD *= <SignalTypeEnum.TXVLDRD: 48>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.TXVLDRD "Link to this definition")

    UNKNOWN *= <SignalTypeEnum.UNKNOWN: 86>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.UNKNOWN "Link to this definition")

    VCCAON *= <SignalTypeEnum.VCCAON: 66>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.VCCAON "Link to this definition")

    VCCIO *= <SignalTypeEnum.VCCIO: 65>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.VCCIO "Link to this definition")

    VDD *= <SignalTypeEnum.VDD: 19>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.VDD "Link to this definition")

    VPP *= <SignalTypeEnum.VPP: 20>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.VPP "Link to this definition")

    VSS *= <SignalTypeEnum.VSS: 85>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.VSS "Link to this definition")

    WCK\_c *= <SignalTypeEnum.WCK\_c: 13>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.WCK_c "Link to this definition")

    WCK\_t *= <SignalTypeEnum.WCK\_t: 12>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.WCK_t "Link to this definition")

    WDQS\_c *= <SignalTypeEnum.WDQS\_c: 9>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.WDQS_c "Link to this definition")

    WDQS\_t *= <SignalTypeEnum.WDQS\_t: 8>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.WDQS_t "Link to this definition")

    WE\_n *= <SignalTypeEnum.WE\_n: 26>*[](#keysight.ads.hsd.metadata.SignalTypeEnum.WE_n "Link to this definition")

*class* keysight.ads.hsd.metadata.SignalNodeType[](#keysight.ads.hsd.metadata.SignalNodeType "Link to this definition")
:   NEGATIVE *= <SignalNodeType.Negative: 2>*[](#keysight.ads.hsd.metadata.SignalNodeType.NEGATIVE "Link to this definition")

    POSITIVE *= <SignalNodeType.Positive: 1>*[](#keysight.ads.hsd.metadata.SignalNodeType.POSITIVE "Link to this definition")

    SINGLE\_ENDED *= <SignalNodeType.SingleEnded: 0>*[](#keysight.ads.hsd.metadata.SignalNodeType.SINGLE_ENDED "Link to this definition")

*class* keysight.ads.hsd.metadata.SignalPortTypeEnum[](#keysight.ads.hsd.metadata.SignalPortTypeEnum "Link to this definition")
:   DIFFERENTIAL *= <SignalPortTypeEnum.Differential: 0>*[](#keysight.ads.hsd.metadata.SignalPortTypeEnum.DIFFERENTIAL "Link to this definition")

    NEGATIVE *= <SignalPortTypeEnum.Negative: 3>*[](#keysight.ads.hsd.metadata.SignalPortTypeEnum.NEGATIVE "Link to this definition")

    POSITIVE *= <SignalPortTypeEnum.Positive: 2>*[](#keysight.ads.hsd.metadata.SignalPortTypeEnum.POSITIVE "Link to this definition")

    SINGLE\_ENDED *= <SignalPortTypeEnum.SingleEnded: 1>*[](#keysight.ads.hsd.metadata.SignalPortTypeEnum.SINGLE_ENDED "Link to this definition")

*class* keysight.ads.hsd.metadata.PortInfoSimilarity[](#keysight.ads.hsd.metadata.PortInfoSimilarity "Link to this definition")
:   HAS\_ALT\_SIGNAL\_ID\_SAME\_AS\_SIGNAL\_ID *= <PortInfoSimilarity.HasAltSignalIdSameAsSignalId: 5>*[](#keysight.ads.hsd.metadata.PortInfoSimilarity.HAS_ALT_SIGNAL_ID_SAME_AS_SIGNAL_ID "Link to this definition")

    HAS\_SAME\_ALT\_SIGNAL\_IDS *= <PortInfoSimilarity.HasSameAltSignalIds: 2>*[](#keysight.ads.hsd.metadata.PortInfoSimilarity.HAS_SAME_ALT_SIGNAL_IDS "Link to this definition")

    HAS\_SAME\_SIGNAL\_IDS *= <PortInfoSimilarity.HasSameSignalIds: 1>*[](#keysight.ads.hsd.metadata.PortInfoSimilarity.HAS_SAME_SIGNAL_IDS "Link to this definition")

    HAS\_SAME\_SIGNAL\_ID\_AND\_ALT\_SIGNAL\_ID *= <PortInfoSimilarity.HasSameSignalIdAndAltSignalId: 3>*[](#keysight.ads.hsd.metadata.PortInfoSimilarity.HAS_SAME_SIGNAL_ID_AND_ALT_SIGNAL_ID "Link to this definition")

    HAS\_SIGNAL\_ID\_SAME\_AS\_ALT\_SIGNAL\_ID *= <PortInfoSimilarity.HasSignalIdSameAsAltSignalId: 4>*[](#keysight.ads.hsd.metadata.PortInfoSimilarity.HAS_SIGNAL_ID_SAME_AS_ALT_SIGNAL_ID "Link to this definition")

*class* keysight.ads.hsd.metadata.PortConnectivityCollisionType[](#keysight.ads.hsd.metadata.PortConnectivityCollisionType "Link to this definition")
:   ALT\_SIGNAL\_ID\_COLLIDING *= <PortConnectivityCollisionType.AltSignalIdColliding: 2>*[](#keysight.ads.hsd.metadata.PortConnectivityCollisionType.ALT_SIGNAL_ID_COLLIDING "Link to this definition")

    NO\_COLLISION *= <PortConnectivityCollisionType.NoCollision: 0>*[](#keysight.ads.hsd.metadata.PortConnectivityCollisionType.NO_COLLISION "Link to this definition")

    SIGNAL\_ID\_AND\_ALT\_SIGNAL\_ID\_COLLIDING *= <PortConnectivityCollisionType.SignalIdAndAltSignalIdColliding: 3>*[](#keysight.ads.hsd.metadata.PortConnectivityCollisionType.SIGNAL_ID_AND_ALT_SIGNAL_ID_COLLIDING "Link to this definition")

    SIGNAL\_ID\_COLLIDING *= <PortConnectivityCollisionType.SignalIdColliding: 1>*[](#keysight.ads.hsd.metadata.PortConnectivityCollisionType.SIGNAL_ID_COLLIDING "Link to this definition")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.metadata.SignalType[](#keysight.ads.hsd.metadata.SignalType "Link to this definition")
:   *property* is\_differential\_type*: bool*[](#keysight.ads.hsd.metadata.SignalType.is_differential_type "Link to this definition")

    *property* is\_power\_type*: bool*[](#keysight.ads.hsd.metadata.SignalType.is_power_type "Link to this definition")

    *property* name*: str*[](#keysight.ads.hsd.metadata.SignalType.name "Link to this definition")

    *property* name\_without\_polarity*: str*[](#keysight.ads.hsd.metadata.SignalType.name_without_polarity "Link to this definition")

    *property* pair*: [SignalType](#keysight.ads.hsd.metadata.SignalType "keysight.ads.hsd._common.metadata.SignalType")*[](#keysight.ads.hsd.metadata.SignalType.pair "Link to this definition")

    *property* signal\_node\_type*: [SignalNodeType](#keysight.ads.hsd.metadata.SignalNodeType "keysight.ads.hsd._common.metadata.SignalNodeType")*[](#keysight.ads.hsd.metadata.SignalType.signal_node_type "Link to this definition")

    *property* type*: [SignalTypeEnum](#keysight.ads.hsd.metadata.SignalTypeEnum "keysight.ads.hsd._common.metadata.SignalTypeEnum")*[](#keysight.ads.hsd.metadata.SignalType.type "Link to this definition")

*class* keysight.ads.hsd.metadata.SignalId[](#keysight.ads.hsd.metadata.SignalId "Link to this definition")
:   *property* index*: int*[](#keysight.ads.hsd.metadata.SignalId.index "Link to this definition")

    *property* is\_power\_type*: bool*[](#keysight.ads.hsd.metadata.SignalId.is_power_type "Link to this definition")

    *property* is\_signal\_type\_unknown*: bool*[](#keysight.ads.hsd.metadata.SignalId.is_signal_type_unknown "Link to this definition")

    is\_valid\_and\_same\_as(*other: [SignalId](#keysight.ads.hsd.metadata.SignalId "keysight.ads.hsd._common.metadata.SignalId")*) → bool[](#keysight.ads.hsd.metadata.SignalId.is_valid_and_same_as "Link to this definition")

    *property* type*: [SignalType](#keysight.ads.hsd.metadata.SignalType "keysight.ads.hsd._common.metadata.SignalType")*[](#keysight.ads.hsd.metadata.SignalId.type "Link to this definition")

    *property* type\_name*: str*[](#keysight.ads.hsd.metadata.SignalId.type_name "Link to this definition")

*class* keysight.ads.hsd.metadata.PortInfo[](#keysight.ads.hsd.metadata.PortInfo "Link to this definition")
:   *property* alt\_signal\_index*: int | None*[](#keysight.ads.hsd.metadata.PortInfo.alt_signal_index "Link to this definition")

    *property* alt\_signal\_type*: [SignalType](#keysight.ads.hsd.metadata.SignalType "keysight.ads.hsd._common.metadata.SignalType") | None*[](#keysight.ads.hsd.metadata.PortInfo.alt_signal_type "Link to this definition")

    *property* channel\_id*: str*[](#keysight.ads.hsd.metadata.PortInfo.channel_id "Link to this definition")

    *property* connected\_pin\_list*: list[str]*[](#keysight.ads.hsd.metadata.PortInfo.connected_pin_list "Link to this definition")

    copy\_with\_new\_port\_name(*new\_port\_name: str*) → [PortInfo](#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo")[](#keysight.ads.hsd.metadata.PortInfo.copy_with_new_port_name "Link to this definition")
    :   Returns a deep copy of this port info object with the new port name.

        Since port\_name cannot be changed directly, this method is used to create a new port info object with the new port name.

        Parameters:
        :   **(****str****)** (*new\_port\_name*)

    *property* has\_alt\_signal\_id*: bool*[](#keysight.ads.hsd.metadata.PortInfo.has_alt_signal_id "Link to this definition")

    *property* is\_terminated*: bool*[](#keysight.ads.hsd.metadata.PortInfo.is_terminated "Link to this definition")

    *property* port\_name*: str*[](#keysight.ads.hsd.metadata.PortInfo.port_name "Link to this definition")

    *property* ref\_des*: str*[](#keysight.ads.hsd.metadata.PortInfo.ref_des "Link to this definition")

    *property* signal\_id*: [SignalId](#keysight.ads.hsd.metadata.SignalId "keysight.ads.hsd._common.metadata.SignalId")*[](#keysight.ads.hsd.metadata.PortInfo.signal_id "Link to this definition")

    *property* signal\_index*: int*[](#keysight.ads.hsd.metadata.PortInfo.signal_index "Link to this definition")

    *property* signal\_type*: [SignalType](#keysight.ads.hsd.metadata.SignalType "keysight.ads.hsd._common.metadata.SignalType")*[](#keysight.ads.hsd.metadata.PortInfo.signal_type "Link to this definition")

    *property* termination\_value*: float*[](#keysight.ads.hsd.metadata.PortInfo.termination_value "Link to this definition")

*class* keysight.ads.hsd.metadata.MetaData[](#keysight.ads.hsd.metadata.MetaData "Link to this definition")
:   \_\_bool\_\_() → bool[](#keysight.ads.hsd.metadata.MetaData.__bool__ "Link to this definition")

    \_\_contains\_\_(*port\_info: [PortInfo](#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo") | str*) → bool[](#keysight.ads.hsd.metadata.MetaData.__contains__ "Link to this definition")

    \_\_getitem\_\_(*key: str | int*) → [PortInfo](#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo")[](#keysight.ads.hsd.metadata.MetaData.__getitem__ "Link to this definition")

    \_\_iter\_\_() → Iterator[[PortInfo](#keysight.ads.hsd.metadata.PortInfo "keysight.ads.hsd._common.metadata.PortInfo")][](#keysight.ads.hsd.metadata.MetaData.__iter__ "Link to this definition")

    \_\_len\_\_() → int[](#keysight.ads.hsd.metadata.MetaData.__len__ "Link to this definition")

    \_\_str\_\_() → str[](#keysight.ads.hsd.metadata.MetaData.__str__ "Link to this definition")
    :   Return str(self).

    apply(*other\_metadata: [MetaData](#keysight.ads.hsd.metadata.MetaData "keysight.ads.hsd._common.metadata.MetaData")*) → None[](#keysight.ads.hsd.metadata.MetaData.apply "Link to this definition")
    :   Applies the port info(s) with the same port name(s) from the other metadata to this metadata.

On this page

[Previous

Core](core.md)
[Next

Smart Wire](smartwire.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top