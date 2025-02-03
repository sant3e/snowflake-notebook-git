from snowflake.snowpark.functions import col

# function that will be called by stored procedure's import parameter
def filter_by_column_value(session, table_name, column_value):
  df = session.table(table_name)
  return df.filter(col("COLUMN3") == column_value)
