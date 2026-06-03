<!-- 来源: reference\quantum\squid_extrema_analysis.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Quantum Python Documentation](../../index.md)
* [Reference](../index.md)
* [Quantum Addon](index.md)
* SQUID Extrema Analysis

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
    - SQUID Extrema Analysis
    - [Dilution Fridge Input Line Designer](dilution_fridge_input_line_designer.md)
    - [Time Dynamics Analysis](time_dynamics_analysis.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
  + [How to Use Pytest](../../howto/pytest.md)

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

On this page

[Previous

Parameter Extraction](parameter_extraction.md)
[Next

Dilution Fridge Input Line Designer](dilution_fridge_input_line_designer.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top