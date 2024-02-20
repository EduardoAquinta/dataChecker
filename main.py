import pandas as pd
import gcsfs
import google.auth
import yaml

# Global variable declarations
bucket_name = 'eduardo_data_hold'
file_name = 'data.csv'
credentials, project_id = google.auth.default(scopes=['https://www.googleapis.com/auth/devstorage.read_only'])


# Import the checklist
def get_checklist():
    with open("Data/correct_list.yaml", "r") as data:
        output = yaml.safe_load(data)
        return output["Checklist"]


# Import the data from GCS
def get_data():
    fs = gcsfs.GCSFileSystem(project='My First Project',
                             token=credentials)
    with fs.open(bucket_name + '/' + file_name) as f:
        output = pd.read_csv(f)
        return output


# Variables for the data Checker
df = get_data()
checklist = get_checklist()
list_of_column_names = list(df.columns)

print("list_of_column_names: ", list_of_column_names)
print("checklist: ", checklist)


# Check the data to see if the columns contain the correct headings
for element in checklist:
    if element not in list_of_column_names:
        print("\u274C " + element + " not found")
    else:
        print('\u2713 ' + element + " found")
