"""Train and save the Spam/Ham text classification pipeline."""
from app import train_model

if __name__ == "__main__":
    train_model()
    print("Model trained successfully: model/spam_classifier.joblib")
