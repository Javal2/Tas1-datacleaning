# Task 1: Data Cleaning and Preprocessing – Sales Dataset

## Dataset Description

This dataset contains sales transaction records with fields like ORDERNUMBER, QUANTITYORDERED, SALES, ORDERDATE, STATUS, PRODUCTLINE, CUSTOMERNAME, and more.

---

## Objective

To clean and preprocess the raw sales dataset by:
- Handling missing values and duplicates
- Fixing column naming inconsistencies
- Converting data types
- Standardizing text fields
- Preparing the dataset for analysis or visualization

---

##  Data Cleaning Steps (Python Script)

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('sales_data.csv')  # Replace with your actual file name

# Step 1: Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Step 2: Check and handle missing values
print(df.isnull().sum())
df = df.ffill()  # Forward fill missing values

# Step 3: Remove duplicate records
df = df.drop_duplicates()
