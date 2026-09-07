import os
import joblib
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define the model path (ensure the file is in the same directory as app.py)
MODEL_PATH = "random_forest_model.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    print(f"Error: {MODEL_PATH} not found! Please run train_model.py first.")
    model = None

@app.route("/")
def home():
    # Renders the main frontend dashboard (index.html must be inside the 'templates' folder)
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"success": False, "error": "Model is not loaded. Please contact the system administrator."}), 500

    try:
        # Collect data from the form and construct a DataFrame matching the model's training features
        input_data = pd.DataFrame({
            "Age": [int(request.form.get("Age"))],
            "Sex": [int(request.form.get("Sex"))],
            "ChestPainType": [int(request.form.get("ChestPainType"))],
            "RestingBP": [int(request.form.get("RestingBP"))],
            "Cholesterol": [int(request.form.get("Cholesterol"))],
            "FastingBS": [int(request.form.get("FastingBS"))],
            "RestingECG": [int(request.form.get("RestingECG"))],
            "MaxHR": [int(request.form.get("MaxHR"))],
            "ExerciseAngina": [int(request.form.get("ExerciseAngina"))],
            "Oldpeak": [float(request.form.get("Oldpeak"))],
            "ST_Slope": [int(request.form.get("ST_Slope"))]
        })

        # Generate prediction using the loaded Random Forest model
        prediction = model.predict(input_data)
        
        # Structure the evaluation output text
        if prediction[0] == 1:
            result_text = "Heart Disease Detected (High Risk)"
            is_positive = True
        else:
            result_text = "No Heart Disease Detected (Low Risk)"
            is_positive = False

        # Send JSON response back to the async frontend fetch request
        return jsonify({
            "success": True,
            "prediction": int(prediction[0]),
            "result_text": result_text,
            "is_positive": is_positive
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)