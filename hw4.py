import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Jane", "Anvesha", "Mike", "Miles", "Taylor"],
    "Age": [25, 32, np.nan, 28, 31],
    "Salary": [50000, 70000, 60000, 55000, 65000],
}
df = pd.DataFrame(data)


# takes in DataFrame and a column name as inputs and returns histogram plot
# if data in the specifed column contains missing values, the function should
# replace them with the mean of the column
def histogram(dataFrame, column_name):
    correct_data = dataFrame.fillna({column_name: dataFrame[column_name].mean()})
    data = correct_data[column_name]
    x_axis = np.arange(min(data), max(data) + 1, 1)
    plt.hist(correct_data[column_name], x_axis, color="green", alpha=0.2, edgecolor="g")
    plt.title("People's Salaries and Age")
    plt.xlabel(column_name)
    plt.ylabel("Amount")
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()


histogram(df, "Salary")
histogram(df, "Age")
