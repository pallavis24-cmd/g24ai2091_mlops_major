"""
Test the trained DecisionTreeClassifier model.
This script loads the saved model and computes its accuracy on the test set.
"""

import joblib
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    print("Loading saved model...")
    
    # Load the saved model and test data
    try:
        model_data = joblib.load('savedmodel.pth')
        clf = model_data['model']
        X_test = model_data['X_test']
        y_test = model_data['y_test']
    except FileNotFoundError:
        print("Error: 'savedmodel.pth' not found. Please run train.py first.")
        return
    
    print(f"Test set size: {len(X_test)}")
    
    # Make predictions on the test set
    print("\nMaking predictions on test set...")
    y_pred = clf.predict(X_test)
    
    # Calculate test accuracy
    test_accuracy = accuracy_score(y_test, y_pred)
    print(f"\n{'='*50}")
    print(f"Test Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")
    print(f"{'='*50}")
    
    # Display additional metrics
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))
    
    # Display confusion matrix statistics
    cm = confusion_matrix(y_test, y_pred)
    print(f"\nConfusion Matrix Shape: {cm.shape}")
    print(f"Correct Predictions: {np.trace(cm)}/{len(y_test)}")
    print(f"Incorrect Predictions: {len(y_test) - np.trace(cm)}/{len(y_test)}")
    
    print("\n✓ Testing completed successfully!")

if __name__ == "__main__":
    main()
