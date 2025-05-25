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

def human_name_convention(invalid_name: str) -> str:
    valid_name = invalid_name.lower().title().strip() # Lowercase everything -> capitalize all first letters -> remove leading/trailing spaces
    valid_name = ' '.join(valid_name.split()) # For extra spaces in the middle of a sentence.
    return valid_name

def clean_data(df: pd.DataFrame) -> tuple[pd.DataFrame, str]:
    """
    Clean the raw data.
    :param df: DataFrame containing raw data.
    :return: Cleaned DataFrame.
    """
    df = df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"))
    df = df.rename(columns={'name': 'patient_name', 'age': 'patient_age'})

    df['date_of_admission'] = pd.to_datetime(df['date_of_admission'])
    df['discharge_date'] = pd.to_datetime(df['discharge_date'])
    df['patient_name'] = df['patient_name'].apply(human_name_convention)

    def _get_max_length(col: pd.Series) -> str:
        return str(col.astype(str).str.len().max())

    column_info = {}
    for col in df.columns:
        if df[col].dtype == 'object':
            column_data_type = f"VARCHAR ({_get_max_length(df[col])})"
        if df[col].dtype == 'float64':
            column_data_type = "NUMERIC (12, 0)"
        if df[col].dtype == 'int64':
            column_data_type = "INTEGER"
        if df[col].dtype == '<M8[ns]' or df[col].dtype == 'datetime64[ns]':
            column_data_type = "DATETIME"
        column_info[col] = column_data_type
    
    table_ddl = f"CREATE TABLE healthcare_data ({', '.join([f'{col} {dtype}' for col, dtype in column_info.items()])});"

    return df, table_ddl

column_descriptions = {
    "patient_name": "The patient''s full name",
    "patient_age": "The patient''s age",
    "gender": "The patient''s gender.",
    "blood_type": "The patient''s blood type.",
    "medical_condition": "The patient''s medical condition.",
    "date_of_admission": "The date the patient was admitted to the hospital.",
    "doctor": "The name of the doctor in charge of the patient.",
    "hospital": "The name of the hospital.",
    "insurance_provider": "The name of the insurance provider.",
    "billing_amount": "The total billing amount.",
    "room_number": "The room number assigned to the patient.",
    "admission_type": "The type of admission (e.g., emergency, elective).",
    "discharge_date": "The date the patient was discharged from the hospital.",
    "medication": "The medication prescribed to the patient.",
    "test_results": "The results of any tests conducted on the patient.",
}
sql_table_description_template = """
EXEC sys.sp_addextendedproperty 
    @name=N'TableDescription', 
    @value=N'{0}',
    @level0type=N'SCHEMA',
    @level0name=N'{1}', 
    @level1type=N'TABLE',
    @level1name=N'{2}';
"""
sql_source_description_template = """
EXEC sys.sp_addextendedproperty 
    @name=N'SourceDescription', 
    @value=N'{0}',
    @level0type=N'SCHEMA',
    @level0name=N'{1}',
    @level1type=N'TABLE',
    @level1name=N'{2}';
"""
sql_column_description_template = """
EXECUTE sp_addextendedproperty
    @name = 'MS_Description', 
    @value = '{0}', 
    @level0type = 'SCHEMA', 
    @level0name = N'{1}', 
    @level1type = N'TABLE',
    @level1name = N'{2}',
    @level2type = N'COLUMN', 
    @level2name = N'{3}';
"""

def sql_description_generator(column_descriptions: dict, table_schema: str, table_name: str, **kwargs) -> str:
    """
    Genberate SQL description for each column in the table.
    :param column_descriptions: Dictionary containing column names and their descriptions.
    :param table_schema: The schema of the table.
    :param table_name: The name of the table.
    :return: SQL description string.
    """
    sql_table_description, sql_source_description = ""
    if kwargs.get("table_description") != None:
        table_description = kwargs.get("table_description")
        sql_table_description = sql_table_description_template.format(
            table_description,
            table_schema,
            table_name
        )
    if kwargs.get("table_source") != None:
        table_source = kwargs.get("table_source")
        sql_source_description = sql_source_description_template.format(
            table_source,
            table_schema,
            table_name
        )
    sql_descriptions = sql_table_description + sql_source_description    
    for column_name, description in column_descriptions.items():
        sql_descriptions = sql_descriptions + sql_column_description_template.format(
            description,
            table_schema,
            table_name,
            column_name
        )
    with open(os.path.join(script_dir, "table_description.sql"), "w") as f:
        f.write(sql_descriptions)
        print("SQL table description generated and saved to table_description.sql")
    return sql_descriptions

def sql_insert_statement_gen(df: pd.DataFrame, schema: str, table_name: str) -> str:
    """
    Generate SQL insert statement for each row in the DataFrame.
    :param df: DataFrame containing the data to be inserted.
    :param table_name: The name of the table.
    :return: SQL insert statement string.
    """
    sql_insert_statements = []
    for index, row in df.iterrows():
        values = ', '.join([f"'{str(value)}'" for value in row.values])
        sql_insert_statements.append(f"INSERT INTO {schema}.{table_name} VALUES ({values});")

    text = '\n'.join(sql_insert_statements)
    with open(os.path.join(script_dir, "insert_statements.sql"), "w") as f:
        f.write(text)
        print("SQL insert statements generated and saved to insert_statements.sql")

# csv_path = os.path.join(script_dir, "raw_healthcare_dataset.csv")
# raw_data_df: pd.DataFrame = pd.read_csv(csv_path)
# df, table_ddl = clean_data(raw_data_df)
# df.to_csv(os.path.join(script_dir, "cleaned_healthcare_dataset.csv"), index=False)

# sql_description_generator(
#     column_descriptions = column_descriptions,
#     table_schema        = "dash_data",
#     table_name          = "healthcare_data",
#     table_source        = "Source: Healthcare data from somewhere important enough.",
#     table_description   = "Healthcare data for patients"
# )

csv_path = os.path.join(script_dir, "cleaned_healthcare_dataset.csv")
raw_data_df: pd.DataFrame = pd.read_csv(csv_path)

# sql_insert_statement_gen(raw_data_df, "dash_data", "healthcare_data")