import pandas as pd


file_in = 'C:/Temp/ls_log.csv'

# Read a csv file
df = pd.read_csv(file_in, sep=',')
print(df.shape)
print(df[['Asset name']].value_counts())



