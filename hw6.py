import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    # "industry": [
    #     "Data Analyst",
    #     "Data Analyst",
    #     "Software Engineer",
    #     "Data Analyst",
    #     "Data Analyst",
    #     "Data Analyst",
    #     "Data Analyst",
    # ],
    "salary": [
        60000,
        40000,
    ],
}
df = pd.DataFrame(data)

# find the most highly correlated variables in the data frame 'df' using some form of visualization
# correlation_matrix = df.corr().abs()
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
# plt.show()

# Use a mix of functions used in the slides to
# find the number of all those whose 'job_title' column value equals 'Data Analyst' in the data frame 'industry'.
# print(
#     df.groupby(["industry"]).apply(lambda x: x[x["industry"] == "Data Analyst"].count())
# )


print(df.groupby("salary").min())
