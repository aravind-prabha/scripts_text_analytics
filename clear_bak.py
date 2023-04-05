# Import os module
import os

# Define a function to delete files with a given extension
def delete_files(extension, path):
  # Loop through all files and directories in the given path
  for root, dirs, files in os.walk(path):
    # Loop through all files in the current directory
    for file in files:
      # Check if the file has the given extension
      if file.endswith(extension):
        # Get the full path of the file
        file_path = os.path.join(root, file)
        # Delete the file
        os.remove(file_path)
        # Print a message
        print(f"Deleted {file_path}")

# Call the function with ".bak" extension and current directory as arguments
delete_files(".bak", ".")