from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load("../models/random_forest_model.pkl")
except FileNotFoundError:
    raise Exception("Model file not found. Ensure the path to 'random_forest_model.pkl' is correct.")

# Default route
@app.route("/")
def home():
    return jsonify({"message": "Model is ready to use"})

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the input JSON
        data = request.get_json()

        # Check if data is provided
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Convert input JSON to DataFrame
        input_df = pd.DataFrame([data])

        # Make predictions
        prediction = model.predict(input_df)

        # Return the prediction
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
