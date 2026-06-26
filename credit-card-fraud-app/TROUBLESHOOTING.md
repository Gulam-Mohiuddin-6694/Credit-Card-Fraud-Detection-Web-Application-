# 🔧 Troubleshooting Guide

Common issues and their solutions for the Credit Card Fraud Detection Web Application.

## 📋 Table of Contents
1. [Installation Issues](#installation-issues)
2. [Dataset Issues](#dataset-issues)
3. [Model Training Issues](#model-training-issues)
4. [Application Runtime Issues](#application-runtime-issues)
5. [Prediction Issues](#prediction-issues)
6. [Deployment Issues](#deployment-issues)

---

## Installation Issues

### Issue: pip install fails
```
ERROR: Could not find a version that satisfies the requirement...
```

**Solution:**
```bash
# Update pip
python -m pip install --upgrade pip

# Install with specific versions
pip install -r requirements.txt --no-cache-dir

# Or install individually
pip install Flask pandas numpy scikit-learn imbalanced-learn matplotlib seaborn
```

### Issue: Python version incompatibility
```
ERROR: Package requires Python >=3.8
```

**Solution:**
```bash
# Check Python version
python --version

# Install Python 3.8 or higher
# Download from: https://www.python.org/downloads/
```

### Issue: Permission denied during installation
```
ERROR: Could not install packages due to an EnvironmentError
```

**Solution:**
```bash
# Use --user flag
pip install -r requirements.txt --user

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

## Dataset Issues

### Issue: Dataset file not found
```
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/creditcard.csv'
```

**Solution:**
1. Download dataset from: https://www.kaggle.com/mlg-ulb/creditcardfraud
2. Place `creditcard.csv` in the `dataset/` folder
3. Verify: `ls dataset/creditcard.csv` (Linux/Mac) or `dir dataset\creditcard.csv` (Windows)

### Issue: Dataset is corrupted or incomplete
```
ParserError: Error tokenizing data
```

**Solution:**
```bash
# Re-download the dataset
# Verify file size (should be ~150 MB)

# Check file integrity
python -c "import pandas as pd; df = pd.read_csv('dataset/creditcard.csv'); print(df.shape)"
# Expected output: (284807, 31)
```

### Issue: Out of memory when loading dataset
```
MemoryError: Unable to allocate array
```

**Solution:**
```bash
# Use chunked reading (modify train_model.py)
# Or increase system RAM
# Or use a smaller sample:
python generate_sample_data.py
```

---

## Model Training Issues

### Issue: Training script not found
```
python: can't open file 'train_model.py': [Errno 2] No such file or directory
```

**Solution:**
```bash
# Make sure you're in the model directory
cd model
python train_model.py
cd ..
```

### Issue: Training takes too long
```
Training is running for more than 30 minutes...
```

**Solution:**
- This is normal for large datasets
- Expected time: 5-15 minutes on modern hardware
- For faster training, reduce n_estimators in Random Forest
- Or use sample data: `python generate_sample_data.py`

### Issue: SMOTE fails with memory error
```
MemoryError during SMOTE resampling
```

**Solution:**
```python
# Modify train_model.py
# Reduce sampling_strategy
smote = SMOTE(random_state=42, sampling_strategy=0.5)
```

### Issue: Models not saving
```
PermissionError: [Errno 13] Permission denied: 'model/model.pkl'
```

**Solution:**
```bash
# Check write permissions
chmod 755 model/  # Linux/Mac

# Or run as administrator (Windows)
# Or change save location
```

---

## Application Runtime Issues

### Issue: Flask app won't start
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
# Install Flask
pip install Flask

# Or install all requirements
pip install -r requirements.txt
```

### Issue: Port 5000 already in use
```
OSError: [Errno 48] Address already in use
```

**Solution:**
```bash
# Option 1: Kill process using port 5000
# Linux/Mac:
lsof -ti:5000 | xargs kill -9

# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Option 2: Change port in app.py
# Change: app.run(debug=True, host='0.0.0.0', port=5000)
# To:     app.run(debug=True, host='0.0.0.0', port=8080)
```

### Issue: Models not loading
```
FileNotFoundError: [Errno 2] No such file or directory: 'model/model.pkl'
```

**Solution:**
```bash
# Train models first
cd model
python train_model.py
cd ..

# Verify models exist
ls model/*.pkl  # Linux/Mac
dir model\*.pkl # Windows
```

### Issue: Templates not found
```
jinja2.exceptions.TemplateNotFound: index.html
```

**Solution:**
```bash
# Verify templates exist
ls templates/  # Linux/Mac
dir templates\ # Windows

# Make sure you're running from project root
cd credit-card-fraud-app
python app.py
```

### Issue: Static files (CSS/images) not loading
```
404 Not Found - /static/css/style.css
```

**Solution:**
```bash
# Verify static files exist
ls static/css/style.css

# Clear browser cache (Ctrl+F5)

# Check Flask static folder configuration in app.py
```

---

## Prediction Issues

### Issue: Prediction returns error
```
ValueError: could not convert string to float
```

**Solution:**
- Ensure all input fields are filled
- Use numeric values only
- Check for special characters
- Use sample data buttons to test

### Issue: All predictions show "Legitimate"
```
Model always predicts class 0
```

**Solution:**
- Model might not be trained properly
- Retrain with balanced data:
```bash
cd model
python train_model.py
cd ..
```
- Try different model from dropdown
- Use "Sample Fraud" button to test

### Issue: Probability scores don't make sense
```
Fraud probability: 0.00%
```

**Solution:**
- Check if scaler is loaded correctly
- Verify input values are in correct range
- Retrain models if necessary

---

## Deployment Issues

### Issue: AWS EC2 connection refused
```
Connection refused when accessing http://EC2_IP:5000
```

**Solution:**
```bash
# Check security group rules
# Ensure port 5000 is open (0.0.0.0/0)

# Check if app is running
ps aux | grep app.py

# Check firewall
sudo ufw status
sudo ufw allow 5000
```

### Issue: Application crashes on EC2
```
Killed
```

**Solution:**
```bash
# Out of memory - add swap space
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Or use larger instance type (t2.medium)
```

### Issue: Gunicorn won't start
```
gunicorn: command not found
```

**Solution:**
```bash
# Install gunicorn
pip install gunicorn

# Verify installation
gunicorn --version
```

---

## General Debugging

### Enable Debug Mode
```python
# In app.py, ensure debug=True for development
app.run(debug=True, host='0.0.0.0', port=5000)
```

### Check Logs
```bash
# View application logs
tail -f app.log

# Check Python errors
python app.py 2>&1 | tee error.log
```

### Verify Setup
```bash
# Run setup verification script
python test_setup.py
```

### Test Individual Components

**Test imports:**
```python
python -c "import flask, pandas, sklearn, imblearn; print('All imports OK')"
```

**Test model loading:**
```python
python -c "import pickle; model = pickle.load(open('model/model.pkl', 'rb')); print('Model loaded OK')"
```

**Test dataset:**
```python
python -c "import pandas as pd; df = pd.read_csv('dataset/creditcard.csv'); print(f'Dataset shape: {df.shape}')"
```

---

## Performance Issues

### Issue: Application is slow
**Solution:**
- Use Gunicorn with multiple workers
- Enable caching
- Optimize model (reduce n_estimators)
- Use faster instance type

### Issue: High memory usage
**Solution:**
- Use smaller model
- Reduce batch size
- Clear unused variables
- Use generator for large datasets

---

## Browser Issues

### Issue: Page not loading
**Solution:**
- Clear browser cache (Ctrl+Shift+Delete)
- Try different browser
- Check browser console for errors (F12)
- Disable browser extensions

### Issue: CSS not applying
**Solution:**
- Hard refresh (Ctrl+F5)
- Check static files path
- Verify CSS file exists
- Check browser console for 404 errors

---

## Quick Fixes

### Reset Everything
```bash
# Stop application
# Ctrl+C or kill process

# Remove generated files
rm model/*.pkl
rm static/images/*.png

# Retrain
cd model
python train_model.py
cd ..

# Restart
python app.py
```

### Fresh Installation
```bash
# Create new virtual environment
python -m venv venv_new
source venv_new/bin/activate  # Linux/Mac
venv_new\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Train and run
cd model && python train_model.py && cd ..
python app.py
```

---

## Still Having Issues?

1. **Run verification script:**
   ```bash
   python test_setup.py
   ```

2. **Check documentation:**
   - README.md
   - QUICKSTART.md
   - AWS_DEPLOYMENT.md

3. **Generate sample data for testing:**
   ```bash
   python generate_sample_data.py
   ```

4. **Check system requirements:**
   - Python 3.8+
   - 4GB RAM minimum
   - 1GB free disk space

5. **Common command sequence:**
   ```bash
   pip install -r requirements.txt
   cd model && python train_model.py && cd ..
   python app.py
   ```

---

## Contact & Support

If you're still experiencing issues:
- Check error messages carefully
- Search for similar issues online
- Review the complete error traceback
- Ensure all prerequisites are met

**Remember:** Most issues are due to:
1. Missing dependencies
2. Dataset not downloaded
3. Models not trained
4. Wrong directory when running commands

---

**Happy Debugging! 🔧**
