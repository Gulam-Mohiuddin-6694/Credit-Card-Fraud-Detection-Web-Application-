# 🚀 Credit Card Fraud Detection Web Application

A complete end-to-end machine learning-powered web application for detecting fraudulent credit card transactions in real-time.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.2-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📌 Project Overview

This web application uses advanced machine learning algorithms to detect fraudulent credit card transactions. The system handles highly imbalanced datasets using techniques like SMOTE, Random Undersampling, and Class Weight Balancing. It provides real-time predictions through an intuitive web interface with comprehensive visualizations and model performance metrics.

### Key Features

- ✅ **Multiple ML Algorithms**: Logistic Regression and Random Forest Classifier
- ✅ **Imbalance Handling**: SMOTE, Random Undersampling, and Class Weight Balancing
- ✅ **Real-time Predictions**: Web-based interface for instant fraud detection
- ✅ **Comprehensive Metrics**: Accuracy, Precision, Recall, F1-Score, ROC-AUC
- ✅ **Interactive Visualizations**: Class distribution, ROC curves, confusion matrix, feature importance
- ✅ **Model Comparison**: Side-by-side performance comparison of all models
- ✅ **Responsive Design**: Mobile-friendly Bootstrap interface

## 📂 Project Structure

```
credit-card-fraud-app/
│
├── app.py                      # Flask application (main backend)
├── model/
│   ├── train_model.py          # ML model training script
│   ├── model.pkl               # Trained Random Forest model (generated)
│   ├── scaler.pkl              # Feature scaler (generated)
│   ├── all_models.pkl          # All trained models (generated)
│   ├── results.pkl             # Model evaluation results (generated)
│   └── feature_importance.csv  # Feature importance data (generated)
│
├── static/
│   ├── css/
│   │   └── style.css           # Custom CSS styles
│   └── images/                 # Visualizations (generated)
│       ├── class_distribution.png
│       ├── confusion_matrix.png
│       ├── roc_curves.png
│       └── feature_importance.png
│
├── templates/
│   ├── index.html              # Home page
│   ├── dashboard.html          # Dashboard with metrics and visualizations
│   └── predict.html            # Prediction page
│
├── dataset/
│   └── creditcard.csv          # Dataset (download separately)
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🧠 Machine Learning Models

### Models Implemented

1. **Logistic Regression** (with 4 variants)
   - Original (Imbalanced data)
   - SMOTE (Synthetic Minority Oversampling)
   - Random Undersampling
   - Class Weight Balancing

2. **Random Forest Classifier**
   - 100 decision trees
   - Balanced class weights
   - Feature importance analysis

### Imbalance Handling Techniques

- **SMOTE**: Generates synthetic samples for the minority class
- **Random Undersampling**: Reduces majority class samples
- **Class Weight Balancing**: Adjusts model weights based on class frequency

### Evaluation Metrics

- **Accuracy**: Overall correctness of predictions
- **Precision**: Accuracy of fraud predictions
- **Recall**: Ability to detect all frauds (most important for fraud detection)
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Model's discrimination ability
- **Confusion Matrix**: Detailed prediction breakdown

## 📊 Dataset

### Dataset Information

- **Source**: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **File**: `creditcard.csv`
- **Size**: 284,807 transactions
- **Features**: 30 (Time, V1-V28, Amount)
- **Target**: Class (0 = Legitimate, 1 = Fraud)
- **Imbalance**: Only 0.172% fraudulent transactions

### Features Description

- **Time**: Seconds elapsed between this transaction and the first transaction
- **V1-V28**: PCA-transformed features (anonymized for privacy)
- **Amount**: Transaction amount
- **Class**: Target variable (0 = Legitimate, 1 = Fraud)

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Step 1: Clone or Download the Project

```bash
# Option 1: Clone with Git
git clone <repository-url>
cd credit-card-fraud-app

# Option 2: Download and extract the ZIP file
```

### Step 2: Download the Dataset

1. Download the dataset from [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)
2. Place `creditcard.csv` in the `dataset/` folder

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Train the Models

```bash
cd model
python train_model.py
cd ..
```

This will:
- Load and preprocess the dataset
- Train multiple models with different imbalance handling techniques
- Generate evaluation metrics
- Save trained models and visualizations
- Create performance comparison reports

**Note**: Training may take 5-15 minutes depending on your system.

### Step 5: Run the Web Application

```bash
python app.py
```

The application will start at: `http://localhost:5000`

## 🌐 Using the Web Application

### Home Page (`/`)
- Project overview and features
- Dataset statistics
- Model information
- Navigation to other pages

### Dashboard (`/dashboard`)
- Model comparison metrics table
- Class distribution visualization
- ROC curves comparison
- Confusion matrix
- Feature importance analysis
- Key insights

### Prediction Page (`/predict`)
- Select ML model
- Enter transaction details (Time, V1-V28, Amount)
- Use sample data buttons for quick testing
- Get real-time fraud prediction
- View fraud probability scores

## 📈 Model Performance

### Expected Results

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression (Original) | ~0.999 | ~0.88 | ~0.61 | ~0.72 | ~0.97 |
| Logistic Regression (SMOTE) | ~0.974 | ~0.06 | ~0.92 | ~0.11 | ~0.97 |
| Logistic Regression (Undersampling) | ~0.976 | ~0.06 | ~0.91 | ~0.11 | ~0.97 |
| Logistic Regression (Weighted) | ~0.974 | ~0.06 | ~0.92 | ~0.11 | ~0.97 |
| Random Forest | ~0.999 | ~0.93 | ~0.76 | ~0.84 | ~0.98 |

**Note**: Actual results may vary slightly based on random state and system configuration.

### Why Recall is Important

In fraud detection, **Recall** is the most critical metric because:
- Missing a fraud (False Negative) is more costly than a false alarm (False Positive)
- High recall ensures we catch most fraudulent transactions
- Financial institutions prioritize catching fraud over minimizing false alarms

## 🚀 Deployment on AWS EC2

### Prerequisites

- AWS Account
- EC2 instance (Ubuntu 20.04 or later recommended)
- Security group with port 5000 open

### Deployment Steps

#### 1. Launch EC2 Instance

```bash
# Choose Ubuntu Server 20.04 LTS
# Instance type: t2.medium or higher (for model training)
# Configure security group to allow:
#   - SSH (port 22) from your IP
#   - Custom TCP (port 5000) from anywhere (0.0.0.0/0)
```

#### 2. Connect to EC2 Instance

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

#### 3. Install Dependencies

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3-pip python3-venv -y

# Install Git
sudo apt install git -y
```

#### 4. Clone Project and Setup

```bash
# Clone repository
git clone <repository-url>
cd credit-card-fraud-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

#### 5. Upload Dataset

```bash
# Option 1: Use SCP from local machine
scp -i your-key.pem creditcard.csv ubuntu@your-ec2-public-ip:~/credit-card-fraud-app/dataset/

# Option 2: Download directly on EC2
cd dataset
wget <dataset-url>
cd ..
```

#### 6. Train Models

```bash
cd model
python train_model.py
cd ..
```

#### 7. Run Application

```bash
# For testing
python app.py

# For production (using nohup)
nohup python app.py > app.log 2>&1 &
```

#### 8. Access Application

```
http://your-ec2-public-ip:5000
```

### Production Deployment (Optional)

For production, use **Gunicorn** and **Nginx**:

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Install and configure Nginx
sudo apt install nginx -y
# Configure Nginx as reverse proxy
```

## 🧪 Testing the Application

### Test with Sample Data

The prediction page includes two sample data buttons:

1. **Sample Legitimate**: Pre-filled with a legitimate transaction
2. **Sample Fraud**: Pre-filled with a fraudulent transaction

### Manual Testing

1. Navigate to `/predict`
2. Select a model
3. Enter transaction details
4. Click "Check Fraud"
5. Review the prediction and probability scores

### API Testing (Optional)

```bash
# Get model information
curl http://localhost:5000/api/model-info
```

## 📝 Model Explanation

### How It Works

1. **Data Preprocessing**
   - Load dataset
   - Handle missing values
   - Feature scaling using StandardScaler
   - Stratified train-test split (80-20)

2. **Imbalance Handling**
   - Apply SMOTE, undersampling, and class weighting
   - Compare performance of different techniques

3. **Model Training**
   - Train Logistic Regression and Random Forest
   - Use cross-validation for robust evaluation

4. **Evaluation**
   - Calculate comprehensive metrics
   - Generate visualizations
   - Compare model performance

5. **Prediction**
   - Load trained model and scaler
   - Scale input features
   - Make prediction with probability scores

### Feature Importance

The Random Forest model provides feature importance scores, showing which features (V1-V28, Time, Amount) contribute most to fraud detection.

## 🔧 Troubleshooting

### Common Issues

**Issue**: Models not loading
```bash
# Solution: Train models first
cd model
python train_model.py
cd ..
```

**Issue**: Dataset not found
```bash
# Solution: Ensure creditcard.csv is in dataset/ folder
ls dataset/creditcard.csv
```

**Issue**: Port 5000 already in use
```bash
# Solution: Change port in app.py
# Or kill the process using port 5000
lsof -ti:5000 | xargs kill -9  # Linux/Mac
netstat -ano | findstr :5000   # Windows
```

**Issue**: Visualizations not displaying
```bash
# Solution: Ensure matplotlib backend is set correctly
# Check static/images/ folder for generated images
ls static/images/
```

## 📸 Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Prediction Page
![Prediction](screenshots/predict.png)

**Note**: Add actual screenshots to the `screenshots/` folder.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Dataset: [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- Machine Learning: Scikit-learn, Imbalanced-learn
- Web Framework: Flask
- Frontend: Bootstrap 5

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Email: your.email@example.com

---

**⭐ If you find this project helpful, please give it a star!**
