<!-- 来源: examples\ex_merge_dataframes.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-ads-dataset](../index.md)
* [Examples](index.md)
* Merge DataFrames

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
  + Merge DataFrames
  + [Merge Irregular DataFrames](ex_merge_irregular_dataframes.md)
  + [Merge Datasets](ex_merge_datasets.md)
  + [Create Dataset from DataFrame](ex_create_dataset_from_dataframe.md)
* [History](../history.md)
* [Dependencies](../dependencies.md)

# Merge DataFrames[](#merge-dataframes "Link to this heading")

This example shows how to merge two DataFrames into a single
DataFrame adding an outer variable corresponding to the original
DataFrames. This same method can be utilized to merge data from
multiple ADS Datasets.

```
# Copyright Keysight Technologies 2025 - 2025

import numpy as np
import pandas as pd

# Create data for the DataFrames
ind_data = [1e-3, 2e-3, 3e-3, 4e-3]
dep_data1 = [1, 2, 5, 10]
dep_data2 = [10, 20, 50, 100]

# Create an Index object named 'time' using the independent data
idx = pd.Index(data=ind_data, name="time")

# Create the DataFrames with the data and index.
df1 = pd.DataFrame({"V": dep_data1}, index=idx)
df2 = pd.DataFrame({"V": dep_data2}, index=idx)

# NOTE: At this point, these DataFrame objects could have come from
#       two ADS Datasets generated from ADS simulations.

# Add a new outer independent variable. In this case we will add 'R'
# to indicate that the data came from two different simulations where
# a resistor value was equal to 100 for one simulation and 2000 for
# the other.

# Get the Index of the data from each DataFrame object (we already
# know the Index value but we would do this if we were using
# DataFrames from ADS Datasets).
idx1 = df1.index.to_frame()
idx2 = df2.index.to_frame()

# Add R to the Index objects
idx1.insert(0, "R", 100)
idx2.insert(0, "R", 2000)

# Update the DataFrames with the updated Index with 'R' values.
df1.index = pd.MultiIndex.from_frame(idx1)
df2.index = pd.MultiIndex.from_frame(idx2)

# Finally create the merged DataFrame
merged_df = pd.concat([df1, df2])

# Validate the data we just created....
expected_dep_data = np.array([[1], [2], [5], [10], [10], [20], [50], [100]])
np.testing.assert_array_equal(merged_df.values, expected_dep_data)

expected_r_data = np.array([100, 100, 100, 100, 2000, 2000, 2000, 2000])
np.testing.assert_array_equal(merged_df.index.get_level_values(0), expected_r_data)

expected_time_data = np.array([1e-3, 2e-3, 3e-3, 4e-3, 1e-3, 2e-3, 3e-3, 4e-3])
np.testing.assert_array_equal(merged_df.index.get_level_values(1), expected_time_data)

# At this point you can display the results directly in Data Display
# using the py_var() function.  Or you can create a new ADS Dataset
# containing the merged DataFrame.
```

On this page

[Previous

Examples](index.md)
[Next

Merge Irregular DataFrames](ex_merge_irregular_dataframes.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top