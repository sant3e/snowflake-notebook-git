from snowflake.snowpark.functions import col
import json

def filter_by_column_value(session, table_name, column_value):
    df = session.table(table_name)
    filtered_df = df.filter(col("COLUMN3") == column_value)
    return filtered_df.to_pandas().to_dict(orient='records')
