#https://www.kaggle.com/jorgesandoval/feature-selection-with-rrelieff-regression
# Base Libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# Transformation
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import power_transform
from sklearn.pipeline import Pipeline
# Feature Selection
import sklearn_relief as sr
# Models
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df_amp = pd.read_csv('Amprion.csv')
dates = df_amp['Date']
df_amp = df_amp.T
df_amp = df_amp[1:]
df_amp.columns = [dates]

df_amp.reset_index(drop=True, inplace=True)

scaler = MinMaxScaler()

df_amp = power_transform(df_amp, method='yeo-johnson')
df_amp = scaler.fit_transform(df_amp)

X = df_amp[:,0:396]
y = df_amp[:,396]

# (optional) plot train & test
fig, ax=plt.subplots(1,2,figsize=(30, 6))
sns.distplot(X, ax=ax[0])
sns.distplot(y, ax=ax[1])

plt.show()

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 0)
r = sr.RReliefF(n_features = 20)
print(r.fit_transform(X_train,y_train))

nof_list=np.arange(1,20)            
high_score=0
nof=0           
score_list =[]
for n in range(len(nof_list)):
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 0)
    fs = sr.RReliefF(n_features = nof_list[n])
    relief = Pipeline([('fs', fs), ('m', RandomForestRegressor())])
    relief.fit(X_train,y_train)
    score = relief.score(X_test,y_test)
    score_list.append(score)
    print(f'NOF: {nof_list[n]}, Score: {score}')
    if(score > high_score):
        high_score = score
        nof = nof_list[n]

print (print(f'High Score: NOF: {nof}, Score: {high_score}'))