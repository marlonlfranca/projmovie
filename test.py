import pandas as pd
import csv

df = pd.read_csv(
    'movies_metadata.csv',
    quotechar='"',
    low_memory=False)


# print(df.columns)
print(df.dtypes)