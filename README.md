# VarClusHi

This is a Python module to perform variable clustering with a hierarchical structure. 


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




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cluster</th>
      <th>N_Vars</th>
      <th>Eigval1</th>
      <th>Eigval2</th>
      <th>VarProp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>2.141357</td>
      <td>0.658413</td>
      <td>0.713786</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>3</td>
      <td>1.766885</td>
      <td>0.900991</td>
      <td>0.588962</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2</td>
      <td>1.371260</td>
      <td>0.628740</td>
      <td>0.685630</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2</td>
      <td>1.552496</td>
      <td>0.447504</td>
      <td>0.776248</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>1</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
demo1_vc.rsquare
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cluster</th>
      <th>Variable</th>
      <th>RS_Own</th>
      <th>RS_NC</th>
      <th>RS_Ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>fixed acidity</td>
      <td>0.882210</td>
      <td>0.277256</td>
      <td>0.162976</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>density</td>
      <td>0.622070</td>
      <td>0.246194</td>
      <td>0.501362</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>pH</td>
      <td>0.637076</td>
      <td>0.194359</td>
      <td>0.450478</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>free sulfur dioxide</td>
      <td>0.777796</td>
      <td>0.010358</td>
      <td>0.224530</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>total sulfur dioxide</td>
      <td>0.786660</td>
      <td>0.042294</td>
      <td>0.222761</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
      <td>residual sugar</td>
      <td>0.202428</td>
      <td>0.045424</td>
      <td>0.835525</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>sulphates</td>
      <td>0.685630</td>
      <td>0.106022</td>
      <td>0.351653</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2</td>
      <td>chlorides</td>
      <td>0.685630</td>
      <td>0.048903</td>
      <td>0.330534</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3</td>
      <td>citric acid</td>
      <td>0.776248</td>
      <td>0.398208</td>
      <td>0.371810</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3</td>
      <td>volatile acidity</td>
      <td>0.776248</td>
      <td>0.040920</td>
      <td>0.233299</td>
    </tr>
    <tr>
      <th>10</th>
      <td>4</td>
      <td>alcohol</td>
      <td>1.000000</td>
      <td>0.082055</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
demo2_df = pd.read_excel('jobrate.xlsx')
demo2_df.drop('Overall_Rating',axis=1,inplace=True)
demo2_vc = VarClusHi(demo2_df,maxeigval2=0,maxclus=3)
demo2_vc.varclus()
```




    <varclushi.varclushi.VarClusHi at 0x15f920cd7b8>




```python
demo2_vc.info
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cluster</th>
      <th>N_Vars</th>
      <th>Eigval1</th>
      <th>Eigval2</th>
      <th>VarProp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>8</td>
      <td>4.663086</td>
      <td>0.715184</td>
      <td>0.582886</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>4</td>
      <td>3.039960</td>
      <td>0.456049</td>
      <td>0.759990</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>1</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
demo2_vc.rsquare
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cluster</th>
      <th>Variable</th>
      <th>RS_Own</th>
      <th>RS_NC</th>
      <th>RS_Ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Communication_Skills</td>
      <td>0.633771</td>
      <td>0.326972</td>
      <td>0.544151</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>Problem_Solving</td>
      <td>0.507940</td>
      <td>0.273017</td>
      <td>0.676852</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>Learning_Ability</td>
      <td>0.612599</td>
      <td>0.126570</td>
      <td>0.443540</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>Observational_Skills</td>
      <td>0.657120</td>
      <td>0.182641</td>
      <td>0.419498</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>Willingness_to_Confront_Problems</td>
      <td>0.620156</td>
      <td>0.237397</td>
      <td>0.498089</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>Desire_for_Self_Improvement</td>
      <td>0.604388</td>
      <td>0.296961</td>
      <td>0.562717</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>Appearance</td>
      <td>0.441876</td>
      <td>0.145928</td>
      <td>0.653485</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>Dependability</td>
      <td>0.585235</td>
      <td>0.453685</td>
      <td>0.759205</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>Judgement_under_Pressure</td>
      <td>0.640120</td>
      <td>0.367677</td>
      <td>0.569139</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
      <td>Interest_in_People</td>
      <td>0.838905</td>
      <td>0.233862</td>
      <td>0.210268</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1</td>
      <td>Interpersonal_Sensitivity</td>
      <td>0.804705</td>
      <td>0.178482</td>
      <td>0.237724</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1</td>
      <td>Integrity</td>
      <td>0.756230</td>
      <td>0.338525</td>
      <td>0.368525</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2</td>
      <td>Physical_Ability</td>
      <td>1.000000</td>
      <td>0.222030</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>





# Highlights



# Installation

Requirements: Python 3.4+

```
pip3 install varclushi
```
 
