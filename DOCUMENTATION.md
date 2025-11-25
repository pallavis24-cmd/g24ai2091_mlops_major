# ML Ops Major Assignment - Complete Documentation
**Student Name:** Pallavi Sarangi  
**Roll No:** G24AI2091  
**Course:** PGDDE IITJ - ML Ops

---

## Repository Links

### GitHub Repository
**URL:** https://github.com/pallavis24-cmd/g24ai2091_mlops_major

### Docker Hub Repository
**URL:** https://hub.docker.com/r/pallavis24/olivetti-classifier

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Branch Strategy](#branch-strategy)
3. [Step-by-Step Implementation](#step-by-step-implementation)
4. [Docker Implementation](#docker-implementation)
5. [Kubernetes Deployment](#kubernetes-deployment)
6. [CI/CD Pipeline](#cicd-pipeline)
7. [Testing and Validation](#testing-and-validation)
8. [Analysis and Results](#analysis-and-results)
9. [Commands Reference](#commands-reference)

---

## Project Overview

This project implements a complete MLOps pipeline for face classification using the Olivetti faces dataset. The pipeline includes:
- Machine learning model training (DecisionTreeClassifier)
- Automated CI/CD with GitHub Actions
- Docker containerization
- Kubernetes deployment with 3 replicas
- Flask web application for inference

### Dataset
- **Name:** Olivetti Faces Dataset
- **Source:** sklearn.datasets
- **Samples:** 400 images (40 individuals, 10 images each)
- **Image Size:** 64x64 pixels, grayscale

### Model
- **Algorithm:** DecisionTreeClassifier (scikit-learn)
- **Train/Test Split:** 70%/30%
- **Expected Accuracy:** ~90%+

---

## Branch Strategy

### 1. Main Branch
**Purpose:** Initial repository setup  
**Contents:**
- README.md
- .gitignore
- Basic project documentation

### 2. Dev Branch
**Purpose:** Model development and CI/CD setup  
**Contents:**
- `train.py` - Model training script
- `test.py` - Model testing script
- `requirements.txt` - Python dependencies
- `.github/workflows/ci.yml` - GitHub Actions workflow

### 3. Docker_CICD Branch
**Purpose:** Containerization and deployment  
**Contents:**
- `app.py` - Flask web application
- `Dockerfile` - Container configuration
- `templates/index.html` - Web UI
- `k8s/deployment.yaml` - Kubernetes deployment
- `k8s/service.yaml` - Kubernetes service

---

## Step-by-Step Implementation

### STEP 1: Main Branch Setup

#### 1.1 Initialize Git Repository
```bash
cd "d:\Pallavi Sarangi PGDDE IITJ\Trimester 3\ML Ops\Assignments\Assignment 2_Major_Due 19th Nov'25"
git init
```

#### 1.2 Create .gitignore
```
# Python
__pycache__/
*.py[cod]
venv/
env/

# Model files
# savedmodel.pth

# IDEs
.vscode/
.idea/

# OS
.DS_Store
```

#### 1.3 Create README.md
- Documented project overview
- Branch strategy
- Installation instructions
- Usage guide

#### 1.4 Commit and Push
```bash
git add .
git commit -m "Initial commit: Add README.md and .gitignore"
git branch -M main
git remote add origin https://github.com/pallavis24-cmd/g24ai2091_mlops_major.git
git push -u origin main
```

---

### STEP 2: Dev Branch - Model Development

#### 2.1 Create Dev Branch
```bash
git checkout -b dev
```

#### 2.2 Create train.py
**Key Features:**
- Loads Olivetti faces dataset using `fetch_olivetti_faces()`
- Splits data: 70% train, 30% test with stratification
- Trains DecisionTreeClassifier with max_depth=20
- Saves model and test data using joblib

**Code Structure:**
```python
# Load dataset
olivetti = fetch_olivetti_faces()
X, y = olivetti.data, olivetti.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Train model
clf = DecisionTreeClassifier(random_state=42, max_depth=20)
clf.fit(X_train, y_train)

# Save model
joblib.dump({'model': clf, 'X_test': X_test, 'y_test': y_test}, 'savedmodel.pth')
```

#### 2.3 Create test.py
**Key Features:**
- Loads saved model from `savedmodel.pth`
- Computes accuracy on test set
- Displays classification report
- Shows confusion matrix statistics

#### 2.4 Create requirements.txt
```
scikit-learn>=1.0.0
joblib>=1.0.0
numpy>=1.21.0
flask>=2.0.0
pillow>=9.0.0
```

#### 2.5 Create CI/CD Workflow
**File:** `.github/workflows/ci.yml`

**Workflow Steps:**
1. Checkout repository
2. Set up Python 3.9
3. Install dependencies
4. Run train.py
5. Verify model file created
6. Run test.py
7. Upload model as artifact

#### 2.6 Commit and Push
```bash
git add .
git commit -m "Add train.py, test.py, requirements.txt, and CI/CD workflow"
git push -u origin dev
```

---

### STEP 3: Docker_CICD Branch

#### 3.1 Create Docker_CICD Branch
```bash
git checkout dev
git checkout -b docker_cicd
```

#### 3.2 Create Flask Application (app.py)
**Key Features:**
- Model loading at startup
- Image preprocessing (resize to 64x64, grayscale, normalize)
- `/predict` endpoint for inference
- `/health` endpoint for health checks
- Error handling and validation

**API Endpoints:**
- `GET /` - Web interface
- `POST /predict` - Image upload and prediction
- `GET /health` - Health check

#### 3.3 Create Web UI (templates/index.html)
**Features:**
- Drag-and-drop image upload
- Image preview
- Real-time prediction display
- Confidence score with progress bar
- Responsive design
- Error handling

#### 3.4 Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY train.py test.py app.py ./
COPY templates/ templates/

# Train model during build
RUN python train.py

EXPOSE 5000

CMD ["python", "app.py"]
```

#### 3.5 Create .dockerignore
```
__pycache__/
*.pyc
venv/
.git
.vscode/
*.pdf
*.docx
```

#### 3.6 Build and Test Docker Image Locally
```bash
# Build image
docker build -t pallavis24/olivetti-classifier:latest .

# Run container
docker run -p 5000:5000 pallavis24/olivetti-classifier:latest

# Test in browser
# Open http://localhost:5000
```

#### 3.7 Push to Docker Hub
```bash
# Login to Docker Hub
docker login

# Push image
docker push pallavis24/olivetti-classifier:latest
```

#### 3.8 Create Kubernetes Manifests

**deployment.yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: olivetti-classifier-deployment
spec:
  replicas: 3  # Ensures 3 replicas always running
  selector:
    matchLabels:
      app: olivetti-classifier
  template:
    metadata:
      labels:
        app: olivetti-classifier
    spec:
      containers:
      - name: olivetti-classifier
        image: pallavis24/olivetti-classifier:latest
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 5000
        readinessProbe:
          httpGet:
            path: /health
            port: 5000
```

**service.yaml:**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: olivetti-classifier-service
spec:
  type: LoadBalancer
  selector:
    app: olivetti-classifier
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
```

#### 3.9 Deploy to Kubernetes
```bash
# Apply deployment
kubectl apply -f k8s/deployment.yaml

# Apply service
kubectl apply -f k8s/service.yaml

# Verify deployment
kubectl get deployments
kubectl get pods
kubectl get services
```

#### 3.10 Commit and Push
```bash
git add .
git commit -m "Add Flask app, Dockerfile, Kubernetes manifests for docker_cicd branch"
git push -u origin docker_cicd
```

---

## Docker Implementation

### Building the Image
```bash
docker build -t pallavis24/olivetti-classifier:latest .
```

### Running Locally
```bash
docker run -d -p 5000:5000 --name olivetti-app pallavis24/olivetti-classifier:latest
```

### Pushing to Docker Hub
```bash
docker login
docker push pallavis24/olivetti-classifier:latest
```

### Useful Docker Commands
```bash
# List images
docker images

# List running containers
docker ps

# View logs
docker logs olivetti-app

# Stop container
docker stop olivetti-app

# Remove container
docker rm olivetti-app

# Remove image
docker rmi pallavis24/olivetti-classifier:latest
```

---

## Kubernetes Deployment

### Prerequisites
- Kubernetes cluster (Minikube, Docker Desktop, or cloud provider)
- kubectl installed and configured

### Deployment Commands
```bash
# Deploy application
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Check deployment status
kubectl get deployments
kubectl get pods
kubectl get services

# View pod details
kubectl describe deployment olivetti-classifier-deployment

# View logs
kubectl logs <pod-name>

# Scale replicas (if needed)
kubectl scale deployment olivetti-classifier-deployment --replicas=5

# Delete deployment
kubectl delete -f k8s/deployment.yaml
kubectl delete -f k8s/service.yaml
```

### Verifying 3 Replicas
```bash
kubectl get pods -l app=olivetti-classifier
# Should show 3 pods running
```

---

## CI/CD Pipeline

### GitHub Actions Workflow

**Trigger:** Push to `dev` or `docker_cicd` branches

**Jobs:**
1. **check_working_repo**
   - Checkout code
   - Setup Python 3.9
   - Install dependencies
   - Train model
   - Verify model file
   - Test model
   - Upload model artifact

### Viewing Workflow Results
1. Go to GitHub repository
2. Click "Actions" tab
3. View workflow runs
4. Check logs for each step

---

## Testing and Validation

### Local Testing

#### 1. Test Model Training
```bash
python train.py
# Expected output: Model saved as 'savedmodel.pth'
```

#### 2. Test Model Accuracy
```bash
python test.py
# Expected output: Test accuracy ~90%+
```

#### 3. Test Flask App
```bash
python app.py
# Open browser: http://localhost:5000
# Upload face image and verify prediction
```

### Docker Testing
```bash
# Build and run
docker build -t test-app .
docker run -p 5000:5000 test-app

# Test health endpoint
curl http://localhost:5000/health
```

### Kubernetes Testing
```bash
# Check pod health
kubectl get pods
kubectl describe pod <pod-name>

# Test service
kubectl get service olivetti-classifier-service
# Access via LoadBalancer IP or port-forward
kubectl port-forward service/olivetti-classifier-service 8080:80
```

---

## Analysis and Results

### Model Performance
- **Training Accuracy:** ~100% (may indicate overfitting)
- **Test Accuracy:** ~90%+
- **Total Classes:** 40 (persons 0-39)
- **Total Test Samples:** 120 (30% of 400)

### CI/CD Benefits
1. **Automation:** Automatic testing on every push
2. **Consistency:** Same environment every time
3. **Quality:** Catches errors early
4. **Documentation:** Workflow serves as documentation

### Docker Benefits
1. **Portability:** Runs anywhere Docker is installed
2. **Consistency:** Same environment dev to prod
3. **Isolation:** Dependencies packaged together
4. **Scalability:** Easy to scale horizontally

### Kubernetes Benefits
1. **High Availability:** 3 replicas ensure uptime
2. **Auto-healing:** Restarts failed pods
3. **Load Balancing:** Distributes traffic
4. **Scalability:** Easy to scale up/down

---

## Commands Reference

### Git Commands
```bash
# Initialize and setup
git init
git remote add origin <url>
git branch -M main

# Branching
git checkout -b <branch-name>
git branch -a

# Committing
git add .
git commit -m "message"
git push -u origin <branch-name>

# Status
git status
git log --oneline
```

### Docker Commands
```bash
# Build
docker build -t <image-name>:<tag> .

# Run
docker run -d -p <host-port>:<container-port> <image-name>

# Management
docker ps
docker images
docker logs <container-id>
docker stop <container-id>
docker rm <container-id>
docker rmi <image-id>

# Registry
docker login
docker push <image-name>:<tag>
docker pull <image-name>:<tag>
```

### Kubernetes Commands
```bash
# Apply configurations
kubectl apply -f <file.yaml>

# Get resources
kubectl get deployments
kubectl get pods
kubectl get services

# Describe resources
kubectl describe deployment <name>
kubectl describe pod <name>

# Logs
kubectl logs <pod-name>
kubectl logs -f <pod-name>  # Follow

# Scale
kubectl scale deployment <name> --replicas=<number>

# Delete
kubectl delete -f <file.yaml>
kubectl delete deployment <name>
kubectl delete service <name>

# Port forwarding
kubectl port-forward service/<name> <local-port>:<service-port>
```

---

## Screenshots Guide

### Required Screenshots:

1. **GitHub Repository**
   - All three branches visible
   - Commit history
   - File structure

2. **Git Commands**
   - Initial setup
   - Branch creation
   - Commits and pushes

3. **Model Training**
   - Running train.py
   - Model file created
   - Training accuracy

4. **Model Testing**
   - Running test.py
   - Test accuracy output
   - Classification report

5. **GitHub Actions**
   - Workflow runs
   - Successful execution
   - Workflow logs

6. **Docker Build**
   - docker build command
   - Build process
   - Image created

7. **Docker Hub**
   - Repository page
   - Image details
   - Tags

8. **Docker Run**
   - Container running
   - docker ps output
   - Application accessible

9. **Flask Application**
   - Homepage
   - Image upload
   - Prediction result
   - Confidence score

10. **Kubernetes Deployment**
    - kubectl apply commands
    - 3 pods running
    - Service details
    - LoadBalancer status

---

## Conclusion

This project successfully demonstrates a complete MLOps pipeline including:
- ✅ Automated ML model training and testing
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Docker containerization
- ✅ Kubernetes deployment with 3 replicas
- ✅ Web interface for model inference

All branches (main, dev, docker_cicd) are maintained separately as required, showcasing proper Git workflow and branching strategy.

---

**Prepared by:** Pallavi Sarangi (G24AI2091)  
**Date:** November 16, 2025  
**Course:** ML Ops - PGDDE IITJ
