# EDA Toolbox API Documentation Knowledge Base
> 本文件由 MarkItDown 自动转换，BFS 遍历自 Keysight ADS2025 Update 2 EDA Toolbox API Documentation HTML 文档。
> 共 34 个页面。

---

## 目录 (Table of Contents)

1. [index.md](#index)
2. [API_Reference\index.md](#api_reference--index)
3. [API_Reference\ads\index.md](#api_reference--ads--index)
4. [API_Reference\ads\functions\index.md](#api_reference--ads--functions--index)
5. [API_Reference\ads\classes\index.md](#api_reference--ads--classes--index)
6. [API_Reference\ads\classes\ads.md](#api_reference--ads--classes--ads)
7. [API_Reference\ads\classes\circuit_simulator.md](#api_reference--ads--classes--circuit_simulator)
8. [API_Reference\circuit\index.md](#api_reference--circuit--index)
9. [API_Reference\circuit\functions\index.md](#api_reference--circuit--functions--index)
10. [API_Reference\circuit\classes\index.md](#api_reference--circuit--classes--index)
11. [API_Reference\circuit\classes\circuit.md](#api_reference--circuit--classes--circuit)
12. [API_Reference\circuit\classes\definition.md](#api_reference--circuit--classes--definition)
13. [API_Reference\circuit\classes\instance.md](#api_reference--circuit--classes--instance)
14. [API_Reference\circuit\classes\node.md](#api_reference--circuit--classes--node)
15. [API_Reference\circuit\classes\optimization_range.md](#api_reference--circuit--classes--optimization_range)
16. [API_Reference\circuit\classes\tuning_range.md](#api_reference--circuit--classes--tuning_range)
17. [API_Reference\circuit\classes\value.md](#api_reference--circuit--classes--value)
18. [API_Reference\dataset\index.md](#api_reference--dataset--index)
19. [API_Reference\extra\index.md](#api_reference--extra--index)
20. [API_Reference\extra\empro\index.md](#api_reference--extra--empro--index)
21. [API_Reference\multi_python\index.md](#api_reference--multi_python--index)
22. [API_Reference\multi_python\functions\index.md](#api_reference--multi_python--functions--index)
23. [API_Reference\xxpro\index.md](#api_reference--xxpro--index)
24. [Initial_Setup\index.md](#initial_setup--index)
25. [Initial_Setup\installation.md](#initial_setup--installation)
26. [Initial_Setup\prerequisites.md](#initial_setup--prerequisites)
27. [Initial_Setup\verifying.md](#initial_setup--verifying)
28. [Initial_Setup\ssh.md](#initial_setup--ssh)
29. [Examples\index.md](#examples--index)
30. [How-To\index.md](#how-to--index)
31. [How-To\circuit.md](#how-to--circuit)
32. [How-To\circuit_sim.md](#how-to--circuit_sim)
33. [How-To\sipro.md](#how-to--sipro)
34. [release_notes\index.md](#release_notes--index)

---



---

## 1. index.md {#index}

# EDA Toolbox API Documentation[](#eda-toolbox-api-documentation "Link to this heading")

Welcome to the EDA Toolbox API documentation. The EDA Toolbox is a set of Python functionality that helps drive Keysight (EDA) tools from Python. The EDA Toolbox helps drive all tools from Python, including for products
that may not have a fully developed Python API yet. The EDA Toolbox does this for ADS/EMPro/SystemVue/VSA, either through adding a thin wrapper on top of the products or providing examples on how to actually do it.
The EDA Toolbox includes an API to work with circuits through netlists, creating and modify circuits.

* [API Reference](API_Reference/index.md)
  + [ADS](API_Reference/ads/index.md)
    - [Functions](API_Reference/ads/functions/index.md)
      * [`get_ads_location()`](API_Reference/ads/functions/index.md#keysight.edatoolbox.ads.get_ads_location)
    - [Classes](API_Reference/ads/classes/index.md)
      * [ADS](API_Reference/ads/classes/ads.md)
        + [`ADS`](API_Reference/ads/classes/ads.md#keysight.edatoolbox.ads.ADS)
          - [`ADS.archive_workspace()`](API_Reference/ads/classes/ads.md#keysight.edatoolbox.ads.ADS.archive_workspace)
          - [`ADS.copy_cellview()`](API_Reference/ads/classes/ads.md#keysight.edatoolbox.ads.ADS.copy_cellview)
          - [`ADS.create_pro_view()`](API_Reference/ads/classes/ads.md#keysight.edatoolbox.ads.ADS.create_pro_view)
          - [`ADS.create_workspace()`](API_Reference/ads/classes/ads.md#keysight.edatoolbox.ads.ADS.create_workspace)
          - [`ADS.generate_netlist()`](API_Reference/ads/classes/ads.md#keysight.edatoolbox.ads.ADS.generate_netlist)
          - [`ADS.import_brd()`](API_Reference/ads/classes/ads.md#keysight.edatoolbox.ads.ADS.import_brd)
          - [`ADS.import_ipc2581()`](API_Reference/ads/classes/ads.md#keysight.edatoolbox.ads.ADS.import_ipc2581)
          - [`ADS.import_odbpp()`](API_Reference/ads/classes/ads.md#keysight.edatoolbox.ads.ADS.import_odbpp)
          - [`ADS.unarchive_workspace()`](API_Reference/ads/classes/ads.md#keysight.edatoolbox.ads.ADS.unarchive_workspace)
      * [CircuitSimulator](API_Reference/ads/classes/circuit_simulator.md)
        + [`CircuitSimulator`](API_Reference/ads/classes/circuit_simulator.md#keysight.edatoolbox.ads.CircuitSimulator)
          - [`CircuitSimulator.run()`](API_Reference/ads/classes/circuit_simulator.md#keysight.edatoolbox.ads.CircuitSimulator.run)
          - [`CircuitSimulator.run_netlist()`](API_Reference/ads/classes/circuit_simulator.md#keysight.edatoolbox.ads.CircuitSimulator.run_netlist)
  + [Circuit API](API_Reference/circuit/index.md)
    - [Functions](API_Reference/circuit/functions/index.md)
      * [`convert_to_value()`](API_Reference/circuit/functions/index.md#keysight.edatoolbox.circuit.convert_to_value)
    - [Classes](API_Reference/circuit/classes/index.md)
      * [Circuit](API_Reference/circuit/classes/circuit.md)
        + [`Circuit`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit)
          - [`Circuit.GND`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.GND)
          - [`Circuit.add()`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.add)
          - [`Circuit.analyses`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.analyses)
          - [`Circuit.connect()`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.connect)
          - [`Circuit.connections()`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.connections)
          - [`Circuit.definitions`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.definitions)
          - [`Circuit.generate_netlist()`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.generate_netlist)
          - [`Circuit.generate_python()`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.generate_python)
          - [`Circuit.import_netlist()`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.import_netlist)
          - [`Circuit.instances`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.instances)
          - [`Circuit.output_dataset`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.output_dataset)
          - [`Circuit.parameters`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.parameters)
          - [`Circuit.variables`](API_Reference/circuit/classes/circuit.md#keysight.edatoolbox.circuit.Circuit.variables)
      * [Definition](API_Reference/circuit/classes/definition.md)
        + [`Definition`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition)
          - [`Definition.GND`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.GND)
          - [`Definition.add()`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.add)
          - [`Definition.analyses`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.analyses)
          - [`Definition.connect()`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.connect)
          - [`Definition.connections()`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.connections)
          - [`Definition.definitions`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.definitions)
          - [`Definition.generate_netlist()`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.generate_netlist)
          - [`Definition.generate_python()`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.generate_python)
          - [`Definition.import_netlist()`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.import_netlist)
          - [`Definition.instances`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.instances)
          - [`Definition.nodes`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.nodes)
          - [`Definition.output_dataset`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.output_dataset)
          - [`Definition.parameters`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.parameters)
          - [`Definition.variables`](API_Reference/circuit/classes/definition.md#keysight.edatoolbox.circuit.Definition.variables)
      * [Instance](API_Reference/circuit/classes/instance.md)
        + [`Instance`](API_Reference/circuit/classes/instance.md#keysight.edatoolbox.circuit.Instance)
          - [`Instance.generate_netlist()`](API_Reference/circuit/classes/instance.md#keysight.edatoolbox.circuit.Instance.generate_netlist)
          - [`Instance.nodes`](API_Reference/circuit/classes/instance.md#keysight.edatoolbox.circuit.Instance.nodes)
      * [Node](API_Reference/circuit/classes/node.md)
        + [`Node`](API_Reference/circuit/classes/node.md#keysight.edatoolbox.circuit.Node)
      * [OptimizationRange](API_Reference/circuit/classes/optimization_range.md)
        + [`OptimizationRange`](API_Reference/circuit/classes/optimization_range.md#keysight.edatoolbox.circuit.OptimizationRange)
      * [TuningRange](API_Reference/circuit/classes/tuning_range.md)
        + [`TuningRange`](API_Reference/circuit/classes/tuning_range.md#keysight.edatoolbox.circuit.TuningRange)
      * [Value](API_Reference/circuit/classes/value.md)
        + [`Value`](API_Reference/circuit/classes/value.md#keysight.edatoolbox.circuit.Value)
  + [Dataset](API_Reference/dataset/index.md)
    - [`keysight.edatoolbox.dataset.Dataset`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset)
    - [`Dataset_DsDump`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_DsDump)
      * [`Dataset_DsDump.VariableBlock`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_DsDump.VariableBlock)
      * [`Dataset_DsDump.dvar_names()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_DsDump.dvar_names)
      * [`Dataset_DsDump.dvar_values()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_DsDump.dvar_values)
      * [`Dataset_DsDump.ivar_names()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_DsDump.ivar_names)
      * [`Dataset_DsDump.ivar_values()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_DsDump.ivar_values)
      * [`Dataset_DsDump.to_dataframe()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_DsDump.to_dataframe)
      * [`Dataset_DsDump.values()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_DsDump.values)
    - [`Dataset_AdsDataset`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_AdsDataset)
      * [`Dataset_AdsDataset.dvar_names()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_AdsDataset.dvar_names)
      * [`Dataset_AdsDataset.dvar_values()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_AdsDataset.dvar_values)
      * [`Dataset_AdsDataset.ivar_names()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_AdsDataset.ivar_names)
      * [`Dataset_AdsDataset.ivar_values()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_AdsDataset.ivar_values)
      * [`Dataset_AdsDataset.to_dataframe()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_AdsDataset.to_dataframe)
      * [`Dataset_AdsDataset.values()`](API_Reference/dataset/index.md#keysight.edatoolbox.dataset.Dataset_AdsDataset.values)
  + [External API](API_Reference/extra/index.md)
    - [empro.analysis](API_Reference/extra/empro/index.md)
      * [`empro.analysis.Analysis`](API_Reference/extra/empro/index.md#empro.analysis.Analysis)
        + [`empro.analysis.Analysis.analysisType`](API_Reference/extra/empro/index.md#empro.analysis.Analysis.analysisType)
        + [`empro.analysis.Analysis.componentModelGroups`](API_Reference/extra/empro/index.md#empro.analysis.Analysis.componentModelGroups)
        + [`empro.analysis.Analysis.name`](API_Reference/extra/empro/index.md#empro.analysis.Analysis.name)
        + [`empro.analysis.Analysis.nets`](API_Reference/extra/empro/index.md#empro.analysis.Analysis.nets)
        + [`empro.analysis.Analysis.ports`](API_Reference/extra/empro/index.md#empro.analysis.Analysis.ports)
        + [`empro.analysis.Analysis.requiredNets()`](API_Reference/extra/empro/index.md#empro.analysis.Analysis.requiredNets)
        + [`empro.analysis.Analysis.sinks`](API_Reference/extra/empro/index.md#empro.analysis.Analysis.sinks)
        + [`empro.analysis.Analysis.vrms`](API_Reference/extra/empro/index.md#empro.analysis.Analysis.vrms)
        + [`empro.analysis.Analysis.isValid()`](API_Reference/extra/empro/index.md#empro.analysis.Analysis.isValid)
        + [`empro.analysis.Analysis.reasonWhyInvalid()`](API_Reference/extra/empro/index.md#empro.analysis.Analysis.reasonWhyInvalid)
      * [`empro.analysis.ComponentModelGroupList`](API_Reference/extra/empro/index.md#empro.analysis.ComponentModelGroupList)
  + [Multi Python API](API_Reference/multi_python/index.md)
    - [Functions](API_Reference/multi_python/functions/index.md)
      * [`xxpro_context()`](API_Reference/multi_python/functions/index.md#keysight.edatoolbox.multi_python.xxpro_context)
      * [`ads_context()`](API_Reference/multi_python/functions/index.md#keysight.edatoolbox.multi_python.ads_context)
  + [xxPro](API_Reference/xxpro/index.md)
    - [`XXProNotFound`](API_Reference/xxpro/index.md#keysight.edatoolbox.xxpro.XXProNotFound)
    - [`get_python_xxpro_location()`](API_Reference/xxpro/index.md#keysight.edatoolbox.xxpro.get_python_xxpro_location)
    - [`get_xxpro_location()`](API_Reference/xxpro/index.md#keysight.edatoolbox.xxpro.get_xxpro_location)
    - [`load_pro_view()`](API_Reference/xxpro/index.md#keysight.edatoolbox.xxpro.load_pro_view)
    - [`use_workspace()`](API_Reference/xxpro/index.md#keysight.edatoolbox.xxpro.use_workspace)
* [Initial Setup](Initial_Setup/index.md)
  + [Installation](Initial_Setup/installation.md)
    - [Installing in xxPro distribution](Initial_Setup/installation.md#installing-in-xxpro-distribution)
      * [Examples](Initial_Setup/installation.md#examples)
  + [Prerequisites](Initial_Setup/prerequisites.md)
    - [EDA Toolbox + Circuit simulation](Initial_Setup/prerequisites.md#eda-toolbox-circuit-simulation)
    - [EDA Toolbox + xxPro simulation](Initial_Setup/prerequisites.md#eda-toolbox-xxpro-simulation)
    - [EDA Toolbox + other](Initial_Setup/prerequisites.md#eda-toolbox-other)
  + [Verifying Installation](Initial_Setup/verifying.md)
    - [Base installation](Initial_Setup/verifying.md#base-installation)
    - [Modules used in examples](Initial_Setup/verifying.md#modules-used-in-examples)
      * [Matplotlib, Numpy, Pandas, Scipy](Initial_Setup/verifying.md#matplotlib-numpy-pandas-scipy)
      * [Seaborn](Initial_Setup/verifying.md#seaborn)
      * [PathWave Datatools](Initial_Setup/verifying.md#pathwave-datatools)
  + [SSH](Initial_Setup/ssh.md)
* [Examples](Examples/index.md)
  + [Get the example workspaces](Examples/index.md#get-the-example-workspaces)
  + [Running the examples](Examples/index.md#running-the-examples)
* [How-To](How-To/index.md)
  + [Create a Circuit](How-To/circuit.md)
    - [Step 0: Getting ready](How-To/circuit.md#step-0-getting-ready)
    - [Step 1: Adding the components](How-To/circuit.md#step-1-adding-the-components)
    - [Step 2: Connecting the instances](How-To/circuit.md#step-2-connecting-the-instances)
    - [Step 3: Analysis?](How-To/circuit.md#step-3-analysis)
    - [Step 4: Run the simulation](How-To/circuit.md#step-4-run-the-simulation)
    - [Step 5: Extracting and plotting results](How-To/circuit.md#step-5-extracting-and-plotting-results)
  + [Run a Circuit Simulation](How-To/circuit_sim.md)
    - [Step 0: Get the example workspaces](How-To/circuit_sim.md#step-0-get-the-example-workspaces)
    - [Step 1: Creating the ADS application object](How-To/circuit_sim.md#step-1-creating-the-ads-application-object)
    - [Step 2: Unarchiving](How-To/circuit_sim.md#step-2-unarchiving)
    - [Step 3: Generating the netlist](How-To/circuit_sim.md#step-3-generating-the-netlist)
    - [Step 4: Working the circuit](How-To/circuit_sim.md#step-4-working-the-circuit)
    - [Step 5: Run the simulation](How-To/circuit_sim.md#step-5-run-the-simulation)
    - [Step 6: Extract the results](How-To/circuit_sim.md#step-6-extract-the-results)
  + [Create SIPro View and Run Simulation](How-To/sipro.md)
    - [Step 0: Get the example workspaces](How-To/sipro.md#step-0-get-the-example-workspaces)
    - [Step 1: Creating the ADS application object](How-To/sipro.md#step-1-creating-the-ads-application-object)
    - [Step 2: Unarchiving](How-To/sipro.md#step-2-unarchiving)
    - [Step 3: Creating the SIPro view](How-To/sipro.md#step-3-creating-the-sipro-view)
    - [Step 4: Loading the SIPro view into the SIPro tool](How-To/sipro.md#step-4-loading-the-sipro-view-into-the-sipro-tool)
    - [Step 5: Creating an Analysis](How-To/sipro.md#step-5-creating-an-analysis)
    - [Step 6: Running an Analysis](How-To/sipro.md#step-6-running-an-analysis)
    - [Step 7: Extracting some results](How-To/sipro.md#step-7-extracting-some-results)
* [Release Notes](release_notes/index.md)
  + [1.2.4](release_notes/index.md#id1)
  + [1.2.3](release_notes/index.md#id2)
  + [1.2.2](release_notes/index.md#id3)
  + [1.2.1](release_notes/index.md#id4)
  + [1.1.6](release_notes/index.md#id5)
  + [1.1.5](release_notes/index.md#id6)
  + [1.1.4](release_notes/index.md#id7)
  + [1.1.3](release_notes/index.md#id8)
  + [1.1.2](release_notes/index.md#id9)
  + [1.0.1](release_notes/index.md#id10)
  + [1.0.0](release_notes/index.md#id11)
  + [0.0.8](release_notes/index.md#id12)
  + [0.0.7](release_notes/index.md#id13)
  + [0.0.6](release_notes/index.md#id14)
  + [0.0.5](release_notes/index.md#id15)
  + [0.0.4](release_notes/index.md#id16)
  + [0.0.3](release_notes/index.md#id17)

# Indices and tables[](#indices-and-tables "Link to this heading")

* [Index](genindex.md)
* [Module Index](py-modindex.md)
* [Search Page](search.md)


---

## 2. API_Reference\index.md {#api_reference--index}

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

## 3. API_Reference\ads\index.md {#api_reference--ads--index}

# ADS[](#ads "Link to this heading")

* [Functions](functions/index.md)
  + [`get_ads_location()`](functions/index.md#keysight.edatoolbox.ads.get_ads_location)
* [Classes](classes/index.md)
  + [ADS](classes/ads.md)
    - [`ADS`](classes/ads.md#keysight.edatoolbox.ads.ADS)
  + [CircuitSimulator](classes/circuit_simulator.md)
    - [`CircuitSimulator`](classes/circuit_simulator.md#keysight.edatoolbox.ads.CircuitSimulator)


---

## 4. API_Reference\ads\functions\index.md {#api_reference--ads--functions--index}

# Functions[](#functions "Link to this heading")

keysight.edatoolbox.ads.get\_ads\_location() → str[](#keysight.edatoolbox.ads.get_ads_location "Link to this definition")
:   Returns the location of the latest installed ADS.


---

## 5. API_Reference\ads\classes\index.md {#api_reference--ads--classes--index}

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

## 6. API_Reference\ads\classes\ads.md {#api_reference--ads--classes--ads}

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

    create\_pro\_view(*workspace: str*, *input\_lcv: LibraryCellView*, *substrate: str*, *pro\_lcv: str*, *tool: str*)[](#keysight.edatoolbox.ads.ADS.create_pro_view "Link to this definition")
    :   Create an SI/PE/RF/Quantumpro view from an existing workspace.

        Parameters:
        :   * **workspace** (*str*) – Path to an existing workspace.
            * **input\_lcv** (*LibraryCellView*) – Input LibraryCellView.
            * **pro\_lcv** (*LibraryCellView*) – Output LibraryCellView.
            * **tool** (*str*) – Tool to create the new view, options: “rfpro”|”pepro”|”sipi”|”quantumpro”.
            * **substrate** (*str*) – String containing the substrate name, without the .subst suffix.

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

    import\_odbpp(*workspace: str*, *tgzFile: str*, *library: str*, *cell: str = None*, *use\_legacy\_importer=True*)[](#keysight.edatoolbox.ads.ADS.import_odbpp "Link to this definition")
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

## 7. API_Reference\ads\classes\circuit_simulator.md {#api_reference--ads--classes--circuit_simulator}

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

## 8. API_Reference\circuit\index.md {#api_reference--circuit--index}

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

## 9. API_Reference\circuit\functions\index.md {#api_reference--circuit--functions--index}

# Functions[](#functions "Link to this heading")

keysight.edatoolbox.circuit.convert\_to\_value(*definition: str*) → [Value](../classes/value.md#keysight.edatoolbox.circuit.Value "keysight.edatoolbox.circuit.Value")[](#keysight.edatoolbox.circuit.convert_to_value "Link to this definition")
:   Extract from a textual fragment a Value object that can be assigned to a parameter or be queried to understand
    what the optimization and tuning ranges were assigned to the parameter.


---

## 10. API_Reference\circuit\classes\index.md {#api_reference--circuit--classes--index}

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

## 11. API_Reference\circuit\classes\circuit.md {#api_reference--circuit--classes--circuit}

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

## 12. API_Reference\circuit\classes\definition.md {#api_reference--circuit--classes--definition}

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

## 13. API_Reference\circuit\classes\instance.md {#api_reference--circuit--classes--instance}

# Instance[](#instance "Link to this heading")

*class* keysight.edatoolbox.circuit.Instance(*\*\*kwargs*)[](#keysight.edatoolbox.circuit.Instance "Link to this definition")
:   A generic class representing an instance in a circuit

    generate\_netlist() → str[](#keysight.edatoolbox.circuit.Instance.generate_netlist "Link to this definition")
    :   Generate the netlist of the instance

    *property* nodes*: List[[Node](node.md#keysight.edatoolbox.circuit.Node "keysight.edatoolbox.circuit.Node")]*[](#keysight.edatoolbox.circuit.Instance.nodes "Link to this definition")
    :   Returns the list of nodes of the instance.


---

## 14. API_Reference\circuit\classes\node.md {#api_reference--circuit--classes--node}

# Node[](#node "Link to this heading")

*class* keysight.edatoolbox.circuit.Node(*name=None*, *instance=None*)[](#keysight.edatoolbox.circuit.Node "Link to this definition")
:   A class representing the node of an instance.


---

## 15. API_Reference\circuit\classes\optimization_range.md {#api_reference--circuit--classes--optimization_range}

# OptimizationRange[](#optimizationrange "Link to this heading")

*class* keysight.edatoolbox.circuit.OptimizationRange(*start: float*, *stop: float*, *enabled: bool = True*)[](#keysight.edatoolbox.circuit.OptimizationRange "Link to this definition")


---

## 16. API_Reference\circuit\classes\tuning_range.md {#api_reference--circuit--classes--tuning_range}

# TuningRange[](#tuningrange "Link to this heading")

*class* keysight.edatoolbox.circuit.TuningRange(*start: float*, *stop: float*, *step: float*, *enabled: bool = True*)[](#keysight.edatoolbox.circuit.TuningRange "Link to this definition")


---

## 17. API_Reference\circuit\classes\value.md {#api_reference--circuit--classes--value}

# Value[](#value "Link to this heading")

*class* keysight.edatoolbox.circuit.Value(*value: float | str*, *optimization: [keysight.edatoolbox.circuit.OptimizationRange](optimization_range.md#keysight.edatoolbox.circuit.OptimizationRange "keysight.edatoolbox.circuit.OptimizationRange") | None = None*, *tuning: [keysight.edatoolbox.circuit.TuningRange](tuning_range.md#keysight.edatoolbox.circuit.TuningRange "keysight.edatoolbox.circuit.TuningRange") | None = None*)[](#keysight.edatoolbox.circuit.Value "Link to this definition")


---

## 18. API_Reference\dataset\index.md {#api_reference--dataset--index}

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

## 19. API_Reference\extra\index.md {#api_reference--extra--index}

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

## 20. API_Reference\extra\empro\index.md {#api_reference--extra--empro--index}

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

## 21. API_Reference\multi_python\index.md {#api_reference--multi_python--index}

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

## 22. API_Reference\multi_python\functions\index.md {#api_reference--multi_python--functions--index}

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

## 23. API_Reference\xxpro\index.md {#api_reference--xxpro--index}

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

## 24. Initial_Setup\index.md {#initial_setup--index}

# Initial Setup[](#initial-setup "Link to this heading")

* [Installation](installation.md)
  + [Installing in xxPro distribution](installation.md#installing-in-xxpro-distribution)
    - [Examples](installation.md#examples)
* [Prerequisites](prerequisites.md)
  + [EDA Toolbox + Circuit simulation](prerequisites.md#eda-toolbox-circuit-simulation)
  + [EDA Toolbox + xxPro simulation](prerequisites.md#eda-toolbox-xxpro-simulation)
  + [EDA Toolbox + other](prerequisites.md#eda-toolbox-other)
* [Verifying Installation](verifying.md)
  + [Base installation](verifying.md#base-installation)
  + [Modules used in examples](verifying.md#modules-used-in-examples)
    - [Matplotlib, Numpy, Pandas, Scipy](verifying.md#matplotlib-numpy-pandas-scipy)
    - [Seaborn](verifying.md#seaborn)
    - [PathWave Datatools](verifying.md#pathwave-datatools)
* [SSH](ssh.md)


---

## 25. Initial_Setup\installation.md {#initial_setup--installation}

# Installation[](#installation "Link to this heading")

These instructions describe how to use `pip` to install the EDA Toolbox.

Warning

These instructions assume you are using a standard Python distribution from [python.org](https://www.python.org). Python 3.10.x is the recommended installation to use.

On Linux:

```
pip install /path/to/wheelfile/keysight.edatoolbox-1.2.1-py3-none-any.whl
```

On Windows, Python is often installed through `py` allowing to select a particular version and acts as jump station to the various Python installation available on the system.

```
py -m pip install c:\path\to\wheelfile\keysight.edatoolbox-1.2.s1-py3-none-any.whl
```

The wheel files can be downloaded here: [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

## Installing in xxPro distribution[](#installing-in-xxpro-distribution "Link to this heading")

The EDA Toolbox can be installed in any generic Python distribution, but also be inside the Python distribution of EMPro or SIPro for that matter. That may be necessary if you
want to combine the capabilities of both. Some example scripts show how to do that and in those cases it is recommended to install the Toolbox into the distribution of xxPro.

Installing into the xxPro distribution starts with making sure you are using the Python of the xxPro distribution.

If you have ADS 2023 or more recent, open a terminal/command prompt and:

```
C:\Program Files\Keysight\ADS2025\fem\2025.00\win32_64\bin\emproenv.bat
```

On Linux start a bash shell under the xxPro environment:

```
/path/to/emproenv.sh bash
```

After you have done that, you can again use the pip installation procedure. Note that on Windows andyou will need to use python instead of py, on Linux use python:

```
python -m pip install c:\path\to\wheelfile\keysight.edatoolbox-1.2.1-py3-none-any.whl
```

```
python -m pip install /path/to/wheelfile/keysight.edatoolbox-1.2.1-py3-none-any.whl
```

### Examples[](#examples "Link to this heading")

The examples can be found on the [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).


---

## 26. Initial_Setup\prerequisites.md {#initial_setup--prerequisites}

# Prerequisites[](#prerequisites "Link to this heading")

## EDA Toolbox + Circuit simulation[](#eda-toolbox-circuit-simulation "Link to this heading")

To use the EDA Toolbox with circuit simulation, including the building and manipulating of circuits, it is sufficient to have a working Python 3.8+ installation and an ADS 2022 U1 or more recent installation.
For the Python EDA Toolbox version 3.10.x is recommended though and that can be found on [python.org](https://www.python.org)

## EDA Toolbox + xxPro simulation[](#eda-toolbox-xxpro-simulation "Link to this heading")

To use the EDA Toolbox with EMPro/SIPro simulation, including the building and manipulating of circuits, it is recommended to use an ADS 2023 or more recent installation. That installation already
comes with Python 3.10 and it is recommend to use the Python installation then that comes with it to fully enjoy the capabilities of the combination. Refer to the installation manual on how
to install the EDA Toolbox into the Python of xxPro or ADS.

## EDA Toolbox + other[](#eda-toolbox-other "Link to this heading")

To use the EDA Toolbox with other functionality it is typically sufficient to have a working Python 3.8+ installation and the respective product like VSA or SystemVue installed.
For the Python EDA Toolbox version 3.10.x is recommended though and that can be found on [python.org](https://www.python.org)


---

## 27. Initial_Setup\verifying.md {#initial_setup--verifying}

# Verifying Installation[](#verifying-installation "Link to this heading")

After the installation you may want to verify if everything is set up properly.

Warning

These instructions assume you are using a standard Python distribution from [python.org](https://www.python.org). Python 3.10.x is the recommended installation to use.
If you have multiple Python distributions installed on Windows you will need to specify to ‘py’ which version you use. In our case this will be: py -3.10, so
equivalent pip instructions below become py -3.10 -m pip instead of just py -m pip.

If you are using the ADS/xxPro installation all these commands will use python instead of py.

## Base installation[](#base-installation "Link to this heading")

In the same command prompt you did the install, now execute below command and it should print out “Keysight EDA Toolbox succesfully installed”, if there is a Python stacktrace with a module import error, then the installation has failed.

```
py -c"import keysight.edatoolbox;print('Keysight EDA Toolbox succesfully installed')"
```

On Linux:

```
python3 -c"import keysight.edatoolbox;print('Keysight EDA Toolbox succesfully installed')"
```

## Modules used in examples[](#modules-used-in-examples "Link to this heading")

The examples also use other modules beyond the keysight.edatoolbox, such as plotting libraries Matplotlib and Seaborn or the PathWave datatools.
You can verify in similar way if the modules are properly installed.

### Matplotlib, Numpy, Pandas, Scipy[](#matplotlib-numpy-pandas-scipy "Link to this heading")

```
py -c"import numpy;print('Numpy succesfully installed')"
py -c"import matplotlib;print('Matplotlib succesfully installed')"
py -c"import pandas;print('Pandas succesfully installed')"
py -c"import scipy;print('Scipy succesfully installed')"
py -c"import plotly ;print('plotly succesfully installed')"
```

If it fails, below instructions can be used to install Matplotlib, the recipe is the same for numpy, maptlotlib, pandas, scipy and plotly.

```
py -m pip install matplotlib
```

Or all at once:

```
py -m pip install numpy matplotlib pandas scipy plotly
```

Matplotlib can require building of additional modules and requiring the availability of a compiler on your system. If that is the case, you can also use some of the pre-built wheels.
Those can be downloaded here: [Pre-built wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib) In that case use the whl file to install it, download the correct wheel for your Python version,
the recommended version is Python 3.10, so the packages will look in signature as follows:

```
py -m pip install SciPy-1.8.1-cp310-cp310-win_amd64.whl
```

### Seaborn[](#seaborn "Link to this heading")

```
py -c"import seaborn;print('Seaborn succesfully installed')"
```

If it fails, below instructions can be used to install Seaborn:

```
py -m pip install seaborn
```

### PathWave Datatools[](#pathwave-datatools "Link to this heading")

```
py -c"import keysight.pwdatatools;print('PathWave datatools succesfully installed')"
```

[PathWave Datatools user installation guide](https://docs.keysight.com/pwdt0x9x0/initial-setup/installation)

Alternatively you can grab the 0.5.0 wheel here: [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202). and install using pip

```
py -m pip install kkeysight_pwdatatools-0.5.0-cp310-cp310-win_amd64.whl
```

There is a possibilty that saving image files can throw error using plotly (for certain versions), in that case , try to install specific version of kaleido

```
py -m pip install kaleido==0.1.0post1
```


---

## 28. Initial_Setup\ssh.md {#initial_setup--ssh}

# SSH[](#ssh "Link to this heading")

When you are using SSH to run Python code on a remote machine in combination with the EDA Toolbox you need to make sure that the SSH session is able to open a graphical window on the remote machine. This is necessary for some operations executed by the EDA Toolbox, even if it does not display a GUI at first sight. In some cases there is no
display available on the remote machine, so you need to use X11 forwarding to display the GUI on your local machine. To enable X11 forwarding, you need to add the -X option to the SSH command.

Alternatively you can use a virtual display, which is a display that is not connected to a physical display device. This is useful when you are running the EDA Toolbox on a remote machine that does not have a display. To use a virtual display, you need to install the xvfb package and run the following command before starting the EDA Toolbox:

`
xvfb-run -a -s “-screen 0 1400x900x24” python3 my\_script.py
`


---

## 29. Examples\index.md {#examples--index}

# Examples[](#examples "Link to this heading")

This guide will go through how to run the examples that are included in the toolbox.
We will assume that you have installed the toolbox, instructions on how to successfully do so are found in the [Initial Setup](../Initial_Setup/installation.md).

Note

Certain examples require additional python packages to be installed. Instructions on which packages, and how they can be installed, are found in the [Verifying Installation](../Initial_Setup/verifying.md) section.

Note

Certain examples require additional products to be installed, such as SystemVue or VSA.

## Get the example workspaces[](#get-the-example-workspaces "Link to this heading")

Download the example workspaces from the [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

Assume you have put these files in your “f:/temp/edatoolbox” directory.
Use a command prompt to navigate to this directory.

## Running the examples[](#running-the-examples "Link to this heading")

Next we need to choose which example to run, and where to write the output to.
Assume the output directory is “f:/temp/edatoolbox/output”.
Run the choses example using python.

```
>>> py <example>.py --output-dir=f:/temp/edatoolbox/output
```

Note

Certain examples require xxPro’s python to be used. If this is the case, make sure the toolbox and any other required packages are installed in xxPro’s distribution. And call python using `python` instead of `py`.


---

## 30. How-To\index.md {#how-to--index}

# How-To[](#how-to "Link to this heading")

* [Create a Circuit](circuit.md)
  + [Step 0: Getting ready](circuit.md#step-0-getting-ready)
  + [Step 1: Adding the components](circuit.md#step-1-adding-the-components)
  + [Step 2: Connecting the instances](circuit.md#step-2-connecting-the-instances)
  + [Step 3: Analysis?](circuit.md#step-3-analysis)
  + [Step 4: Run the simulation](circuit.md#step-4-run-the-simulation)
  + [Step 5: Extracting and plotting results](circuit.md#step-5-extracting-and-plotting-results)
* [Run a Circuit Simulation](circuit_sim.md)
  + [Step 0: Get the example workspaces](circuit_sim.md#step-0-get-the-example-workspaces)
  + [Step 1: Creating the ADS application object](circuit_sim.md#step-1-creating-the-ads-application-object)
  + [Step 2: Unarchiving](circuit_sim.md#step-2-unarchiving)
  + [Step 3: Generating the netlist](circuit_sim.md#step-3-generating-the-netlist)
  + [Step 4: Working the circuit](circuit_sim.md#step-4-working-the-circuit)
  + [Step 5: Run the simulation](circuit_sim.md#step-5-run-the-simulation)
  + [Step 6: Extract the results](circuit_sim.md#step-6-extract-the-results)
* [Create SIPro View and Run Simulation](sipro.md)
  + [Step 0: Get the example workspaces](sipro.md#step-0-get-the-example-workspaces)
  + [Step 1: Creating the ADS application object](sipro.md#step-1-creating-the-ads-application-object)
  + [Step 2: Unarchiving](sipro.md#step-2-unarchiving)
  + [Step 3: Creating the SIPro view](sipro.md#step-3-creating-the-sipro-view)
  + [Step 4: Loading the SIPro view into the SIPro tool](sipro.md#step-4-loading-the-sipro-view-into-the-sipro-tool)
  + [Step 5: Creating an Analysis](sipro.md#step-5-creating-an-analysis)
  + [Step 6: Running an Analysis](sipro.md#step-6-running-an-analysis)
  + [Step 7: Extracting some results](sipro.md#step-7-extracting-some-results)


---

## 31. How-To\circuit.md {#how-to--circuit}

# Create a Circuit[](#create-a-circuit "Link to this heading")

This section will go through an example of how to create a circuit from scratch and run a simulation on it and extract the results from it. In this example we will create a very simple RC low pass filter. If you have the matplotlib module available, then we will also show how to generate a plot of the response of the filter.

## Step 0: Getting ready[](#step-0-getting-ready "Link to this heading")

Import the module that we are going to use. At this point we only need the circuit module giving us access to a Circuit class and start building the actual circuit within Python.

```
>>> from keysight.edatoolbox import circuit
>>> low_pass_filter = circuit.Circuit()
```

## Step 1: Adding the components[](#step-1-adding-the-components "Link to this heading")

Next up is adding the components. There is a wide variety of components that can be added. We will just add 3 types here, a resistor, a component and finally also a voltage source. First up are the R and C components.

```
>>> R1 = low_pass_filter.add(circuit.R(name='R1', R="1 kOhm", p=None, n=None))
>>> C1 = low_pass_filter.add(circuit.C(name='C1', C="1 uF", p=None, n=None))
```

We add the components, given them a name, respectively ‘R1’ and ‘C1’. From the start we give them also a value of ‘1 kOhm’ and ‘1 uF’. Further we need to specify how the components will connect. However we don’t necessarily have to do it at this point, and we can’t. So for that reason we mark the ‘p’ and ‘n’ pin to remain unconnected, we do that by assigning ‘None’ to them. Later on we will connect the components to each other.

Finally we add a voltage source. We intend to do an AC analysis, so we add an AC voltage source:

```
>>> V = low_pass_filter.add(circuit.V_Source(name='V', Freq='freq', Vac='polar(1,0) V', Type='"V_AC"', p=None, n=None))
```

This one requires to use some of the more specifics of a voltage source in ADS netlist language. Critical is to mark the voltage source as an AC source by providing Type=‘“V\_AC”’, note that there is double quoting required!

## Step 2: Connecting the instances[](#step-2-connecting-the-instances "Link to this heading")

What is left is to connect all the instances together, essentially wiring all the instances to each other properly. Note that we will make use of the special .GND node part of any circuit we create.

The first line is will connect the negative pin of the voltage source V to the GND of the circuit.

```
>>> low_pass_filter.connect(V.n, low_pass_filter.GND)
```

Next up is connecting the positive pin of the voltage source V to the positive pin of resistor R1.

```
>>> low_pass_filter.connect(V.p, R1.p)
```

Finally we will connect the negative pin of the resistor R1 to the positive pin of the capacitor of C1. In the same way we finally connect the negative pin of C1 back to the GND node of the circuit.

```
>>> low_pass_filter.connect(R1.n, C1.p)
>>> low_pass_filter.connect(C1.n, low_pass_filter.GND)
```

## Step 3: Analysis?[](#step-3-analysis "Link to this heading")

A circuit has a list of instances, one of those instances could be a simulation controller and while the API does support that way of organizing the circuit, there is also another, more recommended way. To the circuit we can now add an analysis and configure it. It removes the need to go through all the specifics of adding sweep plan instance, option instances, etc.

Setting up an AC analysis is done by creating an AC analysis object, and configuring the desired frequency plan.

```
>>> ac_analysis = circuit.AC_Analysis(name='AC1')
>>> ac_analysis.sweep_plan.append(circuit.sweeps.LogarithmicSweep(1, 1e6, 5))
```

Finally we add the ac\_analysis object to the circuit, and selecting how the circuit simulator should call the resulting dataset. If we leave this blank the circuit simulator will pick a name, making it difficult later on to grab the dataset for reading it.

```
>>> low_pass_filter.analyses.append(ac_analysis)
>>> low_pass_filter.output_dataset = "low_pass_filter"
```

## Step 4: Run the simulation[](#step-4-run-the-simulation "Link to this heading")

Before we can run the simulation we need to import the remaining modules from the edatoolbox. In single script one would typically organize all the imports at the top, but in our example here we import piecemeal.

```
>>> from keysight.edatoolbox import ads
>>> from keysight.edatoolbox.util import safe_makedirs
```

Create now the circuit simulator application object to use to run a netlist. Our netlist comes from the Circuit object.

```
>>> circuit_sim = ads.CircuitSimulator()
>>> safe_makedirs('output')
>>> circuit_sim.run_netlist(low_pass_filter.generate_netlist(), output_dir='output')
```

## Step 5: Extracting and plotting results[](#step-5-extracting-and-plotting-results "Link to this heading")

When the simulation is done we need to extract the data and we are also going to plot it using the matplotlib module.

First step is to import modules we needed for this:

```
>>> import os
>>> import math
>>> from keysight.edatoolbox import dataset
>>> import matplotlib.pyplot as plt
```

Next up we read the dataset and bring it into Python and start with printing the values we find at the positive node of the C1 capacitor.

```
>>> output_data = dataset.Dataset(os.path.join('output','low_pass_filter.ds'))
>>> print('Response at C1', output_data.values('AC1.AC',str(C1.p)))
```

Optionally we also plot the results.

```
>>> import matplotlib.pyplot as plt
>>> response = [20.0*math.log10(abs(x)) for x in output_data.values('AC1.AC',str(C1.p))]
>>> plt.plot(response)
>>> plt.show()
```

Note, you may not have matplotlib available, so you can install it by using pip. For users on Windows, matplotlib can sometimes be problematic to install, especially on Python 3.10. There are several options in case you want to use matplotlib:

* install a pre-release package: py -m pip –pre matplotlib, this is the recommend way
* install a pre-release package: py -m pip matplotlib=3.5.0rc1 has been reported to work
* install seaborn and use seaborn, note that matplotlib is a dependency of seaborn so you may face similar issues
* use a Python distribution shipped with EMPro, IC-CAP or ADS. All of those have matplotlib pre-installed, ready to use!


---

## 32. How-To\circuit_sim.md {#how-to--circuit_sim}

# Run a Circuit Simulation[](#run-a-circuit-simulation "Link to this heading")

This section will go through an example of how to run a circuit simulation on a schematic.

## Step 0: Get the example workspaces[](#step-0-get-the-example-workspaces "Link to this heading")

Download the example workspaces, or if you are familiar with the git revision control system, directly clone the whole directory to a working location.

The examples can be found on the [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

[![../_images/screenshot_download_examples.png](../_images/screenshot_download_examples.png)](../_images/screenshot_download_examples.png)

Assume you have put these files in your “f:/temp/edatoolbox” directory.

## Step 1: Creating the ADS application object[](#step-1-creating-the-ads-application-object "Link to this heading")

First, let’s make an ADS application object that gives access to a workspace and its contents. But even before that, import the `edatoolbox`

```
>>> from keysight.edatoolbox import ads, circuit, dataset
>>> from keysight.edatoolbox.util import safe_makedirs
>>> ads_application = ads.ADS()
```

## Step 2: Unarchiving[](#step-2-unarchiving "Link to this heading")

Next, we use the ads module to unarchive the workspace. Alternatively you can use this manually with tools like 7-zip.

```
>>> target_workspace_dir = r"f:\temp\edatoolbox\examples\scratch"
>>> ads_application.unarchive_workspace(r"f:\temp\edatoolbox\examples\data\run_schematic_wrk.7zads", target_workspace_dir)
```

## Step 3: Generating the netlist[](#step-3-generating-the-netlist "Link to this heading")

The EDA Toolbox makes a distinction between the circuit simulator application, the ADS platform and the netlists as concepts. The circuit simulator will accept a netlist and perform a simulation. The ADS platform is responsible for generating the netlist. If we want to work with the netlist we can turn it into a Circuit object and manipulate it, but that is optional. In our example will be take the circuit and modify one of the resistor values.

We will feed the circuit simulator with a netlist, so the first step is to generate the netlist.

```
>>> target_workspace = os.path.join(target_workspace_dir, 'run_schematic_wrk')
>>> netlist = ads_application.generate_netlist( target_workspace,
                    ads.LibraryCellView(library="run_schematic_lib",
                                        cell="voltage_divider",
                                        view="schematic") )
```

## Step 4: Working the circuit[](#step-4-working-the-circuit "Link to this heading")

Instead of just passing the netlist directly to the circuit simulator we investigate it and also change some of the values of the resistor.

```
>>> voltage_divider = circuit.Circuit(netlist)
>>> print(f'Existing value of R2.R={voltage_divider.R2.R}')
```

Let us also change the value of the resistor.

```
>>> voltage_divider.R2.R = '10 Ohm'
```

## Step 5: Run the simulation[](#step-5-run-the-simulation "Link to this heading")

At this point we are ready to run the circuit simulator by giving it the circuit we just modified. The circuit object called “voltage\_divider” and we need to generate the netlist for it.

```
>>> new_netlist = voltage_divider.generate_netlist()
```

In order to run the netlist we first create a circuit simulator object very similar to how we create the ADS application object.

```
>>> ads_circuitsim = ads.CircuitSimulator()
>>> safe_makedirs(r"f:\temp\edatoolbox\examples\scratch\output")
>>> ads_circuitsim.run_netlist(new_netlist, output_dir=r"f:\temp\edatoolbox\examples\scratch\output")
```

The Python command will complete when the circuit simulator is done.

## Step 6: Extract the results[](#step-6-extract-the-results "Link to this heading")

The final thing left to do is extract the results. For this we use the built-in dataset module of the edatoolbox. The API of keysight.edatoolbox.dataset matches that of the pydataset and pwdatatools. When the pydataset built-in to ADS is available the keysight.edatoolbox will internally use it for speeding up all access to the data. The advantage of the keysight.edatoolbox.dataset is that is available independently of the Python version you are using, as it is a pure Python module. For that it does give us some performance.

```
>>> output_data = dataset.Dataset(os.path.join(r'f:\temp\edatoolbox\examples\scratch\output','voltage_divider.ds'))
>>> print(f"Voltage at node 'in' {output_data.values('DC1.DC', 'in')[0]}V")
>>> print(f"Voltage at node 'out' {output_data.values('DC1.DC', 'out')[0]}V")
```


---

## 33. How-To\sipro.md {#how-to--sipro}

# Create SIPro View and Run Simulation[](#create-sipro-view-and-run-simulation "Link to this heading")

This section will go through an example of how to run a SIPro simulation, starting from a zipped workspace.

## Step 0: Get the example workspaces[](#step-0-get-the-example-workspaces "Link to this heading")

Download the example workspaces, or if you are familiar with the git revision control system, directly clone the whole directory to a working location.

The examples can be found on the [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

Assume you have put these files in your “f:/temp/edatoolbox” directory.

## Step 1: Creating the ADS application object[](#step-1-creating-the-ads-application-object "Link to this heading")

First, let’s make an ADS application object that gives access to a workspace and its contents. But even before that, import the `edatoolbox`

```
>>> from keysight.edatoolbox import ads, momentum, xxpro
>>> ads_application = ads.ADS()
```

## Step 2: Unarchiving[](#step-2-unarchiving "Link to this heading")

Next, we use the ads module to unarchive the workspace. Alternatively you can use this manually with tools like 7-zip.

```
>>> target_workspace_dir = r"f:\temp\edatoolbox\examples\scratch"
>>> ads_application.unarchive_workspace(r"f:\temp\edatoolbox\examples\data\SIPro_PIPro_DDR4_wrk.7zads", target_workspace_dir)
```

## Step 3: Creating the SIPro view[](#step-3-creating-the-sipro-view "Link to this heading")

Now that we have unarchived the workspace, we want to create the SIPro view. To achieve this we define our input LibraryCellView and SIPro LibraryCellView.

```
>>> input_lcv = ads.LibraryCellView( library = "PC4-RDIMM_V090_RC_F0_20131106_lib",
...                                  cell = "PC4-RDIMM_V090_RC_F0_20131106",
...                                  view = "layout")
>>> sipro_lcv = ads.LibraryCellView( library = "PC4-RDIMM_V090_RC_F0_20131106_lib",
...                                  cell = "PC4-RDIMM_V090_RC_F0_20131106",
...                                  view = "sipro")
```

And we use our ads\_application to create the SIPro view.

```
>>> import os
>>> target_workspace = os.path.join(target_workspace_dir, "SIPro_PIPro_DDR4_wrk")
>>> ads_application.create_pro_view( target_workspace,
...                                  input_lcv = input_lcv,
...                                  substrate = "PC4-RDIMM_V090_RC_F0_20131106",
...                                  pro_lcv = sipro_lcv,
...                                  tool = "sipi")
```

## Step 4: Loading the SIPro view into the SIPro tool[](#step-4-loading-the-sipro-view-into-the-sipro-tool "Link to this heading")

In this step, we will start using SIPro’s built-in python API, so we will need to import `empro`

```
>>> import empro
>>> import empro.toolkit
>>> import empro.toolkit.analysis
```

At this point, we have created the SIPro view, but in order to start using SIPro we still need to properly configure it.

First, we will first tell SIPro what momentum to use, using the `edatoolbox`

```
>>> momentum_dir = momentum.get_momentum_location()
>>> empro.toolkit.analysis.setMomentumDir(momentum_dir)
```

Next, we tell SIPro what workspace we are currently using.

```
>>> os.environ['HPEESOF_DIR'] = ads.get_ads_location()  # ensure the referenced env vars in lib.defs can be found
>>> xxpro.use_workspace(target_workspace)
```

Finally, we can load the SIPro view into the SIPro tool and save the SIPro project.

```
>>> xxpro.load_pro_view(sipro_lcv)
>>> empro.activeProject.saveActiveProject()
```

## Step 5: Creating an Analysis[](#step-5-creating-an-analysis "Link to this heading")

Now we are ready to create an Analysis, we will name it “Test”. Use the `empro.analysis.Analysis.PASIAnalysisType` as a first argument, to make sure it will be a Power-Aware-SI Analysis.

```
>>> analysis = empro.analysis.Analysis(empro.analysis.Analysis.PASIAnalysisType, "Test")
```

Let’s define all the ports using the convention: `(port_name, list_of_plus_pin_names, list_of_min_pin_names)`.

```
>>> port_definitions = [ ('DQ00_J1', ['J1.P_5'], ['J1.P_6']),
...                      ('DQ00R_U19', ['U19.P_D3'], ['U19.P_D1']),
...                      ('DQ01_J1',['J1.P_150'],['J1.P_149']),
...                      ('DQ01R_U19',['U19.P_C2'],['U19.P_D1']),
...                      ('DQ02_J1',['J1.P_12'],['J1.P_11']),
...                      ('DQ02R_U19',['U19.P_D7'],['U19.P_C8']),
...                      ('DQ03_J1',['J1.P_157'],['J1.P_156']),
...                      ('DQ03R_U19',['U19.P_B7'],['U19.P_C8'])]
```

To aid us, we will define a helper function to get the `empro.geometry.Pin` object from the `layout`.

```
>>> def pin_from_name(layout, name):
...     try:
...         inst_name, pin_name = name.split(".")
...         return layout.instances[inst_name].instPin(pin_name)
...     except ValueError:
...         return layout.topLevelPins[name]
```

Now we can add the ports to the Analysis.

```
>>> layout = empro.activeProject.layout
>>> for port_def in port_definitions:
...     name, plus_pins, minus_pins = port_def
...     plus_pins = [pin_from_name(layout, name) for name in plus_pins]
...     minus_pins = [pin_from_name(layout, name) for name in minus_pins]
...     port = empro.analysis.Port(plus_pins,minus_pins, name)
...     analysis.ports.append(port)
```

Next, we add the components and set a model for the components to use.

```
>>> component_model_group = empro.analysis.ComponentModelGroup(layout.components['PC4-RDIMM_V090_RC_F0_20131106_lib:rn_2pos_respack_2x0201-510-501140a_15'])
>>> component_model_group.arrayedComponent = True
>>> component_model_group.pinPortMap().update( [('P_1', 1), ('P_2', 2), ('P_3', -2), ('P_4', -1)] )
>>> for instance_name in ['RN95', 'RN97']:
...     component_model_group.appendInstance(empro.analysis.ComponentInstance(layout.instances[instance_name]))

>>> component_model = empro.analysis.ComponentModel(empro.components.RLCSpecification('lumped','15 Ohm',0,0,'Series') )
>>> component_model_group.appendModel(component_model)
>>> analysis.componentModelGroups.append(component_model_group)
```

Finally, we add all the required nets to the Analysis.

```
>>> for net in analysis.requiredNets():
...     analysis.nets.append(net)
```

Now that the Analysis is complete, don’t forget to add it to the activeProject.

```
>>> empro.activeProject.analyses.append(analysis)
```

## Step 6: Running an Analysis[](#step-6-running-an-analysis "Link to this heading")

The previous step actually adds a clone of `analysis` to the activeProject’s analyses list. If we want to be able to view the results afterwards using the SIPro GUI, we need to make sure we run the Analysis that was actually added to the analyses list.

```
>>> active_analysis = empro.activeProject.analyses[-1]
```

Next, we run, wait for completion, and save `active_analysis`.

```
>>> empro.toolkit.analysis.runAnalysis(active_analysis, waitForConfirmation=False, saveProject=True)
>>> empro.activeProject.simulations.isQueueHeld = False
>>> active_simulation = empro.activeProject.simulations[-1]
>>> empro.toolkit.simulation.wait(active_simulation)
>>> empro.activeProject.saveActiveProject()
```

These commands might take some time, depending on the machine you are using.

## Step 7: Extracting some results[](#step-7-extracting-some-results "Link to this heading")

In this final step, we will extract the S21 data and write it to a csv-file. First we grab the datasets.

```
>>> res = empro.analysis.CircuitResults(active_analysis)
>>> freqs = list(res.frequencies())
>>> S21_mag = res.Src(1,0,"ComplexMagnitude")
>>> S21_phase = res.Src(1,0,"Phase")
```

The dataset in `Src` (S-row-column) are 0 indexed, so S21 is accessed as row 1, column 0.

Now we can open a csv file and write the S parameter data to it.

```
>>> output_file = os.path.join(target_workspace_dir, "sparams.csv")
>>> with open(output_file,"w") as file:
...     line = ",".join(["Frequency", "S21 (mag)", "S21 (phase)"])
...     file.write(line + "\n")
...     for i in range(len(freqs)):
...         line = f"{freqs[i]},{S21_mag[i]},{S21_phase[i]}"
...         file.write(line + "\n")
```


---

## 34. release_notes\index.md {#release_notes--index}

# Release Notes[](#release-notes "Link to this heading")

## 1.2.4[](#id1 "Link to this heading")

* Added support for additional parameters on Tran analsyses.

## 1.2.3[](#id2 "Link to this heading")

* On Linux platforms the slower spawning subprocesses from the multiprocessing module is used to ensure
  LD\_LIBRARY\_PATH is properly picked up by the subprocesses.

## 1.2.2[](#id3 "Link to this heading")

* Added detection for when multi\_python runs in an IPython environment.

## 1.2.1[](#id4 "Link to this heading")

* Added support for multi\_python with Open Access use in both ADS and xxPro.

## 1.1.6[](#id5 "Link to this heading")

* Enabled multi\_python to support a mix of ADS and xxPro in the same Python session.
* Integrated the ability to pick up the ADS libr config, making additional libraries visible during circuit simulation.

## 1.1.5[](#id6 "Link to this heading")

* Aligned the dataset API with the ADS 2025 release.
* Improved version request compatibility with more Python versions.

## 1.1.4[](#id7 "Link to this heading")

* Added support for specifying the location of verilog\_a models.
* Increased the maximum number of ports in the S-Parameter block to 120.

## 1.1.3[](#id8 "Link to this heading")

* Introduced the dataset\_name parameter in the circuit simulation run command to specify dataset names.
* Added support for the Balun component.

## 1.1.2[](#id9 "Link to this heading")

* removed links to internal development resources.

## 1.0.1[](#id10 "Link to this heading")

* Fixed a bug related to multi-valued parameter extraction and netlist generation.

## 1.0.0[](#id11 "Link to this heading")

* Bumped version to be an official package.
* The circuit.Circuit.variables returns Var instances like advertised instead of their value str.
* Added support for QuantumPro view creation and an example.

## 0.0.8[](#id12 "Link to this heading")

Added support for compiled models, such as the RfTransistorLibrary.
Enhanced netlist construction capabilities.
Resolved a bug where local variables became global in netlists.
Enabled noise parameter control in the S-Parameter block when extract\_analyses=True.

## 0.0.7[](#id13 "Link to this heading")

* Added support for instance names containing quotes.
* Enabled the creation of SnP blocks and instances with optional nodes.
* Introduced new parameters (ImpMaxFreq, ImpPasses, ImpSaveSpectrum, ImpLFEOn, SteadyState) in Tran circuit netlists.
* Added support for DataFileList.
* Added support for VtLFSR\_DT and Switch1ofN components.
* Enabled modifications to the thickness of dielectric and metal layers in ODB++ layouts.

## 0.0.6[](#id14 "Link to this heading")

* Added support for exclamation marks in instance node names within circuit netlists.
* Fixed a bug involving instantiations from a Python-defined subcircuit definition.
* Enhanced recognition of the global scope of variables in netlists.

## 0.0.5[](#id15 "Link to this heading")

* Introduced the SPSS parameter in SParam circuit netlists.

## 0.0.4[](#id16 "Link to this heading")

* Added support for special characters in node names in netlists (e.g., [“.]).
* Validated lib.defs references to environment variables when using a workspace.

## 0.0.3[](#id17 "Link to this heading")

* Initial public release of EDA Toolbox.
