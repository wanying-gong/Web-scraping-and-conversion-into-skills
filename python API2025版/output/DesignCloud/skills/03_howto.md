# Howto
> **说明：** Howto 相关页面。

> **何时使用：** 当你需要查阅 Howto 相关内容时

---

## 本文件目录

- **How-To** (`howto/index.md`)
- **How to Manage Simulation Jobs** (`howto/job.md`)
- **Wait for All Jobs to Complete** (`howto/manage_jobs/all_job_wait.md`)
- **Cancel a Job** (`howto/manage_jobs/cancel_job.md`)
- **Get the List of Submitted Jobs** (`howto/manage_jobs/job_list.md`)
- **Get the name of a job** (`howto/manage_jobs/job_name.md`)
- **Wait for a Job to Complete** (`howto/manage_jobs/job_wait.md`)
- **Creating a new Python virtual environment based on ADS Python** (`howto/newvenv.md`)
- **Submitting Simulations on a Design Cloud Server** (`howto/submit_sims/dc_server.md`)
- **Submitting simulations on a Local Queue** (`howto/submit_sims/local_queue.md`)
- **Submitting simulations on a Site Cluster Queue** (`howto/submit_sims/sitecluster_queue.md`)
- **Submit a Netlist to Design Cloud Server** (`howto/submit_sims/submit_netlist.md`)
- **Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings** (`howto/submit_sims/submit_pre.md`)
- **How to Submit Simulations on Design Cloud Hosts** (`howto/submit_simulations.md`)
- **How to Set Up a Python Virtual Environment** (`howto/venv.md`)

---

<!-- === 来源: howto/index.md === -->

# How-To[](#how-to "Link to this heading")

* [How to Set Up a Python Virtual Environment](venv.md)
  + [Creating a new Python virtual environment based on ADS Python](newvenv.md)
* [How to Submit Simulations on Design Cloud Hosts](submit_simulations.md)
  + [Submitting simulations on a Local Queue](submit_sims/local_queue.md)
  + [Submitting simulations on a Site Cluster Queue](submit_sims/sitecluster_queue.md)
  + [Submitting Simulations on a Design Cloud Server](submit_sims/dc_server.md)
  + [Submit a Netlist to Design Cloud Server](submit_sims/submit_netlist.md)
  + [Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings](submit_sims/submit_pre.md)
* [How to Manage Simulation Jobs](job.md)
  + [Cancel a Job](manage_jobs/cancel_job.md)
  + [Get the name of a job](manage_jobs/job_name.md)
  + [Wait for a Job to Complete](manage_jobs/job_wait.md)
  + [Get the List of Submitted Jobs](manage_jobs/job_list.md)
  + [Wait for All Jobs to Complete](manage_jobs/all_job_wait.md)


---

<!-- === 来源: howto/job.md === -->

# How to Manage Simulation Jobs[](#how-to-manage-simulation-jobs "Link to this heading")

Once you submit your job with the resource settings to a Design Cloud host, you can perform various operations on the job such as:
- cancel a running/pending job
- get the status of a job
- wait for a job to complete

* [Cancel a Job](manage_jobs/cancel_job.md)
* [Get the name of a job](manage_jobs/job_name.md)
* [Wait for a Job to Complete](manage_jobs/job_wait.md)
* [Get the List of Submitted Jobs](manage_jobs/job_list.md)
* [Wait for All Jobs to Complete](manage_jobs/all_job_wait.md)


---

<!-- === 来源: howto/manage_jobs/all_job_wait.md === -->

# Wait for All Jobs to Complete[](#wait-for-all-jobs-to-complete "Link to this heading")

To wait for all jobs to complete, you can use the `await_all_jobs()` function. This function takes an argument timeout which is the maximum time to wait for all jobs to complete.

```
from keysight.ads.experimental_simulation import hpc
jobs = hpc.get_jobs()

# If you wish to wait for all jobs to complete
status = hpc.await_all_jobs(jobs)
print(status)

# If you wish to wait for all jobs to complete within a timeout
status = hpc.await_all_jobs(jobs, timeout=60) # Wait for 60 seconds
print(status)

# If all jobs are completed, the function will return True
# If all jobs are not completed within the timeout, the function will return False

# You can also check the status of each job
for job in jobs:
    job_status = job.get_status()
    print(job_status)
```


---

<!-- === 来源: howto/manage_jobs/cancel_job.md === -->

# Cancel a Job[](#cancel-a-job "Link to this heading")

To cancel a job, you can use the `cancel()` function. We assume that you already have a design to submit with the resource settings.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.ResourceSettings()
resource_settings.url = "https://mydesigncloudserver.com"  # Replace with your Design Cloud Server URL
resource_settings.parallel_jobs = 4
resource_settings.max_threads_per_job = 4
job = hpc.submit_design_with_settings(design, resource_settings)

# Cancel a running job
if job.is_running():
    job.cancel()

# Cancel a pending job
job_status = job.get_status()
if job_status == "Pending":
    job.cancel()

# Valid job status values:
# - "Running"
# - "Pending"
# - "Completed"
# - "Error"
# - "Canceled"
# - "UnknownId"
# - "Downloading"
```


---

<!-- === 来源: howto/manage_jobs/job_list.md === -->

# Get the List of Submitted Jobs[](#get-the-list-of-submitted-jobs "Link to this heading")

To get the list of submitted jobs, you can use the `get_jobs()` function. This function returns a list of all the jobs submitted by the user.

```
from keysight.ads.experimental_simulation import hpc
jobs = hpc.get_jobs()
print(jobs)
```


---

<!-- === 来源: howto/manage_jobs/job_name.md === -->

# Get the name of a job[](#get-the-name-of-a-job "Link to this heading")

To get the name of a job, you can use the `get_name()` function.

```
from keysight.ads.experimental_simulation import hpc
job = hpc.submit_design_with_settings(design, resource_settings)

job_name = job.get_name()
print(job_name)
```


---

<!-- === 来源: howto/manage_jobs/job_wait.md === -->

# Wait for a Job to Complete[](#wait-for-a-job-to-complete "Link to this heading")

To wait for a job to complete, you can use the `await_job()` function. This function takes an argument timeout which is the maximum time to wait for the job to complete.

```
from keysight.ads.experimental_simulation import hpc
job = hpc.submit_design_with_settings(design, resource_settings)

job.await_job(timeout=60)  # Wait for 60 seconds

# If the job is completed, the function will return True
# If the job is not completed within the timeout, the function will return False

# You can also check the status of the job
job_status = job.get_status()
print(job_status)
```


---

<!-- === 来源: howto/newvenv.md === -->

# Creating a new Python virtual environment based on ADS Python[](#creating-a-new-python-virtual-environment-based-on-ads-python "Link to this heading")

1. Create a Python virtual environment (venv).

   The venv must be created using the Python shipped with ADS, or with another Python installation with the same major and minor version.

   Example for Linux:

   ```
   $HPEESOF_DIR/tools/python/bin/python3 -m venv --system-site-packages $HOME/ads_venv
   ```

   Example for Windows:

   ```
   %HPEESOF_DIR%\tools\python\python -m venv --system-site-packages %USERPROFILE%\ads_venv
   ```
2. Select the venv by setting **ADS\_PYTHONHOME**.

   This can be accomplished either as an environment variable or in de\_sim.cfg (user level or above, i.e. not supported in workspace-level cfg)

   Example for Linux:

   ```
   export ADS_PYTHONHOME=$HOME/ads_venv
   ```

   Example for Windows:

   ```
   set ADS_PYTHONHOME=%USERPROFILE%\ads_venv
   ```

   To set the venv path in de\_sim.cfg rather than an environment variable, add a line like this:

   ```
   ADS_PYTHONHOME={$HOME}/ads_venv
   ```
3. Run ADS. Python support is automatically enabled.

   ```
   ads
   ```

   To verify the venv is being used, execute menu **Python->Python Console…**, and type the following in the console:

   ```
   import sys
   print(sys.executable)
   ```

   The path to the Python executable will be displayed, and it should be prefixed by the venv path.


---

<!-- === 来源: howto/submit_sims/dc_server.md === -->

# Submitting Simulations on a Design Cloud Server[](#submitting-simulations-on-a-design-cloud-server "Link to this heading")

If you already have deployed a Design Cloud Server, you can specify the url of that server in the resource settings.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.ResourceSettings()
resource_settings.url = 'https://mydesigncloudserver.com' # Replace with your Design Cloud server URL
resource_settings.parallel_jobs = 8
resource_settings.threads = 4
resource_settings.memory_value = 16
resource_settings.memory_unit = 'GB'

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```

We have provided an example for your reference on how to submit simulations on a Design Cloud server. see [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)


---

<!-- === 来源: howto/submit_sims/local_queue.md === -->

# Submitting simulations on a Local Queue[](#submitting-simulations-on-a-local-queue "Link to this heading")

If you want to run your design on your local host, you can use the `LocalResourceSettings` class to specify the resource settings. Under this mode, you can also simulate your design parallely on your local machine.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.LocalResourceSettings()
resource_settings.parallel_jobs = 8
resource_settings.threads = 4
resource_settings.memory_value = 16
resource_settings.memory_unit = 'GB'

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```

We have provided an example for your reference on how to submit simulations on a local queue. see [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)


---

<!-- === 来源: howto/submit_sims/sitecluster_queue.md === -->

# Submitting simulations on a Site Cluster Queue[](#submitting-simulations-on-a-site-cluster-queue "Link to this heading")

If you use ADS on a machine which is also a submit host of your HPC cluster then you can directly submit your simulations to the cluster without installing the Design Cloud server.
To do that you can either set `SITECLUSTER` environment variable or use the `set_sitecluster_path()` function.

`SITECLUSTER` refers to the path of the sitecluster wrapper script. This script is used to submit the simulation to the cluster.
You can also define your sitecluster queue name by setting the `SITECLUSTER_NAME` environment variable.

If you have `SITECLUSTER` set in your environment

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.SiteclusterResourceSettings()
```

If you want to set the sitecluster wrapper path in your script

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.SiteclusterResourceSettings()
resource_settings.set_sitecluster_path('/path/to/your/sitecluster/wrapper/script') # path to the sitecluster wrapper script
resource_settings.parallel_jobs = 8
resource_settings.threads = 4
resource_settings.memory_value = 16
resource_settings.memory_unit = 'GB'

# You can specify additional site cluster options. We have given an example below for LSF cluster
# The below option allows user to select the sles15 machines in his LSF cluster
# You can specify any other options as per your cluster configuration.
resource_settings.site_cluster_extra_options = "--customargs=\"-R select[sles15]\""

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```


---

<!-- === 来源: howto/submit_sims/submit_netlist.md === -->

# Submit a Netlist to Design Cloud Server[](#submit-a-netlist-to-design-cloud-server "Link to this heading")

If you have a netlist and want to submit it to the Design Cloud Server, you can use the `submit_netlist()` function.

```
from keysight.ads.experimental_simulation import hpc

resource_settings.url = 'https://mydesigncloudserver.com' # Replace with your Design Cloud server URL
resource_settings = hpc.ResourceSettings()
resource_settings.parallel_jobs = 8
resource_settings.threads = 4
resource_settings.memory_value = 16
resource_settings.memory_unit = 'GB'

# In case you want to upload a supporting file
resource_settings.uploading_filename = "/my/example/upload_file.upl" # Replace with your upl file path
resource_settings.queue = 'normal' # Replace with your queue name

job = hpc.submit_netlist(netlist)  # Where netlist is the netlist object: db.Netlist

# You can also check the status of the job
job_status = job.get_status()
print(job_status)
```


---

<!-- === 来源: howto/submit_sims/submit_pre.md === -->

# Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings[](#submitting-simulations-on-a-design-cloud-server-with-pre-defined-resource-settings "Link to this heading")

If the design context is already set up with the resource settings, you can directly submit the design to the Design Cloud Server using you can use the `submit_design()` function.

```
from keysight.ads.experimental_simulation import hpc

# To view the resource settings saved in the context
resource_settings = hpc.get_resource_settings()
print(resource_settings)

job = hpc.submit_design(design)  # Where design is the design object: db.Design

# You can also check the status of the job
job_status = job.get_status()
print(job_status)

# You can also set the same resource settings to a different design

design2 = db.Design()
hpc.set_resource_settings(design2, resource_settings)
job2 = hpc.submit_design(design2)

# You can also check the status of the job
job_status2 = job2.get_status()
print(job_status2)
```


---

<!-- === 来源: howto/submit_simulations.md === -->

# How to Submit Simulations on Design Cloud Hosts[](#how-to-submit-simulations-on-design-cloud-hosts "Link to this heading")

* [Submitting simulations on a Local Queue](submit_sims/local_queue.md)
* [Submitting simulations on a Site Cluster Queue](submit_sims/sitecluster_queue.md)
* [Submitting Simulations on a Design Cloud Server](submit_sims/dc_server.md)
* [Submit a Netlist to Design Cloud Server](submit_sims/submit_netlist.md)
* [Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings](submit_sims/submit_pre.md)


---

<!-- === 来源: howto/venv.md === -->

# How to Set Up a Python Virtual Environment[](#how-to-set-up-a-python-virtual-environment "Link to this heading")

It is possible to use ADS modules from a Python virtual environment rather than within the embedded ADS Python.
To do this you can create a new virtual environment based on the ADS Python executable.

* [Creating a new Python virtual environment based on ADS Python](newvenv.md)


---

