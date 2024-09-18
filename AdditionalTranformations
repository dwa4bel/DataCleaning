# Additional Cleaning Functions

```
# Check for missing values
print(df.isnull().sum())

# Drop rows with any missing values
df_cleaned = df.dropna()

# Fill missing values with a specific value (e.g., 0 or mean)
df['column_name'] = df['column_name'].fillna(0)

# Fill missing values with the mean of the column
df['column_name'] = df['column_name'].fillna(df['column_name'].mean())

# Find duplicates
duplicates = df[df.duplicated()]

# Remove duplicates
df_cleaned = df.drop_duplicates()

# Convert a column to a numeric data type
df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')

# Convert a column to a numeric data type
df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')

# Convert a column to a numeric data type
df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')

# Convert a column to a numeric data type
df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')

# Convert a column to a numeric data type
df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')

# Melt the DataFrame
df_melted = pd.melt(df, id_vars=['id_vars'], value_vars=['value_vars'])

# Merge two DataFrames
df_merged = pd.merge(df1, df2, on='common_column')

# Concatenate DataFrames
df_concat = pd.concat([df1, df2], axis=0)

# Sort by column values
df_sorted = df.sort_values(by='column_name', ascending=False)

# Reset index
df_reset = df.reset_index(drop=True)

# Set a column as index
df_indexed = df.set_index('column_name')

# Remove outliers
df_no_outliers = df[(df['column_name'] > lower_bound) & (df['column_name'] < upper_bound)]

# Cap outliers
df['column_name'] = df['column_name'].clip(lower=lower_bound, upper=upper_bound)

# Create a new column based on a condition
df['new_column'] = df['column_name'].apply(lambda x: 'High' if x > threshold else 'Low')

# Apply a function to a column
df['column_name'] = df['column_name'].apply(lambda x: x * 2)

# Convert to uppercase
df['column_name'] = df['column_name'].str.upper()

# Convert to datetime
df['date_column'] = pd.to_datetime(df['date_column'])

# Extract year from date
df['year'] = df['date_column'].dt.year

# Calculate rolling mean
df['rolling_mean'] = df['column_name'].rolling(window=3).mean()

# Calculate cumulative sum
df['cumsum'] = df['column_name'].cumsum()

# Interpolate missing values
df['column_name'] = df['column_name'].interpolate()

# One-hot encode categorical variables
df_encoded = pd.get_dummies(df, columns=['categorical_column'])

# Normalize data
df['normalized_column'] = (df['column_name'] - df['column_name'].min()) / (df['column_name'].max() - df['column_name'].min())

# Bin data into intervals
df['binned_column'] = pd.cut(df['column_name'], bins=[0, 10, 20, 30], labels=['Low', 'Medium', 'High'])
```





