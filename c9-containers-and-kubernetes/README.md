# C9. Containers and Kubernetes

>TODO: Add info about running chapter examples

## cAdvisor

- cAdvisor: exporter provides metrics about cgroups
    - CPU Metrics
    - Memory Metrics
- cgroups: Linux kernel isolation feature used for container implementation on Linux
- Run cAdvisor w/ Docker
  ```shell
  docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  gcr.io/cadvisor/cadvisor:v0.45.0
  ```
- cAdvisor running locally on localhost:8080/containers
    ![image](../images/9-cAdvisor-photo.png)
- cAdvisor metrics
    ![image](../images/9-cAdvisor-metrics-photo.png)

## Kubernetes

```shell
# 9-2 Downloading and running Minikube
hostname $ curl -LO \ https://storage.googleapis.com/minikube/releases/latesn/minikube-linux-amd64
hostname $ mv minikube-linux-amd64 minikube
hostname $ chmod +x minikube
hostname $ ./minikube start --kubernetes-version=v1.25.0
```

```shell
# 9-3 Downloading and testing Kubectl
hostname $ wget \ https://storage.googleapis.com/kubernetes-release/release/v1.25.0/bin/linux/amd64/kubectl
hostname $ chmod +x kubectl
hostname $ ./kubectl get services
```
```shell
# 9-4. Setting up permissions and running Prometheus on Kubernetes
hostname $./kubectl apply -f prometheus-deployment.yml
hostname $./minikube service prometheus --url
```

## Service Discovery

- 6 Types of K8s service discoveries
    1. Node
    2. Endpoints
    3. Endpointslice
    4. Service
    5. Pod
    6. Ingress
        > Reminder: Ingress allows traffic to come into K8s clusters by exposing it to the outside world.

## Kube State Metrics

```shell
# Running Kube State Metrics
hostname $./kubectl apply -f kube-state-metrics.yml
hostname $./minikube service kube-state-metrics --url
```
