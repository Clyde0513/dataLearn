from math import nan
from traceback import print_list
import numpy as np
import pandas as pd

# Week 3

# This section is about using numpy ONLY
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30])
result = (
    arr1[:, np.newaxis] * arr2
)  # multiplies each row in arr1 by each column in arr2
print(result)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(np.shape(matrix))  # (2, 3)
print(matrix[1, 2])  # 6
print(matrix[0:, 2])  # [3 6]
small = matrix[:, 1] < 3
print(matrix[:, 1])
print(np.any(small))  # True
print(small)  # [True, False]
print("\n")

print(type(nan))
print(type(None))
print("\n")
# Now, we're moving to pandas
# --> Read in data from Excel spreadsheet or CSV (comma separated value)
# --> Merging/Joining: combine based on common columns or keys
# --> reshaping data, typically from long to wide format
# --> Group: splitting data into groups based on certain criteria
# Series: 1-D Array
#       ndarray: fixed size elements
#       slicing and indexing same rules
# ● pd.read_csv('my_csv_file.csv') or pd.read_excel('my_xls_file.xls')
# ● loc: label based, require name of rows/columns
# ● iloc: positional based, require positions of values (numbers)

print(pd.DataFrame({"apples": [4, 1], "mangoes": [5, 2]}))
print("\n")
data = {"Name": ["Valerie", "Clyde"], "Age": [19, 20], "City": ["Fremont", "Vallejo"]}
df = pd.DataFrame(data)
print(df)
print("\n")
print(df.loc[:, "Name"])
print(df.iloc[:, 0])
print(df.loc[:, "Age"])
print(df.iloc[:, 1])
print(df.loc[:, "City"])
print("\n")

# Modifying DataFrames

my_dict = {
    "States": ["California", "Nevada", "Arizona"],
    "Cities": ["Los Angeles", "Las Vegas", "Phoenix"],
}
df = pd.DataFrame(my_dict)
print(df)
print("\n")
df["     grade"] = ["+", "+", "-"]
df_new = df.sort_values(["     grade"])
print(df_new)
print("\n")
print(df.describe(include="all"))
