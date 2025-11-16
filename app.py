"""
Flask Web Application for Olivetti Face Classification
This app allows users to upload face images and get predictions.
"""

from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = 'savedmodel.pth'
model = None

def load_model():
    """Load the trained model at startup"""
    global model
    try:
        if os.path.exists(MODEL_PATH):
            model_data = joblib.load(MODEL_PATH)
            model = model_data['model']
            print("✓ Model loaded successfully!")
        else:
            print(f"Warning: Model file '{MODEL_PATH}' not found. Please train the model first.")
    except Exception as e:
        print(f"Error loading model: {e}")

def preprocess_image(image_bytes):
    """
    Preprocess uploaded image to match Olivetti faces format (64x64 grayscale)
    """
    try:
        # Open image from bytes
        img = Image.open(io.BytesIO(image_bytes))
        
        # Convert to grayscale
        img = img.convert('L')
        
        # Resize to 64x64 (Olivetti faces format)
        img = img.resize((64, 64))
        
        # Convert to numpy array and normalize
        img_array = np.array(img)
        img_array = img_array.flatten() / 255.0
        
        return img_array.reshape(1, -1)
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle image upload and return prediction"""
    if model is None:
        return jsonify({
            'error': 'Model not loaded. Please train the model first.',
            'success': False
        })
    
    if 'file' not in request.files:
        return jsonify({
            'error': 'No file uploaded',
            'success': False
        })
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({
            'error': 'No file selected',
            'success': False
        })
    
    try:
        # Read and preprocess the image
        image_bytes = file.read()
        processed_image = preprocess_image(image_bytes)
        
        if processed_image is None:
            return jsonify({
                'error': 'Failed to process image',
                'success': False
            })
        
        # Make prediction
        prediction = model.predict(processed_image)[0]
        prediction_proba = model.predict_proba(processed_image)[0]
        confidence = float(max(prediction_proba)) * 100
        
        return jsonify({
            'success': True,
            'prediction': int(prediction),
            'confidence': round(confidence, 2),
            'message': f'Predicted Person ID: {int(prediction)}'
        })
    
    except Exception as e:
        return jsonify({
            'error': f'Prediction failed: {str(e)}',
            'success': False
        })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

if __name__ == '__main__':
    load_model()
    app.run(host='0.0.0.0', port=5000, debug=False)
