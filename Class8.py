import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer(as_frame=True) 
df = data.frame.copy() 
df["target_name"] = df["target"].map(dict(enumerate(data.target_names))) 

print(df.shape) 
print(df.dtypes.value_counts()) 
print(df.isna().sum().sort_values(ascending=False).head()) 
print(df["target_name"].value_counts()) 
print(df.describe().T.head()) 

fig = plt.figure(figsize=(7,4)) 
sns.countplot(data=df, x="target_name") 
plt.title("Class Distribution") 
plt.show() 

fig = plt.figure(figsize=(7,4)) 
sns.histplot(data=df, x="mean radius", hue="target_name", kde=True) 
plt.title("Feature Distribution") 
plt.show() 

fig = plt.figure(figsize=(7,4)) 
sns.boxplot(data=df, x="target_name", y="mean radius") 
plt.title("Group-wise Feature Distribution") 
plt.show() 

corr = df.select_dtypes("number").corr() 
fig = plt.figure(figsize=(10,8)) 
sns.heatmap(corr, cmap="Greys") 
plt.title("Correlation Matrix") 
plt.show()
