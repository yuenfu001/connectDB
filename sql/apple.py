import pandas as pd, numpy as np

url = 'https://api.appstoreconnect.apple.com/v1/salesReports'
df = pd.read_csv(url)
print(df.head(10))