import numpy as np
import torch
import pandas as pd
df = pd.read_csv('bank_fraud.csv')
mapping = {
    "nofraud": 0,
    "Phishing": 1,
    "Account Takeover": 2,
    "Synthetic Identity": 3,
    "Card Cloning": 4,
    "Friendly Fraud": 5,
    'Identity Theft': 6
}
def clean(df):
    df=df.drop(columns=['transaction_id'])
    df=df.drop(columns=['customer_id'])
    df=df.drop(columns=['is_fraud'])
    df=df.drop(columns=['hour_of_day'])
    df=df.drop(columns=['is_weekend'])
    df=df.drop(columns=['is_night_transaction'])
    df["transaction_datetime"] = pd.to_datetime(df["transaction_date"] + " " + df["transaction_time"])
    df["year"] = df["transaction_datetime"].dt.year
    df["month"] = df["transaction_datetime"].dt.month
    df["day_of_week"] = df["transaction_datetime"].dt.dayofweek
    df["hour"] = df["transaction_datetime"].dt.hour
    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)
    df=df.drop(columns=['hour'])
    df=df.drop(columns=['transaction_date'])
    df=df.drop(columns=['transaction_time'])
    df=df.drop(columns=['transaction_datetime'])
    df=pd.get_dummies(df, columns=['city','merchant_category','country','payment_method','device_type'], drop_first=True)
    df.fraud_type=df.fraud_type.fillna('nofraud')
    df.fraud_type=df.fraud_type.map(mapping)
    return df
df=clean(df)
def encode(df):
    X=df.drop(columns=['fraud_type'])
    y=df.fraud_type
    X=X.astype('float32')
    X_tensor = torch.tensor(X.values, dtype=torch.float32)
    y_tensor = torch.tensor(y.values, dtype=torch.long)
    return X_tensor,y_tensor
X_tensor,y_tensor=encode(df)