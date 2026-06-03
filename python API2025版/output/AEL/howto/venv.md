<!-- 来源: howto\venv.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [AEL Python Documentation](../index.md)
* [How-To](index.md)
* How to Set Up a Python Virtual Environment

Advanced Design System 2025 Update 2 (620)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

Contact Keysight

About

*menu* Contents

Table of contents

*close*

Contents:

* [Introduction](../intro/index.md)
  + [Using AEL Functionality in Python](../intro/usage.md)
* [Concepts](../concepts/index.md)
  + [AEL Interoperability](../concepts/ael_interoperability.md)
  + [AEL Type Conversions](../concepts/ael_type_conversions.md)
* [Reference](../reference/index.md)
  + [keysight.ads.ael](../reference/ael.md)
* [Examples](../examples/index.md)
  + [Calling Between AEL and Python](../examples/ex_calling_ael_and_python.md)
* [How-To](index.md)
  + How to Set Up a Python Virtual Environment
  + [How to Use Pytest](pytest.md)

# How to Set Up a Python Virtual Environment[](#how-to-set-up-a-python-virtual-environment "Link to this heading")

It is possible to access AEL python functionality in a python virtual environment rather than the embedded ADS Python installation.

The venv must be created using the Python shipped with ADS, using the **--system-site-packages** flag so that the venv has access to the **keysight.ads.ael** Python API.

> For linux:
>
> ```
> $HPEESOF_DIR/tools/python/bin/python3 -m venv --system-site-packages $HOME/ads_venv
> ```
>
> For windows:
>
> ```
> %HPEESOF_DIR%\tools\python\python -m venv --system-site-packages %HOME%\ads_venv
> ```

On this page

[Previous

How-To](index.md)
[Next

How to Use Pytest](pytest.md)

* © Keysight Technologies 2000-2023
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top