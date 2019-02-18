# VarClusHi

This is a Python module to perform variable clustering with a hierarchical structure. Varclus is a nice dimension reduction algorithm. Here is a short description:

1. A cluster is chosen for splitting.
2. The chosen cluster is split into two clusters by finding the first two principal components, performing an orthoblique rotation, and assigning each variable to the rotated component with which it has the higher squared correlation.
3. Variables are iteratively reassigned to clusters to maximize the variance accounted for by the cluster components.


## Indented Audience:
- Those who are familar with the usage of varclus algorithm in other analytical software like SAS, but always feel distressed when trying to find a RIGHT python version.
- Pythoners who are new to varclus algorithm. The source code will help you gain a deeper understanding of the math behind this algorithm.

## HIGHLIGHTS:
- Existing literature only mentioned use principal components to (refer step 2-3 above). Actually, we DO NOT need to compute principle components at all, correlation matrix and its eigenvectors are enough to calculate the squared correlation between variable and component. If our dataset has millions of observations and hundreds of variables, not calculating principal components will save time and memory.
- Always correct, with professional SAS results as benchmark.

## The shortcomings of this project are:
- 




# Example

```python
import pandas as pd
from varclushi import VarClusHi
```


```python
demo1_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
demo1_df.drop('quality',axis=1,inplace=True)
demo1_vc = VarClusHi(demo1_df)
demo1_vc.varclus()
```

<varclushi.varclushi.VarClusHi at 0x15f96e35e10>




```python
demo1_vc.info
```

```python
demo1_vc.rsqure
```



# Knowledge beyond



# Installation

Requirements: Python 3.4+

```
pip3 install varclushi
```
 
