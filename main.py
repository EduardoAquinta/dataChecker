import pandas as pd

df = pd.read_csv('data.csv')

list_of_column_names = list(df.columns)

print("list_of_column_names: ", list_of_column_names)