# End-to-End MLOps Pipeline
## ML Ops Major Assignment

## Overview
This repository contains a complete, automated MLOps pipeline for face classification using the Olivetti faces dataset. The project demonstrates:
- Machine Learning model training and testing
- CI/CD automation with GitHub Actions
- Containerization with Docker
- Kubernetes deployment with replicas

## Dataset & Model
- **Dataset**: Olivetti faces dataset from sklearn.datasets (400 images of 40 individuals)
- **Model**: DecisionTreeClassifier from scikit-learn
- **Train/Test Split**: 70% training, 30% testing

## Repository Structure
```
.
├── README.md
├── .gitignore
├── train.py              # Model training script (dev branch)
├── test.py               # Model testing script (dev branch)
├── app.py                # Flask web application (docker_cicd branch)
├── Dockerfile            # Docker configuration (docker_cicd branch)
├── requirements.txt      # Python dependencies
├── k8s/                  # Kubernetes manifests (docker_cicd branch)
│   ├── deployment.yaml
│   └── service.yaml
└── .github/
    └── workflows/
        └── ci.yml        # CI/CD pipeline configuration
```

## Branching Strategy
- **main**: Initial setup with README.md and .gitignore
- **dev**: Model development (train.py, test.py) and CI/CD workflow
- **docker_cicd**: Flask app, Docker containerization, and Kubernetes deployment

## Quick Start

### Prerequisites
- Python 3.8+
- Docker
- Kubernetes (kubectl)
- Git

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Install dependencies
pip install -r requirements.txt
```

## Branch-Specific Instructions

### Main Branch (Initial Setup)
Contains basic setup files:
- README.md
- .gitignore

### Dev Branch (Model Development)
```bash
# Switch to dev branch
git checkout dev

# Train the model
python train.py

# Test the model
python test.py
```

### Docker_CICD Branch (Deployment)
```bash
# Switch to docker_cicd branch
git checkout docker_cicd

# Build Docker image
docker build -t <your-dockerhub-username>/olivetti-classifier:latest .

# Push to Docker Hub
docker push <your-dockerhub-username>/olivetti-classifier:latest

# Deploy to Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

## CI/CD Pipeline
The GitHub Actions workflow automatically:
1. Sets up Python environment
2. Installs dependencies
3. Trains the model
4. Tests the model accuracy

## Docker Hub
Docker Image: `<your-dockerhub-username>/olivetti-classifier:latest`

## Kubernetes Deployment
- **Replicas**: 3
- **Service Type**: LoadBalancer
- **Port**: 5000

## Model Performance
- The DecisionTreeClassifier achieves approximately 90%+ accuracy on the test set
- Model is saved as `savedmodel.pth` using joblib

## Web Application
Flask web app features:
- Image upload interface
- Real-time face classification
- Displays predicted person ID (0-39)

## Author
Pallavi Sarangi - PGDDE IITJ

## License
This project is created for educational purposes as part of the MLOps course assignment.
