# Dataset Directory

## Instructions

1. Download the Credit Card Fraud Detection dataset from Kaggle:
   https://www.kaggle.com/mlg-ulb/creditcardfraud

2. Place the `creditcard.csv` file in this directory

3. The file should be approximately 150 MB in size

4. After placing the file, run the training script:
   ```
   cd model
   python train_model.py
   ```

## Dataset Information

- **Filename**: creditcard.csv
- **Size**: ~150 MB
- **Rows**: 284,807 transactions
- **Columns**: 31 (Time, V1-V28, Amount, Class)
- **Target**: Class (0 = Legitimate, 1 = Fraud)

## Note

The dataset is not included in this repository due to its size. You must download it separately from Kaggle.
