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
print(data['Weather'].value_counts())
print(data.info())
wind_speed = data.head(2)
print(wind_speed)
print(data.nunique())
print(data['Wind Speed_km/h'].nunique())
print(data['Wind Speed_km/h'].unique())
 
print(data.head(2))
weather1 = data.Weather.value_counts()
print(weather1)


print(data.head(2))

print(data [data.Weather == 'Clear'])
print(data.groupby('Weather').get_group('Clear'))