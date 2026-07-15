import pandas as pd
df=pd.read_csv("dataset/dataset.csv")
#top 5 cuisine combinations
print(df["Cuisines"].value_counts().head())
#high rated cuisine combinations
top_cuisines = df.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False)
print(top_cuisines.head())
#Conclusion
print("\nConclusion:")
print(f"Cuisine combinations such as Burger,Bar Food & Steak and American, Burger & Grill have the highest average ratings (4.9), indicating that certain cuisine combinations tend to receive higher customer ratings.")