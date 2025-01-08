import pandas as pd

# Load the data from the CSV file
# Replace 'your_file.csv' with the path to your actual file
data = pd.read_csv('/assets/GlobalTemperatures.csv')

# Display the first few rows to understand the data structure
print("Initial Data Preview:")
print(data.head())

# 1. Check for missing values in each column
print("\nMissing Values Before Cleaning:")
print(data.isnull().sum())

# 2. Data Cleaning: Handling missing values
# Option 1: Drop rows with any missing values
data_cleaned = data.dropna()

# Option 2 (if you prefer): Fill missing values (you can choose a strategy)
# data_cleaned = data.fillna({
#     'Column1': data['Column1'].mean(),  # Replace 'Column1' with actual column names
#     'Column2': data['Column2'].median(),
#     'Date': '1900-01-01'  # Replace with a default date for missing dates, if necessary
# })

# 3. Convert date to a consistent format (e.g., YYYY-MM-DD)
# Assuming our date column is named 'dt', replace it if needed
data_cleaned['dt'] = pd.to_datetime(data_cleaned['dt'], errors='coerce')

# Remove rows with invalid dates if any
data_cleaned = data_cleaned.dropna(subset=['dt'])

# Convert the standardized date back to a consistent string format: YYYY-MM-DD
data_cleaned['dt'] = data_cleaned['dt'].dt.strftime('%Y-%m-%d')

# 4. Check for missing values after cleaning
print("\nMissing Values After Cleaning:")
print(data_cleaned.isnull().sum())

# 5. Save the cleaned data to a new CSV file
data_cleaned.to_csv('/cleaned/cleaned_global_temperature.csv', index=False)

# Display the first few rows of the cleaned data
print("\nCleaned Data Preview:")
print(data_cleaned.head())
