#sale distribution

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("cleaned_data.csv", encoding='latin1', on_bad_lines='skip', engine='python')

#top10 products
top_products = (data.groupby('Description')['Quantity']
                .sum()
                .sort_values(ascending=False)
                .head(10))

plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Total Quantity")
plt.ylabel("Product Description")
plt.show()

#top10 contries
top_countries = (data.groupby('Country')['TotalPrice']
                 .sum()
                 .sort_values(ascending=False)
                 .head(10))

plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='mako')
plt.title("Top 10 Countries by Total Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Country")
plt.show()

# customer purchase behavior
# Customer-level aggregation
customer_summary = data.groupby('CustomerID').agg({
    'InvoiceNo': 'nunique',
    'Quantity': 'sum',
    'TotalPrice': 'sum'
}).rename(columns={'InvoiceNo': 'NumTransactions',
                   'Quantity': 'TotalQuantity',
                   'TotalPrice': 'TotalSpend'})

customer_summary.head()

# spend distribution
plt.figure(figsize=(8,5))
sns.histplot(customer_summary['TotalSpend'], bins=50, kde=True)
plt.title("Customer Total Spend Distribution")
plt.xlabel("Total Spend")
plt.ylabel("Frequency")
plt.show()

# time-based analysis
data['InvoiceMonth'] = data['InvoiceDate'].dt.to_period('M')

monthly_sales = (data.groupby('InvoiceMonth')['TotalPrice']
                 .sum()
                 .reset_index())

plt.figure(figsize=(10,5))
sns.lineplot(x='InvoiceMonth', y='TotalPrice', data=monthly_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

#correlation analysis
plt.figure(figsize=(6,4))
sns.heatmap(data[['Quantity', 'UnitPrice', 'TotalPrice']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Key Variables")
plt.show()

