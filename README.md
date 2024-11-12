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
![image](https://github.com/user-attachments/assets/5dde46af-1d30-4f95-9143-c92b6ee494fb)


---

## How to Use
### 1. Clone the Repository
```bash
git clone https://github.com/sersun/BankClientChurn.git
cd BankClientChurn

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Flask app
```bash
python deploy/API.py

### 4. Predict Using the API
Send a POST request to /predict/ with JSON input:

```json
{
  "CreditScore": 600,
  "Geography": "France",
  "Gender": "Male",
  "Age": 40,
  "Tenure": 5,
  "Balance": 50000,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 60000
}


