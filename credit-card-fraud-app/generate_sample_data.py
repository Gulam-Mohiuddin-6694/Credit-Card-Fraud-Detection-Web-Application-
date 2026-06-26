"""
Sample Data Generator for Testing
Generates synthetic transaction data for testing the application without the full dataset
"""

import numpy as np
import pandas as pd

def generate_sample_data(n_samples=1000, fraud_ratio=0.002):
    """
    Generate sample credit card transaction data
    
    Parameters:
    - n_samples: Number of samples to generate
    - fraud_ratio: Ratio of fraudulent transactions
    """
    np.random.seed(42)
    
    n_fraud = int(n_samples * fraud_ratio)
    n_legit = n_samples - n_fraud
    
    print(f"Generating {n_samples} samples...")
    print(f"Legitimate: {n_legit}, Fraud: {n_fraud}")
    
    # Generate legitimate transactions
    legit_data = {
        'Time': np.random.uniform(0, 172800, n_legit),
        'Amount': np.random.lognormal(3, 1.5, n_legit),
        'Class': np.zeros(n_legit)
    }
    
    # Generate V1-V28 features for legitimate transactions
    for i in range(1, 29):
        legit_data[f'V{i}'] = np.random.normal(0, 1, n_legit)
    
    # Generate fraudulent transactions (with different distributions)
    fraud_data = {
        'Time': np.random.uniform(0, 172800, n_fraud),
        'Amount': np.random.lognormal(2, 2, n_fraud),
        'Class': np.ones(n_fraud)
    }
    
    # Generate V1-V28 features for fraudulent transactions (shifted distributions)
    for i in range(1, 29):
        fraud_data[f'V{i}'] = np.random.normal(0.5, 1.5, n_fraud)
    
    # Combine data
    legit_df = pd.DataFrame(legit_data)
    fraud_df = pd.DataFrame(fraud_data)
    
    df = pd.concat([legit_df, fraud_df], ignore_index=True)
    
    # Shuffle
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Reorder columns
    columns = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount', 'Class']
    df = df[columns]
    
    return df

def save_sample_data(output_path='dataset/creditcard_sample.csv', n_samples=1000):
    """Generate and save sample data"""
    df = generate_sample_data(n_samples)
    df.to_csv(output_path, index=False)
    print(f"\n✅ Sample data saved to: {output_path}")
    print(f"Shape: {df.shape}")
    print(f"\nClass distribution:")
    print(df['Class'].value_counts())
    return df

if __name__ == "__main__":
    print("="*60)
    print("Sample Data Generator")
    print("="*60)
    print("\nThis script generates synthetic data for testing.")
    print("For production, use the real creditcard.csv dataset.\n")
    
    # Generate sample data
    df = save_sample_data(n_samples=10000)
    
    print("\n" + "="*60)
    print("Sample data generated successfully!")
    print("="*60)
    print("\nYou can now train models with this sample data:")
    print("1. Rename creditcard_sample.csv to creditcard.csv")
    print("2. Run: cd model && python train_model.py && cd ..")
    print("\nNote: Results will be less accurate than with real data.")
    print("="*60)
