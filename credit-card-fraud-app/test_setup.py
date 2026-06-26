"""
Test script to verify the Credit Card Fraud Detection application setup
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"✅ {description}: Found")
        return True
    else:
        print(f"❌ {description}: Not found")
        return False

def check_directory_exists(dirpath, description):
    """Check if a directory exists"""
    if os.path.isdir(dirpath):
        print(f"✅ {description}: Found")
        return True
    else:
        print(f"❌ {description}: Not found")
        return False

def check_dependencies():
    """Check if required Python packages are installed"""
    required_packages = [
        'flask',
        'pandas',
        'numpy',
        'sklearn',
        'imblearn',
        'matplotlib',
        'seaborn'
    ]
    
    print("\n📦 Checking Python Dependencies:")
    all_installed = True
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}: Installed")
        except ImportError:
            print(f"❌ {package}: Not installed")
            all_installed = False
    
    return all_installed

def main():
    print("="*60)
    print("Credit Card Fraud Detection - Setup Verification")
    print("="*60)
    
    # Check project structure
    print("\n📁 Checking Project Structure:")
    
    checks = [
        ('app.py', 'Main application file'),
        ('requirements.txt', 'Requirements file'),
        ('README.md', 'README file'),
        ('model/train_model.py', 'Training script'),
        ('templates/index.html', 'Home page template'),
        ('templates/dashboard.html', 'Dashboard template'),
        ('templates/predict.html', 'Prediction template'),
        ('static/css/style.css', 'CSS stylesheet'),
    ]
    
    structure_ok = True
    for filepath, description in checks:
        if not check_file_exists(filepath, description):
            structure_ok = False
    
    # Check directories
    print("\n📂 Checking Directories:")
    dirs = [
        ('model', 'Model directory'),
        ('templates', 'Templates directory'),
        ('static', 'Static directory'),
        ('static/css', 'CSS directory'),
        ('static/images', 'Images directory'),
        ('dataset', 'Dataset directory'),
    ]
    
    for dirpath, description in dirs:
        if not check_directory_exists(dirpath, description):
            structure_ok = False
    
    # Check dependencies
    deps_ok = check_dependencies()
    
    # Check dataset
    print("\n📊 Checking Dataset:")
    dataset_exists = check_file_exists('dataset/creditcard.csv', 'Dataset file')
    
    # Check trained models
    print("\n🤖 Checking Trained Models:")
    models_exist = (
        check_file_exists('model/model.pkl', 'Main model') and
        check_file_exists('model/scaler.pkl', 'Scaler') and
        check_file_exists('model/all_models.pkl', 'All models') and
        check_file_exists('model/results.pkl', 'Results')
    )
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    if structure_ok:
        print("✅ Project structure: OK")
    else:
        print("❌ Project structure: INCOMPLETE")
    
    if deps_ok:
        print("✅ Dependencies: OK")
    else:
        print("❌ Dependencies: MISSING (run: pip install -r requirements.txt)")
    
    if dataset_exists:
        print("✅ Dataset: OK")
    else:
        print("❌ Dataset: MISSING (download creditcard.csv to dataset/ folder)")
    
    if models_exist:
        print("✅ Trained models: OK")
    else:
        print("❌ Trained models: MISSING (run: python model/train_model.py)")
    
    print("\n" + "="*60)
    
    if structure_ok and deps_ok and dataset_exists and models_exist:
        print("🎉 All checks passed! You can run the application:")
        print("   python app.py")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print("\nQuick fix steps:")
        if not deps_ok:
            print("1. Install dependencies: pip install -r requirements.txt")
        if not dataset_exists:
            print("2. Download dataset to dataset/creditcard.csv")
        if not models_exist:
            print("3. Train models: cd model && python train_model.py && cd ..")
    
    print("="*60)

if __name__ == "__main__":
    main()
