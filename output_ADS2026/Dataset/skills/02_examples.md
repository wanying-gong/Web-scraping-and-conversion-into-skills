# Examples
> **说明：** Examples 相关页面。

> **何时使用：** 当你需要查阅 Examples 相关内容时

---

## 本文件目录

- **Create Dataset from DataFrame** (`examples/ex_create_dataset_from_dataframe.md`)
- **Merge DataFrames** (`examples/ex_merge_dataframes.md`)
- **Merge Datasets** (`examples/ex_merge_datasets.md`)
- **Merge Irregular DataFrames** (`examples/ex_merge_irregular_dataframes.md`)
- **Examples** (`examples/index.md`)

---

<!-- === 来源: examples/ex_create_dataset_from_dataframe.md === -->

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


---

<!-- === 来源: examples/ex_merge_dataframes.md === -->

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


---

<!-- === 来源: examples/ex_merge_datasets.md === -->

# Merge Datasets[](#merge-datasets "Link to this heading")

This example shows how to merge three ADS Datasets into a single ADS
Dataset containing the merged data.

```
# Copyright Keysight Technologies 2025 - 2025

from os import PathLike
from pathlib import Path
from collections.abc import Sequence

import keysight.ads.dataset as ds
import pandas as pd

example_path = Path(__file__).parent.parent.resolve() / "examples"

def _validate_input_values(
    datasets_to_merge_paths: list[Path],
    sweep_names: list[str],
    sweep_values: list[list[int | float | str]],
) -> None:
    if not datasets_to_merge_paths:
        raise RuntimeError("No datasets to merge were specified.")
    if len(datasets_to_merge_paths) < 2:
        raise RuntimeError("Must include at least 2 datasets to merge.")
    if len(sweep_values) != len(datasets_to_merge_paths):
        raise RuntimeError("The number of datasets and sweep values must be equation.")
    for sweep_value in sweep_values:
        if len(sweep_names) != len(sweep_value):
            raise RuntimeError(
                "The number of sweep names and sweep values must be equation."
            )

def _init_unique_list_of_varblock_names(
    datasets_to_merge_paths: list[Path],
) -> list[str]:
    varblock_names = []
    for ds_path in datasets_to_merge_paths:
        dataset = ds.open_dataset_for_reading(ds_path)
        varblock_names += dataset.varblock_names
    return list(set(varblock_names))

def _add_sweeps_to_single_dataframe(
    df: pd.DataFrame,
    sweep_names: list[str],
    sweep_values: list[int | float | str],
) -> None:
    idx = df.index.to_frame()
    for sn, sv in zip(sweep_names, sweep_values, strict=True):
        idx.insert(0, sn, sv)
    df.index = pd.MultiIndex.from_frame(idx)

def _add_sweeps_to_multiple_dataframes(
    dfs: list[pd.DataFrame],
    sweep_names: list[str],
    sweep_values: list[list[int | float | str]],
) -> None:
    for df, sv in zip(dfs, sweep_values, strict=True):
        _add_sweeps_to_single_dataframe(df, sweep_names, sv)

def _get_dataframe_for_varblock_name_in_single_dataset(
    ds_path: Path, varblock_name: str
) -> pd.DataFrame:
    dataset = ds.open_dataset_for_reading(ds_path)
    if varblock_name not in dataset.varblock_names:
        return pd.DataFrame()
    return dataset[varblock_name].to_dataframe()

def _get_dataframes_for_varblock_name_in_multiple_datasets(
    datasets_to_merge_paths: list[Path],
    varblock_name: str,
) -> list[pd.DataFrame]:
    dfs = []
    for ds_path in datasets_to_merge_paths:
        df = _get_dataframe_for_varblock_name_in_single_dataset(ds_path, varblock_name)
        dfs.append(df)
    return dfs

def _get_merged_dataframe_for_varblock_name_in_multiple_datasets(
    datasets_to_merge_paths: list[Path],
    sweep_names: list[str],
    sweep_values: list[list[int | float | str]],
    varblock_name: str,
) -> pd.DataFrame:
    dfs = _get_dataframes_for_varblock_name_in_multiple_datasets(
        datasets_to_merge_paths, varblock_name
    )
    if not dfs:
        raise RuntimeError(
            'Internal Error: Failed to get at least one DataFrame for the VarBlock "'
            + varblock_name
            + '".'
        )
    _add_sweeps_to_multiple_dataframes(dfs, sweep_names, sweep_values)
    return pd.concat(dfs)

def merge_datasets(
    merged_dataset_name: str | PathLike,
    datasets_to_merge: Sequence[str | PathLike],
    swp_names: Sequence[str],
    swp_values: Sequence[Sequence[int | float | str]],
) -> None:
    """Create a merged dataset from a group of datasets.

    This class creates a single merge dataset from a group of
    datasets. The expectation is that each dataset to be merged was
    created from ADS with the same simulation setup but with different
    discreate values for one or more compentents. The class takes in
    lists of names for each component value that was changed in each
    simulation and the values that were varied.

    Parameters
    ----------
    datasets_to_merge
        A list of datasets names or Paths.
    sweep_names
        A list of sweep names to utilize for each dataset begin merged.
    sweep_values
        A list of list of sweep values. The outer list has an entry
        for each dataset being merged. The inner lists has values that
        match the number of sweep names.

    Example
    -------
        This example creates a merged dataset called 'merged.ds'. It
        takes two ADS Datasets that were created with value R and C
        being changed in the simulations. The simulation that created
        the "a.ds" dataset utilized the values "R=500" and "C=1e-9". A
        different simulation created the "b.ds" dataset with the
        values for set to "R=1000" and "C=10e-9".

    >>> merge_datasets('merged.ds',['a.ds', 'b.ds'], ['R', 'C'], [[500, 1e-9], [1000, 10e-9]])
    """

    datasets_to_merge_paths = [Path(t) for t in datasets_to_merge]
    sweep_names = list(reversed(swp_names))
    sweep_values = [list(reversed(t)) for t in swp_values]
    _validate_input_values(datasets_to_merge_paths, sweep_names, sweep_values)
    varblock_names = _init_unique_list_of_varblock_names(datasets_to_merge_paths)

    merged_dataset_path = Path(merged_dataset_name)
    merged_dataset = ds.open(merged_dataset_path, mode="w")

    for varblock_name in varblock_names:
        df = _get_merged_dataframe_for_varblock_name_in_multiple_datasets(
            datasets_to_merge_paths, sweep_names, sweep_values, varblock_name
        )
        if df.empty:
            raise RuntimeError(
                'Internal Error: Failed to get at least one merged DataFrame for the VarBlock "'
                + varblock_name
                + '".'
            )
        merged_dataset.create_varblock_from_dataframe(varblock_name, df)

if __name__ == "__main__":
    data_path = example_path / "data"
    dataset_paths = (
        data_path / "RLC_10_15_20.ds",
        data_path / "RLC_10_15_25.ds",
        data_path / "RLC_10_20_15.ds",
    )

    sweep_names = ("R", "L", "C")
    sweep_values = ((10, 15, 20), (10, 15, 25), (10, 20, 15))

    # Cleanup the old merged dataset (if it exists).
    merged_dataset_path = Path("RLC_merged.ds").resolve()
    if merged_dataset_path.exists():
        merged_dataset_path.unlink()

    # Do the merge of datsets.
    merge_datasets(merged_dataset_path, dataset_paths, sweep_names, sweep_values)

    # Validate that the merged dataset was created.
    if not merged_dataset_path.exists():
        raise RuntimeError(
            'Failed to generate dataset output in "merge_datasets.py" for "'
            + str(merged_dataset_path.name)
            + '"'
        )
```


---

<!-- === 来源: examples/ex_merge_irregular_dataframes.md === -->

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


---

<!-- === 来源: examples/index.md === -->

# Examples[](#examples "Link to this heading")

Contents:

* [Merge DataFrames](ex_merge_dataframes.md)
* [Merge Irregular DataFrames](ex_merge_irregular_dataframes.md)
* [Merge Datasets](ex_merge_datasets.md)
* [Create Dataset from DataFrame](ex_create_dataset_from_dataframe.md)


---

