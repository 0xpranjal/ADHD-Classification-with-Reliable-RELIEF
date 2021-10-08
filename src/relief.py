#https://www.kaggle.com/jorgesandoval/feature-selection-with-rrelieff-regression
# Base Libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import datasets
import pandas as pd
# Feature Selection
import sklearn_relief as sr

#example of 2 class problem
data = np.array([[9,2,2],[5,1,0],[9,3,2],[8,3,1],[6,0,0]])
target = np.array([0,0,1,1,1])

r = sr.Relief(n_features = 2)
X_train = r.fit_transform(data, target)
print(X_train)
print("--------------")
print("(No. of tuples, No. of Columns before Relief) : "+str(data.shape)+
      "\n(No. of tuples , No. of Columns after Relief) : "+str(X_train.shape))


#example of multi class problem
iris = datasets.load_iris()
X = iris.data
Y = iris.target

fs = sr.ReliefF(n_features = 2)
X_train = fs.fit_transform(X, Y)
print("(No. of tuples, No. of Columns before ReliefF) : "+str(iris.data.shape)+
      "\n(No. of tuples, No. of Columns after ReliefF) : "+str(X_train.shape))


#example of multi class problem
iris = datasets.load_iris()
X = iris.data
Y = iris.target

fs = sr.RReliefF(n_features = 2)
X_train = fs.fit_transform(X, Y)
print("(No. of tuples, No. of Columns before RReliefF) : "+str(iris.data.shape)+
      "\n(No. of tuples, No. of Columns after RReliefF) : "+str(X_train.shape))
