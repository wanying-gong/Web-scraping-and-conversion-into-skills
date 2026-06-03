# Api Reference
> **说明：** Api Reference 相关页面。

> **何时使用：** 当你需要查阅 Api Reference 相关内容时

---

## 本文件目录

- **ADS** (`API_Reference/ads/classes/ads.md`)
- **CircuitSimulator** (`API_Reference/ads/classes/circuit_simulator.md`)
- **Classes** (`API_Reference/ads/classes/index.md`)
- **Functions** (`API_Reference/ads/functions/index.md`)
- **ADS** (`API_Reference/ads/index.md`)
- **Circuit** (`API_Reference/circuit/classes/circuit.md`)
- **Definition** (`API_Reference/circuit/classes/definition.md`)
- **Classes** (`API_Reference/circuit/classes/index.md`)
- **Instance** (`API_Reference/circuit/classes/instance.md`)
- **Node** (`API_Reference/circuit/classes/node.md`)
- **OptimizationRange** (`API_Reference/circuit/classes/optimization_range.md`)
- **TuningRange** (`API_Reference/circuit/classes/tuning_range.md`)
- **Value** (`API_Reference/circuit/classes/value.md`)
- **Functions** (`API_Reference/circuit/functions/index.md`)
- **Circuit API** (`API_Reference/circuit/index.md`)
- **Dataset** (`API_Reference/dataset/index.md`)
- **empro.analysis** (`API_Reference/extra/empro/index.md`)
- **External API** (`API_Reference/extra/index.md`)
- **API Reference** (`API_Reference/index.md`)
- **Functions** (`API_Reference/multi_python/functions/index.md`)
- **Multi Python API** (`API_Reference/multi_python/index.md`)
- **xxPro** (`API_Reference/xxpro/index.md`)

---

<!-- === 来源: API_Reference/ads/classes/ads.md === -->

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


---

<!-- === 来源: API_Reference/ads/classes/circuit_simulator.md === -->

# CircuitSimulator[](#circuitsimulator "Link to this heading")

*class* keysight.edatoolbox.ads.CircuitSimulator(*hpeesof\_dir=None*)[](#keysight.edatoolbox.ads.CircuitSimulator "Link to this definition")
:   run(*commandline: str | List[str]*, *working\_dir: str = None*)[](#keysight.edatoolbox.ads.CircuitSimulator.run "Link to this definition")
    :   Run the circuit simulator with given commandline, for instance ‘-h’

        Parameters:
        :   **commandline** (*Union**[**str**,* *List**[**str**]**]*) – Either a well-formed string or a list of strings (=recommended). The list of strings is then passed on to the circuit simulator.

        Returns:
        :   * *Returns a tuple with as first value the return code of the process. The second part of the tuple is the output collected on stdout/err from*
            * *the circuit simulator.*

        Example

        ```
        >>> CircuitSimulator().run(['-h','R'])
        ```

    run\_netlist(*netlist: str*, *output\_dir: str*, *working\_dir: str = None*, *output\_file: str = None*, *netlist\_file: str = None*, *rel\_data\_dir: str = None*, *dataset\_name: str = None*, *verilog\_dir: str = None*, *pdk\_dirs: List[str] = None*, *extra\_args: List[str] = None*)[](#keysight.edatoolbox.ads.CircuitSimulator.run_netlist "Link to this definition")
    :   Run the provided netlist through the circuit simulator.

        Parameters:
        :   * **netlist** (*str*) – The netlist to run
            * **output\_dir** (*str*) – Where the data should be produced
            * **working\_dir** (*str*) – The optional working dir where the circuit simulator should be started, otherwise the current.
            * **output\_file** (*str*) – Optionally specify the output file where all output from the circuit simulator should be collected. Can be used to extract additional
              information from the run. Otherwise a temporary file is created.
            * **netlist\_file** (*str*) – Optionally specify in which file the netlist will be temporary stored before handing it over to the circuit simulator. If not specified a
              temporary file is created.
            * **rel\_data\_dir** (*str*) – The specification of the data directory where the circuit simulator can pick up additional files specified in the netlist.
            * **dataset\_name** (*str*) – The name of the dataset to save to. Name overrides the default name specified in the netlist.
            * **verilog\_dir** (*str*) – The specification of the verilog directory where the circuit simulator can pick up additional VerilogA files specified in the netlist.
            * **pdk\_dirs** (*List**[**str**]*) – The specification of the PDK directories where the circuit simulator can pick up additional PDK files specified in the netlist. A list of absolute paths is recommended.
            * **extra\_args** (*List**[**str**]*) – Optional list of arguments to pass to the circuit simulator, typically left empty


---

<!-- === 来源: API_Reference/ads/classes/index.md === -->

# Classes[](#classes "Link to this heading")

* [ADS](ads.md)
  + [`ADS`](ads.md#keysight.edatoolbox.ads.ADS)
    - [`ADS.archive_workspace()`](ads.md#keysight.edatoolbox.ads.ADS.archive_workspace)
    - [`ADS.copy_cellview()`](ads.md#keysight.edatoolbox.ads.ADS.copy_cellview)
    - [`ADS.create_pro_view()`](ads.md#keysight.edatoolbox.ads.ADS.create_pro_view)
    - [`ADS.create_workspace()`](ads.md#keysight.edatoolbox.ads.ADS.create_workspace)
    - [`ADS.generate_netlist()`](ads.md#keysight.edatoolbox.ads.ADS.generate_netlist)
    - [`ADS.import_brd()`](ads.md#keysight.edatoolbox.ads.ADS.import_brd)
    - [`ADS.import_ipc2581()`](ads.md#keysight.edatoolbox.ads.ADS.import_ipc2581)
    - [`ADS.import_odbpp()`](ads.md#keysight.edatoolbox.ads.ADS.import_odbpp)
    - [`ADS.unarchive_workspace()`](ads.md#keysight.edatoolbox.ads.ADS.unarchive_workspace)
* [CircuitSimulator](circuit_simulator.md)
  + [`CircuitSimulator`](circuit_simulator.md#keysight.edatoolbox.ads.CircuitSimulator)
    - [`CircuitSimulator.run()`](circuit_simulator.md#keysight.edatoolbox.ads.CircuitSimulator.run)
    - [`CircuitSimulator.run_netlist()`](circuit_simulator.md#keysight.edatoolbox.ads.CircuitSimulator.run_netlist)


---

<!-- === 来源: API_Reference/ads/functions/index.md === -->

# Functions[](#functions "Link to this heading")

keysight.edatoolbox.ads.get\_ads\_location() → str[](#keysight.edatoolbox.ads.get_ads_location "Link to this definition")
:   Returns the location of the latest installed ADS.


---

<!-- === 来源: API_Reference/ads/index.md === -->

# ADS[](#ads "Link to this heading")

* [Functions](functions/index.md)
  + [`get_ads_location()`](functions/index.md#keysight.edatoolbox.ads.get_ads_location)
* [Classes](classes/index.md)
  + [ADS](classes/ads.md)
    - [`ADS`](classes/ads.md#keysight.edatoolbox.ads.ADS)
  + [CircuitSimulator](classes/circuit_simulator.md)
    - [`CircuitSimulator`](classes/circuit_simulator.md#keysight.edatoolbox.ads.CircuitSimulator)


---

<!-- === 来源: API_Reference/circuit/classes/circuit.md === -->

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


---

<!-- === 来源: API_Reference/circuit/classes/definition.md === -->

# Definition[](#definition "Link to this heading")

*class* keysight.edatoolbox.circuit.Definition(*name=None*, *pins=None*, *fragment=None*)[](#keysight.edatoolbox.circuit.Definition "Link to this definition")
:   A definition captures a part of the netlist marked as definition.

    *property* GND*: [Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")*[](#keysight.edatoolbox.circuit.Definition.GND "Link to this definition")
    :   The special GND node that can be used to wire up a circuit to the GND.

    add(*instance: [Instance](instance.md#keysight.edatoolbox.circuit.Instance "keysight.edatoolbox.circuit.Instance")*) → None[](#keysight.edatoolbox.circuit.Definition.add "Link to this definition")
    :   Add an instance to the circuit.

        Parameters:
        :   **instance** ([*Instance*](instance.md#keysight.edatoolbox.circuit.Instance "keysight.edatoolbox.circuit.Instance")) – The instance to add to the circuit.

    *property* analyses*: List[Analysis]*[](#keysight.edatoolbox.circuit.Definition.analyses "Link to this definition")
    :   Returning the extracted analyses

    connect(*node1: [Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")*, *node2: [Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")*) → None[](#keysight.edatoolbox.circuit.Definition.connect "Link to this definition")
    :   Connect two nodes in the circuit.

        Parameters:
        :   * **node1** ([*Node*](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")) – The first node of the connection.
            * **node2** ([*Node*](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")) – The second node of the connection.

    connections(*node\_or\_instance: [Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node") | [Instance](instance.md#keysight.edatoolbox.circuit.Instance "keysight.edatoolbox.circuit.Instance")*) → List[[Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")][](#keysight.edatoolbox.circuit.Definition.connections "Link to this definition")
    :   Returns a list of connected nodes.

        Parameters:
        :   **node\_or\_instance** (*Union**[*[*Node*](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")*,* [*Instance*](instance.md#keysight.edatoolbox.circuit.Instance "keysight.edatoolbox.circuit.Instance")*]*) – Can either be an existing node and then the list of connections to this Node is given. Alternatively an instance, and then all connections to the Instance are given.

    *property* definitions*: Dict[str, [Definition](#keysight.edatoolbox.circuit.Definition "keysight.edatoolbox.circuit.Definition")]*[](#keysight.edatoolbox.circuit.Definition.definitions "Link to this definition")
    :   Returns a dictionary of instance name to the actual instance

    generate\_netlist()[](#keysight.edatoolbox.circuit.Definition.generate_netlist "Link to this definition")
    :   Generate a netlist for this circuit.

        Parameters:
        :   **variables** (*dict*) – Optionally a dictionary containing as key the variable name and as value the value that should be assigned during netlisting. Variables whose value are not provided
            are taken from the circuit.

    generate\_python(*options=None*) → str[](#keysight.edatoolbox.circuit.Definition.generate_python "Link to this definition")
    :   Generate a Python fragment for this circuit. Cannot handle definitions and instances using them.

        > options: object
        > :   Optional object to control how to generate the Python fragment. The attribute ‘.explicit\_connect’
        >     controls if in the generated Python fragment the list of connections is done at the end or while
        >     generating all the instances.

    import\_netlist(*netlist: str*, *import\_options=None*) → None[](#keysight.edatoolbox.circuit.Definition.import_netlist "Link to this definition")
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

    *property* instances*: Dict[str, [Instance](instance.md#keysight.edatoolbox.circuit.Instance "keysight.edatoolbox.circuit.Instance")]*[](#keysight.edatoolbox.circuit.Definition.instances "Link to this definition")
    :   Returns a dictionary of instance name to the actual instance

    *property* nodes*: List[[Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")]*[](#keysight.edatoolbox.circuit.Definition.nodes "Link to this definition")
    :   Returns the list of nodes of the instance.

    *property* output\_dataset*: str*[](#keysight.edatoolbox.circuit.Definition.output_dataset "Link to this definition")
    :   Controls the name of the output dataset file.

        Notes

        Depending on the format of the string it will instruct the circuit simulator to save the dataset at following location:

        * absolute path –> ‘f:/temp/myoutput’
        * relative path –> ‘myoutput’
        * lcv string –> ‘mylibrary:mycell:mycellview’ –> the output name will be ‘mycell’
        * None –> determined by the instances within the circuit

    *property* parameters*: Dict[str, \_SpectreParameter]*[](#keysight.edatoolbox.circuit.Definition.parameters "Link to this definition")
    :   Returns a dictionary of parameter name to the SpectreParameter’s

    *property* variables*: Dict[str, Var]*[](#keysight.edatoolbox.circuit.Definition.variables "Link to this definition")
    :   Returns a dictionary of variable name to the VAR instance


---

<!-- === 来源: API_Reference/circuit/classes/index.md === -->

# Classes[](#classes "Link to this heading")

* [Circuit](circuit.md)
  + [`Circuit`](circuit.md#keysight.edatoolbox.circuit.Circuit)
    - [`Circuit.GND`](circuit.md#keysight.edatoolbox.circuit.Circuit.GND)
    - [`Circuit.add()`](circuit.md#keysight.edatoolbox.circuit.Circuit.add)
    - [`Circuit.analyses`](circuit.md#keysight.edatoolbox.circuit.Circuit.analyses)
    - [`Circuit.connect()`](circuit.md#keysight.edatoolbox.circuit.Circuit.connect)
    - [`Circuit.connections()`](circuit.md#keysight.edatoolbox.circuit.Circuit.connections)
    - [`Circuit.definitions`](circuit.md#keysight.edatoolbox.circuit.Circuit.definitions)
    - [`Circuit.generate_netlist()`](circuit.md#keysight.edatoolbox.circuit.Circuit.generate_netlist)
    - [`Circuit.generate_python()`](circuit.md#keysight.edatoolbox.circuit.Circuit.generate_python)
    - [`Circuit.import_netlist()`](circuit.md#keysight.edatoolbox.circuit.Circuit.import_netlist)
    - [`Circuit.instances`](circuit.md#keysight.edatoolbox.circuit.Circuit.instances)
    - [`Circuit.output_dataset`](circuit.md#keysight.edatoolbox.circuit.Circuit.output_dataset)
    - [`Circuit.parameters`](circuit.md#keysight.edatoolbox.circuit.Circuit.parameters)
    - [`Circuit.variables`](circuit.md#keysight.edatoolbox.circuit.Circuit.variables)
* [Definition](definition.md)
  + [`Definition`](definition.md#keysight.edatoolbox.circuit.Definition)
    - [`Definition.GND`](definition.md#keysight.edatoolbox.circuit.Definition.GND)
    - [`Definition.add()`](definition.md#keysight.edatoolbox.circuit.Definition.add)
    - [`Definition.analyses`](definition.md#keysight.edatoolbox.circuit.Definition.analyses)
    - [`Definition.connect()`](definition.md#keysight.edatoolbox.circuit.Definition.connect)
    - [`Definition.connections()`](definition.md#keysight.edatoolbox.circuit.Definition.connections)
    - [`Definition.definitions`](definition.md#keysight.edatoolbox.circuit.Definition.definitions)
    - [`Definition.generate_netlist()`](definition.md#keysight.edatoolbox.circuit.Definition.generate_netlist)
    - [`Definition.generate_python()`](definition.md#keysight.edatoolbox.circuit.Definition.generate_python)
    - [`Definition.import_netlist()`](definition.md#keysight.edatoolbox.circuit.Definition.import_netlist)
    - [`Definition.instances`](definition.md#keysight.edatoolbox.circuit.Definition.instances)
    - [`Definition.nodes`](definition.md#keysight.edatoolbox.circuit.Definition.nodes)
    - [`Definition.output_dataset`](definition.md#keysight.edatoolbox.circuit.Definition.output_dataset)
    - [`Definition.parameters`](definition.md#keysight.edatoolbox.circuit.Definition.parameters)
    - [`Definition.variables`](definition.md#keysight.edatoolbox.circuit.Definition.variables)
* [Instance](instance.md)
  + [`Instance`](instance.md#keysight.edatoolbox.circuit.Instance)
    - [`Instance.generate_netlist()`](instance.md#keysight.edatoolbox.circuit.Instance.generate_netlist)
    - [`Instance.nodes`](instance.md#keysight.edatoolbox.circuit.Instance.nodes)
* [Node](node.md)
  + [`Node`](node.md#keysight.edatoolbox.circuit.Node)
* [OptimizationRange](optimization_range.md)
  + [`OptimizationRange`](optimization_range.md#keysight.edatoolbox.circuit.OptimizationRange)
* [TuningRange](tuning_range.md)
  + [`TuningRange`](tuning_range.md#keysight.edatoolbox.circuit.TuningRange)
* [Value](value.md)
  + [`Value`](value.md#keysight.edatoolbox.circuit.Value)


---

<!-- === 来源: API_Reference/circuit/classes/instance.md === -->

# Instance[](#instance "Link to this heading")

*class* keysight.edatoolbox.circuit.Instance(*\*\*kwargs*)[](#keysight.edatoolbox.circuit.Instance "Link to this definition")
:   A generic class representing an instance in a circuit

    generate\_netlist() → str[](#keysight.edatoolbox.circuit.Instance.generate_netlist "Link to this definition")
    :   Generate the netlist of the instance

    *property* nodes*: List[[Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")]*[](#keysight.edatoolbox.circuit.Instance.nodes "Link to this definition")
    :   Returns the list of nodes of the instance.


---

<!-- === 来源: API_Reference/circuit/classes/node.md === -->

# Node[](#node "Link to this heading")

*class* keysight.edatoolbox.circuit.Node(*name=None*, *instance=None*)[](#keysight.edatoolbox.circuit.Node "Link to this definition")
:   A class representing the node of an instance.


---

<!-- === 来源: API_Reference/circuit/classes/optimization_range.md === -->

# OptimizationRange[](#optimizationrange "Link to this heading")

*class* keysight.edatoolbox.circuit.OptimizationRange(*start: float*, *stop: float*, *enabled: bool = True*)[](#keysight.edatoolbox.circuit.OptimizationRange "Link to this definition")


---

<!-- === 来源: API_Reference/circuit/classes/tuning_range.md === -->

# TuningRange[](#tuningrange "Link to this heading")

*class* keysight.edatoolbox.circuit.TuningRange(*start: float*, *stop: float*, *step: float*, *enabled: bool = True*)[](#keysight.edatoolbox.circuit.TuningRange "Link to this definition")


---

<!-- === 来源: API_Reference/circuit/classes/value.md === -->

# Value[](#value "Link to this heading")

*class* keysight.edatoolbox.circuit.Value(*value: float | str*, *optimization: [keysight.edatoolbox.circuit.OptimizationRange](optimization_range.md#keysight.edatoolbox.circuit.OptimizationRange "keysight.edatoolbox.circuit.OptimizationRange") | None = None*, *tuning: [keysight.edatoolbox.circuit.TuningRange](tuning_range.md#keysight.edatoolbox.circuit.TuningRange "keysight.edatoolbox.circuit.TuningRange") | None = None*)[](#keysight.edatoolbox.circuit.Value "Link to this definition")


---

<!-- === 来源: API_Reference/circuit/functions/index.md === -->

# Functions[](#functions "Link to this heading")

keysight.edatoolbox.circuit.convert\_to\_value(*definition: str*) → [Value](../classes/value.md#keysight.edatoolbox.circuit.Value "keysight.edatoolbox.circuit.Value")[](#keysight.edatoolbox.circuit.convert_to_value "Link to this definition")
:   Extract from a textual fragment a Value object that can be assigned to a parameter or be queried to understand
    what the optimization and tuning ranges were assigned to the parameter.


---

<!-- === 来源: API_Reference/circuit/index.md === -->

# Circuit API[](#circuit-api "Link to this heading")

* [Functions](functions/index.md)
  + [`convert_to_value()`](functions/index.md#keysight.edatoolbox.circuit.convert_to_value)
* [Classes](classes/index.md)
  + [Circuit](classes/circuit.md)
    - [`Circuit`](classes/circuit.md#keysight.edatoolbox.circuit.Circuit)
  + [Definition](classes/definition.md)
    - [`Definition`](classes/definition.md#keysight.edatoolbox.circuit.Definition)
  + [Instance](classes/instance.md)
    - [`Instance`](classes/instance.md#keysight.edatoolbox.circuit.Instance)
  + [Node](classes/node.md)
    - [`Node`](classes/node.md#keysight.edatoolbox.circuit.Node)
  + [OptimizationRange](classes/optimization_range.md)
    - [`OptimizationRange`](classes/optimization_range.md#keysight.edatoolbox.circuit.OptimizationRange)
  + [TuningRange](classes/tuning_range.md)
    - [`TuningRange`](classes/tuning_range.md#keysight.edatoolbox.circuit.TuningRange)
  + [Value](classes/value.md)
    - [`Value`](classes/value.md#keysight.edatoolbox.circuit.Value)


---

<!-- === 来源: API_Reference/dataset/index.md === -->

# Dataset[](#dataset "Link to this heading")

*class* keysight.edatoolbox.dataset.Dataset[](#keysight.edatoolbox.dataset.Dataset "Link to this definition")
:   Dataset is an alias for either keysight.edatoolbox.dataset.Dataset\_DsDump or keysight.edatoolbox.dataset.Dataset\_AdsDataset. Depending on whether
    the keysight.dataset functionality can be loaded from ADS, it will choose either implementation. The keysight.dataset based one is the most performant and complete.

*class* keysight.edatoolbox.dataset.Dataset\_DsDump(*filename=''*)[](#keysight.edatoolbox.dataset.Dataset_DsDump "Link to this definition")
:   Class to query ADS dataset files. Internally it will use a dsdump approach and parse the contents. This implementation only supports 1 independent variable.

    *class* VariableBlock(*name: str*, *ivar\_names: List[str]*, *dvar\_names: List[str]*, *values: list*)[](#keysight.edatoolbox.dataset.Dataset_DsDump.VariableBlock "Link to this definition")

    dvar\_names(*varblock: str*) → List[str][](#keysight.edatoolbox.dataset.Dataset_DsDump.dvar_names "Link to this definition")
    :   Returns the list of names of dependent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    dvar\_values(*varblock: str*, *var: str*)[](#keysight.edatoolbox.dataset.Dataset_DsDump.dvar_values "Link to this definition")
    :   Returns the values of the specified dependent variable.

        Parameters:
        :   * **varblock** (*str*) – The variable block
            * **var** (*str*) – The variable name

    ivar\_names(*varblock: str*)[](#keysight.edatoolbox.dataset.Dataset_DsDump.ivar_names "Link to this definition")
    :   Returns the list of names of independent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    ivar\_values(*varblock: str*, *var: str*) → List[str][](#keysight.edatoolbox.dataset.Dataset_DsDump.ivar_values "Link to this definition")
    :   Returns the values of the independent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    to\_dataframe(*varblock: str*)[](#keysight.edatoolbox.dataset.Dataset_DsDump.to_dataframe "Link to this definition")
    :   Converts the chosen varblock into a Pandas dataframe

        Parameters:
        :   **varblock** (*str*) – Name of the varblock to convert.

    values(*varblock: str*, *var: str*)[](#keysight.edatoolbox.dataset.Dataset_DsDump.values "Link to this definition")
    :   Returns the values of either the independent or dependent variables in the specified variable block. Gives precedence
        to dependent variable names over independents in the lookup.

        Parameters:
        :   **varblock** (*str*) – The variable block

*class* keysight.edatoolbox.dataset.Dataset\_AdsDataset(*filename: str = ''*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset "Link to this definition")
:   Class to query ADS dataset files. Internally it will use the keysight.dataset module. This implementation is automatically selected when it is available. It is the most
    performant and complete implementation.

    dvar\_names(*varblock: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.dvar_names "Link to this definition")
    :   Returns the list of names of dependent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    dvar\_values(*varblock: str*, *var: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.dvar_values "Link to this definition")
    :   Returns the values of the specified dependent variable.

        Parameters:
        :   * **varblock** (*str*) – The variable block
            * **var** (*str*) – The variable name

    ivar\_names(*varblock: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.ivar_names "Link to this definition")
    :   Returns the list of names of independent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    ivar\_values(*varblock: str*, *var: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.ivar_values "Link to this definition")
    :   Returns the values of the independent variables in the specified variable block.

        Parameters:
        :   **varblock** (*str*) – The variable block

    to\_dataframe(*varblock: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.to_dataframe "Link to this definition")
    :   Converts the chosen varblock into a Pandas dataframe

        Parameters:
        :   **varblock** (*str*) – Name of the varblock to convert.

    values(*varblock: str*, *var: str*)[](#keysight.edatoolbox.dataset.Dataset_AdsDataset.values "Link to this definition")
    :   Returns the values of either the independent or dependent variables in the specified variable block. Gives precedence
        to dependent variable names over independents in the lookup.

        Parameters:
        :   **varblock** (*str*) – The variable block


---

<!-- === 来源: API_Reference/extra/empro/index.md === -->

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


---

<!-- === 来源: API_Reference/extra/index.md === -->

# External API[](#external-api "Link to this heading")

* [empro.analysis](empro/index.md)
  + [`empro.analysis.Analysis`](empro/index.md#empro.analysis.Analysis)
    - [`empro.analysis.Analysis.analysisType`](empro/index.md#empro.analysis.Analysis.analysisType)
    - [`empro.analysis.Analysis.componentModelGroups`](empro/index.md#empro.analysis.Analysis.componentModelGroups)
    - [`empro.analysis.Analysis.name`](empro/index.md#empro.analysis.Analysis.name)
    - [`empro.analysis.Analysis.nets`](empro/index.md#empro.analysis.Analysis.nets)
    - [`empro.analysis.Analysis.ports`](empro/index.md#empro.analysis.Analysis.ports)
    - [`empro.analysis.Analysis.requiredNets()`](empro/index.md#empro.analysis.Analysis.requiredNets)
    - [`empro.analysis.Analysis.sinks`](empro/index.md#empro.analysis.Analysis.sinks)
    - [`empro.analysis.Analysis.vrms`](empro/index.md#empro.analysis.Analysis.vrms)
    - [`empro.analysis.Analysis.isValid()`](empro/index.md#empro.analysis.Analysis.isValid)
    - [`empro.analysis.Analysis.reasonWhyInvalid()`](empro/index.md#empro.analysis.Analysis.reasonWhyInvalid)
  + [`empro.analysis.ComponentModelGroupList`](empro/index.md#empro.analysis.ComponentModelGroupList)


---

<!-- === 来源: API_Reference/index.md === -->

# API Reference[](#api-reference "Link to this heading")

* [ADS](ads/index.md)
  + [Functions](ads/functions/index.md)
  + [Classes](ads/classes/index.md)
* [Circuit API](circuit/index.md)
  + [Functions](circuit/functions/index.md)
  + [Classes](circuit/classes/index.md)
* [Dataset](dataset/index.md)
  + [`keysight.edatoolbox.dataset.Dataset`](dataset/index.md#keysight.edatoolbox.dataset.Dataset)
  + [`Dataset_DsDump`](dataset/index.md#keysight.edatoolbox.dataset.Dataset_DsDump)
  + [`Dataset_AdsDataset`](dataset/index.md#keysight.edatoolbox.dataset.Dataset_AdsDataset)
* [External API](extra/index.md)
  + [empro.analysis](extra/empro/index.md)
* [Multi Python API](multi_python/index.md)
  + [Functions](multi_python/functions/index.md)
* [xxPro](xxpro/index.md)
  + [`XXProNotFound`](xxpro/index.md#keysight.edatoolbox.xxpro.XXProNotFound)
  + [`get_python_xxpro_location()`](xxpro/index.md#keysight.edatoolbox.xxpro.get_python_xxpro_location)
  + [`get_xxpro_location()`](xxpro/index.md#keysight.edatoolbox.xxpro.get_xxpro_location)
  + [`load_pro_view()`](xxpro/index.md#keysight.edatoolbox.xxpro.load_pro_view)
  + [`use_workspace()`](xxpro/index.md#keysight.edatoolbox.xxpro.use_workspace)


---

<!-- === 来源: API_Reference/multi_python/functions/index.md === -->

# Functions[](#functions "Link to this heading")

keysight.edatoolbox.multi\_python.xxpro\_context(*python\_xxpro\_location=None*)[](#keysight.edatoolbox.multi_python.xxpro_context "Link to this definition")
:   Create a context manager that will yield an object to which functions can be sent to be executed in a separate process with the Python version of EMPro/RFPro/SIPro.

    Args:
    :   python\_xxpro\_location (str): The location of the Python executable to use for xxPro (=directory, not the location to the executable).
        :   If not provided, the default Python executable for xxPro will be used

    Usage:

    ```
    >>> with xxpro_context() as caller:
    ...     result = caller.call(my_function, args=[1,2], kwargs={'a':3})
    ```

keysight.edatoolbox.multi\_python.ads\_context(*python\_ads\_location=None*)[](#keysight.edatoolbox.multi_python.ads_context "Link to this definition")
:   Create a context manager that will yield an object to which functions can be sent to be executed in a separate process with the Python version of ADS.

    Args:
    :   python\_ads\_location (str): The location of the Python executable to use for ADS (=directory, not the location to the executable).
        :   If not provided, the default Python executable for ADS will be used.

    Usage:

    ```
    >>> with ads_context() as caller:
    ...     result = caller.call(my_function, args=[1,2], kwargs={'a':3})
    ```


---

<!-- === 来源: API_Reference/multi_python/index.md === -->

# Multi Python API[](#multi-python-api "Link to this heading")

The multi\_python module provides the ability to run multiple Python versions in the same process. This is useful when you need to run both ADS and xxPro in the same Python session.
When you use the multi\_python module, a context for each Python version you want to run a given function in needs to be provided. Once a context is created it is alive until
the context is deleted.

To use the multi\_python module in combination with ADS and xxPro, the EDA Toolbox needs to be installed in the target environment and needs to be sufficiently recent. The EDA Toolbox multi\_python
does detect if that is the case and when it is not, it will raise an exception.

An example of how to use the multi\_python module is shown below:

```
import keysight.edatoolbox.multi_python as mp

def hello_from_xxpro():
    print("Hello from xxPro")
    return 1

def hello_from_ads():
    print("Hello from ADS")
    return 2

with mp.xxpro_context() as xxpro:
    r = xxpro.call(hello_from_xxpro)
    print(r)

with mp.ads_context() as ads:
    r = ads.call(hello_from_ads)
    print(r)
```

* [Functions](functions/index.md)
  + [`xxpro_context()`](functions/index.md#keysight.edatoolbox.multi_python.xxpro_context)
  + [`ads_context()`](functions/index.md#keysight.edatoolbox.multi_python.ads_context)


---

<!-- === 来源: API_Reference/xxpro/index.md === -->

# xxPro[](#module-keysight.edatoolbox.xxpro "Link to this heading")

*exception* keysight.edatoolbox.xxpro.XXProNotFound[](#keysight.edatoolbox.xxpro.XXProNotFound "Link to this definition")
:   Raise if cannot find SI/PI/RFPro.

keysight.edatoolbox.xxpro.get\_python\_xxpro\_location(*from\_ads=True*) → str[](#keysight.edatoolbox.xxpro.get_python_xxpro_location "Link to this definition")
:   Returns the location of the python installed with xxPro.

    Parameters:
    :   **from\_ads** (*bool**,* *default=True*) – If True get xxPro from ADS install folder, otherwise look for EMPROHOME environment variable.

keysight.edatoolbox.xxpro.get\_xxpro\_location(*from\_ads=True*) → str[](#keysight.edatoolbox.xxpro.get_xxpro_location "Link to this definition")
:   Returns the location of the latest installed xxPro.

    Parameters:
    :   **from\_ads** (*bool**,* *default=True*) – If True get xxPro from ADS install folder, otherwise look for EMPROHOME environment variable.

keysight.edatoolbox.xxpro.load\_pro\_view(*xxpro\_lcv: LibraryCellView*)[](#keysight.edatoolbox.xxpro.load_pro_view "Link to this definition")
:   Load an xxpro LibraryCellView into the empro.activeProject.

    Parameters:
    :   **xxpro\_lcv** (*LibraryCellView*) – An xxpro LibraryCellView object.

    Raises:
    :   **ImportError** – Failed to import empro module.

keysight.edatoolbox.xxpro.use\_workspace(*workspace: str*)[](#keysight.edatoolbox.xxpro.use_workspace "Link to this definition")
:   Tell xxpro what workspace to use.

    Parameters:
    :   **workspace** (*str*) – The full path of the workspace.


---

