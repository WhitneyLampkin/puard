# C3. Instrumentation

> TODO: Add all chapter notes

## Approaching Instrumentation

### Service Instrumentation

- Online-serving systems
    - RED method: Rate, Errors and Duration
- Offline-serving systems
    - USE method: Utilization, Saturation and Errors
- Batch jobs
    - Pushgateway
    - Node Exporter textfile collector

### Library Instrumentation

> TODO

### Naming Conventions for Prometheus Metrics

1. Use the _library_name_unit_suffix_ structure
    - Use snake case as shown in the example (each component of the name should be lowercase and separated by an underscore)
1. Start with a letter
    - Regex: [a-zA-Z_:][a-zA-Z0-9_:]*
1. Do not use colons
1. Do not use underscores (reserved for Prometheus use)
1. Avoid using `_total`, `_count`, `_sum`, `_bucket` suffixes
    - Exception is `_total` for counters
1. Use unprefixed base units: seconds, bytes, ratios
    - Always include the unit of metric in the name
    - i.e. _mymetric_seconds_total_
    - Avoid count as a unit
    - It's okay if the unit is missing 
1. Try to use the same prefix on related metrics
1. Don't include labels in metric names
1. Be careful with names for metrics for libraries
