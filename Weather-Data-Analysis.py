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


print(data.isnull())
print(data.isnull().sum())

print(data.notnull())
print(data.notnull().sum())

data.rename(columns = {'Weather': 'weather Condition'})
print(data.rename(columns = {'Weather': 'weather Condition'}, inplace=True))


print(data.Visibility_km.mean())


print(data.Press_kPa.std())

print(data['Rel Hum_%'].var())


# value_counts
print(data['weather Condition'].value_counts())

#filtring
print(data[data['weather Condition'] =='Snow'] )

#str.contains
print(data[data['weather Condition'].str.contains('Snow')].head(50) )
print(data[data['weather Condition'].str.contains('Snow')].tail(50) )



#wind speed
print(data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)] )


print(data.groupby('weather Condition').mean() )



print(data.groupby('weather Condition').min() )



print(data[data['weather Condition'] == 'Fog']  )


print(data[(data['weather Condition'  ] == 'Clear') | (data ['Visibility_km'] > 40)] ) 








