# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:20:33 2024

@author: ShwetaM
"""

from sklearn.ensemble import RandomForestRegressor
#### importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

### read data
df=pd.read_excel('/Users/anushraypingale/Desktop/BE_PROJECT/final_dataset.xlsx')

### load features
x=df.iloc[:,0:7] 

###load target
y=df.iloc[:,10]

####split the data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)

### define random forest
model=RandomForestClassifier(n_estimators=50)

###train model
model.fit(x_train,y_train)

### prediction
predict=model.predict(x_test)

## Model name
filename = 'rf_model.sav'
## Save the model
pickle.dump(model, open(filename, 'wb'))


### load features
x1=df.iloc[:,0:7] 

###load target
y1=df.iloc[:,7:10]

####split the data
x_train1,x_test1,y_train1,y_test1=train_test_split(x1,y1,test_size=0.1)

### define random forest
model1=RandomForestRegressor(n_estimators=10, random_state=42)

###train model
model1.fit(x_train1,y_train1)

### prediction
predict=model1.predict(x_test1)

## Model name
filename = 'rf_model1.sav'
## Save the model
pickle.dump(model1, open(filename, 'wb'))