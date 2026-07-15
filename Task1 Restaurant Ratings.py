import pandas as pd
df=pd.read_csv("dataset/dataset.csv")
#ratings
rating_ranges = pd.cut(df["Aggregate rating"],bins=[0,1,2,3,4,5])
#range count
range_count=rating_ranges.value_counts()
print(range_count)
#most common range
most_common_range=range_count.idxmax()
count=range_count.max()
print(f"The most common rating range is {most_common_range} with {count} restaurants")
#votes
avg_votes = df["Votes"].mean()
print(f'Number of votes received by a restuarant: {avg_votes:.2f}') 