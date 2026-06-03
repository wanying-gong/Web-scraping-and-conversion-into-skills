<!-- 来源: concepts.html -->

[![Logo](_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-ads-dataset](index.md)
* Concepts

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* Concepts
* [API Documentation](apidoc.md)
* [Examples](examples/index.md)
  + [Merge DataFrames](examples/ex_merge_dataframes.md)
  + [Merge Irregular DataFrames](examples/ex_merge_irregular_dataframes.md)
  + [Merge Datasets](examples/ex_merge_datasets.md)
  + [Create Dataset from DataFrame](examples/ex_create_dataset_from_dataframe.md)
* [History](history.md)
* [Dependencies](dependencies.md)

# Concepts[](#concepts "Link to this heading")

## Dataset[](#dataset "Link to this heading")

A **Dataset** contains a list of **VariableBlock**s, which are accessed by their
name. See [Dataset.varblocks](apidoc.md#keysight.ads.dataset.Dataset.varblocks "keysight.ads.dataset.Dataset.varblocks").

## VariableBlock[](#variableblock "Link to this heading")

A **VariableBlock** contains an ordered list of independent variables (`ivars`),
and an ordered list of dependent variables (`dvars`), which are each of type
**Variable**. These lists use a 0-based index.

A VariableBlock has a name. This name is typically formatted as a dotted string,
like `"Optim1.SP1.SP"`, describing the hierarchy of the origin of the data.
There is no hierarchy in the dataset corresponding to the dotted parts of the name.

A VariableBlock has a list of attributes. It’s more common to see attributes on
a **Variable** within a block, than on the block itself.

See [Variable Data](#concepts-variable-data) for more information on getting the data for a
VariableBlock.

## Variable[](#variable "Link to this heading")

A **Variable** contains a series of numeric data. In some cases it can contain a
series of string data, though these cases are rare. Typically a Variable contains
numeric data.

A Variable has a name, which is formatted as a dotted string. The dots typically
represent hierarchy in the simulator’s inputs, or in the simulator’s implementation.
There is no hierarchy in the dataset corresponding to the dotted parts of the name.

Multidimensional data (like S-parameters) is separated into multiple Variables,
with 1-based indices in square brackets.

Example

For example, 2-port S-parameter data produced by the ADS circuit simulator has
these variables:

| Independents | Dependents |
| --- | --- |
| * `freq` | * `S[1,1]` * `S[1,2]` * `S[2,2]` * `S[2,2]` * `PortZ[1]` * `PortZ[2]` |

The S-parameter results, which are a 2x2x*N* array of complex numbers for *N*
frequency points, are represented as 4 Variables, each of size *N*. Similarly,
the reference impedance, which is a 2x*N* array, is represented as 2 Variables.

A Variable has an element type. All data for that Variable is of the same element
type. The types are:

* `float`
* `complex`
* `int`
* `bool`
* `str`
* `None`

A Variable has a list of attributes. Each attribute has a name and a value, and
both are strings. A commonly used attribute is named `"flags"`, which is
accessible through the [Variable.flags](apidoc.md#keysight.ads.dataset.Variable.flags "keysight.ads.dataset.Variable.flags") and
[Variable.variable\_type](apidoc.md#keysight.ads.dataset.Variable.variable_type "keysight.ads.dataset.Variable.variable_type") properties.

## Variable Data[](#variable-data "Link to this heading")

Each **Variable** has a series of data. However, each variable’s series is not
stored separately; instead the **VariableBlock** contains data for all of its
variables.

In concept, a VariableBlock is analogous to a
[pandas DataFrame](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe).
Each Variable is analogous to a series in the dataframe, analogous to one column
in a table.

Use [VariableBlock.to\_dataframe](apidoc.md#keysight.ads.dataset.VariableBlock.to_dataframe "keysight.ads.dataset.VariableBlock.to_dataframe") to extract the data
as a dataframe.

## Attributes[](#attributes "Link to this heading")

Attributes are a list of key/value pairs. The key and value are both strings.

Several different object types can hold attributes. Currently the only one
accessible from Python is [Variable.attrs](apidoc.md#keysight.ads.dataset.Variable.attrs "keysight.ads.dataset.Variable.attrs").

On this page

[Previous

ADS Dataset](index.md)
[Next

API Documentation](apidoc.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top