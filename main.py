import pandas as pd

df = pd.read_csv('Data/data.csv')

list_of_column_names = list(df.columns)

print("list_of_column_names: ", list_of_column_names)

if 'index' in list_of_column_names:
    print("index is in")
else:
    print("index is missing")
