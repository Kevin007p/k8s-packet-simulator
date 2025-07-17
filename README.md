# Kubernetes Packet Simulator

Simulates packet traffic using a Flask app deployed on Kubernetes. Logs requests per pod and shows them on a live dashboard.

## Stack

- Python (Flask)
- Docker
- Kubernetes (Docker Desktop or Minikube)
- Bash

# YAML Files Explanation

### deployment.yaml

- Runs 3 replicas of the Flask app using the local Docker image `packet-inspector:v1.1`.
- Sets pod label `app: packet-inspector` and exposes container port 5000.
- Passes the pod’s name to the app via the `HOSTNAME` environment variable.

### service.yaml

- Creates a NodePort service named `packet-service` exposing port 80.
- Routes traffic to pods labeled `app: packet-inspector` on container port 5000.
- Exposes the service on node port 30007, accessible via `localhost:30007`.

## How to Run

```bash
# 1. Build the Docker image
docker build -t packet-inspector:v1.1 app/

# 2. Deploy to Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

#3. Check if pods are running
kubectl get pods

# 4. Open the dashboard
# Visit in your browser:
http://localhost:30007

# 5. Simulate traffic
chmod +x load-test/simulate-load.sh
load-test/simulate-load.sh
```
