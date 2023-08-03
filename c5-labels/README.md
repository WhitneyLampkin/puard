# C5. Labels

> TODO: Add all chapter notes

## Notes

### What are labels?

- Labels: Key-value pairs associated with time series
- Example: path label added to http request metrics
    ```yaml
    http_requests_total{path="/login"}
    http_requests_total{path="/logout"}
    http_requests_total{path="/adduser"}
    http_requests_total{path="/comment"}
    http_requests_total{path="/view"}
    ```
