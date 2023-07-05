import openpyxl

# Load the workbook and select the worksheet
wb = openpyxl.load_workbook('LLM_Train_set.xlsx')
ws = wb.active

# Open the output file
with open('output.txt', 'w') as f:
    # Iterate over the rows in the worksheet
    for row in ws.iter_rows(values_only=True):
        # Get the values from columns A and B
        left_column = row[0]
        right_column = row[1]
        
        # Generate the output string
        output = '{{"prompt":"Classify this review into the following labels, there can be multiple labels per sentence, the labels are [\'Crowd\',\'aquarium\',\'Food\',\'Queue\',\'Experience\',\'Price\',\'dolphin show\',\'Parking\', \'Exhibits\',\'Staff\',\'Affordablity\',\'Ticket\',\'Animals\',\'Hygiene\',\'Security\',\'Entertainment\',\'Value\',\'Whale Sharks\',\'TSA\',\'Plane Train\'], the review is  : {}","completion":{}}}\n'.format(left_column, right_column)
        
        # Write the output string to the file
        f.write(output)
