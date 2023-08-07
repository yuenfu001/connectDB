import pypyodbc
import pandas as pd, os
from datetime import datetime

# # create connection
# # connection_parameter = ()


connect_str = "Driver={SQL Server};" "Server=D191T8LHYL309RA\MSQL2019;" "PORT=23001;" "Database = Airport_survey;" "Trusted_Connection=yes;"
connection = pypyodbc.connect(connect_str)

query = "SELECT * FROM [Airport_survey].[dbo].[airline_passenger_satisfaction$] WHERE Class = 'Business' AND [Customer Type]='First-time' AND [Departure Delay] > 6"

df = pd.read_sql_query(sql=query, con=connection)

print(df)
# print(pypyodbc.drivers())

