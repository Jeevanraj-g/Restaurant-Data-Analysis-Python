import pandas as pd
#Read the data
df=pd.read_csv("dataset/dataset.csv")
top_cuisines = df["Cuisines"].head(3)
print("\ntop_cuisines:")
print(top_cuisines)