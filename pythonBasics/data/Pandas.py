# pandas DataFrames are data structures that contain:
# - Data organized in two dimensions, rows and columns
# - Labels that correspond to the rows and columns
# You can start working with DataFrames by importing pandas:

import pandas as pd

# Loading a csv file using pandas
file_in = 'C:/Temp/looker_user_email.txt'

def read_users():
    df = pd.read_csv(file_in)
    print(df)

read_users()

# Data in a DataFrame are organized as in a table: Column label, Row labels and Data
# You can access a column in a pandas DataFrame the same way you would get a value from a dictionary:

def read_users2():
    df = pd.read_csv(file_in)
    email_address = df['email']
    print(email_address)

read_users2()
