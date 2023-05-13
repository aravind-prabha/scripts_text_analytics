# Import the libraries
import jsonlines
import json

# Open the original jsonl file
with jsonlines.open("jsonl_file_prepared_valid.jsonl") as reader:
    # Create two lists to store the prompts and completions
    prompts = []
    completions = []
    # Loop through each line in the file
    for line in reader:
        # Append the prompt and completion to the respective lists
        prompts.append(line["prompt"])
        completions.append(line["completion"])

# Open two new jsonl files for writing
with jsonlines.open("prompts.jsonl", mode="w") as writer1, jsonlines.open("completions.jsonl", mode="w") as writer2:
    # Loop through the prompts and completions lists
    for prompt, completion in zip(prompts, completions):
        # Write each prompt and completion as a json object with the specified key in the new files
        writer1.write({"prompt": prompt})
        writer2.write({"completion": completion})