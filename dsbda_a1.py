import numpy as np
import pandas as pd

"""Loading the dataset into dataframe"""

df=pd.read_csv("iris.csv")

"""Data Preprocessing"""

df.describe()

df.head()

df.tail()

df.tail(3)

df.info()

df.shape

df.size

df.duplicated()

df.duplicated().sum()

df.isnull()

df.isnull().sum()

df.notnull()

df.notnull().sum()

df["sepal.length"].isnull()

y=df.drop(["petal.length"], axis=1) # axis=1 column. For row, axis=0
print(y)

"""Turn categorical variables into quamtitative variables"""

df['variety'].replace(['Setosa', 'Versicolor', 'Virginica'], [0, 1, 2], inplace=True)
print(df)

#=====================================================================

df=df.dropna()

df.isnull().sum()

"""Data type of variables"""

df["Fare"].astype(int)