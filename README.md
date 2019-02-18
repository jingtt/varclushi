# VarClusHi

This is a Python module to perform variable clustering with a hierarchical structure. Varclus is a nice dimension reduction algorithm. Here is a short description:

1. A cluster is chosen for splitting.
2. The chosen cluster is split into two clusters by finding the first two principal components, performing an orthoblique rotation, and assigning each variable to the rotated component with which it has the higher squared correlation.
3. Variables are iteratively reassigned to clusters to maximize the variance accounted for by the cluster components.


## Indented Audience:
- Those who are familar with the usage of varclus algorithm in other analytical software like SAS, but always feel distressed when trying to find a RIGHT python module.
- Pythoners who are new to varclus algorithm. The source code will help you gain a deeper understanding of the math behind this algorithm.

## INSIGHTS and HIGHLIGHTS:
- Existing literatures always mention we should use principal components (refer step 2-3 above). Actually, implementing this algorithm DOES NOT require principle components to be calulated, correlation matrix and its eigenvectors are enough to get the squared correlation between component and variable (this can be proved by math). If our dataset has millions of observations and hundreds of variables, not using principal components will save time and memory.
- Always correct, with professional SAS results as benchmark.



# Example

See [demo.ipynb](https://github.com/jingtt/varclushi/blob/master/demo.ipynb) for more details.

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



# Installation

Requirements: Python 3.4+

```
pip3 install varclushi
```

# Comments:
- There are not many parameters controlling this algorithm, only second eigenvalues (maxeigval2, default 1) and max number of clusters (maxclus, default None). I do not develop other functions because it is enough for my use. If you have a need for more flexibility, you can reach out to me via xuanjing@hotmail.com.

- Comments for source code will be added once I have time.

# Thanks

Thank my former manager, I first heard of this method from him. Thank my current manager, who gave me enough encouragement and support to complete this project.


 
