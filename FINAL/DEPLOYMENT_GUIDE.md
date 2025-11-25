# MLOps Major Assignment - Complete Setup Guide

## 🎯 Project Status: ✅ READY FOR DEPLOYMENT

### ✅ Completed Components

1. **Flask Application** (`app.py`)
   - ✅ Health check endpoint: `/health`
   - ✅ Prediction endpoint: `/predict`
   - ✅ Home endpoint: `/`
   - ✅ Model loading from `savedmodel.pth`

2. **Model Training** (`train.py`)
   - ✅ Olivetti faces dataset (400 samples, 40 classes)
   - ✅ DecisionTreeClassifier
   - ✅ 70/30 train/test split
   - ✅ Model saved as `savedmodel.pth`

3. **Docker Configuration**
   - ✅ `Dockerfile` created
   - ✅ `.dockerignore` created
   - ✅ Multi-stage build with model training

4. **CI/CD Pipeline** (`.github/workflows/docker-image.yml`)
   - ✅ Automated Docker build on push
   - ✅ Push to Docker Hub: `pallavis24/olivetti-classifier`
   - ✅ Triggers on `docker_cicd` and `main` branches

5. **Kubernetes Deployment** (`k8s/deployment.yaml`)
   - ✅ 3 replicas configuration
   - ✅ Service with LoadBalancer
   - ✅ Health probes (liveness & readiness)
   - ✅ Resource limits and requests

6. **Git Repository**
   - ✅ All code committed to `docker_cicd` branch
   - ✅ Pushed to GitHub: `pallavis24-cmd/g24ai2091_mlops_major`

---

## 🚀 Next Steps to Complete

### Step 1: Set Up Docker Hub Secrets (REQUIRED for CI/CD)

1. **Go to GitHub Repository Settings:**
   - Navigate to: https://github.com/pallavis24-cmd/g24ai2091_mlops_major
   - Click on **Settings** → **Secrets and variables** → **Actions**

2. **Add Docker Hub Credentials:**
   - Click **New repository secret**
   - Add these two secrets:
     ```
     Name: DOCKER_USERNAME
     Value: pallavis24
     
     Name: DOCKER_PASSWORD
     Value: <your-docker-hub-token-or-password>
     ```

3. **Get Docker Hub Token (Recommended):**
   - Go to: https://hub.docker.com/settings/security
   - Click **New Access Token**
   - Name it: `github-actions-olivetti`
   - Copy the token and use it as `DOCKER_PASSWORD`

### Step 2: Build and Push Docker Image Locally (Optional)

**If Docker Desktop is not running, start it first:**

```powershell
# Check if Docker is running
docker ps

# If not, start Docker Desktop from Start Menu

# Then build the image
cd "d:\Pallavi Sarangi PGDDE IITJ\Trimester 3\ML Ops\Assignments\Assignment 2_Major_Due 19th Nov'25\FINAL"
docker build -t pallavis24/olivetti-classifier:latest .

# Login to Docker Hub
docker login -u pallavis24

# Push to Docker Hub
docker push pallavis24/olivetti-classifier:latest

# Test locally
docker run -d -p 5000:5000 pallavis24/olivetti-classifier:latest
```

### Step 3: Let GitHub Actions Build Automatically (Recommended)

Once secrets are set up, GitHub Actions will automatically:
1. Build the Docker image on every push
2. Push to Docker Hub
3. No need to build locally!

Just push code and check: https://github.com/pallavis24-cmd/g24ai2091_mlops_major/actions

### Step 4: Deploy to Kubernetes

```powershell
# Prerequisites: Install kubectl and have a cluster (minikube/kind/cloud)

# For Minikube (local testing)
minikube start

# Apply deployment
kubectl apply -f k8s/deployment.yaml

# Verify deployment (should see 3 pods)
kubectl get pods -l app=olivetti-classifier
kubectl get deployment olivetti-classifier
kubectl get service olivetti-classifier-service

# Access the service
minikube service olivetti-classifier-service

# Or for cloud deployments, get external IP
kubectl get service olivetti-classifier-service
# Then access: http://<EXTERNAL-IP>/health
```

---

## 📊 Current Test Results

**Local Flask Server:**
- ✅ Running on: http://localhost:5000
- ✅ Health endpoint: http://localhost:5000/health → Status 200
- ✅ Model loaded successfully

**Model Performance:**
- Training Accuracy: 83.21%
- Test Accuracy: 50.83%

---

## 📁 Project Structure

```
FINAL/
├── .github/
│   └── workflows/
│       └── docker-image.yml     # CI/CD pipeline
├── k8s/
│   ├── deployment.yaml          # K8s deployment (3 replicas)
│   └── README.md               # K8s deployment guide
├── app.py                      # Flask application
├── train.py                    # Model training script
├── Dockerfile                  # Docker configuration
├── requirements.txt            # Python dependencies
├── .dockerignore              # Docker ignore rules
├── .gitignore                 # Git ignore rules
└── Readme.md                  # Assignment documentation
```

---

## 🔗 Important Links

- **GitHub Repository:** https://github.com/pallavis24-cmd/g24ai2091_mlops_major
- **Docker Hub:** https://hub.docker.com/r/pallavis24/olivetti-classifier
- **Current Branch:** `docker_cicd`

---

## ✅ Assignment Requirements Met

| Requirement | Status | Details |
|------------|--------|---------|
| Olivetti faces dataset | ✅ | Using sklearn.datasets |
| DecisionTreeClassifier | ✅ | Trained with 70/30 split |
| Model saved as savedmodel.pth | ✅ | Using joblib |
| Flask web application | ✅ | With /health and /predict |
| Docker containerization | ✅ | Dockerfile created |
| CI/CD with GitHub Actions | ✅ | Automated build pipeline |
| Kubernetes deployment | ✅ | 3 replicas configured |
| Docker Hub repository | ✅ | pallavis24/olivetti-classifier |
| Branch strategy | ✅ | main, dev, docker_cicd |

---

## 🎓 Submission Checklist

- [x] Code pushed to GitHub repository
- [x] Flask application with /health endpoint working
- [x] Dockerfile created
- [x] GitHub Actions workflow configured
- [ ] Docker Hub secrets added to GitHub
- [ ] Docker image built and pushed to Docker Hub
- [ ] Kubernetes deployment tested (optional for submission)

---

## 📝 Notes

1. **Priority:** Add Docker Hub secrets to enable automated CI/CD
2. The Flask server is currently running locally on port 5000
3. All code is committed and pushed to the `docker_cicd` branch
4. GitHub Actions will automatically build on next push after secrets are added
5. Docker image will be available at: `docker pull pallavis24/olivetti-classifier:latest`

---

**Student:** Pallavi Sarangi  
**Roll Number:** G24AI2091  
**Institution:** Indian Institute of Technology, Jodhpur  
**Course:** MLOps Major Assignment
