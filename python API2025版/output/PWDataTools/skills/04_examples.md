# Examples
> **说明：** Examples 相关页面。

> **何时使用：** 当你需要查阅 Examples 相关内容时

---

## 本文件目录

- **Examples** (`examples/index.md`)
- **Focus lpcwave file** (`examples/loadpull/focus_lpcwave.md`)
- **Load Pull Examples** (`examples/loadpull/index.md`)
- **Swept Frequency, Gamma, and Power** (`examples/loadpull/swept_freq_gamma_power_example.md`)
- **Swept Gamma** (`examples/loadpull/swept_gamma_example.md`)
- **Swept Gamma and Power** (`examples/loadpull/swept_gamma_power_example.md`)

---

<!-- === 来源: examples/index.md === -->

# Examples[](#examples "Link to this heading")

* [Load Pull Examples](loadpull/index.md)
  + [Simple Examples](loadpull/index.md#simple-examples)
  + [Real World Examples](loadpull/index.md#real-world-examples)


---

<!-- === 来源: examples/loadpull/focus_lpcwave.md === -->

# Focus lpcwave file[](#focus-lpcwave-file "Link to this heading")

In this example, we read a Focus lpcwave file that contains swept gamma and power. This file is an A/B Wave file. Several variables are automatically derived from the A and B waves when the file is read into a LoadPullBlock. Then, we manipulate the data using various methods available in the [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") class. If you haven’t reviewed [Simple Examples](index.md#simple-load-pull-examples) yet, you should do so before continuing.

See also

All Python scripts and data files for the load pull examples are located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

## Perform all imports[](#perform-all-imports "Link to this heading")

First, let’s import all the necessary modules. There are many Python libraries for plotting, but this example uses matplotlib, seaborn, and `pwdatatools.viz`. The `viz` module builds off matplotlib and seaborn to provide additional functionality. Also, we need the `pwdatatools.examples.loadpull` module to create the loadpull data. This example requires pwdatatools version 0.6.0 or later.

```
>>> import os
>>> from pathlib import Path
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> import pandas as pd
>>> import seaborn as sns
>>> from keysight import pwdatatools as pwdt
>>> from keysight.pwdatatools import viz
```

## Read the file[](#read-the-file "Link to this heading")

```
>>> lpblock = pwdt.read_file_as_loadpullblock(input_filepath)
```

Let’s print the [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object to see what it contains:

```
>>> print(lpblock)
LoadPullBlock(
    <'Vin', 'Vout', 'Iout', 'PinDel', 'PLoad', 'GainT', 'GainP', 'PAE', ... with 482 observations>,
    name='loadpull_powersweep_2',
    gamma_ivarname='GammaLoad_F1',
    power_ivarname='PinAvail',
    attrs={'Measurement_Type': ..., 'Sweep_Type': ..., 'Date': ..., 'Re ...},
)
```

We can see some (but not all) of the variable names, including the swept gamma and power independent variable names that are explicitly shown. Also note that the name of the LoadPullBlock is the name of the file (minus the file extension).

## Explore the data[](#explore-the-data "Link to this heading")

We can view all the variable names with the [`LoadPullBlock.varnames`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.varnames.md#keysight.pwdatatools.LoadPullBlock.varnames "keysight.pwdatatools.LoadPullBlock.varnames") attribute.

```
>>> print(lpblock.varnames)
('iGammaLoad_F1', 'iPinAvail', 'PinAvail', 'GammaLoad_F1', 'Vin', 'Vout', 'Iout', 'PinDel', 'PLoad', 'GainT', 'GainP', 'PAE', 'PSource', 'a1_F1', 'b1_F1', 'a2_F1', 'b2_F1', 'a1_F2', 'b1_F2', 'a2_F2', 'b2_F2', 'a1_F3', 'b1_F3', 'a2_F3', 'b2_F3', 'ZrefSource', 'ZrefLoad', 'GammaSource_F1', 'GammaSource_F2', 'GammaSource_F3', 'F1', 'F2', 'F3', 'GammaIn_F1', 'GammaIn_F2', 'GammaLoad_F2', 'GammaIn_F3', 'GammaLoad_F3', 'AMPM', 'DrainEff')
```

There are a bunch of variables in the LoadPullBlock. The variables that start with “i” are the index variables (iGammaLoad\_F1 and iPinAvail). The variables that start with “a” and “b” are A and B power waves (A waves are incident, B waves are reflected). The variables that start with “F” are the frequencies. In this file, F1 is the fundamental frequency, F2 is the second harmonic, and F3 is the third harmonic. However, in general, the frequencies do not necessarily have to be harmonically related. Note that some variables have suffixes like “\_F1”, “\_F2”, and “\_F3”. This means that the variable was measured at a particular frequency. However, some other variables like PLoad, PAE, GainT, GainP, and others are also measured at a particular frequency (F1). But since these variables only have an F1 component, the suffix is omitted. The voltages and currents (Vin, Vout, Iin, and Iout) are measured at DC.

## Reduce number of variables[](#reduce-number-of-variables "Link to this heading")

It is usually a good idea to exclude or remove variables that you will not need. This will speed up data processing tasks and make the DataFrame easier to view. We can easily drop variables using the `LoadpullBlock.drop_vars()` method, or conversely, we can keep only the variables that we want using the `LoadpullBlock.keep_vars()` method. In this example, we keep only a small handful of variables.

```
>>> lpblock = lpblock.keep_vars(["PLoad", "GainP", "DrainEff", "AMPM"])
>>> print(lpblock.varnames)
('iGammaLoad_F1', 'iPinAvail', 'PinAvail', 'GammaLoad_F1', 'PLoad', 'GainP', 'ZrefLoad', 'AMPM', 'DrainEff')
```

Note that the index variables, ZrefLoad, and the swept independent variables (ivars) are still present. By default, these crucial variables are kept by the [`LoadPullBlock.keep_vars()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_vars.md#keysight.pwdatatools.LoadPullBlock.keep_vars "keysight.pwdatatools.LoadPullBlock.keep_vars") method, even when not explicitly listed as variables to keep.

It’s also possible to modify which variables are derived when reading Wave data load pull files. This is done by setting the global option `options.reading.format_specific.loadpull.derived_vars` as shown below. This is useful if you want to keep the LoadPullBlock’s data as small as possible.

```
>>> derived_vars = pwdt.options.reading.format_specific.loadpull.derived_vars
>>> print(derived_vars)
FrozenRolesSet({'power.delivered.load', 'power.delivered.input', 'efficiency.drain', 'efficiency.power-added', 'power.available.source', 'gamma.load', 'gain.power', 'gamma.input', 'power.available.input', 'distortion.ampm'})
```

We can’t directly modify the set of roles, because it’s frozen. Instead, we create a new set of roles and assign it to the global option.

```
>>> new_derived_vars = set(derived_vars)
>>> new_derived_vars.remove("efficiency.power-added")
>>> pwdt.options.reading.format_specific.loadpull.derived_vars = new_derived_vars
```

Now, when we read the load pull datafile, the “efficiency.power-added” variable will not be derived.

```
>>> lpblock_alt = pwdt.LoadPullBlock.from_file(input_filepath)
```

## Renaming variables[](#renaming-variables "Link to this heading")

We can rename variables using the [`LoadPullBlock.rename_vars()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.rename_vars.md#keysight.pwdatatools.LoadPullBlock.rename_vars "keysight.pwdatatools.LoadPullBlock.rename_vars") method. Below, we rename the “GainP” variable to “Gp”.

```
>>> lpblock = lpblock.rename_vars({"GainP": "Gp"})
>>> print(lpblock.varnames)
('iGammaLoad_F1', 'iPinAvail', 'PinAvail', 'GammaLoad_F1', 'PLoad', 'Gp', 'ZrefLoad', 'AMPM', 'DrainEff')
```

## Reduce number of data points[](#reduce-number-of-data-points "Link to this heading")

Many times, loadpull data can include data that you don’t want to include in your analysis. For example, there may be bad data points that distort contours. For convenience, the [`LoadPullBlock.keep_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md#keysight.pwdatatools.LoadPullBlock.keep_observations "keysight.pwdatatools.LoadPullBlock.keep_observations") and [`LoadPullBlock.drop_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_observations.md#keysight.pwdatatools.LoadPullBlock.drop_observations "keysight.pwdatatools.LoadPullBlock.drop_observations") methods are provided. To use either method, we provide a boolean array that is the same length as the number of observations in the LoadPullBlock’s data. For the [`LoadPullBlock.keep_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md#keysight.pwdatatools.LoadPullBlock.keep_observations "keysight.pwdatatools.LoadPullBlock.keep_observations") method, the boolean array should be True for the observations to keep and False for the observations to drop. One way to do this is to use a boolean array from a comparison of a variable to a single value, as shown below.

```
>>> lpblock_filtered = lpblock.keep_observations(lpblock["PLoad"] > 34)
```

Notice the difference in observations count for the two LoadPullBlock instances below. If we didn’t need to keep the unfiltered data, we could’ve assigned the output of the [`LoadPullBlock.keep_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md#keysight.pwdatatools.LoadPullBlock.keep_observations "keysight.pwdatatools.LoadPullBlock.keep_observations") method to the original lpblock variable.

```
>>> print(lpblock.count_observations())
482
>>> print(lpblock_filtered.count_observations())
447
```

Note

The number of observations in the LoadPullBlock’s data is derived from the length of the ndarrays in their first dimension, which is axis 0. This also corresponds to the number of rows if the data is converted to a DataFrame.

## Examine the gamma ivar[](#examine-the-gamma-ivar "Link to this heading")

Let’s take a look at the first few data values of the gamma ivar, which in this dataset is named “GammaLoad\_F1”.

```
>>> print(lpblock['GammaLoad_F1'].to_numpy_ndarray()[0:10])
[-0.59950543-0.0571924j  -0.59945139-0.05724519j -0.59944071-0.05696654j
 -0.59948777-0.05712827j -0.59944238-0.05717805j -0.5993984 -0.05707937j
 -0.59945897-0.05701205j -0.59934044-0.05703576j -0.59934251-0.05693113j
 -0.59926347-0.05688538j]
```

We can see that the real and imaginary parts of gamma can vary slightly, even for the same “gamma point” that corresponds to a single iGammaLoad\_F1 value. This is one of the reasons why we use an integer index for the gamma ivar instead of indexing using the gamma values themselves. The same is true of the other ivars, such as the PinAvail ivar. We use an integer index to avoid any issues related to precision.

Let’s plot the gamma points on a Smith Chart. If we plot all of the gamma values, it would work just fine, but we may end up plotting multiple gammas that are really close to each other. So, before we plot the gamma ivar, let’s select a subset of the data at the first power value at each gamma index value.

```
>>> lpblock_subset = lpblock.keep_observations(lpblock["iPinAvail"] == 0)
```

The LoadPullBlock has a method [`LoadPullBlock.gamma_ivar_scatterplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot.md#keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot "keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot") that can be used to plot the gamma ivar on a rectangular or Smith chart. We must first import matplotlib so that we can create a matplotlib Axes object and also invoke `matplotlib.pyplot.show()` to display the plot. We will use the [`viz.draw_smith_chart()`](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.draw_smith_chart.md#keysight.pwdatatools.viz.draw_smith_chart "keysight.pwdatatools.viz.draw_smith_chart") function from the `pwdatatools.viz` module to create a Smith chart. All keyword arguments to the `gamma_ivar_scatterplot()` method are passed to the `seaborn.scatterplot()` function. See the [seaborn.scatterplot documentation](https://seaborn.pydata.org/generated/seaborn.scatterplot.html) for more information on the available keyword parameters.

```
>>> import matplotlib.pyplot as plt
>>> from keysight.pwdatatools import viz
>>> fig, ax = plt.subplots()
>>> viz.draw_smith_chart(ax)
>>> ax.set_title("Gamma Points")
>>> lpblock_subset.gamma_ivar_scatterplot(ax=ax)
>>> plt.show()
```

[![../../_images/realistic_gamma_points_ungridded_smithchart.png](../../_images/realistic_gamma_points_ungridded_smithchart.png)](../../_images/realistic_gamma_points_ungridded_smithchart.png)

## Select data at a specific power value[](#select-data-at-a-specific-power-value "Link to this heading")

When we plotted the ungridded gamma points above, we selected only the data at the first power value. In practice, the power values may be irregular at each gamma, and so the first power value may not be the same at each gamma. Furthermore, we may want to select data at a specific power value that was not explicitly measured. This requires interpolation and/or extrapolation. We can use the [`LoadPullBlock.at_power()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md#keysight.pwdatatools.LoadPullBlock.at_power "keysight.pwdatatools.LoadPullBlock.at_power") method to select data at specific power value(s). Here, we select one power value (40), but we could also select more than one and input them as a list. We can choose any variable to use for the `power_varname` argument. In this case, we use “PLoad”. Below, we convert the resulting LoadPullBlock’s data to a pandas DataFrame and print the first and last 5 observations of the data.

```
>>> lpblock_at_power = lpblock.at_power(40, "PLoad", power_idxname=None)
>>> dataframe_at_power = lpblock_at_power.to_pandas_dataframe(index="idxs")
>>> print(dataframe_at_power.head())
                     GammaLoad_F1  PLoad   PinAvail         Gp       AMPM   DrainEff   ZrefLoad
iGammaLoad_F1
0             -0.599505-0.057192j   40.0  21.811387  18.337554 -38.916208  29.971846  50.0+0.0j
1             -0.583814-0.159089j   40.0  22.114087  18.079940 -30.199213  28.553411  50.0+0.0j
2             -0.551828-0.256465j   40.0  22.791501  17.464683 -24.248914  26.393401  50.0+0.0j
3             -0.502717-0.343823j   40.0  23.658831  16.670029 -20.936101  29.347165  50.0+0.0j
4             -0.557693-0.380377j   40.0  23.837073  16.502647 -16.757597  23.511156  50.0+0.0j
>>> print(dataframe_at_power.tail())
                     GammaLoad_F1  PLoad   PinAvail         Gp       AMPM   DrainEff   ZrefLoad
iGammaLoad_F1
28            -0.865695-0.394581j   40.0  27.803563  12.651950  -1.825245  13.181057  50.0+0.0j
29            -0.896517-0.318402j   40.0  26.773933  13.605971  -3.776363  14.022184  50.0+0.0j
30            -0.920679-0.240904j   40.0  25.473713  14.826748  -8.160523  15.819262  50.0+0.0j
31            -0.936829-0.162784j   40.0  23.757357  16.441197 -19.359945  19.037109  50.0+0.0j
32            -0.947198-0.081638j   40.0  25.117598  14.927344 -66.137104  23.932672  50.0+0.0j
```

Note that the returned LoadPullBlock has the same number of gamma points as the original LoadPullBlock (33). However, the PLoad values are all the same and there is no longer a power ivar or index (iGammaLoad\_F1 is the only index). We can easily check a LoadPullBlock’s sweep information using the [`LoadPullBlock.get_sweep()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_sweep.md#keysight.pwdatatools.LoadPullBlock.get_sweep "keysight.pwdatatools.LoadPullBlock.get_sweep") method. The returned [`LoadPullSweep`](../../api_reference/loadpull/loadpullsweep/index.md#keysight.pwdatatools.LoadPullSweep "keysight.pwdatatools.LoadPullSweep") object contains all the ivarnames and idxnames of the LoadPullBlock. Note that the power sweep has been removed and therefore `power_ivarname` and `power_idxname` are now None. This is because we set the `power_idxname` argument to `None` in the call to the [`LoadPullBlock.at_power()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md#keysight.pwdatatools.LoadPullBlock.at_power "keysight.pwdatatools.LoadPullBlock.at_power") method.

```
>>> print(lpblock_at_power.get_sweep())
LoadPullSweep(
    outer_ivarnames=(),
    outer_idxnames=(),
    gamma_ivarname='GammaLoad_F1',
    gamma_idxname='iGammaLoad_F1',
    power_ivarname=None,
    power_idxname=None,
)
```

## Calculate gain compression points[](#calculate-gain-compression-points "Link to this heading")

The LoadPullBlock class has an [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method that can calculate all responses at specified gain compression point(s) and return a new LoadPullBlock. The method interpolates and/or extrapolates as needed. You need to specify the gain compression value(s) and the name of the gain variable to use. In this case, we will use “Gp” and calculate at a single gain compression value. However, it is possible to provide a list of more than one compression value to the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method. Note below that `extrap=True`. The default is `extrap=False`, but we need to extrapolate to calculate the gain compression at some gamma points.

```
>>> gcomp_value = 1
>>> lpblock_at_gcomp = lpblock.at_gcomp(gcomp_value, "Gp", gcomp_idxname=None, extrap=True)
```

Viewing the `sweep` attribute of `lpblock_at_gcomp`, we see there is no longer a power sweep defined since we calculated the data at one power level per gamma. Therefore, `power_ivarname` and `power_idxname` are now None. The gamma sweep is still defined since we calculated the gain compression at each gamma point. And because we set `gcomp_idxname` to `None` in the call to the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method, the gain compression does not become a new outer ivar.

```
>>> print(lpblock_at_gcomp.get_sweep())
LoadPullSweep(
    outer_ivarnames=(),
    outer_idxnames=(),
    gamma_ivarname='GammaLoad_F1',
    gamma_idxname='iGammaLoad_F1',
    power_ivarname=None,
    power_idxname=None,
)
```

Let’s plot the 1dB gain compression points for Gp. We create a function to plot Gp from the original LoadPullBlock and then plot the compression points on top.

```
>>> def plot_gain_and_compression_points(
...     loadpullblock, loadpullblock_at_gcomp, gcomp_value, gain_varname
... ):
...     _, ax = plt.subplots()
...     sns.lineplot(
...         y=gain_varname,
...         x="PinAvail",
...         data=loadpullblock,
...         ax=ax,
...         hue=loadpullblock.gamma_ivar("polar_str"),
...         palette="viridis",
...         legend=False,
...         linestyle="--",
...         linewidth=0.5,
...     )
...     sns.scatterplot(
...         y=gain_varname,
...         x="PinAvail",
...         data=loadpullblock_at_gcomp,
...         ax=ax,
...         hue=loadpullblock_at_gcomp.gamma_ivar("polar_str"),
...         palette="viridis",
...     )
...     ax.set_title(f"{gain_varname} at Gcomp = {gcomp_value}")
...     ax.legend(
...         title="GammaLoad values",
...         bbox_to_anchor=(1.1, 1.1),
...         loc="upper left",
...         borderaxespad=0,
...         ncol=2,
...     )
...     plt.show()
```

Now, let’s call the function.

```
>>> plot_gain_and_compression_points(lpblock, lpblock_at_gcomp, gcomp_value, "Gp")
```

[![../../_images/realistic_gcomp_points_all.png](../../_images/realistic_gcomp_points_all.png)](../../_images/realistic_gcomp_points_all.png)

The [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method interpolates and extrapolates to find the gain compression point at each gamma point. The gain compression points are the dots in the plot above. For some gammas, especially those with larger magnitudes, we are extrapolating quite a bit. To limit the amount of extrapolation, we could eliminate some gamma points. Let’s try that now.

```
>>> gamma_mag = np.abs(lpblock.gamma_ivar())
>>> lpblock_filtered = lpblock.keep_observations(gamma_mag < 0.95)
>>> lpblock_filtered_at_gcomp = lpblock_filtered.at_gcomp(gcomp_value, "Gp")
```

Plotting the filtered LoadPullBlock’s gain compression points shows that less extrapolation is needed to calculate the 1dB compression points.

```
>>> plot_gain_and_compression_points(
...     lpblock_filtered, lpblock_filtered_at_gcomp, gcomp_value, "Gp"
... )
```

[![../../_images/realistic_gcomp_points_filtered.png](../../_images/realistic_gcomp_points_filtered.png)](../../_images/realistic_gcomp_points_filtered.png)

## Plot contours[](#plot-contours "Link to this heading")

To create contour plots, we can use the [`LoadPullBlock.contourplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md#keysight.pwdatatools.LoadPullBlock.contourplot "keysight.pwdatatools.LoadPullBlock.contourplot") method. It’s common to plot contours at a particular power level or compression level. So, let’s plot gain and efficiency contours for the `lpblock_at_power` and `lpblock_at_gcomp` objects that we created in the previous steps.

```
>>> fig, axs = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(9, 3))
>>> cs_at_power = lpblock_at_power.contourplot("Gp", ax=axs[0], colors="blue")
>>> plt.clabel(cs_at_power, inline=True, fontsize=10)
>>> cs_at_gcomp = lpblock_at_gcomp.contourplot("Gp", ax=axs[1], colors="blue")
>>> plt.clabel(cs_at_gcomp, inline=True, fontsize=10)
>>> axs[0].set_title("Gp contours at PLoad = 40")
>>> axs[1].set_title(f"Gp contours at Gcomp = {gcomp_value}")
>>> axs[1].set_ylabel("")
>>> plt.show()
```

[![../../_images/realistic_contour_plots.png](../../_images/realistic_contour_plots.png)](../../_images/realistic_contour_plots.png)

## Regularize and grid the data[](#regularize-and-grid-the-data "Link to this heading")

If you do not understand the concept of “gridded” load pull data, please read [What is “gridded” load pull data?](../../howto/work_with_loadpull_data.md#what-is-gridded-load-pull-data) and [this simple gridding tutorial](swept_gamma_power_example.md#grid-data) before proceeding.

The pattern of sampled gamma points looks somewhat polar-shaped. Is the original data gridded? Let’s find out.

```
>>> print(lpblock.is_gridded())
False
```

No, it’s not gridded. Let’s grid it. But before we can apply a grid, the LoadPullBlock must have a regular power sweep. Let’s check if the power sweep is regular.

```
>>> print(lpblock.has_regular_power_ivar())
False
```

No, the power sweep is not regular. But what does this really mean? Let’s plot the power sweeps at each gamma point to see what’s going on. We will create a function to do this.

```
>>> def plot_power_levels_at_each_gamma(loadpullblock, title):
...     _, axes = plt.subplots(figsize=(5, 8))
...     sweep = loadpullblock.get_sweep()
...     gamma_polar_str = viz.complex_vector_to_str_series(
...         loadpullblock.gamma_ivar().to_numpy_ndarray(), "polar"
...     )
...     axes = sns.scatterplot(
...         x=loadpullblock[sweep.power_ivarname],
...         y=gamma_polar_str,
...     )
...     axes.set_title(title)
...     axes.set_xlabel(sweep.power_ivarname, fontsize=14, labelpad=10)
...     axes.set_ylabel(sweep.gamma_ivarname, fontsize=14, labelpad=10)
...     axes.tick_params(axis="y", which="major", labelsize=9)
...     plt.show()
```

Now, let’s use our function to plot the power sweeps at each gamma point.

```
>>> plot_power_levels_at_each_gamma(lpblock, "Irregular Power Sweeps at Each Gamma")
```

[![../../_images/realistic_gamma_vs_power_irreg.png](../../_images/realistic_gamma_vs_power_irreg.png)](../../_images/realistic_gamma_vs_power_irreg.png)

After examining the above plot, it should be clear that the power sweep is not the same for every gamma.

Note

Having a “regular power sweep” does **not** necessarily mean the power values are evenly-spaced.

Let’s regularize the power sweep. We’ll use the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method with extrapolation enabled. Then, we’ll use the [`LoadPullBlock.has_regular_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar.md#keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar "keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar") method to check if the new LoadPullBlock instance has a regular power sweep.

```
>>> lpblock_reg = lpblock.regularize_power_ivar(extrap=True)
>>> print(f"lpblock_reg has regular power sweep: {lpblock_reg.has_regular_power_ivar()}")
lpblock_reg has regular power sweep: True
```

For our regularized LoadPullBlock, let’s use our same function we used before to plot the power sweep values at each gamma point.

```
>>> plot_power_levels_at_each_gamma(lpblock_reg, "Regularized Power Sweeps at Each Gamma")
```

[![../../_images/realistic_gamma_vs_power_reg.png](../../_images/realistic_gamma_vs_power_reg.png)](../../_images/realistic_gamma_vs_power_reg.png)

Let’s also print out all the unique power values for our original LoadPullBlock and compare them to the regularized LoadPullBlock.

```
>>> original_power_vals = np.unique(lpblock.power_ivar())
>>> regularized_power_vals = np.unique(lpblock_reg.power_ivar())
>>> print(f"Original power values:\n{original_power_vals}")
Original power values:
[17.94 17.95 17.96 17.97 17.98 17.99 18.   18.01 18.02 18.04 18.58 18.61
 18.62 18.95 18.97 18.99 19.   19.01 19.02 19.04 19.05 19.56 19.61 19.92
 19.95 19.96 19.97 19.98 19.99 20.   20.01 20.02 20.03 20.55 20.57 20.58
 20.6  20.61 20.94 20.96 20.97 20.98 20.99 21.   21.01 21.02 21.57 21.6
 21.95 21.96 21.97 21.98 21.99 22.   22.02 22.03 22.57 22.6  22.61 22.95
 22.96 22.97 22.98 22.99 23.   23.01 23.02 23.04 23.56 23.58 23.6  23.63
 23.97 23.98 23.99 24.   24.01 24.02 24.03 24.04 24.6  24.62 24.98 24.99
 25.   25.01 25.02 25.03 25.04 25.05 25.06 25.6  25.61 25.65 26.01 26.02
 26.03 26.04 26.05 26.06 26.07 26.08 26.09 26.53 26.63 26.64 26.67 27.05
 27.06 27.07 27.08 27.09 27.1  27.11 27.12 27.64 27.66 27.67 27.69 27.71
 28.08 28.09 28.1  28.11 28.12 28.13 28.15 28.61 28.62 28.65 28.7  28.72
 29.1  29.11 29.12 29.13 29.14 29.15 29.16 29.17 29.18 29.7  29.72 29.73
 29.75 30.1  30.11 30.12 30.13 30.14 30.15 30.16 30.17 30.54 30.7  30.71
 30.73 31.07 31.09 31.1  31.11 31.12 31.13 31.14 31.15 31.16 31.55 31.56
 31.57 31.68 31.7  32.04 32.05 32.07 32.08 32.09 32.11 32.12 32.54 32.65
 33.03 33.04 33.05 33.06 33.63]
>>> print(f"Regularized power values:\n{regularized_power_vals}")
Regularized power values:
[-25.  -23.9 -22.9 -21.8 -20.7 -19.6 -18.6 -17.5 -16.4 -15.4 -14.3 -13.2
-12.1 -11.1 -10. ]
```

By default, the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method produces evenly-spaced sweeps between the max and min power values, rounded to the nearest tenth. However, as previously mentioned, having evenly-spaced power values is not a requirement for a LoadPullBlock’s power sweep to be considered “regular”. By default, the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method uses cubic interpolation to calculate all responses at the new power values. Extrapolation is off by default, but there are cubic, linear, and constant `extrap_method` options. See the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method for more information.

Now that we’ve regularized the LoadPullBlock’s power sweep, let’s grid it. First, let’s create a function that we can use to plot gridded and ungridded gamma points on a Smith chart. That way, we can repeatedly call the function throughout the demo.

```
>>> def plot_gamma_gridded_vs_ungridded_at_power(
...     lpblock_gridded, lpblock_ungridded, power_val, power_col
... ):
...     lpblock_ungridded_at_power = lpblock_ungridded.at_power(power_val, power_col)
...     lpblock_gridded_at_power = lpblock_gridded.at_power(power_val, power_col)
...     fig, ax = plt.subplots()
...     viz.draw_smith_chart(ax)
...     ax.set_title(f"GammaLoad at {power_col} = {power_val}")
...     lpblock_ungridded_at_power.gamma_ivar_scatterplot(
...         color="red", marker="D", label="Ungridded", ax=ax
...     )
...     lpblock_gridded_at_power.gamma_ivar_scatterplot(
..          color="blue", alpha=0.8, marker="X", label="Gridded", ax=ax
...     )
...     plt.show()
```

Either a ‘rect’ or ‘polar’ coordinate system will indeed work, but the ‘polar’ coordinate system is more appropriate for this data since the gamma points are sampled in a polar-shaped pattern.

```
>>> lpblock_gridded = lpblock.grid_data('polar')
>>> plot_gamma_gridded_vs_ungridded_at_power(lpblock_gridded, lpblock_reg, 20, "PSource")
```

[![../../_images/realistic_gamma_points_polar_gridded_smithchart.png](../../_images/realistic_gamma_points_polar_gridded_smithchart.png)](../../_images/realistic_gamma_points_polar_gridded_smithchart.png)

## Send data to ADS[](#send-data-to-ads "Link to this heading")

Let’s demonstrate how to get data into PathWave Advanced Design System (ADS). You can write out the gridded data into an ADS dataset and plot contours in ADS data display. The specialized Block object called ADSContourBlock arranges the data in such a way as to facilitate plotting contours in ADS. You may need to set the HPEESOF\_DIR environment variable as shown to point to an ADS installation.

```
>>> os.environ["HPEESOF_DIR"] = r"C:\Program Files\Keysight\ADS2024"
>>> cblock = lpblock_gridded.to_adscontourblock()
>>> cblock.to_file(output_filepath, dst_mode="w")
```

You can also directly write out a LoadPullBlock to an ADS dataset.

```
>>> lpblock_gridded.to_file(WRK_DATA_FOLDER / output_filepath, dst_mode="w")
```

See also

All Python scripts and data files for the load pull examples are located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)


---

<!-- === 来源: examples/loadpull/index.md === -->

# Load Pull Examples[](#load-pull-examples "Link to this heading")

The load pull examples are separated into two sections. In the first section, [Simple Examples](#simple-load-pull-examples), load pull data is generated from scratch and then manipulated to demonstrate basic concepts and features. In practice, you will typically read load pull data from a file, but this is a good place to start to learn the basics. The second section, [Real World Examples](#realworld-load-pull-examples), covers topics that are not covered in the basic examples, such as data reduction techniques and other features that are useful when dealing with real-world load pull data.

See also

All Python scripts and data files for the load pull examples are located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

## Simple Examples[](#simple-examples "Link to this heading")

These examples demonstrate the basics of using PathWave Data Tools with load pull data. The data in each of these examples is created from scratch in Python and kept simple in order to teach the basics of load pull data analysis. Each example focuses on a particular combination of swept variables. The simplest example demonstrates how to work with data that contains a single swept gamma variable (and no other swept variables). The most complex example includes a sweep of frequency, gamma, and power.

See also

[Work with Load Pull Data](../../howto/work_with_loadpull_data.md#work-with-load-pull-data)

* [Swept Gamma](swept_gamma_example.md)
* [Swept Gamma and Power](swept_gamma_power_example.md)
* [Swept Frequency, Gamma, and Power](swept_freq_gamma_power_example.md)

## Real World Examples[](#real-world-examples "Link to this heading")

These examples demonstrate the how to use PathWave Data Tools with real-world load pull data files.

See also

[Work with Load Pull Data](../../howto/work_with_loadpull_data.md#work-with-load-pull-data)

* [Focus lpcwave file](focus_lpcwave.md)


---

<!-- === 来源: examples/loadpull/swept_freq_gamma_power_example.md === -->

# Swept Frequency, Gamma, and Power[](#swept-frequency-gamma-and-power "Link to this heading")

This example demonstrates how to work with load pull data with swept frequency, gamma, and power. This example builds off [Swept Gamma](swept_gamma_example.md#swept-gamma) and [Swept Gamma and Power](swept_gamma_power_example.md#swept-gamma-and-power). Please make sure to review those examples before proceeding.

See also

All Python scripts and data files for the load pull examples are located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

## Perform all imports[](#perform-all-imports "Link to this heading")

First, let’s import all the necessary modules. There are many Python libraries for plotting, but this example uses matplotlib, seaborn, and `pwdatatools.viz`. The `viz` module builds off matplotlib and seaborn to provide additional functionality. Also, we need the `pwdatatools.examples.loadpull` module to create the loadpull data. This example requires pwdatatools version 0.6.0 or later.

```
>>> import os
>>> from pathlib import Path
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> from keysight import pwdatatools as pwdt
>>> from keysight.pwdatatools import viz
>>> from keysight.pwdatatools.examples import loadpull as lp_examples
```

## Create the data[](#create-the-data "Link to this heading")

Let’s generate the data that we will use. First, let’s define the unique frequency, gamma, and power points. These are the independent variables (ivars).

```
>>> freq_points = [1e9, 2e9, 3e9]
>>> gamma_points = [
...     0 + 0j, 0 + 0.25j, 0 + 0.5j,
...     0.25 + 0j, 0.25 + 0.25j, 0.25 + 0.5j,
...     0.5 + 0j, 0.5 + 0.25j, 0.5 + 0.5j,
... ]
>>> power_points = [-20.0, -10, -5, 0.0]
```

Next, we define the names of the ivars and create a [`Var`](../../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") for each.

```
>>> freq_ivarname = "freq"
>>> freq = pwdt.Var(freq_points, name=freq_ivarname)
>>> gamma_ivarname = "GammaLoad"
>>> gamma = pwdt.Var(gamma_points, name=gamma_ivarname)
>>> power_ivarname = "PSource"
>>> power = pwdt.Var(power_points, name=power_ivarname)
```

Now that we have the ivars handled, let’s create the dependent variables (dvars). We create two dvars: gain and efficiency. We only need to define nominal curves vs. power. These nominal curves will be modified to produce different values at each gamma and frequency. Each gain or efficiency value corresponds to a power value, so the nominal curves need to be the same length as the power points (in this example, the length is 4).

```
>>> gain_name = "Gp"
>>> eff_name = "DrainEff"
>>> gain_nominal = pwdt.Var([10, 10, 9, 8], name=gain_name)
>>> eff_nominal = pwdt.Var([50, 51, 48, 46], name=eff_name)
```

Now that we have all the variables ready, let’s create a LoadPullBlock. [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") is a specialized Block class that is a superset of the generic Block class and contains additional functionality for working with load pull data. We use the `make_swept_freq_gamma_power_loadpullblock()` function, which is part of the `keysight.pwdatatools.examples.loadpull` module, to create a LoadPullBlock.

```
>>> lpblock = lp_examples.make_swept_freq_gamma_power_loadpullblock(
...     freq, gamma, power, gain_nominal, eff_nominal
... )
>>> print(lpblock)
LoadPullBlock(
    <'Gp', 'DrainEff', ... with 108 observations>,
    name='example',
    gamma_ivarname='GammaLoad',
    power_ivarname='PSource',
    outer_ivarnames=('freq',),
    outer_idxnames=('ifreq',),
    attrs={},
)
```

We can see from the `lpblock` object’s printout that frequency is an outer indepedent variable (ivar). Note that `outer_ivarnames` is a tuple, which means that it can support more than one outer ivar.

See also

If you are not familiar with the concept of ivars, please see [Variable dependencies](../../core_concepts/multi_dimensional_data.md#variable-dependencies).

## Examine the variables[](#examine-the-variables "Link to this heading")

Let’s print the names of the independent variables (ivars), the dependent variables (dvars), and the index variables (idxs). Each of the LoadPullBlock’s 3 ivars have an associated integer index variable.

```
>>> print("ivars:", lpblock.ivarnames)
ivars: ('freq', 'GammaLoad', 'PSource')
>>> print("dvars:", lpblock.dvarnames)
dvars: ('Gp', 'DrainEff')
>>> print("idxs:", lpblock.idxnames)
idxs: ('ifreq', 'iGammaLoad', 'iPSource')
```

We can get variables by using the [`LoadPullBlock.__getitem__()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__getitem__.md#keysight.pwdatatools.LoadPullBlock.__getitem__ "keysight.pwdatatools.LoadPullBlock.__getitem__") method. It returns instances of [`Var`](../../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var").

```
>>> freq_var = lpblock[freq_ivarname]
>>> gamma_var = lpblock[gamma_ivarname]
>>> power_var = lpblock[power_ivarname]
>>> print(freq_var)
Var(
    <Float64 data with shape (108,)>,
    name='freq',
    dims=<empty Dims>,
    role='',
    unit=None,
    attrs={},
)
>>> print(gamma_var)
Var(
    <Complex128 data with shape (108,)>,
    name='GammaLoad',
    dims=<empty Dims>,
    role='gamma',
    unit=None,
    attrs={},
)
>>> print(power_var)
Var(
    <Float64 data with shape (108,)>,
    name='PSource',
    dims=<empty Dims>,
    role='power',
    unit=None,
    attrs={},
)
```

Note that the gamma and power ivars have the roles of ‘gamma’ and ‘power’, respectively. This is because those roles were assigned during creation of the LoadPullBlock. The frequency ivar does not have a role because it is an outer ivar, and outer ivars can be any arbitrary independent variables. You could manually assign a “frequency” role to the frequency ivar if you wanted to, but it is not necessary.

Let’s generate some plots. But before we do, let’s activate a color theme. This is an optional step that applies Keysight’s color theme to all charts created by matplotlib and seaborn.

```
>>> viz.use_keysight_theme()
```

Now we plot the gamma points using the [`LoadPullBlock.gamma_ivar_scatterplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot.md#keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot "keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot") method. Note that we format the freq values to scientific notation with one decimal place to make the legend more readable.

```
>>> fig, ax = plt.subplots()
>>> ax.set_title("Gamma points")
>>> lpblock.gamma_ivar_scatterplot(ax=ax, hue="freq", palette="viridis")
>>> handles, labels = ax.get_legend_handles_labels()
>>> formatted_labels = [f"{float(label):.1e}" for label in labels]
>>> ax.legend(
        handles, formatted_labels, bbox_to_anchor=(1, 1), loc="upper left", title="freq"
>>> )
>>> plt.show()
```

[![../../_images/simple_swept_freq_gamma_power_gamma_points.png](../../_images/simple_swept_freq_gamma_power_gamma_points.png)](../../_images/simple_swept_freq_gamma_power_gamma_points.png)

We can see from the plot that the gamma points are arranged in a rectangular grid and that the magnitudes increase with increasing frequency. This is simply because the `make_swept_freq_gamma_power_loadpullblock()` function made the data this way.

## Select frequency[](#select-frequency "Link to this heading")

When dealing with frequency-swept load pull data, it is helpful to know how to select one frequency at a time and how to iterate over frequencies. We can use the methods [`LoadPullBlock.keep_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md#keysight.pwdatatools.LoadPullBlock.keep_observations "keysight.pwdatatools.LoadPullBlock.keep_observations") and [`LoadPullBlock.drop_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_observations.md#keysight.pwdatatools.LoadPullBlock.drop_observations "keysight.pwdatatools.LoadPullBlock.drop_observations") to select subsets of the data. Let’s demonstrate creating a new LoadPullBlock containing just the data at the first frequency (which is located at the 0th index). Alternatively, we can select based upon the actual value of frequency.

```
>>> lpblock_filtered = lpblock.keep_observations(lpblock['ifreq'] == 0) # using ifreq
>>> lpblock_filtered = lpblock.keep_observations(lpblock['freq'] == 1.0e+09) # using freq
```

We can also iterate over the frequencies by finding the unique frequency index values and then iterating in a for-loop. For each iteration below, we have a subset LoadPullBlock that contains the data at a single frequency.

```
>>> ifreq_unique = np.unique(lpblock['ifreq'])
>>> for ifreq_value in ifreq_unique:
...     lpblock_at_single_freq = lpblock.keep_observations(lpblock['ifreq'] == ifreq_value)
...     do_something()
```

## Calculate gain compression[](#calculate-gain-compression "Link to this heading")

Let’s calculate two gain compression points. We use the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method, with extrapolation enabled.

```
>>> gcomp_points = [1.0, 2.5]
>>> lpblock_at_gcomp = lpblock.at_gcomp(gcomp_points, "Gp", extrap=True)
```

Next we plot gain and efficiency vs power and include the calculated gcomp points in the plots. The code to generate the plots is not shown here, but the plots are shown below.

See also

All load pull example code is located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

[![../../_images/simple_swept_freq_gamma_power_gain_vs_power_at_gcomp.png](../../_images/simple_swept_freq_gamma_power_gain_vs_power_at_gcomp.png)](../../_images/simple_swept_freq_gamma_power_gain_vs_power_at_gcomp.png)
[![../../_images/simple_swept_freq_gamma_power_eff_vs_power_at_gcomp.png](../../_images/simple_swept_freq_gamma_power_eff_vs_power_at_gcomp.png)](../../_images/simple_swept_freq_gamma_power_eff_vs_power_at_gcomp.png)

We can see from the plots the the first gain compression point falls within the available data, but the second point was extrapolated.

## Calculate responses at specified power levels[](#calculate-responses-at-specified-power-levels "Link to this heading")

The LoadPullBlock class has a method called [`LoadPullBlock.at_power()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md#keysight.pwdatatools.LoadPullBlock.at_power "keysight.pwdatatools.LoadPullBlock.at_power") that can be used to calculate the responses at specific power level(s). This method is similar to the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method, but instead of calculating the responses at gain compression level(s), it calculates the responses at specific power level(s). The power variable that you use to specify the power levels can be **any variable** in the LoadPullBlock; it doesn’t have to be the swept power independent variable. So, using this method, you could calculate all responses at specified PLoad values. The default behavior is to assign whichever power col is being used to the role of power\_ivar, and to add an integer index to the DataFrame corresponding to values of power.

Let’s calculate the responses at a few power levels. We use the [`LoadPullBlock.at_power()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md#keysight.pwdatatools.LoadPullBlock.at_power "keysight.pwdatatools.LoadPullBlock.at_power") method to calculate the responses at -18 dBm, -10 dBm, and -2 dBm. In order to obtain the data at -18 dBm, interpolation must be used. To get the response values at -2 dBm, extrapolation must be used. For the responses at -10 dBm, the data is available in the LoadPullBlock, so no interpolation or extrapolation is needed.

```
>>> power_values = [-18, -10.0, 2]
>>> power_col = "PSource"
>>> lpblock_at_power = lpblock.at_power(
...      power_values, power_col, extrap=True, interp_method="linear", extrap_method="linear"
... )
```

We can view the data as a pandas DataFrame by utilizing the [`LoadPullBlock.to_pandas_dataframe()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_pandas_dataframe.md#keysight.pwdatatools.LoadPullBlock.to_pandas_dataframe "keysight.pwdatatools.LoadPullBlock.to_pandas_dataframe") method. Here we use the LoadPullBlock’s idxs to form the DataFrame’s rows index.

```
>>> dataframe_at_power = lpblock_at_power.to_pandas_dataframe(index='idxs')
>>> print(dataframe_at_power)
                              freq   GammaLoad  PSource         Gp   DrainEff
ifreq iGammaLoad iPSource
0     0          0         1.0e+09  0.00+0.00j    -18.0  10.000000  50.200000
                 1         1.0e+09  0.00+0.00j    -10.0  10.000000  51.000000
                 2         1.0e+09  0.00+0.00j      2.0   7.600000  45.200000
      1          0         1.0e+09  0.00+0.25j    -18.0  10.250000  45.200000
                 1         1.0e+09  0.00+0.25j    -10.0  10.250000  46.000000
...                            ...         ...      ...        ...        ...
2     7          1         3.0e+09  0.70+0.35j    -10.0  10.782624  35.347524
                 2         3.0e+09  0.70+0.35j      2.0   8.382624  29.547524
      8          0         3.0e+09  0.70+0.70j    -18.0  10.989949  30.401010
                 1         3.0e+09  0.70+0.70j    -10.0  10.989949  31.201010
                 2         3.0e+09  0.70+0.70j      2.0   8.589949  25.401010
```

Next we plot gain and efficiency vs power and include the calculated power points as scatters in the plots. The code to generate the plots is not shown here, but the plots are shown below.

See also

All load pull example code is located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

[![../../_images/simple_swept_freq_gamma_power_gain_vs_power_at_power.png](../../_images/simple_swept_freq_gamma_power_gain_vs_power_at_power.png)](../../_images/simple_swept_freq_gamma_power_gain_vs_power_at_power.png)
[![../../_images/simple_swept_freq_gamma_power_eff_vs_power_at_power.png](../../_images/simple_swept_freq_gamma_power_eff_vs_power_at_power.png)](../../_images/simple_swept_freq_gamma_power_eff_vs_power_at_power.png)

## Create contour plots[](#create-contour-plots "Link to this heading")

Let’s plot gain and efficiency contours. We can utilize the [`LoadPullBlock.contourplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md#keysight.pwdatatools.LoadPullBlock.contourplot "keysight.pwdatatools.LoadPullBlock.contourplot") method to create contour plots. It provides additional conveniences beyond matplotlib’s `Axes.contour()` method, but if you prefer, you could use that method instead. Generally, you can pick either rectangular or Smith charts for these types of plots. We are plotting contours at each gain compression level from the `lpblock_at_gcomp` object, but we could have just as easily plotted contours at each power level from the `lpblock_at_power` object. The code to generate the plots is not shown here, but the plots are shown below.

[![../../_images/simple_swept_freq_gamma_power_gain_contours_at_gcomp.png](../../_images/simple_swept_freq_gamma_power_gain_contours_at_gcomp.png)](../../_images/simple_swept_freq_gamma_power_gain_contours_at_gcomp.png)
[![../../_images/simple_swept_freq_gamma_power_eff_contours_at_gcomp.png](../../_images/simple_swept_freq_gamma_power_eff_contours_at_gcomp.png)](../../_images/simple_swept_freq_gamma_power_eff_contours_at_gcomp.png)

## Grid data[](#grid-data "Link to this heading")

If you do not understand the concept of “gridded” load pull data, please read [this section](../../howto/work_with_loadpull_data.md#what-is-gridded-load-pull-data) before proceeding.

Let’s check our original [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object to see if it is gridded.

```
>>> print(f"lpblock is gridded: {lpblock.is_gridded()}")
lpblock is gridded: True
```

Let’s try to get the information about the grid. The [`LoadPullBlock.get_grid()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_grid.md#keysight.pwdatatools.LoadPullBlock.get_grid "keysight.pwdatatools.LoadPullBlock.get_grid") method returns a [`Grid`](../../api_reference/loadpull/grid/index.md#keysight.pwdatatools.Grid "keysight.pwdatatools.Grid") object (or `None` if the LoadPullBlock is not gridded).

```
>>> grid = lpblock.get_grid()
ValueError: Cannot get grid if there are outer swept variables
```

A ValueError is raised because we have a frequency outer ivar, which means we can potentially have a different grid at each frequency. So how can we get the grid information at each frequency? We can one of the techniques discussed in [Select frequency](#select-frequency).

```
>>> lpblock_at_first_freq = lpblock.keep_observations(lpblock["ifreq"] == 0)
>>> grid_at_first_freq = lpblock_at_first_freq.get_grid()
>>> print(grid_at_first_freq)
Grid(
    coord_system='rect',
    extents=<xmin=0.0, xmax=0.5, ymin=0.0, ymax=0.5>,
    npointsx=3,
    npointsy=3
)
```

So, this [`Grid`](../../api_reference/loadpull/grid/index.md#keysight.pwdatatools.Grid "keysight.pwdatatools.Grid") object contains all the grid information at the first frequency in our data. It contains the coordinate system (‘rect’ or ‘polar’), the extents of the grid, and the number of x and y points. The `x` and `y` extents are real/imaginary for a rectangular grid, and magnitude/phase for a polar grid.

A LoadPullBlock can have different grid specifications at each frequency while still being considered “gridded”. Let’s iterate over the frequencies and collect all the Grids. Then, we can print out the Grid at each frequency and compare.

```
>>> grids = []
>>> unique_ifreq_values = np.unique(lpblock["ifreq"])
>>> for ifreq_value in unique_ifreq_values:
...     lpblock_at_single_freq = lpblock.keep_observations(lpblock["ifreq"] == ifreq_value)
...     grids.append(lpblock_at_single_freq.get_grid())
>>> print(grids)
[Grid(
    coord_system='rect',
    extents=<xmin=0.0, xmax=0.5, ymin=0.0, ymax=0.5>,
    npointsx=3,
    npointsy=3
), Grid(
    coord_system='rect',
    extents=<xmin=0.0, xmax=0.6, ymin=0.0, ymax=0.6>,
    npointsx=3,
    npointsy=3
), Grid(
    coord_system='rect',
    extents=<xmin=0.0, xmax=0.7, ymin=0.0, ymax=0.7>,
    npointsx=3,
    npointsy=3
)]
```

We can see that all the Grids are using a “rect” coordinate system and 3x3 coordinate arrays. However, the Grids have different extents. This is simply because the sample data was constructed this way to illustrate that the Grids do not have to be uniform at all frequencies.

So in this example, the data is already gridded. But, if we needed to force the data to a grid, or regrid it, we can utilize the [`LoadPullBlock.grid_data()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md#keysight.pwdatatools.LoadPullBlock.grid_data "keysight.pwdatatools.LoadPullBlock.grid_data") method. Just to illustrate, we will apply a new grid and create plots comparing the original and new regridded gamma points at each frequency.

```
>>> lpblock_regridded = lpblock.grid_data("rect", npointsx=7)
>>> fig, axs = plt.subplots(1, len(freq_points), sharey=True, figsize=(10, 5))
>>> fig.suptitle("Gamma points", fontsize=15, y=0.9)
>>> for freq_idx in range(len(freq_points)):
...     ax = axs[freq_idx]
...     ax.set_title(f"freq={freq_points[freq_idx]:.1E}", fontsize=12)
...     viz.draw_smith_chart(ax)
...     lpblock_sub = lpblock.keep_observations(lpblock["ifreq"] == freq_idx)
...     lpblock_regridded_sub = lpblock_regridded.keep_observations(
...         lpblock_regridded["ifreq"] == freq_idx
...     )
...     lpblock_sub.gamma_ivar_scatterplot(ax=ax, label="original", legend=False)
...     lpblock_regridded_sub.gamma_ivar_scatterplot(ax=ax, label="regridded", legend=False)
...         if freq_idx == 0:
...             ax.legend(bbox_to_anchor=(1.1, -0.05), loc="upper left", ncols=2)
>>> plt.show()
```

[![../../_images/simple_swept_freq_gamma_power_gamma_regridded.png](../../_images/simple_swept_freq_gamma_power_gamma_regridded.png)](../../_images/simple_swept_freq_gamma_power_gamma_regridded.png)

## Send data to ADS[](#send-data-to-ads "Link to this heading")

Let’s demonstrate how to get data into PathWave Advanced Design System (ADS). We use the [`LoadPullBlock.to_adscontourblock()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_adscontourblock.md#keysight.pwdatatools.LoadPullBlock.to_adscontourblock "keysight.pwdatatools.LoadPullBlock.to_adscontourblock") method to do this. This method returns an `ADSContourBlock` object, which is a specialized type of Block class dedicated to arranging data in a way that is friendly to ADS contour plotting. We are writing several datasets to a workspace’s data folder `WRK_DATA_FOLDER`, whose definition exists in the example script but is not shown here.

```
>>> adsblock0 = lpblock.to_adscontourblock()
>>> adsblock0.to_file(WRK_DATA_FOLDER / "freq_gamma_power_sweep.ds", dst_mode="w")
>>> adsblock1 = lpblock_at_gcomp.to_adscontourblock()
>>> adsblock1.to_file(WRK_DATA_FOLDER / "freq_gamma_power_sweep_at_gcomp.ds", dst_mode="w")
>>> adsblock2 = lpblock_at_power.to_adscontourblock()
>>> adsblock2.to_file(WRK_DATA_FOLDER / "freq_gamma_power_sweep_at_power.ds", dst_mode="w")
```

Important

If you get a PermissionError when writing an ADS dataset, it is likely because the ADS Data Display window is open and accessing the dataset file you are trying to write. If this happens, you must close the ADS Data Display window and try running your script again.

If you prefer, you can combine all the data into a single ADS dataset. However, this requires all the ADSContourBlocks have unique names. So, we need to supply a name when calling the [`LoadPullBlock.to_adscontourblock()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_adscontourblock.md#keysight.pwdatatools.LoadPullBlock.to_adscontourblock "keysight.pwdatatools.LoadPullBlock.to_adscontourblock") method as shown below. Then, we can put all the ADSContourBlocks into a Group and write the Group to an ADS dataset. Note that the equations and graphs in ADS Data Display need to take into account the hierarchical nature of this dataset by accesssing each variable as `blockname.varname`. For example, to access `Gp` in the `at_gcomp` block, an equation in ADS Data Display needs to refer to `at_gcomp.Gp`.

```
>>> adsblock0 = lpblock.to_adscontourblock('original')
>>> adsblock1 = lpblock_at_gcomp.to_adscontourblock('at_gcomp')
>>> adsblock2 = lpblock_at_power.to_adscontourblock('at_power')
>>> group = pwdt.Group([adsblock0, adsblock1, adsblock2])
>>> group.to_file(WRK_DATA_FOLDER / "freq_gamma_power_sweep.ds", dst_mode="w")
```

If you do not need to plot contours in ADS, or if you prefer to do the manipulations needed for contouring yourself in ADS, you can directly write the LoadPullBlock to an ADS dataset.

```
>>> lpblock.to_file(WRK_DATA_FOLDER / "freq_gamma_power_sweep_gridded.ds", dst_mode="w"))
```

See also

There is an accompanying ADS workspace that shows how to plot contours in ADS Data Display using this dataset. The workspace is on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools).


---

<!-- === 来源: examples/loadpull/swept_gamma_example.md === -->

# Swept Gamma[](#swept-gamma "Link to this heading")

This example demonstrates how to work with load pull data with swept gamma (and no other swept variables). It is the simplest type of load pull data.

See also

All Python scripts and data files for the load pull examples are located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

## Create the data[](#create-the-data "Link to this heading")

Let’s generate some data to use for gamma, which is the only independent variable (ivar) in this example. First, we define the unique real and imaginary points. Then, we use `itertools.product()` to compute the cartesian product, which gives us every combination of these real and imaginary points. Here we input 3 real and 3 imaginary points, which results in 9 complex gamma points.

```
>>> import itertools
>>> gamma_real_points = [0, 0.25, 0.5]
>>> gamma_imag_points = [0, 0.25, 0.5]
>>> gamma_points = []
>>> for real_point, imag_point in itertools.product(gamma_real_points, gamma_imag_points):
...     gamma_points.append(real_point + 1j * imag_point)
>>> print(gamma_points)
[0j, 0.25j, 0.5j, (0.25+0j), (0.25+0.25j), (0.25+0.5j), (0.5+0j), (0.5+0.25j), (0.5+0.5j)]
```

Now, let’s create a [`Var`](../../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") for the gamma independent variable (ivar).

```
>>> import keysight.pwdatatools as pwdt
>>> gamma_ivarname = "GammaLoad"
>>> gamma = pwdt.Var(gamma_points, name=gamma_ivarname)
```

Next, we create Vars for gain and efficiency. These are the dependent variables (dvars). We only need to define the nominal values because the function we will use in the next step will generate the rest of the points automatically. So, each Var needs only one value.

```
>>> gain_name = "Gp"
>>> eff_name = "DrainEff"
>>> gain = pwdt.Var([10.0], name=gain_name)
>>> eff = pwdt.Var([50], name=eff_name)
```

## Create a LoadPullBlock[](#create-a-loadpullblock "Link to this heading")

The [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") class in pwdatatools is a powerful object that stores and manipulates load pull data. Its capabilities are a superset of the generic [`Block`](../../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") class. To create a LoadPullBlock, we utilize a function from the `pwdatatools.examples.loadpull` module. You can see the source code for this function in the module. The function creates a DataFrame with the data and an index, and then creates a LoadPullBlock from the DataFrame. It uses the nominal gain and efficiency values to make points that vary with the magnitude of gamma such that gain increases with increasing gamma magnitude, and efficiency decreases vs. increasing gamma magnitude.

```
>>> from keysight.pwdatatools.examples import loadpull as lp_examples
>>> lpblock = lp_examples.make_swept_gamma_loadpullblock(gamma, gain, eff)
>>> print(lpblock)
LoadPullBlock(
    <'Gp', 'DrainEff', ... with 9 observations>,
    name='example',
    gamma_ivarname='GammaLoad',
    attrs={},
)
```

## Explore the data[](#explore-the-data "Link to this heading")

Let’s use the LoadPullBlock’s [`LoadPullBlock.varnames`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.varnames.md#keysight.pwdatatools.LoadPullBlock.varnames "keysight.pwdatatools.LoadPullBlock.varnames") attribute to view the variable names. Note that there is a variable called “iGammaLoad”. This is called an “index” variable, or “idx” variable, because it serves as an index for GammaLoad. LoadPullBlocks always include an integer index for the swept gamma (or swept z). Integer-based indexing is more robust than using complex or float data as indexes because it avoids floating point precision issues. The default naming convention the pwdatatools uses for idx variables is “i” + “varname”, where varname is the name of the variable associated with the idx.

```
>>> print(lpblock.varnames)
('iGammaLoad', 'GammaLoad', 'Gp', 'DrainEff')
```

To access any variable, you can use square brackets indexing directly on the LoadPullBlock object. Let’s access the gamma variable. An instance of [`Var`](../../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") is returned.

```
>>> gamma = lpblock[gamma_ivarname]
>>> print(gamma)
Var(
    <Complex128 data with shape (9,)>,
    name='GammaLoad',
    dims=<empty Dims>,
    role='gamma',
    unit=None,
    attrs={},
)
```

Note that the gamma Var has the role of “gamma”. This is because when we initialized the LoadPullBlock, we passed in the name of the gamma ivar. The LoadPullBlock automatically assigns the role of “gamma”.

There are many Python libraries for plotting, but this demo uses matplotlib, seaborn, and `keysight.pwdatatools.viz`. The `keysight.pwdatatools.viz` module builds on matplotlib and seaborn and provides additional functionality and conveniences. For example, the [`keysight.pwdatatools.viz.draw_smith_chart()`](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.draw_smith_chart.md#keysight.pwdatatools.viz.draw_smith_chart "keysight.pwdatatools.viz.draw_smith_chart") function draws a Smith chart on a matplotlib Axes. The [`keysight.pwdatatools.viz.use_keysight_theme()`](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.use_keysight_theme.md#keysight.pwdatatools.viz.use_keysight_theme "keysight.pwdatatools.viz.use_keysight_theme") function sets the matplotlib rcParams to use the Keysight color theme. The [`keysight.pwdatatools.viz.contourplot()`](../../api_reference/public_submodules/viz/_autosummary/keysight.pwdatatools.viz.contourplot.md#keysight.pwdatatools.viz.contourplot "keysight.pwdatatools.viz.contourplot") function and the [`LoadPullBlock.contourplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md#keysight.pwdatatools.LoadPullBlock.contourplot "keysight.pwdatatools.LoadPullBlock.contourplot") method provide some conveniences for contour plotting beyond those available in matplotlib alone. But, using the plotting features in `keysight.pwdatatools` is optional.

First, let’s import the viz module and activate the Keysight color theme.

```
>>> from keysight.pwdatatools import viz
>>> viz.use_keysight_theme()
```

Now, let’s plot gamma as a scatterplot using the [`LoadPullBlock.gamma_ivar_scatterplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot.md#keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot "keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot") method.

```
>>> import matplotlib.pyplot as plt
>>> fig, ax = plt.subplots()
>>> viz.draw_smith_chart(ax=ax)
>>> lpblock.gamma_ivar_scatterplot(ax=ax)
>>> ax.set_title("Gamma Points")
>>> plt.show()
```

[![../../_images/gamma_points_plot.png](../../_images/gamma_points_plot.png)](../../_images/gamma_points_plot.png)

We can plot gain and efficiency vs. gamma magnitude.

```
>>> gamma_mag = lpblock.gamma_ivar("mag")
>>> fig, axs = plt.subplots(1, 2, figsize=(11, 4))
>>> axs[0].set_title("GainP vs. Gamma Magnitude")
>>> axs[1].set_title("Efficiency vs. Gamma Magnitude")
>>> sns.lineplot(lpblock, x=gamma_mag, y=gain_name, ax=axs[0])
>>> sns.lineplot(lpblock, x=gamma_mag, y=eff_name, ax=axs[1])
>>> plt.show()
```

[![../../_images/simple_swept_gamma_gain_eff_vs_gamma_mag.png](../../_images/simple_swept_gamma_gain_eff_vs_gamma_mag.png)](../../_images/simple_swept_gamma_gain_eff_vs_gamma_mag.png)

We can see from the plots that gain increases linearly with increasing gamma magnitude, while efficiency decreases linearly with increasing gamma magnitude. This is simply because the `make_swept_gamma_loadpullblock()` function constructs the data in this way.

Next, let’s plot gain and efficiency contour plots using the [`LoadPullBlock.contourplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md#keysight.pwdatatools.LoadPullBlock.contourplot "keysight.pwdatatools.LoadPullBlock.contourplot") method. This method returns a `matplotlib.QuadContourSet` object. We also use the `matplotlib.pyplot.clabel()` function to add labels to the contour lines. From the plots, we can see that the nominal gain and efficiency values are at the center of the Smith chart, and that gain increases as we move away from the center, while efficiency decreases as we move away from the center.

```
>>> fig, axs = plt.subplots(1, 2, figsize=(10, 5))
>>> axs[0].set_title("GainP Contour")
>>> viz.draw_smith_chart(ax=axs[0])
>>> cs_gain = lpblock.contourplot(gain_name, ax=axs[0], colors="blue")
>>> plt.clabel(cs_gain, inline=True, fontsize=10, fmt="%.1f")
>>> axs[1].set_title("Efficiency Contour")
>>> viz.draw_smith_chart(ax=axs[1])
>>> cs_eff = lpblock.contourplot(eff_name, ax=axs[1], colors="blue")
>>> plt.clabel(cs_eff, inline=True, fontsize=10)
>>> plt.show()
```

[![../../_images/simple_swept_gamma_gain_eff_contour.png](../../_images/simple_swept_gamma_gain_eff_contour.png)](../../_images/simple_swept_gamma_gain_eff_contour.png)

## Grid the data[](#grid-the-data "Link to this heading")

Let’s explore the concept of a “grid” in LoadPullBlock. A load pull grid is always a 2-dimensional gamma or impedance grid. There are two possible coordinate systems: rectangular and polar. The gamma/impedance values must be regularly-spaced to be considered “gridded”. Also, the data must contain the same number of y points for each x point. For a rectangular coordinate system, x and y are the real and imaginary parts of gamma/impedance, respectively. For polar coordinate systems, x and y are magnitude and phase. Is our LoadPullBlock gridded? Let’s use the [`LoadPullBlock.is_gridded()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.is_gridded.md#keysight.pwdatatools.LoadPullBlock.is_gridded "keysight.pwdatatools.LoadPullBlock.is_gridded") method to find out.

```
>>> print(f"LoadPullBlock is gridded: {lpblock.is_gridded()}")
LoadPullBlock is gridded: True
```

Let’s view information about the grid using the LoadPullblock’s [`LoadPullBlock.get_grid()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_grid.md#keysight.pwdatatools.LoadPullBlock.get_grid "keysight.pwdatatools.LoadPullBlock.get_grid") method. This method returns an instance of [`Grid`](../../api_reference/loadpull/grid/index.md#keysight.pwdatatools.Grid "keysight.pwdatatools.Grid"), which contains information about the grid. We can readily see the grid’s coordinate system, extents, and number of points in x and y.

```
>>> grid = lpblock.get_grid()
>>> print(grid)
Grid(
    coord_system='rect',
    extents=<xmin=0.0, xmax=0.5, ymin=0.0, ymax=0.5>,
    npointsx=3,
    npointsy=3
)
```

Let’s create another [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock"), but this time we pass in gamma points that are not regularly-spaced in the rectangular coordinate system.

```
>>> gamma_real_points = [0, 0.25, 0.5]
>>> gamma_imag_points = [0, 0.35, 0.5]
>>> gamma_points_ungridded = []
>>> for real_point, imag_point in itertools.product(gamma_real_points, gamma_imag_points):
...     gamma_points_ungridded.append(real_point + 1j * imag_point)
>>> print(gamma_points_ungridded)
[0j, 0.35j, 0.5j, (0.25+0j), (0.25+0.35j), (0.25+0.5j), (0.5+0j), (0.5+0.35j), (0.5+0.5j)]
>>> gamma_ungridded = pwdt.Var(gamma_points_ungridded, name="GammaLoad")
>>> lpblock_ungridded = lp_examples.make_swept_gamma_loadpullblock(
...     gamma_ungridded, gain, eff
... )
```

If we plot the gamma points, we can see that they are not regularly-spaced. Therefore, these gammas are not considered gridded.

```
>>> fig, ax = plt.subplots()
>>> viz.draw_smith_chart(ax=ax)
>>> lpblock_ungridded.gamma_ivar_scatterplot(ax=ax)
>>> ax.set_title("Ungridded Gamma Points")
>>> plt.show()
```

[![../../_images/simple_swept_gamma_ungridded_gamma_points.png](../../_images/simple_swept_gamma_ungridded_gamma_points.png)](../../_images/simple_swept_gamma_ungridded_gamma_points.png)

And if we check if the LoadPullBlock is gridded, we can see that it is not.

```
>>> print(f"lpblock_ungridded is gridded: {lpblock_ungridded.is_gridded()}")
lpblock_ungridded is gridded: False
```

When we try to get the Grid object for `lpblock_ungridded`, we get `None` instead.

```
>>> grid = lpblock_ungridded.get_grid()
>>> print(grid)
None
```

Let’s create a new gridded LoadPullBlock from our ungridded LoadPullBlock. We use the [`LoadPullBlock.grid_data()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md#keysight.pwdatatools.LoadPullBlock.grid_data "keysight.pwdatatools.LoadPullBlock.grid_data") method to do this.

```
>>> lpblock_gridded = lpblock.grid_data("rect")
```

Let’s make a plot to compare the gridded and ungridded gamma points.

```
>>> fig, axs = plt.subplots()
>>> viz.draw_smith_chart(ax=axs)
>>> lpblock_ungridded.gamma_ivar_scatterplot(ax=axs, color="blue", label="Ungridded")
>>> lpblock_gridded.gamma_ivar_scatterplot(ax=axs, color="red", label="Gridded")
>>> axs.set_title("Gamma Points")
>>> plt.show()
```

[![../../_images/simple_swept_gamma_gridded_gamma_points.png](../../_images/simple_swept_gamma_gridded_gamma_points.png)](../../_images/simple_swept_gamma_gridded_gamma_points.png)

We can see the grid that was generated is 8 x 8. Note that the grid covers a smaller area of the Smith chart. This is because, by default, the outermost grid points are not included in the final gridded data. This is to avoid edge effects where interpolation is unreliable.

Let’s compare the gridded and ungridded data. If we plot gain and efficiency vs. magnitude of gamma, we can see the lineplots of the gridded and ungridded responses match well.

```
>>> gridded_gamma_mag = lpblock_gridded.gamma_ivar("mag")
>>> ungridded_gamma_mag = lpblock_ungridded.gamma_ivar("mag")
>>> fig, axs = plt.subplots(1, 2, figsize=(10, 5))
>>> axs[0].set_title("GainP vs. Gamma Magnitude")
>>> sns.lineplot(
...     data=lpblock_ungridded,
...     x=ungridded_gamma_mag,
...     y=gain_name,
...     label="Ungridded",
...     marker="o",
...     markersize=8,
...     ax=axs[0],
... )
>>> sns.lineplot(
...     data=lpblock_gridded,
...     x=gridded_gamma_mag,
...     y=gain_name,
...     label="Gridded",
...     marker="o",
...     alpha=0.5,
...     ax=axs[0],
... )
>>> axs[1].set_title("Efficiency vs. Gamma Magnitude")
>>> sns.lineplot(
...     data=lpblock_ungridded,
...     x=ungridded_gamma_mag,
...     y=eff_name,
...     label="Ungridded",
...     marker="o",
...     markersize=8,
...     ax=axs[1],
... )
>>> sns.lineplot(
...     data=lpblock_gridded,
...     x=gridded_gamma_mag,
...     y=eff_name,
...     label="Gridded",
...     marker="o",
...     alpha=0.5,
...     ax=axs[1],
... )
>>> plt.show()
```

[![../../_images/simple_swept_gamma_gridded_vs_ungridded.png](../../_images/simple_swept_gamma_gridded_vs_ungridded.png)](../../_images/simple_swept_gamma_gridded_vs_ungridded.png)

The densely-sampled and evenly-spaced gridded responses were interpolated from the sparse and irregular ungridded data. The fact that the trend lines are similar means the [`LoadPullBlock.grid_data()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md#keysight.pwdatatools.LoadPullBlock.grid_data "keysight.pwdatatools.LoadPullBlock.grid_data") method was able to accurately interpolate. The gridded responses do not cover as wide a range of gamma magnitudes as the ungridded responses. Remember, this is because the outermost grid points are not included in the final gridded data. In the range where we have smaller gamma magnitudes, the gridded data loses a bit of accuracy. This because the ungridded data is even more sparse in this area, making interpolation more challenging.

## Send data to ADS[](#send-data-to-ads "Link to this heading")

Let’s demonstrate how to get this data into PathWave Advanced Design System (ADS). We use the [`LoadPullBlock.to_adscontourblock()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_adscontourblock.md#keysight.pwdatatools.LoadPullBlock.to_adscontourblock "keysight.pwdatatools.LoadPullBlock.to_adscontourblock") method to do this. This method returns an `ADSContourBlock` object, which is a specialized type of Block class dedicated to arranging data in a way that is friendly to ADS contour plotting. Note that we are sending over the gridded data, not the ungridded data. This is because data must be gridded in order to plot contours in ADS. We are writing the dataset to a workspace’s data folder `WRK_DATA_FOLDER`, whose definition exists in the example script but is not shown here.

```
>>> adsblock_gridded = lpblock_gridded.to_adscontourblock()
>>> adsblock_gridded.to_file(WRK_DATA_FOLDER / "gamma_sweep.ds", dst_mode="w")
```

You can also directly write out a LoadPullBlock to an ADS dataset.

```
>>> lpblock_gridded.to_file(WRK_DATA_FOLDER / "gamma_sweep_block.ds", dst_mode="w")
```

Important

If you get a PermissionError when writing an ADS dataset, it is likely because the ADS Data Display window is open and accessing the dataset file you are trying to write. If this happens, you must close the ADS Data Display window and try running your script again.

See also

There is an accompanying ADS workspace that shows how to plot contours in ADS Data Display using this dataset. The workspace is on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools).


---

<!-- === 来源: examples/loadpull/swept_gamma_power_example.md === -->

# Swept Gamma and Power[](#swept-gamma-and-power "Link to this heading")

This example demonstrates how to work with load pull data with swept gamma and power. It is a very common type of load pull sweep.

See also

All Python scripts and data files for the load pull examples are located on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

## Perform all imports[](#perform-all-imports "Link to this heading")

First, let’s import all the necessary modules. There are many Python libraries for plotting, but this example uses matplotlib, seaborn, and `pwdatatools.viz`. The `viz` module builds off matplotlib and seaborn to provide additional functionality. Also, we need the `pwdatatools.examples.loadpull` module to create the loadpull data. This example requires pwdatatools version 0.6.0 or later.

```
>>> import itertools
>>> import os
>>> from pathlib import Path
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> from keysight import pwdatatools as pwdt
>>> from keysight.pwdatatools import viz
>>> from keysight.pwdatatools.examples import loadpull as lp_examples
```

## Create the data[](#create-the-data "Link to this heading")

Let’s generate the data that we will use. First, let’s define the unique gamma and power points. These are the independent variables (ivars). We use `itertools.product()` to compute the cartesian product, which gives us all combinations of real and imaginary gamma points.

```
>>> gamma_real_points = [0, 0.25, 0.5]
>>> gamma_imag_points = [0, 0.25, 0.5]
>>> gamma_points = []
>>> for real_point, imag_point in itertools.product(gamma_real_points, gamma_imag_points):
...     gamma_points.append(real_point + 1j * imag_point)
>>> print(gamma_points)
[0j, 0.25j, 0.5j, (0.25+0j), (0.25+0.25j), (0.25+0.5j), (0.5+0j), (0.5+0.25j), (0.5+0.5j)]
>>> power_points = [-20.0, -10, -5, 0.0]
```

Next, we define the names of the ivars and create a [`Var`](../../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") for each.

```
>>> gamma_ivarname = "GammaLoad"
>>> gamma = pwdt.Var(gamma_points, name=gamma_ivarname)
>>> power_ivarname = "PSource"
>>> power = pwdt.Var(power_points, name=power_ivarname)
```

Now that we have the ivars handled, let’s create the dependent variables (dvars). We create two dvars: gain and efficiency. We only need to define nominal curves vs. power. These nominal curves will be modified to produce different values at each gamma. Each gain or efficiency value corresponds to a power value, so the nominal curves need to be the same length as the power points (in this example, the length is 4).

```
>>> gain_name = "Gp"
>>> eff_name = "DrainEff"
>>> gain_nominal = pwdt.Var([10, 10, 9, 8], name=gain_name)
>>> eff_nominal = pwdt.Var([50, 51, 48, 46], name=eff_name)
```

## Create a LoadPullBlock[](#create-a-loadpullblock "Link to this heading")

Now that we have all the variables ready, let’s create a [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock"). LoadPullBlock is a specialized Block class that is a superset of the generic [`Block`](../../api_reference/main/block/index.md#keysight.pwdatatools.Block "keysight.pwdatatools.Block") class and contains additional functionality for working with load pull data. We use the `make_swept_gamma_power_loadpullblock()` function, which is part of the `keysight.pwdatatools.examples.loadpull` module, to create a LoadPullBlock.

```
>>> lpblock = lp_examples.make_swept_gamma_power_loadpullblock(
...     gamma, power, gain_nominal, eff_nominal
... )
>>> print(lpblock)
LoadPullBlock(
    <'Gp', 'DrainEff', ... with 36 observations>,
    name='example',
    gamma_ivarname='GammaLoad',
    power_ivarname='PSource',
    attrs={},
)
```

## Explore the variables[](#explore-the-variables "Link to this heading")

Let’s print the names of the independent variables (ivars), the dependent variables (dvars), and the index variables (idxs).

```
>>> print(f"ivars: {lpblock.ivarnames}")
ivars: ('GammaLoad', 'PSource')
>>> print(f"dvars: {lpblock.dvarnames}")
dvars: ('Gp', 'DrainEff')
>>> print(f"idxs: {lpblock.idxnames}")
idxs: ('iGammaLoad', 'iPSource')
```

There are two idxs: one for gamma and one for power. The idxs always contain integer data, and are typically named “i” + “varname” (where “varname” is the name of the variable with which the idx is associated). The idxs help with iterating over the combinations of the ivars’ values, avoiding floating point precision issues.

We can get variables from the LoadPullBlock using the [`LoadPullBlock.__getitem__()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.__getitem__.md#keysight.pwdatatools.LoadPullBlock.__getitem__ "keysight.pwdatatools.LoadPullBlock.__getitem__") method. This returns a [`Var`](../../api_reference/main/var/index.md#keysight.pwdatatools.Var "keysight.pwdatatools.Var") object.

```
>>> print(lpblock["GammaLoad"])
Var(
    <Complex128 data with shape (36,)>,
    name='GammaLoad',
    dims=<empty Dims>,
    role='gamma',
    unit=None,
    attrs={},
)
>>> print(lpblock["PSource"])
Var(
    <Float64 data with shape (36,)>,
    name='PSource',
    dims=<empty Dims>,
    role='power',
    unit=None,
    attrs={},
)
```

Note that the gamma variable has the role of “gamma” and the power variable has the role of “power”. These roles were assigned to the variables when the LoadPullBlock was created.

Before we start plotting, let’s activate a color theme. This is an optional step that applies Keysight’s color theme to all charts created by matplotlib and seaborn.

```
>>> viz.use_keysight_theme()
```

Let’s plot gain and efficency. We use the [`LoadPullBlock.gamma_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar.md#keysight.pwdatatools.LoadPullBlock.gamma_ivar "keysight.pwdatatools.LoadPullBlock.gamma_ivar") method to get the gamma variable, converting it to polar string form. This form works well for legend labels. We use these labels to set the hue of the plot. The hue parameter will trigger seaborn to create separate lines with distinct colors for each gamma.

```
>>> fig, axs = plt.subplots(1, 2, figsize=(12, 4))
>>> gamma_label = lpblock.gamma_ivar("polar_str")
>>> axs[0].set_title("GainP vs. Power")
>>> sns.lineplot(data=lpblock, x="PSource", y="Gp", hue=gamma_label, ax=axs[0])
>>> axs[0].legend(bbox_to_anchor=(2, -0.2), title="GammaLoad", ncols=5)
>>> axs[1].set_title("Efficiency vs. Power")
>>> sns.lineplot(data=lpblock, x="PSource", y="DrainEff", ax=axs[1], hue=gamma_label, legend=False)
>>> plt.show()
```

[![../../_images/simple_gamma_power_gain_eff_plot.png](../../_images/simple_gamma_power_gain_eff_plot.png)](../../_images/simple_gamma_power_gain_eff_plot.png)

Let’s plot the gamma points on a Smith chart using the [`LoadPullBlock.gamma_ivar_scatterplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot.md#keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot "keysight.pwdatatools.LoadPullBlock.gamma_ivar_scatterplot") method.

```
>>> fig, ax = plt.subplots()
>>> ax.set_title("Gamma Points")
>>> viz.draw_smith_chart(ax)
>>> lpblock.gamma_ivar_scatterplot(ax=ax)
>>> plt.show()
```

[![../../_images/gamma_points_plot.png](../../_images/gamma_points_plot.png)](../../_images/gamma_points_plot.png)

## Calculate gain compression[](#calculate-gain-compression "Link to this heading")

Let’s calculate gain compression points using the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp"). This method returns a new LoadPullBlock with the power dependency removed (since the data now only has a single power for each gamma). The default behavior is to add the gain compression as an outer independent variable (outer ivar) and to add a new column and integer index to the DataFrame corresponding to values of gain compression. By default, extrapolation is not performed. This means that if the requested gain compression value is not within the limits of the data, then the `fill_value` is used to fill in the data point (which defaults to `numpy.nan`. Here, we set the `extrap` argument to `True` to allow extrapolation, which is needed for the 3dB gcomp value.

```
>>> gcomp_values = [1.0, 2.0, 3.0]
>>> lpblock_at_gcomp = lpblock.at_gcomp(gcomp_values, "Gp", extrap=True)
>>> print(lpblock_at_gcomp)
LoadPullBlock(
    <'PSource', 'Gp', 'DrainEff', ... with 27 observations>,
    name='example',
    gamma_ivarname='GammaLoad',
    outer_ivarnames=('Gp_comp',),
    outer_idxnames=('iGp_comp',),
    attrs={},
)
```

Now, let’s plot the gain compression points along the gain and efficiency curves.

```
>>> gcomp_values_str = ", ".join([str(x) for x in gcomp_values])
>>> fig, axs = plt.subplots(1, 2, figsize=(12, 4))
>>> fig.suptitle(
...     f"GainP and Efficiency with Points at gcomp Values of {gcomp_values_str}",
...     fontsize=16,
... )
>>> gamma_label = lpblock.gamma_ivar("polar_str")
>>> gamma_label_at_gcomp = lpblock_at_gcomp.gamma_ivar("polar_str")
>>> sns.lineplot(
...     data=lpblock,
...     x="PSource",
...     y="Gp",
...     ax=axs[0],
...     hue=gamma_label,
... )
>>> sns.scatterplot(
...     data=lpblock_at_gcomp,
...     x="PSource",
...     y="Gp",
...     ax=axs[0],
...     hue=gamma_label_at_gcomp,
...     legend=False,
... )
>>> sns.lineplot(
...     data=lpblock,
...     x="PSource",
...     y="DrainEff",
...     ax=axs[1],
...     hue=gamma_label,
...     legend=False,
... )
>>> sns.scatterplot(
...    data=lpblock_at_gcomp,
...     x="PSource",
...     y="DrainEff",
...     ax=axs[1],
...     hue=lpblock_at_gcomp.gamma_ivar("polar_str"),
...     legend=False,
... )
>>> axs[0].legend(bbox_to_anchor=(2, -0.2), title="GammaLoad", ncols=5)
>>> plt.show()
```

[![../../_images/simple_gamma_power_gcomp_plot.png](../../_images/simple_gamma_power_gcomp_plot.png)](../../_images/simple_gamma_power_gcomp_plot.png)

You can see from the plots that the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method extrapolated past the last gain data point to find the gain compression point. The [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method automatically interpolates as needed.

## Calculate responses at specified power levels[](#calculate-responses-at-specified-power-levels "Link to this heading")

The LoadPullBlock class has a method called [`LoadPullBlock.at_power()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md#keysight.pwdatatools.LoadPullBlock.at_power "keysight.pwdatatools.LoadPullBlock.at_power") that can be used to calculate the responses at specific power level(s). This method is similar to the [`LoadPullBlock.at_gcomp()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_gcomp.md#keysight.pwdatatools.LoadPullBlock.at_gcomp "keysight.pwdatatools.LoadPullBlock.at_gcomp") method, but instead of calculating the responses at gain compression level(s), it calculates the responses at specific power level(s). The power variable that you use to specify the power levels can be **any variable** in the LoadPullBlock; it doesn’t have to be the swept power independent variable. So, using this method, you could calculate all responses at specified PLoad values. The default behavior is to assign whichever power col is being used to the role of power\_ivar, and to add an integer index to the DataFrame corresponding to values of power.

Let’s calculate the responses at a few power levels. We use the [`LoadPullBlock.at_power()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.at_power.md#keysight.pwdatatools.LoadPullBlock.at_power "keysight.pwdatatools.LoadPullBlock.at_power") method to calculate the responses at -18 dBm, -10 dBm, and -2 dBm. In order to obtain the data at -18 dBm, interpolation must be used. To get the response values at -2 dBm, extrapolation must be used. For the responses at -10 dBm, the data is available in the LoadPullBlock, so no interpolation or extrapolation is needed.

```
>>> power_values = [-18, -10.0, 2]
>>> power_col = "PSource"
>>> lpblock_at_power = lpblock.at_power(
...      power_values, power_col, extrap=True, interp_method="linear", extrap_method="linear"
... )
>>> print(lpblock_at_power)
LoadPullBlock(
    <'Gp', 'DrainEff', ... with 27 observations>,
    name='example',
    gamma_ivarname='GammaLoad',
    power_ivarname='PSource',
    attrs={},
)
```

Plotting the responses calculated at different power levels is similar to plotting at specified gain compression levels. We can do it with minor tweaks to the code we used previously. The code is not shown here, but the resulting plots are shown below.

See also

You can find all the code here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

[![../../_images/simple_gamma_power_at_power_plot.png](../../_images/simple_gamma_power_at_power_plot.png)](../../_images/simple_gamma_power_at_power_plot.png)

## Create contour plots[](#create-contour-plots "Link to this heading")

Let’s plot gain and efficiency contours. We can utilize the [`LoadPullBlock.contourplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md#keysight.pwdatatools.LoadPullBlock.contourplot "keysight.pwdatatools.LoadPullBlock.contourplot") method to create contour plots. It provides additional conveniences beyond matplotlib’s `Axes.contour()` method, but if you prefer, you could use that method instead. Generally, you can pick either rectangular or Smith charts for these types of plots. So, just for demonstration purposes, the gain contours are plotted on Smith charts and the efficiency contours are plotted on rectangular charts. We are plotting contours at each gain compression level from the `lpblock_at_gcomp` object, but we could have just as easily plotted contours at each power level from the `lpblock_at_power` object. Note how `lpblock_at_gcomp` is filtered during each iteration of the for-loop with the [`LoadPullBlock.keep_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.keep_observations.md#keysight.pwdatatools.LoadPullBlock.keep_observations "keysight.pwdatatools.LoadPullBlock.keep_observations") method in order to create a new LoadPullBlock containing only the data for a single gain compression level. Getting rid of the swept outer ivar Gp\_comp allows the [`LoadPullBlock.contourplot()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.contourplot.md#keysight.pwdatatools.LoadPullBlock.contourplot "keysight.pwdatatools.LoadPullBlock.contourplot") method to work correctly.

```
>>> fig_gain, axs_gain = plt.subplots(1, len(gcomp_values), figsize=(12, 4))
>>> fig_gain.suptitle("GainP Contours at Different Compression Levels", fontsize=20)
>>> fig_eff, axs_eff = plt.subplots(1, len(gcomp_values), figsize=(12, 4))
>>> fig_eff.suptitle(
...     "Efficiency Contours at Different GainP Compression Levels", fontsize=20
... )
>>> for i, gcomp_value in enumerate(gcomp_values):
...     viz.draw_smith_chart(axs_gain[i])
...     lpblock_at_single_gcomp = lpblock_at_gcomp.keep_observations(
...         lpblock_at_gcomp["iGp_comp"] == i
...     )
...     cs_gain = lpblock_at_single_gcomp.contourplot(
...         "Gp", ax=axs_gain[i], levels=5, colors="red"
...     )
...     axs_gain[i].clabel(cs_gain, fmt="%1.1f")
...     axs_gain[i].set_title(f"Gp_comp = {gcomp_value}")
...     fig_gain.tight_layout()
...     cs_eff = lpblock_at_single_gcomp.contourplot(
...         "DrainEff", ax=axs_eff[i], colors="blue"
...     )
...     axs_eff[i].clabel(cs_eff, fontsize=11)
...     axs_eff[i].set_title(f"Gp_comp = {gcomp_value}")
...     fig_eff.tight_layout()
>>> plt.show()
```

[![../../_images/simple_gamma_power_gain_contours_vs_gcomp.png](../../_images/simple_gamma_power_gain_contours_vs_gcomp.png)](../../_images/simple_gamma_power_gain_contours_vs_gcomp.png)
[![../../_images/simple_gamma_power_eff_contours_vs_gcomp.png](../../_images/simple_gamma_power_eff_contours_vs_gcomp.png)](../../_images/simple_gamma_power_eff_contours_vs_gcomp.png)

## Regularize power[](#regularize-power "Link to this heading")

It is common for data to contain irregular power sweeps, which means that the swept power values are not exactly the same at each gamma. There are certain scenarios where we want to ensure that the swept power is regular across all gamma values. The [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method can be used to regularize irregular power sweeps. Additionally, the [`LoadPullBlock.has_regular_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar.md#keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar "keysight.pwdatatools.LoadPullBlock.has_regular_power_ivar") method is useful to check if the power sweeps are regular. Let’s check if the power sweeps in our example LoadPullBlocks are regular.

```
>>> print(f"lpblock has regular power: {lpblock.has_regular_power_ivar()}")
lpblock has regular power: True
>>> print(f"lpblock_at_power has regular power: {lpblock_at_power.has_regular_power_ivar()}")
lpblock_at_power has regular power: True
>>> print(f"lpblock_at_gcomp has regular power: {lpblock_at_gcomp.has_regular_power_ivar()}")
<raises ValueError because lpblock_at_gcomp does not have swept power>
```

So, our original [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object has regular power sweeps, as does our `lpblock_at_power` object. But the `lpblock_at_gcomp` object cannot be checked because it no longer has a power sweep. Let’s create a new LoadPullBlock by creating a LoadPullBlock with irregular power sweeps. Let’s drop two observations of data using the [`LoadPullBlock.drop_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_observations.md#keysight.pwdatatools.LoadPullBlock.drop_observations "keysight.pwdatatools.LoadPullBlock.drop_observations") method.

```
>>> gamma_idx = lpblock["iGammaLoad"]
>>> power_idx = lpblock["iPSource"]
>>> lpblock_irreg = lpblock.drop_observations(
...     (gamma_idx == 0) & (power_idx == 2) | (gamma_idx == 8) & (power_idx == 3),
... )
>>> print(lpblock_irreg.has_regular_power_ivar())
False
```

Let’s plot gamma vs power to help visualize regular and irregular power sweeps. We see there are two missing points in the irregular power sweeps.

```
>>> fig, axs = plt.subplots(1, 3, sharey=True, figsize=(7, 3))
>>> fig.suptitle("Gamma vs Power", fontsize=14)
>>> axs[0].set_title("lpblock (regular)", fontsize=10)
>>> axs[1].set_title("lpblock_at_power (regular)", fontsize=10)
>>> axs[2].set_title("lpblock_irreg (irregular)", fontsize=10)
>>> gamma_label = lpblock.gamma_ivar("polar_str")
>>> gamma_label_at_power = lpblock_at_power.gamma_ivar("polar_str")
>>> gamma_label_irreg = lpblock_irreg.gamma_ivar("polar_str")
>>> sns.scatterplot(data=lpblock, x="PSource", y=gamma_label, ax=axs[0])
>>> sns.scatterplot(data=lpblock_at_power, x="PSource", y=gamma_label_at_power, ax=axs[1])
>>> sns.scatterplot(data=lpblock_irreg, x="PSource", y=gamma_label_irreg, ax=axs[2])
>>> fig.tight_layout()
>>> plt.show()
```

[![../../_images/simple_gamma_power_gamma_vs_power_reg_vs_irreg.png](../../_images/simple_gamma_power_gamma_vs_power_reg_vs_irreg.png)](../../_images/simple_gamma_power_gamma_vs_power_reg_vs_irreg.png)

Now, let’s regularize the power sweeps in `lpblock_irreg` by calling the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method. This method will create a new [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") instance with the regularized power sweeps, leaving the original [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object unchanged.

Note

This is how most of the LoadPullBlock methods work; they return a new instance of LoadPullBlock. You can choose to store the new instance in a new variable, or you can store it in the same variable. The latter is useful if don’t you need to keep the original LoadPullBlock object.

We explicitly define the power points that we want to use for the regular power sweeps. This is optional because the [`LoadPullBlock.regularize_power_ivar()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.regularize_power_ivar.md#keysight.pwdatatools.LoadPullBlock.regularize_power_ivar "keysight.pwdatatools.LoadPullBlock.regularize_power_ivar") method is able to automatically determine power points to use. In this simple example, we can easily specify the power points, which helps reduce the amount of interpolation we need to perform. However, usually real measured load pull data will contain enough power points at each gamma to make this unnecessary. We are also explicitly specifying the interpolation and extrapolation methods as “linear”. The defaults are “cubic” for both, which usually works well. However, our simple data doesn’t contain enough power points at each gamma to use “cubic”. We are also specifying that we want to extrapolate the power sweeps. The default value for `extrap` is `False`.

```
>>> lpblock_reg = lpblock_irreg.regularize_power_ivar(
...     points=[-20, -10, -5, 0],
...     interp_method="linear",
...     extrap_method="linear",
...     extrap=True,
...)
>>> print(f"lpblock_reg has regular power: {lpblock_reg.has_regular_power_ivar()}")
lpblock_reg has regular power: True
```

Now let’s compare the irregular and regularized gain and efficiency plots. The code to generate the below plots is not shown here, but it is available on the Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools)

[![../../_images/simple_gamma_power_gain_vs_power_irreg_vs_reg_plot.png](../../_images/simple_gamma_power_gain_vs_power_irreg_vs_reg_plot.png)](../../_images/simple_gamma_power_gain_vs_power_irreg_vs_reg_plot.png)
[![../../_images/simple_gamma_power_eff_vs_power_irreg_vs_reg_plot.png](../../_images/simple_gamma_power_eff_vs_power_irreg_vs_reg_plot.png)](../../_images/simple_gamma_power_eff_vs_power_irreg_vs_reg_plot.png)

Examining the irregular plots reveals two missing points in the gain and efficiency plots (where gamma is 0 < 0 and 0.707 < 45). In the regularized plots, one of the missing points is filled by interpolation, and the other by extrapolation.

## Grid data[](#grid-data "Link to this heading")

If you do not understand the concept of “gridded” load pull data, please read [this section](../../howto/work_with_loadpull_data.md#what-is-gridded-load-pull-data) before proceeding.

Let’s check our regularized [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object to see if it is gridded.

```
>>> print(f"lpblock_reg is gridded: {lpblock_reg.is_gridded()}")
lpblock_reg is gridded: True
```

We can also get all the grid info. The [`LoadPullBlock.get_grid()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_grid.md#keysight.pwdatatools.LoadPullBlock.get_grid "keysight.pwdatatools.LoadPullBlock.get_grid") method returns a [`Grid`](../../api_reference/loadpull/grid/index.md#keysight.pwdatatools.Grid "keysight.pwdatatools.Grid") object (or `None` if the LoadPullBlock is not gridded). The [`Grid`](../../api_reference/loadpull/grid/index.md#keysight.pwdatatools.Grid "keysight.pwdatatools.Grid") object contains the coordinate system (‘rect’ or ‘polar’), the extents of the grid, and the number of x and y points. The `x` and `y` coordinates are real/imaginary for a rectangular grid, and magnitude/phase for a polar grid.

```
>>> grid = lpblock_reg.get_grid()
>>> print(f"lpblock_reg's grid:\n{grid}")
lpblock_reg's grid:
Grid(
    coord_system='rect',
    extents=<xmin=0.0, xmax=0.5, ymin=0.0, ymax=0.5>,
    npointsx=3,
    npointsy=3
)
```

What about our irregular [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") object?

```
>>> print(f"lpblock_irreg is gridded: {lpblock_irreg.is_gridded()}")
lpblock_irreg is gridded: False
>>> print(f"lpblock_irreg's grid: {lpblock_irreg.get_grid()}")
lpblock_irreg's grid: None
```

No, the `lpblock_irreg` object is not gridded because its power sweep is not regular. Notice that the [`LoadPullBlock.get_grid()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.get_grid.md#keysight.pwdatatools.LoadPullBlock.get_grid "keysight.pwdatatools.LoadPullBlock.get_grid") method returns `None` if a LoadPullBlock is not gridded.

Another requirement to be gridded is having the same number of gamma or impedance y points for each x point. To demonstrate, let’s create a new LoadPullBlock that violates this requirement. We can do this by using the [`LoadPullBlock.drop_observations()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.drop_observations.md#keysight.pwdatatools.LoadPullBlock.drop_observations "keysight.pwdatatools.LoadPullBlock.drop_observations") method to drop one of the gamma points from the original `lpblock` object. This method returns a new LoadPullBlock instance.

```
>>> lpblock_ungridded = lpblock.drop_observations(lpblock["iGammaLoad"] == 0)
>>> print(f"lpblock_ungridded's grid: {lpblock_ungridded.get_grid()}")
lpblock_ungridded's grid: None
```

Now, let’s regrid the data so that the gamma points are once again considered “gridded”. The [`LoadPullBlock.grid_data()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md#keysight.pwdatatools.LoadPullBlock.grid_data "keysight.pwdatatools.LoadPullBlock.grid_data") method is able to grid the data onto a rectangular or polar 2D grid. This method creates a new [`LoadPullBlock`](../../api_reference/loadpull/loadpullblock/index.md#keysight.pwdatatools.LoadPullBlock "keysight.pwdatatools.LoadPullBlock") instance with the gridded data.

```
>>> lpblock_gridded = lpblock_ungridded.grid_data("rect")
>>> print(f"lpblock_gridded's grid:\n{lpblock_gridded.get_grid()}")
lpblock_gridded's grid:
Grid(
    coord_system='rect',
    extents=<xmin=0.055556, xmax=0.444444, ymin=0.055556, ymax=0.444444>,
    npointsx=8,
    npointsy=8
)
```

Note how the gridded data has 64 gamma points (8x8). The original data had only 8 gamma points (we had 9 gamma points, and then removed one gamma point to make it ungridded). The [`LoadPullBlock.grid_data()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md#keysight.pwdatatools.LoadPullBlock.grid_data "keysight.pwdatatools.LoadPullBlock.grid_data") method defaults to calculating a 10x10 grid and then dropping the outermost grid points along the edges (resulting in an 8x8 grid). Dropping the points along the grid’s edges is the default behavior because interpolation doesn’t work well there. If you decide you want to keep the outermost grid points, you can set the `drop_edges` argument to `False`. You can also control the number of x and y grid points with the `npointsx` and `npointsy` parameters.

We can plot gridded and ungridded gamma in order to help us visualize the changes.

```
>>> fig, ax = plt.subplots()
>>> ax.set_title("Gamma Points")
>>> viz.draw_smith_chart(ax)
>>> lpblock_gridded.gamma_ivar_scatterplot(ax=ax, color="red", label="gridded")
>>> lpblock_ungridded.gamma_ivar_scatterplot(ax=ax, color="blue", label="ungridded")
>>> plt.show()
```

[![../../_images/gamma_points_gridded_and_ungridded_plot.png](../../_images/gamma_points_gridded_and_ungridded_plot.png)](../../_images/gamma_points_gridded_and_ungridded_plot.png)

Note how the final grid covers a smaller area of the Smith Chart than the original data. Again, this is because the [`LoadPullBlock.grid_data()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.grid_data.md#keysight.pwdatatools.LoadPullBlock.grid_data "keysight.pwdatatools.LoadPullBlock.grid_data") method is dropping the outermost grid points along the edges because interpolation doesn’t work well at the edges of the grid. If you want the final grid edges to be closer to the original data’s extents, it’s recommended to increase the `npointsx` and `npointsy` parameter values, rather than setting the `drop_edges` parameter to `False`. The gridded data at the edges is usually too unreliable.

Finally, let’s plot the gain curves for the gridded data. The code is not shown here, but it’s almost identical to the code we used previously to plot gain and efficency vs. power.

[![../../_images/simple_gamma_power_gain_eff_vs_power_gridded_plot.png](../../_images/simple_gamma_power_gain_eff_vs_power_gridded_plot.png)](../../_images/simple_gamma_power_gain_eff_vs_power_gridded_plot.png)

## Send data to ADS[](#send-data-to-ads "Link to this heading")

Let’s demonstrate how to get data into PathWave Advanced Design System (ADS). We use the [`LoadPullBlock.to_adscontourblock()`](../../api_reference/loadpull/loadpullblock/_autosummary/keysight.pwdatatools.LoadPullBlock.to_adscontourblock.md#keysight.pwdatatools.LoadPullBlock.to_adscontourblock "keysight.pwdatatools.LoadPullBlock.to_adscontourblock") method to do this. This method returns an `ADSContourBlock` object, which is a specialized type of Block class dedicated to arranging data in a way that is friendly to ADS contour plotting. We are writing several datasets to a workspace’s data folder `WRK_DATA_FOLDER`, whose definition exists in the example script but is not shown here.

```
>>> adsblock0 = lpblock_gridded.to_adscontourblock()
>>> adsblock0.to_file(WRK_DATA_FOLDER / "gamma_power_sweep.ds", dst_mode="w")
>>> adsblock1 = lpblock_at_gcomp.to_adscontourblock()
>>> adsblock1.to_file(WRK_DATA_FOLDER / "gamma_power_sweep_at_gcomp.ds", dst_mode="w")
>>> adsblock2 = lpblock_at_power.to_adscontourblock()
>>> adsblock2.to_file(WRK_DATA_FOLDER / "gamma_power_sweep_at_power.ds", dst_mode="w")
```

You can also directly write out a LoadPullBlock to an ADS dataset.

```
>>> lpblock_gridded.to_file(WRK_DATA_FOLDER / "gamma_power_sweep_block.ds", dst_mode="w")
```

Important

If you get a PermissionError when writing an ADS dataset, it is likely because the ADS Data Display window is open and accessing the dataset file you are trying to write. If this happens, you must close the ADS Data Display window and try running your script again.

See also

There is an accompanying ADS workspace that shows how to plot contours in ADS Data Display using this dataset. The workspace is on the Keysight Knowledge Center here: [How to Work with Load Pull Data Using PathWave Data Tools](https://edadocs.software.keysight.com/display/eesofkcads/How%2Bto%2BWork%2Bwith%2BLoadpull%2BData%2BUsing%2BPathWave%2BData%2BTools).


---

