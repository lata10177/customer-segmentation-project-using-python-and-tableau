#data collection and processing
import pandas as pd

data = pd.read_csv("cleaned_data.csv", encoding='latin1', on_bad_lines='skip', engine='python')

print("✅ Data loaded successfully!")
print(data.head())

#data inspection
# Check dataset shape and info
print(data.shape)
print(data.info())

# Check for missing values and duplicates
print(data.isnull().sum())
print(data.duplicated().sum())

#data cleaning
# Remove rows with missing Customer ID or Product Description
data = data.dropna(subset=['CustomerID', 'Description'])
# Remove duplicate rows
data.drop_duplicates(inplace=True)
# Remove rows with non-positive Quantity
data = data[data['Quantity'] > 0]
# Calculate TotalPrice
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']
# Convert InvoiceDate to datetime
data['InvoiceDate'] = pd.to_datetime(
    data['InvoiceDate'],
    format="%m/%d/%Y %H:%M",
    errors='coerce'
)

#data transformation
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
data[['Quantity', 'UnitPrice', 'TotalPrice']] = scaler.fit_transform(
    data[['Quantity', 'UnitPrice', 'TotalPrice']]
)

# final verification
print(data.describe())
print(data.isnull().sum())

# Check basic statistics
print(data.describe())

# overview
# Unique counts
print("Unique Customers:", data['CustomerID'].nunique())
print("Unique Products:", data['Description'].nunique())
print("Transactions:", data['InvoiceNo'].nunique())


