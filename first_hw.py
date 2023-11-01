import numpy as np
import pandas as pd


data = {
    "StudentID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charles", "Dolby"],
    "Age": [21, 22, 23, 24],
}
print("\n")
df = pd.DataFrame(data)
print(df)
print("\n")
print(df.loc[:, "Name"])
print("\n")


df = pd.DataFrame({"column 1": [1, 1], "column 2": [2, 2]})
print(df.shape)
print("\n")

random_int = np.random.randint(-5, 5)
print(random_int)

import numpy as np
import pandas as pd
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("netflixData.csv")
print(data.head())
