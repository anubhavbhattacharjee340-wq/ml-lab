
import pandas as pd
import numpy as np

marks = np.array([72, 85, 91, 68, 77])

print("marks", marks)
print("mean", np.mean(marks))
print("maximum:", np.max(marks))
print("minimum:", np.min(marks))

data = {
    "Name": ["Amit", "Riya", "Sourav", "Neha", "Rahul"],
    "Attendance": [88, 92, 76, 95, 81],
    "Marks": [72, 85, 68, 91, 77]
}

df = pd.DataFrame(data)

# Dynamically calculate Grade based on Marks
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# Add the new Grade column
df["Grade"] = df["Marks"].apply(calculate_grade)

print("\n--- DataFrame with Grade ---")
print(df)
