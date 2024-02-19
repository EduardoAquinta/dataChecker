import pandas as pd
import gcsfs
import google.auth

bucket_name = 'eduardo_data_hold'

access_token = open('access_token.txt', 'r').read()

credentials, project_id = google.auth.default(scopes=['https://www.googleapis.com/auth/devstorage.read_only'])

fs = gcsfs.GCSFileSystem(project='My First Project',
                         token=credentials)
with fs.open(bucket_name + '/data.csv') as f:
    df = pd.read_csv(f)

checklist = open('Data/correct_list.txt', 'r').read()

list_of_column_names = list(df.columns)

print("list_of_column_names: ", list_of_column_names)
print("checklist: ", checklist)


