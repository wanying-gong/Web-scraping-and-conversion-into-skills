<!-- 来源: reference\quantum\dilution_fridge_input_line_designer.html -->

[![Logo](../../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [Quantum Python Documentation](../../index.md)
* [Reference](../index.md)
* [Quantum Addon](index.md)
* Dilution Fridge Input Line Designer

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
    - Dilution Fridge Input Line Designer
    - [Time Dynamics Analysis](time_dynamics_analysis.md)
* [How-To](../../howto/index.md)
  + [How to Set Up a Python Virtual Environment](../../howto/venv.md)
    - [Creating a new Python virtual environment based on ADS Python](../../howto/newvenv.md)
    - [Installing Keysight ADS wheels into an existing Python virtual environment](../../howto/existingvenv.md)
  + [How to Use Pytest](../../howto/pytest.md)

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

On this page

[Previous

SQUID Extrema Analysis](squid_extrema_analysis.md)
[Next

Time Dynamics Analysis](time_dynamics_analysis.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top