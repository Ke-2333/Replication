# -*- coding: utf-8 -*-
"""
Created on Mon May 17 13:54:16 2021
LassoShooting algorithm based on LassoShooting.ado

Version 2, 2021.06.11
New: defined the main function as 'LassoShooting'
     added codes about partialling out controls

Example:
betaPL, index = LassoShooting(y, X, controls = Noneverbose=0, lambda_=0, optTol=0.00001, maxIter=10000, zeroTol=0.0001, hetero = 1, lasIter=100, UpsTol=0.0001)
selX = X[:,index]
selX = nameX[index]
print(selXName)
print(betaPL)
"""

import pandas as pd
import numpy as np
from math import * 
from scipy import linalg
import statsmodels.api as sm

# =============================================================================
# #params
# verbose = 0
# optTol = 0.00001
# maxIter = 10000
# zeroTol = 0.0001
# lasIter = 100
# UpsTol = 0.0001
# hetero=1
# lambda_=0
# =============================================================================


#Solve linear systme using LU decomposition 
def lusolve(A,b):
    lu, piv = linalg.lu_factor(A)
    x = linalg.lu_solve((lu, piv), b)
    return x


#Define parameters for LASSO
def GetLambda(nUse,p,lambda_):
    if lambda_ == 0:
        mylam = 2.2*sqrt(2*nUse*log(2*p/(0.1/log(nUse))))
    else:
        mylam = lambda_
    return mylam

#Get penalty loadings
def MakeLassoWeights(v, XX, hetero=1):
    # v (n,1) colvector
    # XX (n,p) matrix
    # hetero 1 by default
    # return Ups (1,p) rowvector  
    
    nObs = v.shape[0]  # rows
    p = XX.shape[1]  # cols
    
    if hetero == 1:
        st = XX*v.dot(np.ones((1,p)))
        Ups = np.sqrt((st**2).sum(0)/nObs) 
    else:
        a = np.sqrt(((XX**2).sum(0)/nObs).reshape(1,-1))
        b = np.sqrt(((v**2).sum(0)/nObs).reshape(1,-1))
        Ups = np.dot(b.T, a)
    return Ups

#Get Lasso estimators
def DoLasso(y, X, Ups, lambda_, verbose=2, optTol=0.00001, maxIter=10000, zeroTol=0.0001):
    # y (n,ke)
    # X (n,p)
    #Ups (p,1) rowvector
    
    [n,p] = X.shape
    
    XX = (X.T).dot(X)  # (p,p)
    Xy = (X.T).dot(y)  # (p,ke)
    
    #OLS beta
    beta = lusolve((XX + lambda_*np.eye(p)), Xy) #(p,1)

    if(verbose == 2):
        w_old = beta
        print("%8s %8s %10s %14s %14s\n","iter","shoots","n(w)","n(step)","f(w)")
        k = 1
        wp = beta     
        
    m = 0
    XX2 = XX*2 # (p,p)
    Xy2 = Xy*2 # (p,ke)

    while(m < maxIter):      
        beta_old = beta.copy()
        
        for j in range(p):
            s0 = XX2[j,:].dot(beta) - XX2[j,j]*beta[j] - Xy2[j]
            if (s0 > lambda_*Ups[j]):
                beta[j] = (lambda_*Ups[j] - s0)/XX2[j,j]
            elif (s0 < -lambda_*Ups[j]):
                beta[j] = (-lambda_*Ups[j] - s0)/XX2[j,j]
            else:
                beta[j] = 0
        
        m = m + 1
        
        if(verbose == 2):
            print("%8.0g %8.0g %14.8e %14.8e %14.8e\n",m,m*p,abs(beta).sum(0),
                  abs(beta-w_old).sum(0),
                  ((X.dot(beta)-y)**2).sum(0)+lambda_*(abs(beta).sum(0)))
        
        if ((abs(beta-beta_old).sum(0)) < optTol):
            break
    
    if verbose:
        print("Number of iterations: %g\nTotal Shoots: %g\n",m,m*p)
        
    betaAll = beta
    index = np.where(abs(beta)>zeroTol)[0]
    beta = beta[index]
    SelX = X[:,index]
    
    SelXX = SelX.T.dot(SelX)
    SelXy = SelX.T.dot(y)

    if SelXX.size !=0:
        betaPL = lusolve(SelXX, SelXy)
    else:
        betaPL = []
        
    #nameXSel = nameX[index]
    #RealNameXSel = RealNameX[abs(beta)>zeroTol]
        
    return (betaAll, beta, betaPL, index)


#Iterations
def RunLasso(y, X, verbose=0, lambda_=0, optTol=0.00001, maxIter=10000, zeroTol=0.0001, hetero = 1, lasIter=100, UpsTol=0.0001):
    
    [n,p] = X.shape
    Ups = MakeLassoWeights(y, X, hetero)
    
    lambda_ = GetLambda(n, p, lambda_)
    
    lambda0 = 0.5*lambda_
    _, beta, betaPL, index = DoLasso(y, X, Ups, lambda0, verbose, optTol, maxIter, zeroTol)
    v = y - (X[:,index].dot(betaPL)).reshape(-1,1)
    
    oldUps = Ups.copy()
    Ups = MakeLassoWeights(v, X, hetero) #(p,1) rwovector
    UpsNorm = np.sqrt(((Ups - oldUps)**2).sum())   # ke x 1
    
    i = 1
    while (i<lasIter) & (UpsNorm > UpsTol):
        _, beta, betaPL, index = DoLasso(y,X, Ups, lambda_, verbose, optTol, maxIter, zeroTol)
        v = y - (X[:,index].dot(betaPL)).reshape(-1,1)
        
        oldUps = Ups.copy()
        Ups = MakeLassoWeights(v, X, hetero)
        UpsNorm = np.sqrt(((Ups - oldUps)**2).sum())   # ke x 1
        
        i = i+1
    
    return (betaPL, index)

#partial out controls
def ols_resid(y, X):
    model = sm.OLS(y, X)
    return (model.fit().resid).reshape(-1,1)

def LassoShooting(y, X, controls=np.array([]), verbose=0, lambda_=0, optTol=0.00001, maxIter=10000, zeroTol=0.0001, hetero = 1, lasIter=100, UpsTol=0.0001):

    if controls.shape[0] == 0:
        selBeta, index = RunLasso(y, X,verbose, lambda_, optTol, maxIter, zeroTol, hetero , lasIter, UpsTol)

    else:
        controls_cons = sm.add_constant(controls)
        y_resid = ols_resid(y, controls_cons)
        X_resid = ols_resid(X[:,0], controls_cons)
        for i in range(1,X.shape[1]):
            r = ols_resid(X[:,i], controls_cons)
            X_resid = np.c_[X_resid,r]
            
        selBeta, index = RunLasso(y_resid,X_resid,verbose, lambda_, optTol, maxIter, zeroTol, hetero , lasIter, UpsTol)

    
    return selBeta, index



# =============================================================================
# #IV Regression
# #pip install linearmodels
# from linearmodels.iv import IV2SLS
# ivs = df[selXName]
# 
# ivmodel = IV2SLS(df.CSIndex, None, df.NumProCase, ivs)
# iv = ivmodel.fit(cov_type = 'robust')  #by default is robust
# #first stage
# print(iv.first_stage)
# #second stage
# print(iv)
# =============================================================================

