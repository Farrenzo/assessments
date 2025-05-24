"""
Process raw csv data into an actionable analytics ready data set.

1. Read the csv file
2. Remove empty rows
3. Fix formatting issues (e.g., date formats, string casing etc.)
4. Get column properties (names, data type, etc.)
5. Provide a summary of the data in DDL format
6. Save the cleaned data to a new csv file
"""

import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "raw_healthcare_dataset.csv")
raw_data_df: pd.DataFrame = pd.read_csv(csv_path)

def human_name_convention(invalid_name: str) -> str:
    valid_name = invalid_name.lower().title().strip() # Lowercase everything -> capitalize all first letters -> remove leading/trailing spaces
    valid_name = ' '.join(valid_name.split()) # For extra spaces in the middle of a sentence.
    return valid_name

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the raw data.
    :param df: DataFrame containing raw data.
    :return: Cleaned DataFrame.
    """
    print(df.shape[0])
    df = df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"))
    df['date_of_admission'] = pd.to_datetime(df['date_of_admission'])
    df['discharge_date'] = pd.to_datetime(df['discharge_date'])
    df['name'] = df['name'].apply(human_name_convention)

    return df

df = clean_data(raw_data_df)
print(df)