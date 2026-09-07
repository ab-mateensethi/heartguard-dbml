HeartGuard DBML ❤️ 

**Heart Disease Prediction System using Database Design & Machine Learning**

HeartGuard DBML is an end-to-end academic project that combines **Database Management Systems** with **Machine Learning** to build a heart disease prediction system.

The project starts with a real-world heart disease dataset and takes it through **database design, normalization, data processing, machine learning model training, evaluation and prediction on unseen data**. 🧠📊

Key Features ✨ 

- 🗄️ **MySQL Database Design**
- 🔗 **Entity Relationship (ER) Diagram**
- 📐 **Database Normalization — 1NF, 2NF & 3NF**
- 👤 **Patient, Clinical, ECG, Diagnosis & Risk Assessment entities**
- 📊 **Data Analysis & Visualization**
- 🧹 **Data Preprocessing & Missing Value Handling**
- 🔢 **Categorical Feature Encoding**
- 🤖 **Machine Learning Model Training**
- 🌲 **Random Forest Classification**
- 📈 **Model Evaluation & Confusion Matrix**
- 💾 **Trained Model Saved using Pickle**
- 🔮 **Prediction on Unseen User Input**
- 🔄 **Complete Database → ML → Prediction Workflow**

Technologies Used 🛠️ 

- **Python**
- **MySQL / MySQL Workbench**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Joblib**
- **CSV Dataset**

Database Design 🗃️ 

The database was designed and normalized to reduce redundancy and improve data organization.

Main entities include:

- 👤 Patient
- 🩺 Clinical Details
- ❤️ ECG Details
- 📋 Diagnosis
- ⚠️ Risk Assessment

The project also includes the database normalization process from **1NF to 3NF** and an **ER Diagram generated through MySQL Workbench reverse engineering**.

Machine Learning 🤖

The machine learning pipeline includes:

1. 📥 Loading the dataset
2. 🔍 Exploring the data
3. 📊 Visualizing important features
4. 🧹 Handling missing values
5. 🔢 Encoding categorical features
6. ✂️ Splitting data into training and testing sets
7. 🌳 Training multiple classification models
8. 📈 Evaluating model performance
9. 💾 Saving the trained Random Forest model
10. 🔮 Using the saved model for predictions on new data

The Random Forest model achieved an accuracy of approximately **88.59%** on the test data.

Project Files 📁 

```text
heartguard-dbml/
│
├── Abdul/                              # Project-related folder
├── templates/                          # Template files
│
├── app.py                              # Application code
├── train_model.py                      # Model training
├── inference.py                        # Prediction using trained model
├── random_forest_model.pkl             # Saved Random Forest model
│
├── heart.csv                           # Heart disease dataset
├── Updated_Features_Heart.csv          # Updated dataset
│
├── ER diagram of (Updated_Features_heart csv).png
├── Normalization (1NF, 2NF, 3NF).png
│
├── HeartFailure_Presentation.pptx      # Project presentation
├── ML model deployment (Code).docx     # ML deployment documentation
├── Adding Features to Dataset (queries).txt
│
├── Project Report.pdf                  # Complete project report
├── requirements.txt                    # Python dependencies
└── .gitignore
````

Project Report 📄 

A complete **PDF project report** is included in this repository.

**Project Report:** `Project Report.pdf` 📘 

The report documents the complete project journey, including:

* Dataset searching and selection
* Database design
* Entity identification
* Unnormalized table creation
* Additional feature creation
* Table implementation
* Data insertion
* 1NF, 2NF & 3NF normalization
* ER diagram through reverse engineering
* MySQL Workbench implementation
* CSV data export
* Machine learning model training
* Data visualization
* Model evaluation
* Confusion matrix
* Trained model saving
* Inference and prediction on unseen data
* Final project conclusion

Project Objective 🎯 

The main objective of this project is to demonstrate how **Database Systems and Machine Learning can work together in a single real-world application**.

It provides practical experience in designing a structured relational database while also building a machine learning pipeline capable of predicting heart disease based on patient-related features.

Dataset 📊 

The project uses a real-world heart disease dataset containing patient health and clinical features such as:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise Angina
* Oldpeak
* ST Slope
* Heart Disease

Disclaimer ⚠️ 

This project is developed for **academic and educational purposes**. The prediction produced by the machine learning model should not be considered a medical diagnosis or a replacement for professional medical advice.

If you find this project useful, feel free to explore the code, database design and machine learning workflow ⭐.

