# 🚀 Getting Started Guide

**Complete step-by-step guide to set up and run the Credit Card Fraud Detection Web Application**

---

## 📋 Prerequisites Checklist

Before you begin, ensure you have:

- [ ] **Python 3.8 or higher** installed
  - Check: `python --version` or `python3 --version`
  - Download: https://www.python.org/downloads/

- [ ] **pip** (Python package manager) installed
  - Check: `pip --version` or `pip3 --version`
  - Usually comes with Python

- [ ] **Internet connection** for downloading packages and dataset

- [ ] **4GB RAM minimum** (8GB recommended)

- [ ] **1GB free disk space** (for dataset and models)

---

## 🎯 Step-by-Step Setup

### Step 1: Navigate to Project Directory

Open your terminal/command prompt and navigate to the project folder:

```bash
cd "c:\Users\gulam\OneDrive\Desktop\DA PBL\credit-card-fraud-app"
```

**Verify you're in the right place:**
```bash
# Windows
dir

# Linux/Mac
ls
```

You should see files like `app.py`, `requirements.txt`, etc.

---

### Step 2: Create Virtual Environment (Recommended)

**Why?** Keeps project dependencies isolated from your system Python.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**You'll know it worked when you see `(venv)` in your terminal prompt.**

**To deactivate later:** Type `deactivate`

---

### Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

**This will install:**
- Flask (web framework)
- pandas (data processing)
- numpy (numerical computing)
- scikit-learn (machine learning)
- imbalanced-learn (handling imbalanced data)
- matplotlib (visualization)
- seaborn (statistical visualization)

**Expected time:** 2-5 minutes

**Verify installation:**
```bash
python test_setup.py
```

---

### Step 4: Download Dataset

**Option A: Download from Kaggle (Recommended)**

1. Go to: https://www.kaggle.com/mlg-ulb/creditcardfraud
2. Click "Download" (you may need to create a free Kaggle account)
3. Extract the ZIP file
4. Copy `creditcard.csv` to the `dataset/` folder in your project

**Option B: Use Sample Data (For Quick Testing)**

```bash
python generate_sample_data.py
cd dataset
ren creditcard_sample.csv creditcard.csv
cd ..
```

**Note:** Sample data is for testing only. Use real data for accurate results.

**Verify dataset:**
```bash
# Windows
dir dataset\creditcard.csv

# Linux/Mac
ls dataset/creditcard.csv
```

---

### Step 5: Train Machine Learning Models

Navigate to the model directory and run the training script:

```bash
cd model
python train_model.py
```

**What happens:**
- Loads the dataset
- Preprocesses data (scaling, splitting)
- Handles class imbalance (SMOTE, undersampling, weighting)
- Trains multiple models (Logistic Regression, Random Forest)
- Evaluates models (accuracy, precision, recall, F1, ROC-AUC)
- Generates visualizations
- Saves trained models

**Expected time:** 5-15 minutes (depending on your computer)

**You'll see output like:**
```
Loading dataset...
Dataset shape: (284807, 31)
Preprocessing data...
Training on original imbalanced data...
Applying SMOTE...
Training Random Forest...
Saving models...
✅ Training completed successfully!
```

**Return to project root:**
```bash
cd ..
```

**Verify models were created:**
```bash
# Windows
dir model\*.pkl

# Linux/Mac
ls model/*.pkl
```

You should see:
- `model.pkl`
- `scaler.pkl`
- `all_models.pkl`
- `results.pkl`

---

### Step 6: Run the Web Application

Start the Flask application:

```bash
python app.py
```

**You'll see output like:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

**The application is now running!**

---

### Step 7: Access the Application

Open your web browser and go to:

```
http://localhost:5000
```

**Or:**
```
http://127.0.0.1:5000
```

**You should see the home page of the Credit Card Fraud Detection application!**

---

## 🎮 Using the Application

### Home Page (`/`)

**What you'll see:**
- Project overview
- Dataset statistics
- Model information
- Feature highlights

**What to do:**
- Read the overview
- Click "View Dashboard" or "Check Transaction"

---

### Dashboard Page (`/dashboard`)

**What you'll see:**
- Model comparison table
- Class distribution chart
- ROC curves comparison
- Confusion matrix
- Feature importance visualization

**What to do:**
- Review model performance metrics
- Compare different models
- Analyze visualizations
- Understand which model performs best

**Key metric to watch:** **Recall** (most important for fraud detection)

---

### Prediction Page (`/predict`)

**What you'll see:**
- Model selection dropdown
- Input form with 30 fields (Time, V1-V28, Amount)
- Sample data buttons
- Prediction result area

**How to make a prediction:**

1. **Select a model** from the dropdown (default: Random Forest)

2. **Enter transaction details:**
   - **Time**: Seconds since first transaction (e.g., 406)
   - **V1-V28**: PCA-transformed features (e.g., -1.359807)
   - **Amount**: Transaction amount in dollars (e.g., 100.00)

3. **Or use sample data:**
   - Click "Sample Legitimate" for a legit transaction
   - Click "Sample Fraud" for a fraudulent transaction

4. **Click "Check Fraud"**

5. **View results:**
   - Prediction: Fraudulent or Legitimate
   - Fraud probability (%)
   - Legitimate probability (%)
   - Model used

---

## 🧪 Testing the Application

### Quick Test 1: Sample Legitimate Transaction

1. Go to `/predict`
2. Click "Sample Legitimate"
3. Click "Check Fraud"
4. **Expected result:** "Legitimate" with high legitimate probability

### Quick Test 2: Sample Fraudulent Transaction

1. Go to `/predict`
2. Click "Sample Fraud"
3. Click "Check Fraud"
4. **Expected result:** "Fraudulent" with high fraud probability

### Quick Test 3: Different Models

1. Go to `/predict`
2. Click "Sample Fraud"
3. Select different models from dropdown
4. Click "Check Fraud" for each
5. Compare results across models

---

## 🛑 Stopping the Application

To stop the Flask server:

**Press:** `Ctrl + C` in the terminal

**You'll see:**
```
KeyboardInterrupt
```

The application will stop.

---

## 🔄 Restarting the Application

To restart:

```bash
python app.py
```

**Note:** Models are saved, so you don't need to retrain unless you want to update them.

---

## ✅ Verification Checklist

Run the verification script to check everything:

```bash
python test_setup.py
```

**Expected output:**
```
✅ Project structure: OK
✅ Dependencies: OK
✅ Dataset: OK
✅ Trained models: OK
🎉 All checks passed!
```

---

## 🚨 Common Issues & Quick Fixes

### Issue 1: "Module not found" error

**Fix:**
```bash
pip install -r requirements.txt
```

### Issue 2: "Dataset not found" error

**Fix:**
- Download `creditcard.csv` to `dataset/` folder
- Or run: `python generate_sample_data.py`

### Issue 3: "Models not found" error

**Fix:**
```bash
cd model
python train_model.py
cd ..
```

### Issue 4: "Port 5000 already in use"

**Fix:**
```bash
# Kill the process using port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac:
lsof -ti:5000 | xargs kill -9
```

### Issue 5: Application won't start

**Fix:**
1. Check Python version: `python --version` (must be 3.8+)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check you're in the right directory
4. Run verification: `python test_setup.py`

**For more issues, see:** `TROUBLESHOOTING.md`

---

## 📚 Next Steps

### Learn More
- Read `README.md` for detailed documentation
- Check `PROJECT_SUMMARY.md` for complete overview
- Review `FILE_INDEX.md` to understand all files

### Deploy to Production
- Follow `AWS_DEPLOYMENT.md` for AWS EC2 deployment
- Use Gunicorn for production server
- Configure Nginx as reverse proxy

### Customize
- Modify `templates/*.html` for UI changes
- Edit `static/css/style.css` for styling
- Update `model/train_model.py` for different models
- Adjust `app.py` for new features

---

## 🎓 Understanding the Workflow

```
1. User visits website
   ↓
2. Views home page with project info
   ↓
3. Explores dashboard with model metrics
   ↓
4. Goes to prediction page
   ↓
5. Enters transaction details (or uses sample data)
   ↓
6. Selects ML model
   ↓
7. Clicks "Check Fraud"
   ↓
8. Backend loads model and scaler
   ↓
9. Scales input features
   ↓
10. Makes prediction
   ↓
11. Returns result with probability
   ↓
12. User sees: Fraudulent or Legitimate
```

---

## 💡 Tips for Best Experience

1. **Use Chrome or Firefox** for best compatibility
2. **Clear browser cache** if CSS doesn't load (Ctrl+F5)
3. **Use sample data buttons** for quick testing
4. **Try different models** to compare results
5. **Check dashboard** to understand model performance
6. **Read the metrics** to understand why recall is important

---

## 🎯 Success Criteria

You've successfully set up the application when:

- ✅ Application runs without errors
- ✅ All three pages load (Home, Dashboard, Predict)
- ✅ Visualizations appear on dashboard
- ✅ Predictions work on predict page
- ✅ Sample data buttons work
- ✅ Results show fraud probability

---

## 📞 Getting Help

If you're stuck:

1. **Run verification:** `python test_setup.py`
2. **Check troubleshooting:** `TROUBLESHOOTING.md`
3. **Read documentation:** `README.md`
4. **Review error messages** carefully
5. **Check you followed all steps** in order

---

## 🎉 Congratulations!

You've successfully set up and run the Credit Card Fraud Detection Web Application!

**What you can do now:**
- ✅ Detect fraudulent transactions in real-time
- ✅ Compare multiple ML models
- ✅ Analyze model performance
- ✅ Visualize data and results
- ✅ Deploy to production (AWS EC2)

**Enjoy exploring the application!** 🚀

---

## 📖 Quick Command Reference

```bash
# Setup
pip install -r requirements.txt
python generate_sample_data.py  # Optional

# Train
cd model && python train_model.py && cd ..

# Run
python app.py

# Verify
python test_setup.py

# Stop
Ctrl + C
```

---

**For detailed information, see:**
- `README.md` - Complete documentation
- `QUICKSTART.md` - Quick setup
- `TROUBLESHOOTING.md` - Problem solving
- `AWS_DEPLOYMENT.md` - Cloud deployment

**Happy Fraud Detecting! 🛡️**
