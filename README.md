# BankClientChurn

## Project Overview
This project focuses on the exploratory data analysis (EDA) and predictive modeling of customer churn for a bank's client dataset. The primary goal is to analyze customer behavior and develop a machine learning model to predict whether a client will leave the bank (churn). The repository includes detailed data exploration, feature engineering, and model building steps to provide actionable insights and accurate predictions.

---

## Key Features
- **Exploratory Data Analysis (EDA):**
  - Comprehensive visualization and statistical analysis of client data.
  - Identification of key factors influencing customer churn.
- **Machine Learning Modeling:**
  - Balanced and unbalanced data experiments to optimize prediction accuracy.
  - Random Forest Classifier implementation with evaluation metrics such as accuracy, ROC-AUC, precision, and recall.
- **API Development:**
  - A FastAPI and Flask application to deploy the trained model for real-world usage.
  - Support for real-time predictions via HTTP endpoints.
- **Visualization:**
  - Lift Curve, ROC Curve, Precision-Recall Curve, and feature importance visualizations.

---

## Repository Structure


BankClientChurn/
├── data/                           # Contains raw and processed datasets
│   ├── Churn_Modeling.csv          # Original dataset
│   ├── ModelingDataSet.csv.csv     # Cleaned and prepared dataset
├── deploy/                         # Scripts for model deployment
│   ├── API.py                      # Flask-based API implementation
|   ├── data.json                   # Structure of JSON file for use in deployment
|   ├── Test deployment of our models.pdf # Result of API testing
├── models/                         # Trained models and saved artifacts
│   └── random_forest_model.pkl     # Pickled Random Forest model
├── PrimaryAnalysing_EDA.ipynb      # EDA and feature exploration
├── ModelingClientChurn.ipynb       # Model training and evaluation
├── exportToHTML/                   # Exported HTML and PDF versions of notebooks (optional)
├── requirements.txt                # List of Python dependencies
└── README.md                       # Project overview and description
