# C8. Service Discovery

> TODO: Add chapter notes

## Examples

```yml
// Example 8-2. Using Ansible’s templating to create targets for the Node Exporter on all machines

scrape_configs:
 - job_name: node
   static_configs:
    - targets:
{% for host in groups["all"] %}
      - {{ host }}:9100
{% endfor %}
```

```yml
// Example 8-3. Two monitoring targets are provided, each in its own static config

scrape_configs:
 - job_name: node
   static_configs:
    - targets: 1
       - host1:9100
      labels:
        datacenter: paris
    - targets: 2
       - host2:9100
       - host3:9100
      labels:
        datacenter: montreal
```