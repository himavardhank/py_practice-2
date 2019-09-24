import pandas as pd
'''df=pd.read_csv("C:/Users/welcome/Documents/exec2.csv")

rows,columns=df.shape
print(rows)
print(df.columns)
print(df.Date)
print(df.shape)
print(df[' Profit '])
print(type(df['Date']))
print(df[['Date',' COGS ']])

print('max ',df['Units Sold'].max())
print('min',df['Units Sold'].min())
print('mean',df['Units Sold'].mean())
print('std',df['Units Sold'].std())
print(df.describe())
#print(df)
print(df['Units Sold'])

print(df[df['Units Sold']==df['Units Sold'].max()])
print(df.index)
print(df.set_index('Date'))
df.set_index('Date',inplace=True)
print(df.loc['6/1/2014'])
df.reset_index(inplace=True)
print(df)

df1=pd.read_excel("C:/Users/welcome/Documents/excel.xlsx","Sheet2")
print(df1)

weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df = pd.DataFrame(weather_data)
print(df)

weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
print(df)

weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},
    
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
print(df)




df=pd.read_csv("C:/Users/welcome/Documents/exec2.csv",skiprows=1)
print(df)
df=pd.read_csv("C:/Users/welcome/Documents/exec2.csv",header=None,names=['price','tempearture','wind'])
print(df)

df=pd.read_csv("C:/Users/welcome/Documents/exec2.csv",nrows=4)
print(df)

df=pd.read_csv("C:/Users/welcome/Documents/exec2.csv",na_values=['not available',"n.a",'2014'])
print(df)
df=pd.read_csv("C:/Users/welcome/Documents/exec2.csv",na_values={'Year':['n.a'],'Segment':['not available'],'Segment.1':['not available','n.a']})
#print(df)

#df.to_csv('new.csv',index=False)
#print(df.columns)
df.to_csv('new1.csv',index=False,header=False,columns=[' Discount Band ', 'Units Sold',' Manufacturing Price ', ' Sale Price '])

df1=pd.read_excel("C:/Users/welcome/Documents/excel.xlsx","Sheet1")
print(df1)
def con_Segment_cell(cell):
    if cell=="n.a":
        return 'aaaaaaaa'
    return cell
def convert_Month_Name_cell(cell):
    if cell=="n.a":
        return 'bbbbbbb'
    return cell
df1=pd.read_excel("C:/Users/welcome/Documents/excel.xlsx","Sheet1",converters={'Segment':con_Segment_cell,'Month_Name':convert_Month_Name_cell})
print(df1)

print(df1)
df1.to_excel("new.xlsx",sheet_name="pack",startrow=1,startcol=2,index=False)

weather_data = pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
})

weather_data2 = pd.DataFrame([
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
])
with pd.ExcelWriter('weather_data.xlsx')as writer:
    weather_data.to_excel(writer,sheet_name="weather1")
    weather_data2.to_excel(writer,sheet_name="weather2")

df=pd.read_csv("C:/Users/welcome/Documents/exec2.csv",parse_dates=["Date"])
#print(type(df.Date[0]))
df.set_index('Date',inplace=True)
#print(df)'''

#df=pd.read_csv("C:/Users/welcome/Documents/exec2.csv")
#new_df=df.fillna(0)
#print(new_df)
#new_df=df.fillna({'Year':0,'Segment.1':'no_one'})
#print(new_df)

#print(df)
#new_df=df.fillna(method='ffill')
#print(new_df)
#new_df1=df.fillna(method='bfill')
#print(new_df1)

'''new_df=df.fillna(method='ffill',axis='columns')
print(new_df)

new_df=df.fillna(method='bfill',axis='columns')
print(new_df)


new_df=df.fillna(method='ffill',limit=1)
print(new_df)


new_df=df.interpolate(method="time")
print(new_df)

new_df=df.dropna()
#print(new_df)

new_df=df.dropna(how='all')
#print(new_df)

new_df=df.dropna(thresh=5)
print(new_df)

dt=pd.date_range("01-01-2017","01-11-2017")
idx=pd.DatetimeIndex(dt)
df=df.reindex(idx)
print(df)


import numpy as np
df=pd.read_csv("C:/Users/welcome/Documents/exec2.csv")
#print(df)
new_df=df.replace(-99999,np.NaN)
#print(new_df)
new_df1=df.replace([1618.5,1321],np.NaN)
#print(new_df1)
new_df1=df.replace({'Segment':'Government',
                    'Segment.1':'Montana'},np.NaN)
#print(new_df1)

new_df1=df.replace({2518:np.NaN,
                    'not available':'Midmarket'},np.NaN)
#print(new_df1)
new_df1=df.replace({'Units Sold':'[a-zA-Z]',
                    'Segment':'[A-Za-z]'},'',regex=True)
#print(new_df1)


new_df1=df.replace(['Government','Midmarket','Channel Partners','Enterprise'],[1,2,3,4])
#print(new_df1)

df=pd.read_csv("C:/Users/welcome/Documents/exec2.csv")
k=df.groupby(' Month Name ')
#for a,b in k:
#    print(a)
 #   print(b)

l=k.get_group(' June ')
#print(l)
#print(k.max())
#print(k.min())
#print(k.describe())




India_weather = pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']})

#print(India_weather)
Us_weather = pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [12,15,18],
    'windspeed': [10,7,21],
    'event': ['Rain', 'Sunny', 'Snow']})

#print(Us_weather)
df=pd.concat([India_weather,Us_weather])

df=pd.concat([India_weather,Us_weather],ignore_index=True)

df=pd.concat([India_weather,Us_weather],keys=['india','Us'])

print(df.loc['Us'])
print(df)


temperature_df=pd.DataFrame({'temperature': [32,35,28],
    'windspeed': [6,7,2]},index=[0,1,2])
#print(temperature_df)

windspeed_df=pd.DataFrame({'windspeed': [10,7,21],
    'event': ['Rain', 'Sunny', 'Snow']},index=[0,1,2])
#print(windspeed_df)
df=pd.concat([temperature_df,windspeed_df],axis=1)
#print(df)

df1=pd.DataFrame({'temperature': [32,35,28],
    'windspeed': [21,7,2]})
#print(df1)
df2=pd.DataFrame({'windspeed': [10,7,21],
    'event': ['Rain', 'Sunny', 'Snow']})
#print(df2)
df3=pd.merge(df1,df2,on='windspeed')
df4=pd.merge(df1,df2,on='windspeed',how='outer',indicator=True)

df5=pd.merge(df1,df2,on='windspeed',how='left')
df6=pd.merge(df1,df2,on='windspeed',how='right')

#print(df4)

df1=pd.DataFrame({'temperature': [10,35,8],
    'windspeed': [2,17,12]})
df2=pd.DataFrame({'temperature': [32,35,28],
    'windspeed': [21,7,2]})
df3=pd.merge(df1,df2,on='windspeed',suffixes=('_left','_right'))
print(df3)'''

'''import numpy as np
df=pd.read_csv("C:/Users/welcome/Documents/for_pivot12.csv")
#print(df)
k=df.pivot(index='city',columns='date')
#print(k)
l=df.pivot(index='city',columns='date',values="humidity")
#print(l)
k=df.pivot(index='date',columns='city')
#print(k)
m=df.pivot(index='humidity',columns='city')
#print(m)
#j=df.pivot(index='city',columns='date',margins=True)
#print(j)
df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city')'''



'''df=pd.read_csv("C:/Users/welcome/Documents/exec2.csv")
#print(df)
df1=pd.melt(df,id_vars=['Date'])
#print(df1)
print(df1[df1['variable']=='Government'])'''

df1=pd.read_excel("C:/Users/welcome/Documents/excel.xlsx",header=[0,1])
#print(df1)
#print(df1.stack())
print(df1.stack(level=0))

