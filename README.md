
# VarClusHi

This is a Python module to perform variable clustering (varclus) with a hierarchical structure. Varclus is a nice dimension reduction algorithm. Here is a short description:

1. A cluster is chosen for splitting.
2. The chosen cluster is split into two clusters by finding the first two principal components, performing an orthoblique rotation, and assigning each variable to the rotated component with which it has the higher squared correlation.
3. Variables are iteratively reassigned to clusters to maximize the variance accounted for by the cluster components.


## Indented Audience:
- Those who are familar with the usage of varclus algorithm in other analytical software like SAS, but always feel distressed when trying to find a RIGHT python module.
- Pythoners who are new to varclus algorithm. The source code could help you gain a deep understanding of the math behind this algorithm.

## INSIGHTS & HIGHLIGHTS:
- (this is a pure theoretical part, ignore this bullet point does not affect the usage of VarClusHi package) Existing literatures always mention we need principal components (refer step 2-3 above). Actually, implementing this algorithm DOES NOT require principle components to be calulated, correlation matrix and its eigenvectors are enough to get the squared correlation between component and variable (this can be proved by math). If our dataset has millions of observations and hundreds of variables, not using principal components will save time and memory.
- Python package VarClusHi can produce very similar results, if we use SAS VARCLUS Procedure as a benchmark. This gurantees the correctness of the code. :)


# Example


 





## See [demo.ipynb](https://github.com/jingtt/varclushi/blob/master/demo.ipynb) for more details.


```python
import pandas as pd
from varclushi import VarClusHi
```

Create a VarClusHi object and pass the dataframe (df) to be analyzed as a parameter, you can also specify 
- a feature list (feat_list, default all columns of df)
- max second eigenvalue (maxeigval2, default 1)
- max clusters (maxclus, default None)

Then call method varclus(), which performs hierachical variable clustering algorithm

```python
demo1_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
demo1_df.drop('quality',axis=1,inplace=True)
demo1_vc = VarClusHi(demo1_df,maxeigval2=1,maxclus=None)
demo1_vc.varclus()
```
```
<varclushi.varclushi.VarClusHi at 0x15f96e35e10>
```
Call info, you can get the number of clusters, number of variables in each cluster (N_vars), variance explained by each cluster (Eigval1), etc.

```python
demo1_vc.info
```
```python
  Cluster N_Vars   Eigval1   Eigval2   VarProp
0       0      3  2.141357  0.658413  0.713786
1       1      3  1.766885  0.900991  0.588962
2       2      2  1.371260  0.628740  0.685630
3       3      2  1.552496  0.447504  0.776248
4       4      1  1.000000  0.000000  1.000000
```

Call rsquare, you can get the (1 - rsquare) ratio of each variable

```python
demo1_vc.rsquare
```

```python
   Cluster              Variable    RS_Own     RS_NC  RS_Ratio
0        0         fixed acidity  0.882210  0.277256  0.162976
1        0               density  0.622070  0.246194  0.501362
2        0                    pH  0.637076  0.194359  0.450478
3        1   free sulfur dioxide  0.777796  0.010358  0.224530
4        1  total sulfur dioxide  0.786660  0.042294  0.222761
5        1        residual sugar  0.202428  0.045424  0.835525
6        2             sulphates  0.685630  0.106022  0.351653
7        2             chlorides  0.685630  0.048903  0.330534
8        3           citric acid  0.776248  0.398208  0.371810
9        3      volatile acidity  0.776248  0.040920  0.233299
10       4               alcohol  1.000000  0.082055  0.000000
```



# Installation

- Requirements: Python 3.4+

- Install by pip:

```
pip install varclushi
```

# Other Comments:
- The parameters controlling this algorithm only include second eigenvalues and max number of clusters. I do not develop other functions because it is enough for my use. If you have a need for more flexibility, you can reach out to me via xuanjing@hotmail.com.

- Comments for source code will be added once I have time.


