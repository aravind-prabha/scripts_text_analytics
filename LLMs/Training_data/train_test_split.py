# Import the pandas and sklearn modules
import pandas as pd
from sklearn.model_selection import train_test_split

# Read the excel file into a pandas dataframe
df = pd.read_excel("GT.xlsx")

# Split the dataframe into train and test subsets
train, test = train_test_split(df, test_size=0.2, random_state=42)

# Save the subsets as excel files
train.to_excel("train.xlsx", index=False)
test.to_excel("test.xlsx", index=False)