# Import the pandas and openpyxl modules
import pandas as pd
import openpyxl

# Load the excel file
wb = openpyxl.load_workbook("raw_reviews.xlsx")

# Get the sheet by name
ws = wb["prompt"]

# Loop through the cells in the column
for cell in ws["A"]:
    # Check if the cell value is a string
    if isinstance(cell.value, str):
        # Replace the newline characters with spaces
        cell.value = cell.value.replace("\n", " ")
        # Replace the double quotes with escaped double quotes
        cell.value = cell.value.replace('"', '\"')

# Save the modified file
wb.save("raw_reviews_1.xlsx")

# Read the excel file into a pandas dataframe
df = pd.read_excel("raw_reviews_1.xlsx")

# Specify the column name that needs escaping
column_name = "prompt"

# Convert the data to a jsonl string
jsonl = df.to_json(orient="records", lines=True)

# Write the jsonl string to a file
with open("raw_reviews.jsonl", "w") as f:
  f.write(jsonl)