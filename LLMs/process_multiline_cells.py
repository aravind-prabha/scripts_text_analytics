# Import the openpyxl module
import openpyxl

# Load the excel file
wb = openpyxl.load_workbook("Prompt_sheet.xlsx")

# Get the sheet by name
ws = wb["Sheet1"]

# Loop through the cells in the column
for cell in ws["A"]:
    # Check if the cell value is a string
    if isinstance(cell.value, str):
        # Replace the newline characters with spaces
        cell.value = cell.value.replace("\n", " ")

# Save the modified file
wb.save("updated_prompt_Sheet.xlsx")