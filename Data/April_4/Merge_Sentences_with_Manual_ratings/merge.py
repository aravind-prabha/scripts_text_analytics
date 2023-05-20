import pandas as pd

# List of input file names
input_files = [
    'Setences_Rating_1.csv',
    'Setences_Rating_2.csv',
    'Setences_Rating_3.csv',
    'Setences_Rating_4.csv',
    'Setences_Rating_5.csv'
]

# List of manual rating file names
manual_rating_files = [
    'manual_Rating_1.xlsx',
    'manual_Rating_2.xlsx',
    'manual_Rating_3.xlsx',
    'manual_Rating_4.xlsx',
    'manual_Rating_5.xlsx'
]

# Output file name for merged CSV
output_file = 'merged_file.csv'

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Iterate over the input files and merge them into the DataFrame
for i, file in enumerate(input_files):
    if i == len(input_files) - 1:
        df = pd.read_csv(file, encoding='utf-8', usecols=['industry', 'cleantext', 'rating'])
        df.rename(columns={'Setences': 'industry', 'Rating': 'rating', 'cleantext': 'comment'}, inplace=True)
        #df['rating'] = df['comment']  # Set the 'comment' column values to 'rating' column
    else:
        df = pd.read_csv(file, encoding='utf-8', usecols=['industry', 'review_comment', 'rating'])
        df.rename(columns={'industry': 'industry', 'rating': 'rating', 'review_comment': 'comment'}, inplace=True)
    merged_data = merged_data.append(df, ignore_index=True)

# Iterate over the manual rating files and update the 'manual_rating' column
start_index = 0
for i, manual_rating_file in enumerate(manual_rating_files):
    manual_ratings = pd.read_excel(manual_rating_file, usecols=['manual_rating'])['manual_rating']
    end_index = start_index + len(manual_ratings)
    merged_data.loc[start_index:end_index-1, 'manual_rating'] = manual_ratings.values
    start_index = end_index

# Save the merged DataFrame to a new CSV file with UTF-8 encoding
merged_data.to_csv(output_file, encoding='utf-8', index=False)

print("Merged CSV file saved as", output_file)
