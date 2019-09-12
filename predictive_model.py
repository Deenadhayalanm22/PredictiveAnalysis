import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


sns.set()

df = pd.read_csv("data.csv")

train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

#df.plot.scatter(x='Year', y='TotalPopulation')
#plt.show()

#Regressionplot
sns.regplot('Year', 'TotalPopulation', data=df)
plt.show()