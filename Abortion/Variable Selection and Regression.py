# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 16:57:17 2021

@author: Administrator
"""


import numpy as np
import pandas as pd
#import os
#os.chdir("F:\\!BENTLEY\\RA\\Replication")
import statsmodels.api as sm


df = pd.read_csv('Abortion/levitt_data_cleaned.csv')
cols = df.columns
#print(list(cols))

#define variables--------------------------------------------------------------

#controls
tdums = df.loc[:,'_Iyear_87':'_Iyear_97'] #(600,11)
tdumsCtrl = np.array(tdums)
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
violBeta1, violIndex1 = la.LassoShooting(Dyviol, AllViol_X, controls = tdumsCtrl)
AllViol.columns[violIndex1]
#[]
#stata: null

#second selection
violBeta2, violIndex2 = la.LassoShooting(Dviol, AllViol_X, controls = tdumsCtrl)
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
violResult.mse_resid


#Property Outcome--------------------------------------------------------------
propBeta1, propIndex1 = la.LassoShooting(Dyprop, AllProp_X, controls = tdumsCtrl)
AllProp.columns[propIndex1]
#['Mxxincome2Xt2', 'xxincome02Xt2']
#stata:Mxxincome2Xt2 xxincome02Xt2

propBeta2, propIndex2 = la.LassoShooting(Dprop, AllProp_X, controls = tdumsCtrl)
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
propResult.mse_resid


#Muder Outcome----------------------------------------------------------------
murdBeta1, murdIndex1 = la.LassoShooting(Dymurd, AllMurd_X, controls = tdumsCtrl)
AllMurd.columns[murdIndex1]
#[]
#stata: null

murdBeta2, murdIndex2 = la.LassoShooting(Dmurd, AllMurd_X, controls = tdumsCtrl)
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
murdResult.mse_resid



#using 'ft' and 'sir'
from FTIRE import ftire
#partial out controls
Dyviol_re = la.partial_out(Dyviol, tdumsCtrl)
Dviol_re = la.partial_out(Dviol, tdumsCtrl)
AllViol_X_re = la.partial_out(AllViol_X, tdumsCtrl)

Dyprop_re = la.partial_out(Dyprop, tdumsCtrl)
Dprop_re = la.partial_out(Dprop, tdumsCtrl)
AllProp_X_re = la.partial_out(AllProp_X, tdumsCtrl)

Dymurd_re = la.partial_out(Dymurd, tdumsCtrl)
Dmurd_re = la.partial_out(Dmurd, tdumsCtrl)
AllMurd_X_re = la.partial_out(AllMurd_X, tdumsCtrl)

# Using 'ft' twice-------------------------------------------------------------
# Violence outcome-------------------------------------------------------------
#'ft' first step
B_viol_ft1,_,_,_ = ftire.CV(AllViol_X_re,Dyviol_re,1,30,'ft')
viol_ft1 = np.dot(AllViol_X_re, B_viol_ft1)

#'ft' second step
B_vio_ft2,_,_,_ = ftire.CV(AllViol_X_re,Dviol_re,1,30,'ft')
viol_ft2 = np.dot(AllViol_X_re, B_viol_ft2)

X_viol_ft_reduced = pd.DataFrame(np.hstack([viol_ft1,viol_ft2]), columns = ['ft_viol1','ft_viol2'])

#regression
X_viol_ft = pd.concat([df['Dviol'],X_viol_ft_reduced,tdums], axis = 1) 
X_viol_ft = sm.add_constant(X_viol_ft)
viol_ft_reg = sm.OLS(df['Dyprop'],X_viol_ft).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
viol_ft_reg.summary()
viol_ft_reg.mse_resid

# Property outcome-------------------------------------------------------------
#'ft' first step
B_prop_ft1,_,_,_ = ftire.CV(AllProp_X_re,Dyprop_re,1,30,'ft')
prop_ft1 = np.dot(AllProp_X_re, B_prop_ft1)

#'ft' second step
B_prop_ft2,_,_,_ = ftire.CV(AllProp_X_re,Dprop_re,1,30,'ft')
prop_ft2 = np.dot(AllProp_X_re, B_ft2)

X_prop_ft_reduced = pd.DataFrame(np.hstack([prop_ft1,prop_ft2]), columns = ['ft_prop1','ft_prop2'])

#regression
X_prop_ft = pd.concat([df['Dprop'],X_prop_ft_reduced,tdums], axis = 1) 
X_prop_ft = sm.add_constant(X_prop_ft)
prop_ft_reg = sm.OLS(df['Dyprop'],X_prop_ft).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
prop_ft_reg.summary()
prop_ft_reg.mse_resid

# Murder outcome---------------------------------------------------------------
B_murd_ft1,_,_,_ = ftire.CV(AllMurd_X_re,Dymurd_re,1,30,'ft')
murd_ft1 = np.dot(AllMurd_X_re, B_murd_ft1)

#'ft' second step
B_murd_ft2,_,_,_ = ftire.CV(AllMurd_X_re,Dmurd_re,1,30,'ft')
murd_ft2 = np.dot(AllMurd_X_re, B_ft2)

X_murd_ft_reduced = pd.DataFrame(np.hstack([murd_ft1,murd_ft2]), columns = ['ft_murd1','ft_murd2'])

#regression
X_murd_ft = pd.concat([df['Dmurd'],X_murd_ft_reduced,tdums], axis = 1) 
X_murd_ft = sm.add_constant(X_murd_ft)
murd_ft_reg = sm.OLS(df['Dymurd'],X_murd_ft).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
murd_ft_reg.summary()
murd_ft_reg.mse_resid


#Using 'ft' once---------------------------------------------------------------
# Violence Outcome-------------------------------------------------------------
B_viol_ft_V2,_,_,_ = ftire.CV(AllViol_X_re,np.hstack([Dyviol_re,Dviol_re]),1,30,'ft')
viol_ft_V2 = np.dot(AllViol_X_re, B_viol_ft_V2)
X_viol_ft_reducedV2 = pd.DataFrame(viol_ft_V2, columns = ['ft_viol_V2'])

X_viol_ft_V2 = pd.concat([df['Dviol'],X_viol_ft_reducedV2,tdums], axis = 1) 
X_viol_ft_V2 = sm.add_constant(X_viol_ft_V2)
viol_ft_reg_V2 = sm.OLS(df['Dyprop'],X_viol_ft_V2).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
viol_ft_reg_V2.summary()
viol_ft_reg_V2.mse_resid

# Property Outcome-------------------------------------------------------------
B_prop_ft_V2,_,_,_ = ftire.CV(AllProp_X_re,np.hstack([Dyprop_re,Dprop_re]),1,30,'ft')
prop_ft_V2 = np.dot(AllProp_X_re, B_prop_ft_V2)
X_prop_ft_reducedV2 = pd.DataFrame(prop_ft_V2, columns = ['ft_prop_V2'])

X_prop_ft_V2 = pd.concat([df['Dprop'],X_prop_ft_reducedV2,tdums], axis = 1) 
X_prop_ft_V2 = sm.add_constant(X_prop_ft_V2)
prop_ft_reg_V2 = sm.OLS(df['Dyprop'],X_prop_ft_V2).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
prop_ft_reg_V2.summary()
prop_ft_reg_V2.mse_resid

# Murder Outcome---------------------------------------------------------------
B_murd_ft_V2,_,_,_ = ftire.CV(AllMurd_X_re,np.hstack([Dymurd_re,Dmurd_re]),1,30,'ft')
murd_ft_V2 = np.dot(AllMurd_X_re, B_murd_ft_V2)
X_murd_ft_reducedV2 = pd.DataFrame(murd_ft_V2, columns = ['ft_murd_V2'])

X_murd_ft_V2 = pd.concat([df['Dmurd'],X_murd_ft_reducedV2,tdums], axis = 1) 
X_murd_ft_V2 = sm.add_constant(X_murd_ft_V2)
murd_ft_reg_V2 = sm.OLS(df['Dymurd'],X_murd_ft_V2).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
murd_ft_reg_V2.summary()
murd_ft_reg_V2.mse_resid


#Using 'sir'-------------------------------------------------------------------
# Violence outcome-------------------------------------------------------------
#'sir' first step
B_viol_sir1,_,_,_ = ftire.CV(AllViol_X_re,Dyviol_re,1,5,'sir')
viol_sir1 = np.dot(AllViol_X_re, B_viol_sir1)

#'sir' second step
B_viol_sir2,_,_,_ = ftire.CV(AllViol_X_re,Dviol_re,1,5,'sir')
viol_sir2 = np.dot(AllViol_X_re, B_viol_sir2)

X_viol_sir_reduced = pd.DataFrame(np.hstack([viol_sir1,viol_sir2]), columns = ['sir_viol1','sir_viol2'])

#regression
X_viol_sir = pd.concat([df['Dviol'],X_viol_sir_reduced,tdums], axis = 1) 
X_viol_sir = sm.add_constant(X_viol_sir)
viol_sir_reg = sm.OLS(df['Dyprop'],X_viol_sir).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
viol_sir_reg.summary()
viol_sir_reg.mse_resid

# Property outcome-------------------------------------------------------------
#'sir' first step
B_prop_sir1,_,_,_ = ftire.CV(AllProp_X_re,Dyprop_re,1,5,'sir')
prop_sir1 = np.dot(AllProp_X_re, B_prop_sir1)

#'sir' second step
B_prop_sir2,_,_,_ = ftire.CV(AllProp_X_re,Dprop_re,1,5,'sir')
prop_sir2 = np.dot(AllProp_X_re, B_prop_sir2)

X_prop_sir_reduced = pd.DataFrame(np.hstack([prop_sir1,prop_sir2]), columns = ['sir_prop1','sir_prop2'])

#regression
X_prop_sir = pd.concat([df['Dprop'],X_prop_sir_reduced,tdums], axis = 1) 
X_prop_sir = sm.add_constant(X_prop_sir)
prop_sir_reg = sm.OLS(df['Dyprop'],X_prop_sir).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
prop_sir_reg.summary()
prop_sir_reg.mse_resid


# Murder outcome---------------------------------------------------------------
#'sir' first step
B_murd_sir1,_,_,_ = ftire.CV(AllMurd_X_re,Dymurd_re,1,5,'sir')
murd_sir1 = np.dot(AllMurd_X_re, B_murd_sir1)

#'sir' second step
B_murd_sir2,_,_,_ = ftire.CV(AllMurd_X_re,Dmurd_re,1,5,'sir')
murd_sir2 = np.dot(AllMurd_X_re, B_murd_sir2)

X_murd_sir_reduced = pd.DataFrame(np.hstack([murd_sir1,murd_sir2]), columns = ['sir_murd1','sir_murd2'])

#regression
X_murd_sir = pd.concat([df['Dmurd'],X_murd_sir_reduced,tdums], axis = 1) 
X_murd_sir = sm.add_constant(X_murd_sir)
murd_sir_reg = sm.OLS(df['Dymurd'],X_murd_sir).fit(cov_type='cluster',
                                             cov_kwds={'groups':df['statenum']})
murd_sir_reg.summary()
murd_sir_reg.mse_resid
