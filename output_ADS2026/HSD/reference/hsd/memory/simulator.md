<!-- 来源: reference\hsd\memory\simulator.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [HSD Python Documentation](../../../index.md)
* [Reference](../../index.md)
* [keysight.ads.hsd.memory](index.md)
* Memory Interface Simulator

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
    - Memory Interface Simulator
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

# Memory Interface Simulator[](#memory-interface-simulator "Link to this heading")

*class* keysight.ads.hsd.memory.simulator.SimulationMode[](#keysight.ads.hsd.memory.simulator.SimulationMode "Link to this definition")
:   Bases: `EnumWrapper`

    BIT\_BY\_BIT *= <SimulationMode.BITBYBIT: 0>*[](#keysight.ads.hsd.memory.simulator.SimulationMode.BIT_BY_BIT "Link to this definition")

    STATISTICAL *= <SimulationMode.STATISTICAL: 1>*[](#keysight.ads.hsd.memory.simulator.SimulationMode.STATISTICAL "Link to this definition")

    S\_PARAMETER *= <SimulationMode.SPARAMETER: 4>*[](#keysight.ads.hsd.memory.simulator.SimulationMode.S_PARAMETER "Link to this definition")

    TRANSIENT *= <SimulationMode.TRANSIENT: 5>*[](#keysight.ads.hsd.memory.simulator.SimulationMode.TRANSIENT "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.PassivityMode[](#keysight.ads.hsd.memory.simulator.PassivityMode "Link to this definition")
:   Bases: `EnumWrapper`

    NONE *= <PassivityMode.NONE: 0>*[](#keysight.ads.hsd.memory.simulator.PassivityMode.NONE "Link to this definition")

    NORMAL *= <PassivityMode.NORMAL: 1>*[](#keysight.ads.hsd.memory.simulator.PassivityMode.NORMAL "Link to this definition")

    STRICT *= <PassivityMode.STRICT: 2>*[](#keysight.ads.hsd.memory.simulator.PassivityMode.STRICT "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.ToleranceMode[](#keysight.ads.hsd.memory.simulator.ToleranceMode "Link to this definition")
:   Bases: `EnumWrapper`

    AUTO *= <ToleranceMode.AUTO: 1>*[](#keysight.ads.hsd.memory.simulator.ToleranceMode.AUTO "Link to this definition")

    RELAX *= <ToleranceMode.RELAX: 0>*[](#keysight.ads.hsd.memory.simulator.ToleranceMode.RELAX "Link to this definition")

    STRICT *= <ToleranceMode.STRICT: 2>*[](#keysight.ads.hsd.memory.simulator.ToleranceMode.STRICT "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.TimeStepControlMethod[](#keysight.ads.hsd.memory.simulator.TimeStepControlMethod "Link to this definition")
:   Bases: `EnumWrapper`

    FIXED *= <TimeStepControlMethod.FIXED: 0>*[](#keysight.ads.hsd.memory.simulator.TimeStepControlMethod.FIXED "Link to this definition")

    ITERATION\_COUNT *= <TimeStepControlMethod.ITERATION\_COUNT: 1>*[](#keysight.ads.hsd.memory.simulator.TimeStepControlMethod.ITERATION_COUNT "Link to this definition")

    TRUNC\_ERROR *= <TimeStepControlMethod.TRUNC\_ERROR: 2>*[](#keysight.ads.hsd.memory.simulator.TimeStepControlMethod.TRUNC_ERROR "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.IntegrationMethod[](#keysight.ads.hsd.memory.simulator.IntegrationMethod "Link to this definition")
:   Bases: `EnumWrapper`

    GEAR *= <IntegrationMethod.GEAR: 1>*[](#keysight.ads.hsd.memory.simulator.IntegrationMethod.GEAR "Link to this definition")

    TRAPEZOIDAL *= <IntegrationMethod.TRAPEZOIDAL: 0>*[](#keysight.ads.hsd.memory.simulator.IntegrationMethod.TRAPEZOIDAL "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern "Link to this definition")
:   Bases: `EnumWrapper`

    CONTINUOUS\_BITS *= <XtlkAnalysisBitPattern.CONTINUOUS\_BITS: 0>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern.CONTINUOUS_BITS "Link to this definition")

    SINGLE\_BIT *= <XtlkAnalysisBitPattern.SINGLE\_BIT: 1>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern.SINGLE_BIT "Link to this definition")

    STEP\_FALL *= <XtlkAnalysisBitPattern.STEP\_FALL: 3>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern.STEP_FALL "Link to this definition")

    STEP\_RISE *= <XtlkAnalysisBitPattern.STEP\_RISE: 2>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern.STEP_RISE "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.CrosstalkAnalysisVictimMode[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisVictimMode "Link to this definition")
:   Bases: `EnumWrapper`

    HIGHSTATE *= <XtlkAnalysisVictimMode.HIGHSTATE: 0>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisVictimMode.HIGHSTATE "Link to this definition")

    LOWSTATE *= <XtlkAnalysisVictimMode.LOWSTATE: 1>*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisVictimMode.LOWSTATE "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.SparamSweepType[](#keysight.ads.hsd.memory.simulator.SparamSweepType "Link to this definition")
:   Bases: `EnumWrapper`

    LINEAR *= <SweepType.LINEAR: 1>*[](#keysight.ads.hsd.memory.simulator.SparamSweepType.LINEAR "Link to this definition")

    LOG *= <SweepType.LOG: 2>*[](#keysight.ads.hsd.memory.simulator.SparamSweepType.LOG "Link to this definition")

    SINGLE\_POINT *= <SweepType.SINGLE\_POINT: 0>*[](#keysight.ads.hsd.memory.simulator.SparamSweepType.SINGLE_POINT "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.SparamSweepMode[](#keysight.ads.hsd.memory.simulator.SparamSweepMode "Link to this definition")
:   Bases: `EnumWrapper`

    CENTER\_SPAN *= <SweepMode.CENTER\_SPAN: 1>*[](#keysight.ads.hsd.memory.simulator.SparamSweepMode.CENTER_SPAN "Link to this definition")

    START\_STOP *= <SweepMode.START\_STOP: 0>*[](#keysight.ads.hsd.memory.simulator.SparamSweepMode.START_STOP "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.SparamTermPlacement[](#keysight.ads.hsd.memory.simulator.SparamTermPlacement "Link to this definition")
:   Bases: `EnumWrapper`

    CONTROLLER\_DIE\_TO\_MEMORY\_DIE *= <TermPlacementOption.CONTROLLER\_DIE\_TO\_MEMORY\_DIE: 2>*[](#keysight.ads.hsd.memory.simulator.SparamTermPlacement.CONTROLLER_DIE_TO_MEMORY_DIE "Link to this definition")

    CONTROLLER\_DIE\_TO\_MEMORY\_PACKAGE *= <TermPlacementOption.CONTROLLER\_DIE\_TO\_MEMORY\_PACKAGE: 3>*[](#keysight.ads.hsd.memory.simulator.SparamTermPlacement.CONTROLLER_DIE_TO_MEMORY_PACKAGE "Link to this definition")

    CONTROLLER\_PACKAGE\_TO\_MEMORY\_DIE *= <TermPlacementOption.CONTROLLER\_PACKAGE\_TO\_MEMORY\_DIE: 4>*[](#keysight.ads.hsd.memory.simulator.SparamTermPlacement.CONTROLLER_PACKAGE_TO_MEMORY_DIE "Link to this definition")

    CONTROLLER\_PACKAGE\_TO\_MEMORY\_PACKAGE *= <TermPlacementOption.CONTROLLER\_PACKAGE\_TO\_MEMORY\_PACKAGE: 5>*[](#keysight.ads.hsd.memory.simulator.SparamTermPlacement.CONTROLLER_PACKAGE_TO_MEMORY_PACKAGE "Link to this definition")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting "Link to this definition")
:   Bases: `CommonConvolutionSettings`

    *property* anti\_aliasing\_window\_size*: int*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.anti_aliasing_window_size "Link to this definition")

    *property* max\_impulse\_response\_frequency*: float | None*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.max_impulse_response_frequency "Link to this definition")

    *property* max\_impulse\_response\_length*: int*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.max_impulse_response_length "Link to this definition")

    *property* number\_of\_time\_points\_per\_UI*: int*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.number_of_time_points_per_UI "Link to this definition")

    *property* passivity\_mode*: [PassivityMode](#keysight.ads.hsd.memory.simulator.PassivityMode "keysight.ads.hsd._common.simulators.PassivityMode")*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.passivity_mode "Link to this definition")

    *property* reuse\_cached\_impulse\_response*: bool*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.reuse_cached_impulse_response "Link to this definition")

    *property* save\_characterization\_result*: bool*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.save_characterization_result "Link to this definition")

    *property* size\_of\_processing\_block*: int*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.size_of_processing_block "Link to this definition")

    *property* tolerance\_mode*: [ToleranceMode](#keysight.ads.hsd.memory.simulator.ToleranceMode "keysight.ads.hsd._common.simulators.ToleranceMode")*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.tolerance_mode "Link to this definition")

    *property* use\_transient\_low\_freq\_extrapolation*: bool*[](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting.use_transient_low_freq_extrapolation "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.TransientConvolutionSetting[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting "Link to this definition")
:   Bases: `CommonConvolutionSettings`

    *property* absolute\_impulse\_response\_truncation*: float*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.absolute_impulse_response_truncation "Link to this definition")

    *property* number\_of\_passes\_for\_impulse\_calculation*: int | None*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.number_of_passes_for_impulse_calculation "Link to this definition")

    *property* passivity\_mode*: [PassivityMode](#keysight.ads.hsd.memory.simulator.PassivityMode "keysight.ads.hsd._common.simulators.PassivityMode")*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.passivity_mode "Link to this definition")

    *property* relative\_impulse\_response\_truncation\_factor*: float*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.relative_impulse_response_truncation_factor "Link to this definition")

    *property* save\_impulse\_spectrum*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.save_impulse_spectrum "Link to this definition")

    *property* short\_tline\_delay*: str*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.short_tline_delay "Link to this definition")

    *property* tolerance\_mode*: [ToleranceMode](#keysight.ads.hsd.memory.simulator.ToleranceMode "keysight.ads.hsd._common.simulators.ToleranceMode")*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.tolerance_mode "Link to this definition")

    *property* transient\_delta\_impulse\_frequency*: str*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.transient_delta_impulse_frequency "Link to this definition")

    *property* transient\_max\_impulse\_frequency*: str*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.transient_max_impulse_frequency "Link to this definition")

    *property* use\_approximate\_models*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.use_approximate_models "Link to this definition")

    *property* use\_transient\_low\_freq\_extrapolation*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting.use_transient_low_freq_extrapolation "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.TransientConvergenceSettings[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings "Link to this definition")
:   Bases: `object`

    *property* check\_only\_delta\_voltage*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.check_only_delta_voltage "Link to this definition")

    *property* check\_strange\_behavior\_at\_every\_timestep*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.check_strange_behavior_at_every_timestep "Link to this definition")

    *property* connect\_all\_nodes\_to\_ground*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.connect_all_nodes_to_ground "Link to this definition")

    *property* iv\_relative\_tolerance*: float | None*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.iv_relative_tolerance "Link to this definition")

    *property* max\_iteration\_per\_time\_step*: int*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.max_iteration_per_time_step "Link to this definition")

    *property* max\_iterations\_at\_initial\_dc*: int*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.max_iterations_at_initial_dc "Link to this definition")

    *property* perform\_kcl\_check*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.perform_kcl_check "Link to this definition")

    *property* skip\_device\_evaluation*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.skip_device_evaluation "Link to this definition")

    *property* use\_custom\_initial\_condition*: bool*[](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings.use_custom_initial_condition "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.TransientIntegrationSettings[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings "Link to this definition")
:   Bases: `object`

    *property* charge\_accuracy*: float*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.charge_accuracy "Link to this definition")

    *property* integration\_coefficient\_mu*: float | None*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.integration_coefficient_mu "Link to this definition")

    *property* integration\_method*: [IntegrationMethod](#keysight.ads.hsd.memory.simulator.IntegrationMethod "keysight.ads.hsd._common.simulators.IntegrationMethod")*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.integration_method "Link to this definition")

    *property* max\_gear\_order*: int*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.max_gear_order "Link to this definition")

    *property* time\_step\_control\_method*: [TimeStepControlMethod](#keysight.ads.hsd.memory.simulator.TimeStepControlMethod "keysight.ads.hsd._common.simulators.TimeStepControlMethod")*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.time_step_control_method "Link to this definition")

    *property* truncation\_error\_factor*: float*[](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings.truncation_error_factor "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings "Link to this definition")
:   Bases: `object`

    *property* bit\_pattern*: [CrosstalkAnalysisBitPattern](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisBitPattern "keysight.ads.hsd._common.simulators.CrosstalkAnalysisBitPattern")*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings.bit_pattern "Link to this definition")

    *property* enabled*: bool*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings.enabled "Link to this definition")

    *property* victim\_mode*: [CrosstalkAnalysisVictimMode](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisVictimMode "keysight.ads.hsd._common.simulators.CrosstalkAnalysisVictimMode")*[](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings.victim_mode "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings[](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings "Link to this definition")
:   Bases: `object`

    *property* enabled*: bool*[](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings.enabled "Link to this definition")

    *property* limit\_in\_db*: int*[](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings.limit_in_db "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.SParamSweepSettings[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings "Link to this definition")
:   Bases: `object`

    *property* center*: str*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.center "Link to this definition")

    *property* is\_using\_number\_of\_points*: bool*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.is_using_number_of_points "Link to this definition")

    *property* number\_of\_points*: int*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.number_of_points "Link to this definition")

    *property* points\_per\_decade*: int*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.points_per_decade "Link to this definition")

    *property* span*: str*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.span "Link to this definition")

    *property* start*: str*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.start "Link to this definition")

    *property* step\_size*: str*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.step_size "Link to this definition")

    *property* stop*: str*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.stop "Link to this definition")

    *property* sweep\_mode*: [SparamSweepMode](#keysight.ads.hsd.memory.simulator.SparamSweepMode "keysight.ads.hsd._common.simulators.SparamSweepMode")*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.sweep_mode "Link to this definition")

    *property* sweep\_type*: [SparamSweepType](#keysight.ads.hsd.memory.simulator.SparamSweepType "keysight.ads.hsd._common.simulators.SparamSweepType")*[](#keysight.ads.hsd.memory.simulator.SParamSweepSettings.sweep_type "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.BitByBitSimulation[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation "Link to this definition")
:   Bases: `CommonSimulator`

    *property* convolution\_settings*: [ChannelSimConvolutionSetting](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting "keysight.ads.hsd._common.simulators.ChannelSimConvolutionSetting")*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.convolution_settings "Link to this definition")

    *property* crosstalk\_analysis\_settings*: [CrosstalkAnalysisSettings](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings "keysight.ads.hsd._common.simulators.CrosstalkAnalysisSettings")*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.crosstalk_analysis_settings "Link to this definition")

    *property* crosstalk\_limiter\_settings*: [CrosstalkLimiterSettings](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings "keysight.ads.hsd._common.simulators.CrosstalkLimiterSettings")*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.crosstalk_limiter_settings "Link to this definition")

    *property* enable\_low\_BER\_floor*: bool*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.enable_low_BER_floor "Link to this definition")

    *property* number\_of\_bits*: int*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.number_of_bits "Link to this definition")

    *property* simulation\_mode*: [SimulationMode](#keysight.ads.hsd.memory.simulator.SimulationMode "keysight.ads.hsd._common.simulators.SimulationMode")*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.simulation_mode "Link to this definition")

    *property* status\_level*: str*[](#keysight.ads.hsd.memory.simulator.BitByBitSimulation.status_level "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.StatisticalSimulation[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation "Link to this definition")
:   Bases: `CommonSimulator`

    *property* convolution\_settings*: [ChannelSimConvolutionSetting](#keysight.ads.hsd.memory.simulator.ChannelSimConvolutionSetting "keysight.ads.hsd._common.simulators.ChannelSimConvolutionSetting")*[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation.convolution_settings "Link to this definition")

    *property* crosstalk\_limiter\_settings*: [CrosstalkLimiterSettings](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings "keysight.ads.hsd._common.simulators.CrosstalkLimiterSettings")*[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation.crosstalk_limiter_settings "Link to this definition")

    *property* enable\_low\_BER\_floor*: bool*[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation.enable_low_BER_floor "Link to this definition")

    *property* simulation\_mode*: [SimulationMode](#keysight.ads.hsd.memory.simulator.SimulationMode "keysight.ads.hsd._common.simulators.SimulationMode")*[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation.simulation_mode "Link to this definition")

    *property* status\_level*: str*[](#keysight.ads.hsd.memory.simulator.StatisticalSimulation.status_level "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.TransientSimulation[](#keysight.ads.hsd.memory.simulator.TransientSimulation "Link to this definition")
:   Bases: `CommonSimulator`

    *property* convergence\_settings*: [TransientConvergenceSettings](#keysight.ads.hsd.memory.simulator.TransientConvergenceSettings "keysight.ads.hsd._common.simulators.TransientConvergenceSettings")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.convergence_settings "Link to this definition")

    *property* convolution\_settings*: [TransientConvolutionSetting](#keysight.ads.hsd.memory.simulator.TransientConvolutionSetting "keysight.ads.hsd._common.simulators.TransientConvolutionSetting")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.convolution_settings "Link to this definition")

    *property* crosstalk\_analysis\_settings*: [CrosstalkAnalysisSettings](#keysight.ads.hsd.memory.simulator.CrosstalkAnalysisSettings "keysight.ads.hsd._common.simulators.CrosstalkAnalysisSettings")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.crosstalk_analysis_settings "Link to this definition")

    *property* crosstalk\_limiter\_settings*: [CrosstalkLimiterSettings](#keysight.ads.hsd.memory.simulator.CrosstalkLimiterSettings "keysight.ads.hsd._common.simulators.CrosstalkLimiterSettings")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.crosstalk_limiter_settings "Link to this definition")

    *property* enable\_low\_BER\_floor*: bool*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.enable_low_BER_floor "Link to this definition")

    *property* integration\_settings*: [TransientIntegrationSettings](#keysight.ads.hsd.memory.simulator.TransientIntegrationSettings "keysight.ads.hsd._common.simulators.TransientIntegrationSettings")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.integration_settings "Link to this definition")

    *property* limit\_time\_step\_for\_tline*: bool*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.limit_time_step_for_tline "Link to this definition")

    *property* max\_time\_step*: str*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.max_time_step "Link to this definition")

    *property* min\_time\_step*: str*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.min_time_step "Link to this definition")

    *property* simulation\_mode*: [SimulationMode](#keysight.ads.hsd.memory.simulator.SimulationMode "keysight.ads.hsd._common.simulators.SimulationMode")*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.simulation_mode "Link to this definition")

    *property* start\_time*: str*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.start_time "Link to this definition")

    *property* status\_level*: str*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.status_level "Link to this definition")

    *property* stop\_time*: str*[](#keysight.ads.hsd.memory.simulator.TransientSimulation.stop_time "Link to this definition")

*class* keysight.ads.hsd.memory.simulator.SParameterSimulation[](#keysight.ads.hsd.memory.simulator.SParameterSimulation "Link to this definition")
:   Bases: `CommonSimulator`

    *property* enable\_low\_BER\_floor*: bool*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.enable_low_BER_floor "Link to this definition")

    *property* open\_sparam\_toolkit*: bool*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.open_sparam_toolkit "Link to this definition")

    *property* reference\_impedance*: float*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.reference_impedance "Link to this definition")

    *property* simulation\_mode*: [SimulationMode](#keysight.ads.hsd.memory.simulator.SimulationMode "keysight.ads.hsd._common.simulators.SimulationMode")*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.simulation_mode "Link to this definition")

    *property* sparam\_sweep*: [SParamSweepSettings](#keysight.ads.hsd.memory.simulator.SParamSweepSettings "keysight.ads.hsd._common.simulators.SParamSweepSettings")*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.sparam_sweep "Link to this definition")

    *property* status\_level*: str*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.status_level "Link to this definition")

    *property* termination\_placement*: [SparamTermPlacement](#keysight.ads.hsd.memory.simulator.SparamTermPlacement "keysight.ads.hsd._common.simulators.SparamTermPlacement")*[](#keysight.ads.hsd.memory.simulator.SParameterSimulation.termination_placement "Link to this definition")

On this page

[Previous

Memory DRAM](ddr_memory.md)
[Next

Memory Probe](probe.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top