from snowflake.snowpark.functions import col

def filter_by_column_value(sessions, table_name, column_value):
  df = session.table(table_name)
  return df.filter(col("COLUMN3") == column_value)
