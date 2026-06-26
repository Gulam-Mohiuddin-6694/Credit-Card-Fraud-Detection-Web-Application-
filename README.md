📋 Project Summary – Credit Card Fraud Detection Web Application
🎯 Project Overview
A complete, production‑ready web application for detecting fraudulent credit card transactions using machine learning. Built with Flask, Scikit‑learn, and Bootstrap.

✅ Completed Components
1. Backend (Flask Application)
app.py – Main Flask app with routes:

/ Home page

/dashboard Dashboard

/predict Prediction

/api/model-info API endpoint

Error handling and logging

Model loading and prediction logic

Form validation and input processing

2. Machine Learning Pipeline
model/train_model.py – ML training pipeline:

Data loading & preprocessing

Feature scaling with StandardScaler

Stratified train‑test split (80‑20)

Imbalance handling: SMOTE, Random Undersampling, Class Weight Balancing

Models: Logistic Regression (4 variants), Random Forest Classifier

Evaluation metrics & visualization

Model persistence (pickle)

3. Frontend (HTML/CSS/Bootstrap)
templates/index.html – Home page

templates/dashboard.html – Analytics dashboard

templates/predict.html – Prediction interface

static/css/style.css – Custom styling (responsive, modern UI, animations)

4. Documentation
README.md – Comprehensive documentation

QUICKSTART.md – Quick setup guide

AWS_DEPLOYMENT.md – AWS EC2 deployment guide

dataset/README.md – Dataset instructions

5. Utilities
requirements.txt – Python dependencies

.gitignore – Git ignore rules

test_setup.py – Setup verification script

generate_sample_data.py – Sample data generator

📊 Machine Learning Features
Models Implemented
Logistic Regression (4 variants: Original, SMOTE, Undersampling, Class Weight Balancing)

Random Forest (100 estimators, balanced class weights, feature importance analysis)

Evaluation Metrics
Accuracy, Precision, Recall, F1‑Score

ROC‑AUC Score, Confusion Matrix, ROC Curves

Visualizations
Class distribution chart

ROC curves comparison

Confusion matrix heatmap

Feature importance chart (top 15)

🌐 Web Application Features
Home Page
Project description

Dataset overview with statistics

Model information & highlights

Dashboard
Model comparison metrics table

Interactive visualizations

Performance analysis & insights

Prediction Page
Model selection dropdown

Input form for 30 features (Time, V1–V28, Amount)

Sample data buttons (legit & fraud)

Real‑time prediction results with fraud probability visualization

🛠️ Technical Stack
Backend

Flask 3.0.0

scikit‑learn 1.3.2

imbalanced‑learn 0.11.0

pandas 2.1.4, numpy 1.26.2

matplotlib 3.8.2, seaborn 0.13.0

Frontend

Bootstrap 5.3.0

Font Awesome 6.4.0

Custom CSS with animations

Deployment

Local: Python + Flask dev server

Production: Gunicorn + Nginx (optional)

Cloud: AWS EC2 (documented)

📁 Project Structure
Code
credit-card-fraud-app/
├── app.py
├── requirements.txt
├── README.md
├── QUICKSTART.md
├── AWS_DEPLOYMENT.md
├── test_setup.py
├── generate_sample_data.py
├── .gitignore
│
├── model/
│   ├── train_model.py
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── all_models.pkl
│   ├── results.pkl
│   └── feature_importance.csv
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── predict.html
│
├── static/
│   ├── css/style.css
│   └── images/
│       ├── class_distribution.png
│       ├── confusion_matrix.png
│       ├── roc_curves.png
│       └── feature_importance.png
│
└── dataset/
    ├── README.md
    └── creditcard.csv
🚀 Setup Instructions
Install dependencies

bash
pip install -r requirements.txt
Download dataset

From: https://www.kaggle.com/mlg-ulb/creditcardfraud

Place in: dataset/creditcard.csv

Train models

bash
cd model
python train_model.py
cd ..
Run application

bash
python app.py
Open browser  
Navigate to: http://localhost:5000

Verification

bash
python test_setup.py
