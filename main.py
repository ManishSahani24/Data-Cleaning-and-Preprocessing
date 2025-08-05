import pandas as pd
df = pd.read_csv('Titanic-Dataset.csv')

# Check for the total number of missing values in each column
print(df.isnull().sum())