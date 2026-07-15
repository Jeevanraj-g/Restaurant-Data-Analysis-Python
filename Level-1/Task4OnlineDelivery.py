import pandas as pd
df=pd.read_csv("dataset/dataset.csv")

print(df["Has Online delivery"].head(10))
#counts yes and no
online_delivery=df["Has Online delivery"].value_counts()
print(online_delivery)
#prints the number of restaurants that has online delivery
#Determining the percentage of restaurants that offer online delivery.
print(f"There are a total number of {online_delivery["Yes"]} restaurants that allows online delivery")
percentage = online_delivery["Yes"]/online_delivery.sum()*100
print(f" Percentage of restaurants offering online delivery : {percentage:.2f}") 
#Comparing average ratings of restaurants with and without online delivery.
votes_received = df.groupby("Has Online delivery")["Aggregate rating"].mean()
print(votes_received)
