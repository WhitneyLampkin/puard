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

### Naming Conventions for Labels

- Begin with a letter (a–z or A–Z) and be followed with letters, numbers, and underscores
- Not usually namespaced
- Avoid labels likely to be used as target labels, such as `env`, `cluster`, `service`, `team`, `zone`, `region` and `type`
- Use snakecase
- `instance` and `job` label names are reserved for Prometheus only
- Can be any UTF-8 characters
- Empty label values are allowed but my be confusing

### Other Notes

- Had issues running `docker-compose up --build` for the c5 python examples and learned that configuration issues were the cause.
    - Fixed with `rm  ~/.docker/config.json `
    - _[TODO]_: Understand why