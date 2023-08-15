# C7. Node Exporter

> TODO: Add chapter notes

## Introduction

- _Uberagent_: Single process that monitors everything on a machine
    - Can be operational or performance bottleneck
- Prometheus architecture notes
    - Each service exposes its own metrics
    - Each service optionally uses an exporter
    - Service metrics scraped by Prometheus
- Windows Exporter --> Windows
- Node Exporter --> Linux
    - Run as nonroot user
    - Run same as system daemons like sshd or cron
    - If running with Docker, use volumes and command-line parameters for container mounting
    - Config fetched metrics by enabling or disabling with command-line flags
        - _Enable_: `--collector.{METRIC_NAME}`
        - _Disable_: `--no-collector.{METRIC_NAME}`
        - _Disable All_: `collector-disable-defaults`

## Available Metrics

> NOTE: Refer to `/metrics` path for full list of Node Exporter metrics.

### CPU Collector

- `node_cpu_seconds_total`: seconds the CPUs spent in each mode
    - labels: `cpu`, `mode`

### Filesystem Collector

- `node_filesystem_`: metrics about your mounted filesystems
    - labels: `device`, `fstype`, `mountpoint`
    - restricting filesystems: `--collector.filesystem.mount-points-exclude`, `--collector.filesystem.​fs-types-exclude`
    - `_avail_byes` vs. `_free_bytes`
    - `node_filesystem_files` vs. `node_filesystem_files_free`

### Diskstats Collector

- `node_disk_`: disk I/O metrics from /proc/diskstats
    - labels: `device`
    - flags: `--collector.diskstats.device-exclude`
    - most diskstats metrics are collectors
    - metrics: `node_disk_io_now`, `node_disk_io_time_seconds_total`, `node_disk_read_bytes_total`, `node_disk_read_time_seconds_total`, `node_disk_reads_completed_total`, `node_disk_written_bytes_total`, `node_disk_write_time_seconds_total`, `node_disk_writes_completed_total`

### Netdev Collector

- `node_network_`: metrics about your network devices
    - labels: `device`
    - metrics: `node_network_receive_bytes_total`, `node_network_transmit_bytes_total`, `node_network_receive_packets_total`, `node_network_transmit_packets_total`
    - calculating network bandwidth: `rate(node_network_receive_bytes_total[1m])`

### Meminfo Collector

- `node_memory_`: standard memory-related metrics from /proc/meminfo
    - metrics: `node_memory_MemTotal_bytes`, `node_memory_MemFree_bytes`, `node_memory_Cached_bytes`, `node_memory_Buffers_bytes`, `node_memory_MemAvailable`

### Hwmon Collector

- `node_hwmon_`: provides bare metal metrics such as temperature and fan speeds
    - labels: `chip`, `sensor`

### Stat Collector

- Mix of metrics from /proc/stat
    - `node_boot_time_seconds`
    - `node_intr_total`
    - `node_interrupts_total`
    - `node_forks_total`
    - `node_context_switches_total`
    - `node_procs_blocked`
    - `node_procs_running`

### Uname Collector

- `node_uname_info`: Labeled system information as provided by the uname
    system call
    - labels: `nodename`, `instance`

### OS Collector

- `node_os_`
    - metrics: `node_os_info`, `node_os_version`

### Loadavg Collector

- `node_load#`: provides the 1-, 5-, and 15-minute load averages
    - meaning varies per platform

### Pressure Collector

- `node_pressure_`: resource pressure metrics for the following 3 resources: CPU, memory and I/O
    - metrics: `node_pressure_cpu_waiting_seconds_total`, `node_pressure_io_stalled_seconds_total`, `node_pressure_io_waiting_seconds_total`, `node_pressure_memory_stalled_seconds_total`, `node_pressure_memory_waiting_seconds_total`

### Textfile Collector

- metrics gathered from user files
    - metrics about a machine
- can be used to add user metrics to cronjobs or grab static info from files
- using textfile collector
    - enabled by default
    - must provide the `--collector.textfile.directory` command-line flag to the Node Exporter for it to work

**Running the Textfile example**

`./node_exporter --collector.textfile.directory=$PWD/textfile`

### Timestamps

- `node_textfile_mtime_`
