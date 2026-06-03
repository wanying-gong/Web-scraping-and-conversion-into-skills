<!-- 来源: reference\quantum\parameter_extraction.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Quantum Python Documentation](../../index.md)
* [Reference](../index.md)
* [Quantum Addon](index.md)
* Parameter Extraction

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
    - Parameter Extraction
    - [SQUID Extrema Analysis](squid_extrema_analysis.md)
    - [Dilution Fridge Input Line Designer](dilution_fridge_input_line_designer.md)
    - [Time Dynamics Analysis](time_dynamics_analysis.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
  + [How to Use Pytest](../../howto/pytest.md)

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

On this page

[Previous

Hamiltonian Analysis](hamiltonian_analysis.md)
[Next

SQUID Extrema Analysis](squid_extrema_analysis.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top