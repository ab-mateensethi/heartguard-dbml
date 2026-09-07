import joblib
import pandas as pd

model = joblib.load("random_forest_model.pkl")

sample = pd.DataFrame({
    "Age": [int(input("Age: "))],
    "Sex": [int(input("Sex (0=F, 1=M): "))],
    "ChestPainType": [int(input("ChestPainType (0-3): "))],
    "RestingBP": [int(input("RestingBP: "))],
    "Cholesterol": [int(input("Cholesterol: "))],
    "FastingBS": [int(input("FastingBS (0/1): "))],
    "RestingECG": [int(input("RestingECG (0-2): "))],
    "MaxHR": [int(input("MaxHR: "))],
    "ExerciseAngina": [int(input("ExerciseAngina (0/1): "))],
    "Oldpeak": [float(input("Oldpeak: "))],
    "ST_Slope": [int(input("ST_Slope (0-2): "))]
})

prediction = model.predict(sample)
print("----------------------")

print("Prediction:", "Heart Disease")
if prediction[0] == 1:
    print("Heart Disease: YES")
else:
    print("Heart Disease: NO")