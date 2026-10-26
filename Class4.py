import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Reproducible Synthetic Dataset Generation
rng = np.random.default_rng(42)
df = pd.DataFrame({
    "study_hours": rng.normal(5, 1.5, 120).clip(0, 10),
    "sleep_hours": rng.normal(7, 1.0, 120).clip(3, 10),
})
df["score"] = (50 + 5 * df["study_hours"] + rng.normal(0, 7, 120)).clip(0, 100)
df["group"] = rng.choice(["A", "B", "C"], size=len(df))

# 2. Statistical Summaries and Correlation Matrix
print("--- Summary Statistics ---")
print(df.describe())

print("\n--- Pearson Correlation Matrix ---")
print(df[["study_hours", "sleep_hours", "score"]].corr())

# 3. Univariate Distributions: Histogram & Boxplot
plt.figure(figsize=(6, 4))
plt.hist(df["score"], bins=12, edgecolor="black")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Score Distribution")
plt.show()

plt.figure(figsize=(6, 4))
plt.boxplot(df["score"], vert=True)
plt.ylabel("Score")
plt.title("Score Boxplot")
plt.show()

# 4. Categorical Frequency Plot
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="group")
plt.title("Group Frequency")
plt.show()

# 5. Bivariate Relationship & Correlation Heatmap
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="study_hours", y="score")
plt.title("Study Hours versus Score")
plt.show()

plt.figure(figsize=(6, 4))
sns.heatmap(
    df[["study_hours", "sleep_hours", "score"]].corr(), annot=True, fmt=".2f"
)
plt.title("Correlation Matrix")
plt.show()
