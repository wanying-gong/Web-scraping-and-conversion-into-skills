<!-- 来源: API_Reference\circuit\classes\circuit.html -->

[![Logo](../../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../../../index.md)
* [API Reference](../../index.md)
* [Circuit API](../index.md)
* [Classes](index.md)
* Circuit

1.2.5

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../../../_sources/API_Reference/circuit/classes/circuit.rst.txt)

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
  + [ADS](../../ads/index.md)
    - [Functions](../../ads/functions/index.md)
    - [Classes](../../ads/classes/index.md)
      * [ADS](../../ads/classes/ads.md)
      * [CircuitSimulator](../../ads/classes/circuit_simulator.md)
  + [Circuit API](../index.md)
    - [Functions](../functions/index.md)
    - [Classes](index.md)
      * Circuit
      * [Definition](definition.md)
      * [Instance](instance.md)
      * [Node](node.md)
      * [OptimizationRange](optimization_range.md)
      * [TuningRange](tuning_range.md)
      * [Value](value.md)
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

# Circuit[](#circuit "Link to this heading")

*class* keysight.edatoolbox.circuit.Circuit(*netlist: str = ''*, *import\_options=None*)[](#keysight.edatoolbox.circuit.Circuit "Link to this definition")
:   *property* GND*: [Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")*[](#keysight.edatoolbox.circuit.Circuit.GND "Link to this definition")
    :   The special GND node that can be used to wire up a circuit to the GND.

    add(*instance: [Instance](instance.md#keysight.edatoolbox.circuit.Instance "keysight.edatoolbox.circuit.Instance")*) → None[](#keysight.edatoolbox.circuit.Circuit.add "Link to this definition")
    :   Add an instance to the circuit.

        Parameters:
        :   **instance** ([*Instance*](instance.md#keysight.edatoolbox.circuit.Instance "keysight.edatoolbox.circuit.Instance")) – The instance to add to the circuit.

    *property* analyses*: List[Analysis]*[](#keysight.edatoolbox.circuit.Circuit.analyses "Link to this definition")
    :   Returning the extracted analyses

    connect(*node1: [Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")*, *node2: [Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")*) → None[](#keysight.edatoolbox.circuit.Circuit.connect "Link to this definition")
    :   Connect two nodes in the circuit.

        Parameters:
        :   * **node1** ([*Node*](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")) – The first node of the connection.
            * **node2** ([*Node*](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")) – The second node of the connection.

    connections(*node\_or\_instance: [Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node") | [Instance](instance.md#keysight.edatoolbox.circuit.Instance "keysight.edatoolbox.circuit.Instance")*) → List[[Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")][](#keysight.edatoolbox.circuit.Circuit.connections "Link to this definition")
    :   Returns a list of connected nodes.

        Parameters:
        :   **node\_or\_instance** (*Union**[*[*Node*](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")*,* [*Instance*](instance.md#keysight.edatoolbox.circuit.Instance "keysight.edatoolbox.circuit.Instance")*]*) – Can either be an existing node and then the list of connections to this Node is given. Alternatively an instance, and then all connections to the Instance are given.

    *property* definitions*: Dict[str, [Definition](definition.md#keysight.edatoolbox.circuit.Definition "keysight.edatoolbox.circuit.Definition")]*[](#keysight.edatoolbox.circuit.Circuit.definitions "Link to this definition")
    :   Returns a dictionary of instance name to the actual instance

    generate\_netlist(*variables: dict = {}*)[](#keysight.edatoolbox.circuit.Circuit.generate_netlist "Link to this definition")
    :   Generate a netlist for this circuit.

        Parameters:
        :   **variables** (*dict*) – Optionally a dictionary containing as key the variable name and as value the value that should be assigned during netlisting. Variables whose value are not provided
            are taken from the circuit.

    generate\_python(*options=None*) → str[](#keysight.edatoolbox.circuit.Circuit.generate_python "Link to this definition")
    :   Generate a Python fragment for this circuit. Cannot handle definitions and instances using them.

        > options: object
        > :   Optional object to control how to generate the Python fragment. The attribute ‘.explicit\_connect’
        >     controls if in the generated Python fragment the list of connections is done at the end or while
        >     generating all the instances.

    import\_netlist(*netlist: str*, *import\_options=None*) → None[](#keysight.edatoolbox.circuit.Circuit.import_netlist "Link to this definition")
    :   Import a netlist into the circuit.

        Parameters:
        :   * **netlist** (*str*) – The netlist string
            * **import\_options** (*object*) – Optional object to control how to import the netlist. The attribute ‘.extract\_analyses’ controls if in the netlist the
              analyses are extracted into objects on the new API on top of circuit or whether they remain as regular instances in the
              netlist.

        Notes

        Not all analyses types are fully supported yet. If you have no interest in modifying the analyses, or removing/adding some of them, then
        the safest option is to use the .extract\_analyses=False

        ```
        >>> ckt = Circuit()
        >>> ckt.import_netlist(my_netlist_string, Bunch(extract_analyses=False))
        ```

    *property* instances*: Dict[str, [Instance](instance.md#keysight.edatoolbox.circuit.Instance "keysight.edatoolbox.circuit.Instance")]*[](#keysight.edatoolbox.circuit.Circuit.instances "Link to this definition")
    :   Returns a dictionary of instance name to the actual instance

    *property* output\_dataset*: str*[](#keysight.edatoolbox.circuit.Circuit.output_dataset "Link to this definition")
    :   Controls the name of the output dataset file.

        Notes

        Depending on the format of the string it will instruct the circuit simulator to save the dataset at following location:

        * absolute path –> ‘f:/temp/myoutput’
        * relative path –> ‘myoutput’
        * lcv string –> ‘mylibrary:mycell:mycellview’ –> the output name will be ‘mycell’
        * None –> determined by the instances within the circuit

    *property* parameters*: Dict[str, \_SpectreParameter]*[](#keysight.edatoolbox.circuit.Circuit.parameters "Link to this definition")
    :   Returns a dictionary of parameter name to the SpectreParameter’s

    *property* variables*: Dict[str, Var]*[](#keysight.edatoolbox.circuit.Circuit.variables "Link to this definition")
    :   Returns a dictionary of variable name to the VAR instance

On this page

[Previous

Classes](index.md)
[Next

Definition](definition.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top