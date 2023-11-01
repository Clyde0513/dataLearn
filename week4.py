import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

n_rows = 10000
n_cols = 10

data = np.random.randint(0, 100, size=(n_rows, n_cols))
columns = [f"Column_{i}" for i in range(n_cols)]
df = pd.DataFrame(data, columns=columns)
print(df.head())
print("\n")


