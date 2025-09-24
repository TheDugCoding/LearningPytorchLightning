import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
s = 'https://archive.ics.uci.edu/ml/'\
    'machine-learning-databases/iris/iris.data'
print('From URL:', s)
df = pd.read_csv(s, header=None, encoding='utf-8')

print(df.columns)
print(df.tail())
print(df.describe())
#check how many variants are in the dataset
print(df[4].unique())
#
flower_map = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}
df[4] = df[4].map(flower_map)
print(df[4].unique())

#The correlation matrix is a square matrix that contains the Pearson product-moment correlation
#coefficient (often abbreviated as Pearson’s r), which measures the linear dependence between pairs
#of features Two features have a perfect positive
#correlation if r = 1, no correlation if r = 0, and a perfect negative correlation if r = –1.
#a strong correlation is above ±0.7/±0.8
#Variables that are highly correlated might add redundant information
#we can also use the correlation matrix for multicollinearity, some regression models
#do not perform well when two variables are highly correlated
matrix = df.corr()
print(matrix)
plt.figure(figsize=(8,6))
sns.heatmap(matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()