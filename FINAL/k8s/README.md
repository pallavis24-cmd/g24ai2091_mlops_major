# Kubernetes Deployment Guide

## Prerequisites
- Kubernetes cluster (minikube, kind, or cloud provider)
- kubectl installed and configured

## Deployment Steps

### 1. Apply the deployment
```bash
kubectl apply -f k8s/deployment.yaml
```

### 2. Verify deployment
```bash
# Check pods (should see 3 replicas)
kubectl get pods -l app=olivetti-classifier

# Check deployment status
kubectl get deployment olivetti-classifier

# Check service
kubectl get service olivetti-classifier-service
```

### 3. Access the application

#### For Minikube:
```bash
minikube service olivetti-classifier-service
```

#### For Cloud Providers:
```bash
# Get external IP
kubectl get service olivetti-classifier-service

# Access using external IP
curl http://<EXTERNAL-IP>/health
```

### 4. Test the endpoints
```bash
# Health check
curl http://<SERVICE-URL>/health

# Home page
curl http://<SERVICE-URL>/

# Make a prediction (example)
curl -X POST http://<SERVICE-URL>/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [0.1, 0.2, ...]}'  # 4096 features
```

## Scaling

### Scale replicas
```bash
kubectl scale deployment olivetti-classifier --replicas=5
```

## Monitoring

### View logs
```bash
# All pods
kubectl logs -l app=olivetti-classifier

# Specific pod
kubectl logs <POD-NAME>

# Follow logs
kubectl logs -f <POD-NAME>
```

### Describe resources
```bash
kubectl describe deployment olivetti-classifier
kubectl describe service olivetti-classifier-service
kubectl describe pod <POD-NAME>
```

## Cleanup

### Delete all resources
```bash
kubectl delete -f k8s/deployment.yaml
```
