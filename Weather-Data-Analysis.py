import pandas as pd

data = pd.read_csv('C:/Users/PC/Desktop/Weather-Data-Analysis/Weather-Data.csv')
print(data)
print(data.head())
print(data.shape)
print(data.index)
print(data.columns)
print(data.dtypes)
print(data['Weather'].unique())
print(data.nunique())
print(data.count())