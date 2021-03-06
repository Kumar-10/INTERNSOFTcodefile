# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:19:29 2020

@author: admin
"""

#IMPORTING ON LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt 



#READING YOUR DATA FROM YOUR FILE
data = pd.read_csv("advertising.csv")
data.head()



#VISUALISING THE DATA
fig, axs = plt.subplots(1,3,sharey = True)
data.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(16,8))
data.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1])
data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2])




#CREATING X&Y FOR LINEAR REGRESSION
feature_cols = ['TV']
X = data[feature_cols]
y = data.Sales

#IMPORTING LINEAR REGRESSION ALGO
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)

print(lr.intercept_)

y = a+bx

result = 6.97+0.0554*50
print(result)

#CREATING A DATAFRAM WITH MIN AND MAX VALUE OF THE TABLE
X_new = pd.DataFrame({'TV':[data.TV.min(),data.TV.max()]})
X_new.head()


preds = lr.predict(X_new)
preds

data.plot(kind = 'scatter',x='TV',y='Sales')


plt.plot(X_new,preds,c='red',linewidth = 3)

import statsmodels.formula.api as smf
lm = smf.ols(formula='Sales ~ TV', data=data).fit()
lm.conf_int()


#FINDING THE PROBABLILTY VALUE 
lm.pvalues

#FINDING THE R-SQUARED VALUE
lm.rsquared

#MULTI LINEAR REGRESSION
feature_cols = ['TV','Radio','Newspaper']
X = data[feature_cols]
y = data.Sales


lr = LinearRegression()
lr.fit(X,y)


print(lr.intercept_)
print(lr.coef_)



lm = smf.ols(formula='Sales ~ TV+Radio+Newspaper',data=data).fit()
lm.conf_int()
lm.summary()










