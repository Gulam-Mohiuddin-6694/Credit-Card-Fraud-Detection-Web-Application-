import pandas as pd
import numpy as np
import pickle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score, roc_curve
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
import warnings
warnings.filterwarnings('ignore')

class FraudDetectionModel:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.scaler = StandardScaler()
        self.models = {}
        self.results = {}
        
    def load_data(self):
        print("Loading dataset...")
        self.df = pd.read_csv(self.dataset_path)
        print(f"Dataset shape: {self.df.shape}")
        print(f"Fraud cases: {self.df['Class'].sum()}")
        print(f"Legitimate cases: {len(self.df) - self.df['Class'].sum()}")
        return self.df
    
    def preprocess_data(self):
        print("\nPreprocessing data...")
        # Check for missing values
        if self.df.isnull().sum().sum() > 0:
            self.df = self.df.dropna()
        
        # Separate features and target
        X = self.df.drop('Class', axis=1)
        y = self.df['Class']
        
        # Train-test split with stratification
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Feature scaling
        self.X_train = self.scaler.fit_transform(X_train)
        self.X_test = self.scaler.transform(X_test)
        self.y_train = y_train
        self.y_test = y_test
        
        print(f"Training set size: {len(self.X_train)}")
        print(f"Test set size: {len(self.X_test)}")
        
    def handle_imbalance(self):
        print("\nHandling class imbalance...")
        
        # Original imbalanced data
        print("Training on original imbalanced data...")
        lr_original = LogisticRegression(max_iter=1000, random_state=42)
        lr_original.fit(self.X_train, self.y_train)
        self.models['Logistic_Original'] = lr_original
        self.evaluate_model('Logistic_Original', lr_original)
        
        # SMOTE
        print("\nApplying SMOTE...")
        smote = SMOTE(random_state=42)
        X_train_smote, y_train_smote = smote.fit_resample(self.X_train, self.y_train)
        print(f"After SMOTE - Fraud cases: {y_train_smote.sum()}, Legit cases: {len(y_train_smote) - y_train_smote.sum()}")
        
        lr_smote = LogisticRegression(max_iter=1000, random_state=42)
        lr_smote.fit(X_train_smote, y_train_smote)
        self.models['Logistic_SMOTE'] = lr_smote
        self.evaluate_model('Logistic_SMOTE', lr_smote)
        
        # Random Undersampling
        print("\nApplying Random Undersampling...")
        rus = RandomUnderSampler(random_state=42)
        X_train_rus, y_train_rus = rus.fit_resample(self.X_train, self.y_train)
        print(f"After Undersampling - Fraud cases: {y_train_rus.sum()}, Legit cases: {len(y_train_rus) - y_train_rus.sum()}")
        
        lr_rus = LogisticRegression(max_iter=1000, random_state=42)
        lr_rus.fit(X_train_rus, y_train_rus)
        self.models['Logistic_Undersampling'] = lr_rus
        self.evaluate_model('Logistic_Undersampling', lr_rus)
        
        # Class weight balancing
        print("\nApplying Class Weight Balancing...")
        lr_weighted = LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42)
        lr_weighted.fit(self.X_train, self.y_train)
        self.models['Logistic_Weighted'] = lr_weighted
        self.evaluate_model('Logistic_Weighted', lr_weighted)
        
    def train_models(self):
        print("\n" + "="*50)
        print("Training Random Forest...")
        rf = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42, n_jobs=-1)
        rf.fit(self.X_train, self.y_train)
        self.models['Random_Forest'] = rf
        self.evaluate_model('Random_Forest', rf)
        
    def evaluate_model(self, model_name, model):
        y_pred = model.predict(self.X_test)
        y_pred_proba = model.predict_proba(self.X_test)[:, 1]
        
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred)
        recall = recall_score(self.y_test, y_pred)
        f1 = f1_score(self.y_test, y_pred)
        roc_auc = roc_auc_score(self.y_test, y_pred_proba)
        cm = confusion_matrix(self.y_test, y_pred)
        
        self.results[model_name] = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'roc_auc': roc_auc,
            'confusion_matrix': cm,
            'y_pred_proba': y_pred_proba
        }
        
        print(f"\n{model_name} Results:")
        print(f"Accuracy: {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1-Score: {f1:.4f}")
        print(f"ROC-AUC: {roc_auc:.4f}")
        
    def save_models(self):
        print("\nSaving models and scaler...")
        
        # Save best model (Random Forest)
        with open('../model/model.pkl', 'wb') as f:
            pickle.dump(self.models['Random_Forest'], f)
        
        # Save scaler
        with open('../model/scaler.pkl', 'wb') as f:
            pickle.dump(self.scaler, f)
        
        # Save all models
        with open('../model/all_models.pkl', 'wb') as f:
            pickle.dump(self.models, f)
        
        # Save results
        with open('../model/results.pkl', 'wb') as f:
            pickle.dump(self.results, f)
        
        # Save feature importance for Random Forest
        if 'Random_Forest' in self.models:
            feature_names = self.df.drop('Class', axis=1).columns
            importances = self.models['Random_Forest'].feature_importances_
            feature_importance = pd.DataFrame({
                'feature': feature_names,
                'importance': importances
            }).sort_values('importance', ascending=False)
            feature_importance.to_csv('../model/feature_importance.csv', index=False)
        
        print("Models saved successfully!")
        
    def generate_visualizations(self):
        print("\nGenerating visualizations...")
        
        # Class distribution
        plt.figure(figsize=(8, 6))
        self.df['Class'].value_counts().plot(kind='bar', color=['green', 'red'])
        plt.title('Class Distribution')
        plt.xlabel('Class (0: Legit, 1: Fraud)')
        plt.ylabel('Count')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig('../static/images/class_distribution.png')
        plt.close()
        
        # ROC Curves
        plt.figure(figsize=(10, 8))
        for model_name, results in self.results.items():
            fpr, tpr, _ = roc_curve(self.y_test, results['y_pred_proba'])
            plt.plot(fpr, tpr, label=f"{model_name} (AUC = {results['roc_auc']:.3f})")
        plt.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curves Comparison')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('../static/images/roc_curves.png')
        plt.close()
        
        # Confusion Matrix for best model (Random Forest)
        plt.figure(figsize=(8, 6))
        cm = self.results['Random_Forest']['confusion_matrix']
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
        plt.title('Confusion Matrix - Random Forest')
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        plt.tight_layout()
        plt.savefig('../static/images/confusion_matrix.png')
        plt.close()
        
        # Feature Importance
        if 'Random_Forest' in self.models:
            feature_importance = pd.read_csv('../model/feature_importance.csv')
            plt.figure(figsize=(10, 8))
            top_features = feature_importance.head(15)
            plt.barh(top_features['feature'], top_features['importance'])
            plt.xlabel('Importance')
            plt.title('Top 15 Feature Importances - Random Forest')
            plt.gca().invert_yaxis()
            plt.tight_layout()
            plt.savefig('../static/images/feature_importance.png')
            plt.close()
        
        print("Visualizations saved!")
        
    def print_comparison(self):
        print("\n" + "="*80)
        print("MODEL COMPARISON SUMMARY")
        print("="*80)
        print(f"{'Model':<30} {'Accuracy':<12} {'Precision':<12} {'Recall':<12} {'F1-Score':<12} {'ROC-AUC':<12}")
        print("-"*80)
        for model_name, results in self.results.items():
            print(f"{model_name:<30} {results['accuracy']:<12.4f} {results['precision']:<12.4f} {results['recall']:<12.4f} {results['f1_score']:<12.4f} {results['roc_auc']:<12.4f}")
        print("="*80)

if __name__ == "__main__":
    # Initialize and train
    fraud_model = FraudDetectionModel('../dataset/creditcard.csv')
    fraud_model.load_data()
    fraud_model.preprocess_data()
    fraud_model.handle_imbalance()
    fraud_model.train_models()
    fraud_model.save_models()
    fraud_model.generate_visualizations()
    fraud_model.print_comparison()
    
    print("\n✅ Training completed successfully!")
    print("Models and visualizations are ready for the web application.")
