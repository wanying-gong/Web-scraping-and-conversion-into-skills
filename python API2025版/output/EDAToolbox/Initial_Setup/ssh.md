<!-- 来源: Initial_Setup\ssh.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [edatoolbox](../index.md)
* [Initial Setup](index.md)
* SSH

1.2.4

*invert\_colors* Theme

*rate\_review* Feedback
[*code* Source](../_sources/Initial_Setup/ssh.rst.txt)

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

* [API Reference](../API_Reference/index.md)
  + [ADS](../API_Reference/ads/index.md)
    - [Functions](../API_Reference/ads/functions/index.md)
    - [Classes](../API_Reference/ads/classes/index.md)
      * [ADS](../API_Reference/ads/classes/ads.md)
      * [CircuitSimulator](../API_Reference/ads/classes/circuit_simulator.md)
  + [Circuit API](../API_Reference/circuit/index.md)
    - [Functions](../API_Reference/circuit/functions/index.md)
    - [Classes](../API_Reference/circuit/classes/index.md)
      * [Circuit](../API_Reference/circuit/classes/circuit.md)
      * [Definition](../API_Reference/circuit/classes/definition.md)
      * [Instance](../API_Reference/circuit/classes/instance.md)
      * [Node](../API_Reference/circuit/classes/node.md)
      * [OptimizationRange](../API_Reference/circuit/classes/optimization_range.md)
      * [TuningRange](../API_Reference/circuit/classes/tuning_range.md)
      * [Value](../API_Reference/circuit/classes/value.md)
  + [Dataset](../API_Reference/dataset/index.md)
  + [External API](../API_Reference/extra/index.md)
    - [empro.analysis](../API_Reference/extra/empro/index.md)
  + [Multi Python API](../API_Reference/multi_python/index.md)
    - [Functions](../API_Reference/multi_python/functions/index.md)
  + [xxPro](../API_Reference/xxpro/index.md)
* [Initial Setup](index.md)
  + [Installation](installation.md)
  + [Prerequisites](prerequisites.md)
  + [Verifying Installation](verifying.md)
  + SSH
* [Examples](../Examples/index.md)
* [How-To](../How-To/index.md)
  + [Create a Circuit](../How-To/circuit.md)
  + [Run a Circuit Simulation](../How-To/circuit_sim.md)
  + [Create SIPro View and Run Simulation](../How-To/sipro.md)
* [Release Notes](../release_notes/index.md)

# SSH[](#ssh "Link to this heading")

When you are using SSH to run Python code on a remote machine in combination with the EDA Toolbox you need to make sure that the SSH session is able to open a graphical window on the remote machine. This is necessary for some operations executed by the EDA Toolbox, even if it does not display a GUI at first sight. In some cases there is no
display available on the remote machine, so you need to use X11 forwarding to display the GUI on your local machine. To enable X11 forwarding, you need to add the -X option to the SSH command.

Alternatively you can use a virtual display, which is a display that is not connected to a physical display device. This is useful when you are running the EDA Toolbox on a remote machine that does not have a display. To use a virtual display, you need to install the xvfb package and run the following command before starting the EDA Toolbox:

`
xvfb-run -a -s “-screen 0 1400x900x24” python3 my\_script.py
`

On this page

[Previous

Verifying Installation](verifying.md)
[Next

Examples](../Examples/index.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top