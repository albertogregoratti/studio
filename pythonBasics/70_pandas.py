import pandas as pd

#################################################
# Working with a .csv file
#################################################
filepath = "C:/Users/alberto.gregoratti/Downloads/Springer Nature JIRA 2022_01_04.csv"
df = pd.read_csv(filepath)

# provides nb of rows and columns
print('Using df.shape to get number of rows and columns of the file:')
df.shape
# provides more details
print('Using df.info to get some more details about the file:')
df.info()
# display a sample with the first 5 rows
print('Using df.head to display the first rows of the file:')
df.head(5)
# display the last 10 rows
print('Using df.shape to display the last rows of the file:')
df.tail(10)
# accessing a column (it returns a Series)
print('Using df[column name] to access a column:')
df['Assignee']
# OR
df.Assignee
# accessing multiple columns (it returns a DataFrame)
print('Using df[column name] to access multiple columns:')
df[['Assignee', 'Reporter']]
# to get all column names
print('Using df.columns to get all columns:')
df.columns
# to get a row using iloc (integer location): it returns the column names and the value for that row
df.iloc[0]
# to get a subset of rows: it returns a DataFrame
df.iloc[[0, 1]]
# to get a row using loc (by label = index)
df.loc[0]
# to get a subset of rows for a specific list of colums only
df.loc[[0, 1], ['Assignee', 'Reporter']]
df.loc[0:2, ['Assignee', 'Reporter']]