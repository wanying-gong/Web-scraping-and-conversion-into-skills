<!-- 来源: examples\ex_create_dataset_from_dataframe.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-ads-dataset](../index.md)
* [Examples](index.md)
* Create Dataset from DataFrame

Advanced Design System 2026 Update 2 (640)

*invert\_colors* Theme

*rate\_review* Feedback

*help\_center* Help

[Contact Keysight](https://www.keysight.com/in/en/contact.html)

About

*menu* Contents

Table of contents

*close*

* [Concepts](../concepts.md)
* [API Documentation](../apidoc.md)
* [Examples](index.md)
  + [Merge DataFrames](ex_merge_dataframes.md)
  + [Merge Irregular DataFrames](ex_merge_irregular_dataframes.md)
  + [Merge Datasets](ex_merge_datasets.md)
  + Create Dataset from DataFrame
* [History](../history.md)
* [Dependencies](../dependencies.md)

# Create Dataset from DataFrame[](#create-dataset-from-dataframe "Link to this heading")

This example shows how to create a ADS Dataset from a DataFrame.

```
# Copyright Keysight Technologies 2025 - 2025

from pathlib import Path

import pandas as pd
import keysight.ads.dataset as ds

# Create data
str_data = ["str1", "str2", "str3", "str4", "str5", "str6"]
int_data = [1, 20, 50, 2, 22, 55]

# Create independent data
time_data = [1e-3, 1.2e-3, 1.5e-3, 1e-3, 1.2e-3, 1.5e-3]
name_data = ["A", "A", "A", "B", "B", "B"]

# Create an empty DataFrame
df = pd.DataFrame(
    {
        "name": name_data,
        "time": time_data,
        "str_data": str_data,
        "int_data": int_data,
    }
)

assert df["name"].dtype == "object"
assert df["time"].dtype == "float64"
assert df["str_data"].dtype == "object"
assert df["int_data"].dtype == "int64"

# At this point the string data is of dtype == object. However,
# dataset code doesn't know what to do with the dtype of object.
# So, change the dtype to "string" before calling the dataset
# code to create the datasets.
df[["name", "str_data"]] = df[["name", "str_data"]].astype("string")

assert df["name"].dtype == "string"
assert df["time"].dtype == "float64"
assert df["str_data"].dtype == "string"
assert df["int_data"].dtype == "int64"

# Reorganize the DataFrame making "name" and "time" independents
df.set_index(["name", "time"], inplace=True)

# Build the dataset from the dataframe.
dataset_path = Path("string_test.ds")
dataset = ds.open(dataset_path, mode="w")
dataset.create_varblock_from_dataframe("StringTest", df)

assert dataset_path.exists()
```

On this page

[Previous

Merge Datasets](ex_merge_datasets.md)
[Next

History](../history.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top