"""
Train a DecisionTreeClassifier on the Olivetti faces dataset.
This script loads the dataset, splits it into train/test sets (70/30),
trains the model, and saves it using joblib.
"""

import joblib
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np

def main():
    print("Loading Olivetti faces dataset...")
    # Load the Olivetti faces dataset
    olivetti = fetch_olivetti_faces()
    X = olivetti.data
    y = olivetti.target
    
    print(f"Dataset shape: {X.shape}")
    print(f"Number of classes: {len(np.unique(y))}")
    print(f"Total samples: {len(X)}")
    
    # Split the dataset into 70% training and 30% testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    print(f"\nTraining set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}")
    
    # Create and train the DecisionTreeClassifier
    print("\nTraining DecisionTreeClassifier...")
    clf = DecisionTreeClassifier(random_state=42, max_depth=20)
    clf.fit(X_train, y_train)
    
    # Calculate training accuracy
    train_accuracy = clf.score(X_train, y_train)
    print(f"Training Accuracy: {train_accuracy:.4f} ({train_accuracy*100:.2f}%)")
    
    # Save the model and test data using joblib
    print("\nSaving model and test data...")
    model_data = {
        'model': clf,
        'X_test': X_test,
        'y_test': y_test
    }
    joblib.dump(model_data, 'savedmodel.pth')
    print("Model saved as 'savedmodel.pth'")
    
    print("\n✓ Training completed successfully!")

if __name__ == "__main__":
    main()
