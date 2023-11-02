# C19. Alertmanager

Alertmanager collects alerts from all Prometheus servers and creates notifications (emails, chat messages, incidents, pages, etc.).

## Notification Pipeline

**Alertmanager Labels:**

- Inhibition: prevent notifications for some alerts if another more severe alert is firing
- Silencing: ignore certain alerts for a while
- Routing: delivery notifications to different places
- Grouping: group alerts into one per instance (i.e. rack, datacenter, globally, etc.)
- Throttling and repetition: reduces spamming of messages for known issues but repeats unacknowledged alerts so they don't get overlooked.
- Notification: templated, customizable content with details about the system sent via a receiver

## Configuration File

```yml
# alertmanager.yml
# minimal config that sends notifications to an email address
global:
  smtp_smarthost: 'localhost:25'
  smtp_from: 'yourprometheus@example.org' 1

# minimal of 1 route and 1 receiver is required
route:
  receiver: example-email

receivers:
 - name: example-email
   email_configs:
    - to: 'youraddress@example.org'
```

### Routing Tree

```yml
# alertmanager.yml
# routing tree example

# global settings omitted

route:
# post-order tree transversal: the fallback-pager route is the parent route and will only be used if all child routes aren't matched
  receiver: fallback-pager
  routes:
   - matchers:
       - severity = page
     receiver: team-pager
   - matchers:
       - severity = ticket
     receiver: team-ticket
```

**Matching Operators**
- = 
- !=
- =~: must match the provided regex
- !~: must not match the provided regex

```yml
# alertmanager.yml
# regex example
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
# alertmanager.yml
# multi-team example using team label
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

**Grouping**

```yml
# alertmanager.yml
# grouping example

route:
  receiver: fallback-pager
  group_by: [team]
  routes:
   # Frontend team.
   - matchers:
       - team = frontend
     group_by: [region, env]
     receiver: frontend-pager
     routes:
      - matchers:
          - severity = page
        receiver: frontend-pager
      - matchers:
          - severity = ticket
        group_by: [region, env, alertname]
        receiver: frontend-ticket
```

**Throlling and repretition**

### Receivers

```yml
# alertmanager.yml 
# receiver example using notification templates(based on go templating)
receivers:
 - name: frontend-pager
   slack_configs:
    - api_url: https://hooks.slack.com/services/XXXXXXXX
      channel: '#pages'
      title: 'Alerts in {{ .GroupLabels.region }} {{ .GroupLabels.env }}!'
      text: >
        {{ .Alerts | len }} alerts:
        {{ range .Alerts }}
        {{ range .Labels.SortedPairs }}{{ .Name }}={{ .Value }} {{ end }}
        {{ if eq .Annotations.wiki "" -}}
        Wiki: http://wiki.mycompany/{{ .Labels.alertname }}
        {{- else -}}
        Wiki: http://wiki.mycompany/{{ .Annotations.wiki }}
        {{- end }}
        {{ if ne .Annotations.dashboard "" -}}
        Dashboard: {{ .Annotations.dashboard }}&region={{ .Labels.region }}
        {{- end }}

        {{ end }}
```

### Inhibitions

## Alertmanager Web Interface