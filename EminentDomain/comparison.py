# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:13:58 2021

@author: Administrator
"""

from FTIRE import ftire
import pandas as pd
import numpy as np
from math import * 
from scipy import linalg
from linearmodels.iv import IV2SLS

#import data
df = pd.read_excel('EminentDomain/CSExampleData.xlsx')
df = df.iloc[:,0:149]  #drop nControl
X = np.array(df.iloc[:,2:])  #IVs
y = np.array(df.iloc[:,1]).reshape(-1,1)  
nameX = df.columns[2:]
nameY = df.columns[1]
[n,p] = X.shape

#m = 5 if method == 'sir' else 30
#method = 'ft'
zeroTol = 0.0001
B_ft,_,lambcv_ft, maxLoss_ft = ftire.CV(X,y,1,30,'ft')
X_ft = np.dot(X, B_ft) 

#IV regression
ivmodel_ft = IV2SLS(df.CSIndex, None, df.NumProCase, X_ft)
result_ft = ivmodel_ft.fit(cov_type = 'robust')  #by default is robust
#first stage
print(result_ft.first_stage)
#second stage
print(result_ft.summary)
mse_ft = result_ft.resid_ss/result_ft.df_resid
print(mse_ft)

#method = 'sir'
B_sir,_,lambcv_sir,maxLoss_sir = ftire.CV(X,y,1,5,'sir')
X_sir = np.dot(X, B_sir)
#selected 93 IVs

#IV regression
ivmodel_sir = IV2SLS(df.CSIndex, None, df.NumProCase, X_sir)
result_sir = ivmodel_sir.fit(cov_type = 'robust')  #by default is robust
#first stage
print(result_sir.first_stage)
#second stage
print(result_sir.summary)
mse_sir = result_sir.resid_ss/result_sir.df_resid
print(mse_sir)


#LassoShooting, pl means 'post lasso'
import LassoShooting as la
selBeta_pl, index_pl = la.LassoShooting(y,X)
selX_pl = X[:,index_pl]
selXName_pl = nameX[index_pl]

#IV regression
iv_pl = df[selXName_pl]
ivmodel_pl = IV2SLS(df.CSIndex, None, df.NumProCase, iv_pl)
result_pl = ivmodel_pl.fit(cov_type = 'robust')  #by default is robust
#first stage
print(result_pl.first_stage)
#second stage
print(result_pl.summary)
mse_pl = result_pl.resid_ss/result_pl.df_resid
print(mse_pl)
