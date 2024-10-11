# CSV Data Cleaning and Validation

This code performs a series of cleaning and validation steps on a CSV file to identify and separate invalid or "garbage" data from clean and usable data. 

## Functionality

The code includes the following functions:

* **`clean_csv(file_path)`:**
    * Reads the CSV file.
    * Renames columns: 'mail_address' to 'email' and 'birthday_on' to 'date_of_birth'.
    * Handles missing birthdates by removing rows with missing values.
    * Converts gender codes (0 to 'F' and 1 to 'M').
    * Returns the cleaned DataFrame.

* **`remove_blank_records(df, error_df=None)`:**
    * Removes rows with all blank fields.
    * Appends invalid rows to an error DataFrame.
    * Returns the updated DataFrame and the error DataFrame.

* **`validate_emails(df, error_df=None)`:**
    * Validates email addresses using a regular expression.
    * Appends invalid email rows to an error DataFrame.
    * Returns the updated DataFrame and the error DataFrame.

* **`validate_and_remove_invalid_phone_numbers(df, phone_column, error_df=None)`:**
    * Cleans phone numbers by removing special characters.
    * Validates phone numbers to ensure they contain only digits.
    * Appends invalid phone number rows to an error DataFrame.
    * Returns the updated DataFrame and the error DataFrame.

* **`remove_invalid_rows_from_csv(csv_file_path, delimiter=';')`:**
    * Removes rows with an invalid number of columns compared to the header.
    * Returns a list of valid rows.

## Usage

1. **Input File:** 
   * The code expects a CSV file named "lifebear_csv.csv" located in the "/content/" directory.
   * The CSV file should use a semicolon (`;`) as the delimiter.

2. **Output:**
   * **Cleaned data:**  The cleaned data will be saved as "cleaned_lifebear.csv" in the "/content/clean_data" directory.
   * **Garbage data:**  All invalid rows identified during the cleaning process will be saved as "garbage_data.csv" in the "/content/garbage" directory.

3. **Running the Code:**
   * Execute the code. It will automatically perform the cleaning and validation steps and save the output files to the specified directories.

## Example

```python
# Example usage
file_path = "/content/lifebear_csv.csv" 

# ... rest of the code ...
Note
Make sure to have the necessary libraries installed (pandas, logging, re, csv, os).
The code assumes that the phone number column is named 'phone'. If your phone number column has a different name, update the validate_and_remove_invalid_phone_numbers function accordingly.

This README file provides a clear explanation of the code's purpose, func






