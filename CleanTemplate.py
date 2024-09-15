import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('data.csv')

# Step 1: Handling Missing Data

# Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# Fill missing values with the mean of the column
df.fillna(df.mean(), inplace=True)

# Step 2: Removing Duplicates

# Find duplicates
duplicates = df[df.duplicated()]
print(f"\nNumber of duplicate rows: {len(duplicates)}")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Step 3: Converting Data Types

# Convert a column to numeric type (e.g., 'age')
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Convert a column to datetime type (e.g., 'date')
df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')

# Step 4: Handling Outliers

# Define the IQR and outlier bounds for a specific column (e.g., 'salary')
Q1 = df['salary'].quantile(0.25)
Q3 = df['salary'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out rows with outliers in the 'salary' column
df = df[(df['salary'] >= lower_bound) & (df['salary'] <= upper_bound)]

# Step 5: Renaming Columns

# Rename a column (e.g., rename 'Name' to 'name')
df.rename(columns={'Name': 'name'}, inplace=True)

# Step 6: Standardizing Data

# Convert all text in the 'name' column to lowercase
df['name'] = df['name'].str.lower()

# Strip leading and trailing whitespace from 'name' column
df['name'] = df['name'].str.strip()

# Step 7: Dealing with Invalid Data

# Remove rows where 'age' has invalid data (i.e., not a number)
df_cleaned = df[df['age'].apply(lambda x: isinstance(x, (int, float)))]

# Final cleaned data preview
print("\nCleaned Data:")
print(df_cleaned.head())

# Optionally, save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_data.csv', index=False)
