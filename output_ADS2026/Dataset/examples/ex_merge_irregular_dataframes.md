<!-- 来源: examples\ex_merge_irregular_dataframes.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-ads-dataset](../index.md)
* [Examples](index.md)
* Merge Irregular DataFrames

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
  + Merge Irregular DataFrames
  + [Merge Datasets](ex_merge_datasets.md)
  + [Create Dataset from DataFrame](ex_create_dataset_from_dataframe.md)
* [History](../history.md)
* [Dependencies](../dependencies.md)

# Merge Irregular DataFrames[](#merge-irregular-dataframes "Link to this heading")

This example shows how to merge two DataFrames which contain
different sized data into a single DataFrame. First new outer
independent variables are added the DataFrames corresponding to the
original DataFrames. Then the DataFrames are merged into a single
DataFrame that can be displayed in Data Display or saved to an ADS
Dataset.

```
# Copyright Keysight Technologies 2025 - 2025

import numpy as np
import pandas as pd

# Create data for the DataFrames
ind_data1 = [1e-3, 2e-3, 3e-3, 4e-3]
dep_data1 = [1, 2, 5, 10]

# The second set to data has different independent values and
# different number of data points.
ind_data2 = [1.5e-3, 2e-3, 2.5e-3, 3e-3, 3.5e-3]
dep_data2 = [10, 155, 50, 55, 100]

# Create Index objects named 'time' using the independent data.
idx1 = pd.Index(data=ind_data1, name="time")
idx2 = pd.Index(data=ind_data2, name="time")

# Create the DataFrames with the data and index.
df1 = pd.DataFrame({"V": dep_data1}, index=idx1)
df2 = pd.DataFrame({"V": dep_data2}, index=idx2)

# NOTE: At this point, these DataFrame objects could have come from
#       two ADS Datasets generated from ADS simulations.

# Add a new outer independent variable. In this case we will add 'L'
# and 'R' as the outer independent variables.

# Get the Index of the data from each DataFrame object (we already know
# the Index values but we would do this if we were using DataFrames from
# ADS Datasets).
idx1 = df1.index.to_frame()
idx2 = df2.index.to_frame()

# Add L and R to the Index objects
idx1.insert(0, "R", 100)
idx1.insert(0, "L", 1e-9)
idx2.insert(0, "R", 2000)
idx2.insert(0, "L", 10e-9)

# Update the DataFrames with the updated Index values.
df1.index = pd.MultiIndex.from_frame(idx1)
df2.index = pd.MultiIndex.from_frame(idx2)

# Finally create the merged DataFrame
merged_df = pd.concat([df1, df2])

# Validate the data we just created....
expected_dep_data = np.array([[1], [2], [5], [10], [10], [155], [50], [55], [100]])
np.testing.assert_array_equal(merged_df.values, expected_dep_data)

expected_l_data = np.array([1e-9, 1e-9, 1e-9, 1e-9, 10e-9, 10e-9, 10e-9, 10e-9, 10e-9])
np.testing.assert_array_equal(merged_df.index.get_level_values(0), expected_l_data)

expected_r_data = np.array([100, 100, 100, 100, 2000, 2000, 2000, 2000, 2000])
np.testing.assert_array_equal(merged_df.index.get_level_values(1), expected_r_data)

expected_time_data = np.array(
    [1e-3, 2e-3, 3e-3, 4e-3, 1.5e-3, 2e-3, 2.5e-3, 3e-3, 3.5e-3]
)
np.testing.assert_array_equal(merged_df.index.get_level_values(2), expected_time_data)
```

On this page

[Previous

Merge DataFrames](ex_merge_dataframes.md)
[Next

Merge Datasets](ex_merge_datasets.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top