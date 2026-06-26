from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load models and scaler
MODEL_PATH = 'model/model.pkl'
SCALER_PATH = 'model/scaler.pkl'
ALL_MODELS_PATH = 'model/all_models.pkl'
RESULTS_PATH = 'model/results.pkl'

model = None
scaler = None
all_models = {}
results = {}

def load_model_files():
    global model, scaler, all_models, results
    try:
        if os.path.exists(MODEL_PATH):
            with open(MODEL_PATH, 'rb') as f:
                model = pickle.load(f)
            logger.info("Main model loaded successfully")
        
        if os.path.exists(SCALER_PATH):
            with open(SCALER_PATH, 'rb') as f:
                scaler = pickle.load(f)
            logger.info("Scaler loaded successfully")
        
        if os.path.exists(ALL_MODELS_PATH):
            with open(ALL_MODELS_PATH, 'rb') as f:
                all_models = pickle.load(f)
            logger.info(f"All models loaded: {list(all_models.keys())}")
        
        if os.path.exists(RESULTS_PATH):
            with open(RESULTS_PATH, 'rb') as f:
                results = pickle.load(f)
            logger.info("Results loaded successfully")
    except Exception as e:
        logger.error(f"Error loading models: {str(e)}")

load_model_files()

@app.route('/')
def home():
    """Home page with project overview"""
    dataset_info = {
        'total_transactions': 284807,
        'fraud_cases': 492,
        'legitimate_cases': 284315,
        'fraud_percentage': 0.172
    }
    
    model_list = list(all_models.keys()) if all_models else ['Random_Forest']
    
    return render_template('index.html', 
                         dataset_info=dataset_info,
                         models=model_list)

@app.route('/dashboard')
def dashboard():
    """Dashboard with visualizations and metrics"""
    # Prepare results for display
    results_data = []
    if results:
        for model_name, metrics in results.items():
            results_data.append({
                'model': model_name,
                'accuracy': f"{metrics['accuracy']:.4f}",
                'precision': f"{metrics['precision']:.4f}",
                'recall': f"{metrics['recall']:.4f}",
                'f1_score': f"{metrics['f1_score']:.4f}",
                'roc_auc': f"{metrics['roc_auc']:.4f}"
            })
    
    return render_template('dashboard.html', results=results_data)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Prediction page"""
    if request.method == 'GET':
        model_list = list(all_models.keys()) if all_models else ['Random_Forest']
        return render_template('predict.html', models=model_list)
    
    try:
        # Get form data
        features = []
        feature_names = []
        
        # Get Time and Amount
        time_val = float(request.form.get('Time', 0))
        features.append(time_val)
        feature_names.append('Time')
        
        # Get V1 to V28
        for i in range(1, 29):
            val = float(request.form.get(f'V{i}', 0))
            features.append(val)
            feature_names.append(f'V{i}')
        
        amount_val = float(request.form.get('Amount', 0))
        features.append(amount_val)
        feature_names.append('Amount')
        
        # Get selected model
        selected_model_name = request.form.get('model', 'Random_Forest')
        
        # Validate input
        if len(features) != 30:
            return jsonify({
                'error': 'Invalid number of features. Expected 30 features.'
            }), 400
        
        # Scale features
        features_array = np.array(features).reshape(1, -1)
        if scaler:
            features_scaled = scaler.transform(features_array)
        else:
            features_scaled = features_array
        
        # Select model
        selected_model = all_models.get(selected_model_name, model)
        if selected_model is None:
            return jsonify({
                'error': 'Model not loaded. Please train the model first.'
            }), 500
        
        # Make prediction
        prediction = selected_model.predict(features_scaled)[0]
        probability = selected_model.predict_proba(features_scaled)[0]
        
        result = {
            'prediction': 'Fraudulent' if prediction == 1 else 'Legitimate',
            'prediction_class': int(prediction),
            'fraud_probability': float(probability[1]),
            'legit_probability': float(probability[0]),
            'model_used': selected_model_name
        }
        
        logger.info(f"Prediction made: {result}")
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify(result)
        else:
            model_list = list(all_models.keys()) if all_models else ['Random_Forest']
            return render_template('predict.html', 
                                 models=model_list,
                                 result=result,
                                 form_data=request.form)
    
    except ValueError as e:
        error_msg = f"Invalid input: {str(e)}"
        logger.error(error_msg)
        return jsonify({'error': error_msg}), 400
    except Exception as e:
        error_msg = f"Prediction error: {str(e)}"
        logger.error(error_msg)
        return jsonify({'error': error_msg}), 500

@app.route('/api/model-info')
def model_info():
    """API endpoint for model information"""
    info = {
        'models_loaded': list(all_models.keys()),
        'default_model': 'Random_Forest',
        'features_required': 30,
        'feature_names': ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
    }
    return jsonify(info)

@app.errorhandler(404)
def not_found(e):
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
