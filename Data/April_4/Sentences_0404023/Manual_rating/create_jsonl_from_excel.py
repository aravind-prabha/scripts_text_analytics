# Import the pandas module
import pandas as pd
import json

# Read the excel file and specify the column names
df = pd.read_excel("raw_reviews_1.xlsx", usecols=["prompt", "rating"])

# Create an empty list to store the json objects
json_list = []

# Loop through the rows of the dataframe
for i, row in df.iterrows():
  # Get the values from the left and right columns
  left_value = row["prompt"]
  right_value = row["rating"]
  # Create a json object with the prompt and completion keys
  json_object = {
    "prompt": f"Rate this review on a scale from 1 to 5. Output only the integer rating : {left_value}",
    "completion": str(right_value)
  }
  # Append the object to the list
  json_list.append(json_object)

# Convert the list to a json string
json_string = json.dumps(json_list)
# Write the list to a jsonl file
with open("jsonl_file.jsonl", "w") as f:
  for obj in json_list:
    # Write each object as a line in the file
    f.write(json.dumps(obj) + "\n")