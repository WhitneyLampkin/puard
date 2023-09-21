# C10. Common Exporters

> TODO: Add all chapter notes

## Other Monitoring Systems

## InfluxBD
- Similar to Prometheus, little effort to integrate

### Demo

- Running InfluxDB Exporter locally
![Alt text](image.png)

- Sending metrics manually
![Alt text](image-2.png)

- InfluxDB Metrics
![Alt text](image-1.png)

## StatsD
- Uses events instead of metrics

### Demo

- Running StatsD locally
![Alt text](image-3.png)

- StatsD Metrics
![Alt text](image-5.png)

- Manually defining Gauges
![Alt text](image-7.png)
![Alt text](image-6.png)

- Manually defining Summary/Historm metrics
![Alt text](image-9.png)

- Manually defining Counters
![Alt text](image-8.png)

- StatsD Example w/ Mapping Config
![Alt text](image-10.png)

## List of Monitoring Systems and Exporters
- Collectd
- InfluxBD
- Graphite
- StatsD
- Java Management eXtensions (JMX)
- SNMP
- CloudWatch Exporter
- New Relic Exporter
- Pingdom Exporter
- Stackdriver Exporter
- NRPE Exporter