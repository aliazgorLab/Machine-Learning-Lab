import csv
from io import StringIO

scores = [72, 81, 65, 90, 77]
mean_score = sum(scores)/len(scores)
maximum = max(scores)
minimum = min(scores)
range_score = maximum - minimum

print(f"Mean: {mean_score}, Max: {maximum}, Min: {minimum}, Range: {range_score}")



def describe(values):
    if not values: 
        return None
    return {
        "count" : len(values),
        "mean" : sum(values)/len(values),
        "min" : min(values),
        "max" : max(values),
        "range" : max(values) - min(values)
    }

print("\nDescriptive Summary:")
print(describe(scores))

csv_text = "name,score\nA,72\nB,81\nC,65\n"
reader = csv.DictReader(StringIO(csv_text))
rows = list(reader)

print(rows)
