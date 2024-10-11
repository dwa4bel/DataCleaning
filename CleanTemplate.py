
import pandas as pd
import logging
import re
import csv
import os

def clean_csv(file_path):
    """Cleans a CSV file with specific cleaning steps.

    Args:
        file_path (str): The file path of the CSV file.

    Returns:
        pandas.DataFrame: The cleaned DataFrame.
    """

    # Read the CSV file
    df = pd.read_csv(file_path, sep=';', low_memory=True)

    # Rename columns
    df.rename(columns={'mail_address': 'email', 'birthday_on': 'date_of_birth'}, inplace=True)

    # Handle missing birthdates
    df = df.dropna(subset=['date_of_birth'])

    # Convert gender codes to labels
    df = df.replace(0, 'F')
    df = df.replace(1, 'M')

    return df


def remove_blank_records(df, error_df=None):
    """Removes records with blank fields (all fields) and appends them to an error DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to clean.
        error_df (pandas.DataFrame, optional): An existing DataFrame to append invalid records to.
            If None, a new DataFrame is created. Defaults to None.

    Returns:
        tuple: A tuple containing the updated DataFrame and the error DataFrame.
    """

    try:
        if error_df is None:
            error_df = pd.DataFrame(columns=df.columns)  # Ensure error_df has the same columns

        blank_rows = df.isnull().all(axis=1)  # Check for rows where all fields are blank
        invalid_rows = df[blank_rows]
        df = df[~blank_rows]

        error_df = pd.concat([error_df, invalid_rows])

        return df, error_df

    except Exception as e:
        logging.error(f"An error occurred while removing blank records: {e}")
        return df, error_df


def validate_emails(df, error_df=None):
    """Validates email addresses in a DataFrame and separates invalid records.

    Args:
        df (pandas.DataFrame): The DataFrame to validate.
        error_df (pandas.DataFrame, optional): An existing DataFrame to append invalid records to.
            If None, a new DataFrame is created. Defaults to None.

    Returns:
        tuple: A tuple containing the updated DataFrame with valid email addresses and
            the DataFrame with invalid email addresses.
    """

    try:
        if error_df is None:
            error_df = pd.DataFrame(columns=df.columns)  # Ensure error_df has the same columns

        # Regular expression for basic email validation
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        # Find rows with invalid email addresses
        invalid_email_rows = df[~df['email'].str.match(email_regex, na=False)]  # Handle potential NaN values

        # Append invalid rows to the error DataFrame
        error_df = pd.concat([error_df, invalid_email_rows])

        # Remove invalid rows from the original DataFrame
        df = df[df['email'].str.match(email_regex, na=False)]  # Handle potential NaN values

        return df, error_df

    except Exception as e:
        logging.error(f"An error occurred during email validation: {e}")
        return df, error_df


def validate_and_remove_invalid_phone_numbers(df, phone_column, error_df=None):
    """
    Validates phone numbers in a dataframe, appends records with invalid phone
    numbers to a new dataframe, and removes them from the original dataframe.
    If a phone number is valid but contains special characters, they are removed.

    Args:
        df (pd.DataFrame): The dataframe containing phone numbers.
        phone_column (str): The name of the column containing phone numbers.
        error_df (pd.DataFrame, optional): An existing DataFrame to append invalid records to.
            If None, a new DataFrame is created. Defaults to None.


    Returns:
        tuple: A tuple containing the updated dataframe with valid phone numbers
            and a new dataframe with records containing invalid phone numbers.
    """
    try:
        if error_df is None:
            error_df = pd.DataFrame(columns=df.columns)  # Ensure error_df has the same columns

        for index, row in df.iterrows():
            phone_number = row[phone_column]

            # Remove special characters from the phone number
            phone_number = re.sub(r"[+()\-. ]", "", str(phone_number))

            # Check if the phone number contains only digits after cleaning
            if not phone_number.isdigit():
                error_df = pd.concat([error_df, pd.DataFrame([row])], ignore_index=True)
                df.drop(index, inplace=True)
            else:
                # Update the dataframe with the cleaned phone number
                df.at[index, phone_column] = phone_number

        return df, error_df

    except Exception as e:
        logging.error(f"Error occurred during phone number validation: {e}")
        return df, error_df


def remove_invalid_rows_from_csv(csv_file_path, delimiter=';'):
    """Removes rows from a CSV file that have an invalid number of columns.

    Args:
        csv_file_path: The path to the CSV file.
        delimiter: The delimiter used in the CSV file.

    Returns:
        A list of valid rows.
    """

    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        header = next(reader)  # Get the header row
        expected_num_columns = len(header)
        valid_rows = [header]  # Start with the header

        for row in reader:
            if len(row) == expected_num_columns:
                valid_rows.append(row)
            else:
                print(f"Warning: Skipping row with invalid number of columns: {row}")

    return valid_rows


# Example usage
file_path = "/content/lifebear_csv.csv"  # Updated file path

# Specify the desired download path
download_path = "/content/clean_data"  # Updated download path
garbage_path = "/content/garbage"  # Updated garbage path

# Ensure the download and garbage paths exist
os.makedirs(download_path, exist_ok=True)
os.makedirs(garbage_path, exist_ok=True)

# Remove invalid rows with incorrect column count
valid_rows = remove_invalid_rows_from_csv(file_path)

# Write valid rows to a new CSV file
with open(f"{download_path}/valid_rows_lifebear.csv", 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile, delimiter=';')
    writer.writerows(valid_rows)

# Now, read the cleaned CSV
cleaned_df = clean_csv(f"{download_path}/valid_rows_lifebear.csv")

# Initialize the error DataFrames
error_df_blank = pd.DataFrame(columns=cleaned_df.columns)
error_df_email = pd.DataFrame(columns=cleaned_df.columns)
error_df_phone = pd.DataFrame(columns=cleaned_df.columns)

# Remove blank records
updated_df, error_df_blank = remove_blank_records(cleaned_df, error_df_blank)

# Validate emails
updated_df_email, error_df_email = validate_emails(updated_df, error_df_email)


# Save the cleaned DataFrame
updated_df_phone.to_csv(f"{download_path}/cleaned_lifebear.csv", index=False)

# Concatenate all error DataFrames into a single garbage DataFrame
garbage_df = pd.concat([error_df_blank, error_df_email, error_df_phone])

# Save the garbage DataFrame
garbage_df.to_csv(f"{garbage_path}/garbage_data.csv", index=False)
