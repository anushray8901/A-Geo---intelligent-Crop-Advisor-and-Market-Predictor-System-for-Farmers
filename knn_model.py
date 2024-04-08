# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:20:42 2023

@author: Dell
"""
###importing libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier  
import pickle

###read daata
df=pd.read_excel('/Users/anushraypingale/Desktop/BE_PROJECT/dataset_industry.xlsx')

print(df.columns)

x=df.iloc[:,0:2] #### 1,2
print(x)

y=df.iloc[:,2]
print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)

model=KNeighborsClassifier(n_neighbors=1)

model.fit(x_train,y_train)

predict=model.predict(x_test)

## Model name
filename = 'knn_model.sav'
## Save the model
pickle.dump(model, open(filename, 'wb'))




