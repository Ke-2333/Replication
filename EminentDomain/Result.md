

[TOC]



## Summary

|                                   | 'ft'   | 'sir'  | Lasso    |
| :-------------------------------- | ------ | ------ | -------- |
| Selected Variables                |        |        | Z1xJDPSq |
| IV regression: Coef of NumProCase | 0.0200 | 0.0290 | 0.0668   |
| P-value for coef of NumProCase    | 0.6052 | 0.0802 | 0.0052   |
| MSE                               | 0.0026 | 0.0026 | 0.0028   |

For the IV regression, method 'ft' and lasso have similar results. Lasso gave a lower p value.

The method 'sir' failed in the IV regression. The selected instrument matrix does not have full column rank.

## Using ‘ft’

```
   First Stage Estimation Results    
======================================
                            NumProCase
--------------------------------------
R-squared                       0.0936
Partial R-squared               0.0936
Shea's R-squared                0.0936
Partial F-statistic             16.895
P-value (Partial F-stat)      3.95e-05
Partial F-stat Distn           chi2(1)
========================== ===========
instruments                    -0.1172
                             (-4.1104)
--------------------------------------

T-stats reported in parentheses
T-stats use same covariance type as original model

#second stage

print(result_ft.summary)
                          IV-2SLS Estimation Summary                          
==============================================================================
Dep. Variable:                CSIndex   R-squared:                      0.0067
Estimator:                    IV-2SLS   Adj. R-squared:                 0.0012
No. Observations:                 183   F-statistic:                    0.2672
Date:                Mon, Jun 07 2021   P-value (F-stat)                0.6052
Time:                        21:12:08   Distribution:                  chi2(1)
Cov. Estimator:                robust                                         
                                                                              
                             Parameter Estimates                              
==============================================================================
            Parameter  Std. Err.     T-stat    P-value    Lower CI    Upper CI
------------------------------------------------------------------------------
NumProCase     0.0200     0.0387     0.5169     0.6052     -0.0558      0.0957
==============================================================================

Endogenous: NumProCase
Instruments: instruments
Robust Covariance (Heteroskedastic)
Debiased: False
MSE: 0.00259297100692042
```



## Using 'sir'

```
First Stage Estimation Results    
======================================
                            NumProCase
--------------------------------------
R-squared                       0.5402
Partial R-squared               0.5402
Shea's R-squared                0.5402
Partial F-statistic             167.11
P-value (Partial F-stat)        0.0000
Partial F-stat Distn           chi2(1)
========================== ===========
instruments                    -0.3958
                             (-12.927)
--------------------------------------

T-stats reported in parentheses
T-stats use same covariance type as original model
                          IV-2SLS Estimation Summary                          
==============================================================================
Dep. Variable:                CSIndex   R-squared:                      0.0019
Estimator:                    IV-2SLS   Adj. R-squared:                -0.0035
No. Observations:                 183   F-statistic:                    3.0614
Date:                Mon, Jun 07 2021   P-value (F-stat)                0.0802
Time:                        21:24:29   Distribution:                  chi2(1)
Cov. Estimator:                robust                                         
                                                                              
                             Parameter Estimates                              
==============================================================================
            Parameter  Std. Err.     T-stat    P-value    Lower CI    Upper CI
------------------------------------------------------------------------------
NumProCase     0.0290     0.0166     1.7497     0.0802     -0.0035      0.0614
==============================================================================

Endogenous: NumProCase
Instruments: instruments
Robust Covariance (Heteroskedastic)
Debiased: False
```



## Lasso

Selected 1 variable: Z1xJDPSq

IV regression:

```
    First Stage Estimation Results    
======================================
                            NumProCase
--------------------------------------
R-squared                       0.1826
Partial R-squared               0.1826
Shea's R-squared                0.1826
Partial F-statistic             47.101
P-value (Partial F-stat)     6.742e-12
Partial F-stat Distn           chi2(1)
========================== ===========
Z1xJDPSq                        0.4495
                              (6.8630)
--------------------------------------

T-stats reported in parentheses
T-stats use same covariance type as original model

#second stage

                          IV-2SLS Estimation Summary                          
==============================================================================
Dep. Variable:                CSIndex   R-squared:                     -0.0704
Estimator:                    IV-2SLS   Adj. R-squared:                -0.0763
No. Observations:                 183   F-statistic:                    7.7963
Date:                Sat, May 29 2021   P-value (F-stat)                0.0052
Time:                        22:20:33   Distribution:                  chi2(1)
Cov. Estimator:                robust                                         
                                                                              
                             Parameter Estimates                              
==============================================================================
            Parameter  Std. Err.     T-stat    P-value    Lower CI    Upper CI
------------------------------------------------------------------------------
NumProCase     0.0668     0.0239     2.7922     0.0052      0.0199      0.1137
==============================================================================

Endogenous: NumProCase
Instruments: Z1xJDPSq
Robust Covariance (Heteroskedastic)
Debiased: False
MSE: 0.002794100989931522
```

