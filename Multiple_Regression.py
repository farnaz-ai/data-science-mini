import pandas
from sklearn import linear_model
df=pandas.read_csv('data.csv')
x= df[['name','date']]
y= df['time']

regr = linear_model.LinearRegression()
regr.fit(x,y)

predicttime = regr.predict([['0000000517',1402/09/04' ]])

print(predicttime)
