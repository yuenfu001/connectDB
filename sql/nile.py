import pypyodbc as odbc, pandas as pd
from connects import *

server = servername2
database = db1
user = username1
pwd = password
con = odbc.connect("Driver={ODBC Driver 18 for SQL Server};" f"Server={server};Database={database};Uid={user};Pwd={pwd};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
# print(odbc.drivers())

sql = """
            SELECT TOP 100 *
                FROM nunapplicant
"""
df = pd.read_sql_query(sql, con)
print(df.head(20))
