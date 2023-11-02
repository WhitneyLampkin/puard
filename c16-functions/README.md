# C16. Functions

## Notification Pipeline

Alertmanager Labels:

- Inhibition
- Silencing
- Routing
- Grouping
- Throttling and repetition
- Notification

## Configuration File

```yml
global:
  smtp_smarthost: 'localhost:25'
  smtp_from: 'yourprometheus@example.org' 1

route:
  receiver: example-email

receivers:
 - name: example-email
   email_configs:
    - to: 'youraddress@example.org'
```

### Routing Tree

```yml
route:
  receiver: fallback-pager
  routes:
   - matchers:
       - severity = page
     receiver: team-pager
   - matchers:
       - severity = ticket
     receiver: team-ticket
```

```yml
route:
  receiver: fallback-pager
  routes:
   - matchers:
       - severity = page
     receiver: team-pager
   - matchers:
       - severity =~ "(ticket|issue|email)"
     receiver: team-ticket
```

```yml
route:
  receiver: fallback-pager
  routes:
   # Frontend team.
   - matchers:
       - team = frontend
     receiver: frontend-pager
     routes:
      - matchers:
          - severity = page
        receiver: frontend-pager
      - matchers:
          - severity = ticket
        receiver: frontend-ticket
   # Backend team.
   - matchers:
       - team = backend
     receiver: backend-pager
     routes:
      - matchers:
          - severity = page
          - env = dev
        receiver: backend-ticket
      - matchers:
          - severity = page
        receiver: backend-pager
      - matchers:
          - severity = ticket
        receiver: backend-ticket
```

### Receivers

### Inhibitions

## Alertmanager Web Interface