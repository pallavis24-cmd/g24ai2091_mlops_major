"""
Flask application for face classification using trained DecisionTreeClassifier.
Provides /health endpoint for health checks and /predict endpoint for predictions.
"""
from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = 'savedmodel.pth'
model = None

def load_model():
    """Load the trained model if it exists."""
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print(f"Model loaded successfully from {MODEL_PATH}")
    else:
        print(f"Warning: Model file {MODEL_PATH} not found. Please train the model first.")

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    status = {
        'status': 'healthy',
        'model_loaded': model is not None,
        'model_path': MODEL_PATH
    }
    return jsonify(status), 200

@app.route('/predict', methods=['POST'])
def predict():
    """Prediction endpoint for face classification."""
    if model is None:
        return jsonify({
            'error': 'Model not loaded. Please train the model first by running train.py'
        }), 503
    
    try:
        # Get data from request
        data = request.get_json()
        
        if 'features' not in data:
            return jsonify({'error': 'Missing "features" in request'}), 400
        
        # Convert input to numpy array
        features = np.array(data['features']).reshape(1, -1)
        
        # Validate input shape (Olivetti faces have 4096 features: 64x64 pixels)
        if features.shape[1] != 4096:
            return jsonify({
                'error': f'Invalid input shape. Expected 4096 features, got {features.shape[1]}'
            }), 400
        
        # Make prediction
        prediction = model.predict(features)
        prediction_proba = model.predict_proba(features)
        
        response = {
            'prediction': int(prediction[0]),
            'confidence': float(np.max(prediction_proba)),
            'all_probabilities': prediction_proba[0].tolist()
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API information."""
    return jsonify({
        'message': 'Face Recognition System - Olivetti Faces Classifier',
        'endpoints': {
            '/health': 'GET - Health check',
            '/predict': 'POST - Make predictions (requires "features" in JSON body)',
            '/': 'GET - This information page'
        },
        'model': 'DecisionTreeClassifier',
        'dataset': 'Olivetti Faces'
    }), 200

if __name__ == '__main__':
    load_model()
    # Run on all interfaces (0.0.0.0) to work with Docker
    app.run(host='0.0.0.0', port=5000, debug=True)
