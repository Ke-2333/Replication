[TOC]



## Violence Abortion

```
violResult.summary()
Out[28]: 
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Dyviol   R-squared:                       0.271
Model:                            OLS   Adj. R-squared:                  0.245
Method:                 Least Squares   F-statistic:                     31.19
Date:                Tue, 15 Jun 2021   Prob (F-statistic):           1.93e-21
Time:                        22:16:20   Log-Likelihood:                 744.34
No. Observations:                 600   AIC:                            -1445.
Df Residuals:                     578   BIC:                            -1348.
Df Model:                          21                                         
Covariance Type:              cluster                                         
================================================================================
                   coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------
const           -0.4480      0.586     -0.765      0.445      -1.596       0.700
Dviol           -0.1711      0.117     -1.463      0.143      -0.400       0.058
viol0            0.0802      0.106      0.757      0.449      -0.127       0.288
Lxxprison        0.0098      0.009      1.121      0.262      -0.007       0.027
Lxxpolice       -0.0208      0.043     -0.484      0.628      -0.105       0.063
Mxxincome        5.8181      6.796      0.856      0.392      -7.502      19.138
Dxxincome0     -22.9624     39.821     -0.577      0.564    -101.011      55.086
LxxpoliceXt     -0.0475      0.058     -0.823      0.411      -0.161       0.066
MxxincomeXt     -6.0524      9.590     -0.631      0.528     -24.848      12.743
Dxxincome0Xt    21.1692     62.794      0.337      0.736    -101.905     144.244
Dxxbeer0Xt       1.2770      0.592      2.157      0.031       0.117       2.437
_Iyear_87       -0.0268      0.083     -0.322      0.747      -0.190       0.136
_Iyear_88        0.0916      0.157      0.585      0.559      -0.216       0.399
_Iyear_89        0.1464      0.236      0.620      0.535      -0.316       0.609
_Iyear_90        0.2561      0.314      0.815      0.415      -0.360       0.872
_Iyear_91        0.2631      0.385      0.683      0.494      -0.492       1.018
_Iyear_92        0.2963      0.467      0.635      0.526      -0.619       1.212
_Iyear_93        0.3427      0.543      0.632      0.528      -0.721       1.406
_Iyear_94        0.3720      0.620      0.600      0.548      -0.843       1.587
_Iyear_95        0.4306      0.696      0.618      0.536      -0.934       1.795
_Iyear_96        0.4361      0.774      0.563      0.573      -1.081       1.954
_Iyear_97        0.5345      0.849      0.630      0.529      -1.129       2.198
==============================================================================
Omnibus:                       65.969   Durbin-Watson:                   1.991
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              189.029
Skew:                          -0.533   Prob(JB):                     8.97e-42
Kurtosis:                       5.535   Cond. No.                     3.23e+04
==============================================================================

Warnings:
[1] Standard Errors are robust to cluster correlation (cluster)
[2] The condition number is large, 3.23e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
"""







propResult.summary()
Out[29]: 
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Dyprop   R-squared:                       0.264
Model:                            OLS   Adj. R-squared:                  0.237
Method:                 Least Squares   F-statistic:                     32.90
Date:                Tue, 15 Jun 2021   Prob (F-statistic):           5.91e-22
Time:                        22:16:25   Log-Likelihood:                 1005.6
No. Observations:                 600   AIC:                            -1967.
Df Residuals:                     578   BIC:                            -1870.
Df Model:                          21                                         
Covariance Type:              cluster                                         
=================================================================================
                    coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------
const             0.2439      0.214      1.137      0.255      -0.176       0.664
Dprop            -0.0611      0.057     -1.063      0.288      -0.174       0.052
prop0            -0.0124      0.020     -0.636      0.525      -0.051       0.026
Lxxprison         0.0122      0.004      3.011      0.003       0.004       0.020
Lxxpolice        -0.0140      0.010     -1.472      0.141      -0.033       0.005
Lxxincome        36.2695      8.323      4.358      0.000      19.956      52.583
Mxxincome       -37.9860      8.710     -4.361      0.000     -55.056     -20.916
Dxxincome0       48.6654     22.371      2.175      0.030       4.819      92.512
Mxxincome2Xt2   -22.1146     63.892     -0.346      0.729    -147.341     103.112
Dxxincome0Xt    -61.5560     46.047     -1.337      0.181    -151.807      28.695
xxincome02Xt2     0.7056     56.330      0.013      0.990    -109.698     111.110
_Iyear_87        -0.0241      0.010     -2.445      0.014      -0.043      -0.005
_Iyear_88        -0.0368      0.016     -2.369      0.018      -0.067      -0.006
_Iyear_89        -0.0178      0.024     -0.754      0.451      -0.064       0.028
_Iyear_90        -0.0075      0.036     -0.207      0.836      -0.078       0.063
_Iyear_91         0.0114      0.050      0.228      0.820      -0.087       0.109
_Iyear_92        -0.0190      0.070     -0.270      0.787      -0.157       0.119
_Iyear_93         0.0073      0.090      0.080      0.936      -0.170       0.185
_Iyear_94         0.0595      0.115      0.516      0.606      -0.166       0.285
_Iyear_95         0.0894      0.145      0.617      0.537      -0.195       0.373
_Iyear_96         0.0622      0.176      0.354      0.723      -0.282       0.406
_Iyear_97         0.0995      0.210      0.475      0.635      -0.311       0.510
==============================================================================
Omnibus:                       62.372   Durbin-Watson:                   2.128
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              335.923
Skew:                          -0.241   Prob(JB):                     1.14e-73
Kurtosis:                       6.634   Cond. No.                     1.08e+05
==============================================================================

Warnings:
[1] Standard Errors are robust to cluster correlation (cluster)
[2] The condition number is large, 1.08e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""

murdResult.summary()
Out[30]: 
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Dymurd   R-squared:                       0.051
Model:                            OLS   Adj. R-squared:                  0.020
Method:                 Least Squares   F-statistic:                     7.392
Date:                Tue, 15 Jun 2021   Prob (F-statistic):           8.55e-09
Time:                        22:16:28   Log-Likelihood:                -32.921
No. Observations:                 600   AIC:                             105.8
Df Residuals:                     580   BIC:                             193.8
Df Model:                          19                                         
Covariance Type:              cluster                                         
================================================================================
                   coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------
const            0.0517      0.056      0.929      0.353      -0.057       0.161
Dmurd           -0.1888      0.177     -1.066      0.287      -0.536       0.158
murd0            2.6535      1.200      2.212      0.027       0.302       5.004
murd0Xt         -3.8798      2.259     -1.718      0.086      -8.307       0.548
Lxxprison        0.0028      0.026      0.104      0.917      -0.049       0.055
LxxprisonXt      0.0122      0.046      0.265      0.791      -0.078       0.102
LxxpoliceXt     -0.0695      0.046     -1.499      0.134      -0.160       0.021
MxxincomeXt      1.0285      6.409      0.160      0.872     -11.532      13.589
Dxxincome0Xt   -16.4394     35.113     -0.468      0.640     -85.259      52.380
_Iyear_87       -0.0948      0.089     -1.068      0.286      -0.269       0.079
_Iyear_88       -0.0707      0.114     -0.620      0.535      -0.294       0.153
_Iyear_89       -0.0689      0.185     -0.373      0.709      -0.431       0.293
_Iyear_90       -0.0199      0.218     -0.091      0.927      -0.448       0.408
_Iyear_91       -0.0399      0.278     -0.144      0.886      -0.584       0.504
_Iyear_92       -0.0957      0.324     -0.295      0.768      -0.731       0.540
_Iyear_93        0.0220      0.375      0.059      0.953      -0.712       0.757
_Iyear_94       -0.1747      0.442     -0.395      0.693      -1.041       0.692
_Iyear_95       -0.0440      0.476     -0.092      0.926      -0.977       0.890
_Iyear_96       -0.1236      0.545     -0.227      0.821      -1.192       0.945
_Iyear_97       -0.1467      0.591     -0.248      0.804      -1.306       1.013
==============================================================================
Omnibus:                      209.790   Durbin-Watson:                   2.872
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             9317.381
Skew:                          -0.770   Prob(JB):                         0.00
Kurtosis:                      22.244   Cond. No.                     1.24e+04
==============================================================================

Warnings:
[1] Standard Errors are robust to cluster correlation (cluster)
[2] The condition number is large, 1.24e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
```



## Property Abortion

```
propResult.summary()
Out[29]: 
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Dyprop   R-squared:                       0.264
Model:                            OLS   Adj. R-squared:                  0.237
Method:                 Least Squares   F-statistic:                     32.90
Date:                Tue, 15 Jun 2021   Prob (F-statistic):           5.91e-22
Time:                        22:16:25   Log-Likelihood:                 1005.6
No. Observations:                 600   AIC:                            -1967.
Df Residuals:                     578   BIC:                            -1870.
Df Model:                          21                                         
Covariance Type:              cluster                                         
=================================================================================
                    coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------
const             0.2439      0.214      1.137      0.255      -0.176       0.664
Dprop            -0.0611      0.057     -1.063      0.288      -0.174       0.052
prop0            -0.0124      0.020     -0.636      0.525      -0.051       0.026
Lxxprison         0.0122      0.004      3.011      0.003       0.004       0.020
Lxxpolice        -0.0140      0.010     -1.472      0.141      -0.033       0.005
Lxxincome        36.2695      8.323      4.358      0.000      19.956      52.583
Mxxincome       -37.9860      8.710     -4.361      0.000     -55.056     -20.916
Dxxincome0       48.6654     22.371      2.175      0.030       4.819      92.512
Mxxincome2Xt2   -22.1146     63.892     -0.346      0.729    -147.341     103.112
Dxxincome0Xt    -61.5560     46.047     -1.337      0.181    -151.807      28.695
xxincome02Xt2     0.7056     56.330      0.013      0.990    -109.698     111.110
_Iyear_87        -0.0241      0.010     -2.445      0.014      -0.043      -0.005
_Iyear_88        -0.0368      0.016     -2.369      0.018      -0.067      -0.006
_Iyear_89        -0.0178      0.024     -0.754      0.451      -0.064       0.028
_Iyear_90        -0.0075      0.036     -0.207      0.836      -0.078       0.063
_Iyear_91         0.0114      0.050      0.228      0.820      -0.087       0.109
_Iyear_92        -0.0190      0.070     -0.270      0.787      -0.157       0.119
_Iyear_93         0.0073      0.090      0.080      0.936      -0.170       0.185
_Iyear_94         0.0595      0.115      0.516      0.606      -0.166       0.285
_Iyear_95         0.0894      0.145      0.617      0.537      -0.195       0.373
_Iyear_96         0.0622      0.176      0.354      0.723      -0.282       0.406
_Iyear_97         0.0995      0.210      0.475      0.635      -0.311       0.510
==============================================================================
Omnibus:                       62.372   Durbin-Watson:                   2.128
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              335.923
Skew:                          -0.241   Prob(JB):                     1.14e-73
Kurtosis:                       6.634   Cond. No.                     1.08e+05
==============================================================================

Warnings:
[1] Standard Errors are robust to cluster correlation (cluster)
[2] The condition number is large, 1.08e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
```



## Murder Abortion

```
murdResult.summary()
Out[30]: 
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Dymurd   R-squared:                       0.051
Model:                            OLS   Adj. R-squared:                  0.020
Method:                 Least Squares   F-statistic:                     7.392
Date:                Tue, 15 Jun 2021   Prob (F-statistic):           8.55e-09
Time:                        22:16:28   Log-Likelihood:                -32.921
No. Observations:                 600   AIC:                             105.8
Df Residuals:                     580   BIC:                             193.8
Df Model:                          19                                         
Covariance Type:              cluster                                         
================================================================================
                   coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------
const            0.0517      0.056      0.929      0.353      -0.057       0.161
Dmurd           -0.1888      0.177     -1.066      0.287      -0.536       0.158
murd0            2.6535      1.200      2.212      0.027       0.302       5.004
murd0Xt         -3.8798      2.259     -1.718      0.086      -8.307       0.548
Lxxprison        0.0028      0.026      0.104      0.917      -0.049       0.055
LxxprisonXt      0.0122      0.046      0.265      0.791      -0.078       0.102
LxxpoliceXt     -0.0695      0.046     -1.499      0.134      -0.160       0.021
MxxincomeXt      1.0285      6.409      0.160      0.872     -11.532      13.589
Dxxincome0Xt   -16.4394     35.113     -0.468      0.640     -85.259      52.380
_Iyear_87       -0.0948      0.089     -1.068      0.286      -0.269       0.079
_Iyear_88       -0.0707      0.114     -0.620      0.535      -0.294       0.153
_Iyear_89       -0.0689      0.185     -0.373      0.709      -0.431       0.293
_Iyear_90       -0.0199      0.218     -0.091      0.927      -0.448       0.408
_Iyear_91       -0.0399      0.278     -0.144      0.886      -0.584       0.504
_Iyear_92       -0.0957      0.324     -0.295      0.768      -0.731       0.540
_Iyear_93        0.0220      0.375      0.059      0.953      -0.712       0.757
_Iyear_94       -0.1747      0.442     -0.395      0.693      -1.041       0.692
_Iyear_95       -0.0440      0.476     -0.092      0.926      -0.977       0.890
_Iyear_96       -0.1236      0.545     -0.227      0.821      -1.192       0.945
_Iyear_97       -0.1467      0.591     -0.248      0.804      -1.306       1.013
==============================================================================
Omnibus:                      209.790   Durbin-Watson:                   2.872
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             9317.381
Skew:                          -0.770   Prob(JB):                         0.00
Kurtosis:                      22.244   Cond. No.                     1.24e+04
==============================================================================

Warnings:
[1] Standard Errors are robust to cluster correlation (cluster)
[2] The condition number is large, 1.24e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
```

