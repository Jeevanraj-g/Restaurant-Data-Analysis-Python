import pandas as pd
import matplotlib.pyplot as plt
#define
df = pd.read_csv("dataset/dataset.csv")
print(df["Price range"].head(10))  
#price counts
price_counts = df["Price range"].value_counts()
print(price_counts)
#sum 0f prices
print(price_counts.sum())
#calculaating percentage
price_percentage = (price_counts/price_counts.sum()*100)
print(price_percentage)
#drawing graph
price_counts.plot(kind='bar')
#plotting
plt.title("Distribution of Price ranges")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
#showing
plt.show()