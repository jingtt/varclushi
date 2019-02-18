# VarClusHi

This is a Python module to perform variable clustering with a hierarchical structure. Varclus is a nice dimension reduction algorithm.

The audience of this project might be:
- Those who are familar with the usage of varclus algorithm in other analytical software like SAS, but always feel distressed when trying to find a RIGHT python version.
- Pythoners who are new to varclus algorithm. The source code will help you gain a deeper understanding of the math behind the algorithm.

The




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
 
