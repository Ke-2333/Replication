# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 16:57:17 2021

@author: Administrator
"""


import numpy as np
import pandas as pd
import os
os.chdir("F:\\!BENTLEY\\RA\\Replication")
import statsmodels.api as sm


df = pd.read_csv('Abortion/levitt_data_cleaned.csv')
cols = df.columns
#print(list(cols))

#define variables--------------------------------------------------------------

#controls
tdums = df.loc[:,'_Iyear_87':'_Iyear_97'] #(600,11)
tdums_con = np.array(tdums)
# =============================================================================
# ['_Iyear_87', '_Iyear_88', '_Iyear_89', '_Iyear_90', '_Iyear_91',
#  '_Iyear_92', '_Iyear_93', '_Iyear_94', '_Iyear_95', '_Iyear_96', '_Iyear_97']
# =============================================================================

#Violence
contviol = df.loc[:, 'viol0':'Dviol02Xt2'] #(600,12)
# =============================================================================
# ['viol0', 'Dviol0', 'viol02', 'Dviol02', 'viol0Xt', 'viol0Xt2', 
#  'viol02Xt', 'viol02Xt2', 'Dviol0Xt', 'Dviol0Xt2', 'Dviol02Xt', 'Dviol02Xt2']
# =============================================================================

#Property
contprop = df.loc[:, 'prop0':'Dprop02Xt2'] #(600,12)
# =============================================================================
# ['prop0', 'Dprop0', 'prop02', 'Dprop02', 'prop0Xt', 'prop0Xt2', 
#  'prop02Xt', 'prop02Xt2', 'Dprop0Xt', 'Dprop0Xt2', 'Dprop02Xt', 'Dprop02Xt2']
# =============================================================================

#Murder
contmurd = df.loc[:, 'murd0':'Dmurd02Xt2']  #(600,12)
# =============================================================================
# ['murd0', 'Dmurd0', 'murd02', 'Dmurd02', 'murd0Xt', 'murd0Xt2', 'murd02Xt', 
#  'murd02Xt2', 'Dmurd0Xt', 'Dmurd0Xt2', 'Dmurd02Xt', 'Dmurd02Xt2']
# =============================================================================

#Shared variables
shared = df.loc[:, 'Dxxprison': 'xxbeer02Xt2']  #(600,300)

#Instruments for Violence, Property, and Murder
AllViol = pd.concat([contviol,shared], axis = 1) #(600,312)
AllProp = pd.concat([contprop,shared], axis = 1) #(600,312)
AllMurd = pd.concat([contmurd,shared], axis = 1) #(600,312)

AllViol_X = np.array(AllViol)
AllProp_X = np.array(AllProp)
AllMurd_X = np.array(AllMurd)

#The response & the endogenous variable
Dyviol = np.array(df['Dyviol']).reshape(-1,1)
Dviol = np.array(df['Dviol']).reshape(-1,1)

Dyprop = np.array(df['Dyprop']).reshape(-1,1)
Dprop = np.array(df['Dprop']).reshape(-1,1)

Dymurd = np.array(df['Dymurd']).reshape(-1,1)
Dmurd = np.array(df['Dmurd']).reshape(-1,1)

#LassoShooting
import LassoShooting as la

#Violence Outcome--------------------------------------------------------------
#first selection
violBeta1, violIndex1 = la.LassoShooting(Dyviol, AllViol_X, controls = tdums_con)
AllViol.columns[violIndex1]
#[]
#stata: null

#second selection
violBeta2, violIndex2 = la.LassoShooting(Dviol, AllViol_X, controls = tdums_con)
AllViol.columns[violIndex2]
#['viol0', 'Lxxprison', 'Lxxpolice', 'Mxxincome', 'Dxxincome0','LxxpoliceXt', 'MxxincomeXt', 'Dxxincome0Xt', 'Dxxbeer0Xt'],
#stata :viol0 Lxxprison Lxxpolice Mxxincome Dxxincome0 LxxpoliceXt MxxincomeXt Dxxincome0Xt Dxxbeer0Xt

#union selected variables
violIndexAll = np.unique(np.r_[violIndex1,violIndex2])
violSelAll = AllViol.iloc[:,violIndexAll]  #(600,9)

#regression
#Our model needs an intercept so we add a column of 1s
X_viol = pd.concat([df['Dviol'],violSelAll,tdums], axis = 1) 
X_viol = sm.add_constant(X_viol)
violResult = sm.OLS(df['Dyviol'],X_viol).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
violResult.summary()


#Property Outcome--------------------------------------------------------------
propBeta1, propIndex1 = la.LassoShooting(Dyprop, AllProp_X, controls = tdums_con)
propSel1 = AllProp.columns[propIndex1]
#['Mxxincome2Xt2', 'xxincome02Xt2']
#stata:Mxxincome2Xt2 xxincome02Xt2

propBeta2, propIndex2 = la.LassoShooting(Dprop, AllProp_X, controls = tdums_con)
AllProp.columns[propIndex2]
#['prop0', 'Lxxprison', 'Lxxpolice', 'Lxxincome', 'Mxxincome', 'Dxxincome0', 'Dxxincome0Xt']
#stata:prop0 Lxxprison Lxxpolice Lxxincome Mxxincome Dxxincome0 Dxxincome0Xt

propIndexAll = np.unique(np.r_[propIndex1,propIndex2])
propSelAll = AllProp.iloc[:,propIndexAll]  #(600,9)

#regression
X_prop = pd.concat([df['Dprop'],propSelAll,tdums], axis = 1) 
X_prop = sm.add_constant(X_prop)
propResult = sm.OLS(df['Dyprop'],X_prop).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
propResult.summary()


#Muder Outcome----------------------------------------------------------------
murdBeta1, murdIndex1 = la.LassoShooting(Dymurd, AllMurd_X, controls = tdums_con)
AllMurd.columns[murdIndex1]
#[]
#stata: null

murdBeta2, murdIndex2 = la.LassoShooting(Dmurd, AllMurd_X, controls = tdums_con)
AllMurd.columns[murdIndex2]
#['murd0', 'murd0Xt', 'Lxxprison', 'LxxprisonXt', 'LxxpoliceXt','MxxincomeXt', 'Dxxincome0Xt']
#stata:murd0 murd0Xt Lxxprison LxxprisonXt LxxpoliceXt MxxincomeXt Dxxincome0Xt

murdIndexAll = np.unique(np.r_[murdIndex1,murdIndex2])
murdSelAll = AllMurd.iloc[:,murdIndexAll]  #(600,7)

#regression
X_murd = pd.concat([df['Dmurd'],murdSelAll,tdums], axis = 1) 
X_murd = sm.add_constant(X_murd)
murdResult = sm.OLS(df['Dymurd'],X_murd).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
murdResult.summary()






