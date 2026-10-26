from io import StringIO
import pandas as pd

# Clean CSV text
csv_text = """student,department,semester,score,attendance
A,CSE,3,82,91
B,CSE,3,74,85
C,EEE,3,88,94
D,CSE,4,91,96
E,EEE,4,69,78
F,CSE,4,77,88
"""

# 1. Ingestion & Profiling
df = pd.read_csv(StringIO(csv_text))

print("--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Summary Statistics ---")
print(df.describe())

# 2. Selection & Filtering
print("\n--- Column Selection (student, score) ---")
print(df[["student", "score"]])

print("\n--- Label/Condition Filter (score >= 80) ---")
print(df.loc[df["score"] >= 80])

print("\n--- Positional Slicing (First 3 rows, First 3 columns) ---")
print(df.iloc[:3, :3])

# 3. Sorting & Grouped Aggregation
sorted_df = df.sort_values("score", ascending=False)
print("\n--- Sorted by Score (Descending) ---")
print(sorted_df)

summary = (
    df.groupby("department")
    .agg(
        mean_score=("score", "mean"),
        mean_attendance=("attendance", "mean"),
        students=("student", "count"),
    )
    .reset_index()
)

print("\n--- Department Grouped Summary ---")
print(summary)

# 4. Export to CSV without index column
summary.to_csv("department_summary.csv", index=False)
print("\nSummary successfully exported to 'department_summary.csv'!")
