# Import the pandas and openpyxl modules
import pandas as pd
import openpyxl

# Read the excel file into a pandas dataframe
df = pd.read_excel("train.xlsx")

# Specify the column name that needs escaping
column_name = "prompt"

# Loop through the data and escape the double quotes in the column
for i, row in df.iterrows():
  if row[column_name]:
    row[column_name] = row[column_name].replace('"', '\\"')

# Convert the data to a jsonl string
jsonl = df.to_json(orient="records", lines=True)

# Write the jsonl string to a file
with open("train.jsonl", "w") as f:
  f.write(jsonl)

# Read the excel file into a pandas dataframe
df = pd.read_excel("test.xlsx")

# Specify the column name that needs escaping
column_name = "prompt"

# Loop through the data and escape the double quotes in the column
for i, row in df.iterrows():
  if row[column_name]:
    row[column_name] = row[column_name].replace('"', '\\"')

# Convert the data to a jsonl string
jsonl = df.to_json(orient="records", lines=True)

# Write the jsonl string to a file
with open("test.jsonl", "w") as f:
  f.write(jsonl)