import pandas as pd
#read the dataset
df=pd.read_csv("dataset/dataset.csv")
#get top 3 cities
most_restaurants_city = df["City"].value_counts().head(1)
#print
print("\nCity with the highest number of Restaurants:")
print(most_restaurants_city)
#average rating grouped by city
avg_rating = df.groupby("City")["Aggregate rating"].mean().head()
#print average rating
print("\nAverage ratings for each restaurants in each city")
print(avg_rating)
#highest average rating city
top_city = df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False).head(1)
#print
print("\nCity with the highest average rating:")
print(top_city)
