# 🚀 Quick Start Guide

## Prerequisites
- Python 3.8+
- pip

## Setup Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download Dataset
- Go to: https://www.kaggle.com/mlg-ulb/creditcardfraud
- Download `creditcard.csv`
- Place it in the `dataset/` folder

### 3. Train Models
```bash
cd model
python train_model.py
cd ..
```
⏱️ This will take 5-15 minutes

### 4. Run Application
```bash
python app.py
```

### 5. Open Browser
Navigate to: `http://localhost:5000`

## Quick Test

1. Go to **Predict** page
2. Click **"Sample Fraud"** button
3. Click **"Check Fraud"**
4. See the prediction result!

## Troubleshooting

**Models not found?**
```bash
cd model
python train_model.py
cd ..
```

**Port 5000 in use?**
- Edit `app.py` and change the port number

**Dataset not found?**
- Ensure `creditcard.csv` is in `dataset/` folder

## Project Structure
```
credit-card-fraud-app/
├── app.py              # Run this to start the web app
├── model/
│   └── train_model.py  # Run this first to train models
├── dataset/
│   └── creditcard.csv  # Download and place here
├── templates/          # HTML files
├── static/             # CSS and images
└── requirements.txt    # Dependencies
```

## Features

✅ Multiple ML models comparison
✅ Real-time fraud detection
✅ Interactive visualizations
✅ Model performance metrics
✅ Sample data for testing

## Need Help?

Check the full README.md for detailed documentation.

---
**Happy Fraud Detecting! 🛡️**
