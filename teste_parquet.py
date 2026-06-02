import pandas as pd

df = pd.read_parquet("a.parquet")

print(df.columns)
print(df.shape)