import pyodbc
import pandas as pd
from sqlalchemy import create_engine
import urllib
from etlcon import *

try:
    # Connect to the local SQL Server (SSMS)
    con = pyodbc.connect("Driver={SQL Server};" "Server=D191T8LHYL309RA\MSQL2019;" "PORT=23001;" "Database=Airport_survey;" "Trusted_Connection=yes;")
    sql = """
        SELECT *
        FROM [Airport_survey].[dbo].[airline_passenger_satisfaction$] 
    """
    df = pd.read_sql(sql, con)

    print(df)

except Exception as e:
    print("Error connecting to SSMS: ", str(e))

try:
    # Connect to Azure SQL Database using a connection string
    

    connection_string = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"Server=tcp:{server_name},1433;"
        f"Database={database_name};"
        f"Uid={username};"
        f"Pwd={password};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
        f"Connection Timeout=30;"
    )

    # URL encode the connection string (encode it as bytes)
    quoted_conn_str = urllib.parse.quote_plus(connection_string)

    # Create the SQLAlchemy engine for Azure SQL Database
    azure_engine = create_engine(f"mssql+pyodbc:///?odbc_connect={quoted_conn_str}")

    # Export data to Azure SQL Database
    df.to_sql('airline_passenger_satisfaction', azure_engine, if_exists='append', index=False)
    print("Successfully exported from SSMS to Azure SQL DB")

except Exception as e:
    print("Error exporting to Azure SQL DB: ", str(e))
