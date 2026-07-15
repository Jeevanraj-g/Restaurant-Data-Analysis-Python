import pandas as pd
import matplotlib.pyplot as plt
#define
df = pd.read_csv("dataset/dataset.csv")
#plotting scatter graph
plt.scatter(df["Longitude"], df["Latitude"],s=10,alpha=0.6)
#plot title
plt.title("Restaurant Locations by Latitude and Longitude")
#plot labels
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()