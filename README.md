# DataCleaning
Fundamentals of Data Cleaning

Data cleaning is an essential process in data analysis, involving handling errors, missing data, duplicates, and outliers to prepare the data for analysis. Here's a basic introduction to common data cleaning techniques using Python:

# Libraries:
You'll need some basic libraries to work with data in Python:

Pandas: Provides high-level data manipulation tools.
NumPy: Used for numerical computations.

bash
Copy code
```pip install pandas numpy```

# Basic Steps in Data Cleaning
## 1. Loading the Data
The first step is to load your data into a DataFrame using Pandas.

python
Copy code
```import pandas as pd```

# Load the data from a CSV file
```df = pd.read_csv('data.csv')```

## 2. Handling Missing Data
Missing data is common in real-world datasets. You can either remove or fill missing values.

Checking for missing values:
python
Copy code
Check for missing values

```print(df.isnull().sum())```
Removing rows with missing data:
python
Copy code

Drop rows with any missing values
```df_cleaned = df.dropna()```

Filling missing values:
python
Copy code

Fill missing values with a specific value (e.g., 0 or mean)
```df['column_name'] = df['column_name'].fillna(0)```
Fill missing values with the mean of the column
```df['column_name'] = df['column_name'].fillna(df['column_name'].mean())```

# 3. Removing Duplicates
Duplicate data can skew analysis, so it's important to identify and remove it.

python
Copy code
# Find duplicates
duplicates = df[df.duplicated()]

# Remove duplicates
df_cleaned = df.drop_duplicates()
4. Converting Data Types
Sometimes, data may be in the wrong format (e.g., strings instead of integers).

python
Copy code
# Convert a column to a numeric data type
df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')

# Convert to datetime
df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')
5. Handling Outliers
Outliers can distort statistical analysis, so you may want to remove or treat them.

Removing outliers using interquartile range (IQR):
python
Copy code
Q1 = df['column_name'].quantile(0.25)
Q3 = df['column_name'].quantile(0.75)
IQR = Q3 - Q1

# Define bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
df_cleaned = df[(df['column_name'] >= lower_bound) & (df['column_name'] <= upper_bound)]
6. Renaming Columns
For consistency and readability, it’s a good practice to rename columns.

python
Copy code
# Rename a specific column
df.rename(columns={'old_name': 'new_name'}, inplace=True)
7. Standardizing Data
Standardizing data (such as lowercasing all text in a column) can improve consistency.

python
Copy code
# Convert all text to lowercase
df['column_name'] = df['column_name'].str.lower()

# Strip leading and trailing whitespace
df['column_name'] = df['column_name'].str.strip()
8. Dealing with Invalid Data
You may encounter invalid data that doesn't fit expected values. You can remove or correct it.

python
Copy code
# Remove rows where column_name has invalid data
df_cleaned = df[df['column_name'].apply(lambda x: isinstance(x, (int, float)))]
Example Workflow
