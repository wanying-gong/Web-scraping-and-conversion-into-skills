<!-- 来源: API_Reference\ads\classes\ads.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../../../index.md)
* [API Reference](../../index.md)
* [ADS](../index.md)
* [Classes](index.md)
* ADS

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../../_sources/API_Reference/ads/classes/ads.rst.txt)

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* [Initial Setup](../../../Initial_Setup/index.md)
  + [Installation](../../../Initial_Setup/installation.md)
  + [Prerequisites](../../../Initial_Setup/prerequisites.md)
  + [Verifying Installation](../../../Initial_Setup/verifying.md)
  + [SSH](../../../Initial_Setup/ssh.md)
* [How-To](../../../How-To/index.md)
  + [Create a Circuit](../../../How-To/circuit.md)
  + [Run a Circuit Simulation](../../../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../../../How-To/sipro.md)
* [API Reference](../../index.md)
  + [ADS](../index.md)
    - [Functions](../functions/index.md)
    - [Classes](index.md)
      * ADS
      * [CircuitSimulator](circuit_simulator.md)
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
  + [External API](../../extra/index.md)
    - [empro.analysis](../../extra/empro/index.md)
  + [Multi Python API](../../multi_python/index.md)
    - [Functions](../../multi_python/functions/index.md)
  + [xxPro](../../xxpro/index.md)
* [Examples](../../../Examples/index.md)
  + [Running EDA Toolbox Examples](../../../Examples/Running%20Examples.md)
  + [Example baluns](../../../Examples/ex_baluns.md)
  + [Example co optimize matching network](../../../Examples/ex_co_optimize_matching_network.md)
  + [Example create 3d empro serpentines](../../../Examples/ex_create_3d_empro_serpentines.md)
  + [Example dump workspace netlists](../../../Examples/ex_dump_workspace_netlists.md)
  + [Example empro extract resonance](../../../Examples/ex_empro_extract_resonance.md)
  + [Example high pass filter sub circuit](../../../Examples/ex_high_pass_filter_sub_circuit.md)
  + [Example import brd](../../../Examples/ex_import_brd.md)
  + [Example import ipc2581](../../../Examples/ex_import_ipc2581.md)
  + [Example import odb](../../../Examples/ex_import_odb.md)
  + [Example low pass filter](../../../Examples/ex_low_pass_filter.md)
  + [Example multi python](../../../Examples/ex_multi_python.md)
  + [Example odbpp simulate pipro ac reuse sio](../../../Examples/ex_odbpp_simulate_pipro_ac_reuse_sio.md)
  + [Example odbpp simulate pipro dc](../../../Examples/ex_odbpp_simulate_pipro_dc.md)
  + [Example odbpp simulate rfpro](../../../Examples/ex_odbpp_simulate_rfpro.md)
  + [Example optimize matching network](../../../Examples/ex_optimize_matching_network.md)
  + [Example pipro ac](../../../Examples/ex_pipro_example_ac.md)
  + [Example pipro dc](../../../Examples/ex_pipro_example_dc.md)
  + [Example quantumpro one qubit epr](../../../Examples/ex_quantumpro_one_qubit_epr.md)
  + [Example quantumpro one qubit freq](../../../Examples/ex_quantumpro_one_qubit_freq.md)
  + [Example rfpro stop nets](../../../Examples/ex_rfpro_stop_nets.md)
  + [Example run hb simulation](../../../Examples/ex_run_hb_simulation.md)
  + [Example run netlist](../../../Examples/ex_run_netlist.md)
  + [Example run netlist from disk](../../../Examples/ex_run_netlist_from_disk.md)
  + [Example run schematic](../../../Examples/ex_run_schematic.md)
  + [Example sipro automation](../../../Examples/ex_sipro_automation.md)
  + [Example sipro channelsim flow](../../../Examples/ex_sipro_channelsim_flow.md)
  + [Example sipro SI](../../../Examples/ex_sipro_example_si.md)
  + [Example sipro extract tdr](../../../Examples/ex_sipro_extract_tdr.md)
  + [Example sipro eye diagram](../../../Examples/ex_sipro_eye_diagram.md)
  + [Example sipro ploteye plotly](../../../Examples/ex_sipro_ploteye_plotly.md)
  + [Example sweep inductor values](../../../Examples/ex_sweep_inductor_values.md)
  + [Example systemvue basic](../../../Examples/ex_systemvue_basic.md)
  + [Example voltage divider](../../../Examples/ex_voltage_divider.md)
  + [Example vsa meas demo](../../../Examples/ex_vsa_meas_demo.md)
* [Release Notes](../../../release_notes/index.md)

# ADS[](#ads "Link to this heading")

*class* keysight.edatoolbox.ads.ADS(*hpeesof\_dir: str = None*)[](#keysight.edatoolbox.ads.ADS "Link to this definition")
:   archive\_workspace(*input\_workspace\_directory: str*, *output\_dir\_filename: str*)[](#keysight.edatoolbox.ads.ADS.archive_workspace "Link to this definition")
    :   Archive an ADS workspace folder to ADS Workspace file (.7zads).

        Parameters:
        :   * **input\_workspace\_directory** (*str*) – Path to existing workspace location example: C:ADSsimple\_matching\_wrk
            * **output\_dir\_filename** (*str*) – Path to the created 7z archive example : C:ADSsimple\_matching\_wrk.7zads

        Returns:
        :   True if archived successfully, False otherwise.

        Return type:
        :   bool

    copy\_cellview(*workspace: str*, *from\_lcvs: LibraryCellView | List[LibraryCellView]*, *to\_lcvs: LibraryCellView | List[LibraryCellView] = None*)[](#keysight.edatoolbox.ads.ADS.copy_cellview "Link to this definition")
    :   Copy cellviews in the same workspace.

        Parameters:
        :   * **workspace** (*str*) – Path to an existing workspace containing source library-cell-view objects.
            * **from\_lcvs** (*LibraryCellView* *or* *List**[**LibraryCellView**]*) – A source library-cell-view object or a list of such.
            * **to\_lcvs** (*LibraryCellView* *or* *List**[**LibraryCellView**]**,* *default=None*) – A target library-cell-view object or a list of such. If not provided,
              new entries will have the source names with the \_copy suffix.

        Raises:
        :   **RuntimeError** – Failed to make a copy.

    create\_pro\_view(*workspace: str*, *input\_lcv: LibraryCellView*, *substrate: str*, *pro\_lcv: str*, *tool: str*, *substrate\_library: str = None*)[](#keysight.edatoolbox.ads.ADS.create_pro_view "Link to this definition")
    :   Create an SI/PE/RF/Quantumpro view from an existing workspace.

        Parameters:
        :   * **workspace** (*str*) – Path to an existing workspace.
            * **input\_lcv** (*LibraryCellView*) – Input LibraryCellView.
            * **substrate** (*str*) – String containing the substrate name, without the .subst suffix.
            * **pro\_lcv** (*LibraryCellView*) – Output LibraryCellView.
            * **tool** (*str*) – Tool to create the new view, options: “rfpro”|”pepro”|”sipi”|”quantumpro”.
            * **substrate\_library** (*str**,* *optional*) – Substrate library name. If not provided, the substrate library will be the same as the input library.

        Raises:
        :   * **RuntimeError** – Failed to create a PRO view.
            * **OSError** –

    create\_workspace(*location: str*, *workspace\_name: str*, *include\_system\_libraries: bool = True*)[](#keysight.edatoolbox.ads.ADS.create_workspace "Link to this definition")
    :   Create a workspace with given name at the given location.

        Parameters:
        :   * **location** (*str*) – Parent folder of the new workspace.
            * **workspace\_name** (*str*) – Name of the new workspace.
            * **include\_system\_libraries** (*bool**,* *default=True*) – If True, include system libraries, otherwise skip.

        Raises:
        :   * **AssertError** – Parent folder does not exist.
            * **RuntimeError** – Failed to create workspace.

    generate\_netlist(*workspace: str*, *lcvSpec: LibraryCellView | List[LibraryCellView]*)[](#keysight.edatoolbox.ads.ADS.generate_netlist "Link to this definition")
    :   Return the netlist from a workspace.

        Parameters:
        :   * **workspace** (*str*) – Path to an existing workspace.
            * **library-cell-view** (*LibraryCellView* *or* *List**[**LibraryCellView**]*) – A library-cell-view to generate netlist. It may also be a list of library-cell-views,
              in which case the return value will be also a list of netlists corresponding to the input order.

        Returns:
        :   Netlist(s).

        Return type:
        :   list

    import\_brd(*workspace: str*, *brdFile: str*)[](#keysight.edatoolbox.ads.ADS.import_brd "Link to this definition")
    :   Import a brd file into an existing workspace.

        Parameters:
        :   * **workspace** (*str*) – Path to an existing workspace.
            * **brdFile** (*str*) – Path to a brd file.

        Raises:
        :   * **AssertionError** – Workspace does not exist.
            * **RuntimeError** – Failed to import the brd file.

    import\_ipc2581(*workspace: str*, *ipc2581\_file: str*, *library: str*, *cell: str*)[](#keysight.edatoolbox.ads.ADS.import_ipc2581 "Link to this definition")
    :   Import an IPC-2581 file into an existing workspace.
        Requires ADS 2025 or later.

        Parameters:
        :   * **workspace** (*str*) – Path to an existing workspace.
            * **ipc2581\_file** (*str*) – Path to an IPC-2581 document.
            * **library** (*str*) – Library base name. By default, the IPC-2581 importer creates separate libraries for components,
              technology, and layout.
            * **cell** (*str*) – The name of a cell where the top-level design will be placed.

        Raises:
        :   * **AssertionError** – Workspace does not exist.
              Unsupported ADS version.
            * **RuntimeError** – Failed to import the IPC-2581 file.

    import\_odbpp(*workspace: str*, *tgzFile: str*, *library: str*, *cell: str = None*, *use\_legacy\_importer=True*, *import\_options=None*)[](#keysight.edatoolbox.ads.ADS.import_odbpp "Link to this definition")
    :   Import an ODB++ file into an existing workspace.

        Parameters:
        :   * **workspace** (*str*) – Path to an existing workspace.
            * **tgzFile** (*str*) – Path to an ODB++ archive.
            * **library** (*str*) – Library base name. By default, the new ODB++ importer creates separate
              libraries for components {library}\_component\_lib,
              technology {library}\_tech\_lib, and layout {library}\_lib.
              The legacy ODB++ importer creates one library.
            * **cell** (*str**,* *optional*) – The name of a cell where the top-level design will be placed.
              Set to the library name by default.
            * **use\_legacy\_importer** (*bool**,* *default=True*) – Use the legacy ODB++ importer.
            * **import\_options** (*OdbImportOptions**,* *optional*) – ODB++ import options.

        Raises:
        :   * **AssertionError** – Workspace does not exist.
            * **RuntimeError** – Failed to import the ODB++ file.

    unarchive\_workspace(*archive\_location: str*, *out\_dir: str*)[](#keysight.edatoolbox.ads.ADS.unarchive_workspace "Link to this definition")
    :   Decompress an ADS workspace file (.7zads or .7z) into the output directory.

        Parameters:
        :   * **archive\_location** (*str*) – Path to a 7z archive containing a workspace.
            * **out\_dir** (*str*) – Path to the created workspace location.

        Returns:
        :   True if decompressed successfully, False otherwise.

        Return type:
        :   bool

On this page

[Previous

Classes](index.md)
[Next

CircuitSimulator](circuit_simulator.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top