import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder 
from sklearn.compose import ColumnTransformer 
from sklearn.pipeline import Pipeline

df = pd.DataFrame({ 
"age": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], 
"income": [20, 22, 25, 27, 30, 34, 38, 42, 50, 60], 
"city": ["A","A","B","B","C","C","A","B","C","A"], 
"target": [0,0,0,1,1,1,1,1,1,1] 
}) 

X = df.drop(columns="target") 
y = df["target"] 

X_train, X_test, y_train, y_test = train_test_split( 
X, y, test_size=0.30, random_state=42, stratify=y 
) 

numeric = ["age", "income"] 
categorical = ["city"] 

preprocess = ColumnTransformer([ 
("num", StandardScaler(), numeric), 
("cat", OneHotEncoder(handle_unknown="ignore"), categorical) 
]) 

X_train_t = preprocess.fit_transform(X_train) 
X_test_t = preprocess.transform(X_test) 

print("Train shape:", X_train_t.shape) 
print("Test shape:", X_test_t.shape) 
