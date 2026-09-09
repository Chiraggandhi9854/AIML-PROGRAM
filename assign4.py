import math
import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Pi:", math.pi)

arr = np.array([10, 20, 30, 40, 50])
print("\nNumPy Array:", arr)
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))

data = [10, 20, 20, 30, 40]
print("\nSciPy Mode:", stats.mode(data, keepdims=True).mode[0])

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Riya"],
    "Marks": [85, 72, 90, 65, 80]
})

print("\nDataFrame:")
print(df)
print("Average Marks:", df["Marks"].mean())

plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks - Matplotlib")
plt.show()

sns.barplot(x="Name", y="Marks", data=df)
plt.title("Student Marks - Seaborn")
plt.show()