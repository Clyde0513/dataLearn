from calendar import c
import decimal
from statistics import correlation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LogisticRegression

breast_data = pd.read_csv("breast-cancer.csv")
df = pd.DataFrame(breast_data)


# print(df.groupby("area_mean")["id"].mean())
# print(df)


# print(df.area_mean.value_counts())
def histogram(dataFrame, column_name):
    correct_data = dataFrame.fillna({column_name: dataFrame[column_name].mean()})
    data = correct_data[column_name]
    y_axis = np.arange(min(data), max(data))
    plt.hist(
        correct_data[column_name],
        y_axis,
        color="green",
        alpha=0.8,
        edgecolor="g",
    )
    plt.title("Area Mean and Count for Breast Cancer")
    plt.xlabel(column_name, fontsize=15)
    plt.ylabel("Count", fontsize=15)
    plt.xticks(
        fontsize=10,
    )
    plt.yticks(fontsize=10)
    plt.show()


histogram(df, "area_mean")


# Area mean's statistics
Q1 = df["area_mean"].quantile(0.25)
Q3 = df["area_mean"].quantile(0.75)
IQR = Q3 - Q1
median = df["area_mean"].median()
mean = df["area_mean"].mean()
max = df["area_mean"].max()
min = df["area_mean"].min()

print(Q1, "\n")  # Q1 = 420.3
print(Q3, "\n")  # Q3 = 782.7
print(IQR, "\n")  # IQR = 362.403
print(median, "\n")  # median = 551.1
print(mean, "\n")  # mean = 654.889
print(max, "\n")  # max = 2501.0
print(min, "\n")  # min = 143.5

# Perimeter's mean statistics
Q1_perimeter = df["perimeter_mean"].quantile(0.25)
Q3_perimeter = df["perimeter_mean"].quantile(0.75)
IQR_perimeter = Q3_perimeter - Q1_perimeter
median_perimeter = df["perimeter_mean"].median()
mean_perimeter = df["perimeter_mean"].mean()
max_perimeter = df["perimeter_mean"].max()
min_perimeter = df["perimeter_mean"].min()
print("\n")
print(Q1_perimeter, "\n")  # Q1_perimeter = 75.17
print(Q3_perimeter, "\n")  # Q3_perimeter = 104.1
print(IQR_perimeter, "\n")  # IQR_perimeter = 28.93
print(median_perimeter, "\n")  # median_perimeters = 86.24
print(mean_perimeter, "\n")  # mean_perimeter = 91.97
print(max_perimeter, "\n")  # max_perimeter = 188.5
print(min_perimeter, "\n")  # min_perimeter = 43.79
