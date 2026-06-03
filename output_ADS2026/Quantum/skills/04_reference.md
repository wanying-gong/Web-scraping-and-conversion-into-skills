# Reference
> **说明：** Reference 相关页面。

> **何时使用：** 当你需要查阅 Reference 相关内容时

---

## 本文件目录

- **Reference** (`reference/index.md`)
- **Dilution Fridge Input Line Designer** (`reference/quantum/dilution_fridge_input_line_designer.md`)
- **Hamiltonian Analysis** (`reference/quantum/hamiltonian_analysis.md`)
- **Quantum Addon** (`reference/quantum/index.md`)
- **Parameter Extraction** (`reference/quantum/parameter_extraction.md`)
- **SQUID Extrema Analysis** (`reference/quantum/squid_extrema_analysis.md`)
- **Time Dynamics Analysis** (`reference/quantum/time_dynamics_analysis.md`)

---

<!-- === 来源: reference/index.md === -->

# Reference[](#reference "Link to this heading")

* [Quantum Addon](quantum/index.md)

**Indices**

* [Index](../genindex.md)
* [Module Index](../py-modindex.md)


---

<!-- === 来源: reference/quantum/dilution_fridge_input_line_designer.md === -->

# Dilution Fridge Input Line Designer[](#dilution-fridge-input-line-designer "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_design\_tools.python.dilution\_fridge\_input\_line\_designer.DilutionFridgeInputLineParams[](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineParams "Link to this definition")
:   \_\_init\_\_(*params: dict | None = None*)[](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineParams.__init__ "Link to this definition")
    :   Leave `params` empty to use the dilution fridge’s default parameters.

        If using a custom set of parameters, they should match the parameter names per the DilutionFridgeInputLine component.
        [`get_default_params()`](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineParams.get_default_params "quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineParams.get_default_params") can be used as a convenient baseline to modify.

    get\_default\_params() → dict[](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineParams.get_default_params "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_design\_tools.python.dilution\_fridge\_input\_line\_designer.InstanceParams[](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.InstanceParams "Link to this definition")
:   \_\_init\_\_(*dilution\_fridge\_input\_line\_params: [DilutionFridgeInputLineParams](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineParams "quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineParams") | None = None*, *ac\_params: dict | None = None*)[](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.InstanceParams.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_design\_tools.python.dilution\_fridge\_input\_line\_designer.DilutionFridgeInputLineDesigner[](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineDesigner "Link to this definition")
:   \_\_init\_\_(*design: Design*, *clear\_design: bool = True*, *\_parent\_dialog: DilutionFridgeInputLineDesignerDialog | None = None*)[](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineDesigner.__init__ "Link to this definition")
    :   Initialize the DilutionFridgeInputLineDesigner.

        Parameters:
        :   * **design** (*db.Design*) – The schematic design to operate on.
            * **clear\_design** (*bool*) – Whether to clear the design before adding new instances. Recommended to keep this True; True is the default.
            * **\_parent\_dialog** (*Optional**[**DilutionFridgeInputLineDesignerDialog**]*) – An internally used parameter and can be ignored by the user.

    add\_instances\_to\_design(*instance\_params: [InstanceParams](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.InstanceParams "quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.InstanceParams") | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineDesigner.add_instances_to_design "Link to this definition")
    :   Set up the schematic’s design to one that is designed to simulate a dilution fridge input line.

        Parameters:
        :   **instance\_params** ([*InstanceParams*](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.InstanceParams "quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.InstanceParams")) – The parameters to use for the instances (DilutionFridgeInputLine and AC sim block) being added to the design.

    setup\_data\_display\_window(*dds\_file\_name: str | None = None*, *dds\_dir: Path | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineDesigner.setup_data_display_window "Link to this definition")
    :   Set up the graphs and equations of a DDS window to display the most notable results of the dilution fridge simulation.

        Able to be used standalone, but the equations it adds rely on the setup generated via [`add_instances_to_design()`](#quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineDesigner.add_instances_to_design "quantum_addon.src.keysight.ads.quantum_design_tools.python.dilution_fridge_input_line_designer.DilutionFridgeInputLineDesigner.add_instances_to_design"), so doing so may result in graphs that don’t display any data unless modified.

        Parameters:
        :   * **dds\_file\_name** (*Optional**[**str**]*) – The file name to use for the DDS file. If none is specified, the design’s cell name is used.
            * **dds\_dir** (*Optional**[**Path**]*) – The directory to use for the DDS file. If none is specified, the active workspace’s path is used.


---

<!-- === 来源: reference/quantum/hamiltonian_analysis.md === -->

# Hamiltonian Analysis[](#hamiltonian-analysis "Link to this heading")

## Qubit Classes[](#qubit-classes "Link to this heading")

### BaseQubit[](#basequbit "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubits.BaseQubit.BaseQubit[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit "Link to this definition")
:   *property* anharmonicity*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit.anharmonicity "Link to this definition")

    eigenvalues(*k: int = 5*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit.eigenvalues "Link to this definition")

    energy\_difference(*n1: int*, *n2: int*) → float[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit.energy_difference "Link to this definition")

    *property* hamiltonian*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit.hamiltonian "Link to this definition")

    *property* kinetic\_energy\_matrix*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit.kinetic_energy_matrix "Link to this definition")

    *property* potential\_energy\_matrix*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit.potential_energy_matrix "Link to this definition")

    *property* resonance\_frequency*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit.resonance_frequency "Link to this definition")

### Transmon[](#transmon "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubits.Transmon.Transmon[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Transmon.Transmon "Link to this definition")
:   Bases: [`BaseQubit`](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit")

    \_\_init\_\_(*EJ: float*, *EC: float*, *ng: float*, *n\_cutoff: int*)[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Transmon.Transmon.__init__ "Link to this definition")

    calculate\_energy\_level\_data(*x\_vals: ndarray*, *x\_variable: str = 'ng'*, *normalized: bool = False*, *normalization\_point: float = 0.5*, *progress\_worker: Worker | None = None*) → [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Transmon.Transmon.calculate_energy_level_data "Link to this definition")

    calculate\_wavefunction\_data(*x\_vals: ndarray*, *x\_variable: str = 'phase'*) → [WavefunctionData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Transmon.Transmon.calculate_wavefunction_data "Link to this definition")

    *property* kinetic\_energy\_matrix*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Transmon.Transmon.kinetic_energy_matrix "Link to this definition")

    potential(*phi: ndarray*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Transmon.Transmon.potential "Link to this definition")

    *property* potential\_energy\_matrix*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Transmon.Transmon.potential_energy_matrix "Link to this definition")

### TunableTransmon[](#tunabletransmon "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubits.TunableTransmon.TunableTransmon[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.TunableTransmon.TunableTransmon "Link to this definition")
:   Bases: [`BaseQubit`](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit")

    \_\_init\_\_(*EJ1: float*, *alpha: float*, *EC: float*, *ng: float*, *ext\_flux: float*, *n\_cutoff: int*)[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.TunableTransmon.TunableTransmon.__init__ "Link to this definition")

    calculate\_energy\_level\_data(*x\_vals: ndarray*, *x\_variable: str = 'Norm\_Ext\_Flux'*, *normalized: bool = False*, *normalization\_point: float = 0*, *progress\_worker: Worker | None = None*) → [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.TunableTransmon.TunableTransmon.calculate_energy_level_data "Link to this definition")

    calculate\_wavefunction\_data(*x\_vals: ndarray*, *x\_variable: str = 'phase'*) → [WavefunctionData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.TunableTransmon.TunableTransmon.calculate_wavefunction_data "Link to this definition")

    *property* kinetic\_energy\_matrix*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.TunableTransmon.TunableTransmon.kinetic_energy_matrix "Link to this definition")

    potential(*phi: ndarray*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.TunableTransmon.TunableTransmon.potential "Link to this definition")

    *property* potential\_energy\_matrix*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.TunableTransmon.TunableTransmon.potential_energy_matrix "Link to this definition")

### Fluxonium[](#fluxonium "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubits.Fluxonium.Fluxonium[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Fluxonium.Fluxonium "Link to this definition")
:   Bases: [`BaseQubit`](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit")

    \_\_init\_\_(*EJ: float*, *EC: float*, *EL: float*, *flux: float*, *n\_cutoff: int*)[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Fluxonium.Fluxonium.__init__ "Link to this definition")

    calculate\_energy\_level\_data(*x\_vals: ndarray*, *x\_variable: str = 'Norm\_Ext\_Flux'*, *normalized: bool = True*, *normalization\_point: float | None = None*, *progress\_worker: Worker | None = None*) → [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Fluxonium.Fluxonium.calculate_energy_level_data "Link to this definition")

    calculate\_wavefunction\_data(*x\_vals: ndarray*, *x\_variable: str = 'phase'*) → [WavefunctionData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Fluxonium.Fluxonium.calculate_wavefunction_data "Link to this definition")

    cosine\_phase\_operator(*alpha: float = 1*, *beta: float = 0*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Fluxonium.Fluxonium.cosine_phase_operator "Link to this definition")

    *property* hamiltonian*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Fluxonium.Fluxonium.hamiltonian "Link to this definition")

    *property* n\_operator*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Fluxonium.Fluxonium.n_operator "Link to this definition")

    *property* phase\_operator*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Fluxonium.Fluxonium.phase_operator "Link to this definition")

    potential(*phi: ndarray*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Fluxonium.Fluxonium.potential "Link to this definition")

### FluxQubit[](#fluxqubit "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubits.FluxQubit.FluxQubit[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.FluxQubit.FluxQubit "Link to this definition")
:   Bases: [`BaseQubit`](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit")

    \_\_init\_\_(*EJ1: float*, *alpha: float*, *gamma: float*, *ECjunction: float*, *ECalpha: float*, *ECgamma: float*, *ECshunt: float*, *ECgate1: float*, *ECgate2: float*, *ng1: float*, *ng2: float*, *ext\_flux: float*, *n\_cutoff: int*)[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.FluxQubit.FluxQubit.__init__ "Link to this definition")

    calculate\_energy\_level\_data(*x\_vals: ndarray*, *x\_variable: str = 'Norm\_Ext\_Flux'*, *normalized: bool = False*, *normalization\_point: float = 0.5*, *progress\_worker: Worker | None = None*) → [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.FluxQubit.FluxQubit.calculate_energy_level_data "Link to this definition")

    calculate\_wavefunction\_data(*phi1: ndarray*, *phi2: ndarray*, *x\_variable: str = 'phi1'*, *y\_variable: str = 'phi2'*) → [WavefunctionData2D](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.FluxQubit.FluxQubit.calculate_wavefunction_data "Link to this definition")

    *property* capacitance\_matrix*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.FluxQubit.FluxQubit.capacitance_matrix "Link to this definition")

    *property* charging\_energy\_matrix*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.FluxQubit.FluxQubit.charging_energy_matrix "Link to this definition")

    *property* kinetic\_energy\_matrix*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.FluxQubit.FluxQubit.kinetic_energy_matrix "Link to this definition")

    plot\_potential(*phi1\_vals: ndarray*, *phi2\_vals: ndarray*, *x\_variable: str = 'phi1'*, *y\_variable: str = 'phi2'*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.FluxQubit.FluxQubit.plot_potential "Link to this definition")

    potential(*phi1: ndarray*, *phi2: ndarray*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.FluxQubit.FluxQubit.potential "Link to this definition")

    *property* potential\_energy\_matrix*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.FluxQubit.FluxQubit.potential_energy_matrix "Link to this definition")

### ZeroPi[](#zeropi "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubits.ZeroPi.ZeroPi[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi "Link to this definition")
:   Bases: [`BaseQubit`](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit")

    \_\_init\_\_(*EJ: float*, *EL: float*, *ECJ: float*, *EC: float*, *dEJ: float*, *dECJ: float*, *ng: float*, *Norm\_Ext\_Flux: float*, *n\_cutoff: int*, *phi\_grid: ndarray*)[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.__init__ "Link to this definition")

    calculate\_energy\_level\_data(*x\_vals: ndarray*, *x\_variable: str = 'Norm\_Ext\_Flux'*, *normalized: bool = False*, *normalization\_point: float = 0.5*, *progress\_worker: Worker | None = None*) → [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.calculate_energy_level_data "Link to this definition")

    calculate\_wavefunction\_data(*phi: ndarray*, *theta: ndarray*, *x\_variable: str = 'phi'*, *y\_variable: str = 'theta'*) → [WavefunctionData2D](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.calculate_wavefunction_data "Link to this definition")

    cos\_phi\_operator(*phi: ndarray*, *added\_constant: float = 0*) → csc\_array[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.cos_phi_operator "Link to this definition")

    cos\_theta\_operator(*theta\_dim: int*) → csc\_array[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.cos_theta_operator "Link to this definition")

    eigenvalues(*k: int = 5*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.eigenvalues "Link to this definition")

    *property* hamiltonian*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.hamiltonian "Link to this definition")

    *property* kinetic\_energy\_matrix*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.kinetic_energy_matrix "Link to this definition")

    n\_theta\_operator(*n\_cutoff: int*) → csc\_array[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.n_theta_operator "Link to this definition")

    plot\_potential(*phi: ndarray*, *theta: ndarray*, *x\_variable: str = 'phi'*, *y\_variable: str = 'theta'*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.plot_potential "Link to this definition")

    potential(*phi: ndarray | float*, *theta: ndarray | float*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.potential "Link to this definition")

    *property* potential\_energy\_matrix*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.potential_energy_matrix "Link to this definition")

    sin\_phi\_operator(*phi: ndarray*, *added\_constant: float = 0*) → csc\_array[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.sin_phi_operator "Link to this definition")

    sin\_theta\_operator(*theta\_dim: int*) → csc\_array[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPi.ZeroPi.sin_theta_operator "Link to this definition")

### ZeroPiZeta[](#zeropizeta "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubits.ZeroPiZeta.ZeroPiZeta[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta "Link to this definition")
:   Bases: [`BaseQubit`](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit")

    *property* EC*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.EC "Link to this definition")

    *property* ECJ*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.ECJ "Link to this definition")

    *property* EJ*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.EJ "Link to this definition")

    *property* EL*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.EL "Link to this definition")

    *property* Norm\_Ext\_Flux*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.Norm_Ext_Flux "Link to this definition")

    \_\_init\_\_(*EJ: float*, *EL: float*, *ECJ: float*, *EC: float*, *dEJ: float*, *dECJ: float*, *dEL: float*, *dC: float*, *ng: float*, *Norm\_Ext\_Flux: float*, *n\_cutoff: int*, *phi\_grid: ndarray*, *zeta\_cutoff: int = 6*, *primary\_dim: int = 6*)[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.__init__ "Link to this definition")

    calculate\_energy\_level\_data(*x\_vals: ndarray*, *x\_variable: str = 'Norm\_Ext\_Flux'*, *normalized: bool = False*, *normalization\_point: float = 0.5*, *progress\_worker: Worker | None = None*) → [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.calculate_energy_level_data "Link to this definition")

    *property* dECJ*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.dECJ "Link to this definition")

    *property* dEJ*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.dEJ "Link to this definition")

    eigenvalues(*k: int = 5*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.eigenvalues "Link to this definition")

    g\_l\_l\_prime(*zeropi\_eigenvectors: ndarray | None = None*) → csc\_array[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.g_l_l_prime "Link to this definition")

    g\_phi(*zeropi\_eigenvectors: ndarray | None = None*) → csc\_array[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.g_phi "Link to this definition")

    g\_term(*zeropi\_eigenvectors: ndarray | None = None*) → csc\_matrix[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.g_term "Link to this definition")

    g\_theta(*zeropi\_eigenvectors: ndarray | None = None*) → csc\_array[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.g_theta "Link to this definition")

    *property* hamiltonian*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.hamiltonian "Link to this definition")

    *property* n\_cutoff*: int*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.n_cutoff "Link to this definition")

    *property* n\_theta\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.n_theta_operator "Link to this definition")

    *property* ng*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.ng "Link to this definition")

    *property* omega\_zeta*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.omega_zeta "Link to this definition")

    *property* phi\_grid*: ndarray*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.phi_grid "Link to this definition")

    *property* phi\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.phi_operator "Link to this definition")

    plot\_potential(*phi: ndarray | float | None = None*, *theta: ndarray | float | None = None*, *zeta: ndarray | float | None = None*, *x\_variable: str = 'phi'*, *y\_variable: str = 'theta'*) → Figure[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.plot_potential "Link to this definition")

    potential(*phi\_mesh: ndarray | float*, *theta\_mesh: ndarray | float*, *zeta\_mesh: ndarray | float*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.potential "Link to this definition")

    *property* primary\_term*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.ZeroPiZeta.ZeroPiZeta.primary_term "Link to this definition")

### Cos2Phi[](#cos2phi "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubits.Cos2Phi.Cos2Phi[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi "Link to this definition")
:   Bases: [`BaseQubit`](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.BaseQubit.BaseQubit")

    \_\_init\_\_(*EJ: float*, *ECJ: float*, *EL: float*, *EC: float*, *Norm\_Ext\_Flux: float*, *ng: float*, *n\_cutoff: int*, *phi\_cutoff: int*, *zeta\_cutoff: int*)[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.__init__ "Link to this definition")

    calculate\_energy\_level\_data(*x\_vals: ndarray*, *x\_variable: str = 'Norm\_Ext\_Flux'*, *normalized: bool = False*, *normalization\_point: float = 0.5*, *progress\_worker: Worker | None = None*) → [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.calculate_energy_level_data "Link to this definition")

    *property* cos\_phi\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.cos_phi_operator "Link to this definition")

    *property* cos\_phi\_operator\_full*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.cos_phi_operator_full "Link to this definition")

    *property* cos\_theta\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.cos_theta_operator "Link to this definition")

    *property* cos\_theta\_operator\_full*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.cos_theta_operator_full "Link to this definition")

    *property* e\_i\_phi\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.e_i_phi_operator "Link to this definition")

    eigenvalues(*k: int = 5*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.eigenvalues "Link to this definition")

    *property* full\_identity\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.full_identity_operator "Link to this definition")

    *property* hamiltonian*: csc\_matrix*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.hamiltonian "Link to this definition")

    *property* n\_phi\_full*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.n_phi_full "Link to this definition")

    *property* n\_phi\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.n_phi_operator "Link to this definition")

    *property* n\_theta\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.n_theta_operator "Link to this definition")

    *property* n\_theta\_operator\_full*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.n_theta_operator_full "Link to this definition")

    *property* n\_zeta\_full*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.n_zeta_full "Link to this definition")

    *property* n\_zeta\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.n_zeta_operator "Link to this definition")

    *property* phi\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.phi_operator "Link to this definition")

    *property* phi\_plasma\_frequency*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.phi_plasma_frequency "Link to this definition")

    *property* phi\_zpf*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.phi_zpf "Link to this definition")

    plot\_potential(*phi: ndarray | float | None = None*, *theta: ndarray | float | None = None*, *zeta: ndarray | float | None = None*, *x\_variable: str = 'phi'*, *y\_variable: str = 'theta'*) → Figure[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.plot_potential "Link to this definition")

    potential(*phi\_mesh: ndarray | float*, *zeta\_mesh: ndarray | float*, *theta\_mesh: ndarray | float*) → ndarray[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.potential "Link to this definition")

    *property* sin\_phi\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.sin_phi_operator "Link to this definition")

    *property* sin\_phi\_operator\_full*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.sin_phi_operator_full "Link to this definition")

    *property* sin\_theta\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.sin_theta_operator "Link to this definition")

    *property* sin\_theta\_operator\_full*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.sin_theta_operator_full "Link to this definition")

    *property* zeta\_operator*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.zeta_operator "Link to this definition")

    *property* zeta\_operator\_full*: csc\_array*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.zeta_operator_full "Link to this definition")

    *property* zeta\_plasma\_frequency*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.zeta_plasma_frequency "Link to this definition")

    *property* zeta\_zpf*: float*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubits.Cos2Phi.Cos2Phi.zeta_zpf "Link to this definition")

## Qubit Parameters[](#qubit-parameters "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubit\_parameters.Transmon\_Parameters[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Transmon_Parameters "Link to this definition")
:   \_\_init\_\_(*EJ: float*, *EC: float*, *ng: float*, *n\_cutoff: int*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Transmon_Parameters.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubit\_parameters.TunableTransmon\_Parameters[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.TunableTransmon_Parameters "Link to this definition")
:   \_\_init\_\_(*EJ1: float*, *alpha: float*, *EC: float*, *ng: float*, *ext\_flux: float*, *n\_cutoff: int*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.TunableTransmon_Parameters.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubit\_parameters.Fluxonium\_Parameters[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Fluxonium_Parameters "Link to this definition")
:   \_\_init\_\_(*EJ: float*, *EC: float*, *EL: float*, *ext\_flux: float*, *n\_cutoff: int*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Fluxonium_Parameters.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubit\_parameters.FluxQubit\_Parameters[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.FluxQubit_Parameters "Link to this definition")
:   \_\_init\_\_(*EJ1: float*, *alpha: float*, *gamma: float*, *ECjunction: float*, *ECalpha: float*, *ECgamma: float*, *ECshunt: float*, *ECgate1: float*, *ECgate2: float*, *ng1: float*, *ng2: float*, *ext\_flux: float*, *n\_cutoff: int*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.FluxQubit_Parameters.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubit\_parameters.ZeroPi\_Parameters[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPi_Parameters "Link to this definition")
:   \_\_init\_\_(*EJ: float*, *EL: float*, *ECJ: float*, *EC: float*, *dEJ: float*, *dECJ: float*, *ng: float*, *Norm\_Ext\_Flux: float*, *n\_cutoff: int*, *phi\_grid: ndarray*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPi_Parameters.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubit\_parameters.ZeroPiZeta\_Parameters[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPiZeta_Parameters "Link to this definition")
:   \_\_init\_\_(*EJ: float*, *EL: float*, *ECJ: float*, *EC: float*, *dEJ: float*, *dECJ: float*, *dEL: float*, *dC: float*, *Norm\_Ext\_Flux: float*, *ng: float*, *n\_cutoff: int*, *phi\_grid: ndarray*, *zeta\_cutoff: int*, *zeropi\_dim: int = 10*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPiZeta_Parameters.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.qubit\_parameters.Cos2Phi\_Parameters[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Cos2Phi_Parameters "Link to this definition")
:   \_\_init\_\_(*EJ: float*, *ECJ: float*, *EL: float*, *EC: float*, *Norm\_Ext\_Flux: float*, *ng: float*, *n\_cutoff: int*, *phi\_cutoff: float*, *zeta\_cutoff: int*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Cos2Phi_Parameters.__init__ "Link to this definition")

## Schematic Reading Functions[](#schematic-reading-functions "Link to this heading")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.hamiltonian\_analysis\_circuit.read\_schematic\_for\_preset\_qubits(*schematic: Design*) → [Transmon\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Transmon_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Transmon_Parameters") | [TunableTransmon\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.TunableTransmon_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.TunableTransmon_Parameters") | [FluxQubit\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.FluxQubit_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.FluxQubit_Parameters") | [Fluxonium\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Fluxonium_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Fluxonium_Parameters") | [ZeroPi\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPi_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPi_Parameters") | [ZeroPiZeta\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPiZeta_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPiZeta_Parameters") | [Cos2Phi\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Cos2Phi_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Cos2Phi_Parameters") | None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.hamiltonian_analysis_circuit.read_schematic_for_preset_qubits "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.hamiltonian\_analysis\_circuit.read\_transmon\_instance(*design: Design*, *instance: Instance*) → [Transmon\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Transmon_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Transmon_Parameters")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.hamiltonian_analysis_circuit.read_transmon_instance "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.hamiltonian\_analysis\_circuit.read\_tunable\_transmon\_instance(*design: Design*, *instance: Instance*) → [TunableTransmon\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.TunableTransmon_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.TunableTransmon_Parameters")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.hamiltonian_analysis_circuit.read_tunable_transmon_instance "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.hamiltonian\_analysis\_circuit.read\_flux\_qubit\_instance(*design: Design*, *instance: Instance*) → [FluxQubit\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.FluxQubit_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.FluxQubit_Parameters")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.hamiltonian_analysis_circuit.read_flux_qubit_instance "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.hamiltonian\_analysis\_circuit.read\_fluxonium\_instance(*design: Design*, *instance: Instance*) → [Fluxonium\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Fluxonium_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Fluxonium_Parameters")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.hamiltonian_analysis_circuit.read_fluxonium_instance "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.hamiltonian\_analysis\_circuit.read\_zeropi\_instance(*design: Design*, *instance: Instance*) → [ZeroPi\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPi_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPi_Parameters")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.hamiltonian_analysis_circuit.read_zeropi_instance "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.hamiltonian\_analysis\_circuit.read\_zeropizeta\_instance(*design: Design*, *instance: Instance*) → [ZeroPiZeta\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPiZeta_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPiZeta_Parameters")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.hamiltonian_analysis_circuit.read_zeropizeta_instance "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.hamiltonian\_analysis\_circuit.read\_cos2phi\_instance(*design: Design*, *instance: Instance*) → [Cos2Phi\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Cos2Phi_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Cos2Phi_Parameters")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.hamiltonian_analysis_circuit.read_cos2phi_instance "Link to this definition")

## Plotting Functions[](#plotting-functions "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.WavefunctionOutput[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.WavefunctionOutput "Link to this definition")
:   AbsSquared *= 'Abs Squared'*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.WavefunctionOutput.AbsSquared "Link to this definition")

    Imag *= 'Imag'*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.WavefunctionOutput.Imag "Link to this definition")

    Real *= 'Real'*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.WavefunctionOutput.Real "Link to this definition")

    \_\_new\_\_(*value*)[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.WavefunctionOutput.__new__ "Link to this definition")

### Energy Level Plotting[](#energy-level-plotting "Link to this heading")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_energy\_level(*energy\_level\_data: [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData")*, *level: int*, *color: str = ''*, *axis: Axes | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_energy_level "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_energy\_levels(*energy\_level\_data: [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData")*, *levels: list[int]*, *axis: Axes | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_energy_levels "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_energy\_levels\_analysis(*energy\_level\_data: [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData")*, *levels: list[int]*, *x\_min: float | None = None*, *x\_max: float | None = None*, *y\_min: float | None = None*, *y\_max: float | None = None*, *axis: Axes | None = None*) → Figure | None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_energy_levels_analysis "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_first\_two\_transition\_frequencies(*energy\_level\_data: [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData")*, *x\_min: float | None = None*, *x\_max: float | None = None*, *y\_min: float | None = None*, *y\_max: float | None = None*, *axis: Axes | None = None*) → Figure | None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_first_two_transition_frequencies "Link to this definition")

### 1D Plotting Functions (Wavefunctions and Potential)[](#d-plotting-functions-wavefunctions-and-potential "Link to this heading")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_wavefunction(*wavefunction\_data: [WavefunctionData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData")*, *level: int*, *wavefunction\_mode: str*, *color\_hex: str*, *wavefunction\_amplitude\_scaling: float = 3*, *axis: Axes | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_wavefunction "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_wavefunctions(*wavefunction\_data: [WavefunctionData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData")*, *levels: list[int]*, *wavefunction\_mode: str*, *wavefunction\_amplitude\_scaling: float = 3*, *axis: Axes | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_wavefunctions "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_wavefunction\_analysis(*wavefunction\_data: [WavefunctionData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData")*, *levels: list[int]*, *wavefunction\_output: str*, *wavefunction\_amplitude\_scaling: float = 1*, *x\_min: float | None = None*, *x\_max: float | None = None*, *y\_min: float | None = None*, *y\_max: float | None = None*, *axis: Axes | None = None*) → Figure | None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_wavefunction_analysis "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_potential(*wavefunction\_data: [WavefunctionData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData")*, *axis: Axes | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_potential "Link to this definition")

### 2D Plotting Functions (Wavefunctions and Potential)[](#id1 "Link to this heading")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_2d\_potential(*wavefunction\_data: [WavefunctionData2D](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D") | [WavefunctionData2DSlice](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2DSlice "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2DSlice")*, *axis: Axes | None = None*) → QuadContourSet | None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_2d_potential "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_potential\_analysis(*wavefunction\_data: [WavefunctionData2D](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D") | [WavefunctionData2DSlice](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2DSlice "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2DSlice")*, *x\_min: float | None = None*, *x\_max: float | None = None*, *y\_min: float | None = None*, *y\_max: float | None = None*, *axis: Axes | None = None*) → Figure | None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_potential_analysis "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_2d\_wavefunction(*wavefunction\_data: [WavefunctionData2D](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D")*, *level: int*, *wavefunction\_output: str*, *wavefunction\_amplitude\_scaling: float = 1*, *axis: Axes | None = None*) → AxesImage | None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_2d_wavefunction "Link to this definition")

quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.plot.plot\_2d\_wavefunction\_analysis(*wavefunction\_data: [WavefunctionData2D](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D")*, *level: int*, *wavefunction\_output: str*, *wave\_amplitude\_scaling: float = 3*, *x\_min: float | None = None*, *x\_max: float | None = None*, *y\_min: float | None = None*, *y\_max: float | None = None*, *axis: Axes | None = None*) → Figure | None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.plot.plot_2d_wavefunction_analysis "Link to this definition")

## Data Structures[](#data-structures "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.data\_structures.EnergyLevelData[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "Link to this definition")
:   \_\_init\_\_(*x\_variable: str*, *x\_vals: ndarray*, *energy\_levels: list[list[float]]*, *is\_normalized: bool*, *dataset\_path: str = ''*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.data\_structures.WavefunctionData[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData "Link to this definition")
:   \_\_init\_\_(*dependent\_variable: str*, *x\_vals: ndarray*, *potential: ndarray*, *wavefunctions: list*, *eigenvalues: ndarray*, *dataset\_path: str = ''*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.data\_structures.WavefunctionData2D[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D "Link to this definition")
:   \_\_init\_\_(*x\_variable: str*, *x\_vals: ndarray*, *y\_variable: str*, *y\_vals: ndarray*, *potential: ndarray*, *wavefunctions: list*, *eigenvalues: list*, *dataset\_path: str = ''*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.data\_structures.WavefunctionData2DSlice[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2DSlice "Link to this definition")
:   \_\_init\_\_(*x\_variable: str*, *x\_vals: ndarray*, *y\_variable: str*, *y\_vals: ndarray*, *z\_variable: str*, *z\_val: float*, *potential: ndarray*, *wavefunctions: list*, *eigenvalues: list*, *dataset\_path: str = ''*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2DSlice.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.data\_structures.HamiltonianAnalysisData[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.HamiltonianAnalysisData "Link to this definition")
:   \_\_init\_\_(*energy\_level\_data: [EnergyLevelData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.EnergyLevelData") | None*, *wavefunction\_data: [WavefunctionData](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData") | [WavefunctionData2D](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2D") | [WavefunctionData2DSlice](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2DSlice "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.WavefunctionData2DSlice") | None*, *circuit\_parameters: [Transmon\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Transmon_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Transmon_Parameters") | [TunableTransmon\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.TunableTransmon_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.TunableTransmon_Parameters") | [FluxQubit\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.FluxQubit_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.FluxQubit_Parameters") | [Fluxonium\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Fluxonium_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.Fluxonium_Parameters") | [ZeroPi\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPi_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPi_Parameters") | [ZeroPiZeta\_Parameters](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPiZeta_Parameters "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.qubit_parameters.ZeroPiZeta_Parameters") | None = None*, *symbolic\_hamiltonian: str | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.data_structures.HamiltonianAnalysisData.__init__ "Link to this definition")

## Calculation Argument Data Structures[](#calculation-argument-data-structures "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.calculation\_args.EnergyLevelCalculationArgs[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.EnergyLevelCalculationArgs "Link to this definition")
:   \_\_init\_\_(*x\_variable: str*, *x\_val\_min: float*, *x\_val\_max: float*, *num\_of\_x\_values: int*, *normalized: bool*, *normalization\_point: float*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.EnergyLevelCalculationArgs.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.calculation\_args.WavefunctionCalculationArgs[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.WavefunctionCalculationArgs "Link to this definition")
:   \_\_init\_\_(*x\_variable: str*, *x\_val\_min: float*, *x\_val\_max: float*, *num\_of\_x\_values: int*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.WavefunctionCalculationArgs.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.calculation\_args.Wavefunction2DCalculationArgs[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.Wavefunction2DCalculationArgs "Link to this definition")
:   Bases: [`WavefunctionCalculationArgs`](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.WavefunctionCalculationArgs "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.WavefunctionCalculationArgs")

    \_\_init\_\_(*x\_variable: str*, *x\_val\_min: float*, *x\_val\_max: float*, *num\_of\_x\_values: int*, *y\_variable: str*, *y\_val\_min: float*, *y\_val\_max: float*, *num\_of\_y\_values: int*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.Wavefunction2DCalculationArgs.__init__ "Link to this definition")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.hamiltonian\_analysis.calculation\_args.Wavefunction2DSliceCalculationArgs[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.Wavefunction2DSliceCalculationArgs "Link to this definition")
:   Bases: [`Wavefunction2DCalculationArgs`](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.Wavefunction2DCalculationArgs "quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.Wavefunction2DCalculationArgs")

    \_\_init\_\_(*x\_variable: str*, *x\_val\_min: float*, *x\_val\_max: float*, *num\_of\_x\_values: int*, *y\_variable: str*, *y\_val\_min: float*, *y\_val\_max: float*, *num\_of\_y\_values: int*, *z\_variable: str*, *z\_val: float*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.hamiltonian_analysis.calculation_args.Wavefunction2DSliceCalculationArgs.__init__ "Link to this definition")


---

<!-- === 来源: reference/quantum/index.md === -->

# Quantum Addon[](#module-quantum_addon.src.keysight.ads.quantum_analysis.python "Link to this heading")

## Classes[](#classes "Link to this heading")

* [Hamiltonian Analysis](hamiltonian_analysis.md)
* [Parameter Extraction](parameter_extraction.md)
* [SQUID Extrema Analysis](squid_extrema_analysis.md)
* [Dilution Fridge Input Line Designer](dilution_fridge_input_line_designer.md)
* [Time Dynamics Analysis](time_dynamics_analysis.md)


---

<!-- === 来源: reference/quantum/parameter_extraction.md === -->

# Parameter Extraction[](#parameter-extraction "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.parameter\_extraction.parameter\_extraction\_data.CircuitQuantumParameters[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters "Link to this definition")
:   \_\_init\_\_(*config: ExtractionConfig | None = None*)[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.__init__ "Link to this definition")

    get\_dataset\_dir(*workspace\_dir: str = ''*) → str[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_dataset_dir "Link to this definition")
    :   Get the directory that the dataset file is stored under.

    get\_default\_dataset\_filename() → str[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_default_dataset_filename "Link to this definition")
    :   Get the default dataset filename that is used.

    get\_num\_qubits() → int[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_num_qubits "Link to this definition")
    :   Get the number of successfully extracted qubits.

    get\_num\_resonators() → int[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_num_resonators "Link to this definition")
    :   Get the number of successfully extracted resonators.

    get\_qubit\_by\_term(*term: int*) → [QubitData](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData "quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.data_models.QubitData")[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_qubit_by_term "Link to this definition")

    get\_summary() → str[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_summary "Link to this definition")
    :   Get a single-string summary of the extracted quantum parameters.

    get\_table\_column\_headers() → list[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_table_column_headers "Link to this definition")
    :   Get column headers that can be used for a table.

    get\_table\_data(*parameter\_type: ParameterType*, *raw\_data: bool = False*) → list[list][](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_table_data "Link to this definition")
    :   Get data (2D array / list of lists) that can be used in a table. Best used in conjunction with [`get_table_column_headers()`](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_table_column_headers "quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_table_column_headers") and [`get_table_row_headers()`](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_table_row_headers "quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_table_row_headers").

        Parameters:
        :   * **parameter\_type** (*ParameterType*) –

              The type of parameter to extract data for. Options are:
              :   + CHI
                  + RABI
                  + QUBIT\_TO\_QUBIT\_COUPLING
            * **raw\_data** (*bool*) – If True, return raw data values (floats) without any scaling or formatting.
              If False (the default), return formatted and rounded strings, paired with appropriate units.

    get\_table\_row\_headers() → list[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.get_table_row_headers "Link to this definition")
    :   Get row headers that can be used for a table.

    open\_dataset\_and\_extract\_data(*design\_lcv\_name: str*, *s\_param\_controller\_name: str*, *dataset\_path: str | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.open_dataset_and_extract_data "Link to this definition")
    :   Perform parameter extraction. Stores the data in the class.

        If no dataset exists, you must run [`run_simulation()`](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.run_simulation "quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.run_simulation") - passing in the desired design\_lcv\_name - prior to calling this method.

        Parameters:
        :   * **design\_lcv\_name** (*str*) – The design LCV (library:cell:view) name.
            * **s\_param\_controller\_name** (*str*) – The S-parameter controller name to use when viewing the dataset.
            * **dataset\_path** (*str*) – An optional path to the dataset file.

    run\_simulation(*design\_lcv\_name: str*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.run_simulation "Link to this definition")
    :   Run a circuit simulation off the schematic design specified by design\_lcv\_name.

        Parameters:
        :   **design\_lcv\_name** (*str*) – The LCV (library:cell:view) name of the design to simulate.

    set\_dataset\_path(*path: str | Path*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.CircuitQuantumParameters.set_dataset_path "Link to this definition")
    :   Set the path of the dataset to the one specified. An appropriate default is used if this method is never called.

        Parameters:
        :   **path** (*str* *|* *Path*) – The path to the dataset file.

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.parameter\_extraction.parameter\_extraction\_data.QubitData[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData "Link to this definition")
:   QubitData(instance\_name: str = ‘’, term: int = 0, inductance: float = 0.0, capacitance: float = 0.0, frequency: float = 0.0, crossing\_index: int = 0, anharmonicity: float = 0.0, q\_factor: float = 0.0, t1: float = 0.0)

    \_\_init\_\_(*instance\_name: str = ''*, *term: int = 0*, *inductance: float = 0.0*, *capacitance: float = 0.0*, *frequency: float = 0.0*, *crossing\_index: int = 0*, *anharmonicity: float = 0.0*, *q\_factor: float = 0.0*, *t1: float = 0.0*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData.__init__ "Link to this definition")

    anharmonicity*: float* *= 0.0*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData.anharmonicity "Link to this definition")

    capacitance*: float* *= 0.0*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData.capacitance "Link to this definition")

    crossing\_index*: int* *= 0*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData.crossing_index "Link to this definition")

    frequency*: float* *= 0.0*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData.frequency "Link to this definition")

    inductance*: float* *= 0.0*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData.inductance "Link to this definition")

    instance\_name*: str* *= ''*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData.instance_name "Link to this definition")

    q\_factor*: float* *= 0.0*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData.q_factor "Link to this definition")

    t1*: float* *= 0.0*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData.t1 "Link to this definition")

    term*: int* *= 0*[](#quantum_addon.src.keysight.ads.quantum_analysis.python.parameter_extraction.parameter_extraction_data.QubitData.term "Link to this definition")


---

<!-- === 来源: reference/quantum/squid_extrema_analysis.md === -->

# SQUID Extrema Analysis[](#squid-extrema-analysis "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.squid\_analysis.squid\_extrema\_analysis.SQUIDExtremaAnalysis[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaAnalysis "Link to this definition")
:   \_\_init\_\_(*design: Design*, *\_parent\_dialog: SQUIDExtremaDialog | None = None*, *\_progress\_worker: Worker | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaAnalysis.__init__ "Link to this definition")
    :   Initialize the SQUID Extrema Analysis.

        Parameters:
        :   **design** (*db.Design*) – The closed-loop SQUID schematic design to be used to initialize the SQUID Extrema Analysis.

        Example

        ```
        # Access ADS schematic design
        from keysight.ads.de import db_uu as db

        library_cell_view = ("SQUID_lib", "SQUID", "schematic")  # specify library, cell, and view
        design = db.open_design(library_cell_view, mode=db.DesignMode.APPEND)

        # Access Quantum Tool Suite
        quantum_addon = app.import_addon_as_module("Quantum Tools")

        # Access Analysis Class
        from quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis import SQUIDExtremaAnalysis

        # Initialize Analysis
        analysis = SQUIDExtremaAnalysis(design)

        # Run Analysis
        analysis.run()

        # Extract Results
        analysis.extract_results()
        ```

    clear\_plots() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaAnalysis.clear_plots "Link to this definition")
    :   Clear and close all plots that have been generated and displayed via the python console.

    extract\_results() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaAnalysis.extract_results "Link to this definition")
    :   Extract results from the SQUID Extrema Analysis.

        The dataset file must be available from a prior simulation run.
        The plots to view the results will be generated and displayed.

    plot\_effective\_inductance() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaAnalysis.plot_effective_inductance "Link to this definition")
    :   Plot the effective inductance at extrema versus the normalized external flux.

    plot\_flux() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaAnalysis.plot_flux "Link to this definition")
    :   Plot the open-loop normalized flux versus the smallest junction Vphi.

    plot\_loop\_current\_at\_extrema() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaAnalysis.plot_loop_current_at_extrema "Link to this definition")
    :   Plot the loop current at extrema versus the normalized external flux.

    plot\_norm\_potential\_energy() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaAnalysis.plot_norm_potential_energy "Link to this definition")
    :   Plot the normalized potential energy at extrema versus the normalized external flux.

    plot\_smallest\_junction\_voltage\_at\_extrema() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaAnalysis.plot_smallest_junction_voltage_at_extrema "Link to this definition")
    :   Plot the smallest junction voltage (Vphi) at extrema versus the normalized external flux.

    run() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaAnalysis.run "Link to this definition")
    :   Execute the SQUID Extrema Analysis.

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.squid\_analysis.squid\_extrema\_analysis.SQUIDExtremaSetup[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaSetup "Link to this definition")
:   \_\_init\_\_(*design: Design*, *overwrite: bool = False*, *\_parent\_dialog: SQUIDExtremaDialog | None = None*, *\_progress\_worker: Worker | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis.SQUIDExtremaSetup.__init__ "Link to this definition")
    :   Generate the schematic setup that will be used to execute the SQUID Extrema Analysis.

        Parameters:
        :   * **design** (*db.Design*) – The closed-loop SQUID schematic design that is being used to set up the SQUID Extrema Analysis.
            * **overwrite** (*bool**,* *optional*) – Whether to force the overwrite of an existing setup schematic if it already exists.

        Example

        ```
        # Access ADS schematic design
        from keysight.ads.de import db_uu as db

        library_cell_view = ("SQUID_lib", "SQUID", "schematic")  # specify library, cell, and view
        design = db.open_design(library_cell_view, mode=db.DesignMode.APPEND)

        # Access Quantum Tool Suite
        quantum_addon = app.import_addon_as_module("Quantum Tools")

        # Access Setup Class
        from quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_extrema_analysis import SQUIDExtremaSetup

        # Generate Extrema Analysis Setup
        SQUIDExtremaSetup(design=design)
        ```

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.squid\_analysis.squid\_transient\_analysis.SQUIDTransientAnalysis[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_transient_analysis.SQUIDTransientAnalysis "Link to this definition")
:   \_\_init\_\_(*design: Design*, *\_parent\_dialog: SQUIDExtremaDialog | None = None*, *\_progress\_worker: Worker | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_transient_analysis.SQUIDTransientAnalysis.__init__ "Link to this definition")
    :   Initialize the SQUID Transient Analysis.

        Parameters:
        :   **design** (*db.Design*) – The closed-loop SQUID schematic design to be used to initialize the SQUID Transient Analysis.

        Example

        ```
        # Access ADS schematic design
        from keysight.ads.de import db_uu as db

        library_cell_view = ("SQUID_lib", "SQUID", "schematic")  # specify library, cell, and view
        design = db.open_design(library_cell_view, mode=db.DesignMode.APPEND)

        # Access Quantum Tool Suite
        quantum_addon = app.import_addon_as_module("Quantum Tools")

        # Access Analysis Class
        from quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_transient_analysis import SQUIDTransientAnalysis

        # Initialize Analysis
        analysis = SQUIDTransientAnalysis(design)

        # Run Analysis
        analysis.run()

        # Extract Results
        analysis.extract_results()
        ```

    clear\_plots() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_transient_analysis.SQUIDTransientAnalysis.clear_plots "Link to this definition")
    :   Clear and close all plots that have been generated and displayed via the python console.

    extract\_results() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_transient_analysis.SQUIDTransientAnalysis.extract_results "Link to this definition")
    :   Extract results from the SQUID Transient Analysis.

        The dataset file must be available from a prior simulation run.
        The plots to view the results will be generated and displayed.

    plot\_transient\_vphi() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_transient_analysis.SQUIDTransientAnalysis.plot_transient_vphi "Link to this definition")
    :   Plot the transient voltage (Vphi) output versus the normalized external flux.

    run() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_transient_analysis.SQUIDTransientAnalysis.run "Link to this definition")
    :   Execute the SQUID Transient Analysis.

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.squid\_analysis.squid\_transient\_analysis.SQUIDTransientSetup[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_transient_analysis.SQUIDTransientSetup "Link to this definition")
:   \_\_init\_\_(*design: Design*, *overwrite: bool = False*, *\_parent\_dialog: SQUIDExtremaDialog | None = None*, *\_progress\_worker: Worker | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_transient_analysis.SQUIDTransientSetup.__init__ "Link to this definition")
    :   Generate the schematic setup that will be used to execute the SQUID Transient Analysis.

        Parameters:
        :   * **design** (*db.Design*) – The closed-loop SQUID schematic design that is being used to set up the SQUID Transient Analysis.
            * **overwrite** (*bool**,* *optional*) – Whether to force the overwrite of an existing setup schematic if it already exists.

        Example

        ```
        # Access ADS schematic design
        from keysight.ads.de import db_uu as db

        library_cell_view = ("SQUID_lib", "SQUID", "schematic")  # specify library, cell, and view
        design = db.open_design(library_cell_view, mode=db.DesignMode.APPEND)

        # Access Quantum Tool Suite
        quantum_addon = app.import_addon_as_module("Quantum Tools")

        # Access Setup Class
        from quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_transient_analysis import SQUIDTransientSetup

        # Generate Transient Analysis Setup
        SQUIDTransientSetup(design=design)
        ```

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.squid\_analysis.squid\_dc\_analysis.SQUIDDCAnalysis[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_dc_analysis.SQUIDDCAnalysis "Link to this definition")
:   \_\_init\_\_(*design: Design*, *\_parent\_dialog: SQUIDExtremaDialog | None = None*, *\_progress\_worker: Worker | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_dc_analysis.SQUIDDCAnalysis.__init__ "Link to this definition")
    :   Initialize the SQUID DC Analysis.

        Parameters:
        :   **design** (*db.Design*) – The closed-loop SQUID schematic design to be used to initialize the SQUID DC Analysis.

        Example

        ```
        # Access ADS schematic design
        from keysight.ads.de import db_uu as db

        library_cell_view = ("SQUID_lib", "SQUID", "schematic")  # specify library, cell, and view
        design = db.open_design(library_cell_view, mode=db.DesignMode.APPEND)

        # Access Quantum Tool Suite
        quantum_addon = app.import_addon_as_module("Quantum Tools")

        # Access Analysis Class
        from quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_dc_analysis import SQUIDDCAnalysis

        # Initialize Analysis
        analysis = SQUIDDCAnalysis(design)

        # Run Analysis
        analysis.run()

        # Extract Results
        analysis.extract_results()
        ```

    clear\_plots() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_dc_analysis.SQUIDDCAnalysis.clear_plots "Link to this definition")
    :   Clear and close all plots that have been generated and displayed via the python console.

    extract\_results(*fluxoid\_offset: float | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_dc_analysis.SQUIDDCAnalysis.extract_results "Link to this definition")
    :   Extract results from the SQUID DC Analysis.

        The dataset file must be available from a prior simulation run.
        The plots to view the results will be generated and displayed.

        Parameters:
        :   **fluxoid\_offset** (*float* *|* *None**,* *optional*) – The fluxoid offset value obtained from the corresponding SQUID Transient Analysis.
            If provided, the ‘Vphi’ values will be shifted accordingly.

    plot\_dc\_vphi() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_dc_analysis.SQUIDDCAnalysis.plot_dc_vphi "Link to this definition")
    :   Plot the DC voltage (Vphi) output versus the normalized external flux.

    run() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_dc_analysis.SQUIDDCAnalysis.run "Link to this definition")
    :   Execute the SQUID DC Analysis.

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.squid\_analysis.squid\_dc\_analysis.SQUIDDCSetup[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_dc_analysis.SQUIDDCSetup "Link to this definition")
:   \_\_init\_\_(*design: Design*, *overwrite: bool = False*, *\_parent\_dialog: SQUIDExtremaDialog | None = None*, *\_progress\_worker: Worker | None = None*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_dc_analysis.SQUIDDCSetup.__init__ "Link to this definition")
    :   Generate the schematic setup that will be used to execute the SQUID DC Analysis.

        Parameters:
        :   * **design** (*db.Design*) – The closed-loop SQUID schematic design that is being used to set up the SQUID DC Analysis.
            * **overwrite** (*bool**,* *optional*) – Whether to force the overwrite of an existing setup schematic if it already exists.

        Example

        ```
        # Access ADS schematic design
        from keysight.ads.de import db_uu as db

        library_cell_view = ("SQUID_lib", "SQUID", "schematic")  # specify library, cell, and view
        design = db.open_design(library_cell_view, mode=db.DesignMode.APPEND)

        # Access Quantum Tool Suite
        quantum_addon = app.import_addon_as_module("Quantum Tools")

        # Access Setup Class
        from quantum_addon.src.keysight.ads.quantum_analysis.python.squid_analysis.squid_dc_analysis import SQUIDDCSetup

        # Generate DC Analysis Setup
        SQUIDDCSetup(design=design)
        ```


---

<!-- === 来源: reference/quantum/time_dynamics_analysis.md === -->

# Time Dynamics Analysis[](#time-dynamics-analysis "Link to this heading")

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.time\_dynamics\_analysis.experiments.gaussian\_pulse.GaussianPulseExperiment[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse.GaussianPulseExperiment "Link to this definition")
:   \_\_init\_\_(*cross\_kerr: float = 2*, *qubit\_anharmonicity: float = 300*, *qubit\_frequency: float = 6*, *qubit\_lifetime: float = 30*, *qubit\_dephasing\_time: float = 5*, *qubit\_drive\_strength: float = 1000000000.0*, *qubit\_dimension: int = 3*, *resonator\_frequency: float = 8*, *resonator\_lifetime: float = 30*, *resonator\_dimension: int = 2*, *pulse\_amplitude: float = 0.125*, *pulse\_duration: float = 30*, *pulse\_phase: float = 0*, *drive\_detuning: float = 0*, *drag\_coefficient: float = 0*, *total\_time: float = 60*, *time\_steps: float = 300*, *initial\_state: str = 'ground'*, *target\_unitary: list = [[0, 1], [1, 0]]*, *qubit\_temperature: float = 50*, *include\_qubit\_decay: bool = True*, *include\_qubit\_dephasing: bool = True*, *include\_qubit\_bath: bool = False*, *resonator\_temperature: float = 50*, *include\_resonator\_decay: bool = False*, *include\_resonator\_bath: bool = False*, *include\_purcell\_effect: bool = False*, *include\_dressed\_dephasing: bool = False*, *n\_steps: float = 100000000.0*, *r\_tolerance: float = 1e-12*, *a\_tolerance: float = 1e-12*, *max\_step: float = 1*, *\_dialog: TimeDynamicsDialog | None = None*, *\*\*kwargs*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse.GaussianPulseExperiment.__init__ "Link to this definition")
    :   Initialize a Gaussian Pulse experiment.

        Parameters:
        :   * **cross\_kerr** (*float*) – Cross kerr coupling in MHz.
            * **qubit\_anharmonicity** (*float*) – Qubit anharmonicity in MHz.
            * **qubit\_frequency** (*float*) – Qubit frequency in GHz.
            * **qubit\_lifetime** (*float*) – Qubit lifetime in microseconds.
            * **qubit\_dephasing\_time** (*float*) – Qubit dephasing time in microseconds.
            * **qubit\_drive\_strength** (*float*) – Qubit drive strength scaling factor.
            * **qubit\_dimension** (*int*) – Number of qubit energy levels to include.
            * **resonator\_frequency** (*float*) – Resonator frequency in GHz.
            * **resonator\_lifetime** (*float*) – Resonator lifetime in microseconds.
            * **resonator\_dimension** (*int*) – Number of resonator energy levels to include.
            * **pulse\_amplitude** (*float*) – The drive strength of the Gaussian pulse in GHz.
            * **pulse\_duration** (*float*) – The duration of the Gaussian pulse in ns, measured as six standard deviations.
            * **pulse\_phase** (*float*) – The quadrature phase of the complex pulse in degrees.
            * **drive\_detuning** (*float*) – The detuning of the drive away from the qubit resonance in kHz.
            * **drag\_coefficient** (*float*) – The scaling factor of the Gaussian derivative component in the DRAG pulse scheme.
            * **total\_time** (*float*) – Total simulation time in ns.
            * **time\_steps** (*float*) – The number of intermediate states to evaluate the expectated values.
            * **initial\_state** (*str*) – Initial state of the system (“ground” or “steady”).
            * **target\_unitary** (*list*) – An optional qubit target unitary used to compute the process fidelity.
            * **qubit\_temperature** (*float*) – The temperature of the bath, in mK, that the qubit is coupled to.
            * **include\_qubit\_decay** (*bool*) – Whether to include energy relaxation due to photon loss in the qubit.
            * **include\_qubit\_dephasing** (*bool*) – Whether to include qubit dephasing.
            * **include\_qubit\_bath** (*bool*) – Whether to couple the qubit to a thermal bath in the simulation.
            * **resonator\_temperature** (*float*) – The temperature of the bath, in mK, that the resonator is coupled to.
            * **include\_resonator\_decay** (*bool*) – Whether to include energy relaxation due to photon loss in the resonator.
            * **include\_resonator\_bath** (*bool*) – Whether to couple the resonator to a thermal bath in the simulation.
            * **include\_purcell\_effect** (*bool*) – Whether to include dissipation due to the Purcell effect.
            * **include\_dressed\_dephasing** (*bool*) – Whether to include dissipation due to the dressed-dephasing effect.
            * **n\_steps** (*float*) – Sets the the maximum number of steps the solver will take per each interval of integration.
            * **r\_tolerance** (*float*) – Relative Tolerance - Sets a threshold for acceptable magnitudes of error as a proportion of the magnitude of the solution.
            * **a\_tolerance** (*float*) – Absolute Tolerance - Sets a fixed threshold for acceptable magnitudes of error.
            * **max\_step** (*float*) – Sets the maximum step size in ns. For accurate simulation, this number must be smaller then half the width of the shortest pulse in the simulation.
            * **\*\*kwargs** (*dict*) – Collect additional keyword arguments.

        Example

        ```
        # Access Quantum Tool Suite
        quantum_addon = app.import_addon_as_module("Quantum Tools")

        # Access Experiment Class
        from quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse import GaussianPulseExperiment

        # Simulate Experiment
        experiment = GaussianPulseExperiment()  # default parameters
        experiment = GaussianPulseExperiment(
                            cross_kerr=2.0,
                            qubit_frequency=8.0,
                            qubit_lifetime=30.0,
                            resonator_frequency=6.0,
                            resonator_lifetime=30.0) # custom parameters
        experiment.run_simulation()
        ```

    calculate\_fidelity() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse.GaussianPulseExperiment.calculate_fidelity "Link to this definition")
    :   Calculate and display the qubit fidelity.

    calculate\_leakage() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse.GaussianPulseExperiment.calculate_leakage "Link to this definition")
    :   Calculate and display the leakage.

    clear\_plots() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse.GaussianPulseExperiment.clear_plots "Link to this definition")
    :   Clear and close all plots that have been generated and displayed via the python console.

    plot\_bloch\_sphere() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse.GaussianPulseExperiment.plot_bloch_sphere "Link to this definition")
    :   Generate the bloch sphere visualization.

    plot\_leakage() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse.GaussianPulseExperiment.plot_leakage "Link to this definition")
    :   Generate the leakage visualization.

    plot\_polarization() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse.GaussianPulseExperiment.plot_polarization "Link to this definition")
    :   Generate the polarization plot.

    plot\_pulse\_visualization() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse.GaussianPulseExperiment.plot_pulse_visualization "Link to this definition")
    :   Generate the pulse visualization plot.

    plot\_results() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse.GaussianPulseExperiment.plot_results "Link to this definition")
    :   Plot all simulation results.

    run\_simulation() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.gaussian_pulse.GaussianPulseExperiment.run_simulation "Link to this definition")
    :   Run the ADS Time Dynamics simulation for a Gaussian Pulse experiment. All result plots will be generated and displayed.

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.time\_dynamics\_analysis.experiments.rabi\_flopping.RabiFloppingExperiment[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.rabi_flopping.RabiFloppingExperiment "Link to this definition")
:   \_\_init\_\_(*cross\_kerr: float = 2*, *qubit\_anharmonicity: float = 300*, *qubit\_frequency: float = 6*, *qubit\_lifetime: float = 30*, *qubit\_dephasing\_time: float = 5*, *qubit\_drive\_strength: float = 1000000000.0*, *qubit\_dimension: int = 2*, *resonator\_frequency: float = 8*, *resonator\_lifetime: float = 30*, *resonator\_dimension: int = 2*, *pulse\_amplitude: float = 0.07*, *pulse\_duration: float = 5000*, *pulse\_phase: float = 0*, *drive\_detuning: float = 0*, *total\_time: float = 10000.0*, *time\_steps: float = 5000*, *initial\_state: str = 'steady'*, *qubit\_temperature: float = 5*, *include\_qubit\_decay: bool = True*, *include\_qubit\_dephasing: bool = True*, *include\_qubit\_bath: bool = False*, *resonator\_temperature: float = 5*, *include\_resonator\_decay: bool = True*, *include\_resonator\_bath: bool = False*, *include\_purcell\_effect: bool = False*, *include\_dressed\_dephasing: bool = False*, *n\_steps: float = 100000000.0*, *r\_tolerance: float = 1e-12*, *a\_tolerance: float = 1e-12*, *max\_step: float = 1*, *\_dialog: TimeDynamicsDialog | None = None*, *\*\*kwargs*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.rabi_flopping.RabiFloppingExperiment.__init__ "Link to this definition")
    :   Initialize a Rabi Flopping experiment.

        Parameters:
        :   * **cross\_kerr** (*float*) – Cross kerr coupling in MHz.
            * **qubit\_anharmonicity** (*float*) – Qubit anharmonicity in MHz.
            * **qubit\_frequency** (*float*) – Qubit frequency in GHz.
            * **qubit\_lifetime** (*float*) – Qubit lifetime in microseconds.
            * **qubit\_dephasing\_time** (*float*) – Qubit dephasing time in microseconds.
            * **qubit\_drive\_strength** (*float*) – Qubit drive strength scaling factor.
            * **qubit\_dimension** (*int*) – Number of qubit energy levels to include.
            * **resonator\_frequency** (*float*) – Resonator frequency in GHz.
            * **resonator\_lifetime** (*float*) – Resonator lifetime in microseconds.
            * **resonator\_dimension** (*int*) – Number of resonator energy levels to include.
            * **pulse\_amplitude** (*float*) – The drive strength of the Flattop pulse in GHz.
            * **pulse\_duration** (*float*) – The duration of the Flattop pulse in ns, measured as six standard deviations.
            * **pulse\_phase** (*float*) – The quadrature phase of the complex pulse in degrees.
            * **drive\_detuning** (*float*) – The detuning of the drive away from the qubit resonance in kHz.
            * **total\_time** (*float*) – Total simulation time in ns.
            * **time\_steps** (*float*) – The number of intermediate states to evaluate the expectated values.
            * **initial\_state** (*str*) – Initial state of the system (“ground” or “steady”).
            * **qubit\_temperature** (*float*) – The temperature of the bath, in mK, that the qubit is coupled to.
            * **include\_qubit\_decay** (*bool*) – Whether to include energy relaxation due to photon loss in the qubit.
            * **include\_qubit\_dephasing** (*bool*) – Whether to include qubit dephasing.
            * **include\_qubit\_bath** (*bool*) – Whether to couple the qubit to a thermal bath in the simulation.
            * **resonator\_temperature** (*float*) – The temperature of the bath, in mK, that the resonator is coupled to.
            * **include\_resonator\_decay** (*bool*) – Whether to include energy relaxation due to photon loss in the resonator.
            * **include\_resonator\_bath** (*bool*) – Whether to couple the resonator to a thermal bath in the simulation.
            * **include\_purcell\_effect** (*bool*) – Whether to include dissipation due to the Purcell effect.
            * **include\_dressed\_dephasing** (*bool*) – Whether to include dissipation due to the dressed-dephasing effect.
            * **n\_steps** (*float*) – Sets the the maximum number of steps the solver will take per each interval of integration.
            * **r\_tolerance** (*float*) – Relative Tolerance - Sets a threshold for acceptable magnitudes of error as a proportion of the magnitude of the solution.
            * **a\_tolerance** (*float*) – Absolute Tolerance - Sets a fixed threshold for acceptable magnitudes of error.
            * **max\_step** (*float*) – Sets the maximum step size in ns. For accurate simulation, this number must be smaller then half the width of the shortest pulse in the simulation.
            * **\*\*kwargs** (*dict*) – Collect additional keyword arguments.

        Example

        ```
        # Access Quantum Tool Suite
        quantum_addon = app.import_addon_as_module("Quantum Tools")

        # Access Experiment Class
        from quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.rabi_flopping import RabiFloppingExperiment

        # Simulate Experiment
        experiment = RabiFloppingExperiment()  # default parameters
        experiment = RabiFloppingExperiment(
                            cross_kerr=2.0,
                            qubit_frequency=8.0,
                            qubit_lifetime=30.0,
                            resonator_frequency=6.0,
                            resonator_lifetime=30.0) # custom parameters
        experiment.run_simulation()
        ```

    clear\_plots() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.rabi_flopping.RabiFloppingExperiment.clear_plots "Link to this definition")
    :   Clear and close all plots that have been generated and displayed via the python console.

    plot\_excited\_state\_population() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.rabi_flopping.RabiFloppingExperiment.plot_excited_state_population "Link to this definition")
    :   Generate the excited state population plot.

    plot\_pulse\_visualization() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.rabi_flopping.RabiFloppingExperiment.plot_pulse_visualization "Link to this definition")
    :   Generate the pulse visualization plot.

    plot\_results() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.rabi_flopping.RabiFloppingExperiment.plot_results "Link to this definition")
    :   Plot all simulation results.

    run\_simulation() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.rabi_flopping.RabiFloppingExperiment.run_simulation "Link to this definition")
    :   Run the ADS Time Dynamics simulation for a Rabi Flopping experiment. All result plots will be generated and displayed.

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.time\_dynamics\_analysis.experiments.energy\_relaxation.EnergyRelaxationExperiment[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.energy_relaxation.EnergyRelaxationExperiment "Link to this definition")
:   \_\_init\_\_(*cross\_kerr: float = 2*, *qubit\_anharmonicity: float = 300*, *qubit\_frequency: float = 6*, *qubit\_lifetime: float = 30*, *qubit\_dephasing\_time: float = 5*, *qubit\_drive\_strength: float = 1000000000.0*, *qubit\_dimension: int = 2*, *resonator\_frequency: float = 8*, *resonator\_lifetime: float = 30*, *resonator\_dimension: int = 2*, *pulse\_amplitude: float = 0.125*, *pulse\_duration: float = 30*, *pulse\_phase: float = 0*, *drive\_detuning: float = 0*, *drag\_coefficient: float = 0*, *total\_time: float = 50000.0*, *time\_steps: float = 400*, *initial\_state: str = 'steady'*, *qubit\_temperature: float = 50*, *include\_qubit\_decay: bool = True*, *include\_qubit\_dephasing: bool = True*, *include\_qubit\_bath: bool = False*, *resonator\_temperature: float = 50*, *include\_resonator\_decay: bool = True*, *include\_resonator\_bath: bool = False*, *include\_purcell\_effect: bool = False*, *include\_dressed\_dephasing: bool = False*, *n\_steps: float = 100000000.0*, *r\_tolerance: float = 1e-12*, *a\_tolerance: float = 1e-12*, *max\_step: float = 1*, *\_dialog: TimeDynamicsDialog | None = None*, *\*\*kwargs*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.energy_relaxation.EnergyRelaxationExperiment.__init__ "Link to this definition")
    :   Initialize an Energy Relaxation (T1) experiment.

        Parameters:
        :   * **cross\_kerr** (*float*) – Cross kerr coupling in MHz.
            * **qubit\_anharmonicity** (*float*) – Qubit anharmonicity in MHz.
            * **qubit\_frequency** (*float*) – Qubit frequency in GHz.
            * **qubit\_lifetime** (*float*) – Qubit lifetime in microseconds.
            * **qubit\_dephasing\_time** (*float*) – Qubit dephasing time in microseconds.
            * **qubit\_drive\_strength** (*float*) – Qubit drive strength scaling factor.
            * **qubit\_dimension** (*int*) – Number of qubit energy levels to include.
            * **resonator\_frequency** (*float*) – Resonator frequency in GHz.
            * **resonator\_lifetime** (*float*) – Resonator lifetime in microseconds.
            * **resonator\_dimension** (*int*) – Number of resonator energy levels to include.
            * **pulse\_amplitude** (*float*) – The drive strength of the Gaussian pulse in GHz.
            * **pulse\_duration** (*float*) – The duration of the Gaussian pulse in ns, measured as six standard deviations.
            * **pulse\_phase** (*float*) – The quadrature phase of the complex pulse in degrees.
            * **drive\_detuning** (*float*) – The detuning of the drive away from the qubit resonance in kHz.
            * **drag\_coefficient** (*float*) – The scaling factor of the Gaussian derivative component in the DRAG pulse scheme.
            * **total\_time** (*float*) – Total simulation time in ns.
            * **time\_steps** (*float*) – The number of intermediate states to evaluate the expectated values.
            * **initial\_state** (*str*) – Initial state of the system (“ground” or “steady”).
            * **qubit\_temperature** (*float*) – The temperature of the bath, in mK, that the qubit is coupled to.
            * **include\_qubit\_decay** (*bool*) – Whether to include energy relaxation due to photon loss in the qubit.
            * **include\_qubit\_dephasing** (*bool*) – Whether to include qubit dephasing.
            * **include\_qubit\_bath** (*bool*) – Whether to couple the qubit to a thermal bath in the simulation.
            * **resonator\_temperature** (*float*) – The temperature of the bath, in mK, that the resonator is coupled to.
            * **include\_resonator\_decay** (*bool*) – Whether to include energy relaxation due to photon loss in the resonator.
            * **include\_resonator\_bath** (*bool*) – Whether to couple the resonator to a thermal bath in the simulation.
            * **include\_purcell\_effect** (*bool*) – Whether to include dissipation due to the Purcell effect.
            * **include\_dressed\_dephasing** (*bool*) – Whether to include dissipation due to the dressed-dephasing effect.
            * **n\_steps** (*float*) – Sets the the maximum number of steps the solver will take per each interval of integration.
            * **r\_tolerance** (*float*) – Relative Tolerance - Sets a threshold for acceptable magnitudes of error as a proportion of the magnitude of the solution.
            * **a\_tolerance** (*float*) – Absolute Tolerance - Sets a fixed threshold for acceptable magnitudes of error.
            * **max\_step** (*float*) – Sets the maximum step size in ns. For accurate simulation, this number must be smaller then half the width of the shortest pulse in the simulation.
            * **\*\*kwargs** (*dict*) – Collect additional keyword arguments.

        Example

        ```
        # Access Quantum Tool Suite
        quantum_addon = app.import_addon_as_module("Quantum Tools")

        # Access Experiment Class
        from quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.energy_relaxation import EnergyRelaxationExperiment

        # Simulate Experiment
        experiment = EnergyRelaxationExperiment()  # default parameters
        experiment = EnergyRelaxationExperiment(
                            cross_kerr=2.0,
                            qubit_frequency=8.0,
                            qubit_lifetime=30.0,
                            resonator_frequency=6.0,
                            resonator_lifetime=30.0) # custom parameters
        experiment.run_simulation()
        ```

    clear\_plots() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.energy_relaxation.EnergyRelaxationExperiment.clear_plots "Link to this definition")
    :   Clear and close all plots that have been generated and displayed via the python console.

    plot\_excited\_state\_population() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.energy_relaxation.EnergyRelaxationExperiment.plot_excited_state_population "Link to this definition")
    :   Generate the excited state population plot.

    plot\_pulse\_visualization() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.energy_relaxation.EnergyRelaxationExperiment.plot_pulse_visualization "Link to this definition")
    :   Generate the pulse visualization plot.

    plot\_results() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.energy_relaxation.EnergyRelaxationExperiment.plot_results "Link to this definition")
    :   Plot all simulation results.

    run\_simulation() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.energy_relaxation.EnergyRelaxationExperiment.run_simulation "Link to this definition")
    :   Run the ADS Time Dynamics simulation for an Energy Relaxation (T1) simulation. All result plots will be generated and displayed.

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.time\_dynamics\_analysis.experiments.ramsey.RamseyExperiment[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.ramsey.RamseyExperiment "Link to this definition")
:   \_\_init\_\_(*cross\_kerr: float = 2*, *qubit\_anharmonicity: float = 300*, *qubit\_frequency: float = 6*, *qubit\_lifetime: float = 30*, *qubit\_dephasing\_time: float = 5*, *qubit\_drive\_strength: float = 1000000000.0*, *qubit\_dimension: int = 2*, *resonator\_frequency: float = 8*, *resonator\_lifetime: float = 30*, *resonator\_dimension: int = 2*, *pulse\_amplitude: float = 0.0625*, *pulse\_duration: float = 30*, *pulse\_phase: float = 0*, *drive\_detuning: float = -500.0*, *delay\_scan\_start\_time: float = 100*, *delay\_scan\_end\_time: float = 20000.0*, *delay\_scan\_num\_points: float = 400*, *initial\_state: str = 'steady'*, *select\_pulse\_to\_plot: int = 1*, *qubit\_temperature: float = 50*, *include\_qubit\_decay: bool = True*, *include\_qubit\_dephasing: bool = True*, *include\_qubit\_bath: bool = True*, *resonator\_temperature: float = 15*, *include\_resonator\_decay: bool = False*, *include\_resonator\_bath: bool = False*, *include\_purcell\_effect: bool = False*, *include\_dressed\_dephasing: bool = False*, *n\_steps: float = 100000000.0*, *r\_tolerance: float = 1e-12*, *a\_tolerance: float = 1e-12*, *max\_step: float = 1*, *\_dialog: TimeDynamicsDialog | None = None*, *\*\*kwargs*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.ramsey.RamseyExperiment.__init__ "Link to this definition")
    :   Initialize a Ramsey (T2) experiment.

        Parameters:
        :   * **cross\_kerr** (*float*) – Cross kerr coupling in MHz.
            * **qubit\_anharmonicity** (*float*) – Qubit anharmonicity in MHz.
            * **qubit\_frequency** (*float*) – Qubit frequency in GHz.
            * **resonator\_frequency** (*float*) – Resonator frequency in GHz.
            * **qubit\_lifetime** (*float*) – Qubit lifetime in microseconds.
            * **qubit\_dephasing\_time** (*float*) – Qubit dephasing time in microseconds.
            * **qubit\_drive\_strength** (*float*) – Qubit drive strength scaling factor.
            * **qubit\_dimension** (*int*) – Number of qubit energy levels to include.
            * **resonator\_lifetime** (*float*) – Resonator lifetime in microseconds.
            * **resonator\_dimension** (*int*) – Number of resonator energy levels to include.
            * **pulse\_amplitude** (*float*) – The drive strength of the Gaussian pulse(s) in GHz.
            * **pulse\_duration** (*float*) – The duration of the Gaussian pulse(s) in ns, measured as six standard deviations.
            * **pulse\_phase** (*float*) – The quadrature phase of the complex pulse in degrees.
            * **drive\_detuning** (*float*) – The detuning of the drive away from the qubit resonance in kHz.
            * **delay\_scan\_start\_time** (*float*) – The starting value of the pulse delay sweep in ns.
            * **delay\_scan\_end\_time** (*float*) – The ending value of the pulse delay sweep in ns.
            * **delay\_scan\_num\_points** (*int*) – The number of points in the pulse delay sweep.
            * **select\_pulse\_to\_plot** (*int*) – Determines which delay sweep point to choose when plotting pulse operations.
            * **initial\_state** (*str*) – Initial state of the system (“ground” or “steady”).
            * **qubit\_temperature** (*float*) – The temperature of the bath, in mK, that the qubit is coupled to.
            * **include\_qubit\_decay** (*bool*) – Whether to include energy relaxation due to photon loss in the qubit.
            * **include\_qubit\_dephasing** (*bool*) – Whether to include qubit dephasing.
            * **include\_qubit\_bath** (*bool*) – Whether to couple the qubit to a thermal bath in the simulation.
            * **resonator\_temperature** (*float*) – The temperature of the bath, in mK, that the resonator is coupled to.
            * **include\_resonator\_decay** (*bool*) – Whether to include energy relaxation due to photon loss in the resonator.
            * **include\_resonator\_bath** (*bool*) – Whether to couple the resonator to a thermal bath in the simulation.
            * **include\_purcell\_effect** (*bool*) – Whether to include dissipation due to the Purcell effect.
            * **include\_dressed\_dephasing** (*bool*) – Whether to include dissipation due to the dressed-dephasing effect.
            * **n\_steps** (*float*) – Sets the the maximum number of steps the solver will take per each interval of integration.
            * **r\_tolerance** (*float*) – Relative Tolerance - Sets a threshold for acceptable magnitudes of error as a proportion of the magnitude of the solution.
            * **a\_tolerance** (*float*) – Absolute Tolerance - Sets a fixed threshold for acceptable magnitudes of error.
            * **max\_step** (*float*) – Sets the maximum step size in ns. For accurate simulation, this number must be smaller then half the width of the shortest pulse in the simulation.
            * **\*\*kwargs** (*dict*) – Collect additional keyword arguments.

        Example

        ```
        # Access Quantum Tool Suite
        quantum_addon = app.import_addon_as_module("Quantum Tools")

        # Access Experiment Class
        from quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.ramsey import RamseyExperiment

        # Simulate Experiment
        experiment = RamseyExperiment()  # default parameters
        experiment = RamseyExperiment(
                            cross_kerr=2.0,
                            qubit_frequency=8.0,
                            qubit_lifetime=30.0,
                            resonator_frequency=6.0,
                            resonator_lifetime=30.0) # custom parameters
        experiment.run_simulation()
        ```

    clear\_plots() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.ramsey.RamseyExperiment.clear_plots "Link to this definition")
    :   Clear and close all plots that have been generated and displayed via the python console.

    plot\_polarization() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.ramsey.RamseyExperiment.plot_polarization "Link to this definition")
    :   Generate polarization plot.

    plot\_pulse\_visualization() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.ramsey.RamseyExperiment.plot_pulse_visualization "Link to this definition")
    :   Generate pulse visualization plot.

    plot\_results() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.ramsey.RamseyExperiment.plot_results "Link to this definition")
    :   Plot all simulation results.

    run\_simulation() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.ramsey.RamseyExperiment.run_simulation "Link to this definition")
    :   Run the ADS Time Dynamics simulation for a Ramsey (T2) experiment. All result plots will be generated and displayed.

*class* quantum\_addon.src.keysight.ads.quantum\_analysis.python.time\_dynamics\_analysis.experiments.dispersive\_readout.DispersiveReadoutExperiment[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.dispersive_readout.DispersiveReadoutExperiment "Link to this definition")
:   \_\_init\_\_(*cross\_kerr: float = 2*, *qubit\_anharmonicity: float = 300*, *qubit\_frequency: float = 6*, *qubit\_lifetime: float = 30*, *qubit\_dephasing\_time: float = 5*, *qubit\_dimension: int = 3*, *resonator\_frequency: float = 8*, *resonator\_dimension: int = 20*, *kappa\_external: float = 10*, *kappa\_internal: float = 1.67e-05*, *acquisition\_window\_start: float = 1.25*, *acquisition\_window\_end: float = 1.75*, *readout\_pulse: str = 'Flattop'*, *readout\_pulse\_sigma\_edge: float = 5*, *readout\_amplitude: float = 0.016*, *readout\_duration: float = 2000.0*, *readout\_phase: float = 0.0*, *readout\_drive\_detuning: float = -5*, *total\_time: float = 3000.0*, *time\_steps: float = 2000*, *qubit\_temperature: float = 50*, *include\_qubit\_decay: bool = True*, *include\_qubit\_dephasing: bool = True*, *include\_qubit\_bath: bool = True*, *resonator\_temperature: float = 50*, *include\_resonator\_decay: bool = True*, *include\_resonator\_bath: bool = True*, *include\_purcell\_effect: bool = True*, *include\_dressed\_dephasing: bool = True*, *n\_steps: float = 100000.0*, *r\_tolerance: float = 1e-08*, *a\_tolerance: float = 1e-08*, *max\_step: float = 2*, *\_dialog: TimeDynamicsDialog | None = None*, *\*\*kwargs*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.dispersive_readout.DispersiveReadoutExperiment.__init__ "Link to this definition")
    :   Initialize a Dispersive Readout experiment.

        Parameters:
        :   * **cross\_kerr** (*float*) – Cross kerr coupling in MHz.
            * **qubit\_anharmonicity** (*float*) – Qubit anharmonicity in MHz.
            * **qubit\_frequency** (*float*) – Qubit frequency in GHz.
            * **qubit\_lifetime** (*float*) – Qubit lifetime in microseconds.
            * **qubit\_dephasing\_time** (*float*) – Qubit dephasing time in microseconds.
            * **qubit\_dimension** (*int*) – Number of qubit energy levels to include.
            * **resonator\_frequency** (*float*) – Resonator frequency in GHz.
            * **resonator\_dimension** (*int*) – Number of resonator energy levels to include.
            * **kappa\_external** (*float*) – External coupling rate of the resonator in MHz.
            * **kappa\_internal** (*float*) – Internal coupling rate of the resonator in MHz.
            * **acquisition\_window\_start** (*float*) – Start time of the acquisition window in microseconds.
            * **acquisition\_window\_end** (*float*) – End time of the acquisition window in microseconds.
            * **readout\_pulse** (*str*) – The shape of the readout pulse (“Flattop” or “Gaussian”).
            * **readout\_pulse\_sigma\_edge** (*float*) – The standard deviation of the Gaussian edges for a flattop pulse in ns.
            * **readout\_amplitude** (*float*) – The drive strength of the readout pulse in GHz.
            * **readout\_duration** (*float*) – The duration of the readout pulse in ns.
            * **readout\_phase** (*float*) – The quadrature phase of the readout drive in degrees.
            * **readout\_drive\_detuning** (*float*) – The detuning of the readout drive from the resonator frequency in MHz.
            * **total\_time** (*float*) – Total simulation time in ns.
            * **time\_steps** (*float*) – The number of intermediate states to evaluate the expectated values.
            * **qubit\_temperature** (*float*) – Qubit temperature in mK.
            * **include\_qubit\_decay** (*bool*) – Whether to include energy relaxation due to photon loss in the qubit.
            * **include\_qubit\_dephasing** (*bool*) – Whether to include qubit dephasing.
            * **include\_qubit\_bath** (*bool*) – Whether to couple the qubit to a thermal bath in the simulation.
            * **resonator\_temperature** (*float*) – Resonator temperature in mK.
            * **include\_resonator\_decay** (*bool*) – Whether to include energy relaxation due to photon loss in the resonator.
            * **include\_resonator\_bath** (*bool*) – Whether to couple the resonator to a thermal bath in the simulation.
            * **include\_purcell\_effect** (*bool*) – Whether to include dissipation due to the Purcell effect.
            * **include\_dressed\_dephasing** (*bool*) – Whether to include dissipation due to the dressed-dephasing effect.
            * **n\_steps** (*float*) – Sets the the maximum number of steps the solver will take per each interval of integration.
            * **r\_tolerance** (*float*) – Relative Tolerance - Sets a threshold for acceptable magnitudes of error as a proportion of the magnitude of the solution.
            * **a\_tolerance** (*float*) – Absolute Tolerance - Sets a fixed threshold for acceptable magnitudes of error.
            * **max\_step** (*float*) – Sets the maximum step size in ns. For accurate simulation, this number must be smaller then half the width of the shortest pulse in the simulation.
            * **\*\*kwargs** (*dict*) – Collect additional keyword arguments.

        Example

        ```
        # Access Quantum Tool Suite
        quantum_addon = app.import_addon_as_module("Quantum Tools")

        # Access Experiment Class
        from quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.dispersive_readout import DispersiveReadoutExperiment

        # Simulate Experiment
        experiment = DispersiveReadoutExperiment()  # default parameters
        experiment = DispersiveReadoutExperiment(
                            cross_kerr=-10.0,
                            qubit_anharmonicity=-315.0,
                            qubit_frequency=8.98,
                            qubit_lifetime=30.0,
                            qubit_dephasing_time=15.0,
                            resonator_frequency=6.6)  # custom parameters
        experiment.run_simulation()
        ```

    clear\_plots() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.dispersive_readout.DispersiveReadoutExperiment.clear_plots "Link to this definition")
    :   Clear and close all plots that have been generated and displayed via the python console.

    plot\_quantum\_ltd\_readout\_blob() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.dispersive_readout.DispersiveReadoutExperiment.plot_quantum_ltd_readout_blob "Link to this definition")
    :   Generate the quantum limited readout plot.

    plot\_quantum\_trajectory(*start\_time: float = 0.0*, *stop\_time: float = 2e-06*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.dispersive_readout.DispersiveReadoutExperiment.plot_quantum_trajectory "Link to this definition")
    :   Generate the quantum trajectories plot.

    plot\_readout\_amplitude() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.dispersive_readout.DispersiveReadoutExperiment.plot_readout_amplitude "Link to this definition")
    :   Generate the dispersive readout amplitude plot.

    plot\_readout\_phase() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.dispersive_readout.DispersiveReadoutExperiment.plot_readout_phase "Link to this definition")
    :   Generate the dispersive readout phase plot.

    plot\_readout\_stage\_blob(*gain: float = 80*, *noise\_temp: float = 0.5*) → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.dispersive_readout.DispersiveReadoutExperiment.plot_readout_stage_blob "Link to this definition")
    :   Generate a readout stage plot.

    plot\_results() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.dispersive_readout.DispersiveReadoutExperiment.plot_results "Link to this definition")
    :   Plot all simulation results.

    run\_simulation() → None[](#quantum_addon.src.keysight.ads.quantum_analysis.python.time_dynamics_analysis.experiments.dispersive_readout.DispersiveReadoutExperiment.run_simulation "Link to this definition")
    :   Run the ADS Time Dynamics simulation for a Dispersive Readout experiment. All result plots will be generated and displayed.


---

