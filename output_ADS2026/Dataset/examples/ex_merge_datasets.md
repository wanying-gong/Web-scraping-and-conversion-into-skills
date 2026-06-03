<!-- 来源: examples\ex_merge_datasets.html -->

[![Logo](../_static/images/keysight_logo.svg)](http://www.keysight.com/)

* [keysight-ads-dataset](../index.md)
* [Examples](index.md)
* Merge Datasets

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
  + Merge Datasets
  + [Create Dataset from DataFrame](ex_create_dataset_from_dataframe.md)
* [History](../history.md)
* [Dependencies](../dependencies.md)

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

On this page

[Previous

Merge Irregular DataFrames](ex_merge_irregular_dataframes.md)
[Next

Create Dataset from DataFrame](ex_create_dataset_from_dataframe.md)

* © Keysight Technologies 2000-
* [Privacy](https://www.keysight.com/in/en/contact/privacy.html)
* [Terms](https://www.keysight.com/in/en/contact/terms-of-use.html)
* [Feedback](https://www.keysight.com/in/en/contact/support/site-feedback.html)

Built with [Sphinx](https://www.sphinx-doc.org/) using
'Rejoice' theme by Keysight

*arrow\_drop\_up*Top