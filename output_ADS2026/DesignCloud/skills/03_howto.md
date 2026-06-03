# Howto
> **说明：** Howto 相关页面。

> **何时使用：** 当你需要查阅 Howto 相关内容时

---

## 本文件目录

- **How-To** (`howto/index.md`)
- **How to Manage Simulation Jobs** (`howto/job.md`)
- **Wait for All Jobs to Complete** (`howto/manage_jobs/all_job_wait.md`)
- **Cancel a Job** (`howto/manage_jobs/cancel_job.md`)
- **Checking for Running Jobs** (`howto/manage_jobs/check_running_jobs.md`)
- **Getting the dataset after a simulation** (`howto/manage_jobs/get_dataset.md`)
- **Get the List of Submitted Jobs** (`howto/manage_jobs/job_list.md`)
- **Get the name of a job** (`howto/manage_jobs/job_name.md`)
- **Wait for a Job to Complete** (`howto/manage_jobs/job_wait.md`)
- **Polling the Status of a Job** (`howto/manage_jobs/polling_status.md`)
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
  + [Polling the Status of a Job](manage_jobs/polling_status.md)
  + [Getting the dataset after a simulation](manage_jobs/get_dataset.md)
  + [Checking for Running Jobs](manage_jobs/check_running_jobs.md)


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
* [Polling the Status of a Job](manage_jobs/polling_status.md)
* [Getting the dataset after a simulation](manage_jobs/get_dataset.md)
* [Checking for Running Jobs](manage_jobs/check_running_jobs.md)


---

<!-- === 来源: howto/manage_jobs/all_job_wait.md === -->

# Wait for All Jobs to Complete[](#wait-for-all-jobs-to-complete "Link to this heading")

To wait for all jobs to complete, you can use the [`await_all_jobs()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.await_all_jobs "keysight.ads.experimental_simulation.hpc.await_all_jobs") function. This function takes an argument timeout which is the maximum time to wait for all jobs to complete.

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
    print(job_status.value)
```

Note that [`await_all_jobs()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.await_all_jobs "keysight.ads.experimental_simulation.hpc.await_all_jobs") will block until all jobs are completed or the timeout is reached. If you want to cancel the await early, you must cancel all the running jobs.

For example, you can cancel all jobs on a Ctrl-C by adding a signal handler for SIGINT.

```
# cancel all jobs on a Ctrl-C
signal.signal(signal.SIGINT, lambda signal, frame: [job.cancel() for job in hpc.get_jobs()])
```

Note : you could also leave jobs running after a Control-C by calling QCoreApplication.quit() in the signal handler.
If you do this you may have to check if the job is running in any scripts you run later, see [Checking for Running Jobs](check_running_jobs.md) for more information.


---

<!-- === 来源: howto/manage_jobs/cancel_job.md === -->

# Cancel a Job[](#cancel-a-job "Link to this heading")

To cancel a job, you can use the [`cancel()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.cancel "keysight.ads.experimental_simulation.hpc.Job.cancel") function. We assume that you already have a design to submit with the resource settings.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.ResourceSettings(
    url = "https://mydesigncloudserver.com", # Replace with your Design Cloud Server URL
    parallel_jobs = 4,
    max_threads_per_job = 4,
)
job = hpc.submit_design_with_settings(design, resource_settings)

# Cancel a running job
if job.is_running():
    job.cancel()

# Cancel a pending job
job_status = job.get_status()
if job_status == hpc.JobStatus.PENDING:
    job.cancel()
```


---

<!-- === 来源: howto/manage_jobs/check_running_jobs.md === -->

# Checking for Running Jobs[](#checking-for-running-jobs "Link to this heading")

While writing automation scripts you may often be able to assume that it’s okay to submit a new job, but if someone has started a job manually, or if a script started a job and left it running, it’s possible that you won’t be able submit a job because an old instance with the same name is already running.

To account for this you can check for running jobs using [`get_jobs()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.get_jobs "keysight.ads.experimental_simulation.hpc.get_jobs") and wait for them to finish if necessary.

For example:

```
running_jobs = [job for job in hpc.get_jobs() if job.is_running()]
if running_jobs:
    job_names = [job.get_name() for job in running_jobs]
    print(f"These jobs are running : {job_names}, waiting for them to complete")
    hpc.await_all_jobs()

# Now you can submit a new job
```


---

<!-- === 来源: howto/manage_jobs/get_dataset.md === -->

# Getting the dataset after a simulation[](#getting-the-dataset-after-a-simulation "Link to this heading")

When a simulation is finished you can find and read the dataset using the information held in [`JobStartupInfo`](../../reference/hpc/JobStartupInfo.md#keysight.ads.experimental_simulation.hpc.JobStartupInfo "keysight.ads.experimental_simulation.hpc.JobStartupInfo").

```
from keysight.ads.experimental_simulation import hpc
import keysight.ads.dataset as dataset
from pathlib import Path

job = hpc.submit_design_with_settings(design, settings)
job_startup_info = job.get_startup_info()

# wait for the job to complete
hpc.await_all_jobs(600)

# use the workspace dir and dataset name to get the file name of the dataset
dataset_file_name = Path(job_startup_info.workspace_dir) / "data" / (job_startup_info.dataset_name + ".ds")

# open it and print the contents
data = dataset.open(dataset_file_name)
for (name, vb) in data.items():
    print(f"VariableBlock DataFrame: {name}\n{vb.to_dataframe()}")
```


---

<!-- === 来源: howto/manage_jobs/job_list.md === -->

# Get the List of Submitted Jobs[](#get-the-list-of-submitted-jobs "Link to this heading")

To get the list of submitted jobs, you can use the [`get_jobs()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.get_jobs "keysight.ads.experimental_simulation.hpc.get_jobs") function. This function returns a list of all the jobs submitted by the user.

```
from keysight.ads.experimental_simulation import hpc
jobs = hpc.get_jobs()
print(jobs)
```


---

<!-- === 来源: howto/manage_jobs/job_name.md === -->

# Get the name of a job[](#get-the-name-of-a-job "Link to this heading")

To get the name of a job, you can use the [`get_name()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.get_name "keysight.ads.experimental_simulation.hpc.Job.get_name") function.

```
from keysight.ads.experimental_simulation import hpc
job = hpc.submit_design_with_settings(design, resource_settings)

job_name = job.get_name()
print(job_name)
```


---

<!-- === 来源: howto/manage_jobs/job_wait.md === -->

# Wait for a Job to Complete[](#wait-for-a-job-to-complete "Link to this heading")

To wait for a job to complete, you can use the [`await_job()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.await_job "keysight.ads.experimental_simulation.hpc.Job.await_job") function. This function takes an argument timeout which is the maximum time to wait for the job to complete.

```
from keysight.ads.experimental_simulation import hpc
job = hpc.submit_design_with_settings(design, resource_settings)

job.await_job(timeout=60)  # Wait for 60 seconds

# If the job is completed, the function will return True
# If the job is not completed within the timeout, the function will return False

# You can also check the status of the job
job_status = job.get_status()
print(job_status.value)
```

Note that [`await_job()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.await_job "keysight.ads.experimental_simulation.hpc.Job.await_job") will block until the job is completed or the timeout is reached. If you want to cancel the await early, you must cancel the job.

For example, you can cancel a job on a Ctrl-C by adding a signal handler for SIGINT.

```
# cancel a job on a Ctrl-C
signal.signal(signal.SIGINT, lambda signal, frame: job.cancel())
```

Note : you could also leave a job running after a Control-C by calling QCoreApplication.quit() in the signal handler.
If you do this you may have to check if the job is running in any scripts you run later, see [Checking for Running Jobs](check_running_jobs.md) for more information.


---

<!-- === 来源: howto/manage_jobs/polling_status.md === -->

# Polling the Status of a Job[](#polling-the-status-of-a-job "Link to this heading")

To poll the status of a running job you can use a QT Timer and query [`get_status()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.get_status "keysight.ads.experimental_simulation.hpc.Job.get_status") and/or [`get_subjob_status()`](../../reference/hpc/Job.md#keysight.ads.experimental_simulation.hpc.Job.get_subjob_status "keysight.ads.experimental_simulation.hpc.Job.get_subjob_status").

```
from keysight.ads.experimental_simulation import hpc
job = hpc.submit_design_with_settings(design, resource_settings)

# create a QTimer that will poll the job status, and subjob statuses every second
timer = QTimer()
timer.timeout.connect(
    lambda: print(f"Job status: {job.get_status()} : {job.get_subjob_status()}")
)
timer.start(1000)

job.await_job()  # wait for the job to finish
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
resource_settings = hpc.ResourceSettings(
    url = "https://mydesigncloudserver.com", # Replace with your Design Cloud Server URL
    parallel_jobs = 4,
    max_threads_per_job = 4,
    memory_value = 16,
    memory_unit = 'GB',
    queue = 'default', # Replace with your queue name
    # Additional options for Design Cloud
    # project_name='your_project_name', # Replace with your own project name if you have configured
    # uploading_filename='/path/to/your/upload_file.upl', # Replace with your own upload file path
    # email='your_email@address.com', # Replace with your own email address
    # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
)

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```

We have provided an example for your reference on how to submit simulations on a Design Cloud server. see [Simulate a Circuit on Design Cloud Server](../../examples/ex_simulate_dc_server.md)


---

<!-- === 来源: howto/submit_sims/local_queue.md === -->

# Submitting simulations on a Local Queue[](#submitting-simulations-on-a-local-queue "Link to this heading")

If you want to run your design on your local host, you can use the [`LocalResourceSettings`](../../reference/hpc/LocalResourceSettings.md#keysight.ads.experimental_simulation.hpc.LocalResourceSettings "keysight.ads.experimental_simulation.hpc.LocalResourceSettings") class to specify the resource settings. Under this mode, you can also simulate your design parallelly on your local machine.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.LocalResourceSettings(
    parallel_jobs = 8,
    max_threads_per_job = 4,
    queue_job_locally = False,
    # Note: To submit multiple designs on Local queue and want to queue them
    # set queue_job_locally = True".
)

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```

We have provided an example for your reference on how to submit simulations on a local queue. see [Create and Simulate a Circuit on Design Cloud Local Queue](../../examples/ex_simulate_local_queue.md)


---

<!-- === 来源: howto/submit_sims/sitecluster_queue.md === -->

# Submitting simulations on a Site Cluster Queue[](#submitting-simulations-on-a-site-cluster-queue "Link to this heading")

If you use ADS on a machine which is also a submit host of your HPC cluster then you can directly submit your simulations to the cluster without installing the Design Cloud server.

```
from keysight.ads.experimental_simulation import hpc
resource_settings = hpc.SiteclusterResourceSettings(
    sitecluster = "/path/to/your/sitecluster/wrapper/script", # Replace with your own sitecluster wrapper script path (.bat|.sh)
    parallel_jobs = 4,
    max_threads_per_job = 4,
    memory_value = 16,
    memory_unit = 'GB',
    queue = 'default', # Replace with your queue name
    # Additional options for Design Cloud
    # project_name='your_project_name', # Replace with your own project name if you have configured
    # uploading_filename='/path/to/your/upload_file.upl', # Replace with your own upload file path
    # email='your_email@address.com', # Replace with your own email address
    # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
)

job = hpc.submit_design_with_settings(design, resource_settings) # Where design is the design object: db.Design
```


---

<!-- === 来源: howto/submit_sims/submit_netlist.md === -->

# Submit a Netlist to Design Cloud Server[](#submit-a-netlist-to-design-cloud-server "Link to this heading")

If you have a netlist and want to submit it to the Design Cloud Server, you can use the [`submit_netlist()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_netlist "keysight.ads.experimental_simulation.hpc.submit_netlist") function.

```
from keysight.ads.experimental_simulation import hpc

resource_settings.url = 'https://mydesigncloudserver.com' # Replace with your Design Cloud server URL
resource_settings = hpc.ResourceSettings(
    url = "https://mydesigncloudserver.com", # Replace with your Design Cloud server URL
    parallel_jobs = 4,
    max_threads_per_job = 4,
    memory_value = 16,
    memory_unit = 'GB',
    queue = 'default', # Replace with your queue name
    # Additional options for Design Cloud
    # project_name='your_project_name', # Replace with your own project name if you have configured
    # uploading_filename='/path/to/your/upload_file.upl', # Replace with your own upload file path
    # email='your_email@address.com', # Replace with your own email address
    # site_cluster_extra_options='--customargs "-q normal"' # Replace with your own custom args
)

jobname = "mynetlist_job"
netlist_path = "path/to/your/netlist.net"

job = hpc.submit_netlist(jobname, netlist_path, resource_settings)  # Where netlist is the path to your netlist file

# You can also check the status of the job
job_status = job.get_status()
print(job_status.value)
```


---

<!-- === 来源: howto/submit_sims/submit_pre.md === -->

# Submitting Simulations on a Design Cloud Server with Pre-defined Resource Settings[](#submitting-simulations-on-a-design-cloud-server-with-pre-defined-resource-settings "Link to this heading")

If the design context is already set up with the resource settings, you can directly submit the design to the Design Cloud Server using you can use the [`submit_design()`](../../reference/hpc/index.md#keysight.ads.experimental_simulation.hpc.submit_design "keysight.ads.experimental_simulation.hpc.submit_design") function.

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

