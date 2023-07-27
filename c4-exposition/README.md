# C4. Exposition

> TODO: Add all chapter notes

## Notes

### Client Libraries

- Python
- Go
- Java

### Pushgateway

### Bridges

### Parsers

### Text Exposition Format

```
# HELP example_gauge An example gauge
# TYPE example_gauge gauge
example_gauge -0.7
# HELP my_counter_total An example counter
# TYPE my_counter_total counter
my_counter_total 14
# HELP my_summary An example summary
# TYPE my_summary summary
my_summary_sum 0.6
my_summary_count 19
# HELP latency_seconds An example histogram
# TYPE latency_seconds histogram
latency_seconds_bucket{le="0.1"} 7
latency_seconds_bucket{le="0.2"} 18
latency_seconds_bucket{le="0.4"} 24
latency_seconds_bucket{le="0.8"} 28
latency_seconds_bucket{le="+Inf"} 29
latency_seconds_sum 0.6
latency_seconds_count 29
```

### Open Metrics

## Running Examples

### Go Examples

- [Monitor Golang w/ Prometheus](https://antonputra.com/monitoring/monitor-golang-with-prometheus/#gauge)
- `go run 4-6-go-app.go` from c4-exposition/go-examples directory

## Questions

- Did I miss an introduction on what a registry is during an earlier chapter?