# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:58:36 2024

@author: tumel
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv")

"""
Q2
df=pd.read_csv("movie_dataset.csv")

df2 = df["Revenue (Millions)"].mean()
print(df2)
"""
"""
Q3
df2 = df.loc[(df['Year'] >= 2015)&(df['Year'] <= 2017)]
df3 = df2["Revenue (Millions)"].mean()
print(df3)
"""
"""
Q4
df1 = df[df.Year ==2016]
print(df1.describe())
"""
"""
Q5
filtered_df = df[df["Director"].str.contains("Christopher Nolan")]
print(filtered_df)
print(filtered_df.describe())
"""
"""
Q6
df1 = df[df.Rating >=8.0]
print(df1.describe())
"""
"""
Q7
filtered_df = df[df["Director"].str.contains("Christopher Nolan")]
print(filtered_df.Rating.describe())
"""
"""
Q8
df3 = df[["Rating","Year"]]

print(df3.max())
"""
"""
Q9
df2=(df['Year'] == 2006).sum()
df3= (df['Year'] == 2016).sum()
Nominator=df3-df2
deNominator=df2
df3=(Nominator/deNominator)*100
"""
"""
Q10
df5 = df['Actors'].str.split(', ')
df6 = [actor for sublist in df5 for actor in sublist]
#Number of actors
df7= pd.Series(df6).value_counts()
# Most common actors
df8= df7.idxmax()
print(df8)
"""
"""
Q11
#Unique genres
Genre = len(df['Genre'].unique())
"""
"""
Q12
#column for columns

df9 = ['Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']
df_10 = df[df9]

#Correlation matrix
matrix= df_10.corr()

print(matrix)
"""



