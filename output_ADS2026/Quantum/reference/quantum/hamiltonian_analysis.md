<!-- 来源: reference\quantum\hamiltonian_analysis.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Quantum Python Documentation](../../index.md)
* [Reference](../index.md)
* [Quantum Addon](index.md)
* Hamiltonian Analysis

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
  + [Importing Modules](../../intro/importing.md)
  + [Using Visual Studio Code](../../intro/vscode.md)
* [Reference](../index.md)
  + [Quantum Addon](index.md)
    - Hamiltonian Analysis
    - [Parameter Extraction](parameter_extraction.md)
    - [SQUID Extrema Analysis](squid_extrema_analysis.md)
    - [Dilution Fridge Input Line Designer](dilution_fridge_input_line_designer.md)
    - [Time Dynamics Analysis](time_dynamics_analysis.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
  + [How to Use Pytest](../../howto/pytest.md)

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

On this page

[Previous

Quantum Addon](index.md)
[Next

Parameter Extraction](parameter_extraction.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top