
# 📊 Part 6: Combined Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import os

# Load Files
if os.path.exists("customer_segments.csv") and os.path.exists("association_rules.csv"):
    customer_data = pd.read_csv("customer_segments.csv")
    rules = pd.read_csv("association_rules.csv")
    print("✅ Data loaded successfully.")
else:
    print("⚠️ Missing saved files. Please run Part 3 (Market Basket) and Part 4 (Clustering) first.")
    exit()

# Cluster Distribution
plt.figure(figsize=(8,5))
sns.countplot(x='Cluster', data=customer_data, palette='coolwarm')
plt.title("Customer Count by Segment")
plt.xlabel("Cluster")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# Top 10 Customers by Spending
top_customers = customer_data.sort_values(by='Monetary', ascending=False).head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_customers['Monetary'], y=top_customers.index, palette='viridis')
plt.title("Top 10 Customers by Total Spending")
plt.xlabel("Total Spend")
plt.ylabel("Customer Index")
plt.tight_layout()
plt.show()

# Frequent Product Associations Network
plt.figure(figsize=(10,7))

# Some CSV exports contain sets as strings like "{itemA, itemB}"
rules['antecedents'] = rules['antecedents'].astype(str)
rules['consequents'] = rules['consequents'].astype(str)

G = nx.from_pandas_edgelist(rules.head(15), 'antecedents', 'consequents', ['lift'])
nx.draw(G, with_labels=True, node_color='lightgreen', node_size=2000, font_size=9)
plt.title("Frequent Product Associations Network")
plt.show()
