# Reference
> **说明：** Reference 相关页面。

> **何时使用：** 当你需要查阅 Reference 相关内容时

---

## 本文件目录

- **Addon** (`reference/dds/app/addon.md`)
- **Callbacks** (`reference/dds/app/callbacks.md`)
- **keysight.ads.dds.app** (`reference/dds/app/index.md`)
- **Axes** (`reference/dds/axes.md`)
- **Common Properties** (`reference/dds/basic.md`)
- **Equation** (`reference/dds/equation.md`)
- **keysight.ads.dds.experimental** (`reference/dds/experimental/index.md`)
- **DDSFile** (`reference/dds/file.md`)
- **Grid** (`reference/dds/grid.md`)
- **Group** (`reference/dds/group.md`)
- **keysight.ads.dds** (`reference/dds/index.md`)
- **Legend** (`reference/dds/legend.md`)
- **Limit Lines** (`reference/dds/limitlines.md`)
- **Line Markers** (`reference/dds/linemarker.md`)
- **Markers** (`reference/dds/marker.md`)
- **Masks** (`reference/dds/masks.md`)
- **Object** (`reference/dds/objects.md`)
- **Page** (`reference/dds/page.md`)
- **Picture** (`reference/dds/picture.md`)
- **Plots** (`reference/dds/plots.md`)
- **Point** (`reference/dds/point.md`)
- **Print** (`reference/dds/print.md`)
- **PyEquation** (`reference/dds/pyequation.md`)
- **Widget** (`reference/dds/pywidget.md`)
- **Rect** (`reference/dds/rect.md`)
- **Shapes** (`reference/dds/shapes.md`)
- **Specification** (`reference/dds/specifications.md`)
- **Text** (`reference/dds/text.md`)
- **Trace** (`reference/dds/trace.md`)
- **Window** (`reference/dds/windows.md`)
- **Reference** (`reference/index.md`)

---

<!-- === 来源: reference/dds/app/addon.md === -->

# Addon[](#addon "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.dds.app.Addon[](#keysight.ads.dds.app.Addon "Link to this definition")
:   Bases: `object`

    Used to extend the functionality of ADS by adding code that is loaded at startup.

    *property* enabled*: bool*[](#keysight.ads.dds.app.Addon.enabled "Link to this definition")

    *property* location*: [AddonLocale](#keysight.ads.dds.app.AddonLocale "keysight.ads.dds.app.addon.AddonLocale")*[](#keysight.ads.dds.app.Addon.location "Link to this definition")
    :   Specifies the location of the xml configuration file that references this Addon.

    module\_name() → str[](#keysight.ads.dds.app.Addon.module_name "Link to this definition")
    :   Return the full name of the Python module for this Addon.

        Will raise an exception if this Addon does not have a Python module.

    *property* name*: str*[](#keysight.ads.dds.app.Addon.name "Link to this definition")

    *property* raw\_startup\_file*: str*[](#keysight.ads.dds.app.Addon.raw_startup_file "Link to this definition")
    :   The startup file for this Addon - possibly including environment variables.

    *property* root\_directory*: str*[](#keysight.ads.dds.app.Addon.root_directory "Link to this definition")
    :   The directory containing the startup file.

    *property* startup\_file*: str*[](#keysight.ads.dds.app.Addon.startup_file "Link to this definition")
    :   The startup file for this Addon.

    *property* sync\_location*: str*[](#keysight.ads.dds.app.Addon.sync_location "Link to this definition")

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.dds.app.AddonLocale[](#keysight.ads.dds.app.AddonLocale "Link to this definition")
:   Bases: `Enum`

    Specifies the location of the xml configuration file.

    MEMORY *= <AddonLocale.MEMORY: 0>*[](#keysight.ads.dds.app.AddonLocale.MEMORY "Link to this definition")
    :   The Addon is not stored in any file.

    USER *= <AddonLocale.USER: 1>*[](#keysight.ads.dds.app.AddonLocale.USER "Link to this definition")
    :   The Addon location in the HOME directory for Addon’s installed by the user.

    SITE *= <AddonLocale.SITE: 2>*[](#keysight.ads.dds.app.AddonLocale.SITE "Link to this definition")
    :   The Addon location for custom Addon’s installed at the user’s site.

    INSTALLATION *= <AddonLocale.INSTALLATION: 3>*[](#keysight.ads.dds.app.AddonLocale.INSTALLATION "Link to this definition")
    :   The Addon location in the product directory for Addon’s installed by ADS.

## Functions[](#functions "Link to this heading")

> keysight.ads.dds.app.add\_memory\_addon(*addon: [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")*) → None[](#keysight.ads.dds.app.add_memory_addon "Link to this definition")
> :   Add addon to the set of memory Addons (load if enabled).
>
> keysight.ads.dds.app.add\_user\_addon(*addon: [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")*) → None[](#keysight.ads.dds.app.add_user_addon "Link to this definition")
> :   Add addon to the list of user Addons (load if enabled).
>
> keysight.ads.dds.app.addon(*addon\_name: str*) → [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")[](#keysight.ads.dds.app.addon "Link to this definition")
> :   Search all the locations for an Addon with the given name.
>
>     Raises an exception if no enabled Addon was found.
>
> keysight.ads.dds.app.enable\_addon(*addon: [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")*, *enable: bool*) → [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")[](#keysight.ads.dds.app.enable_addon "Link to this definition")
> :   Enable or disable the addon.
>
>     If this is overriding the state of an installation or site
>     addon, this will return a different Addon (either a new override
>     or the original whose override we just removed).
>
> keysight.ads.dds.app.find\_addon(*addon\_name: str*) → [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon") | None[](#keysight.ads.dds.app.find_addon "Link to this definition")
> :   Search all the locations for an Addon with the given name.
>
>     Returns None if no Addon was found.
>
> keysight.ads.dds.app.import\_addon\_as\_module(*addon\_name: str*) → module[](#keysight.ads.dds.app.import_addon_as_module "Link to this definition")
> :   Import the Python module for an ADS Addon.
>
> keysight.ads.dds.app.remove\_memory\_addon(*addon: [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")*) → None[](#keysight.ads.dds.app.remove_memory_addon "Link to this definition")
> :   Remove addon from the set of memory Addons (unload if enabled).
>
> keysight.ads.dds.app.remove\_user\_addon(*addon: [Addon](#keysight.ads.dds.app.Addon "keysight.ads.dds.app.addon.Addon")*) → None[](#keysight.ads.dds.app.remove_user_addon "Link to this definition")
> :   Remove addon from the list of user Addons (unload if enabled).


---

<!-- === 来源: reference/dds/app/callbacks.md === -->

# Callbacks[](#callbacks "Link to this heading")

## Classes[](#classes "Link to this heading")

*class* keysight.ads.dds.app.FileModifiedCallback[](#keysight.ads.dds.app.FileModifiedCallback "Link to this definition")
:   Holds a callback function to be called when a file in a window is modified.

*class* keysight.ads.dds.app.PopupCallback[](#keysight.ads.dds.app.PopupCallback "Link to this definition")

*class* keysight.ads.dds.app.WindowCallback[](#keysight.ads.dds.app.WindowCallback "Link to this definition")
:   Holds a callback function to be called when a file is opened in a window.

## Enumerated Types[](#enumerated-types "Link to this heading")

*class* keysight.ads.dds.app.WindowChange[](#keysight.ads.dds.app.WindowChange "Link to this definition")
:   OPENED *= <WindowChange.OPENED: 0>*[](#keysight.ads.dds.app.WindowChange.OPENED "Link to this definition")

    CLOSED *= <WindowChange.CLOSED: 1>*[](#keysight.ads.dds.app.WindowChange.CLOSED "Link to this definition")

    SAVED\_AS *= <WindowChange.SAVED\_AS: 2>*[](#keysight.ads.dds.app.WindowChange.SAVED_AS "Link to this definition")

## Functions[](#functions "Link to this heading")

> keysight.ads.dds.app.register\_file\_modified\_callback(*cb: Callable[[[DDSFile](../file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile")], None]*) → [FileModifiedCallback](#keysight.ads.dds.app.FileModifiedCallback "keysight.ads.dds.app.callbacks.FileModifiedCallback")[](#keysight.ads.dds.app.register_file_modified_callback "Link to this definition")
>
> keysight.ads.dds.app.register\_popup\_callback(*callback: Callable[[QMenu, [DDSFile](../file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile"), [Window](../windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window"), [Point](../point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")], None]*) → [PopupCallback](#keysight.ads.dds.app.PopupCallback "keysight.ads.dds.app.callbacks.PopupCallback")[](#keysight.ads.dds.app.register_popup_callback "Link to this definition")
>
> keysight.ads.dds.app.register\_window\_callback(*cb: Callable[[[DDSFile](../file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile"), [Window](../windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window"), [WindowChange](#keysight.ads.dds.app.WindowChange "keysight.ads.dds.app.callbacks.WindowChange")], None]*) → [WindowCallback](#keysight.ads.dds.app.WindowCallback "keysight.ads.dds.app.callbacks.WindowCallback")[](#keysight.ads.dds.app.register_window_callback "Link to this definition")
>
> keysight.ads.dds.app.unregister\_file\_modified\_callback(*callback: [FileModifiedCallback](#keysight.ads.dds.app.FileModifiedCallback "keysight.ads.dds.app.callbacks.FileModifiedCallback")*) → None[](#keysight.ads.dds.app.unregister_file_modified_callback "Link to this definition")
> :   Unregister a registered file modified callback.
>
>     callback: Should be the object returned by register\_file\_modified\_callback.
>
> keysight.ads.dds.app.unregister\_popup\_callback(*callback: [PopupCallback](#keysight.ads.dds.app.PopupCallback "keysight.ads.dds.app.callbacks.PopupCallback")*) → None[](#keysight.ads.dds.app.unregister_popup_callback "Link to this definition")
>
> keysight.ads.dds.app.unregister\_window\_callback(*callback: [WindowCallback](#keysight.ads.dds.app.WindowCallback "keysight.ads.dds.app.callbacks.WindowCallback")*) → None[](#keysight.ads.dds.app.unregister_window_callback "Link to this definition")
> :   Unregister a registered file opened callback.
>
>     callback: Should be the object returned by register\_window\_callback.


---

<!-- === 来源: reference/dds/app/index.md === -->

# keysight.ads.dds.app[](#module-keysight.ads.dds.app "Link to this heading")

Data Display GUI scripting.

## Classes[](#classes "Link to this heading")

* [Addon](addon.md)
  + [Classes](addon.md#classes)
  + [Enumerated Types](addon.md#enumerated-types)
  + [Functions](addon.md#functions)
* [Callbacks](callbacks.md)
  + [Classes](callbacks.md#classes)
  + [Enumerated Types](callbacks.md#enumerated-types)
  + [Functions](callbacks.md#functions)

## Functions[](#functions "Link to this heading")

keysight.ads.dds.app.get\_pyside2\_main\_window(*window: [Window](../windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window")*) → QMainWindow | None[](#keysight.ads.dds.app.get_pyside2_main_window "Link to this definition")

keysight.ads.dds.app.is\_alt\_pressed() → bool[](#keysight.ads.dds.app.is_alt_pressed "Link to this definition")

keysight.ads.dds.app.is\_control\_pressed() → bool[](#keysight.ads.dds.app.is_control_pressed "Link to this definition")

keysight.ads.dds.app.is\_shift\_pressed() → bool[](#keysight.ads.dds.app.is_shift_pressed "Link to this definition")


---

<!-- === 来源: reference/dds/axes.md === -->

# Axes[](#axes "Link to this heading")

*class* keysight.ads.dds.AntennaIndepAxis[](#keysight.ads.dds.AntennaIndepAxis "Link to this definition")
:   The independent axis of [`AntennaPlot`](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.AntennaPlot").

    This class cannot be instantiated directly. It is automatically instantiated when an [`AntennaPlot`](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.AntennaPlot") is created.
    It is accessed by the property [`AntennaPlot.indep_axis`](plots.md#keysight.ads.dds.AntennaPlot.indep_axis "keysight.ads.dds.AntennaPlot.indep_axis").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.AntennaIndepAxis.grid_properties "Link to this definition")

    *property* is\_all\_indep\_data\_displayed*: bool*[](#keysight.ads.dds.AntennaIndepAxis.is_all_indep_data_displayed "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.AntennaIndepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.AntennaIndepAxis.label "Link to this definition")

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.AntennaIndepAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.AntennaIndepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.AntennaIndepAxis.orientation "Link to this definition")

    *property* start*: float*[](#keysight.ads.dds.AntennaIndepAxis.start "Link to this definition")

    *property* stop*: float*[](#keysight.ads.dds.AntennaIndepAxis.stop "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.AntennaIndepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.AntennaDepAxis[](#keysight.ads.dds.AntennaDepAxis "Link to this definition")
:   The dependent axis of [`AntennaPlot`](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.AntennaPlot").

    This class cannot be instantiated directly. It is automatically instantiated when an [`AntennaPlot`](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.AntennaPlot") is created.
    It is accessed by the property [`AntennaPlot.dep_axis`](plots.md#keysight.ads.dds.AntennaPlot.dep_axis "keysight.ads.dds.AntennaPlot.dep_axis").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.AntennaDepAxis.grid_properties "Link to this definition")

    *property* is\_autoscaled*: bool*[](#keysight.ads.dds.AntennaDepAxis.is_autoscaled "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.AntennaDepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.AntennaDepAxis.label "Link to this definition")

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.AntennaDepAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.AntennaDepAxis.max "Link to this definition")

    *property* min*: float*[](#keysight.ads.dds.AntennaDepAxis.min "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.AntennaDepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.AntennaDepAxis.orientation "Link to this definition")

    *property* step*: float*[](#keysight.ads.dds.AntennaDepAxis.step "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.AntennaDepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.PolarIndepAxis[](#keysight.ads.dds.PolarIndepAxis "Link to this definition")
:   The independent axis of [`PolarPlot`](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.PolarPlot").

    This class cannot be instantiated directly. It is automatically instantiated when a [`PolarPlot`](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.PolarPlot") is created.
    It is accessed by the property [`PolarPlot.indep_axis`](plots.md#keysight.ads.dds.PolarPlot.indep_axis "keysight.ads.dds.PolarPlot.indep_axis").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.PolarIndepAxis.grid_properties "Link to this definition")

    *property* is\_all\_indep\_data\_displayed*: bool*[](#keysight.ads.dds.PolarIndepAxis.is_all_indep_data_displayed "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.PolarIndepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.PolarIndepAxis.label "Link to this definition")

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.PolarIndepAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.PolarIndepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.PolarIndepAxis.orientation "Link to this definition")

    *property* start*: float*[](#keysight.ads.dds.PolarIndepAxis.start "Link to this definition")

    *property* stop*: float*[](#keysight.ads.dds.PolarIndepAxis.stop "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.PolarIndepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.PolarDepAxis[](#keysight.ads.dds.PolarDepAxis "Link to this definition")
:   The dependent axis of [`PolarPlot`](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.PolarPlot").

    This class cannot be instantiated directly. It is automatically instantiated when a [`PolarPlot`](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.PolarPlot") is created.
    It is accessed by the property [`PolarPlot.dep_axis`](plots.md#keysight.ads.dds.PolarPlot.dep_axis "keysight.ads.dds.PolarPlot.dep_axis").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.PolarDepAxis.grid_properties "Link to this definition")

    *property* is\_autoscaled*: bool*[](#keysight.ads.dds.PolarDepAxis.is_autoscaled "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.PolarDepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.PolarDepAxis.label "Link to this definition")

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.PolarDepAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.PolarDepAxis.max "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.PolarDepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.PolarDepAxis.orientation "Link to this definition")

    *property* step*: float*[](#keysight.ads.dds.PolarDepAxis.step "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.PolarDepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.RectAxis[](#keysight.ads.dds.RectAxis "Link to this definition")
:   The axes of [`RectPlot`](plots.md#keysight.ads.dds.RectPlot "keysight.ads.dds.RectPlot") and [`StackedPlot`](plots.md#keysight.ads.dds.StackedPlot "keysight.ads.dds.StackedPlot").

    This class cannot be instantiated directly. It is automatically instantiated when a [`RectPlot`](plots.md#keysight.ads.dds.RectPlot "keysight.ads.dds.RectPlot") or [`StackedPlot`](plots.md#keysight.ads.dds.StackedPlot "keysight.ads.dds.StackedPlot")
    is created. It is accessed by the properties [`RectPlot.axes`](plots.md#keysight.ads.dds.RectPlot.axes "keysight.ads.dds.RectPlot.axes") and [`StackedPlot.axes`](plots.md#keysight.ads.dds.StackedPlot.axes "keysight.ads.dds.StackedPlot.axes").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.RectAxis.grid_properties "Link to this definition")

    *property* is\_autoscaled*: bool*[](#keysight.ads.dds.RectAxis.is_autoscaled "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.RectAxis.is_grid_on "Link to this definition")

    *property* is\_logarithmic*: bool*[](#keysight.ads.dds.RectAxis.is_logarithmic "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.RectAxis.label "Link to this definition")

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.RectAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.RectAxis.max "Link to this definition")

    *property* min*: float*[](#keysight.ads.dds.RectAxis.min "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.RectAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.RectAxis.orientation "Link to this definition")

    set\_range(*min: float*, *max: float*, *step: float | None = None*) → None[](#keysight.ads.dds.RectAxis.set_range "Link to this definition")

    *property* step*: float*[](#keysight.ads.dds.RectAxis.step "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.RectAxis.string_format "Link to this definition")

*class* keysight.ads.dds.SmithChartIndepAxis[](#keysight.ads.dds.SmithChartIndepAxis "Link to this definition")
:   The independent axis of [`SmithChart`](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart").

    This class cannot be instantiated directly. It is automatically instantiated when a [`SmithChart`](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart") is created.
    It is accessed by the property [`SmithChart.indep_axis`](plots.md#keysight.ads.dds.SmithChart.indep_axis "keysight.ads.dds.SmithChart.indep_axis").

    *property* admittance\_grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.SmithChartIndepAxis.admittance_grid_properties "Link to this definition")

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.SmithChartIndepAxis.grid_properties "Link to this definition")

    *property* is\_all\_indep\_data\_displayed*: bool*[](#keysight.ads.dds.SmithChartIndepAxis.is_all_indep_data_displayed "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.SmithChartIndepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.SmithChartIndepAxis.label "Link to this definition")

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.SmithChartIndepAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.SmithChartIndepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.SmithChartIndepAxis.orientation "Link to this definition")

    *property* start*: float*[](#keysight.ads.dds.SmithChartIndepAxis.start "Link to this definition")

    *property* stop*: float*[](#keysight.ads.dds.SmithChartIndepAxis.stop "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.SmithChartIndepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.SmithChartDepAxis[](#keysight.ads.dds.SmithChartDepAxis "Link to this definition")
:   The dependent axis of [`SmithChart`](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart").

    This class cannot be instantiated directly. It is automatically instantiated when a [`SmithChart`](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart") is created.
    It is accessed by the property [`SmithChart.dep_axis`](plots.md#keysight.ads.dds.SmithChart.dep_axis "keysight.ads.dds.SmithChart.dep_axis").

    *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.SmithChartDepAxis.grid_properties "Link to this definition")

    *property* is\_autoscaled*: bool*[](#keysight.ads.dds.SmithChartDepAxis.is_autoscaled "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.SmithChartDepAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.SmithChartDepAxis.label "Link to this definition")

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.SmithChartDepAxis.label_properties "Link to this definition")

    *property* max*: float*[](#keysight.ads.dds.SmithChartDepAxis.max "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.SmithChartDepAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.SmithChartDepAxis.orientation "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.SmithChartDepAxis.string_format "Link to this definition")

*class* keysight.ads.dds.TextAxis[](#keysight.ads.dds.TextAxis "Link to this definition")
:   *property* grid\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.TextAxis.grid_properties "Link to this definition")

    *property* is\_grid\_on*: bool*[](#keysight.ads.dds.TextAxis.is_grid_on "Link to this definition")

    *property* label*: str | None*[](#keysight.ads.dds.TextAxis.label "Link to this definition")

    *property* label\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.TextAxis.label_properties "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.TextAxis.name "Link to this definition")

    *property* orientation*: AxisOrientation*[](#keysight.ads.dds.TextAxis.orientation "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.TextAxis.string_format "Link to this definition")


---

<!-- === 来源: reference/dds/basic.md === -->

# Common Properties[](#common-properties "Link to this heading")

*class* keysight.ads.dds.Color[](#keysight.ads.dds.Color "Link to this definition")
:   Class that contains color information.

    Available colors specified in the configuration file hpeecolor.cfg, which by default resides in
    $HPEESOF\_DIR/config (where $HPEESOF\_DIR represents the complete installation path).
    See documentation for customizing the ADS environment found in the ADS installation manual for details.
    The available colors can be obtained by the method [`colors()`](#keysight.ads.dds.Color.colors "keysight.ads.dds.Color.colors").
    Individual colors can be obtained either by index or by rgb values.

    Parameters:
    :   **index\_or\_rgb** (*int* *|* *tuple**[**int**,* *int**,* *int**]*) – If an integer is passed, the color returned is nth element in the list of available colors.
        If a tuple is passed, the color returned is the element in the list of available colors that matches the rgb value to the tuple.

    Raises:
    :   * **RuntimeError: Invalid color index "<int>" specified. Color index must be between "0" and "<int>".** – The integer parameter is out of bounds of the available colors.
        * **RuntimeError: Unable to find color r={<int>}****,** **g={<int>}****,** **b={<int>}.** – The tuple parameter does not match any available colors.

    Example

    Obtain the 2nd color in the list of colors

    ```
    >>> from keysight.ads import dds as dds
    >>> yellow = dds.Color(2)
    >>> print(yellow.rgb)
        (255, 255, 0)
    ```

    Create yellow. The rgb values of yellow is (255, 255, 0).

    ```
    >>> from keysight.ads import dds as dds
    >>> yellow = dds.Color((255, 255, 0))
    >>> print(yellow.index)
        2
    ```

    *static* color\_index(*color: tuple[int, int, int]*) → int[](#keysight.ads.dds.Color.color_index "Link to this definition")
    :   Return the index into the available list of colors that matches the rgb parameter.

        The list is obtained by the method [`colors()`](#keysight.ads.dds.Color.colors "keysight.ads.dds.Color.colors").

        Parameters:
        :   **color** (*tuple**[**int**,* *int**,* *int**]**)*) – The rgb values to match.

        Returns:
        :   Index into the list of available colors that matches the tuple. If a match is not found, an exception is thrown.

        Return type:
        :   int

        Raises:
        :   **RuntimeError: Unable to find color r=<int>****,** **g=<int>****,** **b=<int>.** – This occurs when the rgb value is not found in the list of available colors,
            which is obtained by the method [`colors()`](#keysight.ads.dds.Color.colors "keysight.ads.dds.Color.colors").

        Example

        Get the index of a particular rgb value.

        ```
        >>> from keysight.ads import dds as dds
        >>> yellow_index = dds.Color.color_index((255, 255, 0))
        >>> print(dds.Color.colors()[yellow_index])
            (255, 255, 0)
        ```

    *static* colors() → list[tuple[int, int, int]][](#keysight.ads.dds.Color.colors "Link to this definition")
    :   Return a list of colors.

        Returns:
        :   A list of available colors. These are defined in the config file "$HPEESOF\_DIR/config/hpeecolor.cfg".
            Each color in the list is stored as a tuple of 3 integers representing the rgb value of the color.
            Specific colors may be obtained by specifying an index into this list. Matching an element to an
            rgb value can be done by using the method [`color_index()`](#keysight.ads.dds.Color.color_index "keysight.ads.dds.Color.color_index").

        Return type:
        :   list[tuple[int, int, int]]

        Raises:
        :   **RuntimeError: Color map is empty** **or** **missing. Please verify that "$HPEESOF\_DIR/config/hpeecolor.cfg" exists and is correctly configured.** – The config file hpeecolor.cfg is not found. There is no list.

        Example

        Obtain a list of available colors.

        ```
        >>> from keysight.ads import dds as dds
        >>> colors = dds.Color.colors()
        ```

    *property* index*: int*[](#keysight.ads.dds.Color.index "Link to this definition")
    :   The index into the list of available colors.

    *property* rgb*: tuple[int, int, int]*[](#keysight.ads.dds.Color.rgb "Link to this definition")
    :   The rgb value of the color.

*class* keysight.ads.dds.DensitySymbolProperties[](#keysight.ads.dds.DensitySymbolProperties "Link to this definition")

*class* keysight.ads.dds.FillProperties[](#keysight.ads.dds.FillProperties "Link to this definition")
:   Class that contains properties for fill patterns.

    Available fill patterns are specified in the configuration file hpeefill.cfg, which by default resides in
    $HPEESOF\_DIR/config (where $HPEESOF\_DIR represents the complete installation path).
    See documentation for customizing the ADS environment found in the ADS installation manual for details.
    The available fill patterns can be obtained by the method [`fill_patterns()`](#keysight.ads.dds.FillProperties.fill_patterns "keysight.ads.dds.FillProperties.fill_patterns").
    Individual fill patterns can be obtained by indexing into the fill patterns list with a string.

    Parameters:
    :   * **pattern** (*str* *[**optional**,* *default=None**]*) – If a string is passed, the fill pattern used is the element in the list of available fill patterns that matches the string.
          If the patterns is not found, an exception is thrown.
        * **color** ([*Color*](#keysight.ads.dds.Color "keysight.ads.dds.Color") *[**optional**,* *default=None**]*) – If a valid Color is passed, the fill pattern will be drawn in the specified color. If no color is specified (value == None), then
          the fill pattern will be drawn in black. If an invalid color is specified, an exception is thrown.

    Raises:
    :   * **RuntimeError: Unable to find pattern <pattern>** – The “pattern”” parameter is not found in the list of fill patterns.
        * **RuntimeError: Invalid color index "<int>" specified. Color index must be between "0" and "<int>".** – The integer parameter is out of bounds of the available colors.
        * **RuntimeError: Unable to find color r={<int>}****,** **g={<int>}****,** **b={<int>}.** – The tuple parameter does not match any available colors.

    Example

    Set fill to yellow dots in a circle.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> page = dds_file.pages[0]
    >>> center = dds.Point(500, 500)
    >>> obj = page.add_circle(center, 100)
    >>> obj.fill_properties = dds.FillProperties('dots_1', dds.Color(2))
    >>> print(obj.fill_properties)
        <FillProperties pattern="dots_1" color=<Color "2">>
    ```

    *property* color*: [Color](#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.FillProperties.color "Link to this definition")

    *static* fill\_patterns() → list[str][](#keysight.ads.dds.FillProperties.fill_patterns "Link to this definition")
    :   Return a list of patterns.

        Returns:
        :   A list of available patterns. These are defined in the config file "$HPEESOF\_DIR/config/hpeefill.cfg".
            Each pattern in the list is stored as a string.

        Return type:
        :   list[str]

        Example

        Obtain a list of available patterns.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds.FillPatterns.fill_patterns()
        ```

    *property* pattern*: str*[](#keysight.ads.dds.FillProperties.pattern "Link to this definition")

*class* keysight.ads.dds.LineProperties[](#keysight.ads.dds.LineProperties "Link to this definition")
:   Class that contains properties for lines.

    Available types are defined by the class [`LineType`](#keysight.ads.dds.LineType "keysight.ads.dds.LineType").

    Parameters:
    :   * **type** ([*LineType*](#keysight.ads.dds.LineType "keysight.ads.dds.LineType") *[**optional**,* *default=None**]*) – Any value other than a value from class:LineType will throw an exception.
        * **color** ([*Color*](#keysight.ads.dds.Color "keysight.ads.dds.Color") *[**optional**,* *default=None**]*) – If a valid Color is passed, the fill pattern will be drawn in the specified color. If no color is specified (value == None), then
          the fill pattern will be drawn in black. If an invalid color is specified, an exception is thrown.
        * **width** (*float* *[**optional**,* *default=None**]*) – The width is truncated to the nearest tenth. If width is not passed, the width is 0.5. If a negative width is passed, it is simply ignored.

    Raises:
    :   * **RuntimeError: Invalid color index "<int>" specified. Color index must be between "0" and "<int>".** – The integer parameter is out of bounds of the available colors.
        * **RuntimeError: Unable to find color r={<int>}****,** **g={<int>}****,** **b={<int>}.** – The tuple parameter does not match any available colors.

    Example

    Set line type to green long dashes in a circle.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> page = dds_file.pages[0]
    >>> center = dds.Point(500, 500)
    >>> obj = page.add_circle(center, 100)
    >>> obj.line_properties = dds.FillProperties(dds.LineType.LONG_DASH, dds.Color(3), 2.7)
    >>> print(obj.line_properties)
        <LineProperties type=LineType.LONG_DASH color=<Color "3"> width=-2.7>
    ```

    *property* color*: [Color](#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.LineProperties.color "Link to this definition")

    *property* type*: [LineType](#keysight.ads.dds.LineType "keysight.ads.dds.core.ddbase.LineType") | None*[](#keysight.ads.dds.LineProperties.type "Link to this definition")

    *property* width*: float*[](#keysight.ads.dds.LineProperties.width "Link to this definition")

*class* keysight.ads.dds.LineType[](#keysight.ads.dds.LineType "Link to this definition")
:   DOT *= <DDlineTypeC.DOT: 1>*[](#keysight.ads.dds.LineType.DOT "Link to this definition")

    DOT\_DOT *= <DDlineTypeC.DOT\_DOT: 2>*[](#keysight.ads.dds.LineType.DOT_DOT "Link to this definition")

    LONG\_DASH *= <DDlineTypeC.LONG\_DASH: 5>*[](#keysight.ads.dds.LineType.LONG_DASH "Link to this definition")

    LONG\_DOT\_DASH *= <DDlineTypeC.LONG\_DOT\_DASH: 6>*[](#keysight.ads.dds.LineType.LONG_DOT_DASH "Link to this definition")

    SHORT\_DASH *= <DDlineTypeC.SHORT\_DASH: 3>*[](#keysight.ads.dds.LineType.SHORT_DASH "Link to this definition")

    SHORT\_DOT\_DASH *= <DDlineTypeC.SHORT\_DOT\_DASH: 4>*[](#keysight.ads.dds.LineType.SHORT_DOT_DASH "Link to this definition")

    SOLID *= <DDlineTypeC.SOLID\_LINE: 0>*[](#keysight.ads.dds.LineType.SOLID "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.LineType.str "Link to this definition")

*class* keysight.ads.dds.SymbolProperties[](#keysight.ads.dds.SymbolProperties "Link to this definition")

*class* keysight.ads.dds.TextProperties[](#keysight.ads.dds.TextProperties "Link to this definition")
:   Class that contains properties for text.

    The available fonts can be obtained by the method `get_fonts()`.
    The Data Display default font can be obtained by the mothod :meth:’get\_default\_font’.
    Individual fonts can be obtained by indexing into the fonts list with a string.

    Parameters:
    :   * **font** (*str* *[**optional**,* *default=None**]*) – If a string is passed, the font used is the element in the list of available fonts that matches the string.
          If no font is specified, the default font is used.
          If the font is not found, an exception is thrown.
        * **color** ([*Color*](#keysight.ads.dds.Color "keysight.ads.dds.Color") *[**optional**,* *default=None**]*) – If a valid Color is passed, the text will be drawn in the specified color. If no color is specified (value == None), then
          the text will be drawn in black. If an invalid color is specified, an exception is thrown.
        * **size** (*int* *[**optional**,* *default=None**]*) – If an integer is passed, it specifies the size of the font.
          If size is not passed or is negative, the default size is used.

    Raises:
    :   * **RuntimeError: Font name "<font>" not found on system.** – The “font” parameter is not found in the list of fonts.
        * **RuntimeError: Invalid color index "<int>" specified. Color index must be between "0" and "<int>".** – The integer parameter is out of bounds of the available colors.

    Example

    Set text properties on a text on a page.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> page = dds_file.pages[0]
    >>> obj = page.add_text("Hello World"dds.Point(500,500))
    >>> obj.text_properties = dds.TextProperties('Roman', dds.Color(2), 24)
    >>> print(obj.text_properties)
        <TextProperties font="Roman" color=<Color "2"> size=23>
    ```

    *property* color*: [Color](#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.TextProperties.color "Link to this definition")

    *static* default\_font() → str[](#keysight.ads.dds.TextProperties.default_font "Link to this definition")

    *property* font*: str*[](#keysight.ads.dds.TextProperties.font "Link to this definition")

    *static* font\_exists(*font: str*) → bool[](#keysight.ads.dds.TextProperties.font_exists "Link to this definition")

    *static* fonts() → list[str][](#keysight.ads.dds.TextProperties.fonts "Link to this definition")
    :   Return a list of fonts.

        Returns:
        :   A list of available fonts. Each font in the list is stored as a string.

        Return type:
        :   list[str]

        Example

        Obtain a list of available fonts.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds.TextProperties.fonts()
        ```

    *property* size*: int*[](#keysight.ads.dds.TextProperties.size "Link to this definition")

    text\_size(*text: str*) → tuple[int, int][](#keysight.ads.dds.TextProperties.text_size "Link to this definition")

*class* keysight.ads.dds.StringFormat[](#keysight.ads.dds.StringFormat "Link to this definition")
:   *property* complex\_format*: ComplexStringFormatOption*[](#keysight.ads.dds.StringFormat.complex_format "Link to this definition")

    *property* format*: StringFormatOption*[](#keysight.ads.dds.StringFormat.format "Link to this definition")

    *property* signficant\_digits*: int*[](#keysight.ads.dds.StringFormat.signficant_digits "Link to this definition")

    *property* units\_format*: UnitsStringOption*[](#keysight.ads.dds.StringFormat.units_format "Link to this definition")


---

<!-- === 来源: reference/dds/equation.md === -->

# Equation[](#equation "Link to this heading")

*class* keysight.ads.dds.Equation[](#keysight.ads.dds.Equation "Link to this definition")
:   Equations perform complex mathematical operations on data.

    This class cannot be instantiated directly. See [`Page.add_equation()`](page.md#keysight.ads.dds.Page.add_equation "keysight.ads.dds.Page.add_equation").

    activate() → None[](#keysight.ads.dds.Equation.activate "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Equation.bbox "Link to this definition")
    :   The bounding box associated with an object.

    calculate() → None[](#keysight.ads.dds.Equation.calculate "Link to this definition")

    deactivate() → None[](#keysight.ads.dds.Equation.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.Equation.delete_object "Link to this definition")

    *property* errors*: str*[](#keysight.ads.dds.Equation.errors "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.Equation.expression "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.Equation.fill_properties "Link to this definition")

    *property* is\_auto\_calculated*: bool*[](#keysight.ads.dds.Equation.is_auto_calculated "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.Equation.is_deactivated "Link to this definition")

    *property* is\_outlined*: bool*[](#keysight.ads.dds.Equation.is_outlined "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Equation.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Equation.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Equation.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Equation.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Equation.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Equation.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Equation.name "Link to this definition")

    *property* status*: str*[](#keysight.ads.dds.Equation.status "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.Equation.string_format "Link to this definition")

    *property* text\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.Equation.text_properties "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Equation.type "Link to this definition")

    *property* variable*: bool | int | float | complex | str | VariableBlock | None*[](#keysight.ads.dds.Equation.variable "Link to this definition")
    :   The value of this equation as a scalar or Indexed Variable Block. Indexed Variable Blocks can be converted to a dataframe.

        Examples

        Print the value of the equation.

        ```
        >>> eq = page.add_equation('x = vs([10, 20, 30], [1, 2, 3])')
        >>> eq.variable.to_dataframe()
             __d
        __i
        1     10
        2     20
        3     30
        ```


---

<!-- === 来源: reference/dds/experimental/index.md === -->

# keysight.ads.dds.experimental[](#module-keysight.ads.dds.experimental "Link to this heading")

Deprecated experimental module - Replaced by dds.

## Classes[](#classes "Link to this heading")

None

## Functions[](#functions "Link to this heading")

None


---

<!-- === 来源: reference/dds/file.md === -->

# DDSFile[](#ddsfile "Link to this heading")

*class* keysight.ads.dds.DDSFile[](#keysight.ads.dds.DDSFile "Link to this definition")
:   The top of the graphical object structure associated with a Data Display file.

    This class cannot be instantiated directly, but instead
    is created and returned when a Data Display file is created or opened.

    See also

    [`new_dds_file()`](index.md#keysight.ads.dds.new_dds_file "keysight.ads.dds.new_dds_file")
    :   Create a new Data Display file.

    [`open_dds_file()`](index.md#keysight.ads.dds.open_dds_file "keysight.ads.dds.open_dds_file")
    :   Open an existing Data Display file.

    add\_dataset\_alias(*name: str*, *path: str*) → None[](#keysight.ads.dds.DDSFile.add_dataset_alias "Link to this definition")
    :   Add a dataset alias to the [`dataset_aliases`](#keysight.ads.dds.DDSFile.dataset_aliases "keysight.ads.dds.DDSFile.dataset_aliases") properties.

        A dataset alias is a short name mapped to a full path of a dataset.

        Parameters:
        :   * **name** (*str*) – A short name for the dataset alias to add.
            * **path** (*str*) – The path to the dataset. It may be an absolute path or a relative path, and it may include environment variables.

        Return type:
        :   None

    add\_external\_dataset\_path(*path: str | PathLike*) → None[](#keysight.ads.dds.DDSFile.add_external_dataset_path "Link to this definition")
    :   Add a dataset path to the [`external_dataset_paths`](#keysight.ads.dds.DDSFile.external_dataset_paths "keysight.ads.dds.DDSFile.external_dataset_paths") property.

        Parameters:
        :   **name** (*str* *|* *os.PathLike*) – The path to the dataset. It may be an absolute or relative path.

        Return type:
        :   None

    change\_page(*name: str*, *win: [Window](windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window") | None = None*) → None[](#keysight.ads.dds.DDSFile.change_page "Link to this definition")
    :   Change which [`Page`](page.md#keysight.ads.dds.Page "keysight.ads.dds.Page") will be displayed when the DDSFile is opened in Data Display.

        If running in automation mode and the DDSFile is saved after the change\_page(), the next time the DDSFile is
        opened in the Data Display application, it will open to the page specified.
        If running in application mode and the DDSFile is currently opened, the specified page wil be displayed immediately.

        Parameters:
        :   * **name** (*str*) – The name of the page to be displayed.
            * **win** ([*Window*](windows.md#keysight.ads.dds.Window "keysight.ads.dds.Window") *[**optional**]*) – The window which will display the changed page. If this parameter is omitted, the change page will only
              occur on the default page, which is the page that was created when the DDSFile was initially created.

        Return type:
        :   None

        Raises:
        :   **RuntimeError: Unable to find page {"<page name>"}.** – This exception occurs if the specified Page name is not found in DDSfile.

        Examples

        Change pages so that next time the DDSFile is opened in the Data Display application, it displays the first page
        on the first window, and displays the last page in the 2nd window.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds.open_dds_file("test.dds")
        >>> lastIndx = len(ddsfile.pages)
        >>> ddsfile.new_window()
        >>> ddsfile.change_page(ddsfile.pages[0], ddsfile.windows[0])
        >>> ddsfile.change_page(ddsfile.pages[lastIndx - 1].name, ddsfile.windows[1])
        >>> ddsfile.save()
        ```

        Change the page on the default window of DDSFile. Note that when a new page is created in DDSFile, it becomes
        the page that will be displayed in the default window.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = ddsfile = dds.open_dds_file("test.dds")
        >>> ddsfile.new_page("page 2")
        >>> print(ddsfile.windows[0].current_page)
            page 2
        >>> ddsfile.change_page("page 1")
        >>> print(dds_file.windows[0].current_page)
            page 1
        >>> ddsfile.save()
        ```

    close\_window(*win: [Window](windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window")*) → None[](#keysight.ads.dds.DDSFile.close_window "Link to this definition")
    :   Close a window viewing the DDSFile.

        There must always be one window available.

        Parameters:
        :   **win** ([*Window*](windows.md#keysight.ads.dds.Window "keysight.ads.dds.Window")) – The window to delete.

        Return type:
        :   None

    *property* data\_path*: str*[](#keysight.ads.dds.DDSFile.data_path "Link to this definition")
    :   The relative path to a subfolder or a full path that specifies the directory in which the dataset file is located.

        Default value is “./data”. It is reset in [`new_dds_file()`](index.md#keysight.ads.dds.new_dds_file "keysight.ads.dds.new_dds_file") or [`open_dds_file()`](index.md#keysight.ads.dds.open_dds_file "keysight.ads.dds.open_dds_file").

    *property* dataset\_aliases*: dict[str, str]*[](#keysight.ads.dds.DDSFile.dataset_aliases "Link to this definition")
    :   A dictionary that contains the dataset aliases.

        The key-value pairs are [<alias name>, <path>].

        See also

        [`add_dataset_alias()`](#keysight.ads.dds.DDSFile.add_dataset_alias "keysight.ads.dds.DDSFile.add_dataset_alias")
        :   Add a dataset alias to this property.

        [`remove_dataset_alias()`](#keysight.ads.dds.DDSFile.remove_dataset_alias "keysight.ads.dds.DDSFile.remove_dataset_alias")
        :   Remove a dataset alias to this property.

    *property* default\_dataset*: str*[](#keysight.ads.dds.DDSFile.default_dataset "Link to this definition")
    :   The name of the default dataset file.

        The file name may or may not include the extension “.ds”. If it is specified
        as a file name or relative path, the dataset file lives in the directory pointed to by the [`data_path`](#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path") property. It
        may also be specified with an absolute path.

        If the file is not found, the default\_dataset is set to the first dataset file found in the [`data_path`](#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path") property. If no
        default dataset file can be found, then the default\_dataset is set to “dataset”. If default\_dataset cannot be set
        to the specified value, a message is printed to the output.

        Example

        Set the default dataset and ensure that it was found

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file('c:/tmp/MyWorkspace_wrk/myDDSfile.dds')
        >>> dds_file.default_dataset = "myDataset"
        >>> if dds_file.default_dataset != "myDataset":
        >>>     exit()
        ```

    delete\_page(*name: str*) → None[](#keysight.ads.dds.DDSFile.delete_page "Link to this definition")
    :   Delete a page from the DDSFile.

        Each DDSFile is required to have at least one page.
        Any windows viewing that page will have the page changed to the next page or the
        first page if the last page is deleted.
        A list of pages in a DDSFile can be obtained from the [`pages`](#keysight.ads.dds.DDSFile.pages "keysight.ads.dds.DDSFile.pages") property.

        Parameters:
        :   **name** (*str*) – The name of the Page to be renamed.

        Return type:
        :   None

        Raises:
        :   * **RuntimeError: Unable to find page {"<page name>"}.** – This exception occurs if the specified Page name to rename is not found in the DDSFile.
            * **RuntimeError: You cannot delete the last page in a DDS window. The page delete operation has been cancelled.** – This exception occurs if the DDSFile has only 1 page.
            * **RuntimeError: Error deleting current page.** – This exception occurs if for an unknown reason, the page cannot be deleted.

        Example

        Delete a page in the DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds.open_dds_file("test.dds")
        >>> ddsfile.new_window()
        >>> ddsfile.new_page("readme")
        >>> print(ddsfile.pages)
            (<Page "page 1">, <Page "readme">)
        >>> ddsfile.delete("page 1")
        >>> print(ddsfile.pages)
            (<Page "readme">,)
        >>> ddsfile.save()
        ```

    *property* dot\_grid\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.DDSFile.dot_grid_color "Link to this definition")
    :   The color of the dot grid for pages in the DDSFile.

    *property* external\_dataset\_paths*: list[str]*[](#keysight.ads.dds.DDSFile.external_dataset_paths "Link to this definition")
    :   A list of paths to datasets that can be accessed in the DDSFile.

        See also

        [`add_external_dataset_path()`](#keysight.ads.dds.DDSFile.add_external_dataset_path "keysight.ads.dds.DDSFile.add_external_dataset_path")
        :   Add a dataset path to this property.

        [`remove_external_dataset_path()`](#keysight.ads.dds.DDSFile.remove_external_dataset_path "keysight.ads.dds.DDSFile.remove_external_dataset_path")
        :   Remove a dataset path to this property.

    get\_closest\_grid\_point(*value: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")[](#keysight.ads.dds.DDSFile.get_closest_grid_point "Link to this definition")
    :   Return the closest grid point to the specified Point or tuple.

        Parameters:
        :   **value** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – Point or tuple that represents a point on the a page of the DDSFile.

        Return type:
        :   [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point")

        Example

        Insert a plot at a specific point on the page.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> snapPt = dds_file.get_closest_grid_point(dds.Point(100,100))
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot(snapPt)
        >>> dds_file.save("test.dds")
        ```

    *property* grid\_on*: bool*[](#keysight.ads.dds.DDSFile.grid_on "Link to this definition")
    :   Indicates if the grid is on for pages in the DDSFile.

    *property* grid\_type*: [GridType](grid.md#keysight.ads.dds.GridType "keysight.ads.dds.core.ddobj.GridType")*[](#keysight.ads.dds.DDSFile.grid_type "Link to this definition")
    :   The grid type for pages in the DDSFile.

    insert\_template(*path: str | PathLike*) → None[](#keysight.ads.dds.DDSFile.insert_template "Link to this definition")
    :   Insert a Data Display Template into the DDSFile.

        Parameters:
        :   **name** (*str* *|* *os.PathLike*) – The path to the template. It may be an absolute or relative path.
            It may or may not include the “.ddt” extension. However, the actual file must have the extension “.ddt”.

        Return type:
        :   None

        Example

        Insert the Data Display Template “myPlot” into a DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds"")
        >>> dds_file.insert_template("c:/tmp/myPlot")
        ```

        See also

        [`save_as_template()`](#keysight.ads.dds.DDSFile.save_as_template "keysight.ads.dds.DDSFile.save_as_template")
        :   Save a DDSFile to a Data Display template file.

    *property* line\_grid\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.DDSFile.line_grid_color "Link to this definition")
    :   The color of the line grid for pages in the DDSFile.

    *property* name*: str*[](#keysight.ads.dds.DDSFile.name "Link to this definition")

    new\_page(*name: str*) → [Page](page.md#keysight.ads.dds.Page "keysight.ads.dds.core.ddpage.Page")[](#keysight.ads.dds.DDSFile.new_page "Link to this definition")
    :   Return a new Page.

        When a new page is created, it becomes the page being viewed in the default window.
        A list of pages in a DDSFile can be obtained from the [`pages`](#keysight.ads.dds.DDSFile.pages "keysight.ads.dds.DDSFile.pages") property.

        Parameters:
        :   **name** (*str*) – The name of the new Page

        Returns:
        :   If a page with the “name” parameter already exists, a unique page name will be determined by adding
            a space followed by a unique number to the end of “name”.

        Return type:
        :   [Page](page.md#keysight.ads.dds.Page "keysight.ads.dds.Page")

        Raises:
        :   * **RuntimeError: Page name is too long.** – Page names cannot exceed 1023 characters.
            * **RuntimeError: Unable to get new page object.** – This exception occurs if the new page was not created.
            * **RuntimeError: Page not created because "<name>" is an existing page.** – Pages must have a unique name.
            * **RuntimeError: Page not created because "<name>" has leading** **or** **trailing whitespace.** – Page names cannot have any leading or trailing whitespace.

        Example

        Create two new pages.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds.open_dds_file("test.dds")
        >>> page1 = ddsfile.new_page("myNewPage")
        >>> print(page1.name)
            myNewPage
        >>> page2 = ddsfile.new_page("myNewPage")
        >>> print(page2.name)
            myNewPage 1
        >>> print(ddsfile.pages)
            (<Page "page 1">, <Page "myNewPage">, <Page "myNewPage 1">)
        >>> print(ddsfile.window[0].current_page)
            myNewPage 1
        >>> print(ddsfile.window[1].current_page)
            page 1
        ```

    new\_window() → [Window](windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window")[](#keysight.ads.dds.DDSFile.new_window "Link to this definition")
    :   Create an additional window viewing the contents of a page in the DDSFile.

        Each DDSFile can have multiple windows. Multiple windows can view the same or
        different pages and can be scaled to display different views of the page.
        A list of windows in a DDSFile can be obtained from the [`windows`](#keysight.ads.dds.DDSFile.windows "keysight.ads.dds.DDSFile.windows") property.

        Returns:
        :   The new window.

        Return type:
        :   [Window](windows.md#keysight.ads.dds.Window "keysight.ads.dds.Window")

        Example

        Create a new window for DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds.open_dds_file("test.dds")
        >>> win = ddsfile.new_window()
        >>> ddsfile.windows
            [<Window "">, <Window "">]
        ```

    *property* pages*: NamedItemCollectionAbc[[Page](page.md#keysight.ads.dds.Page "keysight.ads.dds.core.ddpage.Page")]*[](#keysight.ads.dds.DDSFile.pages "Link to this definition")
    :   A collection of pages contained in the DDSFile.

        The collection reflects the order in which the pages were created.
        This property is Read-only. Use class methods to modify the collection.

        Examples

        Check if a page exists.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds.open_dds_file("test.dds")
        >>> exists = "page 1" in ddsfile.pages
        ```

        Access a page.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds.open_dds_file("test.dds")
        >>> page = ddsfile.pages[0]
        >>> if 'page 1' in ddsfile.pages:
        >>>     page = ddsfile.pages['page 1']
        ```

        See also

        [`new_page()`](#keysight.ads.dds.DDSFile.new_page "keysight.ads.dds.DDSFile.new_page")
        :   Create a new Page.

        [`rename_page()`](#keysight.ads.dds.DDSFile.rename_page "keysight.ads.dds.DDSFile.rename_page")
        :   Rename a Page.

        [`delete_page()`](#keysight.ads.dds.DDSFile.delete_page "keysight.ads.dds.DDSFile.delete_page")
        :   Delete a Page.

        [`change_page()`](#keysight.ads.dds.DDSFile.change_page "keysight.ads.dds.DDSFile.change_page")
        :   Change page being viewed.

    print\_all\_pages\_to\_pdf(*pdf: str | PathLike*, *orientation: [PrinterOrientation](print.md#keysight.ads.dds.PrinterOrientation "keysight.ads.dds.core.ddobj.PrinterOrientation") | str = PrinterOrientation.LANDSCAPE*, *size: [PaperSize](print.md#keysight.ads.dds.PaperSize "keysight.ads.dds.core.ddobj.PaperSize") | str = PaperSize.LETTER*, *fit\_to\_page: bool = True*) → None[](#keysight.ads.dds.DDSFile.print_all_pages_to_pdf "Link to this definition")
    :   Print all pages of DDSFile to a PDF file.

        Parameters:
        :   * **pdf** (*str* *|* *os.PathLike*) – The path to new PDF file. This may be an absolute or relative path.
            * **orientation** ([*PrinterOrientation*](print.md#keysight.ads.dds.PrinterOrientation "keysight.ads.dds.PrinterOrientation") *|* *str* *[**optional**,* *default=PrinterOrientation.LANDSCAPE**]*) – The orientation of the PDF. :class: dds.PrinterOrientation
            * **size** ([*PaperSize*](print.md#keysight.ads.dds.PaperSize "keysight.ads.dds.PaperSize") *|* *str* *[**optional**,* *default=PaperSize.LETTER**]*) – The paper size to use in the PDF file. :class: dds.PaperSize
            * **fit\_to\_page** (*bool* *[**optional**,* *default=True**]*) – If True, the pages in DDSFile may be scaled to fit on a printed page. Otherwise, the pages in the DDSFile are not scaled.

        Return type:
        :   None

        Raises:
        :   * **RuntimeError: Invalid data display object.** – This exception occurs if the DDSFile is invalid.
            * **RuntimeError: Unable to open the gplot printer.** – Unable to access printer.
            * **RuntimeError: PrinterOrientation has no value** – <str>.: The string passed to the orientation parameter does not correspond to a valid PrinterOrientation value.
            * **RuntimeError: PaperSize has no value** – <str>.: The string passed to the size parameter does not correspond to a valid PaperSize value.

        Example

        Print all pages of a DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds.open_dds_file("test.dds")
        >>> ddfile.print_pages_to_pdf("x.pdf", dds.PrinterOrientation.PORTRAIT, dds.PaperSize.A0, False)
        ```

        See also

        [`print_pages_by_name_to_pdf()`](#keysight.ads.dds.DDSFile.print_pages_by_name_to_pdf "keysight.ads.dds.DDSFile.print_pages_by_name_to_pdf")
        :   Print specific pages to a PDF file.

    print\_pages\_by\_name\_to\_pdf(*pdf: str | PathLike*, *pages: list[str]*, *orientation: [PrinterOrientation](print.md#keysight.ads.dds.PrinterOrientation "keysight.ads.dds.core.ddobj.PrinterOrientation") | str = PrinterOrientation.LANDSCAPE*, *size: [PaperSize](print.md#keysight.ads.dds.PaperSize "keysight.ads.dds.core.ddobj.PaperSize") | str = PaperSize.LETTER*, *fit\_to\_page: bool = True*) → None[](#keysight.ads.dds.DDSFile.print_pages_by_name_to_pdf "Link to this definition")
    :   Print specific pages of DDSFile to a PDF file.

        Parameters:
        :   * **pdf** (*str* *|* *os.PathLike*) – The path to new PDF file. This may be an absolute or relative path.
            * **pages** (*list**[**str**]*) – A list of pages specified by strings. Each page will be printed to the PDF file.
            * **orientation** ([*PrinterOrientation*](print.md#keysight.ads.dds.PrinterOrientation "keysight.ads.dds.PrinterOrientation") *|* *str* *[**optional**,* *default=PrinterOrientation.LANDSCAPE**]*) – The orientation of the PDF. :class: dds.PrinterOrientation
            * **size** ([*PaperSize*](print.md#keysight.ads.dds.PaperSize "keysight.ads.dds.PaperSize") *|* *str* *[**optional**,* *default=PaperSize.LETTER**]*) – The paper size to use in the PDF file. :class: dds.PaperSize
            * **fit\_to\_page** (*bool* *[**optional**,* *default=True**]*) – If True, the pages in DDSFile may be scaled to fit on a printed page. Otherwise, the pages in the DDSFile are not scaled.

        Return type:
        :   None

        Raises:
        :   * **RuntimeError: Invalid data display object.** – This exception occurs if the DDSFile is invalid.
            * **RuntimeError: Unable to open the gplot printer.** – Unable to access printer.
            * **RuntimeError: PrinterOrientation has no value** – <str>.: The string passed to the orientation parameter does not correspond to a valid PrinterOrientation value.
            * **RuntimeError: PaperSize has no value** – <str>.: The string passed to the size parameter does not correspond to a valid PaperSize value.

        Example

        Print all pages of a DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds.open_dds_file("test.dds")
        >>> ddfile.print_pages_by_name_to_pdf("x.pdf"", ["page 1"])
        ```

        See also

        [`print_all_pages_to_pdf()`](#keysight.ads.dds.DDSFile.print_all_pages_to_pdf "keysight.ads.dds.DDSFile.print_all_pages_to_pdf")
        :   Print all pages to a PDF file.

    remove\_dataset\_alias(*name: str*) → None[](#keysight.ads.dds.DDSFile.remove_dataset_alias "Link to this definition")
    :   Remove a dataset alias from the [`dataset_aliases`](#keysight.ads.dds.DDSFile.dataset_aliases "keysight.ads.dds.DDSFile.dataset_aliases") property.

        A dataset alias is a short name mapped to a full path of a dataset.

        Parameters:
        :   **name** (*str*) – Name of the dataset alias to remove.

        Return type:
        :   None

    remove\_external\_dataset\_path(*path: str | PathLike*) → None[](#keysight.ads.dds.DDSFile.remove_external_dataset_path "Link to this definition")
    :   Remove a dataset path from the [`external_dataset_paths`](#keysight.ads.dds.DDSFile.external_dataset_paths "keysight.ads.dds.DDSFile.external_dataset_paths") property.

        Parameters:
        :   **name** (*str* *|* *os.PathLike*) – The path to the dataset. It may be an absolute or relative path.

        Return type:
        :   None

    rename\_page(*name: str*, *new\_name: str*) → None[](#keysight.ads.dds.DDSFile.rename_page "Link to this definition")
    :   Rename a page.

        The rename is effective in all windows in the DDSFile.

        Parameters:
        :   * **name** (*str*) – The name of the page to be renamed.
            * **new\_name** (*str*) – The new name of the page.

        Return type:
        :   None

        Raises:
        :   **RuntimeError: Unable to find page {"<page name>"}** – This exception occurs if the specified page to rename is not found in the DDSFile.

        Example

        Rename a page in the DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds.open_dds_file("test.dds")
        >>> ddsfile.new_window()
        >>> print(ddsfile.pages)
            (<Page "page 1">)
        >>> ddsfile.rename("page 1", "readme")
        >>> print(ddsfile.pages)
            (<Page "readme">)
        >>> print(ddsfile.windows[0].current_page)
            readme
        >>> print(ddsfile.windows[1].current_page)
            readme
        >>> ddsfile.save()
        ```

    save(*name: str | None = None*, *path: str | PathLike | None = None*) → None[](#keysight.ads.dds.DDSFile.save "Link to this definition")
    :   Save the DDSFile.

        Parameters:
        :   * **name** (*str* *[**optional**,* *default=None**]*) – Specifies the file name where the DDSFile will be saved. This may include an absolute path or relative path.
              The extension “.dds” may or may not be included. However, when saved, it will ensure the file has a “.dds” extension.
              If it is an absolute path, the “path” parameter will be ignored.
              If its a relative path, it is joined with the “path” parameter.
              If the DDSFile has been saved before, the current file name will be used UNLESS “name” is passed.
              If DDSFile is a new file that has never been saved before, this parameter MUST be passed or an exception will occur.
            * **path** (*str* *[**optional**,* *default=None**]*) – Specifies the directory where the DDSFile will be saved.
              If the DDSFile has been saved before, the current directory will be used UNLESS “path” is passed.
              If DDSFile is a new file that has never been saved before, this parameter MUST be passed or an exception will occur.

        Return type:
        :   None

        Raises:
        :   * **RuntimeError: No filename specified to save object.** – This exception occurs if the DDSFile is a new file that has never been saved and the “name” parameter is not passed or empty.
            * **RuntimeError: No path specified to save object.** – This exception occurs if the DDSFile is a new file that has never been saved and the “path” parameter is not passed or empty.
            * **RuntimeError: Writing dds file failed\** – {<path>}.: This exception occurs when the file write failed.

        Examples

        Open an existing file and save it

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds.open_dds_file("test.dds")
        >>> ddsfile.save()  #Overwrites test.dds
        >>> ddsfile = dds.open_dds_file("c:/tmp/external.dds")
        >>> ddsfile.save()  #Overwrites "c:/tmp/external.dds"
        ```

        Open an existing file save it to a different file in the same directory.

        ```
        >>> from keysight.ads import dds as dds
        >>> ddsfile = dds.open_dds_file("test.dds")
        >>> ddfile.save("newTest.dds")         #Writes new file "newTest.dds" in the current directory
        >>> ddsfile = dds.open_dds_file("c:/tmp/external.dds")
        >>> ddsfile.save("newExternal.dds")    #Writes new file "c:/tmp/newExternal.dds"
        ```

        Open new file and save it

        ```
        >>> ddsfile = dds.new_dds_file("cell_1.ds", "c:/tmp")
            Opens a new DDSFile with path set to "c:/tmp"
        >>> ddsfile.save("newFile.dds")
            Writes new file "c:/tmp/newFile.dds"
        ```

        See also

        [`new_dds_file()`](index.md#keysight.ads.dds.new_dds_file "keysight.ads.dds.new_dds_file")
        :   Create a new Data Display file.

        [`open_dds_file()`](index.md#keysight.ads.dds.open_dds_file "keysight.ads.dds.open_dds_file")
        :   Open an existing Data Display file.

    save\_as\_template(*path: str | PathLike*) → None[](#keysight.ads.dds.DDSFile.save_as_template "Link to this definition")
    :   Save the DDSFile as a Data Display Template.

        Parameters:
        :   **name** (*str* *|* *os.PathLike*) – The path to the template. It may be an absolute or relative path.
            It may or may not include the [\*](#id1).ddt extension.

        Return type:
        :   None

        Example

        Create a template from a DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.new_dds_file("xxx.ds", "c:/tmp")
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot()
        >>> trace = plot.add_trace("SimpleVar")
        >>> dds_file.save_as_template("c:/tmp/myPlot")
        ```

        See also

        [`insert_template()`](#keysight.ads.dds.DDSFile.insert_template "keysight.ads.dds.DDSFile.insert_template")
        :   Insert a Data Display template into the DDSFile.

    *property* selected\_objects*: list[GraphicalObject]*[](#keysight.ads.dds.DDSFile.selected_objects "Link to this definition")
    :   A list of selected objects.

        Example

        Select a plot on the DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds"")
        >>> page = dds_file.pages[0]
        >>> selObjs == dds_file.selected_objects
        >>> print(selObjs)
            []
        >>> plot = page.objects[0]
        >>> dds_file.selected_objects = [plot]
        >>> selObjs = dds_file.selected_objects
        >>> print(selObjs)
            [<RectPlot "">]
        ```

    *property* snap\_auto\_set\_xy*: bool*[](#keysight.ads.dds.DDSFile.snap_auto_set_xy "Link to this definition")
    :   Indicate whether or not to automatically set Y=X when any X value in snap grid property is modified.

        In this mode, the Y value can still be modified independently.

    *property* snap\_distance\_x*: float*[](#keysight.ads.dds.DDSFile.snap_distance_x "Link to this definition")
    :   The snap grid distance (in inches) for the X-coordinate for pages in the DDSFile.

    *property* snap\_distance\_y*: float*[](#keysight.ads.dds.DDSFile.snap_distance_y "Link to this definition")
    :   The snap grid distance (in inches) for the Y-coordinate for pages in the DDSFile.

    *property* snap\_enabled*: bool*[](#keysight.ads.dds.DDSFile.snap_enabled "Link to this definition")
    :   Indicate whether or not the snap grid is enabled for pages in the DDSFile.

        When enabled, plots, lists, and other graphical objects snap to the grid when
        they are moved or resized. This makes it easier to move the objects into
        exact alignment on the display, or to space them evenly.

    *property* snap\_grid\_per\_display\_grid\_x*: int*[](#keysight.ads.dds.DDSFile.snap_grid_per_display_grid_x "Link to this definition")
    :   The snap grid per display grid for the X-coordinate for pages in the DDSFile.

    *property* snap\_grid\_per\_display\_grid\_y*: int*[](#keysight.ads.dds.DDSFile.snap_grid_per_display_grid_y "Link to this definition")
    :   The snap grid per display grid for the Y-coordinate for pages in the DDSFile.

    *property* type*: ObjectType*[](#keysight.ads.dds.DDSFile.type "Link to this definition")

    *property* windows*: list[[Window](windows.md#keysight.ads.dds.Window "keysight.ads.dds.core.ddwin.Window")]*[](#keysight.ads.dds.DDSFile.windows "Link to this definition")
    :   A list of Windows viewing the contents of the DDSFile.

        See also

        [`new_window()`](#keysight.ads.dds.DDSFile.new_window "keysight.ads.dds.DDSFile.new_window")
        :   Create a new window in the DDSFile.


---

<!-- === 来源: reference/dds/grid.md === -->

# Grid[](#grid "Link to this heading")

*class* keysight.ads.dds.GridType[](#keysight.ads.dds.GridType "Link to this definition")
:   An enumerated type for describing grids. The grid is accessed in class [`DDSFile`](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile").

    DOT\_GRID *= <GridType.DotGrid: 0>*[](#keysight.ads.dds.GridType.DOT_GRID "Link to this definition")
    :   This value will make the grid on pages be displayed with dots.

    LINE\_GRID *= <GridType.LineGrid: 1>*[](#keysight.ads.dds.GridType.LINE_GRID "Link to this definition")
    :   This value will make the grid on pages be displyed with lines.

    NO\_GRID *= <GridType.NoGrid: 2>*[](#keysight.ads.dds.GridType.NO_GRID "Link to this definition")
    :   This value will make the grid on pages not be displayed.

    *property* str*: str*[](#keysight.ads.dds.GridType.str "Link to this definition")


---

<!-- === 来源: reference/dds/group.md === -->

# Group[](#group "Link to this heading")

*class* keysight.ads.dds.Group[](#keysight.ads.dds.Group "Link to this definition")
:   Objects grouped together.

    This class cannot be instantiated directly. See [`Page.add_group()`](page.md#keysight.ads.dds.Page.add_group "keysight.ads.dds.Page.add_group").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Group.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Group.delete_object "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Group.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Group.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Group.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Group.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Group.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Group.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Group.type "Link to this definition")


---

<!-- === 来源: reference/dds/index.md === -->

# keysight.ads.dds[](#module-keysight.ads.dds "Link to this heading")

ADS Data Display scripting.

Automate the Data Display Environment using the `keysight.ads.dds` package. This is typically
imported as:

```
from keysight.ads import dds
```

## Classes[](#classes "Link to this heading")

* [DDSFile](file.md)
  + [`DDSFile`](file.md#keysight.ads.dds.DDSFile)
* [Page](page.md)
  + [`Page`](page.md#keysight.ads.dds.Page)
* [Point](point.md)
  + [`Point`](point.md#keysight.ads.dds.Point)
* [Rect](rect.md)
  + [`Rect`](rect.md#keysight.ads.dds.Rect)
* [Grid](grid.md)
  + [`GridType`](grid.md#keysight.ads.dds.GridType)
* [Plots](plots.md)
  + [`AntennaPlot`](plots.md#keysight.ads.dds.AntennaPlot)
  + [`Listing`](plots.md#keysight.ads.dds.Listing)
  + [`PolarPlot`](plots.md#keysight.ads.dds.PolarPlot)
  + [`RectPlot`](plots.md#keysight.ads.dds.RectPlot)
  + [`Slider`](plots.md#keysight.ads.dds.Slider)
  + [`SmithChart`](plots.md#keysight.ads.dds.SmithChart)
  + [`StackedPlot`](plots.md#keysight.ads.dds.StackedPlot)
* [Axes](axes.md)
  + [`AntennaIndepAxis`](axes.md#keysight.ads.dds.AntennaIndepAxis)
  + [`AntennaDepAxis`](axes.md#keysight.ads.dds.AntennaDepAxis)
  + [`PolarIndepAxis`](axes.md#keysight.ads.dds.PolarIndepAxis)
  + [`PolarDepAxis`](axes.md#keysight.ads.dds.PolarDepAxis)
  + [`RectAxis`](axes.md#keysight.ads.dds.RectAxis)
  + [`SmithChartIndepAxis`](axes.md#keysight.ads.dds.SmithChartIndepAxis)
  + [`SmithChartDepAxis`](axes.md#keysight.ads.dds.SmithChartDepAxis)
  + [`TextAxis`](axes.md#keysight.ads.dds.TextAxis)
* [Legend](legend.md)
  + [`Legend`](legend.md#keysight.ads.dds.Legend)
* [Trace](trace.md)
  + [`Trace`](trace.md#keysight.ads.dds.Trace)
  + [`TextTrace`](trace.md#keysight.ads.dds.TextTrace)
* [Markers](marker.md)
  + [`TraceMarker`](marker.md#keysight.ads.dds.TraceMarker)
  + [`MarkerType`](marker.md#keysight.ads.dds.MarkerType)
  + [`MarkerMode`](marker.md#keysight.ads.dds.MarkerMode)
  + [`MarkerReadoutContentProperties`](marker.md#keysight.ads.dds.MarkerReadoutContentProperties)
  + [`TraceMarkerSymbol`](marker.md#keysight.ads.dds.TraceMarkerSymbol)
  + [`TraceMarkerSymbolProperties`](marker.md#keysight.ads.dds.TraceMarkerSymbolProperties)
* [Line Markers](linemarker.md)
  + [`LineMarker`](linemarker.md#keysight.ads.dds.LineMarker)
  + [`LineMarkerSymbolProperties`](linemarker.md#keysight.ads.dds.LineMarkerSymbolProperties)
* [Limit Lines](limitlines.md)
  + [`LimitLine`](limitlines.md#keysight.ads.dds.LimitLine)
  + [`LimitLineType`](limitlines.md#keysight.ads.dds.LimitLineType)
* [Masks](masks.md)
  + [`LineMask`](masks.md#keysight.ads.dds.LineMask)
  + [`PolygonMask`](masks.md#keysight.ads.dds.PolygonMask)
  + [`PolylineMask`](masks.md#keysight.ads.dds.PolylineMask)
  + [`RectMask`](masks.md#keysight.ads.dds.RectMask)
* [Specification](specifications.md)
  + [`Specification`](specifications.md#keysight.ads.dds.Specification)
* [Equation](equation.md)
  + [`Equation`](equation.md#keysight.ads.dds.Equation)
* [PyEquation](pyequation.md)
  + [`PyEquation`](pyequation.md#keysight.ads.dds.PyEquation)
* [Text](text.md)
  + [`Text`](text.md#keysight.ads.dds.Text)
* [Picture](picture.md)
  + [`Picture`](picture.md#keysight.ads.dds.Picture)
* [Shapes](shapes.md)
  + [`Box`](shapes.md#keysight.ads.dds.Box)
  + [`Circle`](shapes.md#keysight.ads.dds.Circle)
  + [`Line`](shapes.md#keysight.ads.dds.Line)
  + [`Polyline`](shapes.md#keysight.ads.dds.Polyline)
  + [`Polygon`](shapes.md#keysight.ads.dds.Polygon)
* [Group](group.md)
  + [`Group`](group.md#keysight.ads.dds.Group)
* [Common Properties](basic.md)
  + [`Color`](basic.md#keysight.ads.dds.Color)
  + [`DensitySymbolProperties`](basic.md#keysight.ads.dds.DensitySymbolProperties)
  + [`FillProperties`](basic.md#keysight.ads.dds.FillProperties)
  + [`LineProperties`](basic.md#keysight.ads.dds.LineProperties)
  + [`LineType`](basic.md#keysight.ads.dds.LineType)
  + [`SymbolProperties`](basic.md#keysight.ads.dds.SymbolProperties)
  + [`TextProperties`](basic.md#keysight.ads.dds.TextProperties)
  + [`StringFormat`](basic.md#keysight.ads.dds.StringFormat)
* [Print](print.md)
  + [`PaperSize`](print.md#keysight.ads.dds.PaperSize)
  + [`PrinterOrientation`](print.md#keysight.ads.dds.PrinterOrientation)
* [Object](objects.md)
  + [`ObjectType`](objects.md#keysight.ads.dds.ObjectType)
* [Window](windows.md)
  + [`Window`](windows.md#keysight.ads.dds.Window)
* [Widget](pywidget.md)
  + [`Widget`](pywidget.md#keysight.ads.dds.Widget)

## Functions[](#functions "Link to this heading")

keysight.ads.dds.get\_dds\_path() → str[](#keysight.ads.dds.get_dds_path "Link to this definition")
:   Return the path of the current working directory.

    Returns:
    :   Path of the current working directory.
        In application mode, if running in ADS (Advanced Design System), it is set by default to the path of the opened workspace.
        In application mode, if running in standalone DDS (Data Display), it is set by default to the path from which DDS was invoked.
        In automation mode, it is set by default to the path from which python was invoked.
        This path may be set by [`init_dds_path()`](#keysight.ads.dds.init_dds_path "keysight.ads.dds.init_dds_path").

    Return type:
    :   string

    Examples

    ```
    >>> from keysight.ads import dds
    >>> dds_path = dds.dds.get_dds_path()
    ```

keysight.ads.dds.init\_dds\_path(*path: str | PathLike*) → None[](#keysight.ads.dds.init_dds_path "Link to this definition")
:   Initialize the dds path.

    The dds path is the path used as a default path in the functions [`new_dds_file()`](#keysight.ads.dds.new_dds_file "keysight.ads.dds.new_dds_file"), [`open_dds_file()`](#keysight.ads.dds.open_dds_file "keysight.ads.dds.open_dds_file") and
    [`save()`](file.md#keysight.ads.dds.DDSFile.save "keysight.ads.dds.DDSFile.save").
    It is typically set once per python script.
    In application mode, if running in ADS (Advanced Design System), it is set by default to the path of the opened workspace.
    In application mode, if running in standalone DDS (Data Display), it is set by default to the path from which DDS was invoked.
    In automation mode, it is set by default to the path from which python was invoked.
    This path may be retrieved by [`get_dds_path()`](#keysight.ads.dds.get_dds_path "keysight.ads.dds.get_dds_path").

    Parameters:
    :   **path** (*str* *|* *os.PathLike*) – The path may be a relative path or an absolute path.

    Return type:
    :   None

    Example

    ```
    >>> from keysight.ads import dds
    >>> dds.init_dds_path("c:/tmp")
    ```

keysight.ads.dds.running\_automation() → bool[](#keysight.ads.dds.running_automation "Link to this definition")
:   Return True if running in Data Display automation mode.

    Return type:
    :   bool

keysight.ads.dds.version() → int[](#keysight.ads.dds.version "Link to this definition")
:   Return the product version.

    Returns:
    :   Example: 615

    Return type:
    :   int

keysight.ads.dds.product\_version() → str[](#keysight.ads.dds.product_version "Link to this definition")
:   Return a string with the product name, build version and date of build.

    Returns:
    :   Example: ‘Data Display Server (\*) 615.gDevelop Jul 25 2024 (64-bit)’

    Return type:
    :   str

keysight.ads.dds.close\_dds\_file(*file: [DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile")*) → None[](#keysight.ads.dds.close_dds_file "Link to this definition")
:   Close a DDSFile.

    If the DDSFile has modifications, the modifications will be lost.
    If running in application mode and the DDSFile is currently opened, the Data Display window will be closed.

    Parameters:
    :   **file** ([*DDSFile*](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile")) –

    Return type:
    :   None

    Raises:
    :   **RuntimeError: Error: Attempting to access a deleted object.** – This can occur in application mode when the window associated with DDSFile is closed interactively. In automation mode,
        this can occur if the DDSFile was previously closed.

keysight.ads.dds.get\_dds\_files() → NamedItemCollectionAbc[[DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile")][](#keysight.ads.dds.get_dds_files "Link to this definition")
:   Return a mutable list of opened DDSFiles.

    Return type:
    :   NamedItemCollectionAbc[[DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile")]

    Example

    Obtain a DDSFile named “test.dds” that is currently opened.

    ```
    >>> from keysight.ads import dds as dds
    >>> dds_file = None
    >>> if 'test' in dds.get_dds_files():
    >>>     dds_file = dds.get_dds_files()['test']
    ```

keysight.ads.dds.new\_dds\_file(*dataset: str | ~os.PathLike | None = None*, *path: str | ~os.PathLike | ~collections.abc.Callable[[]*, *str] | None = <function dds\_path>*) → [DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile")[](#keysight.ads.dds.new_dds_file "Link to this definition")
:   Create a new DDSFile and sets the [`data_path`](file.md#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path") and the [`default_dataset`](file.md#keysight.ads.dds.DDSFile.default_dataset "keysight.ads.dds.DDSFile.default_dataset").

    The DDSFile is only in memory until [`save()`](file.md#keysight.ads.dds.DDSFile.save "keysight.ads.dds.DDSFile.save") is called.
    If running in application mode, the new Data Display window will open and be visible.

    Parameters:
    :   * **dataset** (*str* *|* *os.PathLike* *[**optional**]*) – The name of the default dataset. It may be an absolute or relative path.
          It may or may not include the “.ds” extension.
          If the path is relative or omitted or not found, then the default dataset is set to the first
          dataset found in the dataset path (See 2nd parameter for details about the dataset path).
          If no default dataset can be found in the dataset path, it is
          set to whatever was passed, or if no parameter was passed, then it is set to “dataset”.
          The default dataset can be obtained from the property [`default_dataset`](file.md#keysight.ads.dds.DDSFile.default_dataset "keysight.ads.dds.DDSFile.default_dataset").
        * **path** (*str* *|* *os.PathLike* *|* *Callable**[**[**]**,* *str**]* *[**default = get\_dds\_path**(**)**]*) – It may be an absolute path, a relative path, or
          the name of a function that takes no parameters and returns a str that will be interpreted as a path.
          If the path is relative, it is joined to the path obtained from the function [`get_dds_path()`](#keysight.ads.dds.get_dds_path "keysight.ads.dds.get_dds_path").
          If it is omitted, the path is obtained from the function [`get_dds_path()`](#keysight.ads.dds.get_dds_path "keysight.ads.dds.get_dds_path").
          This path will also be used when the DDSFile is saved. See [`save()`](file.md#keysight.ads.dds.DDSFile.save "keysight.ads.dds.DDSFile.save").
          The path will be joined with the property [`data_path`](file.md#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path") and then reset that property
          to reflect the newly joined path. The dataset path is used to search for dataset files and can be
          obtained from the property [`data_path`](file.md#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path").

    Returns:
    :   When a new DDSFile is created, its dataset path and default dataset will be set.
        In addition, a [`Window`](windows.md#keysight.ads.dds.Window "keysight.ads.dds.Window") and the first [`Page`](page.md#keysight.ads.dds.Page "keysight.ads.dds.Page") will be created.

    Return type:
    :   [DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile")

    Examples

    Create a new DDSFile in the current directory indicated by the function get\_dds\_path() that will use
    the first dataset found in property data\_path. Assume the datasets in data\_path are: amplifier.ds, swept\_s\_param.ds.

    ```
    >>> from keysight.ads import dds as dds
    >>> print(get_dds_path())
        c:\\workspaces\\my_wrk
    >>> dds_file = dds.new_dds_file()
    >>> print(dds_file.data_path)
        c:\\workspaces\\my_wrk\\data
    >>> print(dds_file.default_dataset)
    >>> amplifier
    ```

    Create a new DDSFile in a specific ADS workspace and that will use the first dataset found in the property data\_path.
    Assume the datasets in data\_path are: amplifier.ds, swept\_s\_param.ds.

    ```
    >>> from keysight.ads import dds as dds
    >>> dds_file = dds.new_dds_file(None, "c:/tmp/my_wrk")
    >>> print(dds_file.data_path)
        c:\\tmp\\my_wrk\\data
    >>> print(dds_file.default_dataset)
    >>> amplifier
    ```

    Create a new DDSFile in a specific ADS workspace and that will use a specific dataset found in the property data\_path.
    Assume the datasets in data\_path are: amplifier.ds, swept\_s\_param.ds.

    ```
    >>> from keysight.ads import dds as dds
    >>> dds_file = dds.new_dds_file("swept_s_param", "c:/tmp/my_wrk")
    >>> print(dds_file.data_path)
        c:\\tmp\\my_wrk\\data
    >>> print(dds_file.default_dataset)
        swept_s_param
    ```

    Create a new DDSFile and set the dataset to a dataset not found in the data\_path.
    Assume the datasets in data\_path are: amplifier.ds, swept\_s\_param.ds.

    ```
    >>> from keysight.ads import dds as dds
    >>> dds_file = dds.new_dds_file("c:/datasets/sim1.ds", "c:/my_data")
    >>> print(dds_file.data_path)
        c:\\my_data\\data
    >>> print(dds_file.default_dataset)
        c:\\datasets\\sim1.ds
    ```

    See also

    [`default_dataset`](file.md#keysight.ads.dds.DDSFile.default_dataset "keysight.ads.dds.DDSFile.default_dataset")
    :   The default dataset being used by the DDSFile.

    [`data_path`](file.md#keysight.ads.dds.DDSFile.data_path "keysight.ads.dds.DDSFile.data_path")
    :   The default dataset being used by the DDSFile.

keysight.ads.dds.open\_dds\_file(*path: str | PathLike*) → [DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.core.ddobj.DDSFile")[](#keysight.ads.dds.open_dds_file "Link to this definition")
:   Open a DDSFile.

    If running in application mode, a new Data Display window will open and show contents of the DDSFile.

    Parameters:
    :   **path** (*str* *|* *os.PathLike*) – The name of the DDSFile to open. It may be an absolute or relative path.
        The file must include the “.dds” extension.
        If the path is relative, it is joined to the path obtained from the function [`get_dds_path()`](#keysight.ads.dds.get_dds_path "keysight.ads.dds.get_dds_path").

    Return type:
    :   [DDSFile](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile")

    Raises:
    :   * **RuntimeError: The file path is empty.** –
        * **RuntimeError: The file does not exist: <path>** –

    Example

    Modify a DDSFile.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> ddsfile.new_page("newPage")
    >>> ddsfile.save()
    ```


---

<!-- === 来源: reference/dds/legend.md === -->

# Legend[](#legend "Link to this heading")

*class* keysight.ads.dds.Legend[](#keysight.ads.dds.Legend "Link to this definition")
:   Legends help identify specific traces in a plot.

    This class cannot be instantiated directly. An instance is created by the method add\_legend() in a plot.

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Legend.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Legend.delete_object "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.Legend.fill_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Legend.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Legend.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Legend.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Legend.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Legend.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Legend.name "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.Legend.string_format "Link to this definition")

    *property* text\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.Legend.text_properties "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Legend.type "Link to this definition")


---

<!-- === 来源: reference/dds/limitlines.md === -->

# Limit Lines[](#limit-lines "Link to this heading")

*class* keysight.ads.dds.LimitLine[](#keysight.ads.dds.LimitLine "Link to this definition")
:   Limit lines provide an object that indicates a desired expectation of the trace data.

    This class cannot be instantiated directly.
    An instance is created by [`RectPlot.add_greater_than_limit_line()`](plots.md#keysight.ads.dds.RectPlot.add_greater_than_limit_line "keysight.ads.dds.RectPlot.add_greater_than_limit_line"), [`RectPlot.add_less_than_limit_line()`](plots.md#keysight.ads.dds.RectPlot.add_less_than_limit_line "keysight.ads.dds.RectPlot.add_less_than_limit_line"),
    [`RectPlot.add_inside_limit_line()`](plots.md#keysight.ads.dds.RectPlot.add_inside_limit_line "keysight.ads.dds.RectPlot.add_inside_limit_line"), and [`RectPlot.add_outside_limit_line()`](plots.md#keysight.ads.dds.RectPlot.add_outside_limit_line "keysight.ads.dds.RectPlot.add_outside_limit_line").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.LimitLine.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* data\_points*: list[tuple[float | str, float | str]]*[](#keysight.ads.dds.LimitLine.data_points "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.LimitLine.delete_object "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.LimitLine.dep_axis "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.LimitLine.expression "Link to this definition")

    *property* fail\_line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.LimitLine.fail_line_properties "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.LimitLine.indep_axis "Link to this definition")

    *property* is\_locked*: bool*[](#keysight.ads.dds.LimitLine.is_locked "Link to this definition")

    *property* limit\_line\_type*: [LimitLineType](#keysight.ads.dds.LimitLineType "keysight.ads.dds.core.ddplot.LimitLineType")*[](#keysight.ads.dds.LimitLine.limit_line_type "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.LimitLine.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.LimitLine.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.LimitLine.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.LimitLine.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.LimitLine.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.LimitLine.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.LimitLine.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.LimitLine.type "Link to this definition")

*class* keysight.ads.dds.LimitLineType[](#keysight.ads.dds.LimitLineType "Link to this definition")
:   GREATER\_THAN *= <LimitLineType.GreaterThan: 2>*[](#keysight.ads.dds.LimitLineType.GREATER_THAN "Link to this definition")

    INSIDE *= <LimitLineType.Inside: 0>*[](#keysight.ads.dds.LimitLineType.INSIDE "Link to this definition")

    LESS\_THAN *= <LimitLineType.LessThan: 3>*[](#keysight.ads.dds.LimitLineType.LESS_THAN "Link to this definition")

    OUTSIDE *= <LimitLineType.Outside: 1>*[](#keysight.ads.dds.LimitLineType.OUTSIDE "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.LimitLineType.str "Link to this definition")


---

<!-- === 来源: reference/dds/linemarker.md === -->

# Line Markers[](#line-markers "Link to this heading")

*class* keysight.ads.dds.LineMarker[](#keysight.ads.dds.LineMarker "Link to this definition")
:   A line marker displays all trace values at a specific independent value.

    This class cannot be instantiated directly.
    An instance is created by [`RectPlot.add_line_marker()`](plots.md#keysight.ads.dds.RectPlot.add_line_marker "keysight.ads.dds.RectPlot.add_line_marker") and [`StackedPlot.add_line_marker()`](plots.md#keysight.ads.dds.StackedPlot.add_line_marker "keysight.ads.dds.StackedPlot.add_line_marker").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.LineMarker.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.LineMarker.delete_object "Link to this definition")

    *property* dep\_values*: dict[str, str]*[](#keysight.ads.dds.LineMarker.dep_values "Link to this definition")

    *property* indep\_value*: str*[](#keysight.ads.dds.LineMarker.indep_value "Link to this definition")

    *property* is\_name\_displayed*: bool*[](#keysight.ads.dds.LineMarker.is_name_displayed "Link to this definition")

    *property* is\_readout\_displayed*: bool*[](#keysight.ads.dds.LineMarker.is_readout_displayed "Link to this definition")

    *property* is\_symbol\_displayed*: bool*[](#keysight.ads.dds.LineMarker.is_symbol_displayed "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.LineMarker.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.LineMarker.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.LineMarker.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.LineMarker.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.LineMarker.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.LineMarker.name "Link to this definition")

    *property* readout\_content\_properties*: [MarkerReadoutContentProperties](marker.md#keysight.ads.dds.MarkerReadoutContentProperties "keysight.ads.dds.core.ddbase.MarkerReadoutContentProperties")*[](#keysight.ads.dds.LineMarker.readout_content_properties "Link to this definition")

    *property* symbol\_properties*: [LineMarkerSymbolProperties](#keysight.ads.dds.LineMarkerSymbolProperties "keysight.ads.dds.core.ddplot.LineMarkerSymbolProperties")*[](#keysight.ads.dds.LineMarker.symbol_properties "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.LineMarker.type "Link to this definition")

    *property* variable*: VariableBlock | None*[](#keysight.ads.dds.LineMarker.variable "Link to this definition")

*class* keysight.ads.dds.LineMarkerSymbolProperties[](#keysight.ads.dds.LineMarkerSymbolProperties "Link to this definition")
:   *property* color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.LineMarkerSymbolProperties.color "Link to this definition")

    *property* size*: int*[](#keysight.ads.dds.LineMarkerSymbolProperties.size "Link to this definition")


---

<!-- === 来源: reference/dds/marker.md === -->

# Markers[](#markers "Link to this heading")

*class* keysight.ads.dds.TraceMarker[](#keysight.ads.dds.TraceMarker "Link to this definition")
:   Markers return the independent and dependent values of the data.

    This class cannot be instantiated directly.
    An instance is created by the [`Trace.add_marker()`](trace.md#keysight.ads.dds.Trace.add_marker "keysight.ads.dds.Trace.add_marker").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.TraceMarker.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.TraceMarker.delete_object "Link to this definition")

    *property* delta\_dep\_value*: str | None*[](#keysight.ads.dds.TraceMarker.delta_dep_value "Link to this definition")

    *property* delta\_indep\_value*: str | None*[](#keysight.ads.dds.TraceMarker.delta_indep_value "Link to this definition")

    *property* dep\_value*: str*[](#keysight.ads.dds.TraceMarker.dep_value "Link to this definition")

    *property* indep\_value*: str*[](#keysight.ads.dds.TraceMarker.indep_value "Link to this definition")

    *property* index*: int*[](#keysight.ads.dds.TraceMarker.index "Link to this definition")

    *property* is\_name\_displayed*: bool*[](#keysight.ads.dds.TraceMarker.is_name_displayed "Link to this definition")

    *property* is\_readout\_displayed*: bool*[](#keysight.ads.dds.TraceMarker.is_readout_displayed "Link to this definition")

    *property* is\_symbol\_displayed*: bool*[](#keysight.ads.dds.TraceMarker.is_symbol_displayed "Link to this definition")

    *property* marker\_type*: [MarkerType](#keysight.ads.dds.MarkerType "keysight.ads.dds.core.ddplot.MarkerType")*[](#keysight.ads.dds.TraceMarker.marker_type "Link to this definition")

    *property* mode*: [MarkerMode](#keysight.ads.dds.MarkerMode "keysight.ads.dds.core.ddplot.MarkerMode")*[](#keysight.ads.dds.TraceMarker.mode "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.TraceMarker.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.TraceMarker.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.TraceMarker.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.TraceMarker.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.TraceMarker.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.TraceMarker.name "Link to this definition")

    *property* offset*: float | None*[](#keysight.ads.dds.TraceMarker.offset "Link to this definition")

    *property* offset\_dep\_value*: str | None*[](#keysight.ads.dds.TraceMarker.offset_dep_value "Link to this definition")

    *property* offset\_indep\_value*: str | None*[](#keysight.ads.dds.TraceMarker.offset_indep_value "Link to this definition")

    *property* readout\_content\_properties*: [MarkerReadoutContentProperties](#keysight.ads.dds.MarkerReadoutContentProperties "keysight.ads.dds.core.ddbase.MarkerReadoutContentProperties")*[](#keysight.ads.dds.TraceMarker.readout_content_properties "Link to this definition")

    reset\_mode() → None[](#keysight.ads.dds.TraceMarker.reset_mode "Link to this definition")

    set\_delta(*reference\_marker: [TraceMarker](#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker") | str*) → None[](#keysight.ads.dds.TraceMarker.set_delta "Link to this definition")

    set\_offset(*reference\_marker: [TraceMarker](#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker") | str*, *offset\_expr: float | str*) → None[](#keysight.ads.dds.TraceMarker.set_offset "Link to this definition")

    *property* symbol\_properties*: [TraceMarkerSymbolProperties](#keysight.ads.dds.TraceMarkerSymbolProperties "keysight.ads.dds.core.ddplot.TraceMarkerSymbolProperties")*[](#keysight.ads.dds.TraceMarker.symbol_properties "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.TraceMarker.type "Link to this definition")

    *property* variable*: VariableBlock | None*[](#keysight.ads.dds.TraceMarker.variable "Link to this definition")

*class* keysight.ads.dds.MarkerType[](#keysight.ads.dds.MarkerType "Link to this definition")
:   MAX *= <MarkerType.MAX: 8>*[](#keysight.ads.dds.MarkerType.MAX "Link to this definition")

    MIN *= <MarkerType.MIN: 16>*[](#keysight.ads.dds.MarkerType.MIN "Link to this definition")

    NORMAL *= <MarkerType.NORMAL: 1>*[](#keysight.ads.dds.MarkerType.NORMAL "Link to this definition")

    PEAK *= <MarkerType.PEAK: 2>*[](#keysight.ads.dds.MarkerType.PEAK "Link to this definition")

    VALLEY *= <MarkerType.VALLEY: 4>*[](#keysight.ads.dds.MarkerType.VALLEY "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.MarkerType.str "Link to this definition")

*class* keysight.ads.dds.MarkerMode[](#keysight.ads.dds.MarkerMode "Link to this definition")
:   DELTA *= <MarkerMode.DELTA: 1>*[](#keysight.ads.dds.MarkerMode.DELTA "Link to this definition")

    NORMAL *= <MarkerMode.NORMAL: 0>*[](#keysight.ads.dds.MarkerMode.NORMAL "Link to this definition")

    OFFSET *= <MarkerMode.OFFSET: 2>*[](#keysight.ads.dds.MarkerMode.OFFSET "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.MarkerMode.str "Link to this definition")

*class* keysight.ads.dds.MarkerReadoutContentProperties[](#keysight.ads.dds.MarkerReadoutContentProperties "Link to this definition")
:   *property* show\_dependent\_value*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_dependent_value "Link to this definition")

    *property* show\_independent\_value*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_independent_value "Link to this definition")

    *property* show\_name*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_name "Link to this definition")

    *property* show\_smith\_chart\_value*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_smith_chart_value "Link to this definition")

    *property* show\_sweep\_value*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_sweep_value "Link to this definition")

    *property* show\_type*: bool*[](#keysight.ads.dds.MarkerReadoutContentProperties.show_type "Link to this definition")

*class* keysight.ads.dds.TraceMarkerSymbol[](#keysight.ads.dds.TraceMarkerSymbol "Link to this definition")
:   CIRCLE *= <TraceMarkerSymbol.CIRCLE: 2>*[](#keysight.ads.dds.TraceMarkerSymbol.CIRCLE "Link to this definition")

    TRIANGLE\_EMPTY *= <TraceMarkerSymbol.TRIANGLE\_EMPTY: 1>*[](#keysight.ads.dds.TraceMarkerSymbol.TRIANGLE_EMPTY "Link to this definition")

    TRIANGLE\_FILLED *= <TraceMarkerSymbol.TRIANGLE\_FILLED: 0>*[](#keysight.ads.dds.TraceMarkerSymbol.TRIANGLE_FILLED "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.TraceMarkerSymbol.str "Link to this definition")

*class* keysight.ads.dds.TraceMarkerSymbolProperties[](#keysight.ads.dds.TraceMarkerSymbolProperties "Link to this definition")
:   *property* color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.TraceMarkerSymbolProperties.color "Link to this definition")

    *property* size*: int*[](#keysight.ads.dds.TraceMarkerSymbolProperties.size "Link to this definition")

    *property* type*: [TraceMarkerSymbol](#keysight.ads.dds.TraceMarkerSymbol "keysight.ads.dds.core.ddplot.TraceMarkerSymbol") | None*[](#keysight.ads.dds.TraceMarkerSymbolProperties.type "Link to this definition")


---

<!-- === 来源: reference/dds/masks.md === -->

# Masks[](#masks "Link to this heading")

*class* keysight.ads.dds.LineMask[](#keysight.ads.dds.LineMask "Link to this definition")
:   Line mask on a plot.

    This class cannot be instantiated directly.
    An instance is created by [`RectPlot.add_line_mask()`](plots.md#keysight.ads.dds.RectPlot.add_line_mask "keysight.ads.dds.RectPlot.add_line_mask").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.LineMask.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* data\_points*: list[tuple[float | str, float | str]]*[](#keysight.ads.dds.LineMask.data_points "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.LineMask.delete_object "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.LineMask.dep_axis "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.LineMask.indep_axis "Link to this definition")

    *property* is\_locked*: bool*[](#keysight.ads.dds.LineMask.is_locked "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.LineMask.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.LineMask.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.LineMask.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.LineMask.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.LineMask.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.LineMask.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.LineMask.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.LineMask.type "Link to this definition")

*class* keysight.ads.dds.PolygonMask[](#keysight.ads.dds.PolygonMask "Link to this definition")
:   Polygon mask on a plot.

    This class cannot be instantiated directly.
    An instance is created by [`RectPlot.add_polygon_mask()`](plots.md#keysight.ads.dds.RectPlot.add_polygon_mask "keysight.ads.dds.RectPlot.add_polygon_mask").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.PolygonMask.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* data\_points*: list[tuple[float | str, float | str]]*[](#keysight.ads.dds.PolygonMask.data_points "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.PolygonMask.delete_object "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.PolygonMask.dep_axis "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.PolygonMask.fill_properties "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.PolygonMask.indep_axis "Link to this definition")

    *property* is\_locked*: bool*[](#keysight.ads.dds.PolygonMask.is_locked "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.PolygonMask.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.PolygonMask.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.PolygonMask.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.PolygonMask.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.PolygonMask.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.PolygonMask.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.PolygonMask.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.PolygonMask.type "Link to this definition")

*class* keysight.ads.dds.PolylineMask[](#keysight.ads.dds.PolylineMask "Link to this definition")
:   Polyline mask on a plot.

    This class cannot be instantiated directly.
    An instance is created by [`RectPlot.add_polyline_mask()`](plots.md#keysight.ads.dds.RectPlot.add_polyline_mask "keysight.ads.dds.RectPlot.add_polyline_mask").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.PolylineMask.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* data\_points*: list[tuple[float | str, float | str]]*[](#keysight.ads.dds.PolylineMask.data_points "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.PolylineMask.delete_object "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.PolylineMask.dep_axis "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.PolylineMask.indep_axis "Link to this definition")

    *property* is\_locked*: bool*[](#keysight.ads.dds.PolylineMask.is_locked "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.PolylineMask.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.PolylineMask.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.PolylineMask.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.PolylineMask.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.PolylineMask.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.PolylineMask.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.PolylineMask.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.PolylineMask.type "Link to this definition")

*class* keysight.ads.dds.RectMask[](#keysight.ads.dds.RectMask "Link to this definition")
:   Rectangle mask on a plot.

    This class cannot be instantiated directly.
    An instance is created by [`RectPlot.add_rectangle_mask()`](plots.md#keysight.ads.dds.RectPlot.add_rectangle_mask "keysight.ads.dds.RectPlot.add_rectangle_mask").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.RectMask.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* data\_points*: list[tuple[float | str, float | str]]*[](#keysight.ads.dds.RectMask.data_points "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.RectMask.delete_object "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.RectMask.dep_axis "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.RectMask.fill_properties "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.RectMask.indep_axis "Link to this definition")

    *property* is\_locked*: bool*[](#keysight.ads.dds.RectMask.is_locked "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.RectMask.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.RectMask.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.RectMask.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.RectMask.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.RectMask.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.RectMask.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.RectMask.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.RectMask.type "Link to this definition")


---

<!-- === 来源: reference/dds/objects.md === -->

# Object[](#object "Link to this heading")

*class* keysight.ads.dds.ObjectType[](#keysight.ads.dds.ObjectType "Link to this definition")
:   This class provides functions that can determine what type of object is passed.

    *static* is\_antenna\_plot(*obj: BaseObject*) → TypeGuard[[AntennaPlot](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.AntennaPlot")][](#keysight.ads.dds.ObjectType.is_antenna_plot "Link to this definition")

    *static* is\_box(*obj: BaseObject*) → TypeGuard[[Box](shapes.md#keysight.ads.dds.Box "keysight.ads.dds.Box")][](#keysight.ads.dds.ObjectType.is_box "Link to this definition")

    *static* is\_circle(*obj: BaseObject*) → TypeGuard[[Circle](shapes.md#keysight.ads.dds.Circle "keysight.ads.dds.Circle")][](#keysight.ads.dds.ObjectType.is_circle "Link to this definition")

    *static* is\_equation(*obj: BaseObject*) → TypeGuard[[Equation](equation.md#keysight.ads.dds.Equation "keysight.ads.dds.Equation")][](#keysight.ads.dds.ObjectType.is_equation "Link to this definition")

    *static* is\_group(*obj: BaseObject*) → TypeGuard[[Group](group.md#keysight.ads.dds.Group "keysight.ads.dds.Group")][](#keysight.ads.dds.ObjectType.is_group "Link to this definition")

    *static* is\_limit\_line(*obj: BaseObject*) → TypeGuard[[LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.LimitLine")][](#keysight.ads.dds.ObjectType.is_limit_line "Link to this definition")

    *static* is\_line(*obj: BaseObject*) → TypeGuard[[Line](shapes.md#keysight.ads.dds.Line "keysight.ads.dds.Line")][](#keysight.ads.dds.ObjectType.is_line "Link to this definition")

    *static* is\_listing(*obj: BaseObject*) → TypeGuard[[Listing](plots.md#keysight.ads.dds.Listing "keysight.ads.dds.Listing")][](#keysight.ads.dds.ObjectType.is_listing "Link to this definition")

    *static* is\_mask(*obj: BaseObject*) → TypeGuard[Mask][](#keysight.ads.dds.ObjectType.is_mask "Link to this definition")

    *static* is\_picture(*obj: BaseObject*) → TypeGuard[[Picture](picture.md#keysight.ads.dds.Picture "keysight.ads.dds.Picture")][](#keysight.ads.dds.ObjectType.is_picture "Link to this definition")

    *static* is\_plot(*obj: BaseObject*) → TypeGuard[Plot][](#keysight.ads.dds.ObjectType.is_plot "Link to this definition")

    *static* is\_polar\_plot(*obj: BaseObject*) → TypeGuard[[PolarPlot](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.PolarPlot")][](#keysight.ads.dds.ObjectType.is_polar_plot "Link to this definition")

    *static* is\_polygon(*obj: BaseObject*) → TypeGuard[[Polygon](shapes.md#keysight.ads.dds.Polygon "keysight.ads.dds.Polygon")][](#keysight.ads.dds.ObjectType.is_polygon "Link to this definition")

    *static* is\_polyline(*obj: BaseObject*) → TypeGuard[[Polyline](shapes.md#keysight.ads.dds.Polyline "keysight.ads.dds.Polyline")][](#keysight.ads.dds.ObjectType.is_polyline "Link to this definition")

    *static* is\_py\_equation(*obj: BaseObject*) → TypeGuard[[PyEquation](pyequation.md#keysight.ads.dds.PyEquation "keysight.ads.dds.PyEquation")][](#keysight.ads.dds.ObjectType.is_py_equation "Link to this definition")

    *static* is\_rect\_plot(*obj: BaseObject*) → TypeGuard[[RectPlot](plots.md#keysight.ads.dds.RectPlot "keysight.ads.dds.RectPlot")][](#keysight.ads.dds.ObjectType.is_rect_plot "Link to this definition")

    *static* is\_slider(*obj: BaseObject*) → TypeGuard[[Slider](plots.md#keysight.ads.dds.Slider "keysight.ads.dds.Slider")][](#keysight.ads.dds.ObjectType.is_slider "Link to this definition")

    *static* is\_smith\_chart(*obj: BaseObject*) → TypeGuard[[SmithChart](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.SmithChart")][](#keysight.ads.dds.ObjectType.is_smith_chart "Link to this definition")

    *static* is\_specification(*obj: BaseObject*) → TypeGuard[[Specification](specifications.md#keysight.ads.dds.Specification "keysight.ads.dds.Specification")][](#keysight.ads.dds.ObjectType.is_specification "Link to this definition")

    *static* is\_stacked\_plot(*obj: BaseObject*) → TypeGuard[[StackedPlot](plots.md#keysight.ads.dds.StackedPlot "keysight.ads.dds.StackedPlot")][](#keysight.ads.dds.ObjectType.is_stacked_plot "Link to this definition")

    *static* is\_text(*obj: BaseObject*) → TypeGuard[[Text](text.md#keysight.ads.dds.Text "keysight.ads.dds.Text")][](#keysight.ads.dds.ObjectType.is_text "Link to this definition")

    *static* is\_trace(*obj: BaseObject*) → TypeGuard[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.Trace")][](#keysight.ads.dds.ObjectType.is_trace "Link to this definition")

    *static* is\_widget(*obj: BaseObject*) → TypeGuard[[Widget](pywidget.md#keysight.ads.dds.Widget "keysight.ads.dds.Widget")][](#keysight.ads.dds.ObjectType.is_widget "Link to this definition")


---

<!-- === 来源: reference/dds/page.md === -->

# Page[](#page "Link to this heading")

*class* keysight.ads.dds.Page[](#keysight.ads.dds.Page "Link to this definition")
:   A page is an area to organize Data Display objects that can be viewed in windows.

    This class cannot be instantiated directly. When a Data Display file is created, a page is
    automatically created. Additional pages can be created with [`DDSFile.new_page()`](file.md#keysight.ads.dds.DDSFile.new_page "keysight.ads.dds.DDSFile.new_page").
    Pages can be access by the property [`DDSFile.pages`](file.md#keysight.ads.dds.DDSFile.pages "keysight.ads.dds.DDSFile.pages")

    Data Display objects that can be inserted into a page include plots, equations, shapes,
    pictures, text, widgets, and groups.

    Example

    Access default page of a DDSFile.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> default_page = ddsfile.pages[0]
    ```

    Create a new page in a DDSFile.

    ```
    >>> from keysight.ads import dds as dds
    >>> ddsfile = dds.open_dds_file("test.dds")
    >>> myPage = ddsfile.new_page("myPage")
    >>> print(ddsfile.pages)
        (<Page "myPage">, <Page "page 1">)
    >>> ddfile.save()
    ```

    add\_antenna\_plot(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [AntennaPlot](plots.md#keysight.ads.dds.AntennaPlot "keysight.ads.dds.core.ddplot.AntennaPlot")[](#keysight.ads.dds.Page.add_antenna_plot "Link to this definition")
    :   Add an antenna plot to the page,.

        It is the same as [`add_plot()`](#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot") except that it returns an antenna plot.

    add\_box(*rect: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → [Box](shapes.md#keysight.ads.dds.Box "keysight.ads.dds.core.ddshape.Box")[](#keysight.ads.dds.Page.add_box "Link to this definition")
    :   Add a box to the page.

        Parameters:
        :   **rect** ([*Rect*](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – Coordinates of the box.

        Returns:
        :   Returns the box placed on the page.

        Return type:
        :   [Box](shapes.md#keysight.ads.dds.Box "keysight.ads.dds.Box")

        Example

        Insert a box.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> tl = dds.Point(500, 500)
        >>> br = dds.Point(1500, 1500)
        >>> obj = page.add_box(dds.Rect(top_left=tl, bottom_right=br))
        ```

    add\_circle(*center: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*, *radius: int*) → [Circle](shapes.md#keysight.ads.dds.Circle "keysight.ads.dds.core.ddshape.Circle")[](#keysight.ads.dds.Page.add_circle "Link to this definition")
    :   Add a circle to the page.

        Parameters:
        :   * **center** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]*) – Coordinates of the center of the circle.
            * **radius** (*int*) – Specifies the radius of the circle.

        Returns:
        :   Returns the circle placed on the page.

        Return type:
        :   [Circle](shapes.md#keysight.ads.dds.Circle "keysight.ads.dds.Circle")

        Example

        Insert a circle.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> center = dds.Point(500, 500)
        >>> obj = page.add_circle(center, 100)
        ```

    add\_equation(*name: str*, *value: str*, */*, *location: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*) → [Equation](equation.md#keysight.ads.dds.Equation "keysight.ads.dds.core.ddshape.Equation")[](#keysight.ads.dds.Page.add_equation "Link to this definition")

    add\_equation(*expression: str*, *location: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, */*) → [Equation](equation.md#keysight.ads.dds.Equation "keysight.ads.dds.core.ddshape.Equation")
    :   Add an equation to the page.

        Parameters:
        :   * **expression\_or\_name** (*name - str**,* *value -str* *|* *expressions : str*) – An expression can be specified by two strings, e.g. “x” and “S11”, or by one string, e.g. “x = S11”
            * **Location** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]* *[**optional**,* *default = None**]*) – Coordinates of where to place the equation on the page.
              If a Point or tuple[int,int] is passed, the top\_left corner of the equation will be placed at that location.
              If omitted, the equation is placed in an empty spot on the page.
              The location of the equation may be moved to a different location with the method [`Equation.move()`](equation.md#keysight.ads.dds.Equation.move "keysight.ads.dds.Equation.move").

        Returns:
        :   Returns the equation placed on the page.

        Return type:
        :   [Equation](equation.md#keysight.ads.dds.Equation "keysight.ads.dds.Equation")

        Raises:
        :   **RuntimeError: The equation must contain a name and value separated by an = sign.** – This occurs when only 1 string parameter is passed that does not contain a full expression.

        Example

        Insert equations.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> page = dds_file.pages[0]
        >>> equ1 = page.add_equation("x", "S11")
        >>> print(equ1)
            <UserExpression "x=S11">
        >>> equ2 = page.add_equation("y = S12",(100,100))
        >>> print(equ2)
            <UserExpression "y=S12">
        >>> dds_file.save()
        ```

    add\_group(*objs: list[GraphicalObject]*) → [Group](group.md#keysight.ads.dds.Group "keysight.ads.dds.core.ddshape.Group")[](#keysight.ads.dds.Page.add_group "Link to this definition")
    :   Add a group to the page.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Returns:
        :   Returns the group that contains the specified objects.

        Return type:
        :   [Group](group.md#keysight.ads.dds.Group "keysight.ads.dds.Group")

        Example

        Insert a group.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> eq = page.add_equation("x", "10")
        >>> text = page.add_text("text", (0, 0))
        >>> group = page.add_group([eq, text])
        ```

    add\_line(*start: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*, *end: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → [Line](shapes.md#keysight.ads.dds.Line "keysight.ads.dds.core.ddshape.Line")[](#keysight.ads.dds.Page.add_line "Link to this definition")
    :   Add a line to the page.

        Parameters:
        :   * **start** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]*) – Coordinates of where to start the line.
            * **end** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]*) – Coordinates of where to end the line.

        Returns:
        :   Returns the line placed on the page.

        Return type:
        :   [Line](shapes.md#keysight.ads.dds.Line "keysight.ads.dds.Line")

        Example

        Insert a line.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> start = dds.Point(500, 500)
        >>> end = dds.Point(1500, 1500)
        >>> obj = page.add_line(start, end)
        ```

    add\_list(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [Listing](plots.md#keysight.ads.dds.Listing "keysight.ads.dds.core.ddplot.Listing")[](#keysight.ads.dds.Page.add_list "Link to this definition")
    :   Add a list plot to the page.

        It is the same as [`add_plot()`](#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot") except that it returns a list plot.

    add\_picture(*path: str*, *rect: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → [Picture](picture.md#keysight.ads.dds.Picture "keysight.ads.dds.core.ddshape.Picture")[](#keysight.ads.dds.Page.add_picture "Link to this definition")
    :   Add a picture to the page.

        Parameters:
        :   * **path** (*str*) – The path of the file that contains the picture. This path may be either a relative or absolute path.
            * **rect** ([*Rect*](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – Coordinates of the rectangle that will contain the picture.

        Returns:
        :   Returns the picture placed on the page.

        Return type:
        :   [Picture](picture.md#keysight.ads.dds.Picture "keysight.ads.dds.Picture")

        Example

        Insert a picture.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> rect = dds.Rect(top=0, left=0, bottom=100, right=100)
        >>> obj = page.add_picture("some_path", rect)
        ```

    add\_plot(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [RectPlot](plots.md#keysight.ads.dds.RectPlot "keysight.ads.dds.core.ddplot.RectPlot")[](#keysight.ads.dds.Page.add_plot "Link to this definition")
    :   Add a rectangle plot to the page.

        Parameters:
        :   * **Location** ([*Rect*](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.Rect") *|* [*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]* *[**optional**,* *default = None**]*) – Coordinates of where to place the plot on the page.
              If a Rect is passed, the plot will be placed at that location, and it will have the dimensions of the Rect.
              If a Point or tuple[int,int] is passed, the top\_left corner of the plot will be placed at that location,
              and it will be a default size.
              If omitted, the plot is placed in an empty spot on the page, and it will be a default size.
              The location of the plot may be moved to a different location with the method [`RectPlot.move()`](plots.md#keysight.ads.dds.RectPlot.move "keysight.ads.dds.RectPlot.move").
              The location and size of the plot may be modified with the property [`RectPlot.bbox`](plots.md#keysight.ads.dds.RectPlot.bbox "keysight.ads.dds.RectPlot.bbox").
            * **traces** (*str* *|* *list**[**str**]* *[**optional**,* *default = None**]*) – A single trace or a list of trace specified by name that will be placed on the plot.
              A trace may be a variable from a dataset or it may be an equation in the DDSFile.
              See [`Trace`](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.Trace") for details.
              If omitted, an empty plot will be created.
              Traces may be added with the methods [`RectPlot.add_trace()`](plots.md#keysight.ads.dds.RectPlot.add_trace "keysight.ads.dds.RectPlot.add_trace") and [`RectPlot.add_traces()`](plots.md#keysight.ads.dds.RectPlot.add_traces "keysight.ads.dds.RectPlot.add_traces").
            * **title** (*str* *[**optional**,* *default = None**]*) – The string to be used as the title of the plot.
              If omitted, the plot will not have a title.
              The title may be added by modifying the property [`RectPlot.title`](plots.md#keysight.ads.dds.RectPlot.title "keysight.ads.dds.RectPlot.title").

        Returns:
        :   Returns the rectangle plot placed on the page.

        Return type:
        :   [RectPlot](plots.md#keysight.ads.dds.RectPlot "keysight.ads.dds.RectPlot")

        Example

        Insert two rectangle plots side by side onto the default page.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> page = dds_file.pages[0]
        >>> plot = page.add_plot(dds.Rect(top=0,left=0,bottom=4000,right=4000), ["dB(S11)", "eqn1"], "Rectangle Plot 1")
        >>> empty_plot = page.add_plot()
        >>> empty_plot.add_traces(["dB(S12)","eqn1"])
        >>> empty_plot.move((6000,-4500))
        >>> empty_plot.title = "Rectangle Plot 2"
        >>> dds_file.save()
        ```

    add\_polar\_plot(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [PolarPlot](plots.md#keysight.ads.dds.PolarPlot "keysight.ads.dds.core.ddplot.PolarPlot")[](#keysight.ads.dds.Page.add_polar_plot "Link to this definition")
    :   Add a polar plot to the page.

        It is the same as [`add_plot()`](#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot") except that it returns a polar plot.

    add\_polygon(*pts: list[[Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]]*) → [Polygon](shapes.md#keysight.ads.dds.Polygon "keysight.ads.dds.core.ddshape.Polygon")[](#keysight.ads.dds.Page.add_polygon "Link to this definition")
    :   Add a polygon to the page.

        Parameters:
        :   **pts** (*list**[*[*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]**]*) – Coordinates of vertices of the polygon.

        Returns:
        :   Returns the polygon placed on the page.

        Return type:
        :   [Polygon](shapes.md#keysight.ads.dds.Polygon "keysight.ads.dds.Polygon")

        Example

        Insert a polygon.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> points = [
        >>>     dds.Point(2000, 2000),
        >>>     dds.Point(3000, 3000),
        >>>     dds.Point(4000, 4000),
        >>> ]
        >>> obj = page.add_polygon(points)
        ```

    add\_polyline(*pts: list[[Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]]*) → [Polyline](shapes.md#keysight.ads.dds.Polyline "keysight.ads.dds.core.ddshape.Polyline")[](#keysight.ads.dds.Page.add_polyline "Link to this definition")
    :   Add a polyline to the page.

        Parameters:
        :   **pts** (*list**[*[*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]**]*) – Coordinates of vertices of the polyline.

        Returns:
        :   Returns the polyline placed on the page.

        Return type:
        :   PolyLine

        Example

        Insert a polyline.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> points = [
        >>>     dds.Point(2000, 2000),
        >>>     dds.Point(3000, 3000),
        >>>     dds.Point(4000, 4000),
        >>> ]
        >>> obj = page.add_polyline(points)
        ```

    add\_py\_equation(*expression: str*, *location: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*) → [PyEquation](pyequation.md#keysight.ads.dds.PyEquation "keysight.ads.dds.core.ddshape.PyEquation")[](#keysight.ads.dds.Page.add_py_equation "Link to this definition")
    :   Add a python code to the page as a graphical object.

        Parameters:
        :   * **expression** (*str*) – An expression can be one or multiple lines of python code.
            * **Location** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]* *[**optional**,* *default = None**]*) – Coordinates of where to place the equation on the page.
              If a Point or tuple[int,int] is passed, the top\_left corner of the equation will be placed at that location.
              If omitted, the equation is placed in an empty spot on the page.

        Returns:
        :   Returns the python object placed on the page.

        Return type:
        :   [PyEquation](pyequation.md#keysight.ads.dds.PyEquation "keysight.ads.dds.PyEquation")

        Examples

        Add a python equation that calculates a numerical value

        ```
        >>> exp = page.add_py_equation('''
        from math import sqrt
        y = sqrt(4)''')
        >>> print(exp.values['y'])
        2
        ```

    add\_slider(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [Slider](plots.md#keysight.ads.dds.Slider "keysight.ads.dds.core.ddplot.Slider")[](#keysight.ads.dds.Page.add_slider "Link to this definition")
    :   Add a slider to the page.

        A slider will typically have one trace with a marker for an independent variable.

        Example

        For a swept simulation with Independent Variables ‘R1’ and ‘R2’ and Dependent Variable ‘V’, the trace
        would be “V[::,0]” for sweeping with ‘R1’ data.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.open_dds_file("test.dds")
        >>> page = dds_file.pages[0]
        >>> plot = page.add_slider(traces="swept_simulation..V[::,0]")
        >>> dds_file.save()
        ```

    add\_smith\_chart(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [SmithChart](plots.md#keysight.ads.dds.SmithChart "keysight.ads.dds.core.ddplot.SmithChart")[](#keysight.ads.dds.Page.add_smith_chart "Link to this definition")
    :   Add a smith chart to the page.

        It is the same as [`add_plot()`](#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot") except that it returns a smith chart.

    add\_stacked\_plot(*location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*, *traces: str | list[str] | None = None*, *title: str | None = None*) → [StackedPlot](plots.md#keysight.ads.dds.StackedPlot "keysight.ads.dds.core.ddplot.StackedPlot")[](#keysight.ads.dds.Page.add_stacked_plot "Link to this definition")
    :   Add a stacked plot to the page.

        It is the same as [`add_plot()`](#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot") except that it returns a stacked plot.

    add\_text(*text: str*, *location: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → [Text](text.md#keysight.ads.dds.Text "keysight.ads.dds.core.ddshape.Text")[](#keysight.ads.dds.Page.add_text "Link to this definition")
    :   Add a text to the page.

        Parameters:
        :   * **text** (*str*) – Contents of the text.
            * **location** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,**int**]*) – Coordinates of the location of the text.

        Returns:
        :   Returns the text placed on the page.

        Return type:
        :   [Text](text.md#keysight.ads.dds.Text "keysight.ads.dds.Text")

        Example

        Insert a text.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> obj = page.add_text("text", (0, 0))
        ```

    add\_widget(*widget: QWidget*, *location: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect") | [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | None = None*) → [Widget](pywidget.md#keysight.ads.dds.Widget "keysight.ads.dds.core.ddshape.Widget")[](#keysight.ads.dds.Page.add_widget "Link to this definition")

    align\_bottom(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_bottom "Link to this definition")
    :   Align a list of graphical objects along the bottom coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the bottom.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_bottom([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(50,0), bottom_right=(150,100)">
        ```

    align\_center\_horizontal(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_center_horizontal "Link to this definition")
    :   Align a list of graphical objects along the center horizontal coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the center horizontal.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_center_horizontal([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(50,0), bottom_right=(150,100)">
        ```

    align\_center\_vertical(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_center_vertical "Link to this definition")
    :   Align a list of graphical objects along the center vertical coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the center vertical.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_center_vertical([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(0,50), bottom_right=(100,150)">
        ```

    align\_grid(*objs: list[GraphicalObject]*, *rows: int*, *columns: int*) → None[](#keysight.ads.dds.Page.align_grid "Link to this definition")
    :   Align a list of graphical objects into specified rows and columns, based on the location of the first object in the list.

        Parameters:
        :   * **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.
            * **rows** (*int*) – The number of rows in the layout of the objects.
            * **columns** (*int*) – The number of columns in the layout of the objects.

        Return type:
        :   None

        Raises:
        :   **RuntimeError: Not enough rows and columns specified for objects.** – Too many objects to fit in the specified row/column layout.

        Example

        Align objects on the grid in 2 rows, 1 column.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_grid([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(0,200), bottom_right=(100,300)">
        ```

    align\_left(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_left "Link to this definition")
    :   Align a list of graphical objects along the left coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the left.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_left([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(0,50), bottom_right=(100,150)">
        ```

    align\_right(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_right "Link to this definition")
    :   Align a list of graphical objects along the right coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the right.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_right([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(0,50), bottom_right=(100,150)">
        ```

    align\_top(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.align_top "Link to this definition")
    :   Align a list of graphical objects along the top coordinate of the first object in the list.

        Parameters:
        :   **objs** (*list**[**GraphicalObject**]*) – A list of graphical objects, which includes plots, equations, text, shapes, pictures and groups.

        Return type:
        :   None

        Example

        Align objects to the top.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> box1 = page.add_box(dds.Rect(top_left=(0, 0), bottom_right=(100, 100)))
        >>> box2 = page.add_box(dds.Rect(top_left=(50, 50), bottom_right=(150, 150)))
        >>> page.align_top([box1, box2])
        >>> print(box1)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> print(box2)
            <Rect "top_left=(50,0), bottom_right=(150,100)">
        ```

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Page.bbox "Link to this definition")
    :   The calculation of adding the bounding boxes of all the objects on the page.

        This property is Read-only.

        Raises:
        :   **RuntimeError: Invalid bounding box calculated for page.** – This occurs when there are no objects on the page.

        Example

        Find an empty space on a page to place a new plot.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds"")
        >>> page = dds_file.pages[0]
        >>> locForNewPlot = (0,0)
        >>> if len(page.objects) > 0:
        >>>     locForNewPlot = page.bbox.bottom_right + (1000,0)
        >>> plot = page.new_plot(locForNewPlot)
        ```

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Page.change_object_order "Link to this definition")
    :   Change the order that the objects are referenced and displayed.

        Change the order that the objects are referenced and displayed.
        Objects that exist on the page but are not included in
        the list of objects to be reorderd will be place before the
        objects being reordered. Objects that are not referenced
        in the page are ignored.

        Example

        Build three objects and change order to display the box under the
        plot and list.

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>> list = page.add_list();
        >>> box = page.add_box(dds.Rect(top=1000, left=1000, bottom=5000, right=5000));
        >>>
        >>> page.objects
        [<RectPlot "">, <TextPlot "">, <Box "">]
        >>>
        >>> page.change_object_order([list, plot])
        >>>
        >>> page.objects
        [<Box "">, <TextPlot "">, <RectPlot "">]
        ```

    *property* name*: str*[](#keysight.ads.dds.Page.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.Page.objects "Link to this definition")
    :   A list of objects on a page.

        This property is Read-only.
        It is may be modified by adding/deleting objects on the page.

        Example

        Obtain a list of objects in the default page that has a plot and an equation.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds"")
        >>> page = dds_file.pages[0]
        >>> objs == page.objects
        >>> print(objs)
            [<AntennaPlot "">, <UserExpression  "a = S11">]
        >>> textObj = page.add_text("hello", (100,100))
        >>> print(page.objects)
            [<Text "hello", <AntennaPlot "">, <UserExpression  "a = S11">]
        >>> textObj.delete_object()
        >>> print(page.objects)
            [<AntennaPlot "">, <UserExpression  "a = S11">]
        ```

    remove\_group(*group: [Group](group.md#keysight.ads.dds.Group "keysight.ads.dds.core.ddshape.Group")*) → None[](#keysight.ads.dds.Page.remove_group "Link to this definition")
    :   Remove a group to the page.

        Parameters:
        :   **group** ([*Group*](group.md#keysight.ads.dds.Group "keysight.ads.dds.Group")) – The group to remove from the page.

        Return type:
        :   None

        Example

        Insert a group.

        ```
        >>> import keysight.ads.dds as dds
        >>> dds_file = dds.new_dds_file("cell_1.ds", tmp_workspace_path)
        >>> page = dds_file.pages[0]
        >>> eq = page.add_equation("x", "10")
        >>> text = page.add_text("text", (0, 0))
        >>> group = page.add_group([eq, text])
        >>> page.remove(group)
        ```

    *property* selected\_objects*: list[GraphicalObject]*[](#keysight.ads.dds.Page.selected_objects "Link to this definition")
    :   A list of selected objects on a page.

        This property may be modified.

        Example

        Select the plots on the default page of a DDSFile.

        ```
        >>> from keysight.ads import dds as dds
        >>> dds_file = dds.open_dds_file("test.dds"")
        >>> page = dds_file.pages[0]
        >>> selObjs == page.selected_objects
        >>> print(selObjs)
            []
        >>> objs = page.objects
        >>> print(objs)
            [<AntennaPlot "">, <RectPlot "">, <UserExpression  "a = S11">]
        >>> objsToSelect = []
        >>> for obj in objs:
        >>>     if dds.ObjectType.is_plot(obj):
        >>>         objsToSelect.append(obj)
        >>> page.selected_objects = objsToSelect
        >>> selObjs = page.selected_objects
        >>> print(selObjs)
            [<AntennaPlot "">, <RectPlot "">]
        ```

    *property* type*: ObjectType*[](#keysight.ads.dds.Page.type "Link to this definition")


---

<!-- === 来源: reference/dds/picture.md === -->

# Picture[](#picture "Link to this heading")

*class* keysight.ads.dds.Picture[](#keysight.ads.dds.Picture "Link to this definition")
:   An image on a page.

    This class cannot be instantiated directly. See [`Page.add_picture()`](page.md#keysight.ads.dds.Page.add_picture "keysight.ads.dds.Page.add_picture").

    activate() → None[](#keysight.ads.dds.Picture.activate "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Picture.bbox "Link to this definition")
    :   The bounding box associated with an object.

    deactivate() → None[](#keysight.ads.dds.Picture.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.Picture.delete_object "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.Picture.expression "Link to this definition")

    *property* file*: str*[](#keysight.ads.dds.Picture.file "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.Picture.is_deactivated "Link to this definition")

    *property* is\_outlined*: bool*[](#keysight.ads.dds.Picture.is_outlined "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Picture.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Picture.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Picture.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Picture.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Picture.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Picture.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Picture.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Picture.type "Link to this definition")


---

<!-- === 来源: reference/dds/plots.md === -->

# Plots[](#plots "Link to this heading")

*class* keysight.ads.dds.AntennaPlot[](#keysight.ads.dds.AntennaPlot "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_antenna_plot()`](page.md#keysight.ads.dds.Page.add_antenna_plot "keysight.ads.dds.Page.add_antenna_plot").

    activate() → None[](#keysight.ads.dds.AntennaPlot.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.AntennaPlot.add_legend "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.AntennaPlot.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.AntennaPlot.add_traces "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.AntennaPlot.bbox "Link to this definition")
    :   The bounding box associated with an object.

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.AntennaPlot.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.AntennaPlot.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.AntennaPlot.children_bbox "Link to this definition")

    deactivate() → None[](#keysight.ads.dds.AntennaPlot.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.AntennaPlot.delete_object "Link to this definition")

    *property* dep\_axis*: [AntennaDepAxis](axes.md#keysight.ads.dds.AntennaDepAxis "keysight.ads.dds.core.ddplot.AntennaDepAxis")*[](#keysight.ads.dds.AntennaPlot.dep_axis "Link to this definition")

    *property* indep\_axis*: [AntennaIndepAxis](axes.md#keysight.ads.dds.AntennaIndepAxis "keysight.ads.dds.core.ddplot.AntennaIndepAxis")*[](#keysight.ads.dds.AntennaPlot.indep_axis "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.AntennaPlot.is_deactivated "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.AntennaPlot.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.AntennaPlot.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.AntennaPlot.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.AntennaPlot.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.AntennaPlot.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.AntennaPlot.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.AntennaPlot.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    *property* title*: str | None*[](#keysight.ads.dds.AntennaPlot.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.AntennaPlot.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.AntennaPlot.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.AntennaPlot.type "Link to this definition")

*class* keysight.ads.dds.Listing[](#keysight.ads.dds.Listing "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_list()`](page.md#keysight.ads.dds.Page.add_list "keysight.ads.dds.Page.add_list").

    activate() → None[](#keysight.ads.dds.Listing.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.Listing.add_legend "Link to this definition")

    add\_trace(*expression: str*) → [TextTrace](trace.md#keysight.ads.dds.TextTrace "keysight.ads.dds.core.ddplot.TextTrace")[](#keysight.ads.dds.Listing.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[TextTrace](trace.md#keysight.ads.dds.TextTrace "keysight.ads.dds.core.ddplot.TextTrace")][](#keysight.ads.dds.Listing.add_traces "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Listing.bbox "Link to this definition")
    :   The bounding box associated with an object.

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Listing.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.Listing.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Listing.children_bbox "Link to this definition")

    deactivate() → None[](#keysight.ads.dds.Listing.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.Listing.delete_object "Link to this definition")

    *property* is\_autosized*: bool*[](#keysight.ads.dds.Listing.is_autosized "Link to this definition")

    *property* is\_column\_headings\_displayed*: bool*[](#keysight.ads.dds.Listing.is_column_headings_displayed "Link to this definition")

    *property* is\_data\_transposed*: bool*[](#keysight.ads.dds.Listing.is_data_transposed "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.Listing.is_deactivated "Link to this definition")

    *property* is\_indep\_data\_displayed*: bool*[](#keysight.ads.dds.Listing.is_indep_data_displayed "Link to this definition")

    *property* is\_outlined*: bool*[](#keysight.ads.dds.Listing.is_outlined "Link to this definition")

    *property* is\_table\_format\_suppressed*: bool*[](#keysight.ads.dds.Listing.is_table_format_suppressed "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Listing.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Listing.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Listing.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Listing.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Listing.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Listing.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Listing.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.Listing.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.Listing.string_format "Link to this definition")

    *property* text\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.Listing.text_properties "Link to this definition")

    *property* title*: str | None*[](#keysight.ads.dds.Listing.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.Listing.title_properties "Link to this definition")

    *property* traces*: list[[TextTrace](trace.md#keysight.ads.dds.TextTrace "keysight.ads.dds.core.ddplot.TextTrace")]*[](#keysight.ads.dds.Listing.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Listing.type "Link to this definition")

*class* keysight.ads.dds.PolarPlot[](#keysight.ads.dds.PolarPlot "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_polar_plot()`](page.md#keysight.ads.dds.Page.add_polar_plot "keysight.ads.dds.Page.add_polar_plot").

    activate() → None[](#keysight.ads.dds.PolarPlot.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.PolarPlot.add_legend "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.PolarPlot.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.PolarPlot.add_traces "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.PolarPlot.bbox "Link to this definition")
    :   The bounding box associated with an object.

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.PolarPlot.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.PolarPlot.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.PolarPlot.children_bbox "Link to this definition")

    deactivate() → None[](#keysight.ads.dds.PolarPlot.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.PolarPlot.delete_object "Link to this definition")

    *property* dep\_axis*: [PolarDepAxis](axes.md#keysight.ads.dds.PolarDepAxis "keysight.ads.dds.core.ddplot.PolarDepAxis")*[](#keysight.ads.dds.PolarPlot.dep_axis "Link to this definition")

    *property* indep\_axis*: [PolarIndepAxis](axes.md#keysight.ads.dds.PolarIndepAxis "keysight.ads.dds.core.ddplot.PolarIndepAxis")*[](#keysight.ads.dds.PolarPlot.indep_axis "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.PolarPlot.is_deactivated "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.PolarPlot.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.PolarPlot.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.PolarPlot.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.PolarPlot.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.PolarPlot.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.PolarPlot.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.PolarPlot.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    *property* title*: str | None*[](#keysight.ads.dds.PolarPlot.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.PolarPlot.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.PolarPlot.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.PolarPlot.type "Link to this definition")

*class* keysight.ads.dds.RectPlot[](#keysight.ads.dds.RectPlot "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_plot()`](page.md#keysight.ads.dds.Page.add_plot "keysight.ads.dds.Page.add_plot").

    activate() → None[](#keysight.ads.dds.RectPlot.activate "Link to this definition")

    add\_greater\_than\_limit\_line(*name: str*, *x1: float | str*, *x2: float | str*, *y: float | str*) → [LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.core.ddplot.LimitLine")[](#keysight.ads.dds.RectPlot.add_greater_than_limit_line "Link to this definition")

    add\_inside\_limit\_line(*name: str*, *x1: float | str | None = None*, *y1: float | str | None = None*, *x2: float | str | None = None*, *y2: float | str | None = None*, *pt1: tuple[float | str, float | str] | None = None*, *pt2: tuple[float | str, float | str] | None = None*) → [LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.core.ddplot.LimitLine")[](#keysight.ads.dds.RectPlot.add_inside_limit_line "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.RectPlot.add_legend "Link to this definition")

    add\_less\_than\_limit\_line(*name: str*, *x1: float | str*, *x2: float | str*, *y: float | str*) → [LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.core.ddplot.LimitLine")[](#keysight.ads.dds.RectPlot.add_less_than_limit_line "Link to this definition")

    add\_line\_marker(*name: str*, *independent\_value: str | float*) → [LineMarker](linemarker.md#keysight.ads.dds.LineMarker "keysight.ads.dds.core.ddplot.LineMarker")[](#keysight.ads.dds.RectPlot.add_line_marker "Link to this definition")

    add\_line\_mask(*name: str*, *pt1: tuple[float | str, float | str]*, *pt2: tuple[float | str, float | str]*) → [LineMask](masks.md#keysight.ads.dds.LineMask "keysight.ads.dds.core.ddplot.LineMask")[](#keysight.ads.dds.RectPlot.add_line_mask "Link to this definition")

    add\_outside\_limit\_line(*name: str*, *x1: float | str | None = None*, *y1: float | str | None = None*, *x2: float | str | None = None*, *y2: float | str | None = None*, *pt1: tuple[float | str, float | str] | None = None*, *pt2: tuple[float | str, float | str] | None = None*) → [LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.core.ddplot.LimitLine")[](#keysight.ads.dds.RectPlot.add_outside_limit_line "Link to this definition")

    add\_polygon\_mask(*name: str*, *points: list[tuple[float | str, float | str]]*) → [PolygonMask](masks.md#keysight.ads.dds.PolygonMask "keysight.ads.dds.core.ddplot.PolygonMask")[](#keysight.ads.dds.RectPlot.add_polygon_mask "Link to this definition")

    add\_polyline\_mask(*name: str*, *points: list[tuple[float | str, float | str]]*) → [PolylineMask](masks.md#keysight.ads.dds.PolylineMask "keysight.ads.dds.core.ddplot.PolylineMask")[](#keysight.ads.dds.RectPlot.add_polyline_mask "Link to this definition")

    add\_rectangle\_mask(*name: str*, *x1: float | str | None = None*, *y1: float | str | None = None*, *x2: float | str | None = None*, *y2: float | str | None = None*, *pt1: tuple[float | str, float | str] | None = None*, *pt2: tuple[float | str, float | str] | None = None*) → [RectMask](masks.md#keysight.ads.dds.RectMask "keysight.ads.dds.core.ddplot.RectMask")[](#keysight.ads.dds.RectPlot.add_rectangle_mask "Link to this definition")

    add\_specification(*name: str*, *objs: list[PlotGraphicalObject]*) → [Specification](specifications.md#keysight.ads.dds.Specification "keysight.ads.dds.core.ddplot.Specification")[](#keysight.ads.dds.RectPlot.add_specification "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.RectPlot.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.RectPlot.add_traces "Link to this definition")

    *property* axes*: NamedItemCollectionAbc[[RectAxis](axes.md#keysight.ads.dds.RectAxis "keysight.ads.dds.core.ddplot.RectAxis")]*[](#keysight.ads.dds.RectPlot.axes "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.RectPlot.bbox "Link to this definition")
    :   The bounding box associated with an object.

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.RectPlot.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.RectPlot.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.RectPlot.children_bbox "Link to this definition")

    deactivate() → None[](#keysight.ads.dds.RectPlot.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.RectPlot.delete_object "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.RectPlot.is_deactivated "Link to this definition")

    *property* limit\_lines*: list[[LimitLine](limitlines.md#keysight.ads.dds.LimitLine "keysight.ads.dds.core.ddplot.LimitLine")]*[](#keysight.ads.dds.RectPlot.limit_lines "Link to this definition")

    *property* line\_markers*: NamedItemCollectionAbc[[LineMarker](linemarker.md#keysight.ads.dds.LineMarker "keysight.ads.dds.core.ddplot.LineMarker")]*[](#keysight.ads.dds.RectPlot.line_markers "Link to this definition")

    *property* masks*: list[Mask]*[](#keysight.ads.dds.RectPlot.masks "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.RectPlot.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.RectPlot.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.RectPlot.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.RectPlot.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.RectPlot.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.RectPlot.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.RectPlot.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    remove\_specification(*spec: [Specification](specifications.md#keysight.ads.dds.Specification "keysight.ads.dds.core.ddplot.Specification")*) → None[](#keysight.ads.dds.RectPlot.remove_specification "Link to this definition")

    *property* specifications*: NamedItemCollectionAbc[[Specification](specifications.md#keysight.ads.dds.Specification "keysight.ads.dds.core.ddplot.Specification")]*[](#keysight.ads.dds.RectPlot.specifications "Link to this definition")

    *property* title*: str | None*[](#keysight.ads.dds.RectPlot.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.RectPlot.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.RectPlot.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.RectPlot.type "Link to this definition")

*class* keysight.ads.dds.Slider[](#keysight.ads.dds.Slider "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_slider()`](page.md#keysight.ads.dds.Page.add_slider "keysight.ads.dds.Page.add_slider").

    activate() → None[](#keysight.ads.dds.Slider.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.Slider.add_legend "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.Slider.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.Slider.add_traces "Link to this definition")

    *property* axes*: NamedItemCollectionAbc[[RectAxis](axes.md#keysight.ads.dds.RectAxis "keysight.ads.dds.core.ddplot.RectAxis")]*[](#keysight.ads.dds.Slider.axes "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Slider.bbox "Link to this definition")
    :   The bounding box associated with an object.

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.Slider.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.Slider.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Slider.children_bbox "Link to this definition")

    deactivate() → None[](#keysight.ads.dds.Slider.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.Slider.delete_object "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.Slider.is_deactivated "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Slider.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Slider.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Slider.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Slider.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Slider.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Slider.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.Slider.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    *property* title*: str | None*[](#keysight.ads.dds.Slider.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.Slider.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.Slider.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Slider.type "Link to this definition")

*class* keysight.ads.dds.SmithChart[](#keysight.ads.dds.SmithChart "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_smith_chart()`](page.md#keysight.ads.dds.Page.add_smith_chart "keysight.ads.dds.Page.add_smith_chart").

    activate() → None[](#keysight.ads.dds.SmithChart.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.SmithChart.add_legend "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.SmithChart.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.SmithChart.add_traces "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.SmithChart.bbox "Link to this definition")
    :   The bounding box associated with an object.

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.SmithChart.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.SmithChart.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.SmithChart.children_bbox "Link to this definition")

    deactivate() → None[](#keysight.ads.dds.SmithChart.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.SmithChart.delete_object "Link to this definition")

    *property* dep\_axis*: [SmithChartDepAxis](axes.md#keysight.ads.dds.SmithChartDepAxis "keysight.ads.dds.core.ddplot.SmithChartDepAxis")*[](#keysight.ads.dds.SmithChart.dep_axis "Link to this definition")

    *property* indep\_axis*: [SmithChartIndepAxis](axes.md#keysight.ads.dds.SmithChartIndepAxis "keysight.ads.dds.core.ddplot.SmithChartIndepAxis")*[](#keysight.ads.dds.SmithChart.indep_axis "Link to this definition")

    *property* is\_admittance\_displayed*: bool*[](#keysight.ads.dds.SmithChart.is_admittance_displayed "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.SmithChart.is_deactivated "Link to this definition")

    *property* is\_impedance\_displayed*: bool*[](#keysight.ads.dds.SmithChart.is_impedance_displayed "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.SmithChart.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.SmithChart.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.SmithChart.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.SmithChart.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.SmithChart.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.SmithChart.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.SmithChart.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    *property* title*: str | None*[](#keysight.ads.dds.SmithChart.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.SmithChart.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.SmithChart.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.SmithChart.type "Link to this definition")

*class* keysight.ads.dds.StackedPlot[](#keysight.ads.dds.StackedPlot "Link to this definition")
:   This class cannot be instantiated directly. See [`Page.add_stacked_plot()`](page.md#keysight.ads.dds.Page.add_stacked_plot "keysight.ads.dds.Page.add_stacked_plot").

    activate() → None[](#keysight.ads.dds.StackedPlot.activate "Link to this definition")

    add\_legend() → [Legend](legend.md#keysight.ads.dds.Legend "keysight.ads.dds.core.ddplot.Legend")[](#keysight.ads.dds.StackedPlot.add_legend "Link to this definition")

    add\_line\_marker(*name: str*, *independent\_value: str*) → [LineMarker](linemarker.md#keysight.ads.dds.LineMarker "keysight.ads.dds.core.ddplot.LineMarker")[](#keysight.ads.dds.StackedPlot.add_line_marker "Link to this definition")

    add\_trace(*expression: str*) → [Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")[](#keysight.ads.dds.StackedPlot.add_trace "Link to this definition")

    add\_traces(*expressions: list[str]*) → list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")][](#keysight.ads.dds.StackedPlot.add_traces "Link to this definition")

    *property* axes*: list[[RectAxis](axes.md#keysight.ads.dds.RectAxis "keysight.ads.dds.core.ddplot.RectAxis")]*[](#keysight.ads.dds.StackedPlot.axes "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.StackedPlot.bbox "Link to this definition")
    :   The bounding box associated with an object.

    change\_object\_order(*objs: list[GraphicalObject]*) → None[](#keysight.ads.dds.StackedPlot.change_object_order "Link to this definition")
    :   Change the order of the objects that have been added to the plot.

    change\_trace\_order(*objs: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*) → None[](#keysight.ads.dds.StackedPlot.change_trace_order "Link to this definition")
    :   Change the order that the traces in a plot are referenced and displayed.

        Traces that exist on the plot but are not included in the
        list of traces to be reorderd will be place before the
        traces being reordered. Traces that are not referenced in
        the plot are ignored.

        Example

        Build a plot with a two trace and change the order that
        they will be displayed

        ```
        >>> import keysight.ads.dds as dds
        >>>
        >>> dds_file = dds.new_dds_file()
        >>> page = dds_file.pages[0]
        >>>
        >>> plot = page.add_plot();
        >>>
        >>> trace1 = plot.add_trace("[0::10]")
        >>> trace2 = plot.add_trace("[10::20]")
        >>>
        >>> plot.traces
        [<Trace "[0::10}>, <Trace "[10::20}>]
        >>>
        >>> plot.change_trace_order([trace2, trace1])
        >>>
        >>> page.traces
        [ <Trace "[10::20}>, <Trace "[0::10}>]
        ```

    *property* children\_bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.StackedPlot.children_bbox "Link to this definition")

    deactivate() → None[](#keysight.ads.dds.StackedPlot.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.StackedPlot.delete_object "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.StackedPlot.is_deactivated "Link to this definition")

    *property* line\_markers*: NamedItemCollectionAbc[[LineMarker](linemarker.md#keysight.ads.dds.LineMarker "keysight.ads.dds.core.ddplot.LineMarker")]*[](#keysight.ads.dds.StackedPlot.line_markers "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.StackedPlot.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.StackedPlot.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.StackedPlot.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.StackedPlot.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.StackedPlot.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.StackedPlot.name "Link to this definition")

    *property* objects*: list[GraphicalObject]*[](#keysight.ads.dds.StackedPlot.objects "Link to this definition")
    :   Returns a list of objects that have been added to the plot.

    *property* title*: str | None*[](#keysight.ads.dds.StackedPlot.title "Link to this definition")

    *property* title\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.StackedPlot.title_properties "Link to this definition")

    *property* traces*: list[[Trace](trace.md#keysight.ads.dds.Trace "keysight.ads.dds.core.ddplot.Trace")]*[](#keysight.ads.dds.StackedPlot.traces "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.StackedPlot.type "Link to this definition")


---

<!-- === 来源: reference/dds/point.md === -->

# Point[](#point "Link to this heading")

*class* keysight.ads.dds.Point[](#keysight.ads.dds.Point "Link to this definition")
:   An (x,y) coordinate grid point.

    Parameters:
    :   * **x** (*int*) – X-coordinate
        * **y** (*int*) – Y-coordinate

    Example

    Create a Point.

    ```
    >>> from keysight.ads import dds
    >>> snap_pt == dds.Point(100, 50)
    >>> print(snap_pt)
        Point(x=100, y=50)
    ```

    astuple() → tuple[int, int][](#keysight.ads.dds.Point.astuple "Link to this definition")
    :   Convert a Point to a tuple.

        Returns:
        :   returns a tuple containing the x,y values of Point

        Return type:
        :   tuple[int, int]

        Example

        Convert a Point to a tuple.

        ```
        >>> from keysight.ads import dds
        >>> snap_pt == dds.Point(100, 50)
        >>> print(snap_pt)
            Point(x=100, y=50)
        >>> print(snap_pt.astuple())
            (100,50)
        ```

    x*: int* *= 0*[](#keysight.ads.dds.Point.x "Link to this definition")
    :   The x-coordinate.

        Example

        Modify a Point.

        ```
        >>> from keysight.ads import dds
        >>> snap_pt == dds.Point(100, 50)
        >>> print(snap_pt)
            Point(x=100, y=50)
        >>> snap_pt.x = 200
        >>> print(snap_pt)
            Point(x=200, y=50)
        ```

    y*: int* *= 0*[](#keysight.ads.dds.Point.y "Link to this definition")
    :   The y-coordinate.

        Example

        Modify a Point.

        ```
        >>> from keysight.ads import dds
        >>> snap_pt == dds.Point(100, 50)
        >>> print(snap_pt)
            Point(x=100, y=50)
        >>> snap_pt.y = 200
        >>> print(snap_pt)
            Point(x=200, y=200)
        ```


---

<!-- === 来源: reference/dds/print.md === -->

# Print[](#print "Link to this heading")

*class* keysight.ads.dds.PaperSize[](#keysight.ads.dds.PaperSize "Link to this definition")
:   An enumerated type to describe printer paper sizes.

    Printing is provided in class [`DDSFile`](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile").

    A0 *= <PaperSize.A0: 5>*[](#keysight.ads.dds.PaperSize.A0 "Link to this definition")

    A1 *= <PaperSize.A1: 6>*[](#keysight.ads.dds.PaperSize.A1 "Link to this definition")

    A2 *= <PaperSize.A2: 7>*[](#keysight.ads.dds.PaperSize.A2 "Link to this definition")

    A3 *= <PaperSize.A3: 8>*[](#keysight.ads.dds.PaperSize.A3 "Link to this definition")

    A4 *= <PaperSize.A4: 0>*[](#keysight.ads.dds.PaperSize.A4 "Link to this definition")

    A5 *= <PaperSize.A5: 9>*[](#keysight.ads.dds.PaperSize.A5 "Link to this definition")

    A6 *= <PaperSize.A6: 10>*[](#keysight.ads.dds.PaperSize.A6 "Link to this definition")

    A7 *= <PaperSize.A7: 11>*[](#keysight.ads.dds.PaperSize.A7 "Link to this definition")

    A8 *= <PaperSize.A8: 12>*[](#keysight.ads.dds.PaperSize.A8 "Link to this definition")

    A9 *= <PaperSize.A9: 13>*[](#keysight.ads.dds.PaperSize.A9 "Link to this definition")

    B0 *= <PaperSize.B0: 14>*[](#keysight.ads.dds.PaperSize.B0 "Link to this definition")

    B1 *= <PaperSize.B1: 15>*[](#keysight.ads.dds.PaperSize.B1 "Link to this definition")

    B10 *= <PaperSize.B10: 16>*[](#keysight.ads.dds.PaperSize.B10 "Link to this definition")

    B2 *= <PaperSize.B2: 17>*[](#keysight.ads.dds.PaperSize.B2 "Link to this definition")

    B3 *= <PaperSize.B3: 18>*[](#keysight.ads.dds.PaperSize.B3 "Link to this definition")

    B4 *= <PaperSize.B4: 19>*[](#keysight.ads.dds.PaperSize.B4 "Link to this definition")

    B5 *= <PaperSize.B5: 1>*[](#keysight.ads.dds.PaperSize.B5 "Link to this definition")

    B6 *= <PaperSize.B6: 20>*[](#keysight.ads.dds.PaperSize.B6 "Link to this definition")

    B7 *= <PaperSize.B7: 21>*[](#keysight.ads.dds.PaperSize.B7 "Link to this definition")

    B8 *= <PaperSize.B8: 22>*[](#keysight.ads.dds.PaperSize.B8 "Link to this definition")

    B9 *= <PaperSize.B9: 23>*[](#keysight.ads.dds.PaperSize.B9 "Link to this definition")

    C5E *= <PaperSize.C5E: 24>*[](#keysight.ads.dds.PaperSize.C5E "Link to this definition")

    COMM10E *= <PaperSize.Comm10E: 25>*[](#keysight.ads.dds.PaperSize.COMM10E "Link to this definition")

    DLE *= <PaperSize.DLE: 26>*[](#keysight.ads.dds.PaperSize.DLE "Link to this definition")

    EXECUTIVE *= <PaperSize.Executive: 4>*[](#keysight.ads.dds.PaperSize.EXECUTIVE "Link to this definition")

    FOLIO *= <PaperSize.Folio: 27>*[](#keysight.ads.dds.PaperSize.FOLIO "Link to this definition")

    LEDGER *= <PaperSize.Ledger: 28>*[](#keysight.ads.dds.PaperSize.LEDGER "Link to this definition")

    LEGAL *= <PaperSize.Legal: 3>*[](#keysight.ads.dds.PaperSize.LEGAL "Link to this definition")

    LETTER *= <PaperSize.Letter: 2>*[](#keysight.ads.dds.PaperSize.LETTER "Link to this definition")

    TABLOID *= <PaperSize.Tabloid: 29>*[](#keysight.ads.dds.PaperSize.TABLOID "Link to this definition")

    *property* str*: str*[](#keysight.ads.dds.PaperSize.str "Link to this definition")

*class* keysight.ads.dds.PrinterOrientation[](#keysight.ads.dds.PrinterOrientation "Link to this definition")
:   An enumerated type to describe printer orientation.

    Printing is provided in class [`DDSFile`](file.md#keysight.ads.dds.DDSFile "keysight.ads.dds.DDSFile").

    LANDSCAPE *= <PrinterOrientation.Landscape: 1>*[](#keysight.ads.dds.PrinterOrientation.LANDSCAPE "Link to this definition")
    :   This value will print image horizontally on paper.

    PORTRAIT *= <PrinterOrientation.Portrait: 0>*[](#keysight.ads.dds.PrinterOrientation.PORTRAIT "Link to this definition")
    :   This value will print image vertically on paper.

    *property* str*: str*[](#keysight.ads.dds.PrinterOrientation.str "Link to this definition")


---

<!-- === 来源: reference/dds/pyequation.md === -->

# PyEquation[](#pyequation "Link to this heading")

*class* keysight.ads.dds.PyEquation[](#keysight.ads.dds.PyEquation "Link to this definition")
:   Python Equations execute python statements with dependency tracking between other equations.

    Some uses cases include defining functions, performing complex mathematical operations on data,
    importing modules, displaying widgets or windows and manipulating graphical objects.

    This class cannot be instantiated directly. See [`Page.add_py_equation()`](page.md#keysight.ads.dds.Page.add_py_equation "keysight.ads.dds.Page.add_py_equation").

    activate() → None[](#keysight.ads.dds.PyEquation.activate "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.PyEquation.bbox "Link to this definition")
    :   The bounding box associated with an object.

    calculate() → None[](#keysight.ads.dds.PyEquation.calculate "Link to this definition")

    deactivate() → None[](#keysight.ads.dds.PyEquation.deactivate "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.PyEquation.delete_object "Link to this definition")

    *property* errors*: str*[](#keysight.ads.dds.PyEquation.errors "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.PyEquation.expression "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.PyEquation.fill_properties "Link to this definition")

    *property* is\_auto\_calculated*: bool*[](#keysight.ads.dds.PyEquation.is_auto_calculated "Link to this definition")

    *property* is\_deactivated*: bool*[](#keysight.ads.dds.PyEquation.is_deactivated "Link to this definition")

    *property* is\_outlined*: bool*[](#keysight.ads.dds.PyEquation.is_outlined "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.PyEquation.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.PyEquation.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.PyEquation.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.PyEquation.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.PyEquation.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.PyEquation.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.PyEquation.name "Link to this definition")

    *property* status*: str*[](#keysight.ads.dds.PyEquation.status "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.PyEquation.string_format "Link to this definition")

    *property* text\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.PyEquation.text_properties "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.PyEquation.type "Link to this definition")

    *property* values*: dict[str, Any]*[](#keysight.ads.dds.PyEquation.values "Link to this definition")
    :   A dictionary of the expression’s variable names and evaluated values.

        Examples

        Print the value of a variable in a python equation.

        ```
        >>> exp = page.add_py_equation(
        '''\
        x = 1
        y = x*2''')
        >>> exp.values['y']
        2
        ```


---

<!-- === 来源: reference/dds/pywidget.md === -->

# Widget[](#widget "Link to this heading")

*class* keysight.ads.dds.Widget[](#keysight.ads.dds.Widget "Link to this definition")
:   A PySide2 widget wrapped into a Data Display graphical object.

    A PySide2 widget wrapped into a Data Display graphical object that can
    be placed on a Page, resized, and zoomed like any other graphical object.
    This class cannot be instantiated directly. See [`Page.add_widget()`](page.md#keysight.ads.dds.Page.add_widget "keysight.ads.dds.Page.add_widget").
    This class can only be used in application mode.

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Widget.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Widget.delete_object "Link to this definition")

    *property* is\_outlined*: bool*[](#keysight.ads.dds.Widget.is_outlined "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Widget.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Widget.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Widget.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Widget.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Widget.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Widget.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Widget.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Widget.type "Link to this definition")

    *property* widget*: QWidget*[](#keysight.ads.dds.Widget.widget "Link to this definition")


---

<!-- === 来源: reference/dds/rect.md === -->

# Rect[](#rect "Link to this heading")

*class* keysight.ads.dds.Rect[](#keysight.ads.dds.Rect "Link to this definition")
:   A simple rectangle defined by top, left, bottom, right values.

    The (top,left) values are always less than the (bottom,right) values.
    If they are specified otherwise, they will automatically be swapped. However, the
    dimensions of the rectangle will remain as specified.

    Parameters:
    :   * **top** (*int* *[**optional**,* *default=None**]*) – An integer that represents the y-coordinate of the top edge of the rectangle.
        * **left** (*int* *[**optional**,* *default=None**]*) – An integer that represents the x-coordinate of the left edge the rectangle
        * **bottom** (*int* *[**optional**,* *default=None**]*) – An integer that represents the y-coordinate of the bottom edge of the rectangle.
        * **right** (*int* *[**optional**,* *default=None**]*) – An integer that represents the x-coordinate of the right edge of the rectangle.
        * **top\_left** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]* *[**optional**,* *default=None**]*) – A Point or tuple[int,int] that contains x,y coordinates that represent the top-left corner of the rectangle.
        * **bottom\_right** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]* *[**optional**,* *default=None**]*) – A Point or tuple[int,int] that contains x,y coordinates that represent the bottom-right corner of the rectangle.
        * **width** (*int* *[**optional**,* *default=None**]*) – An integer that represents the width of the rectangle.
        * **height** (*int* *[**optional**,* *default=None**]*) – An integer that represents the height of the rectangle.

    Example

    Valid combinations of parameters to create a Rect.

    ```
    >>> from keysight.ads import dds
    >>> a = dds.Rect()
    >>> print(a)
        <Rect "top_left=(0,0), bottom_right=(0,0)">
    >>> b = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
    >>> print(b)
        <Rect "top_left=(0,0), bottom_right=(100,100)">
    >>> c = dds.Rect(top_left=dds.Point(50, 100), bottom_right=dds.Point(150, 200))
    >>> print(c)
        <Rect "top_left=(50,100), bottom_right=(150,200)">
    >>> d = dds.Rect(top_left=dds.Point(50,100), width = 500, height = 200)
    >>> print(d)
        <Rect "top_left=(50,100), bottom_right=(550,300)">
    >>> e = dds.Rect(top = 100, left = 50, width = 500, height = 200)
    >>> print(e)
            <Rect "top_left=(50,100), bottom_right=(550,300)">
    ```

    adjust(*\**, *left: int | None = None*, *top: int | None = None*, *right: int | None = None*, *bottom: int | None = None*) → None[](#keysight.ads.dds.Rect.adjust "Link to this definition")
    :   Modify the rectangle by adding parameters to the corresponding edge.

        Parameters:
        :   * **left** (*int* *[**optional**,* *default=None**]*) – An integer to add to “left” property
            * **top** (*int* *[**optional**,* *default=None**]*) – An integer to add to “top” property
            * **right** (*int* *[**optional**,* *default=None**]*) – An integer to add to “right” property
            * **bottom** (*int* *[**optional**,* *default=None**]*) – An integer to add to “bottom” property

        Return type:
        :   None

        Example

        Modify the rectangle to be narrower and taller.

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> r.adjust(right =-50, bottom = 100)
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(50,200)">
        ```

    adjusted(*\**, *left: int | None = None*, *top: int | None = None*, *right: int | None = None*, *bottom: int | None = None*) → [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")[](#keysight.ads.dds.Rect.adjusted "Link to this definition")
    :   Return a new Rect with coordinates determined by adding parameter(s) to the rectangle.

        The original Rect is not modified.

        Parameters:
        :   * **left** (*int* *[**optional**,* *default=None**]*) – An integer to add to “left” property
            * **top** (*int* *[**optional**,* *default=None**]*) – An integer to add to “top” property
            * **right** (*int* *[**optional**,* *default=None**]*) – An integer to add to “right” property
            * **bottom** (*int* *[**optional**,* *default=None**]*) – An integer to add to “bottom” property

        Returns:
        :   Create a new Rect with coordinates determined by adding the parameter(s) to the corresponding edge of the rectangle.

        Return type:
        :   [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")

        Example

        Create a new rect that is narrower and taller than self(Rect).

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> newRect = r.adjusted(right =-50, bottom = 100)
        >>> print(newRect)
            <Rect "top_left=(0,0), bottom_right=(50,200)">
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        ```

    *property* bottom*: int*[](#keysight.ads.dds.Rect.bottom "Link to this definition")
    :   An integer that represents the y-coordinate of the bottom edge of the rectangle.

    *property* bottom\_left*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Rect.bottom_left "Link to this definition")
    :   A Point that contains x,y coordinates that represent the bottom-left corner of the rectangle.

    *property* bottom\_right*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Rect.bottom_right "Link to this definition")
    :   A Point that contains x,y coordinates that represent the bottom-right corner of the rectangle.

    center() → [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")[](#keysight.ads.dds.Rect.center "Link to this definition")
    :   Return the center point of the rectangle.

        Returns:
        :   The center Point of the rectangle.

        Return type:
        :   [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point")

        Example

        Get the center point of the rectangle.

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> c = r.center()
        >>> print(c)
            Point(x=50, y=50)
        ```

    contains(*shape: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → bool[](#keysight.ads.dds.Rect.contains "Link to this definition")
    :   Return True if a shape is contained inside the rectangle.

        Parameters:
        :   **shape** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]* *|* [*Rect*](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – The shape to check is a point, tuple[int,int] or a rectangle.

        Returns:
        :   True if “shape” is completely contained inside the rectangle.
            Otherwise, returns False.

        Return type:
        :   bool

        Example

        Check if a Rect or a Point is contained in the rectangle.

        ```
        >>> from keysight.ads import dds
        >>> first = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> second = dds.Rect(top = 0, left = 0, bottom = 90, right = 90)
        >>> inside = first.contains(second)
        >>> print(inside)
            True
        >>> inside = first.contains(dds.Point(100, 200))
        >>> print(inside)
            False
        ```

    expand(*shape: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → None[](#keysight.ads.dds.Rect.expand "Link to this definition")
    :   Modify the rectangle by possibly expanding it to include a shape.

        Parameters:
        :   **shape** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]* *|* [*Rect*](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – The shape to include in the rectangle is a point, tuple[int,int] or another rectangle.

        Return type:
        :   None

        Example

        Expand the rectangle to include a Point and a Rect

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> r.expand(dds.Point(-50, 80))
        >>> print(r)
            <Rect "top_left=(-50,0), bottom_right=(100,100)">
        >>> r.expand(dds.Rect(top = -50, left = -40, bottom = 200, right = 150))
        >>> print(r)
            <Rect "top_left=(-50,-50), bottom_right=(150,200)">
        ```

    expanded(*shape: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int] | [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")[](#keysight.ads.dds.Rect.expanded "Link to this definition")
    :   Return a new Rect with coordinates determined by expanding the rectangle to include a shape.

        The original Rect is not modified.

        Parameters:
        :   **shape** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]* *|* [*Rect*](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – The shape to include in the rectangle is a point, tuple[int,int] or another rectangle.

        Returns:
        :   Create a new Rect with coordinates determined by expanding the rectangle to include “shape”.

        Return type:
        :   [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")

        Example

        Create a new Rect by expanding the rectangle to include a Point and a Rect.

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> one = r.expanded(dds.Point(-50, 80))
        >>> print(one)
            <Rect "top_left=(-50,0), bottom_right=(100,100)">
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        >>> two = r.expand(dds.Rect(top = -50, left = -40, bottom = 200, right = 150))
        >>> print(two)
            <Rect "top_left=(-50,-50), bottom_right=(150,200)">
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        ```

    *property* height*: int*[](#keysight.ads.dds.Rect.height "Link to this definition")
    :   An integer that represents the height of the rectangle.

    intersected(*rect: [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")[](#keysight.ads.dds.Rect.intersected "Link to this definition")
    :   Return a new rectangle that represents the intersection between 2 rectangles.

        The original Rect is not modified.

        Parameters:
        :   **rect** ([*Rect*](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – A rectangle used to calculate the intersection.

        Returns:
        :   Calculates the intersection between “rect” and the rectangle and creates a new Rect to represent the intersection.
            There are 10 cases of intersection: any of the 4 corners of “rect” are contained in the rectangle,
            any of the 4 sides of “rect” are contained in the rectangle, “rect” is totally contained in the rectangle,
            or “rect” equals the rectangle.

        Return type:
        :   [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")

        Example

        Get the intersection between 2 rectangles.

        ```
        >>> from keysight.ads import dds
        >>> first = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> second = dds.Rect(top = 10, left = 10, bottom = 110, right = 110)
        >>> intersection = first.intersects(second)
        >>> print(intersection)
            <Rect "top_left=(10,10), bottom_right=(100,100)">
        ```

    intersects(*rect: [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*) → bool[](#keysight.ads.dds.Rect.intersects "Link to this definition")
    :   Return True if 2 rectangles intersect.

        Parameters:
        :   **rect** ([*Rect*](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")) – A rectangle used to check for intersection.

        Returns:
        :   True if any point of “rect” is contained in the rectangle.
            Otherwise, returns False.

        Return type:
        :   bool

        Example

        Check if 2 rectangles intersect.

        ```
        >>> from keysight.ads import dds
        >>> first = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> second = dds.Rect(top = 10, left = 10, bottom = 110, right = 110)
        >>> inside = first.intersects(second)
        >>> print(inside)
            True
        ```

    *property* left*: int*[](#keysight.ads.dds.Rect.left "Link to this definition")
    :   An integer that represents the x-coordinate of the left edge of the rectangle.

    *property* right*: int*[](#keysight.ads.dds.Rect.right "Link to this definition")
    :   An integer that represents the y-coordinate of the right edge of the rectangle.

    *property* top*: int*[](#keysight.ads.dds.Rect.top "Link to this definition")
    :   An integer that represents the y-coordinate of the top edge of the rectangle.

    *property* top\_left*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Rect.top_left "Link to this definition")
    :   A Point that contains x,y coordinates that represent the top-left corner of the rectangle.

    *property* top\_right*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Rect.top_right "Link to this definition")
    :   A Point that contains x,y coordinates that represent the top-right corner of the rectangle.

    translate(*x\_offset: int*, *y\_offset: int*) → None[](#keysight.ads.dds.Rect.translate "Link to this definition")
    :   Modify the rectangle by adding offsets to its coordinates.

        Parameters:
        :   * **x\_offset** (*int*) – An integer to add to the x-coordinates
            * **y\_offset** (*int*) – An integer to add to the y-coordinates

        Return type:
        :   None

        Example

        Modify a rectangle to be wider and shorter.

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> r.translate(x_offset = 50, y_offset = -50)
        >>> print(r)
            <Rect "top_left=(50,-50), bottom_right=(150,50)">
        ```

    translated(*x\_offset: int*, *y\_offset: int*) → [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")[](#keysight.ads.dds.Rect.translated "Link to this definition")
    :   Return a new Rect with coordinates determined by adding offsets to the rectangle.

        The original Rect is not modified.

        Parameters:
        :   * **x\_offset** (*int*) – An integer to add to the x-coordinates
            * **y\_offset** (*int*) – An integer to add to the y-coordinates

        Returns:
        :   Creates a new Rect with coordinates determined by adding “x\_offset” and “y\_offset” to the x,y coordinates of the rectangle.

        Return type:
        :   [Rect](#keysight.ads.dds.Rect "keysight.ads.dds.Rect")

        Example

        Create a new Rect that is wider and shorter than the rectangle.

        ```
        >>> from keysight.ads import dds
        >>> r = dds.Rect(top = 0,left = 0, bottom = 100, right = 100)
        >>> newRect = r.translated(x_offset = 50, y_offset = -50)
        >>> print(newRect)
            <Rect "top_left=(50,-50), bottom_right=(150,50)">
        >>> print(r)
            <Rect "top_left=(0,0), bottom_right=(100,100)">
        ```

    *property* width*: int*[](#keysight.ads.dds.Rect.width "Link to this definition")
    :   An integer that represents the width of the rectangle.


---

<!-- === 来源: reference/dds/shapes.md === -->

# Shapes[](#shapes "Link to this heading")

*class* keysight.ads.dds.Box[](#keysight.ads.dds.Box "Link to this definition")
:   A simple box on a page.

    This class cannot be instantiated directly. See [`Page.add_box()`](page.md#keysight.ads.dds.Page.add_box "keysight.ads.dds.Page.add_box").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Box.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Box.delete_object "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.Box.fill_properties "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Box.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Box.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Box.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Box.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Box.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Box.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Box.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Box.type "Link to this definition")

*class* keysight.ads.dds.Circle[](#keysight.ads.dds.Circle "Link to this definition")
:   A simple circle on a page.

    This class cannot be instantiated directly. See [`Page.add_circle()`](page.md#keysight.ads.dds.Page.add_circle "keysight.ads.dds.Page.add_circle").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Circle.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* center*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Circle.center "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.Circle.delete_object "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.Circle.fill_properties "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Circle.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Circle.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Circle.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Circle.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Circle.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Circle.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Circle.name "Link to this definition")

    *property* radius*: int*[](#keysight.ads.dds.Circle.radius "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Circle.type "Link to this definition")

*class* keysight.ads.dds.Line[](#keysight.ads.dds.Line "Link to this definition")
:   A simple line on a page.

    This class cannot be instantiated directly. See [`Page.add_line()`](page.md#keysight.ads.dds.Page.add_line "keysight.ads.dds.Page.add_line").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Line.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Line.delete_object "Link to this definition")

    *property* end*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Line.end "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Line.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Line.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Line.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Line.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Line.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Line.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Line.name "Link to this definition")

    *property* start*: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")*[](#keysight.ads.dds.Line.start "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Line.type "Link to this definition")

*class* keysight.ads.dds.Polyline[](#keysight.ads.dds.Polyline "Link to this definition")
:   A simple polyline on a page.

    This class cannot be instantiated directly. See [`Page.add_polyline()`](page.md#keysight.ads.dds.Page.add_polyline "keysight.ads.dds.Page.add_polyline").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Polyline.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Polyline.delete_object "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Polyline.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Polyline.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Polyline.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Polyline.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Polyline.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Polyline.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Polyline.name "Link to this definition")

    *property* points*: list[[Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")]*[](#keysight.ads.dds.Polyline.points "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Polyline.type "Link to this definition")

*class* keysight.ads.dds.Polygon[](#keysight.ads.dds.Polygon "Link to this definition")
:   A simple polygon on a page.

    This class cannot be instantiated directly. See [`Page.add_polygon()`](page.md#keysight.ads.dds.Page.add_polygon "keysight.ads.dds.Page.add_polygon").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Polygon.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Polygon.delete_object "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.Polygon.fill_properties "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Polygon.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Polygon.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Polygon.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Polygon.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Polygon.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Polygon.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Polygon.name "Link to this definition")

    *property* points*: list[[Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point")]*[](#keysight.ads.dds.Polygon.points "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Polygon.type "Link to this definition")


---

<!-- === 来源: reference/dds/specifications.md === -->

# Specification[](#specification "Link to this heading")

*class* keysight.ads.dds.Specification[](#keysight.ads.dds.Specification "Link to this definition")
:   A group of limit lines and masks.

    This class cannot be instantiated directly.
    An instance is created by [`RectPlot.add_specification()`](plots.md#keysight.ads.dds.RectPlot.add_specification "keysight.ads.dds.RectPlot.add_specification").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Specification.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Specification.delete_object "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.Specification.expression "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Specification.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Specification.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Specification.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Specification.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Specification.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Specification.name "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Specification.type "Link to this definition")


---

<!-- === 来源: reference/dds/text.md === -->

# Text[](#text "Link to this heading")

*class* keysight.ads.dds.Text[](#keysight.ads.dds.Text "Link to this definition")
:   A group of characters on a page.

    This class cannot be instantiated directly. See [`Page.add_text()`](page.md#keysight.ads.dds.Page.add_text "keysight.ads.dds.Page.add_text").

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Text.bbox "Link to this definition")
    :   The bounding box associated with an object.

    delete\_object() → None[](#keysight.ads.dds.Text.delete_object "Link to this definition")

    *property* fill\_properties*: [FillProperties](basic.md#keysight.ads.dds.FillProperties "keysight.ads.dds.core.ddbase.FillProperties")*[](#keysight.ads.dds.Text.fill_properties "Link to this definition")

    *property* is\_outlined*: bool*[](#keysight.ads.dds.Text.is_outlined "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Text.line_properties "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Text.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Text.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Text.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Text.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Text.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Text.name "Link to this definition")

    *property* string*: str*[](#keysight.ads.dds.Text.string "Link to this definition")

    *property* string\_format*: [StringFormat](basic.md#keysight.ads.dds.StringFormat "keysight.ads.dds.core.ddbase.StringFormat")*[](#keysight.ads.dds.Text.string_format "Link to this definition")

    *property* text\_properties*: [TextProperties](basic.md#keysight.ads.dds.TextProperties "keysight.ads.dds.core.ddbase.TextProperties")*[](#keysight.ads.dds.Text.text_properties "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Text.type "Link to this definition")


---

<!-- === 来源: reference/dds/trace.md === -->

# Trace[](#trace "Link to this heading")

*class* keysight.ads.dds.Trace[](#keysight.ads.dds.Trace "Link to this definition")
:   Traces are used to display data on a plot.

    This class cannot be instantiated directly.
    An instance(s) is created by the methods add\_trace() and add\_traces() in a plot.

    add\_marker(*name: str*, *indep\_value\_or\_expr: float | str*, *type: [MarkerType](marker.md#keysight.ads.dds.MarkerType "keysight.ads.dds.core.ddplot.MarkerType") | str = MarkerType.NORMAL*) → [TraceMarker](marker.md#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker")[](#keysight.ads.dds.Trace.add_marker "Link to this definition")

    *property* autosequence\_settings*: AutoSequenceSettings*[](#keysight.ads.dds.Trace.autosequence_settings "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Trace.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* bus\_always\_display\_transition*: bool*[](#keysight.ads.dds.Trace.bus_always_display_transition "Link to this definition")

    *property* bus\_text\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.Trace.bus_text_color "Link to this definition")

    *property* color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.Trace.color "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.Trace.delete_object "Link to this definition")

    *property* density\_num\_colors*: int*[](#keysight.ads.dds.Trace.density_num_colors "Link to this definition")

    *property* density\_start\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.Trace.density_start_color "Link to this definition")

    *property* density\_symbol\_type*: DensitySymbolType*[](#keysight.ads.dds.Trace.density_symbol_type "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.Trace.dep_axis "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.Trace.expression "Link to this definition")

    *property* font*: str*[](#keysight.ads.dds.Trace.font "Link to this definition")

    *property* histogram\_enable\_fill*: bool*[](#keysight.ads.dds.Trace.histogram_enable_fill "Link to this definition")

    *property* histogram\_fill\_pattern*: str*[](#keysight.ads.dds.Trace.histogram_fill_pattern "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.Trace.indep_axis "Link to this definition")

    *property* label\_properties*: TraceLabelProperties*[](#keysight.ads.dds.Trace.label_properties "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.Trace.line_properties "Link to this definition")

    *property* line\_type*: [LineType](basic.md#keysight.ads.dds.LineType "keysight.ads.dds.core.ddbase.LineType")*[](#keysight.ads.dds.Trace.line_type "Link to this definition")

    *property* linear\_symbol\_spacing*: SymbolSpacing*[](#keysight.ads.dds.Trace.linear_symbol_spacing "Link to this definition")

    *property* markers*: NamedItemCollectionAbc[[TraceMarker](marker.md#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker")]*[](#keysight.ads.dds.Trace.markers "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.Trace.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.Trace.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.Trace.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.Trace.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.Trace.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.Trace.name "Link to this definition")

    *property* spectral\_display\_arrowheads*: bool*[](#keysight.ads.dds.Trace.spectral_display_arrowheads "Link to this definition")

    *property* string\_format\_option*: StringFormatOption*[](#keysight.ads.dds.Trace.string_format_option "Link to this definition")

    *property* symbol\_type*: SymbolType*[](#keysight.ads.dds.Trace.symbol_type "Link to this definition")

    *property* trace\_type*: TraceType*[](#keysight.ads.dds.Trace.trace_type "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.Trace.type "Link to this definition")

    *property* variable*: bool | int | float | complex | str | VariableBlock | None*[](#keysight.ads.dds.Trace.variable "Link to this definition")

    *property* width*: float*[](#keysight.ads.dds.Trace.width "Link to this definition")

*class* keysight.ads.dds.TextTrace[](#keysight.ads.dds.TextTrace "Link to this definition")
:   add\_marker(*name: str*, *indep\_value\_or\_expr: float | str*, *type: [MarkerType](marker.md#keysight.ads.dds.MarkerType "keysight.ads.dds.core.ddplot.MarkerType") | str = MarkerType.NORMAL*) → [TraceMarker](marker.md#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker")[](#keysight.ads.dds.TextTrace.add_marker "Link to this definition")

    *property* autosequence\_settings*: AutoSequenceSettings*[](#keysight.ads.dds.TextTrace.autosequence_settings "Link to this definition")

    *property* bbox*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.TextTrace.bbox "Link to this definition")
    :   The bounding box associated with an object.

    *property* bus\_always\_display\_transition*: bool*[](#keysight.ads.dds.TextTrace.bus_always_display_transition "Link to this definition")

    *property* bus\_text\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.TextTrace.bus_text_color "Link to this definition")

    *property* color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.TextTrace.color "Link to this definition")

    delete\_object() → None[](#keysight.ads.dds.TextTrace.delete_object "Link to this definition")

    *property* density\_num\_colors*: int*[](#keysight.ads.dds.TextTrace.density_num_colors "Link to this definition")

    *property* density\_start\_color*: [Color](basic.md#keysight.ads.dds.Color "keysight.ads.dds.core.ddbase.Color")*[](#keysight.ads.dds.TextTrace.density_start_color "Link to this definition")

    *property* density\_symbol\_type*: DensitySymbolType*[](#keysight.ads.dds.TextTrace.density_symbol_type "Link to this definition")

    *property* dep\_axis*: str*[](#keysight.ads.dds.TextTrace.dep_axis "Link to this definition")

    *property* expression*: str*[](#keysight.ads.dds.TextTrace.expression "Link to this definition")

    *property* font*: str*[](#keysight.ads.dds.TextTrace.font "Link to this definition")

    *property* histogram\_enable\_fill*: bool*[](#keysight.ads.dds.TextTrace.histogram_enable_fill "Link to this definition")

    *property* histogram\_fill\_pattern*: str*[](#keysight.ads.dds.TextTrace.histogram_fill_pattern "Link to this definition")

    *property* indep\_axis*: str*[](#keysight.ads.dds.TextTrace.indep_axis "Link to this definition")

    *property* label\_properties*: TraceLabelProperties*[](#keysight.ads.dds.TextTrace.label_properties "Link to this definition")

    *property* line\_properties*: [LineProperties](basic.md#keysight.ads.dds.LineProperties "keysight.ads.dds.core.ddbase.LineProperties")*[](#keysight.ads.dds.TextTrace.line_properties "Link to this definition")

    *property* line\_type*: [LineType](basic.md#keysight.ads.dds.LineType "keysight.ads.dds.core.ddbase.LineType")*[](#keysight.ads.dds.TextTrace.line_type "Link to this definition")

    *property* linear\_symbol\_spacing*: SymbolSpacing*[](#keysight.ads.dds.TextTrace.linear_symbol_spacing "Link to this definition")

    *property* markers*: NamedItemCollectionAbc[[TraceMarker](marker.md#keysight.ads.dds.TraceMarker "keysight.ads.dds.core.ddplot.TraceMarker")]*[](#keysight.ads.dds.TextTrace.markers "Link to this definition")

    move(*delta: [Point](point.md#keysight.ads.dds.Point "keysight.ads.dds.core.ddgeom.Point") | tuple[int, int]*) → None[](#keysight.ads.dds.TextTrace.move "Link to this definition")
    :   Move an object.

        Parameters:
        :   **delta** ([*Point*](point.md#keysight.ads.dds.Point "keysight.ads.dds.Point") *|* *tuple**[**int**,* *int**]*) – A point or a tuple[int,int] that represents a coordinate which will determine the relative move from the object’s current position.

        Return type:
        :   None

    move\_back() → None[](#keysight.ads.dds.TextTrace.move_back "Link to this definition")
    :   Move the object backward one location in the display order.

        Moves the object backward in the display order by one object.
        This allows the object to be displayed before adjacent objects
        in the display order.

    move\_forward() → None[](#keysight.ads.dds.TextTrace.move_forward "Link to this definition")
    :   Move the object forward one location in the display order.

        Moves the object forward in the display order by one object.
        This allows the object to be displayed after adjacent objects
        in the display order.

    move\_to\_back() → None[](#keysight.ads.dds.TextTrace.move_to_back "Link to this definition")
    :   Move the object to be displayed behind all other objects.

        Moves the object to the beginning of the display order so that
        it is display first.

    move\_to\_front() → None[](#keysight.ads.dds.TextTrace.move_to_front "Link to this definition")
    :   Move the object to be displayed in front of all other objects.

        Moves the object to the end of the display order so that it is
        displayed last.

    *property* name*: str*[](#keysight.ads.dds.TextTrace.name "Link to this definition")

    *property* spectral\_display\_arrowheads*: bool*[](#keysight.ads.dds.TextTrace.spectral_display_arrowheads "Link to this definition")

    *property* string\_format\_option*: StringFormatOption*[](#keysight.ads.dds.TextTrace.string_format_option "Link to this definition")

    *property* symbol\_type*: SymbolType*[](#keysight.ads.dds.TextTrace.symbol_type "Link to this definition")

    *property* trace\_type*: TraceType*[](#keysight.ads.dds.TextTrace.trace_type "Link to this definition")

    *property* type*: ObjectType*[](#keysight.ads.dds.TextTrace.type "Link to this definition")

    *property* variable*: bool | int | float | complex | str | VariableBlock | None*[](#keysight.ads.dds.TextTrace.variable "Link to this definition")

    *property* width*: float*[](#keysight.ads.dds.TextTrace.width "Link to this definition")


---

<!-- === 来源: reference/dds/windows.md === -->

# Window[](#window "Link to this heading")

*class* keysight.ads.dds.Window[](#keysight.ads.dds.Window "Link to this definition")
:   A Window is a view of a Page.

    This class cannot be instantiated directly. When a Data Display file is created, a page and
    a window are automatically created. Additional windows can be created with [`DDSFile.new_window()`](file.md#keysight.ads.dds.DDSFile.new_window "keysight.ads.dds.DDSFile.new_window").
    Pages can be access by the property [`DDSFile.windows`](file.md#keysight.ads.dds.DDSFile.windows "keysight.ads.dds.DDSFile.windows").

    *property* current\_page*: [Page](page.md#keysight.ads.dds.Page "keysight.ads.dds.core.ddpage.Page")*[](#keysight.ads.dds.Window.current_page "Link to this definition")

    *property* name*: str*[](#keysight.ads.dds.Window.name "Link to this definition")

    *property* page*: str*[](#keysight.ads.dds.Window.page "Link to this definition")
    :   current\_page

        Type:
        :   page is deprecated, and will be removed in the 2026 Update 1 release. Use

    *property* type*: ObjectType*[](#keysight.ads.dds.Window.type "Link to this definition")

    *property* view\_rect*: [Rect](rect.md#keysight.ads.dds.Rect "keysight.ads.dds.core.ddgeom.Rect")*[](#keysight.ads.dds.Window.view_rect "Link to this definition")

    zoom\_all() → None[](#keysight.ads.dds.Window.zoom_all "Link to this definition")


---

<!-- === 来源: reference/index.md === -->

# Reference[](#reference "Link to this heading")

* [keysight.ads.dds](dds/index.md)
  + [Classes](dds/index.md#classes)
    - [DDSFile](dds/file.md)
    - [Page](dds/page.md)
    - [Point](dds/point.md)
    - [Rect](dds/rect.md)
    - [Grid](dds/grid.md)
    - [Plots](dds/plots.md)
    - [Axes](dds/axes.md)
    - [Legend](dds/legend.md)
    - [Trace](dds/trace.md)
    - [Markers](dds/marker.md)
    - [Line Markers](dds/linemarker.md)
    - [Limit Lines](dds/limitlines.md)
    - [Masks](dds/masks.md)
    - [Specification](dds/specifications.md)
    - [Equation](dds/equation.md)
    - [PyEquation](dds/pyequation.md)
    - [Text](dds/text.md)
    - [Picture](dds/picture.md)
    - [Shapes](dds/shapes.md)
    - [Group](dds/group.md)
    - [Common Properties](dds/basic.md)
    - [Print](dds/print.md)
    - [Object](dds/objects.md)
    - [Window](dds/windows.md)
    - [Widget](dds/pywidget.md)
  + [Functions](dds/index.md#functions)
    - [`get_dds_path()`](dds/index.md#keysight.ads.dds.get_dds_path)
    - [`init_dds_path()`](dds/index.md#keysight.ads.dds.init_dds_path)
    - [`running_automation()`](dds/index.md#keysight.ads.dds.running_automation)
    - [`version()`](dds/index.md#keysight.ads.dds.version)
    - [`product_version()`](dds/index.md#keysight.ads.dds.product_version)
    - [`close_dds_file()`](dds/index.md#keysight.ads.dds.close_dds_file)
    - [`get_dds_files()`](dds/index.md#keysight.ads.dds.get_dds_files)
    - [`new_dds_file()`](dds/index.md#keysight.ads.dds.new_dds_file)
    - [`open_dds_file()`](dds/index.md#keysight.ads.dds.open_dds_file)
* [keysight.ads.dds.experimental](dds/experimental/index.md)
  + [Classes](dds/experimental/index.md#classes)
  + [Functions](dds/experimental/index.md#functions)
* [keysight.ads.dds.app](dds/app/index.md)
  + [Classes](dds/app/index.md#classes)
    - [Addon](dds/app/addon.md)
    - [Callbacks](dds/app/callbacks.md)
  + [Functions](dds/app/index.md#functions)
    - [`get_pyside2_main_window()`](dds/app/index.md#keysight.ads.dds.app.get_pyside2_main_window)
    - [`is_alt_pressed()`](dds/app/index.md#keysight.ads.dds.app.is_alt_pressed)
    - [`is_control_pressed()`](dds/app/index.md#keysight.ads.dds.app.is_control_pressed)
    - [`is_shift_pressed()`](dds/app/index.md#keysight.ads.dds.app.is_shift_pressed)

**Indices**

* [Index](../genindex.md)
* [Module Index](../py-modindex.md)


---

