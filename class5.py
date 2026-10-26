import pandas as pd
import numpy as np

df = pd.DataFrame({
    "age": [21, 22, np.nan, 24, 24, 25, 120, 23],
    "city": ["Dhaka", "dhaka", "Dhaka", "Chattogram", "Chattogram", "Dhaka", "Dhaka", 
"Dhaka"],
    "score": [75, 81, 79, np.nan, 85, 90, 88, 90]
})

print("Missing Valuse: ")
print(df.isna().sum())

print("Duplicated row: ", df.duplicated().sum())

df["city_clean"]= (
    df["city"].astype("string")
    .str.strip()
    .str.lower()
    .str.title()
)
q1 = df["age"].quantile(0.25)
q3 = df["age"].quantile(0.75)
iqr = q3-q1
lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr

outlier_mask = (df["age"]<lower) | (df["age"]>upper)
print("Outlier row:")
print(outlier_mask)

clean = df.copy()
clean["age"] = clean["age"].fillna(clean["age"].median())
clean["score"] = clean["score"].fillna(clean["score"].median())
clean = clean.drop_duplicates()
print(clean)
