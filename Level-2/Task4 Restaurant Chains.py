import pandas as pd
df=pd.read_csv("dataset/dataset.csv")
#restaurant counts
restaurant_counts=df["Restaurant Name"].value_counts()
#restaurant chain counts
chain_names=restaurant_counts[restaurant_counts>1].index
chain_data=df[df["Restaurant Name"].isin(chain_names)]
print("Restaurant Chains:")
print(chain_data.head())
#analyzing popularity
chain_analysis=chain_data.groupby("Restaurant Name")[["Aggregate rating","Votes"]].mean()
#highest rating
highest_rated=chain_analysis.sort_values(by="Aggregate rating",ascending=False)
print("\nHighest Rated Restaurants")
print(highest_rated.head(10))
#highest voted
highest_voted=chain_analysis.sort_values(by="Votes",ascending=False)
print("\nHighest Voted Restaurant")
print(highest_voted.head(10))
#Conclusion
print("\nConclusion:")
print("Restaurant chains such as those at the top of the rating list have the highest average ratings.")
print("Chains at the top of the votes list are the most popular based on customer votes.")