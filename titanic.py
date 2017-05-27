#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 01:05:56 2017

@author: anirban727
"""

from IPython.core.display import HTML
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

pd.options.display.max_rows = 100
pd.options.display.max_columns = 100

data = pd.read_csv('/home/anirban727/Downloads/Kaggle Titanic/train.csv')

data['Age'].fillna(data['Age'].median(), inplace = True)

# plotting survival with sex  
survived_sex = data[data['Survived'] == 1]['Sex'].value_counts()
dead_sex     = data[data['Survived'] == 0]['Sex'].value_counts()
df1 = pd.DataFrame([survived_sex, dead_sex])
df1.index = ['Survived','Dead']
df1.plot(kind = 'bar', stacked = True, figsize = (10,8))
##  clearly shows that females survived more than males

# plotting survival with age

plt.figure(figsize = (20,8))
survived_age = data[data['Survived'] == 1]['Age']
dead_age     = data[data['Survived'] == 0]['Age']
plt.hist([survived_age, dead_age], bins = 50, stacked = True, rwidth = 0.8,
         color = ['g','r'], label = ['Survived','Dead'])
plt.xlabel('Age')
plt.ylabel('No. of passengers')
plt.grid(True)
plt.legend()
## shows that people belonging to age group 27-29 died the most

#plotting survival with 

















