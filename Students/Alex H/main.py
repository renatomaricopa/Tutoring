import pandas as pd

f1 = pd.read_csv("file1.csv")
f2 = pd.read_csv("file2.csv")
df = pd.concat([f1, f2]).reset_index(drop=True)
df = df.drop(['id'], axis=1)
df.to_csv("output.csv", index=True) 