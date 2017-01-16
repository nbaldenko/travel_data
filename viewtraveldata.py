# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd

import json

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
#matplotlib inline

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

#load data
purchases_df = pd.read_csv('/Users/nicolasbaldenko/Documents/Projects/Apps/travel_data_flask/data/Trip_Expenses_Dec_Jan.csv')

#recategorize anything called "Food" to be called "Groceries"
purchases_df.loc[purchases_df.Category == 'Food', "Category"] = 'Groceries'
purchases_df.loc[purchases_df.Category == 'Misc', "Category"] = 'Miscellaneous'
#make all costs positive
purchases_df.loc[:,"Amount"] *= -1



sum_by_cat = purchases_df.groupby(by=['Category'])['Amount'].sum()
sum_by_cat.plot(kind = "bar")
plt.figure()
sum_by_cat.plot(kind = "pie")
