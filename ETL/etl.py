import pypyodbc as odbc, pandas as pd
from sqlalchemy import create_engine
import os


# extract data from MSQL server

try:
        sql_conn = odbc.connect("Driver={SQL Server};" "Server=D191T8LHYL309RA\MSQL2019;" "PORT=23001;" "Database = Airport_survey;" "Trusted_Connection=yes;")
        sql = """
            SELECT * 
            FROM [Airport_survey].[dbo].[airline_passenger_satisfaction$] 
            WHERE Class = 'Business' 
                AND [Customer Type]='First-time' 
                    AND [Departure Delay] > 6
            """
        df = pd.read_sql_query(sql,sql_conn)
        print(df)
except Exception as error:
        print("Data extract error: ", str(error))

# extract()
#load data to PostgreSQL
try:
        engine = create_engine('postgresql://postgres:5773@localhost:5432/airport_survey')
        # save to postgres
        df.to_sql('fromsqlserver', engine, if_exists='replace', index=False)
        print('Successfully loaded')
    
except Exception as e:
        print("data load error: " + str(e))
