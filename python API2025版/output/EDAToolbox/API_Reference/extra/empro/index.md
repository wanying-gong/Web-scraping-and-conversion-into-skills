<!-- 来源: API_Reference\extra\empro\index.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../../../index.md)
* [API Reference](../../index.md)
* [External API](../index.md)
* empro.analysis

1.2.4

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../../_sources/API_Reference/extra/empro/index.rst.txt)

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

* [API Reference](../../index.md)
  + [ADS](../../ads/index.md)
    - [Functions](../../ads/functions/index.md)
    - [Classes](../../ads/classes/index.md)
      * [ADS](../../ads/classes/ads.md)
      * [CircuitSimulator](../../ads/classes/circuit_simulator.md)
  + [Circuit API](../../circuit/index.md)
    - [Functions](../../circuit/functions/index.md)
    - [Classes](../../circuit/classes/index.md)
      * [Circuit](../../circuit/classes/circuit.md)
      * [Definition](../../circuit/classes/definition.md)
      * [Instance](../../circuit/classes/instance.md)
      * [Node](../../circuit/classes/node.md)
      * [OptimizationRange](../../circuit/classes/optimization_range.md)
      * [TuningRange](../../circuit/classes/tuning_range.md)
      * [Value](../../circuit/classes/value.md)
  + [Dataset](../../dataset/index.md)
  + [External API](../index.md)
    - empro.analysis
  + [Multi Python API](../../multi_python/index.md)
    - [Functions](../../multi_python/functions/index.md)
  + [xxPro](../../xxpro/index.md)
* [Initial Setup](../../../Initial_Setup/index.md)
  + [Installation](../../../Initial_Setup/installation.md)
  + [Prerequisites](../../../Initial_Setup/prerequisites.md)
  + [Verifying Installation](../../../Initial_Setup/verifying.md)
  + [SSH](../../../Initial_Setup/ssh.md)
* [Examples](../../../Examples/index.md)
* [How-To](../../../How-To/index.md)
  + [Create a Circuit](../../../How-To/circuit.md)
  + [Run a Circuit Simulation](../../../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../../../How-To/sipro.md)
* [Release Notes](../../../release_notes/index.md)

# empro.analysis[](#empro-analysis "Link to this heading")

*class* empro.analysis.Analysis[](#empro.analysis.Analysis "Link to this definition")
:   An analysis that is used to specify what needs to be analysed in SI/PI/PE/RFPro.

    *property* analysisType[](#empro.analysis.Analysis.analysisType "Link to this definition")
    :   The type of analysis to be performed. Any choice of empro.analysis.Analysis[‘DCAnalysisType’, ‘DDRAnalysisType’, ‘EMFUAnalysisType’, ‘EMFUPEAnalysisType’, ‘EMSMAnalysisType’, ‘EMUDAnalysisType’, ‘EMUDPEAnalysisType’, ‘ETHAnalysisType’, ‘PASIAnalysisType’, ‘PPRAnalysisType’, ‘SMPSPERFAnalysisType’, ‘THAnalysisType’]

    *property* componentModelGroups[](#empro.analysis.Analysis.componentModelGroups "Link to this definition")
    :   The list of component model groups as empro.analysis.ComponentModelGroupList.

    *property* name[](#empro.analysis.Analysis.name "Link to this definition")
    :   The name of the analysis. It cannot contain any special characters, when it does, the analysis may become invalid.

    *property* nets[](#empro.analysis.Analysis.nets "Link to this definition")
    :   The list of nets part of this analysis when applicable to analysis type.

    *property* ports[](#empro.analysis.Analysis.ports "Link to this definition")
    :   The list of ports of this analysis when applicable.

    requiredNets()[](#empro.analysis.Analysis.requiredNets "Link to this definition")
    :   Returns the list of required nets to complete this analysis.

        ```
        >>> for net in analysis.requiredNets():
        ...    analysis.nets.append(net)
        ```

    *property* sinks[](#empro.analysis.Analysis.sinks "Link to this definition")
    :   The Sinks of this analysis. Applies to PIPro.

    *property* vrms[](#empro.analysis.Analysis.vrms "Link to this definition")
    :   The VRMs of this analysis. Applies to PIPro.

    isValid()[](#empro.analysis.Analysis.isValid "Link to this definition")
    :   Returns True when the analysis is valid

    reasonWhyInvalid()[](#empro.analysis.Analysis.reasonWhyInvalid "Link to this definition")
    :   When the analysis is invalid returns the reason why it is invalid.

*class* empro.analysis.ComponentModelGroupList[](#empro.analysis.ComponentModelGroupList "Link to this definition")
:   A container for component model groups, part of an analysis.

On this page

[Previous

External API](../index.md)
[Next

Multi Python API](../../multi_python/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top