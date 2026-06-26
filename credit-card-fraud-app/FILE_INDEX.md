# 📚 Project File Index

Complete reference guide for all files in the Credit Card Fraud Detection Web Application.

## 🎯 Core Application Files

### `app.py`
**Purpose:** Main Flask application (Backend)
**Contains:**
- Flask routes (/, /dashboard, /predict)
- Model loading logic
- Prediction endpoint
- Error handling
- API endpoints

**Usage:** `python app.py`

---

### `requirements.txt`
**Purpose:** Python dependencies
**Contains:**
- Flask 3.0.0
- pandas 2.1.4
- numpy 1.26.2
- scikit-learn 1.3.2
- imbalanced-learn 0.11.0
- matplotlib 3.8.2
- seaborn 0.13.0

**Usage:** `pip install -r requirements.txt`

---

## 🤖 Machine Learning Files

### `model/train_model.py`
**Purpose:** ML model training pipeline
**Contains:**
- Data loading and preprocessing
- Feature scaling
- Imbalance handling (SMOTE, undersampling, weighting)
- Model training (Logistic Regression, Random Forest)
- Evaluation metrics calculation
- Visualization generation
- Model persistence

**Usage:** `cd model && python train_model.py && cd ..`

**Generates:**
- `model/model.pkl` - Trained Random Forest model
- `model/scaler.pkl` - StandardScaler for features
- `model/all_models.pkl` - All trained models
- `model/results.pkl` - Evaluation results
- `model/feature_importance.csv` - Feature importance data
- `static/images/*.png` - Visualization images

---

## 🌐 Frontend Files

### `templates/index.html`
**Purpose:** Home page
**Contains:**
- Project overview
- Dataset statistics
- Feature highlights
- Model information
- Navigation menu

**Route:** `/`

---

### `templates/dashboard.html`
**Purpose:** Analytics dashboard
**Contains:**
- Model comparison table
- Class distribution chart
- ROC curves comparison
- Confusion matrix
- Feature importance visualization
- Key insights

**Route:** `/dashboard`

---

### `templates/predict.html`
**Purpose:** Prediction interface
**Contains:**
- Model selection dropdown
- Input form (30 features)
- Sample data buttons
- Prediction result display
- Probability visualization

**Route:** `/predict`

---

### `static/css/style.css`
**Purpose:** Custom styling
**Contains:**
- Responsive design rules
- Component styles
- Animations
- Color schemes
- Mobile optimizations

---

## 📖 Documentation Files

### `README.md`
**Purpose:** Main documentation
**Contains:**
- Project overview
- Installation instructions
- Usage guide
- Model explanation
- Dataset information
- Deployment instructions
- Troubleshooting basics

**Audience:** All users

---

### `QUICKSTART.md`
**Purpose:** Quick setup guide
**Contains:**
- 5-step setup process
- Quick test instructions
- Common commands
- Troubleshooting tips

**Audience:** New users wanting fast setup

---

### `AWS_DEPLOYMENT.md`
**Purpose:** AWS EC2 deployment guide
**Contains:**
- EC2 instance setup
- Security group configuration
- Application deployment
- Production setup (Gunicorn, Nginx)
- Auto-start configuration
- Monitoring and maintenance

**Audience:** Users deploying to AWS

---

### `TROUBLESHOOTING.md`
**Purpose:** Problem-solving guide
**Contains:**
- Common issues and solutions
- Installation problems
- Runtime errors
- Deployment issues
- Debug techniques

**Audience:** Users facing issues

---

### `PROJECT_SUMMARY.md`
**Purpose:** Complete project overview
**Contains:**
- All implemented features
- Technical stack
- Project structure
- Performance metrics
- Workflow description
- Best practices

**Audience:** Reviewers, developers

---

### `dataset/README.md`
**Purpose:** Dataset instructions
**Contains:**
- Download instructions
- Dataset information
- File placement guide

**Audience:** Users setting up dataset

---

## 🛠️ Utility Files

### `test_setup.py`
**Purpose:** Setup verification script
**Contains:**
- File structure checks
- Dependency verification
- Dataset validation
- Model existence checks
- Summary report

**Usage:** `python test_setup.py`

**Output:** Verification report with ✅/❌ status

---

### `generate_sample_data.py`
**Purpose:** Sample data generator
**Contains:**
- Synthetic data generation
- Sample transaction creation
- Quick testing data

**Usage:** `python generate_sample_data.py`

**Output:** `dataset/creditcard_sample.csv`

**Use Case:** Testing without full dataset

---

### `run.bat`
**Purpose:** Windows run script
**Contains:**
- Virtual environment activation
- Application startup
- User-friendly messages

**Usage:** Double-click or `run.bat`

**Platform:** Windows

---

### `run.sh`
**Purpose:** Linux/Mac run script
**Contains:**
- Virtual environment activation
- Application startup
- User-friendly messages

**Usage:** `./run.sh` or `bash run.sh`

**Platform:** Linux/Mac

**Note:** Make executable: `chmod +x run.sh`

---

### `.gitignore`
**Purpose:** Git ignore rules
**Contains:**
- Python cache files
- Virtual environments
- Generated models (*.pkl)
- Dataset files (*.csv)
- Log files
- IDE files

**Usage:** Automatic with Git

---

## 📁 Directory Structure

### `model/`
**Purpose:** ML model files
**Contains:**
- Training script
- Generated model files (*.pkl)
- Feature importance data

---

### `templates/`
**Purpose:** HTML templates
**Contains:**
- index.html (Home)
- dashboard.html (Dashboard)
- predict.html (Prediction)

---

### `static/`
**Purpose:** Static assets
**Subdirectories:**
- `css/` - Stylesheets
- `images/` - Generated visualizations

---

### `dataset/`
**Purpose:** Dataset storage
**Contains:**
- README.md (instructions)
- creditcard.csv (download separately)

---

## 🔄 File Generation Flow

### Initial Setup
1. Download `creditcard.csv` → `dataset/`
2. Run `pip install -r requirements.txt`

### Training Phase
3. Run `python model/train_model.py`
   - Generates: `model/*.pkl`
   - Generates: `static/images/*.png`
   - Generates: `model/feature_importance.csv`

### Runtime Phase
4. Run `python app.py`
   - Loads: `model/*.pkl`
   - Serves: `templates/*.html`
   - Serves: `static/css/style.css`
   - Displays: `static/images/*.png`

---

## 📊 Generated Files (Not in Repository)

These files are created during training:

### Model Files
- `model/model.pkl` (~10 MB) - Main Random Forest model
- `model/scaler.pkl` (~1 KB) - Feature scaler
- `model/all_models.pkl` (~50 MB) - All trained models
- `model/results.pkl` (~10 KB) - Evaluation results
- `model/feature_importance.csv` (~1 KB) - Feature data

### Visualization Files
- `static/images/class_distribution.png` - Bar chart
- `static/images/confusion_matrix.png` - Heatmap
- `static/images/roc_curves.png` - Line plot
- `static/images/feature_importance.png` - Horizontal bar chart

### Log Files
- `app.log` - Application logs (if configured)
- `gunicorn.log` - Gunicorn logs (if using Gunicorn)

---

## 📝 File Sizes (Approximate)

| File | Size |
|------|------|
| app.py | 5 KB |
| model/train_model.py | 8 KB |
| requirements.txt | 1 KB |
| templates/*.html | 10-15 KB each |
| static/css/style.css | 6 KB |
| README.md | 15 KB |
| AWS_DEPLOYMENT.md | 10 KB |
| TROUBLESHOOTING.md | 12 KB |
| **Generated Files** | |
| model/model.pkl | ~10 MB |
| model/all_models.pkl | ~50 MB |
| static/images/*.png | ~100-500 KB each |
| **Dataset** | |
| creditcard.csv | ~150 MB |

---

## 🎯 Quick Reference

### To Setup:
1. `pip install -r requirements.txt`
2. Download dataset to `dataset/`
3. `cd model && python train_model.py && cd ..`

### To Run:
- `python app.py`
- Or: `run.bat` (Windows)
- Or: `./run.sh` (Linux/Mac)

### To Verify:
- `python test_setup.py`

### To Deploy:
- See `AWS_DEPLOYMENT.md`

### To Troubleshoot:
- See `TROUBLESHOOTING.md`

---

## 📚 Documentation Reading Order

### For New Users:
1. `README.md` - Overview
2. `QUICKSTART.md` - Setup
3. `TROUBLESHOOTING.md` - If issues

### For Deployment:
1. `README.md` - Basics
2. `AWS_DEPLOYMENT.md` - AWS setup
3. `TROUBLESHOOTING.md` - Issues

### For Development:
1. `PROJECT_SUMMARY.md` - Complete overview
2. `README.md` - Details
3. Code files - Implementation

### For Review:
1. `PROJECT_SUMMARY.md` - Quick overview
2. `README.md` - Full documentation
3. Code files - Verification

---

## 🔍 Finding Specific Information

| Need | File |
|------|------|
| Installation | README.md, QUICKSTART.md |
| Usage | README.md, QUICKSTART.md |
| Deployment | AWS_DEPLOYMENT.md |
| Troubleshooting | TROUBLESHOOTING.md |
| Project overview | PROJECT_SUMMARY.md |
| Dataset info | dataset/README.md |
| Model details | README.md, PROJECT_SUMMARY.md |
| API info | README.md (Model Explanation) |
| Performance | PROJECT_SUMMARY.md |

---

## ✅ Checklist for Complete Setup

- [ ] All core files present
- [ ] Dependencies installed (`requirements.txt`)
- [ ] Dataset downloaded (`dataset/creditcard.csv`)
- [ ] Models trained (`model/*.pkl` exist)
- [ ] Visualizations generated (`static/images/*.png` exist)
- [ ] Application runs (`python app.py` works)
- [ ] All pages accessible (/, /dashboard, /predict)
- [ ] Predictions working

**Verify with:** `python test_setup.py`

---

**This index provides a complete reference for all project files and their purposes.** 📚
