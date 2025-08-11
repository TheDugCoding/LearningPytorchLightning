import pandas as pd
import numpy as np

#source
#https://wesmckinney.com/book/pandas-basics

#in pandas, we have dataframe and series. A dataframe is a multidimensional array, a series a single dimensional array
#compared to numpy, pandas offers more flexibility (attaching labels, working with missing data etc.)

#a pandas series can be created from a list or array as follows
#pd.Series(data, index=index)

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
print(type(data))
print(data.values)
pd.Series({2:'a', 1:'b', 3:'c'})
pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])

#in pandas the index is a bit more flexible compared to numpy, in numpy the index is implicitly defined in pandas we
# can define it ourselves. We can consider it as a dictionary
print(data.index)
print(data[1:3])
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(f'value at index b = {data["b"]}')
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[2, 5, 3, 7])
print(f'value at index 2 = {data[2]}')

#for the dataframes they are basically multidimensional arrays
data = [{'a': i, 'b': 2 * i}
for i in range(3)]
pd.DataFrame(data)

pd_data = pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'], index=['a', 'b', 'c'])
print(pd_data)
print(pd_data['foo'])

#we can also create a dataframe from dictionaries, keys are used as indexes, notice that in both cases the keys are the same
area = pd.Series({'California': 423967, 'Texas': 695662,
'New York': 141297, 'Florida': 170312,
'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
'New York': 19651127, 'Florida': 19552860,
'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
print(data)

#to detect missing data we can use pd.isna(data), or to count how many are not NaN notna
print(pd.isna(data))
#count how many values are missing per column
print(data.isna().count())

#use .head to select the first n rows, default is 5
print(data.head(2))
#use .tail to select the last n rows, default is 5
print(data.tail(2))
# .describe() gives a nice description of the columns values
print(data.describe())

#we can retrieve a column by using dot notation or dictionary like notation
print(data['area'])
print(data.area)

#to retrieve rows we can use loc and iloc, loc selects columns names (labels) while iloc uses numerical indices
print(data.loc['California'])
print(data.loc[['California' ,'Texas']])
print(data.loc['California':'Texas'])
#we can also use conditionals
print(data.loc[data['area'] != 423967])

#with loc is similar
print(data.iloc[0, 0])

# when we assign new values to an existing column the length of a series must match the length of the column
#assign a column that doesn't exist will create a new column
order = pd.Series({'California': 1, 'Texas': 2,
'New York': 3, 'Florida': 4,
'Illinois': 5})
data['position'] = order
print(data)
#let's add a new column but we don't fill every entry then the new column will have nan values
val = pd.Series([-1.2, -1.5, -1.7], index=['California', 'Texas', 'New York'])
data["debt"] = val
print(data)

#we can use del to remove a column
del data["debt"]
print(data)

#remember that any modification to a series taken from the dataframe is considered a view and not a copy

#checking name of index and columns
print(data.columns)
print(data.index.names)

#pandas dataset can contain duplicate indexes

#reindex rearrange the order of the elements
data2 = data.reindex(np.random.permutation(data.index))
print(data)
print(data2)

#we can also use .drop() to drop a column
print(data.drop(columns=["position"]))


