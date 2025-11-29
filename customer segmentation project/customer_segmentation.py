import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Step 1️⃣: Load Data and Select Country
file_path = "cleaned_data.csv"   # <-- Using your actual file name
df = pd.read_csv(file_path, encoding='latin1', on_bad_lines='skip', engine='python')

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

# Ask user for country
country_choice = input("Enter country name for analysis (or type 'all' for all countries): ").strip().lower()

if country_choice == 'all':
    data_country = df.copy()
else:
    data_country = df[df['Country'].str.lower() == country_choice]

if data_country.empty:
    print("⚠️ No records found for that country. Try again.")
    exit()

print(f"\n✅ Selected country: {country_choice.title()} — {len(data_country)} transactions loaded.")
print(f"Available columns: {list(data_country.columns)}")

# Step 2️⃣: Prepare Customer-Level RFM Metrics
data_country['TotalPrice'] = data_country['Quantity'] * data_country['UnitPrice']

customer_data = data_country.groupby('CustomerID').agg({
    'InvoiceNo': 'nunique',   # Frequency
    'TotalPrice': 'sum',      # Monetary
    'InvoiceDate': 'max'      # Recency
}).rename(columns={'InvoiceNo': 'Frequency', 'TotalPrice': 'Monetary'})

# Calculate Recency
recent_date = data_country['InvoiceDate'].max()
customer_data['Recency'] = (recent_date - customer_data['InvoiceDate']).dt.days
customer_data.drop(columns='InvoiceDate', inplace=True)

print("\n🔍 Checking for missing values before scaling...")
print(customer_data.isnull().sum())

# Remove missing values
customer_data = customer_data.dropna(subset=['Frequency', 'Monetary', 'Recency'])
print(f"✅ Remaining records after cleaning: {len(customer_data)}")

if len(customer_data) < 2:
    print("⚠️ Not enough data for clustering. Try a country with more transactions.")
    exit()

# Step 3️⃣: Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_data)
scaled_df = pd.DataFrame(scaled_data, columns=customer_data.columns, index=customer_data.index)

# Step 4️⃣: K-Means Clustering
num_clusters = min(4, len(customer_data))  # avoid more clusters than samples
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
customer_data['Cluster'] = kmeans.fit_predict(scaled_df)

print("\n✅ Clustering complete!")
print(customer_data.groupby('Cluster')[['Frequency', 'Monetary', 'Recency']].mean())

# Step 5️⃣: Save results
output_file = f"segments_{country_choice}.csv"
customer_data.to_csv(output_file)
print(f"💾 Saved clustered data to {output_file}")

# NEW: Save universal customer segment file
customer_data.to_csv("customer_segments.csv", index=False)
print("💾 Saved master file: customer_segments.csv")
