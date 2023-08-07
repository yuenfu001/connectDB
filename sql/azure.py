import pypyodbc as odbc, pandas as pd
from azure_con import *

server = Server
database = Database
user = Uid
pwd = Pwd
con = odbc.connect("Driver={ODBC Driver 18 for SQL Server};" f"Server={server};Database={database};Uid={user};Pwd={pwd};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
# print(odbc.drivers())

sql = """
            SELECT TOP 100 *
                FROM [dbo].[airline_passenger_satisfaction]
"""
df = pd.read_sql_query(sql, con)
print(df.head(20))


# print(odbc.drivers())  




