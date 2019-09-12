import pandas as pd
import pickle as pi
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.externals import joblib


sns.set()

df = pd.read_csv("P12-SalaryData.csv")

X_data=np.matrix(df['YearsExperience'])

Y_data=np.matrix(df['Salary'])

train_set, test_set = train_test_split(df, test_size=0.2)

df_copy = train_set.copy()
train_set = train_set.drop(["Salary"], axis=1)

train_labels = df_copy['Salary']

lin_reg = LinearRegression()
lin_reg.fit(train_set, train_labels)
#df.plot.scatter(x='Year', y='TotalPopulation')
#plt.show()

#Regressionplot
#sns.regplot('Year', 'TotalPopulation', data=df)
joblib.dump(lin_reg, "linear_regression_model.pkl")