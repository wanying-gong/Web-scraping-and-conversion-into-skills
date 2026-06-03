<!-- 来源: reference\quantum\time_dynamics_analysis.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Quantum Python Documentation](../../index.md)
* [Reference](../index.md)
* [Quantum Addon](index.md)
* Time Dynamics Analysis

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
    - [Hamiltonian Analysis](hamiltonian_analysis.md)
    - [Parameter Extraction](parameter_extraction.md)
    - [SQUID Extrema Analysis](squid_extrema_analysis.md)
    - [Dilution Fridge Input Line Designer](dilution_fridge_input_line_designer.md)
    - Time Dynamics Analysis
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
  + [How to Use Pytest](../../howto/pytest.md)

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

On this page

[Previous

Dilution Fridge Input Line Designer](dilution_fridge_input_line_designer.md)
[Next

How-To](../../howto/index.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top