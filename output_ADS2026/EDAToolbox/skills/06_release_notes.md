# Release Notes
> **说明：** Release Notes 相关页面。

> **何时使用：** 当你需要查阅 Release Notes 相关内容时

---

## 本文件目录

- **Release Notes** (`release_notes/index.md`)

---

<!-- === 来源: release_notes/index.md === -->

# Release Notes[](#release-notes "Link to this heading")

## 1.2.4[](#id1 "Link to this heading")

* Documentation/examples update

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


---

