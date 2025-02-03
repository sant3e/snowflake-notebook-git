CREATE OR REPLACE PROCEDURE filter_by_column_value(tableName VARCHAR, column_value VARCHAR)
    LANGUAGE PYTHON
    RUNTIME_VERSION = '3.8'
    PACKAGES = ('snowflake-snowpark-python')
    IMPORTS = ('@demo.public.my_github_repo/branches/master/python-script/filter.py')
    HANDLER = 'filter.filter_by_column_value';
