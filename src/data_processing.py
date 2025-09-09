import pandas as pd
import numpy as np

def load_data():
    from sklearn import datasets 
    california = datasets.fetch_california_housing()
    df = pd.Dataframe(california.data, columns=california.feature_names)
    df['PRICE'] = california.target
    return df 

def clean_data(df):
    df = df.drop_duplicates()
    df = df.fillna(df.mean())
    return df

if __name__ == "__main__":
    print("Testing data preprocessing module...")
    data = load_data()
    print(f"Data loaded with shape: {data.shape}")