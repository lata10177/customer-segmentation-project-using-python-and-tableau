# 🧺 FAST Market Basket Analysis (Optimized)

import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
import warnings
warnings.filterwarnings('ignore')

# Load dataset
data = pd.read_csv("cleaned_data.csv", encoding='latin1', on_bad_lines='skip', engine='python')
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], errors='coerce')
data['Country'] = data['Country'].str.lower()

# User input
country_choice = input("Enter country for Market Basket Analysis: ").strip().lower()

basket_data = data[data['Country'] == country_choice]

if basket_data.empty:
    print("⚠️ No records found for that country.")
    exit()

print(f"✅ Loaded {len(basket_data)} rows for {country_choice}")

# SUPER OPTIMIZATION: FILTER RARE ITEMS + LIMIT TRANSACTIONS

# Keep only items purchased >= 20 times (prevents huge matrix)
item_counts = basket_data['Description'].value_counts()
popular_items = item_counts[item_counts >= 20].index
basket_data = basket_data[basket_data['Description'].isin(popular_items)]

# Limit to first 5,000 invoices (fastest approach)
basket_data = basket_data[basket_data['InvoiceNo'].isin(
    basket_data['InvoiceNo'].unique()[:5000]
)]

print(f" After filtering → {basket_data['InvoiceNo'].nunique()} invoices, "
      f"{basket_data['Description'].nunique()} items")

if basket_data['Description'].nunique() < 2:
    print("⚠️ Not enough frequent items to proceed.")
    exit()

# Create Basket Matrix (FAST)
basket = (
    basket_data
    .groupby(['InvoiceNo', 'Description'])['Quantity']
    .sum()
    .unstack(fill_value=0)
)

basket = (basket > 0).astype(int)

print("Basket matrix created:", basket.shape)

# FP-Growth
frequent_items = fpgrowth(basket, min_support=0.02, use_colnames=True)

if frequent_items.empty:
    print("⚠️ No frequent itemsets found.")
    exit()

print(f"✨ Found {len(frequent_items)} frequent itemsets.")

# Association Rules
rules = association_rules(frequent_items, metric="lift", min_threshold=1)

if rules.empty:
    print("⚠️ No association rules generated.")
    exit()

# Sort
rules = rules.sort_values("confidence", ascending=False)

# Save
rules.to_csv("association_rules.csv", index=False)
print("💾 Saved → association_rules.csv")

print("\nTOP 5 RULES:")
print(rules[['antecedents','consequents','support','confidence','lift']].head())
