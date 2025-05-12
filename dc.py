import pandas as pd

# Step 1: Load the dataset with appropriate encoding
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')  # Fixes UnicodeDecodeError

# Step 2: Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Step 3: Check and handle missing values
print("Missing values:\n", df.isnull().sum())
df = df.ffill()  # Forward fill missing values

# Step 4: Remove duplicate rows
df = df.drop_duplicates()

# Step 5: Convert orderdate to datetime format
df['orderdate'] = pd.to_datetime(df['orderdate'], errors='coerce')

# Step 6: Convert numeric columns to proper types
df['quantityordered'] = df['quantityordered'].astype(int)
df['priceeach'] = df['priceeach'].astype(float)
df['sales'] = df['sales'].astype(float)
df['msrp'] = df['msrp'].astype(float)

# Step 7: Standardize text fields
df['status'] = df['status'].str.upper().str.strip()
df['productline'] = df['productline'].str.title().str.strip()
df['country'] = df['country'].str.title().str.strip()
df['dealsize'] = df['dealsize'].str.upper().str.strip()

# Step 8: Save cleaned dataset
df.to_csv('cleaned_sales_data.csv', index=False)

print("Cleaned dataset saved as 'cleaned_sales_data.csv'")
