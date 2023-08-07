from sql.connect import *
import psycopg2, pandas as pd, sqlalchemy as sa
engine = sa.create_engine('postgresql://postgres:5773@localhost:5432/chioma')
try:

    query = "SELECT * FROM public.africa_provider WHERE provider_name='Phone Bill 1'"

    df = pd.read_sql(query, engine)
    print(df)
except Exception as error:
    print(error)
