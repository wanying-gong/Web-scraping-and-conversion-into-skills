# Concepts
> **说明：** Concepts 相关页面。

> **何时使用：** 当你需要查阅 Concepts 相关内容时

---

## 本文件目录

- **Python Script Execution** (`concepts/execution.md`)
- **Concepts** (`concepts/index.md`)

---

<!-- === 来源: concepts/execution.md === -->

# Python Script Execution[](#python-script-execution "Link to this heading")

When developing Python scripts for DDS (or ADS\*), it is important to consider the execution context the script runs in,
as the set of available functionality differs depending on whether or not the script executes within the context
of the application.

When executing scripts from within the DDS application, whether from the Python console, or menu action, etc.,
application level functionality is available, you can display a message box or access a window, for example.
Scripts executing outside the application context do not have access to ADS application functionality, such as user interface
and interprocess communication. This includes, but is not limited to, the [`keysight.ads.dds.app`](../reference/dds/app/index.md#module-keysight.ads.dds.app "keysight.ads.dds.app") package and AEL application
functions that interact with the user interface or access the simulator in some manner. Simulation in automation mode can make
use of the `keysight.edatoolbox` package, which is beyond the scope of this document.

To determine if the executing context is the DDS application, the script can check `keysight.ads.dds.is_dds_app()`.

*\*Note: DDS is the Data Display application, which is a separate application that can be launched from the command line or
from within ADS. Both ADS and DDS have their own embedded Python interpreter and are separate execution contexts.*

## Automation[](#automation "Link to this heading")

‘Automation’ is a term used to describe when the execution context of an extension module is not the owning application.
Importing the `keysight.ads.de` or [`keysight.ads.dds`](../reference/dds/index.md#module-keysight.ads.dds "keysight.ads.dds") packages directly into a Python process is considered
ADS or DDS automation, respectively. Additionally, importing the [`keysight.ads.dds`](../reference/dds/index.md#module-keysight.ads.dds "keysight.ads.dds") package from within the
ADS application is considered DDS automation, just as importing `keysight.ads.de` from within the DDS application
is considered ADS automation.

When running in an automation mode (ADS, DDS, or both), scripts are not able to access the associated application’s user
interface. For example, when running scripts inside ADS, the DDS user interface APIs are not available, and vice versa.
Examples of UI functionality include, but are not limited to: windows, message boxes, palettes, menus, and toolbars.

To determine if a particular execution context is automation, the script can check the return value of the appropriate
`is_app` function, for ADS, this is `keysight.ads.de.is_pde_app()`, and for DDS, this is `keysight.ads.dds.is_dds_app()`.

*Note: The* `keysight.ads.de.running_automation()` *and* [`keysight.ads.dds.running_automation()`](../reference/dds/index.md#keysight.ads.dds.running_automation "keysight.ads.dds.running_automation") *functions are misnamed and
those names will be deprecated in a future release. Both functions mean the same thing, that the script is not executing in
either the ADS or DDS application context, but a Python application context.*

The following examples demonstrate the different results of the `is_pde_app`, `is_dds_app`, and `running_automation`
functions when executed from different contexts:

From within the DDS application:

![../_images/DDS_app_automation_modes.png](../_images/DDS_app_automation_modes.png)

From within the ADS application:

![../_images/ADS_app_automation_modes.png](../_images/ADS_app_automation_modes.png)

From the command line:

![../_images/Automation_mode.png](../_images/Automation_mode.png)


---

<!-- === 来源: concepts/index.md === -->

# Concepts[](#concepts "Link to this heading")

* [Python Script Execution](execution.md)
  + [Automation](execution.md#automation)


---

